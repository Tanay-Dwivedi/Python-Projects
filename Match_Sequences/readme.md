# Sequence Matcher

This Python script utilizes the difflib library to calculate the similarity ratio between two input sentences. It prompts the user to enter two sentences, computes the similarity score using SequenceMatcher, and prints the percentage
of similarity between the sentences.

-----

## Code Break:

```python
# Import the SequenceMatcher class from the difflib module
from difflib import SequenceMatcher
```

This line imports the `SequenceMatcher` class from the `difflib` module. `SequenceMatcher` is used to compare sequences, such as strings, and compute a similarity ratio.

```python
# Prompt the user to input the first and second sentences
text1 = input("Enter the first sentence: ")
text2 = input("Enter the second sentence: ")
```

Prompt the user to enter two sentences and store them in the variables `text1` and `text2`.

```python
# Calculate the similarity ratio between the input sentences
sequence_score = SequenceMatcher(None, text1, text2).ratio()
```

This line uses `SequenceMatcher` to calculate the similarity ratio between `text1` and `text2`. The result is stored in the variable `sequence_score`.

```python
# Print the similarity score as a percentage
print(f"The entered texts are {sequence_score * 100} % similar")
```

Finally, this section prints the similarity score between the entered texts as a percentage.

-----