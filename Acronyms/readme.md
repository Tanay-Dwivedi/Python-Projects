# Acronyms

An acronym is a short form of a word created by long words or phrases such as NLP for natural language processing.

-----

# Code Break:

```python
word = "United Nations Educational, Scientific and Cultural Organization"
```

This line initializes a string variable `word` with the specified text.

```python
result_string = ""
```

An empty string `result_string` is initialized to store the uppercase letters.

```python
for char in word:
    if char.isupper():
        result_string += char
```

A `for` loop iterates through each character in the `word` string. For each character, it checks if it is an uppercase letter using the `isupper()` method. If true, the character is appended to the `result_string`.

```python
print(result_string)
```

The script prints the `result_string`, which contains only the uppercase letters extracted from the original string.

-----