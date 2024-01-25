# BMI Calculator

The Body Mass Index or BMI is calculated from weight and height of a Person.
The body mass index is calculated by dividing an individual’s weight in kilograms by their height in meters, then dividing the answer again by their height.

-----

## Code Break:

```python
Height = float(input("Enter your height in centimeters: "))
Weight = float(input("Enter your Weight in Kg: "))
```

These lines prompt the user to enter their height and weight. The `float()` function is used to convert the input to floating-point numbers.

```python
Height = Height / 100
BMI = Weight / (Height * Height)
```

These lines convert the height from centimeters to meters and calculate the BMI using the formula: BMI = Weight / (Height * Height).

```python
print("your Body Mass Index is: ", BMI)
```

This line prints the calculated BMI.

```python
if BMI > 0:
    if BMI <= 16:
        print("you are severely underweight")
    elif BMI <= 18.5:
        print("you are underweight")
    elif BMI <= 25:
        print("you are Healthy")
    elif BMI <= 30:
        print("you are overweight")
    else:
        print("you are severely overweight")
else:
    ("enter valid details")
```

This block of code checks the BMI and prints a corresponding classification. The BMI categories are defined as follows:

- BMI <= 16: Severely underweight
- 16 < BMI <= 18.5: Underweight
- 18.5 < BMI <= 25: Healthy weight
- 25 < BMI <= 30: Overweight
- BMI > 30: Severely overweight

The script also includes a check to ensure that the entered details are valid.

However, there's a small issue in the last line:

```python
else:
    ("enter valid details")
```

It should be:

```python
else:
    print("Enter valid details")
```

This line prints a message if the BMI is not greater than 0, indicating that the details entered are not valid.

-----