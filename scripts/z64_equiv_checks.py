"""z64 EQUIV: exact sanity checks of the dictionary rows of Z64_EQUIV.md section 4.
(i)   E1: k-Frobenius: for coprime u,B, the largest N with exactly k representations N = xu + yB (x,y>=0)
      is (k+1)uB - u - B   (u,B <= 13, k <= 6; brute force).
(ii)  E8: for every (*) solution (u,B,C) of n (odd n <= 3000), gamma = T^u (-L^{-4C}) T^B is in SL2(Z),
      has upper-right entry n, lower-left 4C, diagonal = (4uC-1, 4BC-1) = 4C*(u,B) - 1.
(iii) E14: for every prime p <= 3000, p = 1 (4), and every (*) solution, the triple (x,y,z) = (uBC, pBC, puC)
      is lcm-balanced (lcm of each pair = N = puBC) and admits a,b,c in Z/N, a+b+c = 0, with
      gcd(a,N) = N/x, gcd(b,N) = N/y, gcd(c,N) = N/z (cyclic 3-point cover with these ramification orders);
      genus formula 2g-2 = N(1 - 1/x - 1/y - 1/z) = uBC(p-4).
(iv)  E7: for words n = tuv - u - v (t,u,v>=2, n <= 3000), M = [[v,-1,0],[-1,t,-1],[0,-1,u]] has det n
      (coker cyclicity is proved by hand in the memo: a 2x2 minor equals 1; not checked here), and (M^-1)_{11} = (tu-1)/n, (M^-1)_{33} = (tv-1)/n; Jacobi((tu-1)/n) = Jacobi((tv-1)/n).
Prints OK/FAIL counts."""
from math import gcd
from fractions import Fraction as F
import itertools, sys
from sympy import isprime, jacobi_symbol
from sympy import Matrix

def lcm(a, b): return a // gcd(a, b) * b
bad = 0
# (i)
cnt = 0
for u in range(1, 14):
    for B in range(1, 14):
        if gcd(u, B) != 1: continue
        LIM = 8 * u * B + 50
        reps = [0] * (LIM + 1)
        for x in range(0, LIM // u + 1):
            for y in range(0, (LIM - x * u) // B + 1):
                reps[x * u + y * B] += 1
        for k in range(0, 7):
            want = (k + 1) * u * B - u - B
            # largest N <= LIM-? with reps exactly k  (reps grows ~N/uB, so LIM is safe)
            Ns = [N for N in range(0, LIM - u * B) if reps[N] == k]
            got = max(Ns) if Ns else None
            cnt += 1
            if want >= 0 and got != want:
                bad += 1; print("FAIL kFrob", u, B, k, want, got)
print("(i) k-Frobenius checks:", cnt, "bad so far", bad)
# helpers
def mul(X, Y):
    return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]],
            [X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]
def T(k): return [[1, k], [0, 1]]
def stars(n):
    out = []
    for C in range(1, n + 1):
        if 4 * C - 1 > n + 1: break
        for u in range(1, n + 1):
            m = 4 * u * C - 1
            if m > n + u: break
            if (n + u) % m == 0:
                B = (n + u) // m
                if B >= 1: out.append((u, B, C))
    return out
c2 = c3 = 0
for n in range(3, 3001, 2):
    for (u, B, C) in stars(n):
        c = 4 * C
        g = mul(mul(T(u), [[-1, 0], [c, -1]]), T(B))
        if not (g[0][1] == n and g[1][0] == c and g[0][0] == c*u - 1 and g[1][1] == c*B - 1
                and g[0][0]*g[1][1] - g[0][1]*g[1][0] == 1):
            bad += 1; print("FAIL SL2", n, u, B, C, g)
        c2 += 1
        if isprime(n) and n % 4 == 1:
            p = n; x, y, z = u*B*C, p*B*C, p*u*C
            assert F(1, x) + F(1, y) + F(1, z) == F(4, p)
            N = p * u * B * C
            if not (lcm(x, y) == N and lcm(y, z) == N and lcm(x, z) == N):
                bad += 1; print("FAIL lcm", p, u, B, C)
            ok = False
            # search a,b,c: a = (N/x)*a', etc.  small search suffices (CRT argument in memo)
            ax, by, cz = N // x, N // y, N // z
            for a1 in range(1, 60):
                a = ax * a1 % N
                if gcd(a, N) != ax: continue
                for b1 in range(1, 60):
                    b = by * b1 % N
                    if gcd(b, N) != by: continue
                    cc = (-a - b) % N
                    if gcd(cc, N) == cz: ok = True; break
                if ok: break
            if not ok: bad += 1; print("FAIL cyclic", p, u, B, C)
            if 2 * (1 + u*B*C*(p - 4) // 2) - 2 != u*B*C*(p - 4) or (u*B*C*(p-4)) % 2: 
                bad += 1; print("FAIL genus parity", p, u, B, C)
            c3 += 1
print("(ii) SL2 factorisations:", c2, " (iii) cyclic-cover checks:", c3, "bad so far", bad)
c4 = 0
for t in range(2, 3001):
    for u in range(2, 3001):
        if t*u*2 - u - 2 > 3000: break
        for v in range(2, 3001):
            n = t*u*v - u - v
            if n > 3000: break
            M = Matrix([[v, -1, 0], [-1, t, -1], [0, -1, u]])
            if M.det() != n: bad += 1; print("FAIL det", t, u, v)
            Mi = M.inv()
            if Mi[0, 0] != F(t*u - 1, n) and Mi[0, 0] != __import__('sympy').Rational(t*u-1, n):
                bad += 1; print("FAIL inv11", t, u, v)
            if Mi[2, 2] != __import__('sympy').Rational(t*v - 1, n): bad += 1; print("FAIL inv33")
            if n % 2 == 1 and gcd(t*u - 1, n) == 1:
                if jacobi_symbol(t*u - 1, n) != jacobi_symbol(t*v - 1, n): bad += 1; print("FAIL rev", t, u, v)
            c4 += 1
print("(iv) A3 critical-matrix checks:", c4)
print("TOTAL bad:", bad)
