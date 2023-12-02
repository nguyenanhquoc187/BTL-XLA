import cv2
import numpy as np


# Đọc ảnh grayscale từ file
image = cv2.imread('uploads/am7ucnbewr.png', cv2.IMREAD_GRAYSCALE)

negative_image = cv2.bitwise_not(image)


cv2.imshow('Original Image', image)

cv2.imshow('Negative Image', negative_image)

cv2.waitKey(0)
cv2.destroyAllWindows()