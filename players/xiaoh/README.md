也许更好的阅读体验： <https://xiao-h.com/2024/11/13/Hackergame2024-WriteUp/>

## 签到

下载各种输入法，多练习一下，应该就能输完了。~~不会真有人这么做吧~~

不会打字，我还不能复制粘贴吗？抱歉，还真不行，在网页源代码中我们可以看到粘贴被禁用了：

```html
<input type="text" class="input-box" id="zh" placeholder="中文：启动" onpaste="return false">
```

要想解决这一问题，可以用浏览器的调试工具把 `paste` 相关的内容全删了，这样就可以粘贴了。

## 喜欢做签到的 CTFer 你们好呀

首先要找到招新网站，其实玩意儿就在主页底下的承办单位里~~不知道为啥这么多人找不到~~

打开招新主页发现是个终端一样的东西，提示我们可以输 `help` 看可用的命令。多试几个命令，发现输入 `env` 可以获取第一个 flag.

输入 `cat`，得到提示：

```txt
file not found, maybe you can consider about Members / Awards / hidden files
```

说明还有隐藏文件。尝试 `cd`，发现要 root，这个时候加上 `sudo`，恭喜获得奶龙（

输入 `ls -a` 可以显示隐藏文件，于是我们就能看到隐藏的 `.flag` 了，`cat .flag` 即可。

## 猫咪问答

第 1、3、5 题可以简单地通过搜索得到答案；

第 2 题可以去往年题解的界面数题目个数，再到 LUG 官网找人数。~~虽然这里说约 25 道题目，但好像都不止~~

第 4 题，找到 USENIX Security 2024 的网站，搜索中科大的英文名，可以找到这篇论文，然后可以在论文中找到组合的数量。（注意，不是 $16 \times 20$）

第 6 题，你可以自己去下 Llama 3 70B 的完整模型，但是需要通过申请。在比赛的时候申请没过，这条路没走通。于是考虑直接搜索 tokenizer，找到了在线工具，把这一页 html 弄下来，用工具处理即可。

## 打不开的盒

下载文件，用 Blender 导入，移动视角到盒子里就能看见了。

## 每日论文太多了

首先下载论文，这道题肯定不会让全看一遍的~~不会真有人读了吧~~，直接搜索 flag，可以看到 `flag here` 这几个和背景颜色一样的字。~~我交了好多遍 flag{here}~~

仔细观察可以发现这边的有个框一样的东西，flag 应该是盖在底下了，用一些 PDF 编辑工具（比如福昕），可以把盖在上面的图片揭掉，这样就拿到 flag 了。

## 比大小王

~~快来成为口算大师~~

可以看到我们的对手非常强大，做题飞快，我们肯定不能莽，要智取。

考虑修改 js 源码。刚开始我想的是直接 submit，但是服务器会校验答案是否正确，这一招不行；接下来考虑让对手赢不了，把时间限制改成 114514，但是服务器还是会校验，再次失败；因为服务器会校验，所以只能考虑在规定时间内做出正确答案，看到数据 fetch 之后存在本地，我打算在刷新的时候在代码里计算下一个结果，然后添加进 `inputs` 里，可惜这样做速度不够（从中我们可以推知，就算你手速再快也是赢不了的）。

其实在加载的时候所有数据都已经存进 `data` 里了，不需要等待刷新，直接读取 `data.values` 就行了。我怕太快又被服务器 ban 掉，所以只是添加了个作弊键：

```js
if (e.key === 'ArrowLeft' || e.key === 'a') {
    document.getElementById('less-than').classList.add('active');
    setTimeout(() => document.getElementById('less-than').classList.remove('active'), 200);
    chooseAnswer('<');
} else if (e.key === 'ArrowRight' || e.key === 'd') {
    document.getElementById('greater-than').classList.add('active');
    setTimeout(() => document.getElementById('greater-than').classList.remove('active'), 200);
    chooseAnswer('>');
} else {
    if (state.values[state.score1][0] < state.values[state.score1][1]) {
        chooseAnswer('<');
        state.value1 = state.values[state.score1][0];
        state.value2 = state.values[state.score1][1];
        document.getElementById('value1').textContent = state.values[state.score1][0];
        document.getElementById('value2').textContent = state.values[state.score1][1];
        updateCountdown();
    } else {
        chooseAnswer('>');
        state.value1 = state.values[state.score1][0];
        state.value2 = state.values[state.score1][1];
        document.getElementById('value1').textContent = state.values[state.score1][0];
        document.getElementById('value2').textContent = state.values[state.score1][1];
        updateCountdown();
    }
}
```

然后按任意键，等差不多了再自己做，这样就能获得 flag 了。

## 旅行照片 4.0

### 第一题

科大人从东区到中区应该都能看到那栋大厦，问题 1 送分。

问题二我尝试搜索 B 站看有没有标时间，但是只发现了录播。你可以从录播上传日期往前试，不用几次就能拿到 flag 了。当然，也可以直接去 Leo 官群翻群公告（

### 第二题

问题 4 直接 Google 搜图可以得到结果，注意是景点名不是景观名。

问题 3 相对麻烦很多，因为可用信息太少了。我们可以从中发现两个比较突出的特征：彩虹跑道、垃圾桶。

仔细看垃圾桶上的字，可以分辨出 『六安』 两个字，这帮我们缩小了范围，大概率是在六安，当然也不能排除安徽省内。

以 『六安 彩虹跑道』等关键字搜索，翻遍各种平台，在百度的资讯选项卡中找到了一篇文章，包含了类似的图片，虽然它标的公园名字是错的，但我们可以通过这些图片继续搜图，最终找到了公园名称。

### 第三题

第三题对于火车迷来说应该是很容易的，但我完全不会，怎么办呢？

以提示的『四编组动车』为关键词进行搜索，可以得到 『CRH6F-A』和『CRH6A-A』这两个比较标志性的型号，此外可以看到列车涂装是红色的，通过对比图片可以看到列车的名称是『怀密号』，B 站找视频，看乘车全程，可以找到类似的地方，在地图上找一下就能找到最近的医院了。

## 不宽的宽字符

~~小 A 是怎么做到测试无误的~~

写个辅助函数帮助我们看文件名：

```cpp
typedef unsigned char *byte_pointer;
void show_bytes(byte_pointer start, int len) {
  int i;
  for (i = 0; i < len; i++)
    printf(" %.2x", start[i]); // line:data:show_bytes_printf
  printf("\n");
}
```

然后添加 `show_bytes((byte_pointer)filename.c_str(), 24);`，可以发现如果是直接输进去 `Z:\\theflag`（注意，题目里给 `Z:\theflag`，并不代表真的是这么输就行了，因为 `\` 会转义，需要两个 `\` 才能正常得到 `\` 字符），会输出：

```text
5a 00 3a 00 5c 00 74 00 68 00 65 00 66 00 6c 00 61 00 67 00 0d 00 00 00
```

其实我们可以发现，后面加不加东西，根本就不影响我们能不能弄到 flag，因为代码本来就有问题！

欸，为什么中间会有这么多 0 呢。这是因为输入的数据以 utf-8 储存，每个字符占 8 比特，也就是上面的两个 16 进制数字，经过了神奇的变化，就变成了现在这样。

要想让中间的 0 消失，我们直接输入 utf-16 的内容，就可以避免被转成这样了。可以用 Visual Studio Code 改编码方式，把 `Z:\\theflag` 存为 utf-16 编码。由于 utf-16 一个字符占两个字节，转成 utf-16 之后的内容没法正常显示，因为少了一个字节，用 16 进制编辑器在最后加上两个 0 就好了。

## PowerfulShell

我们首先看一下还剩什么符号：: ` 0 1 2 3 4 5 6 7 8 9 + - _ | $ [] {} ~ =

用这些符号是不足以实现命令 `cat /flag` 的，我们至少需要字母。

最开始我考虑获取 \ 来对八进制数字进行转义获取字母，但发现 \ 很难获取。

我们可以通过 `${var:a:b}` 来截取变量中的字符，而首先我们需要一个可获取的字符串并存入变量。

执行 `_1=~`，我们就获得了 `/players`，这还不够，我们还需要更多字符。

于是尝试截取字母 p 和 s，组成 ps，并将输出捕获，这样就有了更多字符，从中我们仍然得不到 `flag` 这个字符串，但我们有了 `cd` 和 `ls`。

来到根目录，捕获 `ls` 的输出，这样字母就足够了。

变量参考：

```shell
_1=~
_2=${_1:1:1}
_3=${_1:7:1}
_4=`$_2$_3`
_5=${_4:56:1}
_6=${_4:58:1}
_7=${_1:$[1-1]:1}
_8=$[1-1] // 替代 0
_9=${_4:1${_8}1:1}
_11=`$_9$_3 $_7`
_12=${_11:19:1}
_13=${_11:7:1}
_14=${_11:17:4}
```

## Node.js is Web Scale

我先把 set 操作时可能会影响我的 `JSON.stringify` 干掉，改成直接传没转义过的字符串。

分析源代码我们发现，唯一可能让我们执行 `cat /flag` 的地方在这里：

```js
app.get("/execute", (req, res) => {
  const key = req.query.cmd;
  const cmd = cmds[key];
  res.setHeader("content-type", "text/plain");
  res.send(execSync(cmd).toString());
});
```

但是我们发现 `cmds` 似乎已经写死了。拷打 LLM 之后，LLM 告诉我这里有原型链污染的问题，`{}` 实际上是一个对象（如果你往键里塞 `...`，按 `.` 分割之后再获取，就会输出 `{}` 的类型 `Object` 了），而它有额外的属性 `__proto__`，这个属性继承自 `Object`，在分割输入的键值时如果没有滤掉这个属性，在设置的时候其实设置的是 `Object` 对象的 `__proto__` 属性，这会导致所有继承于 `Object` 的对象 `__proto__` 都变掉，这样就可以修改 `cmds` 了。

## PaoluGPT

从小题名字上我们就可以猜出大概的做法了。

第一题毕竟是 『千里挑一』 嘛，flag 肯定就藏在这些网页里了。只要你有耐心可以一个个去找，当然，更好的方法是爬虫。

第二题，『未知』的东西一定不在这个列表里，我最开始尝试随机生成 UUID 然后访问，但算了算发现地球爆炸都跑不完，所以放弃了这种做法。

```py
@app.route("/view")
def view():
    conversation_id = request.args.get("conversation_id")
    results = execute_query(f"select title, contents from messages where id = '{conversation_id}'")
    return render_template("view.html", message=Message(None, results[0], results[1]))
```

分析代码我们可以发现，这里的 `conversation_id` 是直接替换进去的，没有经过转义，所以会存在 SQL 注入的风险。上面有查找 `shown = true` 的，要想“窥探未知”，自然就是找 `shown = false` 的了。

在地址栏中把 `conversation_id=` 后面改成 `' or shown = false--` 即可。

## 强大的正则表达式

第一问通过搜索发现，只要最后四位是 16 的倍数，整个数字就是 16 的倍数了。直接用 1000 以内的数字去匹配后四位即可。

第二问仍然搜索，可以找到[一道题](https://www.codewars.com/kata/5993c1d917bc97d05d000068)，想办法搞到题解就可以了。或者也可以在 Github 上搜这道题的名字，也有人分享了做法。这里有好多做法没法通过，可能要多试几个。

可惜我 Not Powerful Enough，做不出来第三题。

## 惜字如金 3.0

第一题直接人肉补全就行了。剩下的我不会。

## 优雅的不等式

知乎搜索『量化调酒师』，他有篇文章刚好能解决这题。

我们需要写脚本来自动生成式子，这可以用 ai 来辅助。

注意如果直接用网页复制粘贴，连接会超时被切断，需要使用一些方法（比如 `pwntools`）来上传。

以及 $n$ 的迭代，虽然不知道为什么，但是 $n = 3$ 跑得奇慢，建议直接用 $2^k$ 来作为 $n$。特别地，当到了 $37$ 个测试点以后，$n$ 为 128，生成的字符串会太长，可以适当降低 $n$。

~~非常烂的~~参考代码：

```py
from sympy import symbols
from sympy import expand, simplify, collect, solve, solveset
from sympy import integrals
from sympy import log, pi
from sympy import factor_terms
from sympy import Eq, Interval
from pwn import remote
import time, re

conn = remote('202.38.93.141', 14514)
token = b'input_your_token'
conn.send(token)
conn.send(b'\n')
conn.recvline()
conn.recvline()
conn.sendline(b'4*((1-x**2)**(1/2)-(1-x))')
conn.recvline()
conn.recvline()
conn.sendline(b'x**2*(x - 1)**2*(15*x**2 - 2*x + 15)/(x**2 + 1)')
conn.recvline()
conn.recvline()
conn.recvline()

x = symbols('x')
a, b, c = symbols('a b c')
n = symbols('n')

formula = (x**n * (1-x)**n * (a + b*x + c*x*x))/(1+x**2)

cnt: int = 3

while True:
    print("testcase", cnt)
    cnt += 1
    line = conn.recvline()
    response = line.decode('utf-8')
    print(response.strip('\n'))

    pattern = r'\d+/\d+'
    matches = re.findall(pattern, response)
    numbers = matches[0].split('/')

    p: int = int(numbers[0])
    q: int = int(numbers[1])

    domain = Interval(0, 1)
    cur_n: int = 32

    if (cnt > 18 and cnt <= 30):
        cur_n = 64
    elif (cnt > 30 and cnt < 37):
        cur_n = 128
    elif (cnt >= 37):
        cur_n = 112

    while True:
        print(cur_n, end=' ')
        cur_formula = formula.subs({n: cur_n})
        integraled_formula = integrals.integrate(cur_formula, (x, 0, 1))
        integraled_formula = simplify(integraled_formula)

        pi_formula = integraled_formula.coeff(pi)
        log2_formula = integraled_formula.coeff(log(2))
        other_formula = integraled_formula.subs({pi: 0, log(2): 0})

        solutions = solve(
            (
                Eq(pi_formula, q),
                Eq(log2_formula, 0),
                Eq(other_formula, -p)
            ), (a, b, c)
        ) 

        solution = cur_formula.subs(solutions)
        result = cur_formula.subs(solutions)/q
        result = simplify(result)

        f = (a + b*x + c*x*x).subs(solutions)
        formula_str = str(result).replace(' ', '')
        if (solveset(f >= 0, x, domain) != domain):
            cur_n *= 2
            continue
        if (len(formula_str) > 400 and cnt >= 37):
            print(len(formula_str), end='! ')
            expanded_str = str(expand(formula_str))
            if (len(expanded_str) <= 400):
                formula_str = expanded_str
            else:
                cur_n += 4
                continue
        print('\n')
        print(formula_str)
        print(len(formula_str))
        conn.sendline(formula_str)
        conn.recvline()
        break

```

## 无法获得的秘密

只能通过屏幕获取信息，考虑 OCR。

使用 `hexdump /secret | more` 可以逐页获取 `/secret` 内数据的十六进制字符串表示，然后只需要截图就可以了。

为了方便下面的 OCR 步骤，我们可以控制每一张图片的格式一致，并且尽量调大字体。我把屏幕分辨率调至某个值，同时终端最大化，字体设置为 `Monospace Bold`，字号 $20$，直接按固定的屏幕坐标截图就可以了，这样可以保证每次截图获取的数据都一样。

截图需要避免一些坑点，因为页数比较多，我写了个脚本自动帮我往下翻，但是如果翻得太快会导致视频来不及刷新~~建议在网络环境比较好的条件下进行，比如插网线~~；而太慢会导致超过 $15$ 分钟~~等半天也烦人~~

同样是为了便于 OCR，我先将图片二值化。

我尝试使用现有的解决方案，发现虽然准确率较高，但是不太能保证百分之百的准确率，即使是微调的模型我也没法确保必定正确~~也有可能是我太菜~~，所以尝试之后我就另寻他法了。

注意到截下来的图片都是固定格式的，字符都等宽的，我想到可以选一些字符作为标准，对于图片中的字符逐个匹配，计算相似度，选取最高的作为结果，如果相似度差太多就标成问号，在得到的结果中搜索问号手动排除。

在上一步的基础上，我得到了一系列文件，经过去重（因为截图步骤可能有差错）之后转为 `bytes` 写入文件即可。

整个步骤思路挺简单，但实现起来耗了很久时间~~菜~~。

（我怎么就没想到用容错率更高的手段，比如 QRCode 呢呜呜呜）

## 链上转账助手

直接 Copilot 启动，问 o1-preview，就可以获得前两问的 flag 了（第三问它告诉我要写底层代码，可能是我 PUA 技术还不够，它没法写出来）

## 不太分布式的软总线

仍然是用 o1 大法，顺利获得 3 个 flag（我都不知道我怎么就获得了，莫名其妙就过了）

~~或许这才是 AI 题吧~~

## 关灯

前三小题其实就是 OI 题，经典的关灯问题，转化成求解异或线性方程组，然后进行高斯消元。参考代码（灯的状态手动填一下）：

```cpp
#include <iostream>
#include <vector>
#include <bitset>
#include <string>

using namespace std;

const int n = 11;
const int tot = n * n * n;
bool result[n + 1][n + 1][n + 1];
bool M[tot + 1][tot + 2];

int conv(int x, int y, int z) {
    return (x - 1) * n * n + (y - 1) * n + z;
}

void generateMatrix(){
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= n; k++) {
                int index = conv(i, j, k);
                M[index][index] = true;
                if (i > 1) {
                    M[index][conv(i - 1, j, k)] = true;
                }
                if (i < n) {
                    M[index][conv(i + 1, j, k)] = true;
                }
                if (j > 1) {
                    M[index][conv(i, j - 1, k)] = true;
                }
                if (j < n) {
                    M[index][conv(i, j + 1, k)] = true;
                }
                if (k > 1) {
                    M[index][conv(i, j, k - 1)] = true;
                }
                if (k < n) {
                    M[index][conv(i, j, k + 1)] = true;
                }
                M[index][n*n*n+1] = result[i][j][k];
            }
        }
    }
}

void gauss() {
    int tot = n*n*n;
    for (int i = 1; i <= tot; i++) {
        int k = i;
        for (int j = i+1; j <= tot; j++) if (M[j][i] == 1) k = j;
        int now = M[k][i];
        if (k != i) for (int j = i; j <= tot + 1; j++) swap(M[i][j],M[k][j]);
        for (int k = 1; k <= tot; k++) if (k != i && M[k][i]) {
            for (int j = i; j <= tot + 1;j++) M[k][j] = M[k][j] ^ M[i][j];
        }
    }
}

int main() {
    std::string input = "input_light_status";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= n; k++) {
                result[i][j][k] = input[(i - 1) * n * n + (j - 1) * n + k - 1] == '1';
            }
        }
    }
    generateMatrix();
    gauss();

    for (int i = 1; i <= tot; i++) {
        cout << M[i][tot + 1];
    }
}
```

## 零知识数独

不会数独，也不会什么零知识证明，不过第一题还是可以做的，直接搜在线的解数独工具即可。

## 先不说关于我从零开始独自在异世界转生成某大厂家的 LLM 龙猫女仆这件事可不可能这么离谱，发现 Hackergame 内容审查委员会忘记审查题目标题了ごめんね，以及「这么长都快赶上轻小说了真的不会影响用户体验吗🤣」

~~这题什么鬼名字啊~~

第一题配合大模型，手动还原即可。有个坑点就是 `Txx xxxx wxs on` 这里的 `xxxx` 容易被猜成 `race`，实际上是 `game`，这玩意儿卡了我好多天。

~~所以你们穿 lab coat 吗~~
