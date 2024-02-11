# 3D Graphs

The most basic three-dimensional plot is a line or scatter plot created from sets of (x,y,z) triples. In analogy with more common two-dimensional plots, we can create these using the ax.plot3D and ax.scatterd3D functions. The call signature of these is nearly identical to that of their two-dimensional counterparts.

-----

## Installation

```
pip install numpy matplotlib plotly
```
Firstly import the `numpy matplotlib plotly` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import numpy as np
import matplotlib.colors as col
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
```
Imports necessary modules including NumPy for numerical computations, Matplotlib for plotting, and specific modules for three-dimensional plotting.

```python
# Data for a three-dimensional line
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot3D(x, y, z, "grey")
```
Generates data for a three-dimensional line, creates a new figure and subplot with three-dimensional projection, and plots the line using `plot3D()`.

```python
# Data for three-dimensional scattered points
z = 15 * np.random.random(100)
x = np.sin(z) + 0.1 * np.random.randn(100)
y = np.cos(z) + 0.1 * np.random.randn(100)
ax.scatter3D(x, y, z, c=z, cmap="Greens")
plt.show()
```
Generates data for three-dimensional scattered points, and plots them as a scatter plot using `scatter3D()`.

```python
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))
```
Defines a function `f(x, y)` which computes values based on input coordinates `(x, y)`.

```python
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
x, y = np.meshgrid(x, y)
z = f(x, y)
```
Creates a grid of `x` and `y` coordinates using `meshgrid()`, and computes corresponding `z` values using the function `f(x, y)`.

```python
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.contour3D(x, y, z, 50, cmap="binary")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
```
Creates a contour plot of the surface defined by `x`, `y`, and `z` using `contour3D()`.

```python
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_wireframe(x, y, z, color="black")
ax.set_title("wireframe")
plt.show()
```
Creates a wireframe plot of the surface using `plot_wireframe()`.

```python
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap="viridis", edgecolor="none")
ax.set_title("surface")
plt.show()
```
Creates a surface plot of the surface using `plot_surface()`.

-----