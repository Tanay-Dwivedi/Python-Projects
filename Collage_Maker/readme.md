# Collage Maker

A collage maker is a tool used to merge different images into one. It allows you to save and share images as a collection of memories.

-----

## Installation

```
pip install numpy
```
Firstly import the `numpy` library through the terminal that will help in the program.

-----

## Code Break:

To create a collage maker using the Python programming language, you must first learn how to read and convert images to arrays using Python. To create a photo collage, you first need to read the images and convert them into arrays before merging them into a collage.

```python
# Import necessary libraries
from PIL import Image
import numpy as np
```

These lines import the required libraries (`Image` from `PIL` and `numpy`).

```python
# Define a function to create a vertical collage from two images
def collage_maker(image1, image2, name):
    # Convert the images to numpy arrays
    i1 = np.array(image1)
    i2 = np.array(image2)

    # Stack the arrays vertically to create a collage
    collage = np.vstack([i1, i2])

    # Convert the resulting array back to an image
    image = Image.fromarray(collage)

    # Save the collage with the specified name
    image.save(name)

# Note: Both images should have the same size (width x height)
```

This part defines the `collage_maker` function. It takes three parameters: `image1`, `image2`, and `name`. The function converts the images to numpy arrays, stacks them vertically using `np.vstack()`, converts the resulting array back to an image using `Image.fromarray()`, and saves the collage with the specified name using `image.save()`.

```python
# To run the function with example images
collage_maker("image1.jpg", "image2.jpg", "new.jpg")
```

This line demonstrates how to use the `collage_maker` function with example images. In this case, it creates a vertical collage from "image1.jpg" and "image2.jpg" and saves it as "new.jpg". It's important to note that both input images should have the same size (width x height) for this function to work correctly.

-----