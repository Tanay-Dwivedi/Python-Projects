# Monty Hall Problem

The Monty Hall Problem is a well-known puzzle derived from an American game show, “Let’s Make a Deal”.
The intuition behind this game leads many people to get it wrong, and when the Monty Hall issue is featured in a newspaper or discussion list, it often leads to a long argument in letters to the editor and on bulletin boards. electronic.

The Monty Hall Problem is like this:

- The show has three doors. A prize like a car or vacation is behind a door, and the other two doors hide a worthless prize called a Zonk; in most discussions of the problem, the Zonk is a goat.
- The competitor chooses a door. We’ll assume that the entrant has no internal knowledge of which gate is holding the prize, so the entrant will simply make a random choice.
- Smiling host Monty Hall opens one of the other doors, always choosing the one that shows a goat, and always offers the contestant a chance to change their choice for the remaining unopened door.
- The competitor chooses to change the gate or chooses to stick to the first choice.

-----

## Code Break:

```python
import random
from random import seed, randint
import numpy
```
These lines import the necessary libraries, including `random`, `seed`, `randint` from `random`, and `numpy`.

```python
def game(winningdoor, selecteddoor, change=False):
    assert winningdoor < 3
    assert winningdoor >= 0

    # Presenter removes the first door that was not selected nor winning
    removeddoor = next(i for i in range(3) if i != selecteddoor and i != winningdoor)

    # Player decides to change its choice
    if change:
        selecteddoor = next(
            i for i in range(3) if i != selecteddoor and i != removeddoor
        )

    # We suppose the player never wants to change its initial choice.
    return selecteddoor == winningdoor
```
This function `game` simulates the Monty Hall game. It takes three parameters: `winningdoor` (the door with the prize), `selecteddoor` (the player's initial choice), and an optional parameter `change` (indicating whether the player changes their choice after a door is revealed). The function returns `True` if the player wins and `False` otherwise.

```python
if __name__ == "__main__":
    playerdoors = numpy.random.random_integers(0, 2, (1000 * 1000 * 1,))
```
In this block, an array `playerdoors` is generated with random integers representing the player's initial choices. The array has a size of 1000000.

```python
    winningdoors = [d for d in playerdoors if game(1, d)]
    print(
        "Winning percentage without changing choice: ",
        len(winningdoors) / len(playerdoors),
    )
```
This part calculates the winning percentage without changing the initial choice. It uses a list comprehension to filter the winning doors and then prints the winning percentage.

```python
    winningdoors = [d for d in playerdoors if game(1, d, change=True)]
    print(
        "Winning percentage while changing choice: ",
        len(winningdoors) / len(playerdoors),
    )
```
Similar to the previous block, this part calculates the winning percentage when the player changes their initial choice and prints the result.

The code essentially simulates the Monty Hall problem multiple times and computes the winning percentages for both cases (changing and not changing the initial choice). The output provides insight into the probability difference between the two strategies.

-----