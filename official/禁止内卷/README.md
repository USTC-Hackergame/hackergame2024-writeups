# 禁止内卷

题解作者：[taoky](https://github.com/taoky)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：web

- 题目分值：250

**（以下剧情均为虚构，请助教和学生都不要模仿！）**

XXX 课程实验一内容：

> 本实验需要使用给定的用户评论预测用户对书籍、电影和动画的评分。
>
> …………（部分省略）
>
> 我们提供来自诸如某瓣、某某艺、某字母站、某某米等网站的一部分用户评论和评分数据作为训练集，你需要使用这些数据训练模型，来预测对于另一部分给定的评论（测试集），用户会打出怎样的给分。测试集只提供评论数据，不提供评分。用户评分均归一化到 0 到 100 分的整数。
>
> 对于我们给定的 50000 项的测试集，本实验要求提交对这些测试集你的模型的输出结果，以 JSON 列表的格式输出，列表中每一项是一个 0 到 100 的整数。
>
> 特别地，为了鼓励同学们互相 PK，我们特别开设了评分网站，提供**前 500 项**的数据测试。诸位可以在做实验的时候提交自己的结果，直接看到自己距离预期分数的平方差，更有榜单功能。
>
> 实验 DDL：…………（部分省略）

但是这周的实验和作业实在是太多了，太多了，太多了。而且和你同班的有至少 114 个卷王。你刷新着榜单网站，看到榜一越来越小的平方差，陷入了绝望。

不过你的舍友好像之前说他帮这门课助教写了个啥东西（没有加分），好像就是这个网站。你私聊问他要到了源代码，白盒审计的时候发现了不得了的事情……你发现，你不仅可以拿到答案，而且可以搞点破坏，让各位卷王不要再卷了！

本题的 flag 位于评分数据**原始 JSON 文件**的列表头部，将对应的数字加 65 后使用 ASCII 编码转换后即为 flag 文本。

这是你从舍友那里获取到的网站主要代码文件：

<details markdown="1">
  <summary style="display: revert; cursor: pointer" markdown="1"><b>题目源代码</b>（点击展开）</summary>

```python3
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
        for idx, i in enumerate(answers):
            if i < 0:
                answers[idx] = 0
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
        score = 0
        for idx, i in enumerate(answers):
            score += (i - user[idx]) * (i - user[idx])
    except:
        flash("分数计算出现错误")
        traceback.print_exc()
        return redirect("/")
    # ok, update results
    results.append(score)
    with open("results.json", "w") as f:
        json.dump(results, f)
    flash(f"评测成功，你的平方差为 {score}")
    return redirect("/")
```

</details>

提示：助教部署的时候偷懒了，直接用了 `flask run`（当然了，助教也读过 Flask 的文档，所以 DEBUG 是关了的）。而且有的时候助教想改改代码，又懒得手动重启，所以还开了 `--reload`。启动的**完整命令**为 `flask run --reload --host 0`。网站代码运行在 `/tmp/web`。

提示：点击下面的「打开/下载题目」按钮会为你创建一个独立的题目环境，有效时间一小时。如果环境遇到问题，可以 [关闭环境](https://chal02-manager.hack-challenge.lug.ustc.edu.cn/docker-manager/stop?{token}) 后再试。

[打开/下载题目](https://chal02-manager.hack-challenge.lug.ustc.edu.cn/docker-manager/start?{token})

## 题解

本题事实上是由真实案例改编的，当然当时用的不是平方差，数据集也没这么离谱（

看过 [Flask 文档 "Uploading Files"](https://flask.palletsprojects.com/en/stable/patterns/fileuploads/) 的同学应该知道，有一个重要的函数 `secure_filename()`，用来处理用户提供的文件名：

```console
>> secure_filename("My cool movie.mov")
'My_cool_movie.mov'
>> secure_filename("../../../etc/passwd")
'etc_passwd'
>> secure_filename('i contain cool \xfcml\xe4uts.txt')
'i_contain_cool_umlauts.txt'
```

但是题目代码没有做这样的处理。从浏览器的 devtools 可以注意到，在上传文件的时候，HTTP 请求长这样：

```http
POST /submit HTTP/1.1
Host: chal02-y6bf22ju.hack-challenge.lug.ustc.edu.cn:8443
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,zh-CN;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate, br, zstd
Content-Type: multipart/form-data; boundary=---------------------------315661599216369553353790654512
Content-Length: 253
Origin: https://chal02-y6bf22ju.hack-challenge.lug.ustc.edu.cn:8443
DNT: 1
Connection: keep-alive
Referer: https://chal02-y6bf22ju.hack-challenge.lug.ustc.edu.cn:8443/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Sec-GPC: 1
Priority: u=0, i
Pragma: no-cache
Cache-Control: no-cache

-----------------------------315661599216369553353790654512
Content-Disposition: form-data; name="file"; filename="hostname"
Content-Type: application/octet-stream

hostname.example.com

-----------------------------315661599216369553353790654512--
```

Body 里的 `filename` 就对应的代码中的 `file.filename`，虽然是「文件名」，但是没有什么东西在阻止你往这个文件名里面加别的字符，比如说 `/` 和 `.`。如果 `filename` 是 `../../../../../tmp/a`，那么 `os.path.join` 和 `file.save` 都不会做任何处理，导致路径穿越漏洞。

然后接下来我们需要确定要写什么文件，写到哪里。根据题目提示，一个非常直觉的做法就是覆盖掉这段 Python 代码的文件。根据 [Flask "Command Line Interface"](https://flask.palletsprojects.com/en/stable/cli/) 的文档可以知道：

> While --app supports a variety of options for specifying your application, most use cases should be simple. Here are the typical values:
>
> (nothing)
>
> The name “app” or “wsgi” is imported (as a “.py” file, or package), automatically detecting an app (app or application) or factory (create_app or make_app).

可以尝试下面几种选项：

- `/tmp/web/app.py`（题目的实际文件位置）
- `/tmp/web/wsgi.py`
- `/tmp/web/app/__init__.py`
- `/tmp/web/wsgi/__init__.py`

最后一步是要发修改后的请求。Burp Suite 可以轻松实现，如果没有的话也没事，Firefox 开发者工具也支持修改并重放包。不过如果用后者的话，Firefox 似乎无法在重放时正确处理文件中的中文字符（原因不明），因此需要手动把中文字符删掉。

我没有找到用 curl 修改文件名的方法，如果有知道的话欢迎在自己的 writeup 中写出。

## 致谢与附注

在此非常感谢徐童老师与 2019 秋季学期的 [Web 信息处理与应用](https://icourse.club/course/18319/)课程的助教，以及为助教编写相关实验评测网站的同学（我不太确定这里提及名字是否合适）。

本代码中使用 JSON 文件而不是 SQLite（或者别的数据库）保存结果，事实上也是直接拿的当时的实验评测网站的逻辑。

有反馈问：如果是算平方差的话，是不是构造很多数据去试就能试出来——最开始将所有项都设置成 0，然后对第 $i$ 项设置成 1，那么就能知道平方差减小了 $n_i^2-(n_i-1)^2$，可以把 $n_i$ 算出来。不过如果真的去尝试，会发现拿不到完全正确的 flag（只能拿到一部分），因为在 flask 代码中也做了「归一化」的操作：

```python
for idx, i in enumerate(answers):
    if i < 0:
        answers[idx] = 0
```

因为 flag 中有些字符（比如说感叹号）不在对应的范围里面。当时没有考虑那么多，不过弄巧成拙的是，也算是排除了一个非预期解？否则这题的分类就是简单的 math 了。最后的结果也是和题目文案相符的，毕竟算平方差的时候 `answers` 确实是 0 到 100 的嘛。也有人在群里说题目有误导性，但是明明我在题面里面写了是 **原始 JSON 文件**！我还加粗了，真的不看题的话我也没有什么办法 :(
