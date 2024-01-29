# Sunburst Plot

Sunburst plot is an amazing visualization technique used to visualize hierarchical data. It extends radially outward from the root to the leaves to visualize hierarchical data.

-----

## Installation

```
pip install plotly
```
Firstly import the `plotly` library through the terminal that will help in the program.

-----

## Code Break:

```python
import plotly.express as px  # Import the plotly express library for interactive plotting
```

This line imports the `plotly.express` library, which provides an easy-to-use interface for creating a variety of interactive plots.

```python
data = px.data.tips()  # Load the "tips" dataset provided by plotly express
```

This line loads the "tips" dataset from plotly express into a DataFrame named `data`.

```python
figure = px.sunburst(data, path=["day", "sex"], values="total_bill")  # Create a sunburst plot
```

Here, a sunburst plot is created using plotly express's `sunburst` function. The `path` parameter specifies the hierarchical structure of the sunburst plot, and `values` represents the numerical values associated with each category.

```python
figure.show()  # Display the plot
```

Finally, this line displays the created sunburst plot using `figure.show()`. The sunburst plot visualizes the distribution of the "total_bill" values based on the "day" and "sex" categories.

-----