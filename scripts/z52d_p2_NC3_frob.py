# Z3013 (concrete reading): point counts N_q(p) = #{(t,u,v) in F_q^3 : tuv - u - v = p} of the affine cubic surface W_p mod q,
# for primes q <= 101 and all p in F_q.  Frobenius/Deligne for a smooth cubic surface: |N - q^2| <= 6q-ish; we record the max
# normalised deviation and the character-sum decomposition N - q^2 = sum over nontrivial characters psi(xi) of (the fibre sums):
# here via the additive-character expansion of the constraint tuv - u - v = p:  N(p) = (1/q) sum_xi sum_{t,u,v} e(xi(tuv-u-v-p)/q).
import cmath, math
from collections import Counter
def counts(q):
    N = Counter()
    for t in range(q):
        for u in range(q):
            for v in range(q):
                N[(t*u*v - u - v) % q] += 1
    return N
res = []
for q in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]:
    N = counts(q)
    dev = max(abs(N[p] - q*q) for p in range(q))
    res.append((q, dev, round(dev/q, 3)))
print("q, max_p |N_q(p) - q^2|, normalised by q:")
for r in res: print(r)
print("max normalised deviation over q <= 101:", max(r[2] for r in res))
