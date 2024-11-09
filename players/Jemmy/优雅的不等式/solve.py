from pwn import *
import sympy
from tqdm import tqdm

cache = {}

x = sympy.Symbol('x')
n = sympy.Symbol('n')
a = sympy.Symbol('a')
b = sympy.Symbol('b')
c = sympy.Symbol('c')
t = sympy.Symbol('t')

f_exp = sympy.parsing.sympy_parser.parse_expr('((x**n)*((1-x)**n)*(a+b*x+c*(x**2)))/(1+(x**2))')

for j in tqdm(range(1, 80)):
    f = f_exp.subs(n, j)
    int_exp = sympy.expand_log(sympy.integrate(f, (x, 0, 1)).simplify())
    assert int_exp.free_symbols <= {a, b, c}, int_exp.free_symbols
    int_exp = sympy.collect(int_exp, ['log(2)', 'pi'], evaluate=False)

    cache[j] = f, int_exp


local = False

if local:
    io = process(['python3', 'equation.py'])
else:
    io = remote('202.38.93.141', 14514)
    io.recvuntil(b'Please input your token: \n')
    io.sendline(
        b'1411:MEQCIAplFMrlOcSGiuyvXbD2viXkZel+YtLmOBzUXj48+rzXAiBrX2C/xRLIxhAn+TJYUsQtGEDzpleulEFWzyijebwTXA==')

for i in range(0, 40):
    io.recvuntil(b'Please prove that pi>=')
    line = sympy.parsing.sympy_parser.parse_expr(
        io.recvline().decode().strip())
    print(i, line)

    for j in range(max(1, 2 * i - 2), 100):
        if j not in cache:
            print('cache miss', j)
            f = f_exp.subs(n, j)
            int_exp = sympy.expand_log(
                sympy.integrate(f, (x, 0, 1)).simplify())
            assert int_exp.free_symbols <= {a, b, c}, int_exp.free_symbols
            int_exp = sympy.collect(int_exp, ['log(2)', 'pi'], evaluate=False)

            cache[j] = f, int_exp
        else:
            f, int_exp = cache[j]

        solutions = sympy.solve(
            [int_exp[sympy.log(2)], int_exp[sympy.pi] - 1, int_exp[1] + line], [a, b, c])
        print(f'i={i}, j={j}, solutions={solutions}')
        if not solutions:
            continue

        f = f.subs(solutions)
        int_exp = sympy.expand_log(sympy.integrate(f, (x, 0, 1)).simplify())

        domain = sympy.Interval(0, 1)
        if not (sympy.solveset(f >= 0, x, domain) == domain):
            continue

        break

    else:
        assert False  # no solution found

    print('final', f, int_exp)

    io.recvuntil(b'Enter the function f(x): ')
    io.sendline(str(f).encode())

    peek = io.recv(5)
    if peek == b'Q.E.D':
        io.recvline()
    elif peek == b'Trace':
        print((peek + io.recvall()).decode())
    if i == 1:
        print(io.recvline().decode())
print(io.recvall())
