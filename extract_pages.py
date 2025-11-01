"""
Extract Specific Pages from PDF

Simple script to extract specific page numbers from a PDF file.
You can specify individual pages or ranges (e.g., 1, 3, 5-10, 15)
"""

from PyPDF2 import PdfReader, PdfWriter
import os


def extract_pages(input_pdf, output_pdf, page_numbers):
    """
    Extract specific pages from a PDF.

    Args:
        input_pdf: Path to the input PDF file
        output_pdf: Path for the output PDF file
        page_numbers: List of page numbers to extract (1-based)
    """
    # Read the PDF
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()
    total_pages = len(pdf_reader.pages)

    print(f"Total pages in PDF: {total_pages}")
    print(f"Extracting pages: {sorted(page_numbers)}")

    # Add selected pages
    for page_num in sorted(page_numbers):
        if 1 <= page_num <= total_pages:
            # Convert to 0-based index
            pdf_writer.add_page(pdf_reader.pages[page_num - 1])
            print(f"  Added page {page_num}")
        else:
            print(f"  Warning: Page {page_num} doesn't exist (skipped)")

    # Write output file
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

    print(f"\nSuccess! Created '{output_pdf}' with {len(pdf_writer.pages)} pages")


def parse_page_input(page_string):
    """
    Parse page numbers from user input.
    Supports: "1,3,5" or "1-5,8,10-12" format

    Returns:
        List of page numbers
    """
    pages = []
    parts = page_string.replace(" ", "").split(",")

    for part in parts:
        if "-" in part:
            # Handle range (e.g., "5-10")
            try:
                start, end = part.split("-")
                pages.extend(range(int(start), int(end) + 1))
            except:
                print(f"Warning: Invalid range '{part}' (skipped)")
        else:
            # Handle single page
            try:
                pages.append(int(part))
            except:
                print(f"Warning: Invalid page number '{part}' (skipped)")

    return list(set(pages))  # Remove duplicates


if __name__ == "__main__":
    print("=" * 60)
    print("EXTRACT SPECIFIC PAGES FROM PDF")
    print("=" * 60)
    print()

    # Get input PDF
    input_pdf = input("Enter the PDF file path: ").strip().strip('"')

    if not os.path.exists(input_pdf):
        print(f"Error: File '{input_pdf}' not found!")
        input("\nPress Enter to exit...")
        exit()

    # Show total pages
    try:
        pdf_reader = PdfReader(input_pdf)
        total_pages = len(pdf_reader.pages)
        print(f"\nThis PDF has {total_pages} pages.")
    except Exception as e:
        print(f"Error reading PDF: {e}")
        input("\nPress Enter to exit...")
        exit()

    # Get pages to extract
    print("\nWhich pages do you want to extract?")
    print("Examples:")
    print("  - Single pages: 1,3,5")
    print("  - Range: 1-5")
    print("  - Mixed: 1,3,5-10,15")
    print()

    page_input = input("Enter page numbers: ").strip()
    page_numbers = parse_page_input(page_input)

    if not page_numbers:
        print("No valid page numbers entered!")
        input("\nPress Enter to exit...")
        exit()

    # Get output filename
    default_output = os.path.splitext(input_pdf)[0] + "_extracted.pdf"
    output_pdf = input(f"Output filename (default: '{default_output}'): ").strip() or default_output

    # Extract pages
    print("\n" + "-" * 60)
    try:
        extract_pages(input_pdf, output_pdf, page_numbers)
    except Exception as e:
        print(f"Error: {e}")

    print("-" * 60)
    input("\nPress Enter to exit...")
