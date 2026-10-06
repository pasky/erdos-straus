"""R80: independent re-check of Mordell's step: every unit residue t mod 840 that is not a square
is covered by some ET family class (integrality on t+840Z checked exactly), using the same
from-scratch family formulas as review_mordell_check.py."""
from math import gcd
from itertools import product
from review_mordell_check import sol, family_ok, identity_ok, covers

L = 840
units = [t for t in range(1, L) if gcd(t, L) == 1]
sqs = {k*k % L for k in units}
todo = [t for t in units if t not in sqs]
print('non-square units mod 840:', len(todo), ' squares:', sorted(sqs))
cands = []
R = range(1, 41)
for fam in ['I1', 'I2', 'I3', 'I4', 'II1', 'II2', 'II3']:
    for P in product(R, R, R):
        if family_ok(fam, P) and P[2] <= 40:
            cands.append((fam, P))
left = set(todo); wit = {}
for c in cands:
    if not left: break
    hit = [t for t in left if covers(*c, t, L)]
    if hit:
        assert identity_ok(*c)
        for t in hit: wit[t] = c
        left -= set(hit)
print('uncovered non-squares:', sorted(left))
print('distinct witness classes:', len(set(wit.values())))
# squares must be uncovered by any class (sanity, ET Prop 1.6 / Mordell): check with candidates
sq_cov = [t for t in sqs if any(covers(*c, t, L) for c in cands)]
print('squares covered (should be none):', sq_cov)
