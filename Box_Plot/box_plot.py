import pandas as pd
import plotly.express as px

data = pd.read_csv(
    "https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv"
)

print(data.head())

figure = px.box(data, y="TV")
figure.show()
