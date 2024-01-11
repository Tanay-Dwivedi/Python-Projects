# Correct Spellings

The SpellChecker module in can be used to correct misspelt words in a piece of text.

The Python script employs the SpellChecker module to verify the spelling of a word entered by the user. After prompting the user for input, it checks if the word is in its spell checker database. If the word is correct, it prints "Correct spelling"; otherwise, it suggests a likely correct spelling using the correction method and prints the corrected version. Essentially, the script aids users in detecting and rectifying potential spelling mistakes in their input.

-----

## Installation

```
pip install pyspellchecker
```
Firstly import the `pyspellChecker` library through the terminal that will help in the program.

-----

## Code Break:

```python
# Import the SpellChecker class from the spellchecker module
from spellchecker import SpellChecker
```

This line imports the `SpellChecker` class from the `spellchecker` module.

```python
# Create an instance of the SpellChecker class
correct = SpellChecker()
```

Here, an instance of the `SpellChecker` class is created.

```python
# Get user input for a word
word = input("Enter a Word: ")
```

The program prompts the user to enter a word, and the input is stored in the variable `word`.

```python
# Check if the entered word is in the SpellChecker instance
if word in correct:
    print("Correct spelling")
else:
    # If the word is not in the SpellChecker, find the correct spelling
    correct_word = correct.correction(word)
    print("The correct spelling is:", correct_word)
```

This block of code checks if the entered word is in the dictionary of the `SpellChecker` instance. If it is, it prints "Correct spelling." If the word is not found, it uses the `correction` method of the `SpellChecker` class to find the correct spelling and prints it. The `correction` method suggests a correction for misspelled words based on the words present in the dictionary used by the `SpellChecker` instance.

-----