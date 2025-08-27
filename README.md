# Calaméo Downloader

A Python script to download books from [Calaméo](https://www.calameo.com/) for free by saving each page as an SVG file.

## Features

- Extract image URLs from a Calaméo book using Selenium.
- Automatically download pages as `.svg` or `.svgz`.
- Supports decompression of `.svgz` files.
- Saves all pages in a local folder named `imgs`.
- Works with any publicly accessible Calaméo book.

## Requirements

- Python 3.x
- `selenium`
- `requests`
- `PyMuPDF` (`fitz`) — optional if you later want to create PDFs
- Chrome WebDriver (make sure `chromedriver` is installed and in PATH)

## Usage

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>

2. Install required packages:
   pip install selenium requests PyMuPDF

3. Run the script:
   python G4F.py

4. Enter the URL of the Calaméo book when prompted.
All pages will be saved in the imgs/ folder.
   