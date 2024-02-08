# Face Detection

Face detection is the process of detecting faces, from an image or a video does not matter. The program does nothing more than finding the faces. But on the other hand in the task of face recognition, the program finds faces and can also tell which face belongs to which. So it’s more informative than just detecting them. There is more programming, in other words, more training in the process.

-----

## Installation

```
pip install opencv-python
```
Firstly import the `opencv-python` library through the terminal that will help in the program.

-----

## Code Break:

```python
import cv2
```
Imports the OpenCV library.

```python
face_cascade = cv2.CascadeClassifier("face_detector.xml")
```
Creates a cascade classifier object `face_cascade` using the XML file `"face_detector.xml"`, which contains pre-trained data for detecting faces.

```python
img = cv2.imread("image.jpg")
```
Reads an image file named "image.jpg" and stores it as a NumPy array `img`.

```python
faces = face_cascade.detectMultiScale(img, 1.1, 4)
```
Detects faces in the image using the `detectMultiScale()` method of the cascade classifier. This method takes the input image (`img`) and two parameters: `scaleFactor` (which specifies how much the image size is reduced at each image scale) and `minNeighbors` (which specifies how many neighbors each candidate rectangle should have to retain it).

```python
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
```
Iterates over each detected face and draws a rectangle around it using the `rectangle()` function. The parameters are the input image `img`, the top-left corner coordinates `(x, y)` of the rectangle, the bottom-right corner coordinates `(x + w, y + h)`, the color `(255, 0, 0)` (in BGR format), and the thickness of the rectangle (2 pixels).

```python
cv2.imwrite("face_detected.png", img)
```
Writes the modified image with the detected faces to a new file named "face_detected.png" using the `imwrite()` function.

```python
print("Successfully saved")
```
Prints a message indicating that the image with detected faces has been successfully saved.
```

-----