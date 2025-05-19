REM Set release network drive
@echo on

setlocal EnableDelayedExpansion EnableExtensions
set "SHARE=\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP"

if not exist "%SHARE%" (
    @echo ERROR: Configuration - you do not have permission to access %SHARE%
    goto ERROR
)

REM Set directory for Python installation.
REM NOTE: Python 2 and 3 build dirs must be distinct or Jenkins fails
REM NOTE: Base directory must be called Python 3 zip extraction gives wrong directory structure
cd ..
set "PYTHONDIR=%cd%\build\3\Python"
cd %~dp0

REM Build Python in the designated directory
call common_build_python.bat
if %errorlevel% neq 0 exit /b %errorlevel%

for %%i in ( %WORKSPACE% ) do set WORKDRIVE=%%~di
REM need to translate / to _ in job name for multibranch pipelines
set "STAGEDIR=%WORKDRIVE%\STG\%JOB_NAME:/=_%_%BUILD_NUMBER%"
if not exist "%STAGEDIR%" mkdir "%STAGEDIR%"

REM These are part of "debugging tools for windows" and can be installed via
REM the Windows SDK, you can just select this and unselect other items
REM have been getting a missing entry point with symstore x64 and DbgHelp.dll
REM since updatign to VS2022. Have tried reinstall debug SDK but no change.
set "SYMSTORE32=C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\symstore.exe"
set "SYMSTORE64=C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\symstore.exe"
"%SYMSTORE64%" /? >NUL
if %errorlevel% equ 87 (
    set "SYMSTORE=%SYMSTORE64%"
) else (
    set "SYMSTORE=%SYMSTORE32%"
)
set "SYMCHK=C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\symchk.exe"
if "%RELEASE%"=="YES" (
    set "SYMDIR=%SHARE%\Releases\Symbols"
) else (
    set "SYMDIR=%SHARE%\EPICS\Symbols"
)

REM Don't group these RELEASE checks. Bat expands all if at once, not sequentially which causes issues
set KITS_DIR=
if "%RELEASE%" == "YES" (
	set RELEASE_DIR=%SHARE%\Releases\%RELEASE_BRANCH%
	set KITS_DIR=%SHARE%\Releases\%RELEASE_BRANCH%\genie_python_3
	set RELEASE_VERSION=%RELEASE_BRANCH%
) else (
   	set RELEASE_VERSION=devel-%GIT_COMMIT:~0,7%
    if "%BRANCH_NAME%" == "main" (
	    if not "%BUILD_NUMBER%" == "" (
			set KITS_DIR=%SHARE%\genie_python_3\BUILD-%BUILD_NUMBER%
	    )
    ) else (
        set "RELEASE_DIR=%SHARE%\genie_python_3\branches\%BRANCH_NAME%"
        set "KITS_DIR=%SHARE%\genie_python_3\branches\%BRANCH_NAME%\BUILD-%BUILD_NUMBER%"
    )
)

REM mkdir on a share does not seem to create intermediate directories
REM hence setting RELEASE_DIR above for branch builds
if not "%RELEASE_DIR%" == "" (
	if not exist "%RELEASE_DIR%" (
		mkdir %RELEASE_DIR%
	)
)

set BASEDIR=%~dp0
set "PYZIPTMP=Python-tmp.7z"
if not "%KITS_DIR%" == "" (
    REM Copy to kits
	if exist "%KITS_DIR%" (
        RMDIR /S /Q %KITS_DIR% || goto ERROR
	)

    "%BASEDIR%sleep" 10

    mkdir %KITS_DIR% || goto ERROR
    REM xcopy /q /s /e /h /i %PYTHONDIR% %KITS_DIR%\Python

	@echo !TIME! Start stage robocopy
    robocopy "%PYTHONDIR%" "%STAGEDIR%\Python" -MIR -XD ".git" "%PYTHONDIR%\build" "package_builder" -XF ".git" ".gitignore" ".gitmodules" ".gitattributes" "PULL_REQUEST_TEMPLATE.md" "Jenkinsfile" -NFL -NDL -NP -MT -NC -NS -R:1 -LOG:"robocopy_stage_log.txt"
	if !errorlevel! geq 4 (
        @echo ERROR: !errorlevel! in robocopy
	    goto ERROR
    )
    @echo !TIME! End stage robocopy

	@echo !TIME! Start zip
    pushd %STAGEDIR%\Python
    if exist "%STAGEDIR%\%PYZIPTMP%" del "%STAGEDIR%\%PYZIPTMP%"
    REM disable method filters to avoid 7zip version mismatch with new ARM64 filter
    "c:\Program Files\7-Zip\7z.exe" a "%STAGEDIR%\%PYZIPTMP%" . -mx1 -mf=off -r -xr^^!*-arm.exe -xr^^!*-arm64.exe
    set errcode=!errorlevel!
    popd
    if !errcode! gtr 1 exit /b !errcode!
	@echo !TIME! End zip

	@echo !TIME! Start network robocopy
    if "%RELEASE%" == "YES" (
        robocopy "%STAGEDIR%\Python" "%KITS_DIR%\Python" -MIR -NFL -NDL -NP -MT -NC -NS -R:1 -LOG:"robocopy_net_log.txt"
        set errcode=!errorlevel!
    ) else (
        robocopy "%STAGEDIR%\Python" "%KITS_DIR%\Python" BUILD_NUMBER.txt VERSION.txt -S -NFL -NDL -NP -MT -NC -NS -R:1 -LOG:"robocopy_net_log.txt"
        set errcode=!errorlevel!
        @echo YES>%KITS_DIR%\Python\ZIP_ONLY_INSTALL.txt
    )
	if !errcode! geq 4 (
        @echo ERROR: !errcode! in robocopy
	    goto ERROR
    )
    @echo !TIME! End network robocopy

    REM add debugging symbols to central store
    REM /o gives more verbose output
    if exist "%SYMSTORE%" (
        @echo Using "%SYMSTORE%"
	    pushd "%PYTHONDIR%"
        "%SYMSTORE%" add /r /f . /s %SYMDIR% /t "genie_python" /v "%RELEASE_VERSION%" /c "%GIT_COMMIT:~0,7% (%BUILD_NUMBER%)"
		set errcode=!errorlevel!
		popd
        if !errcode! neq 0 (
            @echo ERROR: SYMSTORE terminated with code !errcode!
            exit /b !errcode!
        )
		REM symchk takes a long time, need to rethink. It is partly because it is checking ICP_Binaries and the Python
		REM that is copied into the jenkins workspace. Maybe need to run it on selective directories.
		REM
        REM add /os to print symbol path
        REM "%SYMCHK%" /r %BUILD_DIR% /seu srv*%SYMDIR%*https://msdl.microsoft.com/download/symbols /ob
        REM if !errorlevel! neq 0 exit /b !errorlevel!
    ) else (
        @echo ERROR: SYMSTORE is not installed
        exit /b 1
    )
	
	REM copy 7zip
	if not exist "%KITS_DIR%\zips" mkdir "%KITS_DIR%\zips"
	if exist "%KITS_DIR%\zips\%PYZIPTMP%" del "%KITS_DIR%\zips\%PYZIPTMP%"
	if exist "%KITS_DIR%\zips\Python.7z" del "%KITS_DIR%\zips\Python.7z"
	xcopy /y /j /i "%STAGEDIR%\%PYZIPTMP%" "%KITS_DIR%\zips"
    if !errorlevel! neq 0 exit /b !errorlevel!
	rd /s /q "%STAGEDIR%"
    ren "%KITS_DIR%\zips\%PYZIPTMP%" "Python.7z"
    if !errorlevel! neq 0 (
        waitfor /t 30 WillNeverHappen >NUL 2>&1
        ren "%KITS_DIR%\zips\%PYZIPTMP%" "Python.7z"
    )

	REM Add top level deployment files
    @echo on
    @echo %BUILD_NUMBER%> %KITS_DIR%\BUILD_NUMBER.txt
    @echo %RELEASE_VERSION%> %KITS_DIR%\VERSION.txt
	@echo off
	copy %BASEDIR%\ipython_config.py %KITS_DIR%\ipython_config.py
    if !errorlevel! neq 0 goto ERROR
    copy %BASEDIR%\genie_python_install.bat %KITS_DIR%\genie_python_install.bat
    if !errorlevel! neq 0 goto ERROR
    copy %BASEDIR%\create_ipython_config.bat %KITS_DIR%\create_ipython_config.bat
    if !errorlevel! neq 0 goto ERROR
    
    @echo Copy complete>%KITS_DIR%\COPY_COMPLETE.txt

    if not "%RELEASE%" == "YES" (
      @echo %BUILD_NUMBER%>%KITS_DIR%\..\LATEST_BUILD.txt
    )

)

REM Report errors if any
if %errorlevel% neq 0 exit /b %errorlevel%

goto :EOF
:ERROR
exit /b 1
