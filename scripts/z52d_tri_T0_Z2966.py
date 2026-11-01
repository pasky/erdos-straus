# z52d triage T0, Z2966: (★) pure-congruence coverage of hard classes p ≡ 1 (24) for M = 840, 2520, 9240, 120120 (non-square uncovered counts)
# z52d P2 TO8 Z2966: residues p mod M covered by pure congruence certificates: class r covered if ∃ q | M, q≡3 (4), (q+1)/4 = u*C (u,C>=1)
# with r ≡ -u (mod q)  (then B=(p+u)/q is a positive integer for p large, and (u,C,B) is a (★)-certificate for every p≡r mod M).
# Compare uncovered classes among p≡1 (mod 24) with the square classes mod 840 (T1 forces no certificate at odd squares).
import math
def covered_classes(M):
    cov = set()
    qs = [q for q in range(3, M + 1, 4) if M % q == 0]
    for q in qs:
        N = (q + 1) // 4
        for u in range(1, N + 1):
            if N % u == 0:
                for r in range(M):
                    if (r + u) % q == 0: cov.add(r)
    return cov
for M in [840, 2520, 9240, 9240*13]:
    cov = covered_classes(M)
    hard = [r for r in range(M) if r % 24 == 1 and math.gcd(r, M) == 1]
    unc = [r for r in hard if r not in cov]
    sq = sorted({(x * x) % M for x in range(M) if math.gcd(x, M) == 1} & set(hard))
    print(f"M={M}: hard classes(p≡1 mod 24, coprime)={len(hard)}, covered by pure congruences={len([r for r in hard if r in cov])}, uncovered={len(unc)}; nonsquare uncovered={len(set(unc)-set(sq))} of nonsquare {len(set(hard)-set(sq))}")
