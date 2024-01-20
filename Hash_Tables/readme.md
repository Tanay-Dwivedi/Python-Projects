# Hash Tables

Hash tables are like dictionaries in Python, they are data structures that are used to store and retrieve a large amount of data in the format of keys and values.
The concept of hash tables is widely used in applications such as:

- Database indexing
- Compiler design
- Caching
- Password authentication
- Error analysis and many more.

Hash tables are based on the concept of hash, which means using a hash function used to map key and values. Since it is used to map key and value pairs, it is commonly known as a hashmap.

-----

## Code Break:

```python
def create_hashtable(items):
    hashtable = {}
    for key, value in items:
        hash_value = hash(key)
        index = hash_value % len(items)
        if index not in hashtable:
            hashtable[index] = []
        hashtable[index].append((key, value))
    return hashtable
```

This function `create_hashtable` takes a list of key-value pairs (`items`) and creates a basic hashtable. It iterates over each key-value pair, calculates the hash value of the key, determines the index in the hashtable by using the modulo operation with the length of the items, and appends the key-value pair to the corresponding index in the hashtable.

```python
def get_value(hashtable, input_key):
    hash_value = hash(input_key)
    index = hash_value % len(hashtable)
    bucket = hashtable.get(index, [])
    for key, value in bucket:
        if key == input_key:
            return value
    return None
```

This function `get_value` takes a hashtable and an input key. It calculates the hash value of the input key, determines the index in the hashtable using the modulo operation, and retrieves the bucket (list of key-value pairs) at that index. It then iterates through the bucket, searching for the input key, and returns the corresponding value if found; otherwise, it returns `None`.

```python
# Example usage:
items = [("name", "John"), ("age", 25), ("city", "New York")]
my_hashtable = create_hashtable(items)

# Retrieve values
print(get_value(my_hashtable, "name"))  # Output: John
print(get_value(my_hashtable, "age"))  # Output: 25
print(get_value(my_hashtable, "city"))  # Output: New York
print(get_value(my_hashtable, "gender"))  # Output: None (key not found)
```

In this example, a list of key-value pairs is provided (`items`), and a hashtable (`my_hashtable`) is created using the `create_hashtable` function. The `get_value` function is then used to retrieve values from the hashtable based on different input keys. The print statements demonstrate the expected output for each retrieval operation.

-----