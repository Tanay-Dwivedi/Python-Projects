# Treemap

A treemap is used to visualize hierarchical data as a set of nested rectangles. It is a data visualization tool for displaying data structured in a tree structure using nested rectangles.
A treemap displays hierarchical data in such a way that each branch of the tree receives a rectangle which is filled with smaller rectangles as sub-branches.

-----

## Code Break:

```python
import plotly.graph_objects as go
```

This line imports the necessary module from Plotly for creating graph objects.

```python
fig = go.Figure(
    go.Treemap(
        labels=["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        parents=["", "A", "A", "C", "C", "A", "A", "G", "A"],
    )
)
```

This code creates a `Figure` object with a single trace, which is a `Treemap`. The `labels` parameter provides the labels for each rectangle, and the `parents` parameter specifies the parent of each rectangle in the hierarchy.

```python
fig.show()
```

This line displays the treemap chart.

In the treemap hierarchy:

- "A" has children "B", "C", "F", "G", and "I".
- "C" has children "D" and "E".
- "G" has a child "H".

Each letter represents a rectangle, and the hierarchy is defined by the `parents` list.

-----