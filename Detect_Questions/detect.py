import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize

question_words = [
    "what",
    "why",
    "when",
    "where",
    "name",
    "is",
    "how",
    "do",
    "does",
    "which",
    "are",
    "could",
    "would",
    "should",
    "has",
    "have",
    "whom",
    "whose",
    "don't",
]

question_input = input("Enter a sentence: ")
question_input = question_input.lower()
question_input = word_tokenize(question_input)

if any(x in question_input[0] for x in question_words):
    print("This is a question!")
else:
    print("This is not a question!")
