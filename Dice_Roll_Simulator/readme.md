# Dice Roll Simulator

The Dice Roll Simulation can be done by choosing a random integer between 1 and 6 for which we can use the random module in the Python programming language.

-----

## Code Break:

```python
import random
```

This line imports the `random` module, which is used for generating random numbers.

```python
min_val = 1
max_val = 6
```

These lines set the minimum and maximum values for the six-sided dice.

```python
roll_again = "yes"
```

This line initializes the variable `roll_again` to "yes" to start the loop.

```python
while roll_again == "yes" or roll_again == "y":
```

This initiates a `while` loop that continues as long as the user wants to roll the dice. It checks if `roll_again` is equal to "yes" or "y".

```python
    print("Rolling The Dices...")
    print("The Values are :")

    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))
```

These lines print messages indicating that the dice are being rolled and then print the values obtained for two six-sided dice using `random.randint()`.

```python
    roll_again = input("Roll the Dices Again?")
```

This line prompts the user to input whether they want to roll the dice again and assigns the input to the variable `roll_again`.

The loop continues as long as the user enters "yes" or "y". If the user enters anything else, the loop exits, and the script ends.

-----