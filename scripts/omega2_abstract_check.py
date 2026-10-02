"""Brute-force check of POINTWISE_OMEGA2 Lemmas 1.1-1.2 (support-truncated minorant).

Random event systems on a few coordinates; for every outcome x we compute
B_L(x) directly from the definition, compare with the closed form R_L of
Lemma 1.1, and check B_L - 4^{L+1} e_{L+1}(a) <= 1[A=empty] and
|B_L - 1[A=empty]| <= 4^{L+1} e_{L+1}(a).

usage: omega2_abstract_check.py [trials] [seed]
"""
import itertools, random, sys
from math import comb


def esym(vals, k):
    e = [1] + [0] * k
    for v in vals:
        for j in range(k, 0, -1):
            e[j] += e[j - 1] * v
    return e[k]


def run(trials, seed):
    rng = random.Random(seed)
    checked = 0
    for _ in range(trials):
        P = rng.randint(2, 6)
        sizes = [rng.randint(2, 3) for _ in range(P)]
        k = rng.randint(1, 3)
        events = []
        for _ in range(rng.randint(1, 12)):
            s = rng.randint(1, min(k, P))
            supp = tuple(sorted(rng.sample(range(P), s)))
            vals = tuple(rng.randrange(sizes[l]) for l in supp)
            events.append((supp, vals))
        events = list(set(events))
        for x in itertools.product(*[range(m) for m in sizes]):
            A = [e for e in events if all(x[l] == v for l, v in zip(*e))]
            V = set().union(*[set(e[0]) for e in A]) if A else set()
            N = len(V)
            a = [sum(1 for e in A if l in e[0]) for l in range(P)]
            for L in range(0, P + 2):
                # direct definition
                B = 0
                for r in range(len(A) + 1):
                    for F in itertools.combinations(A, r):
                        sF = set().union(*[set(e[0]) for e in F]) if F else set()
                        if len(sF) <= L:
                            B += (-1) ** r
                ind = 1 if not A else 0
                if A:
                    R = 0
                    for w in range(0, min(L, N) + 1):
                        for W in itertools.combinations(sorted(V), w):
                            if w == N:
                                continue
                            if any(set(e[0]) <= set(W) for e in A):
                                continue
                            R += (-1) ** (L - w) * comb(N - w - 1, L - w)
                    assert R == B, (events, x, L, B, R)
                    if N <= L:
                        assert B == 0
                else:
                    assert B == 1
                G = esym(a, L + 1)
                assert B - 4 ** (L + 1) * G <= ind, (events, x, L)
                assert abs(B - ind) <= 4 ** (L + 1) * G, (events, x, L)
                checked += 1
    print(f"trials={trials} seed={seed}: {checked} (system,x,L) cases, 0 failures")


if __name__ == "__main__":
    run(int(sys.argv[1]) if len(sys.argv) > 1 else 300, int(sys.argv[2]) if len(sys.argv) > 2 else 1)
