from pwn import *

local = False

if local:
    io = process(['python3', 'riscv_challenge.py'])
else:
    io = remote('202.38.93.141', 10025)
    io.recvuntil(b'Please input your token: \n')
    io.sendline(
        b'1411:MEQCIAplFMrlOcSGiuyvXbD2viXkZel+YtLmOBzUXj48+rzXAiBrX2C/xRLIxhAn+TJYUsQtGEDzpleulEFWzyijebwTXA==')
    
io.recvuntil(b'Choose your challenge: \n')
io.sendline(b'2')
io.recvuntil(b'Input your firmware in hex (empty line to end): \n')

with open('firmware.hex', 'r') as f:
    for line in f:
        io.sendline(line.strip().encode())

io.sendline('')

while True:
    try:
        print(io.recvline().decode()[:-1])
    except EOFError:
        break