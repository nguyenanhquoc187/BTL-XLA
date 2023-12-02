import cv2
import numpy as np

def otsu_threshold(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Tính histogram của ảnh xám
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    hist = hist.ravel() / hist.max()
    
    # Tính tổng xác suất
    sum_prob = np.cumsum(hist)
    
    # Tính tổng xác suất trung bình
    sum_prob_times_intensity = np.cumsum(hist * np.arange(256))
    mean_intensity = sum_prob_times_intensity[-1]
    
    between_class_variances = np.square(mean_intensity * sum_prob - sum_prob_times_intensity)
    max_variance = between_class_variances.max()
    
    optimal_threshold = np.argmax(between_class_variances)
    
    binary_image = np.zeros_like(gray_image)
    binary_image[gray_image > optimal_threshold] = 255
    
    return binary_image

image = cv2.imread('uploads/moon.png')

binary_image = otsu_threshold(image)

cv2.imshow('Original Image', image)
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()