# Count Rainy Days

A numerical computational task with Python to count rainy days with python. Imagine you have a data series that represents the amount of precipitation each day for a year in a given city.

-----

## Installation

```
pip install numpy pandas matplotlib plotly seaborn
```
Firstly import the `numpy pandas matplotlib plotly seaborn` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
```
These lines import the necessary libraries for data manipulation (`numpy` and `pandas`), data visualization (`matplotlib.pyplot` and `seaborn`), and numerical operations (`numpy`).

```python
data = pd.read_csv("Seattle2014.csv")
print(data.head())
```
This code reads the data from the CSV file "Seattle2014.csv" into a pandas DataFrame named `data`. It then prints the first few rows of the DataFrame using the `head()` method to inspect the structure and content of the data.

```python
rainfall = data["PRCP"].values
inches = rainfall / 254
print(inches.shape)
```
These lines extract the "PRCP" column from the DataFrame `data`, representing rainfall data, and store it as a NumPy array `rainfall`. The values in `rainfall` are converted from tenths of millimeters to inches by dividing by 254, as there are 25.4 millimeters in an inch. The shape of the resulting array `inches` is printed to inspect its dimensions.

```python
seaborn.set()
plt.hist(inches, 40)
plt.show()
```
These lines configure the default style settings for seaborn with `seaborn.set()` and then create a histogram of the `inches` data with 40 bins using `plt.hist()`. The histogram is displayed using `plt.show()`.

```python
print("Number of days without rain: ", np.sum(inches == 0))
print("Number of days with rain: ", np.sum(inches != 0))
print("Number of days with rain more than 0.5 inches: ", np.sum(inches > 0.5))
print("Number of days with rain < 0.2 inches: ", np.sum((inches > 0) & (inches < 0.2)))
```
These lines calculate and print various statistics based on the `inches` data using NumPy's array operations:
- The number of days without rain (where `inches` equals 0).
- The number of days with rain (where `inches` is not equal to 0).
- The number of days with rain more than 0.5 inches.
- The number of days with rain less than 0.2 inches, using a logical AND operation between two conditions.

-----