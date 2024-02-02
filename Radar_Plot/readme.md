# Radar Plot

A radar plot is also known as a spider plot or a star plot. It is used to display multivariate data as a two-dimensional visualization of quantitative features that are represented on axes coming from the centre.

-----

## Installation

```
pip install plotly pandas
```
Firstly import the `plotly pandas` library through the terminal that will help in the program.

-----

## Code Break:

```python
import plotly.express as px
import pandas as pd
```

Imports the necessary libraries and modules.

```python
data = pd.DataFrame(
    dict(
        keys=[10, 20, 30, 40],
        values=["Labour Cost", "Manufacturing Cost", "Promotion Cost", "Selling Cost"],
    )
)
```

Creates a Pandas DataFrame named `data` with two columns: "keys" and "values". "keys" represents numerical values, and "values" represents corresponding cost categories.

```python
figure = px.line_polar(data, r="keys", theta="values", line_close=True)
```

Uses `plotly.express` to create a polar line chart (`line_polar`). The "keys" column is assigned to the radial coordinate `r`, and the "values" column is assigned to the angular coordinate `theta`. `line_close=True` connects the last point to the first point, creating a closed line.

```python
figure.update_traces(fill="toself")
```

Fills the area enclosed by the polar line chart with color, creating a closed shape. The argument `toself` specifies that the area should be filled with color up to the line itself.

```python
figure.show()
```

Displays the polar line chart with the filled area.

In summary, this script uses `plotly.express` to generate a polar line chart with filled areas, representing different cost categories ("Labour Cost," "Manufacturing Cost," "Promotion Cost," and "Selling Cost") on the chart. The polar line chart visually illustrates the values associated with each category.

-----