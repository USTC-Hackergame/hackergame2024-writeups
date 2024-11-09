# Himalalps writeup

## 签到

打开页面后点击 "等不及了，马上启动！" 按钮，发现浏览器的地址栏变为 [http://202.38.93.141:12024/?pass=false](http://202.38.93.141:12024/?pass=false) ，此时修改为 [http://202.38.93.141:12024/?pass=true](http://202.38.93.141:12024/?pass=true) 即可得到 flag.

---

## 喜欢做签到的 CTFer 你们好呀

搜索 "中国科学技术大学校内 CTF 战队的招新主页" 发现 [USTC NEBULA 2024 招新安排](https://github.com/Nebula-CTFTeam/Recruitment-2024)，打开 这个[GitHub organization 账号](https://github.com/Nebula-CTFTeam)，看到 README 里有链接指向 [招新主页](https://nebuu.la/).

输入 help 后依次尝试可行的 command.

1. `env` 命令得到第一个 flag.

2. `cat` 命令得到提示 `file not found, maybe you can consider about Members / Awards / hidden files`

3. `ls -la` 查看隐藏文件，发现 `.flag` 文件，`cat .flag` 得到第二个 flag.

~~4. `sudo` 命令打开 [奶龙](https://www.bilibili.com/bangumi/play/ss40551) 链接。~~

---

## 猫咪问答 (Hackergame 十周年纪念版)

1. 搜索 "Hackergame 2015"，找到 [LUG 主页上信息安全大赛 Hackergame 的介绍](https://lug.ustc.edu.cn/wiki/lug/events/hackergame/)，其中有 [第二届安全竞赛（存档）](https://lug.ustc.edu.cn/wiki/sec/contest.html) 的链接，打开发现网络攻防技巧讲座在 3A204 举办。

2. 同样在上方 [介绍](https://lug.ustc.edu.cn/wiki/lug/events/hackergame/) 页面中打开近五届的新闻稿，发现 2019、2020、2021 三年都有准确注册人数，再打开该年题解数数，发现是 2019 年，即 2682 人。

3. 打开 [Hackergame 2018 题解](https://github.com/ustclug/hackergame2018-writeups)，点击 [猫咪问答](https://github.com/ustclug/hackergame2018-writeups/blob/master/official/ustcquiz/README.md)，发现当年的第 4 题要搜索 “程序员的自我修养”。

4. 搜索 "USENIX Security USTC"，看到 [黄轩博同学赴美参与2024年USENIX Security学术会议](https://if.ustc.edu.cn/news/2024_08_20.php)，其中关于电子邮件的论文显然是 *FakeBehalf: Imperceptible Email Spoofing Attacks against the Delegation Mechansim in Email Systems*，搜索打开论文后，在 Section 6 Imperceptible Email Spoofing Attack 部分看到 "resulting in 336 combinations"，即 336 种组合。

5. 搜索 "Greg Kroah-Hartman remove maintainer patch"，找到 [[PATCH] MAINTAINERS: Remove some entries due to various compliance requirements](https://lore.kernel.org/all/2024101835-tiptop-blip-09ed@gregkh/) 在下方 Thread overview 中点击 [this message] 下方一条 [[PATCH] MAINTAINERS: Remove some entries due to various compliance requirements Geert Uytterhoeven](https://lore.kernel.org/all/a520d1f5-8273-d67e-97fe-67f73edce9f1@linux-m68k.org/) 看到其中提到 "which is now commit 6e90b675cf942e50"，因此结果为 6e90b6.

6. 搜索 "Llama 3 tokenizer online"，找到 [Llama3-tokenizer playground](https://belladoreai.github.io/llama3-tokenizer-js/example-demo/build/)，将网页源代码粘贴进去，即可得到解答，注意去除额外的空行，1833 个 token.

---

## 打不开的盒

下载文件后发现是 STL 文件，搜索在线查看器，上传后挪动视角即发现 flag.

---

## 每日论文太多了！

点开论文页面，下载 PDF 文件，全文搜索 flag，发现在某张图片里有文本 flag here，但被形状遮挡，下载后挪动上方白色矩形即可看到 flag.

~~真会玩，竟然在 camera ready 版本论文里放 flag~~

---

## 比大小王

查看网页源码，发现其中所有的值都存在 `state` 里，包括输入 `state.inputs` 和需要比较的值 `state.values`，最后提交通过 `submit(state.inputs)`，若服务器端检查结果正确则返回 flag.

因此只需本地检查 `values` 将正确结果存入 `state.inputs` 即可。

```javascript
function play() {
    for (let i = 0; i < 100; i++) {
        value1 = state.values[i][0];
        value2 = state.values[i][1];
        state.inputs.push(value1 > value2 ? '>' : '<');
    }
    submit(state.inputs);
}
```

---

## 旅行照片 4.0

1. 地图搜索科里科气科创驿站，发现位于中科大中区东边，坐西朝东，显然需要在东区西门附近才能拍到。~~科大学生应该不需要搜索也能知道在哪吧，不要说你没有晚上去跑过步~~

2. 搜索 USTC ACG 2024，在 B站上找到一些单品视频，~~这时候就可以暴力往前试日期了~~但发现没有在当天发的。在LEO动漫协会的B站动态制定看到 QQ，翻空间看到 5 月 19 日发的当晚 ACG 音乐会节目单。

3. 看到右侧垃圾桶上有“六安园林”字样，搜索 “六安 彩虹步道”，发现是六安中央公园。

4. 将图片下载，尝试各个搜索引擎搜图，发现~~竟然还是~~百度能搜到结果，在三峡，但不是三个字的，再次搜索 “三峡 喷泉”，发现分几大园区，其中 “坛子岭” 为三个字的，尝试发现正确。

5. 依然搜图，发现是北京北动车所，地图查看发现最近的是北京积水潭医院。

6. 搜索 “京张高铁北京北动车所” 看到专栏 [体验乘坐+蹲点等拍京郊网红粉萌“小火车”CRH6F-A型——怀密号！](https://zhuanlan.zhihu.com/p/346241499)，结果为 CRH6F-A.

注：其实最后一题卡了很久，把复兴号常规型号都试了一遍。

---

## PaoluGPT

### 千里挑一

读取所有页面，然后搜索 "flag" 即可。

```python
import bs4
import requests


session = requests.Session()

url = "https://chal01-bt5v8qga.hack-challenge.lug.ustc.edu.cn:8443/"

res = session.get(
    url,
    params={
        "token": "629:MEYCIQC8vdaJoUpOUNI+WGaLF2Yq5p12/Scc13ItWbF7KPl0uQIhAP4Sz1g6iy1v+QGCtaqoszgIqyqlUhOr3pwOO93oFN2e",
    },
)

res = session.get(
    url + "list",
)


soup = bs4.BeautifulSoup(res.text, "html.parser")

for a in soup.find_all("a"):
    if "conversation_id" in a["href"]:
        conversation_id = a["href"].split("=")[1]
        res = session.get(
            url + "view",
            params={"conversation_id": conversation_id},
        )
        new_soup = bs4.BeautifulSoup(res.text, "html.parser")

        if "flag" in new_soup.text:
            print(conversation_id)
```

---

## 强大的正则表达式

### Easy

需要用正则表达式处理 16 的倍数，特征为后四位为 16 的倍数。发现长度限制很大，所以可以直接将 10000 以下所有 16 的倍数列出来，然后匹配前面的所有数字即可。~~不知道为什么如果正则表达式长度到 4000 左右时会报错~~但其实以下这个正则表达式没法匹配小于10000的数，但因为随机出来的结果都很大，所以不影响结果。

```python
string = ""
for i in range(9999, -1, -1):
    if i % 16 == 0:
        string += f"{i:04d}|"
print("((1|2|3|4|5|6|7|8|9)((0|1|2|3|4|5|6|7|8|9)*)(" + string[:-1] + "))")
```

### Medium

需要用正则表达式处理二进制下 13 的倍数。使用自动机的思想，先用如下代码得到每个状态要到达其他状态需要的字符。状态为 0-12，即模 13 的余数，字符为 0 或 1.

```python
regex_list = {}
to_list = {i:set() for i in range(13)}
for i in range(13):
    regex_list[i] = {}
    regex_list[i][(i * 2) % 13] = "0"
    to_list[(i * 2) % 13].add(i)
    regex_list[i][(i * 2 + 1) % 13] = "1"
    to_list[(i * 2 + 1) % 13].add(i)
```

然后再用如下代码去除 `index` 对应的状态。

```python
target_list = regex_list[index]
regex_list.pop(index)
if index in target_list:
    target_list[index] = f"({target_list[index]})*"
    for i in target_list:
        if i != index:
            target_list[i] = target_list[index] + target_list[i]
    target_list.pop(index)
for s, l in regex_list.items():
    if index in l:
        p = l[index]
        l.pop(index)
        for t, v in target_list.items():
            if t in l:
                l[t] = f"({l[t]}|{p}{v})"
            else:
                l[t] = f"{p}{v}"
```

注意因为某些状态可达状态较多，需要考虑去除的顺序使得最终结果较短。

使用顺序 12, 11, 10, 9, 8, 7, 1, 2, 4, 3, 5, 6，最终 `regex_list[0][0]` 即为从 0 出发回到 0 的正则表达式，但还要最终加上一个 `*` 使得可以匹配任意长度。

---

## 惜字如金 3.0

### 题目 A

不断按照规则复原，提交后处理出错的行即可。

---

## 优雅的不等式

### Easy

发现题目给出了一个 1 级的正解 `4*((1-x**2)**(1/2)-(1-x))`，只需调整一下即可通过 2 级的检查 `4*((1-x**2)**(1/2)-(1-x**2))`.

## 关灯

### Hard

搜索“关灯游戏”，发现二维版本的一般通过线性代数方法解决。在 GitHub 上找到 [一个 Python 版的解法](https://github.com/Abtinz/Lights-Out-Solver/tree/main)，修改为三维版本，可以处理到 Hard 难度。

```python
import math
import numpy as np


def show_result(solver_matrix, dimension):
    solved = True
    for row_index in range(0, solver_matrix.shape[0]):
        if (
            np.sum(solver_matrix[row_index, 0 : solver_matrix.shape[1] - 2]) == 0
            and solver_matrix[row_index, solver_matrix.shape[1] - 1] == 1
        ):
            print("This solution cannot be resolved ")
            solved = False
            break

    if solved:
        solved_map = solver_matrix[:, solver_matrix.shape[1] - 1].reshape(
            dimension, dimension, dimension
        )
        # print("Solved Map:\n1 --> press for solving\n", solved_map)
        print("".join(map(str, solved_map.flatten().tolist())))


def swap_zero_piviot(solver_matrix, index):
    if index < solver_matrix.shape[0]:
        if solver_matrix[index, index] != 1:
            for current_row_index in range(index + 1, solver_matrix.shape[0]):
                if solver_matrix[current_row_index, index]:
                    temp = np.matrix(solver_matrix[index])
                    solver_matrix[index] = solver_matrix[current_row_index]
                    solver_matrix[current_row_index] = np.array(temp)
                    break

    return solver_matrix


def xor_matrix_func(solver_matrix, second_row_index, row_index):
    for col_index in range(0, solver_matrix.shape[1]):
        if solver_matrix[row_index, col_index]:
            if solver_matrix[second_row_index, col_index] == 0:
                solver_matrix[second_row_index, col_index] = 1
            else:
                solver_matrix[second_row_index, col_index] = 0
    return solver_matrix[second_row_index, :]


def reduced_echlon(solver_matrix, dimension):
    for row_index in range(solver_matrix.shape[0] - 1, -1, -1):

        for second_row_index in range(row_index - 1, -1, -1):
            if solver_matrix[second_row_index, row_index] == 1:
                solver_matrix[second_row_index, :] = xor_matrix_func(
                    solver_matrix, second_row_index, row_index
                )
    # print("Reduced Echlon:\n", solver_matrix)
    show_result(solver_matrix, dimension)


def echlon_matrix(solver_matrix, dimension):
    for row_index in range(0, solver_matrix.shape[0]):
        solver_matrix = swap_zero_piviot(solver_matrix, row_index)
        for second_row_index in range(row_index + 1, solver_matrix.shape[0]):
            if solver_matrix[second_row_index, row_index] == 1:
                solver_matrix[second_row_index, :] = xor_matrix_func(
                    solver_matrix, second_row_index, row_index
                )
    # print("Echlon Matrix:\n", solver_matrix)
    reduced_echlon(solver_matrix, dimension)


def distance(i, j, k, m, n, l):
    return (i - m) ** 2 + (j - n) ** 2 + (k - l) ** 2


def make_matrix_for_solver(game_matrix, dim):
    dim_square = int(math.pow(dim, 3))
    solver_matrix = (
        np.arange(0, dim_square * (dim_square + 1)).reshape(dim_square, dim_square + 1)
        * 0
    )
    solver_matrix[:, dim_square] = game_matrix.ravel().tolist()

    for i, j, k in np.ndindex(dim, dim, dim):
        for m, n, l in np.ndindex(dim, dim, dim):
            if distance(i, j, k, m, n, l) <= 1:
                solver_matrix[
                    i * dim * dim + j * dim + k, m * dim * dim + n * dim + l
                ] = 1

    # print("\nAgmented Matrix:\n", solver_matrix)
    echlon_matrix(solver_matrix, dim)


dimension = int(input("Enter the dimension of the matrix: "))
array = input("Enter the matrix: ")
matrix = np.array(list(map(int, array))).reshape(dimension, dimension, dimension)

print(make_matrix_for_solver(matrix, dimension))
```

---

## 零知识数独

### 数独高手

找一个在线数独求解器，将四个难度的题目输入，得到结果后提交得到 flag.

---

## 先不说关于我从零开始独自在异世界转生成某大厂家的 LLM 龙猫女仆这件事可不可能这么离谱，发现 Hackergame 内容审查委员会忘记审查题目标题了ごめんね，以及「这么长都快赶上轻小说了真的不会影响用户体验吗🤣」

### 「行吧就算标题可以很长但是 flag 一定要短点」

用相同的输入，不同的 seed 生成不同的文本，然后使用相同的规则替换，尝试补全原文，得到结果。

```
In the grand hall of Hackergame 2024, where the walls are lined with screens showing the latest exploits from the cyber world, contestants gathered in a frenzy, their eyes glued to the virtual exploits. The atmosphere was electric, with the smell of freshly brewed coffee mingling with the scent of burnt Ethernet cables. As the first challenge was announced, a team of hackers, dressed in lab coats and carrying laptops, sprinted to the nearest server room, their faces a mix of excitement and determination. The game was on, and the stakes were high, with the ultimate prize being a golden trophy and the bragging rights to say they were the best at cracking codes and hacking systems in the land of the rising sun.
```