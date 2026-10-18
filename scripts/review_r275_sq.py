"""R275 from-scratch checks for MODP_RECIPROCITY §4: Prop 4.1 identities and EVIDENCE 4.2 (square levels favoured).
Usage: review_r275_sq.py PLO PHI DLO DHI"""
import sys
from math import isqrt, gcd
import numpy as np


def spf_sieve(n):
    s = np.zeros(n + 1, dtype=np.int64)
    for i in range(2, isqrt(n) + 1):
        if s[i] == 0:
            blk = s[i*i::i]; blk[blk == 0] = i
    idx = np.nonzero(s == 0)[0]; s[idx] = idx
    return s


def factor(n, spf):
    f = {}
    while n > 1:
        q = int(spf[n]); f[q] = f.get(q, 0) + 1; n //= q
    return f


def divs(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds


def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0


def two_sq(p):
    for b in range(2, isqrt(p) + 1, 2):
        a = isqrt(p - b * b)
        if a * a == p - b * b: return a, b


def phi(n, spf):
    r = n
    for q in factor(n, spf): r = r // q * (q - 1)
    return r


def main():
    PLO, PHI, DLO, DHI = map(int, sys.argv[1:5])
    spf = spf_sieve(PHI + 4 * DHI + 10)
    # Prop 4.1
    n = f = 0
    for p in range(5, 20001, 4):
        if spf[p] != p: continue
        a, b = two_sq(p)
        for k in range(1, 12):
            for l in factor(p + 4 * k * k, spf):
                if l == 2 or k % l == 0: continue
                n += 1
                if (l % 4 == 3) != (jacobi(l, p) == -1): f += 1; continue
                if l % 4 == 1:
                    c, e = two_sq(l)
                    s_pl = 1 if pow(p, (l - 1) // 4, l) == 1 else -1
                    s_lp = 1 if pow(l, (p - 1) // 4, p) == 1 else -1
                    if s_pl != jacobi(k, l) or s_lp != jacobi(k, l) * jacobi(a * c - b * e, l): f += 1
    print(f"Prop 4.1: {n} triples (p<=2e4, k<=11, l | p+4k^2), {f} violations")
    # EVIDENCE 4.2
    P = [p for p in range(PLO + (1 - PLO) % 4, PHI + 1, 4) if spf[p] == p]
    cnt = {'sq': [0, 0], 'ns+': [0, 0], 'ns-': [0, 0]}
    c1 = {'sq': [0, 0], 'ns': [0, 0]}   # hits by a c=1 witness (w = 4d-1)
    for p in P:
        for d in range(DLO, DHI + 1):
            N = p + 4 * d
            ws = [w for w in divs(factor(N, spf)) if w % (4 * d) == 4 * d - 1 and w < N]
            h = bool(ws)
            key = 'sq' if isqrt(d)**2 == d else ('ns+' if jacobi(d, p) == 1 else 'ns-')
            cnt[key][0] += 1; cnt[key][1] += h
            k2 = 'sq' if key == 'sq' else 'ns'
            c1[k2][0] += 1; c1[k2][1] += (N % (4 * d - 1) == 0)
    print(f"EVIDENCE 4.2: {len(P)} primes p=1(4) in [{PLO},{PHI}], levels {DLO}..{DHI}")
    for k, (t, h) in cnt.items(): print(f"  {k:4s}: {h}/{t} = {100*h/t:.3f} %")
    for k, (t, h) in c1.items(): print(f"  c=1 witness w=4d-1 divides p+4d, {k}: {100*h/t:.3f} %")
    # naive prediction sum_c 1/phi(4cd-1), w <= W
    W = (PLO + PHI) // 2
    S = {'sq': [], 'ns': []}; S1 = {'sq': [], 'ns': []}
    for d in range(DLO, DHI + 1):
        k2 = 'sq' if isqrt(d)**2 == d else 'ns'
        tot = 0.0; c = 1
        while 4 * c * d - 1 <= W:
            tot += 1 / phi(4 * c * d - 1, spf); c += 1
        S[k2].append(tot); S1[k2].append(1 / phi(4 * d - 1, spf))
    m = {k: sum(v) / len(v) for k, v in S.items()}; m1 = {k: sum(v) / len(v) for k, v in S1.items()}
    print(f"  naive E#witnesses sum_c 1/phi(4cd-1) (w<={W}): sq {m['sq']:.5f}, ns {m['ns']:.5f}, ratio {m['sq']/m['ns']:.3f}")
    print(f"  c=1 term alone 1/phi(4d-1): sq {m1['sq']:.6f}, ns {m1['ns']:.6f}, ratio {m1['sq']/m1['ns']:.3f}")
    print(f"  observed ratio sq / all-nonsquare: "
          f"{(cnt['sq'][1]/cnt['sq'][0]) / ((cnt['ns+'][1]+cnt['ns-'][1])/(cnt['ns+'][0]+cnt['ns-'][0])):.3f}")


if __name__ == "__main__":
    main()
