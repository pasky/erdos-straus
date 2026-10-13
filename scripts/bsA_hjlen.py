"""bsA_hjlen: HJ length r(n/A) statistics; Farey least non-residue lambda(p).
Usage: PYTHONPATH=scripts uv run python scripts/bsA_hjlen.py [check|stats PMAX]"""
import sys, math
from sympy import primerange, jacobi_symbol

def hj_direct(n, A):
    r = 0
    while A > 0:
        b = -(-n // A); n, A = A, b * A - n; r += 1
    return r

def hj_len(n, A):
    # r = 1 + sum of odd-indexed regular partial quotients of n/A = [a0;a1,...]
    # with the standard expansion [a0;...,a_k] (a_k>=2): r = 1+sum_odd if k even, sum_odd if k odd (validated in 'check')
    q = []
    a, b = n, A
    while b:
        q.append(a // b); a, b = b, a % b
    k = len(q) - 1
    return sum(q[1::2]) + (1 if k % 2 == 0 else 0)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    if mode == "check":
        bad = 0
        for n in range(2, 400):
            for A in range(1, n):
                if math.gcd(A, n) == 1 and hj_direct(n, A) != hj_len(n, A):
                    bad += 1
        print("hj_len vs direct, n<400: failures", bad)
    else:
        P = int(sys.argv[2])
        for p in primerange(10**3, P):
            if p % 8 != 1: continue
            rs = sorted(hj_len(p, A) for A in range(1, p))
            lam = min(hj_len(p, A) for A in range(1, p) if jacobi_symbol(A, p) == -1)
            mean = sum(rs) / len(rs)
            L = math.log(p)
            print(p, "lam", lam, "median", rs[len(rs)//2], "mean %.1f" % mean,
                  "med/(lnp lnlnp) %.3f" % (rs[len(rs)//2] / (L*math.log(L))),
                  "mean/ln2p %.3f" % (mean / L**2))
