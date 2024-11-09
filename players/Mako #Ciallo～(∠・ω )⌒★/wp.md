# Mako #Ciallo～(∠・ω< )⌒★ writeup
- 不知名参赛大一新生 - [My Github](https://github.com/x-spy)
- 时间有限，只写了一些有意思的题目

## 比大小王
__~~致敬传奇CTF靶场小猿口算~~__

直接用Selenium模拟浏览器，接着读取js内容
``` Python
try:
    driver.get("http://202.38.93.141:12122/")
    time.sleep(5) # 为了输入token

    state_values = driver.execute_script("return state.values")

    for pair in state_values:
        print(pair)
        answer = "<" if pair[0] < pair[1] else ">"
        driver.execute_script("state.inputs.push(arguments[0])", answer)
        time.sleep(0.00001)


    driver.execute_script("submit(state.inputs)")
```
经过测试，最短时间2.2秒左右，不然会提示时空穿越

## 不宽的宽字符
这道题的难度在于我们很少了解Windows API中的`MultiByteToWideChar`

自己编译并测试几次输入后发现：
1. 如果输入ASCII，转换的结果会是该字符的ASCII码 + 00h，所以读到该字符后会停止
2. 如果输入Unicode，转换的结果会是该Unicode编码的倒序
3. 如果输入UTF-8，会将该字符转换为对应的Unicode，然后倒序

所以解决方法就是：

构建对应`Z:\theflag` 的ASCII码 每两个字符反转后的payload，最后加上一个空格，防止后面添加的字符被解析

## PowerfulShell
题目规定了无法使用的字符：`FORBIDDEN_CHARS="'\";,.%^*?!@#%^&()><\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0"`

经过一段时间的搜寻，我们发现：
1. `$_` 代表 `input`
2. `~` 代表当前的目录 `/players`
3. 我们使用 `${_:m:n}` 可以使用`$_`以索引`m`开始的`n`个字节

第一个问题是，因为~ 并不能使用`${~:m:n}` 取的其中的某个字符，并且我们也不能export一个环境变量。

经过一段时间的尝试，我们可以发现可以将值赋值给`__` 或者`___`等任意长度的下划线，所以 __=~后，我们就可以通过`${__:m:n}`的方式构造包含`/players`的任何字符串，这其中当然就包括`ls /`

现在我们的目标是访问`/flag`文件，那么我们自然要构造出`cat /flag`
1. 使用`___=ls /`的方式，将`ls /`返回的字符保存在`___`中
2. 使用`${___:m:n}`的方式就可以访问`___`中的任何字符，所以我们可以使用`etc`中的`c`，`/players`中的`a`和`/`，`input`中的`t`，以及`flag`本身，构造出`cat /flag`

小提示：`ls /` 输出的第一个目录`bin`的第一个字符`b`的索引是0，但下一个目录的的第一个字母索引是4，因为`bin`后面有一个换行符

## 惜字如金 3.0
### Flag 1
直接补全代码就能得到结果

### Flag 2
由于完全不懂数学，所以在这里使用了无脑解法：爆破 （所以理所当然的没做出来Flag 3）

#### 一、爆破理论
知周所众，如果某一行经过计算后与保存的文件名不对应，会返回服务器计算得出的该行的hash，而这个hash仅与crc的poly有关，而当我们阅读代码后发现poly为49位且最高位和最低位都是B

因此，我们的爆破范围只有0 -> 2**48-1

#### 二、抛弃 Python
将第七行改为一个单字符`a`，上传，服务器返回`a`的hash为`5f11989062ad`

尝试使用原代码 + for循环爆破，发现速度很慢（一秒只能验证100 000个值），因此，我决定使用高效的golang重写一份并行计算的爆破工具

#### 三、抛弃 CPU
在golang中，实现了下面的代码：
``` Go
func crc(input []byte, polyMiddle uint64) uint64 {
	var flip uint64
	polyDegree := 48
	for i := 0; i < polyDegree; i++ {
		flip = (flip << 1) | (polyMiddle & 1)
		polyMiddle >>= 1
	}
	
	digest := uint64((1 << polyDegree) - 1)
	for _, b := range input {
		digest ^= uint64(b)
		for j := 0; j < 8; j++ {
			if digest&1 == 1 {
				digest = (digest >> 1) ^ flip
			} else {
				digest >>= 1
			}
		}
	}

	return digest ^ uint64((1<<polyDegree)-1)
}

func hash(input []byte, polyMiddle uint64) []byte {
	digest := crc(input, polyMiddle)
	u2, u1, u0 := uint64(0xdbeEaed4cF43), uint64(0xFDFECeBdeeD9), uint64(0xB7E85A4E5Dcd)
	digest = (digest*(digest*u2+u1) + u0) % (1 << 48)
	hashBytes := make([]byte, 6)
	binary.LittleEndian.PutUint16(hashBytes[0:], uint16(digest))
	binary.LittleEndian.PutUint32(hashBytes[2:], uint32(digest>>16))
	return hashBytes
}

func worker(id int, tasks chan uint64, expectedHash []byte, wg *sync.WaitGroup, found chan string) {
	defer wg.Done()
	for start := range tasks {
		fmt.Printf("Checking: %d\n", id, start)
		end := start + 10000000
		for i := start; i < end; i++ {
			if bytes.Equal(expectedHash, hash([]byte{'a'}, i)) {
				found <- fmt.Sprintf("%047b", i)
				return
			}
		}
	}
}

func start(startNum uint64) {
	expectedHash := []byte{0x5f, 0x11, 0x98, 0x90, 0x62, 0xad}
	var wg sync.WaitGroup
	found := make(chan string, 1)
	tasks := make(chan uint64, 32)
	maxNum := uint64(140737488355327)

	for i := 0; i < 64; i++ {
		wg.Add(1)
		go worker(i, tasks, expectedHash, &wg, found)
	}

	go func() {
		for start := startNum; start < maxNum; start += 10000000 {
			select {
			case tasks <- start:
			case poly := <-found:
				close(tasks)
				fmt.Printf("Found poly: %s\n", poly)
				panic("Found")
				return
			}
		}
		close(tasks)
	}()

	wg.Wait()
	close(found)
}
```
经实验，此代码在14900K上以400w+整机功耗运行仅需6天即可跑出结果，这样的效率会使我损失高达一顿KFC的电费

所以：

#### 四、拥抱CUDA
经过对14900K缩缸问题一段时间的思考，我决定让4090担起爆破的重任，于是便有了下面的代码：
``` C
#include <stdio.h>
#include <stdint.h>
#include <cuda_runtime.h>

struct Result {
    int found;
    uint64_t poly;
};

__device__ uint64_t crc(uint8_t* input, int input_length, uint64_t bpoly) {
    uint64_t flip = 0;
    int polyDegree = 48;
    uint64_t poly = (1ULL << polyDegree) | (bpoly << 1) | 1;
    for (int i = 0; i < polyDegree; i++) {
        flip = (flip << 1) | ((poly >> i) & 1);
    }

    uint64_t digest = (1ULL << polyDegree) - 1;

    for (int idx = 0; idx < input_length; idx++) {
        uint8_t b = input[idx];
        digest ^= (uint64_t)b;

        for (int j = 0; j < 8; j++) {
            digest = (digest >> 1) ^ ((digest & 1) ? flip : 0);
        }
    }

    return digest ^ ((1ULL << polyDegree) - 1);
}

__device__ void hash(uint8_t* input, int input_length, uint64_t bpoly, uint8_t* hashBytes) {
    uint64_t digest = crc(input, input_length, bpoly);
    uint64_t u2 = 0xdbeEaed4cF43ULL;
    uint64_t u1 = 0xFDFECeBdeeD9ULL;
    uint64_t u0 = 0xB7E85A4E5DcdULL;
    digest = (digest * (digest * u2 + u1) + u0) % (1ULL << 48);

    for (int i = 0; i < 6; i++) {
        hashBytes[i] = (uint8_t)((digest >> (8 * i)) & 0xFF);
    }
}

__global__ void searchKernel(uint64_t startNum, uint64_t batchSize, uint8_t* expectedHash_d, Result* result_d) {
    uint64_t idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= batchSize) return;

    uint64_t i = startNum + idx;
    uint8_t input[1] = { 'a' };
    uint8_t hashBytes[6];
    hash(input, 1, i, hashBytes);

    bool match = true;
    for (int k = 0; k < 6; k++) {
        if (hashBytes[k] != expectedHash_d[k]) {
            match = false;
            break;
        }
    }

    if (match) {
        if (atomicCAS(&(result_d->found), 0, 1) == 0) {
            result_d->poly = i;
        }
    }
}
```

当`batchSize = 1 000 000 000` 时，4090仅需不到15分钟就能遍历并校验`140737488355328`种可能性

最终，它给出了答案：`BbbbBbbBBbbBbBbbbbbBbBBBbBBbbbBBBbBBbbBBbbBBBbB`

## 无法获得的秘密
VNC server 禁用了剪贴板，我们能够怎样通过视频获得足够的信息？

那当然是找到一个`能够纠错 有较高信息密度 通过图像方式传输信息`的方法

所以我很自然的想到了QR Code

使用Python的pyautogui库模拟键盘，向服务器写入一个tiny-qr.html，接着手动复制文本进去并逐张截图，最后用一个脚本自动拼接到一起，就能拿到最终的文件

> tiny-qr.html 来源：[GitHub](https://github.com/six-two/qr.html/blob/main/tiny-qr.html)

