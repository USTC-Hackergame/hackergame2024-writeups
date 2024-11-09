# -*- coding: utf-8 -*-

import requests
import urllib
import re

# 提示用户输入实例 ID 和 token，发送 GET 请求获取 COOKIE
entry = input("请输入您的实例ID(chal01-到点号之间的字符串): ")
token = input("请输入您的 token: ")
url = f"https://chal01-{entry}.hack-challenge.lug.ustc.edu.cn:8443/"
f = {'token': token}
token = urllib.parse.urlencode(f)
url_get = f"{url}?{token}"
response_get = requests.get(url_get)
cookie = response_get.history[0].headers.get('Set-Cookie')

# 发送请求到 /list 页面，获取所有链接
headers = {'Cookie': cookie}
response_list = requests.get(url + 'list', headers=headers)
links = re.findall(r'href="(.*?)"', response_list.text)

# 逐一访问每个链接，检查是否包含 flag{xxx}
for idx, link in enumerate(links, 1):
    print(f"正在扫描第 {idx} 个页面...")
    response_page = requests.get(url + link, headers=headers)
    match = re.search(r'flag\{.*?\}', response_page.text)
    if match:
        print(f"找到 flag: {match.group(0)}")
        break