# Count Character Occurrences

Counting occurrences of a character in a string means counting all substrings of a character from the input string.

-----

## Code Break:

```python
def count_characters(s):
```

This line defines a function named `count_characters` that takes a string `s` as a parameter.

```python
    count = {}
```

A dictionary named `count` is initialized to store the count of each character in the string.

```python
    for i in s:
```

A for loop is used to iterate through each character `i` in the input string `s`.

```python
        if i in count:
            count[i] += 1
```

If the character `i` is already a key in the dictionary `count`, its count is incremented.

```python
        else:
            count[i] = 1
```

If the character `i` is not in the dictionary, a new key is created with a count of 1.

```python
    print(count)
```

The final dictionary containing the count of each character is printed to the console.

```python
print(count_characters("Tanay Dwivedi"))
```

The `count_characters` function is called with the string "Tanay Dwivedi" as an argument, and the result (the count of each character) is printed to the console.

-----