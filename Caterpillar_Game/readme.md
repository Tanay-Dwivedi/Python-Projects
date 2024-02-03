# Caterpillar Game

To make a caterpillar game with python you need to develop a logic in which you will use the four arrow keys to move around the caterpillar to make it eat the leaf, every time it eats the leaf it will grow bigger and move around faster.

-----

## Installation

```
pip install turtle
```
Firstly import the `turtle` library through the terminal that will help in the program.

-----

## Code Break:

```python
import turtle as t
import random as rd
```

Imports the Turtle graphics library as `t` and the `random` module as `rd`.

```python
t.bgcolor('yellow')
```

Sets the background color of the Turtle graphics window to yellow.

```python
caterpillar = t.Turtle()
```

Creates a Turtle object named `caterpillar`.

```python
# ... (Similar initialization for caterpillar, leaf, and turtles for text and score)
```

Initialize the caterpillar, leaf, text_turtle, and score_turtle with various properties like shape, color, speed, and visibility.

```python
def outside_window():
    # ... (Function to check if the caterpillar is outside the window boundaries)
```

Defines a function `outside_window` that checks if the caterpillar is outside the window boundaries.

```python
def game_over():
    # ... (Function to display 'GAME OVER!' message)
```

Defines a function `game_over` to display a 'GAME OVER!' message when the game ends.

```python
def display_score(current_score):
    # ... (Function to display the current score)
```

Defines a function `display_score` to display the current score on the screen.

```python
def place_leaf():
    # ... (Function to place the leaf at a random position)
```

Defines a function `place_leaf` to place the leaf at a random position on the screen.

```python
def start_game():
    # ... (Function to start the game, handle collisions, and update score)
```

Defines a function `start_game` that starts the game, handles collisions between the caterpillar and the leaf, and updates the score.

```python
def move_up():
    # ... (Function to set the caterpillar's heading when moving up)
```

Defines a function `move_up` to set the caterpillar's heading when moving up.

```python
# ... (Similar functions for moving right, down, and left)
```

Define functions `move_down`, `move_left`, and `move_right` for moving the caterpillar in different directions.

```python
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.listen()
t.mainloop()
```

Configures event handlers for specific keys and starts listening for key events to control the caterpillar's movement. The main loop (`t.mainloop()`) keeps the Turtle graphics window open and responsive to user input.

In summary, the script creates a simple caterpillar game using the Turtle graphics library, allowing the player to control the caterpillar's movement and collect leaves to score points. The game provides a basic graphical user interface using the Turtle module.

-----