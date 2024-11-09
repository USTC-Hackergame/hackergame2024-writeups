from z3 import *
import numpy as np

def solve_puzzle(n, initial_state):

    # 创建一个布尔变量矩阵，表示每个点的开关状态
    S = [[[Bool(f"S_{i}_{j}_{k}") for k in range(n)] for j in range(n)] for i in range(n)]
    
    # 创建一个求解器
    solver = Solver()

    # 将初始灯光状态转化为三维数组
    initial_lights = np.array(initial_state).reshape((n, n, n))
    
    # 添加约束条件
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # 获取当前点及其邻近点的开关状态
                neighbors = [S[i][j][k]]
                if i > 0: neighbors.append(S[i-1][j][k])  # 上
                if i < n-1: neighbors.append(S[i+1][j][k])  # 下
                if j > 0: neighbors.append(S[i][j-1][k])  # 左
                if j < n-1: neighbors.append(S[i][j+1][k])  # 右
                if k > 0: neighbors.append(S[i][j][k-1])  # 前
                if k < n-1: neighbors.append(S[i][j][k+1])  # 后

                # 异或关系：计算多个开关的异或
                xor_expr = neighbors[0]
                for neighbor in neighbors[1:]:
                    xor_expr = Xor(xor_expr, neighbor) 
                
                initial_light_state = True if initial_lights[i, j, k] else False
                solver.add(xor_expr == initial_light_state)

    # 求解器求解
    if solver.check() == sat:
        model = solver.model()
        solution = np.zeros((n, n, n), dtype=int)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    solution[i, j, k] = 1 if model.eval(S[i][j][k]) else 0
        return solution
    else:
        return None

def generate_answer(n, solution):
    # 将解转化为01序列
    return ''.join(map(str, solution.flatten()))

# 主程序

if __name__ == "__main__":
    # 输入难度
    difficulty = int(input("Enter difficulty level (1~3): "))
    
    if difficulty == 1:
        n = 3
    elif difficulty == 2:
        n = 5
    elif difficulty == 3:
        n = 11
    else:
        raise ValueError("Invalid difficulty level")
    
    # 输入初始灯光状态的01序列
    initial_state = input(f"Enter the initial light state for {n**3} points as a binary sequence (0s and 1s): ")
    
    if len(initial_state) != n**3:
        raise ValueError(f"Initial state must be a sequence of {n**3} binary digits.")
    
    # 将初始灯光状态转化为数字列表
    initial_state = [int(x) for x in initial_state]
    
    # 求解
    solution = solve_puzzle(n, initial_state)
    
    if solution is not None:
        print("Solution found:")
        answer = generate_answer(n, solution)
        print(answer)
    else:
        print("No solution found.")

# 题目源码
# 这是3D关灯游戏的源代码。请确保你正确理解了题目：按下一个点的开关时，其周围的点（包括自身）的灯的开关状态会反转。现在请使用z3库来求解这个3D关灯问题。具体地来说，你需要将n**3的立方体内每一个点都设置为一个未知数，他们的取值为0或1，这些未知数的值即代表了最初的开关灯数组状态。而在z3求解器中添加方程时，你需要对灯光数组中每一个点都列写一个方程：当前点灯光数组的值等于其相邻点（包括自己）的异或和。然后用z3求解器求解这个方程组，把结果整理成一个题目能识别的n**3的01序列输入。
# 请根据如下要求修改代码：初始除了输入n以外还将输入一个n**3的01序列表示初始的灯光状态。z3求解器添加约束时请根据灯光初始状态添加
# 执行你的代码发生如下错误TypeError: Xor() takes from 2 to 3 positional arguments but 4 were given 请修改

# flag{bru7e_f0rce_1s_a1l_y0u_n3ed_8b9a43d33e}
# flag{prun1ng_1s_u5eful_6ede2e5608}
# flag{lin3ar_alg3bra_1s_p0werful_d243d8b66e}

'''
#Z3尝试解t4未果，复杂度还是太爆了
token = your_token

import numpy
import zlib
import base64
import time
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from pwn import *

def decrypt_and_decompress(data: str, key: bytes) -> str:
    data = base64.b64decode(data.encode('utf-8'))
    cipher = AES.new(key, AES.MODE_CBC, iv=data[:AES.block_size])
    decrypted_data = unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size)
    decompressed_data = zlib.decompress(decrypted_data).decode('utf-8')
    return decompressed_data

p = remote('202.38.93.141',10098)
p.sendlineafter(b': ', token.encode())

p.sendlineafter(b'(1~4): ',b'4')
enc = p.recvline().strip().decode()
p.sendline()
aeskey = p.recvline().strip().split(b': ')[1].decode()

print("aeskey hex:", aeskey )
aeskey = bytes.fromhex(aeskey)
print("aeskey :", aeskey , "len :",len(aeskey))

inputdata = decrypt_and_decompress(enc,aeskey)
initial_state = [int(x) for x in inputdata]

print("Init successful")

solution = solve_puzzle(149, initial_state)
    
if solution is not None:
    print("Solution found:")
    answer = generate_answer(149, solution)
    sha256_of_answer = hashlib.sha256(answer).hexdigest()
    p.sendline(sha256_of_answer.encode())
    p.sendlineafter(b'answer:',answer.encode())
    print(p.recvline())
    print(p.recvline())
    print(p.recvline())
    # print(answer)
else:
    print("No solution found.")
    
'''