# Reverse String

This Python script defines a function to reverse a given string and then demonstrates its usage by taking user input, reversing the input string, and printing the result.

-----

## Code Break:

```python
# Define a function to reverse a string
def reverse_string(string):
    return string[::-1]
```

This section defines a function named `reverse_string` that takes a string as input and returns its reversed version using slicing (`[::-1]`).

```python
# Prompt the user to input a string and store it in the variable 'a'
a = input("Enter the string: ")
```

Prompt the user to enter a string, and store the input in the variable `a`.

```python
# Call the reverse_string function with the user-input string 'a'
# Print the reversed string along with a descriptive message
print("The reversed string is", reverse_string(a))
```

This section calls the `reverse_string` function with the user-input string `a` and prints the reversed string along with a descriptive message.

-----