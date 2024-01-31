# Scrape Trending News

Most of the datasets that you find from different data sources on the internet are created by collecting data from websites. Using the `GoogleNews API` in Python, we can scrape trending updates based on any keyword or country.

-----

## Installation

```
pip install googlenews pandas
```
Firstly import the `googlenews pandas` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
from GoogleNews import GoogleNews
import pandas as pd
```

These lines import the necessary libraries and modules. `GoogleNews` is used for fetching news from Google News, and `pandas` is used for data manipulation.

```python
news = GoogleNews(period="1d")
news.search("India")
result = news.result()
```

An instance of the `GoogleNews` class is created with a period parameter set to "1d" (representing the last 24 hours). A search for news related to the term "India" is performed using the `search` method, and the result is stored in the variable `result`.

```python
data = pd.DataFrame.from_dict(result)
data = data.drop(columns=["img"])
data.head()
```

The script converts the result into a Pandas DataFrame using `pd.DataFrame.from_dict()`, and the "img" column is dropped as it contains image URLs. The first few rows of the DataFrame are displayed using `data.head()`.

```python
for i in result:
    print("Title : ", i["title"])
    print("News : ", i["desc"])
    print("Read Full News : ", i["link"])
```

A loop iterates through each news item in the `result`. For each news item, it prints the title, description, and a link to the full news article.

In summary, this script utilizes the `GoogleNews` library to fetch and display news related to the search term "India." The news data is initially stored in a Pandas DataFrame for further analysis, and then individual news items are printed in the console, including their titles, descriptions, and links to the full articles.

-----