# Cho ví dụ rõ ràng ở phần nhắc nhập để người dùng không gõ nhầm chữ
raw_name = input("- Nhập họ và tên (Ví dụ: Nguyen Van A): ")
raw_id = input("- Nhập mã bệnh nhân (Ví dụ: BN102): ")
raw_temp = input("- Nhập nhiệt độ cơ thể (Chỉ gõ số, ví dụ: 36.5 hoặc 37): ")
raw_heart = input("- Nhập số nhịp tim (Chỉ gõ số, ví dụ: 80): ")
raw_weight = input("- Nhập số cân nặng (Chỉ gõ số, ví dụ: 60.5): ")

# Nhập xong rồi tách dòng ra để ép kiểu
patient_name = raw_name
patient_id = raw_id
body_temperature = float(raw_temp)
heart_rate = int(raw_heart)
body_weight = float(raw_weight)

# KHỐI HIỂN THỊ PHIẾU KHÁM VÀ LOG IT
print("\n===== PHIẾU KHÁM BỆNH ĐIỆN TỬ =====")
print("Mã bệnh nhân    :", patient_id)
print("Họ và tên       :", patient_name)
print("Nhiệt độ cơ thể :", body_temperature, "độ C")
print("Nhịp tim        :", heart_rate, "nhịp/phút")
print("Cân nặng        :", body_weight, "kg")

print("\n--------- KIỂM TRA CHUẨN HÓA DỮ LIỆU HỆ THỐNG ---------")
print("-> Biến 'patient_name'     | Kiểu dữ liệu:", type(patient_name))
print("-> Biến 'patient_id'       | Kiểu dữ liệu:", type(patient_id))
print("-> Biến 'body_temperature' | Kiểu dữ liệu:", type(body_temperature))
print("-> Biến 'heart_rate'       | Kiểu dữ liệu:", type(heart_rate))
print("-> Biến 'body_weight'      | Kiểu dữ liệu:", type(body_weight))
print("-------------------------------------------------------")
