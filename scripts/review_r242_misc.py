"""R242: from-scratch checks of CAP_DOWN Lemma 3.1, T1 (§3), Prop 4.1(a)/(b)."""
from fractions import Fraction
from math import gcd, isqrt
from review_r242_common import spf_sieve, factor, jacobi, order

spf = spf_sieve(400000)


def direct_cap(n, y, z):
    """cap of (y, z) per Def 1.1, None if not in ES^{(y,inf)}."""
    den = z.denominator
    r = isqrt(den)
    if r * r != den or r % 2 == 0 or gcd(r, n) != 1:
        return None
    cap = 0
    for p, v in factor(r, spf).items():
        if y % p:
            return None
        cap = max(cap, v)
    return cap


# ---- Lemma 3.1: bijection + criterion, exhaustive over D1 <= B
bad = 0
tested = 0
for n in range(3, 80, 2):
    for x in range(1, 80):
        m = 4 * x - n
        if m <= 0 or gcd(m, n) != 1 or gcd(x, n) != 1:
            continue
        N = n * x
        fN = factor(N, spf)
        B = 40 * N * N
        D1 = (-N) % m or m
        while D1 <= B:
            y = (N + D1) // m
            z = Fraction(N * y, D1)
            assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
            dc = direct_cap(n, y, z) if D1 < 400000 else None
            if D1 >= 400000:
                break
            fD = factor(D1, spf)
            ok = all(s in fN or s == 2 for s in fD)
            cap = 0
            if ok:
                for s, c in fD.items():
                    b = fN.get(s, 0)
                    if s == 2 or n % s == 0:
                        if c > 2 * b:
                            ok = False
                    else:
                        if c > 2 * b:
                            if c % 2:
                                ok = False
                            else:
                                cap = max(cap, (c - 2 * b) // 2)
            lem = cap if ok else None
            tested += 1
            if lem != dc:
                bad += 1
                if bad < 5:
                    print('Lemma 3.1 mismatch', n, x, D1, lem, dc)
            D1 += m
print('Lemma 3.1: tested', tested, 'mismatches', bad)


# ---- T1: no Lemma-1.1 divisor at any cap for n = a^2 (odd a), windows m <= 300
def any_cap_reach(fk, m):
    R = {1 % m}
    for s, b in fk.items():
        if s == 2:
            cs = range(0, 2 * b + 1)
        else:
            cs = set(range(0, 2 * b + 1)) | set(range(0, 2 * b + 2 * m + 2, 2))
        P = {pow(s, c, m) for c in cs}
        R = {r * p % m for r in R for p in P}
    return R


hits = 0
cnt = 0
for a in range(3, 400, 2):
    n = a * a
    for m in range(3, 301, 4):
        K = (n + m) // 4
        fk = factor(K, spf)
        if any(n % s == 0 for s in fk):
            continue
        cnt += 1
        if (-K) % m in any_cap_reach(fk, m):
            hits += 1
print('T1: square windows tested', cnt, 'with a Lemma-1.1 divisor (must be 0):', hits)

# ---- Prop 4.1(a): K = s prime, primitive mod q, n = 4K - q: exhaustive least cap == (q-3)/4
cases = 0
for q in [p for p in range(7, 140, 4) if spf[p] == p]:
    for s in range(3, 20000):
        if spf[s] != s or s == q or order(s, q) != q - 1:
            continue
        n = 4 * s - q
        if n % 4 != 1 or n % s == 0:
            continue
        ex = 0
        while True:
            R = {1}
            cs = set(range(0, 3)) | set(range(0, 2 + 2 * ex + 1, 2))
            P = {pow(s, c, q) for c in cs}
            if (-s) % q in P:
                break
            ex += 1
        assert ex == (q - 3) // 4, (q, s, ex)
        cases += 1
print('Prop 4.1(a): cases', cases, 'all exact (q-3)/4')

# ---- Prop 4.1(b): composite forced windows; one-prime witness cap formula vs brute force over j
cnt = 0
for n in range(5, 3000, 4):
    if isqrt(n) ** 2 == n or any(p % 4 == 3 for p in factor(n, spf)):
        continue
    for m in range(3, 800, 8):
        m2 = m + ((4 - n) % 8 - m % 8) % 8  # m = 4 - n (mod 8)
        fm = factor(m2, spf)
        if len(fm) < 2 or any(q % 4 != 3 or jacobi(q, n) != -1 for q in fm) or gcd(m2, n) != 1:
            continue
        K = (n + m2) // 4
        fk = factor(K, spf)
        for s, b in fk.items():
            if s == 2 or b % 2 == 0:
                continue
            os = [order(s, q ** k) for q, k in fm.items()]
            if any(o % 2 for o in os):
                continue
            L = 1
            for o in os:
                L = L * (o // 2) // gcd(L, o // 2)
            jbest = next(j for j in range(1, 4 * m2) if pow(s, j, m2) == m2 - 1)
            assert jbest == L and L % 2 == 1
            cnt += 1
print('Prop 4.1(b): (n, m, s) cases', cnt, 'least j == L (odd) in all')
