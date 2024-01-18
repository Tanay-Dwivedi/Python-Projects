# Pick a Random Card

There are so many card games today where you choose a card at random from a deck of cards to create an event. This is the feature of every card game today because you have to choose a card at random and once you choose a card it becomes an event.

Below is a table that shows the type of cards present in a deck of cards:

```
| Spade       | Club       | Diamond    | Heart      |
|-------------|------------|------------|------------|
| 1 King      | 1 King     | 1 King     | 1 King     |
| 1 Queen     | 1 Queen    | 1 Queen    | 1 Queen    |
| 1 Jack      | 1 Jack     | 1 Jack     | 1 Jack     |
| 1 Ace       | 1 Ace      | 1 Ace      | 1 Ace      |
| 2-10 Cards  | 2-10 Cards | 2-10 Cards | 2-10 Cards |
| Total = 13  | Total = 13 | Total = 13 | Total = 13 |
```


-----

# Code Break:

```python
import random
```

This line imports the `random` module, which is used to generate random choices.

```python
cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
```

These lines define lists `cards` and `ranks` representing the suits and ranks in a deck of cards.

```python
def pick_a_card():
```

This line defines a function named `pick_a_card`.

```python
    card = random.choices(cards)
```

Here, `random.choices(cards)` randomly selects a suit from the `cards` list.

```python
    rank = random.choices(ranks)
```

Similarly, `random.choices(ranks)` randomly selects a rank from the `ranks` list.

```python
    return f"The {rank} of {card}"
```

The function returns a formatted string representing the randomly chosen card with its rank and suit.

```python
print(pick_a_card())
```

The `pick_a_card` function is called, and the result (a randomly chosen card) is printed to the console.

-----