#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <string.h>

#define MiB (1024 * 1024)

void send(int sockfd, const char *path, int size_in_MiB) {
    int fd = open(path, O_RDWR);
    if (fd < 0) return;

    char buffer[MiB];
    for (int i = size_in_MiB - 1; i >= 0; --i) {
        // Seek to the position where we want to read
        lseek(fd, i * MiB, SEEK_SET);
        
        // Read 1 MiB
        ssize_t bytes_read = read(fd, buffer, MiB);
        if (bytes_read <= 0) break;

        // Send the data
        ssize_t total_sent = 0;
        while (total_sent < bytes_read) {
            ssize_t sent = write(sockfd, buffer + total_sent, bytes_read - total_sent);
            if (sent <= 0) break;
            total_sent += sent;
        }

        // Truncate the file
        ftruncate(fd, i * MiB);
    }
    
    close(fd);
}

void receive(int sockfd, const char *path, int size_in_MiB) {
    void *blocks[1000];
    
    // Receive phase
    for (int i = size_in_MiB - 1; i >= 0; --i) {
        // Allocate memory for this block
        blocks[i] = malloc(MiB);
        if (!blocks[i]) break;

        // Receive 1 MiB of data
        ssize_t total_received = 0;
        while (total_received < MiB) {
            ssize_t received = read(sockfd, (char*)blocks[i] + total_received, 
                                  MiB - total_received);
            if (received <= 0) break;
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
        // Clean up if file couldn't be opened
        for (int i = 0; i < size_in_MiB; ++i) {
            if (blocks[i]) free(blocks[i]);
        }
    }
}
