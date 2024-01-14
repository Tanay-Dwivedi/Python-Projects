# QR Code Generator

this code snippet creates a QR code image for a specific GitHub profile link and saves it as a PNG file

-----

## Installation

```python
pip install PyQRCode
```
```python
pip install pypng
```
Firstly import the `PyQRCode` and `pypng` library through the terminal that will help in this program.

-----

## Code Break:

```python
# Import the pyqrcode library for generating QR codes and the png module for handling PNG images
import pyqrcode
import png
```
In this section, the code imports the `pyqrcode` library, which is used for generating QR codes, and the `png` module for handling PNG images.

```python
# Define the URL link to be encoded in the QR code
link = "https://github.com/Tanay-Dwivedi"
```
This line assigns a URL link (in this case, a GitHub profile link) to the variable `link`. This link will be encoded into a QR code.

```python
# Create a QR code object using pyqrcode with the specified link
qr_code = pyqrcode.create(link)
```
Here, the code uses the `pyqrcode.create()` function to generate a QR code object (`qr_code`) based on the provided URL link.

```python
# Generate a PNG image of the QR code with a specified filename and scale
qr_code.png("GitHub_profile.png", scale=5)
```
The last line saves the generated QR code as a PNG image named "GitHub_profile.png" with a specified scaling factor of 5. The resulting PNG image contains the encoded information from the provided URL link in the form of a QR code.

***Outputs***

![GitHub QR Code](GitHub_profile.png)

-----