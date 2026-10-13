"""R165 from-scratch: R(p) = #{b >= 3 : j = (-p mod b) >= 1 and 4j | b+1}  (= #{(A,B,C): 4ABC - A - B = p}).
Complete range: b = f <= p + j with j <= (p+1)/3, so b <= (4p+1)/3 suffices.  Also the dyadic profile.
Cross-check at small p by direct (A,C) enumeration.  Usage: review_pf_R.py p"""
import sys
import numpy as np


def R_b(p, chunk=10 ** 7):
    bmax = (4 * p + 1) // 3 + 2
    hits = []
    for lo in range(3, bmax + 1, chunk):
        b = np.arange(lo, min(lo + chunk, bmax + 1), dtype=np.int64)
        j = (-p) % b
        m = j > 0
        bb, jj = b[m], j[m]
        ok = (bb + 1) % (4 * jj) == 0
        hits.extend(bb[ok].tolist())
    return hits


def R_ABC(p):
    cnt = 0
    for A in range(1, p + 1):
        if 4 * A - 1 > p + A: break
        C = 1
        while 4 * A * C - 1 <= p + A:
            cnt += (p + A) % (4 * A * C - 1) == 0
            C += 1
    return cnt


if __name__ == "__main__":
    for q in (101, 1009, 10007, 100003):
        assert len(R_b(q)) == R_ABC(q), q
    p = int(sys.argv[1])
    h = R_b(p)
    prof = {}
    for b in h:
        prof[b.bit_length()] = prof.get(b.bit_length(), 0) + 1
    print(f"p={p} p%840={p%840} R(p)={len(h)}")
    print("dyadic (bitlength:count):", dict(sorted(prof.items())))
