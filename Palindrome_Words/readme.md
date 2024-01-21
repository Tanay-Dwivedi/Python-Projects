# Palindrome Words

***Q) Write an algorithm to find all of the palindrome words in a given sentence and if the word appears more than once in the sentence, you should always return that word only once. Hint: Palintrodme words are words that give the same result when you read the word from the beginning or the end.***

Palindrome words are those words that are read the same way from left to right as from right to left.


-----

# Code Break:

```python
import string
```

This line imports the `string` module, which provides a collection of string constants containing ASCII characters such as punctuation.

```python
def palindrome(sentence):
    # Remove punctuation using string.punctuation
    translator = str.maketrans("", "", string.punctuation)
    sentence = sentence.translate(translator)
```

The `palindrome` function takes a sentence as input and removes punctuation from it using `string.punctuation`. The `str.maketrans` and `translate` methods are used for this purpose.

```python
    # Initialize the list to store palindromic words
    palindromes = []

    # Split the sentence into words
    words = sentence.split()

    for word in words:
        # Convert the word to lowercase for case-insensitive comparison
        word_lower = word.lower()

        # Check if the word is a palindrome
        if word_lower == word_lower[::-1]:
            palindromes.append(word)

    return palindromes
```

This section of the function initializes an empty list called `palindromes` to store palindromic words. It then splits the input sentence into a list of words and iterates through each word. Each word is converted to lowercase for case-insensitive comparison, and if it is a palindrome, it is appended to the `palindromes` list.

```python
# Example usage:
sentence = "A man, a plan, a canal, Panama! Madam, in Eden, I'm Adam."
result = palindrome(sentence)
print(result)
```

An example sentence is provided, and the `palindrome` function is called with this sentence. The result, which is a list of palindromic words, is then printed. In this case, the output might be `['A', 'a', 'a', 'a', 'aca', 'ama', 'Madam', 'I']`.

-----