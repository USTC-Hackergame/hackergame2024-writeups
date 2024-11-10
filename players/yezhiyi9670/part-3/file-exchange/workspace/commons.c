#include<unistd.h>
#include<sys/stat.h>
#include<stdio.h>
#include "comm.h"

char tempbuf[SIG_MSG_SIZE];

int get_file_size_1(const char *fileName) {
    if (fileName == NULL) {
        return 0;
    }
    
    struct stat statbuf;

    stat(fileName, &statbuf);
    
    int filesize = statbuf.st_size;

    return filesize;
}

void swap_bytes(char *x, char *y) {
    char z = *x;
    *x = *y;
    *y = z;
}

void reverse_file_truncating(const char *src, const char *dst, int lower_limit, bool appending) {
    FILE *fp_src = fopen(src, "rb+");
    FILE *fp_dst = NULL;
    if(appending) {
        fp_dst = fopen(dst, "a");
    } else {
        fp_dst = fopen(dst, "w");
    }
    int src_size = get_file_size_1(src);
    int prev_ptr = src_size;
    int curr_ptr = prev_ptr - SIG_MSG_SIZE;
    if(curr_ptr < lower_limit) {
        curr_ptr = lower_limit;
    }
    while(curr_ptr < prev_ptr) {
        fseek(fp_src, curr_ptr, SEEK_SET);
        int size = fread(tempbuf, 1, prev_ptr - curr_ptr, fp_src);
        for(int i = 0, j = size - 1; i < j; i++, j--) {
            swap_bytes(tempbuf + i, tempbuf + j);
        }
        fwrite(tempbuf, 1, prev_ptr - curr_ptr, fp_dst);

        ftruncate(fileno(fp_src), curr_ptr);
        prev_ptr = curr_ptr;
        curr_ptr = prev_ptr - SIG_MSG_SIZE;
        if(curr_ptr < lower_limit) {
            curr_ptr = lower_limit;
        }
    }
    fclose(fp_src);
    fclose(fp_dst);
}
