#ifndef COMMON_H
#define COMMON_H

#define MiB (1024 * 1024)
#define PORT 8080

void send_(int sockfd, const char *path, int size_in_MiB);
void recv_(int sockfd, const char *path, int size_in_MiB);

#endif  // COMMON_H
