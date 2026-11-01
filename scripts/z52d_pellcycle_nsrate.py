r"""z52d PELLCYCLE: unconditional census on near-square primes p = m^2+1, 12 | m (so p ≡ 1 (mod 24)), m <= MMAX.
For each such prime: R = R3(p) ∪ U(p) (lib.root_sets + unit data {2m, 2, 2m±2, 4}); records whether every component meeting R
is monochromatic ("cycle-dead"), and separately whether the components of {1,2,4} alone are monochromatic.
Usage: uv run --with sympy python scripts/z52d_pellcycle_nsrate.py MMAX OUT.txt
"""
import sys
from sympy import isprime
from z52d_pellcycle_lib import root_sets, explore

MMAX = int(sys.argv[1])
out = open(sys.argv[2], "w")
n = dead = dead_small = 0
dead_list = []
for m in range(12, MMAX + 1, 12):
    p = m * m + 1
    if not isprime(p):
        continue
    n += 1
    R = set(root_sets(p)["R3"]) | {2 * m, 2, 2 * m - 2, 2 * m + 2, 4}
    st = {u: explore(p, u)[0] for u in R}
    assert "censored" not in st.values()
    small_mono = all(st[u] == "mono" for u in (1, 2, 4))
    big_hit = [u for u in R if u > 4 and st[u] == "hit"]
    d = small_mono and not big_hit
    dead += d
    dead_small += small_mono
    if d:
        dead_list.append(p)
    if big_hit:
        out.write(f"m={m} p={p} large-root hit {big_hit}\n")
out.write(f"primes p=m^2+1, 12|m, m<={MMAX}: {n}; every R3∪U component monochromatic: {dead}; "
          f"components of 1,2,4 monochromatic: {dead_small}\n")
out.write("cycle-dead primes (first 60): " + " ".join(map(str, dead_list[:60])) + "\n")
out.close()
print(open(sys.argv[2]).read()[-2000:])
