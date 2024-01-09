# Group Anagrams

*Anagrams* are words formed by rearranging the letters of another word

The code groups a list of words into sets of anagrams. It uses a `defaultdict` to create groups based on the sorted characters of each word. The resulting groups are then printed. The primary use case is to identify and group words that are anagrams of each other.

-----

## Code Break:

```python
# Import defaultdict from the collections module
from collections import defaultdict
```

This line imports the `defaultdict` class from the `collections` module.

```python
# Define a function to group anagrams
def group_anagram(a):
    # Create a defaultdict with lists as default values
    grouped = defaultdict(list)
    
    # Iterate over each word in the input list
    for i in a:
        # Sort the characters of the word and join them into a single string
        sorted_word = " ".join(sorted(i))
        
        # Use the sorted word as the key to group anagrams
        grouped[sorted_word].append(i)
    
    # Return the values (lists of anagrams) from the defaultdict
    return grouped.values()
```

This part defines the `group_anagram` function. It initializes a `defaultdict` where the default value is an empty list. It then iterates over each word in the input list, sorts its characters, and joins them into a string. This sorted string is used as the key to group anagrams in the defaultdict.

```python
# List of words
words = ["tea", "eat", "bat", "ate", "arc", "car"]
```

Here, a list of words is defined.

```python
# Call the group_anagram function with the list of words and print the result
print(group_anagram(words))
```

The `group_anagram` function is called with the list of words, and the result is printed. The output will be a list of lists, where each inner list contains words that are anagrams of each other based on the provided input list.

-----
