# Netflix Recommendation System

Netflix is a subscription-based streaming platform that allows users to watch movies and TV shows without advertisements. One of the reasons behind the popularity of Netflix is its recommendation system. Its recommendation system recommends movies and TV shows based on the user’s interest.

-----

## Installation

```
pip install numpy pandas nltk scikit-learn
```
Firstly import the `numpy pandas nltk scikit-learn` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import numpy as np
import pandas as pd
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import re
from nltk.corpus import stopwords
import string

nltk.download("stopwords")
```
This part of the code imports necessary libraries: `numpy` and `pandas` for data manipulation, `text` from `sklearn.feature_extraction` for text vectorization, `cosine_similarity` from `sklearn.metrics.pairwise` to calculate similarity, `nltk` for natural language processing tasks, `re` for regular expressions, `stopwords` from `nltk.corpus` to remove common words, and `string` for handling punctuation. It also downloads the NLTK stopwords resource.

```python
data = pd.read_csv("netflixData.csv")
```
The Netflix data is loaded from a CSV file named "netflixData.csv" into a pandas DataFrame called `data`, allowing for easy manipulation and analysis.

```python
print(data.head())
```
This prints the first few rows of the DataFrame `data`, giving a glimpse of the data structure.

```python
print(data.isnull().sum())
```
This prints the sum of missing values in each column of the DataFrame `data`, helping to identify any missing data that needs to be handled.

```python
data = data[["Title", "Description", "Content Type", "Genres"]]
```
This line retains only the relevant columns ("Title", "Description", "Content Type", "Genres") in the DataFrame `data`, discarding any other columns that are not needed for the recommendation system.

```python
print(data.head())
```
This prints the first few rows of the DataFrame `data` after selecting the relevant columns, providing insight into the data structure.

```python
data = data.dropna()
```
This removes any rows with missing values from the DataFrame `data` to ensure data quality and consistency for further analysis.

```python
stopword = set(stopwords.words("english"))
stemmer = nltk.SnowballStemmer("english")
```
A set of stopwords for the English language is created using NLTK's `stopwords.words("english")`. Additionally, a stemmer object is initialized using NLTK's SnowballStemmer for English.

```python
def clean(text):
    text = str(text).lower()
    text = re.sub("\[.*?\]", "", text)
    text = re.sub("https?://\S+|www\.\S+", "", text)
    text = re.sub("<.*?>+", "", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub("\n", "", text)
    text = re.sub("\w*\d\w*", "", text)
    text = [word for word in text.split(" ") if word not in stopword]
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split(" ")]
    text = " ".join(text)
    return text
```
A function named `clean()` is defined to preprocess text data. It performs various text cleaning operations, such as converting text to lowercase, removing URLs, punctuation, stopwords, and numerical characters. It also applies stemming to reduce words to their root form.

```python
data["Title"] = data["Title"].apply(clean)
```
The `clean()` function is applied to the "Title" column of the DataFrame `data` to preprocess the titles, ensuring consistency and improving the quality of data for analysis.

```python
feature = data["Genres"].tolist()
tfidf = text.TfidfVectorizer(input=feature, stop_words="english")
tfidf_matrix = tfidf.fit_transform(feature)
```
The "Genres" column of the DataFrame `data` is converted into a list called `feature`. Then, `TfidfVectorizer` from sklearn is used to convert the textual feature (genres) into a TF-IDF matrix (`tfidf_matrix`). This transformation represents the textual data in a numerical format suitable for machine learning algorithms.

```python
similarity = cosine_similarity(tfidf_matrix)
```
Cosine similarity is calculated between TF-IDF vectors of genres using `cosine_similarity()` from sklearn. This metric quantifies the similarity between two non-zero vectors, providing a measure of similarity between Netflix titles based on their genres.

```python
indices = pd.Series(data.index, index=data["Title"]).drop_duplicates()
```
A Pandas Series named `indices` is created where the index is set as the "Title" column of the DataFrame `data`, and the values are set as the corresponding indices. This allows for quick lookup of indices based on titles.

```python
def netFlix_recommendation(title, similarity=similarity):
    index = indices[title]
    similarity_scores = list(enumerate(similarity[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[0:10]
    movieindices = [i[0] for i in similarity_scores]
    return data["Title"].iloc[movieindices]
```
A function named `netFlix_recommendation()` is defined to generate Netflix recommendations based on a given title. This function takes a title as input, finds its index in the DataFrame `data`, computes similarity scores with other titles, sorts the titles based on similarity scores, selects the top 10 similar titles, and returns them as recommendations.

```python
print(netFlix_recommendation("girlfriend"))
```
The `netFlix_recommendation()` function is called with the input title "girlfriend", and the recommendations are printed. This demonstrates the functionality of the recommendation system.

-----