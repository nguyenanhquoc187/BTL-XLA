import numpy as np
import cv2

# Đọc ảnh vào
image = cv2.imread('uploads/anh-co-gai.jpg', cv2.IMREAD_GRAYSCALE)

# Tạo kernel Roberts x và y
kernel_roberts_x = np.array([[1, 0],
                             [0, -1]])

kernel_roberts_y = np.array([[0, -1],
                             [1, 0]])

# Áp dụng kernel Roberts x và y
roberts_x = cv2.filter2D(image, cv2.CV_16S, kernel_roberts_x)
roberts_y = cv2.filter2D(image, cv2.CV_16S, kernel_roberts_y)

# Chuyển đổi ma trận kết quả về dạng uint8 (8-bit unsigned integer)
roberts_x = cv2.convertScaleAbs(roberts_x)
roberts_y = cv2.convertScaleAbs(roberts_y)

# Kết hợp kết quả từ toán tử Roberts x và y
roberts_combined = cv2.bitwise_or(roberts_x, roberts_y)


cv2.imshow('Original Image', image)
# cv2.imshow('Roberts X', roberts_x)
# cv2.imshow('Roberts Y', roberts_y)
cv2.imshow('Roberts Combined', roberts_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()