# Print Emojis

Emojis are used to express our emotions while writing a message or any piece of text.

This Python code utilizes the emoji module to enhance text output with emojis. The user is prompted to input an emoji name. The program then constructs a corresponding emoji string with colons around the input and prints the result, showcasing the entered emoji

The emoji.emojize method helps you write the description of any emoji inside “::” while writing a piece of text. You can find the description of all the emojis [here](https://carpedm20.github.io/emoji/).

-----

## Installation

```
pip install emoji
```
Firstly import the emoji library through the terminal that will help in the program.

-----

## Code Break:

```python
# Import the emoji module
import emoji
```
The code imports the `emoji` module, which provides functions to work with emojis in Python.

```python
# Print a message with an emoji using the emojize function
print(emoji.emojize("Hey there peeps :call_me_hand:"))
```
It prints a message that includes an emoji ":call_me_hand:" using the `emojize` function from the `emoji` module.

```python
# Prompt the user to input an emoji name
emj = input("Input your emoji name: ")
# Construct the emoji string with colons around the input, then print the result
inp_emj = ":" + emj + ":"
print("The emoji for", emj, "is", emoji.emojize(inp_emj))
```
The code prompts the user to input an emoji name. It then constructs an emoji string by adding colons around the input and prints the result using the `emojize` function.

-----