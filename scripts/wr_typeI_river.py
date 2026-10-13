"""Type I: does the river of the sigma-symmetric form [c, p, -c d] (disc D = p^2 + 4c^2 d)
carry an ambiguous form whose divisor f satisfies the Type I condition f = -p (mod 4cd)? (O164 §4)

Type I (STATUS): ES(p) if f | p^2 + 4c^2 d with f = -p (mod 4cd).
River = orbit of R on simple forms a>0>c'.  Ambiguous simple form: a | b or c' | b.
Usage: python wr_typeI_river.py PMAX CMAX DMAX
"""
import sys
from math import gcd
from sympy import isprime, divisors


def R(f):
    a, b, c = f
    v = a + b + c
    return (v, b + 2 * c, c) if v > 0 else (a, b + 2 * a, v)


def river(f0, cap=10**6):
    out, f = [], f0
    while True:
        out.append(f)
        f = R(f)
        if f == f0 or len(out) > cap:
            return out


def main(pmax, cmax, dmax):
    ps = [p for p in range(25, pmax + 1, 24) if isprime(p)]
    tot = amb_cls = hit = anyok = hit_given_any = 0
    hit_primes = set()
    stat = [0, 0, 0, 0]
    any_primes = set()
    for p in ps:
        for c in range(1, cmax + 1):
            for d in range(1, dmax + 1):
                D = p * p + 4 * c * c * d
                M = 4 * c * d
                from math import isqrt
                if isqrt(D) ** 2 == D:
                    continue
                tot += 1
                riv = river((c, p, -c * d))
                fs = set()
                for (a, b, cc) in riv:
                    if b % a == 0:
                        fs.add(a)
                    if b % cc == 0:
                        fs.add(-cc)
                fs = {f for f in fs if D % f == 0}
                divs = [f for f in divisors(D) if f * f < D]
                cert = [f for f in divs if (f + p) % M == 0 or (D // f + p) % M == 0]
                ok_any = bool(cert)
                pairs_in = {min(f, D // f) for f in fs}
                stat[0] += len(pairs_in); stat[1] += len(divs)
                stat[2] += len(pairs_in & set(cert)); stat[3] += len(cert)
                ok_hit = any((f + p) % M == 0 or (D // f + p) % M == 0 for f in fs)
                amb_cls += bool(fs)
                hit += ok_hit
                anyok += ok_any
                hit_given_any += ok_hit and ok_any
                if ok_hit:
                    hit_primes.add(p)
                if ok_any:
                    any_primes.add(p)
    print("primes", len(ps), "pairs(c,d)", tot, "class ambiguous", amb_cls,
          "river-ambiguous hits", hit, "any-divisor ok", anyok,
          "primes hit", len(hit_primes), "primes any", len(any_primes))
    print("factor pairs in sigma-class / all:", stat[0], stat[1], "certificate pairs in sigma-class / all:", stat[2], stat[3])


if __name__ == "__main__":
    main(*map(int, sys.argv[1:4]))
