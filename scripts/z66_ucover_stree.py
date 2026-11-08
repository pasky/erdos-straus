"""z66 UCOVER: rigorous (computer-assisted) survivor accounting for the (S)-word families at the profiles e_{ell,g}.

For levels k <= K2 the good caught residues rho mod ell^k are computed exactly by scripts/z66_ucover_swords.c.
* Levels k <= K1: exact survivor tree S_k (non-residues g mod ell^k none of whose truncations is caught).
* Levels K1 < k <= K2: for each surviving branch g0 mod ell, subtract the Haar mass 1/phi(ell^k) of every caught
  cylinder lying over S_{K1} in that branch (sub-additivity: an upper bound for the mass removed).
* Levels k > K2: subtract a rigorous upper bound (interval arithmetic) for sum_{k>K2} B(ell^k, k)/phi(ell^k), where
  B(N, k) bounds the number of candidates z66_ucover_swords.c's algorithm scans at level k (hence the number of events
  and of caught residues); see tail_upper.  Masses and removals are exact fractions.
A branch g0 whose final lower bound is > 0 contains some g with e_{ell,g} in no good-word class (compactness: the caught
set is a countable union of cylinders; positive remaining mass means non-empty complement).
Usage: uv run python scripts/z66_ucover_stree.py ELL K1 K2 [binary]
"""
import math
import subprocess
import sys


def caught(binary, ell, k):
    out = subprocess.run([binary, str(ell), str(k)], capture_output=True, text=True, check=True)
    res = set()
    for line in out.stdout.splitlines():
        t = line.split()
        r = int(t[1])
        if r % ell == 0:
            continue  # cylinder outside Z_ell^x (non-unit profile component); irrelevant for g in Z_ell^x
        if t[0] == "W1":
            if k % 2 == 1 and pow(r % ell, (ell - 1) // 2, ell) == ell - 1:
                res.add(r)
        elif t[4] == "1":
            assert pow(r % ell, (ell - 1) // 2, ell) == ell - 1, "good W2 event at a residue?!"
            res.add(r)
    cand = int(out.stderr.strip().split("candidates_scanned=")[1])
    return res, cand


def tail_upper(ell, K2):
    """Rigorous upper bound (mpmath interval arithmetic) for sum_{k>K2} B(ell^k, k)/phi(ell^k).

    Majorant (Z66_UCOVER.md Lemma S2'): for N >= 10^5 the candidate count of z66_ucover_swords.c satisfies
        B(N, k) <= sqrt(N) (k + 2) (2.44 ln N + 10.15),
    so  B/phi(ell^k) <= T_k := ell/(ell-1) (k+2)(2.44 k ln(ell) + 10.15) ell^{-k/2}.
    The sum over k > K2 is evaluated exactly-interval to k = K3 and the rest bounded by T_{K3+1}/(1 - rho) with
    rho = (1 + 1/(K3+3)) (1 + 2.44 ln(ell)/(2.44 (K3+1) ln(ell) + 10.15)) ell^{-1/2} >= T_{k+1}/T_k (k > K3)."""
    from mpmath import iv
    iv.dps = 40
    L = iv.mpf(ell)
    lnl = iv.log(L)

    def T(k):
        return L / (L - 1) * (k + 2) * (iv.mpf("2.44") * k * lnl + iv.mpf("10.15")) * L ** (-iv.mpf(k) / 2)

    assert ell ** (K2 + 1) >= 10 ** 5, "majorant needs N >= 1e5"
    K3 = K2 + 200
    tot = iv.mpf(0)
    for k in range(K2 + 1, K3 + 1):
        tot += T(k)
    rho = (1 + iv.mpf(1) / (K3 + 3)) * (1 + iv.mpf("2.44") * lnl / (iv.mpf("2.44") * (K3 + 1) * lnl + iv.mpf("10.15"))) \
        * L ** iv.mpf("-0.5")
    assert rho.b < 1
    tot += T(K3 + 1) / (1 - rho)
    return tot.b  # upper endpoint (an mpf)


def main():
    ell, K1, K2 = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    binary = sys.argv[4] if len(sys.argv) > 4 else "/tmp/zsw"
    E = {}
    for k in range(1, K2 + 1):
        E[k], cand = caught(binary, ell, k)
        N = ell ** k
        print(f"level {k}: good caught residues {len(E[k])}, candidates scanned {cand}",
              flush=True)
        if N >= 10 ** 5:
            assert cand <= math.isqrt(N + 1) * (k + 2) * (2.44 * math.log(N) + 10.15), "majorant violated"
    # exact tree to K1 (integer counts; masses as exact fractions)
    from fractions import Fraction
    from mpmath import mpf
    S = [g for g in range(1, ell) if pow(g, (ell - 1) // 2, ell) == ell - 1 and g not in E[1]]
    Q = ell
    for k in range(2, K1 + 1):
        S = [g + Q * t for g in S for t in range(ell)]
        Q *= ell
        S = [g for g in S if g not in E[k]]
    phiK1 = ell ** (K1 - 1) * (ell - 1)
    cnt = {}
    for g in S:
        cnt[g % ell] = cnt.get(g % ell, 0) + 1
    mass = {g0: Fraction(c, phiK1) for g0, c in cnt.items()}
    Sset = set(S)
    print(f"exact tree to level {K1}: {len(S)} survivors; branch masses " +
          ", ".join(f"{g0}:{float(m):.6f}" for g0, m in sorted(mass.items())))
    removed = {g0: Fraction(0) for g0 in mass}
    for k in range(K1 + 1, K2 + 1):
        phik = ell ** (k - 1) * (ell - 1)
        for r in E[k]:
            if r % (ell ** K1) in Sset:
                removed[r % ell] += Fraction(1, phik)
    tail = tail_upper(ell, K2)
    print(f"rigorous tail bound (k > {K2}): {float(tail):.4e}")
    ok = []
    for g0 in sorted(mass):
        exact = mass[g0] - removed[g0]           # exact rational
        lb = mpf(exact.numerator) / mpf(exact.denominator) - tail  # tail is an upper endpoint; compare rigorously below
        # rigorous comparison: exact > tail  <=>  exact.numerator > tail * exact.denominator (tail upper endpoint)
        surv = mpf(exact.numerator) > tail * mpf(exact.denominator) * (1 + mpf(10) ** -30)
        print(f"branch g0={g0}: exact mass {float(mass[g0]):.6f}, removed (levels {K1+1}..{K2}) {float(removed[g0]):.6f} "
              f"(exact sum), tail <= {float(tail):.3e}; lower bound {float(lb):.6f} -> {'SURVIVES' if surv else 'undecided'}")
        if surv:
            ok.append(g0)
    print(f"ell={ell}: branches g0 mod ell proved to contain U_S-profiles e_(ell,g): {ok}")


if __name__ == "__main__":
    main()
