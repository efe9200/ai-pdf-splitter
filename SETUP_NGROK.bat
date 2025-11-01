@echo off
echo ============================================================
echo NGROK SETUP - Make Your Website Public
echo ============================================================
echo.
echo STEP 1: Download ngrok
echo ------------------------
echo 1. Go to: https://ngrok.com/download
echo 2. Create a free account
echo 3. Download ngrok for Windows
echo 4. Move ngrok.exe to this folder: %~dp0
echo.
echo STEP 2: Get your auth token
echo ---------------------------
echo 1. Login to: https://dashboard.ngrok.com/
echo 2. Copy your auth token
echo.
echo STEP 3: Authenticate ngrok
echo --------------------------
echo Run this command (replace YOUR_TOKEN with your actual token):
echo    ngrok authtoken YOUR_TOKEN
echo.
echo STEP 4: Start your website
echo --------------------------
echo 1. Run START_WEBSITE.bat first
echo 2. Wait for it to show "Running on http://127.0.0.1:5000"
echo.
echo STEP 5: Run ngrok
echo -----------------
echo Run this command:
echo    ngrok http 5000
echo.
echo You'll get a public URL like: https://abc123.ngrok.io
echo Share this URL with anyone!
echo.
echo ============================================================
echo.
echo Press any key to open ngrok website...
pause > nul
start https://ngrok.com/download
