import cv2

image = cv2.imread('uploads/anh-co-gai.jpg', cv2.IMREAD_GRAYSCALE)

threshold1 = 60
threshold2 = 30

edges = cv2.Canny(image, threshold1, threshold2)

cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()