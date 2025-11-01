"""
Create a desktop shortcut for the PDF Splitter with custom icon
"""
import os
import winshell
from pathlib import Path

# Get paths
current_dir = Path(__file__).parent.absolute()
desktop = winshell.desktop()

# Create shortcut for DeepSeek version (cheapest AI option)
shortcut_path = os.path.join(desktop, "AI PDF Splitter.lnk")
batch_file = str(current_dir / "START_WEBSITE_WITH_DEEPSEEK.bat")
icon_file = str(current_dir / "pdf_splitter_icon.ico")

# Check if batch file exists
if not os.path.exists(batch_file):
    print("Warning: DeepSeek batch file not found. Creating generic launcher...")
    batch_file = str(current_dir / "START_WEBSITE.bat")

# Create the shortcut
try:
    from win32com.client import Dispatch

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = batch_file
    shortcut.WorkingDirectory = str(current_dir)
    shortcut.IconLocation = icon_file
    shortcut.Description = "AI-Powered PDF Splitter - Smart PDF analysis and splitting tool"
    shortcut.save()

    print(f"[OK] Desktop shortcut created: {shortcut_path}")
    print(f"[OK] Icon: {icon_file}")
    print(f"[OK] Target: {batch_file}")
    print("\nYou can now double-click 'AI PDF Splitter' on your desktop!")

except Exception as e:
    print(f"Error creating shortcut: {e}")
    print("\nAlternative: You can manually create a shortcut:")
    print(f"1. Right-click on: {batch_file}")
    print(f"2. Select 'Create shortcut'")
    print(f"3. Drag shortcut to desktop")
    print(f"4. Right-click shortcut -> Properties -> Change Icon -> Browse to: {icon_file}")
