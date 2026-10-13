"""O165 numerics: the (A)3 family at a fixed prime p, in the one-variable form
   success(b)  :<=>  A := (-p mod b) satisfies 4A | b+1     (b = 4AC-1, Lemma 1.1 with h = 1)
over b <= Bmax (Bmax = p+1 gives the full (A)3 count R(p); b <= p+A always, A < b).
Also general h: success_h(m), m = 4hj-1:  k := (-hp mod m) divides j.   (Lemma 1.1)
Reports: counts, dyadic profile, Liouville parity of b and of p+A at successes, and the
Q-character/spin statistics.  Usage:  pf_mass.py p Bmax [hmax]
"""
import sys
import numpy as np
from sympy import factorint, isprime


def successes_h1(p, Bmax, chunk=10**7):
    out = []
    lo = 3
    while lo <= Bmax:
        hi = min(Bmax, lo + chunk - 1)
        b = np.arange(lo, hi + 1, dtype=np.int64)
        A = (-p) % b
        ok = (A > 0) & (((b + 1) % (4 * np.maximum(A, 1))) == 0)
        out.extend(b[ok].tolist())
        lo = hi + 1
    return out


def successes_h(p, h, Jmax, chunk=10**7):
    """m = 4hj-1, j<=Jmax; k = (-h p) mod m must divide j (then d = j/k)."""
    out = []
    lo = 1
    while lo <= Jmax:
        hi = min(Jmax, lo + chunk - 1)
        j = np.arange(lo, hi + 1, dtype=np.int64)
        m = 4 * h * j - 1
        k = (-(h % m) * (p % m)) % m  # h*p may overflow for big p: reduce first
        ok = (k > 0) & ((j % np.maximum(k, 1)) == 0)
        out.extend(zip(j[ok].tolist(), k[ok].tolist()))
        lo = hi + 1
    return out


def liou(n):
    return (-1) ** sum(factorint(n).values())


if __name__ == "__main__":
    p = int(sys.argv[1]); Bmax = int(sys.argv[2]); hmax = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    assert isprime(p)
    S = successes_h1(p, Bmax)
    print(f"p={p} p%840={p%840} Bmax={Bmax:.3g}  R_1(p; b<=Bmax) = {len(S)}")
    prof = {}
    for b in S:
        e = b.bit_length() - 1
        prof[e] = prof.get(e, 0) + 1
    print(" dyadic profile log2(b):count ", " ".join(f"{e}:{c}" for e, c in sorted(prof.items())))
    lb = [liou(b) for b in S]
    lN = [liou(p + ((-p) % b)) for b in S]
    print(f" sum lambda(b) over successes = {sum(lb)} ; sum lambda(p+A) = {sum(lN)} ; n = {len(S)}")
    # h>1 (truncated: m <= 4h*Jmax)
    for h in range(2, hmax + 1):
        Jmax = min(Bmax // (4 * h), (h * p) // (4 * h) + 1)
        T = successes_h(p, h, Jmax)
        print(f" h={h}: count with m=4hj-1, j<={Jmax:.3g}: {len(T)}")
