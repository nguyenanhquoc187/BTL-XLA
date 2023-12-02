import cv2
import numpy as np


image = cv2.imread('uploads/anh-co-gai.jpg', cv2.IMREAD_GRAYSCALE)


laplacian = cv2.Laplacian(image,cv2.CV_16S)


laplacian = np.uint8(np.absolute(laplacian))

cv2.imshow('Original Image', image)

cv2.imshow('Laplacian', laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
