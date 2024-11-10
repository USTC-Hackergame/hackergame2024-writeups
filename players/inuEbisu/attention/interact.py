from pwn import *
from algo import attention

LOCAL_DEBUG = False
remote_ip = "202.38.93.141"
remote_port = 14514
local_process = "graceful_inequality.py"
context(os = "linux", log_level = "info")
token = "CENSORED"

if LOCAL_DEBUG:
    io = process(local_process)
else:
    io = remote(remote_ip, remote_port)
    io.recvline()
    io.sendline(token.encode())

# Start interact

n = 0
n_next = 0
count = 0

while count < 40:
    count += 1
    info(f"Case {count}:")

    # Receive
    io.recvuntil(b">=", timeout = 5)
    frac = io.recvuntil(b"\n", timeout = 5).decode()[:-1]
    info(frac)

    # Get p, q
    ints = frac.split("/")
    if len(ints) == 2:
        p, q = int(ints[0]), int(ints[1])
    elif len(ints) == 1:
        p, q = int(ints[0]), 1
    
    # Attention is all you need!
    n_solved, res = attention(p, q, n)

    # Happy output
    io.sendline(res.encode())
    info(n_solved)
    info(res)
    info(b"")
    n = n_solved

info(io.recvall())
io.close()