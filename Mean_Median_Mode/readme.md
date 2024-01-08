# Mean, Median & Mode

This Python program calculates and prints the mean, median, and mode of a given list of numbers using the statistics module.

Mean - The mean is the average value of all the values in a dataset. To calculate the mean value of a dataset, we first need to find the sum of all the values and then divide the sum of all the values by the total number of values.

Median - The Median is the middle value among all the values in sorted order. Here we need to calculate the mid-value of all the values in a dataset. But before calculating the Median, we need to arrange all the values in sorted order.
There are two different ways of calculating the median value:
- when the total number of values is even: Median  = `[(n/2)th term + {(n/2)+1}th]/2`
- when the total number of values is odd: Median = `{(n+1)/2}thterm`

Mode - Mode is the most frequently occurring value among all the values.

-----

## Code Break :

### Mean - 

```python
# Import the statistics module
import statistics
```

This line imports the `statistics` module, which provides statistical functions for calculating mean, median, mode, and other measures.

```python
# Create a list of numbers
list = [24, 35, 12, 78, 44, 95, 10]
```

Here, a list named `list` is created, containing the numbers `[24, 35, 12, 78, 44, 95, 10]`. However, using `list` as a variable name is generally not recommended as it shadows the built-in `list` type.

```python
# Calculate the mean of the list using the mean() function from the statistics module
mean_value = statistics.mean(list)
```

The `statistics.mean()` function is applied to the list to calculate its mean. The result is stored in a variable named `mean_value`.

```python
# Print the result
print("The mean of the given list is:", mean_value)
```

Finally, the result is printed using the `print()` function. It outputs the string "The mean of the given list is:" followed by the value stored in the `mean_value` variable.

So, when you run this code, it will import the `statistics` module, create a list of numbers, calculate the mean of the list, and print the result along with a descriptive message.

### Median - 

```python
# Import the statistics module
import statistics
```

This line imports the `statistics` module, which contains various statistical functions, including the `median()` function.

```python
# Create a list of numbers
list = [24, 35, 12, 78, 44, 95, 10]
```

Here, a list named `list` is created, containing the numbers `[24, 35, 12, 78, 44, 95, 10]`.

```python
# Calculate the median of the list using the median() function from the statistics module
median_value = statistics.median(list)
```

The `statistics.median()` function is applied to the list to calculate its median. The result is stored in a variable named `median_value`.

```python
# Print the result
print("The median of the given list is:", median_value)
```

Finally, the result is printed using the `print()` function. It outputs the string "The median of the given list is:" followed by the value stored in the `median_value` variable.

So, this code calculates and prints the median of the provided list. The median is the middle value of a sorted list, or the average of the two middle values if the list has an even number of elements.

### Mode -

```python
# Import the statistics module
import statistics
```

This line imports the `statistics` module, which provides various statistical functions, including the `mode()` function.

```python
# Create a list of numbers
list = [23, 45, 23, 45, 44, 12, 21, 45]
```

Here, a list named `list` is created, containing the numbers `[23, 45, 23, 45, 44, 12, 21, 45]`.

```python
# Calculate the mode of the list using the mode() function from the statistics module
mode_value = statistics.mode(list)
```

The `statistics.mode()` function is applied to the list to calculate its mode. The result is stored in a variable named `mode_value`.

```python
# Print the result
print("The mode of the given list is:", mode_value)
```

Finally, the result is printed using the `print()` function. It outputs the string "The mode of the given list is:" followed by the value stored in the `mode_value` variable.

The mode of a list is the value that appears most frequently. If there is no unique mode (i.e., multiple values have the same highest frequency), the `statistics.mode()` function raises a `StatisticsError`.

-----