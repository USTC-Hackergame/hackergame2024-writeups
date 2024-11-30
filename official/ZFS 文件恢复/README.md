# ZFS 文件恢复

题解作者：[iBug](https://github.com/iBug)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：general

- 题目分值：Text File（200）+ Shell Script（250）

你拿到了一份 ZFS 的磁盘镜像，里面据说有某沉迷 ZFS 的出题人**刚刚删除**的 flag。

「ZFS，我懂的。」这样说着，你尝试挂载了这个镜像（**请注意，以下命令仅供参考，且系统需要安装 ZFS 内核模块**）：

```shell
sudo losetup -fP ./zfs.img
sudo zpool import -d /dev/loop0 hg2024
cd /hg2024

# Hint: 使用以下命令取消挂载：
# sudo zpool export hg2024
# sudo losetup -d /dev/loop0
```

但是里面却没有你想要的 flag，这是怎么回事呢？

备注：

- 对于第一小题，你需要还原神秘消失的 `flag1.txt`。
- 对于第二小题，你需要还原神秘消失的 `flag2.sh`，并根据该 shell 脚本的内容恢复出更多信息，然后运行该脚本获得本小题的 flag。

[打开/下载题目](files/zfs.zip)

## 题解

题目灵感来源于 @taoky (sugoi!) 在调查 USTC 镜像站磁盘空间占用问题时提交的 bug：<https://github.com/openzfs/zfs/issues/15998>。当时我把这个有问题的 `pool1/log` dataset 打了个快照，send 到本地导入尝试排查，但是无论如何都无法复现，而且 ZFS 输出的大小也令人十分困惑：

```text
NAME                USED  AVAIL  REFER  MOUNTPOINT
pool1/log           173G  1.33T  2.73G  /mnt/mirrorlog
pool1/log@20240313  112K      -   170G  -
```

与传统文件系统依靠 OS 做“已删除文件”的 accounting 不同，ZFS 会把“已删除但仍有 open fd”的文件移进一个叫做 delete queue 的“目录”中，这样即使系统发生崩溃，ZFS 本身仍然处于一致的状态，不像其他文件系统在开机后需要立刻 fsck，所以其实这中间差的容量都隐藏在 delete queue 里了。

解题显而易见地需要挂载镜像，这里推荐使用 Ubuntu 或者 Proxmox VE（什么您在用这么高端的系统？），它们自带了 `zfs.ko` 无需手动 DKMS 编译安装，能节省不少时间。

挂在之后首先发现的是一个空的 data 目录，可能有人已经预料到本题考察的就是硬核 ZFS 知识了（也可能有人直接猜到是谁出的题了）。根据题目名称 `disk_snapshot`，观察一下快照情况：

```shell
# zfs list -rt all hg2024
NAME                 USED  AVAIL  REFER  MOUNTPOINT
hg2024               130K  23.9M    13K  /hg2024
hg2024/data           23K  23.9M    12K  /hg2024/data
hg2024/data@mysnap    11K      -    16K  -
```

果然还是有个快照的，再根据文案提示，两个被删掉的文件肯定就在这个快照的 delete queue 里了。

### Text File

本来我是想给一个 `zfs send` stream 文件作为题目附件的，但是那样就相当于直接告诉你 ZFS 有 `send`/`receive` 这个功能了，并且 `zfs send` 在不带参数的情况下默认是明文发送，那么你只需要把这个附件 receive 进一个地方，再重新 send 出来，就可以对新的 send stream 直接跑 `grep` 了，<s>违背了本题的初衷</s>。考虑到这一点，决定还是给 disk image 吧。这也是为什么恢复文件内容放在第一题，错误地估计了两题的难度。

如果你真的制造了一个 send stream 文件并且尝试打开它观察的话，你很快就会发现一大串小写字母，并且后面的内容大概是这样：

```text
zvzifjqdusmrxesmhxlpwadknaqtmiyakrgqcgimngyzjltqoskuyojvicmrnyplplngtoythfcnmzjg
eeaharhrleqvkyppyhirmpynvqzlploluaixmprpghaqjfl^C^@^@^@^@^@^@^@^B^@^@^@^@^@^@^@^
^S^@^@^@^@^@^@^@^@^P^@^@^@^@^@^@^@^P^@^@^@^@^@^@^?<B4>^NT<BD>m.8^B^@^@^@^@^@^@^@
^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@
^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@
^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@
^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@
^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@
^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@eo <9A><DE>^A^@^@Y<A7>!_^?<C6>^D
^@r2<EE><BA>^]<C6>ؒ<FB><8E>eg<9F>'ag{p1AInNNmmnnmmntExxt_50easy~r1ght?~}
```

再大胆假设一下，前面的一串小写字母结尾是 `fl`，后面一串可读的文字开头是 `ag{`，那么它肯定就是 flag 了！

---

以下是“正确”解法，全程高能 `zdb` 警告，并且还要 ddddd……因此这里强烈建议你在旁边打开一份 [`zdb(8)`](https://openzfs.github.io/openzfs-docs/man/master/8/zdb.8.html) 以供随时查阅，下面将不再介绍 `zdb` 的参数。

首先你需要找到 ZFS delete queue，它可以从 ZFS master node（固定为 1 号 object）里发现：

```shell
# zdb -ddddd hg2024/data@mysnap 1
Dataset hg2024/data@mysnap [ZPL], ID 139, cr_txg 11, 16K, 8 objects, rootbp DVA[0]=<0:23400:200> [L0 DMU objset] fletcher4 lz4 unencrypted LE contiguous unique single size=1000L/200P birth=11L/11P fill=8 cksum=0000000d1b083d83:0000050fca7ea511:0001038dc0199371:0023d987a86dd034

    Object  lvl   iblk   dblk  dsize  dnsize  lsize   %full  type
         1    1   128K    512    512     512    512  100.00  ZFS master node
        dnode flags: USED_BYTES USERUSED_ACCOUNTED USEROBJUSED_ACCOUNTED
        dnode maxblkid: 0
        microzap: 512 bytes, 7 entries

                utf8only = 0
                VERSION = 5
                normalization = 0
                DELETE_QUEUE = 33
                SA_ATTRS = 32
                ROOT = 34
                casesensitivity = 0
Indirect blocks:
               0 L0 0:f000:200 200L/200P F=1 B=7/7 cksum=00000007070b98aa:00000222f74a5222:0000630246afb9e8:000d204779823196

                segment [0000000000000000, 0000000000000200) size   512
```

对 delete queue 跑一下 `zdb`：

```shell
# zdb -ddddd hg2024/data@mysnap 33
Dataset hg2024/data@mysnap [ZPL], ID 139, cr_txg 11, 16K, 8 objects, rootbp DVA[0]=<0:23400:200> [L0 DMU objset] fletcher4 lz4 unencrypted LE contiguous unique single size=1000L/200P birth=11L/11P fill=8 cksum=0000000d1b083d83:0000050fca7ea511:0001038dc0199371:0023d987a86dd034

    Object  lvl   iblk   dblk  dsize  dnsize  lsize   %full  type
        33    1   128K    512      0     512    512  100.00  ZFS delete queue
        dnode flags: USED_BYTES USERUSED_ACCOUNTED USEROBJUSED_ACCOUNTED
        dnode maxblkid: 0
        microzap: 512 bytes, 2 entries

                2 = 2
                3 = 3
Indirect blocks:
               0 L0 EMBEDDED et=0 200L/34P B=11

                segment [0000000000000000, 0000000000000200) size   512
```

可以看到两个文件的 dnode number（即 inode number）分别是 2 和 3。

首先观察 2 号文件：

```shell
# zdb -ddddd hg2024/data@mysnap 2
Dataset hg2024/data@mysnap [ZPL], ID 139, cr_txg 11, 16K, 8 objects, rootbp DVA[0]=<0:23400:200> [L0 DMU objset] fletcher4 lz4 unencrypted LE contiguous unique single size=1000L/200P birth=11L/11P fill=8 cksum=0000000d1b083d83:0000050fca7ea511:0001038dc0199371:0023d987a86dd034

    Object  lvl   iblk   dblk  dsize  dnsize  lsize   %full  type
         2    2   128K     4K  3.50K     512     8K  100.00  ZFS plain file
                                               176   bonus  System attributes
        dnode flags: USED_BYTES USERUSED_ACCOUNTED USEROBJUSED_ACCOUNTED
        dnode maxblkid: 1
        path    on delete queue
        uid     0
        gid     0
        atime   Thu Mar  9 23:56:50 2006
        mtime   Sun May 29 03:49:29 1977
        ctime   Wed Oct 23 21:37:22 2024
        crtime  Wed Oct 23 21:37:22 2024
        gen     10
        mode    100644
        size    4135
        parent  34
        links   0
        pflags  840800000004
Indirect blocks:
               0 L1  0:21800:400 20000L/400P F=2 B=11/11 cksum=00000090a02a87e8:00005c1242163a70:001f9a22c2a8565e:07b4c5ba8259446b
               0  L0 0:20e00:a00 1000L/a00P F=1 B=11/11 cksum=0000014a1deb79ea:0001a7601903257e:0162d0f05c3cdc80:ddef6cee5f27f0da
            1000  L0 EMBEDDED et=0 1000L/49P B=11

                segment [0000000000000000, 0000000000002000) size    8K
```

从这里可以得知它的大小是 4135 字节，权限是 `100644`（无执行权限的普通文件），那么它很可能是第一题的文本文件。

```shell
# zdb -R hg2024 0:20e00:1000/a00:d
Found vdev: /dev/loop0

0:20e00:1000/a00:d
          0 1 2 3 4 5 6 7   8 9 a b c d e f  0123456789abcdef
000000:  7967786d6f656a74  6e686c63716a6468  tjeomxgyhdjqclhn
000010:  6f716466796c6f63  6866776675626d6a  colyfdqojmbufwfh
[...]
000fe0:  79706d7269687970  6f6c706c7a71766e  pyhirmpynvqzlplo
000ff0:  72706d786961756c  6c666a7161686770  luaixmprpghaqjfl
```

于是你拿到了本文件的前 4096 字节，但是里面并没有 flag，尝试解析下一个 block，发现它是 EMBEDDED，因此你需要从那个 L1 的 block 里尝试解析：

```shell
# zdb -R hg2024 0:21800:20000/400:d
Found vdev: /dev/loop0

0:21800:20000/400:d
          0 1 2 3 4 5 6 7   8 9 a b c d e f  0123456789abcdef
[...]
000080:  74302eaf4c4b9c78  cbcdcdcbf3f3ccf4  x.KL..0t........
000090:  78928a8ad712e203  22bacae2c4d48353  .......xS......"
0000a0:  2e5abafb128cf4c3  1828c1460a305186  ......Z..Q0.F.(.
0000b0:  8013008a90000fff  3051828c1460a305  ..........`...Q0
0000c0:  60a3051828c1460a  0e341800005d0c14  .F.(...`..]...4.
0000d0:  000000000000000b  00000000000000b2  ................
0000e0:  0000000000000000  0000000000000000  ................
0000f0:  0000000000000000  0000000000000000  ................
000100:  0000000000000000  0000000000000000  ................
[...]

# zdb -E 74302eaf4c4b9c78:cbcdcdcbf3f3ccf4:78928a8ad712e203:22bacae2c4d48353:2e5abafb128cf4c3:1828c1460a305186:8013008a90000fff:3051828c1460a305:60a3051828c1460a:0e341800005d0c14:000000000000000b:00000000000000b2:0000000000000000:0000000000000000:0000000000000000:0000000000000000
ag{p1AInNNmmnnmmntExxt_50easy~r1ght?~}
```

好了，你已经获得了本文件完整的 4135 字节了，可以提交 flag 了。

---

为什么第一小题这么麻烦呢？因为前面提到，直接 `zfs send` 可以（几乎）逃课 zdb，因此在生成这份 disk.img 的时候，我特地做了额外的措施避免让 `disk.img` 文件可以直接 grep 或者 binwalk：

- `zfs set recordsize=4k compression=gzip`
- 在前面填充 4094 个字节的小写字母，使得第一个 block 包含 flag 开头的 `fl` 两个字母，并且高度可压缩
- flag 剩余的字节数不超过 112，可以被 ZFS 放进一个 embedded block pointer 里

### Shell Script

如果你已经做出第一题了，那么恢复 shell 脚本文件肯定难不倒你了：

```shell
# zdb -R hg2024 0:20800:200
Found vdev: /dev/loop0

0:20800:200
          0 1 2 3 4 5 6 7   8 9 a b c d e f  0123456789abcdef
000000:  732f6e69622f2123  6b5f67616c660a68  #!/bin/sh.flag_k
000010:  30326768223d7965  61747328245f3432  ey="hg2024_$(sta
000020:  2e582520632d2074  3167616c66205925  t -c %X.%Y flag1
000030:  28245f297478742e  20632d2074617473  .txt)_$(stat -c
000040:  24222059252e5825  2273667a5f292230  %X.%Y "$0")_zfs"
000050:  3422206f6863650a  3731623831356336  .echo "46c518b17
000060:  3034346431353635  3839363338313737  5651d44077183698
000070:  3430343765346137  3461303262343866  7a4e7404f84b20a4
000080:  3339393831636333  3733613761626666  3cc18993ffba7a37
000090:  2038303566363031  742f203e20222d20  106f508  -" > /t
0000a0:  35326168732f706d  7478742e6d757336  mp/sha256sum.txt
0000b0:  2066746e6972700a  6624222022732522  .printf "%s" "$f
0000c0:  2279656b5f67616c  3532616873207c20  lag_key" | sha25
0000d0:  632d2d206d757336  6d742f206b636568  6sum --check /tm
0000e0:  3635326168732f70  207478742e6d7573  p/sha256sum.txt
0000f0:  2074697865207c7c  66746e6972700a31  || exit 1.printf
000100:  737b67616c662220  5f746f687370616e   "flag{snapshot_
000110:  2220226e5c7d7325  66746e6972702824  %s}\n" "$(printf
000120:  2422202273252220  79656b5f67616c66   "%s" "$flag_key
000130:  31616873207c2022  6568207c206d7573  " | sha1sum | he
000140:  323320632d206461  00000000000a2229  ad -c 32)"......
[...]
```

恢复出的脚本内容如下：

```shell
#!/bin/sh
flag_key="hg2024_$(stat -c %X.%Y flag1.txt)_$(stat -c %X.%Y "$0")_zfs"
echo "46c518b175651d440771836987a4e7404f84b20a43cc18993ffba7a37106f508  -" > /tmp/sha256sum.txt
printf "%s" "$flag_key" | sha256sum --check /tmp/sha256sum.txt || exit 1
printf "flag{snapshot_%s}\n" "$(printf "%s" "$flag_key" | sha1sum | head -c 32)"
```

根据代码提示，需要拼出 `flag_key` 字符串，你只需要看一下 [`stat(1)`](https://linux.die.net/man/1/stat) 就知道还需要找出 `flag1.txt` 和本文件（`$0`）的 atime 和 mtime，相信这也难不倒<s>已经被迫把 `zdb` 用熟练的</s>你：

```shell
# zdb -ddddd hg2024/data@mysnap 2
[...]
        atime   Thu Mar  9 23:56:50 2006
        mtime   Sun May 29 03:49:29 1977
[...]
# zdb -ddddd hg2024/data@mysnap 3
[...]
        atime   Mon Nov 10 04:49:03 2036
        mtime   Sat Jan 12 01:18:00 2013
[...]
```

还原得到 `flag_key` 手工替换进脚本中：

```shell
#!/bin/sh
flag_key="hg2024_1141919810.233696969_2109876543.1357924680_zfs"
echo "46c518b175651d440771836987a4e7404f84b20a43cc18993ffba7a37106f508  -" > /tmp/sha256sum.txt
printf "%s" "$flag_key" | sha256sum --check /tmp/sha256sum.txt || exit 1
printf "flag{snapshot_%s}\n" "$(printf "%s" "$flag_key" | sha1sum | head -c 32)"
```

运行脚本确认 `sha256sum` 结果正确即可得到 `flag{snapshot_6db0f20dd59a448d314cb9cabe8daea9}`。

## 花絮

<!-- autocorrect-disable -->

果不其然有同学私聊我说：

> 妈的 hkgame这zfs题是不是群zfs专家出的

> \[表情\]

> 现在熟练使用zdb和了解zfs on-disk了 md

🤣
