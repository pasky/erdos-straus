"""R276 from-scratch: (a) explicit family n = 64m^2-24m+1 in the 4|t length-3 slice (RS Def 2.4 condition (1));
(b) no square n (odd or even) <= X has a length-3 word [[v,t,u]] with 4|t or 4|A=tu-1 (n = 1 mod 4 required for Prop 3.1);
(c) total count of length-3 HJ words with numerator <= X (BK-normalised exponent);
(d) Zhang g_j = -T^{-2j} S T^{-2j}."""
import sys, math
from sympy import jacobi_symbol, Matrix
X = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
# (a)
for m in range(1, 2000):
    t, u, v = 4, 4*m-1, 4*m
    n = t*u*v - u - v
    assert n == 64*m*m - 24*m + 1 and n % m == 1 % m and n % 8 == 1
    A = t*u - 1
    assert 0 < A < n and math.gcd(A, n) == 1 and jacobi_symbol(A, n) == -1
print("(a) family ok m<2000")
# (b),(c): enumerate t,u,v>=2 with tuv-u-v<=X
sq_hits = {}; total = 0; cnt_by_X = {}
marks = [X//100, X//10, X]
tot_at = {k: 0 for k in marks}
for t in range(2, X+1):
    if 4*t - 4 > X: break
    for u in range(2, X+1):
        if t*u*2 - u - 2 > X: break
        # v from 2 while t*u*v - u - v <= X
        c = t*u - 1
        vmax = (X + u) // c
        for v in range(2, vmax+1):
            n = c*v - u
            for k in marks:
                if n <= k: tot_at[k] += 1
            r = math.isqrt(n)
            if r*r == n and (t % 4 == 0 or c % 4 == 0 or u % 4 == 0 or v % 4 == 0 or (t*v-1) % 4 == 0):
                if n % 4 == 1:
                    sq_hits.setdefault(n, []).append((t, u, v))
print("(b) odd squares n=1(4) with a five-slice word:", len(sq_hits))
for k in marks:
    print(f"(c) X={k}: #len-3 words={tot_at[k]}  /(X log^2 X)={tot_at[k]/(k*math.log(k)**2):.3f}")
# (d)
T = lambda a: Matrix([[1, a], [0, 1]]); S = Matrix([[0, -1], [1, 0]])
for j in range(1, 20):
    g = Matrix([[2*j, 1-4*j*j], [-1, 2*j]])
    assert g == -T(-2*j)*S*T(-2*j)
    assert g != T(2*j)*S*T(2*j) and g != -T(2*j)*S*T(2*j)
print("(d) g_j = -T^{-2j} S T^{-2j}, not ±T^{2j} S T^{2j}")
