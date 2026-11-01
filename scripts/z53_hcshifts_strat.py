# z53 HCSHIFTS (N2b): are the line-miss correlations explained by p modulo small primes?
# Empirical P(HC > X) vs  sum_strata w_s * prod_x P_s(line x misses), strata = p mod M (M = 1, 105, 1155, 15015).
# If conditioning on p mod M removes the excess, the correlation is congruence (small-prime) data and the private
# parts behave independently across lines (privacy).
import sys, collections
C128 = [x for x in range(4, 129) if x % 4 == 0 or x % 8 == 7]
def load(fn):
    rows = []
    for line in open(fn):
        if line.startswith('#'): continue
        f = line.split()
        if len(f) < 13: continue
        rows.append((int(f[0]), int(f[11], 16) | int(f[12], 16)))
    return rows
Xs = [7, 8, 12, 15, 16, 20, 23, 24]
for fn in sys.argv[1:]:
    rows = load(fn); n = len(rows)
    print(f"== {fn} n={n}")
    print("  X  empirical   " + "  ".join(f"M={M:<6d}" for M in (1, 105, 1155, 15015)))
    preds = {}
    for M in (1, 105, 1155, 15015):
        groups = collections.defaultdict(list)
        for p, m in rows: groups[p % M].append(m)
        for X in Xs:
            k = sum(1 for x in C128 if x <= X)
            tot = 0.0
            for g in groups.values():
                pr = 1.0
                for i in range(k):
                    pr *= 1 - sum(1 for m in g if m >> i & 1) / len(g)
                tot += len(g) / n * pr
            preds[(M, X)] = tot
    for X in Xs:
        k = sum(1 for x in C128 if x <= X); mask = (1 << k) - 1
        emp = sum(1 for _, m in rows if m & mask == 0) / n
        print(f" {X:2d}  {emp:.2e}  " + "  ".join(f"{emp/preds[(M,X)]:8.2f}" for M in (1, 105, 1155, 15015)))
