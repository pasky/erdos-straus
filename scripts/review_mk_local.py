"""R202 from-scratch check of MARKOFF_ES Lemma 3.1, Cor 3.2, Props 3.3/3.4 (local parts).

(1) Lemma 3.1: for each n and D <= Dmax, decide existence of l-adic admissible points of
    nA^2 + B^2 + D = 2 D lam A B  (not l|A&l|B; l|n => l∤B; l=2: A even, B odd)
    for every prime l | 2nD by integer search (A, B < l^E; lam l-integral iff valuation inequality),
    and compare with the closed-form criterion (D = 3 mod 4, gcd(D,n)=1, (-n/l)=1 for l | D).
(2) Prop 3.4: for admissible D and l = 3 mod 4 with v_l(D) odd, collect the pairs
    ((A,-D)_l, (B,-nD)_l) over admissible l-adic points; must be all four.
(3) Prop 3.3 (n = m^2): over family l-adic points (A, B, lam, with D = (nA^2+B^2)/(2 lam A B - 1) in Z_l),
    inv_l (-1, D) = 0 for odd l and D = 3 mod 4 at l = 2.
Usage: review_mk_local.py Dmax n [n ...]
"""
import sys
from math import gcd


def primes_of(m):
    out, p = [], 2
    while p * p <= m:
        if m % p == 0:
            out.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        out.append(m)
    return out


def v(l, x):
    if x == 0:
        return 10 ** 9
    c = 0
    while x % l == 0:
        x //= l
        c += 1
    return c


def leg(a, l):
    a %= l
    if a == 0:
        return 0
    return 1 if pow(a, (l - 1) // 2, l) == 1 else -1


def hilbert_odd(a, b, l):
    al, bl = v(l, a), v(l, b)
    u, w = a // l ** al, b // l ** bl
    s = (-1) ** (al * bl * ((l - 1) // 2))
    return s * leg(u, l) ** bl * leg(w, l) ** al


def local_points(n, D, l, E):
    """yield (A, B) integers representing admissible l-adic points."""
    mod = l ** E
    for A in range(1, mod):
        for B in range(1, mod):
            if A % l == 0 and B % l == 0:
                continue
            if n % l == 0 and B % l == 0:
                continue
            if l == 2 and not (A % 2 == 0 and B % 2 == 1):
                continue
            if v(l, n * A * A + B * B + D) >= v(l, 2 * D) + v(l, A) + v(l, B):
                yield A, B


def criterion(n, D):
    return D % 4 == 3 and gcd(D, n) == 1 and all(leg(-n, l) == 1 for l in primes_of(D) if l > 2)


def main():
    Dmax = int(sys.argv[1])
    bad = 0
    stats = dict(checked=0, adm=0, p34_ok=0, p34_bad=0, p33_bad=0)
    for n in map(int, sys.argv[2:]):
        for D in range(1, Dmax + 1):
            ok = True
            for l in sorted(set(primes_of(2 * D * n))):
                E = v(l, 2 * D) + 2 if l == 2 else max(v(l, D), 1)
                if not any(True for _ in local_points(n, D, l, E)):
                    ok = False
                    break
            stats['checked'] += 1
            if ok != criterion(n, D):
                bad += 1
                print("Lemma 3.1 MISMATCH", n, D, ok, criterion(n, D))
            if ok:
                stats['adm'] += 1
                for l in primes_of(D):
                    if l % 4 == 3 and v(l, D) % 2 == 1:
                        pats = set()
                        for A, B in local_points(n, D, l, v(l, D) + 1):
                            pats.add((hilbert_odd(A, -D, l), hilbert_odd(B, -n * D, l)))
                        if len(pats) == 4:
                            stats['p34_ok'] += 1
                        else:
                            stats['p34_bad'] += 1
                            print("Prop 3.4: patterns", n, D, l, pats)
                        break
        r = int(round(n ** .5))
        if r * r == n:  # Prop 3.3 at odd l <= 13 and at 2
            for l in (2, 3, 5, 7, 11, 13):
                mod = l ** 2 if l > 2 else 16
                for A in range(1, mod):
                    for B in range(1, mod):
                        if (A % l == 0 and B % l == 0) or (n % l == 0 and B % l == 0):
                            continue
                        if l == 2 and not (A % 2 == 0 and B % 2 == 1):
                            continue
                        for lam in range(1, (l if l > 2 else 8) + 1):
                            num, den = n * A * A + B * B, 2 * lam * A * B - 1
                            if v(l, num) < v(l, den) or v(l, num) > 50:
                                continue
                            if l == 2:
                                Dm = (num * pow(den, -1, 2 ** 10)) % 2 ** 10
                                if Dm % 4 != 3:
                                    stats['p33_bad'] += 1
                            else:
                                vD = v(l, num) - v(l, den)
                                if vD % 2 == 1 and leg(-1, l) == -1:
                                    stats['p33_bad'] += 1
                                    print("Prop 3.3 bad", n, l, A, B, lam)
    print("Lemma 3.1 mismatches:", bad, stats)


if __name__ == "__main__":
    main()
