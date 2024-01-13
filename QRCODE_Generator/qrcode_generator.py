import pyqrcode
import png

link = "https://github.com/Tanay-Dwivedi"
qr_code = pyqrcode.create(link)
qr_code.png("GitHub_profile.png", scale=5)
