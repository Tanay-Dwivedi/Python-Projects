# Get Live Covid-19 Data

To get live covid-19 data by using the Python programming language we will be using some of the popular methods of scraping data from the web.

-----

## Installation

```
pip install urllib3 beautifulsoup4
```
Firstly import the `urllib3 beautifulsoup4` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import csv  # Import the CSV module for handling CSV files
from urllib.request import urlopen  # Import urlopen to open the Wikipedia page
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing
import pandas as pd  # Import pandas for data manipulation
```

The above lines import necessary libraries: `csv` for CSV file handling, `urlopen` for opening URLs, `BeautifulSoup` for HTML parsing, and `pandas` for data manipulation.

```python
html = urlopen("https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data#covid-19-pandemic-data")
```

This line opens the Wikipedia page using the `urlopen` function and stores the HTML content in the `html` variable.

```python
soup = BeautifulSoup(html, "html.parser")
```

Here, BeautifulSoup is used to create a soup object, which parses the HTML content using the "html.parser."

```python
table = soup.findAll("table", {"class": "wikitable"})[0]
```

This line finds all tables in the HTML with the class "wikitable" and selects the first one (index 0) since it contains the COVID-19 pandemic data.

```python
rows = table.findAll("tr")
```

The code extracts all rows (`tr` tags) from the selected table.

```python
with open("Dataset.csv", "wt+", newline="") as f:
    writer = csv.writer(f)
    for i in rows:
        row = []
        for cell in i.findAll(["td", "th"]):
            row.append(cell.get_text())
        writer.writerow(row)
```

This block creates a CSV file named "Dataset.csv" and writes the extracted table data into it using the CSV module.

```python
data = pd.read_csv("Dataset.csv")
data.head()
```

Finally, the code reads the CSV file into a pandas DataFrame and displays the first few rows of the DataFrame using `head()`.


-----