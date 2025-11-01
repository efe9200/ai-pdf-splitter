"""
PDF Splitter - Split a PDF file into multiple files

This script allows you to split a PDF in different ways:
1. Split into individual pages (one page per file)
2. Split into chunks of N pages
3. Extract specific page ranges
"""

from PyPDF2 import PdfReader, PdfWriter
import os


def split_by_pages(input_pdf, output_folder, pages_per_file=1):
    """
    Split a PDF into multiple files with specified pages per file.

    Args:
        input_pdf: Path to the input PDF file
        output_folder: Folder where split PDFs will be saved
        pages_per_file: Number of pages in each output file (default: 1)
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the PDF
    pdf_reader = PdfReader(input_pdf)
    total_pages = len(pdf_reader.pages)

    print(f"Total pages in PDF: {total_pages}")
    print(f"Splitting into files with {pages_per_file} page(s) each...\n")

    # Split the PDF
    file_number = 1
    for page_num in range(0, total_pages, pages_per_file):
        pdf_writer = PdfWriter()

        # Add pages to the current output file
        end_page = min(page_num + pages_per_file, total_pages)
        for page in range(page_num, end_page):
            pdf_writer.add_page(pdf_reader.pages[page])

        # Create output filename
        base_name = os.path.splitext(os.path.basename(input_pdf))[0]
        output_filename = f"{base_name}_part_{file_number}.pdf"
        output_path = os.path.join(output_folder, output_filename)

        # Write the output file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f"Created: {output_filename} (pages {page_num + 1}-{end_page})")
        file_number += 1

    print(f"\nDone! Created {file_number - 1} files in '{output_folder}'")


def extract_page_range(input_pdf, output_pdf, start_page, end_page):
    """
    Extract a specific range of pages from a PDF.

    Args:
        input_pdf: Path to the input PDF file
        output_pdf: Path for the output PDF file
        start_page: First page to extract (1-based)
        end_page: Last page to extract (1-based, inclusive)
    """
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()

    total_pages = len(pdf_reader.pages)

    # Validate page numbers
    if start_page < 1 or end_page > total_pages or start_page > end_page:
        print(f"Invalid page range! PDF has {total_pages} pages.")
        return

    # Add selected pages (convert to 0-based index)
    for page_num in range(start_page - 1, end_page):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    # Write output file
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

    print(f"Extracted pages {start_page}-{end_page} to '{output_pdf}'")


if __name__ == "__main__":
    print("=" * 60)
    print("PDF SPLITTER")
    print("=" * 60)
    print("\nChoose an option:")
    print("1. Split into individual pages (one page per file)")
    print("2. Split into chunks of N pages")
    print("3. Extract specific page range")
    print()

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        input_pdf = input("Enter the PDF file path: ").strip().strip('"')
        output_folder = input("Enter output folder (default: 'split_output'): ").strip() or "split_output"
        split_by_pages(input_pdf, output_folder, pages_per_file=1)

    elif choice == "2":
        input_pdf = input("Enter the PDF file path: ").strip().strip('"')
        pages_per_file = int(input("How many pages per file? ").strip())
        output_folder = input("Enter output folder (default: 'split_output'): ").strip() or "split_output"
        split_by_pages(input_pdf, output_folder, pages_per_file=pages_per_file)

    elif choice == "3":
        input_pdf = input("Enter the PDF file path: ").strip().strip('"')
        start_page = int(input("Start page number: ").strip())
        end_page = int(input("End page number: ").strip())
        output_pdf = input("Enter output PDF filename: ").strip()
        extract_page_range(input_pdf, output_pdf, start_page, end_page)

    else:
        print("Invalid choice!")

    print("\nPress Enter to exit...")
    input()
