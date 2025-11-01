# AI-Powered PDF Splitter - Setup Guide

## Overview

Your PDF splitter now has AI capabilities! The AI can:
- Analyze the content and structure of your PDF
- Understand what type of document it is (textbook, report, manual, etc.)
- Suggest intelligent ways to split it based on the content
- Answer your specific questions about how to split the document

## Quick Start

### Option 1: Using Anthropic Claude (Recommended)

1. **Get an API Key:**
   - Go to https://console.anthropic.com/
   - Sign up for an account (free tier available)
   - Go to "API Keys" section
   - Click "Create Key" and copy it

2. **Set the API Key:**

   **Windows (Command Prompt):**
   ```cmd
   set ANTHROPIC_API_KEY=your_key_here
   python app.py
   ```

   **Windows (PowerShell):**
   ```powershell
   $env:ANTHROPIC_API_KEY="your_key_here"
   python app.py
   ```

   **Or create a batch file (EASIEST):**
   - Edit `START_WEBSITE_WITH_AI.bat`
   - Replace `your_anthropic_api_key_here` with your actual key
   - Double-click the batch file to start

### Option 2: Using OpenAI GPT

1. **Get an API Key:**
   - Go to https://platform.openai.com/api-keys
   - Sign up for an account (requires credit card, pay-as-you-go)
   - Click "Create new secret key" and copy it

2. **Set the API Key:**

   **Windows (Command Prompt):**
   ```cmd
   set OPENAI_API_KEY=your_key_here
   set AI_PROVIDER=openai
   python app.py
   ```

## Cost Comparison

### Anthropic Claude
- **Free Tier:** $5 credit for new users
- **Cost:** ~$0.003 per PDF analysis (very cheap)
- **Model:** Claude 3.5 Sonnet (excellent quality)
- **Recommended for:** Most users

### OpenAI GPT
- **Free Tier:** None (but $5 credit for new users sometimes)
- **Cost:** ~$0.001 per PDF analysis (cheaper but requires credit card)
- **Model:** GPT-4o-mini (good quality)
- **Recommended for:** Users who already have OpenAI account

## How to Use

1. **Start the website** with your API key configured

2. **You'll see two tabs:**
   - **AI Analysis** - Upload PDF and let AI suggest how to split
   - **Manual Split** - Traditional page number entry

3. **In AI Analysis tab:**
   - Upload your PDF
   - (Optional) Ask AI a specific question like:
     - "How should I split this textbook?"
     - "Separate by chapters"
     - "Split into introduction and main content"
   - Click "Analyze with AI"
   - AI will suggest 2-3 splitting strategies
   - Click on any suggestion to automatically use it

4. **Review and Extract:**
   - Click on a suggestion to auto-fill the pages
   - Switch to "Manual Split" tab (pages will be filled in)
   - Click "Extract Pages" to download

## Example Usage

### Example 1: Chemistry Textbook
**Upload:** chemistry_textbook.pdf (500 pages)

**AI Analysis Says:**
- **Document Type:** Academic Textbook
- **Structure:** 15 chapters with introduction and appendix
- **Suggestions:**
  1. By Major Sections: Introduction (1-20), Chapters (21-450), Appendix (451-500)
  2. By Chapter Groups: Intro Chemistry (1-100), Organic (101-250), Advanced (251-500)
  3. Individual Chapters: 15 separate files

**You Choose:** Click "By Chapter Groups" → Automatically extracts 3 PDFs

### Example 2: Business Report
**Upload:** annual_report.pdf (80 pages)

**AI Analysis Says:**
- **Document Type:** Business Report
- **Structure:** Executive summary, financial data, and appendices
- **Suggestions:**
  1. Executive Summary Only (1-5)
  2. Main Report (1-60), Appendices (61-80)
  3. By Sections: Exec Summary (1-5), Operations (6-30), Financials (31-60), Appendices (61-80)

## Troubleshooting

### "AI Analysis Not Configured"
- You haven't set your API key
- Follow the setup steps above

### "API key is invalid"
- Check that you copied the entire key
- Make sure there are no extra spaces
- Try regenerating the key

### Analysis takes too long
- Normal for large PDFs (30-60 seconds)
- AI analyzes up to first 30 pages to save time and cost
- If it times out, try a smaller PDF first

### "Insufficient credits" error
- Your free credits ran out
- Add payment method to your AI provider account
- Each analysis costs less than 1 cent

## Privacy & Security

- **PDFs are NOT stored** - Deleted immediately after analysis
- **Content is sent to AI provider** - Don't use for confidential documents
- **API keys are never logged** - Kept in your environment variables only

## Advanced: Permanent Configuration

To avoid setting the API key every time:

1. **Create a `.env` file:**
   ```
   ANTHROPIC_API_KEY=your_actual_key_here
   AI_PROVIDER=anthropic
   ```

2. **Install python-dotenv:**
   ```
   pip install python-dotenv
   ```

3. **Update app.py** to load from .env (already configured if you follow the code)

## Cost Estimates

Based on typical usage:

| PDF Size | Pages Analyzed | Cost (Anthropic) | Cost (OpenAI) |
|----------|---------------|------------------|---------------|
| Small    | 10 pages      | $0.001          | $0.0005       |
| Medium   | 30 pages      | $0.003          | $0.001        |
| Large    | 50 pages      | $0.005          | $0.002        |

**Bottom line:** You can analyze ~1000 PDFs with just $5 credit!

## Need Help?

1. Check that your API key is set correctly
2. Make sure you have internet connection
3. Try with a small PDF first (under 20 pages)
4. Check your API provider's dashboard for usage and errors

## What AI Can Do

✅ **Can Do:**
- Identify document type and structure
- Suggest logical splitting points
- Understand chapters, sections, topics
- Respond to your specific splitting questions
- Handle multiple languages

❌ **Cannot Do:**
- Read images or scanned PDFs perfectly (text-based PDFs work best)
- Split files automatically (you still need to click extract)
- Process password-protected PDFs
- Analyze more than 50 pages (to save costs)

Enjoy your AI-powered PDF splitter! 🚀
