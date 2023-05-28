def checksumCheck(data):
    checksum = sum(data) % 256

    # ตรวจสอบ checksum
    if checksum == 0:
        return True  # ข้อมูลถูกต้อง
    else:
        return False  # ข้อมูลไม่ถูกต้อง

data = input("กรอกข้อมูลที่ต้องการตรวจสอบ: ")
data = [ord(ch) for ch in data]  # แปลงเป็นรหัส ASCII

result = checksumCheck(data)

if result:
    print("ข้อมูลถูกต้อง (Data is correct)")
else:
    print("ข้อมูลไม่ถูกต้อง (Data is incorrect)")
