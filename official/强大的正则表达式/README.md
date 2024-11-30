# 强大的正则表达式

题解作者：[mingliangz](https://github.com/mlzeng)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：math

- 题目分值：Easy（150）+ Medium（200）+ Hard（200）

从小 Q 开始写代码以来，他在无数的项目、帖子中看到各种神秘的字符串，听人推荐过，这就是传说中万能的正则表达式。本着能摆烂就绝不努力的原则，小 Q 从来没想过了解这门高雅艺术，遇到不懂的正则表达式就通通丢给 LLM 嘛，他这样想到。不过夜深人静的时候，小 Q 也时常在纠结写这么多 `switch-case` 到底是为了什么。

终于在一个不眠夜，小 Q 一口气看完了正则表达式的教程。哈？原来这么简单？小 Q 并两分钟写完了自测题目，看着教程剩下的目录，「分组」、「贪婪」、「前瞻」，正则表达式也不过如此嘛，他心想，也就做一些邮箱匹配之类的简单任务罢了。

正当他还沉浸在「不过如此」的幻想中，他刷到了那个关于正则表达式的古老而又神秘的传说：

「正则表达式可以用来计算取模和 CRC 校验……」

<details markdown="1">
  <summary style="display: revert; cursor: pointer" markdown="1"><b>题目源代码</b>（点击展开） <a href="files/powerful_re.py">下载</a></summary>

```python3
import re
import random

# pip install libscrc
import libscrc

allowed_chars = "0123456789()|*"
max_len = 1000000
num_tests = 300

difficulty = int(input("Enter difficulty level (1~3): "))
if difficulty not in [1, 2, 3]:
    raise ValueError("Invalid difficulty level")

regex_string = input("Enter your regex: ").strip()

if len(regex_string) > max_len:
    raise ValueError("Regex string too long")

if not all(c in allowed_chars for c in regex_string):
    raise ValueError("Invalid character in regex string")

regex = re.compile(regex_string)

for i in range(num_tests):
    expected_result = (i % 2 == 0)
    while True:
        t = random.randint(0, 2**64)  # random number for testing
        if difficulty == 1:
            test_string = str(t)  # decimal
            if (t % 16 == 0) == expected_result:  # mod 16
                break
        elif difficulty == 2:
            test_string = bin(t)[2:]  # binary
            if (t % 13 == 0) == expected_result:  # mod 13
                break
        elif difficulty == 3:
            test_string = str(t)  # decimal
            if (libscrc.gsm3(test_string.encode()) == 0) == expected_result:  # crc
                break
        else:
            raise ValueError("Invalid difficulty level")
    regex_result = bool(regex.fullmatch(test_string))
    if regex_result == expected_result:
        print("Pass", test_string, regex_result, expected_result)
    else:
        print("Fail", test_string, regex_result, expected_result)
        raise RuntimeError("Failed")

print(open(f"flag{difficulty}").read())
```

</details>

你可以通过 `nc 202.38.93.141 30303` 来连接，或者点击下面的「打开/下载题目」按钮通过网页终端与远程交互。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

[打开/下载题目](http://202.38.93.141:30304/?token={token})

## 题解

这道题 idea 是 @zzh1996 的，我负责 implementation。

第一问，由于判断一个十进制数是否整除 16 只需要看最后四位，所以枚举所有符合条件的最后四位，构造对应的正则表达式就可以了。严格来说还要考虑不足四位的情况，但是测试数据里面出现这种情况的概率很小，忽略掉也是通过的。

```python
print('(0|1|2|3|4|5|6|7|8|9)*' + '(' + '|'.join(f'{i:04d}' for i in range(0, 10000, 16)) + ')')
```

第二问，可以构造一个有限状态自动机（DFA）来判断一个二进制数是否整除 13。构造方法：DFA 的状态代表余数（有 0~12 一共 13 个状态），初始状态是 0，每次读入一个 bit 更新余数（状态转移）（`s:=(s*2+b)%13`），读入完毕后如果 DFA 处于 0 状态（余数为 0），就意味着这个二进制数整除 13。然后可以使用 [状态消除算法](https://courses.grainger.illinois.edu/cs374/sp2019/extra_notes/01_nfa_to_reg.pdf)，将 DFA 转化为正则表达式。

```python
# pip install greenery
# pip install regex
from greenery import Fsm, Charclass, rxelems
import regex as re
import random

m = 13
d = 2

digits = [Charclass(str(i)) for i in range(d)]
other = ~Charclass("".join(str(i) for i in range(d)))
alphabet = set(digits + [other])
states = set(range(m + 1))  # m is the dead state
initial_state = 0
accepting_states = {0}
transition_map = dict()
for s in range(m):
    transition_map[s] = {digits[i]: (s * d + i) % m for i in range(d)}
    transition_map[s][other] = m
transition_map[m] = {digits[i]: m for i in range(d)}
transition_map[m][other] = m

dfa = Fsm(
    alphabet=alphabet,
    states=states,
    initial=initial_state,
    finals=accepting_states,
    map=transition_map,
)

def convert_regex(regex):
    # `(...)?` -> `((...)|)`
    while '?' in regex:
        regex = re.sub(r'\((.*?)\)\?', r'(\1|)', regex)
    # Handle `{n}` quantifier
    n = 1
    while '{' in regex:
        while '{' + str(n) + '}' in regex:
            regex = re.sub(r'(\((.*?)\)|\w)\{n\}'.replace('n', str(n)), r'\1' * n, regex)
        n += 1
    # [abc] -> (a|b|c)
    while '[' in regex:
        def convert_charset(match):
            chars = match.group(1)
            return '(' + '|'.join(chars) + ')'
        regex = re.sub(r'\[([^\]]+)\]', convert_charset, regex)
    assert set(regex) <= set("0123456789|()*")
    return regex

dfa = dfa.reduce()
regex = rxelems.from_fsm(dfa)
regex = regex.reduce()
regex = convert_regex(str(regex))
print(regex)
```

第三问，同样是构造 DFA 然后转换成正则表达式。这次 DFA 的状态是线性反馈移位寄存器（LFSR）的状态，寄存器有 3 位，一共是 8 种状态（000~111），DFA 初始状态是 111，每次读入一个字符更新状态，读入完毕后如果 DFA 处于 000 状态，就意味着这个字符串符合要求。

```python
# pip install greenery
# pip install regex
# pip install libscrc
from greenery import Fsm, Charclass, rxelems
import regex as re
import libscrc

digits = [Charclass(str(i)) for i in range(10)]
other = ~Charclass(''.join(str(i) for i in range(10)))
alphabet = set(digits + [other])
states = set(range(9))  # 8 is the dead state
initial_state = libscrc.gsm3(b'')  # 7 (111)
accepting_states = {0}
transition_map = {s:dict() for s in states}
for s in states:
    transition_map[s][other] = 8
for prefix in range(1000):
    for i in range(10):
        s_1 = libscrc.gsm3(str(prefix).encode())
        s_2 = libscrc.gsm3(str(prefix).encode() + str(i).encode())
        transition_map[s_1][digits[i]] = s_2
for i in range(10):
    transition_map[8][digits[i]] = 8

dfa = Fsm(
    alphabet=alphabet,
    states=states,
    initial=initial_state,
    finals=accepting_states,
    map=transition_map,
)

def convert_regex(regex):
    # `(...)?` -> `((...)|)`
    while '?' in regex:
        regex = re.sub(r'\((.*?)\)\?', r'(\1|)', regex)
    # Handle `{n}` quantifier
    n = 1
    while '{' in regex:
        while '{' + str(n) + '}' in regex:
            regex = re.sub(r'(\((.*?)\)|\w)\{n\}'.replace('n', str(n)), r'\1' * n, regex)
        n += 1
    # [abc] -> (a|b|c)
    while '[' in regex:
        def convert_charset(match):
            chars = match.group(1)
            return '(' + '|'.join(chars) + ')'
        regex = re.sub(r'\[([^\]]+)\]', convert_charset, regex)
    assert set(regex) <= set("0123456789|()*")
    return regex

dfa = dfa.reduce()
regex = rxelems.from_fsm(dfa)
regex = regex.reduce()
regex = convert_regex(str(regex))
print(regex)
```
