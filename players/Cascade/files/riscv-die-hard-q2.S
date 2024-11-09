# riscv64-elf-as -march=rv32i -mabi=ilp32 *.S -o a.out && riscv64-elf-objcopy -O binary a.out a.bin && python3 makehex.py a.bin > firmware.hex
.section .text
_start:
    la x30, 0xf80
    la x31, 0xfc0
    
    lw x1, 0(x30)
    lw x2, 4(x30)
    lw x3, 8(x30)
    lw x4, 12(x30)
    lw x5, 16(x30)
    lw x6, 20(x30)
    lw x7, 24(x30)
    lw x8, 28(x30)
    lw x9, 32(x30)
    lw x10, 36(x30)
    lw x11, 40(x30)
    lw x12, 44(x30)
    lw x13, 48(x30)
    lw x14, 52(x30)
    lw x15, 56(x30)
    lw x16, 60(x30)

# Insert 2
_in2:
    bgt x2, x1, _in3
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in3:
    bgt x3, x2, _in4
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in4
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in4:
    bgt x4, x3, _in5
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in5
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in5
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in5:
    bgt x5, x4, _in6
    mv x29, x5
    mv x5, x4
    mv x4, x29

    bgt x4, x3, _in6
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in6
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in6
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in6:
    bgt x6, x5, _in7
    mv x29, x6
    mv x6, x5
    mv x5, x29

    bgt x5, x4, _in7
    mv x29, x5
    mv x5, x4
    mv x4, x29

    bgt x4, x3, _in7
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in7
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in7
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in7:
    bgt x7, x6, _in8
    mv x29, x7
    mv x7, x6
    mv x6, x29

    bgt x6, x5, _in8
    mv x29, x6
    mv x6, x5
    mv x5, x29

    bgt x5, x4, _in8
    mv x29, x5
    mv x5, x4
    mv x4, x29

    bgt x4, x3, _in8
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in8
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in8
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in8:
    bgt x8, x7, _in9
    mv x29, x8
    mv x8, x7
    mv x7, x29

    bgt x7, x6, _in9
    mv x29, x7
    mv x7, x6
    mv x6, x29

    bgt x6, x5, _in9
    mv x29, x6
    mv x6, x5
    mv x5, x29

    bgt x5, x4, _in9
    mv x29, x5
    mv x5, x4
    mv x4, x29

    bgt x4, x3, _in9
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in9
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in9
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in9:
    bgt x9, x8, _in10
    mv x29, x9
    mv x9, x8
    mv x8, x29

    bgt x8, x7, _in10
    mv x29, x8
    mv x8, x7
    mv x7, x29

    bgt x7, x6, _in10
    mv x29, x7
    mv x7, x6
    mv x6, x29

    bgt x6, x5, _in10
    mv x29, x6
    mv x6, x5
    mv x5, x29

    bgt x5, x4, _in10
    mv x29, x5
    mv x5, x4
    mv x4, x29

    bgt x4, x3, _in10
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in10
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in10
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in10:
    bgt x10, x9, _in11
    mv x29, x10
    mv x10, x9
    mv x9, x29

    bgt x9, x8, _in11
    mv x29, x9
    mv x9, x8
    mv x8, x29

    bgt x8, x7, _in11
    mv x29, x8
    mv x8, x7
    mv x7, x29

    bgt x7, x6, _in11
    mv x29, x7
    mv x7, x6
    mv x6, x29

    bgt x6, x5, _in11
    mv x29, x6
    mv x6, x5
    mv x5, x29

    bgt x5, x4, _in11
    mv x29, x5
    mv x5, x4
    mv x4, x29

    bgt x4, x3, _in11
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in11
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in11
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in11:
    bgt x11, x10, _in12
    mv x29, x11
    mv x11, x10
    mv x10, x29

    bgt x10, x9, _in12
    mv x29, x10
    mv x10, x9
    mv x9, x29

    bgt x9, x8, _in12
    mv x29, x9
    mv x9, x8
    mv x8, x29

    bgt x8, x7, _in12
    mv x29, x8
    mv x8, x7
    mv x7, x29

    bgt x7, x6, _in12
    mv x29, x7
    mv x7, x6
    mv x6, x29

    bgt x6, x5, _in12
    mv x29, x6
    mv x6, x5
    mv x5, x29

    bgt x5, x4, _in12
    mv x29, x5
    mv x5, x4
    mv x4, x29

    bgt x4, x3, _in12
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in12
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in12
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in12:
    bgt x12, x11, _in13
    mv x29, x12
    mv x12, x11
    mv x11, x29

    bgt x11, x10, _in13
    mv x29, x11
    mv x11, x10
    mv x10, x29

    bgt x10, x9, _in13
    mv x29, x10
    mv x10, x9
    mv x9, x29

    bgt x9, x8, _in13
    mv x29, x9
    mv x9, x8
    mv x8, x29

    bgt x8, x7, _in13
    mv x29, x8
    mv x8, x7
    mv x7, x29

    bgt x7, x6, _in13
    mv x29, x7
    mv x7, x6
    mv x6, x29

    bgt x6, x5, _in13
    mv x29, x6
    mv x6, x5
    mv x5, x29

    bgt x5, x4, _in13
    mv x29, x5
    mv x5, x4
    mv x4, x29

    bgt x4, x3, _in13
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in13
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in13
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in13:
    bgt x13, x12, _in14
    mv x29, x13
    mv x13, x12
    mv x12, x29

    bgt x12, x11, _in14
    mv x29, x12
    mv x12, x11
    mv x11, x29

    bgt x11, x10, _in14
    mv x29, x11
    mv x11, x10
    mv x10, x29

    bgt x10, x9, _in14
    mv x29, x10
    mv x10, x9
    mv x9, x29

    bgt x9, x8, _in14
    mv x29, x9
    mv x9, x8
    mv x8, x29

    bgt x8, x7, _in14
    mv x29, x8
    mv x8, x7
    mv x7, x29

    bgt x7, x6, _in14
    mv x29, x7
    mv x7, x6
    mv x6, x29

    bgt x6, x5, _in14
    mv x29, x6
    mv x6, x5
    mv x5, x29

    bgt x5, x4, _in14
    mv x29, x5
    mv x5, x4
    mv x4, x29

    bgt x4, x3, _in14
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in14
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in14
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in14:
    bgt x14, x13, _in15
    mv x29, x14
    mv x14, x13
    mv x13, x29

    bgt x13, x12, _in15
    mv x29, x13
    mv x13, x12
    mv x12, x29

    bgt x12, x11, _in15
    mv x29, x12
    mv x12, x11
    mv x11, x29

    bgt x11, x10, _in15
    mv x29, x11
    mv x11, x10
    mv x10, x29

    bgt x10, x9, _in15
    mv x29, x10
    mv x10, x9
    mv x9, x29

    bgt x9, x8, _in15
    mv x29, x9
    mv x9, x8
    mv x8, x29

    bgt x8, x7, _in15
    mv x29, x8
    mv x8, x7
    mv x7, x29

    bgt x7, x6, _in15
    mv x29, x7
    mv x7, x6
    mv x6, x29

    bgt x6, x5, _in15
    mv x29, x6
    mv x6, x5
    mv x5, x29

    bgt x5, x4, _in15
    mv x29, x5
    mv x5, x4
    mv x4, x29

    bgt x4, x3, _in15
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in15
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in15
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in15:
    bgt x15, x14, _in16
    mv x29, x15
    mv x15, x14
    mv x14, x29

    bgt x14, x13, _in16
    mv x29, x14
    mv x14, x13
    mv x13, x29

    bgt x13, x12, _in16
    mv x29, x13
    mv x13, x12
    mv x12, x29

    bgt x12, x11, _in16
    mv x29, x12
    mv x12, x11
    mv x11, x29

    bgt x11, x10, _in16
    mv x29, x11
    mv x11, x10
    mv x10, x29

    bgt x10, x9, _in16
    mv x29, x10
    mv x10, x9
    mv x9, x29

    bgt x9, x8, _in16
    mv x29, x9
    mv x9, x8
    mv x8, x29

    bgt x8, x7, _in16
    mv x29, x8
    mv x8, x7
    mv x7, x29

    bgt x7, x6, _in16
    mv x29, x7
    mv x7, x6
    mv x6, x29

    bgt x6, x5, _in16
    mv x29, x6
    mv x6, x5
    mv x5, x29

    bgt x5, x4, _in16
    mv x29, x5
    mv x5, x4
    mv x4, x29

    bgt x4, x3, _in16
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in16
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in16
    mv x29, x2
    mv x2, x1
    mv x1, x29
_in16:
    bgt x16, x15, _in17
    mv x29, x16
    mv x16, x15
    mv x15, x29

    bgt x15, x14, _in17
    mv x29, x15
    mv x15, x14
    mv x14, x29

    bgt x14, x13, _in17
    mv x29, x14
    mv x14, x13
    mv x13, x29

    bgt x13, x12, _in17
    mv x29, x13
    mv x13, x12
    mv x12, x29

    bgt x12, x11, _in17
    mv x29, x12
    mv x12, x11
    mv x11, x29

    bgt x11, x10, _in17
    mv x29, x11
    mv x11, x10
    mv x10, x29

    bgt x10, x9, _in17
    mv x29, x10
    mv x10, x9
    mv x9, x29

    bgt x9, x8, _in17
    mv x29, x9
    mv x9, x8
    mv x8, x29

    bgt x8, x7, _in17
    mv x29, x8
    mv x8, x7
    mv x7, x29

    bgt x7, x6, _in17
    mv x29, x7
    mv x7, x6
    mv x6, x29

    bgt x6, x5, _in17
    mv x29, x6
    mv x6, x5
    mv x5, x29

    bgt x5, x4, _in17
    mv x29, x5
    mv x5, x4
    mv x4, x29

    bgt x4, x3, _in17
    mv x29, x4
    mv x4, x3
    mv x3, x29

    bgt x3, x2, _in17
    mv x29, x3
    mv x3, x2
    mv x2, x29

    bgt x2, x1, _in17
    mv x29, x2
    mv x2, x1
    mv x1, x29

_in17:
    sw x1, 0(x31)
    sw x2, 4(x31)
    sw x3, 8(x31)
    sw x4, 12(x31)
    sw x5, 16(x31)
    sw x6, 20(x31)
    sw x7, 24(x31)
    sw x8, 28(x31)
    sw x9, 32(x31)
    sw x10, 36(x31)
    sw x11, 40(x31)
    sw x12, 44(x31)
    sw x13, 48(x31)
    sw x14, 52(x31)
    sw x15, 56(x31)
    sw x16, 60(x31)

_end:
    j _end
