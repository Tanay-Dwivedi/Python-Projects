# Print Colored Text

In Python the `Colorama` module allows us to easily create colored terminal text.
Using the Colorama module we can print colored text with Python. We can use it and call its built-in variables which are aliases for the desired ANSI codes. This makes our code more readable and works better with Windows command prompts after calling `colorama.init()` at the start of your script.

-----

## Installation

```
pip install colorama
```
Firstly import the `colorama` library through the terminal that will help in the program.

-----

## Code Break:

```python
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
```

These lines import the `colorama` module and initialize it with `autoreset=True`. The `autoreset` parameter ensures that the color changes are automatically reset to default after each print statement.

```python
print(
    Fore.BLUE
    + Back.YELLOW
    + "Hi My name is Tanay Dwivedi."
    + Fore.YELLOW
    + Back.BLUE
    + "I am learning Data Science."
)
```

This line prints a message with alternating blue and yellow colors for the text and background, respectively.

```python
print(Back.CYAN + "Hi My name is Tanay Dwivedi.")
```

This line prints a message with a cyan background.

```python
print(Fore.RED + Back.GREEN + "Hi My name is Tanay Dwivedi.")
```

This line prints a message with red text and a green background.

The use of `Fore` and `Back` classes allows you to easily set the text and background colors for console output. The `autoreset` feature ensures that subsequent print statements revert to the default colors.

-----