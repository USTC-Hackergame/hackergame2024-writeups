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
#include <assert.h>

// #define MY_FILE "./A/file"
// #define MY_FILE1 "./A/file1"
// #define MY_FILE2 "./A/file2"
// #define MY_TMP_FILE "./A/file_tmp"

#define MY_FILE "/space/file"
#define MY_FILE1 "/space/file1"
#define MY_FILE2 "/space/file2"
#define MY_TMP_FILE "/space/tmp_file"

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

    int fd0 = -1, fd1 = -1;
    if ((fd0 = open(MY_FILE, O_RDWR)) == -1 || (fd1 = open(MY_FILE2, O_RDWR | O_CREAT, 0666)) == -1)
    {
        perror("Open");
        return 1;
    }

    for (int round = 0; round < 64; ++round)
    {
        if (ftruncate(fd1, (round + 1) * BUF_SIZE) != 0)
        {
            perror("Ftruncate fd1");
            return 1;
        }
        void *buf0 = (char *)mmap(NULL, BUF_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd0, (64 + (63 - round)) * BUF_SIZE);
        void *buf1 = (char *)mmap(NULL, BUF_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd1, round * BUF_SIZE);
        if (buf0 == MAP_FAILED || buf1 == MAP_FAILED)
        {
            perror("Mmap");
            return 1;
        }

        printf("Round %d\n", round);
        memcpy(shmp_A_buf, buf0, BUF_SIZE);
        shmp_A_state[round] = 1;
        printf("Copied to shared memory, waiting for Bob to share his data\n");
        while (shmp_B_state[round] != 1)
            usleep(100);
        printf("Bob has shared his data, copying to file\n");
        memcpy(buf1, shmp_B_buf, BUF_SIZE);
        shmp_B_state[round] = 2;
        printf("Copied to file, waiting for Bob to copy his data\n");
        while (shmp_A_state[round] != 2)
            usleep(100);

        if (munmap(buf0, BUF_SIZE) != 0 || munmap(buf1, BUF_SIZE) != 0)
        {
            perror("Munmap");
            return 1;
        }
        if (ftruncate(fd0, (64 + (63 - round)) * BUF_SIZE) != 0)
        {
            perror("Ftruncate fd0");
            return 1;
        }
    }
    if (close(fd0) != 0 || close(fd1) != 0)
    {
        perror("Close");
        return 1;
    }

    int fd = -1;
    if ((fd = open(MY_FILE, O_RDWR)) == -1)
    {
        perror("Open");
        return 1;
    }
    void *buf = (char *)mmap(NULL, 64 * BUF_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (buf == MAP_FAILED)
    {
        perror("Mmap");
        return 1;
    }
    for (int round = 0; round < 64; ++round)
    {
        printf("Round %d\n", 64 + round);
        memcpy(shmp_A_buf, buf + round * BUF_SIZE, BUF_SIZE);
        shmp_A_state[64 + round] = 1;
        printf("Copied to shared memory, waiting for Bob to share his data\n");
        while (shmp_B_state[64 + round] != 1)
            usleep(100);
        printf("Bob has shared his data, copying to file\n");
        memcpy(buf + round * BUF_SIZE, shmp_B_buf, BUF_SIZE);
        shmp_B_state[64 + round] = 2;
        printf("Copied to file, waiting for Bob to copy his data\n");
        while (shmp_A_state[64 + round] != 2)
            usleep(100);
    }
    if (munmap(buf, 64 * BUF_SIZE) != 0)
    {
        perror("Munmap");
        return 1;
    }
    if (close(fd) != 0)
    {
        perror("Close");
        return 1;
    }

    if ((fd = open(MY_FILE2, O_RDWR)) == -1)
    {
        perror("Open");
        return 1;
    }
    buf = (char *)mmap(NULL, 64 * BUF_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (buf == MAP_FAILED)
    {
        perror("Mmap");
        return 1;
    }
    for (int i = 0; i < 32; ++i)
    {
        memcpy(shmp_A_buf, buf + i * BUF_SIZE, BUF_SIZE);
        memcpy(buf + i * BUF_SIZE, buf + (63 - i) * BUF_SIZE, BUF_SIZE);
        memcpy(buf + (63 - i) * BUF_SIZE, shmp_A_buf, BUF_SIZE);
    }
    if (munmap(buf, 64 * BUF_SIZE) != 0)
    {
        perror("Munmap");
        return 1;
    }
    if (close(fd) != 0)
    {
        perror("Close");
        return 1;
    }

    fd0 = -1, fd1 = -1;
    if ((fd0 = open(MY_FILE, O_RDWR)) == -1 || (fd1 = open(MY_TMP_FILE, O_RDWR | O_CREAT, 0666)) == -1)
    {
        perror("Open");
        return 1;
    }
    for (int round = 0; round < 64; ++round)
    {
        if (ftruncate(fd1, (round + 1) * BUF_SIZE) != 0)
        {
            perror("Ftruncate fd1");
            return 1;
        }
        void *buf0 = (char *)mmap(NULL, BUF_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd0, (63 - round) * BUF_SIZE);
        void *buf1 = (char *)mmap(NULL, BUF_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd1, round * BUF_SIZE);
        if (buf0 == MAP_FAILED || buf1 == MAP_FAILED)
        {
            perror("Mmap");
            return 1;
        }

        printf("file -> tmp %d\n", round);
        memcpy(shmp_A_buf, buf0, BUF_SIZE);
        memcpy(buf0, buf1, BUF_SIZE);
        memcpy(buf1, shmp_A_buf, BUF_SIZE);

        if (munmap(buf0, BUF_SIZE) != 0 || munmap(buf1, BUF_SIZE) != 0)
        {
            perror("Munmap");
            return 1;
        }
        if (ftruncate(fd0, (63 - round) * BUF_SIZE) != 0)
        {
            perror("Ftruncate fd0");
            return 1;
        }
    }
    if (close(fd0) != 0 || close(fd1) != 0)
    {
        perror("Close");
        return 1;
    }

    if ((fd0 = open(MY_TMP_FILE, O_RDWR)) == -1 || (fd1 = open(MY_FILE1, O_RDWR | O_CREAT, 0666)) == -1)
    {
        perror("Open");
        return 1;
    }

    for (int round = 0; round < 64; ++round)
    {
        if (ftruncate(fd1, (round + 1) * BUF_SIZE) != 0)
        {
            perror("Ftruncate fd1");
            return 1;
        }
        void *buf0 = (char *)mmap(NULL, BUF_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd0, (63 - round) * BUF_SIZE);
        void *buf1 = (char *)mmap(NULL, BUF_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd1, round * BUF_SIZE);
        if (buf0 == MAP_FAILED || buf1 == MAP_FAILED)
        {
            perror("Mmap");
            return 1;
        }

        printf("tmp -> file1 %d\n", round);
        memcpy(shmp_A_buf, buf0, BUF_SIZE);
        memcpy(buf0, buf1, BUF_SIZE);
        memcpy(buf1, shmp_A_buf, BUF_SIZE);

        if (munmap(buf0, BUF_SIZE) != 0 || munmap(buf1, BUF_SIZE) != 0)
        {
            perror("Munmap");
            return 1;
        }
        if (ftruncate(fd0, (63 - round) * BUF_SIZE) != 0)
        {
            perror("Ftruncate fd0");
            return 1;
        }
    }
    if (close(fd0) != 0 || close(fd1) != 0)
    {
        perror("Close");
        return 1;
    }

    return 0;
}
