import sys; sys.path.insert(0, 'scripts')
from z53_genusredei_twist import range_scan
X, lo, hi = map(int, sys.argv[1:4])
n, noB1, agg, onlyP, noev, rows = range_scan(X, lo, hi)
print(f"# X={X} primes p≡1(4) in [{lo},{hi}): {n}; with no B1-visible event level: {noB1}")
print(f"#  among those: event levels by class {agg}; primes whose event levels are all protected (P2/Podd): {onlyP}; no event level at all: {noev}")
for p, o in rows: print(p, o)
