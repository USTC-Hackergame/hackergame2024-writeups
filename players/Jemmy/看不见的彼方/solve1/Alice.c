#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <sys/mman.h>

#define BUF_SIZE (1024 * 1024)
#define STATE_SIZE 128
#define A_BUF_KEY 0x1234
#define B_BUF_KEY 0x5678
#define A_STATE_KEY 0x9abc
#define B_STATE_KEY 0xdef0

int main(int argc, char *argv[])
{
    int shmid_A_buf = -1, shmid_B_buf = -1, shmid_A_state = -1, shmid_B_state = -1;
    char *shmp_A_buf = NULL, *shmp_B_buf = NULL;
    volatile char *shmp_A_state = NULL, *shmp_B_state = NULL;

    if ((shmid_A_buf = shmget(A_BUF_KEY, BUF_SIZE, 0666 | IPC_CREAT)) == -1 || (shmid_B_buf = shmget(B_BUF_KEY, BUF_SIZE, 0666 | IPC_CREAT)) == -1 || (shmid_A_state = shmget(A_STATE_KEY, STATE_SIZE, 0666 | IPC_CREAT)) == -1 || (shmid_B_state = shmget(B_STATE_KEY, STATE_SIZE, 0666 | IPC_CREAT)) == -1)
    {
        perror("Shmget");
        return 1;
    }

    if ((shmp_A_buf = shmat(shmid_A_buf, NULL, 0)) == (void *)-1 || (shmp_B_buf = shmat(shmid_B_buf, NULL, 0)) == (void *)-1 || (shmp_A_state = shmat(shmid_A_state, NULL, 0)) == (void *)-1 || (shmp_B_state = shmat(shmid_B_state, NULL, 0)) == (void *)-1)
    {
        perror("Shmat");
        return 1;
    }

    int fd;
    if ((fd = open("fileA", O_RDWR)) == -1)
    {
        perror("Open");
        return 1;
    }

    void *buf = (char *)mmap(NULL, 128 * BUF_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (buf == MAP_FAILED)
    {
        perror("Mmap");
        return 1;
    }

    for (int round = 0; round < 128; ++round)
    {
        printf("Round %d\n", round);
        memcpy(shmp_A_buf, buf + round * BUF_SIZE, BUF_SIZE);
        shmp_A_state[round] = 1;
        printf("Copied to shared memory, waiting for Bob to share his data\n");
        while (shmp_B_state[round] != 1)
            usleep(100);
        printf("Bob has shared his data, copying to file\n");
        memcpy(buf + round * BUF_SIZE, shmp_B_buf, BUF_SIZE);
        shmp_B_state[round] = 2;
        printf("Copied to file, waiting for Bob to copy his data\n");
        while (shmp_A_state[round] != 2)
            usleep(100);
    }

    munmap(buf, 128 * BUF_SIZE);
    close(fd);
    return 0;
}
