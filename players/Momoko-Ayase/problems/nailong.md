# 喜欢做签到的 CTFer 你们好呀

题目类型：web  
分值：50+50

>![我要成为签到题高手](../assets/checkin.jpg)  
> 喜欢做签到的 CTFer 你们好呀，我是一道更**典型**的 checkin：有两个 flag 就藏在中国科学技术大学校内 CTF 战队的招新主页里！
---

这是一道web题，所以忽略题干的那张图（

根据提示“中国科学技术大学校内 CTF 战队”，搜索后得知名称为“USTC NEBULA”，进一步搜索后在[CTFtime](https://ctftime.org/team/168863/)可以找到域名为[nebuu.la](https://nebuu.la/)。打开后是一个基于LiveTerm的Web模拟终端。

> 后来的时候也是才发现，比赛的首页下面放着这样一段：
>
>> ## 承办单位
>>
>> - [中国科学技术大学学生 Linux 用户协会（LUG @ USTC）](https://lug.ustc.edu.cn/)
>> - [中国科学技术大学微软学生俱乐部（USTC MSC）](https://lug.ustc.edu.cn/)
>> - [**中国科学技术大学 NEBULA 战队（USTC NEBULA）**](https://www.nebuu.la/)
>> - [中国科学技术大学信息安全俱乐部](https://lug.ustc.edu.cn/)
>
> 点列表中第三个（这里加粗了）也能跳转到主页去。（晕

第一个flag直接在终端输入`env`即可获得：

```bash
ctfer@ustc-nebula:$ ~ env
PWD=/root/Nebula-Homepage
ARCH=loong-arch
NAME=Nebula-Dedicated-High-Performance-Workstation
OS=NixOS❄️
FLAG=flag{actually_theres_another_flag_here_trY_to_f1nD_1t_y0urself___join_us_ustc_nebula}
REQUIREMENTS=1. you must come from USTC; 2. you must be interested in security!
```

这里也提示了有第二个flag的存在 ~~（废话，题目列表里也提示了有两个子题）~~

`ls`一下，能看到：

```bash
ctfer@ustc-nebula:$ ~ ls
Awards
Members
Welcome-to-USTC-Nebula-s-Homepage/
and-We-are-Waiting-for-U/
```

`cd`是不行的，会提示`Permission denied: root needed.`，而如果你去执行`sudo`了... ~~打什么Hackergame，看奶龙去了~~

注意到`Welcome-to-USTC-Nebula-s-Homepage/`和`and-We-are-Waiting-for-U/`了吗，这两行末尾的斜杠提示这是文件夹，因此对这两项执行`ls`：

```bash
ctfer@ustc-nebula:$ ~ ls Welcome-to-USTC-Nebula-s-Homepage/
Awards
Members
Welcome-to-USTC-Nebula-s-Homepage/
and-We-are-Waiting-for-U/

ctfer@ustc-nebula:$ ~ ls and-We-are-Waiting-for-U/
.flag
.oh-you-found-it/
Awards
Members
Welcome-to-USTC-Nebula-s-Homepage/
and-We-are-Waiting-for-U/
```

好，出现隐藏flag了，~~召唤一只猫咪问答高手~~`cat`一下：

```bash
ctfer@ustc-nebula:$ ~ cat .flag
flag{0k_175_a_h1dd3n_s3c3rt_f14g___please_join_us_ustc_nebula_anD_two_maJor_requirements_aRe_shown_somewhere_else}
```
