@echo off
setlocal EnableDelayedExpansion
REM 一键将 Sean's Skills 的 rules 与「引用本库」的规则配置到目标项目的 .cursor 中，无需人工参与，AI 可直接使用。
REM 用法: scripts\integrate-into-project.bat <目标项目路径> [sean-s-skills 路径]
REM 示例: scripts\integrate-into-project.bat ..\my-app
REM       scripts\integrate-into-project.bat D:\proj\my-app D:\repos\sean-s-skills

if "%~1"=="" (
  echo 用法: %~nx0 ^<目标项目路径^> [sean-s-skills 路径]
  exit /b 1
)

set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
if "%~2"=="" (
  for %%I in ("%SCRIPT_DIR%\..") do set "SEAN_SKILLS_PATH=%%~fI"
) else (
  for %%I in ("%~2") do set "SEAN_SKILLS_PATH=%%~fI"
)
for %%I in ("%~1") do set "TARGET=%%~fI"

echo 目标项目: %TARGET%
echo Sean's Skills 路径: %SEAN_SKILLS_PATH%

REM 用 PowerShell 计算相对路径（目标项目到本库），并统一为 /
for /f "usebackq delims=" %%R in (`powershell -NoProfile -Command "$t='%TARGET:\=/%'; $s='%SEAN_SKILLS_PATH:\=/%'; $t=[System.IO.Path]::GetFullPath($t); $s=[System.IO.Path]::GetFullPath($s); $r=[System.IO.Path]::GetRelativePath($t, $s).Replace('\', '/'); Write-Output $r"`) do set "REL_PATH=%%R"
if not defined REL_PATH set "REL_PATH=../sean-s-skills"
echo 相对路径: %REL_PATH%

REM 创建 .cursor\rules
if not exist "%TARGET%\.cursor\rules" mkdir "%TARGET%\.cursor\rules"

REM 1. 写入 use-sean-s-skills.mdc（调用 PowerShell 脚本生成）
set "RULE_FILE=%TARGET%\.cursor\rules\use-sean-s-skills.mdc"
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_DIR%\integrate-into-project-impl.ps1" -RelPath "%REL_PATH%" -OutFile "%RULE_FILE%" -SkillsRoot "%SEAN_SKILLS_PATH%\skills"
if errorlevel 1 exit /b 1
echo 已创建 %RULE_FILE%

REM 2. 复制用户级规则
if exist "%SEAN_SKILLS_PATH%\rules\skill-usage.mdc" (
  copy /Y "%SEAN_SKILLS_PATH%\rules\skill-usage.mdc" "%TARGET%\.cursor\rules\skill-usage.mdc" >nul
  echo 已复制 rules\skill-usage.mdc
)
if exist "%SEAN_SKILLS_PATH%\rules\confirmation-before-action.mdc" (
  copy /Y "%SEAN_SKILLS_PATH%\rules\confirmation-before-action.mdc" "%TARGET%\.cursor\rules\confirmation-before-action.mdc" >nul
  echo 已复制 rules\confirmation-before-action.mdc
)

echo.
echo 集成完成。目标项目 .cursor\rules 已包含：
echo   - use-sean-s-skills.mdc（引用本库路径，AI 可直接使用 本库全部 Skill + 7 个 Agent）
echo   - skill-usage.mdc、confirmation-before-action.mdc（用户级规则）
echo 在 Cursor 中打开目标项目即可使用，无需其他配置。
endlocal
