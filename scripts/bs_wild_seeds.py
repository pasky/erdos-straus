"""O153 W1 experiment: do Cornacchia seeds (p = u^2 + v^2) carry ES information beyond congruences?

For primes p = 1 (mod 24), p <= X, and prime e = 3 (mod 4), e <= EMAX, the e-slice
(LONGSHOT_PIGEONHOLE Lemma 1.1) succeeds iff -1 lies in Sigma_e(N) = prod_{l^v || N} {l^t : |t| <= v}
mod e, with N = (p+e)/4 (Type II) or (pe+1)/4 (Type I).
We compare the success rate among p that are squares mod e, split by whether e | v (non-congruence
condition on the representation) or e | u, or neither.
Usage: PYTHONPATH=scripts uv run python scripts/bs_wild_seeds.py X EMAX
"""
import sys
from math import isqrt
from sympy import factorint, primerange


def sigma_has_minus1(N, e):
    S = {1}
    for l, v in factorint(N).items():
        lm = l % e
        inv = pow(lm, -1, e)
        powers = {1}
        x = y = 1
        for _ in range(v):
            x = x * lm % e; y = y * inv % e
            powers.add(x); powers.add(y)
        S = {s * t % e for s in S for t in powers}
        if len(S) == e - 1:
            break
    return (e - 1) in S


def two_squares(p):
    # Cornacchia / brute: u odd, v even
    for v in range(0, isqrt(p) + 1, 2):
        r = p - v * v
        u = isqrt(r)
        if u * u == r:
            return u, v
    raise ValueError(p)


def main():
    X = int(sys.argv[1]); EMAX = int(sys.argv[2])
    es = [e for e in primerange(3, EMAX + 1) if e % 4 == 3]
    # stats[e][typ][cls] = [trials, successes], cls in {'v','u','none'}
    stats = {e: {t: {c: [0, 0] for c in ('v', 'u', 'none')} for t in ('II', 'I')} for e in es}
    for p in primerange(25, X + 1):
        if p % 24 != 1:
            continue
        u, v = two_squares(p)
        for e in es:
            if pow(p % e, (e - 1) // 2, e) != 1:
                continue  # only p that are squares mod e (congruence data held fixed)
            cls = 'v' if v % e == 0 else ('u' if u % e == 0 else 'none')
            for t, N in (('II', (p + e) // 4), ('I', (p * e + 1) // 4)):
                s = stats[e][t][cls]
                s[0] += 1
                s[1] += sigma_has_minus1(N, e)
    print(f"X={X} EMAX={EMAX}; rates = successes/trials among p=1(24), (p/e)=+1")
    for e in es:
        row = []
        for t in ('II', 'I'):
            for c in ('v', 'u', 'none'):
                n, k = stats[e][t][c]
                row.append(f"{t}/{c}: {k}/{n}={k / n:.3f}" if n else f"{t}/{c}: -")
        print(f"e={e:3d}  " + "  ".join(row))


if __name__ == "__main__":
    main()
