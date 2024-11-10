/* --- Alice.c --- */
#include"comm.h"
#include<stdbool.h>
#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

const char *my_file = "/space/file";
const char *my_file_1 = "/space/file1";
const char *my_file_2 = "/space/file2";
const char *my_file_temp = "/space/file_tmp";

// const char *my_file = "/root/experiments/file-exchange/A/file";
// const char *my_file_1 = "/root/experiments/file-exchange/A/file1";
// const char *my_file_2 = "/root/experiments/file-exchange/A/file2";
// const char *my_file_temp = "/root/experiments/file-exchange/A/file_tmp";

#include "commons.c"

int main() {
    int shmid = CreateShm(SIG_BUFFER_SIZE);
    sleep(1);
    char *shm_addr = shmat(shmid,NULL,0);
    char *buf = sig_buffer(shm_addr);
    sig_init(shm_addr);
    sleep(1);

    FILE *fp = fopen(my_file, "rb+");
    int total_received = 0;
    int ptr = 0;
    while(1) {
        fseek(fp, ptr, SEEK_SET);
        int send_size = fread(buf, 1, SIG_MSG_SIZE, fp);
        sig_invoke(shm_addr, 1, send_size);
        printf("Alice: Sent %d bytes to Bob.\n", send_size);
        // (Bob processes the message now)
        int rcev_size = sig_wait(shm_addr, 2);
        printf("Alice: Received %d bytes from Bob.\n", rcev_size);
        // Now Alice has a Bob's copy in buf
        if(rcev_size > 0) {
            total_received += rcev_size;
            fseek(fp, ptr, SEEK_SET);
            fwrite(buf, 1, rcev_size, fp);
        }
        printf("Alice: Writing finished.\n");
        // Tell if the exchange has ended
        if(rcev_size == 0 && send_size == 0) {
            break;
        }
        ptr += SIG_MSG_SIZE;
    }
    fclose(fp);

    truncate(my_file, total_received);
    printf("Alice: Total %d bytes received.\n", total_received);
    
    ///<problem-2-exclusive>
    // Split the file into two
    reverse_file_truncating(my_file, my_file_temp, 0, false);
    reverse_file_truncating(my_file_temp, my_file_1, total_received / 2, false);
    reverse_file_truncating(my_file_temp, my_file_2, 0, false);
    printf("Alice: Files split.\n");
    ///</problem-2-exclusive>

    shmdt(shm_addr);
    return 0;
}
