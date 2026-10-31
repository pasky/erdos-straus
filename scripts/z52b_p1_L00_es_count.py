"""z52b pass1 L00 item Z0222: exact count f(p) = #{x<=y<=z : 4/p = 1/x+1/y+1/z} for primes p <= PMAX.

Method: for each x in (p/4, 3p/4], 4/p-1/x = a/b (reduced), a = 4x-p, b = px/g.
1/y+1/z = a/b  <=>  (a y - b)(a z - b) = b^2.  Enumerate divisors d of b^2 with d <= b, d = a y - b, y >= x.
Every hit is re-verified in exact integer arithmetic.
Memory: spf sieve up to 0.75*PMAX^2 (int32). Usage: python3 scripts/z52b_p1_L00_es_count.py PMAX
"""
import sys, csv, math
import numpy as np

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
OUT = "data/z52b/pass1/L00/es_counts.csv"
NMAX = PMAX + 2  # spf only for numbers <= PMAX (p and x are both <= PMAX; b = p*x/g is factored from these)

spf = np.zeros(NMAX + 1, dtype=np.int32)
for i in range(2, int(NMAX ** 0.5) + 1):
    if spf[i] == 0:
        seg = spf[i * i::i]
        mask = seg == 0
        seg[mask] = i
for i in range(2, NMAX + 1):
    if spf[i] == 0:
        spf[i] = i
spf = spf.tolist()  # plain list for fast scalar access

def factor(n):
    f = {}
    while n > 1:
        q = spf[n]
        while n % q == 0:
            n //= q
            f[q] = f.get(q, 0) + 1
    return f

def divisors_from(fac):
    ds = [1]
    for q, e in fac.items():
        new = []
        for d in ds:
            m = d
            for _ in range(e + 1):
                new.append(m)
                m *= q
        ds = new
    return ds

def f_count(p):
    cnt = 0
    xlo = p // 4 + 1  # x > p/4
    for x in range(xlo, (3 * p) // 4 + 1):
        a0 = 4 * x - p
        if a0 <= 0:
            continue
        b0 = p * x
        g = math.gcd(a0, b0)
        a, b = a0 // g, b0 // g
        # factor b = p*x/g from factor(p), factor(x), minus factor(g)
        fb = dict(factor(p))
        for q, e in factor(x).items():
            fb[q] = fb.get(q, 0) + e
        gg = g
        for q in list(fb):
            while gg % q == 0:
                gg //= q
                fb[q] -= 1
        assert gg == 1 and all(e >= 0 for e in fb.values())
        fb = {q: e for q, e in fb.items() if e > 0}
        assert math.prod(q ** e for q, e in fb.items()) == b
        fb2 = {q: 2 * e for q, e in fb.items()}
        for d in divisors_from(fb2):
            if d > b:            # enforce d <= e = b^2/d  (y <= z)
                continue
            if (d + b) % a:
                continue
            y = (d + b) // a
            if y < x:
                continue
            e = (b * b) // d
            if (e + b) % a:
                continue
            z = (e + b) // a
            # exact re-verification of 4xyz = p(xy+yz+zx) (1/x+1/y+1/z = 4/p)
            if 4 * x * y * z == p * (x * y + y * z + z * x) and x <= y <= z:
                cnt += 1
    return cnt

def primes_upto(n):
    return [i for i in range(2, n + 1) if spf[i] == i]

if __name__ == "__main__":
    rows = []
    for p in primes_upto(PMAX):
        if p < 3:
            continue
        rows.append((p, f_count(p)))
    with open(OUT, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["p", "f_p"])
        w.writerows(rows)
    print("primes:", len(rows), "wrote", OUT)
