# Distance Between Two Locations

Calculating the distance between two locations helps companies like Swiggy and Zomato calculate the delivery time for an order

We can use the `Haversine formula` to calculate the distance between two locations. The haversine formula calculates the distance between two latitude and longitude points. This formula is defined as:


\[ \text{haversine}\left(\frac{d}{R}\right) = \text{haversine}(\text{latitude}_2 - \text{latitude}_1 + \cos(\text{latitude}_1) \cdot \cos(\text{latitude}_2) \cdot \text{haversine}(\text{longitude}_2 - \text{longitude}_1) \]


-----

## Code Break:

```python
import numpy as np
```
This line imports the NumPy library with the alias `np`. NumPy is commonly used for numerical operations in Python.

```python
# Set the earth's radius (in kilometers)
r = 6371
```
This line initializes a variable `r` with the value 6371, representing the Earth's radius in kilometers.

```python
# Convert degrees to radians
def deg_to_rad(degrees):
    return degrees * (np.pi / 180)
```
Here, a function `deg_to_rad` is defined to convert degrees to radians. It takes a parameter `degrees` and returns the corresponding value in radians.

```python
# Function to calculate the distance between two points
# using the haversine formula
def distcalculate(lat1, lon1, lat2, lon2):
    d_lat = deg_to_rad(lat2 - lat1)
    d_lon = deg_to_rad(lon2 - lon1)
    a = (
        np.sin(d_lat / 2) ** 2
        + np.cos(deg_to_rad(lat1)) * np.cos(deg_to_rad(lat2)) * np.sin(d_lon / 2) ** 2
    )
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return r * c
```
This part defines a function `distcalculate` that computes the distance between two geographical points using the Haversine formula. It takes latitude and longitude coordinates for two points as parameters (`lat1`, `lon1`, `lat2`, `lon2`). The function first converts the differences in latitude and longitude to radians using `deg_to_rad`. Then, it calculates intermediate values (`a` and `c`) based on the Haversine formula and computes the final distance using Earth's radius (`r`). The result is returned as the distance between the two points.

```python
print(distcalculate(22.745049, 75.892471, 22.765049, 75.912471))
```
This line prints the distance between two geographical points with specific latitude and longitude coordinates using the `distcalculate` function. The output of this specific example is printed to the console.

-----