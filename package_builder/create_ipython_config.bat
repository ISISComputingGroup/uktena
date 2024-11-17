REM create a default ipython_config
REM passed python directory as first arg
setlocal

set "PYDIR=%1"
set "PATH=%PYDIR%;%PYDIR%\DLLs;%PATH%"
set "PYTHONHOME=%PYDIR%"

set "OLDDIR=%CD%"
cd /d %PYDIR%
%PYDIR%\python.exe Scripts\ipython.exe profile create
set errcode=%errorlevel%
cd /d %OLDDIR%
if %errcode% neq 0 (
    @echo ERROR: Creating ipython profile %errcode%
	exit /B %errcode%
)

REM exclude LocalSystem account used for running jenkins service 
if "%UserProfile%" == "%SystemRoot%\system32\config\systemprofile" (
    exit /b 0
)	

REM auto copy the ipython_config
set "IPPROFDIR=%UserProfile%\.ipython\profile_default"

if exist "%IPPROFDIR%\ipython_config.py" (
    @echo INFO: Backing up old ipython config as %IPPROFDIR%\ipython_config.py.old
	copy /y %IPPROFDIR%\ipython_config.py %IPPROFDIR%\ipython_config.py.old
)

copy /y %~dp0ipython_config.py %IPPROFDIR%\ipython_config.py
if %errorlevel% neq 0 (
    @echo ERROR: Copying ipython profile %errorlevel%
	exit /B %errorlevel%
)

@echo ipython profile and config created
