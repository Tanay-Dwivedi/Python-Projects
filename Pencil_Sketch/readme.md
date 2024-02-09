# Pencil Sketch

We need to read the image in RBG format and then convert it to a grayscale image. This will turn an image into a classic black and white photo.

Then the next thing to do is invert the grayscale image also called negative image, this will be our inverted grayscale image. Inversion can be used to enhance details.

Then we can finally create the pencil sketch by mixing the grayscale image with the inverted blurry image. This can be done by dividing the grayscale image by the inverted blurry image. Since images are just arrays, we can easily do this programmatically using the divide function from the cv2 library in Python.

-----

## Installation

```
pip install opencv-python
```
Firstly import the `opencv-python` library through the terminal that will help in the program.

-----

## Code Break:

Sure, I'll provide a breakdown of the code line by line:

```python
import cv2
```
This line imports the OpenCV library, which is used for various computer vision tasks, including image processing and manipulation.

```python
image = cv2.imread("dog.jpg")
```
This line reads the image named "dog.jpg" from the current directory and stores it in the variable `image`.

```python
cv2.imshow("Dog", image)
cv2.waitKey(0)
```
These lines display the original image named "Dog" in a window and wait for a key press to close the window. The `cv2.imshow()` function is used to display the image, and `cv2.waitKey(0)` waits indefinitely for a key press (here, '0' indicates an indefinite wait).

```python
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Dog", gray_image)
cv2.waitKey(0)
```
These lines convert the original color image to grayscale using the `cv2.cvtColor()` function with the `cv2.COLOR_BGR2GRAY` conversion flag. Then, it displays the grayscale image named "New Dog" and waits for a key press to close the window.

```python
inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()
```
Here, the grayscale image is inverted by subtracting each pixel value from 255. It then displays the inverted image and waits for a key press to close the window.

```python
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
```
These lines apply Gaussian blur to the inverted image using a kernel size of (21, 21) and displays it. Then, it inverts the blurred image again.

```python
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)
```
Here, the division operation is applied between the grayscale image and the inverted blurred image, with scaling. This operation aims to create a pencil sketch effect. The resulting sketch is displayed, and the program waits for a key press to close the window.

```python
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)
```
These lines display both the original color image and the pencil sketch side by side and wait for a key press to close the windows.

Overall, this script reads an image, converts it to grayscale, creates an inverted version, applies Gaussian blur, and then combines the grayscale and blurred images to produce a pencil sketch effect. Finally, it displays the original image, the pencil sketch, and the intermediate steps in separate windows.

-----