def lrcCheck(data):
    lrc = 0
    # คำนวณค่า LRC
    for ch in data:
        lrc ^= ord(ch)
    # เพิ่ม bit parity 0
    lrc ^= 0
    # ตรวจสอบ parity
    if lrc == 0:
        return True  # ไม่มีข้อผิดพลาด (Even parity)
    else:
        return False  # มีข้อผิดพลาด (Odd parity)
data = input("กรอกข้อมูลที่ต้องการตรวจสอบ: ")
result = lrcCheck(data)
if result:
    print("ไม่พบข้อผิดพลาด (No parity error)")
else:
    print("พบข้อผิดพลาด (Parity error)")
