"""z67 K11: survivor tree of the K-box over P-smooth levels (exact for the stated levels).

Start at Q0 = 9240 = 2^3*3*5*7*11 with the residues of B = {1 mod 840, non-residue mod 11}; multiply the level by the
primes in STEPS one at a time.  A child of an open node can only be caught by a class whose modulus divides the new
level but not the old one, so only those classes are tested.  Prints, per level, open/tested and the surviving
Haar fraction of B.  Optionally dumps the final open nodes (npy) for the tail certificate.
Usage: uv run --with cypari2 --with numpy python scripts/z67_k11_tree.py STEPS [--dump FILE]
       STEPS like 13,13,3,2,11,5,7  (each entry multiplies the level by that prime)
"""
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from z67_k11_classes import classes_dividing  # noqa: E402


def main():
    steps = [int(x) for x in sys.argv[1].split(",")]
    dump = sys.argv[sys.argv.index("--dump") + 1] if "--dump" in sys.argv else None
    exps = Counter({2: 3, 3: 1, 5: 1, 7: 1, 11: 1})
    for p in steps:
        exps[p] += 1
    S = classes_dividing(dict(exps))
    print(f"# final exponents {dict(exps)}: {len(S)} moduli, {sum(len(v) for v in S.values())} B-compatible classes",
          flush=True)
    Q = 9240
    nodes = np.array([x for x in range(Q) if x % 840 == 1 and pow(x % 11, 5, 11) == 10], dtype=np.int64)
    tot_nodes = len(nodes)  # number of B-residues mod Q (all of equal measure)
    cur = Counter({2: 3, 3: 1, 5: 1, 7: 1, 11: 1})

    def test(nodes, Q, oldQ):
        keep = np.ones(len(nodes), dtype=bool)
        for m, R in S.items():
            if Q % m or (oldQ and oldQ % m == 0):
                continue
            Rarr = np.fromiter(R, dtype=np.int64)
            keep &= ~np.isin(nodes % m, Rarr)
        return nodes[keep]

    nodes = test(nodes, Q, 0)
    print(f"level {Q} {dict(cur)}: open {len(nodes)}/{tot_nodes}  fraction {len(nodes)/tot_nodes:.6g}", flush=True)
    for p in steps:
        newQ = Q * p
        tot_nodes *= (p - 1) if Q % p else p
        ch = (nodes[:, None] + Q * np.arange(p, dtype=np.int64)[None, :]).ravel()
        ch = ch[ch % p != 0]
        cur[p] += 1
        nodes = test(ch, newQ, Q)
        Q = newQ
        print(f"level {Q} {dict(cur)}: open {len(nodes)}/{tot_nodes}  fraction {len(nodes)/tot_nodes:.6g}",
              flush=True)
        if len(nodes) == 0:
            print("# ALL COVERED: finite covering found")
            break
    if dump:
        np.save(dump, nodes)
        print(f"# dumped {len(nodes)} open nodes mod {Q} to {dump}")


if __name__ == "__main__":
    main()
