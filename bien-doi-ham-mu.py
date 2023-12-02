import numpy as np
import cv2

# Đọc ảnh grayscale từ file
image = cv2.imread('uploads/moon.png', cv2.IMREAD_GRAYSCALE)

gamma = 2.5
c = 1.5

# Biến đổi hàm vũ với hàm có sẵn của OpenCV
transformed_image = cv2.pow(image / 255 , gamma)

# Hiển thị ảnh gốc và ảnh đã biến đổi
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()