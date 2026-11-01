# z53 HCSHIFTS (N2b): are the line-miss correlations explained by p modulo small primes?
# Empirical P(HC > X) = P(all lines x in C ∩ [4,X] miss) vs  sum_s w_s * prod_lines P_s(line misses), strata s = p mod M.
# Options:  --sep      treat the endpoint and the level integer of each coordinate as two separate events
#                      (default: one event per coordinate = endpoint OR level fires, as in HC)
#           --holdout  fit the per-stratum marginals on the even-indexed rows, evaluate the empirical all-miss
#                      frequency on the odd-indexed rows (avoids in-sample fitting)
import sys, collections
C128 = [x for x in range(4, 129) if x % 4 == 0 or x % 8 == 7]
SEP = '--sep' in sys.argv; HOLD = '--holdout' in sys.argv
files = [a for a in sys.argv[1:] if not a.startswith('--')]
MS = (1, 105, 1155, 15015)
def load(fn):
    rows = []
    for line in open(fn):
        if line.startswith('#'): continue
        f = line.split()
        if len(f) < 13: continue
        mE, mL = int(f[11], 16), int(f[12], 16)
        if SEP:  # interleave: bit 2i = endpoint of i-th coordinate, bit 2i+1 = level
            m = 0
            for i in range(len(C128)):
                m |= ((mE >> i) & 1) << (2 * i) | ((mL >> i) & 1) << (2 * i + 1)
        else:
            m = mE | mL
        rows.append((int(f[0]), m))
    return rows
Xs = [7, 8, 12, 15, 16, 20, 23, 24]
for fn in files:
    rows = load(fn)
    fit = rows[0::2] if HOLD else rows; ev = rows[1::2] if HOLD else rows
    print(f"== {fn} n_fit={len(fit)} n_eval={len(ev)} sep={SEP} holdout={HOLD}")
    print("  X  empirical  (#events)  ratio emp/pred for M = " + " ".join(f"{M:<6d}" for M in MS))
    preds = {}
    for M in MS:
        groups = collections.defaultdict(list)
        for p, m in fit: groups[p % M].append(m)
        evw = collections.Counter(p % M for p, _ in ev)
        for X in Xs:
            k = sum(1 for x in C128 if x <= X) * (2 if SEP else 1)
            tot = 0.0
            for s, g in groups.items():
                pr = 1.0
                for i in range(k):
                    pr *= 1 - sum(1 for m in g if m >> i & 1) / len(g)
                tot += evw.get(s, 0) / len(ev) * pr
            preds[(M, X)] = tot
    for X in Xs:
        k = sum(1 for x in C128 if x <= X) * (2 if SEP else 1); mask = (1 << k) - 1
        cnt = sum(1 for _, m in ev if m & mask == 0); emp = cnt / len(ev)
        print(f" {X:2d}  {emp:.2e}  ({cnt:4d})   " + " ".join(f"{emp/preds[(M,X)] if preds[(M,X)] > 0 else float('nan'):6.2f}" for M in MS))
