from pyzbar.pyzbar import decode
from PIL import Image

decoded_QR = decode(Image.open("<your image anme.extension>"))

print(decoded_QR[0].data.decode("ascii"))
