import pywhatkit as kit
import cv2


text = input("Enter your text: ")

kit.text_to_handwriting(text, save_to="handwritten_text.png")
image = cv2.imread("handwriting.png")

cv2.imshow("Text to Handwriting", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
