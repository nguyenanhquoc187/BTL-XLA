import cv2
import numpy as np

image = cv2.imread('uploads\\anh-co-gai.jpg', cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(image, cv2.CV_16S, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_16S, 0, 1, ksize=3)

# Chuyển đổi ma trận kết quả về dạng uint8 (8-bit unsigned integer) để hiển thị
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Kết hợp kết quả từ toán tử Sobel x và y
sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)

cv2.imshow('Original Image', image)
# cv2.imshow('Sobel X', sobel_x)
# cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Sobel Combined', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()