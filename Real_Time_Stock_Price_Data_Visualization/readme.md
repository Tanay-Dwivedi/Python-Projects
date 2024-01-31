# Real-time Stock Price Data Visualization

To create a realtime stock price data visualization application, I will be using the streamlit library in Python. In this task, we can use the streamlit library to create an interactive user interface where a user will enter the name of any company and the stock price data will be visualized.
For the task of visualizing stock prices, we can use any data visualization library in Python compatible with the streamlit framework.

-----

## Installation

```
pip install pandas pandas-datareader matplotlib plotly streamlit
```
Firstly import the `pandas pandas-datareader matplotlib plotly streamlit` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
from datetime import date, timedelta
import streamlit as st
```

These lines import the necessary libraries and modules. `pandas` and `pandas_datareader` are used for data manipulation and fetching financial data, `matplotlib` for plotting, `datetime` for working with dates, and `streamlit` for creating web applications.

```python
today = date.today()
d1 = today.strftime("%Y/%m/%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y/%m/%d")
start_date = d2
```

The script obtains today's date and the date 360 days ago, formatting them as strings in the "YYYY/MM/DD" format. These dates are used to define the start and end dates for fetching stock price data.

```python
st.title("Real-time Stock Price Data")
a = st.text_input("Enter Any Company >>:")
```

A Streamlit application is created with a title and an input box for the user to enter the name of a company.

```python
data = web.DataReader(name=a, data_source="yahoo", start=start_date, end=end_date)
```

Using `pandas_datareader`, the script fetches stock price data for the specified company (`a`) from Yahoo Finance for the specified date range.

```python
fig, ax = plt.subplots()
ax = data["Close"].plot(
    figsize=(12, 8), title=a + " Stock Prices", fontsize=20, label="Close Price"
)
plt.legend()
plt.grid()
st.pyplot(fig)
```

A Matplotlib figure is created, and the closing prices from the fetched data are plotted. The resulting plot is displayed using `st.pyplot()` within the Streamlit application.

In summary, the script creates a simple Streamlit application that allows users to input a company name and fetches and displays real-time stock price data using the Yahoo Finance API. The stock prices are plotted using Matplotlib within the Streamlit web interface.

-----