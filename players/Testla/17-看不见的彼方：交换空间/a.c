#include "common.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);

    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Attaching socket to the port
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt))) {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Binding the socket
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    // Listening for connections
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }

    printf("Server listening on port %d\n", PORT);

    // Accepting a connection
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
        perror("accept");
        exit(EXIT_FAILURE);
    }

    // puts("Received connection");
    // recv_(new_socket, "space/tmp", 128);
    // puts("Received file");
    // send_(new_socket, "space/file", 128);
    // send_(new_socket, "space/tmp", 128);
    // recv_(new_socket, "space/file", 128);
    // sync();
    // if (rename("space/tmp", "space/file")) {
    //     perror("rename");
    //     exit(EXIT_FAILURE);
    // }
    // rename: Operation not permitted
    // flag{just A p1ece 0f cake_30905ae13c}
    send_(new_socket, "space/file", 128);
    recv_(new_socket, "space/file1", 64);
    recv_(new_socket, "space/file2", 64);
    // flag{fa1I0catiIling_1NChains_15fun_75b6c610c4}

    // Cleaning up
    close(new_socket);
    close(server_fd);
    return 0;
}
