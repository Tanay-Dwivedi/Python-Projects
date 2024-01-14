import csv
import pandas as pd

data = {
    "Name": ["Aman", "Diksha", "Akanksha", "Sajid", "Akshit"],
    "Age": [23, 21, 25, 23, 22],
}

data = pd.DataFrame(data)
data.to_csv("data.csv", index=False)

print(data.head())
