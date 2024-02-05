# Game of Life

The game of life, imagined by the British mathematician John H. Conway, is a Solitaire type game analogous to the rise, fall and alternations of a society of living organisms.

-----

## Code Break:

```python
from typing import List
```
This line imports the `List` type from the `typing` module, which is used to specify the type hints for function arguments.

```python
class game_of_life:
```
This line defines a class named `game_of_life` to encapsulate the functionality related to the Game of Life.

```python
    def gameOfLife(self, board: List[List[int]]) -> None:
```
This line declares a method named `gameOfLife` within the class. It takes a 2D list `board` of integers as input and specifies that it does not return anything (`-> None`).

```python
        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]
```
This block initializes a list called `neighbors` with tuples representing the relative positions of 8 neighboring cells around a given cell.

```python
        rows = len(board)
        cols = len(board[0])
```
These lines determine the number of rows and columns in the input board and store the values in `rows` and `cols` variables.

```python
        # Create a copy of the original board
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]
```
This line creates a deep copy of the original board using a nested list comprehension to ensure that modifications are made based on the original state.

```python
        # Iterate through the board cell by cell.
        for row in range(rows):
            for col in range(cols):
```
These lines initiate nested loops to iterate through each cell in the board.

```python
                # For each cell, count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]
```
This block sets up a count (`live_neighbors`) for the number of live neighbors for the current cell and iterates through the neighboring cells using the pre-defined `neighbors` list.

```python
                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    # The evaluation is done against the copy since that is never updated.
                    if (
                        (r < rows and r >= 0)
                        and (c < cols and c >= 0)
                        and (copy_board[r][c] == 1)
                    ):
                        live_neighbors += 1
```
These lines check the validity of the neighboring cell and whether it was originally a live cell. If both conditions are met, the `live_neighbors` count is incremented.

```python
                # Rule 1 or Rule 3
                if copy_board[row][col] == 1 and (
                    live_neighbors < 2 or live_neighbors > 3
                ):
                    board[row][col] = 0
```
This block applies Rule 1 or Rule 3 of Conway's Game of Life. If the current cell is alive and has fewer than 2 or more than 3 live neighbors, the cell is set to be dead (0).

```python
                # Rule 4
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1
```
This block applies Rule 4. If the current cell is dead and has exactly 3 live neighbors, the cell is set to be alive (1).

```python
game = game_of_life()
```
This line creates an instance of the `game_of_life` class.

```python
initial_board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
```
This line initializes an example board.

```python
game.gameOfLife(initial_board)
```
This line applies the Game of Life rules to the initial board.

```python
print(initial_board)
```
Finally, this line prints the modified board after applying the rules.

------