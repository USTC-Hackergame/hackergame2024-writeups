for i in range(38):
    for j in range(100):
        code = str((i + j) % 8 + 90)
        print(f'\033[{code}m\u2588\033[0m', end='', flush=True)
for j in range(99):
        code = str((38 + j) % 8 + 90)
        print(f'\033[{code}m\u2588\033[0m', end='', flush=True)
while True:
    pass