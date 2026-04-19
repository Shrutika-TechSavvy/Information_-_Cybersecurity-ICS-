#include <windows.h>

int main() {
    HANDLE file = CreateFile("test.txt", GENERIC_WRITE, 0, NULL, CREATE_NEW, FILE_ATTRIBUTE_NORMAL, NULL);
    CloseHandle(file);
    return 0;
}