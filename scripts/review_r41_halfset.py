"""R41 referee: from-scratch brute force of the half-set lemma, beta(a), the window
criterion (vs. direct unit-fraction search), Remark 3.2(i), and Lemma 2.6."""
from math import gcd
from itertools import product
import sys

def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def divisors(n):
    ds = [1]
    for q, e in factor(n).items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds

def rat_def(a, x):
    """Rat_a(x) straight from the definition {u/v: gcd(u,v)=1, uv | x}."""
    out = set()
    for u in divisors(x):
        for v in divisors(x // u):
            if gcd(u, v) == 1:
                out.add(u * pow(v, -1, a) % a)
    return out

def selections(a):
    G = [g for g in range(1, a) if gcd(g, a) == 1]
    seen = set(); orbits = []
    for g in G:
        if g in seen: continue
        gi = pow(g, -1, a)
        orb = {g, gi, (-g) % a, (-gi) % a}
        seen |= orb
        if len(orb) == 4:
            orbits.append([{g, gi}, {(-g) % a, (-gi) % a}])
        else:
            assert len(orb) == 2 and g * g % a == 1
            if 1 in orb: orbits.append([{1}])
            else: orbits.append([{g}, {(-g) % a}])
    sels = []
    for ch in product(*orbits):
        S = set().union(*ch); sels.append(frozenset(S))
    return G, sels

def omega(n): return len(factor(n))

def phi(n):
    r = n
    for q in factor(n): r = r // q * (q - 1)
    return r

def check_halfset(amax=63, xmax=20000):
    for a in range(3, amax + 1, 4):
        G, sels = selections(a)
        beta = (phi(a) - 2**omega(a)) // 4 + 2**(omega(a) - 1) - 1
        assert len(sels) == 2**beta, (a, len(sels), beta)
        assert all(len(S) == phi(a) // 2 for S in sels)
        nfail = 0
        for x in range(1, xmax + 1):
            if gcd(x, a) != 1: continue
            R = rat_def(a, x)
            if (a - 1) in R: continue
            nfail += 1
            C = {q % a for q in factor(x)}
            assert any(C <= S for S in sels), (a, x, C)
        print(f"a={a}: beta={beta} #sel={len(sels)} -1-free x<= {xmax}: {nfail} all confined")

def window_direct(p, a):
    """Does 4/p - 1/x = a/(p x) = 1/y + 1/z have a solution? (direct search)"""
    x = (p + a) // 4; num, den = a, p * x
    g = gcd(num, den); num //= g; den //= g
    # 1/y <= num/den, y >= den/num; y <= 2 den/num
    lo = -(-den // num); hi = 2 * den // num
    for y in range(lo, hi + 1):
        n2 = num * y - den; d2 = den * y
        if n2 > 0 and d2 % n2 == 0: return True
    return False

def isprime(n): return n > 1 and all(n % d for d in range(2, int(n**.5) + 1))

def check_criterion(pmax=4000):
    cnt = 0
    for p in range(5, pmax, 4):
        if not isprime(p): continue
        for a in range(3, 3 * p, 4):
            x = (p + a) // 4
            R = rat_def(a, x)
            crit = ((a - 1) in R) or ((-p) % a in R)
            assert crit == window_direct(p, a), (p, a)
            cnt += 1
        # Lemma 2.6
        if p % 24 == 1:
            x3 = (p + 3) // 4
            fails3 = not window_direct(p, 3)
            assert fails3 == all(q % 3 != 2 for q in factor(x3)), p
    print("window criterion vs direct search: ok on", cnt, "pairs")

if __name__ == "__main__":
    # Remark 3.2(i)
    assert isprime(61) and rat_def(7, 17) == {1, 3, 5} and not window_direct(61, 7)
    check_halfset(int(sys.argv[1]) if len(sys.argv) > 1 else 63)
    check_criterion(int(sys.argv[2]) if len(sys.argv) > 2 else 1500)
