"""O31 (POINTWISE_TYPEI.md §5, EVIDENCE): ck_min(p) versus n_p for hard primes p=1 (24).

ck_min (notes (48.9)) = least ck over slices (c,k) in B_p with sf(c) not in {1,2,3,6} and
M_{c,k}(p)>0.  Forced slices (chi_s(p)=+1) are skipped by Thm 48.1 (M=0); the check `--noskip`
recomputes them to confirm.  Output: per-p lines (p, n_p, ck_min) to a file, plus a summary of the
ratio ck_min/n_p and records."""
import sys
from sympy import primerange, factorint, legendre_symbol
from itertools import product


def sf(c):
    r = 1
    for q, e in factorint(c).items():
        if e % 2:
            r *= q
    return r


def divs_from_fac(fac):
    ds = [1]
    for q, e in fac.items():
        ds = [d * q ** i for d in ds for i in range(e + 1)]
    return ds


def chi_minus_s(s, p):
    # (-s/p) for p = 1 (mod 4): product of (q/p) over q | s
    v = 1
    for q in factorint(s):
        v *= legendre_symbol(q % p, p)
    return v


def ckmin(p, cklim, skip=True):
    for P in range(1, cklim + 1):
        if P % p == 0:
            continue
        for c in range(1, P + 1):
            if P % c:
                continue
            k = P // c
            s = sf(c)
            if s in (1, 2, 3, 6) or k > 2 * p // 3 or c > (2 * p + k) // (4 * k):
                continue
            if skip and chi_minus_s(s, p) == 1:
                continue
            h = 4 * c * k
            N = p * p + 4 * c * k * k
            if any((d + p) % h == 0 for d in divs_from_fac(factorint(N))):
                return P
    return None


def least_qnr(p):
    a = 2
    while legendre_symbol(a, p) == 1:
        a += 1
    return a


if __name__ == "__main__":
    X0, X, cklim = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    out = sys.argv[4] if len(sys.argv) > 4 else None
    noskip = "--noskip" in sys.argv
    rows = []
    for p in primerange(X0, X):
        if p % 24 != 1:
            continue
        n = least_qnr(p)
        cm = ckmin(p, cklim, skip=not noskip)
        rows.append((p, n, cm))
    if out:
        with open(out, "w") as f:
            for r in rows:
                f.write("%d %d %s\n" % r)
    cens = [r for r in rows if r[2] is None]
    viol = [r for r in rows if r[2] is not None and r[2] < r[1]]
    rat = sorted(((r[2] / r[1]) if r[2] else float("inf"), r) for r in rows)
    print(f"primes p=1(24) in [{X0},{X}): {len(rows)}; ck_min<n_p violations: {len(viol)}; censored(>{cklim}): {len(cens)}")
    print("eq ck_min==n_p:", sum(1 for r in rows if r[2] == r[1]))
    print("top ratios ck_min/n_p:", [(round(a, 2), r) for a, r in rat[-12:]])
    recs, best = [], 0
    for r in rows:
        if r[2] is not None and r[2] > best:
            best = r[2]
            recs.append(r)
    print("ck_min records (p,n_p,ck_min):", recs)
    sys.exit(1 if viol else 0)
