def vrcCheck(data):
    sum = 0
    # คำนวณผลรวมของข้อมูล
    for ch in data:
        sum += ord(ch)
    # ตรวจสอบ VRC
    if sum % 256 == 0:
        return True  # ข้อมูลถูกต้อง
    else:
        return False  # ข้อมูลไม่ถูกต้อง
data = input("กรอกข้อมูลที่ต้องการตรวจสอบ: ")
result = vrcCheck(data)
if result:
    print("ข้อมูลถูกต้อง (Data is correct)")
else:
    print("ข้อมูลไม่ถูกต้อง (Data is incorrect)")
