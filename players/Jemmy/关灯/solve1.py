from sage.all import *
from pwn import *

n = 3
N = n**3

def toggle(v, x, y, z):
    if x < 0 or x >= n or y < 0 or y >= n or z < 0 or z >= n:
        return
    v[x * n**2 + y * n + z] ^= 1

def build_matrix():
    global A
    A = matrix(GF(2), N, N)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                v = [0 for _ in range(N)]
                toggle(v, x, y, z)
                toggle(v, x+1, y, z)
                toggle(v, x-1, y, z)
                toggle(v, x, y+1, z)
                toggle(v, x, y-1, z)
                toggle(v, x, y, z+1)
                toggle(v, x, y, z-1)
                for i in range(N):
                    A[i, x * n**2 + y * n + z] = v[i]


def solve(s):
    global A
    v = vector(GF(2), [int(c) for c in s])
    r = A.solve_right(v)
    return "".join(str(int(c)) for c in r)

build_matrix()

local = False
if local:
    io = process(["python3", "lights.py"])
else:
    io = remote('202.38.93.141', 10098)
    io.recvuntil(b'Please input your token: \n')
    io.sendline(b'1411:MEQCIAplFMrlOcSGiuyvXbD2viXkZel+YtLmOBzUXj48+rzXAiBrX2C/xRLIxhAn+TJYUsQtGEDzpleulEFWzyijebwTXA==')

io.recvuntil(b"Enter difficulty level (1~4): ")
io.sendline(b"1")
question = io.recvline().strip()
print('Question', question)

answer = solve(question)
io.recvuntil(b"Enter your answer: ")
io.sendline(answer.encode())
print(io.recvall())