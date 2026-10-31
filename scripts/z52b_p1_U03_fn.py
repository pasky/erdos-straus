"""z52b Pass-1 U03: (Z0948/Z1363/Z2462) f(n) = #ordered (x,y,z) with 4/n = 1/x+1/y+1/z, n<=NMAX, via sorted
triples x<=y<=z (x in (n/4,3n/4]; (y,z) via D | b^2, D=ay-b) and permutation counts; partial sums and moments.
(Z0901) minlcm(p)/p for primes p<=PM: min over solutions of lcm(x,y,z), largest prime factor of minlcm/p.
(Z1907) sum over primes p<=PM of [8/p not 3-unit-fraction] /(p log p) for m=8.  Uses multiprocessing (24 cores)."""
import json, math, sys
from math import gcd, isqrt, log
from multiprocessing import Pool
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
PM = 20000
def fac(n):
    f = {}; q = 2
    while q * q <= n:
        while n % q == 0: f[q] = f.get(q, 0) + 1; n //= q
        q += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def divisors(f):
    ds = [1]
    for q, e in f.items(): ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
def two_term(a, b, fb2):
    # all (y,z), y<=z, positive, with 1/y+1/z = a/b  (a,b>0 coprime)
    out = []
    for D in divisors(fb2):
        if (D + b) % a == 0:
            y = (D + b) // a; Z = b * b // D + b
            if Z % a == 0:
                z = Z // a
                if y <= z: out.append((y, z))
    return out
def sorted_triples(n, m_filter=None):
    res = []
    for x in range(n // 4 + 1, (3 * n) // 4 + 1):
        if 4 * x <= n: continue
        num = 4 * x - n; den = n * x
        g = gcd(num, den); a, b = num // g, den // g
        fb = fac(b); fb2 = {q: 2 * e for q, e in fb.items()}
        for (y, z) in two_term(a, b, fb2):
            if y >= x: res.append((x, y, z))
    return res
def f_of_n(n):
    tr = sorted_triples(n); tot = 0
    for (x, y, z) in tr:
        tot += 1 if x == y == z else (3 if (x == y or y == z) else 6)
    return n, tot
def min_lcm(p):
    tr = sorted_triples(p)
    if not tr: return p, None
    best = min(x * y // gcd(x, y) * z // gcd(x * y // gcd(x, y), z) for (x, y, z) in tr)
    return p, best
def m8_failure(p):
    # 8/p = 1/x+1/y+1/z solvable? (x in (p/8, 3p/8])
    for x in range(p // 8 + 1, (3 * p) // 8 + 1):
        num = 8 * x - p; den = p * x
        if num <= 0: continue
        g = gcd(num, den); a, b = num // g, den // g
        fb = fac(b); fb2 = {q: 2 * e for q, e in fb.items()}
        for D in divisors(fb2):
            if (D + b) % a == 0 and (b * b // D + b) % a == 0: return p, False
    return p, True
if __name__ == "__main__":
    with Pool(24) as pool:
        fn = dict(pool.map(f_of_n, range(2, NMAX + 1), chunksize=50))
        json.dump(fn, open("data/z52b/pass1/U03/fn_partial.json", "w"))
        S = lambda X: sum(fn[n] for n in range(2, X + 1))
        for X in [10**3, 3 * 10**3, 10**4]:
            if X <= NMAX:
                print(f"Z0948 N={X}: sum f(n)={S(X)}  ratio to N log^3 N = {S(X)/(X*log(X)**3):.4f}")
        if NMAX >= 10**4:
            print("Z0948 ratio N=1e3 -> 1e4 of partial sums:", round(S(10**4) / S(10**3), 2), " (N log^3N ratio:", round(10 * (log(10**4)/log(10**3))**3, 2), ")")
        print("Z2462 moments over n<=%d: sum f^2 / sum f^3 median f:" % NMAX, sum(v*v for v in fn.values()), sum(v**3 for v in fn.values()), sorted(fn.values())[len(fn)//2])
        ps = [p for p in range(3, PM + 1, 2) if all(p % q for q in range(2, isqrt(p) + 1))]
        ps = [p for p in ps if p % 4 == 1][:]
        ml = dict(pool.map(min_lcm, ps, chunksize=20))
        ratios = []
        for p, mlv in ml.items():
            if mlv: ratios.append((max(fac(mlv // gcd(mlv, p) if False else mlv // p).keys(), default=1) if mlv % p == 0 else -1))
        bad = [p for p, mlv in ml.items() if mlv and mlv % p != 0]
        print("Z0901 primes p=1 mod 4 <= %d: minlcm divisible by p: %d of %d; sample minlcm/p:" % (PM, len(ps) - len(bad), len(ps)), [(p, ml[p] // p if ml[p] and ml[p] % p == 0 else ml[p]) for p in ps[:6]])
        import collections
        mx = []
        for p in ps:
            mlv = ml[p]
            if mlv and mlv % p == 0 and mlv // p > 1:
                mx.append(max(fac(mlv // p).keys()) / p)
        print("Z0901 max log P+(minlcm/p)/log p:", round(max(math.log(max(fac(ml[p]//p).keys()))/math.log(p) for p in ps if ml[p] and ml[p] % p == 0 and ml[p] // p > 1), 3))
        fails = [p for p, ok in pool.map(m8_failure, [q for q in range(3, 6001, 2) if all(q % r for r in range(2, isqrt(q)+1))]) if not ok]
        print("Z1907 m=8 failures p<=6000 (odd primes):", fails[:30], " count", len(fails))
        print("Z1907 sum 1/(p log p) over failures:", round(sum(1/(p*math.log(p)) for p in fails), 6))
