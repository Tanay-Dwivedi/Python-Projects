# Decode a QR Code

Decoding a QR code means finding the value, number, text or link behind the QR code.

-----

## Installation

```python
pip install pyzbar
```
```python
pip install pillow
```
Firstly import the `pyzbar` and `pillow` library through the terminal that will help in this program.

-----

## Code Break:

```python
# Import the decode function from the pyzbar.pyzbar module for decoding QR codes
from pyzbar.pyzbar import decode

# Import the Image class from the PIL module for working with images
from PIL import Image
```
These lines import the necessary functions and modules. The `decode` function from `pyzbar.pyzbar` is used for decoding QR codes, and the `Image` class from `PIL` is used for working with images.

```python
# Open the image file containing the QR code
image_path = "<your image name.extension>"
decoded_QR = decode(Image.open(image_path))
```
This line opens the image file containing the QR code using the `Image.open()` function from the PIL module. The variable `image_path` should be replaced with the actual path and filename of the image containing the QR code. The `decode` function is then applied to the opened image to obtain decoded information.

```python
# Extract and print the decoded data from the QR code
print(decoded_QR[0].data.decode("ascii"))
```
Here, the code prints the decoded data from the QR code. The `decoded_QR` variable contains a list of QR code objects, and `[0]` is used to access the first (and presumably only) QR code in the list. The `.data` attribute contains the raw bytes of the decoded information, and `decode("ascii")` is used to convert these bytes into a string assuming ASCII encoding. The final decoded information is then printed to the console.

Make sure to replace `"<your image name.extension>"` with the actual path and filename of the image containing the QR code before running the code.

-----