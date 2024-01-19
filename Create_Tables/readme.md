# Create Tables

The `tabulate` module in Python allows us to create and display data in a tabular format which makes the data look more readable. It can be used to organize your data to make it more understandable.

-----

## Installation

```
pip install tabulate
```
Firstly import the `tabulate` library through the terminal that will help in the program.

-----

## Code Break:

```python
from tabulate import tabulate
```

This line imports the `tabulate` function from the `tabulate` module.

```python
data = [
    ["Name", "Place", "Gender"],
    ["Aman", "New Delhi", "Male"],
    ["Hritika", "New Delhi", "Female"],
    ["Krishna", "UP", "Male"],
]
```

A 2D list `data` is defined, representing tabular data with headers ("Name", "Place", "Gender") and corresponding values.

```python
print(tabulate(data))
```

Print the tabulated data using the default format. The table includes headers and rows with aligned columns.

```python
print(tabulate(data, headers="firstrow"))
```

Print the tabulated data with the first row as headers. The output is similar to the first `print` statement, but without the underlines.

```python
print(tabulate(data, headers="firstrow", tablefmt="grid"))
```

Print the tabulated data with the first row as headers and using the "grid" format. The output includes a grid representation of the table.

```python
print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))
```

Print the tabulated data with the first row as headers and using the "fancy_grid" format. The output includes a fancier grid representation of the table.

These examples demonstrate different ways to format and display tabular data using the `tabulate` module. The module allows for customization of headers, formats, and styles when presenting tabular information.

-----