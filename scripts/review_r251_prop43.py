"""R251: from-scratch check of Prop 4.3 for c = 3 (i = 1): SG windows m(t) = 12 t^4 - 1 at mu = 0 fire iff
m(t) | N(t) = 3^a g+^x g-^y + 2^(x+y), g+- = 2t^2 +- 2t + 1, 0 <= a, x, y <= 2.
Bound t via m(t) | Res(N, m) and test every t below the bound."""
import sys
import sympy as sp
t = sp.symbols('t')
c = int(sys.argv[1]) if len(sys.argv) > 1 else 3
i = {3: 1, 15: 2, 63: 3}[c]
m = 4*c*t**4 - 1
gp, gm = 2*t**2 + 2*t + 1, 2*t**2 - 2*t + 1
qs = sp.primefactors(c)
hits = []
import itertools
for avec in itertools.product(range(3), repeat=len(qs)):
    for x in range(3):
        for y in range(3):
            pre = sp.Mul(*[q**a for q, a in zip(qs, avec)])
            N = sp.expand(pre*gp**x*gm**y + 4**(i-1)*2**(x+y))
            R = abs(sp.resultant(N, m, t))
            assert R != 0
            T = int(sp.integer_nthroot(int(R)//(4*c) + 1, 4)[0]) + 2
            if T > 10**6:
                print('bound too large', avec, x, y, T); continue
            Np = sp.Poly(N, t)
            for tv in range(1, T + 1):
                mv = 4*c*tv**4 - 1
                if int(Np.eval(tv)) % mv == 0:
                    hits.append((tv, avec, x, y))
print('c =', c, 'firings (t, a, x, y):', hits)
