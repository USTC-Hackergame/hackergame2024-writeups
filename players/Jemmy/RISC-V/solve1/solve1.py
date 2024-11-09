from offsets import *

lines = []


lines.append(".section .text")
lines.append("_start:")

read_ptr = 0xf80
final_ptr = 0xfc0

lines.append(f"    la a0, {hex(read_ptr)}")
lines.append(f"    la a1, {hex(final_ptr)}")
lines.append(f'    li sp, {hex(15 * 4)}')

# for i in range(0, 16 * 4, 4):
lines.append(f'_loop_i_init:')
lines.append(f'    li s0, 0')  # i = 0
lines.append(f'_loop_i_head:')
lines.append(f'    mv s10, s0')
lines.append(f'    mv s11, sp')
lines.append(f'    jal ra, _leq')
lines.append(f'    slli gp, gp, 2')
lines.append(f'    la a4, {offset_loop_i_exit}')
lines.append(f'    add a4, a4, gp')
lines.append(f'    jr a4')

lines.append(f'_loop_i_exit:')
lines.append(f'    j _loop_i_end')
if True:
    lines.append(f'_loop_i_body:')

    lines.append(f"    add a2, a0, s0")  # read_ptr + i
    lines.append(f"    lw s2, (a2)")  # s2 = *(read_ptr + i)

    # for j in range(i + 4, 16 * 4, 4):
    lines.append(f"_loop_j_init:")
    lines.append(f"    addi s1, s0, 4")  # j = i + 4
    lines.append(f'_loop_j_head:')

    lines.append(f'    mv s10, s1')
    lines.append(f'    mv s11, sp')
    lines.append(f'    jal ra, _leq')
    lines.append(f'    slli gp, gp, 2')
    lines.append(f'    la a4, {offset_loop_j_exit}')
    lines.append(f'    add a4, a4, gp')
    lines.append(f'    jr a4')

    lines.append(f'_loop_j_exit:')
    lines.append(f'    j _loop_j_end')

    if True:
        lines.append(f"_loop_j_body:")

        lines.append(f"    add a3, a0, s1")  # read_ptr + j
        lines.append(f"    lw s3, (a3)")  # s3 = *(read_ptr + j)

        # lines.append(f"    bltu s2, s3, _loop_j_tail")
        lines.append(f'    mv s10, s2')
        lines.append(f'    mv s11, s3')
        lines.append(f'    jal ra, _leq')
        lines.append(f'    slli gp, gp, 3')
        lines.append(f'    la a4, {offset_loop_j_swap}')
        lines.append(f'    add a4, a4, gp')
        lines.append(f'    jr a4')

        lines.append(f"_loop_j_swap:")
        lines.append(f"    sw s2, (a3)")
        lines.append(f"    mv s2, s3")

        lines.append(f"_loop_j_tail:")
        lines.append(f"    addi s1, s1, 4")
        lines.append(f"    j _loop_j_head")

    lines.append(f"_loop_j_end:")

    lines.append(f"    add a2, a1, s0")  # write_ptr + i
    lines.append(f"    sw s2, (a2)")  # *(write_ptr + i) = s2

    lines.append(f"_loop_i_tail:")
    lines.append(f"    addi s0, s0, 4")
    lines.append(f"    j _loop_i_head")

lines.append(f"_loop_i_end:")

lines.append(f"_end:")
lines.append(f"    j _end")


# lines.append("_leq:")
# lines.append("    li gp, 0")
# lines.append("    bgt s10, s11, _leq_label")
# lines.append("    li gp, 1")
# lines.append("_leq_label:")
# lines.append("    jalr zero, (ra)")

# lines.append("_leq:")
# lines.append(f"    jal s7, _bit_leq")
# lines.append(f"    jalr zero, (ra)")

# lines.append("_leq:")
# lines.append(f"    jal s7, _bit_leq")
# lines.append(f"    slli gp, gp, 2")
# lines.append(f'    la a4, {offset_leq2_exit_false}')
# lines.append(f'    add a4, a4, gp')
# lines.append(f"    jr a4")
# lines.append(f"_leq2_exit_false:")
# lines.append(f"    j _leq_ret_false")
# lines.append(f"    j _leq_ret_true")


lines.append(f"_leq:")
for i in range(31, 0, -1):
    lines.append(f"    mv s8, s10")
    lines.append(f"    srli s8, s8, {i}")
    lines.append(f"    slli s8, s8, 31")
    lines.append(f"    srli s8, s8, 31")
    lines.append(f"    mv s9, s11")
    lines.append(f"    srli s9, s9, {i}")
    lines.append(f"    slli s9, s9, 31")
    lines.append(f"    srli s9, s9, 31")

    lines.append(f"    jal s7, _bit_leq")
    lines.append(f"    slli gp, gp, 2")
    lines.append(f'    la a4, {offset_leq_exit_false[i]}')
    lines.append(f'    add a4, a4, gp')
    lines.append(f"    jr a4")
    lines.append(f"_leq_exit_false_{i}:")
    lines.append(f"    j _leq_ret_false")

    lines.append(f"    jal s7, _bit_geq")
    lines.append(f"    slli gp, gp, 2")
    lines.append(f'    la a4, {offset_leq_exit_true[i]}')
    lines.append(f'    add a4, a4, gp')
    lines.append(f"    jr a4")
    lines.append(f"_leq_exit_true_{i}:")
    lines.append(f"    j _leq_ret_true")

lines.append(f"    slli s8, s8, 31")
lines.append(f"    srli s8, s8, 31")
lines.append(f"    mv s9, s11")
lines.append(f"    slli s9, s9, 31")
lines.append(f"    srli s9, s9, 31")

lines.append(f"    jal s7, _bit_leq")
lines.append(f"    slli gp, gp, 2")
lines.append(f'    la a4, {offset_leq_exit_false[0]}')
lines.append(f'    add a4, a4, gp')
lines.append(f"    jr a4")
lines.append(f"_leq_exit_false_{0}:")
lines.append(f"    j _leq_ret_false")

lines.append(f"    jal s7, _bit_geq")
lines.append(f"    slli gp, gp, 2")
lines.append(f'    la a4, {offset_leq_exit_true[0]}')
lines.append(f'    add a4, a4, gp')
lines.append(f"    jr a4")
lines.append(f"_leq_exit_true_{0}:")
lines.append(f"    j _leq_ret_true")
lines.append(f"    j _leq_ret_true")

lines.append(f"_leq_ret_true:")
lines.append(f"    li gp, 1")
lines.append(f"    jalr zero, (ra)")

lines.append(f"_leq_ret_false:")
lines.append(f"    li gp, 0")
lines.append(f"    jalr zero, (ra)")

# lines.append(f"_bit_geq:")
# lines.append(f"    add t0, s8, 1")
# lines.append(f"    slli t0, t0, 31")
# lines.append(f"    srli t0, t0, 31")
# lines.append(f"    add t0, t0, s9")
# lines.append(f"    srli t0, t0, 1") # lt
# lines.append(f"    add t0, t0, 1")
# lines.append(f"    slli t0, t0, 31")
# lines.append(f"    srli gp, t0, 31")
# lines.append(f"    jalr zero, (s7)")

lines.append(f"_bit_geq:")
lines.append(f"    li gp, 0")
lines.append(f"    bgt s9, s8, _bit_geq_label")
lines.append(f"    li gp, 1")
lines.append(f"_bit_geq_label:")
lines.append(f"    jalr zero, (s7)")

# lines.append(f"_bit_leq:")
# lines.append(f"    add t0, s9, 1")
# lines.append(f"    slli t0, t0, 31")
# lines.append(f"    srli t0, t0, 31")
# lines.append(f"    add t0, t0, s8")
# lines.append(f"    srli t0, t0, 1") # gt
# lines.append(f"    add t0, t0, 1")
# lines.append(f"    slli t0, t0, 31")
# lines.append(f"    srli gp, t0, 31")
# lines.append(f"    mv gp, t0")
# lines.append(f"    jalr zero, (s7)")

lines.append(f"_bit_leq:")
lines.append(f"    li gp, 0")
lines.append(f"    slli s8, s8, 31")
lines.append(f"    srli s8, s8, 31")
lines.append(f"    slli s9, s9, 31")
lines.append(f"    srli s9, s9, 31")
lines.append(f"    bgt s8, s9, _bit_leq_label")
lines.append(f"    li gp, 1")
lines.append(f"_bit_leq_label:")
lines.append(f"    jalr zero, (s7)")

with open("riscv.S", "w") as f:
    f.write("\n".join(lines))
    f.write("\n")
    f.close()
