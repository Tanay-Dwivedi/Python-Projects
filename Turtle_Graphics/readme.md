# Turtle Graphics

Originally, the turtle was just a physical object, like a robot that can be placed on a sheet of paper and instructed to move. Then the turtle became a visual display on a high-resolution screen, often depicted as any type of shape.

-----

## Installation

```
pip install turtle
```
Firstly import the `turtle` library through the terminal that will help in the program.

-----

## Code Break:

The provided code is a Python script that uses the turtle graphics library to draw a fractal tree pattern with multiple branches of different colors. Let's break down the code:

```python
import turtle as tu
```
This line imports the turtle graphics library and renames it to `tu` for convenience.

```python
roo = tu.Turtle()  # Turtle object
wn = tu.Screen()  # Screen Object
wn.bgcolor("black")  # Screen Bg color
wn.title("Fractal Tree Pattern")
```
These lines create a turtle object (`roo`) and a screen object (`wn`). The screen background color is set to black, and the window title is set to "Fractal Tree Pattern".

```python
roo.left(90)  # moving the turtle 90 degrees towards left
roo.speed(20)  # setting the speed of the turtle
```
These lines adjust the initial orientation of the turtle (`left(90)`) and set its drawing speed (`speed(20)`).

```python
# ...

def draw(l):
    if l < 10:
        return
    else:
        # ...
        roo.pensize(2)
        roo.backward(l)

draw(20)  # drawing 20 times
```
This is the main recursive function `draw` responsible for drawing the fractal tree. It takes a length parameter `l` and recursively draws branches with varying colors. The function is called with an initial length of 20.

After drawing the first set of branches, the script repeats similar code blocks with different colors and lengths to draw additional layers of the fractal tree. Each set of branches is drawn in a different color.

The script ends with the `wn.exitonclick()` call, which allows the user to close the turtle graphics window by clicking on it.

Overall, the script demonstrates the use of recursion and the turtle graphics library to create an aesthetically pleasing fractal tree pattern with different colors for various branches.

-----