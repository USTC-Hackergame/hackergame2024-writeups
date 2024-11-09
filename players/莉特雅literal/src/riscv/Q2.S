# mem: 0x000 ~ 0xffc
# sort 16 * u32(4 bytes * 16)
# input:  0xf80 ~ 0xfbc (64 bytes) 刚好放下
# output: 0xfc0 ~ 0xffc
# free 3968 bytes (992 * u32)

# 思路：内存有问题那我不用内存也可以啊，tm 31 个寄存器呢，才 16 个数字

.section .text
_start:
    li a0, 0xf80 # in
    li a1, 0xfc0 # out

    mv a2, a0 # index
    # loading
    lw a6, (a2)
    add a2, a2, 4
    lw a7,(a2)
    add a2, a2, 4
    lw s2,(a2)
    add a2, a2, 4
    lw s3,(a2)
    add a2, a2, 4
    lw s4,(a2)
    add a2, a2, 4
    lw s5,(a2)
    add a2, a2, 4
    lw s6,(a2)
    add a2, a2, 4
    lw s7,(a2)
    add a2, a2, 4
    lw s8,(a2)
    add a2, a2, 4
    lw s9,(a2)
    add a2, a2, 4
    lw s10,(a2)
    add a2, a2, 4
    lw s11,(a2)
    add a2, a2, 4
    lw t3,(a2)
    add a2, a2, 4
    lw t4,(a2)
    add a2, a2, 4
    lw t5,(a2)
    add a2, a2, 4
    lw t6,(a2)
    add a2, a2, 4


#     bltu a6, a7, 1f
#     mv a5, a6
#     mv a6, a7
#     mv a7, a5
# 1:

    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu s3, s4, 1f
    mv a5, s3
    mv s3, s4
    mv s4, a5
1:
    bltu s4, s5, 1f
    mv a5, s4
    mv s4, s5
    mv s5, a5
1:
    bltu s5, s6, 1f
    mv a5, s5
    mv s5, s6
    mv s6, a5
1:
    bltu s6, s7, 1f
    mv a5, s6
    mv s6, s7
    mv s7, a5
1:
    bltu s7, s8, 1f
    mv a5, s7
    mv s7, s8
    mv s8, a5
1:
    bltu s8, s9, 1f
    mv a5, s8
    mv s8, s9
    mv s9, a5
1:
    bltu s9, s10, 1f
    mv a5, s9
    mv s9, s10
    mv s10, a5
1:
    bltu s10, s11, 1f
    mv a5, s10
    mv s10, s11
    mv s11, a5
1:
    bltu s11, t3, 1f
    mv a5, s11
    mv s11, t3
    mv t3, a5
1:
    bltu t3, t4, 1f
    mv a5, t3
    mv t3, t4
    mv t4, a5
1:
    bltu t4, t5, 1f
    mv a5, t4
    mv t4, t5
    mv t5, a5
1:
    bltu t5, t6, 1f
    mv a5, t5
    mv t5, t6
    mv t6, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu s3, s4, 1f
    mv a5, s3
    mv s3, s4
    mv s4, a5
1:
    bltu s4, s5, 1f
    mv a5, s4
    mv s4, s5
    mv s5, a5
1:
    bltu s5, s6, 1f
    mv a5, s5
    mv s5, s6
    mv s6, a5
1:
    bltu s6, s7, 1f
    mv a5, s6
    mv s6, s7
    mv s7, a5
1:
    bltu s7, s8, 1f
    mv a5, s7
    mv s7, s8
    mv s8, a5
1:
    bltu s8, s9, 1f
    mv a5, s8
    mv s8, s9
    mv s9, a5
1:
    bltu s9, s10, 1f
    mv a5, s9
    mv s9, s10
    mv s10, a5
1:
    bltu s10, s11, 1f
    mv a5, s10
    mv s10, s11
    mv s11, a5
1:
    bltu s11, t3, 1f
    mv a5, s11
    mv s11, t3
    mv t3, a5
1:
    bltu t3, t4, 1f
    mv a5, t3
    mv t3, t4
    mv t4, a5
1:
    bltu t4, t5, 1f
    mv a5, t4
    mv t4, t5
    mv t5, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu s3, s4, 1f
    mv a5, s3
    mv s3, s4
    mv s4, a5
1:
    bltu s4, s5, 1f
    mv a5, s4
    mv s4, s5
    mv s5, a5
1:
    bltu s5, s6, 1f
    mv a5, s5
    mv s5, s6
    mv s6, a5
1:
    bltu s6, s7, 1f
    mv a5, s6
    mv s6, s7
    mv s7, a5
1:
    bltu s7, s8, 1f
    mv a5, s7
    mv s7, s8
    mv s8, a5
1:
    bltu s8, s9, 1f
    mv a5, s8
    mv s8, s9
    mv s9, a5
1:
    bltu s9, s10, 1f
    mv a5, s9
    mv s9, s10
    mv s10, a5
1:
    bltu s10, s11, 1f
    mv a5, s10
    mv s10, s11
    mv s11, a5
1:
    bltu s11, t3, 1f
    mv a5, s11
    mv s11, t3
    mv t3, a5
1:
    bltu t3, t4, 1f
    mv a5, t3
    mv t3, t4
    mv t4, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu s3, s4, 1f
    mv a5, s3
    mv s3, s4
    mv s4, a5
1:
    bltu s4, s5, 1f
    mv a5, s4
    mv s4, s5
    mv s5, a5
1:
    bltu s5, s6, 1f
    mv a5, s5
    mv s5, s6
    mv s6, a5
1:
    bltu s6, s7, 1f
    mv a5, s6
    mv s6, s7
    mv s7, a5
1:
    bltu s7, s8, 1f
    mv a5, s7
    mv s7, s8
    mv s8, a5
1:
    bltu s8, s9, 1f
    mv a5, s8
    mv s8, s9
    mv s9, a5
1:
    bltu s9, s10, 1f
    mv a5, s9
    mv s9, s10
    mv s10, a5
1:
    bltu s10, s11, 1f
    mv a5, s10
    mv s10, s11
    mv s11, a5
1:
    bltu s11, t3, 1f
    mv a5, s11
    mv s11, t3
    mv t3, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu s3, s4, 1f
    mv a5, s3
    mv s3, s4
    mv s4, a5
1:
    bltu s4, s5, 1f
    mv a5, s4
    mv s4, s5
    mv s5, a5
1:
    bltu s5, s6, 1f
    mv a5, s5
    mv s5, s6
    mv s6, a5
1:
    bltu s6, s7, 1f
    mv a5, s6
    mv s6, s7
    mv s7, a5
1:
    bltu s7, s8, 1f
    mv a5, s7
    mv s7, s8
    mv s8, a5
1:
    bltu s8, s9, 1f
    mv a5, s8
    mv s8, s9
    mv s9, a5
1:
    bltu s9, s10, 1f
    mv a5, s9
    mv s9, s10
    mv s10, a5
1:
    bltu s10, s11, 1f
    mv a5, s10
    mv s10, s11
    mv s11, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu s3, s4, 1f
    mv a5, s3
    mv s3, s4
    mv s4, a5
1:
    bltu s4, s5, 1f
    mv a5, s4
    mv s4, s5
    mv s5, a5
1:
    bltu s5, s6, 1f
    mv a5, s5
    mv s5, s6
    mv s6, a5
1:
    bltu s6, s7, 1f
    mv a5, s6
    mv s6, s7
    mv s7, a5
1:
    bltu s7, s8, 1f
    mv a5, s7
    mv s7, s8
    mv s8, a5
1:
    bltu s8, s9, 1f
    mv a5, s8
    mv s8, s9
    mv s9, a5
1:
    bltu s9, s10, 1f
    mv a5, s9
    mv s9, s10
    mv s10, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu s3, s4, 1f
    mv a5, s3
    mv s3, s4
    mv s4, a5
1:
    bltu s4, s5, 1f
    mv a5, s4
    mv s4, s5
    mv s5, a5
1:
    bltu s5, s6, 1f
    mv a5, s5
    mv s5, s6
    mv s6, a5
1:
    bltu s6, s7, 1f
    mv a5, s6
    mv s6, s7
    mv s7, a5
1:
    bltu s7, s8, 1f
    mv a5, s7
    mv s7, s8
    mv s8, a5
1:
    bltu s8, s9, 1f
    mv a5, s8
    mv s8, s9
    mv s9, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu s3, s4, 1f
    mv a5, s3
    mv s3, s4
    mv s4, a5
1:
    bltu s4, s5, 1f
    mv a5, s4
    mv s4, s5
    mv s5, a5
1:
    bltu s5, s6, 1f
    mv a5, s5
    mv s5, s6
    mv s6, a5
1:
    bltu s6, s7, 1f
    mv a5, s6
    mv s6, s7
    mv s7, a5
1:
    bltu s7, s8, 1f
    mv a5, s7
    mv s7, s8
    mv s8, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu s3, s4, 1f
    mv a5, s3
    mv s3, s4
    mv s4, a5
1:
    bltu s4, s5, 1f
    mv a5, s4
    mv s4, s5
    mv s5, a5
1:
    bltu s5, s6, 1f
    mv a5, s5
    mv s5, s6
    mv s6, a5
1:
    bltu s6, s7, 1f
    mv a5, s6
    mv s6, s7
    mv s7, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu s3, s4, 1f
    mv a5, s3
    mv s3, s4
    mv s4, a5
1:
    bltu s4, s5, 1f
    mv a5, s4
    mv s4, s5
    mv s5, a5
1:
    bltu s5, s6, 1f
    mv a5, s5
    mv s5, s6
    mv s6, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu s3, s4, 1f
    mv a5, s3
    mv s3, s4
    mv s4, a5
1:
    bltu s4, s5, 1f
    mv a5, s4
    mv s4, s5
    mv s5, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu s3, s4, 1f
    mv a5, s3
    mv s3, s4
    mv s4, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu s2, s3, 1f
    mv a5, s2
    mv s2, s3
    mv s3, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:
    bltu a7, s2, 1f
    mv a5, a7
    mv a7, s2
    mv s2, a5
1:
    bltu a6, a7, 1f
    mv a5, a6
    mv a6, a7
    mv a7, a5
1:

    mv a2, a1 # index
    # store
    sw a6, (a2)
    add a2, a2, 4
    sw a7,(a2)
    add a2, a2, 4
    sw s2,(a2)
    add a2, a2, 4
    sw s3,(a2)
    add a2, a2, 4
    sw s4,(a2)
    add a2, a2, 4
    sw s5,(a2)
    add a2, a2, 4
    sw s6,(a2)
    add a2, a2, 4
    sw s7,(a2)
    add a2, a2, 4
    sw s8,(a2)
    add a2, a2, 4
    sw s9,(a2)
    add a2, a2, 4
    sw s10,(a2)
    add a2, a2, 4
    sw s11,(a2)
    add a2, a2, 4
    sw t3,(a2)
    add a2, a2, 4
    sw t4,(a2)
    add a2, a2, 4
    sw t5,(a2)
    add a2, a2, 4
    sw t6,(a2)
    add a2, a2, 4
