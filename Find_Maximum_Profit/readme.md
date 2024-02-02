# Find Maximum Profit

You are given a list of stock prices of a particular day. You need to write an algorithm to find the maximum profit that you can achieve at most two transactions.

-----

## Code Break:

```python
class MaximumProfitFinder:
```

Defines a class named `MaximumProfitFinder`.

```python
    def maximumProfit(self, prices, fees):
```

Defines a method named `maximumProfit` within the class. It takes `prices` (a list of stock prices) and `fees` as parameters.

```python
        def cost(i, n, prev):
```

Defines a helper function `cost` within the `maximumProfit` method. It calculates the cost based on the current index `i`, the total number of prices `n`, and whether the previous transaction occurred (`prev`).

```python
            if i >= n:
                return 0
```

If the index `i` is greater than or equal to the total number of prices `n`, the function returns 0, indicating the end of the recursion.

```python
            elif prev == True:
```

If the previous transaction occurred (`prev` is `True`), the following code block executes.

```python
                return max(
                    cost(i + 1, n, False) + prices[i] - fees, cost(i + 1, n, prev)
                )
```

Calculates the maximum profit considering the option of selling the stock at the current price (`prices[i]`) minus the transaction fees (`fees`) or skipping the current price and moving to the next index.

```python
            else:
```

If the previous transaction did not occur, the following code block executes.

```python
                return max(cost(i + 1, n, True) - prices[i], cost(i + 1, n, prev))
```

Calculates the maximum profit considering the option of buying the stock at the current price (`prices[i]`) and marking the previous transaction as occurred or skipping the current price and moving to the next index without buying.

```python
        return cost(0, len(prices), False)
```

Invokes the `cost` function with initial values: starting from index 0, total number of prices `len(prices)`, and `False` indicating that no previous transaction has occurred.

```python
profit = MaximumProfitFinder()
```

Creates an instance of the `MaximumProfitFinder` class named `profit`.

```python
prices = [10, 20, 30, 40, 50]
```

Defines a list of stock prices named `prices`.

```python
print(profit.maximumProfit(prices, fees=15))
```

Calls the `maximumProfit` method on the `profit` instance, passing the `prices` list and a fee of 15. Prints the result, which represents the maximum profit considering the given stock prices and fees.

-----