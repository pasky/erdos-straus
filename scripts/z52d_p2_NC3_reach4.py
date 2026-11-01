# Z3147: which primes p are reached by words with t ∈ 4Z (equivalently some level t=4C, C>=1)?
# Exact criterion (level_words identity): p reached at level 4C  <=>  4Cp+1 = A*B with A ≡ B ≡ -1 (mod 4C), A,B >= 8C-1.
# Validation against brute force (minlevel data, p ≡ 1 mod 8, p <= 2e5): least C via divisors equals brute-force least C for
# all C up to the brute-force value; unreachable primes (no 4|t word at all) are the 33 (≤1e6) / 26 (≤2e5) of the C scan.
import sys
sys.path.insert(0, 'scripts')
from z52d_p2_NC3_levels import level_words
rows = [tuple(map(int, l.split())) for l in open('data/z52b/pass2/NC3/minlevel_2e5_mod8.txt')]
agree = dis = 0; tested = 0
for p, nw, minC, nC4, nA4 in rows:
    if minC == 0: continue
    if p > 200000: continue
    tested += 1
    ok = all((len(level_words(p, 4*C)) > 0) == (C == minC) for C in range(1, minC+1)) if minC <= 60 else None
    if ok is None: continue
    agree += ok; dis += (not ok)
print("least-level check (p ≡ 1 mod 8, p ≤ 2e5, minC ≤ 60):", agree, "agree,", dis, "disagree; tested", tested)
# reachability summary: fraction of unreachable primes in the scan
unreach = [r[0] for r in rows if r[3] == 0]
print("primes ≡1 (8) ≤ 2e5 with no level-4C word:", len(unreach), unreach)
