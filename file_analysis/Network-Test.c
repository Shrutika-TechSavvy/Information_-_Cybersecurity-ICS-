#include <winsock2.h>

int main() {
    WSADATA wsa;
    WSAStartup(MAKEWORD(2,2), &wsa);
    return 0;
}