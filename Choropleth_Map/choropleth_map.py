import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv("usa.csv")
print(data.head())


figure = go.Figure(
    data=go.Choropleth(
        locations=data["code"],
        z=data["total exports"].astype(float),
        locationmode="USA-states",
        colorscale="Reds",
        colorbar_title="Millions USD",
    )
)


figure.update_layout(title_text="US Agriculture Exports", geo_scope="usa")
figure.show()
