"""R281 from-scratch: boxed equation a(m1 m2 d - 4) = m1 + 16 m2 (EXP_15 Lemma 2.2'), with R281's own bound proof:
  d <= 21; m2 = 1: m1 <= 24 (d = 1, m1-4 | 20) / m1 <= 20 (d >= 2);
  m2 >= 2: m1 >= 17 => m2 <= 21, m1 <= 36;  m1 <= 16, t = m1 d >= 5 => a <= (m1+32)/6, m2 <= m1 + 4a <= 48;
           t <= 4 => (a t - 16)(t m2 - 4) = t m1 + 64 <= 80 => m2 <= 84.
So the box d <= 21, m1 <= 36, m2 <= 84 is exhaustive (a determined). Cross-check on a much larger box with numpy.
Also: Capelli / (C1) check, Remark 2.3, positive control (63)."""
import numpy as np
import sympy as sp
from sympy import perfect_power

sols = set()
for d in range(1, 22):
    for m1 in range(1, 37):
        for m2 in range(1, 85):
            den = m1 * m2 * d - 4
            if den > 0 and (m1 + 16 * m2) % den == 0:
                sols.add(((m1 + 16 * m2) // den, d, m1, m2))
print("solutions in proved box:", len(sols))
# big box cross-check: d <= 60, m1 <= 3000, m2 <= 3000
big = set()
m1 = np.arange(1, 3001, dtype=np.int64)[:, None]
m2 = np.arange(1, 3001, dtype=np.int64)[None, :]
for d in range(1, 61):
    den = m1 * m2 * d - 4
    num = m1 + 16 * m2
    ok = (den > 0) & (num % np.where(den > 0, den, 1) == 0)
    for i, j in zip(*np.nonzero(ok)):
        big.add((int(num[0, j] + i) // int(den[i, j]) if False else int((i + 1 + 16 * (j + 1)) // ((i + 1) * (j + 1) * d - 4)), d, i + 1, j + 1))
print("solutions in big box:", len(big), "equal:", big == sols)
print("max a, d, m1, m2:", max(s[0] for s in sols), max(s[1] for s in sols), max(s[2] for s in sols), max(s[3] for s in sols))
# verify the X, X' interpretation and (C1)
for a, d, m1, m2 in sorted(sols):
    X, Xp = m1 * a * d - 16, m2 * a * d - 1
    assert X * Xp == 16 + 4 * a * a * d
K_hits = []
for a, d, m1, m2 in sorted(sols):
    K = 4 * a * a * d + 1
    if K % 15 == 0:
        q = K // 15
        pp = perfect_power(q)
        K_hits.append((a, d, q, pp))
print("15 | 4a^2d+1:", sorted(set(K_hits)))
print("distinct (a,d) with a,d odd:", sorted({(a, d) for a, d, _, _ in sols if a % 2 and d % 2}))
print("all sols:", sorted(sols))

Y = sp.symbols('Y')
print("Y^6+27:", sp.factor_list(Y**6 + 27))
print("Y^4-3Y^2+9 - (Y^2+3Y+3)(Y^2-3Y+3) =", sp.expand(Y**4 - 3 * Y**2 + 9 - (Y**2 + 3 * Y + 3) * (Y**2 - 3 * Y + 3)))
# astra example a=1,d=101: K = 405 = 15*27
print("1+4*101 =", 1 + 4 * 101, "= 15*", (1 + 4 * 101) // 15)
# positive control 63: K = 63 u^p
a, d = 5, 17
print("63 control: 1+4a^2d =", 1 + 4 * a * a * d, "= 63*", (1 + 4 * a * a * d) / 63, "; 64+4a^2d =", 64 + 4 * a * a * d, "= 21*84")
# Capelli sanity: 15Y^D + K reducible iff K/15 is a p-th power, p | D odd (sample)
bad = 0
for D in range(2, 13):
    for K in range(5, 2000, 4):  # K = 1 + 4a^2d is 1 mod 4
        red = len(sp.factor_list(15 * Y**D + K)[1]) > 1 or sp.factor_list(15 * Y**D + K)[1][0][1] > 1
        pred = K % 15 == 0 and any(D % p == 0 and sp.integer_nthroot(K // 15, p)[1] for p in sp.primerange(3, D + 1))
        if red != pred:
            bad += 1
            print("Capelli mismatch", D, K)
print("Capelli sample mismatches:", bad)
