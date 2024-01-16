# Display a Calendar

The calendar module in Python provides access to the calendar of any month of any year.
There are so many useful built-in modules in Python that can be used to fulfil your goal in a few lines of code. One of these modules in Python is the `calendar` module which provides access to the calendar of any month of any year.

-----

## Code Break:

```python
# Import the calendar module
import calendar
```

This line imports the `calendar` module.

```python
# Prompt the user to enter the year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
```

These lines use the `input()` function to prompt the user to enter the year and month. The entered values are converted to integers using `int()`.

```python
# Print the calendar for the specified month and year
print(calendar.month(year, month))
```

The `calendar.month()` function is used to generate a formatted text representation of the calendar for the specified month (`month`) and year (`year`). This formatted text is then printed to the console.

When you run this script, it will ask you to input the year and month, and then it will display the corresponding calendar.

-----