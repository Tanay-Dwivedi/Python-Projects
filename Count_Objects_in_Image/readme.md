# Count Objects in Image

Counting objects in an image is the task of computer vision.Counting objects in an image is a task of computer vision. There are many computer vision libraries that you can use for this task, such as OpenCV, TensorFlow, PyTorch, Scikit-image, and cvlib.

-----

## Installation

```
pip install opencv-python numpy matplotlib plotly cvlib
```
Firstly import the `opencv-python numpy matplotlib plotly cvlib` libraries through the terminal that will help in the program.

-----

## Code Break:

Let's break down the provided Python script that uses OpenCV, cvlib, NumPy, and Matplotlib to perform object detection on an image:

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
```

These lines import the necessary libraries and modules. `cv2` is OpenCV for image processing, `numpy` is used for numerical operations, `matplotlib.pyplot` for plotting images, and `cvlib` is a library that simplifies computer vision tasks. The `draw_bbox` function is imported from `cvlib.object_detection` to draw bounding boxes on detected objects.

```python
image = cv2.imread("cars.jpeg")
```

Here, an image named "cars.jpeg" is read using OpenCV's `imread` function, and the resulting image is stored in the variable `image`.

```python
box, label, count = cv.detect_common_objects(image)
```

The `detect_common_objects` function from `cvlib` is used to perform object detection on the image. It returns the bounding boxes (`box`), labels (`label`) of the detected objects, and the count of detected objects (`count`).

```python
output = draw_bbox(image, box, label, count)
```

The `draw_bbox` function is called to draw bounding boxes on the detected objects. It takes the original image (`image`), bounding boxes (`box`), labels (`label`), and object count (`count`) as input and returns an image with bounding boxes drawn.

```python
plt.imshow(output)
plt.show()
```

The `imshow` and `show` functions from Matplotlib are used to display the image with bounding boxes.

```python
print("Number of cars in this image are " + str(label.count("car")))
```

Finally, the script prints the number of cars detected in the image by counting the occurrences of the label "car" in the `label` list obtained from object detection.

In summary, the script reads an image, performs object detection to identify common objects, draws bounding boxes around the detected objects, displays the resulting image, and prints the count of cars detected in the image.

-----