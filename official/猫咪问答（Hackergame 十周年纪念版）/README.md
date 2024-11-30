# 猫咪问答（Hackergame 十周年纪念版）

题解作者：emc2314

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：general

- 题目分值：喵？（100）+ 喵！（150）

多年回答猫咪问答的猫咪大多目光锐利，极度自信，且智力逐年增加，最后完全变成猫咪问答高手。回答猫咪问答会优化身体结构，突破各种猫咪极限。猫咪一旦开始回答猫咪问答，就说明这只猫咪的智慧品行样貌通通都是上等，这辈子注定在猫咪界大有作为。

提示：**解出谜题不需要是科大在校猫咪**。解题遇到困难？你可以参考以下题解：

- [2018 年猫咪问答题解](https://github.com/ustclug/hackergame2018-writeups/blob/master/official/ustcquiz/README.md)
- [2020 年猫咪问答++ 题解](https://github.com/USTC-Hackergame/hackergame2020-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E9%97%AE%E7%AD%94++/README.md)
- [2021 年猫咪问答 Pro Max 题解](https://github.com/USTC-Hackergame/hackergame2021-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E9%97%AE%E7%AD%94%20Pro%20Max/README.md)
- [2022 年猫咪问答喵题解](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E9%97%AE%E7%AD%94%E5%96%B5/README.md)
- [2023 年猫咪小测题解](https://github.com/USTC-Hackergame/hackergame2023-writeups/blob/master/official/%E7%8C%AB%E5%92%AA%E5%B0%8F%E6%B5%8B/README.md)

[打开/下载题目](http://202.38.93.141:13030/?token={token})

## 题解

1. 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？https://lug.ustc.edu.cn/wiki/sec/contest.html
2. 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？https://lug.ustc.edu.cn/news/2019/12/hackergame-2019/
3. Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？https://github.com/ustclug/hackergame2018-writeups/blob/master/misc/others.md
4. 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？https://www.usenix.org/system/files/usenixsecurity24-ma-jinrui.pdf
   > Consequently, we propose six types of email spoofing attacks and measure their impact across 16 email services and 20 clients. All 20 clients are configured as MUAs for all 16 providers via IMAP, resulting in 336 combinations (including 16 web interfaces of target providers).
5. 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=6e90b675cf942e50c70e8394dfb5862975c3b3b2
6. 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？

   ```python
   import transformers
   import requests
   tk=transformers.AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-70B")
   s=requests.session()
   t=s.get("http://202.38.93.141:13030/", cookies={"session":"REDACTED"}).text
   print(len(tk.encode(t)))
   ```

   注意到 tokenizer.encode 会自带一个 BOS token，这个 token 严格来说并不算文章内容的一部分，所以答案需要减一，是 1833。
