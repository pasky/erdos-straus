"""Shared helpers for z52d Pass-2 NC0 / G4 items.

Residue-certificate families (repo formulas, cf. scripts/z52b_dividing_leastfam.py):
  Type I  (a,d): s=ad,  m=4s,  R = { -f mod m : f | 4a^2 d + 1 }
  Type II (a,b): s=ab,  m=4ab, R = { -e mod m : e | a + b }
A prime p is 'covered' by a family iff p mod m in R (the repo's certificate claim).
Only residues compatible with p = 1 (mod 4) are relevant for the ES reduction.
"""
import numpy as np


def primes_upto(N):
    s = np.ones(N + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0].astype(np.int64)


def divisors(n):
    out = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            if i * i != n:
                out.append(n // i)
        i += 1
    return sorted(out)


def families(s_max):
    """List of dicts: name, type, s, m, R (set of residues mod m), params."""
    fams = []
    for a in range(1, s_max + 1):
        for d in range(1, s_max // a + 1):
            s = a * d
            m = 4 * s
            R = {(-f) % m for f in divisors(4 * a * a * d + 1)}
            fams.append(dict(name=f"I({a},{d})", type="I", s=s, m=m, R=R, params=(a, d)))
    for a in range(1, s_max + 1):
        for b in range(a, s_max // a + 1):
            s = a * b
            m = 4 * a * b
            R = {(-e) % m for e in divisors(a + b)}
            fams.append(dict(name=f"II({a},{b})", type="II", s=s, m=m, R=R, params=(a, b)))
    fams.sort(key=lambda t: (t["s"], t["m"], t["name"]))
    return fams


def covered_mask(fam, ps):
    tab = np.zeros(fam["m"], dtype=bool)
    tab[list(fam["R"])] = True
    return tab[ps % fam["m"]]
