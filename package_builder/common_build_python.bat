cd %~dp0\..
set PYTHONDIR=%cd%
cd %~dp0

@echo Using PYTHONDIR %PYTHONDIR%

set PYTHONHOME=%PYTHONDIR%
set PYTHONPATH=%PYTHONDIR%
set PYTHON=%PYTHONDIR%\python.exe
set PYTHON3=%PYTHONDIR%\python.exe
set PYTHONW=%PYTHONDIR%\pythonw.exe
set PYTHON3W=%PYTHONDIR%\pythonw.exe

set PYTHOND=%PYTHONDIR%\python_d.exe
set PYTHON3D=%PYTHONDIR%\python_d.exe

set PIP_CONSTRAINT=%~dp0\constraints.txt

git clean -fqdX %PYTHONDIR%\Lib\
del /q /f %PYTHONDIR%\*.exe
del /q /f %PYTHONDIR%\*.dll
del /q /f %PYTHONDIR%\*.pdb
del /q /f %PYTHONDIR%\DLLs\*
del /q /f %PYTHONDIR%\__pycache__\*
del /q /f /s %PYTHONDIR%\Scripts\*

REM Check this isn't an EPICS terminal
if not "%ICP_CONFIG_ENV_BASE_RUN%" == "" (
    echo ERROR: Python detected on system path. Do not run from an EPICS terminal
    set errorlevel=1
    goto :ERROR
)

REM Copy in genie_python.bat
copy %~dp0\genie_python.bat %PYTHONDIR%\.
copy %~dp0\genie_python3.bat %PYTHONDIR%\.
copy %~dp0\genie_python_main.bat %PYTHONDIR%\.
copy %~dp0\genie_python_simulate.bat %PYTHONDIR%\.
copy %~dp0\get_isis_ip.bat %PYTHONDIR%\.
copy %~dp0\genie_python.ico %PYTHONDIR%\.


REM Add version
@echo on
@echo %BUILD_NUMBER%> BUILD_NUMBER.txt
@echo %RELEASE_VERSION%> VERSION.txt
copy %~dp0\BUILD_NUMBER.txt %PYTHONDIR%\.
copy %~dp0\VERSION.txt %PYTHONDIR%\.

set "SHARE=\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP"
robocopy "%SHARE%\EPICS_UTILS\EPICS_UTILS" "%PYTHONDIR%\EPICS_UTILS" /MIR /PURGE /MT /NP /NFL /NDL /NC /NS /LOG:NUL
if %errorlevel% geq 4 (
    @echo ERROR: %errorlevel% in robocopy of EPICS_UTILS
    goto ERROR
)
xcopy /q /y %PYTHONDIR%\EPICS_UTILS\caRepeater.exe %PYTHONDIR%
if %errorlevel% neq 0 exit /b %errorlevel%

robocopy "%SHARE%\uktena_dependencies" "%~dp0\python_deps" /MIR /PURGE /MT /NP /NFL /NDL /NC /NS /LOG:NUL
if %errorlevel% geq 4 (
    @echo ERROR: %errorlevel% in robocopy of uktena_dependencies
    goto ERROR
)

set ZIPEXE=C:\"Program Files"\7-Zip\7z.exe

set PYTHONVER=3.12
set PYTHONPATCH=9
set PYTHONVERND=%PYTHONVER:.=%

%ZIPEXE% x "%~dp0\python_deps\python_clean_%PYTHONVER%.%PYTHONPATCH%.zip" -y -o%PYTHONDIR%
if %errorlevel% neq 0 exit /b %errorlevel%

setlocal

cd %PYTHONDIR%

del /f /q %~dp0\pip_upgrade.log
del /f /q %~dp0\pip_requirements.log

%PYTHON% -m ensurepip
if %errorlevel% neq 0 exit /b %errorlevel%

set "PATH=%PYTHONDIR%\Scripts;%PATH%"

%PYTHON% -m pip install --cache-dir %~dp0\.pip_cache --upgrade pip --log %~dp0\pip_upgrade.log
if %errorlevel% neq 0 exit /b %errorlevel%

%PYTHON% -m pip install --cache-dir %~dp0\.pip_cache -r %~dp0\requirements.txt --no-warn-script-location --log %~dp0\pip_requirements.log
if %errorlevel% neq 0 exit /b %errorlevel%

cd %~dp0

REM make sure we have a python3 executable
if not exist "%PYTHONDIR%\python3.exe" (
    copy "%PYTHONDIR%\python.exe" "%PYTHONDIR%\python3.exe"
    copy "%PYTHONDIR%\python.pdb" "%PYTHONDIR%\python3.pdb"
)
if not exist "%PYTHONDIR%\python%PYTHONVER%.exe" (
    copy "%PYTHONDIR%\python.exe" "%PYTHONDIR%\python%PYTHONVER%.exe"
    copy "%PYTHONDIR%\python.pdb" "%PYTHONDIR%\python%PYTHONVER%.pdb"
)

xcopy /i /y snmp-mibs\*.py %PYTHONDIR%\Lib\site-packages\pysnmp\smi\mibs

goto :EOF

:ERROR
exit /b %errorlevel%
