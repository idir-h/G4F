import os
import shutil
import cairosvg
from PyPDF2 import PdfMerger
import sys
import time
from UI import input_clignotant

input_folder = "imgs"

def print_progress_bar(iteration, total, length=50):
    percent = int((iteration / total) * 100)
    filled_length = int(length * iteration // total)
    bar = "\\" * filled_length + "-" * (length - filled_length)
    sys.stdout.write(f"\rConverting: \033[91m{bar}\033[0m {percent}%")
    sys.stdout.flush()

def pdf_maker(total_pages):
    while True:
        print("\n\n")
        output_pdf = input_clignotant("Enter the book name (without extension): ").strip()
        if output_pdf != "":
            output_pdf += ".pdf"
            break

    pdf_files = []

    for index in range(1, total_pages + 1):
        svg_path = os.path.join(input_folder, f"p{index}.svg")
        if os.path.exists(svg_path):
            pdf_path = svg_path.replace(".svg", ".pdf")
            cairosvg.svg2pdf(url=svg_path, write_to=pdf_path)
            pdf_files.append(pdf_path)
        print_progress_bar(index, total_pages)
        time.sleep(0.05)

    print("\nFiles converted! Merging PDFs...")

    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output_pdf)
    merger.close()
    if os.path.exists(input_folder):
        shutil.rmtree(input_folder)
    print(f"All files merged into: {output_pdf}")
