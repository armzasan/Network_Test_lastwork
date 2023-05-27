#include <stdio.h>
#include <stdbool.h>
#include <string.h>
bool parityCheck(const char *data) {
    int count = 0;
    int length = strlen(data);
    // นับจำนวนบิตที่เป็น 1
    for (int i = 0; i < length; i++) {
        if (data[i] == '1') {
            count++;
        }
    }
    // ตรวจสอบ parity
    if (count % 2 == 0) {
        return true;  // ไม่มีข้อผิดพลาด (Even parity)
    } else {
        return false; // มีข้อผิดพลาด (Odd parity)
    }
}
int main() {
    char data[100];
    printf("Enter data to perform parity check: ");
    fgets(data, sizeof(data), stdin);
    
    // ตรวจสอบ Parity
    bool result = parityCheck(data);
    if (result) {
        printf("No parity error\n");
    } else {
        printf("Parity error detected\n");
    }
    return 0;
}
