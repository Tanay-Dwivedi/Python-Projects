# Weight Converter GUI

Weight conversion means to multiply the value of a unit with the standard conversion value.

The standard weight conversion values include:

- 1 milligram = 0.001 gram
- 1 centigram = 0.01 gram
- 1 decigram = 0.1 gram
- 1 kilogram = 1000 grams
- 1 gram = 1000 milligrams
- 1 ton = 2000 pounds
- 1 pound = 16 ounces

-----

## Installation

```
pip install tkinter
```
Firstly import the `tkinter` library through the terminal that will help in the program.

-----

## Code Break:

```python
from tkinter import *
```
Imports all classes and functions from the `tkinter` module.

```python
window = Tk()
```
Creates a Tkinter window object.

```python
def from_kg():
    gram = float(e2_value.get()) * 1000
    pound = float(e2_value.get()) * 2.20462
    ounce = float(e2_value.get()) * 35.274
    t1.delete("1.0", END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)
```
Defines a function `from_kg()` which calculates the weight in gram, pound, and ounce based on the input value in kilograms provided in the Entry widget `e2`, and displays the results in Text widgets `t1`, `t2`, and `t3`, respectively.

```python
e1 = Label(window, text="Input the weight in KG")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Gram")
e4 = Label(window, text="Pound")
e5 = Label(window, text="Ounce")

t1 = Text(window, height=5, width=30)
t2 = Text(window, height=5, width=30)
t3 = Text(window, height=5, width=30)

b1 = Button(window, text="Convert", command=from_kg)
```
Creates various widgets:
- `e1`: Label for input instruction.
- `e2`: Entry widget to input weight in kilograms.
- `e3`, `e4`, `e5`: Labels for gram, pound, and ounce.
- `t1`, `t2`, `t3`: Text widgets to display the converted weights.
- `b1`: Button to trigger the conversion function `from_kg()`.

```python
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)
```
Arranges the widgets in a grid layout within the window, specifying their positions using the `grid()` method.

```python
window.mainloop()
```
Starts the Tkinter event loop to display the window and handle user interactions until the window is closed.

-----