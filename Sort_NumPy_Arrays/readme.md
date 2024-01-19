# Sort NumPy Arrays

The sort function in the NumPy library works the same as the sort function in the Python programming language.

-----

## Installation

```
pip install numpy
```
Firstly import the `numpy` library through the terminal that will help in the program.

-----

## Code Break:

```python
# Method 1 - using inbuilt method

import numpy as np

a = np.array([34, 5, 89, 23, 76])
# Use the np.sort() function to sort the NumPy array 'a'
print(np.sort(a))
```

In Method 1, the NumPy library is utilized to sort the array `a` using the `np.sort()` function. The sorted result is printed to the console.

```python
# Method 2 - using logic

def sorting(x):
    for i in range(len(x)):
        # Find the index of the minimum element in the remaining unsorted part of the array
        swap = i + np.argmin(x[i:])
        # Swap the current element with the minimum element
        (x[i], x[swap]) = (x[swap], x[i])
    return x

# Call the sorting function with the array 'a'
print(sorting(a))
```

In Method 2, a sorting function (`sorting`) is defined using a selection sort algorithm. It iterates through the array, finds the index of the minimum element in the remaining unsorted part, and swaps the current element with the minimum element. The sorted result is printed to the console. Note that this method demonstrates a basic sorting algorithm for educational purposes and may not be as efficient as built-in sorting functions for larger datasets.

-----