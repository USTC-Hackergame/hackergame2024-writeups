.section .text
_start:
    la a0, 0xf80
    la a1, 0xfc0
    lw s0, 0(a0)
    lw s1, 4(a0)
    lw s2, 8(a0)
    lw s3, 12(a0)
    lw s4, 16(a0)
    lw s5, 20(a0)
    lw s6, 24(a0)
    lw s7, 28(a0)
    lw s8, 32(a0)
    lw s9, 36(a0)
    lw s10, 40(a0)
    lw s11, 44(a0)
    lw t2, 48(a0)
    lw t3, 52(a0)
    lw t4, 56(a0)
    lw t5, 60(a0)
_sort_0_1_start:
    bltu s0, s1, _sort_0_1_noswap
    mv t0, s0
    mv s0, s1
    mv s1, t0
_sort_0_1_noswap:
_sort_0_1_end:
_sort_0_2_start:
    bltu s0, s2, _sort_0_2_noswap
    mv t0, s0
    mv s0, s2
    mv s2, t0
_sort_0_2_noswap:
_sort_0_2_end:
_sort_0_3_start:
    bltu s0, s3, _sort_0_3_noswap
    mv t0, s0
    mv s0, s3
    mv s3, t0
_sort_0_3_noswap:
_sort_0_3_end:
_sort_0_4_start:
    bltu s0, s4, _sort_0_4_noswap
    mv t0, s0
    mv s0, s4
    mv s4, t0
_sort_0_4_noswap:
_sort_0_4_end:
_sort_0_5_start:
    bltu s0, s5, _sort_0_5_noswap
    mv t0, s0
    mv s0, s5
    mv s5, t0
_sort_0_5_noswap:
_sort_0_5_end:
_sort_0_6_start:
    bltu s0, s6, _sort_0_6_noswap
    mv t0, s0
    mv s0, s6
    mv s6, t0
_sort_0_6_noswap:
_sort_0_6_end:
_sort_0_7_start:
    bltu s0, s7, _sort_0_7_noswap
    mv t0, s0
    mv s0, s7
    mv s7, t0
_sort_0_7_noswap:
_sort_0_7_end:
_sort_0_8_start:
    bltu s0, s8, _sort_0_8_noswap
    mv t0, s0
    mv s0, s8
    mv s8, t0
_sort_0_8_noswap:
_sort_0_8_end:
_sort_0_9_start:
    bltu s0, s9, _sort_0_9_noswap
    mv t0, s0
    mv s0, s9
    mv s9, t0
_sort_0_9_noswap:
_sort_0_9_end:
_sort_0_10_start:
    bltu s0, s10, _sort_0_10_noswap
    mv t0, s0
    mv s0, s10
    mv s10, t0
_sort_0_10_noswap:
_sort_0_10_end:
_sort_0_11_start:
    bltu s0, s11, _sort_0_11_noswap
    mv t0, s0
    mv s0, s11
    mv s11, t0
_sort_0_11_noswap:
_sort_0_11_end:
_sort_0_12_start:
    bltu s0, t2, _sort_0_12_noswap
    mv t0, s0
    mv s0, t2
    mv t2, t0
_sort_0_12_noswap:
_sort_0_12_end:
_sort_0_13_start:
    bltu s0, t3, _sort_0_13_noswap
    mv t0, s0
    mv s0, t3
    mv t3, t0
_sort_0_13_noswap:
_sort_0_13_end:
_sort_0_14_start:
    bltu s0, t4, _sort_0_14_noswap
    mv t0, s0
    mv s0, t4
    mv t4, t0
_sort_0_14_noswap:
_sort_0_14_end:
_sort_0_15_start:
    bltu s0, t5, _sort_0_15_noswap
    mv t0, s0
    mv s0, t5
    mv t5, t0
_sort_0_15_noswap:
_sort_0_15_end:
    sw s0, 0(a1)
_sort_1_2_start:
    bltu s1, s2, _sort_1_2_noswap
    mv t0, s1
    mv s1, s2
    mv s2, t0
_sort_1_2_noswap:
_sort_1_2_end:
_sort_1_3_start:
    bltu s1, s3, _sort_1_3_noswap
    mv t0, s1
    mv s1, s3
    mv s3, t0
_sort_1_3_noswap:
_sort_1_3_end:
_sort_1_4_start:
    bltu s1, s4, _sort_1_4_noswap
    mv t0, s1
    mv s1, s4
    mv s4, t0
_sort_1_4_noswap:
_sort_1_4_end:
_sort_1_5_start:
    bltu s1, s5, _sort_1_5_noswap
    mv t0, s1
    mv s1, s5
    mv s5, t0
_sort_1_5_noswap:
_sort_1_5_end:
_sort_1_6_start:
    bltu s1, s6, _sort_1_6_noswap
    mv t0, s1
    mv s1, s6
    mv s6, t0
_sort_1_6_noswap:
_sort_1_6_end:
_sort_1_7_start:
    bltu s1, s7, _sort_1_7_noswap
    mv t0, s1
    mv s1, s7
    mv s7, t0
_sort_1_7_noswap:
_sort_1_7_end:
_sort_1_8_start:
    bltu s1, s8, _sort_1_8_noswap
    mv t0, s1
    mv s1, s8
    mv s8, t0
_sort_1_8_noswap:
_sort_1_8_end:
_sort_1_9_start:
    bltu s1, s9, _sort_1_9_noswap
    mv t0, s1
    mv s1, s9
    mv s9, t0
_sort_1_9_noswap:
_sort_1_9_end:
_sort_1_10_start:
    bltu s1, s10, _sort_1_10_noswap
    mv t0, s1
    mv s1, s10
    mv s10, t0
_sort_1_10_noswap:
_sort_1_10_end:
_sort_1_11_start:
    bltu s1, s11, _sort_1_11_noswap
    mv t0, s1
    mv s1, s11
    mv s11, t0
_sort_1_11_noswap:
_sort_1_11_end:
_sort_1_12_start:
    bltu s1, t2, _sort_1_12_noswap
    mv t0, s1
    mv s1, t2
    mv t2, t0
_sort_1_12_noswap:
_sort_1_12_end:
_sort_1_13_start:
    bltu s1, t3, _sort_1_13_noswap
    mv t0, s1
    mv s1, t3
    mv t3, t0
_sort_1_13_noswap:
_sort_1_13_end:
_sort_1_14_start:
    bltu s1, t4, _sort_1_14_noswap
    mv t0, s1
    mv s1, t4
    mv t4, t0
_sort_1_14_noswap:
_sort_1_14_end:
_sort_1_15_start:
    bltu s1, t5, _sort_1_15_noswap
    mv t0, s1
    mv s1, t5
    mv t5, t0
_sort_1_15_noswap:
_sort_1_15_end:
    sw s1, 4(a1)
_sort_2_3_start:
    bltu s2, s3, _sort_2_3_noswap
    mv t0, s2
    mv s2, s3
    mv s3, t0
_sort_2_3_noswap:
_sort_2_3_end:
_sort_2_4_start:
    bltu s2, s4, _sort_2_4_noswap
    mv t0, s2
    mv s2, s4
    mv s4, t0
_sort_2_4_noswap:
_sort_2_4_end:
_sort_2_5_start:
    bltu s2, s5, _sort_2_5_noswap
    mv t0, s2
    mv s2, s5
    mv s5, t0
_sort_2_5_noswap:
_sort_2_5_end:
_sort_2_6_start:
    bltu s2, s6, _sort_2_6_noswap
    mv t0, s2
    mv s2, s6
    mv s6, t0
_sort_2_6_noswap:
_sort_2_6_end:
_sort_2_7_start:
    bltu s2, s7, _sort_2_7_noswap
    mv t0, s2
    mv s2, s7
    mv s7, t0
_sort_2_7_noswap:
_sort_2_7_end:
_sort_2_8_start:
    bltu s2, s8, _sort_2_8_noswap
    mv t0, s2
    mv s2, s8
    mv s8, t0
_sort_2_8_noswap:
_sort_2_8_end:
_sort_2_9_start:
    bltu s2, s9, _sort_2_9_noswap
    mv t0, s2
    mv s2, s9
    mv s9, t0
_sort_2_9_noswap:
_sort_2_9_end:
_sort_2_10_start:
    bltu s2, s10, _sort_2_10_noswap
    mv t0, s2
    mv s2, s10
    mv s10, t0
_sort_2_10_noswap:
_sort_2_10_end:
_sort_2_11_start:
    bltu s2, s11, _sort_2_11_noswap
    mv t0, s2
    mv s2, s11
    mv s11, t0
_sort_2_11_noswap:
_sort_2_11_end:
_sort_2_12_start:
    bltu s2, t2, _sort_2_12_noswap
    mv t0, s2
    mv s2, t2
    mv t2, t0
_sort_2_12_noswap:
_sort_2_12_end:
_sort_2_13_start:
    bltu s2, t3, _sort_2_13_noswap
    mv t0, s2
    mv s2, t3
    mv t3, t0
_sort_2_13_noswap:
_sort_2_13_end:
_sort_2_14_start:
    bltu s2, t4, _sort_2_14_noswap
    mv t0, s2
    mv s2, t4
    mv t4, t0
_sort_2_14_noswap:
_sort_2_14_end:
_sort_2_15_start:
    bltu s2, t5, _sort_2_15_noswap
    mv t0, s2
    mv s2, t5
    mv t5, t0
_sort_2_15_noswap:
_sort_2_15_end:
    sw s2, 8(a1)
_sort_3_4_start:
    bltu s3, s4, _sort_3_4_noswap
    mv t0, s3
    mv s3, s4
    mv s4, t0
_sort_3_4_noswap:
_sort_3_4_end:
_sort_3_5_start:
    bltu s3, s5, _sort_3_5_noswap
    mv t0, s3
    mv s3, s5
    mv s5, t0
_sort_3_5_noswap:
_sort_3_5_end:
_sort_3_6_start:
    bltu s3, s6, _sort_3_6_noswap
    mv t0, s3
    mv s3, s6
    mv s6, t0
_sort_3_6_noswap:
_sort_3_6_end:
_sort_3_7_start:
    bltu s3, s7, _sort_3_7_noswap
    mv t0, s3
    mv s3, s7
    mv s7, t0
_sort_3_7_noswap:
_sort_3_7_end:
_sort_3_8_start:
    bltu s3, s8, _sort_3_8_noswap
    mv t0, s3
    mv s3, s8
    mv s8, t0
_sort_3_8_noswap:
_sort_3_8_end:
_sort_3_9_start:
    bltu s3, s9, _sort_3_9_noswap
    mv t0, s3
    mv s3, s9
    mv s9, t0
_sort_3_9_noswap:
_sort_3_9_end:
_sort_3_10_start:
    bltu s3, s10, _sort_3_10_noswap
    mv t0, s3
    mv s3, s10
    mv s10, t0
_sort_3_10_noswap:
_sort_3_10_end:
_sort_3_11_start:
    bltu s3, s11, _sort_3_11_noswap
    mv t0, s3
    mv s3, s11
    mv s11, t0
_sort_3_11_noswap:
_sort_3_11_end:
_sort_3_12_start:
    bltu s3, t2, _sort_3_12_noswap
    mv t0, s3
    mv s3, t2
    mv t2, t0
_sort_3_12_noswap:
_sort_3_12_end:
_sort_3_13_start:
    bltu s3, t3, _sort_3_13_noswap
    mv t0, s3
    mv s3, t3
    mv t3, t0
_sort_3_13_noswap:
_sort_3_13_end:
_sort_3_14_start:
    bltu s3, t4, _sort_3_14_noswap
    mv t0, s3
    mv s3, t4
    mv t4, t0
_sort_3_14_noswap:
_sort_3_14_end:
_sort_3_15_start:
    bltu s3, t5, _sort_3_15_noswap
    mv t0, s3
    mv s3, t5
    mv t5, t0
_sort_3_15_noswap:
_sort_3_15_end:
    sw s3, 12(a1)
_sort_4_5_start:
    bltu s4, s5, _sort_4_5_noswap
    mv t0, s4
    mv s4, s5
    mv s5, t0
_sort_4_5_noswap:
_sort_4_5_end:
_sort_4_6_start:
    bltu s4, s6, _sort_4_6_noswap
    mv t0, s4
    mv s4, s6
    mv s6, t0
_sort_4_6_noswap:
_sort_4_6_end:
_sort_4_7_start:
    bltu s4, s7, _sort_4_7_noswap
    mv t0, s4
    mv s4, s7
    mv s7, t0
_sort_4_7_noswap:
_sort_4_7_end:
_sort_4_8_start:
    bltu s4, s8, _sort_4_8_noswap
    mv t0, s4
    mv s4, s8
    mv s8, t0
_sort_4_8_noswap:
_sort_4_8_end:
_sort_4_9_start:
    bltu s4, s9, _sort_4_9_noswap
    mv t0, s4
    mv s4, s9
    mv s9, t0
_sort_4_9_noswap:
_sort_4_9_end:
_sort_4_10_start:
    bltu s4, s10, _sort_4_10_noswap
    mv t0, s4
    mv s4, s10
    mv s10, t0
_sort_4_10_noswap:
_sort_4_10_end:
_sort_4_11_start:
    bltu s4, s11, _sort_4_11_noswap
    mv t0, s4
    mv s4, s11
    mv s11, t0
_sort_4_11_noswap:
_sort_4_11_end:
_sort_4_12_start:
    bltu s4, t2, _sort_4_12_noswap
    mv t0, s4
    mv s4, t2
    mv t2, t0
_sort_4_12_noswap:
_sort_4_12_end:
_sort_4_13_start:
    bltu s4, t3, _sort_4_13_noswap
    mv t0, s4
    mv s4, t3
    mv t3, t0
_sort_4_13_noswap:
_sort_4_13_end:
_sort_4_14_start:
    bltu s4, t4, _sort_4_14_noswap
    mv t0, s4
    mv s4, t4
    mv t4, t0
_sort_4_14_noswap:
_sort_4_14_end:
_sort_4_15_start:
    bltu s4, t5, _sort_4_15_noswap
    mv t0, s4
    mv s4, t5
    mv t5, t0
_sort_4_15_noswap:
_sort_4_15_end:
    sw s4, 16(a1)
_sort_5_6_start:
    bltu s5, s6, _sort_5_6_noswap
    mv t0, s5
    mv s5, s6
    mv s6, t0
_sort_5_6_noswap:
_sort_5_6_end:
_sort_5_7_start:
    bltu s5, s7, _sort_5_7_noswap
    mv t0, s5
    mv s5, s7
    mv s7, t0
_sort_5_7_noswap:
_sort_5_7_end:
_sort_5_8_start:
    bltu s5, s8, _sort_5_8_noswap
    mv t0, s5
    mv s5, s8
    mv s8, t0
_sort_5_8_noswap:
_sort_5_8_end:
_sort_5_9_start:
    bltu s5, s9, _sort_5_9_noswap
    mv t0, s5
    mv s5, s9
    mv s9, t0
_sort_5_9_noswap:
_sort_5_9_end:
_sort_5_10_start:
    bltu s5, s10, _sort_5_10_noswap
    mv t0, s5
    mv s5, s10
    mv s10, t0
_sort_5_10_noswap:
_sort_5_10_end:
_sort_5_11_start:
    bltu s5, s11, _sort_5_11_noswap
    mv t0, s5
    mv s5, s11
    mv s11, t0
_sort_5_11_noswap:
_sort_5_11_end:
_sort_5_12_start:
    bltu s5, t2, _sort_5_12_noswap
    mv t0, s5
    mv s5, t2
    mv t2, t0
_sort_5_12_noswap:
_sort_5_12_end:
_sort_5_13_start:
    bltu s5, t3, _sort_5_13_noswap
    mv t0, s5
    mv s5, t3
    mv t3, t0
_sort_5_13_noswap:
_sort_5_13_end:
_sort_5_14_start:
    bltu s5, t4, _sort_5_14_noswap
    mv t0, s5
    mv s5, t4
    mv t4, t0
_sort_5_14_noswap:
_sort_5_14_end:
_sort_5_15_start:
    bltu s5, t5, _sort_5_15_noswap
    mv t0, s5
    mv s5, t5
    mv t5, t0
_sort_5_15_noswap:
_sort_5_15_end:
    sw s5, 20(a1)
_sort_6_7_start:
    bltu s6, s7, _sort_6_7_noswap
    mv t0, s6
    mv s6, s7
    mv s7, t0
_sort_6_7_noswap:
_sort_6_7_end:
_sort_6_8_start:
    bltu s6, s8, _sort_6_8_noswap
    mv t0, s6
    mv s6, s8
    mv s8, t0
_sort_6_8_noswap:
_sort_6_8_end:
_sort_6_9_start:
    bltu s6, s9, _sort_6_9_noswap
    mv t0, s6
    mv s6, s9
    mv s9, t0
_sort_6_9_noswap:
_sort_6_9_end:
_sort_6_10_start:
    bltu s6, s10, _sort_6_10_noswap
    mv t0, s6
    mv s6, s10
    mv s10, t0
_sort_6_10_noswap:
_sort_6_10_end:
_sort_6_11_start:
    bltu s6, s11, _sort_6_11_noswap
    mv t0, s6
    mv s6, s11
    mv s11, t0
_sort_6_11_noswap:
_sort_6_11_end:
_sort_6_12_start:
    bltu s6, t2, _sort_6_12_noswap
    mv t0, s6
    mv s6, t2
    mv t2, t0
_sort_6_12_noswap:
_sort_6_12_end:
_sort_6_13_start:
    bltu s6, t3, _sort_6_13_noswap
    mv t0, s6
    mv s6, t3
    mv t3, t0
_sort_6_13_noswap:
_sort_6_13_end:
_sort_6_14_start:
    bltu s6, t4, _sort_6_14_noswap
    mv t0, s6
    mv s6, t4
    mv t4, t0
_sort_6_14_noswap:
_sort_6_14_end:
_sort_6_15_start:
    bltu s6, t5, _sort_6_15_noswap
    mv t0, s6
    mv s6, t5
    mv t5, t0
_sort_6_15_noswap:
_sort_6_15_end:
    sw s6, 24(a1)
_sort_7_8_start:
    bltu s7, s8, _sort_7_8_noswap
    mv t0, s7
    mv s7, s8
    mv s8, t0
_sort_7_8_noswap:
_sort_7_8_end:
_sort_7_9_start:
    bltu s7, s9, _sort_7_9_noswap
    mv t0, s7
    mv s7, s9
    mv s9, t0
_sort_7_9_noswap:
_sort_7_9_end:
_sort_7_10_start:
    bltu s7, s10, _sort_7_10_noswap
    mv t0, s7
    mv s7, s10
    mv s10, t0
_sort_7_10_noswap:
_sort_7_10_end:
_sort_7_11_start:
    bltu s7, s11, _sort_7_11_noswap
    mv t0, s7
    mv s7, s11
    mv s11, t0
_sort_7_11_noswap:
_sort_7_11_end:
_sort_7_12_start:
    bltu s7, t2, _sort_7_12_noswap
    mv t0, s7
    mv s7, t2
    mv t2, t0
_sort_7_12_noswap:
_sort_7_12_end:
_sort_7_13_start:
    bltu s7, t3, _sort_7_13_noswap
    mv t0, s7
    mv s7, t3
    mv t3, t0
_sort_7_13_noswap:
_sort_7_13_end:
_sort_7_14_start:
    bltu s7, t4, _sort_7_14_noswap
    mv t0, s7
    mv s7, t4
    mv t4, t0
_sort_7_14_noswap:
_sort_7_14_end:
_sort_7_15_start:
    bltu s7, t5, _sort_7_15_noswap
    mv t0, s7
    mv s7, t5
    mv t5, t0
_sort_7_15_noswap:
_sort_7_15_end:
    sw s7, 28(a1)
_sort_8_9_start:
    bltu s8, s9, _sort_8_9_noswap
    mv t0, s8
    mv s8, s9
    mv s9, t0
_sort_8_9_noswap:
_sort_8_9_end:
_sort_8_10_start:
    bltu s8, s10, _sort_8_10_noswap
    mv t0, s8
    mv s8, s10
    mv s10, t0
_sort_8_10_noswap:
_sort_8_10_end:
_sort_8_11_start:
    bltu s8, s11, _sort_8_11_noswap
    mv t0, s8
    mv s8, s11
    mv s11, t0
_sort_8_11_noswap:
_sort_8_11_end:
_sort_8_12_start:
    bltu s8, t2, _sort_8_12_noswap
    mv t0, s8
    mv s8, t2
    mv t2, t0
_sort_8_12_noswap:
_sort_8_12_end:
_sort_8_13_start:
    bltu s8, t3, _sort_8_13_noswap
    mv t0, s8
    mv s8, t3
    mv t3, t0
_sort_8_13_noswap:
_sort_8_13_end:
_sort_8_14_start:
    bltu s8, t4, _sort_8_14_noswap
    mv t0, s8
    mv s8, t4
    mv t4, t0
_sort_8_14_noswap:
_sort_8_14_end:
_sort_8_15_start:
    bltu s8, t5, _sort_8_15_noswap
    mv t0, s8
    mv s8, t5
    mv t5, t0
_sort_8_15_noswap:
_sort_8_15_end:
    sw s8, 32(a1)
_sort_9_10_start:
    bltu s9, s10, _sort_9_10_noswap
    mv t0, s9
    mv s9, s10
    mv s10, t0
_sort_9_10_noswap:
_sort_9_10_end:
_sort_9_11_start:
    bltu s9, s11, _sort_9_11_noswap
    mv t0, s9
    mv s9, s11
    mv s11, t0
_sort_9_11_noswap:
_sort_9_11_end:
_sort_9_12_start:
    bltu s9, t2, _sort_9_12_noswap
    mv t0, s9
    mv s9, t2
    mv t2, t0
_sort_9_12_noswap:
_sort_9_12_end:
_sort_9_13_start:
    bltu s9, t3, _sort_9_13_noswap
    mv t0, s9
    mv s9, t3
    mv t3, t0
_sort_9_13_noswap:
_sort_9_13_end:
_sort_9_14_start:
    bltu s9, t4, _sort_9_14_noswap
    mv t0, s9
    mv s9, t4
    mv t4, t0
_sort_9_14_noswap:
_sort_9_14_end:
_sort_9_15_start:
    bltu s9, t5, _sort_9_15_noswap
    mv t0, s9
    mv s9, t5
    mv t5, t0
_sort_9_15_noswap:
_sort_9_15_end:
    sw s9, 36(a1)
_sort_10_11_start:
    bltu s10, s11, _sort_10_11_noswap
    mv t0, s10
    mv s10, s11
    mv s11, t0
_sort_10_11_noswap:
_sort_10_11_end:
_sort_10_12_start:
    bltu s10, t2, _sort_10_12_noswap
    mv t0, s10
    mv s10, t2
    mv t2, t0
_sort_10_12_noswap:
_sort_10_12_end:
_sort_10_13_start:
    bltu s10, t3, _sort_10_13_noswap
    mv t0, s10
    mv s10, t3
    mv t3, t0
_sort_10_13_noswap:
_sort_10_13_end:
_sort_10_14_start:
    bltu s10, t4, _sort_10_14_noswap
    mv t0, s10
    mv s10, t4
    mv t4, t0
_sort_10_14_noswap:
_sort_10_14_end:
_sort_10_15_start:
    bltu s10, t5, _sort_10_15_noswap
    mv t0, s10
    mv s10, t5
    mv t5, t0
_sort_10_15_noswap:
_sort_10_15_end:
    sw s10, 40(a1)
_sort_11_12_start:
    bltu s11, t2, _sort_11_12_noswap
    mv t0, s11
    mv s11, t2
    mv t2, t0
_sort_11_12_noswap:
_sort_11_12_end:
_sort_11_13_start:
    bltu s11, t3, _sort_11_13_noswap
    mv t0, s11
    mv s11, t3
    mv t3, t0
_sort_11_13_noswap:
_sort_11_13_end:
_sort_11_14_start:
    bltu s11, t4, _sort_11_14_noswap
    mv t0, s11
    mv s11, t4
    mv t4, t0
_sort_11_14_noswap:
_sort_11_14_end:
_sort_11_15_start:
    bltu s11, t5, _sort_11_15_noswap
    mv t0, s11
    mv s11, t5
    mv t5, t0
_sort_11_15_noswap:
_sort_11_15_end:
    sw s11, 44(a1)
_sort_12_13_start:
    bltu t2, t3, _sort_12_13_noswap
    mv t0, t2
    mv t2, t3
    mv t3, t0
_sort_12_13_noswap:
_sort_12_13_end:
_sort_12_14_start:
    bltu t2, t4, _sort_12_14_noswap
    mv t0, t2
    mv t2, t4
    mv t4, t0
_sort_12_14_noswap:
_sort_12_14_end:
_sort_12_15_start:
    bltu t2, t5, _sort_12_15_noswap
    mv t0, t2
    mv t2, t5
    mv t5, t0
_sort_12_15_noswap:
_sort_12_15_end:
    sw t2, 48(a1)
_sort_13_14_start:
    bltu t3, t4, _sort_13_14_noswap
    mv t0, t3
    mv t3, t4
    mv t4, t0
_sort_13_14_noswap:
_sort_13_14_end:
_sort_13_15_start:
    bltu t3, t5, _sort_13_15_noswap
    mv t0, t3
    mv t3, t5
    mv t5, t0
_sort_13_15_noswap:
_sort_13_15_end:
    sw t3, 52(a1)
_sort_14_15_start:
    bltu t4, t5, _sort_14_15_noswap
    mv t0, t4
    mv t4, t5
    mv t5, t0
_sort_14_15_noswap:
_sort_14_15_end:
    sw t4, 56(a1)
    sw t5, 60(a1)
_end:
    j _end
