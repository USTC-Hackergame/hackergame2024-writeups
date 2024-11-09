#!/bin/bash

python3 solve1.py
riscv64-unknown-elf-as -march=rv32i -mabi=ilp32 riscv.S -o a.out
python3 offset_helper.py
python3 solve1.py
riscv64-unknown-elf-as -march=rv32i -mabi=ilp32 riscv.S -o a.out
riscv64-unknown-elf-objcopy -O binary a.out a.bin
python3 makehex.py a.bin > firmware.hex