import libscrc
import random

def gsm3(data):
    return libscrc.gsm3(data) ^ 7

arr = [None for _ in range(8)]

for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/':
    arr[gsm3(c.encode())] = c.encode()
    if all(arr):
        break
print(arr)

d = dict()
for s in range(8):
    m = dict()
    for c in '0123456789':
        m[c] = gsm3(arr[s] + c.encode())
    d[s] = m

print(d)

def test_gsm3(s):
    d = {0: {'0': 3, '1': 0, '2': 5, '3': 6, '4': 4, '5': 7, '6': 2, '7': 1, '8': 6, '9': 5}, 1: {'0': 1, '1': 2, '2': 7, '3': 4, '4': 6, '5': 5, '6': 0, '7': 3, '8': 4, '9': 7}, 2: {'0': 7, '1': 4, '2': 1, '3': 2, '4': 0, '5': 3, '6': 6, '7': 5, '8': 2, '9': 1}, 3: {'0': 5, '1': 6, '2': 3, '3': 0, '4': 2, '5': 1, '6': 4, '7': 7, '8': 0, '9': 3}, 4: {'0': 0, '1': 3, '2': 6, '3': 5, '4': 7, '5': 4, '6': 1, '7': 2, '8': 5, '9': 6}, 5: {'0': 2, '1': 1, '2': 4, '3': 7, '4': 5, '5': 6, '6': 3, '7': 0, '8': 7, '9': 4}, 6: {'0': 4, '1': 7, '2': 2, '3': 1, '4': 3, '5': 0, '6': 5, '7': 6, '8': 1, '9': 2}, 7: {'0': 6, '1': 5, '2': 0, '3': 3, '4': 1, '5': 2, '6': 7, '7': 4, '8': 3, '9': 0}}
    state = 0

    for c in s:
        state = d[state][c]
    return state

for i in range(500):
    num = random.randint(0, 999999999)
    s = str(num)
    assert test_gsm3(s) == gsm3(s.encode())