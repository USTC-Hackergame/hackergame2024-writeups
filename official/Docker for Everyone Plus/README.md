# Docker for Everyone Plus

题解作者：[RTXUX](https://github.com/RTXUX)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](https://hack.lug.ustc.edu.cn/credits/)。

## 题目描述

- 题目分类：general

- 题目分值：No Enough Privilege（200）+ Unbreakable!（200）

X 是实验室机器的管理员，为了在保证安全的同时让同学们都用上 Docker，之前他直接将同学的用户加入 `docker` 组，但在去年参加了信息安全大赛之后，他发现将用户加入 `docker` 用户组相当于给了 root 权限。于是他想到了一个好方法，只授予普通用户使用 `sudo` 运行特定 Docker 命令的权限，这样就不需要给同学完整的 sudo 权限，也不用将同学加入 `docker` 组了！

但果真如此吗？

---

本题有两个小题。

- 可以使用 202.38.93.141 的 10338 端口或 [这个链接](http://202.38.93.141:10339/?token={token}) 访问第一小题。
- 可以使用 202.38.93.141 的 10340 端口或 [这个链接](http://202.38.93.141:10341/?token={token}) 访问第二小题。

---

提供的环境会自动登录低权限的 `user` 用户。登录后可以通过特定的 `sudo docker` 命令使用 Docker，通过 `sudo -l` 可以查看允许提权执行的命令。读取 `/flag`（注意其为软链接）获取 flag。

提供的环境中有 `rz` 命令，可以使用 ZMODEM 接收文件。

题目环境运行 15 分钟后会自动关闭。

你可以在下面列出的两种方法中任选其一来连接题目：

- 点击上面的链接，通过网页终端与远程交互。如果采用这种方法，在正常情况下，你不需要手动输入 token。
- 在 Linux、macOS、WSL 或 Git Bash 等本地终端中使用 `stty raw -echo; nc 202.38.93.141 10338; stty sane`（第一小题）或 `stty raw -echo; nc 202.38.93.141 10340; stty sane`（第二小题）命令来连接题目。如果采用这种方法，你必须手动输入 token（复制粘贴也可）。**注意，输入的 token 不会被显示，输入结束后按 Ctrl-J 即可开始题目。**

无论采用哪种方法连接题目，启动题目均需要数秒时间，出现黑屏是正常现象，请耐心等待。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

## 题解

这题是 @taoky 根据我在某实验室的集群上~~手痒~~提权的经历产生的 idea，我负责实现。去年 [Docker for Everyone](https://github.com/USTC-Hackergame/hackergame2023-writeups/blob/master/official/Docker%20for%20Everyone/README.md) 这题指出了 `docker` 用户组和 `root` 事实上是等价的，然而今年我看到有实验室集群使用受限 sudo 的方案来让大家能使用 Docker，但这种方案要处理的 corner case 很多，难以正确实现。

### No Enough Privilege

这个小题很简单，观察 `sudo -l` 的输出，发现 `user` 用户可以执行 `docker image load`，但 `docker run` 不能指定 `root` 用户，因此只需要制作自定义镜像，在其中嵌入合适的具有 SUID 的程序用来提权即可。下面的 Dockerfile 构建了一个简单的镜像。

```Dockerfile
FROM docker.io/library/alpine:latest

RUN apk add --no-cache su-exec && \
    chmod +s /sbin/su-exec
```

然后将该镜像导出后使用 ZModem 上传至环境，执行 `sudo docker image load` 导入，最后执行并把主机 `/` 挂入容器，提权即可获得 flag。

```sh
docker run --rm -u 1000:1000 -it --privileged -v /:/host:ro (image name)
exec su-exec root /bin/ash
cat /host/flag
```

### Unbreakable!

这个小题稍微增加了一些限制，从 `sudo -l` 可以看出 `docker run` 命令必须带上 `--security-opt=no-new-privileges` 参数，因此不能在容器内提权。但注意到 `mount` 的输出中 `/var/lib/docker` 挂载点没有 `nodev` 选项，而 flag 又位于 `/dev/vdb`，具有固定的设备号，因此我们可以加载一个带对应设备文件，且该文件所有者为 1000:1000 的镜像来读取 flag。

然而，Docker 采用了 cgroup 进行资源限制，其中 Device Controller 阻止容器访问未经授权的设备，同时也可以注意到，运行带 `--privileged` 或 `--device` 的 Docker 命令是被禁止的，因此无法从容器内读取 flag。但我们可以另辟蹊径，procfs 中提供了一个“穿越点”，即 `/proc/<pid>/root`，可以用于访问对应进程的挂载命名空间的根目录，而 `sudo docker run` 启动的容器是以 `user` 的 UID 执行的，因此 `user` 可以访问主机上 procfs 中容器内进程的目录。所以只需要预制一个带已修改所有者的设备文件的镜像，使用该镜像启动一个 `sleep` 命令，然后在主机上 `ps` 查看 `sleep` 命令的 PID，读取 `/proc/<pid>/root/flag` 即可得到 flag。

构建解题镜像的 Dockerfile:

```Dockerfile
FROM docker.io/library/alpine:latest

RUN mknod /flag b 253 16 && \
    chown 1000:1000 /flag
```

## 附注

@taoky:

看到群里很多人在困惑如何使用 ZMODEM 协议传文件。其中一个坑点是需要在 `/tmp`（或者其他 tmpfs）下面接收数据，因为其他部分是只读文件系统。`sz` 只会显示 "skipped: xxx" 而不会显示传输失败原因。

以下给出几种我本地测试有效的方法。这些方法都需要**本地安装 `lrzsz`**。注意 Arch Linux 用户需要使用 `lrzsz-sz` 而非 `sz`。

1. `screen`

    启动 `screen` 之后在其中 `nc` 连接，启动成功，输入 `rz` 后按下 Ctrl + A，然后输入 `:exec !! sz /path/to/yourfile`。

2. [Konsole](https://apps.kde.org/zh-cn/konsole/)

    `nc` 连接之后输入 `rz`，然后在弹出的文件对话框中选择对应的文件即可。

至于 Windows 用户，我也不知道咋上传。

因为工期比较紧张，所以最后用了 ZMODEM 这种比较低效的方法处理，网页 nc 也没有做相关的逻辑。之后如果还有 ZMODEM 的题目的话可能会考虑做一下网页端的处理，当然更有可能是用更加正常的协议来做文件上传。

@RTXUX (2024-11-09):

今天比赛结束后看到可以用 `--security-opt=no-new-privileges:false` 来绕过第二小问的限制，感觉当头一棒。其实赛前我草草看了一眼 [Docker CLI 的源码](https://github.com/docker/cli/blob/917d2dc837673ba6426ff72cabd53325028be809/cli/command/container/opts.go#L918)，认为解析 `--security-opt` 的部分会跳过对 `no-new-privileges` 值的解析，以为这个选项不能被覆盖，今天仔细重新看了一下这段代码，才理解了它的意思是 `no-new-privileges` 不需要值，但指定它的值也可以覆盖，导致了非预期解，再次印证了上面那句话「这种方案要处理的 corner case 很多，难以正确实现」。