# Choropleth Map

A choropleth map is a shaded map where the intensity of the colour indicates the `intensity or quantity` of a particular feature. In Data Science, the choropleth maps are used to visualize the distribution of a feature in a geographical area.

-----

## Installation

```
pip install pandas plotly
```
Firstly import the `pandas plotly` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import plotly.graph_objects as go
import pandas as pd
```

These lines import the necessary libraries and modules. `plotly.graph_objects` is used for creating interactive visualizations, and `pandas` is used for data manipulation.

```python
data = pd.read_csv("usa.csv")
print(data.head())
```

The script reads data from a CSV file named "usa.csv" using `pandas` and prints the first few rows of the DataFrame to the console.

```python
figure = go.Figure(
    data=go.Choropleth(
        locations=data["code"],
        z=data["total exports"].astype(float),
        locationmode="USA-states",
        colorscale="Reds",
        colorbar_title="Millions USD",
    )
)
```

A `Figure` object is created using `plotly.graph_objects`. Inside the figure, a `Choropleth` object is added, specifying the locations (`locations`), values (`z`), location mode (`locationmode`), color scale (`colorscale`), and color bar title (`colorbar_title`). The locations correspond to state codes, and the values are the total exports in millions USD.

```python
figure.update_layout(title_text="US Agriculture Exports", geo_scope="usa")
figure.show()
```

The layout of the figure is updated to include a title, "US Agriculture Exports," and set the geographical scope to "usa." Finally, the figure is displayed using `figure.show()`.

In summary, this script reads data on US agriculture exports, creates a choropleth map using Plotly, and displays the map with interactive features. The color of each state on the map represents the total exports of agriculture products in millions of USD.

-----