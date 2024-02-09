# Instagram Filters

You must have used Instagram once in your life, have you noticed that you see a variety of Instagram filters when uploading an image. These filters are designed to improve the quality of the image. These filters are an example of complex machine learning algorithms that are deployed in production to serve Instagram. So if these filters are created by machine learning algorithms, it means that we can also create Instagram filters with Python.

-----

## Installation

```
pip install opencv-python instafilter
```
Firstly import the `opencv-python instafilter` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import cv2
from instafilter import Instafilter
```
These lines import the necessary modules. `cv2` is OpenCV library used for image processing, while `Instafilter` is a class from the `instafilter` module, which is presumably used for applying Instagram-like filters to images.

```python
model = Instafilter("Lo-fi")
```
This line creates an instance of the `Instafilter` class with the filter name "Lo-fi". This filter is presumably one of the filters available within the `instafilter` module.

```python
new_image = model("image.jpg")
```
This line applies the "Lo-fi" filter to the image named "image.jpg" using the `model` object created earlier. The filtered image is returned and stored in the variable `new_image`.

```python
cv2.imwrite("modified_image.jpg", new_image)
```
This line saves the filtered image (`new_image`) to a file named "modified_image.jpg" using the `cv2.imwrite()` function. This function is provided by OpenCV and is used to write an image to a file.

Overall, this script loads an image, applies an Instagram-like filter ("Lo-fi") to it, and saves the filtered image as "modified_image.jpg".

-----