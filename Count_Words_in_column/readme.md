# Count Number of Words in a Column

This Python code uses the Pandas library to load article data from a CSV file hosted online. It calculates the number of words in each article, adds a new column with this information to the dataset, and prints the resulting DataFrame. Essentially, it performs data analysis and manipulation tasks on the provided dataset.

-----

## Installation

```python
pip install pandas
```
Firstly import the pandas library through the terminal that will help in this data analysis.

-----

## Code Break:

```python
# Import the pandas library and alias it as pd
import pandas as pd
```
In this line, the code imports the `pandas` library and uses the alias `pd` for convenience throughout the code.

```python
# Read a CSV file from a specified URL into a DataFrame named data
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", encoding="latin1")
```
Here, the code reads a CSV file from the provided URL using Pandas' `read_csv` function. The data is loaded into a DataFrame named `data`. The `encoding` parameter is set to "latin1" to handle special characters in the data.

```python
# Print the entire DataFrame data
print(data)
```
This line prints the entire DataFrame `data` to the console, displaying the content of the CSV file, including all columns and rows.

```python
# Add a new column "Number of Words" to the DataFrame, calculated based on the number of words in each article
data["Number of Words"] = data["Article"].apply(lambda n: len(n.split()))
```
The code adds a new column named "Number of Words" to the DataFrame using the `apply` function along with a lambda function. The lambda function calculates the number of words in each article by splitting the text and then counting the resulting list's length.

```python
# Print the first few rows of the DataFrame with the added "Number of Words" column
print(data.head())
```
This line prints the first few rows of the modified DataFrame using the `head()` method. It displays the original columns along with the newly added "Number of Words" column, providing a glimpse of the dataset's updated structure.

-----