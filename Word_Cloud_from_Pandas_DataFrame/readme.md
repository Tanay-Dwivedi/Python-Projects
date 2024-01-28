# Word Cloud from a Pandas DataFrame

A [word cloud](https://github.com/amueller/word_cloud) is a data visualization technique that shows the most used words in large font and the least used words in small font. It helps to get an idea about your text data, especially when working on problems based on natural language processing.

-----

## Installation

```
pip install wordcloud
```
Firstly import the `wordcloud` library through the terminal that will help in the program.

-----

## Code Break:

Certainly! Let's break down the provided code:

```python
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
```
These lines import necessary libraries for creating a word cloud visualization. `WordCloud` is used to generate the word cloud, `ImageColorGenerator` helps generate colors from an image, `STOPWORDS` is a set of common words to be ignored, `matplotlib.pyplot` is used for plotting, and `pandas` is used for handling data.

```python
data = pd.read_csv(
    "https://raw.githubusercontent.com/amankharwal/Website-data/master/spam.csv&quot"
)
print(data.head())
```
This reads a CSV file from the given URL into a Pandas DataFrame. The first five rows of the DataFrame are then printed.

```python
text = " ".join(i for i in data.text)
```
This line concatenates all the text in the "text" column of the DataFrame into a single string.

```python
stopwords = set(STOPWORDS)
```
This creates a set of common English stop words using `STOPWORDS`.

```python
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
```
This creates a WordCloud object with specified parameters such as stopwords and background color, and then generates the word cloud from the concatenated text.

```python
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
```
This sets up the plot, displays the word cloud, and turns off the axis labels. The figure size is set to 15x10 inches, and the interpolation method "bilinear" is used for image smoothing. Finally, `plt.show()` displays the word cloud plot.

-----