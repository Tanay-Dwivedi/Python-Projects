# Password Picker

A password prevents others from accessing our system’s e-mails and other login information.
A password picker is an application that allows you to create strong passwords by combining words, numbers, and special characters.

-----

## Code Break:

```python
import random
import string
```

Imports necessary modules (`random` for generating random values and `string` for string-related operations).

```python
print("Welcome to Password Picker")
```

Prints a welcome message.

```python
adjectives = [
    "sleepy", "slow", "smelly", "wet", "fat", "red", "orange", "yellow",
    "green", "blue", "purple", "fluffy", "white", "proud", "brave",
]

nouns = [
    "apple", "dinosaur", "ball", "toaster", "goat", "dragon", "hammer",
    "duck", "panda",
]
```

Defines lists of adjectives and nouns that will be used to generate passwords.

```python
adjective = random.choice(adjectives)
noun = random.choice(nouns)

number = random.randrange(0, 100)
special_char = random.choice(string.punctuation)

password = adjective + noun + str(number) + special_char
print("You Password is : %s" % password)
```

Generates an initial password using a randomly chosen adjective, noun, number, and special character. Prints the generated password.

```python
while True:
    # ... (Repeatedly generates and prints passwords based on user input)
```

Enters into an infinite loop to repeatedly generate passwords based on user input. The user can choose to continue generating passwords or exit the loop.

```python
    response = input("Would you like another password? Type Y or N: ")
    if response == "N":
        break
```

Asks the user if they want another password. If the user types "N," the loop breaks, and the program ends.

-----