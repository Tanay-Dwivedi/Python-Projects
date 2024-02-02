# Language Detection

The task of language detection comes into use when you are working on a very large dataset that contains data in different languages.

-----

## Installation

```
pip install langdetect
```
Firstly import the `langdetect` library through the terminal that will help in the program.

-----

## Code Break:

```python
from langdetect import detect
```

Imports the `detect` function from the `langdetect` library.

```python
text = input("Enter any text in any language: ")
```

Prompts the user to enter any text through the command line.

```python
print(detect(text))
```

Uses the `detect` function to determine the language of the entered text and prints the result.

In summary, this script takes user input, which can be any text in any language, and uses the `langdetect` library to identify and print the detected language.

-----