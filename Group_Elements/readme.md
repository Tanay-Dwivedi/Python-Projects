# Group Elements by Indices

Grouping elements of the same indices means grouping elements of two or more data structures according to their indices.
This Python program performs matrix transposition on a 3x3 matrix. 
It takes the input matrix and creates a new matrix where the rows of the original matrix become columns in the transposed matrix. The transposed columns are then unpacked into variables a, b, and c, and these variables are printed. The output represents the columns of the transposed matrix.

----

## Code Break:

```python
# Define a 2D list named list1
list1 = [[10,20,30], [40,50,60], [70,80,90]]
```
This line initializes a 2D list named `list1` with three inner lists, each representing a row of a matrix.

```python
# Initialize an empty list named list2
list2 = []
```
Here, an empty list named `list2` is initialized. This list will store the transposed matrix.

```python
# Initialize an index variable to keep track of the current column in the transposed matrix
index = 0
```
The code sets up an index variable to keep track of the current column during the transposition process.

```python
# Iterate over the columns of the original matrix
for i in range(len(list1[0])):
    # Append an empty list to list2 for each column
    list2.append([])
    # Iterate over the rows of the original matrix
    for j in range(len(list1)):
        # Extract the corresponding element from each row and append it to the newly added list in list2
        list2[index].append(list1[j][index])
        # Increment the index variable
        index = index + 1

```
The code starts an outer loop that iterates over the columns of the original matrix (`list1`). Inside the outer loop, an empty list is appended to `list2` for each column, initializing the structure for the transposed matrix. An inner loop begins, iterating over the rows of the original matrix. Within the inner loop, the code extracts the corresponding element from each row of the original matrix and appends it to the newly added list in `list2`. After processing each column, the index variable is incremented, preparing for the next column. 

```python
# Unpack the transposed lists into variables a, b, and c
a, b, c = list2[0], list2[1], list2[2]
```
The transposed lists are unpacked into variables `a`, `b`, and `c`. Each variable represents a column of the transposed matrix.

```python
# Print the transposed lists
print(a, b, c)
```
Finally, the transposed columns of the original matrix are printed. The output will be the transposed matrix columns.

-----