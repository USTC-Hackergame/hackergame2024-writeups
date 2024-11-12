import z3


def main() -> None:
    solver = z3.Solver()
    s = input("input lights: ")
    n = 0
    while n**3 != len(s):
        n += 1
        if n == 150:
            print(f"Wrong input length {len(s)}")
            return
    lights = [
        [[bool(s[i * n**2 + j * n + k] == "1") for k in range(n)] for j in range(n)]
        for i in range(n)
    ]
    switches = [[[z3.Bool(f"s[{i}][{j}][{k}]") for k in range(n)] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                state = switches[i][j][k]
                if i > 0:
                    state = z3.Xor(state, switches[i - 1][j][k])
                if i < n - 1:
                    state = z3.Xor(state, switches[i + 1][j][k])
                if j > 0:
                    state = z3.Xor(state, switches[i][j - 1][k])
                if j < n - 1:
                    state = z3.Xor(state, switches[i][j + 1][k])
                if k > 0:
                    state = z3.Xor(state, switches[i][j][k - 1])
                if k < n - 1:
                    state = z3.Xor(state, switches[i][j][k + 1])
                solver.add(state == lights[i][j][k])
    result = solver.check()
    print(result)
    if result == z3.unsat:
        return
    m = solver.model()
    # print(m)
    l = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                l.append(str(int(z3.is_true(m[switches[i][j][k]]))))
    print(''.join(l))
    # flag{bru7e_f0rce_1s_a1l_y0u_n3ed_e1b34b8422}
    # flag{prun1ng_1s_u5eful_2f0a9a41b4}
    # flag{lin3ar_alg3bra_1s_p0werful_2ec8b8b9b1}


if __name__ == "__main__":
    main()
