import pandas as pd

data = pd.DataFrame(
    {
        "Demand": [20, 30, 31, 33, 30, 33, 35],
        "Price": [2000, 1800, 1850, 1700, 1800, 1700, 1600],
    }
)

print(data)

# The first rows of this dataset contain the initial demand and price for a product, and the subsequent rows contain the change in demand and the change in the price of the product.

# Now to add two more columns as the Percentage change in Demand and Percentage change in Price.

data["% Change in Demand"] = data["Demand"].pct_change()
data["% Change in Price"] = data["Price"].pct_change()
print(data)

# the last step is to calculate the price elasticity of demand (% Change in Demand / % Change in Price) by adding a new column to this data.

data["Price Elasticity"] = data["% Change in Demand"] / data["% Change in Price"]
print(data)
