"""R264 from-scratch misc checks for FORCED_WINDOW.
(1) Prop 2.2 reading: prime q ≡ 3 (4), q | s^j + 1 (j odd, s odd prime), q > 4 s^2 — first examples per j; none for j = 3.
(2) Prop 1.2 Fourier criterion on random boxes in Z/n (n odd): whenever the criterion sum < 1, W = G.
(3) Thm 3.2 parenthetical: proportion of classes p mod 4P(y) whose least CRT window m = (-p mod 4P) is >= h.
"""
import random
from math import cos, pi, sin, isqrt, prod


def isprime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def pfactors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


print("(1) Prop 2.2 windows q | s^j+1, q≡3(4), q>4s^2:")
for j in (3, 5, 7, 9):
    ex = []
    for s in [x for x in range(3, 400) if isprime(x)]:
        for q in pfactors(s**j + 1):
            if q % 4 == 3 and q > 4 * s * s:
                ex.append((s, q))
    print(f"  j={j}: {len(ex)} examples with s<400; first: {ex[:3]}")

print("(2) Prop 1.2 random tests")
random.seed(1)
bad = 0
fired = 0
for trial in range(3000):
    n = random.choice([x for x in range(15, 400, 2)])
    k = random.randint(1, 4)
    g = [random.randrange(n) for _ in range(k)]
    L = [random.randint(1, 12) for _ in range(k)]
    tot = 0.0
    for a in range(1, n):  # characters psi_a(x) = e(a x / n) on Z/n
        pr = 1.0
        for gi, Li in zip(g, L):
            th = (a * gi % n) / n
            d = min(th, 1 - th)
            pr *= 1.0 if d == 0 else min(1.0, 1.0 / ((Li + 1) * 2 * d))
        tot += pr
    if tot < 1:
        fired += 1
        W = {0}
        for gi, Li in zip(g, L):
            W = {(w + j * gi) % n for w in W for j in range(Li + 1)}
        if len(W) != n:
            bad += 1
print(f"  criterion fired {fired} times, W != G in {bad}")

print("(3) Thm 3.2: least CRT window vs h")
P = 1
ps = [x for x in range(2, 60) if isprime(x)]
for i, s in enumerate(ps[:-1]):
    P *= s
    nxt = ps[i + 1]
    for h in (P, P * nxt - 1):
        # proportion of residues r = -p mod 4P (p ≡ 1 mod 4, gcd(p,P)=1) with r >= h
        M = 4 * P
        tot = big = 0
        if M > 10**6:
            break
        for r in range(3, M, 4):
            from math import gcd
            if gcd(r, P) == 1:
                tot += 1
                big += r >= h
        print(f"  y={s}: P={P}, h={h}: fraction of classes with least CRT window >= h: {big/tot:.3f}")
