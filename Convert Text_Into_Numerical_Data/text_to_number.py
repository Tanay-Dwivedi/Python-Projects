import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer()

text = ["Hi, how are you", "I hope you are doing good", "My name is Aman Kharwal"]

vect.fit(text)

train = vect.transform(text)
train.toarray()


data = pd.DataFrame(train.toarray(), columns=vect.get_feature_names())
data
