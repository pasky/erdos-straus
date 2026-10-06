"""R77: from-scratch check of the planting construction (Lemma 10.1) in the identical-marginal case and of the
BGP comparison sentence in 'Relation to the literature' (v6):
  n_c(k,p) <= (k+1)p/(1-p) + 2k + 2, and ratio to BGP's lower bound (k/(2(1-p))+1, k even; (k+1)/(2(1-p)), k odd;
  p >= 1/2) is <= 3, -> about 2 as p -> 1.
Construction: nu = nu0 + P0 sum_J w_J sigma_J  (exact Fractions), checked for nonnegativity, k-marginals, nu(0)=0.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import prod


def construct(N, k, q):  # q = P(b_i = 1), identical
    r = q / (1 - q)
    P0 = (1 - q) ** N
    nu = {}
    for x in product((0, 1), repeat=N):
        nu[x] = P0 * r ** sum(x)
    Js = list(combinations(range(N), k + 1))
    w = F(1, len(Js))  # identical r: all w_J equal
    for J in Js:
        for a in range(len(J) + 1):
            for y in combinations(J, a):
                x = tuple(1 if i in y else 0 for i in range(N))
                nu[x] += P0 * w * (-1) ** (a + 1)
    return nu


def ok(N, k, q):
    nu = construct(N, k, q)
    if min(nu.values()) < 0:
        return False
    assert nu[(0,) * N] == 0 and sum(nu.values()) == 1
    for K in combinations(range(N), k):
        for z in product((0, 1), repeat=k):
            m = sum(v for x, v in nu.items() if all(x[i] == z[t] for t, i in enumerate(K)))
            assert m == prod(q if zz else 1 - q for zz in z)
    return True


if __name__ == "__main__":
    for k in [1, 2, 3]:
        for p in [F(1, 2), F(2, 3), F(3, 4), F(4, 5)]:
            q = 1 - p  # flip: BGP mean p, all-ones prob 0  <->  our bits with P(1)=1-p, all-zeros prob 0
            bound = (k + 1) * p / (1 - p) + 2 * k + 2
            N = int(bound) if bound == int(bound) else int(bound) + 1
            # Lemma hypothesis at N:
            r = q / (1 - q)
            assert N * r >= (k + 1) + (2 * k + 1) * r
            if N <= 13:
                assert ok(N, k, q), (k, p, N)
                # smallest N for which the construction itself is nonnegative
                Nmin = next(n for n in range(k + 1, N + 1) if ok(n, k, q))
            else:
                Nmin = None
            lower = F(k, 2) / (1 - p) + 1 if k % 2 == 0 else F(k + 1, 2) / (1 - p)
            print(f"k={k} p={p}: lemma N={N}, construction works from N={Nmin}, BGP lower={float(lower):.2f}, ratio={float(bound/lower):.2f}")
            assert bound / lower <= 3
    # ratio sup over p in [1/2,1) for many k
    for k in range(1, 200):
        for i in range(1, 1000):
            p = 0.5 + 0.4999 * i / 1000
            lower = k / (2 * (1 - p)) + 1 if k % 2 == 0 else (k + 1) / (2 * (1 - p))
            assert ((k + 1) * p / (1 - p) + 2 * k + 2) / lower <= 3 + 1e-9
    print("ratio <= 3 on p in [1/2,1), k < 200: OK")
