# 零知识数独

题解作者：[tl2cents](https://github.com/tl2cents)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：math

- 题目分值：数独高手（100）+ ZK 高手（150）+ 无解之谜（300）

一款全新的零知识数独！你已然是数独高手，也终将成为零知识证明大师！

> "If the proof is correct, then no other recognition is needed."
>
> — by Grigori Perelman

**[下载题目源代码](files/zksudoku.zip)**

[打开/下载题目](http://202.38.93.141:21112/?token={token})

### ZK 验证逻辑

本题的附件中给出了零知识数独电路，以及对应的 Groth16 验证密钥，服务端会使用它保存的谜题（Public Signals）和验证密钥（Verification Key）来验证提交的 Groth16 证明  `proof.json`。你的证明在本地需要满足：

```bash
$ snarkjs groth16 verify verification_key.json public.json proof.json
[INFO]  snarkJS: OK!
```

## 题解

这题数独约束的 circuit 参考 [Snarky Sudoku](https://github.com/nalinbhardwaj/snarky-sudoku) 改的，然后加了一个前端。前面两问基本没有任何难度，主要为第三问铺垫。

### 数独高手

简单的数独求解，所有逻辑都在前端，可以直接求解，或者进行前端数据篡改。flag 字符串经过混淆，直接搜 flag 应该是找不到的，Web 的做法和数独求解都是预期的。求解数独可以自己写一个深搜，也可以使用现成的库。笔者使用 SageMath 数独求解器：

```python
from sage.games.sudoku import Sudoku
puzzle_string = ".85..7.......43.....3.6.9.89..52...3.7.....46..........6...9.8...4.....9..2...6.."
sudoku_puzzle = Sudoku(puzzle_string)
solu = next(sudoku_puzzle.solve())
solu = [int(x) for x in solu.to_list()]
print(f"Solution: {solu}")
```

### ZK 高手

求解一个 expert 难度的 sudoku，然后利用 `snarkjs` 生成一个 Groth16 证明。这题主要让选手了解 circom 电路、snarkjs、零知识证明（groth16）的基本信息。使用命令行或者 snarkjs 的 API 都可以生成证明。细节可以参考 [generate_proof.js](./solution/generate_proof.js) 和 [GenrateProof.sh](./solution/hacker-circuits/GenrateProof.sh)。

### 无解之谜

这题主要涉及 circom 电路和对 r1cs 的理解，也是 ZK 在实际区块链应用上两个比较经典的漏洞，本题设计参考 [zk-bug-tracker](https://github.com/0xPARC/zk-bug-tracker) 中的在野漏洞 [1. Missing Bit Length Check](https://github.com/0xPARC/zk-bug-tracker#dark-forest-1) 和 [14. Assigned but not Constrained](https://github.com/0xPARC/zk-bug-tracker?tab=readme-ov-file#14-mimc-hash-assigned-but-not-constrained)。与传统编程语言不同的是，circom 电路编译生成的是一阶约束系统（Rank-1 Con­straint Sys­tem），其本质是一个方程组：

$$
Az \circ Bz = Cz
$$

其中 $z = 1 || x || w$ ， $x$ 向量是公开输入， $w$ 向量是秘密的 witness（约束系统的解）， $A, B, C$ 是约束系统形成的矩阵， $\circ$ 是 element-wise product。所谓一阶约束系统，是指约束系统的所有方程只能是 $\gamma = \alpha \times \beta$ 的形式，其中 $\alpha, \beta, \gamma$ 是约束系统的变量或者常数。因此高次的约束方程需要通过一阶约束系统的组合来实现，比如 $x \times x \times x = y$ 可以引入新的变量，通过两个约束 $x_2 = x \times x, y = x_2 \times x$ 来实现。对此有兴趣的读者可以参考 UC Berkeley 的 [ZKP MOOC](https://zk-learning.org/) 的 [Lecture 3](https://youtu.be/UpRSaG6iuks)。了解了这一点，再来看预期的漏洞点：

```circom
gt_zero_signals[i][j] <-- (solved_grid[i][j] > 0);
gt_zero_signals[i][j] === 1;
```

其中 `<--` 是极不安全的赋值操作，**它不会构成约束，因此 sudoku 中的解必须大于 0 的约束是不存在的**，赋值操作在最终的约束系统中其实可以当作公开输入，即 $x$ 向量。事实上读者可以尝试将上述赋值操作改成 `<==`，circom 会报错不支持大于二次的约束方程，这些非线性的比较操作在 circom 内表达是比较困难的。我们将在下文中提到 sudoku 输入必须小于等于 9 的约束是如何做到的。

如果我们在数独中填入 0，互异的约束 `SudokuChecker` 会不满足，考虑 circom 中的边界情况。circom 构建的约束系统是约束在有限域 $F_p$ 上的，虽然表示上没有负数，但还是存在负数的，即 $-1 = p - 1$。

```circom
template IsValidInput(){
  signal input value;
  signal output out;
  component upperBound = LessEqThan(4); 
  upperBound.in[0] <== value;
  upperBound.in[1] <== 9;
  out <== upperBound.out;
}
```

上述约束系统的 `LessEqThan` 会将输入 `value` 加上 $2^{4}$ 然后减去目标值 9 得到一个输出，这个输出必须是 4 + 1 bit 的数，然后根据最高位得到比较的结果，细节参考 [comparators.circom](https://github.com/iden3/circomlib/blob/master/circuits/comparators.circom#L89) 的实现。因此上述函数将 value 约束在 $F_p$ 的 $[-6, 9]$ 内，除了 0 之外，我们可供选择的数独字符集扩张到 15 个数。利用方法是，修改 `gt_zero_signals[i][j] <-- (solved_grid[i][j] > 0);` 为 `gt_zero_signals[i][j] <-- 1;` ，重新生成新的电路，从而伪造 proof。Range Proof 的设计必须考虑边界条件，否则会导致漏洞，或在像 [Snarky Sudoku](https://github.com/nalinbhardwaj/snarky-sudoku) 中一样上下都进行约束，这样取交集区间即可得到正确的 Range Proof。

EXP 和相关利用参考 [solution](./solution)。

### 其他

看到有选手讨论 ZK 环境搭建的问题，这里简单说明一下 circom 的环境问题。笔者本地是通过 `nvm` 安装的 nodejs，指定版本 22.10，然后通过 `npm` 安装 snarkjs。circom 环境不建议通过 `npm` 安装，可能导致无法编译赛题提供的 circom 电路，建议直接 clone 官方仓库：[Circom](https://github.com/iden3/circom)，然后使用 cargo 编译安装。