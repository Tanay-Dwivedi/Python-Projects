from GoogleNews import GoogleNews
import pandas as pd

news = GoogleNews(period="1d")
news.search("India")
result = news.result()


data = pd.DataFrame.from_dict(result)
data = data.drop(columns=["img"])
data.head()


for i in result:
    print("Title : ", i["title"])
    print("News : ", i["desc"])
    print("Read Full News : ", i["link"])
