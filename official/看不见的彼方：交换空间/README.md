# 看不见的彼方：交换空间

题解作者：[taoky](https://github.com/taoky)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：general

- 题目分值：小菜一碟（200）+ 捉襟见肘（250）

[两年过去了](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/%E7%9C%8B%E4%B8%8D%E8%A7%81%E7%9A%84%E5%BD%BC%E6%96%B9/README.md)，今年，Alice 和 Bob 再次来到了 Hackergame 的赛场上。这一次，他们需要在各自的 `chroot(2)` 的限制下，将自己手头 tmpfs 里面（比较大的）文件交给对方。

好消息是，这次没有额外的 `seccomp(2)` 限制，但是，他们所处的容器环境的 rootfs 是只读的，并且内存也是有限的，所以如果再复制一份的话，整个容器就会被杀死。Alice 和 Bob 希望请你帮助他们解决这个难题。

对于本题的第一小题，两个文件（`/home/pwn/A/space/file` 和 `/home/pwn/B/space/file`）大小均为 128 MiB。你需要在你的程序运行完成后使两者的内容互换。

对于本题的第二小题，Alice 有一个 128 MiB 的文件（`/home/pwn/A/space/file`），Bob 有两个 64 MiB 的文件（`/home/pwn/B/space/file1` 和 `/home/pwn/B/space/file2`）。你需要在你的程序运行完成后实现（原始文件 -> 交换后的文件）：

- `/home/pwn/A/space/file` -> `/home/pwn/B/space/file`
- `/home/pwn/B/space/file1` -> `/home/pwn/A/space/file1`
- `/home/pwn/B/space/file2` -> `/home/pwn/A/space/file2`

容器内存限制 316 MiB，你提交的程序文件会复制为两份，分别占用一份内存空间。环境限制总 PID 数为 32。对于 chroot 内部的进程，只有 `/space` 可读写。`/space`（`/home/pwn/A/space/` 和 `/home/pwn/B/space/`）为 tmpfs，使用内存空间。

**[题目附件下载](files/swap.zip)**

[打开/下载题目](http://202.38.93.141:22024/?token={token})

## 题解

本题是 [@zzh1996](https://github.com/zzh1996) 的 idea，和两年前一样，我做了实现。本题放开了系统调用限制，因为没有必要再在这个地方卡人。

### Flag 1

Flag 1 可以用很简单的方式处理：Alice 和 Bob 分别作为 HTTP client 和 server，每一轮互相传 1M 数据，传 128 轮就好了。本题解为了方便，直接用 Golang 写了：

Client:

```go
// client.go
package main

import (
	"bytes"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"runtime"
	"runtime/debug"
	"time"
)

const (
	DataSize    = 1 << 20 // 1MB
	TotalRounds = 128
	ServerURL   = "http://127.0.0.1:8080/exchange"
)

func main() {
	runtime.GOMAXPROCS(2)
	debug.SetMemoryLimit(10485760)

	client := &http.Client{}
	file, err := os.OpenFile("/space/file", os.O_RDWR, 0644)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	time.Sleep(1 * time.Second)

	buffer := make([]byte, DataSize)

	for i := 1; i <= TotalRounds; i++ {
		n, err := file.Read(buffer)
		if err != nil || n != DataSize {
			panic(err)
		}
		req, err := http.NewRequest("POST", ServerURL, bytes.NewReader(buffer))
		if err != nil {
			log.Fatalf("%d new request failed: %v", i, err)
		}
		req.Header.Set("Content-Type", "application/octet-stream")
		req.ContentLength = DataSize

		resp, err := client.Do(req)
		if err != nil {
			log.Fatalf("%d send failed: %v", i, err)
		}

		responseData := make([]byte, DataSize)
		n, err = io.ReadFull(resp.Body, responseData)
		resp.Body.Close()
		if err != nil {
			log.Fatalf("%d read failed: %v", i, err)
		}
		if n != DataSize {
			log.Fatalf("%d read size not match", i)
		}

		_, err = file.Seek(-int64(n), io.SeekCurrent)
		if err != nil {
			panic(err)
		}
		_, err = file.Write(responseData)
		if err != nil {
			panic(err)
		}

		fmt.Printf("%d succeed.\n", i)
	}

	fmt.Println("Done!")
}
```

Server:

```go
// server.go
package main

import (
	"errors"
	"io"
	"log"
	"net/http"
	"os"
	"runtime"
	"runtime/debug"
)

const (
	DataSize     = 1 << 20 // 1MB
	TotalRounds  = 128
	Port         = ":8080"
	EndpointPath = "/exchange"
)

var file *os.File
var cnt = 0

func exchangeHandler(w http.ResponseWriter, r *http.Request) {
	buffer := make([]byte, DataSize)
	n, err := file.Read(buffer)
	if err != nil {
		panic(err)
	}
	if n != DataSize {
		panic(errors.New("n != DataSize"))
	}
	_, err = file.Seek(-int64(n), io.SeekCurrent)
	if err != nil {
		panic(err)
	}

	if r.Method != http.MethodPost {
		http.Error(w, "not allowed", http.StatusMethodNotAllowed)
		return
	}

	r.Body = http.MaxBytesReader(w, r.Body, DataSize)
	defer r.Body.Close()

	receivedData := make([]byte, DataSize)
	n, err = io.ReadFull(r.Body, receivedData)
	if err != nil {
		http.Error(w, "read failed", http.StatusBadRequest)
		return
	}
	if n != DataSize {
		http.Error(w, "read size failed", http.StatusBadRequest)
		return
	}

	_, err = file.Write(receivedData)
	if err != nil {
		panic(err)
	}

	w.Header().Set("Content-Type", "application/octet-stream")
	w.Header().Set("Content-Length", "1048576")
	_, err = w.Write(buffer)
	if err != nil {
		log.Printf("write failed: %v", err)
	}
	cnt += 1
	if cnt == TotalRounds {
		os.Exit(0)
	}
}

func main() {
	runtime.GOMAXPROCS(2)
	debug.SetMemoryLimit(10485760)
	var err error
	file, err = os.OpenFile("/space/file", os.O_RDWR, 0644)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	http.HandleFunc(EndpointPath, exchangeHandler)

	log.Printf("Listening %s", Port)
	if err := http.ListenAndServe(Port, nil); err != nil {
		log.Fatalf("Start failed: %v", err)
	}
}
```

需要注意的是：

- Go 默认编译的二进制很大，除了加上 `-ldflags "-s -w"` 以外，还需要用 `upx` 再压缩一下，才能满足上传大小约束。
- 运行环境的 PID 数量和内存有限制，因此需要用 `runtime.GOMAXPROCS(2)` 和 `debug.SetMemoryLimit(10485760)` 压一下运行时的线程和内存使用。

### Flag 2

Flag 2 要复杂一些。**一个核心的问题是：怎么在传输到新文件的过程中把旧文件部分区域释放出来**？这可以用 [`fallocate(2)`](https://www.man7.org/linux/man-pages/man2/fallocate.2.html) 完成。在 Golang 中对应的是：

```golang
err = syscall.Fallocate(int(file.Fd()), 0x1|0x2, curr, DataSize)
```

其中 `0x1|0x2` 对应 `FALLOC_FL_KEEP_SIZE | FALLOC_FL_PUNCH_HOLE`。

Alice:

```go
// server.go Alice
package main

import (
	"errors"
	"io"
	"log"
	"net/http"
	"os"
	"runtime"
	"runtime/debug"
	"syscall"
)

const (
	DataSize     = 1 << 20 // 1MB
	Port         = ":8080"
	EndpointPath = "/exchange"
	Half         = 64
)

var file *os.File
var file1 *os.File
var file2 *os.File
var counter int

func exchangeHandler(w http.ResponseWriter, r *http.Request) {
	buffer := make([]byte, DataSize)
	n, err := file.Read(buffer)
	if err != nil {
		panic(err)
	}
	if n != DataSize {
		panic(errors.New("n != DataSize"))
	}
	_, err = file.Seek(-int64(n), io.SeekCurrent)
	if err != nil {
		panic(err)
	}
	curr, err := file.Seek(0, io.SeekCurrent)
	if err != nil {
		panic(err)
	}
	err = syscall.Fallocate(int(file.Fd()), 0x1|0x2, curr, DataSize)
	if err != nil {
		panic(err)
	}
	_, err = file.Seek(int64(n), io.SeekCurrent)
	if err != nil {
		panic(err)
	}
	if r.Method != http.MethodPost {
		http.Error(w, "not allowed", http.StatusMethodNotAllowed)
		return
	}

	r.Body = http.MaxBytesReader(w, r.Body, DataSize)
	defer r.Body.Close()

	receivedData := make([]byte, DataSize)
	n, err = io.ReadFull(r.Body, receivedData)
	if err != nil {
		http.Error(w, "read failed", http.StatusBadRequest)
		return
	}
	if n != DataSize {
		http.Error(w, "read size failed", http.StatusBadRequest)
		return
	}

	if counter < Half {
		_, err = file1.Write(receivedData)
	} else {
		_, err = file2.Write(receivedData)
	}
	if err != nil {
		panic(err)
	}
	counter++

	w.Header().Set("Content-Type", "application/octet-stream")
	w.Header().Set("Content-Length", "1048576") // 1MB = 1048576 字节
	_, err = w.Write(buffer)
	if err != nil {
		log.Printf("write failed: %v", err)
	}
	if counter == Half*2 {
		os.Exit(0)
	}
}

func main() {
	runtime.GOMAXPROCS(2)
	debug.SetMemoryLimit(10485760)

	var err error
	file1, err = os.Create("/space/file1")
	if err != nil {
		panic(err)
	}
	defer file1.Close()
	file1.Truncate(DataSize * Half)
	file2, err = os.Create("/space/file2")
	if err != nil {
		panic(err)
	}
	defer file2.Close()
	file2.Truncate(DataSize * Half)

	file, err = os.OpenFile("/space/file", os.O_RDWR, 0644)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	http.HandleFunc(EndpointPath, exchangeHandler)

	log.Printf("Listening %s", Port)
	if err := http.ListenAndServe(Port, nil); err != nil {
		log.Fatalf("Start failed: %v", err)
	}
}
```

Bob:

```golang
// client.go Bob
package main

import (
	"bytes"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"runtime"
	"runtime/debug"
	"syscall"
	"time"
)

const (
	DataSize    = 1 << 20 // 1MB
	Half        = 32 * 2
	TotalRounds = Half * 2
	ServerURL   = "http://127.0.0.1:8080/exchange"
)

func main() {
	runtime.GOMAXPROCS(2)
	debug.SetMemoryLimit(10485760)

	client := &http.Client{}
	file1, err := os.OpenFile("/space/file1", os.O_RDWR, 0644)
	if err != nil {
		panic(err)
	}
	defer file1.Close()
	file2, err := os.OpenFile("/space/file2", os.O_RDWR, 0644)
	if err != nil {
		panic(err)
	}
	defer file2.Close()
	file, err := os.Create("/space/file")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	file.Truncate(DataSize * TotalRounds)

	time.Sleep(1 * time.Second)

	buffer := make([]byte, DataSize)

	var n int
	for i := 1; i <= TotalRounds; i++ {
		if i <= Half {
			n, err = file1.Read(buffer)
		} else {
			n, err = file2.Read(buffer)
		}
		if err != nil {
			panic(err)
		}
		if n != DataSize {
			log.Fatalf("%d: read size not match", i)
		}
		if i <= Half {
			_, err = file1.Seek(-int64(n), io.SeekCurrent)
			curr, err := file1.Seek(0, io.SeekCurrent)
			if err != nil {
				panic(err)
			}
			err = syscall.Fallocate(int(file1.Fd()), 0x1|0x2, curr, DataSize)
			if err != nil {
				panic(err)
			}
			_, err = file1.Seek(int64(n), io.SeekCurrent)
			if err != nil {
				panic(err)
			}
		} else {
			_, err = file2.Seek(-int64(n), io.SeekCurrent)
			curr, err := file2.Seek(0, io.SeekCurrent)
			if err != nil {
				panic(err)
			}
			err = syscall.Fallocate(int(file2.Fd()), 0x1|0x2, curr, DataSize)
			if err != nil {
				panic(err)
			}
			_, err = file2.Seek(int64(n), io.SeekCurrent)
			if err != nil {
				panic(err)
			}
		}
		req, err := http.NewRequest("POST", ServerURL, bytes.NewReader(buffer))
		if err != nil {
			log.Fatalf("%d new request failed: %v", i, err)
		}
		req.Header.Set("Content-Type", "application/octet-stream")
		req.ContentLength = DataSize

		resp, err := client.Do(req)
		if err != nil {
			log.Fatalf("%d send failed: %v", i, err)
		}

		responseData := make([]byte, DataSize)
		n, err = io.ReadFull(resp.Body, responseData)
		resp.Body.Close()
		if err != nil {
			log.Fatalf("%d read failed: %v", i, err)
		}
		if n != DataSize {
			log.Fatalf("%d read size not match", i)
		}

		_, err = file.Write(responseData)
		if err != nil {
			panic(err)
		}

		fmt.Printf("%d succeed.\n", i)
	}

	fmt.Println("Done!")
}
```

## 出题思路提供者的话

本节作者：[@zzh1996](https://github.com/zzh1996)

这道题的出题思路是我提供的。这道题的出题灵感来源于，我有一台服务器上面有两块很大的盘，里面分别存放了不同的数据。我发现第一块盘快满了，而且磁盘占用增长的很快；而第二块盘更大，剩余空间很多，并且内容增长缓慢。我想着，这不是两个磁盘的内容互换一下，就解决问题了么？但是想了想，在不借助其他存储空间的前提下，这玩意就跟华容道一样，真是让人头秃。

一开始我是想把这题出成两个 tmpfs 中分别有一大堆文件，有复杂的目录结构。后来我想，只要选手可以实现文件分割和合并这两个基本操作，其实多少个文件都没区别。所以跟 [taoky](https://github.com/taoky) 讨论了之后这题就出成了现在的两个小问。其中第一个小问只要直接覆盖内容即可，而第二小问必须要切割和合并文件。

虽然 Linux 的文件系统提供了「打洞」这种能力，但是其实第二问不打洞也能解出来，只要 `truncate` 就可以了。`truncate` 可以用来把文件的尾部给缩小，所以你可以通过让一个文件末尾缩小、另一个文件末尾增大的方式来实现文件的合并和拆分。有人会问，这样文件内容不就逆序了么？比如一个文件是 01234，另一个文件是 56789，这种一边缩小一边增大的方式只能搞出来 0123498765。要解决这个问题只要在文件内部对调一下就行了。

说到这个，我之前还遇到一个场景，让我想把文件进行原地切分和合并。就是，把一个大文件从一个服务器传输到另一个服务器。你会发现 rsync 不支持多线程传输，而 rclone 支持多线程，却只能对多个文件进行多线程传输，一个文件只能单线程。所以在多线程传输能显著加快传输速度的网络环境下，想尽快传输单个大文件，也只能切分然后合并了。有人可能会问为什么不用 HTTP 和 FTP，然后用一些多线程下载工具？那当然是因为文件路径的特殊字符和文件 Metadata 的问题。当然，你也可以使用 HTTP 多线程下载，然后用其他工具修复 Metadata，也很麻烦。

最后，Linux 是不是根本没有办法原地（不要进行任何复制地）切分和合并文件？
