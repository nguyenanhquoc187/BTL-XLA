import cv2
import numpy as np


# Đọc ảnh grayscale từ file
image = cv2.imread('uploads\moon.png', cv2.IMREAD_GRAYSCALE)

# c = 255 / np.log(1 + np.max(image))
c = 40
log_transformed_image = c * (np.log(image + 1))

transformed_image = np.array(log_transformed_image, dtype = np.uint8)

cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()