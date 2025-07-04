setlocal EnableDelayedExpansion

set DEFAULT_PATH=C:\Instrument\Apps\Python3

REM %~dp0 expands to directory where this file lives
set BASEDIR=%~dp0

if not "%KITS_DIR%" == "" (
	if not exist "%BASEDIR%COPY_COMPLETE.txt" (
		@echo Incomplete distribution - please try again later
		exit/B 1
	)
)

REM Copy the files across
if "%1" == "" (
    set PYDIR=%DEFAULT_PATH%
) else (
    set PYDIR=%1
)

if exist "%PYDIR%" rd /s /q %PYDIR%
REM try with long path prefix. Note that we haven't added it
REM directly to PYDIR as we may need to check PYDIR for UNC path and
REM also robocopy would need /256 flag to stop it adding this prefix itself
REM and erroring
if exist "%PYDIR%" rd /s /q "\\.\%PYDIR%"

mkdir %PYDIR%

REM we unzip the archive and then robocopy as before
REM this is in case there has been a patch to the on-disk files
REM if there are no changes the robocopy is very quick
set "ZIPPROG=c:\Program Files\7-Zip\7z.exe"
if exist "%ZIPPROG%" (
    if exist "%BASEDIR%zips\Python.7z" (
        "%ZIPPROG%" x -aoa -o%PYDIR% "%BASEDIR%zips\Python.7z"
        set errcode=!errorlevel!
        if !errcode! gtr 1 (
            @echo UNZIP error !errcode!
            exit /b !errcode!
        )
    )
)

@echo %TIME% genie_python robocopy started
if exist "%BASEDIR%\Python\ZIP_ONLY_INSTALL.txt" (
    if not exist "%ZIPPROG%" (
        @echo ERROR: No 7-ZIP program found for genie_python install
        exit /b 1
    )
    robocopy "%BASEDIR%\Python" "%PYDIR%" /E /R:2 /MT /NFL /NDL /NP /NC /NS /LOG:NUL /XF "ZIP_ONLY_INSTALL.txt"
) else (
    robocopy "%BASEDIR%\Python" "%PYDIR%" /MIR /R:2 /MT /NFL /NDL /NP /NC /NS /LOG:NUL
)
set errcode=%errorlevel%
if %errcode% GEQ 4 (
    @echo ERROR %errcode% in robocopy
    exit /b %errcode%
)

@echo %TIME% genie_python robocopy finished

if not exist "%PYDIR%\python.exe" (
    @echo ERROR: genie_python did not install correctly to %PYDIR%
    exit /b 1
)

REM we need to set PYTHONPATH and PYTHONHOME if we plan to run python in this script.
REM They can get set during a deploy that runs python from the network
set "PYTHONPATH=%PYDIR%"
set "PYTHONHOME=%PYDIR%"

REM re-install lewis so lewis-control.exe can be used (currently it bakes in the build server Python path) see https://github.com/ISISComputingGroup/IBEX/issues/6256
REM hotfix needed in lewis for https://github.com/ISISComputingGroup/IBEX/issues/6177 and https://github.com/ess-dmsc/lewis/pull/293
%PYDIR%\python.exe -m pip install --force-reinstall lewis

REM create a default ipython_config
call %BASEDIR%\create_ipython_config.bat %PYDIR%
if %errorlevel% neq 0 exit /b %errorlevel%

echo %TIME% genie_python installed to %PYDIR%
