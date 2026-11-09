"""z67 ELL0, Lemma D check: every (A) event with k2 >= 3 at level k reduces mod ell^(k-1) to a level-(k-1) (A) residue.
Usage: uv run python scripts/z67_ell0_dilation_check.py ELL K  (needs /tmp/zlev = gcc -O2 scripts/z66_ucover_levels.c)"""
import subprocess, sys
ell, K = int(sys.argv[1]), int(sys.argv[2])
def A(k):
    out = subprocess.run(["/tmp/zlev", str(ell), str(k)], capture_output=True, text=True, check=True).stdout
    ev = []
    for line in out.splitlines():
        p = line.split()
        if p[0] == "A":
            d = dict(x.split("=") for x in p[2:])
            ev.append((int(p[1]), int(d["k1"])))
    return ev
lo = {r for r, _ in A(K - 1)}
hi = A(K)
red = [r for r, k1 in hi if K - k1 >= 3]
bad = [r for r in red if r % ell ** (K - 1) not in lo]
print(f"ell={ell} k={K}: (A) events {len(hi)}, with k2>=3: {len(red)}, not reduced to level {K-1}: {len(bad)}; "
      f"level {K-1} (A) residues {len(lo)}")
