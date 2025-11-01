# AI-Powered PDF Splitter

A powerful web application that uses AI to intelligently analyze and split PDF documents.

## Features

### 🤖 AI-Powered Analysis
- **4 AI Options**: DeepSeek (super cheap), OpenAI, Anthropic Claude, or Ollama (free & local)
- **Smart Suggestions**: AI analyzes your PDF and suggests intelligent ways to split it
- **Multiple Output Formats**: Single PDF or multiple PDFs in a ZIP archive

### 📄 Multiple PDF Generation
- **Intelligent Splitting**: When AI suggests splitting by sections (e.g., "By Chapter"), it automatically creates separate PDF files for each section
- **ZIP Download**: All split PDFs are packaged in a single ZIP file for easy download
- **Named Files**: Each PDF is named according to the section (e.g., "Introduction.pdf", "Chapter_1.pdf")

### ⚡ Manual Splitting
- **Two Modes**:
  - **Single File Mode**: Extract one PDF with specified pages (e.g., "1-10,15,20-25")
  - **Multiple Files Mode**: Create multiple named PDFs (e.g., "Chapter 1: pages 1-10", "Chapter 2: pages 11-20")
- **Large File Support**: Up to 500MB PDFs
- **Instant Download**: Extract and download in seconds
- **Custom Naming**: Name each section in multiple files mode

## Quick Start (Windows)

### Easy Installation (Recommended)

1. **Download the project:**
   - Click the green "Code" button → "Download ZIP"
   - Extract the ZIP file to your desired location

2. **Run the setup:**
   - Double-click `SETUP.bat`
   - Follow the on-screen instructions
   - The setup will:
     - Install all required packages
     - Create a desktop icon
     - Optionally configure AI provider

3. **Launch the app:**
   - Double-click "AI PDF Splitter" icon on your desktop
   - Or double-click any `START_WEBSITE_WITH_*.bat` file
   - Your browser will open automatically

That's it! The app is ready to use.

---

## Manual Installation (Advanced Users)

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone https://github.com/efe9200/ai-pdf-splitter.git
cd ai-pdf-splitter
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up AI Provider (Optional)

Choose one of the following AI providers for the AI analysis feature:

#### Option A: DeepSeek (Recommended - Super Cheap!)
1. Get API key from: https://platform.deepseek.com/api_keys
2. Copy `START_WEBSITE_WITH_DEEPSEEK.bat.template` to `START_WEBSITE_WITH_DEEPSEEK.bat`
3. Edit the file and replace `your-deepseek-api-key-here` with your actual API key

#### Option B: OpenAI GPT
1. Get API key from: https://platform.openai.com/api-keys
2. Copy `START_WEBSITE_WITH_AI.bat.template` to `START_WEBSITE_WITH_AI.bat`
3. Edit the file and replace `your-openai-api-key-here` with your actual API key

#### Option C: Anthropic Claude
1. Get API key from: https://console.anthropic.com/settings/keys
2. Copy `START_WEBSITE_WITH_ANTHROPIC.bat.template` to `START_WEBSITE_WITH_ANTHROPIC.bat`
3. Edit the file and replace `your-anthropic-api-key-here` with your actual API key

#### Option D: Ollama (Free & Local)
1. Download and install Ollama from: https://ollama.com
2. Run: `ollama pull llama3.2`
3. Copy `START_WEBSITE_WITH_OLLAMA.bat.template` to `START_WEBSITE_WITH_OLLAMA.bat`

**Note:** Manual split mode works without any AI provider!

## Usage

### Windows Users
Simply double-click one of the batch files:
- `START_WEBSITE_WITH_DEEPSEEK.bat` (DeepSeek - Cheapest)
- `START_WEBSITE_WITH_AI.bat` (OpenAI)
- `START_WEBSITE_WITH_ANTHROPIC.bat` (Anthropic)
- `START_WEBSITE_WITH_OLLAMA.bat` (Ollama - Free)

### Mac/Linux Users
```bash
# For DeepSeek (cheapest)
export DEEPSEEK_API_KEY="your-api-key-here"
export AI_PROVIDER="deepseek"
python app.py

# For OpenAI
export OPENAI_API_KEY="your-api-key-here"
export AI_PROVIDER="openai"
python app.py

# For Anthropic
export ANTHROPIC_API_KEY="your-api-key-here"
export AI_PROVIDER="anthropic"
python app.py

# For Ollama (free, local)
export AI_PROVIDER="ollama"
python app.py
```

### 2. Use the Application

1. **Upload PDF** in the AI Analysis tab
2. **(Optional)** Ask AI a question like "Split this textbook by chapters"
3. **Click "Analyze with AI"**
4. **Review suggestions** - AI will show 2-3 splitting strategies
5. **Click a suggestion** - Confirm to download

## How Multiple PDF Split Works

When AI suggests splitting with sections (like "By Compound Type"):

```
Suggestion: By Compound Type
├── Anions and Basic Naming (Pages 1-3) → Anions_and_Basic_Naming.pdf
├── Inorganic Compounds (Pages 4-6) → Inorganic_Compounds.pdf
└── Organic Compounds (Pages 7-8) → Organic_Compounds.pdf

Result: Downloads "By_Compound_Type.zip" containing 3 PDFs
```

### Example Workflow

1. Upload: `chemistry_textbook.pdf` (1059 pages)
2. AI suggests:
   - **By Chapters** (15 separate PDFs)
   - **By Units** (5 separate PDFs)
   - **Introduction + Main Content + Appendix** (3 PDFs)
3. Click "By Chapters"
4. Download `By_Chapters.zip`
5. Extract to get 15 PDF files, each named after the chapter

## Cost Comparison

| Provider | Per Analysis | 1000 Analyses | Notes |
|----------|--------------|---------------|-------|
| **DeepSeek** | $0.0001 | $0.10 | 97% cheaper! |
| **Ollama** | FREE | FREE | Runs locally |
| OpenAI | $0.003 | $3.00 | Good quality |
| Claude | $0.003 | $3.00 | Best quality |

## File Structure

```
python_pdf/
├── app.py                          # Main Flask application
├── ai_analyzer.py                  # AI analysis engine
├── templates/
│   └── index.html                  # Web interface
├── START_WEBSITE_WITH_DEEPSEEK.bat # DeepSeek launcher (configured)
├── START_WEBSITE_WITH_AI.bat       # OpenAI launcher (configured)
├── START_WEBSITE_WITH_OLLAMA.bat   # Ollama launcher
├── SETUP_DEEPSEEK.md              # DeepSeek setup guide
├── SETUP_FREE_AI.md               # Ollama setup guide
└── AI_SETUP_GUIDE.md              # Complete AI guide
```

## Features Summary

✅ **AI Analysis** - 4 provider options
✅ **Multiple PDF Output** - Split into separate files
✅ **ZIP Download** - All files in one archive
✅ **Smart Naming** - Files named by section
✅ **Large Files** - Up to 500MB supported
✅ **Manual Mode** - Traditional page selection
✅ **Free Options** - DeepSeek (almost free) or Ollama (totally free)

## Troubleshooting

### "Request Entity Too Large"
- Fixed! Now supports up to 500MB files

### AI Not Working
- Make sure you're using the correct batch file
- DeepSeek: START_WEBSITE_WITH_DEEPSEEK.bat (configured)
- OpenAI: START_WEBSITE_WITH_AI.bat (configured)

### Want Multiple PDFs
- Use suggestions with sections (AI will show "📦 Will create X separate PDF files")
- Downloads as ZIP file
- Extract ZIP to get all PDFs

## Next Steps

1. **Start the website**: Double-click `START_WEBSITE_WITH_DEEPSEEK.bat`
2. **Upload a PDF**: Try your Atkins.pdf
3. **Get AI suggestions**: See intelligent splitting options
4. **Download**: Get single PDF or ZIP with multiple PDFs

Enjoy your AI-powered PDF splitter! 🚀
