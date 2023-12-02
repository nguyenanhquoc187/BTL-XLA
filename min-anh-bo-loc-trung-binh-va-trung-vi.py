import cv2
import numpy as np


# Đọc ảnh grayscale từ file
image = cv2.imread('uploads/bang-mach.jpg', cv2.IMREAD_GRAYSCALE)

# Sử dụng toán tứ neiborhood để lọc ảnh với bộ lọc trung bình 3x3
kernel = np.ones((5,5),np.float32)/25
average_filtere_image = cv2.filter2D(image,-1,kernel)

# Sử dụng hàm có sẵn của OpenCV để lọc ảnh với bộ lọc trung vị
median_filtered_image = cv2.medianBlur(image, 5)


# Hiển thị ảnh gốc và ảnh đã lọc
cv2.imshow('Anh goc', image)

cv2.imshow('Bo loc trung binh', average_filtere_image)

cv2.imshow('Bo loc trung vi', median_filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()