"""R164 from-scratch spot-check of WINDMILL_REDUCTION §4 (Type I sigma-symmetric class, no enrichment).
For primes p = 1 (24) <= PMAX, c,d <= CMAX,DMAX, D = p^2+4c^2 d (nonsquare):
for every unordered factor pair {f, D/f} (f < sqrt D) we build the ambiguous form [f, f, (f - D/f)/4]
(disc D; D = 1 mod 4 so f = D/f mod 4) and decide, by Gauss reduction (independent of the river map),
whether it is properly equivalent to [c, p, -cd]. A pair is a certificate if f or D/f = -p (mod 4cd).
Reports: pairs in class / all pairs, certificate pairs in class / all certificate pairs; primitive pairs separately.
"""
import sys
from math import gcd, isqrt
from review_wr_zagier import canon, primes


def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
        i += 1
    return ds


def main(pmax, cmax, dmax, mode='all4'):
    P = [p for p in primes(pmax) if p % 24 == 1]
    tot = [0, 0, 0, 0]; prim = [0, 0, 0, 0]; cases = 0; amb = 0
    for p in P:
        for c in range(1, cmax + 1):
            for d in range(1, dmax + 1):
                D = p * p + 4 * c * c * d
                if isqrt(D) ** 2 == D:
                    continue
                cases += 1
                M = 4 * c * d
                C0 = canon((c, p, -c * d), D)
                # class ambiguous iff equivalent to its inverse
                amb += C0 == canon((c, -p, -c * d), D)
                for f in divisors(D):
                    g = D // f
                    if f * f >= D:
                        continue
                    form = (f, f, (f - g) // 4)
                    # all ambiguous forms attached to the pair: [+-f, f, .], [+-g, g, .]
                    forms4 = [(f, f, (f - g) // 4), (-f, f, (g - f) // 4), (g, g, (g - f) // 4), (-g, g, (f - g) // 4)]
                    inC = any(canon(h, D) == C0 for h in forms4) if mode == 'all4' else canon(form, D) == C0
                    cert = (f + p) % M == 0 or (g + p) % M == 0
                    isprim = gcd(gcd(form[0], form[1]), form[2]) == 1
                    for arr, use in ((tot, True), (prim, isprim)):
                        if use:
                            arr[0] += inC; arr[1] += 1; arr[2] += inC and cert; arr[3] += cert
    print(f"primes {len(P)}, (c,d) cases {cases}, ambiguous class {amb}")
    print(f"all pairs: in-class {tot[0]}/{tot[1]} = {tot[0]/tot[1]:.3f}; cert in-class {tot[2]}/{tot[3]} = {tot[2]/max(1,tot[3]):.3f}")
    print(f"primitive pairs: in-class {prim[0]}/{prim[1]} = {prim[0]/prim[1]:.3f}; cert in-class {prim[2]}/{prim[3]} = {prim[2]/max(1,prim[3]):.3f}")


if __name__ == "__main__":
    main(*map(int, sys.argv[1:4]), *(sys.argv[4:5]))
