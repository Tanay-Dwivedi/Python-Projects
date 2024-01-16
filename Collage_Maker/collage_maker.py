from PIL import Image
import numpy as np


def collage_maker(image1, image2, name):
    i1 = np.array(image1)
    i2 = np.array(image2)
    collage = np.vstack([i1, i2])
    image = Image.fromarray(collage)
    image.save(name)

# PS - Bothe images should have same size (lxb)
# To Run The Above Function
collage_maker("image1.jpg", "image2.jpg", "new.jpg")
