# -*- coding: utf-8 -*-

import requests
import urllib
import time

# 提示用户输入 token，发送 GET 请求获取初始的 SET-COOKIE
token = input("请输入您的 token: ")
f = {'token': token}
token = urllib.parse.urlencode(f)
url_get = f"http://202.38.93.141:12122/?{token}"
response_get = requests.get(url_get)
cookie_1 = response_get.history[0].headers.get('Set-Cookie')

# 发送 POST 请求到 /game，使用获取的 COOKIE，获取新的 SET-COOKIE和响应体 JSON
url_game = "http://202.38.93.141:12122/game"
headers = {
    'Cookie': cookie_1
}
response_game = requests.post(url_game, headers=headers, json={})
cookie_2 = response_game.headers.get('Set-Cookie')

# 对响应体 JSON 中的每一对 value 进行大小比较，保存结果
data = response_game.json()
inputs = []
for pair in data['values']:
    if pair[0] > pair[1]:
        inputs.append(">")
    else:
        inputs.append("<")

# 等待5s(避免"检测到时空穿越，挑战失败！"的提示)
time.sleep(5)

# 发送 POST 请求到 /submit，使用比较结果，输出响应体 JSON 中的 message
url_submit = "http://202.38.93.141:12122/submit"
headers['Cookie'] = cookie_2
response_submit = requests.post(url_submit, headers=headers, json={"inputs": inputs})
print(response_submit.json()['message'])