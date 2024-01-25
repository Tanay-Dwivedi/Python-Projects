# Convert Roman Numbers to Decimals

The process of converting roman numbers to decimals:

- Work your way through the string of Roman numerals from left to right, examining two adjacent characters at a time. If you want then you can also specify that the direction of loops, but it does not matter as long as the comparisons are implemented accordingly.
- If the value on the left is higher than the value on the right, then subtract the count at that position from the final value. Otherwise, just add it.
- Once the process is complete, the final value is the decimal value equivalent of the roman number.

-----

## Code Break:

```python
tallies = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
```

This dictionary `tallies` stores the Roman numerals as keys and their corresponding decimal values as values.

```python
def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNumeral[-1]]
    return sum
```

This function `RomanNumeralToDecimal` takes a Roman numeral string as input and iterates through the characters. It compares adjacent characters and adjusts the sum accordingly based on the Roman numeral rules. The final result is the decimal equivalent of the Roman numeral.

```python
result = RomanNumeralToDecimal("XIV")
```

This line calls the function with the Roman numeral "XIV" and stores the result in the variable `result`.

```python
print(f"The decimal equivalent is: {result}")
```

This line prints the decimal equivalent of the Roman numeral "XIV" using an f-string.

-----