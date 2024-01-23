# Story Generator

This script generates a random story by selecting elements from predefined lists for various components of the story, such as when, who, name, residence, went, and happened. It then prints the randomly generated story.

-----

## Code Break:

```python
import random
```

This line imports the `random` module, which is used to generate random choices.

```python
when = ["A few years ago", "Yesterday", "Last night", "A long time ago", "On 20th Jan"]
who = ["a rabbit", "an elephant", "a mouse", "a turtle", "a cat"]
name = ["Ali", "Miriam", "daniel", "Hoouk", "Starwalker"]
residence = ["Barcelona", "India", "Germany", "Venice", "England"]
went = ["cinema", "university", "seminar", "school", "laundry"]
happened = [
    "made a lot of friends",
    "Eats a burger",
    "found a secret key",
    "solved a mistery",
    "wrote a book",
]
```

These lines define lists containing different options for each component of the story: when, who, name, residence, went, and happened.

```python
print(
    random.choice(when)
    + ", "
    + random.choice(who)
    + " that lived in "
    + random.choice(residence)
    + ", went to the "
    + random.choice(went)
    + " and "
    + random.choice(happened)
)
```

This line uses `random.choice()` to randomly select one item from each list and constructs a story by concatenating these selected items with appropriate strings. Finally, it prints the randomly generated story.

-----