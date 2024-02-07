# Image Converter GUI

A large number of image file formats are available for storing graphic data, the most popular being JPG and PNG.

-----

## Installation

```
pip install tkinter pillow
```
Firstly import the `tkinter pillow` library through the terminal that will help in the program.

-----

## Code Break:

```python
import tkinter as tk
from tkinter import filedialog
from PIL import Image
```
Imports the required modules: `tkinter` for GUI, `filedialog` from tkinter to open file dialogs, and `Image` from PIL (Python Imaging Library) to work with images.

```python
root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=250, bg="azure3", relief="raised")
canvas1.pack()
```
Creates the main window (`root`) and a canvas (`canvas1`) within it with specified dimensions and background color.

```python
label1 = tk.Label(root, text="Image Converter", bg="azure3")
label1.config(font=("helvetica", 20))
canvas1.create_window(150, 60, window=label1)
```
Creates a label (`label1`) with text "Image Converter" and places it on the canvas at coordinates (150, 60).

```python
def getPNG():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
```
Defines a function `getPNG()` which opens a file dialog to select a PNG file, stores the selected image using `Image.open()` from PIL, and assigns it to the global variable `im1`.

```python
browse_png = tk.Button(
    text="Select PNG file",
    command=getPNG,
    bg="royalblue",
    fg="white",
    font=("helvetica", 12, "bold"),
)
canvas1.create_window(150, 130, window=browse_png)
```
Creates a button (`browse_png`) labeled "Select PNG file" with a command to execute `getPNG()` when clicked. It's placed on the canvas at coordinates (150, 130).

```python
def convert():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    im1.save(export_file_path)
```
Defines a function `convert()` which opens a file dialog to save the converted image as a JPG file, and saves the image using `Image.save()` from PIL.

```python
saveasbutton = tk.Button(
    text="Convert PNG to JPG",
    command=convert,
    bg="royalblue",
    fg="white",
    font=("helvetica", 12, "bold"),
)
canvas1.create_window(150, 180, window=saveasbutton)
```
Creates a button (`saveasbutton`) labeled "Convert PNG to JPG" with a command to execute `convert()` when clicked. It's placed on the canvas at coordinates (150, 180).

```python
root.mainloop()
```
Starts the Tkinter event loop, which listens for events such as button clicks, window resizing, etc., and keeps the GUI application running until it's explicitly terminated.

-----