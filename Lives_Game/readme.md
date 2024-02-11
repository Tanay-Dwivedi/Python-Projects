# Lives Game

In this game, you have to guess the secret word letter by letter. If you guessed a letter incorrectly, you will lose a life. As the title suggests, you need to choose the letters carefully as you will have a very limited number of lives.

-----

## Code Break:

This script implements a simple word guessing game. Let's break it down:

```python
import random
```
This imports the `random` module, which is used to generate random numbers and make random selections.

```python
lives = 3
```
Sets the initial number of lives for the player.

```python
words = ["pizza", "fairy", "teeth", "shirt", "otter", "plane"]
secret_word = random.choice(words)
```
Defines a list of words and randomly selects one of them as the secret word for the player to guess.

```python
clue = list("?????")
```
Initializes a list called `clue` with question marks representing unknown letters of the secret word.

```python
heart_symbol = "\u2764"
```
Defines a heart symbol as a Unicode character for displaying lives.

```python
guessed_word_correctly = False
```
Sets a flag to track if the player has guessed the word correctly.

```python
def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1
```
Defines a function `update_clue()` to update the clue based on the guessed letter. It replaces the question marks with the guessed letter if it matches any letter in the secret word.

The game loop starts with a `while` loop that continues as long as the player has lives left (`lives > 0`).

```python
    print(clue)
    print("Lives left: " + heart_symbol * lives)
```
Prints the current clue and the number of lives left.

```python
    guess = input("Guess a letter or the whole word: ")
```
Prompts the player to input a letter or the whole word they want to guess.

```python
    if guess == secret_word:
        guessed_word_correctly = True
        break
```
Checks if the guess matches the secret word. If it does, sets the `guessed_word_correctly` flag to `True` and breaks out of the loop.

```python
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print("Incorrect. You lose a life")
        lives = lives - 1
```
If the guess is a letter in the secret word, updates the clue accordingly. Otherwise, informs the player that they lose a life.

After the game loop ends, the script checks if the player has guessed the word correctly and prints the corresponding message. If not, it reveals the secret word.

This script allows the player to guess letters or the entire word and provides feedback on correct and incorrect guesses until the player either guesses the word correctly or runs out of lives.

-----