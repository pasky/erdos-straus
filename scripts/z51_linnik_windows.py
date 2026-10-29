#!/usr/bin/env python3
"""z51 linnik §5: the window lottery behind escape (c).
For a prime p == 1 (mod 4) and a prime window q == 3 (mod 4), q not dividing p, put x := (p+q)/4 when 4 | p+q (else
skip the window).  The window carries an ES solution with this x (cap 0, CAP_DOWN Lemma 3.1 at e = 0) iff
q/(p x) = 1/y + 1/z is solvable iff there are divisors d1, d2 of p*x with q | d1 + d2.
For Mordell-hard primes p (p mod 840 in the six classes) in [P0, P0 + W) and the windows q == 3 (mod 4) in (y/2, y]
(4 | p + q; odd and even windows, CAP_DOWN Thm 1.2), record: forced windows ((q/p) = -1), and which of them have cap 0.
Report P(no forced window has cap 0 | k forced windows) against the independence prediction prod(1 - rho_q), the
pairwise correlation of cap-0 events, and the non-residue fraction of the "R_W-failure" primes (no cap-0 forced window
in the block) against all primes.
Usage: z51_linnik_windows.py P0 W y"""
import sys, math, json, random
import numpy as np
HARD = {1, 121, 169, 289, 361, 529}
def spf_table(n):
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, math.isqrt(n) + 1):
        if spf[i] == 0:
            blk = spf[i * i::i]; blk[blk == 0] = i
    return spf
def leg(a, q):
    r = pow(a % q, (q - 1) // 2, q); return 0 if r == 0 else (1 if r == 1 else -1)
def isprime(n):
    if n < 2: return False
    for d in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % d == 0: return n == d
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True
def main():
    P0, W, y = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    spf = spf_table((P0 + W + y) // 4 + 10)
    qs = [q for q in range(y // 2 + 1, y + 1) if q % 4 == 3 and isprime(q)]
    def cap0(p, q):
        x = (p + q) // 4
        f = {}; n = x
        while n > 1:
            r = int(spf[n]) or n; f[r] = f.get(r, 0) + 1; n //= r
        res = {1}
        for r, e in f.items():
            res = {(a * pow(r, k, q)) % q for a in res for k in range(e + 1)}
        allr = res | {(a * p) % q for a in res}
        return any((q - a) % q in allr for a in allr)
    recs = []
    for p in range(P0 | 1, P0 + W, 2):
        if p % 840 not in HARD or not isprime(p): continue
        row = {}
        for q in qs:
            if (p + q) % 4:                          # 4 | p + q (always for p == 1, q == 3 mod 4)
                continue
            row[q] = (leg(p, q) == -1, cap0(p, q))
        recs.append((p, row))
    # marginals
    rho = {q: (sum(1 for p, r in recs if q in r and r[q][0] and r[q][1]) /
               max(1, sum(1 for p, r in recs if q in r and r[q][0]))) for q in qs}
    rho_unf = {q: (sum(1 for p, r in recs if q in r and not r[q][0] and r[q][1]) /
                   max(1, sum(1 for p, r in recs if q in r and not r[q][0]))) for q in qs}
    byk = {}
    for p, r in recs:
        forced = [q for q in r if r[q][0]]
        k = len(forced)
        fail = all(not r[q][1] for q in forced)
        pred = math.prod(1 - rho[q] for q in forced)
        d = byk.setdefault(k, [0, 0, 0.0]); d[0] += 1; d[1] += fail; d[2] += pred
    # pairwise correlation of cap-0 events among forced windows
    cors = []
    for i, q in enumerate(qs):
        for q2 in qs[i + 1:]:
            xs = [(r[q][1], r[q2][1]) for p, r in recs if q in r and q2 in r and r[q][0] and r[q2][0]]
            if len(xs) > 200:
                a = np.array(xs, dtype=float)
                c = np.corrcoef(a[:, 0], a[:, 1])[0, 1]
                cors.append(c)
    # non-residue fraction among the windows, for failures vs all
    def nrfrac(rr):
        v = [sum(1 for q in r if r[q][0]) / len(r) for p, r in rr if r]
        return sum(v) / max(1, len(v))
    fails = [(p, r) for p, r in recs if all(not r[q][1] for q in r if r[q][0])]
    out = dict(P0=P0, W=W, y=y, nprimes=len(recs), windows=qs,
               rho_forced={q: round(v, 3) for q, v in rho.items()}, rho_unforced={q: round(v, 3) for q, v in rho_unf.items()},
               fail_by_k={k: dict(n=v[0], obs=round(v[1] / v[0], 4), indep=round(v[2] / v[0], 4)) for k, v in sorted(byk.items())},
               pair_corr_mean=round(float(np.mean(cors)), 4) if cors else None,
               pair_corr_min=round(float(np.min(cors)), 4) if cors else None, pair_corr_max=round(float(np.max(cors)), 4) if cors else None,
               nr_frac_all=round(nrfrac(recs), 4), nr_frac_fail=round(nrfrac(fails), 4), nfail=len(fails))
    print(json.dumps(out))
if __name__ == "__main__":
    main()
