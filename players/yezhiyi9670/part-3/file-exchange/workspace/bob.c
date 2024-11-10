/* --- Bob.c --- */
#include"comm.h"
#include<stdbool.h>
#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
 
const char *my_file = "/space/file";
const char *my_file_1 = "/space/file1";
const char *my_file_2 = "/space/file2";
const char *my_file_temp = "/space/file_tmp";

// const char *my_file = "/root/experiments/file-exchange/B/file";
// const char *my_file_1 = "/root/experiments/file-exchange/B/file1";
// const char *my_file_2 = "/root/experiments/file-exchange/B/file2";
// const char *my_file_temp = "/root/experiments/file-exchange/B/file_tmp";

#include "commons.c"

int main() {
    sleep(1);
    int shmid = GetShm(SIG_BUFFER_SIZE);
 
    char *shm_addr = shmat(shmid,NULL,0);
    char *buf = sig_buffer(shm_addr);
    sig_init(shm_addr);
    sleep(1);

    ///<problem-2-exclusive>
    // Combine the two files into one
    reverse_file_truncating(my_file_2, my_file_temp, 0, false);
    reverse_file_truncating(my_file_1, my_file_temp, 0, true);
    reverse_file_truncating(my_file_temp, my_file, 0, false);
    printf("Bob: Files combined.\n");
    ///</problem-2-exclusive>
    
    FILE *fp = fopen(my_file, "rb+");
    int total_received = 0;
    int ptr = 0;
    while(1) {
        int rcev_size = sig_wait(shm_addr, 1);
        printf("Bob: Received %d bytes from Alice.\n", rcev_size);
        if(rcev_size > 0) {
            // Copy into tempbuf
            for(int i = 0; i < rcev_size; i++) {
                tempbuf[i] = buf[i];
            }
        }
        // Now read the file and send out
        fseek(fp, ptr, SEEK_SET);
        int send_size = fread(buf, 1, SIG_MSG_SIZE, fp);
        sig_invoke(shm_addr, 2, send_size);
        printf("Bob: Sent %d bytes to Alice.\n", send_size);
        // Now Bob has an Alice's copy in tempbuf
        if(rcev_size > 0) {
            total_received += rcev_size;
            fseek(fp, ptr, SEEK_SET);
            fwrite(tempbuf, 1, rcev_size, fp);
        }
        printf("Bob: Writing finished.\n");
        // Tell if the exchange has ended
        if(rcev_size == 0 && send_size == 0) {
            break;
        }
        ptr += SIG_MSG_SIZE;
    }
    fclose(fp);

    truncate(my_file, total_received);
    printf("Bob: Total %d bytes received.\n", total_received);
    
    shmdt(shm_addr);
    sleep(1);
    DestroyShm(shmid);
    return 0;
}
