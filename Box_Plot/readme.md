# Box Plot

A box plot is a statistical data visualization technique for analyzing the distribution and patterns of numerical data points of a dataset. It represents quartile 1, quartile 3, median, maximum and minimum data points of a feature which helps to understand the distribution of the numerical values of a dataset.

-----

## Installation

```
pip install pandas
```
Firstly import the `pandas` library through the terminal that will help in the program.
```
pip install plotly
```
Firstly import the `plotly` library through the terminal that will help in the program.

-----

## Code Break:

```python
import pandas as pd
```

This line imports the `pandas` library and aliases it as `pd`. Pandas is a powerful library for data manipulation and analysis.

```python
import plotly.express as px
```

This line imports the `plotly.express` module, a high-level interface for creating various types of plots and charts.

```python
data = pd.read_csv(
    "https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv"
)
```

The `read_csv` function from Pandas is used to read data from a CSV file hosted on GitHub. The data is loaded into a DataFrame named `data`. The CSV file is specified by its URL.

```python
print(data.head())
```

This line prints the first few rows of the DataFrame `data` to the console, providing a preview of the dataset.

```python
figure = px.box(data, y="TV")
```

A box plot is created using Plotly Express (`px.box`). The `data` parameter specifies the DataFrame to use, and `y="TV"` indicates that the "TV" column should be used for the vertical axis in the box plot.

```python
figure.show()
```

The `show` method is called on the `figure` object to display the box plot. This will typically open a new window or render the plot in a Jupyter Notebook environment. The box plot visually represents the distribution of the "TV" column values, including measures like the median, quartiles, and potential outliers.

-----