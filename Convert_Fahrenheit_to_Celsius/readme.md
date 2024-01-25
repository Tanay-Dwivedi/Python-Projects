# Convert Fahrenheit to Celsius

Calculating temperature conversion is simple. We have to convert the temperature because Celsius and Fahrenheit have different starting points; 0 degrees Celsius is 32 degrees Fahrenheit. So to convert Fahrenheit to degrees Celsius, we just need to subtract 32 from the temperature Fahrenheit.

-----

## Code Break:

```python
def convert(s):
    f = float(s)
    c = (f - 32) * 5 / 9
    return c
```

This part of the code defines a function named `convert` that takes a single parameter `s`, representing the temperature in Fahrenheit. Inside the function:

- `float(s)` converts the input to a floating-point number.
- The formula `(f - 32) * 5 / 9` is used to convert Fahrenheit to Celsius.
- The result `c` is returned.

```python
print(convert(78))
```

This line calls the `convert` function with the argument `78`, which represents a temperature in Fahrenheit. The function calculates the equivalent temperature in Celsius and returns the result. The `print` statement then outputs the calculated Celsius value.

-----