"""z66 UCOVER: two-prime survivor grid for the brief's K = {n = 1 (840), (n/11) = -1} (EVIDENCE only).

Profiles pi = (g at 11, h at 13, 1 elsewhere): pi lies in K iff g is a non-residue mod 11.  Events at all levels
(k', j') <= (K, J) from scripts/z66_ucover_levels2.c; a pair (g mod 11^K, h mod 13^J) survives iff no event cylinder
(g = rho1 mod 11^k', h = rho2 mod 13^j') contains it.  A-splits above MCAP are skipped (reported), so the survivor
count is an UPPER bound for the true one at these levels.
Usage: uv run python scripts/z66_ucover_ktree.py K J [MCAP]
"""
import subprocess
import sys


def main():
    K, J = int(sys.argv[1]), int(sys.argv[2])
    mcap = sys.argv[3] if len(sys.argv) > 3 else "300000000"
    p1, p2 = 11, 13
    Q1, Q2 = p1 ** K, p2 ** J
    alive = set((g, h) for g in range(Q1) if g % p1 and pow(g % p1, 5, 11) == 10
                for h in range(Q2) if h % p2)
    total = len(alive)
    skipped = []
    for k in range(0, K + 1):
        for j in range(0, J + 1):
            if k + j == 0:
                continue
            r = subprocess.run(["/tmp/zlev2", "11", str(k), "13", str(j), mcap], capture_output=True, text=True)
            skipped += [l for l in r.stderr.splitlines() if "SKIPPED" in l]
            cyl = set()
            for line in r.stdout.splitlines():
                t = line.split()
                cyl.add((int(t[1]), int(t[2])))
            m1, m2 = p1 ** k, p2 ** j
            before = len(alive)
            alive = set((g, h) for (g, h) in alive if (g % m1, h % m2) not in cyl)
            print(f"level (11^{k},13^{j}): {len(cyl)} cylinders; alive {before} -> {len(alive)}", flush=True)
    print(f"# skipped A-splits: {len(skipped)}", *skipped[:10], sep="\n")
    print(f"surviving fraction of K-box at (11^{K},13^{J}): {len(alive)}/{total} = {len(alive)/total:.4f}")
    byg = {}
    for g, h in alive:
        byg.setdefault(g % 11, set()).add(h % 13)
    print("surviving (g mod 11 -> h mod 13):", {g: sorted(v) for g, v in sorted(byg.items())})


if __name__ == "__main__":
    main()
