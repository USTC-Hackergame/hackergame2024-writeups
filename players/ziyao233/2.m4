	.global _start
	.text

define(`regidx', `eval($1 + 16)')
define(`numreg', `format(x%d, regidx($1))')

define(`gen_load', `dnl
	lw		numreg($1),dnl
			format(%d(x1), eval($1 * 4))
	ifelse($1, 0, `', `gen_load(decr($1))')')

define(`gen_store', `dnl
	sw		numreg($1),dnl
			format(%d(x1), eval($1 * 4))
	ifelse($1, 0, `', `gen_store(decr($1))')')

dnl $1: start
dnl x1: current minimum index
dnl x2: current minimum value
define(`gen_cmp_and_set', `
	bgeu		numreg($1),	x2,		1f
	li		x1,		regidx($1)
	mv		x2,		numreg($1)
1:	ifelse($1, 15, `', `gen_cmp_and_set(incr($1))')')

dnl $1: start
define(`cmp_and_select', `dnl
	li		x1,		regidx($1)
	mv		x2,		numreg($1)
	gen_cmp_and_set($1)
	slli		x1,		x1,		7
	lla		x4,		1f
	li		x5,		0x18013		// addi zero, x3, 0
	or		x5,		x5,		x1
	sw		x5,		0(x4)
	fence.i
	addi		x3,		numreg($1),	0
	addi		numreg($1),	x2,		0
1:	addi		zero,		x3,		0')

define(`gen_sort_seq', `
	cmp_and_select($1)
	ifelse($1, 15, `', `gen_sort_seq(incr($1))')')

_start:
	li		x1,		0xf80
	gen_load(15)

	gen_sort_seq(0)

	li		x1,		0xfc0
	gen_store(15)

_end:
	j		_end
