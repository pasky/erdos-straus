# z70 LOOSE I6: leading singular coefficients of G(z) = sum_n R(n) e(nz) at rationals r = a0/c (Z70_LOOSE §2, Lemma K):
#   kappa(a0/c)/kappa(0) = S(a0,c)/c^3,  S(a0,c) = sum_{alpha,beta,delta mod c} e(a0 (4 alpha beta delta - alpha - beta)/c)
#                                              = c * sum_{alpha,beta mod c, c | 4 alpha beta} e(-a0 (alpha+beta)/c).
# Exact evaluation (complex sums rounded), independence of a0, multiplicativity, and zero pattern.
import cmath, math, sys
def S(a0, c):
    tot = 0
    for al in range(c):
        for be in range(c):
            if (4 * al * be) % c == 0: tot += cmath.exp(-2j * math.pi * a0 * (al + be) / c)
    return tot / c**2          # = S(a0,c)/c^3
def S3(a0, c):                  # brute force over delta too (check of the delta-sum step)
    tot = 0
    for al in range(c):
        for be in range(c):
            for de in range(c): tot += cmath.exp(2j * math.pi * a0 * (4*al*be*de - al - be) / c)
    return tot / c**3
for c in [2, 3, 4, 5, 6, 8, 9, 12]:
    assert abs(S(1, c) - S3(1, c)) < 1e-9 and abs(S(1,c) - S3(c-1 if c>2 else 1, c)) < 1e-9
print("delta-sum step and a0-independence verified for c in 2..12 subset")
vals = {}
for c in range(1, 122):
    v = [S(a0, c) for a0 in range(1, c + 1) if math.gcd(a0, c) == 1]
    assert max(abs(x - v[0]) for x in v) < 1e-9, c
    vals[c] = v[0].real; assert abs(v[0].imag) < 1e-9
def fac(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
bad = 0
for c in range(2, 122):
    prod = 1.0
    for q, e in fac(c).items(): prod *= vals[q**e]
    if abs(prod - vals[c]) > 1e-9: bad += 1
print("multiplicativity failures c<=121:", bad)
print("local factors F(l^e) = kappa(./l^e)/kappa(0):")
for l in [2, 3, 5, 7, 11]:
    print("  l=%d:" % l, ", ".join("e=%d: %+.6f (x l^%d = %+.4f)" % (e, vals[l**e], e, vals[l**e] * l**(2*e)) for e in range(1, 6) if l**e <= 121))
print("c <= 121 with kappa = 0:", [c for c in range(1, 122) if abs(vals[c]) < 1e-12])
print("odd squares c = m^2 <= 121, kappa:", {m*m: round(vals[m*m], 12) for m in range(3, 12, 2)})
