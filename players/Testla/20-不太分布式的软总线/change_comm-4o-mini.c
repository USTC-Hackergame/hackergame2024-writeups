#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    // New command name to set
    const char *new_comm = "MyNewCommandName";

    // Open /proc/self/comm for writing
    int fd = open("/proc/self/comm", O_WRONLY);
    if (fd == -1) {
        perror("Failed to open /proc/self/comm");
        return 1;
    }

    // Write the new command name to /proc/self/comm
    ssize_t bytes_written = write(fd, new_comm, strlen(new_comm));
    if (bytes_written == -1) {
        perror("Failed to write to /proc/self/comm");
        close(fd);
        return 1;
    }

    // Close the file descriptor
    close(fd);

    // Get and print the PID
    pid_t pid = getpid();
    printf("Changed command name to: %s\n", new_comm);
    printf("Process ID (PID): %d\n", pid);

    // Keep the program running to observe the change
    while (1) {
        sleep(1);
    }

    return 0;
}
