# Quicksort

Quicksort is a sorting algorithm that selects an item and rearranges the array forming two partitions so that all items below the item come before and all items above come after. The algorithm is then used recursively to the parts until it gets a sorted list.

-----

## Code Break:

```python
def partition(input_list, low, high):
    i = low - 1
    item = input_list[high]
    for j in range(low, high):
        if input_list[j] <= item:
            i = i + 1
            input_list[i], input_list[j] = input_list[j], input_list[i]
    input_list[i + 1], input_list[high] = input_list[high], input_list[i + 1]
    return i + 1
```
- `partition()` function takes three arguments: `input_list`, `low`, and `high`.
- It initializes `i` as `low - 1`.
- It selects the pivot element (`item`) as the last element of the list.
- It iterates through the elements of the list from `low` to `high - 1`.
- If an element is less than or equal to the pivot, it increments `i` and swaps the current element with `input_list[i]`.
- Finally, it places the pivot element in its correct position and returns the partition index.

```python
def quickSort(input_list, low, high):
    if low < high:
        partition_index = partition(input_list, low, high)
        quickSort(input_list, low, partition_index - 1)
        quickSort(input_list, partition_index + 1, high)
```
- `quickSort()` function takes three arguments: `input_list`, `low`, and `high`.
- It checks if `low` is less than `high`, if not, it returns indicating the sublist is already sorted.
- It calls `partition()` to partition the list and returns the partition index.
- It recursively calls `quickSort()` on the sublists to the left and right of the partition index.

```python
input_l = [9, 3, 5, 2, 6, 8, 6, 1, 3]
list_length = len(input_l)
quickSort(input_l, 0, list_length - 1)

print(input_l)
```
- A sample list `input_l` is defined.
- The length of the list is calculated.
- `quickSort()` is called with `low = 0` and `high = list_length - 1` to sort the list.
- Finally, the sorted list is printed.

-----