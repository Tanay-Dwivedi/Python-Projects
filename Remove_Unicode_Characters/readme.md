# Remove Unicode Characters

Unicode Characters can be defined as the smallest component of any language that has a semantic value. They are the combination of special values which represents special characters.

-----

## Code Break:

```python
a = "Happy Holi 😀 May this festival of colours bring you happiness, love and joy.🥰 Stay safe everyone 😊"
```

Defines a string `a` containing a festive message with emojis.

```python
a = a.encode("ascii", "ignore").decode()
```

Encodes the string to ASCII, ignoring any non-ASCII characters (including emojis), and then decodes it back to a string.

```python
print(a)
```

Prints the modified string, which now contains only ASCII characters.

In summary, this script takes a string containing emojis, encodes it to ASCII while ignoring non-ASCII characters (removing emojis in the process), and then decodes it back to a string. The final result is a string without emojis.

-----