# 关灯

题解作者：[mingliangz](https://github.com/mlzeng)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：math

- 题目分值：Easy（100）+ Medium（100）+ Hard（100）+ Impossible（300）

3D 版本的关灯游戏。

注：解决这道题不需要很多计算资源，一般的笔记本电脑都是可以完成任务的。最后一问传输数据量较大而且时限很短，为了避免网速的影响，使用了多阶段的题目下载与答案上传机制。

<details markdown="1">
  <summary style="display: revert; cursor: pointer" markdown="1"><b>题目源代码</b>（点击展开） <a href="files/lights_out.py">下载</a></summary>

```python3
import numpy
import zlib
import base64
import time
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def convert_switch_array_to_lights_array(switch_array: numpy.array) -> numpy.array:
    lights_array = numpy.zeros_like(switch_array)
    lights_array ^= switch_array
    lights_array[:-1, :, :] ^= switch_array[1:, :, :]
    lights_array[1:, :, :] ^= switch_array[:-1, :, :]
    lights_array[:, :-1, :] ^= switch_array[:, 1:, :]
    lights_array[:, 1:, :] ^= switch_array[:, :-1, :]
    lights_array[:, :, :-1] ^= switch_array[:, :, 1:]
    lights_array[:, :, 1:] ^= switch_array[:, :, :-1]
    return lights_array

def generate_puzzle(n: int) -> numpy.array:
    random_bytes = get_random_bytes((n**3) // 8 + 1)
    switch_array = numpy.unpackbits(numpy.frombuffer(random_bytes, dtype=numpy.uint8))[:(n**3)].reshape(n, n, n)
    lights_array = convert_switch_array_to_lights_array(switch_array)
    return lights_array

def compress_and_encrypt(data: str, key: bytes) -> str:
    compressed_data = zlib.compress(data.encode('utf-8'))
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = base64.b64encode(cipher.iv + cipher.encrypt(pad(compressed_data, AES.block_size))).decode('utf-8')
    return encrypted_data

def decrypt_and_decompress(data: str, key: bytes) -> str:
    data = base64.b64decode(data.encode('utf-8'))
    cipher = AES.new(key, AES.MODE_CBC, iv=data[:AES.block_size])
    decrypted_data = unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size)
    decompressed_data = zlib.decompress(decrypted_data).decode('utf-8')
    return decompressed_data

difficulty = int(input("Enter difficulty level (1~4): "))

if difficulty == 1:
    n = 3
    time_limit = 200
elif difficulty == 2:
    n = 5
    time_limit = 200
elif difficulty == 3:
    n = 11
    time_limit = 200
elif difficulty == 4:
    n = 149
    time_limit = 10
else:
    raise ValueError("Invalid difficulty level")

lights_array = generate_puzzle(n)
lights_string = "".join(map(str, lights_array.flatten().tolist()))
key = get_random_bytes(16)
encrypted_data = compress_and_encrypt(lights_string, key)
assert lights_string == decrypt_and_decompress(encrypted_data, key)

# print the puzzle
if difficulty != 4:
    start_time = time.time()
    print(lights_string)
else:
    print(encrypted_data)
    input("Press [Enter] to reveal the decryption key and start the timer: ")
    start_time = time.time()
    print(key.hex())  # Hint: you can use bytes.fromhex method to convert the hex string to bytes

# get the answer
if difficulty != 4:
    answer = input("Enter your answer: ").strip()
    stop_time = time.time()
    if stop_time - start_time > time_limit:
        raise RuntimeError("Time limit exceeded")
else:
    commitment = input("Enter SHA-256 hash of your answer as soon as possible: ")
    stop_time = time.time()
    if stop_time - start_time > time_limit:
        raise RuntimeError("Time limit exceeded")
    answer = input("Enter your answer: ").strip()
    sha256_of_answer = hashlib.sha256(answer.encode('utf-8')).hexdigest()
    if sha256_of_answer != commitment:
        raise ValueError("Invalid commitment {} != {}".format(sha256_of_answer, commitment))

# check the answer
if len(answer) != n**3:
    raise ValueError("Invalid answer length {} != {}".format(len(answer), n**3))
if not all(map(lambda x: x in "01", answer)):
    raise ValueError("Invalid answer format (only 0 and 1 are allowed)")
switch_array = numpy.array(list(map(int, answer)), dtype=numpy.uint8).reshape(n, n, n)
actual_lights_array = convert_switch_array_to_lights_array(switch_array)
if not numpy.array_equal(lights_array, actual_lights_array, equal_nan=False):
    raise ValueError("Incorrect answer")

# print the flag
print(open(f"flag{difficulty}").read())
```

</details>

你可以通过 `nc 202.38.93.141 10098` 来连接，或者点击下面的「打开/下载题目」按钮通过网页终端与远程交互。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

[打开/下载题目](http://202.38.93.141:10099/?token={token})

## 题解

经典版本关灯游戏的解法可以在网络上找到很多资料，3D 版本关灯游戏解法也是类似的。第一问只有 $3^3=27$ 个灯，可以直接枚举全部可能的操作，一共是 $2^{27}=134217728$ 种情况。第二问有 $5^3=125$ 个灯，直接枚举是不行的，但是可以只枚举最上面一层的操作，一共 $5^2=25$ 个灯，然后逐层推导出其它地方的操作，那么只需要枚举 $2^{25}=33554432$ 种情况。第三问有 $11^3=1331$ 个灯，只枚举一层 $11^2=121$ 个灯也是不现实的，但是可以把问题转换为异或方程组求解，使用高斯消元算法就能直接解出答案，整体算法复杂度是 $O(n^9)$，所需计算次数的量级是 2e9，是可以接受的。

第四问是比较难的，如果按照第三问的做法，所需计算次数的量级是 3e19，是不可接受的，需要一些高级的算法优化。第四问的解法是结合第二问和第三问的解法。

经典版本关灯游戏有一个技巧叫做 light chasing，先通过逐层关闭法把灯关闭到只剩底部的一层，然后根据底部状态查表点击顶层的灯，最后再做一次逐层关闭，底部的灯就会被全部关闭。

```
Bottom row is:      Toggle on top row:

11100               01000
□□□■■	            ■□■■■

11011               00100
□□■□□	            ■■□■■

10110               00001
□■□□■	            ■■■■□

10001               11000
□■■■□	            □□■■■

01101               10000
■□□■□	            □■■■■

01010               10010
■□■□■	            □■■□■

00111               00010
■■□□□	            ■■■□■
```

仔细思考可以发现，底层的灯的状态和顶部的操作方案是线性相关的，对于更大规模更高维度的情形也是一样。这也就意味着，可以对 3D 版本的关灯游戏进行同样的操作，利用线性代数方法根据底部的灯的状态解出顶部的操作方案。

枚举顶部的每个灯，假设只有这一个灯亮着，计算逐层关闭后底部的状态，得到 $n^2*n^2$ 的 01 矩阵，这一步算法复杂度为 $O(n^5)$，会需要比较长时间，但是这个矩阵是固定不变的，可以提前算出来，不受解题时限的约束。

然后就可以列出异或方程组解出操作方案了，如果直接用高斯消元算法，算法复杂度是 $O(n^6)$，会导致解题超时。但是方程里面矩阵是固定不变的，所以可以提前对矩阵进行 PLU 分解，之后就可以利用分解结果快速求解异或方程组了，算法复杂度为 $O(n^4)$，足以在时限内解出答案。

解题脚本第一次运行时会计算 PLU 分解结果并保存成文件，之后再次运行时会直接读取这个文件，这样就可以在时限内解出答案了。对于前三问，分解和求解都是瞬间完成。对于第四问，分解需要大约十分钟，求解需要大约一秒钟。

```python
import numpy
import os
import sys
import pwn
import base64
import zlib
import hashlib
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def lu_decomposition_mod2(A):
    """
    Perform LU decomposition of a matrix A over GF(2) with pivoting.

    Parameters:
    A (array-like): A square binary matrix.

    Returns:
    P (ndarray): Permutation matrix over GF(2).
    L (ndarray): Lower triangular matrix over GF(2).
    U (ndarray): Upper triangular matrix over GF(2).
    """
    A = numpy.array(A, dtype=bool)
    n = A.shape[0]
    if A.shape[1] != n:
        raise ValueError("Input matrix must be square.")

    # Initialize P as an identity matrix
    P = numpy.eye(n, dtype=bool)
    L = numpy.eye(n, dtype=bool)
    U = A.copy()
    rank = 0

    for k in range(n):
        print(f'LU {k}/{n}', file=sys.stderr)
        # Pivot if necessary
        if not U[k, k]:
            # Find a row below with a 1 in the k-th column
            rows_with_one = numpy.where(U[k+1:, k])[0]
            if rows_with_one.size > 0:
                i = rows_with_one[0] + k + 1  # Adjust index
                # Swap rows in U
                U[[k, i], k:] = U[[i, k], k:]
                # Swap rows in P
                P[[k, i], :] = P[[i, k], :]
                # Swap rows in L, but only columns before k
                if k > 0:
                    L[[k, i], :k] = L[[i, k], :k]
                rank += 1
            else:
                # Cannot pivot; U[k, k] remains zero
                continue
        else:
            rank += 1

        # Identify rows to eliminate
        rows_below = numpy.arange(k+1, n)
        rows_to_eliminate = rows_below[U[rows_below, k]]

        # Update L and U
        L[rows_to_eliminate, k] = True
        U[rows_to_eliminate, k+1:] ^= U[k, k+1:]
        U[rows_to_eliminate, k] = False

    print(f"Rank: {rank}", file=sys.stderr)

    return P, L, U


def forward_substitution_mod2(L, b):
    """
    Solve the lower triangular system L y = b (mod 2) using forward substitution.

    Parameters:
    L (ndarray): Lower triangular matrix over GF(2) with ones on the diagonal.
    b (ndarray): Right-hand side vector.

    Returns:
    y (ndarray): Solution vector.
    """
    n = L.shape[0]
    y = numpy.zeros(n, dtype=bool)
    for i in range(n):
        sum_Ly = numpy.dot(L[i, :i], y[:i]) % 2
        y[i] = (b[i] ^ sum_Ly) % 2  # XOR operation
    return y


def back_substitution_mod2(U, y):
    """
    Solve the upper triangular system U x = y (mod 2) using back substitution.

    Parameters:
    U (ndarray): Upper triangular matrix over GF(2).
    y (ndarray): Right-hand side vector.

    Returns:
    x (ndarray): Solution vector, or None if no solution exists.
    """
    n = U.shape[0]
    x = numpy.zeros(n, dtype=bool)
    for i in reversed(range(n)):
        if U[i, i]:
            sum_Ux = numpy.dot(U[i, i+1:], x[i+1:]) % 2
            x[i] = (y[i] ^ sum_Ux) % 2  # XOR operation
        else:
            sum_Ux = numpy.dot(U[i, i+1:], x[i+1:]) % 2
            if y[i] != sum_Ux:
                # No solution exists
                return None
            else:
                # Variable can be assigned any value; we choose 0
                x[i] = False
    return x


def solve_mod2(n, b, PLU=None):
    if PLU is not None:
        P, L, U = PLU
    else:
        P, L, U = lu_decomposition_mod2(get_matrix(n))
        P = P.astype(numpy.uint8)
        L = L.astype(numpy.uint8)
        U = U.astype(numpy.uint8)
        numpy.savez_compressed(f'PLU-{n}.npz', P=P, L=L, U=U)

    b = numpy.array(b, dtype=bool)
    # Apply permutation to b
    b_permuted = numpy.dot(P, b) % 2
    # Forward substitution to solve L y = b_permuted
    y = forward_substitution_mod2(L, b_permuted)
    # Back substitution to solve U x = y
    x = back_substitution_mod2(U, y)
    if x is None:
        print("The system has no solution.")
    return x.astype(numpy.uint8) if x is not None else None


def get_matrix(n):
    def test(i, j, n):
        lights = numpy.zeros((n, n, n), dtype=numpy.uint8)
        lights[0, i, j] = 1
        lights[1, i, j] = 1
        if i > 0:
            lights[0, i - 1, j] = 1
        if i < n - 1:
            lights[0, i + 1, j] = 1
        if j > 0:
            lights[0, i, j - 1] = 1
        if j < n - 1:
            lights[0, i, j + 1] = 1
        for level in range(n - 1):
            x = level
            y = (level + 1)
            z = (level + 2)
            lights[y, :, :] ^= lights[x, :, :]
            lights[y, :-1, :] ^= lights[x, 1:, :]
            lights[y, 1:, :] ^= lights[x, :-1, :]
            lights[y, :, :-1] ^= lights[x, :, 1:]
            lights[y, :, 1:] ^= lights[x, :, :-1]
            if level < n - 2:
                lights[z, :, :] ^= lights[x, :, :]
            lights[x, :, :] = 0
        return lights[-1, :, :]
    mat = []
    for i in range(n):
        print(f'GM {i}/{n}', file=sys.stderr)
        for j in range(n):
            mat.append(test(i, j, n).flatten().astype(numpy.uint8))
    return numpy.array(mat)


def lights_chasing(lights):
    switch = numpy.zeros_like(lights)
    n = lights.shape[0]
    for level in range(n - 1):
        x = level
        y = (level + 1)
        z = (level + 2)
        lights[y, :, :] ^= lights[x, :, :]
        lights[y, :-1, :] ^= lights[x, 1:, :]
        lights[y, 1:, :] ^= lights[x, :-1, :]
        lights[y, :, :-1] ^= lights[x, :, 1:]
        lights[y, :, 1:] ^= lights[x, :, :-1]
        if level < n - 2:
            lights[z, :, :] ^= lights[x, :, :]
        switch[y, :, :] ^= lights[x, :, :]
        lights[x, :, :] = 0
    return switch


def decrypt_and_decompress(data: str, key: bytes) -> str:
    data = base64.b64decode(data.encode('utf-8'))
    cipher = AES.new(key, AES.MODE_CBC, iv=data[:AES.block_size])
    decrypted_data = unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size)
    decompressed_data = zlib.decompress(decrypted_data).decode('utf-8')
    return decompressed_data


difficulty = int(sys.argv[1])
if difficulty == 1:
    n = 3
elif difficulty == 2:
    n = 5
elif difficulty == 3:
    n = 11
elif difficulty == 4:
    n = 149
else:
    raise ValueError("Invalid difficulty level.")

PLU = None
if os.path.exists(f'PLU-{n}.npz'):
    with numpy.load(f'PLU-{n}.npz') as data:
        P = data['P']
        L = data['L']
        U = data['U']
        PLU = (P, L, U)

conn = pwn.remote('202.38.93.141', 10098)
token = open('token').read().strip()
conn.sendline(token.encode())
conn.recvuntil(b'Enter difficulty level (1~4): ')
conn.sendline(str(difficulty).encode())
if difficulty == 4:
    enc = conn.recvline().strip().decode()
    conn.recvuntil(b'start the timer: ')
    conn.sendline(b'')
    key = conn.recvline().strip().decode()
    lights = decrypt_and_decompress(enc, bytes.fromhex(key))
else:
    lights = conn.recvline().strip().decode()
start_time = time.time()
assert set(lights) <= set('01')
lights = numpy.array(list(map(int, lights)), dtype=numpy.uint8)
assert (n**3) == lights.size
lights = lights.reshape(n, n, n)
switch = lights_chasing(lights)
b = lights[-1].flatten()
x = solve_mod2(n, b, PLU=PLU)
switch[0] ^= x.reshape(n, n)
lights[0, :, :] ^= switch[0, :, :]
lights[1, :, :] ^= switch[0, :, :]
lights[0, :-1, :] ^= switch[0, 1:, :]
lights[0, 1:, :] ^= switch[0, :-1, :]
lights[0, :, :-1] ^= switch[0, :, 1:]
lights[0, :, 1:] ^= switch[0, :, :-1]
switch ^= lights_chasing(lights)
assert numpy.all(lights == 0)
answer = ''.join(map(str, switch.flatten().tolist()))
commitment = hashlib.sha256(answer.encode()).hexdigest().encode()
end_time = time.time()
print(f"Time used: {end_time - start_time:.2f} seconds")
if difficulty == 4:
    conn.recvuntil(b'as soon as possible: ')
    conn.sendline(commitment)
    conn.recvuntil(b'Enter your answer: ')
    conn.sendline(answer.encode())
else:
    conn.recvuntil(b'Enter your answer: ')
    conn.sendline(answer.encode())
print(conn.recvall().decode())
```