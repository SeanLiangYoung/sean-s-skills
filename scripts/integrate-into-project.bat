@echo off
setlocal
REM Usage: integrate-into-project.bat <target project> [library root]
if "%~1"=="" (
  echo Usage: %~nx0 ^<target project^> [library root]
  exit /b 1
)
if "%~2"=="" (
  powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0integrate-into-project-impl.ps1" -TargetProject "%~1"
) else (
  powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0integrate-into-project-impl.ps1" -TargetProject "%~1" -LibraryRoot "%~2"
)
exit /b %errorlevel%
