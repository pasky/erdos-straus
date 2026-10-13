"""R200 from-scratch recomputation of EXPONENT_CAP §5.1 (S = {3}) for primes 5 <= p < PMAX, j <= JMAX.
Factorisation by GNU coreutils `factor` (batched via stdin); divisor enumeration, admissibility and overflow
computed here independently of scripts/xc_leaste.py.  Also: T1 control on odd squares, and a comparison with
the author's data/xc/leaste_s3_primes.txt.gz.
Usage: review_xc_leaste.py PMAX JMAX
"""
import gzip, subprocess, sys
from collections import Counter
from fractions import Fraction as F


def primes_below(N):
    s = bytearray([1]) * N; s[0:2] = b"\0\0"
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(N) if s[i]]


def factor_batch(nums):
    out = subprocess.run(["factor"], input="\n".join(map(str, nums)) + "\n", capture_output=True,
                         text=True, check=True).stdout.splitlines()
    res = {}
    for line in out:
        a, b = line.split(":")
        fs = Counter(int(t) for t in b.split())
        res[int(a)] = fs
    return res


def divs(fs):
    ds = [1]
    for p, a in fs.items():
        ds = [d * p ** i for d in ds for i in range(a + 1)]
    return ds


def v3(x):
    c = 0
    while x % 3 == 0:
        x //= 3; c += 1
    return c


def best(n, J, fac):
    """least overflow e over admissible shots (Q=3^j, g | n+4Q^2, g==3 mod 4, j==0 or 3|(g+1)/4); also prime-g only"""
    be = bp = None; bj = bg = bk = None
    for j in range(J + 1):
        N = n + 4 * 9 ** j
        fs = fac[N]
        for g in divs(fs):
            if g % 4 != 3:
                continue
            K = (g + 1) // 4
            kap = v3(K)
            if j > 0 and kap == 0:
                continue
            e = max(0, j - kap)
            if be is None or e < be or (e == be and j < bj):
                be, bj, bg, bk = e, j, g, kap
            if is_prime_g(g, fs) and (bp is None or e < bp):
                bp = e
    return be, bj, bg, bk, bp


def is_prime_g(g, fs):
    return g in fs and fs[g] >= 1


def complete_upto(n, J):
    # all shots with overflow <= t have Q0 = 3^{j-e} <= Q1^2 (n+1)/2 (Thm 2.1 proof, both cases)
    t = -1
    while True:
        tt = t + 1
        if 3 ** (J - tt) >= 9 ** tt * F(n + 1, 2):
            t = tt
        else:
            return t


def verify(n, j, g):
    Q = 3 ** j; N = n + 4 * Q * Q; m = N // g
    x = (n + m) // 4; y = n * (g + 1) // 4; z = F(n * x * (g + 1), 4 * Q * Q)
    assert N % g == 0 and (n + m) % 4 == 0 and F(4, n) == F(1, x) + F(1, y) + 1 / z
    d = z.denominator
    while d % 3 == 0:
        d //= 3
    assert d == 1 and (z.denominator == 1 or y % 3 == 0)
    return v3(z.denominator) // 2


def main(PMAX, J):
    ps = [p for p in primes_below(PMAX) if p >= 5]
    nums = sorted({p + 4 * 9 ** j for p in ps for j in range(J + 1)})
    fac = {}
    for i in range(0, len(nums), 20000):
        fac.update(factor_batch(nums[i:i + 20000]))
    hist = Counter(); histp = Counter(); mine = {}
    e0_p4 = 0; unsolved = []
    for p in ps:
        be, bj, bg, bk, bp = best(p, J, fac)
        if be is None:
            unsolved.append(p); continue
        assert verify(p, bj, bg) == be
        hist[be] += 1; histp[bp] += 1
        if be == 0 and bj == 0:
            e0_p4 += 1
        mine[p] = (be, bp, complete_upto(p, J))
    print(f"primes={len(ps)} unsolved={unsolved[:10]} least-e hist={sorted(hist.items())}")
    print(f"  e=0 via j=0: {e0_p4}; prime-g least-e max={max(k for k in histp if k is not None)}")
    print(f"  completeness t: {Counter(v[2] for v in mine.values())}")
    # compare with author's file
    diff = 0; cmp = 0
    with gzip.open("data/xc/leaste_s3_primes.txt.gz", "rt") as fh:
        for line in fh:
            c = list(map(int, line.split()))
            if c[0] in mine:
                cmp += 1
                if (c[1], c[5]) != mine[c[0]][:2]:
                    diff += 1
                    if diff <= 5: print("  DIFF", c, mine[c[0]])
    print(f"  compared with author rows: {cmp}, differences (least e, least prime-g e): {diff}")


def t1(MMAX, J):
    sq = [m * m for m in range(3, MMAX, 2) if m % 3]
    nums = sorted({n + 4 * 9 ** j for n in sq for j in range(J + 1)})
    fac = {}
    for i in range(0, len(nums), 20000):
        fac.update(factor_batch(nums[i:i + 20000]))
    hits = sum(1 for n in sq for j in range(J + 1) for g in divs(fac[n + 4 * 9 ** j]) if g % 4 == 3)
    print(f"T1 control: {len(sq)} odd squares m^2 (3 ∤ m, m < {MMAX}), j <= {J}: divisors ≡ 3 mod 4 found: {hits}")


if __name__ == "__main__":
    PMAX = int(sys.argv[1]); J = int(sys.argv[2])
    main(PMAX, J)
    t1(1000, 30)
