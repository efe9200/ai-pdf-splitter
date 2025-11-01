@echo off
REM ========================================
REM AI-Powered PDF Splitter - Setup Script
REM ========================================

echo.
echo ========================================
echo AI-POWERED PDF SPLITTER - SETUP
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed!
    echo.
    echo Please install Python 3.7 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

echo [OK] Python is installed
python --version
echo.

REM Install required packages
echo Installing required packages...
echo.
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to install packages!
    pause
    exit /b 1
)

echo.
echo [OK] All packages installed successfully!
echo.

REM Create the application icon
echo Creating application icon...
python create_icon.py
if errorlevel 1 (
    echo [WARNING] Could not create icon, but continuing...
)

echo.
echo ========================================
echo SETUP AI PROVIDER (Optional)
echo ========================================
echo.
echo The PDF Splitter has two modes:
echo   1. Manual Mode - Works without AI (no setup needed)
echo   2. AI Mode - Requires an API key
echo.
echo Choose your AI provider:
echo.
echo   A. DeepSeek (Recommended - Super cheap: $0.0001 per analysis)
echo      Get key: https://platform.deepseek.com/api_keys
echo.
echo   B. OpenAI GPT-4o-mini (Fast: $0.003 per analysis)
echo      Get key: https://platform.openai.com/api-keys
echo.
echo   C. Anthropic Claude (Best quality: $0.003 per analysis)
echo      Get key: https://console.anthropic.com/settings/keys
echo.
echo   D. Ollama (FREE - runs locally, requires download)
echo      Download: https://ollama.com
echo.
echo   E. Skip AI setup (Manual mode only)
echo.

choice /C ABCDE /N /M "Select option (A/B/C/D/E): "

if errorlevel 5 goto :skip_ai
if errorlevel 4 goto :setup_ollama
if errorlevel 3 goto :setup_anthropic
if errorlevel 2 goto :setup_openai
if errorlevel 1 goto :setup_deepseek

:setup_deepseek
echo.
echo Setting up DeepSeek...
echo.
set /p DEEPSEEK_KEY="Enter your DeepSeek API key: "
(
echo @echo off
echo set DEEPSEEK_API_KEY=%DEEPSEEK_KEY%
echo set AI_PROVIDER=deepseek
echo start http://localhost:5000
echo python app.py
echo pause
) > START_WEBSITE_WITH_DEEPSEEK.bat
echo [OK] DeepSeek configured! Use START_WEBSITE_WITH_DEEPSEEK.bat
goto :create_shortcut

:setup_openai
echo.
echo Setting up OpenAI...
echo.
set /p OPENAI_KEY="Enter your OpenAI API key: "
(
echo @echo off
echo set OPENAI_API_KEY=%OPENAI_KEY%
echo set AI_PROVIDER=openai
echo start http://localhost:5000
echo python app.py
echo pause
) > START_WEBSITE_WITH_AI.bat
echo [OK] OpenAI configured! Use START_WEBSITE_WITH_AI.bat
goto :create_shortcut

:setup_anthropic
echo.
echo Setting up Anthropic Claude...
echo.
set /p ANTHROPIC_KEY="Enter your Anthropic API key: "
(
echo @echo off
echo set ANTHROPIC_API_KEY=%ANTHROPIC_KEY%
echo set AI_PROVIDER=anthropic
echo start http://localhost:5000
echo python app.py
echo pause
) > START_WEBSITE_WITH_ANTHROPIC.bat
echo [OK] Anthropic configured! Use START_WEBSITE_WITH_ANTHROPIC.bat
goto :create_shortcut

:setup_ollama
echo.
echo To use Ollama:
echo 1. Download and install from: https://ollama.com
echo 2. Run: ollama pull llama3.2
echo 3. Use START_WEBSITE_WITH_OLLAMA.bat
echo.
goto :create_shortcut

:skip_ai
echo.
echo [OK] Skipping AI setup. You can use Manual mode.
echo.

:create_shortcut
echo.
echo ========================================
echo CREATE DESKTOP SHORTCUT
echo ========================================
echo.
choice /C YN /M "Create a desktop shortcut with icon? (Y/N)"
if errorlevel 2 goto :finish

echo.
echo Creating desktop shortcut...
python create_shortcut.py
if errorlevel 1 (
    echo [WARNING] Could not create shortcut automatically.
    echo You can manually create a shortcut to the .bat file.
)

:finish
echo.
echo ========================================
echo SETUP COMPLETE!
echo ========================================
echo.
echo You can now run the PDF Splitter by:
echo   1. Double-clicking "AI PDF Splitter" on your desktop, OR
echo   2. Double-clicking START_WEBSITE_WITH_*.bat in this folder, OR
echo   3. Running: python app.py
echo.
echo The application will open in your web browser at:
echo http://localhost:5000
echo.
echo Enjoy splitting your PDFs!
echo ========================================
echo.
pause
