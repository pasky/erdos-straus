"""R181: Thm 2.2 hypothesis 'P a prime power' — is it needed?  P = Q1*Q2 (deg 1 * deg n-1), c=(1,1,1):
count points with nonzero odd-order invariant at Q1 (and check inv_Q1 + inv_Q2 = 0 odd part)."""
import sys, collections
from review_dr_ff import FF
from review_dr_bl import solutions, alpha_args
p, m, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); A = (0, 1); F = FF(p)
st = collections.Counter(); cnt = 0
for Q1 in F.monics(1):
    if F.gcd(Q1, A) != (1,): continue
    for Q2 in F.monics(n - 1):
        if not F.is_irred(Q2) or Q2 == Q1: continue
        P = F.mul(Q1, Q2); cnt += 1
        if cnt > int(sys.argv[4]): break
        for X in solutions(F, A, P, (1, 1, 1), n):
            inv = F.all_invariants(*alpha_args(F, (1, 1, 1), X), m)
            st['inv_Q1', inv.get(Q1, 0)] += 1
            st['sumQ', (inv.get(Q1, 0) + inv.get(Q2, 0)) % m] += 1
            st['others nonzero', any(v for kk, v in inv.items() if kk not in (Q1, Q2))] += 1
print(f"p={p} m={m} n={n} P=Q1Q2 (#P={min(cnt, int(sys.argv[4]))}):", dict(st))
