/* --- comm.c --- */
#include"comm.h"
 
static int CommShm(int size,int flags) {
    // key_t key = ftok(PATHNAME,PROJ_ID);
    key_t key = 241354996;
    if(key < 0) {
    	perror("ftok");
    	return -1;
    }
    int shmid = 0;
    if((shmid = shmget(key,size,flags)) < 0) {
        perror("shmget");
        return -2;
    }
    return shmid;
}
int DestroyShm(int shmid) {
    if(shmctl(shmid,IPC_RMID,NULL) < 0) {
        perror("shmctl");
        return -1;
    }
    return 0;
}
int CreateShm(int size) {
    return CommShm(size,IPC_CREAT | IPC_EXCL | 0666);
}
int GetShm(int size) {
    return CommShm(size,IPC_CREAT);
}

void sig_init(char *shm_addr) {
    *shm_addr = 0;
    *(shm_addr + 1) = 0;
    *(shm_addr + 2) = 0;
    *(shm_addr + 3) = 0;
}

char *sig_buffer(char *shm_addr) {
    return shm_addr + 8;
}

void sig_invoke(char *shm_addr, int identifier, int size) {
    int *size_addr = (int*)(shm_addr + 4);
    char *sem_addr = shm_addr + identifier;
    while(*sem_addr != 0);
    *size_addr = size;
    *sem_addr = 1;
}

int sig_wait(char *shm_addr, int identifier) {
    int *size_addr = (int*)(shm_addr + 4);
    char *sem_addr = shm_addr + identifier;
    while(*sem_addr == 0);
    *sem_addr = 0;
    int size = *size_addr;
    return size;
}
