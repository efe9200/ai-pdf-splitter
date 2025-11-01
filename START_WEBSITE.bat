@echo off
echo ============================================================
echo PDF PAGE EXTRACTOR - WEB APPLICATION
echo ============================================================
echo.
echo Starting the website...
echo.
echo The website will open in your browser automatically.
echo Go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server when you're done.
echo ============================================================
echo.

cd /d "%~dp0"
python app.py

pause
