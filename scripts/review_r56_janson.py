"""R56 from-scratch exact test of Lemma 4.1, Lemma 4.2 and Thm 4.3 (Janson-type) of es-subexp-note v4.
Random small product spaces with non-uniform marginals, random atomic events."""
import itertools, math, random

def run(trials, seed=1):
    rng = random.Random(seed)
    checked = 0
    worst = 1e9
    for t in range(trials):
        nv = rng.randint(2, 5)
        sizes = [rng.randint(2, 6) for _ in range(nv)]
        probs = []
        for s in sizes:
            w = [rng.random() + 0.05 for _ in range(s)]
            z = sum(w); probs.append([x / z for x in w])
        pts = list(itertools.product(*[range(s) for s in sizes]))
        pw = [math.prod(probs[v][x[v]] for v in range(nv)) for x in pts]
        nE = rng.randint(1, 9)
        F = []
        for _ in range(nE):
            k = rng.randint(1, nv)
            S = rng.sample(range(nv), k)
            F.append({v: rng.randrange(sizes[v]) for v in S})
        def occ(E, x): return all(x[v] == a for v, a in E.items())
        def P(pred): return sum(p for x, p in zip(pts, pw) if pred(x))
        PE = [P(lambda x, E=E: occ(E, x)) for E in F]
        def conflict(E, G): return any(v in G and G[v] != a for v, a in E.items())
        def share(E, G): return any(v in G for v in E) and not conflict(E, G)
        # Lemma 4.1 check
        A = F[0]
        C = [G for G in F[1:] if not conflict(A, G)]
        lhs = P(lambda x: occ(A, x) and not any(occ(G, x) for G in C))
        rhs = PE[0] * P(lambda x: not any(occ(G, x) for G in C))
        assert lhs <= rhs + 1e-12, "compat"
        # LLL hypothesis with x_E = c*P(E), try several c
        for c in (1.5, 2.0, 3.0):
            xE = [min(c * p, 0.999) for p in PE]
            Gam = [[j for j in range(nE) if j != i and conflict(F[i], F[j])] for i in range(nE)]
            if not all(PE[i] <= xE[i] * math.prod(1 - xE[j] for j in Gam[i]) + 1e-15 for i in range(nE)):
                continue
            K = max(math.prod(1 / (1 - xE[j]) for j in Gam[i]) for i in range(nE))
            mu = sum(PE)
            Delta = sum(P(lambda x, i=i, j=j: occ(F[i], x) and occ(F[j], x))
                        for i in range(nE) for j in range(i + 1, nE) if share(F[i], F[j]))
            av = P(lambda x: not any(occ(G, x) for G in F))
            L = -math.log(av) if av > 0 else float('inf')
            b1 = mu - K * Delta
            b2 = mu / 2 if Delta == 0 else min(mu / 2, mu * mu / (4 * K * Delta))
            assert L >= b1 - 1e-12 and L >= b2 - 1e-12, ("janson", L, b1, b2)
            # Lemma 4.2 with random subfamily S and atomic A from F
            S = [G for G in F if rng.random() < 0.5]
            for i, A in enumerate(F):
                avS = P(lambda x: not any(occ(G, x) for G in S))
                if avS == 0: continue
                cond = P(lambda x: occ(A, x) and not any(occ(G, x) for G in S)) / avS
                bound = PE[i] * math.prod(1 / (1 - xE[j]) for j in range(nE) if F[j] in S and conflict(A, F[j]))
                assert cond <= bound + 1e-12, "lopsided"
            worst = min(worst, L - max(b1, b2))
            checked += 1
            break
    print("trials", trials, "instances with LLL hypothesis checked", checked, "min slack", worst)

if __name__ == "__main__":
    run(4000)
