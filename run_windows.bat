@echo off
setlocal
cd /d "%~dp0"

echo =============================================
echo   GymManagementDjango - Windows Launcher
echo =============================================
echo.

set "PYTHON_CMD="
where py >nul 2>nul
if %errorlevel%==0 (
    set "PYTHON_CMD=py -3"
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        set "PYTHON_CMD=python"
    ) else (
        where python3 >nul 2>nul
        if %errorlevel%==0 set "PYTHON_CMD=python3"
    )
)

if "%PYTHON_CMD%"=="" (
    echo [ERROR] Python not found.
    echo Install Python and enable "Add Python to PATH", then run this file again.
    pause
    exit /b 1
)

echo [1/5] Creating virtual environment (if needed)...
if not exist ".venv\Scripts\python.exe" (
    %PYTHON_CMD% -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Could not create virtual environment.
        pause
        exit /b 1
    )
)

set "VENV_PY=.venv\Scripts\python.exe"

echo [2/5] Installing/updating dependencies...
"%VENV_PY%" -m pip install --upgrade pip
if exist "requirements.txt" (
    "%VENV_PY%" -m pip install -r requirements.txt
) else (
    "%VENV_PY%" -m pip install "Django>=5,<6"
)
if errorlevel 1 (
    echo [ERROR] Dependency installation failed.
    pause
    exit /b 1
)

echo [3/5] Applying migrations...
"%VENV_PY%" manage.py migrate --noinput
if errorlevel 1 (
    echo [ERROR] Database migration failed.
    pause
    exit /b 1
)

echo [4/5] Opening browser...
start "" http://127.0.0.1:8000/

echo [5/5] Starting server...
echo Press Ctrl+C to stop the server.
echo.
"%VENV_PY%" manage.py runserver 127.0.0.1:8000

echo.
echo Server stopped.
pause
