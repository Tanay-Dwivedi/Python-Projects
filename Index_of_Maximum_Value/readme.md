# Index of Maximum Value

Finding the index of the maximum value in a list or an array.

-----

## Code Break:

```python
def maximum(x):
```

This line defines a function named `maximum` that takes a list `x` as its parameter.

```python
    maximum_index = 0
    current_index = 1
```

Two variables, `maximum_index` and `current_index`, are initialized. `maximum_index` is the index of the current maximum element, and `current_index` starts from the second element in the list.

```python
    while current_index < len(x):
```

A `while` loop is initiated, which will iterate as long as `current_index` is less than the length of the list `x`.

```python
        if x[current_index] > x[maximum_index]:
            maximum_index = current_index
```

Within the loop, it checks if the element at the current index is greater than the element at the `maximum_index`. If true, it updates `maximum_index` with the current index.

```python
        current_index = current_index + 1
```

The `current_index` is incremented in each iteration of the loop.

```python
    return maximum_index
```

Once the loop is completed, the function returns the index of the maximum element.

```python
a = [23, 76, 45, 20, 70, 65, 15, 54]
print(maximum(a))
```

A list `a` is defined, and the `maximum` function is called with this list as an argument. The result, which is the index of the maximum element, is printed to the console. In this case, it would print the index of the maximum element in the list `a`.

-----