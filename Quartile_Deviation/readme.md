# Quartile Deviation

The quartile deviation is the absolute measure of dispersion, where dispersion is the extent to which the values of distribution differ from the mean value of the distribution. If only one very high or low value is present in the data it can still reduce the usefulness of the range as a measure of dispersion.

Quartile deviation means the absolute measure of dispersion. It is the product of half the difference between the upper and lower quartiles
`(Quartile Deviation = (Q3 – Q1)/2)`.

-----

## Installation

```
pip install numpy
```
Firstly import the `numpy` library through the terminal that will help in the program.

-----

# Code Break:

```python
import numpy as np
```

This line imports the NumPy library and gives it the alias `np`.

```python
data = list(range(20, 100, 5))
print(data)
```

This code generates a list named `data` containing values ranging from 20 to 95 with a step of 5 and prints the list.

```python
Q1 = np.quantile(data, 0.25)
Q2 = np.quantile(data, 0.50)
Q3 = np.quantile(data, 0.75)
```

These lines calculate quartiles (Q1, Q2, Q3) using the `np.quantile()` function from NumPy.

```python
print("Quartile 1 : ", Q1)
print("Quartile 2 : ", Q2)
print("Quartile 3 : ", Q3)
```

These lines print the calculated quartiles to the console.

```python
def QuartileDeviation(a, b):
    return (a - b) / 2
```

This defines a function `QuartileDeviation` that takes two parameters and calculates the Quartile Deviation using the formula `(a - b) / 2`.

```python
print("Quartile Deviation: ", QuartileDeviation(Q3, Q1))
```

This line prints the Quartile Deviation by calling the defined function with Q3 and Q1 as arguments.

-----