"""Offline behavioral tests; temporary fixtures under current working directory."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('builder', Path(__file__).with_name('build_audit_bundle.py'))
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def fixture():
    run = {'at': '2026-10-09T10:00:00+08:00', 'method': 'Local synthetic probe', 'expected': 'Reject', 'observed': 'Accepted', 'outcome': 'present', 'evidence_ids': ['E01']}
    retest = {**run, 'at': '2026-10-09T10:01:00+08:00', 'kind': 'repeat', 'evidence_ids': ['E02']}
    return {
        'schema_version': 1, 'redaction_reviewed': True,
        'project': {'name': 'Synthetic fixture', 'repository': 'fixture repository', 'commit': 'fixture-commit', 'dirty': False},
        'audit': {'date': '2026-10-09', 'timezone': 'Asia/Shanghai', 'auditor': 'Offline test', 'cost': 'No external calls', 'scope': ['local'], 'excluded': ['cloud'], 'authorized_actions': ['synthetic only'], 'baseline_changes': []},
        'executive_summary': 'Synthetic test data, not an audit conclusion.', 'methods': ['offline fixture'],
        'coverage': [{'area': 'local', 'status': 'partial', 'details': 'Synthetic only'}], 'limitations': ['No real project audited'],
        'findings': [{'id': 'F01', 'title': 'Synthetic issue', 'severity': 'medium', 'classification': 'confirmed', 'locations': ['fixture.py:1'], 'root_cause': 'Synthetic cause', 'preconditions': ['Local only'], 'impact': 'Synthetic effect', 'recommendation': 'Reject input', 'status': 'open', 'evidence_ids': ['E01', 'E02'], 'script_ids': ['R01'], 'initial': run, 'retest': retest, 'detailed_description': {'explain':'Synthetic input acceptance', 'chain':'input -> validator -> acceptance', 'scenario':'Local untrusted input', 'limits':'Synthetic only', 'steps':['Run local probe and inspect acceptance']}, 'key_evidence':[{'file':'fixture.py','start':1,'end':1,'excerpt':'accepted = True','evidence_id':'E01'}]}],
        'verified_controls': [], 'test_runs': [{'group': 'synthetic', 'round': 'initial', 'at': run['at'], 'command': 'python probe.py', 'total': 1, 'passed': 1, 'failed': 0, 'skipped': 0, 'evidence_ids': ['E01']}],
        'remediation_plan': [{'priority': 'P1', 'action': 'Synthetic repair', 'owner': 'Fixture', 'acceptance': 'Reject'}], 'next_steps': ['No live action'], 'references': [],
        'evidence': [{'id': 'E01', 'file': 'first.json', 'description': 'First synthetic result'}, {'id': 'E02', 'file': 'second.json', 'description': 'Retest synthetic result'}],
        'scripts': [{'id': 'R01', 'file': 'probe.py', 'description': 'Local fixture', 'command': 'python {script}', 'dependencies': ['Python standard library'], 'environment_variables': [], 'safety_scope': 'Local synthetic only', 'side_effects': 'None', 'stop_conditions': 'Reject remote targets'}]
    }


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path.cwd(), prefix='audit-selftest-')
        self.root = Path(self.temp.name)
        self.source = self.root / 'source'
        self.source.mkdir()
        for n in ['first.json', 'second.json']:
            (self.source / n).write_text('{"synthetic": true}', encoding='utf-8')
        (self.source / 'probe.py').write_text('print("synthetic offline probe")\n', encoding='utf-8')
        self.d = fixture()
    def tearDown(self):
        self.temp.cleanup()
    def build(self):
        (self.source / 'audit.json').write_text(json.dumps(self.d), encoding='utf-8')
        return builder.build(self.source / 'audit.json', self.root / 'bundle')
    def test_bundle_integrity_and_reproduction(self):
        result = self.build()
        self.assertEqual(result['findings'], 1)
        out = self.root / 'bundle'
        record = json.loads((out / 'audit.json').read_text(encoding='utf-8'))
        self.assertEqual(record['scripts'][0]['command'], 'python reproduce/probe.py')
        self.assertTrue((out / 'reproduce/probe.py').is_file())
        with zipfile.ZipFile(out / 'audit-bundle.zip') as z:
            self.assertIsNone(z.testzip())
            for line in z.read('SHA256SUMS.txt').decode().splitlines():
                digest, name = line.split('  ', 1)
                self.assertEqual(hashlib.sha256(z.read(name)).hexdigest(), digest)
    def test_detailed_report_contract(self):
        self.build()
        md=(self.root/'bundle/report.md').read_text(encoding='utf-8')
        for title in ['漏洞说明','数据流与漏洞链','关键证据','复现步骤','验证边界']:
            self.assertIn(title, md)
        for title in ['## 方法与覆盖','## 修复计划','## 费用']:
            self.assertNotIn(title, md)
    def test_historical_reference_not_rendered(self):
        self.d['historical_review']=[{'title':'HISTORICAL_ONLY_MARKER','previous':'Old claim','current':'Current observation','limits':'Local only','evidence_ids':['E01']}]
        self.build()
        for name in ['report.md','report.html']:
            text=(self.root/'bundle'/name).read_text(encoding='utf-8')
            self.assertNotIn('HISTORICAL_ONLY_MARKER',text)
            self.assertNotIn('历史问题对照',text)
            self.assertNotIn('旧报告与当前代码的对照',text)
    def test_thin_finding_rejected(self):
        del self.d['findings'][0]['detailed_description']
        with self.assertRaises(builder.AuditError): self.build()
    def test_missing_key_evidence_rejected(self):
        self.d['findings'][0]['key_evidence']=[]
        with self.assertRaises(builder.AuditError): self.build()
    def test_html_code_and_unsafe_url(self):
        page=builder.render('## Evidence\n\n```text\n<script>alert(1)</script>\n```\n\n[x](javascript:alert)')
        self.assertIn('<pre><code',page)
        self.assertIn('&lt;script&gt;',page)
        self.assertNotIn('href="javascript:',page)
        self.assertIn('<nav>',page)
    def test_missing_retest_rejected(self):
        del self.d['findings'][0]['retest']
        with self.assertRaises(builder.AuditError): self.build()
    def test_false_closure_rejected(self):
        self.d['findings'][0]['status'] = 'closed'
        with self.assertRaises(builder.AuditError): self.build()
    def test_fixed_closure_accepted(self):
        f = self.d['findings'][0]; f['status'] = 'closed'; f['retest']['kind'] = 'after_fix'; f['retest']['outcome'] = 'absent'
        self.build()
    def test_blocked_is_reported(self):
        r = self.d['findings'][0]['retest']; r.update(kind='blocked', outcome='blocked', reason='No authorized cloud access', evidence_ids=[])
        self.assertEqual(self.build()['blocked_retests'], 1)
        self.assertIn('未完成复测：F01', (self.root / 'bundle/report.md').read_text(encoding='utf-8'))
    def test_path_traversal_rejected(self):
        self.d['evidence'][0]['file'] = '../outside.json'
        with self.assertRaises(builder.AuditError): self.build()
    def test_unknown_evidence_rejected(self):
        self.d['findings'][0]['initial']['evidence_ids'] = ['missing']
        with self.assertRaises(builder.AuditError): self.build()
    def test_secret_rejected_before_delivery(self):
        (self.source / 'first.json').write_text('Bearer ' + 'a' * 40, encoding='utf-8')
        with self.assertRaises(builder.AuditError): self.build()
        self.assertFalse((self.root / 'bundle').exists())
    def test_wrong_test_counts_rejected(self):
        self.d['test_runs'][0]['total'] = 2
        with self.assertRaises(builder.AuditError): self.build()
    def test_html_escaped_and_csv_formula_neutralized(self):
        self.d['findings'][0]['title'] = '=1+1 <script>alert(1)</script>'
        self.build()
        out = self.root / 'bundle'
        self.assertNotIn('<script>', (out / 'report.html').read_text(encoding='utf-8'))
        self.assertIn("'=1+1", (out / 'findings.csv').read_text(encoding='utf-8-sig'))
    def test_no_findings_does_not_imply_full_coverage(self):
        self.d['findings'] = []
        self.assertEqual(self.build()['findings'], 0)
        self.assertIn('验证限制', (self.root / 'bundle/report.md').read_text(encoding='utf-8'))
    def test_existing_output_protected(self):
        self.build()
        with self.assertRaises(builder.AuditError): self.build()


if __name__ == '__main__':
    unittest.main(verbosity=2)
