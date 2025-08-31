# 📖 G4F  

**G4F** is a Python program that allows you to **download books from Calaméo for free**.  
The script automatically saves each page in **SVG format**, then converts all pages into a **single PDF file** for easy offline reading.  
 

---

The project is modular and organized into three main components:  
- `UI.py` → manages the user interface (messages, colors, blinking cursor).  
- `imgs_downloader.py` → handles image extraction and downloading from a given URL.  
- `pdf_maker.py` → converts the downloaded images into a single PDF.  

---

## 🚀 Features 

-  Download full books from Calaméo by simply providing the URL  
-  Save pages in **SVG** format for best quality  
-  Automatically merge all pages into a **clean, single PDF file**  
-  Temporary files are cleaned up after PDF generation  
-  Simple to use with a professional terminal interface 

---

## 🛠️ Requirements  
Make sure you have installed:  

- Python 3.8+  
- Google Chrome  
- ChromeDriver (compatible with your Chrome version)  
- Python packages:  

  ```bash
  pip install selenium requests fitz PyMuPDF colorama
  
## 📂 Project Structure  
   ```bash
   ├── UI.py               # Handles the terminal user interface (progress bar, messages, cursor, etc.)  
   ├── imgs_downloader.py  # Downloads images from a given URL  
   ├── pdf_maker.py        # Converts images into a PDF  
   ├── main.py             # Main entry point of the program  
   └── README.md           # Project documentation
   ```
## ▶️ Usage  

Installation:

```bash
git clone https://github.com/idir-h/G4F.git
cd G4F
```

![Image](https://github.com/user-attachments/assets/bc9112a4-1421-493e-a1d4-0909bacac5e1)
Run the program with:  

```bash
python ./G4F.py
```
