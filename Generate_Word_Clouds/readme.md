# Generate Word Clouds

Word clouds are one of the most common methods of representing the textual dataset in a graphical format.

-----

## Installation

```
pip install wordcloud matplotlib plotly pandas
```
Firstly import the `wordcloud matplotlib plotly pandas` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
```

Imports necessary modules (`WordCloud`, `STOPWORDS`, `matplotlib.pyplot`, and `pandas`).

```python
df1 = pd.read_csv("five_star_reviews.csv")
df1.head()
```

Reads a CSV file named "five_star_reviews.csv" into a Pandas DataFrame (`df1`) and displays the first few rows.

```python
df2 = pd.read_csv("one_star_reviews.csv")
df2.head()
```

Reads a CSV file named "one_star_reviews.csv" into another Pandas DataFrame (`df2`) and displays the first few rows.

```python
stopwords = set(STOPWORDS)
```

Creates a set of stopwords using the predefined stopwords from the `STOPWORDS` set in the `wordcloud` library.

```python
words = ""
for review in df1.Review:
    # ... (Loop to process and concatenate words from five-star reviews)
```

Processes and concatenates words from the "Review" column of the DataFrame `df1` into the `words` string.

```python
wordcloud = WordCloud(
    width=800,
    height=800,
    background_color="white",
    stopwords=stopwords,
    min_font_size=10,
).generate(words)
```

Creates a WordCloud object (`wordcloud`) with specified parameters such as width, height, background color, stopwords, and minimum font size. The WordCloud is generated using the processed words.

```python
# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
```

Plots the WordCloud image using `matplotlib.pyplot`. The figure size, axis properties, and layout are adjusted before displaying the word cloud. The final word cloud image is shown using `plt.show()`.

-----