# Read Data From Google Sheets

Google Sheets is an online spreadsheet service from Google that lets you create spreadsheets in the cloud. Reading Google Sheets is different from reading a Microsoft Excel or CSV file using Python.

-----

## Installation

```
pip install oauth2client
```
```
pip install gspread
```
```
pip install --upgrade google-auth
```
Firstly import the `pyspellChecker`, `gspread` and `--upgrade google-auth` libraries through the terminal that will help in the program.

-----

# Code Break:

```python
from google.colab import auth
import pandas as pd
```

These lines import the necessary modules for authentication (`auth` from Google Colab) and handling dataframes (`pd` for Pandas).

```python
auth.authenticate_user()
```

This line authenticates the user in the Google Colab environment.

```python
import requests
import gspread
from oauth2client.client import GoogleCredentials
```

These lines import additional modules for handling HTTP requests (`requests`), accessing Google Sheets (`gspread`), and managing OAuth2 credentials (`GoogleCredentials`).

```python
gc = gspread.authorize(GoogleCredentials.get_application_default())
```

An instance of the `gspread` module is created and authorized using the default application credentials.

```python
sheetname = "enrollment"  # Enter Sheet name without using extension
```

The variable `sheetname` is assigned the name of the Google Sheets document (without the file extension).

```python
sh = gc.open(sheetname)
```

The `gc.open` method is called to open the Google Sheets document with the specified name, and the result is assigned to the variable `sh`.

```python
worksheet = sh.sheet1
```

The `sheet1` attribute of the opened Google Sheets document is accessed and assigned to the variable `worksheet`.

```python
values_list = worksheet.get_all_values()
```

The `get_all_values` method is called on the `worksheet` to retrieve all the values present in the sheet. The result is assigned to the variable `values_list`.

```python
df = pd.DataFrame(values_list)
```

A Pandas DataFrame is created using the values obtained from the Google Sheets document.

```python
df.head()
```

The `head` method is called on the DataFrame to display the first few rows of the data. This provides a quick overview of the data structure.

-----