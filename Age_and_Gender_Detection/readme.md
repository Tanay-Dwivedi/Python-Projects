# Age and Gender Detection

Age and Gender Detection is the task of Computer vision so I will be using the OpenCV library in Python.

The task of detecting age and gender, however, is an inherently difficult problem, more so than many other computer vision tasks. The main reason for this difficulty gap lies in the data required to train these types of systems.

While general object detection tasks can often have access to hundreds of thousands or even millions of images for training, datasets with age and/or gender labels are considerably smaller, usually in the thousands or, at best, tens of thousands.

The reason is that to have tags for such images, we need to access the personal information of the subjects in the images. Namely, we would need their date of birth and gender, and in particular date of birth is infrequently published information.

-----

## Installation

```
pip install opencv-python
```
Firstly import the `opencv-python` library through the terminal that will help in the program.

-----

## Code Break:

```python
import cv2 as cv
```
Imports the OpenCV library under the alias `cv`.

```python
def getFaceBox(net, frame, conf_threshold=0.7):
```
Defines a function named `getFaceBox` that takes a neural network (`net`), a frame of the image (`frame`), and an optional confidence threshold (`conf_threshold`) as input parameters.

```python
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
```
Creates a copy of the input frame and retrieves its height and width.

```python
    blob = cv.dnn.blobFromImage(
        frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False
    )
```
Preprocesses the frame to prepare it for input into a deep neural network using OpenCV's `blobFromImage` function.

```python
    net.setInput(blob)
    detections = net.forward()
    bboxes = []
```
Sets the input of the neural network to the preprocessed image blob and performs forward pass inference to obtain the detections. Initializes an empty list `bboxes` to store bounding boxes.

```python
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
```
Iterates over the detections and checks if the confidence of the detection exceeds the specified threshold.

```python
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
```
Calculates the coordinates of the top-left and bottom-right corners of the bounding box based on the detected object's position and the frame dimensions.

```python
            bboxes.append([x1, y1, x2, y2])
```
Appends the coordinates of the bounding box to the `bboxes` list.

```python
            cv.rectangle(
                frameOpencvDnn,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                int(round(frameHeight / 150)),
                8,
            )
```
Draws a rectangle around the detected object on the original frame with the specified coordinates, color `(0, 255, 0)` (green), thickness, and line type.

```python
    return frameOpencvDnn, bboxes
```
Returns the frame with bounding boxes drawn and the list of bounding boxes.

```python
def detectGenderAndAge(frame, face, genderNet, ageNet, genderList, ageList):
```
Defines a function named `detectGenderAndAge` that takes a frame, a cropped face image (`face`), gender and age neural networks (`genderNet` and `ageNet`), and lists of gender and age labels as input parameters.

```python
    blob = cv.dnn.blobFromImage(
        face, 1, (227, 227), [78.4263377603, 87.7689143744, 114.895847746], swapRB=False
    )
```
Preprocesses the cropped face image to prepare it for input into the gender and age classification models using OpenCV's `blobFromImage` function.

```python
    genderNet.setInput(blob)
    genderPreds = genderNet.forward()
    gender = genderList[genderPreds[0].argmax()]
```
Sets the input of the gender neural network to the preprocessed face image blob, performs forward pass inference, and retrieves the predicted gender label from the `genderList` based on the index of the maximum predicted value.

```python
    ageNet.setInput(blob)
    agePreds = ageNet.forward()
    age = ageList[agePreds[0].argmax()]
```
Sets the input of the age neural network to the preprocessed face image blob, performs forward pass inference, and retrieves the predicted age label from the `ageList` based on the index of the maximum predicted value.

```python
    return gender, age
```
Returns the predicted gender and age labels.

```python
def main():
```
Defines the main function.

```python
    genderProto = "gender_deploy.prototxt"
    genderModel = "gender_net.caffemodel"
    ageProto = "age_deploy.prototxt"
    ageModel = "age_net.caffemodel"
```
Defines the file paths for the gender and age model configurations and weights.

```python
    genderNet = cv.dnn.readNet(genderModel, genderProto)
    ageNet = cv.dnn.readNet(ageModel, ageProto)
```
Reads the gender and age neural network models from the provided configuration and weight files.

```python
    net = cv.dnn.readNetFromCaffe(
        "deploy.prototxt", "res10_

300x300_ssd_iter_140000.caffemodel"
    )
```
Reads the deep learning model for face detection from the provided configuration and weight files.

```python
    genderList = ["Male", "Female"]
    ageList = [
        "(0 - 2)",
        "(4 - 6)",
        "(8 - 12)",
        "(15 - 20)",
        "(25 - 32)",
        "(38 - 43)",
        "(48 - 53)",
        "(60 - 100)",
    ]
```
Defines lists containing gender and age labels.

```python
    cap = cv.VideoCapture(0)
    hasFrame, frame = cap.read()
```
Opens a video capture device (webcam) for capturing frames from the camera.

```python
    while hasFrame:
```
Enters a loop to process each frame captured from the camera.

```python
        frameFace, bboxes = getFaceBox(net, frame)
```
Calls the `getFaceBox` function to detect faces in the current frame and obtain bounding boxes around the detected faces.

```python
        for bbox in bboxes:
            face = frame[
                max(0, bbox[1] - 20) : min(bbox[3] + 20, frame.shape[0] - 1),
                max(0, bbox[0] - 20) : min(bbox[2] + 20, frame.shape[1] - 1),
            ]
```
Extracts the face region from the frame using the bounding box coordinates.

```python
            gender, age = detectGenderAndAge(
                frame, face, genderNet, ageNet, genderList, ageList
            )
```
Calls the `detectGenderAndAge` function to predict the gender and age of the detected face.

```python
            label = "{}, {}".format(gender, age)
```
Formats the predicted gender and age labels into a single string.

```python
            cv.putText(
                frameFace,
                label,
                (bbox[0], bbox[1] - 20),
                cv.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                3,
                cv.LINE_AA,
            )
```
Draws the predicted gender and age label on the frame.

```python
        cv.imshow("Age Gender Demo", frameFace)
```
Displays the frame with the predicted gender and age labels.

```python
        hasFrame, frame = cap.read()
```
Reads the next frame from the video capture device.

```python
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
```
Waits for a key press, and if the key 'q' is pressed, exits the loop.

```python
    cv.destroyAllWindows()
    cap.release()
```
Closes all OpenCV windows and releases the video capture device resources.

```python
if __name__ == "__main__":
    main()
```
Calls the `main` function if the script is executed directly.

-----