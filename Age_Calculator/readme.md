# Age Calculator

This python program is an age calculator that takes a user's date of birth as input and calculates and prints their present age in years based on the current date.

-----

## Code Break:

```python
# Import the datetime module
import datetime
```

This line imports the `datetime` module, which provides classes for working with dates and times.

```python
# Define a function for calculating age
def age_calculator(y, m, d):
    today = datetime.datetime.now().date()
    date_of_birth = datetime.date(y, m, d)
    age = int((today - date_of_birth).days / 365.25)
    print("Your present age is", age)
```

Here, a function named `age_calculator` is defined. It takes three arguments (year, month, and day) representing the date of birth. It calculates the age by subtracting the date of birth from the current date and then dividing by 365.25 to account for leap years. The calculated age is printed as output.

```python
# Prompt the user to enter their date of birth
birth_date = input("Enter your DOB in dd-mm-yyyy format: ")
# for example 1999-10-12
```

The user is prompted to enter their date of birth in the specified format (dd-mm-yyyy).

```python
# Extract day, month, and year from the input string
date, month, year = map(int, birth_date.split("-"))
```

The entered date of birth is split using the '-' delimiter, and the resulting values are converted to integers. These values are assigned to the variables `date`, `month`, and `year`.

```python
# Call the age_calculator function with the extracted values
age_calculator(year, month, date)
```

The `age_calculator` function is then called with the extracted values of day, month, and year as arguments to calculate and print the person's age.

-----