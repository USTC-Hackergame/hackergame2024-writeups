# Purofle's Writeup
> 先自我介绍：  
 Github: [Purofle](https://github.com/purofle)  
 在校高三生，实在没时间做，只做了一些简单的题目

## 签到
看到这道题之后，直接给 JavaScript 打了个断点，然后手动把答案复制了进去，然后就过了。

## 喜欢做签到的 CTFer 你们好呀
打开 USTC 校内 CTF 站内招新主页之后发现好熟悉的页面，这不就是 LiveTerm（

好巧，我的主页也是基于 LiveTerm 的：[archlinux.tech](https://archlinux.tech)。

使用 help 查看所有可用的指令，在乱尝试几次后，发现 `env` 会输出第一个 flag。
```bash
ctfer@ustc-nebula:$ ~
env
PWD=/root/Nebula-Homepage
ARCH=loong-arch
NAME=Nebula-Dedicated-High-Performance-Workstation
OS=NixOS❄️
FLAG=flag{actually_theres_another_flag_here_trY_to_f1nD_1t_y0urself___join_us_ustc_nebula}
REQUIREMENTS=1. you must come from USTC; 2. you must be interested in security!
```

第二个 flag 直接使用了 F12 大法，在 _next/static/chunks/pages/index-5cb01f7ec808f452.js 中搜索 flag 得到以下内容：
```javascript
return t.("return", ".flag\noh-you-found-it\nAwards\nMembers\come-to-USTC-Nebula-sHomepage\nand-We-are-Waiting-or-U/");
```

发现 flag 在 .flag 文件中，于是直接 `cat .flag` 得到第二个 flag。

## 猫咪问答（Hackergame 十周年纪念版）
1~5 题我跟 [官方 Writeup](https://github.com/USTC-Hackergame/hackergame2024-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E9%97%AE%E7%AD%94%EF%BC%88Hackergame%20%E5%8D%81%E5%91%A8%E5%B9%B4%E7%BA%AA%E5%BF%B5%E7%89%88%EF%BC%89/README.md) 解法相同，这里不再重复（

6.大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？

这里我在 GitHub 找到了 LLaMA 3 的在线分词器：[belladoreai/llama3-tokenizer-js](https://belladoreai.github.io/llama3-tokenizer-js/example-demo/build/)。

直接把 HTML 源代码粘贴进去，得到结果为 1833 个 token。

## 打不开的盒
电脑上正好有拓竹的切片软件，stl 模型下载之后直接使用 Bambu Studio 打开，点切片拖到下面，然后就看到 flag 了。
![image](https://github.com/user-attachments/assets/27332f27-0bd8-4bc9-ad7b-3cb4787fe754)

## 比大小王
打开题目后先人工尝试，发现不可解（或许机器人可以（x）），F12 后发现其实就是发请求给 `/game` 拿到游戏数据后通过 `submit` 函数提交，于是写 JavaScript 脚本模拟提交，得到 flag。

```javascript
fetch('/game', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({}),
      })
        .then(response => response.json())
        .then(data => {
            answer = []
            data.values.forEach(v => {
                if (v[0] > v[1]) {
                    answer.push(">")
                } else {
                    answer.push("<")
                }
            })
            setTimeout(() => {
                submit(answer)
            }, 5000);
        })
```

注意 `setTimeout` 的时间不可少，不然会提示「检测到时空穿越，挑战失败！」。

## 旅行照片 4.0
### LEO_CHAN?
高德地图直接搜索「科里科气科创驿站」，找到了这么一个地方叫「科里科气科创驿站」（科大站）。发现旁边就是中科大，观察地图后得出答案为东校区西门。

> [!NOTE]
>
> 这道题成功让我搞明白了中科大到底有几个校区（

### OMINOUS_BELL
使用新版 Chrome 单独打开照片，右键选择 Sarch with Google Lens，框选左下角的车，得出答案是 CRH6F-A。
![image](https://github.com/user-attachments/assets/c376ee5e-e668-48b3-b083-1625e476ca49)

第二题依旧是 Search with Google Lens 的界面，找到标题为“北京有一趟仅仅4节车厢的粉色动车：周末特别火”的新闻，点进去发现这辆车是 [怀密号](https://zh.wikipedia.org/wiki/%E5%8C%97%E4%BA%AC%E5%B8%82%E9%83%8A%E9%93%81%E8%B7%AF%E6%80%80%E6%9F%94%E2%80%94%E5%AF%86%E4%BA%91%E7%BA%BF)。

仔细观察图片后发现图片内并无普速列车，所以确定目标为动车运用所。

> [!NOTE]
>
> 此处需要车迷的直觉（x）

通过高德地图不难发现北京有三个动车运用所，分别是北京北，北京朝阳，北京南。因为怀密号始发为北京北，所以直接看北京北动车运用所的卫星照片，发现了拍摄点为积水潭医院。

## PaoluGPT
下载题目源代码，查看 `main.py` 后，发现明显 SQL 注入点：
```python
results = execute_query(f"select title, contents from messages where id = '{conversation_id}'")
```

问题是我并不会 SQL 注入（x），所以直接搜索 [SQL 注入的 payload](https://zh.wikipedia.org/wiki/SQL%E6%B3%A8%E5%85%A5)（没错我的 SQL 注入是现场在维基百科学的），找到了 `1' or '1'='1`，于是直接尝试，构建出以下 conversation_id：
```sql
1' or '1'='1' AND contents like '%flag%
```
于是获取到了 flag1，那么 flag2 怎么获取呢？这里我用了一个非常聪明的办法，flag1 开头是 `flag{zU1_xiA0` 那么我排除掉这些字符，剩下的 flag 就是 flag2 了（
```sql
1' or '1'='1' AND contents NOT like '%flag{zU1_xiA0%' AND contents like '%flag%
```

## 链上转账助手
### 转账失败
这道题的 flag1 拿的实在是意外，执行题目源码目录下的 `compile.py` 后，直接把 `challenge1.sol` 编译出的 bytecode 复制过去，于是就拿到 flag 1 了。

~~原理在看了官方 writeup 才明白，原来是合约默认行为是收到转账的时候会回滚~~

## 转账又失败
第二题直接 revert 不行了，于是想想别的招（

> [!NOTE]
>
> 我是真的抱着试一试的心态写出来的这一坨，没想到直接拿到 flag2 了

在 `BatchTransfer` 中发现了没用到的函数 `withdrawPending`，诶...这个函数是啥呢？要不...在 `receive` 里面调用一下这个函数试试？

```solidity
contract Hakc {
    BatchTransfer public batchTransfer;

    receive() external payable {
        batchTransfer = BatchTransfer(msg.sender);
        batchTransfer.withdrawPending();
    }
}
```

然后直接编译 Hakc 合约，拿到 flag2。

## 不太分布式的软总线
### What DBus Gonna Do?
flag1 查看源码后，发现调用 `cn.edu.ustc.lug.hack.FlagService` 的 `getFlag1` 函数并且带上 `string` 类型的 "Please give me flag1" 作为参数即可拿到 flag1：
```bash
#!/bin/bash

dbus-send --system \
          --dest=cn.edu.ustc.lug.hack.FlagService \
          --type=method_call \
          --print-reply \
          /cn/edu/ustc/lug/hack/FlagService \
          cn.edu.ustc.lug.hack.FlagService.GetFlag1 \
          string:"Please give me flag1"
```


> [!NOTE]
>
> 开始时候忘记 --system 了，导致一直报错，后来才知道这是系统总线

### If I Could Be A File Descriptor
观察 `flagserver.c` 发现 GetFlag2 的参数有以下要求：
- 需要一个文件描述符
- 需要一个 gint32 类型的参数作为 fd_index
- fd 不能指向系统上的文件
- fd 必须可被读取
- fd 读取到的内容必须是 `Please give me flag2\n`

经过整理之后，我们可以写出以下 C 代码：
```c
#include "gio/gunixfdlist.h"
#include "glib.h"
#include <time.h>
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

  GUnixFDList *fd_list = g_unix_fd_list_new();
  int fd[2];
  if (pipe(fd) == -1) {
    perror("pipe");
    exit(EXIT_FAILURE);
  }

  const char *message = "Please give me flag2\n";
  write(fd[1], message, strlen(message));


  g_unix_fd_list_append(fd_list, fd[0], NULL);

  // Call the D-Bus method
  result = g_dbus_connection_call_with_unix_fd_list_sync(
      connection,
      DEST,                         // destination
      OBJECT_PATH,                  // object path
      INTERFACE,                    // interface name
      METHOD,                       // method
      g_variant_new("(h)", 0), // parameters
      NULL,                         // expected return type
      G_DBUS_CALL_FLAGS_NONE,
      -1,      // timeout (use default)
      fd_list, // Unix FD list
      NULL, NULL, &error);

  if (result) {
    gchar *flag;
    g_variant_get(result, "(s)", &flag);
    g_print("%s\n", flag);
    g_variant_unref(result);
  } else {
    g_printerr("Error calling D-Bus method %s: %s\n", METHOD, error->message);
    g_error_free(error);
  }

  g_object_unref(connection);

  return EXIT_SUCCESS;
}
```

这里我使用 `pipe` 创建了一个管道，然后将 `Please give me flag2\n` 写入管道，最后将管道的文件描述符传递给 D-Bus，成功拿到 flag2。

### Comm Say Maybe

第三个 flag 给了 `getflag3.c`，但是它不会输出结果：
```c
if (result) {
  g_print("Get result but I won't show you :)\n");
  g_variant_unref(result);
}
```

我们可以通过修改 `getflag3.c` 来输出结果：
```c
if (result) {
    // g_print("Get result but I won't show you :)\n");
    // print result
    gchar *flag;
    g_variant_get(result, "(s)", &flag);
    g_print("%s\n", flag);
    g_variant_unref(result);
}
```

经过编译上传后，依旧无法获取 flag3。查看 `flagserver.c` 发现会使用 `/proc/%d/comm` 检测调用者的名字是否是 `flag3`，直接使用 `prctl` 给进程设置名字即可：
```c
#include <sys/prctl.h>
#include <unistd.h>

prctl(PR_SET_NAME, "getflag3");
```

编译上传后，成功拿到 flag3。

## 零知识数独
### 数独高手
这道题的数独我是真的不会，直接搜索了数独的解法，找到了 [LeetCode 37.解数独](https://leetcode.cn/problems/sudoku-solver/description/)。

一个个对着把题目的数独填进去，然后直接提交，拿到了 flag1。
![image](https://github.com/user-attachments/assets/7af618d0-bb77-41bb-9e53-fc6d8aee1d50)

## 总结
今年的 Hackergame 很好玩，但是因为高三时间原因，只靠周末时间研究了一小部分题目，希望明年能有更多时间参与 Hackergame！