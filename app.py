"""
PDF Page Extractor Web Application

A Flask web application that allows users to:
1. Upload a PDF file
2. Specify which pages to extract
3. Download the extracted pages as a new PDF
"""

from flask import Flask, render_template, request, send_file, flash, redirect, url_for, jsonify
from PyPDF2 import PdfReader, PdfWriter
import os
from werkzeug.utils import secure_filename
import tempfile
import shutil
import json
from ai_analyzer import PDFAnalyzer

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

# Configuration
UPLOAD_FOLDER = tempfile.gettempdir()
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max file size

# AI Configuration - Set your API key here or as environment variable
AI_PROVIDER = os.getenv('AI_PROVIDER', 'anthropic')  # 'anthropic', 'openai', 'deepseek', or 'ollama'
API_KEY = os.getenv('ANTHROPIC_API_KEY') or os.getenv('OPENAI_API_KEY') or os.getenv('DEEPSEEK_API_KEY')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama3.2')  # Model for Ollama


def allowed_file(filename):
    """Check if file has allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def parse_page_input(page_string):
    """
    Parse page numbers from user input.
    Supports: "1,3,5" or "1-5,8,10-12" format
    Returns list of page numbers
    """
    pages = []
    parts = page_string.replace(" ", "").split(",")

    for part in parts:
        if "-" in part:
            try:
                start, end = part.split("-")
                pages.extend(range(int(start), int(end) + 1))
            except:
                pass
        else:
            try:
                pages.append(int(part))
            except:
                pass

    return sorted(list(set(pages)))  # Remove duplicates and sort


def extract_pdf_pages(input_path, output_path, page_numbers):
    """
    Extract specific pages from a PDF file

    Args:
        input_path: Path to input PDF
        output_path: Path to save extracted PDF
        page_numbers: List of page numbers to extract (1-based)

    Returns:
        Tuple of (success: bool, message: str, pages_extracted: int)
    """
    try:
        pdf_reader = PdfReader(input_path)
        pdf_writer = PdfWriter()
        total_pages = len(pdf_reader.pages)

        extracted_count = 0
        invalid_pages = []

        for page_num in page_numbers:
            if 1 <= page_num <= total_pages:
                pdf_writer.add_page(pdf_reader.pages[page_num - 1])
                extracted_count += 1
            else:
                invalid_pages.append(page_num)

        if extracted_count == 0:
            return False, "No valid pages to extract", 0

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        message = f"Successfully extracted {extracted_count} page(s)"
        if invalid_pages:
            message += f". Invalid pages skipped: {invalid_pages}"

        return True, message, extracted_count

    except Exception as e:
        return False, f"Error processing PDF: {str(e)}", 0


@app.route('/')
def index():
    """Display the main upload form"""
    # AI is enabled if we have an API key OR using Ollama
    ai_enabled = API_KEY is not None or AI_PROVIDER == 'ollama'
    return render_template('index.html', ai_enabled=ai_enabled)


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and page extraction"""

    # Check if file was uploaded
    if 'pdf_file' not in request.files:
        flash('No file uploaded', 'error')
        return redirect(url_for('index'))

    file = request.files['pdf_file']

    # Check if file was selected
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('index'))

    # Check if pages were specified
    page_input = request.form.get('pages', '').strip()
    if not page_input:
        flash('Please specify which pages to extract', 'error')
        return redirect(url_for('index'))

    # Validate file type
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # Create temporary files
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], f"temp_input_{filename}")
        output_filename = f"extracted_{filename}"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

        try:
            # Save uploaded file
            file.save(input_path)

            # Parse page numbers
            page_numbers = parse_page_input(page_input)

            if not page_numbers:
                flash('Invalid page numbers format', 'error')
                os.remove(input_path)
                return redirect(url_for('index'))

            # Extract pages
            success, message, count = extract_pdf_pages(input_path, output_path, page_numbers)

            if success:
                # Send file and clean up
                response = send_file(
                    output_path,
                    as_attachment=True,
                    download_name=output_filename,
                    mimetype='application/pdf'
                )

                # Clean up temp files after sending
                @response.call_on_close
                def cleanup():
                    try:
                        os.remove(input_path)
                        os.remove(output_path)
                    except:
                        pass

                return response
            else:
                flash(message, 'error')
                os.remove(input_path)
                return redirect(url_for('index'))

        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            # Clean up files
            try:
                if os.path.exists(input_path):
                    os.remove(input_path)
                if os.path.exists(output_path):
                    os.remove(output_path)
            except:
                pass
            return redirect(url_for('index'))

    else:
        flash('Invalid file type. Please upload a PDF file.', 'error')
        return redirect(url_for('index'))


@app.route('/analyze', methods=['POST'])
def analyze_pdf():
    """Analyze PDF content with AI and return splitting suggestions"""

    # Check if AI is available
    if AI_PROVIDER != 'ollama' and not API_KEY:
        return jsonify({
            "error": "AI analysis is not configured. Please set ANTHROPIC_API_KEY, OPENAI_API_KEY, or use Ollama."
        }), 400

    # Check if file was uploaded
    if 'pdf_file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['pdf_file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], f"temp_analyze_{filename}")

        try:
            # Save uploaded file
            file.save(input_path)

            # Get user's question if any
            user_question = request.form.get('question', '').strip()

            # Initialize AI analyzer
            analyzer = PDFAnalyzer(
                api_key=API_KEY,
                provider=AI_PROVIDER,
                ollama_model=OLLAMA_MODEL
            )

            # Extract PDF text
            pdf_data = analyzer.extract_text_from_pdf(input_path, max_pages=30)

            # Analyze with AI
            analysis = analyzer.analyze_with_ai(pdf_data, user_question)

            # Clean up
            os.remove(input_path)

            return jsonify(analysis)

        except Exception as e:
            # Clean up on error
            try:
                if os.path.exists(input_path):
                    os.remove(input_path)
            except:
                pass

            return jsonify({"error": f"Analysis failed: {str(e)}"}), 500

    else:
        return jsonify({"error": "Invalid file type"}), 400


@app.route('/split-multiple', methods=['POST'])
def split_multiple():
    """Split PDF into multiple files based on sections"""

    if 'pdf_file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['pdf_file']
    sections_json = request.form.get('sections', '[]')

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    try:
        sections = json.loads(sections_json)
        print(f"DEBUG: Received {len(sections)} sections: {sections}")  # Debug
    except Exception as e:
        print(f"DEBUG: JSON parse error: {e}")  # Debug
        return jsonify({"error": "Invalid sections data"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], f"temp_split_{filename}")

        try:
            # Save uploaded file
            file.save(input_path)

            # Create output folder
            import uuid
            import zipfile
            from io import BytesIO

            zip_buffer = BytesIO()
            files_created = 0

            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                pdf_reader = PdfReader(input_path)

                for section in sections:
                    print(f"DEBUG: Processing section: {section}")  # Debug
                    section_name = section.get('name', 'Section')
                    page_range = section.get('pages', '')

                    # Parse page range
                    page_numbers = parse_page_input(page_range)

                    if page_numbers:
                        # Create PDF for this section
                        pdf_writer = PdfWriter()

                        for page_num in page_numbers:
                            if 1 <= page_num <= len(pdf_reader.pages):
                                pdf_writer.add_page(pdf_reader.pages[page_num - 1])

                        # Write to bytes
                        pdf_bytes = BytesIO()
                        pdf_writer.write(pdf_bytes)
                        pdf_bytes.seek(0)

                        # Add to zip
                        safe_name = section_name.replace('/', '_').replace('\\', '_')
                        zip_file.writestr(f"{safe_name}.pdf", pdf_bytes.read())

            # Clean up input file
            os.remove(input_path)

            # Send zip file
            zip_buffer.seek(0)
            return send_file(
                zip_buffer,
                mimetype='application/zip',
                as_attachment=True,
                download_name=f"split_{os.path.splitext(filename)[0]}.zip"
            )

        except Exception as e:
            # Clean up on error
            try:
                if os.path.exists(input_path):
                    os.remove(input_path)
            except:
                pass

            return jsonify({"error": f"Split failed: {str(e)}"}), 500

    else:
        return jsonify({"error": "Invalid file type"}), 400


if __name__ == '__main__':
    print("=" * 60)
    print("PDF PAGE EXTRACTOR WEB APPLICATION")
    print("=" * 60)
    print("\nStarting server...")
    print("Open your browser and go to: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 60)
    app.run(debug=True, port=5000)
