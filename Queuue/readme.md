# Queues

A queue is a data structure where we insert items from the back and remove items from the front. It follows the principle of First In, First Out data structures.
A queue is like stacks where you can insert and delete items in a specific order, but unlike stacks that follow the principle of last-in-first-out data structures, queues follow the principle of last-in-first-out data structures where the first item added is the first item removed.


-----

## Code Break:

```python
def create_queue():
    return []
```

This function `create_queue` creates and returns an empty list, which serves as the foundation for implementing a queue.

```python
def is_empty(queue):
    return len(queue) == 0
```

This function `is_empty` takes a queue (represented as a list) as a parameter and returns `True` if the queue is empty, otherwise `False`.

```python
def enqueue(queue, item):
    queue.insert(0, item)
```

This function `enqueue` takes a queue and an item as parameters and inserts the item at the front (index 0) of the list, simulating the addition of an element to the rear of the queue.

```python
def dequeue(queue):
    return queue.pop()
```

This function `dequeue` takes a queue as a parameter and removes and returns the last element from the list, simulating the removal of an element from the front of the queue.

```python
def size(queue):
    return len(queue)
```

This function `size` takes a queue as a parameter and returns the number of elements in the queue, indicating the size.

```python
# Example usage:
my_queue = create_queue()

# Enqueue some items
enqueue(my_queue, 1)
enqueue(my_queue, 2)
enqueue(my_queue, 3)
```

An example of using the functions to create a queue (`my_queue`) and enqueue some items (1, 2, and 3).

```python
# Dequeue and print items
while not is_empty(my_queue):
    print(dequeue(my_queue))  # Output: 1, 2, 3
```

A loop is used to dequeue and print items from the queue until it becomes empty. The expected output is 1, 2, and 3, as items are dequeued in the order they were enqueued.

-----