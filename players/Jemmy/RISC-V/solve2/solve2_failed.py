lines = []

lines.append(".section .text")
lines.append("_start:")

read_ptr = 0xf80
write_ptr = 0xf40
final_ptr = 0xfc0

lines.append(f"    la a0, {hex(read_ptr)}")
lines.append(f"    la a1, {hex(write_ptr)}")
lines.append(f"    la a2, {hex(final_ptr)}")
lines.append(f"    li s3, 0x7fffffff # min number of this round")

for i in range(0, 16*4, 4):
    lines.append(f"    mv s0, s3")

    for j in range(i, 16*4, 4):
        lines.append(f"_sort_{i}_{j}_start:")

        lines.append(f"    lw s1, {j}(a0)")
        lines.append(f"    bltu s0, s1, _sort_{i}_{j}_noswap")
        lines.append(f"    mv s2, s0")
        lines.append(f"    mv s0, s1")
        lines.append(f"    mv s1, s2")
        lines.append(f"_sort_{i}_{j}_noswap:")
        if j != i:
            lines.append(f"    sw s1, {j}(a1)")

        if j == 16*4 - 4:
            lines.append(f"    sw s0, {i}(a2)")
        lines.append(f"_sort_{i}_{j}_end:")

    lines.append(f"    addi a0, a0, -64")
    lines.append(f"    addi a1, a1, -64")

lines.append("_end:")
lines.append("    j _end")

with open("riscv.S", "w") as f:
    f.write("\n".join(lines))
    f.write("\n")
    f.close()
