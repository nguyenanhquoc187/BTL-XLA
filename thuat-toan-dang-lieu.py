import cv2
import numpy as np

def isodata_threshold(image, initial_threshold, min_size, max_iterations):
    # Chuyển ảnh sang ảnh grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Khởi tạo ngưỡng ban đầu
    threshold = initial_threshold

    for _ in range(max_iterations):
        # Phân đoạn ảnh bằng ngưỡng hiện tại
        _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

        # Tính toán giá trị ngưỡng mới dựa trên các vùng kết quả
        mean_object = np.mean(gray[binary == 255])
        mean_background = np.mean(gray[binary == 0])
        new_threshold = (mean_object + mean_background) / 2

        # Kiểm tra điều kiện dừng
        if abs(new_threshold - threshold) <= 1:
            break

        # Kiểm tra kích thước vùng đối tượng
        num_object_pixels = np.sum(binary == 255)
        if num_object_pixels < min_size:
            break

        # Cập nhật ngưỡng
        threshold = new_threshold

    return threshold


# Đọc ảnh vào
image = cv2.imread('uploads/moon.png')

# Áp dụng thuật toán đẳng liệu để xác định ngưỡng tối ưu
threshold = isodata_threshold(image, initial_threshold=128, min_size=100, max_iterations=10)

# Phân đoạn ảnh bằng ngưỡng tối ưu
_, binary = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)


cv2.imshow('Original Image', image)
cv2.imshow('Binary Image', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()