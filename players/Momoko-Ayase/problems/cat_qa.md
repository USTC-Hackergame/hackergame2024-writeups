# 猫咪问答（十周年纪念版）

题目类型：general  
分值：100+150

> 多年回答猫咪问答的猫咪大多目光锐利，极度自信，且智力逐年增加，最后完全变成猫咪问答高手。回答猫咪问答会优化身体结构，突破各种猫咪极限。猫咪一旦开始回答猫咪问答，就说明这只猫咪的智慧品行样貌通通都是上等，这辈子注定在猫咪界大有作为。  
> 提示：**解出谜题不需要是科大在校猫咪**。解题遇到困难？你可以参考以下题解：
>
> - [2018 年猫咪问答题解](https://github.com/ustclug/hackergame2018-writeups/blob/master/official/ustcquiz/README.md)
> - [2020 年猫咪问答++ 题解](https://github.com/USTC-Hackergame/hackergame2020-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E9%97%AE%E7%AD%94++/README.md)
> - [2021 年猫咪问答 Pro Max 题解](https://github.com/USTC-Hackergame/hackergame2021-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E9%97%AE%E7%AD%94%20Pro%20Max/README.md)
> - [2022 年猫咪问答喵题解](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E9%97%AE%E7%AD%94%E5%96%B5/README.md)
> - [2023 年猫咪小测题解](https://github.com/USTC-Hackergame/hackergame2023-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E5%B0%8F%E6%B5%8B/README.md)

---

### 1. 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？

打开[中国科学技术大学 Linux 用户协会网站](https://lug.ustc.edu.cn/)，点开Wiki - 侧边栏活动 - 信息安全大赛，根据时间推断Hackergame 2015为第二届，点击活动记录 - [第二届安全竞赛（存档）](https://lug.ustc.edu.cn/wiki/sec/contest.html)，即可看到答案为`3A204`。

### 2. 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？

近五年即2019\~2023年，根据每年Writeups中显示的具体题目数：

| 年份 | 题目数 |
|------|-------|
| 2023 |  29   |
| 2022 |  33   |
| 2021 |  31   |
| 2020 |  31   |
| 2019 |  28   |

[经查](https://lug.ustc.edu.cn/news/2019/12/hackergame-2019/)，可知2019年共有2682人注册。

### 3. Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？

别去lib.ustc.edu.cn找，找不到的（

Hackergame 2018的猫咪问答里中有如下题目：

```plain
4. 在中国科大图书馆中，有一本书叫做《程序员的自我修养:链接、装载与库》，请问它的索书号是？
打开中国科大图书馆主页，直接搜索“程序员的自我修养”即可。
```

答案由此可知。

<!--
### 4. 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？

Google搜索**USENIX Security**并打开[USENIX Security '24](https://www.usenix.org/conference/usenixsecurity24)，点击框框中的[technical sessions](https://www.usenix.org/conference/usenixsecurity24/technical-sessions)按钮。因为其与电子邮件有关，因此全文搜索`Email`，可找到一篇名为《FakeBehalf: Imperceptible Email Spoofing Attacks against the Delegation Mechanism in Email Systems》的论文。点击后在Abstract部分可找到以下内容：

> ...We assess their impact across 16 service providers and 20 clients...

### 5. 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？

进行搜索后可以找到patch提交记录位于[[PATCH] MAINTAINERS: Remove some entries due to various compliance requirements. - Greg Kroah-Hartman](https://lore.kernel.org/all/2024101835-tiptop-blip-09ed@gregkh/)。查找`diff`语句的下一行，即`index 9d20ace6fa40..21b31c6d20d0 100644`

### 6. 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？
-->