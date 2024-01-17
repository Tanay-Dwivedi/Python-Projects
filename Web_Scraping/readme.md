# Web Scraping to Create a Dataset

The datasets that you find on the internet from various data sources are either created by companies and organizations or are collected from websites.

-----

## How are Datasets Created by Scraping the Web?

There are so many libraries, frameworks, and tools that are used for the task of web scraping. Some of the most common libraries and modules in Python used for web scraping are:

- Scrapy
- Selenium
- BeautifulSoup
- Urlib.request

All of the above Python libraries and modules are great for scraping data from websites. After scraping the data, the data is prepared so that it can be stored in a CSV file to create a dataset.

-----

## Installation

```
pip install BeautofulSoup
```
```
pip install urlib
```
```
pip install pandas
```
Firstly import the `BeautofulSoup`, `urlib` and `pandas` libraries through the terminal that will help in the program.

-----

## Code Beak:

```python
# Import necessary libraries
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
```

These lines import the required libraries (`csv`, `urlopen`, `BeautifulSoup`, and `pandas`).

```python
# Fetch the HTML content of the Wikipedia page
html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_programming_languages")
soup = BeautifulSoup(html, "html.parser")
```

The `urlopen` function is used to open the specified URL, and `BeautifulSoup` is used to parse the HTML content of the page.

```python
# Find the first table with the class "wikitable"
table = soup.findAll("table", {"class": "wikitable"})[0]
```

The `findAll` method is used to find all tables with the class "wikitable" on the Wikipedia page. In this case, it assumes that the first table is the one of interest, so `[0]` is used to select that table.

```python
# Find all rows in the table
rows = table.findAll("tr")
```

This line finds all rows (`tr` elements) within the selected table.

```python
# Open a CSV file for writing
with open("language.csv", "wt+", newline="", encoding="utf-8") as f:
    # Create a CSV writer
    writer = csv.writer(f)

    # Loop through each row
    for i in rows:
        row = []
        # Loop through each cell in the row
        for cell in i.findAll(["td", "th"]):
            # Append the text content of the cell to the row
            row.append(cell.get_text())

        # Write the row to the CSV file
        writer.writerow(row)
```

This block of code opens a CSV file named "language.csv" for writing and uses a CSV writer to write the content of the table to the file. It loops through each row (`tr`) and each cell (`td` or `th`) within the row, extracting the text content and writing it to the CSV file.

```python
# Read the CSV file using pandas with the correct encoding
a = pd.read_csv("language.csv", encoding="ISO-8859-1")
```

This line uses `pandas` (`pd`) to read the CSV file into a DataFrame named `a`. The `encoding` parameter is set to "ISO-8859-1" to handle potential encoding issues.

```python
# Display the first few rows of the DataFrame
a.head()
```

This line prints the first few rows of the DataFrame to the console using the `head()` method.

This Python script uses the `urlopen` function from `urllib.request`, `BeautifulSoup` from `bs4` (Beautiful Soup), and `csv` to scrape a table from a Wikipedia page and save it as a CSV file. It then uses `pandas` to read and display the CSV file.

-----