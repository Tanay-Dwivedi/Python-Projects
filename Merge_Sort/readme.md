# Merge Sort

To sort an array we need to arrange the elements of the array by comparing each element efficiently. The merge sort algorithm uses the divide and conquer approach to sort an array by making the least number of comparisons between the elements of an array.

-----

# Code Break:

```python
def merge(listA, listB):
```

This line defines a function named `merge` that takes two sorted lists (`listA` and `listB`) and merges them into a new sorted list (`newlist`).

```python
    newlist = list()
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newlist.append(listA[a])
            a += 1
        else:
            newlist.append(listB[b])
            b += 1
```

Here, a new list (`newlist`) is initialized, and two pointers (`a` and `b`) are used to iterate through `listA` and `listB`. The while loop compares elements at the current positions and appends the smaller one to `newlist`. The pointers are incremented accordingly.

```python
    while a < len(listA):
        newlist.append(listA[a])
        a += 1
```

This part handles the remaining elements in `listA` if any.

```python
    while b < len(listB):
        newlist.append(listB[b])
        b += 1
```

This part handles the remaining elements in `listB` if any.

```python
    return newlist
```

The merged and sorted list (`newlist`) is returned.

```python
def merge_sort(input_list):
```

This line defines a function named `merge_sort` that implements the merge sort algorithm. It takes an input list (`input_list`).

```python
    if len(input_list) <= 1:
        return input_list
```

If the length of the input list is 1 or less, it is considered already sorted, and the function returns the input list.

```python
    else:
        mid = len(input_list) // 2
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])
        newlist = merge(left, right)
```

If the input list is longer, it calculates the middle index (`mid`) and recursively applies `merge_sort` to the left and right halves. The sorted halves are then merged using the `merge` function.

```python
        return newlist
```

The sorted and merged list is returned.

```python
a = [56, 89, 45, 34, 90, 32, 20, 67, 43]
```

This line initializes an example list `a` that you want to sort using merge sort.

```python
print(merge_sort(a))
```

The `merge_sort` function is called with the list `a`, and the sorted result is printed to the console.

-----