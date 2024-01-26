# using Pillow

from PIL import Image

image = Image.open("img.png")

from numpy import asarray

data = asarray(image)
print(data)


# using keras

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

img = load_img("img.png")
data = img_to_array(img)

print(data)
