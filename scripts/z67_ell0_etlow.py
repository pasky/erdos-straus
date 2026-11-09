"""z67 ELL0: falsifier scan for (T-all) at small primes (ET families, single-prime profiles e_{ell,g}).

For each prime ell in [LO, HI) runs scripts/z66_ucover_levels.c (exact generator residues, UCOVER Lemma 1) for levels
1..K and reports the survivor tree: |S_k| = non-residues g mod ell^k none of whose truncations is caught, the surviving
mass m_k = |S_k|/phi(ell^k) (non-residue mass 1/2), and the plain sum of event masses sum_k |E_k|/phi(ell^k).
A prime with S_k empty for some k is a CERTIFIED counterexample to (T-all) at that ell (every non-residue profile is
caught).  Usage: uv run --with sympy python scripts/z67_ell0_etlow.py LO HI K [binary] [workers]
"""
import subprocess
import sys
from multiprocessing import Pool

BIN = "/tmp/zlev"
K = 1


def caught(ell, k):
    out = subprocess.run([BIN, str(ell), str(k)], capture_output=True, text=True, check=True).stdout
    return set(int(line.split()[1]) for line in out.splitlines() if line.strip())


def run(ell):
    S = [g for g in range(1, ell) if pow(g, (ell - 1) // 2, ell) == ell - 1]
    Q = 1
    rows = []
    evsum = 0.0
    for k in range(1, K + 1):
        if k > 1:
            S = [g + Q * t for g in S for t in range(ell)]
        Q *= ell
        E = caught(ell, k)
        assert all(pow(r % ell, (ell - 1) // 2, ell) == ell - 1 for r in E)
        S = [g for g in S if g not in E]
        phi = Q // ell * (ell - 1)
        evsum += len(E) / phi
        rows.append((k, len(E), len(S), len(S) / phi))
        if not S:
            break
    return ell, rows, evsum


def _init(b, k):
    global BIN, K
    BIN, K = b, k


def main():
    lo, hi, k = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    b = sys.argv[4] if len(sys.argv) > 4 else BIN
    w = int(sys.argv[5]) if len(sys.argv) > 5 else 5
    from sympy import primerange
    ps = list(primerange(lo, hi))
    dead = []
    minmass = None
    with Pool(w, initializer=_init, initargs=(b, k)) as pool:
        for ell, rows, evsum in pool.imap(run, ps, chunksize=4):
            last = rows[-1]
            print(f"{ell} " + " ".join(f"k{r[0]}:E={r[1]},S={r[2]},m={r[3]:.4f}" for r in rows) + f" evsum={evsum:.4f}",
                  flush=True)
            if last[2] == 0:
                dead.append(ell)
            if minmass is None or last[3] < minmass[1]:
                minmass = (ell, last[3])
    print(f"# primes in [{lo},{hi}): {len(ps)}; all non-residues caught (T-all fails): {dead}; "
          f"min surviving mass at the last level: {minmass}")


if __name__ == "__main__":
    main()
