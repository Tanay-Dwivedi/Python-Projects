# Calculator GUI

I will use the Kivy package in Python to build a Calculator GUI.

Kivy is a free, Open Source Python library that enables the rapid and easy development of highly interactive cross-platform applications. Kivy’s execution speed is the same as compared to the other mobile development alternatives like Java for Android and Objective C for iOS.

-----

## Installation

```
pip install Kivy
```
Firstly import the `Kivy` library through the terminal that will help in the program.

-----

## Code Break:

```python
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
```
These statements import the necessary classes from the Kivy framework for building the application.

```python
class myApp(App):
    def build(self):
        # ... (Building the UI components)
        return root_widget
```
This class inherits from `App` and defines the main application. The `build()` method is called automatically when the application starts. It constructs the UI components, configures their behavior, and returns the root widget of the application.

```python
root_widget = BoxLayout(orientation="vertical")
output_label = Label(size_hint_y=0.75, font_size=50)
button_symbols = (
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", ".",
    "0", "*", "/", "="
)
button_grid = GridLayout(cols=4, size_hint_y=2)
for symbol in button_symbols:
    button_grid.add_widget(Button(text=symbol))
clear_button = Button(text="Clear", size_hint_y=None, height=100)
```
- `root_widget`: A vertical `BoxLayout` serving as the main container for other widgets.
- `output_label`: A `Label` widget to display the output of the calculator.
- `button_grid`: A `GridLayout` containing the calculator buttons arranged in a 4x4 grid.
- `clear_button`: A button to clear the calculator's output.

```python
def print_button_text(instance):
    output_label.text += instance.text

for button in button_grid.children[1:]:
    button.bind(on_press=print_button_text)
```
This function binds the `print_button_text` function to all buttons except the first one. When pressed, these buttons append their respective text to the output label.

```python
def clear_label(instance):
    output_label.text = " "

clear_button.bind(on_press=clear_label)
```
This function binds the `clear_label` function to the clear button. When pressed, it clears the output label.

```python
def evaluate_result(instance):
    try:
        output_label.text = str(eval(output_label.text))
    except SyntaxError:
        output_label.text = "Python Syntax error!"

button_grid.children[0].bind(on_press=evaluate_result)
```
This function binds the `evaluate_result` function to the first button (the equal sign). When pressed, it evaluates the expression in the output label using Python's `eval()` function and displays the result. If there's a syntax error, it displays an error message.

```python
def resize_label_text(label, new_height):
    label.fontsize = 0.5 * label.height

output_label.bind(height=resize_label_text)
```
This function resizes the text of the output label dynamically as the label's height changes.

```python
myApp().run()
```
This line creates an instance of the `myApp` class and starts the Kivy application's main loop, running the application.

-----