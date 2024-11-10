import sympy as sp

def attention(p, q, n_start_from = 0):
    x, a, b = sp.symbols("x a b", real = True)
    n = n_start_from

    while True:
        # Attention
        f = (x**(2*n))*((1-x**2)**n)*(a+b*x**2)/(1+x**2)

        # Calc the int and collect the coeff
        int_res = sp.integrate(f, (x, 0, 1))
        co_pi = int_res.coeff(sp.pi, 1)
        co_c = sp.simplify(int_res - co_pi * sp.pi)

        # Solve the linear
        solution = sp.solve(
            (co_pi - 1, co_c + sp.Rational(p, q)),
            (a, b)
        )
        _a = solution[a]
        _b = solution[b]
        
        # If f(x) >= 0
        if(_a > 0 and _a + _b > 0):
            # Output
            g = (x**(2*n))*((1-x**2)**n)*(_a+_b*x**2)/(1+x**2)
            g = sp.simplify(g)
            g = str(g)
            g = g.replace(" ", "")
            return n, g
        
        # Otherwise continue
        n += 1

if __name__ == "__main__":
    p = 262525878336290261680719458057270510949100859034284448510038
    q = 83564582453524230333969022236729704984363928821026354073077
    n = 60
    _, g = attention(p, q, n) # It takes kind of long...
    print(g)