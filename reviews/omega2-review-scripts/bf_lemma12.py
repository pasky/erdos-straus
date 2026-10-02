"""Independent brute force for POINTWISE_OMEGA2 Lemmas 1.1, 1.2, 1.3(2).
Written by the reviewer without reading scripts/omega2_abstract_check.py.
Events: arbitrary subsets of prod_{supp} Omega_l, supports of size 1..kmax.
Checks for every outcome x and every L in 0..|P|+1:
  (a) B_L(x) (definition, subsets F of A(x)) == closed form R_L (Lemma 1.1)
  (b) B_L - 4^{L+1} e_{L+1}(a) <= 1[A=0] and |B_L - 1[A=0]| <= 4^{L+1} e_{L+1}(a)
  (c) M_1(B_L) (exact cell expansion, merged per (U,cell)) <= E prod(1+2 a_l)
      with uniform independent X_l.
"""
import itertools, random, sys
from math import comb
from fractions import Fraction

def esym(vals, k):
    e = [1] + [0] * k
    for v in vals:
        for j in range(k, 0, -1):
            e[j] += e[j - 1] * v
    return e[k]

def run(trials, seed):
    rng = random.Random(seed)
    nfail = 0; ncase = 0; tight = 0.0
    for _ in range(trials):
        nP = rng.randint(1, int(sys.argv[4]) if len(sys.argv)>4 else 4)
        sizes = [rng.randint(1, 3) for _ in range(nP)]
        kmax = rng.randint(1, min(3, nP))
        nE = rng.randint(0, int(sys.argv[3]) if len(sys.argv)>3 else 6)
        events = []
        for _ in range(nE):
            k = rng.randint(1, kmax)
            supp = tuple(sorted(rng.sample(range(nP), k)))
            cells = list(itertools.product(*[range(sizes[l]) for l in supp]))
            p = rng.choice([0.2, 0.4, 0.7])
            S = frozenset(c for c in cells if rng.random() < p)
            events.append((supp, S))
        outcomes = list(itertools.product(*[range(s) for s in sizes]))
        prob = Fraction(1, len(outcomes))
        def occ(E, x):
            supp, S = E
            return tuple(x[l] for l in supp) in S
        for L in range(0, nP + 2):
            # (c) cell expansion of B_L: coefficient per (U, cell on U)
            coef = {}
            for r in range(0, nE + 1):
                for F in itertools.combinations(range(nE), r):
                    U = tuple(sorted(set().union(*[set(events[i][0]) for i in F]))) if F else ()
                    if len(U) > L:
                        continue
                    for c in itertools.product(*[range(sizes[l]) for l in U]):
                        xx = dict(zip(U, c))
                        if all(tuple(xx[l] for l in events[i][0]) in events[i][1] for i in F):
                            key = (U, c)
                            coef[key] = coef.get(key, 0) + (-1) ** r
            M1 = Fraction(0)
            for (U, c), v in coef.items():
                pc = Fraction(1, 1)
                for l in U:
                    pc /= sizes[l]
                M1 += abs(v) * pc
            Eprod = Fraction(0)
            for x in outcomes:
                A = [i for i in range(nE) if occ(events[i], x)]
                a = [sum(1 for i in A if l in events[i][0]) for l in range(nP)]
                V = set().union(*[set(events[i][0]) for i in A]) if A else set()
                N = len(V)
                prod2 = 1
                for v in a:
                    prod2 *= (1 + 2 * v)
                Eprod += prob * prod2
                # definition
                B = 0
                for r in range(0, len(A) + 1):
                    for F in itertools.combinations(A, r):
                        U = set().union(*[set(events[i][0]) for i in F]) if F else set()
                        if len(U) <= L:
                            B += (-1) ** r
                # closed form
                if not A:
                    R = 1
                else:
                    R = 0
                    Vl = sorted(V)
                    for w in range(0, min(L, N) + 1):
                        for W in itertools.combinations(Vl, w):
                            if w == N:
                                continue
                            Ws = set(W)
                            if any(set(events[i][0]) <= Ws for i in A):
                                continue
                            R += (-1) ** (L - w) * (comb(N - w - 1, L - w) if N - w - 1 >= L - w else 0)
                G = esym(a, L + 1)
                ind = 1 if not A else 0
                ncase += 1
                ok = (B == R) and (B - 4 ** (L + 1) * G <= ind) and (abs(B - ind) <= 4 ** (L + 1) * G)
                if A and N >= L + 1 and G > 0:
                    tight = max(tight, abs(B) / (4 ** (L + 1) * G))
                if not ok:
                    nfail += 1
                    if nfail < 5:
                        print("FAIL", events, x, L, B, R, G)
            ncase += 1
            if M1 > Eprod:
                nfail += 1
                print("M1 FAIL", events, L, M1, Eprod)
    print(f"seed={seed} trials={trials} cases={ncase} failures={nfail} max|B|/(4^(L+1)G)={tight:.4f}")

if __name__ == "__main__":
    run(int(sys.argv[1]), int(sys.argv[2]))
