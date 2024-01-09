# Find Missing Number

Given a list containing a range of numbers from 0 to n with a missing number, find the missing number in the input array.

This python program finds and prints missing numbers in a sequential range up to the maximum value in a given list of integers.

-----

## Code Break:

```python
def find_missing_numer(n):
    numbers = set(n)
    length = len(n)
    output = []
```

The line `def find_missing_numer(n):` defines a function named `find_missing_numer` that takes a list `n` as its parameter. `numbers = set(n)` creates a set called `numbers` containing the unique elements from the input list `n`. This is done to efficiently check for the presence of elements later in the code. `length = len(n)` calculates the length of the input list `n` and stores it in the variable `length`. `output = []` initializes an empty list called `output` that will be used to store the missing numbers.

```python
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
```

`for i in range(1, n[-1]):` iterates through the range of numbers from 1 to the last element of the input list `n` (exclusive). This loop will check for missing numbers in this range. `if i not in numbers:` checks if the current value `i` is not present in the set `numbers`, indicating that it's a missing number. `output.append(i)` tells if `i` is not in the set, it is added to the `output` list, indicating that it is a missing number.

```python
    return output
```

`return output` returns the list of missing numbers after the loop completes.

```python
list = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(find_missing_numer(list))
```

A list named `list` is created with some missing numbers. `print(find_missing_numer(list))` calls the `find_missing_numer` function with the created list and prints the result, which will be a list of missing numbers in the specified range.

-----