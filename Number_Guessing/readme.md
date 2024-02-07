# Number Guessing Game

A number guessing game aims to guess the number that the program has come up with. Essentially the program logic is:

- The program randomly selects a number between 1 and 100 or any other combination of numbers.
- It will then ask the player to enter his proposal.
- It will then check if this number is the same as the one generated randomly by the computer; if so, the player wins.
- If the player’s guess is not the same, then he will check if the number is higher or lower than the guess and tell the player.

-----

## Code Break:

```python
import random
```
Imports the `random` module, which provides functions for generating random numbers.

```python
n = random.randrange(1, 100)
```
Generates a random integer between 1 and 99 (inclusive) and assigns it to the variable `n`.

```python
guess = int(input("Enter any number: "))
```
Prompts the user to enter a number via standard input (`input()`), converts the input value to an integer using `int()`, and assigns it to the variable `guess`.

```python
while n != guess:
```
Starts a while loop that continues as long as the guessed number (`guess`) is not equal to the random number (`n`).

```python
    if guess < n:
```
Checks if the guessed number is less than the random number.

```python
        print("Too low")
```
Prints "Too low" to inform the user that their guess is lower than the random number.

```python
        guess = int(input("Enter number again: "))
```
Prompts the user to enter a number again as their guess, converts the input value to an integer using `int()`, and updates the `guess` variable.

```python
    elif guess > n:
```
Checks if the guessed number is greater than the random number.

```python
        print("Too high!")
```
Prints "Too high!" to inform the user that their guess is higher than the random number.

```python
        guess = int(input("Enter number again: "))
```
Prompts the user to enter a number again as their guess, converts the input value to an integer using `int()`, and updates the `guess` variable.

```python
    else:
```
Executes when neither of the above conditions (`guess < n` or `guess > n`) is met, indicating that the guessed number matches the random number.

```python
        break
```
Exits the while loop.

```python
print("you guessed it right!!")
```
Prints a congratulatory message indicating that the user has guessed the correct number.

-----