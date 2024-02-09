import cv2
from instafilter import Instafilter

model = Instafilter("Lo-fi")
new_image = model("image.jpg")

cv2.imwrite("modified_image.jpg", new_image)
