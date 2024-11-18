@echo off

setlocal
call "%~dp0genie_python_main.bat" "%~dp0python3.exe" %*
if %errorlevel% neq 0 exit /B %errorlevel%
