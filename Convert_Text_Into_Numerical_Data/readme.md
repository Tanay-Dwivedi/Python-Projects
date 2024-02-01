# Convert Text into Numerical Data

Text analysis is one of the major applications where machine learning algorithms are used. The process of converting textual data into numerical data is known as the process of vectorization in machine learning. It is an important task because you cannot use machine learning algorithms directly on a text as they only support numerical data.

-----

## Installation

```
pip install scikit-learn pandas
```
Firstly import the `scikit-learn pandas` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
```

These lines import the necessary libraries and modules. `pandas` is used for data manipulation, and `CountVectorizer` is used for converting text data into a bag-of-words representation.

```python
vect = CountVectorizer()
```

An instance of the `CountVectorizer` class is created.

```python
text = ["Hi, how are you", "I hope you are doing good", "My name is Aman Kharwal"]
```

A list of three text strings is created for demonstration purposes.

```python
vect.fit(text)
```

The `fit` method is called on the `CountVectorizer` instance to learn the vocabulary of the text data.

```python
train = vect.transform(text)
train.toarray()
```

The `transform` method is called to convert the text data into a bag-of-words representation. The resulting sparse matrix is then converted to a dense array using `toarray()`.

```python
data = pd.DataFrame(train.toarray(), columns=vect.get_feature_names())
data
```

A Pandas DataFrame is created using the bag-of-words representation. The columns are named with the feature names obtained from `get_feature_names()`, and the values represent the frequency of each word in the corresponding text.

In summary, this script uses `CountVectorizer` to convert a list of text strings into a bag-of-words representation and then displays the resulting data in a Pandas DataFrame. Each row in the DataFrame represents one of the input text strings, and the columns represent the words in the vocabulary with their corresponding frequencies in each text string.

-----