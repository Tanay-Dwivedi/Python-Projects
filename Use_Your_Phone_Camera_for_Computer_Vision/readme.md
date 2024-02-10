# Use Your Phone Camera for Computer Vision

The process of using a phone camera with Python:

- First, install the OpenCV library in Python; pip install opencv-python.
- Download and install the [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_IN&gl=US) application on your smartphones.
- After installing the IP Webcam app, make sure your phone and PC are connected to the same network. Run the app on your phone and click Start Server.
- After that, your camera will open with an IP address at the bottom. Copy the IP address as we will need to use it in our Python code to open your phone’s camera.

-----

## Installation

```
pip install numpy opencv-python
```
Firstly import the `numpy opencv-python` libraries through the terminal that will help in the program.

-----

## Code Break:

This code seems to be attempting to capture video from a network camera using OpenCV (`cv2`). Let's break it down:

```python
import cv2
import numpy as np
```
Imports the OpenCV library (`cv2`) and NumPy.

```python
url = "Your IP Address/video"
```
Specifies the URL of the network camera feed. You should replace `"Your IP Address/video"` with the actual URL of the camera feed.

```python
cp = cv2.VideoCapture(url)
```
Creates a `VideoCapture` object `cp` to capture video from the specified URL.

```python
while True:
    camera, frame = cp.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
```

Enters a loop that continuously reads frames from the camera feed and displays them in a window. If a frame is successfully read (`frame is not None`), it is displayed using `cv2.imshow()`. The loop continues until the user presses the "q" key, at which point the loop breaks and the program exits.

```python
cv2.destroyAllWindows()
```
Closes all OpenCV windows once the loop exits.

-----