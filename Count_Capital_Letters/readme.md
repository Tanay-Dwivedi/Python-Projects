# Count Capital Letters in a File

Count the number of capital letters from a file

-----

## Code Break:

```python
with open("text.txt", "r") as file:
```

This line opens the file named "text.txt" in read mode (`"r"`) using a `with` statement. The `with` statement ensures that the file is properly closed after reading.

```python
    count = 0
    text = file.read()
```

Inside the `with` block, a variable `count` is initialized to 0, and the entire content of the file is read using the `read()` method and stored in the variable `text`.

```python
    for i in text:
```

A `for` loop iterates through each character in the `text` string.

```python
        if i.isupper():
```

For each character, it checks if the character is an uppercase letter using the `isupper()` method.

```python
            count += 1
```

If the character is an uppercase letter, the `count` variable is incremented by 1.

```python
    print(count)
```

After the loop, the total count of uppercase letters is printed to the console. The output will be the number of uppercase letters present in the file "text.txt".

-----