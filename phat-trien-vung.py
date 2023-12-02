import cv2
import numpy as np

def region_growing(image, seed):

    height, width = image.shape[:2]
    visited = np.zeros((height, width), dtype=np.uint8)
    threshold = 10  # Ngưỡng cho phép sự khác biệt của pixel
    
    # Lấy giá trị màu của điểm hạt giống
    seed_value = image[seed[1], seed[0]]
    
    # Khởi tạo hàng đợi
    queue = []
    queue.append(seed)
    
    # Phát triển vùng
    while len(queue) > 0:

        point = queue.pop(0)
        

        if visited[point[1], point[0]] == 1:
            continue
        
        if np.abs(int(image[point[1], point[0]]) - int(seed_value)) > threshold:
            continue
        
        visited[point[1], point[0]] = 1
        
        if point[0] > 0:
            queue.append((point[0] - 1, point[1]))
        if point[0] < width - 1:
            queue.append((point[0] + 1, point[1]))
        if point[1] > 0:
            queue.append((point[0], point[1] - 1))
        if point[1] < height - 1:
            queue.append((point[0], point[1] + 1))
    
    # Trả về ảnh đã đánh dấu vùng phát triển
    marked_image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    marked_image[visited == 1] = [0, 0, 255]  # Đánh dấu màu đỏ
    
    return marked_image

image = cv2.imread('uploads/moon.png', 0)

# Chọn điểm hạt giống
seed_point = (100, 100)

# Áp dụng thuật toán phát triển vùng
result_image = region_growing(image, seed_point)

# Hiển thị kết quả
cv2.imshow('Original Image', image)
cv2.imshow('Result Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()