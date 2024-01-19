# Recursive Binary Search

Recursion means solving problems by breaking down a complex problem into smaller problems and then solving it step by step.
Binary search means to find an item in a sorted array by repeatedly dividing the search interval into two halves and recursive binary search means to subdivide the entire binary search process into smaller problems.

Here are the properties that all recursive solutions must satisfy:

- A recursive solution must have a base case.
- A recursive solution must have a recursive case.
- A recursive solution must make progress towards the base case.

-----

## Code Break:

```python
def rec_binarySearch(target, sequence, first, last):
```

This line defines a recursive binary search function named `rec_binarySearch`. It takes four parameters: `target` (the value to search for), `sequence` (the sorted sequence to search in), `first` (the index of the first element in the current search range), and `last` (the index of the last element in the current search range).

```python
    if first > last:
        return False
```

If the `first` index is greater than the `last` index, it means the search range is empty, and the function returns `False` indicating that the target is not present in the sequence.

```python
    else:
        mid = (last + first) // 2
```

If the search range is not empty, the function calculates the middle index (`mid`) of the current search range.

```python
        if sequence[mid] == target:
            return True
```

If the value at the middle index is equal to the target, the function returns `True` indicating that the target is found in the sequence.

```python
        elif target < sequence[mid]:
            return rec_binarySearch(target, sequence, first, mid - 1)
```

If the target is less than the value at the middle index, the function recursively calls itself with the updated search range from `first` to `mid - 1`.

```python
        else:
            return rec_binarySearch(target, sequence, mid + 1, last)
```

If the target is greater than the value at the middle index, the function recursively calls itself with the updated search range from `mid + 1` to `last`.

```python
# Example usage:
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = rec_binarySearch(target, sequence, 0, len(sequence) - 1)
```

An example usage of the `rec_binarySearch` function with a sorted sequence `[1, 2, 3, 4, 5, 6, 7, 8, 9]` and a target value of `5`.

```python
if result:
    print(f"{target} is present in the sequence.")
else:
    print(f"{target} is not present in the sequence.")
```

Prints whether the target value is present or not in the sequence based on the result of the binary search. In this case, it prints that `5` is present in the sequence.

-----