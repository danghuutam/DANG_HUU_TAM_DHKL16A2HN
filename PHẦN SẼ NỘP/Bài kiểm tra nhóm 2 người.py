import pyshark

# Tải file .pcapng (cập nhật đường dẫn file của bạn ở đây)
cap = pyshark.FileCapture("D:/16A2DHKL/TamvaDat.pcapng")

# Lặp qua từng gói tin trong file
for packet in cap:
    try:
        # Truy xuất thông tin tầng 2: Ethernet
        print(f"Tầng 2 - MAC nguồn: {packet.eth.src}, MAC đích: {packet.eth.dst}")
    except AttributeError:
        print("Không có thông tin tầng 2 (Ethernet).")
    try:
        # Truy xuất thông tin tầng 3: IP
        print(f"Tầng 3 - IP nguồn: {packet.ip.src}, IP đích: {packet.ip.dst}")
    except AttributeError:
        print("Không có thông tin tầng 3 (IP).")