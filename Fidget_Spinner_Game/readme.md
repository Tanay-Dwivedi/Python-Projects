# Fidget Spinner Game

To create a very simple game based on a fidget spinner. The logic of the game is that the turns will keep increasing as you press the space bar, and it will reduce its speed and stop at a point where you stop pressing the space bar.

------

## Installation

```
pip install turtle
```
Firstly import the `turtle` library through the terminal that will help in the program.

-----

## Code Break:

```python
from turtle import *
```
This line imports the `turtle` module, which provides a simple graphics library for creating drawings and animations.

```python
state = {"turn": 0}
```
This line initializes a dictionary `state` with a single key-value pair. The key is "turn," and its initial value is 0. This dictionary is used to keep track of the current state of the animation.

```python
def spinner():
    clear()
    angle = state["turn"] / 10
    right(angle)
    forward(100)
    dot(120, "red")
    back(100)
    right(120)
    forward(100)
    dot(120, "green")
    back(100)
    right(120)
    forward(100)
    dot(120, "blue")
    back(100)
    right(120)
    update()
```
This function `spinner` clears the current turtle drawing, calculates an angle based on the current "turn" value in the state, and then draws a spinning pattern using the turtle graphics commands. It draws three dots of different colors (red, green, and blue) forming a triangular pattern.

```python
def animate():
    if state["turn"] > 0:
        state["turn"] -= 1

    spinner()
    ontimer(animate, 20)
```
This function `animate` is a recursive function that continuously updates the animation. It decreases the "turn" value in the state, calls the `spinner` function to draw the spinning pattern, and sets a timer to call itself again after 20 milliseconds using `ontimer`.

```python
def flick():
    state["turn"] += 10
```
This function `flick` increases the "turn" value in the state by 10 when the space key is pressed. This function is associated with the space key using `onkey`.

```python
setup(420, 420, 370, 0)
```
This line sets up the turtle graphics window with a width of 420 pixels, a height of 420 pixels, and the window positioned at coordinates (370, 0).

```python
hideturtle()
```
This line hides the turtle cursor.

```python
tracer(False)
```
This line turns off animation updates, allowing the drawing to appear instantly rather than gradually.

```python
width(20)
```
This line sets the width of the turtle pen to 20 units.

```python
onkey(flick, "space")
```
This line associates the `flick` function with the space key so that when the space key is pressed, the `flick` function is called.

```python
listen()
```
This line listens for events, enabling the program to respond to keyboard input.

```python
animate()
```
This line initiates the animation by calling the `animate` function.

```python
done()
```
This line keeps the turtle graphics window open until it is manually closed by the user. It is necessary to prevent the window from closing immediately after running the script.

-----