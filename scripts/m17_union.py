"""Union of all 17-generic ET boxes in the cells C_5, C_7 (POINTWISE_MORDELL17 §3).

usage: m17_union.py kmax Kmax [--bin /tmp/o83/m17_enum] [--cmp boxes.pkl]
  Q,U data for levels k<=kmax, P data for K<=Kmax (levels ceil(K/2)); resolution 17^R (R>=all levels used).
Boxes by Lemma 1.1: Q, Q^-1, sqrt(Q) (both roots), U, U^-1, P.  Prints per level the new boxes
meeting C_5/C_7 and the covered fraction of each cell at resolution 17^R.
"""
import sys, subprocess, pickle
from collections import defaultdict

args = sys.argv[1:]
BIN = '/tmp/o83/m17_enum'
CMP = None
if '--bin' in args:
    i = args.index('--bin'); BIN = args[i + 1]; del args[i:i + 2]
if '--cmp' in args:
    i = args.index('--cmp'); CMP = args[i + 1]; del args[i:i + 2]
kmax, Kmax = map(int, args[:2])


def run(mode, k):
    import os
    fn = f'/tmp/o83/out_{mode}{k}.txt'   # cached output of `m17_enum mode k | sort -u`
    if os.path.exists(fn):
        return sorted({int(l.split()[1]) for l in open(fn) if l.strip()})
    out = subprocess.run([BIN, mode, str(k)], capture_output=True, text=True, check=True)
    sys.stderr.write(out.stderr)
    return sorted({int(l.split()[1]) for l in out.stdout.split('\n') if l})


def sqrts(r, k):
    """all s mod 17^k with s^2 = r (r a unit)"""
    sols = [s for s in range(17) if (s * s - r) % 17 == 0]
    m = 17
    for _ in range(1, k):
        m2 = m * 17
        sols = [s + m * t for s in sols for t in range(17) if ((s + m * t) ** 2 - r) % m2 == 0]
        m = m2
    return sols


boxes = defaultdict(set)   # level -> residues mod 17^level
src = defaultdict(lambda: defaultdict(set))
for k in range(1, kmax + 1):
    F = 17 ** k
    for r in run('Q', k):
        if r % 17 == 0:
            continue
        for t, s in (('Q', r), ('Q-1', pow(r, -1, F))):
            boxes[k].add(s); src[k][t].add(s)
        for s in sqrts(r, k):
            boxes[k].add(s); src[k]['sqrtQ'].add(s)
    for r in run('U', k):
        if r % 17 == 0:
            continue
        for t, s in (('U', r), ('U-1', pow(r, -1, F))):
            boxes[k].add(s); src[k][t].add(s)
for K in range(1, Kmax + 1):
    k = (K + 1) // 2
    for r in run('P', K):
        boxes[k].add(r); src[k]['P'].add(r)

# ultrametric: balls are nested or disjoint, so the union measure is the sum over maximal boxes.
from fractions import Fraction
for v in (5, 7):
    print(f"cell C_{v}:")
    tot = Fraction(0)
    for k in sorted(boxes):
        F = 17 ** k
        inC = sorted(r for r in boxes[k] if r % 17 == v)
        per = {t: sum(1 for r in S if r % 17 == v) for t, S in src[k].items()}
        new = [r for r in inC if not any(r % 17 ** j in boxes.get(j, ()) for j in range(1, k))]
        tot += Fraction(len(new), F)
        pernew = {t: sum(1 for r in new if r in S) for t, S in src[k].items()}
        print(f"    new boxes by type: {pernew}")
        print(f"  level {k}: {len(inC)} boxes in cell {per}, {len(new)} maximal; "
              f"covered fraction of cell after level {k}: {float(tot * 17):.6f}")
        if len(inC) <= 12:
            print("    residues:", inC)
pickle.dump({k: sorted(s) for k, s in boxes.items()}, open(f'/tmp/o83/boxes_{kmax}_{Kmax}.pkl', 'wb'))
if CMP:
    bb = pickle.load(open(CMP, 'rb'))
    miss = [(MT, r) for (MT, r) in bb if MT > 1 and r % 17 in (5, 7)
            and r not in boxes.get(len(str(MT)) and __import__('math').ceil(__import__('math').log(MT, 17) - 1e-9), set())]
    print("brute-force boxes in C not in complete list:", miss[:20], len(miss))
