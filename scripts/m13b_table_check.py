"""m13b_table_check.py — validate Lemma 1.1 of POINTWISE_MORDELL13B.md.

For random family parameters P (all seven ET Prop 1.9 families), random T-units-ish
parameters (factors 11, 13 inserted at random) and random u (integer prime to 2*3*11*13... any
u prime to 143), compare
  (A) membership of the T-generic point x(u) (x_q = u for q in T={11,13}, x_q = 1 otherwise)
      in the class, read off mordell_lib.cls_modulus_residues: some residue r mod M with
      r = 1 mod M', r = u mod M_T   (M' = T-free part, M_T = T-part of M);
  (B) the closed-form conditions of Lemma 1.1.
usage: PYTHONPATH=scripts uv run python scripts/m13b_table_check.py [trials] [seed]
"""
import random
import sys
from math import gcd

from mordell_lib import cls_modulus_residues

T = (11, 13)


def tpart(m):
    r = 1
    for q in T:
        while m % q == 0:
            m //= q
            r *= q
    return r


def member(fam, P, u, w=1):
    M, res = cls_modulus_residues(fam, P)
    MT = tpart(M)
    Mp = M // MT
    return any((r - w) % Mp == 0 and (r - u) % MT == 0 for r in res)


def table(fam, P, u, w=1):
    if fam in ('I1', 'II3', 'II1', 'I4'):
        a, d, e = P  # (a,d,f) for I1 ; (a,d,e) for II3 ; (a,b,e) for II1/I4
        m = a * d
        mT = tpart(m)
        mp = m // mT
        if fam == 'I4':
            return (w * e + 1) % (4 * mp) == 0 and (u * e + 1) % mT == 0
        ok = (e + w) % (4 * mp) == 0 and (e + u) % mT == 0
        if fam == 'II3':
            eT = tpart(e)
            ok = ok and (4 * a * a * d + w) % (e // eT) == 0 and (u + 4 * a * a * d) % eT == 0
        return ok
    if fam == 'I2':
        a, c, f = P
        m = a * c
        mT = tpart(m)
        fT = tpart(f)
        return ((f + w) % (4 * (m // mT)) == 0 and (f + u) % mT == 0
                and (w * a + c) % (f // fT) == 0 and (c + u * a) % fT == 0)
    if fam == 'I3':
        c, d, f = P
        m = c * d
        mT = tpart(m)
        fT = tpart(f)
        return ((f + w) % (4 * (m // mT)) == 0 and (f + u) % mT == 0
                and (4 * c * c * d + w * w) % (f // fT) == 0 and (u * u + 4 * c * c * d) % fT == 0)
    if fam == 'II2':
        a, d, f = P
        fT = tpart(f)
        return (4 * a * a * d + w) % (f // fT) == 0 and (u + 4 * a * a * d) % fT == 0
    raise ValueError(fam)


def rnd(rng, maxv=60):
    x = rng.randint(1, maxv)
    for q in T:
        x *= q ** rng.choice((0, 0, 1, 2))
    return x


def random_params(fam, rng, u):
    """Random valid family parameters; biased so that membership happens often."""
    for _ in range(10000):
        if fam == 'I1':
            a, d = rnd(rng), rnd(rng)
            N = 4 * a * a * d + 1
            fs = [f for f in range(1, min(N, 10 ** 6) + 1) if N % f == 0] if N < 10 ** 6 else [1, N]
            return (a, d, rng.choice(fs))
        if fam in ('II1', 'I4'):
            a, b = rnd(rng), rnd(rng)
            es = [e for e in range(1, a + b + 1) if (a + b) % e == 0 and gcd(e, 4 * a * b) == 1]
            return (a, b, rng.choice(es))
        if fam == 'II2':
            a, d = rnd(rng, 20), rnd(rng, 20)
            # f = 4ad m - 1 with m random; bias: choose f with T-part
            m = rng.randint(1, 3000)
            return (a, d, 4 * a * d * m - 1)
        if fam in ('I2', 'I3', 'II3'):
            a, c = rnd(rng, 30), rnd(rng, 30)
            f = rng.randint(1, 4000) * rng.choice((1, 11, 13, 121, 143))
            if gcd(4 * a * c, f) == 1:
                if fam == 'I3' and f > 1:
                    # need f | something with sqrt; cls handles empty root sets
                    pass
                return (a, c, f)
    raise RuntimeError


def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    rng = random.Random(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    fams = ['I1', 'I2', 'I3', 'I4', 'II1', 'II2', 'II3']
    stats = {f: [0, 0] for f in fams}
    bad = 0
    for t in range(trials):
        fam = fams[t % 7]
        u = rng.choice([v for v in range(1, 143 * 13) if gcd(v, 143) == 1])
        P = random_params(fam, rng, u)
        w = 1
        # force a hit half of the time: take (u, w) from a class residue (general off-T value w)
        if rng.random() < 0.5:
            M, res = cls_modulus_residues(fam, P)
            if not res:
                continue
            r = rng.choice(res)
            u, w = r % tpart(M), r
            if gcd(u, 143) != 1 or gcd(w, M // tpart(M)) != 1:
                continue
            if rng.random() < 0.3:
                u = (u + tpart(M) // 11 if tpart(M) % 11 == 0 else u + 1)  # near miss
        elif rng.random() < 0.5:
            w = rng.randint(1, 10 ** 6)
        A = member(fam, P, u, w)
        B = table(fam, P, u, w)
        stats[fam][0] += 1
        stats[fam][1] += A
        if A != B:
            bad += 1
            if bad < 10:
                print('MISMATCH', fam, P, u, A, B)
    for f in fams:
        print(f, 'trials', stats[f][0], 'members', stats[f][1])
    print('mismatches', bad)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
