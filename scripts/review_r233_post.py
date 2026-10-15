"""R233 post-processing of review_r233_census output (lines: n Ntot Nm U U2 minmin).
 - psi-odd part of n+1 for the N- < U/2 failures
 - Landau triple <=> minmin >= 3 (Cor 1.2), Landau depth K(p) histogram, minmin vs K+1
 - min N-/U split by psi-odd profile of n+1."""
import sys
from collections import Counter
from sympy import factorint
from review_r233_common import jacobi

fn = sys.argv[1]
depth_mode = len(sys.argv) > 2 and sys.argv[2] == 'depth'


def psi_odd(x, n):
    return {r: e for r, e in factorint(x).items() if jacobi(r, n) == -1}


def isclean(x, n):
    return not psi_odd(x, n)


rows = [tuple(map(int, l.split())) for l in open(fn)]
print("failures 2N- < U:")
for n, N, Nm, U, U2, mm in rows:
    if 2 * Nm < U:
        print(" ", n, n % 8, "psi-odd part of n+1:", psi_odd(n + 1, n), "factor n:", factorint(n))
mism = 0
prof = {}
Kh = Counter()
Kexcess = Counter()
for n, N, Nm, U, U2, mm in rows:
    lt = isclean(n + 1, n) and isclean(n + 2, n) and isclean(2 * n + 1, n)
    if lt != (mm >= 3 or U == 0):
        mism += 1
    po = psi_odd(n + 1, n)
    key = 'clean' if not po else ('odd-exp' if any(e % 2 for e in po.values()) else
                                  ('3^2' if po == {3: 2} else 'other-even'))
    st = prof.setdefault(key, [0, 9.0, 0])
    st[0] += 1
    st[1] = min(st[1], Nm / U) if U else st[1]
    st[2] += (2 * Nm < U)
    if depth_mode:
        s = 1
        while isclean(n + s, n) and isclean(s * n + 1, n):
            s += 1
        K = s - 1
        Kh[K] += 1
        if K >= 2:
            Kexcess[(K, mm - (K + 1))] += 1
print("Landau-triple <=> minmin>=3 mismatches:", mism, "of", len(rows))
print("profile of n+1: [count, min N-/U, #failures]")
for k, v in sorted(prof.items()):
    print(" ", k, v)
if depth_mode:
    print("K histogram", sorted(Kh.items()))
    print("(K, minmin-(K+1)) for K>=2", sorted(Kexcess.items()))
