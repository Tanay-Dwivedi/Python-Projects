# Calculate Execution Time

 The execution or running time of the program indicates how quickly the output is delivered based on the algorithm you used to solve the problem.

 This Python code generates an acronym from a given phrase by extracting the uppercase characters in the input string. It measures the execution time of this operation and prints both the resulting acronym and the time taken.

-----

## Code Break:

```python
# Import the 'time' function from the 'time' module to measure execution time
from time import time
```
This line imports the `time` function from the `time` module, allowing the program to measure execution time.

```python
# Record the start time before the code execution begins
start = time()
```
Here, the current time is stored in the variable `start` to mark the beginning of the code execution.

```python
# Define the input string
word = "Artificial Intelligence"
```
The variable `word` is assigned the string "Artificial Intelligence," which will be processed to extract capital characters.

```python
# Initialize an empty string to store the capital characters
result_string = ""
```
An empty string `result_string` is initialized to store the extracted capital characters.

```python
# Start a loop that iterates through each character in the input string
for char in word:
    # Check if the current character is an uppercase letter
    if char.isupper():
        # If the character is uppercase, append it to the result_string
        result_string += char
```
This loop iterates through each character in the `word`. If the character is uppercase, it is appended to the `result_string`.

```python
# Print the final result_string containing the capital characters
print(result_string)
```
The final `result_string` containing the extracted capital characters is printed.

```python
# Record the end time after the code execution is completed
end = time()
```
The current time is stored in the variable `end` to mark the end of the code execution.

```python
# Calculate the total execution time by subtracting the start time from the end time
execution_time = end - start
```
The total execution time is calculated by subtracting the `start` time from the `end` time.

```python
# Print the total execution time of the program
print("Execution Time: ", execution_time)
```
The total execution time of the program is printed to the console.

-----