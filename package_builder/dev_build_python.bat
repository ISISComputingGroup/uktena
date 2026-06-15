@echo off
setlocal

REM Set directory for Python installation
cd ..
set PYTHONDIR=%cd%
cd %~dp0

for /f "usebackq" %%f in (`tasklist /fi "modules eq python3.dll" ^| findstr /i "image name"`) do (
    @echo ERROR: Python processes running - please stop these / ibex server
    tasklist /fi  "modules eq python3.dll"
    exit /b 1
)

REM kill caRepeater.exe in case we need to replace it
taskkill /f /im caRepeater.exe

@echo on

REM Build Python in the designated directory
call common_build_python.bat %*
if %errorlevel% neq 0 exit /b %errorlevel%

REM create ipython config
call create_ipython_config.bat %PYTHONDIR%
if %errorlevel% neq 0 exit /b %errorlevel%
