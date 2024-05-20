# Image Text Bulk Renamer

This tool is designed to bulk rename image files based on the text extracted from the images using optical character recognition (OCR). It provides a graphical user interface (GUI) for easy interaction.

## Features

- Select a directory containing images.
- Extract text from supported image formats using EasyOCR.
- Clean extracted text to create valid filenames.
- Generate unique filenames to avoid duplicates.
- Rename image files based on the extracted text.

## Installation

1. **Python**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Tkinter**: Tkinter is a standard Python library for GUI. It is usually included with Python installations. If you encounter any issues, refer to the [official documentation](https://docs.python.org/3/library/tkinter.html).

3. **easyocr**: Install the EasyOCR library using pip:

   ```bash
   pip install easyocr
   ```

## How to Run

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Hyperion-IT-Cyber-Consulting/ImageTextBulkRenamer.git
   ```

2. Navigate to the cloned directory:

   ```bash
   cd ImageTextBulkRenamer
   ```

3. Run the script:

   ```bash
   python bulk_renamer.py
   ```

4. The GUI will open. Follow the on-screen instructions to select a directory, choose whether to use GPU for processing, and start the renaming process.

## Note

- Supported image formats for text extraction: PNG, JPG, JPEG, TIFF, BMP, GIF.
