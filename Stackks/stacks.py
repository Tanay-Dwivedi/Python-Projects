def create_stack():
    return []


def is_empty(stack):
    return not stack


def push(stack, item):
    stack.append(item)


def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        raise IndexError("pop from an empty stack")


def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        raise IndexError("peek from an empty stack")


def size(stack):
    return len(stack)


my_stack = create_stack()
print(is_empty(my_stack))

push(my_stack, 10)
push(my_stack, 20)
push(my_stack, 30)

print(pop(my_stack))
print(peek(my_stack))
print(size(my_stack))
