# Get Stock Price Data

Yahoo Finance is one of the most popular websites to collect stock price data. You need to visit the website, enter the company’s name or stock symbol, and you can easily download the dataset. But if you want to get the latest dataset every time you are running your code, you need to use the yfinance API. yfinance is an API provided by Yahoo Finance to collect the latest stock price data.

-----

## Installation

```
pip install yfinance pandas
```
Firstly import the `yfinance, pandas` libraries through the terminal that will help in the program.

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
today = date.today()
```
This line gets the current date using `date.today()` and assigns it to the variable `today`.

```python
d1 = today.strftime("%Y-%m-%d")
end_date = d1
```
Here, it formats the `today` date as a string in the format "YYYY-MM-DD" and assigns it to both `d1` and `end_date`.

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
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
```
Here, a new "Date" column is created in the DataFrame using the index. Then, the DataFrame is filtered to include only specific columns ("Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"). Finally, the index is reset and replaced with a default integer index.

```python
print(data.head())
```
This prints the first few rows of the modified DataFrame to the console.

-----