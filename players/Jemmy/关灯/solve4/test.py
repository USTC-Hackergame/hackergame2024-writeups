from tqdm import tqdm

n = 149
N = n * n

with open("A", "rb") as f:
    A = f.read()
    print(len(A))

# for i in tqdm(range(N)):
#     for j in range(N):
#         assert A[i * N + j] in [0, 1], (i, j, A[i * N + j])

# for i in tqdm(range(N)):
#     for j in range(i):
#         if A[i * N + j] != 0:
#             print(i, j)

# for i in tqdm(range(N)):
#     for j in range(i):
#         if A[j * N + i] != 0 and A[i * N + i] != 0:
#             print(i, j)

# for i in tqdm(range(N)):
#     if A[i * N + i] == 0 and not all(A[i * N + j] == 0 for j in range(N)):
#         print(i)

with open('ignore.txt', 'w') as f:
    for i in tqdm(range(N)):
        if all(A[i * N + j] == 0 for j in range(N)):
            f.write(str(i) + '\n')