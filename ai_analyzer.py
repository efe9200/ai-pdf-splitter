"""
AI-Powered PDF Content Analyzer

This module uses AI to analyze PDF content and provide intelligent
splitting recommendations based on document structure.

Supports:
- Anthropic Claude (cloud, paid)
- OpenAI GPT (cloud, paid)
- DeepSeek (cloud, very cheap!)
- Ollama (local, free!)
"""

import pdfplumber
from anthropic import Anthropic
from openai import OpenAI
import os
import json
import requests


class PDFAnalyzer:
    """Analyzes PDF content using AI to suggest intelligent splitting strategies"""

    def __init__(self, api_key=None, provider="anthropic", ollama_model="llama3.2"):
        """
        Initialize the PDF Analyzer

        Args:
            api_key: API key for the AI provider (not needed for ollama)
            provider: "anthropic", "openai", "deepseek", or "ollama"
            ollama_model: Model name for Ollama (default: llama3.2)
        """
        self.provider = provider.lower()
        self.ollama_model = ollama_model
        self.api_key = api_key

        if self.provider == "ollama":
            self.client = None  # Ollama uses REST API
            self.ollama_url = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        elif self.provider == "anthropic":
            self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
            self.client = Anthropic(api_key=self.api_key) if self.api_key else None
        elif self.provider == "deepseek":
            self.api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
            # DeepSeek uses OpenAI-compatible API
            self.client = OpenAI(
                api_key=self.api_key,
                base_url="https://api.deepseek.com"
            ) if self.api_key else None
        else:  # openai
            self.api_key = api_key or os.getenv("OPENAI_API_KEY")
            self.client = OpenAI(api_key=self.api_key) if self.api_key else None

    def extract_text_from_pdf(self, pdf_path, max_pages=50):
        """
        Extract text content from PDF with page information

        Args:
            pdf_path: Path to the PDF file
            max_pages: Maximum number of pages to analyze (to save on API costs)

        Returns:
            dict with page_count and page_contents
        """
        page_contents = []

        try:
            with pdfplumber.open(pdf_path) as pdf:
                total_pages = len(pdf.pages)
                pages_to_analyze = min(max_pages, total_pages)

                for i, page in enumerate(pdf.pages[:pages_to_analyze]):
                    text = page.extract_text() or ""
                    page_contents.append({
                        "page_number": i + 1,
                        "text": text[:2000],  # Limit text per page to save tokens
                        "char_count": len(text)
                    })

                return {
                    "total_pages": total_pages,
                    "analyzed_pages": pages_to_analyze,
                    "page_contents": page_contents
                }

        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")

    def analyze_with_ai(self, pdf_data, user_question=None):
        """
        Use AI to analyze PDF content and suggest splitting strategies

        Args:
            pdf_data: Dictionary containing page contents from extract_text_from_pdf
            user_question: Optional specific question from user about how to split

        Returns:
            dict with analysis results and splitting suggestions
        """
        # Build the analysis prompt
        prompt = self._build_analysis_prompt(pdf_data, user_question)

        try:
            if self.provider == "ollama":
                # Use Ollama local AI
                ai_response = self._call_ollama(prompt)

            elif self.provider == "anthropic":
                if not self.client:
                    return {"error": "No Anthropic API key configured", "suggestions": []}

                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=2000,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                ai_response = response.content[0].text

            elif self.provider == "deepseek":
                if not self.client:
                    return {"error": "No DeepSeek API key configured", "suggestions": []}

                response = self.client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that analyzes PDF documents and suggests how to split them intelligently."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=2000
                )
                ai_response = response.choices[0].message.content

            else:  # OpenAI
                if not self.client:
                    return {"error": "No OpenAI API key configured", "suggestions": []}

                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that analyzes PDF documents and suggests how to split them intelligently."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=2000
                )
                ai_response = response.choices[0].message.content

            # Parse the AI response
            return self._parse_ai_response(ai_response, pdf_data["total_pages"])

        except Exception as e:
            return {
                "error": f"AI analysis failed: {str(e)}",
                "suggestions": []
            }

    def _call_ollama(self, prompt):
        """Call Ollama REST API for local AI inference"""
        try:
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.ollama_model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120  # 2 minutes timeout for local processing
            )

            if response.status_code == 200:
                return response.json().get("response", "")
            else:
                raise Exception(f"Ollama error: {response.status_code} - {response.text}")

        except requests.exceptions.ConnectionError:
            raise Exception("Cannot connect to Ollama. Make sure Ollama is running. Install from https://ollama.com")
        except requests.exceptions.Timeout:
            raise Exception("Ollama request timed out. Try a smaller PDF or restart Ollama.")
        except Exception as e:
            raise Exception(f"Ollama error: {str(e)}")

    def _build_analysis_prompt(self, pdf_data, user_question):
        """Build the prompt for AI analysis"""

        # Create a summary of the PDF
        page_summaries = []
        for page in pdf_data["page_contents"][:20]:  # Limit to first 20 pages
            preview = page["text"][:300].replace("\n", " ")
            page_summaries.append(f"Page {page['page_number']}: {preview}...")

        prompt = f"""I have a PDF document with {pdf_data['total_pages']} total pages. I need help deciding how to split it into smaller, logical sections.

Here's a preview of the first pages:

{chr(10).join(page_summaries)}

"""

        if user_question:
            prompt += f"\nUser's specific question: {user_question}\n"

        prompt += """
Please analyze this document and provide:

1. **Document Type**: What type of document is this? (e.g., textbook, report, manual, article collection)

2. **Content Structure**: Describe the structure (e.g., chapters, sections, topics)

3. **Splitting Suggestions**: Provide 2-3 specific recommendations for how to split this PDF. For each suggestion:
   - Describe the splitting strategy
   - List the specific page ranges
   - Explain why this split makes sense

Format your response as JSON:
{
  "document_type": "type here",
  "structure": "structure description",
  "suggestions": [
    {
      "name": "Suggestion name",
      "description": "Why this split makes sense",
      "page_ranges": "1-10,11-25,26-50",
      "sections": [
        {"name": "Section 1 name", "pages": "1-10"},
        {"name": "Section 2 name", "pages": "11-25"}
      ]
    }
  ]
}
"""

        return prompt

    def _parse_ai_response(self, ai_response, total_pages):
        """Parse the AI response and extract structured suggestions"""

        try:
            # Try to extract JSON from the response
            start = ai_response.find('{')
            end = ai_response.rfind('}') + 1

            if start >= 0 and end > start:
                json_str = ai_response[start:end]
                parsed = json.loads(json_str)
                return parsed
            else:
                # Fallback: return raw response
                return {
                    "document_type": "Unknown",
                    "structure": "Could not parse structure",
                    "raw_response": ai_response,
                    "suggestions": []
                }

        except json.JSONDecodeError:
            return {
                "document_type": "Unknown",
                "structure": "Could not parse structure",
                "raw_response": ai_response,
                "suggestions": []
            }

    def get_quick_summary(self, pdf_path):
        """
        Get a quick summary of the PDF without AI analysis

        Args:
            pdf_path: Path to PDF file

        Returns:
            dict with basic PDF information
        """
        try:
            with pdfplumber.open(pdf_path) as pdf:
                total_pages = len(pdf.pages)

                # Get first page text
                first_page_text = pdf.pages[0].extract_text()[:500] if total_pages > 0 else ""

                return {
                    "total_pages": total_pages,
                    "first_page_preview": first_page_text,
                    "file_size_mb": os.path.getsize(pdf_path) / (1024 * 1024)
                }
        except Exception as e:
            return {
                "error": f"Could not read PDF: {str(e)}"
            }


def analyze_pdf(pdf_path, user_question=None, api_key=None, provider="anthropic"):
    """
    Convenience function to analyze a PDF in one call

    Args:
        pdf_path: Path to PDF file
        user_question: Optional user question about splitting
        api_key: API key for AI provider
        provider: "anthropic" or "openai"

    Returns:
        Analysis results
    """
    analyzer = PDFAnalyzer(api_key=api_key, provider=provider)

    # Extract text
    pdf_data = analyzer.extract_text_from_pdf(pdf_path)

    # Analyze with AI
    results = analyzer.analyze_with_ai(pdf_data, user_question)

    # Add page count to results
    results["total_pages"] = pdf_data["total_pages"]

    return results


if __name__ == "__main__":
    # Test the analyzer
    import sys

    if len(sys.argv) < 2:
        print("Usage: python ai_analyzer.py <pdf_file> [question]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    question = sys.argv[2] if len(sys.argv) > 2 else None

    print("Analyzing PDF with AI...")
    results = analyze_pdf(pdf_path, question)

    print("\n" + "=" * 60)
    print("ANALYSIS RESULTS")
    print("=" * 60)
    print(json.dumps(results, indent=2))
