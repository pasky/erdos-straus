"""z66 UCOVER: rigorous (computer-assisted) survivor accounting for the (S)-word families at the profiles e_{ell,g}.

For levels k <= K2 the good caught residues rho mod ell^k are computed exactly by scripts/z66_ucover_swords.c.
* Levels k <= K1: exact survivor tree S_k (non-residues g mod ell^k none of whose truncations is caught).
* Levels K1 < k <= K2: for each surviving branch g0 mod ell, subtract the Haar mass 1/phi(ell^k) of every caught
  cylinder lying over S_{K1} in that branch (sub-additivity: an upper bound for the mass removed).
* Levels k > K2: subtract the explicit bound TAIL = sum_{k>K2} B(ell^k, k)/phi(ell^k), where B(N, k) is the number of
  candidates the enumeration of z66_ucover_swords.c scans at level k (an upper bound for the number of events, hence
  for the number of caught residues), bounded analytically by B_ratio below.  The sum is evaluated to k = KMAX with the
  remainder bounded by a geometric series.
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


def B_ratio(ell, k):
    """B_up(ell^k, k) / ell^k, evaluated without forming ell^k as a float.  B_up is an analytic upper bound for
    the number of candidates scanned by z66_ucover_swords.c at level k (N = ell^k):
    W1: sum_{X<=X0} 2(R/X+1) + sum_{z<=Z}(S/z+1);  W2 (k+1 splits): sum_{s<=s0} 2(R/s+1) + 2 sum_{z<=Z'}(Rr/z+1),
    X0 = s0 = isqrt(2N)+2, R = isqrt(N+X0)+1, S = Z = isqrt(N/2)+3, Rr = isqrt(2N)+4, Z' = isqrt(N/2)+4;
    harmonic sums bounded by 1 + ln(x)."""
    lnN = k * math.log(ell)
    x = math.exp(-lnN / 2)          # N^{-1/2}
    # quantities divided by N: sqrt(c N)/N = sqrt(c) x ; constants/N = c x^2
    X0 = math.sqrt(2) * x + 2 * x * x            # X0 / N
    lnX0 = 0.5 * (math.log(2) + lnN) + 1e-9 + math.log1p(2 / math.sqrt(2) * x)  # ln X0 (upper bound)
    R = x * math.sqrt(1 + X0) + 2 * x * x       # R / N, R = sqrt(N + X0) + 2
    S = x / math.sqrt(2) + 3 * x * x            # S / N
    lnS = 0.5 * (lnN - math.log(2)) + math.log1p(3 * math.sqrt(2) * x)
    # products like R*(1+lnX0): (R/N)*(1+lnX0) is (R(1+lnX0))/N; S*(1+lnS)/N similar; but S/z sums: S/N*(1+lnS)
    w1 = 2 * R * (1 + lnX0) + 2 * X0 + S * (1 + lnS) + S
    Rr = math.sqrt(2) * x + 4 * x * x
    Z2 = x / math.sqrt(2) + 4 * x * x
    lnZ2 = 0.5 * (lnN - math.log(2)) + math.log1p(4 * math.sqrt(2) * x)
    w2 = 2 * R * (1 + lnX0) + 2 * X0 + 2 * Rr * (1 + lnZ2) + 2 * Z2
    return w1 + (k + 1) * w2


def main():
    ell, K1, K2 = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    binary = sys.argv[4] if len(sys.argv) > 4 else "/tmp/zsw"
    E = {}
    for k in range(1, K2 + 1):
        E[k], cand = caught(binary, ell, k)
        N = ell ** k
        print(f"level {k}: good caught residues {len(E[k])}, candidates scanned {cand}, B_up {B_ratio(ell, k) * N:.0f}",
              flush=True)
        assert cand <= B_ratio(ell, k) * N, "analytic candidate bound violated"
    # exact tree to K1
    S = [g for g in range(1, ell) if pow(g, (ell - 1) // 2, ell) == ell - 1 and g not in E[1]]
    Q = ell
    for k in range(2, K1 + 1):
        S = [g + Q * t for g in S for t in range(ell)]
        Q *= ell
        S = [g for g in S if g not in E[k]]
    phiK1 = ell ** (K1 - 1) * (ell - 1)
    mass = {}
    for g in S:
        mass[g % ell] = mass.get(g % ell, 0.0) + 1.0 / phiK1
    Sset = set(S)
    print(f"exact tree to level {K1}: {len(S)} survivors; branch masses " +
          ", ".join(f"{g0}:{m:.6f}" for g0, m in sorted(mass.items())))
    removed = {g0: 0.0 for g0 in mass}
    for k in range(K1 + 1, K2 + 1):
        phik = ell ** (k - 1) * (ell - 1)
        for r in E[k]:
            if r % (ell ** K1) in Sset:
                removed[r % ell] += 1.0 / phik
    # tail
    KMAX = 400
    tail = 0.0
    for k in range(K2 + 1, KMAX + 1):
        tail += B_ratio(ell, k) * ell / (ell - 1)
    # remainder k > KMAX: B_up(N,k)/phi <= C k^2 ell^{-k/2} with ratio < 1/2 for these k; bound by twice last term
    last = B_ratio(ell, KMAX) * ell / (ell - 1)
    tail += 2 * last
    print(f"explicit tail bound (k > {K2}): {tail:.3e}")
    ok = []
    for g0 in sorted(mass):
        lb = mass[g0] - removed[g0] - tail
        print(f"branch g0={g0}: exact mass {mass[g0]:.6f}, removed (levels {K1+1}..{K2}) <= {removed[g0]:.6f}, "
              f"tail <= {tail:.2e}; lower bound {lb:.6f} -> {'SURVIVES' if lb > 0 else 'undecided'}")
        if lb > 0:
            ok.append(g0)
    print(f"ell={ell}: branches g0 mod ell proved to contain U_S-profiles e_(ell,g): {ok}")


if __name__ == "__main__":
    main()
