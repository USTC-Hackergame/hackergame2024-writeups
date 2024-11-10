import requests
import re

url = "http://202.38.93.141:13030/"
headers = {
    "Cookie": "travel_photo=CENSORED; session=CENSORED",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
}

score_pattern = r'本次测验总得分为 (\d*)。达到 100 分获取第二个 flag'

ans = {
    "q1": "3A204",
    "q2": 2682,
    "q3": "程序员的自我修养",
    "q4": 336,
    "q5": "6e90b6",
    "q6": 1833
}

# for i in range(1, 10000):
#     print(i)
#     ans["q4"] = i
#     res = requests.post(url, data = ans, headers = headers)
#     score = int(re.findall(score_pattern, res.text)[0])
#     if not score == 85:
#         break

for i in range(1, 10000):
    print(i)
    ans["q6"] = i
    res = requests.post(url, data = ans, headers = headers)
    score = int(re.findall(score_pattern, res.text)[0])
    if not score == 95:
        break