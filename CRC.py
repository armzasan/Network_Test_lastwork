def crcCheck(data, generator):
    crc = 0
    # ใส่ข้อมูลใน CRC
    crc = int(data, 2) << (len(generator) - 1)
    # คำนวณ CRC
    for i in range(len(data)):
        if crc >> (len(generator) - 1) == 1:
            crc = crc ^ int(generator, 2)
        crc = crc << 1
    # ตรวจสอบ CRC
    if crc == 0:
        return True  # ข้อมูลถูกต้อง
    else:
        return False  # ข้อมูลไม่ถูกต้อง
data = input("กรอกข้อมูลที่ต้องการตรวจสอบ: ")
generator = input("กรอกเจนเนอเรเตอร์ (Generator): ")
result = crcCheck(data, generator)
if result:
    print("ข้อมูลถูกต้อง (Data is correct)")
else:
    print("ข้อมูลไม่ถูกต้อง (Data is incorrect)")
