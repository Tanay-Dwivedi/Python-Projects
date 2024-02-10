# Keyword Research

Google Trends is a keyword research tool that helps the researchers, bloggers, digital marketers and some more people in the digital industry to find how often a keyword is entered into Google search engine over a given period. Google Trends is used for keyword research mostly is writing articles on hot topics.

-----

## Installation

```
pip install pyspellchecker
```
Firstly import the `pyspellChecker` library through the terminal that will help in the program.

-----

## Code Break:

```python
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
```
This part of the code imports necessary modules: `pandas` for data manipulation and analysis, `TrendReq` from `pytrends.request` for accessing Google Trends data, and `matplotlib.pyplot` for plotting graphs.

```python
trends = TrendReq()

trends.build_payload(kw_list=["Data Science"])
data = trends.interest_by_region()
print(data.sample(10))
```
An instance of `TrendReq` is created. Then, the `build_payload()` method is used to specify the keyword(s) for the query. Here, "Data Science" is provided as the keyword. The `interest_by_region()` method fetches data on interest by region for the specified keyword. A sample of 10 rows from the fetched data is printed.

```python
df = data.sample(15)
df.reset_index().plot(x="geoName", y="Data Science", figsize=(120, 16), kind="bar")
plt.show()
```
A sample of 15 rows from the fetched data is stored in a DataFrame `df`. Then, the index of the DataFrame is reset and a bar plot is created using `matplotlib`. The x-axis represents the regions (`geoName`), the y-axis represents the interest in "Data Science", and each bar represents the interest level in a specific region. Finally, the plot is displayed.

```python
data = trends.trending_searches(pn="india")
print(data.head(10))
```
The `trending_searches()` method is used to fetch the currently trending searches in India (`pn="india"`). The top 10 trending searches are printed.

```python
keyword = trends.suggestions(keyword="Programming")
data = pd.DataFrame(keyword)
print(data.head())
```
The `suggestions()` method is used to fetch suggestions related to the keyword "Programming". The results are converted into a DataFrame using `pd.DataFrame()` and printed.

-----