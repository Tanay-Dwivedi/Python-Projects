# Remove Cuss Words

Cuss Words are the words that make your language sound very impolite, rude, and culturally offensive. Sometimes we need to identify and remove cuss words from a piece of text.

-----

## Installation

```python
pip install better_profanity
```
Firstly import the `better_profanity` library through the terminal that will help in this program.

-----

# Code Break:

```python
# Import the profanity class from the better_profanity module
from better_profanity import profanity
```
This line imports the `profanity` class from the `better_profanity` module. `better_profanity` is a library used for detecting and censoring profanity in text.

```python
# Prompt the user to input a sentence
text = input("Enter a sentence: ")
```
This line uses the `input()` function to get user input and stores it in the variable `text`. The user is prompted to enter a sentence, which will be processed for profanity in the next steps.

```python
# Censor the profanity in the entered text using the profanity.censor() method
censored_text = profanity.censor(text)
```
Here, the `censor()` method of the `profanity` class is applied to the entered text (`text`). This method replaces profane words in the text with asterisks or other characters, effectively censoring them.

```python
# Print the censored version of the entered text
print(censored_text)
```
Finally, the censored version of the entered text is printed to the console.

In summary, this code takes user input, checks for profanity using the `better_profanity` library, and prints a censored version of the entered text if any profanity is detected. It's a simple example of using a profanity filter in Python.

-----