"""
AI-Powered PDF Splitter - Desktop Launcher
This script launches the web application and opens it in your default browser.
"""
import os
import sys
import webbrowser
import time
import subprocess
from pathlib import Path

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    print("=" * 60)
    print("AI-POWERED PDF SPLITTER")
    print("=" * 60)
    print()

    # Check if AI provider is configured
    ai_provider = os.getenv('AI_PROVIDER', '').lower()

    if ai_provider:
        print(f"✓ AI Provider: {ai_provider.upper()}")
    else:
        print("ℹ AI Analysis: Not configured (Manual mode only)")
        print("  To enable AI features:")
        print("  1. Get an API key from DeepSeek, OpenAI, or Anthropic")
        print("  2. Set environment variables before running")
        print()

    print("Starting web server...")
    print("Open your browser and go to: http://localhost:5000")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    print()

    # Start the Flask app
    app_path = get_resource_path('app.py')

    # Wait a moment for server to start
    time.sleep(2)

    # Open browser
    webbrowser.open('http://localhost:5000')

    # Import and run the Flask app
    # We need to add the app directory to the path
    app_dir = os.path.dirname(app_path)
    if app_dir not in sys.path:
        sys.path.insert(0, app_dir)

    # Import the Flask app
    try:
        import app as pdf_app
        # The app.py file will run when imported due to its structure
    except Exception as e:
        print(f"Error starting application: {e}")
        print("\nPlease ensure all dependencies are installed:")
        print("pip install -r requirements.txt")
        input("\nPress Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nShutting down server...")
        print("Goodbye!")
