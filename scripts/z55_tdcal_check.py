# z55 TDCAL: exact checks of Lemma S (a),(b),(c) and Prop D (ii),(iii) on consecutive primes.
# Usage: python z55_tdcal_check.py P0 COUNT   (U = floor(p^{1/4}))
import sys, math
from sympy import nextprime
P0, CNT = int(sys.argv[1]), int(sys.argv[2])
def iroot4(n):
    r = int(round(n ** 0.25))
    while r**4 > n: r -= 1
    while (r+1)**4 <= n: r += 1
    return r
p = P0; bad = 0; agg_T = {}; aggE = 0; aggA = {}; aggE1p = 0
Ts = [0, 1, 4, 16, 64]; deltas = [0.02, 0.05, 0.1]
for _ in range(CNT):
    p = nextprime(p); U = iroot4(p); U2 = U*U
    # strip E1 by m
    E1 = []
    for m in range(U2+1, 4*U2+1):
        r = (-p) % m
        if 2*U < r <= 4*U: E1.append((r, m))
    # (a) central slice
    x, y = p + 2*U, 2*U
    sl = sum((x+y)//m - x//m for m in range(U2+1, 4*U2+1))
    if sl != len(E1): bad += 1; print("S(a) mismatch", p)
    # (b) two-shift vs product definition
    n2 = sum(1 for u in range(U+1, 2*U+1) for B in range(u+1, 2*U+1) if (p+u+B) % (u*B) == 0)
    n2b = sum(1 for u in range(U+1, 2*U+1) for w in range(1, 2*U-u+1) if (p+w) % u == 0 and (p-w) % (u+w) == 0)
    if n2 != n2b: bad += 1; print("S(b) mismatch", p, n2, n2b)
    # (c) m | p^2 - D
    for (s, m) in E1:
        if (p*p - (s*s - 4*m)) % m: bad += 1; print("S(c) fail", p, s, m)
    # Prop D (iii): sum_{|tau|<=T} N^[tau] = sum_{E1+} #{j>=1 : |D - j^2| <= T}
    E1p = [(s, m, s*s - 4*m) for (s, m) in E1 if s*s - 4*m >= 1]; aggE1p += len(E1p); aggE += len(E1)
    for T in Ts:
        c = 0
        for (s, m, D) in E1p:
            lo = math.isqrt(max(D - T, 0)); 
            for j in range(max(lo, 1), math.isqrt(D + T) + 2):
                if abs(D - j*j) <= T: c += 1
        agg_T[T] = agg_T.get(T, 0) + c
        if T == 0 and c < n2: bad += 1; print("D(ii) fail", p)
    # NC count A(delta) vs 2 delta |E1+|
    for d in deltas:
        a = sum(1 for (s, m, D) in E1p if abs(math.sqrt(D) - round(math.sqrt(D))) <= d)
        aggA[d] = aggA.get(d, 0) + a
print(f"P0={P0} primes={CNT} U~{U} checks_failed={bad} mean|E1|={aggE/CNT:.2f} mean|E1+|={aggE1p/CNT:.2f}")
for T in Ts: print(f"  T={T}: mean sum_|tau|<=T N^[tau] = {agg_T[T]/CNT:.3f}  (ratio to T: {agg_T[T]/CNT/max(T,1):.3f})")
for d in deltas: print(f"  delta={d}: mean A(delta) = {aggA[d]/CNT:.3f}  vs 2*delta*|E1+| = {2*d*aggE1p/CNT:.3f}")
