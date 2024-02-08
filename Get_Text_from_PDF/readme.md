# Extract Text from PDF

The biggest challenge we face while we extract text from PDF file is that PDF files come in different file formats. So first we need to prepare a function so that we can convert every format of a PDF file into our desired one.

-----

## Installation

```
pip install pdf2image Pillow pytesseract
```
Firstly import the `pdf2image Pillow pytesseract` library through the terminal that will help in the program.

-----

## Code Break:

```python
import pdf2image
import os, sys

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
```
We import necessary modules: `pdf2image` for converting PDFs to images, `os` and `sys` for file operations, `PIL` (Python Imaging Library) or `Image` from `Pillow` for image processing, and `pytesseract` for text recognition (OCR).

```python
PATH = "Enter your path"

i = 1
```
We define the path where the PDF files are located and initialize a variable `i` to keep track of the file number.

```python
def delete_ppms():
    for file in os.listdir(PATH):
        if ".ppm" in file or ".DS_Store" in file:
            try:
                os.remove(PATH + file)
            except FileNotFoundError:
                pass
```
We define a function `delete_ppms()` to delete any `.ppm` files or `.DS_Store` files in the directory.

```python
pdf_files = []
docx_files = []

for f in os.listdir(PATH):
    full_name = os.path.join(PATH, f)
    if os.path.isfile(full_name):
        name = os.path.basename(f)
        filename, ext = os.path.splitext(name)
        if ext == ".pdf":
            pdf_files.append(name)
        elif ext == (".docx"):
            docx_files.append(name)
```
We loop through the files in the directory and categorize them into `pdf_files` and `docx_files` based on their extensions.

```python
def pdf_extract(file, i):
    print("extracting from file:", file)
    delete_ppms()
    images = pdf2image.convert_from_path(PATH + file, output_folder=PATH)
    j = 0
    for file in sorted(os.listdir(PATH)):
        if ".ppm" in file and "image" not in file:
            os.rename(PATH + file, PATH + "image" + str(i) + "-" + str(j) + ".ppm")
            j += 1
    j = 0
    f = open(PATH + "result{}.txt".format(i), "w")
    files = [f for f in os.listdir(PATH) if ".ppm" in f]

    for file in sorted(files, key=lambda x: int(x[x.index("-") + 1 : x.index(".")])):
        temp = pytesseract.image_to_string(Image.open(PATH + file))
        f.write(temp)
    f.close()
```
We define a function `pdf_extract()` to extract text from PDF files. It converts each page of the PDF to images, then uses OCR to extract text from the images, and finally writes the extracted text to a text file.

```python
for i in range(len(pdf_files)):
    pdf_file = pdf_files[i]
    pdf_extract(pdf_file, i)
```
We loop through each PDF file in the `pdf_files` list and call the `pdf_extract()` function to extract text from each PDF file.

Overall, this script extracts text from PDF files using OCR and saves the extracted text in separate text files.

-----