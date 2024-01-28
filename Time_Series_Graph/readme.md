# Time Series Graph

A time-series graph is a `line plot` that displays trends or patterns over a dataset collected over an interval of time.

A time-series graph is a line plot used to visualize time series data. Time-series data is the data collected over an interval of time.

-----

## Installation

```
pip install pandas yfinance plotly
```
Firstly import the `pandas, yfinance, plotly` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import pandas as pd
```
This line imports the Pandas library with the alias `pd`. Pandas is a powerful data manipulation library for Python.

```python
import yfinance as yf
```
This line imports the `yfinance` library, which is used for fetching financial data from Yahoo Finance.

```python
import datetime
from datetime import date, timedelta
```
These lines import the `datetime` module and specific classes (`date` and `timedelta`) from it. These will be used for handling date and time.

```python
import plotly.express as px
```
This line imports the `plotly.express` module, a part of the Plotly library, which is used for creating interactive visualizations.

```python
today = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1
```
Here, it gets the current date using `date.today()` and then formats it as a string in the format "YYYY-MM-DD". This formatted date is assigned to both `d1` and `end_date`.

```python
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2
```
This part calculates a date `360` days ago from today using `timedelta`, formats it, and assigns it to `start_date`.

```python
data = yf.download("AAPL", start=start_date, end=end_date, progress=False)
```
This line uses `yfinance` to download historical stock data for the symbol "AAPL" (Apple Inc.) from the `start_date` to the `end_date`. The data is stored in the `data` variable.

```python
print(data.head())
```
This prints the first few rows of the downloaded data to the console.

```python
figure = px.line(data, x=data.index, y="Close")
```
This line creates a line chart (`px.line`) using the Plotly Express library. It uses the `data` DataFrame, setting the x-axis as the index of the DataFrame (`data.index`) and the y-axis as the "Close" column.

```python
figure.show()
```
This displays the interactive line chart. The `show()` method is used to render the visualization.

-----