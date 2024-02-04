# Contact Book

A contact book is a database used to store entries related to a person’s contacts like a phone number, email address, etc. It is also known as the address book.

-----

## Code Break:

```python
names = []
phone_numbers = []
num = 3

for i in range(num):
    name = input("Name: ")
    phone_number = input(
        "Phone Number: "
    )  # for convert to int => int(input("Phone Number: "))

    names.append(name)
    phone_numbers.append(phone_number)
```

This part of the code initializes empty lists `names` and `phone_numbers`. It then prompts the user to input names and corresponding phone numbers for a specified number of times (`num`). The entered values are added to the respective lists.

```python
print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))
```

Prints a formatted table header and displays the entered names and phone numbers in a tabular format.

```python
search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_term, phone_number))
else:
    print("Name Not Found")
```

Prompts the user to enter a search term and then searches for the entered term in the `names` list. If found, it retrieves the corresponding phone number and prints the result. If not found, it prints "Name Not Found."

-----