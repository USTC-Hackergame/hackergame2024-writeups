from tqdm import tqdm

ignore = set()

n = 149
with open("ignore.txt", "r") as f:
    for line in f:
        ignore.add(int(line.strip()))

bb = []
with open("matrix", "rb") as f:
    for i in tqdm(range(n * n)):
        v = f.read(n * n)
        if i in ignore:
            continue

        b = bytes([v[j] for j in range(n * n) if j not in ignore])
        assert len(b) == n*n - len(ignore)
        bb.append(b)

    assert len(bb) == n*n - len(ignore)
    assert f.tell() == n * n * n * n

with open("matrix2", "wb") as f:
    for b in bb:
        f.write(b)

print("Done")
print(len(ignore))
