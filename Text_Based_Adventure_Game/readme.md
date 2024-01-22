# Text-Based Adventure Game

Text-Based Adventure Game is a very basic adventure game that any Python beginner can work on.
In this game, users have options to tackle a situation and with each input provided by the user, the game will continue to increase by putting more situations and more options.

-----

## Code Break:

```python
name = str(input("Enter Your Name: "))
```

This line prompts the user to input their name and assigns the input to the variable `name`.

```python
print(f"{name} you are stuck at work")
```

This line uses an f-string to print a message that includes the user's name, indicating that they are stuck at work.

```python
print(
    " You are still working and suddenly you saw a ghost, Now you have two options"
)
```

This line prints a narrative setup, describing that the user sees a ghost and now has two options.

```python
print("1. Run. 2. Jump from the window")
```

This line prints the options for the user to choose from.

```python
user = int(input("Choose 1 or 2: "))
```

This line prompts the user to input their choice (1 or 2) and converts the input to an integer.

```python
if user == 1:
    print("You did it")
elif user == 2:
    print("You are not that smart")
else:
    print("Please Check your input")
```

This block of code uses an `if-elif-else` statement to provide different outcomes based on the user's choice. If the user chooses 1, it prints "You did it." If the user chooses 2, it prints "You are not that smart." If the user enters an invalid choice, it prints "Please Check your input."

-----