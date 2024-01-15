# Price Elasticity of Demand

Price is one of the most important factors influencing the demand for a product. `Elasticity` refers to the degree of response, and the price elasticity of demand refers to the degree of responsiveness of demand for a product due to the change in its price.

`Price elasticity` of demand refers to the degree of responsiveness of demand for a product to a change in price. Simply put, it means the degree to which the demand for a product changes with an increase or decrease in its price.

**Formula** - `Percentage Change in Quantity Demanded / Percentage Change in the Price`

-----

## Code Break:

```python
import pandas as pd
```

This line imports the `pandas` library and aliases it as `pd`. Pandas is a powerful library for data manipulation and analysis.

```python
data = pd.DataFrame(
    {
        "Demand": [20, 30, 31, 33, 30, 33, 35],
        "Price": [2000, 1800, 1850, 1700, 1800, 1700, 1600],
    }
)
```

A DataFrame named `data` is created with two columns: "Demand" and "Price". It represents a dataset where each row corresponds to a different point in time with values for demand and price.

```python
print(data)
```

This line prints the original DataFrame `data`, displaying the initial demand and price values.

```python
# The first rows of this dataset contain the initial demand and price for a product, and the subsequent rows contain the change in demand and the change in the price of the product.
```

This is a comment explaining the structure of the dataset.

```python
# Now to add two more columns as the Percentage change in Demand and Percentage change in Price.
```

This comment indicates the intention to calculate percentage changes for demand and price.

```python
data["% Change in Demand"] = data["Demand"].pct_change()
data["% Change in Price"] = data["Price"].pct_change()
```

Two new columns, "% Change in Demand" and "% Change in Price," are added to the DataFrame using the `pct_change()` method. These columns represent the percentage change in demand and price, respectively, from the previous time point.

```python
print(data)
```

This line prints the DataFrame `data` with the newly added columns showing the percentage changes in demand and price.

```python
# the last step is to calculate the price elasticity of demand (% Change in Demand / % Change in Price) by adding a new column to this data.
```

This comment outlines the final step, which involves calculating the price elasticity of demand.

```python
data["Price Elasticity"] = data["% Change in Demand"] / data["% Change in Price"]
```

A new column named "Price Elasticity" is added to the DataFrame, calculated by dividing the "% Change in Demand" by the "% Change in Price." This represents the price elasticity of demand for each time point.

```python
print(data)
```

This line prints the final DataFrame `data` with the added column for price elasticity of demand.

-----