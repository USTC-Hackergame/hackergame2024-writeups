#include <unistd.h>
#include <stdio.h>

int main() {
    pid_t pid = getpid();
    printf("Current process ID: %d\n", pid);

    int fd = open("/proc/self/comm", 0);
    if (fd == -1) {
        perror("open");
        return 1;
    }

    char comm[1024];
    int len = read(fd, comm, sizeof(comm));
    if (len == -1) {
        perror("read");
        return 1;
    }

    comm[len] = 0;
    printf("Current process name: %s\n", comm);
    return 0;
}