from sage.all import *
from pwn import *
from tqdm import tqdm
from hashlib import sha256

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import zlib

n = 149

def getVector(v, rs=None):
    m0 = [[0 for _ in range(n)] for _ in range(n)]
    m1 = [[v[i * n + j] for j in range(n)] for i in range(n)]
    # m1 = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(1, n + 1):
        m = [[0 for _ in range(n)] for _ in range(n)]
        r = rs[i - 1] if rs else [0 for _ in range(n * n)]
        r = [r[i * n: (i + 1) * n] for i in range(n)]
        for j in range(n):
            for k in range(n):
                v = m0[j][k] + m1[j][k] + r[j][k]
                if j > 0:
                    v += m1[j - 1][k]
                if j < n - 1:
                    v += m1[j + 1][k]
                if k > 0:
                    v += m1[j][k - 1]
                if k < n - 1:
                    v += m1[j][k + 1]
                m[j][k] = v % 2
        m0, m1 = m1, m
    return [m1[i][j] for i in range(n) for j in range(n)]


def prepare_hint():
    global hinter, ignore

    ignore = set()
    with open('ignore.txt', 'r') as f:
        for line in f:
            ignore.add(int(line.strip()))

    hinter = process("./hinter")
    hinter.recvuntil(b"Ready\n")


def get_hint(v):
    global hinter, ignore
    print('Getting hint')
    b = bytes([v[j] + ord('0') for j in range(n * n) if j not in ignore])
    hinter.sendline(b)
    print('Sent input')
    hint = hinter.recvline().decode().strip()
    print('Got hint')
    result = []
    pos = 0
    for i in range(n * n):
        if i in ignore:
            result.append(0)
        else:
            result.append(int(hint[pos]))
            pos += 1
    assert pos == len(hint)
    print('Finished hint')
    return result


def getAnswer(v, rs):
    m0 = [[0 for _ in range(n)] for _ in range(n)]
    m1 = [[v[i * n + j] for j in range(n)] for i in range(n)]

    m = []
    m.append(m1)

    for i in range(1, n):
        m2 = [[0 for _ in range(n)] for _ in range(n)]
        r = rs[i - 1] if rs else [0 for _ in range(n * n)]
        r = [r[i * n: (i + 1) * n] for i in range(n)]
        for j in range(n):
            for k in range(n):
                v = m0[j][k] + m1[j][k] + r[j][k]
                if j > 0:
                    v += m1[j - 1][k]
                if j < n - 1:
                    v += m1[j + 1][k]
                if k > 0:
                    v += m1[j][k - 1]
                if k < n - 1:
                    v += m1[j][k + 1]
                m2[j][k] = v % 2
        m0, m1 = m1, m2
        m.append(m1)
    return m


def decrypt_and_decompress(data: str, key: bytes) -> str:
    data = base64.b64decode(data.encode('utf-8'))
    cipher = AES.new(key, AES.MODE_CBC, iv=data[:AES.block_size])
    decrypted_data = unpad(cipher.decrypt(
        data[AES.block_size:]), AES.block_size)
    decompressed_data = zlib.decompress(decrypted_data).decode('utf-8')
    return decompressed_data


def solve(question):
    global A
    question = [int(question[i]) for i in range(n ** 3)]
    question = [question[i * n**2: (i + 1) * n**2] for i in range(n)]

    v0 = [0 for _ in range(n * n)]
    r0 = getVector(v0, question)
    hint = get_hint(r0)

    result = getAnswer(hint, question)
    result = [str(result[i][j][k]) for i in range(n)
              for j in range(n) for k in range(n)]
    return ''.join(result)


prepare_hint()
local = False
if local:
    io = process(["python3", "lights.py"])
else:
    io = remote('202.38.93.141', 10098)
    io.recvuntil(b'Please input your token: \n')
    io.sendline(
        b'1411:MEQCIAplFMrlOcSGiuyvXbD2viXkZel+YtLmOBzUXj48+rzXAiBrX2C/xRLIxhAn+TJYUsQtGEDzpleulEFWzyijebwTXA==')

io.recvuntil(b"Enter difficulty level (1~4): ")
io.sendline(b"4")
# io.recvuntil(b"Hint: ")
# hint = io.recvline().decode().strip()
encrypted_data = io.recvline().decode().strip()
io.recvuntil(
    b"Press [Enter] to reveal the decryption key and start the timer: ")
io.sendline()
key = bytes.fromhex(io.recvline().decode().strip())
question = decrypt_and_decompress(encrypted_data, key)

answer = solve(question)
# print('Answer', answer)
sha256_of_answer = hashlib.sha256(answer.encode('utf-8')).hexdigest()
io.recvuntil(b"Enter SHA-256 hash of your answer as soon as possible: ")
io.sendline(sha256_of_answer.encode())

io.recvuntil(b"Enter your answer: ")
io.sendline(answer.encode())
print(io.recvall())
