#  Calender GUI

To make a calendar GUI application using Tkinter. In this application, User will have to fill the desired year, and the calendar for that specific year will appear through this application.

-----

## Installation

```
pip install tkinter
```
Firstly import the `tkinter` library through the terminal that will help in the program.

-----

## Code Break:

This script creates a simple GUI application using Tkinter to display a calendar for a given year. Let's break it down:

```python
from tkinter import *
import calendar
```
Imports the necessary modules, including `Tk` and `calendar`.

```python
def showCalendar():
    year = int(year_field.get())
    gui = Tk()
    gui.config(background="grey")
    gui.title("Calendar for the year")
    gui.geometry("550x600")
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.grid(row=5, column=1, padx=20)
    gui.mainloop()
```
Defines a function `showCalendar()` which retrieves the year entered by the user from the entry field, creates a new Tkinter window (`gui`), configures its properties such as title, background color, and size, generates the calendar content using `calendar.calendar(year)`, creates a label to display the calendar, and then starts the GUI main loop.

```python
if __name__ == "__main__":
    new = Tk()
    new.config(background="grey")
    new.title("Calendar")
    new.geometry("250x140")
```
Checks if the script is being run as the main program, and if so, creates a new Tkinter window (`new`) for the main calendar application, configures its properties such as title, background color, and size.

```python
    cal = Label(new, text="Calendar", bg="grey", font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg="dark grey")
    year_field = Entry(new)
    button = Button(
        new, text="Show Calendar", fg="black", bg="blue", command=showCalendar
    )

    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    new.mainloop()
```
Creates labels, entry fields, and buttons for the main window (`new`), sets their properties such as text, colors, and fonts, and arranges them in the window using the `grid()` method. The `command=showCalendar` parameter in the `Button` widget associates the `showCalendar()` function with the button. Finally, starts the GUI main loop to display the window.

-----