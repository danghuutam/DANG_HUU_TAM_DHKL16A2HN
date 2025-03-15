import numpy as np

def calculate_co_channel_interference(K, D):
    # Định nghĩa các tham số hệ thống
    P = 1  # Công suất phát sóng giả định (đơn vị tương đối)
    N = int(np.sqrt(3 * K))  # Số cell đồng kênh trong khu vực

    # Tính toán nhiễu từ mỗi cell đồng kênh
    interference = 0
    for i in range(1, N + 1):
        for j in range(6):
            angle = np.radians(j * 60)
            x_offset = i * D * np.cos(angle)
            y_offset = i * D * np.sin(angle)
            distance = np.sqrt(x_offset**2 + y_offset**2)
            interference += P / (distance ** 2)  # Giả định giảm thiểu công suất theo khoảng cách bình phương

    return interference

# Tính toán và so sánh nhiễu cho K=7 và K=12
D7 = np.sqrt(3 * 7)
D12 = np.sqrt(3 * 12)
interference_K7 = calculate_co_channel_interference(7, D7)
interference_K12 = calculate_co_channel_interference(12, D12)

print(f"Nhiễu đồng kênh cho K=7: {interference_K7}")
print(f"Nhiễu đồng kênh cho K=12: {interference_K12}")
