# Count Most Frequent Words

Counting the number of specific words in a file.

-----

# Code Break:

```python
from collections import Counter
```

This line imports the `Counter` class from the `collections` module. `Counter` is used to count the occurrences of elements in a collection.

```python
words = []
```

An empty list named `words` is created to store the words read from the file.

```python
with open("file name.txt", "r") as f:
```

This line opens the file named "file name.txt" in read mode (`"r"`) using a `with` statement. The `with` statement ensures that the file is properly closed after reading.

```python
    for line in f:
```

A `for` loop iterates through each line in the file.

```python
        words.extend(line.split())
```

For each line, the `split()` method is used to split the line into a list of words, and the `extend()` method is used to add these words to the `words` list.

```python
counts = Counter(words)
```

The `Counter` class is used to count the occurrences of each word in the `words` list, creating a dictionary-like object where keys are words, and values are their counts.

```python
top5 = counts.most_common(5)
```

The `most_common()` method is called on the `Counter` object to retrieve the five most common words and their frequencies. The result is stored in the `top5` variable.

```python
print(top5)
```

This line prints the five most common words and their frequencies to the console. The output will be a list of tuples, where each tuple contains a word and its count, sorted in descending order of frequency.

-----