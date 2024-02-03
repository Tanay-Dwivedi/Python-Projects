import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")
nltk.download("punkt")

text = "Hi, My name is Tanay Dwivedi, I am currently learning and exploring the Data Science field."
tokens = word_tokenize(text)
tokenization = [word for word in tokens if not word in stopwords.words("english")]

print(tokens)
print(tokenization)
