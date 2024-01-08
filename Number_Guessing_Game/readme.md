# Number Guessing Game

This Python script is a simple number guessing game. It generates a random number between 1 and 10, and the user repeatedly guesses the number until they get it right. After each guess, the program provides feedback if the guess is too high or too low. Once the correct number is guessed, a congratulatory message is displayed along with the actual number. The game continues until the player guesses the correct number.

## Code Break:


```python
import random
```
This line imports the `random` module, which is used to generate random numbers.

```python
num = random.randint(1, 10)
```
This line generates a random integer between 1 and 10 (inclusive) and assigns it to the variable `num`. This is the number that the player needs to guess.

```python
guess = 0
```
This line initializes the variable `guess` to 0. It will be used to store the player's guessed number.

```python
while guess != num:
    guess = int(input("Enter your guessed number: "))
```
This starts a `while` loop that continues until the player correctly guesses the number (`guess == num`). Inside the loop, the player is prompted to enter their guessed number using `input()`, and the entered value is converted to an integer using `int()` and stored in the variable `guess`.

```python
    if guess > num:
        print("Guessed too high.🙂")
    elif guess < num:
        print("Guessed too low.😑")
    else:
        print("Congo. You guessed it right.🎉")
        print("The number was ", num)
        break
```
Inside the loop, there are conditional statements to provide feedback to the player based on their guess. If the guess is too high, it prints a message saying "Guessed too high." If the guess is too low, it prints "Guessed too low." If the guess is correct, it prints a congratulatory message, reveals the correct number, and breaks out of the loop.

```python
print("Thanks for playing.😎")
```
Finally, outside the loop, a message is printed thanking the player for playing. This message is always executed, regardless of whether the player guessed the correct number or not.

</br>