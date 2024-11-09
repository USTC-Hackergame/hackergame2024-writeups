# Rainy's Writeup of Hackergame 2024

> 纯新人，第一年来，菜菜 /(ㄒoㄒ)/~~

## 签到

**启动**！观察到URL带上了`?pass=false`，改为true即可拿到flag

flag{we!cOM3-TO-haCK3rGAME-AND-3njOy-H@cK1Ng-Z0Z4}

## 喜欢做签到的 CTFer 你们好呀

从[Hackergame首页](https://hack.lug.ustc.edu.cn/)下拉，在承办单位处找到 [NEBULA战队](https://www.nebuu.la/)，进入题目说的招新主页

这是一个Bash风格的网页，先打help看下可用命令，把~~sudo（奶龙😀）~~、about、env什么的先试一遍

执行env后发现一个flag

``` bash
PWD=/root/Nebula-Homepage
ARCH=loong-arch
NAME=Nebula-Dedicated-High-Performance-Workstation
OS=NixOS❄️
FLAG=flag{actually_theres_another_flag_here_trY_to_f1nD_1t_y0urself___join_us_ustc_nebula}
REQUIREMENTS=1. you must come from USTC; 2. you must be interested in security!
```

然后尝试正常ls列出目录（一开始还没往隐藏文件去想），还去搜了NixOS啥的，发现好像与本题无太大关系😂

再尝试下源代码审计，在`index-5c589ff418560b46.js`中检索flag，在第2个flag结果附近，注意到

``` javascript
"".concat(atob("ZmxhZ3swa18xNzVfYV9oMWRkM25fczNjM3J0X2YxNGdfX19wbGVhc2Vfam9pbl91c191c3RjX25lYnVsYV9hbkRfdHdvX21hSm9yX3JlcXVpcmVtZW50c19hUmVfc2hvd25fc29tZXdoZXJlX2Vsc2V9"))
```
欸，这不是base64吗，把atob(……)这段F12放到控制台执行，解码后得到第二个flag

flag{0k_175_a_h1dd3n_s3c3rt_f14g___please_join_us_ustc_nebula_anD_two_maJor_requirements_aRe_shown_somewhere_else}

## 猫咪问答（Hackergame 十周年纪念版）

1. 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？

    Hackergame从2014开始举办，2015是第二届，在[活动记录](https://lug.ustc.edu.cn/wiki/lug/events/hackergame/)找到第二届的[存档](https://lug.ustc.edu.cn/wiki/sec/contest.html)，可知3A204

2. 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？

    一年一年试，到2019年，可知2682

3. Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？

    找[Hackergame 2018 猫咪问答题解](https://github.com/ustclug/hackergame2018-writeups/blob/master/official/ustcquiz/README.md)，可知程序员的自我修养

5. 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？

    先跳第5题（感觉好找一点），直接搜索就可以找到对应的[Github Commit](https://github.com/torvalds/linux/commit/6e90b675cf942e50c70e8394dfb5862975c3b3b2)，可知6e90b6

4. 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？

    在浏览器控制台执行：

    ``` typescript
    for(let q4=1;q4<=1000;q4++){
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `q1=3A204&q2=2682&q3=%E7%A8%8B%E5%BA%8F%E5%91%98%E7%9A%84%E8%87%AA%E6%88%91%E4%BF%AE%E5%85%BB&q4=${q4}&q5=6e90b6&q6=`,
        })
            .then(response => response.text())
            .then(html => {
                //解析HTML DOM
                let parser = new DOMParser()
                let doc = parser.parseFromString(html, "text/html")
                let _text = doc.querySelector(".alert-secondary").innerText
                //分数增加就说明我们找到了答案
                if (_text.includes("75")) {
                    console.log(q4)
                }
            })
            .catch(error => {
                console.log(error)
            })
    }
    ```

    可知336

6. 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？

    穷举！在浏览器控制台执行：

    ``` typescript
    for(let q6=1000;q6<2000;q6++){
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `q1=3A204&q2=2682&q3=%E7%A8%8B%E5%BA%8F%E5%91%98%E7%9A%84%E8%87%AA%E6%88%91%E4%BF%AE%E5%85%BB&q4=336&q5=6e90b6&q6=${q6}`,
        })
            .then(response => response.text())
            .then(html => {
                let parser = new DOMParser()
                let doc = parser.parseFromString(html, "text/html")
                let _html = doc.querySelector(".alert-secondary").innerText
                if (_html.includes("为 100")) {
                    console.log(q6)
                }
            })
            .catch(error => {
                console.log(error)
            })
    }
    ```

    可知1833

## 打不开的盒

找个3D打印在线查看器，比如[这个](https://imagetostl.com/cn/view-stl-online)，放大，从2024透过去对内部截图，再 OCR识别/人眼识别手打 转文字即可取到flag

flag{Dr4W_Us!nG_fR3E_C4D!!w0W}

## 每日论文太多了！

把PDF文件下载下来，搜索flag，发现在其中一面论文的左上角一张图片里有白色字体写的"flag is here"，但是没有flag{}的字样，推测可能是被隐藏了

然后找个提取PDF中图片的工具，比如[这个](https://pdfcandy.com/cn/extract-images.html)，下载下来，其中一张图片就有flag，用OCR识别转文字即可

flag{h4PpY_hAck1ng_3veRyd4y}

## 比大小王

Web的事情就让Web来解决吧~

在浏览器控制台执行：

``` typescript
let newinputs = []

function newsubmit(inputs) {
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ inputs }),
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.message)//输出包含flag的消息
            state.stopUpdate = true
            document.getElementById('dialog').textContent = data.message
            document.getElementById('dialog').style.display = 'flex'
        })
        .catch(error => {
            console.log(error)
        })
}

function go() {
    let values = state.values;
    for (let i = 0; i < values.length; i++) {
        //拿到的是String，先转Number
        if (Number(values[i][0]) > Number(values[i][1])) {
            newinputs.push(">")
        } else {
            newinputs.push("<")
        }
    }
    setTimeout(()=>{
        newsubmit(newinputs)
    },1000)
}

go()
```

可以得到：

flag{!-4M-ThE-H4cK3r-K!nG-0f-cOmPaR!NG-NUMb3Rs-2oZ4}

## 旅行照片 4.0

1. 照片拍摄的位置距离中科大的哪个校门更近？

    东西南北都试一试，可知东校区西门

2. 话说 Leo 酱上次出现在桁架上是……科大今年的 ACG 音乐会？活动日期我没记错的话是？

    搜索“中国科大2024ACG音乐会”，可知20240519

flag{5UB5CR1B3_T0_L30_CH4N_0N_B1L1B1L1_PLZ_98794d67e7}

3. 这个公园的名称是什么？（不需要填写公园所在市区等信息）

    把图片放大，注意到垃圾桶上面有**六安**字样，搜索发现是城市名，再尝试搜这个城市的公园，对照跑道，可知中央森林公园

4. 这个景观所在的景点的名字是？（三个汉字）

    搜图，结合题目三个汉字的要求，确定坛子岭

flag{D3T41LS_M4TT3R_1F_R3V3RS3_S34RCH_1S_1MP0SS1BL3_8cb69a32c8}

5. 距离拍摄地最近的医院是？（无需包含院区、地名信息，格式：XXX医院）

    对准中间两个车间搜图，确定为[北京北动车所](http://tech.chinadaily.com.cn/a/201909/06/WS5d7197d6a31099ab995de441.html)，在地图上搜附近的医院，可知积水潭医院

6. 左下角的动车组型号是？

    搜索四编组动车型号，试出CRH6F-A

flag{1_C4NT_C0NT1NU3_TH3_5T0RY_4NYM0R3_50M30N3_PLZ_H3LP_8195f39157}

## Node.js is Web Scale

注意到：

``` typescript
let cmds = {
  getsource: "cat server.js",
  test: "echo 'hello, world!'",
};

let store = {};
```

推测原型链污染

输入 key: `__proto__.t`, value: `cat /flag`
再调用`/execute?cmd=t`

flag{n0_pr0topOIl_50_U5E_new_Map_1n5teAD_Of_0bject2kv_86e388ff83}

## PaoluGPT

### 千里挑一

Web的事情就让Web来解决吧~ +1

进入查看聊天记录页面，在浏览器控制台执行：

``` typescript
let links = document.querySelectorAll("a")
for (let i = 0; i < links.length; i++) {
    //遍历所有对话
    if (links[i].href.includes("view")) {
        fetch(links[i].href, {
            method: 'GET',
            headers: {
                'Content-Type': 'text/html',
            }
        })
            .then(response => response.text())
            .then(html => {
                let parser = new DOMParser()
                let doc = parser.parseFromString(html, "text/html")
                let _html = doc.querySelector(".container .pt-3").innerHTML
                //输出包含flag的对话
                if (_html.includes("flag")) {
                    console.log(_html)
                }
            })
            .catch(error => {
                console.log(error)
            })
    }
}
```

稍等一会，得到：

flag{zU1_xiA0_de_11m_Pa0lule!!!_196f3121f3}

### 窥视未知

查看Python源码，注意到：

``` Python
results = execute_query("select id, title from messages where shown = true", fetch_all=True)
…
results = execute_query(f"select title, contents from messages where id = '{conversation_id}'")
```

默认不显示shown=true的对话，推测另一个应该就是在shown=false的对话中，同时下边SQL查询的存在注入风险，然后构造`' or where shown = false--`

flag{enJ0y_y0uR_Sq1_&_1_would_xiaZHOU_hUI_guo_a706cea1d6}

## 惜字如金 3.0（题目A）

根据规则修改Python脚本：

``` Python
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
flag{C0mpl3ted-Th3-Pyth0n-C0de-N0w}

## 优雅的不等式（Easy）

在知乎上搜索到[文章](https://zhuanlan.zhihu.com/p/669285539)，根据其中第1种类型的原理，解出系数
`x*x*(1-x)**2*(15-2*x+15*x*x)/(1+x*x)`

flag{y0u_ar3_g0od_at_constructi0n_982b662cda}

## 零知识数独

### 数独高手

解出数独即可（应该也可在网页源代码里找混淆过的flag？

### ZK高手

搜索`snarkjs`和`circom`，配好环境

执行
``` Bash
circom sudoku.circom --r1cs --wasm --sym
```
生成`sudoku.wasm`

解出数独，根据`sudoku.circom`的要求，编辑出`input.json`

``` JSON
{
    "unsolved_grid": [
        [9, 0, 0, 0, 0, 0, 1, 0, 0],
        [8, 0, 0, 0, 0, 0, 2, 0, 0],
        [7, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 6],
        [0, 2, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 7],
        [0, 3, 0, 0, 0, 0, 0, 0, 0]
    ],   
    "solved_grid": [
        [9, 0, 0, 0, 0, 0, 1, 0, 0],
        [8, 0, 0, 0, 0, 0, 2, 0, 0],
        [7, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 6],
        [0, 2, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 7],
        [0, 3, 0, 0, 0, 0, 0, 0, 0]
    ]
}
```

执行
``` Bash
node sudoku_js/generate_witness.js sudoku.wasm input.json witness.wtns
snarkjs groth16 prove sudoku.zkey witness.wtns proof.json public.json
``` 
生成`proof.json`和`public.json`

`proof.json`
``` JSON
{
 "pi_a": [
  "8675764042730050040124473686079059135006151345534014969424964870071614018797",
  "17195090035365156877369809768777783243963395905574970663133842667808990032952",
  "1"
 ],
 "pi_b": [
  [
   "20748128216962356572272652831648516597010475465959768852216688635045904926326",
   "10009917252567508546769680988504601965080993252615750621430495365805680127858"
  ],
  [
   "3572893038827597083070199460367895852880043891776436058659254264527221527243",
   "8249384538129175745796114250196881670919110375219561724477973349773360238214"
  ],
  [
   "1",
   "0"
  ]
 ],
 "pi_c": [
  "2884699217974106299853460376620977186228499829621229753780411559592403969860",
  "11538995908966585640951866062597231689540460300896188617485836455930231898784",
  "1"
 ],
 "protocol": "groth16",
 "curve": "bn128"
}
```
`public.json`
``` JSON
[
 "0",
 "6",
 "0",
 "0",
 "4",
 "0",
 "7",
 "0",
 "1",
 "0",
 "9",
 "3",
 "0",
 "0",
 "0",
 "0",
 "0",
 "0",
 "7",
 "0",
 "0",
 "0",
 "9",
 "0",
 "8",
 "0",
 "0",
 "3",
 "0",
 "0",
 "0",
 "0",
 "0",
 "0",
 "0",
 "5",
 "0",
 "0",
 "8",
 "7",
 "0",
 "0",
 "0",
 "4",
 "0",
 "0",
 "0",
 "0",
 "0",
 "3",
 "0",
 "0",
 "0",
 "0",
 "0",
 "0",
 "0",
 "0",
 "0",
 "2",
 "1",
 "6",
 "0",
 "0",
 "4",
 "0",
 "8",
 "0",
 "5",
 "9",
 "0",
 "0",
 "0",
 "0",
 "0",
 "0",
 "0",
 "0",
 "0",
 "0",
 "7"
]
```
执行
``` Bash
snarkjs groth16 verify verification_key.json public.json proof.json
```
验证通过，提交`proof.json`

flag{you_are_a_5udoku_expert_and_pr0ved_your_kn0wledge_dc29a4dd28}

## 先不说关于我从零开始独自在异世界转生成某大厂家的 LLM 龙猫女仆这件事可不可能这么离谱，发现 Hackergame 内容审查委员会忘记审查题目标题了ごめんね，以及「这么长都快赶上轻小说了真的不会影响用户体验吗🤣」（「行吧就算标题可以很长但是 flag 一定要短点」）

Amazing啊这个标题😎

~~先尝试根据英语积累人工推测复原（人工智能，人手工的智能😎），可以复原前面的一些词~~
在本地跑一下`build.sh`，根据生成的内容中相似的部分，可以复原一些词
再到[通义千问](https://tongyi.aliyun.com/qianwen/)上面跑一下`……（x代指hackergame中的字母（包括x），请将本文段还原，用英文输出原文）`，可以再恢复一些词
基本能拿到原文，验一下sha256发现正确（这算是非预期解？

``` text
In the grand hall of Hackergame 2024, where the walls are lined with screens showing the latest exploits from the cyber world, contestants gathered in a frenzy, their eyes glued to the virtual exploits. The atmosphere was electric, with the smell of freshly brewed coffee mingling with the scent of burnt Ethernet cables. As the first challenge was announced, a team of hackers, dressed in lab coats and carrying laptops, sprinted to the nearest server room, their faces a mix of excitement and determination. The game was on, and the stakes were high, with the ultimate prize being a golden trophy and the bragging rights to say they were the best at cracking codes and hacking systems in the land of the rising sun.
```

flag{llm_lm_lm_koshitantan_fa7b655c38bc8847}

## 一点碎碎念

题目都是很有意思的，虽因时间原因（中间隔了几天没有来，周六快到十二点前最后半小时借助Kimi解出软总线第1问🤣）难以完全感受各个题目的内涵

但其中收获，却也足以令人驻足忘怀

（明年再战！/(ㄒoㄒ)/~~
