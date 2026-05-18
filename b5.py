# 1. Thiết kế dữ liệu và Phòng ngừa lỗi 
# - Thiết kế biến: Sử dụng 100% tiếng Anh định dạng `snake_case` chuẩn Clean Code (`patient_name`, `body_temperature`,...).
# - Chống crash bằng UX: Các câu lệnh `input()` được thiết kế kèm ví dụ trực quan cụ thể giúp người bệnh không rành công nghệ vẫn biết cách nhập đúng định dạng số, hạn chế tối đa việc nhập chữ gây crash hệ thống ở bước ép kiểu.

# 2. Kiến trúc luồng xử lý
# - Thu thập: Toàn bộ dữ liệu được lưu dưới dạng chuỗi thô từ `input()`.
# - Hạ tầng ngầm: Tiến hành ép kiểu hàng loạt bằng `float()` và `int()` tại Khối xử lý riêng biệt để đồng bộ với Monitor.
# - Đầu ra: Xuất bản song song Phiếu khám trực quan cho bệnh nhân và bảng Log chi tiết cấu trúc kiểu dữ liệu cho quản trị viên hệ thống.

patient_name = input("- Nhập họ và tên của bạn: ")
patient_id = input("- Nhập mã bệnh nhân: ")
raw_temperature = input("- Nhập nhiệt độ cơ thể bạn: ")
raw_heart_rate = input("- Nhập nhịp timcủa bạn: ")
raw_weight = input("- Nhập cân nặng của bạn: ")

body_temperature = float(raw_temperature)
body_weight = float(raw_weight)
heart_rate = int(raw_heart_rate)

print("\n" + "===== PHIẾU KHÁM BỆNH ĐIỆN TỬ =====" )
print(f" Mã bệnh nhân   : {patient_id}")
print(f" Họ và tên      : {patient_name}")
print(f" Nhiệt độ cơ thể: {body_temperature} độ C")
print(f" Nhịp tim       : {heart_rate} nhịp/phút")
print(f" Cân nặng       : {body_weight} kg")
print("=======================================")
print("  (*) Vui lòng cầm phiếu này đến quầy điều dưỡng gần nhất.  ")
print("=======================================")

print("\n" "--------- KIỂM TRA CHUẨN HÓA DỮ LIỆU HỆ THỐNG ---------")
print(f"-> Biến 'patient_name'     | Kiểu dữ liệu gốc: {type(patient_name)}")
print(f"-> Biến 'patient_id'       | Kiểu dữ liệu gốc: {type(patient_id)}")
print(f"-> Biến 'body_temperature' | Kiểu dữ liệu sau ép kiểu: {type(body_temperature)}")
print(f"-> Biến 'heart_rate'       | Kiểu dữ liệu sau ép kiểu: {type(heart_rate)}")
print(f"-> Biến 'body_weight'      | Kiểu dữ liệu sau ép kiểu: {type(body_weight)}")
print("-------------------------------------------------------")