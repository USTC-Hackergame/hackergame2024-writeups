# 凌六的 hackergame2024 题解

本篇题解涵盖签到到旅行照片 4.0 的七个题目，以及PaoluGPT-千里挑一，惜字如金 3.0-题目 A 和无法获得的秘密这几个题目。

~~感觉自己好菜XD~~

### 签到

直接发 get 请求，不用管前端。

### 喜欢做签到的 CTFer 你们好呀

搜半天，终于找到了 https://ftp.lug.ustc.edu.cn/%E6%B4%BB%E5%8A%A8/2023.10.27_Hackergame%E5%8A%A8%E5%91%98%E4%BC%9A/ ，PPT 看到 github 链接，点进去找到主页，主页进去 env 拿到第一个 flag，然后分析 js 拿到第二个 flag（cat .flag）也行。

### 猫咪问答（Hackergame 十周年纪念版）

1. 在 Hackergame 2015 比赛开始前一天晚上开展的赛前讲座是在哪个教室举行的？
	- https://lug.ustc.edu.cn/wiki/lug/events/hackergame/
	- [第二届安全竞赛（存档）](https://lug.ustc.edu.cn/wiki/sec/contest.html)
	- 3A204
2. 众所周知，Hackergame 共约 25 道题目。近五年（不含今年）举办的 Hackergame 中，题目数量最接近这个数字的那一届比赛里有多少人注册参加？
	- [2020 猫咪问答题解](https://github.com/USTC-Hackergame/hackergame2020-writeups/tree/master/official/%E7%8C%AB%E5%92%AA%E9%97%AE%E7%AD%94%2B%2B)
	- [里面能找到个公众号](https://mp.weixin.qq.com/s/b7VGQ17aWOFOgC8dTynMkw)
	- 2682
3. Hackergame 2018 让哪个热门检索词成为了科大图书馆当月热搜第一？
	- 程序员的自我修养
4. 在今年的 USENIX Security 学术会议上中国科学技术大学发表了一篇关于电子邮件伪造攻击的论文，在论文中作者提出了 6 种攻击方法，并在多少个电子邮件服务提供商及客户端的组合上进行了实验？
	- ![](attachments/Pasted%20image%2020241102132317.png)
	- ![](attachments/Pasted%20image%2020241102132832.png)
5. 10 月 18 日 Greg Kroah-Hartman 向 Linux 邮件列表提交的一个 patch 把大量开发者从 MAINTAINERS 文件中移除。这个 patch 被合并进 Linux mainline 的 commit id 是多少？
	- https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/log/
	- ![](attachments/Pasted%20image%2020241102133702.png)
	- 6e90b6
6. 大语言模型会把输入分解为一个一个的 token 后继续计算，请问这个网页的 HTML 源代码会被 Meta 的 Llama 3 70B 模型的 tokenizer 分解为多少个 token？
	- 搜索关键词：Llama3 tokenizer playground
	- https://belladoreai.github.io/llama3-tokenizer-js/example-demo/build/
	- 1833

### 打不开的盒

https://www.viewstl.com/

![](attachments/Pasted%20image%2020241102134602.png)
![](attachments/Pasted%20image%2020241102134605.png)

flag{Dr4W_Us!nG_fR3E_C4D!!w0W}

### 每日论文太多了！

下载论文 pdf 文件，搜索 flag 可以看到在一个图例中有隐藏的“flag here”字样，使用 pdf 图片提取脚本可以提取出 flag 图片。

![](attachments/Pasted%20image%2020241102135824.png)

### 比大小王

反复拷打 Copilot，最终得到在浏览器控制台内执行如下代码

```js
(function autoPlayGame() {
  function simulateKeyPress(key) {
    document.dispatchEvent(new KeyboardEvent('keydown', { key }));
  }

  function chooseAnswer() {
    if (!state.allowInput) {
      return;
    }
    const [value1, value2] = [state.value1, state.value2];
    const choice = value1 < value2 ? '<' : '>';
    simulateKeyPress(choice === '<' ? 'ArrowLeft' : 'ArrowRight');
  }

  function startAutoPlay() {
    const intervalId = setInterval(() => {
      if (state.stopUpdate || state.score1 === 100) {
        clearInterval(intervalId);
        return;
      }
      chooseAnswer();
    }, 1); // Adjust the interval if needed
  }

  document.addEventListener('load', loadGame());
  // Start the auto play after a slight delay to ensure the game is fully loaded
  setTimeout(startAutoPlay, 1000);
})();
```

### 旅行照片 4.0

#### 题目 1-2

![](attachments/Pasted%20image%2020241102150420.png)

https://www.thepaper.cn/newsDetail_forward_22122807 -> 与科大仅一路之隔的“科大硅谷”蜀山园科创驿站科大站

![](attachments/Pasted%20image%2020241102150525.png)

[开个acg音乐会的实时交流贴](https://tieba.baidu.com/p/9022584688)得知是 20240519。

#### 题目 3-4

搜索关键词1：彩色道路标线 公园 六安市 -> [中央公园](https://www.sohu.com/a/498872898_100023473)

第二个直接百度搜图。

![](attachments/Pasted%20image%2020241102153506.png)

![](attachments/Pasted%20image%2020241102153523.png)

#### 题目 5-6

![](attachments/Pasted%20image%2020241102163141.png)

在 b 站搜索四编组动车，在 BV1db421t7DW 下看到这么一条评论。

![](attachments/Pasted%20image%2020241102163113.png)

![](attachments/Pasted%20image%2020241102163123.png)

得到关键信息：怀柔号。
![](attachments/Pasted%20image%2020241102163218.png)

百度地图先搜索北京，再搜“动车运用所”得到答案：

![](attachments/Pasted%20image%2020241102163312.png)

### PaoluGPT

#### 千里挑一

使用如下脚本爬取所有内容拼接在一起作为一个 html 文件，然后打开全文搜索拿到 flag。

```python
import requests
from bs4 import BeautifulSoup

login = 'https://chal01-oaxdssuz.hack-challenge.lug.ustc.edu.cn:8443/list?token=' # 改成你的登录网址
url = 'https://chal01-oaxdssuz.hack-challenge.lug.ustc.edu.cn:8443'

session = requests.Session()
session.get(login)

response = session.get(url+'/list')
soup = BeautifulSoup(response.content, 'html.parser')

links = soup.select('html > body > div.container.px-3.pt-3 > div.container.pt-3 > ul > li > a')
urls = [link.get('href') for link in links]


f = open('output\\output.html', 'a', encoding='utf-8')
len = len(urls)
j = 0
for i in urls:
    response = session.get(url+i)
    f.write(response.text)
    j+=1
    print(f'{j}/{len}')
f.close()
```

### 惜字如金 3.0

题目 A：直接补全出错的代码即可。

### 无法获得的秘密

只能通过 VNC 使用键鼠输入，看视频输出。考虑使用 python 读取 secret，并以某种方式存储在 BMP 位图（因为好像 BMP 位图的数据结构是最简单的）中，之后读图获取。存在色差，因此决定将多种颜色映射到相同字节。

#### 设计字节转图片

使用 RGB 分别存储数据，RGB 每种的取值为 0~255，因此 8 取 1 映射至 32 种颜色。8 位 32 进制颜色索引能转化成 5 位 256 进制数。要使读图时不读填充的空数据，可在开始时设置“像素头”，在最开始的 4 个字节中存储之后要读取的字节数，python 脚本实现如下。

文件转图片：

```python
import struct
from pathlib import Path

# 定义：0-31 种颜色叫 32 进制颜色索引
# 颜色索引对应的 0-255 颜色值叫做 256 进制等效颜色
# 8 位 32 进制颜色索引转换为 5 字节。

def colorIndex_to_color(colorIndex:int)-> int:
    '''将 32 进制颜色索引转换为 256 进制等效颜色\n
    例：颜色值为 4 12 之类的中间量\n
    单数字对一个中心颜色的映射'''
    return colorIndex*8+4

def base256_to_base32(intList:list)-> list:
    '''将 5 位 256 进制数列表转换为 8 位 32 进制数列表'''
    number = intList[0]*256**4 + intList[1]*256**3 + intList[2]*256**2 + intList[3]*256 + intList[4]
    return [number//32**7, number//32**6%32, number//32**5%32, number//32**4%32, number//32**3%32, number//32**2%32, number//32%32, number%32]

def byte5_to_color8(byte:bytes)-> bytes:
    '''将 5 个字节转换为 8 个 256 进制等效颜色'''
    colorBytes = [color for color in byte]     # bytes -> list
    colorBytes = base256_to_base32(colorBytes) # 转成 32 进制颜色索引
    colorBytes = [colorIndex_to_color(color) for color in colorBytes] # 转成 256 进制等效颜色
    return bytes(colorBytes) # List -> bytes

def bytes_to_colors(bytes:bytearray)-> bytearray:
    '''将字节流转换为等效颜色字节流，统一使用 bytearray\n
    源 bytes 不是 5 的倍数时，末尾补 0\n
    只有最后一组不足 5 位时才会补 0 ，其他组没有补 0'''
    if len(bytes)%5 != 0:
        bytes += b'\x00'*(5-len(bytes)%5)
    colorarary = bytearray()
    for i in range(0, len(bytes), 5):
        colorarary += byte5_to_color8(bytes[i:i+5])
    return colorarary
    
def colors_to_bmp_data(colors:bytearray, width:int)-> tuple[bytearray, int]:
    '''将等效颜色字节流转换为由 bmp 实际数据和 bmp 高度的列表'''
    data = bytearray()
    # bmp 在色深为 24 时一行为 3*width 字节，不足 4 的倍数时补 0
    line_data_bytes = 3*width
    line_addition = (4 - line_data_bytes % 4) % 4
    line_bytes = line_data_bytes + line_addition
    for i in range(0, len(colors), line_data_bytes):
        data += colors[i:i+line_data_bytes]
        data += b'\x00'*(line_addition)
    # 最后一行像素数不足时补 0
    data += b'\x00'*((line_bytes - len(data)%line_bytes) % line_bytes)
    height = len(data)//line_bytes
    return (data, height)

def file_to_bmp_bytes(file:str, width:int)-> bytearray:
    '''将文件转换为 bmp 数据'''
    with open(file, 'rb') as f:
        file_bytes = bytearray(f.read())
    pix_header = bytearray(struct.pack('<i', len(file_bytes)))
    # 用最开始存储数据的 4 个字节存后续要读多少字节
    file_bytes = pix_header + file_bytes
    colors = bytes_to_colors(file_bytes)
    bmp_data, height = colors_to_bmp_data(colors, width)
    bmp_data_len = len(bmp_data)
    bmp_file_len = 54 + bmp_data_len
    bmp_file_header = bytearray(b'\x42\x4D'+struct.pack('<i', bmp_file_len)+b'\x00\x00\x00\x00'+b'\x36\x00\x00\x00'+b'\x28\x00\x00\x00'+struct.pack('<i', width)+struct.pack('<i', height)+b'\x01\x00'+b'\x18\x00'+b'\x00\x00\x00\x00'+struct.pack('<i', bmp_data_len)+b'\x25\x16\x00\x00'+b'\x25\x16\x00\x00'+b'\x00\x00\x00\x00'+b'\x00\x00\x00\x00')
    bmp_file = bmp_file_header + bmp_data
    print(f"转换的文件宽度为 {width} 像素，高度为 {height} 像素")

    return bmp_file

root = Path('/home/user')
a = root/input('input: ').strip()
b = root/input('output: ').strip()
bmp_bytes = file_to_bmp_bytes(a, 512)
with open(b, 'wb') as f:
    f.write(bmp_bytes)
```

图片转文件：

```python
import struct
from PIL import Image
from pathlib import Path

def color_to_colorIndex(color:int)-> int:
    '''将 256 进制等效颜色转换为 32 进制颜色索引\n
    多颜色对单数字的映射'''
    return color//8

def base32_to_base256(intList:list)-> list:
    '''将 8 位 32 进制数转换为 5 位 256 进制数'''
    number = intList[0]*32**7 + intList[1]*32**6 + intList[2]*32**5 + intList[3]*32**4 + intList[4]*32**3 + intList[5]*32**2 + intList[6]*32 + intList[7]
    return [number//256**4, (number//256**3)%256, (number//256**2)%256, (number//256)%256, number%256]

def color8_to_byte5(colorBytes:bytes)-> bytes:
    '''将 8 个等效颜色字节转换为 5 字节'''
    colorBytes = [color_to_colorIndex(color) for color in colorBytes] # 转成 32 进制数 | bytes -> list
    colorBytes = base32_to_base256(colorBytes) # 转成 256 进制
    return bytes(colorBytes) # List -> bytes

def colors_to_bytes(colors:bytearray)-> bytearray:
    '''将等效颜色字节流转换为字节流\n
    源颜色字节不是5的倍数时，末尾补0'''
    if len(colors)%8 != 0:
        colors += b'\x00'*(8-len(colors)%8)
    bytes = bytearray()
    for i in range(0, len(colors), 8):
        bytes += color8_to_byte5(colors[i:i+8])
    return bytes

def pic_to_colors(file: str, width: int, height: int) -> bytearray:
    '''读取图片文件，返回等效颜色字节流'''
    img = Image.open(file)
    img = img.convert('RGB')
    img_width, img_height = img.size
    colors = bytearray()

    for y in range(height):
        for x in range(width):
            # x*img_width//width 可以得到分块左上角坐标，加上 img_width//(2*width) 可以得到中心坐标
            center_x = (x * img_width) // width + (img_width // (2 * width))
            center_y = (y * img_height) // height + (img_height // (2 * height))
            # getpixel 以左上角为原点
            # 假设高度为 100，坐标为 0~99，因此从下到上的坐标 1 等于从上到下坐标 98，1+98+1=100
            r, g, b = img.getpixel((center_x, img_height - center_y - 1))
            for i in (b, g, r):
                colors.append(i)
            # RGB 翻转成 BGR，这样符合实际保存时的顺序
            # 最终 colors 为等效颜色字节流
    return colors

def pic_to_file_bytes(input_file: str, width: int, height: int):
    colors = pic_to_colors(input_file, width, height)
    colors = colors_to_bytes(colors)
    data_len = struct.unpack('<i', colors[:4])[0]
    data = colors[4:4+data_len]
    return data

file_bytes = pic_to_file_bytes('hackergame2024\\1.png', 128, 137)
with open('hackergame2024\\aaa.bin', 'wb') as f:
    f.write(file_bytes)
```

#### VNC 内操作

```sh
split -b 32K /secret a
# 将文件切分成 16 份分别转图片，以免图片过大，读取时有误差
vim a.py
# vim 内使用 :set paste 避免自动缩进，按 I 进入输入模式，然后进行如下操作
```

将图片转文件脚本通过 pyautogui 模拟键盘输入到 VNC 中：

```python
import pyautogui

file_str = r'''
import struct
from pathlib import Path

def colorIndex_to_color(colorIndex:int)-> int:
    return colorIndex*8+4

def base256_to_base32(intList:list)-> list:
    number = intList[0]*256**4 + intList[1]*256**3 + intList[2]*256**2 + intList[3]*256 + intList[4]
    return [number//32**7, number//32**6%32, number//32**5%32, number//32**4%32, number//32**3%32, number//32**2%32, number//32%32, number%32]

def byte5_to_color8(byte:bytes)-> bytes:
    colorBytes = [color for color in byte]
    colorBytes = base256_to_base32(colorBytes)
    colorBytes = [colorIndex_to_color(color) for color in colorBytes]
    return bytes(colorBytes)

def bytes_to_colors(bytes:bytearray)-> bytearray:
    if len(bytes)%5 != 0:
        bytes += b'\x00'*(5-len(bytes)%5)
    colorarary = bytearray()
    for i in range(0, len(bytes), 5):
        colorarary += byte5_to_color8(bytes[i:i+5])
    return colorarary
    
def colors_to_bmp_data(colors:bytearray, width:int)-> tuple[bytearray, int]:
    data = bytearray()
    line_data_bytes = 3*width
    line_addition = (4 - line_data_bytes % 4) % 4
    line_bytes = line_data_bytes + line_addition
    for i in range(0, len(colors), line_data_bytes):
        data += colors[i:i+line_data_bytes]
        data += b'\x00'*(line_addition)
    data += b'\x00'*((line_bytes - len(data)%line_bytes) % line_bytes)
    height = len(data)//line_bytes
    return (data, height)

def file_to_bmp_bytes(file:str, width:int)-> bytearray:
    with open(file, 'rb') as f:
        file_bytes = bytearray(f.read())
    pix_header = bytearray(struct.pack('<i', len(file_bytes)))
    file_bytes = pix_header + file_bytes
    colors = bytes_to_colors(file_bytes)
    bmp_data, height = colors_to_bmp_data(colors, width)
    bmp_data_len = len(bmp_data)
    bmp_file_len = 54 + bmp_data_len
    bmp_file_header = bytearray(b'\x42\x4D'+struct.pack('<i', bmp_file_len)+b'\x00\x00\x00\x00'+b'\x36\x00\x00\x00'+b'\x28\x00\x00\x00'+struct.pack('<i', width)+struct.pack('<i', height)+b'\x01\x00'+b'\x18\x00'+b'\x00\x00\x00\x00'+struct.pack('<i', bmp_data_len)+b'\x25\x16\x00\x00'+b'\x25\x16\x00\x00'+b'\x00\x00\x00\x00'+b'\x00\x00\x00\x00')
    bmp_file = bmp_file_header + bmp_data
    print(f"width: {width}, height: {height}")
    return bmp_file

root = Path('/home/user')
a = root/input('input: ').strip()
b = root/input('output: ').strip()
bmp_bytes = file_to_bmp_bytes(a, 128)
with open(b, 'wb') as f:
    f.write(bmp_bytes)
'''
print(len(file_str))

# 等待几秒以便切换到目标窗口
time.sleep(3)
pyautogui.write(file_str)
```

```sh
# 使用 Esc 然后输入 :wq
python3 a.py
>>> aaa
>>> 1
# 重复到 aap 和 16
sha256sum a* # 校验原始分片的 sha256
```

在 VNC 内用 Firefox 打开 BMP 文件，设置图片 CSS 样式为 image-rendering: pixelated; 进入全屏模式，放大到最大。然后截图 16 张保存并用上述 Python 脚本转成 16 个分片文件。

在 linux 环境内使用 `cat a*.bin > combinedfile.bin` 将 16 个分片恢复成原来的文件，提交后拿到 flag。

### 写在最后

感谢看到这里的你，也感谢 Hackergame 组委会组织了这么一场比赛。虽然这次比赛专业性太强，我这三脚猫功夫没做几题就是了（笑）。不过我倒也借助这次比赛学了不少东西，比如 BMP 文件格式，有所收获。那么，下次见，Next phantasm...

