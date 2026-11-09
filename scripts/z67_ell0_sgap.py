"""z67 ELL0: close the (S)-gap 101 < ell < 10^5 of Z66_UCOVER Theorem S by a *global* mass certificate per prime.

For a prime ell the caught set C^S_ell = {g in Z_ell^x : e_{ell,g} lies in some good-word class} is a union of cylinders
rho + ell^k Z_ell over the good caught unit residues rho of level k (UCOVER Lemma S1), all at quadratic non-residues.
Sub-additivity gives
    mu(C^S_ell) <= sum_{k <= K} |E_k| / phi(ell^k) + sum_{k > K} T_k(ell),
with E_k computed exactly by scripts/z66_ucover_swords.c and T_k the UCOVER Lemma S2' majorant
    T_k = ell/(ell-1) (k+2)(2.44 k ln ell + 10.15) ell^{-k/2}   (valid for ell^k >= 10^5),
evaluated in mpmath interval arithmetic (upper endpoint, converted exactly).  If the bound is < 1/2 = mass of the
non-residues, some non-residue g has e_{ell,g} in U_S (the complement of an open set of smaller mass).
K is increased from 1 until the certificate holds (or KMAX is reached).
Usage: uv run --with mpmath --with sympy python scripts/z67_ell0_sgap.py LO HI [KMAX] [binary] [workers]
Output: one line per prime: ell K exact_part tail total verdict.
"""
import math
import subprocess
import sys
from fractions import Fraction
from multiprocessing import Pool

BIN = "/tmp/zsw"
KMAX = 4


def caught(ell, k):
    out = subprocess.run([BIN, str(ell), str(k)], capture_output=True, text=True, check=True)
    res = set()
    for line in out.stdout.splitlines():
        t = line.split()
        r = int(t[1])
        if r % ell == 0:
            continue
        nonres = pow(r % ell, (ell - 1) // 2, ell) == ell - 1
        if t[0] == "W1":
            if k % 2 == 1 and nonres:
                res.add(r)
        elif t[4] == "1":
            assert nonres, "good W2 event at a residue?!"
            res.add(r)
    cand = int(out.stderr.strip().split("candidates_scanned=")[1])
    N = ell ** k
    if N >= 10 ** 5:
        assert cand <= math.isqrt(N + 1) * (k + 2) * (2.44 * math.log(N) + 10.15), "majorant violated"
    return len(res), cand


def tail_upper(ell, K):
    """Rigorous upper bound for sum_{k>K} T_k(ell) (same construction as z66_ucover_stree.tail_upper)."""
    from mpmath import iv
    iv.dps = 40
    L = iv.mpf(ell)
    lnl = iv.log(L)

    def T(k):
        return L / (L - 1) * (k + 2) * (iv.mpf("2.44") * k * lnl + iv.mpf("10.15")) * L ** (-iv.mpf(k) / 2)

    assert ell ** (K + 1) >= 10 ** 5, "majorant needs N >= 1e5"
    K3 = K + 80
    tot = iv.mpf(0)
    for k in range(K + 1, K3 + 1):
        tot += T(k)
    rho = (1 + iv.mpf(1) / (K3 + 3)) * (1 + iv.mpf("2.44") * lnl / (iv.mpf("2.44") * (K3 + 1) * lnl + iv.mpf("10.15"))) \
        * L ** iv.mpf("-0.5")
    assert rho.b < 1
    tot += T(K3 + 1) / (1 - rho)
    return upper_fraction(tot)


def upper_fraction(x):
    """The interval's upper endpoint as an exact Fraction, read from mpmath's raw (sign, man, exp, bc) tuple.
    (Do NOT go through mpf(x.b): that re-rounds the endpoint to the working precision of the mp context, possibly
    downward; this was a bug found by the internal review.)"""
    sign, man, exp_, _bc = x._mpi_[1]
    v = Fraction(int(man)) * (Fraction(2) ** int(exp_))
    return -v if sign else v


def certify(ell):
    exact = Fraction(0)
    for K in range(1, KMAX + 1):
        n, cand = caught(ell, K)
        exact += Fraction(n, ell ** (K - 1) * (ell - 1))
        if ell ** (K + 1) < 10 ** 5:
            continue
        tail = tail_upper(ell, K)
        tot = exact + tail
        if tot < Fraction(1, 2):
            return (ell, K, float(exact), float(tail), float(tot), "CERTIFIED")
    return (ell, KMAX, float(exact), float(tail), float(tot), "UNDECIDED")


def main():
    global BIN, KMAX
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    if len(sys.argv) > 3:
        KMAX = int(sys.argv[3])
    if len(sys.argv) > 4:
        BIN = sys.argv[4]
    workers = int(sys.argv[5]) if len(sys.argv) > 5 else 5
    from sympy import primerange
    ps = list(primerange(lo, hi))
    worst = None
    nund = 0
    with Pool(workers, initializer=_init, initargs=(BIN, KMAX)) as pool:
        for r in pool.imap(certify, ps, chunksize=8):
            print("%d K=%d exact=%.6f tail=%.6f total=%.6f %s" % r, flush=True)
            if r[5] != "CERTIFIED":
                nund += 1
            if worst is None or r[4] > worst[4]:
                worst = r
    print(f"# primes in [{lo},{hi}): {len(ps)}; undecided: {nund}; worst total bound: {worst}")


def _init(b, k):
    global BIN, KMAX
    BIN, KMAX = b, k


if __name__ == "__main__":
    main()
