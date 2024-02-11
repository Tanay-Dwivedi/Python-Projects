# Analog Clock

Python provides Tkinter to develop GUI applications. Now, it’s upto the skills and imagination of the developer, what he want to develop using tkinter.

-----

## Installation

```
pip install tkinter
```
Firstly import the `tkinter` library through the terminal that will help in the program.

-----

## Code Break:

```python
try:
    import Tkinter
except:
    import tkinter as Tkinter
```
This block of code imports the `Tkinter` module and falls back to `tkinter` (with lowercase 't') if importing `Tkinter` fails. This ensures compatibility with both Python 2 and Python 3.

```python
import math
import time
```
Imports the `math` module for mathematical operations and the `time` module for time-related functions.

```python
class main(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.x = 150
        self.y = 150
        self.length = 50
        self.creating_all_function_trigger()
```
Defines a class `main` which inherits from `Tkinter.Tk`. Initializes the window with a fixed size and sets the initial coordinates and length for drawing clock hands. Calls the `creating_all_function_trigger()` method to set up the clock.

```python
def creating_all_function_trigger(self):
    self.create_canvas_for_shapes()
    self.creating_background_()
    self.creating_sticks()
    return
```
Defines a method to trigger all necessary functions for setting up the clock.

```python
def creating_background_(self):
    self.image = Tkinter.PhotoImage(file="clock.gif")
    self.canvas.create_image(150, 150, image=self.image)
    return
```
Defines a method to create the background of the clock using an image file named "clock.gif".

```python
def create_canvas_for_shapes(self):
    self.canvas = Tkinter.Canvas(self, bg="black")
    self.canvas.pack(expand="yes", fill="both")
    return
```
Defines a method to create a canvas widget for drawing clock hands.

```python
def creating_sticks(self):
    self.sticks = []
    for i in range(3):
        store = self.canvas.create_line(
            self.x,
            self.y,
            self.x + self.length,
            self.y + self.length,
            width=2,
            fill="red",
        )
        self.sticks.append(store)
    return
```
Defines a method to create clock hands using lines on the canvas.

```python
def update_class(self):
    now = time.localtime()
    t = time.strptime(str(now.tm_hour), "%H")
    hour = int(time.strftime("%I", t)) * 5
    now = (hour, now.tm_min, now.tm_sec)
    for n, i in enumerate(now):
        x, y = self.canvas.coords(self.sticks[n])[0:2]
        cr = [x, y]
        cr.append(
            self.length * math.cos(math.radians(i * 6) - math.radians(90)) + self.x
        )
        cr.append(
            self.length * math.sin(math.radians(i * 6) - math.radians(90)) + self.y
        )
        self.canvas.coords(self.sticks[n], tuple(cr))
    return
```
Defines a method to update the clock hands based on the current time. It calculates the angles for hour, minute, and second hands and updates their positions accordingly.

```python
if __name__ == "__main__":
    root = main()

    while True:
        root.update()
        root.update_idletasks()
        root.update_class()
```
Creates an instance of the `main` class and enters a loop to continuously update the clock hands based on the current time. The `update()` and `update_idletasks()` methods are called to update the Tkinter window and its widgets.

-----