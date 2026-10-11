"""R138 from-scratch checks for barrier-note section 6.1 (covering in e-slices)."""
import itertools, random
from math import gcd
from sympy import factorint, isprime, jacobi_symbol, divisors, totient

def pairs(N, e):
    out = []
    for a in divisors(N):
        for b in divisors(N // a):
            if (a + b) % e == 0:
                out.append((a, b))
    return out

def sigma(N, e):
    S = {1}
    for l, v in factorint(N).items():
        S = {s * pow(l, t, e) % e if t >= 0 else s * pow(pow(l, -t, e), -1, e) % e
             for s in S for t in range(-v, v + 1)}
    return S

bad = 0
pdivE_II = []
for p in [q for q in range(5, 400) if isprime(q) and q % 4 == 1]:
    for e in range(3, 3 * p + 50, 4):
        for T in ("I", "II"):
            num = p * e + 1 if T == "I" else p + e
            if num % 4: continue
            N = num // 4
            P = pairs(N, e)
            if e % p == 0:
                if T == "II" and P: pdivE_II.append((p, e, P[:2]))
                continue
            assert gcd(N, e) == 1
            S = sigma(N, e)
            ratios = {a * pow(b, -1, e) % e for a in divisors(N) for b in divisors(N // a)}
            assert S == ratios
            assert (len(P) > 0) == ((e - 1) in S)
            # genus lemma (i),(ii)
            for l in factorint(N):
                chi = jacobi_symbol(l % e, e) if l != 2 else jacobi_symbol(2, e)
                assert chi == jacobi_symbol(l, p), (p, e, T, l)
            chiN = jacobi_symbol(N % e, e)
            assert chiN == (1 if T == "I" else jacobi_symbol(e, p))
            # solutions check
            for a, b in P:
                c, d = (a + b) // e, N // (a * b)
                if T == "II": x, y, z = a*b*d, a*c*d*p, b*c*d*p
                else: x, y, z = a*b*d*p, a*c*d, b*c*d
                assert 4 * x * y * z == p * (x*y + y*z + z*x)
print("slice/genus lemma checks OK; Type II slices with p|e nonempty:", pdivE_II[:5], len(pdivE_II))

# collision lemma identities (signed solutions)
for p in [q for q in range(5, 300) if isprime(q) and q % 4 == 1]:
    for e in range(3, 400, 4):
        for T in ("I", "II"):
            num = p * e + 1 if T == "I" else p + e
            if num % 4 or e % p == 0: continue
            N = num // 4
            f = factorint(N)
            unit = [1]
            for l, v in f.items(): unit += [u * l**v for u in unit]
            if len(unit) <= totient(e): continue
            seen = {}
            for u in unit:
                r = u % e
                if r in seen:
                    g = gcd(u, seen[r]); a, b = max(u, seen[r]) // g, min(u, seen[r]) // g
                    break
                seen[r] = u
            assert gcd(a, b) == 1 and N % (a * b) == 0 and (a - b) % e == 0
            c, d = (a - b) // e, N // (a * b)
            from fractions import Fraction as F
            if T == "II": s = F(1, a*b*d) - F(1, a*c*d*p) + F(1, b*c*d*p)
            else: s = F(1, a*b*d*p) - F(1, a*c*d) + F(1, b*c*d)
            assert s == F(4, p)
print("collision identities OK")

# Kneser criterion: criterion => t0 in Sigma, cyclic groups Z/n (all subgroups dZ, d|n)
random.seed(1)
cnt = 0
for _ in range(20000):
    n = random.randint(2, 40); k = random.randint(1, 4)
    g = [random.randrange(n) for _ in range(k)]; v = [random.randint(1, 3) for _ in range(k)]
    t0 = random.randrange(n)
    S = {0}
    for gi, vi in zip(g, v): S = {(s + t * gi) % n for s in S for t in range(-vi, vi + 1)}
    ok = True
    for d in divisors(n):  # H = dZ/n, index d
        if t0 % d == 0: continue
        tot = sum(min(2 * vi + 1, d // gcd(gi, d)) - 1 for gi, vi in zip(g, v))
        if tot < d - 1: ok = False; break
    if ok:
        cnt += 1; assert t0 in S, (n, g, v, t0)
print("Kneser criterion verified on", cnt, "random instances where it applies")
# sharpness example Z/2m
for m in range(1, 15):
    for k in range(1, 20):
        n = 2 * m
        crit = all(k * (min(3, d) - 1) >= d - 1 for d in divisors(n) if m % d != 0)
        assert crit == (k >= m) == (m in {t % n for t in range(-k, k + 1)})
print("sharpness example OK")
