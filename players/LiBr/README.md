# LiBr

简单题解（

## 签到

`http://202.38.93.141:12024/?pass=false`=>`http://202.38.93.141:12024/?pass=true`

##  喜欢做签到的 CTFer 你们好呀

https://www.nebuu.la/ 

```bash
ls -la
cat .flag
env
```

## 猫咪问答（Hackergame 十周年纪念版）

```
1. https://lug.ustc.edu.cn/wiki/sec/contest.html
2. https://lug.ustc.edu.cn/news/2019/12/hackergame-2019/
3. https://github.com/ustclug/hackergame2018-writeups/blob/master/misc/others.md
4. https://www.usenix.org/system/files/usenixsecurity24-ma-jinrui.pdf 
5. https://github.com/torvalds/linux/commit/6e90b675cf942e50c70e8394dfb5862975c3b3b2
6.找个 tokenizer 就好
```

## 打不开的盒

找个 3D 建模软件把视角放进去就好

## 每日论文太多了！

用 word/ps 打开，搜索 flag，移除上面的图片。

## 比大小王

```python
import requests as r
from urllib.parse import quote
from json import dumps
from time import sleep
s = r.Session()
host = "202.38.93.141:12122"
token = ""
headers = {
    "Host": host,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
}
assert s.get(f"http://{host}/?token={quote(token)}",headers=headers,allow_redirects=False).status_code == 302
response = s.post(f"http://{host}/game",headers={
    "Host": host,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Content-Type": "application/json",
},data="{}").json()["values"]

request = {"inputs":["<>"[int(i[0]>i[1])] for i in response]}
sleep(6)
print(s.post(f"http://{host}/submit",headers={
    "Host": host,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Content-Type": "application/json",
},data=dumps(request)).json())
```

## 旅行照片

1.1 关键词：科里科气科创驿站

1.2 关键词：中科大 ACG 音乐会

2.1 图片垃圾桶旁边有六安公园

2.2 丢谷歌识图

3.2 粉色涂装+四编组列车->CRH6F-A，怀密线S501？沿着线路找能找到三个红房子。->积水潭医院

![image-20241109195112454](https://cdn.nvme0n1p.dev/2024/11/a45acd0ab8082287ceb1b3e4aabeed47.webp)

## 不宽的宽字符

![](https://cdn.nvme0n1p.dev/2024/11/07d08d72b36bbd61b1c443a9cf084f27.webp)

把`Z:/theflag`经过如图操作之后发送即可。

## PowerfulShell

bash 默认变量+cut。

## Node.js is Web Scale

设置`__proto__.getflag`为`cat /flag`。然后 `/execute?cmd=getflag`。

## PaoluGPT

sqlmap一把梭。丢进去直接`select content where content like '%flag%'`就好。

## 强大的正则表达式

### Easy

打表后四位。

### Medium / Hard

转换为 dfa 自动机。

## 惜字如金3.0

第一问直接补全就好。

第二问可以通过给出的 hash 还原出 crc 的参数。

第三问首先还原参数，然后控制某行内容使`base85encode(hash(crc(某行内容)))='answer_c'`，可以读取 flag 文件的后几位。已知前六位，控制这六位可以撞 crc。

## 优雅的不等式

参考知乎“量化调酒师”的文章。https://zhuanlan.zhihu.com/p/669285539

## 无法获得的秘密

找到https://github.com/ganlvtech/qrcode-file-transfer/

取出其中的encode.js/qr.js/encode.html 打包后base64，通过xdotool 让键盘输入，在 vnc 中解包取出，然后录屏丢到 decode 中解码。

## Docker for Everyone Plus

### 第一问

造一个带 suid 提权的容器，拿到 root 可以直接`cat  /dev/vdb`

## 链上转账助手

丢给 GPT 能把前两问出了。

第一问 revert，第二问 whiletrue 耗gas。

## 不太分布式的软总线

GPT 可以直接三问解决。

## 动画分享

第一问使用 cargo fuzz 跑一跑。

第二问是 zutty 的 RCE 洞+chroot 逃逸。

## 关灯

前三问可以直接 GPT 搞定，写了个高斯换元。

第四问是需要预处理的 OI 题，没做😡。

## 禁止内卷

flask 开成了热重载，所以直接上传文件后修改内容就能 RCE。

## 零知识数独

第一问：玩数独

## 神秘代码

第一个：base64换表

第二个：迷惑的分组+换表+混淆输出

第三个：甚至还加了花指令

## LLM 

第一问其实就是个 wordle。大部分可以直接给 gpt 还原好。
