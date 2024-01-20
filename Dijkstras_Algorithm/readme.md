# Dijkstra’s Algorithm

Dijkstra’s algorithm is also known as the single-source shortest path algorithm. It is used for finding the shortest path between the nodes of a graph where the cost of each path is not the same.
Dijkstra’s algorithm is used to find the shortest path between the nodes of a graph. In real-world applications, it is used to automatically find directions between physical locations, as the directions you get on Google Maps is an example of Dijkstra’s algorithm.


-----

## Code Break:

```python
from heapq import *
from collections import defaultdict
```

These lines import necessary modules (`heapq` for the heap queue algorithm and `defaultdict` for creating a dictionary with default values).

```python
def dijkstra(edges, start_node, end_node):
```

This line defines a function named `dijkstra` that takes a list of edges, a start node, and an end node as parameters.

```python
    g = defaultdict(list)
    for start, end, weight in edges:
        g[start].append((weight, end))
```

A defaultdict named `g` is created to represent the graph. It is filled with information from the provided edges, where each start node has a list of tuples representing connected nodes and their weights.

```python
    q, visited = [(0, start_node, ())], set()
```

A priority queue (`q`) is initialized with a tuple containing the starting cost (0), the start node, and an empty tuple representing the path. `visited` is set to an empty set to keep track of visited nodes.

```python
    while q:
        (cost, v1, path) = heappop(q)
```

A loop starts, and in each iteration, the tuple with the minimum cost is popped from the priority queue.

```python
        if v1 not in visited:
            visited.add(v1)
            path = (v1, path)
```

If the current node (`v1`) has not been visited, it is marked as visited, and the current node is added to the path.

```python
            if v1 == end_node:
                return (cost, path)
```

If the current node is the end node, the function returns the cost and path tuple.

```python
            for c, v2 in g.get(v1, ()):
                if v2 not in visited:
                    heappush(q, (cost + c, v2, path))
```

For each connected node (`v2`) to the current node, if it has not been visited, a new tuple is pushed into the priority queue with an updated cost and path.

```python
        print(q)
```

This line prints the current state of the priority queue during each iteration for illustration purposes.

```python
    return float("inf")
```

If the end node is not reached, the function returns positive infinity.

```python
edges = [
    ("A", "B", 7),
    ("A", "D", 5),
    ("B", "C", 8),
    ("B", "D", 9),
    ("B", "E", 7),
    ("C", "E", 5),
    ("D", "E", 7),
    ("D", "F", 6),
    ("E", "F", 8),
    ("E", "G", 9),
    ("F", "G", 11),
]
```

A list of edges representing a graph is provided for testing.

```python
print("=== Dijkstra ===")
print("A >> G:")
print(dijkstra(edges, "A", "G"))
```

The `dijkstra` function is called with the provided edges, start node "A," and end node "G." The result (cost and path) is printed to the console. The print statements provide a simple explanation of what the function is calculating.

-----