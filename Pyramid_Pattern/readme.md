# Pyramid Pattern

A pyramid pattern is like a triangle that is not empty,

-----

## Code Break:

```python
def pyramid_pattern(n):
```

This line defines a function named `pyramid_pattern` that takes an integer `n` as a parameter.

```python
    a = 2 * n - 2
```

An auxiliary variable `a` is initialized with the value `2 * n - 2`.

```python
    for i in range(0, n):
```

The function uses a nested loop to iterate over rows. The outer loop runs `n` times for the number of rows.

```python
        for j in range(0, a):
            print(end=" ")
```

The inner loop prints spaces (`" "`) before the stars based on the value of `a`.

```python
        a = a - 1
```

The value of `a` is decremented after each row to reduce the number of spaces in the next row.

```python
        for j in range(0, i + 1):
            print("*", end=" ")
```

Another inner loop prints stars (`"*"`) based on the row number `i`.

```python
        print("\r")
```

A newline is printed after each row to move to the next line.

```python
print(pyramid_pattern(10))
```

The `pyramid_pattern` function is called with the argument `10`, and the pattern is printed to the console. Note that the function itself does not return anything, so `None` is printed by the `print` statement.

-----