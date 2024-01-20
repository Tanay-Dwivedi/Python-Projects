def create_queue():
    return []


def is_empty(queue):
    return len(queue) == 0


def enqueue(queue, item):
    queue.insert(0, item)


def dequeue(queue):
    return queue.pop()


def size(queue):
    return len(queue)


# Example usage:
my_queue = create_queue()

# Enqueue some items
enqueue(my_queue, 1)
enqueue(my_queue, 2)
enqueue(my_queue, 3)

# Dequeue and print items
while not is_empty(my_queue):
    print(dequeue(my_queue))  # Output: 1, 2, 3
