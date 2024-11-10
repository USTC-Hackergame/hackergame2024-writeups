/* --- comm.h --- */
#ifndef _COMM_H__
#define _COMM_H__

#include<stdio.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/shm.h>

#define PATHNAME "."
#define PROJ_ID 0x3654

int CreateShm(int size);
int DestroyShm(int shmid);
int GetShm(int size);

/**
 Signaling address space

 shm_addr + 0: Char values. Non-zero value indicates that the message has arrived.
 shm_addr + 4: A int32 value. Size of the message. Negative value indicates that there is no further message.
 shm_addr + 8: The message buffer.
 */

#define SIG_MSG_SIZE (8 * 1024 * 1024)
// #define SIG_MSG_SIZE (50)
#define SIG_BUFFER_SIZE (SIG_MSG_SIZE + 256)

// Clear message for both sides
void sig_init(char *shm_addr);

// Get the beginning of the message buffer.
char *sig_buffer(char *shm_addr);

// Wait until message is cleared. Write size info and set the semaphore byte.
void sig_invoke(char *shm_addr, int identifier, int size);

// Block until message is available, clear the semaphore byte and return its size.
int sig_wait(char *shm_addr, int identifier);

#endif
