"""z66 UCOVER: the ell-adic survivor tree for the profiles e_g (1 away from ell, g at ell).

Runs scripts/z66_ucover_levels.c for k = 1..K and keeps S_k = residues g mod ell^k (non-residues mod ell) none of
whose truncations g mod ell^j (j <= k) is a caught residue at level j.  Prints |E_k| (caught residues at level k),
|S_k| and the surviving Haar mass  m_k = |S_k| / phi(ell^k)  (the non-residues have mass 1/2).
Usage: uv run python scripts/z66_ucover_tree.py ELL K [binary]
"""
import subprocess
import sys


def caught(binary, ell, k):
    out = subprocess.run([binary, str(ell), str(k)], capture_output=True, text=True, check=True).stdout
    return set(int(line.split()[1]) for line in out.splitlines() if line.strip())


def main():
    ell, K = int(sys.argv[1]), int(sys.argv[2])
    binary = sys.argv[3] if len(sys.argv) > 3 else "/tmp/zlev"
    S = [g for g in range(1, ell) if pow(g, (ell - 1) // 2, ell) == ell - 1]
    Q = 1
    for k in range(1, K + 1):
        Qn = Q * ell
        if k > 1:
            S = [g + Q * t for g in S for t in range(ell)]
        E = caught(binary, ell, k)
        assert all(pow(r % ell, (ell - 1) // 2, ell) == ell - 1 for r in E), "caught residue is a QR?!"
        S = [g for g in S if g not in E]
        Q = Qn
        phi = Q // ell * (ell - 1)
        print(f"ell={ell} k={k}: |E_k|={len(E)} |S_k|={len(S)} surviving mass={len(S)/phi:.6f} "
              f"(non-residue mass 0.5); E_k mass={len(E)/phi:.6f}", flush=True)
        if not S:
            print(f"ell={ell}: ALL non-residue profiles e_g caught by level {k}")
            break
    if S:
        print(f"ell={ell}: sample survivors mod ell^{K}: {S[:8]}")


if __name__ == "__main__":
    main()
