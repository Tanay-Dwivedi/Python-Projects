# Scrape Table from a Website

This Python script uses the `urllib.request` module to fetch the HTML content from a specified Wikipedia URL and then uses `pandas` to read the HTML tables into a DataFrame. Finally, it prints the first few rows of the DataFrame and saves the entire DataFrame to a CSV file.

-----

## Installation

```
pip install lxml
```
Firstly import the `lxml` library through the terminal that will help in the program.

-----

## Code Break:

```python
# Import necessary libraries
import urllib.request
import pandas as pd
```

These lines import the required libraries (`urllib.request` and `pandas`).

```python
# Specify the URL of the Wikipedia page containing information about programming languages
url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
```

This line sets the URL to the Wikipedia page containing information about programming languages used in popular websites.

```python
# Open the URL and read the HTML content
with urllib.request.urlopen(url) as i:
    html = i.read()
```

The `urllib.request.urlopen()` function is used to open the URL and read its HTML content. The content is stored in the `html` variable.

```python
# Use pandas to read HTML tables into a DataFrame
data = pd.read_html(html)[0]
```

`pd.read_html(html)` is a pandas function that reads HTML tables from a string and returns a list of DataFrames. In this case, it's assumed that the first table on the page is the one of interest, so `[0]` is used to select that DataFrame.

```python
# Print the first few rows of the DataFrame
print(data.head())
```

This line prints the first few rows of the DataFrame to the console.

```python
# Save the DataFrame to a CSV file
data.to_csv("scraped_data.csv")
```

The `to_csv()` method is used to save the entire DataFrame to a CSV file named "scraped_data.csv."

-----

## Output

[CSV File](scraped_data.csv)

-----