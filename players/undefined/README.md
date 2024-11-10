# hackergame2024-writeup

by [@undefined-moe](https://github.com/undefined-moe)

## 签到

~~是的我没注意到直接有变量可以用~~

```js
document.querySelectorAll('input').forEach((i) => {
    i.value = i.placeholder.replace('：', ':').split(':')[1].trim()
})
```

得 `flag{W3!COmE-70-H4cKeRGAm3-And-eNJoy-H4CK!NG-2o24}`

## 喜欢做签到的 CTFer 你们好呀

搜索 `中国科学技术大学校内 CTF "战队"` ，可得 `网络空间安全学院李卫海副书记、USTC-NEBULA 战队指导老师吴文涛老师、本届比赛负责人、USTC-NEBULA 战队成员、本届比赛参赛选手出席了本次颁奖典礼。...`

再次搜索 `USTC-NEBULA`, 发现 `USTC NEBULA 2024 招新安排`，进入对应 Github Org 主页，找到官网 `https://www.nebuu.la/`，

使用 `env` 得到 flag1；  
使用 `ls -a` 看到 `.flag`，使用 `cat .flag` 得到 flag2。

p.s. 这个终端不支持复制，差评。需要审查元素从调试窗口复制。

## 猫咪问答

1. 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？（30 分）

在 Hackergame 官网 https://lug.ustc.edu.cn/wiki/lug/events/hackergame/ 找到 [第二届安全竞赛（存档）](https://lug.ustc.edu.cn/wiki/sec/contest.html) 内写 3A204。

3. Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？（20 分）

[Hackergame 2018 writeups 花絮部分](https://github.com/ustclug/hackergame2018-writeups/blob/master/misc/others.md) 内提到了 "程序员的自我修养"。

5. 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？（5 分）

从浏览器翻出历史记录 [https://lore.kernel.org/linux-patches/2024101835-tiptop-blip-09ed@gregkh/T/](https://lore.kernel.org/linux-patches/2024101835-tiptop-blip-09ed@gregkh/T/) 即得到 `6e90b6`。

其他三问均为正整数答案，可直接使用[脚本](./qa.ts)爆破。

## 打不开的盒

搜索 stl viewer online, 进入 [https://www.viewstl.com/](https://www.viewstl.com/) 上传 `flagbox.stl`，切换视角后使用瞪眼法可得 `flag{Dr4W_Us!nG_fR3E_C4D!!w0W}`。

## 每日论文太多了！

打开 pdf，搜索 flag 发现有一处匹配。  
~~使用 pdf dump 出所有文字，发现找不到 flag，卡了很久很久~~

直到把 pdf 拖进了 acrobat ，发现 flag 以图片的形式藏在了一个白色的遮罩层后面，草。
得 `flag{h4PpY_hAck1ng_3veRyd4y}` （好糊）。

## 比大小王

写了一个脚本 [number.ts](./number.ts) 自动提交但是一直说非法请求。
最后在浏览器里跑了一个看准时期粘贴得到 flag。

```js
const r=[];
for (const t of state.values) {
    if (t[0] > t[1]) r.push('>')
    else if (t[0] < t[1]) r.push('<')
    else r.push('=')
}
submit(r);
```

## 旅行照片

题 1：枚举两个东南西北。
题 2：在 https://space.bilibili.com/7021308/dynamic 翻找可得日期。

后面两问没做出来，合理怀疑主办方收了百度和小红薯的广告费，记得给参赛选手分钱。

## Node.js is Web Scale

下载源代码发现非常明显的 prototype pollution。
（如果没有一眼发现的话思考一下为什么 kv store 要做 jsonpath 展开也很容易得到）

提交 `__proto__.t = cat /flag` 后访问 `/execute?cmd=t` 即可。

## 跑路 GPT

第一小问非常简单。直接 `wget --mirror` 把网页全部下载下来然后搜索 flag 即可。
第二小问是普通的 SQL 注入，访问 `/view?conversation_id=‘ or shown=false or id='` 可得 flag。


## Docker For Everyone Plus

个人认为这道题的难点在于上传一个能用的容器镜像。  
听信出题人去研究 rz 是最大的失误。浪费了我超过三个小时。  
最终还是最朴素的 [echo+base64 大法](./docker.py) 最好用。

## 看不见的彼方：交换空间

可以通过 HTTP Server 进行数据交换。  
~~因为题目的 10MiB 限制，没法写js或者py了并发现自己完全不会写 Golang。~~  
于是使用 Copylot 写了一个 HTTP Server [alice.go](./alice.go) 和一个 HTTP Client [bob.go](./bob.go) ，本地能跑但是好像传上去爆了，故开摆。

## 禁止内卷

题目内提到启用了 reload 功能，暗示需要修改文件。  
后端使用 `filepath = os.path.join(UPLOAD_DIR, filename)` 拼接路径，即只需要传递一个绝对路径即可任意修改。  

花絮：Node 端使用的 form-data 库会在本地将路径提取 basename 导致失效，需要将 `node_modules/form-data/lib/form_data.js` 手动 patch 掉：

```diff
  FormData.prototype._getContentDisposition = function(value, options) {
  var filename, contentDisposition;
- if (typeof options.filepath === 'string') {
-   // custom filepath for relative paths
-   filename = path.normalize(options.filepath).replace(/\\/g, '/');
- } else if (options.filename || value.name || value.path) {
-   // custom filename take precedence
-   // formidable and the browser add a name property
-   // fs- and request- streams have path property
-   filename = path.basename(options.filename || value.name || value.path);
- } else if (value.readable && value.hasOwnProperty('httpVersion')) {
-  // or try http response
-   filename = path.basename(value.client._httpMessage.path || '');
- }
+ filename=options.filename;
  if (filename) contentDisposition = 'filename="' + filename + '"';
  return contentDisposition;
};
```

能够修改服务端代码后就无敌了。
