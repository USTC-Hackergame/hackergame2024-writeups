# Node.js is Web Scale

题解作者：[taoky](https://github.com/taoky)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：web

- 题目分值：200

小 Q 最近在写 Node.js，需要一个键值数据库来存储数据。

<del>众所周知</del>，其他的数据库无论如何都需要 write to disk，所以它们 don't scale。直接写到 `/dev/null` 嘛，虽然性能很好，但是好像就拿不到写入的数据了。基于这个想法，小 Q 利用最新最热的<del>还没跑路的</del>大语言模型，生成了一段内存数据库的 Node.js 代码，绝对 web scale！

注：

- 如果你在好奇标题是什么意思，可以搜索一个标题叫 "Mongo DB Is Web Scale" 的视频（虽然与本题解法无关）。

- flag 在 `/flag` 文件中。

- 点击下面的「打开/下载题目」按钮会为你创建一个独立的题目环境，有效时间一小时。如果环境遇到问题，可以 [关闭环境](https://chal03-manager.hack-challenge.lug.ustc.edu.cn/docker-manager/stop?{token}) 后再试。

[打开/下载题目](https://chal03-manager.hack-challenge.lug.ustc.edu.cn/docker-manager/start?{token})

## 题解

这是一道简单的 Node.js 原型链污染的题目。JavaScript 语言的初学者可能很难意识到的是，JavaScript 中 `{}` 不仅仅是一个字典/哈希表，它事实上是个**对象**，因此它有一些意料之外的属性。原型链污染就和 [`Object.prototype.__proto__`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto) 这个属性有关。从效果上讲，通过 `__proto__` 属性，可以给对象的的属性设置默认值：

```console
$ node
Welcome to Node.js v23.1.0.
Type ".help" for more information.
> a = {}
{}
> a.__proto__.test = 114
114
> b = {}
{}
> b.test
114
```

而且可能让其他语言的程序员感到反直觉的是，这样也是可以的：

```console
$ node
Welcome to Node.js v23.1.0.
Type ".help" for more information.
> a = {}
{}
> a["__proto__"]["test"] = 114
114
> b = {}
{}
> b["test"]
114
```

如果用户可以任意控制这类赋值的话，就构成了原型链污染漏洞。本题也符合这个条件。观察 `/set`：

```js
const keys = key.split(".");
let current = store;

for (let i = 0; i < keys.length - 1; i++) {
  const key = keys[i];
  if (!current[key]) {
    current[key] = {};
  }
  current = current[key];
}

// Set the value at the last key
current[keys[keys.length - 1]] = value;
```

可以发现它会将用户的 key 输入按 `.` 分割，然后一个循环操作 `current`。如果 `key` 是 `__proto__.a` 的话，结果就是 `current["__proto__"]["a"]` 被设定上了用户给定的值。而本题中，执行命令参考的表长这样：

```js
let cmds = {
  getsource: "cat server.js",
  test: "echo 'hello, world!'",
};
```

这是一个对象，因此会被原型链污染问题影响。接下来怎么做应该不用多介绍了。

JavaScript 中真正的「字典」是 [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)。JS 引擎可能会实现成哈希表或者搜索树结构。

此外，`JSON.parse()` 函数可以[正确处理 `__proto__` 作为键的情况](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#object_literal_syntax_vs._json)。但是对 `JSON.parse()` 的输出做处理时，程序员仍然需要特别注意。
