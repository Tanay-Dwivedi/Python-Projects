import string


def palindrome(sentence):
    # Remove punctuation using string.punctuation
    translator = str.maketrans("", "", string.punctuation)
    sentence = sentence.translate(translator)

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


# Example usage:
sentence = "A man, a plan, a canal, Panama! Madam, in Eden, I'm Adam."
result = palindrome(sentence)
print(result)
