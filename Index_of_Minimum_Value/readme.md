# Index of Minimum Value

-----

## Code Break:

```python
def minimum(x):
```

This line defines a function named `minimum` that takes a list `x` as its parameter.

```python
    minimum_index = 0
    current_index = 1
```

Two variables, `minimum_index` and `current_index`, are initialized. `minimum_index` is the index of the current minimum element, and `current_index` starts from the second element in the list.

```python
    while current_index < len(x):
```

A `while` loop is initiated, which will iterate as long as `current_index` is less than the length of the list `x`.

```python
        if x[current_index] < x[minimum_index]:
            minimum_index = current_index
```

Within the loop, it checks if the element at the current index is less than the element at the `minimum_index`. If true, it updates `minimum_index` with the current index.

```python
        current_index = current_index + 1
```

The `current_index` is incremented in each iteration of the loop.

```python
    return minimum_index
```

Once the loop is completed, the function returns the index of the minimum element.

```python
a = [23, 76, 45, 20, 70, 65, 15, 54]
print(minimum(a))
```

A list `a` is defined, and the `minimum` function is called with this list as an argument. The result, which is the index of the minimum element, is printed to the console. In this case, it would print the index of the minimum element in the list `a`.

-----