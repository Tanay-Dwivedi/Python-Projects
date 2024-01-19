# Validate Anagrams

An Anagram is a word or phrase that forms a different word or phrase when the letters of a word are rearranged.

-----

## Code Break:

```python
def anagram(word1, word2):
```

This line defines a function named `anagram` that takes two words (`word1` and `word2`) as parameters.

```python
    word1 = word1.lower()
    word2 = word2.lower()
```

Convert both words to lowercase to ensure a case-insensitive comparison.

```python
    return sorted(word1) == sorted(word2)
```

Check if the sorted list of characters in `word1` is equal to the sorted list of characters in `word2`. If they are equal, the function returns `True`, indicating that the words are anagrams; otherwise, it returns `False`.

```python
print(anagram("cinema", "iceman"))
```

Test the `anagram` function with the words "cinema" and "iceman". The result is printed to the console (`True`).

```python
print(anagram("cool", "loco"))
```

Test the `anagram` function with the words "cool" and "loco". The result is printed to the console (`True`).

```python
print(anagram("men", "women"))
```

Test the `anagram` function with the words "men" and "women". The result is printed to the console (`False`).

-----