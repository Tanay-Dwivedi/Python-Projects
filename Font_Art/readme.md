# Create Font Art

The font that appears in the output of your Python program is the default font for your operating system. Changing the font of your output may not be possible without using an external library.
The `PyFiglet` library in Python can be used to visualize the output of your Python program with an amazing font style.

-----

## Installation

```
pip install pyfiglet
```
Firstly import the `pyfiglet` library through the terminal that will help in the program.

-----

## Code Break:

```python
# Import the pyfiglet library
import pyfiglet
```

This line imports the `pyfiglet` library.

```python
# Prompt the user to enter text
text = input("Enter your text: ")
```

The script uses the `input()` function to prompt the user to enter some text, and the entered text is stored in the variable `text`.

```python
# Generate ASCII art text for the user-entered text using the default font
font = pyfiglet.figlet_format(text)
```

`pyfiglet.figlet_format()` is used to generate ASCII art text for the user-entered text using the default font. The result is stored in the variable `font`.

```python
# Print the generated ASCII art text to the console
print(font)
```

Finally, the script prints the generated ASCII art text to the console.

When you run this script, you'll be prompted to enter some text, and the script will then generate and display the ASCII art representation of the entered text using the default font provided by the `pyfiglet` library.

-----