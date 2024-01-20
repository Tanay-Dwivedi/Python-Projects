def create_hashtable(items):
    hashtable = {}
    for key, value in items:
        hash_value = hash(key)
        index = hash_value % len(items)
        if index not in hashtable:
            hashtable[index] = []
        hashtable[index].append((key, value))
    return hashtable


def get_value(hashtable, input_key):
    hash_value = hash(input_key)
    index = hash_value % len(hashtable)
    bucket = hashtable.get(index, [])
    for key, value in bucket:
        if key == input_key:
            return value
    return None


# Example usage:
items = [("name", "John"), ("age", 25), ("city", "New York")]
my_hashtable = create_hashtable(items)

# Retrieve values
print(get_value(my_hashtable, "name"))  # Output: John
print(get_value(my_hashtable, "age"))  # Output: 25
print(get_value(my_hashtable, "city"))  # Output: New York
print(get_value(my_hashtable, "gender"))  # Output: None (key not found)
