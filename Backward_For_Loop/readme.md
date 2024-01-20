# Backward For Loop

Python has an inbuilt function known as `reversed()` that can be used to reverse the order of a Python object while using a for loop.

-----

## Code Break:

```python
# forward loop

list_ = ["Aman", "Kharwal", "Akanksha", "Hritika", "Shiwangi"]

for i in list_:
    print(i)
```

This block of code demonstrates a forward loop through the elements of the list `list_`. It prints each element on a new line.

```python
# reverse loop

for i in reversed(list_):
    print(i)
```

Here, a reversed loop is used to iterate through the elements of the list in reverse order. It prints each element on a new line, but this time in reverse order. The `reversed()` function is used to reverse the order of elements during iteration.

-----