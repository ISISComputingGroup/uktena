REM Set release network drive
@echo off
setlocal
@echo on

REM Set directory for Python installation
cd ..
set PYTHONDIR=%cd%
cd %~dp0

REM kill caRepeater.exe in case we need to replace it
taskkill /f /im caRepeater.exe

set PYTHONRUNNING=
for /f "usebackq" %%f in (`tasklist ^| findstr /i python.exe`) do set PYTHONRUNNING=1
if not "%PYTHONRUNNING%" == "" (
    @echo ERROR: Python.exe processes running - please stop these / ibex server
    tasklist /fi  "IMAGENAME eq python.exe"
    exit /b 1
)
set PYTHONWRUNNING=
for /f "usebackq" %%f in (`tasklist ^| findstr /i pythonw.exe`) do set PYTHONWRUNNING=1
if not "%PYTHONWRUNNING%" == "" (
    @echo ERROR: Pythonw.exe processes running - please stop these / ibex server
    tasklist /fi  "IMAGENAME eq pythonw.exe"
    exit /b 1
)

REM Build Python in the designated directory
call common_build_python.bat %*
if %errorlevel% neq 0 exit /b %errorlevel%

REM create ipython config
call create_ipython_config.bat %PYTHONDIR%
if %errorlevel% neq 0 exit /b %errorlevel%
