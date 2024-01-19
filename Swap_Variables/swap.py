# Method 1

a = 8
b = 10

c = a
a = b
b = c

print("a =", a)
print("b = ", b)

# Method 2

a = 8
b = 10

a, b = b, a

print("a = ", a)
print("b = ", b)
