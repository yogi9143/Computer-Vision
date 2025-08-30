import cv2
import numpy as np

image = cv2.imread('D:\practice.jpg')  # Replace 'image.jpg' with your image path
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5), np.uint8)
opened_image = cv2.morphologyEx(gray_image, cv2.MORPH_OPEN, kernel)

cv2.imshow('Original Image', image)
cv2.imshow('Opened Image', opened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
