import cv2
import numpy as np


# Đọc ảnh grayscale từ file
image = cv2.imread('uploads\moon.png', cv2.IMREAD_GRAYSCALE)


# Phân ngưỡng ảnh với hàm có sẵn của OpenCV
threshold = 100
_ , thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)


# Hiển thị ảnh gốc và ảnh đã biến đổi
cv2.imshow('Original Image', image)

cv2.imshow('Thresholded Image', thresholded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
