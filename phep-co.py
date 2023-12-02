import cv2
import numpy as np

def erosion(image, kernel_size):
    kernel = np.ones(kernel_size, np.uint8)
    
    result_image = cv2.erode(image, kernel, iterations=1)
    
    return result_image

image = cv2.imread('uploads/bang-mach.jpg', 0)  

result_image = erosion(image, (5, 5)) 

cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()