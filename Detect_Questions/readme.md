# Detect Question

Detecting questions means identifying whether a sentence is interrogative or not. We can also use machine learning to detect questions

-----

## Installation

```python
pip install nltk
```
Firstly import the `nltk` library through the terminal that will help in this data analysis.

-----

## Code Break:

```python
import nltk
```

This line imports the Natural Language Toolkit (nltk) library, which is commonly used for natural language processing tasks.

```python
# run it only once and then you can remove this line from the code
nltk.download('punkt')
```

This line is commented out, but if uncommented, it would download the 'punkt' module from NLTK. 'punkt' is a module used for tokenization, and it includes pre-trained models for various languages.

```python
from nltk.tokenize import word_tokenize
```

This line imports the `word_tokenize` function from the `nltk.tokenize` module. This function is used for tokenizing sentences into words.

```python
question_words = [
    "what",
    "why",
    "when",
    "where",
    "name",
    "is",
    "how",
    "do",
    "does",
    "which",
    "are",
    "could",
    "would",
    "should",
    "has",
    "have",
    "whom",
    "whose",
    "don't",
]
```

A list named `question_words` is created, containing common words that are often found in questions.

```python
question_input = input("Enter a sentence: ")
```

The user is prompted to enter a sentence, and the input is stored in the variable `question_input`.

```python
question_input = question_input.lower()
```

The content of `question_input` is converted to lowercase to make the comparison case-insensitive.

```python
question_input = word_tokenize(question_input)
```

The `word_tokenize` function is used to tokenize the input sentence into a list of words.

```python
if any(x in question_input[0] for x in question_words):
    print("This is a question!")
else:
    print("This is not a question!")
```

This block of code checks if any word in the list `question_words` is present in the first word of the tokenized input sentence (`question_input[0]`). If a match is found, it is concluded that the input is a question, and the corresponding message is printed. Otherwise, it is considered not a question, and a different message is printed.

-----