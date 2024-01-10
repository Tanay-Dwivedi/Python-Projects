from time import time

start = time()

# Python program to create acronyms
word = "United Nations Educational, Scientific and Cultural Organization"
result_string = ""

for char in word:
    if char.isupper():
        result_string += char

print(result_string)

end = time()
execution_time = end - start
print("Execution Time: ", execution_time)
