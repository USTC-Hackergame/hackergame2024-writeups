#include <assert.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>

#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>

#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

#define IMG_DIM 1024
#define SZ_FRAMEBUFFER (IMG_DIM * IMG_DIM * 4)
// #define SZ_READ_CHUNKSIZE (IMG_DIM * IMG_DIM / 2) // 16位编码一张图搞定

// 记得改成 /secret
#define TARGET_FILE "/secret"

#define OUTPUT "result.png"

[[noreturn]]
void die(const char *message)
{
    printf("die: %s\n", message);
    abort();
}

uint8_t color_tbl[][4] = {
    {0,    0,    0,    0xff}, // 0
    {0x7f, 0,    0,    0xff},
    {0,    0x7f, 0,    0xff},
    {0,    0,    0x7f, 0xff},
    {0,    0x7f, 0x7f, 0xff},
    {0x7f, 0,    0x7f, 0xff},
    {0x7f, 0x7f, 0,    0xff},
    {0x55, 0x55, 0x55, 0xff}, // 1/3
// 什么 16bit 彩色
    {0xaa, 0xaa, 0xaa, 0xff}, // 2/3
    {0xff, 0,    0,    0xff},
    {0,    0xff, 0,    0xff},
    {0,    0,    0xff, 0xff},
    {0,    0xff, 0xff, 0xff},
    {0xff, 0,    0xff, 0xff},
    {0xff, 0xff, 0,    0xff},
    {0xff, 0xff, 0xff, 0xff}, // 3/3
};

// src -> 1byte
// dst -> 2 pixel = 8 bytes
void
encode_pixels_from_byte(uint8_t *dst, uint8_t *src)
{
    uint8_t val = *src;
    uint8_t low = val & 0xf;
    uint8_t high = (val >> 4) & 0xf;
    const size_t sz_color = 4;
    memcpy(dst, &color_tbl[low], sz_color);
    dst += sz_color;
    memcpy(dst, &color_tbl[high], sz_color);
}

size_t adjust_size(size_t sz)
{
    return sz + (4096 - (sz % 4096));
}

int
main(void)
{
    int targetfd = open(TARGET_FILE, O_RDONLY);

    size_t fbsz = adjust_size(SZ_FRAMEBUFFER);
    void *fb = mmap(NULL, fbsz, PROT_READ | PROT_WRITE, MAP_ANON | MAP_SHARED, -1, 0);
    if (fb == MAP_FAILED) {
        perror("mmap()");
        die("mmap() framebuffer failed");
    }

    void *content = malloc(512 * 1024); // 512K
    if (!content)
    {
        die("out of memory");
    }

    struct stat stat_thefile;
    stat(TARGET_FILE, &stat_thefile);
    if(stat_thefile.st_size != 512 * 1024)
    {
        die("unexpected size of target file"); // 你害我！！！
    }

    if (read(targetfd, content, 512 * 1024) != 512 * 1024)
    {
        die("unexpected read");
    }
    
    for(int count = 0; count < (512 * 1024); ++count)
    {
        uint8_t *readfile = (uint8_t *)content + count;
        uint8_t *writefb = (uint8_t *)fb + (count * 2 * 4);
        encode_pixels_from_byte(writefb, readfile);
    }

    stbi_write_png_compression_level = 0;
    stbi_write_png(OUTPUT, IMG_DIM, IMG_DIM, 4, fb, IMG_DIM * 4);

    free(content);
    munmap(fb, fbsz);
    return 0;
}
