# 不宽的宽字符

题解作者：[luojh](https://github.com/ustcljh)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](https://hack.lug.ustc.edu.cn/credits/)。

## 题目描述

- 题目分类：general

- 题目分值：150

A 同学决定让他设计的 Windows 程序更加「国际化」一些，首先要做的就是读写各种语言写下的文件名。于是他放弃 C 语言中的 `char`，转而使用宽字符 `wchar_t`，显然这是一个国际化的好主意。

经过一番思考，他写出了下面这样的代码，用来读入文件名：

```cpp
// Read the filename
std::wstring filename;
std::getline(std::wcin, filename);
```

转换后要怎么打开文件呢？小 A 使用了 C++ 最常见的写法：

```cpp
// Create the file object and open the file specified
std::wifstream f(filename);
```

可惜的是，某些版本的 C++ 编译器以及其自带的头文件中，文件名是 `char` 类型的，因此这并不正确。这时候小 A 灵光一闪，欸🤓👆，我为什么不做一个转换呢？于是：

```cpp
std::wifstream f((char*)filename);
```

随便找了一个文件名测试过无误后，小 A 对自己的方案非常自信，大胆的在各个地方复用这段代码。然而，代价是什么呢？

---

现在你拿到了小 A 程序的一部分，小 A 通过在文件名后面加上一些内容，让你不能读取藏有 flag 的文件。

你需要的就是使用某种输入，读取到文件 `theflag` 的内容（完整位置是：`Z:\theflag`）。

> 注：为了使得它能在一些系统上正确地运行，我们使用 Docker 作了一些封装，并且使用 WinAPI 来保证行为一致，不过这并不是题目的重点。

**[完整题目附件下载](files/what_if_wider.zip)**

<details markdown="1">
  <summary style="display: revert; cursor: pointer" markdown="1"><b>题目核心逻辑预览</b>（点击展开）</summary>

```cpp
#include <iostream>
#include <fstream>
#include <cctype>
#include <string>
#include <windows.h>

int main()
{
    std::wcout << L"Enter filename. I'll append 'you_cant_get_the_flag' to it:" << std::endl;

    // Get the console input and output handles
    HANDLE hConsoleInput = GetStdHandle(STD_INPUT_HANDLE);
    HANDLE hConsoleOutput = GetStdHandle(STD_OUTPUT_HANDLE);

    if (hConsoleInput == INVALID_HANDLE_VALUE || hConsoleOutput == INVALID_HANDLE_VALUE)
    {
        // Handle error – we can't get input/output handles.
        return 1;
    }

    DWORD mode;
    GetConsoleMode(hConsoleInput, &mode);
    SetConsoleMode(hConsoleInput, mode | ENABLE_PROCESSED_INPUT);

    // Buffer to store the wide character input
    char inputBuffer[256] = { 0 };
    DWORD charsRead = 0;

    // Read the console input (wide characters)
    if (!ReadFile(hConsoleInput, inputBuffer, sizeof(inputBuffer), &charsRead, nullptr))
    {
        // Handle read error
        return 2;
    }

    // Remove the newline character at the end of the input
    if (charsRead > 0 && inputBuffer[charsRead - 1] == L'\n')
    {
        inputBuffer[charsRead - 1] = L'\0'; // Null-terminate the string
        charsRead--;
    }

    // Convert to WIDE chars
    wchar_t buf[256] = { 0 };
    MultiByteToWideChar(CP_UTF8, 0, inputBuffer, -1, buf, sizeof(buf) / sizeof(wchar_t));

    std::wstring filename = buf;

    // Haha!
    filename += L"you_cant_get_the_flag";

    std::wifstream file;
    file.open((char*)filename.c_str());

    if (file.is_open() == false)
    {
        std::wcout << L"Failed to open the file!" << std::endl;
        return 3;
    }

    std::wstring flag;
    std::getline(file, flag);

    std::wcout << L"The flag is: " << flag << L". Congratulations!" << std::endl;

    return 0;
}
```

</details>

你可以通过 `nc 202.38.93.141 14202` 来连接题目，或者点击下面的「打开/下载题目」按钮通过网页终端与远程交互。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

[打开/下载题目](http://202.38.93.141:14203?token={token})

## 题解

### 由来

Windows 程序的国际化问题，特别是原生 (Native) 程序的国际化问题，一直令许多程序员苦恼。这与 Windows 在发展初期采用了宽窄字符并存（例如不少 API 都有宽字符版本（`W` 后缀）和 ANSI 版本（`A` 后缀））的设计方法，以及 Windows 中大量采用 16 位宽字符存储文本内容有关。在将这些 API 与 C++ 程序结合使用的时候不可避免地会遇到字符集之间，以及不同的文本类型之间的转换。在一部分 `iostream` 的实现中，我们注意到 `wfstream` 并没有如预期的一样提供 `wstring`（即使用 16 位的 `wchar_t` 的 `std::string` 类似物）传入文件名的方式。这时候，正确的处理方法是使用宽窄字符集转换的 API 来完成从 `wstring` 到 `string` 的转换。这需要先取出 `wstring` 的原始内容（通过 `c_str()`），对原始数据进行转换然后再用转换后的窄字符文本重新创建 `string` 对象。这一步骤的操作稍有不慎也可能引起例如缓冲区溢出，以及不正确的文本转换（由于部分字符的特殊语义）之类的问题。此时，就有不了解相关原理的人，直接使用强制转换的方式转换不同类型成员的字符指针（题目里面那样）。这种做法是可能带来很大的问题的。

### 解法

我们首先来讨论题目的构造。本题目要求读取一个路径为 `Z:\theflag` 的文件。通过下载附件并构建 Docker 容器，您应该可以发现 `wider.exe` 程序运行时的当前目录 (Current directory) 就是 `Z:\`。此时为了读取这个文件，使用 `Z:\theflag` 或者 `theflag` 传入 `open()` 都是可以的。不幸的是，题目在转换完选手的输入后，在字符串的后面加上了一段文字，使其不可能完全等于被读取的文件名。然而，真的是这样吗？我们刚才是从二进制数据的角度去理解这个过程的，现在换成用字符串的角度去理解。已经知道，字符串是 `NULL` 结尾 (zero-terminated) 的，如果在字符串的中间加入一个 `\0`，就可以在**字符串层面**丢弃后面的内容。尽管我们不能从终端输入 `\0`，代码中的宽字符到窄字符的转换为我们提供了帮助。如果我们构造十六进制 `uvwx` 这样的字符，在将其从宽字符转换为窄字符的过程中，内存布局会是下面这样（注意，系统平台是小端字节序的 (little-endian)）：

```
          7      4 3      0 7      4 3      0
         +--------+--------+--------+--------+
wchar_t  |    w        x        u        v   |
         +--------+--------+--------+--------+
char     |    w        x   |    u        v   |
         +--------+--------+--------+--------+
```

按照刚才的想法，我们想要的结果是一个 `g\0` 这样子的字符作为结束，以此来抛弃后面加上的内容，而这里就应该是 (uv) = `\0`，(wx) = `g`。这在宽字符中刚好就是字母 `g`！这里，我们需要选择 `theflag`，而不是 `Z:\theflag`，是因为前者是 7 个字符的，加上一个 `\0` 恰好凑齐了 8 字节，对应 4 个宽字符。

剩下的字符构造起来就简单了。例如我们想要构造前两个字符 `th` 对应的输入，那么就去找到 t 和 h 的 [ASCII 代码](https://www.ascii-code.com/)，分别是 `0x74` 和 `0x68`，然后根据上面的讨论，需要构造的宽字符就是 `0x6874`，去 [Unicode 代码表](https://symbl.cc/en/unicode-table/) 上找到这个字符，即 `桴`。就这样一步一步地转化，可以得到我们的 payload，即 `桴晥慬g`。

您可以参考下面的表：

```
         +--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
wchar_t  |                桴                 |                晥                 |                慬                 |                g                  |
         +--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
hex      |       7 4       |       6 8       |       6 6       |       6 5       |       6 1       |       6 c       |       6 7       |       0 0       |
         +--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
char     |        t        |        h        |        e        |        f        |        l        |        a        |        g        |        \0       |
         +--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
```

## 附注

@taoky:

之所以要弄成 Windows 程序，是因为 POSIX 的 `wchar_t` 是 32 位的。

这道题最初始的版本是直接用 C++ std 的，但是在 wine + Linux terminal 下跑输入会变成 UTF-8，所以改成了用 Windows API 读数据。熟悉 Windows API 的同学可能会疑惑为什么不使用 `ReadConsoleW()`。这是因为：部署的时候题目程序实际的 I/O 是 socket 而不是 console，如果用 `ReadConsoleW` 的话，在 wine 下跑会抛出句柄无效的错误。

有人说这个逻辑明显是错误的，可能是因为小 A 拿了个纯中文名测试没问题吧（

另外题目里面的 `inputBuffer`，如果里面都没有 0，似乎可能造成 `MultiByteToWideChar` 之后 `buf` 也不以 0 结尾的问题。

最后，作为 Linux 用户，我只有一句话：[All in UTF-8](https://tonsky.me/blog/unicode/) 不香吗？反正 UTF-16 也没法准确地 O(1) 获取第 n 个字符嘛。

[@zzh1996](https://github.com/zzh1996) 补充：

在 Python 中执行 `b'theflag\x00'.decode('utf-16-le')` 即可得到 `桴晥慬g`

luojh 再补充：

实际上，假设文件名真的是偶数个字符呢？其实也是有办法的。注意到路径中重复的 `\` 或者 `/` 会被算作一个，那我们可以把要读取的文件名补全到奇数个字符。例如，`.//flag` 就是当前目录下的偶数个字符文件名 `flag` 的奇数个字符的写法。注意 `/flag` 对于当前目录下的 flag 文件是不正确的，因为这是指根目录下的 flag 文件，因此上面我们用 `.` 来表示当前目录。

@taoky 补充（2024/11/10）：

以上提到「可能是因为小 A 拿了个纯中文名测试没问题吧」，之后发现照理来讲，只有在小 A 输入一个字符的情况下才会出现这种情况。所以我拿以下的 C 标准程序在 Windows 10 LTSC 上做了一些测试：

```c
#include <stdio.h>
#include <wchar.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "");

    wchar_t buffer[256];
    fgetws(buffer, 256, stdin);

    for (int i = 0; buffer[i] != L'\0'; i++) {
        wchar_t wc = buffer[i];
        unsigned char *bytes = (unsigned char*) &wc;
        int size = sizeof(wchar_t);

        wprintf(L"Character %c in hexadecimal: ", wc);
        for (int j = 0; j < size; j++) {
            wprintf(L"%02x ", bytes[j]);
        }
        wprintf(L"\n");
    }

    return 0;
}
```

简体中文 Windows 的默认代码页是 CP936（GBK），这种情况读取到的是 UTF-16，没有问题：

```console
测试abc
Character 测 in hexadecimal: 4b 6d
Character 试 in hexadecimal: d5 8b
Character a in hexadecimal: 61 00
Character b in hexadecimal: 62 00
Character c in hexadecimal: 63 00
Character
 in hexadecimal: 0a 00
```

但是如果使用 `chcp 65001` 把代码页改成 UTF-8，神奇的事情就发生了——程序会读取到无法解释的内容：

```console
测试abc
Character 娴 in hexadecimal: 34 5a
Character 嬭 in hexadecimal: 2d 5b
Character 瘯 in hexadecimal: 2f 76
Character a in hexadecimal: 61 00
Character b in hexadecimal: 62 00
Character c in hexadecimal: 63 00
Character
 in hexadecimal: 0a 00
```

不知道是个啥编码。

在 wine 下运行的话结果似乎是有宽字符特色的 UTF-8：

```console
$ echo 测试abc | wine wide.exe
Character æ in hexadecimal: e6 00
Character µ in hexadecimal: b5 00
Character 9 in hexadecimal: 39 20
Character è in hexadecimal: e8 00
Character ¯ in hexadecimal: af 00
Character " in hexadecimal: 22 20
Character a in hexadecimal: 61 00
Character b in hexadecimal: 62 00
Character c in hexadecimal: 63 00
Character
 in hexadecimal: 0a 00
```

实在太乱了，还是 All in UTF-8 好。
