// zig build-lib -dynamic -target x86_64-linux-gnu -OReleaseSmall -fstrip -lc set_comm_to_getflag3.c
#include <sys/syscall.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

static void set_comm(const char *comm)
{
    int fd = open("/proc/self/comm", O_RDWR);
    if (fd < 0) {
        perror("open /proc/self/comm failed: ");
        exit(1);
    }
    ssize_t ret = write(fd, comm, strlen(comm));
    if (ret < 0) {
        perror("write failed: ");
        exit(1);
    } else if (ret < strlen(comm)) {
        fprintf(stderr, "write too few bytes: %zd\n", ret);
        exit(1);
    }
    close(fd);
}

int socket(int domain, int type, int protocol)
{
    set_comm("getflag3");
    return syscall(SYS_socket, domain, type, protocol);
}
