import cv2
import numpy as np

image = cv2.imread('uploads/anh-co-gai.jpg', cv2.IMREAD_GRAYSCALE)

kernel_prewitt_x = np.array([[-1, 0, 1],
                            [-1, 0, 1],
                            [-1, 0, 1]])

kernel_prewitt_y = np.array([[-1, -1, -1],
                            [ 0,  0,  0],
                            [ 1,  1,  1]])

prewitt_x = cv2.filter2D(image, cv2.CV_16S, kernel_prewitt_x)
prewitt_y = cv2.filter2D(image, cv2.CV_16S, kernel_prewitt_y)

prewitt_x = cv2.convertScaleAbs(prewitt_x)
prewitt_y = cv2.convertScaleAbs(prewitt_y)

prewitt_combined = cv2.bitwise_or(prewitt_x, prewitt_y)


cv2.imshow('Original Image', image)
# cv2.imshow('Prewitt X', prewitt_x)
# cv2.imshow('Prewitt Y', prewitt_y)
cv2.imshow('Prewitt Combined', prewitt_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()