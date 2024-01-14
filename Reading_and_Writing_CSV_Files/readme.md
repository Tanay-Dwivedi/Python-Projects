# Reading and Writing CSV Files

CSV (Comma Separated Values) files are the most commonly used file format for importing and exporting big datasets. The reason why a CSV file is preferred over an Excel file is that a CSV file consumes less memory as compared to an Excel file.

-----

## Installation

```python
pip install pandas
```
Firstly import the `pandas` library through the terminal that will help to run the program.

-----

## Code Break:

### Write file

```python
import csv
```

This line imports the `csv` module, which provides functionality for reading from and writing to CSV files.

```python
import pandas as pd
```

This line imports the `pandas` library and aliases it as `pd`. Pandas is a powerful library for data manipulation and analysis.

```python
data = {
    "Name": ["Aman", "Diksha", "Akanksha", "Sajid", "Akshit"],
    "Age": [23, 21, 25, 23, 22],
}
```

A dictionary named `data` is created, containing two key-value pairs. The keys are column names ("Name" and "Age"), and the values are lists representing data for each column.

```python
data = pd.DataFrame(data)
```

The dictionary `data` is converted into a Pandas DataFrame using `pd.DataFrame()`. This creates a tabular structure with columns "Name" and "Age".

```python
data.to_csv("data.csv", index=False)
```

The `to_csv` method of the Pandas DataFrame is used to write the DataFrame to a CSV file named "data.csv". The `index=False` parameter indicates that the row indices should not be included in the CSV file.

```python
print(data.head())
```

This line prints the first few rows of the DataFrame using the `head()` method. It displays the content of the DataFrame, providing a preview of the data that has been created and written to the CSV file.

### Read File:

```python
import pandas as pd
```

This line imports the `pandas` library and aliases it as `pd`. Pandas is a powerful library for data manipulation and analysis.

```python
data = pd.read_csv("data.csv")
```

The `read_csv` function from Pandas is used to read the contents of a CSV file named "data.csv" into a DataFrame named `data`. This assumes that there is a CSV file named "data.csv" in the current working directory.

```python
print(data.head())
```

This line prints the first few rows of the DataFrame `data` using the `head()` method. It displays the content of the CSV file that was read into the DataFrame, providing a preview of the data. The `head()` method by default shows the first 5 rows of the DataFrame.

-----