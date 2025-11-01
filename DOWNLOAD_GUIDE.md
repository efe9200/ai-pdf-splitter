# How to Download and Run AI PDF Splitter

## For Windows Users (Easiest Method)

### Step 1: Download the Program

1. Go to: **https://github.com/efe9200/ai-pdf-splitter**
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Save the file to your computer (e.g., Downloads folder)

### Step 2: Extract the Files

1. Find the downloaded file (ai-pdf-splitter-main.zip)
2. Right-click on it
3. Select **"Extract All..."**
4. Choose where to extract (e.g., Desktop or Documents)
5. Click **"Extract"**

### Step 3: Run the Setup

1. Open the extracted folder (ai-pdf-splitter-main)
2. Find **"SETUP.bat"**
3. Double-click **"SETUP.bat"**
4. Follow the on-screen instructions:
   - The setup will install all needed software
   - You can choose to set up AI features (optional)
   - It will create a desktop icon for you

### Step 4: Launch the Application

**Method 1: Desktop Icon (Easiest)**
- Double-click the **"AI PDF Splitter"** icon on your desktop
- Your web browser will open automatically

**Method 2: Batch Files**
- Go to the program folder
- Double-click any of these files:
  - `START_WEBSITE_WITH_DEEPSEEK.bat` (if you configured DeepSeek)
  - `START_WEBSITE_WITH_AI.bat` (if you configured OpenAI)
  - `START_WEBSITE.bat` (manual mode only)

### Step 5: Use the Application

1. Your browser opens to http://localhost:5000
2. Choose a mode:
   - **AI Analysis Tab**: Upload PDF and let AI suggest how to split it
   - **Manual Split Tab**: Choose specific pages yourself
3. Upload your PDF file
4. Follow the instructions on screen
5. Download your split PDFs!

---

## Troubleshooting

### "Python is not installed" error
1. Download Python from: https://www.python.org/downloads/
2. During installation, CHECK the box "Add Python to PATH"
3. Run SETUP.bat again

### The desktop icon doesn't appear
- Open the program folder
- Double-click one of the START_WEBSITE_*.bat files instead

### The browser doesn't open automatically
- Open your web browser manually
- Go to: http://localhost:5000

### "pip install failed" error
1. Open Command Prompt as Administrator
2. Navigate to the program folder:
   ```
   cd path\to\ai-pdf-splitter-main
   ```
3. Run:
   ```
   pip install -r requirements.txt
   ```

### AI features don't work
- AI features are optional
- Manual split mode always works without AI
- To use AI:
  1. Get an API key from DeepSeek, OpenAI, or Anthropic
  2. Run SETUP.bat again
  3. Choose the AI option and enter your key

---

## What You Get

After setup, you'll have:
- A desktop icon with custom design
- Easy one-click access to the PDF splitter
- AI-powered PDF analysis (if configured)
- Manual PDF splitting (always available)
- Support for files up to 500MB

---

## Uninstalling

To remove the program:
1. Delete the desktop icon
2. Delete the program folder (ai-pdf-splitter-main)
3. That's it!

---

## Need Help?

- Check the README.md file in the program folder
- Visit: https://github.com/efe9200/ai-pdf-splitter/issues
- Review the troubleshooting section above

---

**Enjoy your AI-Powered PDF Splitter!** 🚀
