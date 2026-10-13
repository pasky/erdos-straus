"""R201 from-scratch recomputation of GROWING_MUTE §4.1 (least overflow at primes p = 1 mod 4).

Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_gm_least.py PMAX KMAX BMAX

Stage 1 (COMPLETE, no k-bound): the B = 1 slice  D(2 lam A - 1) = pA^2 + 1, A even.  With D = 2A kap - 1
(D = -1 mod 2A is forced) this is  A(4 lam kap - p) = 2(lam + kap), symmetric in (lam, kap).  With
t := min(lam, kap) one has t <= (1 + sqrt(1+4p))/4 and the criterion  "p + 4t^2 has a divisor
d = -p (mod 4t)"  (d = 4 lam kap - p).  Both orderings give triples (g and D swap), so a triple with lam odd
exists iff some solution has lam or kap odd.
Stage 2: for primes with no B = 1 triple, search B odd squarefree, gcd(B, p) = 1, B <= BMAX, A = 2k, k <= KMAX,
g | pA^2 + B^2, g = -1 (mod 2AB); every hit is verified with exact rationals via review_gm_dict.classify.
"""
import sys
from math import gcd, isqrt
from sympy import factorint, primerange
from review_gm_dict import classify, shot_solution, sqfree


def divs(m):
    ds = [1]
    for p, e in factorint(m).items():
        ds = [d * p**i for d in ds for i in range(e + 1)]
    return ds


def b1_pairs(p):
    """All (lam, kap) solutions of A(4 lam kap - p) = 2(lam+kap) with A even (complete)."""
    out = set()
    T = (1 + isqrt(1 + 4 * p)) // 4 + 1
    for t in range(1, T + 1):
        for d in divs(p + 4 * t * t):
            if (d + p) % (4 * t):
                continue
            o = (p + d) // (4 * t)
            if (t + o) % d:
                continue
            A = 2 * (t + o) // d
            assert A % 2 == 0 and A * (4 * t * o - p) == 2 * (t + o)
            out.add((t, o, A))
            out.add((o, t, A))
    return out


def check_triple(p, A, B, g):
    lam = (g + 1) // (2 * A * B)
    x, y, z = shot_solution(p, lam * B * B, g)
    c = classify(p, x, y, z)
    assert c['adm'] and c['q'] == B and c['y1'], (p, A, B, g)
    return lam, (x, y, z)


def stage2(p, KMAX, BMAX, lam_odd):
    for B in range(3, BMAX + 1, 2):
        if gcd(B, p) != 1 or not sqfree(B):
            continue
        for k in range(1, KMAX + 1):
            A = 2 * k
            if gcd(A, B) != 1:
                continue
            for g in sorted(divs(p * A * A + B * B)):
                if (g + 1) % (2 * A * B) == 0:
                    lam, _ = check_triple(p, A, B, g)
                    if lam_odd and lam % 2 == 0:
                        continue
                    return B, k, g, lam
    return None


def main(PMAX, KMAX, BMAX):
    nP = noB1 = noB1odd = 0
    fails, fails_odd, maxA = [], [], 0
    for p in primerange(5, PMAX):
        if p % 4 != 1:
            continue
        nP += 1
        pairs = b1_pairs(p)
        for lam, kap, A in pairs:  # verify each B = 1 triple exactly
            g = 2 * lam * A - 1
            assert (p * A * A + 1) % g == 0
            assert check_triple(p, A, 1, g)[0] == lam
            maxA = max(maxA, A / (p + 1))
        if not pairs:
            noB1 += 1
            r = stage2(p, KMAX, BMAX, False)
            fails.append((p, r))
        if not any(l % 2 == 1 for l, _, _ in pairs):
            noB1odd += 1
            r = stage2(p, KMAX, BMAX, True)
            fails_odd.append((p, r))
    print(f'primes p=1(4), 5<=p<{PMAX}: {nP}; no B=1 triple at all: {noB1}; no B=1 triple with lam odd: {noB1odd}')
    print(f'max A/(p+1) over B=1 triples: {maxA:.4f}')
    print('no B=1 (any lam): (p, (B,k,g,lam) least-B with k<=KMAX)')
    for f in fails:
        print(' ', f)
    print('no B=1 with lam odd: (p, least (B,k,g,lam) with lam odd)')
    for f in fails_odd:
        print(' ', f)


if __name__ == '__main__':
    main(*(int(a) for a in sys.argv[1:4]))
