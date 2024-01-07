# Import necessary library
import qrcode as qr

# Create a QR code with the specified data (in this case, a GitHub URL)
qr_code = qr.make("https://github.com/Tanay-Dwivedi")

# Save the generated QR code image
qr_code.save("Tanay's GitHub.png")