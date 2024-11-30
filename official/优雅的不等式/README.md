# 优雅的不等式

题解作者：[mingliangz](https://github.com/mlzeng)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：math

- 题目分值：Easy（150）+ Hard（250）

> 注意到
>
> $$ e^2  - 7 = \int_{0}^{1} (1-x)^2 \cdot 4x^2 \cdot e^{2 x} \mathrm{d} x > 0 $$

你的数学分析助教又在群里发这些奇怪的东西，「注意力惊人」，你随手在群里吐槽了一句。

不过，也许可以通过技术手段弥补你涣散的注意力。

---

你需要用优雅的方式来证明 $\pi$ 大于等于一个有理数 $p/q$。

具体来说就是只使用**整数**和**加减乘除幂运算**构造一个简单函数 $f(x)$，使得这个函数在 $[0, 1]$ 区间上取值均大于等于 $0$，并且 $f(x)$ 在 $[0, 1]$ 区间上的定积分（显然大于等于 $0$）刚好等于 $\pi-p/q$。

给定题目（证明 $\pi\geq p/q$），你提交的证明只需要包含函数 $f(x)$。

- 要优雅：函数字符串有长度限制，
- 要显然：SymPy 能够**快速**计算这个函数的定积分，并验证 $[0,1]$ 上的非负性。

注：解决这道题不需要使用商业软件，只使用 SymPy 也是可以的。

<details markdown="1">
  <summary style="display: revert; cursor: pointer" markdown="1"><b>题目源代码</b>（点击展开） <a href="files/graceful_inequality.py">下载</a></summary>

```python3
import sympy

x = sympy.Symbol('x')
allowed_chars = "0123456789+-*/()x"
max_len = 400

# Example input for difficulty 0:   4*((1-x**2)**(1/2)-(1-x))

for difficulty in range(0, 40):
    if difficulty == 0:
        p, q = 2, 1
    elif difficulty == 1:
        p, q = 8, 3
    else:
        a = (2**(difficulty * 5))
        q = sympy.randprime(a, a * 2)
        p = sympy.floor(sympy.pi * q)
    p = sympy.Integer(p)
    q = sympy.Integer(q)
    if q != 1:
        print("Please prove that pi>={}/{}".format(p, q))
    else:
        print("Please prove that pi>={}".format(p))
    f = input("Enter the function f(x): ").strip().replace(" ", "")
    assert len(f) <= max_len, len(f)
    assert set(f) <= set(allowed_chars), set(f)
    assert "//" not in f, "floor division is not allowed"
    f = sympy.parsing.sympy_parser.parse_expr(f)
    assert f.free_symbols <= {x}, f.free_symbols
    # check if the range integral is pi - p/q
    integrate_result = sympy.integrate(f, (x, 0, 1))
    assert integrate_result == sympy.pi - p / q, integrate_result
    # verify that f is well-defined and real-valued and non-negative on [0, 1]
    domain = sympy.Interval(0, 1)
    assert sympy.solveset(f >= 0, x, domain) == domain, "f(x)>=0 does not always hold on [0, 1]"
    print("Q.E.D.")
    if difficulty == 1:
        print(open("flag1").read())

# finished all challenges
print(open("flag2").read())
```

</details>

你可以通过 `nc 202.38.93.141 14514` 来连接，或者点击下面的「打开/下载题目」按钮通过网页终端与远程交互。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

[打开/下载题目](http://202.38.93.141:14515/?token={token})

## 题解

这道题 idea 是 @zzh1996 的，我负责 implementation。

第一问，从代码注释给出的样例输入可以看出，将四分之一圆减去其内接三角形转换成定积分形式就能证明 $\pi \geq 2$，显然构造一个可以被四分之一圆覆盖并且面积等于 $2/3$ 的函数图像就可以证明 $\pi \geq 8/3$，一个很容易想到的例子就是抛物线 $f(x)=1-x^2$，刚好可以满足要求，于是提交函数 `4*((1-x**2)**(1/2)-(1-x**2))` 就可以完成证明。经过测试，一些大语言模型可以直接构造出这个函数。

第二问，后面的不等式会非常紧，通过上一问的方式构造函数是行不通的，所以需要寻找一些其它的技巧，在网络上很容易找到相关资料，比如知乎用户量化调酒师的[文章](https://zhuanlan.zhihu.com/p/669285539)，或者 Lucas 的[论文](https://educ.jmu.edu/~lucassk/Papers/more%20on%20pi.pdf)。可以发现一个很好用的函数形式是 $f(x)=\frac{(x(1-x))^n}{1+x^2}$，这个函数在 $[0, 1]$ 区间上取值均大于等于 $0$，定积分结果包含 $\pi$，并且 $n$ 取值越大就可以得到越小的定积分结果，同时 $\pi$ 的系数更大，进而证明更紧的不等式。枚举一些 $n$ 的值，用 SymPy 计算定积分，可以发现一个规律，就是 $n$ 为 8 的倍数时，得到的定积分结果的形式是有理数（负数）加上有理数（正数）系数乘以 $\pi$，最适合用于题目的不等式证明。当 $n$ 取 80 的时候，得到的定积分结果就已经可以达到题目要求。但是完成题目还需要能够得到一个精确相等的定积分值，解决方法也很简单，把 $n=80$ 和 $n=0$ 对应的函数加权求和即可。

```python
import sympy
import sys
import pwn

conn = pwn.remote('202.38.93.141', 14514)
token = open('token').read().strip()
conn.sendline(token.encode())

n = 80

assert n % 8 == 0
x = sympy.Symbol('x')
c = 4  # result of n=0
f = ((x * (1 - x))**n)
denom = (1 + x**2)

assert sympy.integrate(c / denom, (x, 0, 1)) == sympy.pi
f_integrate = sympy.integrate(f / denom, (x, 0, 1))
pi_coef = sympy.parse_expr([i for i in str(f_integrate).split('+') if 'pi' in i][0]) / sympy.pi
f = f / pi_coef
f_integrate = f_integrate / pi_coef

while True:
    while True:
        line = conn.recvline().strip().decode()
        print(line)
        if 'pi' in line:
            ab = line.split()[-1][4:]
            break
    if '/' in ab:
        a, b = ab.split('/')
        a = sympy.Integer(a)
        b = sympy.Integer(b)
    else:
        a = sympy.Integer(ab)
        b = 1
    w = (sympy.Integer(a) / sympy.Integer(b)) / (sympy.pi - f_integrate)
    ans = sympy.simplify((w * f + (1 - w) * c) / denom)
    print(ans)
    conn.sendline(str(ans).encode())
```
