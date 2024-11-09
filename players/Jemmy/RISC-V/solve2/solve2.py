lines = []

lines.append(".section .text")
lines.append("_start:")

read_ptr = 0xf80
write_ptr = 0xf40
final_ptr = 0xfc0

registers = ['s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 't2', 't3', 't4', 't5']

lines.append(f"    la a0, {hex(read_ptr)}")
lines.append(f"    la a1, {hex(final_ptr)}")

for i in range(16):
    lines.append(f"    lw {registers[i]}, {i * 4}(a0)")

for i in range(0, 16):

    for j in range(i + 1, 16):
        lines.append(f"_sort_{i}_{j}_start:")

        lines.append(f"    bltu {registers[i]}, {registers[j]}, _sort_{i}_{j}_noswap")
        lines.append(f"    mv t0, {registers[i]}")
        lines.append(f"    mv {registers[i]}, {registers[j]}")
        lines.append(f"    mv {registers[j]}, t0")
        lines.append(f"_sort_{i}_{j}_noswap:")
        lines.append(f"_sort_{i}_{j}_end:")
    lines.append(f"    sw {registers[i]}, {i * 4}(a1)")

lines.append("_end:")
lines.append("    j _end")

with open("riscv.S", "w") as f:
    f.write("\n".join(lines))
    f.write("\n")
    f.close()
