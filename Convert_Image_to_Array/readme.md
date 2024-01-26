# Convert Image to Array

We need to convert an image to an array to use it for any kind of data science task where we need to understand the features of an image.

-----

## Installation

```
pip install Pillow
```
```
pip install keras
```
Firstly import the `Pillow` and `keras` libraries through the terminal that will help in the program.

-----

## Code Break:

The provided code demonstrates how to use both the Pillow (PIL) library and the Keras library to load and convert an image into a NumPy array. Let's break down each part:

### Using Pillow (PIL):

```python
from PIL import Image

# Open an image file using Pillow
image = Image.open("img.png")

# Convert the image to a NumPy array
from numpy import asarray
data = asarray(image)

# Print the resulting NumPy array
print(data)
```

1. The `Image.open("img.png")` line opens an image file named "img.png" using the Pillow library.

2. The `asarray(image)` line converts the opened image into a NumPy array.

3. The `print(data)` line prints the resulting NumPy array.

### Using Keras:

```python
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

# Load an image file using Keras
img = load_img("img.png")

# Convert the image to a NumPy array
data = img_to_array(img)

# Print the resulting NumPy array
print(data)
```

1. The `load_img("img.png")` line loads an image file named "img.png" using the Keras library.

2. The `img_to_array(img)` line converts the loaded image into a NumPy array.

3. The `print(data)` line prints the resulting NumPy array.

Note: Ensure that you have the necessary libraries (Pillow, Keras) installed in your Python environment before running this code. Additionally, replace the image file name ("img.png") with the actual file name or path of your image.

-----