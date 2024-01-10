# Rock Paper Scissors Game

This code implements a simple Rock, Paper, Scissors game where the user selects an option, and the computer randomly selects one as well. The game outcome is determined based on the choices, and the result is printed to the console, indicating whether the user or the computer won, or if it's a tie.

-----

## Code Break:

```python
# Import the random module
import random
```
The code imports the `random` module to generate random choices for the computer player.

```python
# Get the user's choice for Rock, Paper, or Scissor, convert it to lowercase
player1 = input("Select Rock, Paper, or Scissor: ").lower()
```
The user is prompted to input their choice (Rock, Paper, or Scissor), and the input is converted to lowercase for case-insensitive comparison.

```python
# Randomly choose a play for the computer from Rock, Paper, or Scissor, convert it to lowercase
player2 = random.choice(["rock", "paper", "scissor"]).lower()
print("Computer selected:", player2)
```
The computer's choice is randomly selected from Rock, Paper, or Scissor. The choice is converted to lowercase, and it is printed to the console.

```python
# Check the game outcome based on the choices of the user and the computer
if player1 == "rock" and player2 == "paper":
    print("Computer Won.")
elif player1 == "paper" and player2 == "scissor":
    print("Computer Won.")
elif player1 == "scissor" and player2 == "rock":
    print("Computer Won.")
elif player1 == player2:
    print("It's a Tie.")
else:
    print("You Won.")
```
The code checks the game outcome based on the choices of the user (`player1`) and the computer (`player2`). It considers various scenarios such as Paper covering Rock, Scissor cutting Paper, and Rock smashing Scissor. If the choices are the same, it's a tie. The outcome is then printed to the console.

-----