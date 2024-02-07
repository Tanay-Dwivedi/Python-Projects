# Chessboard

A chessboard is the type of game board used for the game of chess, on which pawns and chess pieces are placed. A chessboard is usually square, with an alternating pattern of squares of two colours.

-----

## Installation

```
pip install matplotlib plotly numpy
```
Firstly import the `matplotlib plotly numpy` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import matplotlib.pyplot as plt
```
Imports the `matplotlib.pyplot` module under the alias `plt`.

```python
import numpy as np
```
Imports the `numpy` module under the alias `np`.

```python
from matplotlib.colors import LogNorm
```
Imports the `LogNorm` class from the `matplotlib.colors` module.

```python
dx, dy = 0.015, 0.05
```
Defines the step sizes in the x and y directions.

```python
x = np.arange(-4.0, 4.0, dx)
y = np.arange(-4.0, 4.0, dy)
```
Creates arrays `x` and `y` using NumPy's `arange` function, representing the x and y coordinates within a range from -4.0 to 4.0 with the given step sizes.

```python
X, Y = np.meshgrid(x, y)
```
Creates a grid of coordinates `X` and `Y` using NumPy's `meshgrid` function.

```python
extent = np.min(x), np.max(x), np.min(y), np.max(y)
```
Calculates the extent of the plot in terms of x and y coordinates.

```python
z1 = np.add.outer(range(8), range(8)) % 2
```
Creates a binary pattern using modulus operation on outer addition of two ranges.

```python
plt.imshow(z1, cmap="binary_r", interpolation="nearest", extent=extent, alpha=1)
```
Displays the binary pattern `z1` as an image using `imshow` function with specified colormap (`binary_r`), interpolation method (`nearest`), extent, and alpha value.

```python
def chess(x, y):
    return (1 - x / 2 + x**5 + y**6) * np.exp(-(x**2 + y**2))
```
Defines a function `chess` that computes values for a chessboard pattern based on input x and y coordinates.

```python
z2 = chess(X, Y)
```
Generates the chessboard pattern `z2` by applying the `chess` function to the coordinate grid `X` and `Y`.

```python
plt.imshow(z2, alpha=0.7, interpolation="bilinear", extent=extent)
```
Overlays the chessboard pattern `z2` on top of the binary pattern `z1` with a reduced alpha value for transparency, using bilinear interpolation method.

```python
plt.title("Chess Board with Python")
```
Sets the title of the plot to "Chess Board with Python".

```python
plt.show()
```
Displays the plot.

-----