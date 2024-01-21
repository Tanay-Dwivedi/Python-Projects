# Stacks

Stacks are abstract data types that are commonly used in almost all programming languages. A stack is a data structure that simulates real-world stacks such as a deck of cards, a stack of plates, etc.

Stacks follow the principle of Last-in-first-out data structures, where the last item inserted is the first item out. It generally has five functions:

- `is_empty`: it returns True if the stacks are empty and return False if the stack is not empty.
- `push`: it inserts an item to the top of the stack.
- `pop`: it removes and returns the top item from the stack.
- `peep`: it returns the top item from the stack but it doesn’t remove it.
- `size`: it returns an integer that represents the number of items present in the stack.

-----

# Code Break:

```python
def create_stack():
    return []
```

This function `create_stack` creates and returns an empty list, which serves as the underlying structure for implementing a stack.

```python
def is_empty(stack):
    return not stack
```

This function `is_empty` takes a stack (represented as a list) as a parameter and returns `True` if the stack is empty, otherwise `False`.

```python
def push(stack, item):
    stack.append(item)
```

This function `push` takes a stack and an item as parameters and appends the item to the end of the list, simulating the addition of an element to the top of the stack.

```python
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        raise IndexError("pop from an empty stack")
```

This function `pop` takes a stack as a parameter, removes and returns the last element from the list (top of the stack) if the stack is not empty. If the stack is empty, it raises an `IndexError` with the message "pop from an empty stack."

```python
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        raise IndexError("peek from an empty stack")
```

This function `peek` takes a stack as a parameter and returns the last element from the list (top of the stack) without removing it, if the stack is not empty. If the stack is empty, it raises an `IndexError` with the message "peek from an empty stack."

```python
def size(stack):
    return len(stack)
```

This function `size` takes a stack as a parameter and returns the number of elements in the stack, indicating the size.

```python
my_stack = create_stack()
print(is_empty(my_stack))

push(my_stack, 10)
push(my_stack, 20)
push(my_stack, 30)

print(pop(my_stack))
print(peek(my_stack))
print(size(my_stack))
```

An example of using the functions to create a stack (`my_stack`), check if it is empty, push elements onto the stack, and then pop, peek, and get the size of the stack. The output demonstrates the behavior of these stack operations.

-----