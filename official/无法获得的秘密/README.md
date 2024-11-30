# 无法获得的秘密

题解作者：[RTXUX](https://github.com/RTXUX)

出题人、验题人、文案设计等：见 [Hackergame 2024 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：general

- 题目分值：250

小 A 有一台被重重限制的计算机，不仅没有联网，而且你只能通过 VNC 使用键鼠输入，看视频输出。上面有个秘密文件位于 `/secret`，你能帮他把文件**丝毫不差地**带出来吗？

[打开/下载题目](http://202.38.93.141:12010/?token={token})

## 题解

这题主要是通过鼠标、键盘输入和视频输出将一个文件带出来，最简单的容易想到的方法就是将文件编码成图片，然后截图或者录视频解码。注意到环境中有浏览器，因此可以用 canvas 和 js 实现一个简单的灰度编码算法。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script type="text/javascript" src="index.js"></script>
</head>
<body style="margin: 0;">
<div>
    <input type="file" id="file-input">
    <button id="btn-run">run</button>
</div>
<div>
    <canvas width="1024px" height="512px" id="canvas-data"></canvas>
</div>
</body>
</html>
```

```js
const width = 1024;
const height = 512;
document.addEventListener("DOMContentLoaded", (e) => {
    const fileInput = document.getElementById("file-input");
    const btnRun = document.getElementById("btn-run");
    btnRun.addEventListener("click", (e) => {
        if (fileInput.files.length === 0) {
            console.log("No file selected");
            return;
        }

        const reader = new FileReader();
        reader.onload = () => {
            const buffer = reader.result;
            const canvas = document.getElementById("canvas-data");
            const ctx = canvas.getContext("2d")
            const imageData = ctx.getImageData(0, 0, width, height);
            const data = imageData.data;
            const fileData = new Uint8Array(buffer);
            for (let i = 0; i < fileData.length; ++i) {
                const dataOffset = i * 4;
                data[dataOffset] = fileData[i];
                data[dataOffset + 1] = fileData[i];
                data[dataOffset + 2] = fileData[i];
                data[dataOffset + 3] = 255;
            }
            ctx.putImageData(imageData, 0, 0);
        }

        reader.readAsArrayBuffer(fileInput.files[0]);
    })
})
```

将以上两段代码分别保存为 `index.html` 和 `index.js`，用浏览器打开 `index.html`，点击按钮选择文件，选中 `/secret` 并点击 `Run` 按钮，就可以看到文件内容被编码为一幅灰度图显示了出来，截图并精细裁切后，使用一段简单的 Python 代码即可解码。

```python
from PIL import Image
import numpy as np

if __name__ == "__main__":
    IMG_PATH = ""
    img = Image.open(IMG_PATH)
    img.load()
    data = np.asarray(img, dtype=np.uint8)[:, :, 0]
    data = data.flatten()
    with open(IMG_PATH.replace(".png", ".bin"), "wb") as f:
        f.write(data)
```

然而，在题目提供的 noVNC 中直接执行上述方案并不可行，原因在于 noVNC 使用有损编码传输图像，而上面的编码算法没有任何冗余，很容易就出现某个字节差 1 的情况。这里可以使用更高级的带纠错的编码算法，也可以使用一些小技巧，比如编写一个小程序将 WebSocket 转为 TCP：

```python
import asyncio
import websockets

COOKIE=open("cookie").read().strip()
SERVER_IP = ""

async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    async with websockets.connect(f"ws://{SERVER_IP}:12010/connect", extra_headers=[("Cookie", COOKIE)]) as ws_conn:
        async def client_to_server():
            try:
                while True:
                    data = await reader.read(4096)
                    if not data:
                        break
                    await ws_conn.send(data)
            except websockets.exceptions.ConnectionClosed:
                return
            except asyncio.CancelledError:
                return
            finally:
                await ws_conn.close()

        async def server_to_client():
            try:
                while True:
                    data = await ws_conn.recv()
                    if not data:
                        break
                    writer.write(data)
                    await writer.drain()
            except websockets.exceptions.ConnectionClosed:
                return
            except asyncio.CancelledError:
                return
            finally:
                writer.close()

        await asyncio.gather(client_to_server(), server_to_client())

async def main():
    server = await asyncio.start_server(handler, "127.0.0.1", 12010)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
```

这样就可以在本机使用其他 VNC 客户端来连接题目环境，从而将图像传输调整为无损编码，即可执行上述方案。解码得到文件后可以 `sha256sum` 一下确认与题目环境提供的一致，上传该文件到题目网页即可得到 flag。

---

## 附注

### 出题思路提供者的话

本节作者：[@zzh1996](https://github.com/zzh1996)

这道题是我提供的出题思路，感谢 [RTXUX](https://github.com/RTXUX) 的实现。

我想出这道题是因为 2017 年我刚入门 CTF 的时候，有一些在线教学平台，就会提供一个类似这道题一样的 Windows 桌面环境，允许你在里面解题。当时我看到这个环境中有一个文件夹，里面全是整理好的各种 CTF 工具，我当时就特别想把这些工具都下载下来。可惜我跟这个环境唯一的交互方式就是键盘鼠标以及屏幕画面。

我当时花了很多时间写了一个能够把文件内容显示成动态变化的类似二维码的东西的网页，还有哈希校验。我再用 Python 来不断截图并且解析里面的数据，逐渐组装出来整个文件。我用一个 VBS 脚本来模拟键盘按键把网页源代码输入到了远程环境。

最后，当我终于得到了一个哈希完全匹配的压缩包的时候，我特别开心。

我当年的源代码在 [这里](https://github.com/zzh1996/ScreenTransfer)。当时我写代码的风格比较糟糕，所以随便看看就好。

当然，正如我买的很多 Steam 游戏买了之后就从来没有玩过一样，我好不容易搞出来的这个 CTF 工具集也从来没真的用过。

### 在 Wayland 以及浏览器下的输入自动化

本节作者：[@taoky](https://github.com/taoky)

相信大家在做题的时候可以发现，在 Windows/X11 (With XTEST extension) 和 macOS 下要做输入自动化都非常简单，实在不行让 LLM 生成出来的代码应该也都是能用的。

但是 Wayland 的情况就有点蛋疼了，我在比赛前放弃了验证这道题也是因为这个原因：

- Xwayland 似乎对调用 XTEST 的程序（比如说 `xdotool`）有一些特殊处理，但是看起来有 bug 还不能用。
- 对于支持 [`virtual-keyboard`](https://wayland.app/protocols/virtual-keyboard-unstable-v1) 协议的混成器，可以使用类似 [wtype](https://github.com/atx/wtype) 的工具。
- GNOME 和 KDE 可以使用 XDG Desktop Portal 中的 [Remote Desktop Portal](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.RemoteDesktop.html) 实现自动化输入。但是我找了一圈，没有找到成熟的有关工具。
- 实在不行，可以用 kernel 的 uinput 内核模块。

以下给出我在比赛时写的使用 XDG Desktop Portal 实现自动化输入的 Rust 代码，在 GNOME 47 下测试无问题。每次运行的时候会弹一个是否允许远程控制的框，允许即可。

https://github.com/user-attachments/assets/6dad242e-2ed3-4c0e-b7ab-34bd250c90ed

[gnome-wayland-portal-autokeyboard.mp4](assets/gnome-wayland-portal-autokeyboard.mp4)

```rust
// [dependencies]
// ashpd = "0.10.2"
// keycode = "0.4.0"
// tokio = { version = "1.41.1", features = ["full"] }
use std::{fs::File, io::Read, process::exit, time::Duration};

use ashpd::desktop::{
    remote_desktop::{DeviceType, KeyState, RemoteDesktop},
    PersistMode, Session,
};
use keycode::{KeyMap, KeyMappingId};

async fn press_key(
    proxy: &RemoteDesktop<'_>,
    session: &Session<'_, RemoteDesktop<'_>>,
    ch: char,
) -> ashpd::Result<()> {
    let shiftkeycode = KeyMap::from(KeyMappingId::ShiftLeft).evdev as i32;
    let kid = match ch.to_ascii_lowercase() {
        'a' => KeyMappingId::UsA,
        'b' => KeyMappingId::UsB,
        'c' => KeyMappingId::UsC,
        'd' => KeyMappingId::UsD,
        'e' => KeyMappingId::UsE,
        'f' => KeyMappingId::UsF,
        'g' => KeyMappingId::UsG,
        'h' => KeyMappingId::UsH,
        'i' => KeyMappingId::UsI,
        'j' => KeyMappingId::UsJ,
        'k' => KeyMappingId::UsK,
        'l' => KeyMappingId::UsL,
        'm' => KeyMappingId::UsM,
        'n' => KeyMappingId::UsN,
        'o' => KeyMappingId::UsO,
        'p' => KeyMappingId::UsP,
        'q' => KeyMappingId::UsQ,
        'r' => KeyMappingId::UsR,
        's' => KeyMappingId::UsS,
        't' => KeyMappingId::UsT,
        'u' => KeyMappingId::UsU,
        'v' => KeyMappingId::UsV,
        'w' => KeyMappingId::UsW,
        'x' => KeyMappingId::UsX,
        'y' => KeyMappingId::UsY,
        'z' => KeyMappingId::UsZ,
        '0' | ')' => KeyMappingId::Digit0,
        '1' | '!' => KeyMappingId::Digit1,
        '2' | '@' => KeyMappingId::Digit2,
        '3' | '#' => KeyMappingId::Digit3,
        '4' | '$' => KeyMappingId::Digit4,
        '5' | '%' => KeyMappingId::Digit5,
        '6' | '^' => KeyMappingId::Digit6,
        '7' | '&' => KeyMappingId::Digit7,
        '8' | '*' => KeyMappingId::Digit8,
        '9' | '(' => KeyMappingId::Digit9,
        ' ' => KeyMappingId::Space,
        '\n' => KeyMappingId::Enter,
        '\t' => KeyMappingId::Tab,
        '`' | '~' => KeyMappingId::Backquote,
        '-' | '_' => KeyMappingId::Minus,
        '=' | '+' => KeyMappingId::Equal,
        '[' | '{' => KeyMappingId::BracketLeft,
        ']' | '}' => KeyMappingId::BracketRight,
        '\\' | '|' => KeyMappingId::Backslash,
        ';' | ':' => KeyMappingId::Semicolon,
        '\'' | '"' => KeyMappingId::Quote,
        ',' | '<' => KeyMappingId::Comma,
        '.' | '>' => KeyMappingId::Period,
        '/' | '?' => KeyMappingId::Slash,
        // "Super" => KeyMappingId::Super,
        _ => unimplemented!(),
    };
    let key = KeyMap::from(kid);
    let keycode = key.evdev as i32;
    let shift = ch.is_uppercase() || "~!@#$%^&*()_+{}|:\"<>?".contains(ch);
    if shift {
        proxy
            .notify_keyboard_keycode(session, shiftkeycode, KeyState::Pressed)
            .await?;
    }
    proxy
        .notify_keyboard_keycode(session, keycode, KeyState::Pressed)
        .await?;
    proxy
        .notify_keyboard_keycode(session, keycode, KeyState::Released)
        .await?;
    if shift {
        proxy
            .notify_keyboard_keycode(session, shiftkeycode, KeyState::Released)
            .await?;
    }
    Ok(())
}

async fn run(buffer: Vec<u8>) -> ashpd::Result<()> {
    let proxy = RemoteDesktop::new().await?;
    let session = proxy.create_session().await?;
    proxy
        .select_devices(
            &session,
            DeviceType::Keyboard.into(),
            None,
            PersistMode::DoNot,
        )
        .await?;

    let response = proxy.start(&session, None).await?.response()?;
    println!("{:#?}", response.devices());

    println!("Wait 2s for you to focus...");
    std::thread::sleep(Duration::new(2, 0));

    for i in buffer {
        press_key(&proxy, &session, i as char).await?;
    }

    Ok(())
}

#[tokio::main]
async fn main() {
    let argv: Vec<_> = std::env::args().collect();
    if argv.len() <= 1 {
        println!("Usage: {} [filename]", argv[0]);
        exit(1);
    }
    let filename = &argv[1];
    let mut file = File::open(filename).unwrap();
    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer).unwrap();
    run(buffer).await.unwrap();
}
```

同样，在浏览器里面，利用 web console 也可以实现输入自动化，参考代码：

```python
with open("index.html") as f:
    contents = f.read()

contents = repr(contents)
# print(contents)

# Generated by LLM
output = f"""
const inputElement = document.getElementsByTagName("canvas")[0];
var x = {contents}

// Function to simulate typing a character
function simulateTyping(inputElement, char, delay) {{
    // Create synthetic events
    const keydownEvent = new KeyboardEvent('keydown', {{ key: char }});
    const keypressEvent = new KeyboardEvent('keypress', {{ key: char }});
    const keyupEvent = new KeyboardEvent('keyup', {{ key: char }});

    // Dispatch KeyboardEvent 'keydown'
    inputElement.dispatchEvent(keydownEvent);

    // Update the input field value (this is necessary since Chrome autocomplete might block the event)
    inputElement.value += char;

    // Dispatch KeyboardEvent 'keypress'
    inputElement.dispatchEvent(keypressEvent);

    // Dispatch KeyboardEvent 'keyup'
    inputElement.dispatchEvent(keyupEvent);
}}

// Function to simulate typing the entire string
function simulateTypingString(inputElement, text, typingDelay = 100) {{
    let delay = 0;

    for (let i = 0; i < text.length; i++) {{
        ((char, delay) => {{
            setTimeout(() => {{
                simulateTyping(inputElement, char);
            }}, delay);
        }})(text[i], delay);
        delay += typingDelay; // Introduce a delay between each keystroke
    }}
}}

// Call the function to simulate typing the string
simulateTypingString(inputElement, x, 5);  // 5ms delay between keypresses
"""

print(output)
```
