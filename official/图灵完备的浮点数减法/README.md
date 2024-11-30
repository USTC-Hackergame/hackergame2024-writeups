# 图灵完备的浮点数减法

题解作者：[zzh1996](https://github.com/zzh1996)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：math

- 题目分值：300

> 以下内容包含 AI 辅助创作

「老师说神经网络必须要有非线性激活函数，那岂不是意味着单靠浮点数的加减法是做不到图灵完备的，但是……」你摸着下巴若有所思。

在计算机的世界里，总有一些出人意料的存在：PowerPoint 可以做出图灵机，Minecraft 的红石电路能实现 CPU，甚至只靠 x86 的 MOV 指令都能构建起完整的计算世界。

而现在，你盯着 IEEE-754 浮点数标准发起了呆。在这片看似平凡的数字海洋中，小数点的漂移、尾数的舍入、指数的溢出，都在无声地诉说着某种可能性。

「如果只用浮点数减法……」

「如果真的只用浮点数减法……」

你的嘴角渐渐浮现出神秘的微笑。

现在，请用浮点数减法实现 SHA-256 算法。记住，只能用减法。

> AI 辅助创作部分结束

（注：本题未实现循环，所以只是组合完备而非图灵完备。）

<details markdown="1">
  <summary style="display: revert; cursor: pointer" markdown="1"><b>题目源代码</b>（点击展开） <a href="files/floatsha256.py">下载</a></summary>

```python3
import os
from hashlib import sha256

LIMIT = 1000000

def read_program():
    print('Your program:')
    program = []
    while True:
        line = input().strip()
        if line == 'EOF':
            break
        if len(program) >= LIMIT:
            raise ValueError('Program too long')
        nums = line.split()
        if len(nums) == 1:
            program.append(float(nums[0]))
        elif len(nums) == 2:
            program.append((int(nums[0]), int(nums[1])))
        else:
            raise ValueError('Invalid input')
    return program

def run_program(program, data, output_size):
    mem = [float(b) for b in data]
    for line in program:
        if isinstance(line, float):
            mem.append(line)
        else:
            index0, index1 = line
            assert index0 in range(len(mem)), 'Index out of range'
            assert index1 in range(len(mem)), 'Index out of range'
            mem.append(mem[index0] - mem[index1])
    assert len(mem) >= output_size
    output = []
    for x in mem[-output_size:]:
        b = int(x)
        assert float(b) == x, 'Output is not an integer'
        assert b in range(256), 'Output not in range'
        output.append(b)
    return bytes(output)

def main():
    prog = read_program()
    for i in range(10):
        print(f'Testing {i}')
        data = os.urandom(32)
        if sha256(data).digest() != run_program(prog, data, 32):
            print(f'Wrong answer at input {data.hex()}')
            exit(-1)
    print(open('flag').read())

if __name__ == "__main__":
    main()
```

</details>

你可以通过 `nc 202.38.93.141 10094` 来连接，或者点击下面的「打开/下载题目」按钮通过网页终端与远程交互。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

[打开/下载题目](http://202.38.93.141:10095/?token={token})

## 题解

### 理解题目

这道题让你只用浮点数的减法实现一个 SHA-256 计算程序。与其说是「程序」，不如说是「电路」或者「计算图」更贴切一些。题目要求你输入的每一行是两种格式之一，一种就是一个浮点数，表示一个常数；另一种是两个整数，含义是两个编号，表示把这个计算图中的哪两个节点取出来进行浮点数减法运算。

SHA-256 的计算过程可以理解成一个巨大的组合逻辑电路。为了实现 SHA-256，我们可以拆解一下问题，先用浮点数减法实现 AND 和 OR 之类的基本逻辑门的功能，然后再用这些逻辑门组合成完整的 SHA-256。除此之外，我们还要想办法解决一下输入和输出的转换问题，也就是，如何把 0 到 255 的整数，拆解成一个一个 bit，以及反向的过程如何实现。

### 逻辑门的构造

如果我们可以实现一个 NAND 门，那么就可以用它实现任意的组合逻辑电路。

先假设 False 对应浮点数的 0.0，True 对应浮点数的 1.0。这样实现 NOT 运算很简单，`x` 的 NOT 就是 `1.0 - x` 即可。

现在再实现 AND 运算。首先如果有浮点数减法，那么我们可以实现浮点数加法，因为 `x + y = x - (0.0 - y)`。然后如果我们简单地把 AND 的两个输入加起来，得到的结果有 0.0、1.0、2.0 三种情况。然后减去 1，可以得到 -1.0、0.0、1.0 三种情况。我们现在需要做的就是，想办法把这里的 -1.0 和 0.0 都变成 0.0，这样就可以跟 AND 的真值表相对应了。

这里可以使用浮点数计算的舍入来实现。我们知道浮点数正因为它是浮动的小数点，所以在不同数量级下的精度是不同的，也就是说相邻两个浮点数的距离是不一样的。那我们只要找到精度变化的地方，比方说，如果三个相邻的浮点数分别是 `a - 2`、`a` 和 `a + 1`，那么就应该可以让 `a - 1` 舍入到 `a`，同时保持 `a + 1` 不变。这样，我们把 -1.0、0.0、1.0 三种情况分别加上 `a` 然后减去 `a`，就可以利用精度把 -1.0 卡成 0.0。如何找到这样的 `a` 呢？在理解浮点数的编码格式之后，只要根据尾数最后一位的影响反过来推算一下，或者不断增加指数来穷举一下就行，`a` 其实就是 2 的 53 次方再取个相反数。

![浮点数精度](assets/float.png)

所以，在 False 对应 0.0、True 对应 1.0 的前提下，AND 运算的公式就是 `x AND y = x - (0.0 - y) - 1.0 - float(2 ** 53) + float(2 ** 53)`。

既然已经有了 NOT 和 AND，理论上我们可以实现任意的组合逻辑电路。如果需要降低总的减法运算次数，我们也可以直接用上述思路实现其他的逻辑门。

### 输入输出的处理

那如何把输入的 0 到 255 的整数拆解成 8 个 bit 呢？

我们定义两种操作：一种叫做截断，例如说把 0 到 127 都变成 0、把 128 到 255 都变成 128。用 Python 写出来就是 `x // (2 ** i) * (2 ** i)`。另一种是除以 2，不过只支持 2 的幂即可，例如把 0 和 128 分别变成 0 和 64。

为了实现截断，我们可以把输入的数值平移到某个浮点数精度的地方，比如让浮点数的最小精度是 128，这样靠舍入就可以实现截断了。

至于把 2 的幂除以 2，我们可以使用构造逻辑门的时候的卡精度的方法，找到一个三个相邻浮点数是 `a - 1`、`a` 和 `a + 2` 的地方，然后让输入是 `a - 1` 或者 `a + 1`，这样就可以靠舍入让两个数的间距减半，然后平移回去就行了。

有了这两种操作，我们就可以把一个 0 到 255 整数的二进制最高位取出来，变成 0 或者 1，然后把最高位减掉，再继续取最高位，从而把所有 bit 都拆解出来。

至于输出，也就是把 8 个 bit 组合成 0 到 255 的整数，这个就简单了。既然我们有加法和乘以 2 的操作（乘以 2 就是自己和自己相加），我们直接把 bit 乘以权重加起来就行了。

### 实现 SHA-256

为了实现 SHA-256 算法，我是用逻辑门实现了 32 位整数的加法器、位运算、移位等等操作，然后参考 [PyPy 的 SHA-256 实现](https://foss.heptapod.net/pypy/pypy/-/blob/branch/default/lib_pypy/_sha256.py) 写了一个计算图的生成程序。

**最终完整的解题代码在 [这里](solve.py)**。使用 `(echo '[你的 Token]' && sleep 1 && python3 solve.py && cat) | nc 202.38.93.141 10094` 即可得到 flag。

实际上，由于这种布尔电路在零知识证明等密码学场景中比较常用，所以你也可以寻找一个现成的电路来使用，例如 [这个](http://stevengoldfeder.com/projects/circuits/sha2circuit.html)。我这里手工实现，只是想说明不依赖于别人的布尔电路也能解出这题。

### 出题思路

我出这道题是因为看到了 [这篇博客文章](https://orlp.net/blog/subtraction-is-functionally-complete/)。

我一开始想出成用 `+0`、`-0` 来计算的，但是这样似乎就必须用 `+0`、`-0` 作为程序的输出，对于解法的提示太明显，也不好玩。于是我自己试了一下，其实不用 `+0`、`-0` 也是可以的，于是改成了输出和输出都是 0 到 255 的整数的形式。

### 一些思考

这题我限制了输入最多有一百万行，其实这个约束是相当宽松的。如果第一版的实现超过了限制，很容易通过一些基本的优化就能减少到一百万以内。我出这道题的时候没有仔细去思考如何优化到极致。我在想，是否有办法突破逻辑门这层抽象来优化，比方说把多个 bit 打包进一个浮点数里面进行向量化（类似 SIMD）的运算。如果有人有巧妙的构造非常欢迎交流讨论。
