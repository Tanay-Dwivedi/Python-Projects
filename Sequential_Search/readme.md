# Sequential Search

The `Sequential Search algorithm` is a searching algorithm. To implement this algorithm, we start by searching for the target value from the beginning of the array and continue till we find the target value.

For example, imagine that you are trying to find a specific card from a deck of cards. You will go through each card in the deck one by one until you find the card you are looking for. Once you got the card you were looking for you will stop. This is how the sequential search algorithm works.

-----

# Code Break:

```python
def sequential_search(list_, n):
```

This line defines a function named `sequential_search` that takes two parameters: a list `list_` and a value `n` to be searched.

```python
    found = False
```

A variable `found` is initialized to `False` before starting the search.

```python
    for i in list_:
```

A `for` loop is used to iterate through each element `i` in the input list `list_`.

```python
        if i == n:
            found = True
            break
```

Within the loop, if the current element `i` is equal to the target value `n`, the `found` variable is set to `True`, and the loop is terminated using the `break` statement.

```python
    return found
```

After the loop, the function returns the final value of the `found` variable, indicating whether the target value was found in the list.

```python
numbers = list(range(0, 20))
```

A list of numbers ranging from 0 to 19 is created.

```python
print(sequential_search(numbers, 3))
```

The `sequential_search` function is called with the list of numbers and the value `3` to search. The result (`True` or `False`) is printed to the console.

-----