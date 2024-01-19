# Swap Variables

Swapping variables means assigning the value of variable a to variable b and vice versa.

-----

## Code Break:

```python
# Method 1

a = 8
b = 10

# Store the value of 'a' in a temporary variable 'c'
c = a
# Update the value of 'a' with the value of 'b'
a = b
# Update the value of 'b' with the original value of 'a' (stored in 'c')
b = c

print("a =", a)
print("b =", b)
```

Method 1 swaps the values of `a` and `b` using a temporary variable `c`. After the execution, `a` becomes 10, and `b` becomes 8.

```python
# Method 2

a = 8
b = 10

# Swap the values of 'a' and 'b' using tuple unpacking
a, b = b, a

print("a =", a)
print("b =", b)
```

Method 2 achieves the same result as Method 1 but in a more concise way. It directly swaps the values of `a` and `b` using tuple unpacking. After the execution, `a` becomes 10, and `b` becomes 8.

-----