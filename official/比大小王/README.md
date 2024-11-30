# 比大小王

题解作者：[Hypercube](https://0x01.me/)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：web

- 题目分值：150

「小孩哥，你干了什么？竟然能一边原崩绝鸣舟，一边农瓦 CSGO。你不去做作业，我等如何排位上分？」

小孩哥不禁莞尔，淡然道：「很简单，做完口算题，拿下比大小王，家长不就让我玩游戏了？」

说罢，小孩哥的气息终于不再掩饰，一百道题，十秒速通。

在这场巅峰对决中，你能否逆风翻盘狙击小孩哥，捍卫我方尊严，成为新一代的「比大小王」？！

[打开/下载题目](http://202.38.93.141:12122/?token={token})

## 题解

### 题目代码逻辑

（可参考[网页源代码](src)阅读）

网页加载完毕后，前端会调用 `loadGame()` 函数向后端发送 `POST /game` 请求，获取 100 道题目的数字和开始时间。这个请求可以通过浏览器的开发者工具看到，其中的信息会被存入 `state` 变量中。

后端随机生成 100 道题，并按照收到请求的时间加 5 秒作为开始时间。这是为了确保在网络延迟较高的情况下，玩家仍然能看到比赛开始前的倒计时，而不会在收到题目时比赛已经开始。当然这也意味着玩家在比赛开始前已经拿到了题目，可以提前做题和提交，以负数时长完成比赛。后端如果检测到开始时间之前就提交答案，会回复 `检测到时空穿越，挑战失败！`。

后端会在回复题目数据的同时，利用 Flask 的 session 机制，将题目数据签名存储在 cookies 中。这样后端无需存储给出过的所有题目数据，等到玩家提交答案时，后端可以从 cookies 中读取题目的数字和开始时间用于验证，并且玩家无法篡改这些信息。

加载题目后，`updateCountdown()` 函数会根据当前时间和开始时间相差的秒数，播放倒计时动画。

比赛开始后，`updateTimer()` 函数会不断更新显示的时间，以及对手的进度。对手每 100 毫秒完成一道题，10 秒（100 题）后停止，显示挑战失败。

玩家每次选择小于或大于后，会调用 `chooseAnswer('<')` 或 `chooseAnswer('>')`，这个函数会用绿色或红色指示是否正确，持续 200 毫秒，这期间是不能操作的。200 毫秒之后，如果正确，会显示下一题，如果错误，会显示挑战失败。

玩家正确完成 100 题后，前端会调用 `submit(state.inputs)` 函数向后端发送 `POST /submit` 请求，提交玩家的 100 次选择（长度为 100 的数组，每个元素为 `'<'` 或 `'>'`），并显示回复。

后端会从 cookies 中读取题目的数字，验证签名，验证玩家的 100 次选择是正确的。这个过程中任何错误都会导致回复 `检测到异常提交`。如果验证通过，取决于当前时间和开始时间的差值，回复 `检测到时空穿越，挑战失败！` 或 `挑战成功！flag{...}` 或 `对手已完成，挑战失败！`。

### 难点

每次选择后会有 200 毫秒不能操作，即使完美操作也不可能在 10 秒内完成 100 题。需要修改代码去除这一限制，或者直接调用最终的提交函数。

如果挑战失败，前端不会发送最后的提交请求，因此难以在浏览器的开发者工具中看到提交请求的格式。需要修改代码真的实现 10 秒内完成 100 题来触发提交请求，或者阅读代码发现相关逻辑。

如果提交请求参数错误，后端会回复 `检测到异常提交`，但不会给出具体错误信息。

如果后端收到提交请求的时间不在比赛开始后 10 秒内，也就是说，不在后端收到获取题目数据请求后 5 到 15 秒这个范围内，会因为时间错误失败。如果选手的本地时钟和服务器有偏差，前端显示可能会有一些误导性。（出题人：这个确实没考虑到，我只考虑了要给足够长的窗口，避免网络不稳定的选手难以控制后端收到请求的时间，但没考虑前后端时间不一致的问题。如今真的还有设备不自动校准时间吗？）

### 解题思路 1：自动化操作，实现 10 秒内完成 100 题

在网页上按 F12 打开浏览器的开发者工具，在 Console（控制台）标签页运行以下代码，可以自动循环选择答案（注意不能用循环，必须用定时器，因为 JavaScript 是单线程的，循环运行一段代码会卡住所有其他定时器和交互逻辑）：

```javascript
function f() {
  // 只要还没到 100 分
  if (state.score1 < 100) {
    // 选择正确的答案
    if (state.value1 < state.value2) {
      chooseAnswer('<');
    } else {
      chooseAnswer('>');
    }
    // 1 毫秒后再次调用 f 函数
    setTimeout(f, 1);
  }
}

f();
```

执行后会发现，能够自动做题了，但速度追不上对手，必须移除每次 200 毫秒的等待时间，这是在 `chooseAnswer` 函数中实现的。要修改一个函数的代码，一般需要使用开发者工具的 override（覆盖）功能，但对于一些简单的情况，例如这道题，直接复制相关函数的代码，修改后粘贴到控制台中运行即可。

刷新网页，在控制台运行以下代码（`chooseAnswer` 函数除了注释的一行以外，完全没有修改）：

```javascript
function f() {
  // 只要还没到 100 分
  if (state.score1 < 100) {
    // 选择正确的答案
    if (state.value1 < state.value2) {
      chooseAnswer('<');
    } else {
      chooseAnswer('>');
    }
    // 1 毫秒后再次调用 f 函数
    setTimeout(f, 1);
  }
}

f();

function chooseAnswer(choice) {
  if (!state.allowInput) {
    return;
  }
  state.inputs.push(choice);
  let correct;
  if (state.value1 < state.value2 && choice === '<' || state.value1 > state.value2 && choice === '>') {
    correct = true;
    state.score1++;
    document.getElementById('answer').style.backgroundColor = '#5e5';
  } else {
    correct = false;
    document.getElementById('answer').style.backgroundColor = '#e55';
  }
  document.getElementById('answer').textContent = choice;
  document.getElementById('score1').textContent = state.score1;
  document.getElementById('progress1').style.width = `${state.score1}%`;
  state.allowInput = false;
  setTimeout(() => {
    if (state.score1 === 100) {
      submit(state.inputs);
    } else if (correct) {
      state.value1 = state.values[state.score1][0];
      state.value2 = state.values[state.score1][1];
      state.allowInput = true;
      document.getElementById('value1').textContent = state.value1;
      document.getElementById('value2').textContent = state.value2;
      document.getElementById('answer').textContent = '?';
      document.getElementById('answer').style.backgroundColor = '#fff';
    } else {
      state.allowInput = false;
      state.stopUpdate = true;
      document.getElementById('dialog').textContent = '你选错了，挑战失败！';
      document.getElementById('dialog').style.display = 'flex';
    }
  }, 1);  // 这里的 200 改成了 1
}
```

很快就可以完成 100 题，看到 flag。

### 解题思路 2：在比赛开始后 10 秒内直接发送提交请求

如果看明白了题目逻辑，可以发现 100 道题目的数字在 `state.values` 变量中，最终需要调用 `submit` 函数提交答案，所以可以等待比赛开始后，在控制台执行以下代码：

```javascript
submit(state.values.map(([v1,v2])=>v1<v2?'<':'>'))
```

它会把 `state.values` 的每一项映射为 `'<'` 或 `'>'`，得到一个长度为 100 的数组，作为参数调用 `submit` 函数。
