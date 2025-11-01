# Setup DeepSeek - Super Cheap AI API!

## What is DeepSeek?

DeepSeek is a Chinese AI company offering **extremely affordable** AI API access:

**Cost Comparison:**
- **OpenAI GPT-4**: ~$0.003 per PDF analysis
- **Anthropic Claude**: ~$0.003 per PDF analysis
- **DeepSeek**: ~$0.0001 per PDF analysis (**30x cheaper!**)

**Benefits:**
- ✅ **95% cheaper** than OpenAI/Claude
- ✅ **No downloads** - Cloud-based API
- ✅ **Good quality** - Competitive with GPT-3.5
- ✅ **Fast** - 10-20 second analysis
- ✅ **$5 free credit** for new users

**Trade-offs:**
- Quality slightly lower than GPT-4 or Claude
- Chinese company (data privacy considerations)
- Newer service (less established than OpenAI)

---

## Quick Setup (2 Steps)

### Step 1: Get Your API Key

1. **Go to DeepSeek Platform:**
   - Visit: https://platform.deepseek.com/
   - Click "Sign Up" or "Log In"

2. **Sign up:**
   - Use email or phone
   - Verify your account
   - **Get $5 free credit** (~50,000 PDF analyses!)

3. **Get API Key:**
   - Go to API Keys section
   - Click "Create API Key"
   - Copy your key (starts with `sk-...`)

### Step 2: Use It!

1. **Double-click:** `START_WEBSITE_WITH_DEEPSEEK.bat`
2. **Enter your API key** when prompted
3. **Start analyzing PDFs!**

---

## Cost Analysis

With DeepSeek's incredibly low pricing:

| Usage | OpenAI Cost | DeepSeek Cost | **Savings** |
|-------|-------------|---------------|-------------|
| 10 PDFs | $0.03 | $0.001 | **97%** |
| 100 PDFs | $0.30 | $0.01 | **97%** |
| 1,000 PDFs | $3.00 | $0.10 | **97%** |
| 10,000 PDFs | $30.00 | $1.00 | **97%** |

**With $5 credit, you can analyze ~50,000 PDFs!**

---

## Quality Comparison

**DeepSeek Chat** (their main model):
- **Strength:** Mathematics, coding, logical reasoning
- **Good for:** Technical documents, academic papers, structured content
- **Quality:** Similar to GPT-3.5 Turbo
- **Speed:** Fast (10-20 seconds)

**When to use DeepSeek:**
- ✅ Budget-conscious users
- ✅ High-volume PDF processing
- ✅ Technical/academic documents
- ✅ Testing and development

**When to use OpenAI/Claude:**
- Complex creative writing analysis
- Mission-critical applications
- Highest quality requirements
- Privacy-sensitive documents

---

## Privacy Considerations

**Important to know:**
- DeepSeek is a Chinese AI company
- Data is processed on their servers
- Subject to Chinese data regulations

**Recommendations:**
- ✅ **Use for:** Public documents, academic papers, general content
- ❌ **Avoid for:** Confidential business documents, personal information, sensitive data

**For maximum privacy:** Use Ollama (local, free) instead

---

## How to Switch Between Providers

You can easily switch between AI providers:

**Option 1: Edit Batch File**
- Open `START_WEBSITE_WITH_DEEPSEEK.bat`
- Change `set AI_PROVIDER=deepseek` to:
  - `openai` - Use OpenAI GPT
  - `anthropic` - Use Claude
  - `ollama` - Use local AI (free)

**Option 2: Use Different Batch Files**
- `START_WEBSITE_WITH_DEEPSEEK.bat` - DeepSeek (super cheap)
- `START_WEBSITE_WITH_AI.bat` - OpenAI (configured)
- `START_WEBSITE_WITH_OLLAMA.bat` - Ollama (free, local)

---

## Troubleshooting

### "Invalid API key"
- Make sure you copied the entire key
- Check for extra spaces
- Try regenerating the key

### "Insufficient balance"
- Add credits to your DeepSeek account
- Minimum ~$1 for thousands of analyses

### "Request failed"
- Check your internet connection
- DeepSeek servers might be down (rare)
- Try again in a few minutes

### Analysis quality is poor
- DeepSeek works best on technical/structured documents
- Try rephrasing your question
- Consider using OpenAI/Claude for complex docs

---

## Recommended Usage Strategy

**Best approach for most users:**

1. **Start with DeepSeek** (super cheap)
   - Test with your PDFs
   - See if quality meets your needs
   - Save 97% on costs!

2. **Use Ollama for privacy** (free, local)
   - Install once
   - Unlimited usage
   - No internet needed
   - Perfect for sensitive docs

3. **Reserve OpenAI/Claude for special cases**
   - Very complex documents
   - When highest quality needed
   - Critical business documents

---

## Example: Cost of 1000 PDFs

**Scenario:** Analyzing 1000 technical PDF documents

| Provider | Cost | Quality | Speed |
|----------|------|---------|-------|
| **DeepSeek** | **$0.10** | Good | Fast |
| Ollama | **$0.00** | Good | Medium |
| OpenAI | $3.00 | Excellent | Fast |
| Claude | $3.00 | Excellent | Fast |

**Best choice:** DeepSeek for high volume, Ollama for free unlimited!

---

## Getting Started

1. **Sign up:** https://platform.deepseek.com/
2. **Get $5 credit** (new users)
3. **Copy API key**
4. **Double-click:** `START_WEBSITE_WITH_DEEPSEEK.bat`
5. **Analyze 50,000 PDFs with your free credit!**

Enjoy super cheap AI-powered PDF splitting! 🚀
