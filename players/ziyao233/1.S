# riscv64-elf-as -march=rv32i -mabi=ilp32 *.S -o a.out && riscv64-elf-objcopy -O binary a.out a.bin && python3 makehex.py a.bin > firmware.hex
.section .text

	.org		0

// dst = src1 - src2
.macro	sub_num		dst, src1, src2
	sw		a0,			-4(sp)
	addi		sp,			sp,		-4

	mv		a0,			\src2
	call		get_not
	addi		a0,			a0,		1
	add		\dst,			\src1,		a0

	addi		sp,			sp,		4
	lw		a0,			-4(sp)
.endmacro

/*	t5, t6 as scratch register		*/
.macro jmp_not_equal	src1, src2, dst
	sub_num		t6,			\src1,			\src2

	sw		t6,			-4(sp)

	lbu		t6,			-4(sp)
	add		t6,			t6,			s5
	// add		t5,			zero,			zero
	lbu		t5,			0(t6)

	lbu		t6,			-3(sp)
	add		t6,			t6,			s5
	lbu		t6,			0(t6)
	add		t5,			t5,			t6

	lbu		t6,			-2(sp)
	add		t6,			t6,			s5
	lbu		t6,			0(t6)
	add		t5,			t5,			t6

	lbu		t6,			-1(sp)
	add		t6,			t6,			s5
	lbu		t6,			0(t6)
	add		t5,			t5,			t6

	lla		t6,			to\@
	add		t6,			t6,			t5
	jr		t6

to\@:
	j		\dst
	j		\dst
	j		\dst
	j		\dst
.endmacro

/*	t5, t6 used as scratch register	*/
.macro jmp_if_less	src1, src2, dst
	sub_num		t6,			\src1,			\src2

	sw		t6,			-4(sp)
	lbu		t6,			-1(sp)
	add		t6,			t6,			s4
	lbu		t6,			0(t6)

	lla		t5,			to\@
	add		t6,			t6,			t5
	jr		t6
to\@:	j		\dst

.endmacro

	.global		_start
_start:
	lla		s6,		not_table
	lla		s5,		sum_table
	lla		s4,		cmp_table
	j really_start
not_table:

	.byte 0xff, 0xfe, 0xfd, 0xfc, 0xfb, 0xfa, 0xf9, 0xf8
	.byte 0xf7, 0xf6, 0xf5, 0xf4, 0xf3, 0xf2, 0xf1, 0xf0
	.byte 0xef, 0xee, 0xed, 0xec, 0xeb, 0xea, 0xe9, 0xe8
	.byte 0xe7, 0xe6, 0xe5, 0xe4, 0xe3, 0xe2, 0xe1, 0xe0
	.byte 0xdf, 0xde, 0xdd, 0xdc, 0xdb, 0xda, 0xd9, 0xd8
	.byte 0xd7, 0xd6, 0xd5, 0xd4, 0xd3, 0xd2, 0xd1, 0xd0
	.byte 0xcf, 0xce, 0xcd, 0xcc, 0xcb, 0xca, 0xc9, 0xc8
	.byte 0xc7, 0xc6, 0xc5, 0xc4, 0xc3, 0xc2, 0xc1, 0xc0
	.byte 0xbf, 0xbe, 0xbd, 0xbc, 0xbb, 0xba, 0xb9, 0xb8
	.byte 0xb7, 0xb6, 0xb5, 0xb4, 0xb3, 0xb2, 0xb1, 0xb0
	.byte 0xaf, 0xae, 0xad, 0xac, 0xab, 0xaa, 0xa9, 0xa8
	.byte 0xa7, 0xa6, 0xa5, 0xa4, 0xa3, 0xa2, 0xa1, 0xa0
	.byte 0x9f, 0x9e, 0x9d, 0x9c, 0x9b, 0x9a, 0x99, 0x98
	.byte 0x97, 0x96, 0x95, 0x94, 0x93, 0x92, 0x91, 0x90
	.byte 0x8f, 0x8e, 0x8d, 0x8c, 0x8b, 0x8a, 0x89, 0x88
	.byte 0x87, 0x86, 0x85, 0x84, 0x83, 0x82, 0x81, 0x80
	.byte 0x7f, 0x7e, 0x7d, 0x7c, 0x7b, 0x7a, 0x79, 0x78
	.byte 0x77, 0x76, 0x75, 0x74, 0x73, 0x72, 0x71, 0x70
	.byte 0x6f, 0x6e, 0x6d, 0x6c, 0x6b, 0x6a, 0x69, 0x68
	.byte 0x67, 0x66, 0x65, 0x64, 0x63, 0x62, 0x61, 0x60
	.byte 0x5f, 0x5e, 0x5d, 0x5c, 0x5b, 0x5a, 0x59, 0x58
	.byte 0x57, 0x56, 0x55, 0x54, 0x53, 0x52, 0x51, 0x50
	.byte 0x4f, 0x4e, 0x4d, 0x4c, 0x4b, 0x4a, 0x49, 0x48
	.byte 0x47, 0x46, 0x45, 0x44, 0x43, 0x42, 0x41, 0x40
	.byte 0x3f, 0x3e, 0x3d, 0x3c, 0x3b, 0x3a, 0x39, 0x38
	.byte 0x37, 0x36, 0x35, 0x34, 0x33, 0x32, 0x31, 0x30
	.byte 0x2f, 0x2e, 0x2d, 0x2c, 0x2b, 0x2a, 0x29, 0x28
	.byte 0x27, 0x26, 0x25, 0x24, 0x23, 0x22, 0x21, 0x20
	.byte 0x1f, 0x1e, 0x1d, 0x1c, 0x1b, 0x1a, 0x19, 0x18
	.byte 0x17, 0x16, 0x15, 0x14, 0x13, 0x12, 0x11, 0x10
	.byte 0xf, 0xe, 0xd, 0xc, 0xb, 0xa, 0x9, 0x8
	.byte 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0

sum_table:
	.byte 4, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0

cmp_table:
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 4, 4, 4, 4, 4, 4, 4, 4
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0
	.byte 0, 0, 0, 0, 0, 0, 0, 0

	.fill		64
stack_top:
const_data_area:
src_loc_addr:		.long		0xf80
dst_loc_addr:		.long		0xfc0
really_start:
	lla		t0,		const_data_area
	lla		sp,		stack_top
	/*
		la a0, 0xf80 # location of numbers
		la a1, 0xfc0 # location to write sorted numbers
	 */
//	lw		a0,		0(t0)
//	lw		a1,		4(t0)
	li		a0,		0xf80
	li		a1,		0xfc0
	mv t0, zero
	//	li t2, 15*4 # n-1
	addi t2, zero, 30
	addi t2, t2, 30
_loop1:
	li t1, 0 # j
//	sub t3, t2, t0 # n-1-i
	sub_num		t3,		t2,		t0
_loop2:
	add t4, a0, t1
	lw s0, (t4) # [j]
	lw s1, 4(t4) # [j+1]
//	bltu s0, s1, _noexchange
	jmp_if_less s0, s1, _noexchange
	mv s2, s0
	mv s0, s1
	mv s1, s2
	sw s0, (t4)
	sw s1, 4(t4)
_noexchange:
	addi t1, t1, 4 # j++
//	bne t1, t3, _loop2
	jmp_not_equal t1, t3, _loop2
	addi t0, t0, 4 # i++
//	bne t0, t2, _loop1
	jmp_not_equal t0, t2, _loop1

	li t0, 0 # copy to destination
	addi		t2,		zero,		32
	addi		t2,		t2,		32
_loop3:
	add t4, a0, t0
	add t5, a1, t0
	lw s0, (t4)
	sw s0, (t5)
	addi t0, t0, 4
//	bne t0, t2, _loop3
	jmp_not_equal t0, t2, _loop3

_end:
	j _end

/*	get ~a0		*/
get_not:
	sw		a0,			-4(sp)

	lbu		a0,			-4(sp)
	add		a0,			a0,			s6
	lbu		a0,			0(a0)
	sb		a0,			-4(sp)

	lbu		a0,			-3(sp)
	add		a0,			a0,			s6
	lbu		a0,			0(a0)
	sb		a0,			-3(sp)

	lbu		a0,			-2(sp)
	add		a0,			a0,			s6
	lbu		a0,			0(a0)
	sb		a0,			-2(sp)

	lbu		a0,			-1(sp)
	add		a0,			a0,			s6
	lbu		a0,			0(a0)
	sb		a0,			-1(sp)

	lw		a0,			-4(sp)
	ret
