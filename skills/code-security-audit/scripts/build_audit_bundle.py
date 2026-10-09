"""Build an audit deliverable from real, reviewed records. Python 3.10+, stdlib only."""
import argparse
import csv
from datetime import datetime
import hashlib
import html
import io
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import zipfile


class AuditError(ValueError):
    pass


def need(condition, message):
    if not condition:
        raise AuditError(message)


def linklike(path):
    """Also reject Windows junctions/reparse points, not just POSIX symlinks."""
    if path.is_symlink():
        return True
    try:
        return bool(getattr(path.lstat(), 'st_file_attributes', 0) & 0x400)
    except FileNotFoundError:
        return False


def text_fields(obj, fields, where):
    need(isinstance(obj, dict), f"{where}: object required")
    for field in fields:
        need(isinstance(obj.get(field), str) and obj[field].strip(), f"{where}.{field}: nonempty string required")


def timestamp(value):
    try:
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except (ValueError, TypeError):
        raise AuditError('Execution time must be ISO 8601 with timezone') from None
    need(parsed.tzinfo is not None, 'Execution time must include timezone')
    return parsed


def list_field(obj, key, where):
    need(isinstance(obj.get(key), list), f"{where}.{key}: array required")
    return obj[key]


def source_file(root, value):
    need(isinstance(value, str) and value, "File path required")
    p = Path(value)
    need(not p.is_absolute() and not p.drive and '..' not in p.parts, "Only contained relative paths allowed")
    candidate = root / p
    for item in [candidate, *candidate.parents]:
        if item == root:
            break
        need(not linklike(item), "Symlink/junction source not allowed")
    resolved = candidate.resolve()
    need(resolved.is_relative_to(root) and resolved.is_file(), "Source must be a regular file within input root")
    return resolved


def secret_check(data, label, forbidden):
    value = data.decode('utf-8', errors='replace')
    patterns = [
        r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----\s+[A-Za-z0-9+/=\r\n]{24,}',
        r'\bBearer\s+[A-Za-z0-9._~-]{24,}',
        r'\b(?:ghp_|github_pat_|AKIA)[A-Za-z0-9_]{16,}',
        r'(?:https?|postgres(?:ql)?|redis(?:s)?|mysql)://[^\s/:@]+:[^\s/@]+@',
    ]
    need(not any(re.search(p, value) for p in patterns), f"Secret pattern detected in {label}; remove/redact before packaging")
    assignments = re.finditer(r'''(?i)["']?(?:password|api[_-]?key|client[_-]?secret|access[_-]?token)["']?\s*[:=]\s*["']([^"'\r\n]+)["']''', value)
    for match in assignments:
        sample = match.group(1)
        allowed = re.search(r'(?i)redacted|synthetic|placeholder|example|dummy|\$\{|\$\(|<[^>]+>', sample)
        need(bool(allowed), f"Possible credential assignment in {label}; manually redact")
    need(not any(v in value for v in forbidden), f"Forbidden sensitive value found in {label}")


def validate(d, root):
    need(isinstance(d, dict) and d.get('schema_version') == 1, "schema_version must be 1")
    need(d.get('redaction_reviewed') is True, "Manual redaction_reviewed=true required")
    text_fields(d.get('project'), ['name', 'repository', 'commit'], 'project')
    need(isinstance(d['project'].get('dirty'), bool), "project.dirty must be boolean")
    text_fields(d.get('audit'), ['date', 'timezone', 'auditor'], 'audit')
    for k in ['scope', 'excluded', 'authorized_actions', 'baseline_changes']:
        list_field(d['audit'], k, 'audit')
    text_fields(d, ['executive_summary'], 'audit record')
    for k in ['methods', 'coverage', 'limitations', 'findings', 'verified_controls', 'test_runs', 'remediation_plan', 'next_steps', 'references', 'evidence', 'scripts']:
        list_field(d, k, 'record')
    need(bool(d['coverage']), "Explicit coverage required")
    for item in d['coverage']:
        text_fields(item, ['area', 'status', 'details'], 'coverage')
        need(item['status'] in ['complete', 'partial', 'not_tested', 'blocked'], "Invalid coverage status")
    files, evidence_ids, script_ids, destinations = [], set(), set(), set()
    for category, ids in [('evidence', evidence_ids), ('scripts', script_ids)]:
        for item in d[category]:
            text_fields(item, ['id', 'file', 'description'], category)
            need(bool(re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]{0,63}', item['id'])), "Invalid evidence/script ID")
            need(item['id'] not in ids, "Duplicate evidence/script ID")
            ids.add(item['id'])
            src = source_file(root, item['file'])
            folder = 'evidence' if category == 'evidence' else 'reproduce'
            relative = Path(item['file'])
            if relative.parts[0] == folder:
                relative = Path(*relative.parts[1:])
            dest = folder + '/' + relative.as_posix()
            need(dest.casefold() not in destinations, 'Duplicate bundle destination')
            destinations.add(dest.casefold())
            if category == 'scripts':
                text_fields(item, ['command', 'safety_scope', 'side_effects', 'stop_conditions'], 'script')
                need('{script}' in item['command'], "Script command must contain {script} placeholder")
                item['command'] = item['command'].replace('{script}', dest)
                list_field(item, 'dependencies', 'script')
                list_field(item, 'environment_variables', 'script')
                need(src.suffix.lower() in ['.py', '.js', '.cjs', '.mjs', '.ts', '.ps1', '.sh', '.sql'], "Reproduction must be a script file")
            files.append((src, dest))
            item['bundle_file'] = dest
    def refs(item, key='evidence_ids', allowed=None, required=True):
        values = list_field(item, key, 'reference')
        if required:
            need(bool(values), "Evidence/script reference cannot be empty")
        need(all(v in (allowed if allowed is not None else evidence_ids) for v in values), "Unknown evidence/script reference")
    findings_ids = set()
    for f in d['findings']:
        text_fields(f, ['id', 'title', 'severity', 'classification', 'root_cause', 'impact', 'recommendation', 'status'], 'finding')
        need(bool(re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]{0,63}', f['id'])) and f['id'] not in findings_ids, "Invalid/duplicate finding ID")
        findings_ids.add(f['id'])
        need(f['severity'] in ['critical', 'high', 'medium', 'low', 'info'], "Invalid severity")
        need(f['classification'] in ['confirmed', 'dependency', 'configuration', 'conditional', 'unverified'], "Invalid classification")
        need(f['status'] in ['open', 'mitigated', 'closed', 'unverified'], "Invalid finding status")
        details = f.get('detailed_description')
        text_fields(details, ['explain', 'chain', 'scenario', 'limits'], 'detailed_description')
        steps = list_field(details, 'steps', 'detailed_description')
        need(bool(steps) and all(isinstance(x, str) and x.strip() for x in steps), 'Concrete reproduction steps required')
        excerpts = list_field(f, 'key_evidence', 'finding')
        need(bool(excerpts), 'Key evidence excerpts required')
        for excerpt in excerpts:
            text_fields(excerpt, ['file', 'excerpt', 'evidence_id'], 'key evidence')
            need(excerpt['evidence_id'] in evidence_ids, 'Unknown key evidence reference')
            need(type(excerpt.get('start')) is int and excerpt['start'] > 0, 'Evidence start line required')
            need(type(excerpt.get('end')) is int and excerpt['end'] >= excerpt['start'], 'Evidence end line required')
        list_field(f, 'locations', 'finding')
        list_field(f, 'preconditions', 'finding')
        refs(f)
        refs(f, 'script_ids', script_ids)
        for phase in ['initial', 'retest']:
            run = f.get(phase)
            text_fields(run, ['at', 'method', 'expected', 'observed', 'outcome'], phase)
            timestamp(run['at'])
            need(run['outcome'] in ['present', 'absent', 'blocked', 'inconclusive'], "Invalid verification outcome")
            refs(run, required=run['outcome'] != 'blocked')
            if run['outcome'] == 'blocked':
                text_fields(run, ['reason'], phase)
        kind = f['retest'].get('kind')
        need(kind in ['repeat', 'after_fix', 'configuration_recheck', 'blocked'], "Retest kind required")
        need((kind == 'blocked') == (f['retest']['outcome'] == 'blocked'), "Blocked retest must be explicit")
        if kind != 'blocked':
            need(timestamp(f['initial']['at']) < timestamp(f['retest']['at']), "Retest must occur after initial execution")
        if f['classification'] == 'confirmed':
            need(f['initial']['outcome'] == 'present', 'Confirmed finding requires initial present outcome')
        if f['status'] == 'closed':
            need(f['initial']['outcome'] == 'present' and kind == 'after_fix' and f['retest']['outcome'] == 'absent', "Closed requires initial present, after_fix and absent outcome")
    for control in d['verified_controls']:
        text_fields(control, ['control', 'initial', 'retest'], 'verified control')
        refs(control)
    for t in d['test_runs']:
        text_fields(t, ['group', 'round', 'at', 'command'], 'test run')
        timestamp(t['at'])
        need(t['round'] in ['initial', 'retest', 'after_fix'], "Invalid test round")
        for k in ['total', 'passed', 'failed', 'skipped']:
            need(type(t.get(k)) is int and t[k] >= 0, "Test counts must be nonnegative integers")
        need(t['passed'] + t['failed'] + t['skipped'] == t['total'], "Test counts do not sum to total")
        refs(t)
    for r in d['remediation_plan']:
        text_fields(r, ['priority', 'action', 'owner', 'acceptance'], 'remediation')
    for r in d['references']:
        text_fields(r, ['title', 'url'], 'reference')
        need(r['url'].startswith(('https://', 'http://')), "Reference URL must be http(s)")
    for service in d.get('services', []):
        text_fields(service, ['name', 'entry_points', 'trust_boundaries', 'analysis'], 'service')
        refs(service)
        need(all(x in findings_ids for x in list_field(service, 'finding_ids', 'service')), 'Unknown service finding')
    for item in d.get('historical_review', []):
        text_fields(item, ['title', 'previous', 'current', 'limits'], 'historical review')
        refs(item)
    return files


def table(headers, rows):
    def cell(x):
        return str(x).replace('|', '\\|').replace('\n', ' / ')
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] + ['| ' + ' | '.join(cell(x) for x in row) + ' |' for row in rows])


def report(d):
    a, p = d['audit'], d['project']
    evidence = {x['id']: x for x in d['evidence']}
    scripts = {x['id']: x for x in d['scripts']}
    def refs(ids):
        return ', '.join('[' + x + '](' + evidence[x]['bundle_file'] + ')' for x in ids)
    def fence(value, language='text'):
        marker = '`' * max(3, max((len(x) + 1 for x in re.findall(r'`+', value)), default=3))
        return marker + language + '\n' + value + '\n' + marker
    blocked = [f['id'] for f in d['findings'] if f['retest']['outcome'] == 'blocked']
    blocks = [f"# {p['name']} 安全审计详细报告", f"日期：{a['date']}；时区：{a['timezone']}；审计者：{a['auditor']}",
        f"仓库：{p['repository']}；Commit：{p['commit']}；工作区变更：{p['dirty']}",
        '## 审计结论', d['executive_summary'], '结论限于实际验证的对象和条件；未发现问题不代表所有服务或线上环境安全。', f"问题条目：{len(d['findings'])}。未完成复测：{', '.join(blocked) or '无'}。",
        '## 风险汇总', table(['编号', '等级', '问题', '证据性质', '状态', '复测'], [(f['id'],f['severity'],f['title'],f['classification'],f['status'],f['retest']['kind']+'/'+f['retest']['outcome']) for f in d['findings']])]
    if d.get('services'):
        blocks += ['## 逐服务安全分析']
        for service in d['services']:
            blocks += ['### '+service['name'], '入口与职责：'+service['entry_points'], '身份与信任边界：'+service['trust_boundaries'], '安全设计分析：'+service['analysis'], '关联问题：'+', '.join(service['finding_ids']), '证据：'+refs(service['evidence_ids'])]
    blocks += ['## 漏洞详述']
    for f in d['findings']:
        detail=f['detailed_description']
        blocks += [f"### {f['id']} {f['title']}", f"等级：{f['severity']}；证据性质：{f['classification']}；状态：{f['status']}", '位置：'+'; '.join(f['locations']), '#### 漏洞说明', detail['explain'], '根因：'+f['root_cause'], '#### 数据流与漏洞链', detail['chain'], '#### 触发前提与影响', '; '.join(f['preconditions']), detail['scenario'], f['impact'], '#### 关键证据']
        for e in f['key_evidence']:
            blocks += [f"{e['file']}:{e['start']}–{e['end']}；证据：{refs([e['evidence_id']])}", fence(e['excerpt'])]
        blocks += ['#### 复现步骤', '\n'.join(str(i)+'. '+step for i,step in enumerate(detail['steps'],1))]
        for sid in f['script_ids']:
            script=scripts[sid]
            blocks += ['['+sid+']('+script['bundle_file']+')：'+script['description'], fence(script['command'], 'text'), '依赖：'+'; '.join(script['dependencies']), '环境变量：'+'; '.join(script['environment_variables']), '执行边界：'+script['safety_scope'], '副作用：'+script['side_effects'], '停止条件：'+script['stop_conditions']]
        for phase,title in [('initial','初测结果'),('retest','复测结果')]:
            run=f[phase]
            blocks += ['#### '+title, '\n'.join('- '+k+'：'+str(run[k]) for k in ['at','kind','method','expected','observed','outcome','reason'] if k in run), '实际执行证据：'+refs(run['evidence_ids'])]
        blocks += ['#### 验证边界', detail['limits'], '#### 修复建议与验收条件', f['recommendation']]
    blocks += ['## 已验证的保护措施', table(['控制','初测','复测','证据'], [(c['control'],c['initial'],c['retest'],refs(c['evidence_ids'])) for c in d['verified_controls']]), '## 验证限制', '\n'.join('- '+str(x) for x in d['limitations']) or '无额外记录。', '## 证据索引', table(['编号','文件','说明'], [(e['id'],'['+e['bundle_file']+']('+e['bundle_file']+')',e['description']) for e in d['evidence']]), '## 参考依据', '\n'.join('- ['+r['title']+']('+r['url']+')' for r in d['references']), '## 复现包与完整性', '从解包根目录执行上述命令。SHA256SUMS.txt 覆盖报告、记录、问题表、证据和脚本。打包器不执行探针。']
    return '\n\n'.join(blocks)+'\n'


def inline(value):
    # Never interpret raw HTML or executable URL schemes from audit input.
    parts=[]; offset=0
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)|`([^`]+)`', value):
        parts.append(html.escape(value[offset:match.start()]))
        if match[3] is not None:
            parts.append('<code>'+html.escape(match[3])+'</code>')
        else:
            target=match[2]
            safe=target.startswith(('https://','http://','#')) or (not re.search(r'[:\\\s]',target) and not target.startswith(('/', '//')) and '..' not in target.split('/'))
            parts.append('<a href="'+html.escape(target,quote=True)+'">'+html.escape(match[1])+'</a>' if safe else html.escape(match[0]))
        offset=match.end()
    parts.append(html.escape(value[offset:]))
    return ''.join(parts)


def render(md):
    lines=md.splitlines();parts=[];nav=[];i=0
    while i<len(lines):
        l=lines[i]
        if not l.strip():i+=1;continue
        if re.match(r'^`{3,}',l):
            marker=re.match(r'^`{3,}',l)[0];language=l[len(marker):];i+=1;code=[]
            while i<len(lines) and lines[i] != marker:code.append(lines[i]);i+=1
            parts.append('<pre><code data-language="'+html.escape(language)+'">'+html.escape('\n'.join(code))+'</code></pre>');i+=1;continue
        h=re.match(r'^(#{1,4}) (.*)',l)
        if h:
            level=len(h[1]);title=h[2];anchor='section-'+str(i)
            parts.append(f'<h{level} id="{anchor}">'+inline(title)+f'</h{level}>')
            if level==2:nav.append('<a href="#'+anchor+'">'+html.escape(title)+'</a>')
            i+=1;continue
        if l.startswith('| '):
            rows=[]
            while i<len(lines) and lines[i].startswith('| '):rows.append(lines[i]);i+=1
            cell=lambda r:[inline(c.strip().replace('\\|','|')) for c in re.split(r'(?<!\\)\|',r)[1:-1]]
            parts.append('<div class="table"><table><thead><tr>'+''.join('<th>'+c+'</th>' for c in cell(rows[0]))+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+c+'</td>' for c in cell(r))+'</tr>' for r in rows[2:])+'</tbody></table></div>');continue
        if l.startswith('- '):
            rows=[]
            while i<len(lines) and lines[i].startswith('- '):rows.append('<li>'+inline(lines[i][2:])+'</li>');i+=1
            parts.append('<ul>'+''.join(rows)+'</ul>');continue
        if re.match(r'^\d+\. ',l):
            rows=[]
            while i<len(lines) and re.match(r'^\d+\. ',lines[i]):rows.append('<li>'+inline(re.sub(r'^\d+\. ','',lines[i]))+'</li>');i+=1
            parts.append('<ol>'+''.join(rows)+'</ol>');continue
        parts.append('<p>'+inline(l)+'</p>');i+=1
    return '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>代码安全审计详细报告</title><style>body{font:16px/1.75 Segoe UI,Microsoft YaHei,sans-serif;margin:0;color:#1e293b;background:#f4f6f8}main{max-width:1180px;margin:auto;padding:36px;background:white}h1,h2{color:#17456b}h2{border-top:1px solid #d6dee5;padding-top:28px;margin-top:42px;scroll-margin-top:16px}h3{margin-top:28px}a{color:#1263a0;overflow-wrap:anywhere}nav{padding:20px;background:#eaf1f6;columns:2}nav a{display:block}pre{padding:16px;border:1px solid #d6dee5;border-radius:6px;background:#f6f8fa;overflow:auto;font:13px/1.6 Consolas,monospace}code{font-family:Consolas,monospace;overflow-wrap:anywhere}table{width:100%;border-collapse:collapse;font-size:13px}td,th{border:1px solid #d6dee5;padding:10px;vertical-align:top;text-align:left}th{background:#eaf1f6}td{overflow-wrap:anywhere}.table{overflow:auto}p{overflow-wrap:anywhere}@media print{body{background:white}main{padding:0}nav{display:none}pre{white-space:pre-wrap}tr{break-inside:avoid}}</style></head><body><main><nav>'+''.join(nav)+'</nav>'+''.join(parts)+'</main></body></html>'

def build(input_path, output_path, overwrite=False):
    raw_output = Path(output_path).absolute()
    need(not any(linklike(p) for p in [raw_output, *raw_output.parents]), 'Output path must not traverse symlinks/junctions')
    input_path = Path(input_path).resolve()
    root, output = input_path.parent, Path(output_path).resolve()
    need(not output.is_relative_to(root) and not root.is_relative_to(output), "Input and output directories must be separate, non-nested")
    need(not output.exists() or output.is_dir(), "Output must be a directory")
    need(overwrite or not output.exists() or not any(output.iterdir()), "Nonempty output: choose new path or explicit --overwrite")
    d = json.loads(input_path.read_text(encoding='utf-8-sig'))
    files = validate(d, root)
    forbidden = json.loads(os.environ.get('SECURITY_AUDIT_FORBIDDEN_VALUES', '[]'))
    need(isinstance(forbidden, list) and all(isinstance(v, str) and len(v) >= 8 for v in forbidden), "Forbidden values must be a JSON array of strings at least 8 characters")
    payloads = {dst: src.read_bytes() for src, dst in files}
    md = report(d)
    payloads.update({'report.md': md.encode(), 'report.html': render(md).encode(), 'audit.json': json.dumps(d, ensure_ascii=False, indent=2).encode()})
    stream = io.StringIO(newline='')
    writer = csv.writer(stream)
    writer.writerow(['编号', '等级', '问题', '证据性质', '状态', '初测', '复测类型', '复测结果'])
    def safe_cell(v):
        s = str(v)
        return "'" + s if s.lstrip().startswith(('=', '+', '-', '@')) else s
    for f in d['findings']:
        writer.writerow([safe_cell(v) for v in [f['id'], f['severity'], f['title'], f['classification'], f['status'], f['initial']['outcome'], f['retest']['kind'], f['retest']['outcome']]])
    payloads['findings.csv'] = ('\ufeff' + stream.getvalue()).encode()
    for name, data in payloads.items():
        secret_check(data, name, forbidden)
    payloads['SHA256SUMS.txt'] = ('\n'.join(hashlib.sha256(data).hexdigest() + '  ' + name for name, data in sorted(payloads.items())) + '\n').encode()
    # Validate everything before creating delivery files. Never recursively delete an existing output.
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='audit-package-', dir=output.parent) as temp:
        staging = Path(temp)
        for name, data in payloads.items():
            target = staging / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        with zipfile.ZipFile(staging / 'audit-bundle.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
            for name in sorted(payloads):
                archive.writestr(name, payloads[name])
        with zipfile.ZipFile(staging / 'audit-bundle.zip') as archive:
            need(archive.testzip() is None, "ZIP integrity failure")
        output.mkdir(parents=True, exist_ok=True)
        for name in [*payloads, 'audit-bundle.zip']:
            target = output / name
            need(not linklike(target), "Output symlink/junction not allowed")
            for parent in target.parents:
                if parent == output:
                    break
                need(not linklike(parent), "Output ancestor symlink/junction not allowed")
            target.parent.mkdir(parents=True, exist_ok=True)
            (staging / name).replace(target)
    return {'findings': len(d['findings']), 'blocked_retests': sum(f['retest']['outcome'] == 'blocked' for f in d['findings']), 'files': len(payloads), 'output': str(output)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.input, args.output, args.overwrite), ensure_ascii=False))
    except (AuditError, OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        # Avoid printing input contents or secret values from parsing exceptions.
        print('Packaging failed: ' + (str(error) if isinstance(error, AuditError) else type(error).__name__), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
