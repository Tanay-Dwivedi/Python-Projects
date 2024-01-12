# Extract Text from PDF

This Python code uses the PyPDF2 library to open a specified PDF file, extract the text from its first page, and print it. It provides a simple demonstration of how to work with PDF files in Python, specifically focusing on extracting textual content from the initial page.

-----

## Installation

```
pip install pypdf2
```
Firstly import the `pypdf2` library through the terminal that will help in the program.

-----

## Code Break:

```python
# Import the PyPDF2 module for working with PDF files
import PyPDF2
```

This line imports the `PyPDF2` module, which provides functionalities for working with PDF files.

```python
# Open the specified PDF file in binary mode ("rb")
pdf = open("<your file name.pdf>", "rb")
```

Here, it opens a PDF file specified by `<your file name.pdf>` in binary mode ("rb"). You should replace `<your file name.pdf>` with the actual name or path of the PDF file you want to work with.

```python
# Create a PdfReader object from the opened PDF file
reader = PyPDF2.PdfReader(pdf)
```

This line creates a `PdfReader` object called `reader` from the opened PDF file. The `PdfReader` class is part of the `PyPDF2` module and is used for reading PDF files.

```python
# Get the first page of the PDF document
page = reader.pages[0]
```

Here, it retrieves the first page of the PDF document using the `pages` attribute of the `PdfReader` object and stores it in the variable `page`. Note that indexing starts from 0, so `[0]` refers to the first page.

```python
# Extract and print the text content of the first page
print(page.extract_text())
```

Finally, this line extracts the text content from the first page using the `extract_text()` method of the `page` object and prints it to the console. This can be useful for extracting information from a PDF document, such as text-based data.

-----