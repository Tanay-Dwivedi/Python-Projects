# Spelling Correction

Correcting spelling mistakes is an integral part of writing in the modern world, whether it is part of texting a phone, sending an email, writing large documents or searching for information on the web.

-----

## Installation

```
pip install textblob
```
Firstly import the `textblob` library through the terminal that will help in the program.

-----

## Code Break:

```python
from textblob import TextBlob
```
This line imports the `TextBlob` class from the `textblob` library. `TextBlob` is a natural language processing library that provides simple API for common text processing tasks.

```python
words = ["Data Scence", "Mahine Learnin"]
```
This line initializes a list `words` containing two misspelled words.

```python
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
```
This block of code creates a new list `corrected_words` by applying the `TextBlob` constructor to each word in the `words` list. `TextBlob(i)` creates a `TextBlob` object for each word, allowing for various text processing operations.

```python
print("Wrong words :", words)
```
This line prints the label "Wrong words :" followed by the contents of the `words` list.

```python
print("Corrected Words are :")
```
This line prints the label "Corrected Words are :" to indicate the following output will be the corrected versions of the words.

```python
for i in corrected_words:
    print(i.correct(), end=" ")
```
This loop iterates through each `TextBlob` object in the `corrected_words` list and prints the corrected version of each word using the `correct()` method provided by `TextBlob`. The `end=" "` parameter ensures that the corrected words are printed on the same line separated by a space.

So, the overall purpose of this code is to demonstrate the use of the `TextBlob` library to correct misspelled words in a list and print the corrected versions. Note that `TextBlob` uses a pre-trained model for spell correction.

-----