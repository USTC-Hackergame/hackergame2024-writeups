# PaoluGPT

题目类型：web  
分值：150+200

> 在大语言模型时代，几乎每个人都在和大语言模型聊天。小 Q 也想找一个方便使用的 GPT 服务，所以在熟人推荐下，他注册了某个 GPT 服务，并且付了几块钱。只是出乎小 Q 意料的是，他才用了几天，服务商就跑路了！跑路的同时，服务商还公开了一些用户的聊天记录。小 Q 看着这些聊天记录，突然发现里面好像有 flag……
>
> [题目附件下载](../assets/paolugpt.zip)
>
> **免责声明：本题数据来源自 [COIG-CQIA 数据集](https://modelscope.cn/datasets/m-a-p/COIG-CQIA/)。本题显示的所有该数据集中的数据均不代表 Hackergame 组委会的观点、意见与建议。**

---

~~遇事不决先抓包~~

抓完之后发现，这次一个很鸡贼的地方，就是它不再是服务端返回JSON再渲染前端了，而是直接返回HTML。

反正读HTML获取完所有链接直接一个个扫描呗，简单粗暴（（（

~~Python，启动！~~[示例源代码](../codes/compare_size.py)

运行结果：`找到 flag: flag{zU1_xiA0_de_11m_Pa0lule!!!_1e7e88d683}`

第二个flag咕了，看[官方题解](https://github.com/USTC-Hackergame/hackergame2024-writeups/blob/master/official/PaoluGPT/README.md)吧（其实一开始能看出来这是道SQL注入题，但是不知道为啥我跑的时候session没传进去于是一直403，~~应该是菜爆了~~）
