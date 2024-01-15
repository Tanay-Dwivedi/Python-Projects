# LCM

LCM stands for Least Common Multiple, which means finding the smallest number that is a multiple of two or more numbers.

-----

## Code Break:

```python
def find_lcm(a, b):
```
This line defines a function named `find_lcm` that takes two parameters, `a` and `b`.

```python
    if a > b:
        greater = a
    elif b > a:
        greater = b
```
This block of code determines which of the two input numbers (`a` and `b`) is greater and assigns the value to the variable `greater`.

```python
    while True:
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        greater = greater + 1
```
This `while` loop iterates indefinitely until it finds a common multiple of both `a` and `b`. It checks if `greater` is a multiple of both `a` and `b` using the modulo operator. If a common multiple is found, the loop breaks, and the LCM is stored in the variable `lcm`.

```python
    return lcm
```
The function returns the calculated LCM.

```python
print(find_lcm(10, 12))
```
This line calls the `find_lcm` function with the arguments 10 and 12 and prints the result. In this case, it would print the LCM of 10 and 12.

-----