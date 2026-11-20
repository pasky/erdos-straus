"""Independent by-p replay of the Z72_PAIR_PHASE support-<=2 sieve (z74 Opus cross-review, lane Z72PHASE).

For every prime p = 1 mod 4 in [lo, hi] it searches c = 3, 7, 11, ... in increasing order, factors K = (p+c)/4 with
a smallest-prime-factor table and tests every Type II certificate with coprime AB | K, c | A+B and omega(AB) <= 2:
(1, q^i), (1, q^i r^j), (q^i, r^j). It shares no code with scripts/z72_two_support.cpp (which marks n = 4kD - c by k).
Each found certificate is re-checked as the integer identity p + c = 4ABD.

  ulimit -v 6000000; timeout 1800 uv run --offline --no-project --with numpy \
      python scripts/z74_xrev_z72phase_bypsieve.py LO HI
"""
import sys
import time
from array import array

import numpy as np


def main(lo, hi, dump=None):
    t0 = time.time()
    cpad = 20000
    kmax = max((hi + cpad) // 4, (hi + 1) // 2) + 2
    spf_np = np.zeros(kmax + 1, dtype=np.int32)
    lim = int(kmax ** 0.5) + 1
    for q in range(2, lim + 1):
        if spf_np[q] == 0:
            blk = spf_np[q * q::q]
            blk[blk == 0] = q
    idx = np.nonzero(spf_np == 0)[0]
    spf_np[idx] = idx.astype(np.int32)
    spf = array('i', spf_np.tobytes())
    del spf_np, idx
    # primes in [lo, hi] (segmented odd sieve using the spf table's small primes)
    base = [q for q in range(3, int(hi ** 0.5) + 2) if spf[q] == q]
    seg = np.ones(hi - lo + 1, dtype=np.bool_)
    for q in base:
        start = max(q * q, (lo + q - 1) // q * q)
        seg[start - lo::q] = False
    if lo <= 1:
        seg[:2 - lo] = False
    nums = np.nonzero(seg)[0] + lo
    primes = [int(p) for p in nums if p % 4 == 1]
    del seg, nums
    print(f'tables ready in {time.time() - t0:.1f}s; {len(primes)} primes p=1 mod 4 in [{lo},{hi}]', flush=True)

    tested = 0
    worst = (0, 0)
    first_over_123 = None
    worst_hard = (0, 0)  # p = 1 mod 840 with h = (p+1)/2 prime (the counter_tail family, below 10^18)
    hist = {}
    for p in primes:
        c = 3
        while True:
            K = (p + c) >> 2
            assert K < len(spf), 'spf table too small'
            fs = []
            k = K
            while k > 1:
                q = spf[k]
                e = 0
                pe = 1
                while k % q == 0:
                    k //= q
                    e += 1
                    pe *= q
                fs.append((q, e))
            found = None
            for q, e in fs:
                qi = 1
                for _ in range(e):
                    qi *= q
                    if (1 + qi) % c == 0:
                        found = (1, qi)
                        break
                if found:
                    break
            if not found:
                nf = len(fs)
                for a in range(nf):
                    q, e = fs[a]
                    for b in range(a + 1, nf):
                        r, f = fs[b]
                        qi = 1
                        for _ in range(e):
                            qi *= q
                            rj = 1
                            for _ in range(f):
                                rj *= r
                                if (1 + qi * rj) % c == 0:
                                    found = (1, qi * rj)
                                elif (qi + rj) % c == 0:
                                    found = (qi, rj)
                                if found:
                                    break
                            if found:
                                break
                        if found:
                            break
                    if found:
                        break
            if found:
                A, B = found
                assert K % (A * B) == 0 and (A + B) % c == 0 and p + c == 4 * A * B * (K // (A * B))
                break
            c += 4
            assert 3 * c <= p + 4, ('no support<=2 certificate', p)
        tested += 1
        if dump is not None and p < 200000:
            dump.append((p, c))
        hist[c] = hist.get(c, 0) + 1
        if c > worst[0]:
            worst = (c, p)
        if c > 123 and first_over_123 is None:
            first_over_123 = (p, c)
        if p % 840 == 1 and spf[(p + 1) // 2] == (p + 1) // 2 and c > worst_hard[0]:
            worst_hard = (c, p)
    print(f'by-p replay [{lo},{hi}]: {tested} primes p=1 mod 4, all have a support<=2 Type II certificate; '
          f'latest first shift {worst[0]} at p={worst[1]}; shifts used <=11: '
          f'{sum(v for k, v in hist.items() if k <= 11)}; time {time.time() - t0:.0f}s', flush=True)
    print(f'first prime with first shift > 123: {first_over_123}; latest first shift on p=1 mod 840 with (p+1)/2 '
          f'prime: {worst_hard[0]} at p={worst_hard[1]}', flush=True)


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
