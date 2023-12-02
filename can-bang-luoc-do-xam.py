import cv2
import numpy as np


# Đọc ảnh grayscale từ file
image = cv2.imread('uploads/soi-da.png', cv2.IMREAD_GRAYSCALE)

# Cân bằng lược đồ xám bằng hàm có sẵn của OpenCV
equalized_image = cv2.equalizeHist(image)

# Hiển thị ảnh gốc và ảnh đã cân bằng lược đồ xám
cv2.imshow('Original Image', image)

cv2.imshow('Equalized Image', equalized_image)


cv2.waitKey(0)
cv2.destroyAllWindows()