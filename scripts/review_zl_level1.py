"""review_zl_level1.py -- R231, FROM SCRATCH: level-1 coverage of the non-residue cells mod a prime r.
Level-1 boxes meeting non-residue cells (M17 Lemmas 1.1, 1.3, 2.1, 2.3, 5.2; U subsumed by P):
  P (K=1, N=r): 4abd = r+e, a+b = ce, a<=b, r∤cd   -> residues -(4acd-1), -(4bcd-1) mod r
  Q (k=1, F=r): 4abcd = r(a+b)+c, c|a+b, a<=b, r∤e (e=(a+b)/c) -> residues -4a^2 d, -4b^2 d mod r
Optionally (env LOOSE=1) drops the r-conditions to show they change nothing in non-residue cells.
Usage: review_zl_level1.py lo hi"""
import sys, os
loose = bool(os.environ.get("LOOSE"))
def primes(lo, hi):
    s = bytearray([1]) * hi; s[0:2] = b"\0\0"
    for p in range(2, int(hi ** .5) + 1):
        if s[p]: s[p*p::p] = bytearray(len(s[p*p::p]))
    return [p for p in range(max(lo, 3), hi) if s[p]]
def cover(r):
    cov = set()
    a = 1
    while 4 * a * a - 2 * a <= r:
        b = a
        while 4 * a * b - 2 * b <= r:
            m = 4 * a * b
            for d in range(-(-(r + 1) // m), (r + a + b) // m + 1):
                e = m * d - r
                if 1 <= e <= a + b and (a + b) % e == 0:
                    c = (a + b) // e
                    if loose or (c % r and d % r):
                        cov.add((-(4 * a * c * d - 1)) % r); cov.add((-(4 * b * c * d - 1)) % r)
            b += 1
        a += 1
    a = 1
    while 4 * a - 1 <= 2 * r:
        d = 1
        while 4 * a * d - 1 <= 2 * r:
            c = 1
            while c * (4 * a * d - 1) <= 2 * r:
                f = 4 * a * c * d - r
                if f > 0 and (a * r + c) % f == 0:
                    b = (a * r + c) // f
                    if b >= a and (a + b) % c == 0:
                        e = (a + b) // c
                        if loose or e % r:
                            cov.add((-4 * a * a * d) % r); cov.add((-4 * b * b * d) % r)
                c += 1
            d += 1
        a += 1
    return cov
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for r in primes(lo, hi):
    sq = {x * x % r for x in range(1, r)}
    nr = [u for u in range(1, r) if u not in sq]
    surv = sorted(set(nr) - cover(r))
    print(r, len(nr), len(surv), surv if len(surv) <= 8 else "")
