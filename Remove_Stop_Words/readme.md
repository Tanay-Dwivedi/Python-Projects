# Remove Stop Words

Stop Words removal is an important step while working on any application of natural language processing. Stop Words are words that carry very little or no significant semantic context in a piece of text which is why such words need to be removed.

-----

## Installation

```
pip install nltk
```
Firstly import the `nltk` library through the terminal that will help in the program.

-----

## Code Break:

```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
```

Imports necessary modules from the NLTK library.

```python
nltk.download("stopwords")
nltk.download("punkt")
```

Downloads the NLTK resources for stopwords and the Punkt tokenizer.

```python
text = "Hi, My name is Tanay Dwivedi, I am currently learning and exploring the Data Science field."
```

Defines a sample text for tokenization.

```python
tokens = word_tokenize(text)
```

Tokenizes the input text using the NLTK word tokenizer (`word_tokenize`), resulting in a list of words.

```python
tokenization = [word for word in tokens if not word in stopwords.words("english")]
```

Creates a list named `tokenization` that contains only those words from the `tokens` list that are not stopwords in English. Stopwords are common words that are often excluded from text processing because they usually don't carry much meaning.

```python
print(tokens)
```

Prints the original list of tokens (words) from the text.

```python
print(tokenization)
```

Prints the list of tokens after removing English stopwords.

In summary, this script tokenizes a given sentence and then removes common English stopwords using NLTK. The NLTK library provides a convenient way to handle text processing tasks like tokenization and stopword removal.

-----