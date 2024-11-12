#include "common.h"

#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

void send_(int sockfd, const char *path, int size_in_MiB) {
    int fd = open(path, O_RDWR);
    if (fd < 0) {
        printf("send_: Failed to open %s\n", path);
        exit(1);
    }

    static char buffer[MiB];
    for (int i = size_in_MiB - 1; i >= 0; --i) {
        // Seek to the position where we want to read
        lseek(fd, i * MiB, SEEK_SET);

        // Read 1 MiB
        ssize_t bytes_read = read(fd, buffer, MiB);
        if (bytes_read != MiB) {
            printf("send_: read returned %lld\n", (long long)bytes_read);
            exit(1);
        }

        // Send the data
        ssize_t total_sent = 0;
        while (total_sent < bytes_read) {
            ssize_t sent = write(sockfd, buffer + total_sent, bytes_read - total_sent);
            if (sent <= 0) {
                puts("send_: write failed");
                exit(1);
            }
            total_sent += sent;
        }

        // Truncate the file
        ftruncate(fd, i * MiB);
    }

    close(fd);
}

void recv_(int sockfd, const char *path, int size_in_MiB) {
    void *blocks[1000];

    // Receive phase
    for (int i = size_in_MiB - 1; i >= 0; --i) {
        // Allocate memory for this block
        blocks[i] = malloc(MiB);
        if (!blocks[i]) {
            puts("recv_: malloc failed");
            exit(1);
        }

        // Receive 1 MiB of data
        ssize_t total_received = 0;
        while (total_received < MiB) {
            ssize_t received = read(sockfd, (char*)blocks[i] + total_received,
                                  MiB - total_received);
            if (received <= 0) {
                puts("recv_: read failed");
                exit(1);
            }
            total_received += received;
        }
    }

    // Write phase
    int fd = open(path, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd >= 0) {
        for (int i = 0; i < size_in_MiB; ++i) {
            if (blocks[i]) {
                write(fd, blocks[i], MiB);
                free(blocks[i]);
            }
        }
        close(fd);
    } else {
        puts("recv_: open failed");
        exit(1);
    }
}
