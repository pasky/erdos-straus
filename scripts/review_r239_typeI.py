#!/usr/bin/env python3
"""R239 from-scratch check of Prop 4.1 (Type I windows), with GENERAL y (author only treats a | y).
x = p*a, a = (p k' + 1)/4; 4/p - 1/x = k'/a = 1/y + 1/z, z rational.  ES^{(y,inf)} condition: den z odd square,
coprime to p, every prime of den z divides y.  Usage: review_r239_typeI.py PMAX KMAX YMAX
"""
import sys
from fractions import Fraction
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from review_r239_windows import sieve_spf, jacobi, factor


def ok_den(d, p, y):
    if d % 2 == 0 or d % p == 0:
        return False
    r = int(round(d ** 0.5))
    while r * r > d: r -= 1
    while (r + 1) ** 2 <= d: r += 1
    if r * r != d:
        return False
    t = r
    for l in range(3, int(t ** 0.5) + 2, 2):
        if t % l == 0:
            if y % l: return False
            while t % l == 0: t //= l
    return t == 1 or y % t == 0


def main():
    PM, KM, YM = map(int, sys.argv[1:4])
    spf = sieve_spf(PM * KM + 10)
    isprime = lambda k: k > 1 and spf[k] == k
    ident = 0; dead_pred = 0; dead_viol = 0; dead_viol_adivy = 0; live_found = 0; live = 0; sols_a_ndiv_y = 0
    for p in range(5, PM + 1, 4):
        if not isprime(p): continue
        for kp in range(3, KM + 1, 4):
            if not isprime(kp) or kp == p: continue
            a = (p * kp + 1) // 4
            af = factor(a, spf)
            for s in af:
                if s != 2:
                    assert jacobi(s, kp) == jacobi(s, p); ident += 1
            assert jacobi(a, p) == 1
            pred = all(jacobi(s, p) == 1 for s in af if s != 2) and (a % 2 == 1 or kp % 8 == 7)
            nsol = 0
            for y in range(a // kp + 1, YM + 1):
                den = kp * y - a
                if den <= 0: continue
                z = Fraction(a * y, den)
                if ok_den(z.denominator, p, y):
                    nsol += 1
                    if y % a: sols_a_ndiv_y += 1
            if pred:
                dead_pred += 1
                if nsol: dead_viol += 1
            else:
                live += 1
                if nsol: live_found += 1
    print("symbol identities (a):", ident)
    print("predicted-dead windows:", dead_pred, " violations (any y <= %d):" % YM, dead_viol)
    print("other windows:", live, " with a solution found:", live_found)
    print("solutions with a not dividing y (general-y family):", sols_a_ndiv_y)


if __name__ == "__main__":
    main()
