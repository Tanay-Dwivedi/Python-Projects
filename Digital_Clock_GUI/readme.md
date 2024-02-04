# Digital Clock GUI

The great part of creating your own GUI apps is that you can customize them however you want. From text font to background colour, all features are available for customization.

-----

## Installation

```
pip install tkinter
```
Firstly import the `tkinter` library through the terminal that will help in the program.

-----

## Code Break:

```python
from tkinter import Label, Tk
import time
```

Imports necessary modules from the `tkinter` library and the `time` module.

```python
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1, 1)
```

Creates the main application window with a title, size, and resizable options.

```python
text_font = ("Boulder", 68, "bold")
background = "#f2e750"
foreground = "#363529"
border_width = 25
```

Defines the font style, background color, foreground color, and border width for the digital clock.

```python
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)
```

Creates a label widget for displaying the digital clock. Sets the font, background color, foreground color, and border width. Places the label in the window using the `grid` method.

```python
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)
```

Defines a function `digital_clock` that updates the label text with the current time in the format HH:MM:SS. The `after` method is used to call the `digital_clock` function every 200 milliseconds, creating a continuous update.

```python
digital_clock()
app_window.mainloop()
```

Calls the `digital_clock` function to start the clock, and then starts the main event loop using `app_window.mainloop()`. The window will continuously update with the current time.

-----