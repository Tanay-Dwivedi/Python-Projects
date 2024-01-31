# Data Visualization on Map

There are many situations where we need to analyze geospatial data by creating a map of any location in the world. To analyze geospatial data, we just need to plot the latitude and longitude data on a map.

-----

## Installation

```
pip install pandas numpy folium
```
Firstly import the `pandas numpy folium` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import numpy as np
import pandas as pd
import folium as fo
```

These lines import the necessary libraries and modules. `numpy` is used for numerical operations, `pandas` for data manipulation, and `folium` for creating interactive maps.

```python
data = pd.read_csv(
    "https://raw.githubusercontent.com/amankharwal/Website-data/master/Volcano.csv"
)
print(data.head())
```

The script reads volcano data from a CSV file hosted on GitHub using `pandas` and prints the first few rows of the DataFrame to the console.

```python
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Name"])
```

Lists are created from the "Latitude," "Longitude," and "Name" columns of the DataFrame for further processing.

```python
volcano = fo.FeatureGroup(name="Volcano")
for a, b, c in zip(lat, lon, name):
    volcano.add_child(fo.Marker(location=[a, b], popup=c, icon=fo.Icon(color="blue")))
```

A `FeatureGroup` named "Volcano" is created. The script iterates through the lists of latitude, longitude, and volcano names, adding markers for each volcano to the `volcano` feature group. Each marker has a popup displaying the volcano's name and is represented by a blue icon.

```python
fo.Map().add_child(volcano)
```

A Folium map is created, and the `volcano` feature group is added to the map.

In summary, this script reads volcano data from a CSV file, creates a Folium map, and adds markers for each volcano with their names and locations, producing an interactive map.

-----