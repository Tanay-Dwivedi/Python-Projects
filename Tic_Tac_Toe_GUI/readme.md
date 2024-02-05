# Tic Tac Toe GUI

This game is very popular and is quite simple in itself. It is a two-player game. In this game, there is a board with 3×3 squares.

-----

## Installation

```
pip install tkinter numpy
```
Firstly import the `tkinter numpy` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
from tkinter import *
import numpy as np
```
These lines import the required modules, including `tkinter` for creating the GUI and `numpy` for numerical operations.

```python
size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
symbol_X_color = "#EE4035"
symbol_O_color = "#0492CF"
Green_color = "#7BC043"
```
These constants define the size of the board, symbol size, thickness, and colors for X and O symbols.

```python
class Tic_Tac_Toe:
    def __init__(self):
        # ... (Initialization functions)

    def mainloop(self):
        self.window.mainloop()

    # ... (Drawing functions)

    # ... (Logical functions)

    def click(self, event):
        # ... (Handling mouse click events)
```

The class `Tic_Tac_Toe` encapsulates the entire game. It initializes the GUI, handles drawing functions, and contains logical functions to determine the game's state.

- `__init__`: Initializes the game window, canvas, and sets up initial game state.

- `draw_O`: Draws an O symbol on the canvas at a given logical position.
- `draw_X`: Draws an X symbol on the canvas at a given logical position.
- `display_gameover`: Displays the game result, including the winner or a tie.

- `convert_logical_to_grid_position`: Converts logical grid position to actual pixel position.
- `convert_grid_to_logical_position`: Converts pixel position to logical grid position.
- `is_grid_occupied`: Checks if a grid position is already occupied.
- `is_winner`: Checks if a player has won.
- `is_tie`: Checks if the game is a tie.
- `is_gameover`: Checks if the game is concluded.

- `click`: Handles mouse click events, updating the board and checking for a gameover condition.

```python
game_instance = Tic_Tac_Toe()
game_instance.mainloop()
```
Creates an instance of the `Tic_Tac_Toe` class and starts the main loop.

Overall, the code provides a simple and interactive Tic-Tac-Toe game with a graphical user interface.

-----