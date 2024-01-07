# Import necessary libraries
import qrcode
from PIL import Image

# Create a QRCode instance with specified parameters
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,
    border=2,
)

# Add data to the QRCode instance
qr.add_data("Your Data Here")

# Generate the QR code matrix and make it fit
qr.make(fit=True)

# Create an image from the QR code matrix with specified colors
img = qr.make_image(fill_color="white", back_color="cyan")

# Save the generated QR code image
img.save("Tanay's GitHub_formatted.png")
