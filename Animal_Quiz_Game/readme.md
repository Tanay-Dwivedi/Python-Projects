# Animal Quiz Game

This quiz game uses a function; a block of code with a name that performs a specific task. A function allows you to use the same code several times, without having to type everything each time.

-----

## Code Break:

```python
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ", answer)


score = 0
```

This part of the code defines a function `check_guess` that takes a user's guess and the correct answer as parameters. It uses a `while` loop to allow the user up to three attempts to guess the correct answer. The function updates the global variable `score` if the answer is correct.

```python
print("Guess the Animal")
```

This line prints a message indicating the start of the quiz.

```python
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
```

These lines prompt the user to input their guess for the first question and call the `check_guess` function to check if the answer is correct.

```python
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
```

These lines do the same for the second question.

```python
guess3 = input("Which is the largest animal? ")
check_guess(guess3, "Blue Whale")
```

These lines do the same for the third question.

```python
print("Your Score is " + str(score))
```

Finally, this line prints the user's score after answering all the questions.

-----