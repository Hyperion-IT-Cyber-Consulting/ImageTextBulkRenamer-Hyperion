import os
import tkinter as tk
from tkinter import filedialog, messagebox
import easyocr
import re

# Function to extract text from an image using EasyOCR
def extract_text_from_image(image_path, use_gpu):
    reader = easyocr.Reader(['en'], gpu=use_gpu)  # Initialize the EasyOCR reader with GPU or CPU
    result = reader.readtext(image_path, detail=0)  # Extract text without coordinates
    return ' '.join(result).strip()

# Function to clean the extracted text to make it a valid filename
def clean_filename(filename):
    # Define a regex pattern to match invalid characters
    invalid_chars = r'[<>:"/\\|?*]'
    # Replace invalid characters with an underscore
    return re.sub(invalid_chars, '_', filename)

# Function to generate a unique filename if a file with the same name already exists
def generate_unique_filename(directory, filename, extension):
    base_name = filename
    counter = 2
    new_filename = f"{base_name}{extension}"
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base_name} (v{counter}){extension}"
        counter += 1
    return new_filename

# Function to rename files based on extracted text
def rename_files_in_directory(directory, use_gpu):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            image_path = os.path.join(directory, filename)
            extracted_text = extract_text_from_image(image_path, use_gpu)
            if extracted_text:
                cleaned_text = clean_filename(extracted_text)
                new_filename = generate_unique_filename(directory, cleaned_text, os.path.splitext(filename)[1])
                new_file_path = os.path.join(directory, new_filename)
                try:
                    os.rename(image_path, new_file_path)
                except OSError as e:
                    print(f"Error renaming file '{filename}' to '{new_filename}': {e}. Skipping...")
                    continue
    messagebox.showinfo("Complete", "All files have been renamed successfully!")

# Function to open a directory dialog
def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_label.config(text=f"Selected Directory: {directory}")
        start_button.config(state=tk.NORMAL)
        return directory
    else:
        directory_label.config(text="No directory selected")
        start_button.config(state=tk.DISABLED)
        return None

# Function to start the renaming process
def start_renaming():
    directory = directory_label.cget("text").replace("Selected Directory: ", "")
    use_gpu = gpu_var.get()
    if directory and os.path.isdir(directory):
        rename_files_in_directory(directory, use_gpu)
        complete_label.config(text="Renaming Complete!")
    else:
        messagebox.showerror("Error", "Please select a valid directory.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Bulk Renamer for Images with Text")

# Create and place the header
header = tk.Label(root, text="Bulk Renamer for Images with Text", font=("Helvetica", 16))
header.pack(pady=10)

# Create and place the description
description = tk.Label(root, text="Takes the text in an image and renames the file to the word found in the image.")
description.pack(pady=5)

# Create and place the button to select the directory
select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack(pady=10)

# Create and place the label to show the selected directory
directory_label = tk.Label(root, text="No directory selected")
directory_label.pack(pady=5)

# Create and place the GPU/CPU selection checkbox
gpu_var = tk.BooleanVar(value=True)
gpu_checkbox = tk.Checkbutton(root, text="Use GPU for processing", variable=gpu_var)
gpu_checkbox.pack(pady=5)

# Create and place the button to start the renaming process
start_button = tk.Button(root, text="Start Renaming", command=start_renaming, state=tk.DISABLED)
start_button.pack(pady=10)

# Create and place the label to show the completion status
complete_label = tk.Label(root, text="")
complete_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
