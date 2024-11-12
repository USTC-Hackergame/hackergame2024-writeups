#include "common.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;

    puts("1b running");
    sleep(1);
    // return 0;

    // Creating socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("Socket creation error\n");
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Convert IPv4 and IPv6 addresses from text to binary form
    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        printf("Invalid address/ Address not supported\n");
        return -1;
    }

    // Connecting to server
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        printf("Connection failed\n");
        return -1;
    }

    // puts("Connected");
    // send_(sock, "space/file", 128);
    // puts("Sent");
    // recv_(sock, "space/file", 128);
    // recv_(sock, "space/tmp", 128);
    // send_(sock, "space/tmp", 128);
    recv_(sock, "space/file", 128);
    send_(sock, "space/file1", 64);
    send_(sock, "space/file2", 64);

    // Cleaning up
    close(sock);
    return 0;
}
