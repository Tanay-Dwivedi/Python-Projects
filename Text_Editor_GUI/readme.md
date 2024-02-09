# Text Editor GUI

To create a text editor GUI with Python that can create, open, edit, and save text files. We need three important widgets to create the desired text editor GUI with Python; 2 button widgets to save and close, and a text box widget to create and edit text files.

-----

## Installation

```
pip install tkinter
```
Firstly import the `tkinter` library through the terminal that will help in the program.

-----

## Code Break:

```python
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
```
These lines import the necessary modules from Tkinter for creating the GUI window (`tkinter`) and for opening and saving files (`tkinter.filedialog`).

```python
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Thecleverprogrammer - {filepath}")
```
This function `open_file()` is defined to handle the opening of a file. It uses `askopenfilename()` to open a file dialog where the user can select a file to open. If a file is selected, its contents are read and displayed in the text editor widget (`txt_edit`). The title of the window is updated to reflect the name of the opened file.

```python
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Thecleverprogrammer - {filepath}")
```
This function `save_file()` is defined to handle the saving of the current content in the text editor. It uses `asksaveasfilename()` to open a file dialog where the user can specify the file name and location to save the text. The title of the window is updated to reflect the name of the saved file.

```python
window = tk.Tk()
window.title("Thecleverprogrammer")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
```
These lines create the main Tkinter window (`window`) with the title "Thecleverprogrammer". They also configure the resizing behavior of the window, ensuring that the text editor widget inside it can expand properly.

```python
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
```
These lines create the text editor widget (`txt_edit`) and the frame (`fr_buttons`) to hold buttons for opening and saving files. Two buttons (`btn_open` and `btn_save`) are created with appropriate labels and associated commands (`open_file` and `save_file`, respectively). The buttons are then placed inside the frame, and the frame and text editor are positioned within the main window using the `grid()` geometry manager.

```python
window.mainloop()
```
This line starts the Tkinter event loop, which listens for user actions and updates the GUI accordingly. It keeps the GUI window open until the user closes it.

-----