"""R47 from-scratch brute force of Thm 6.9 (filtration energy bound).

Coordinates ell=0..L-1, each a tuple of independent digits i0(ell)<=i<f(ell)
with arbitrary distributions.  Events: digit-prefix events fixing digits
i0<=i<v_ell for each ell.  Weights lambda_ell>=1 with prod lambda^{2 v_ell(E)}<=2.
Check  sum_U prod_{ell:U_ell nonempty} lambda_ell^{1+max U_ell} ||F^{=U}||^2 <= 1.
Also checks Lemma 7.1-style fact used later is not needed here.
"""
import itertools, random, math
import numpy as np
from review_r47_energy import es_components, norm2

def run(trials=400, seed=7):
    rng = random.Random(seed)
    worst = 0.0
    for t in range(trials):
        L = rng.randint(1, 3)
        i0 = [rng.randint(0, 2) for _ in range(L)]
        nd = [rng.randint(1, 3) for _ in range(L)]
        if sum(nd) > 6:
            continue
        digits = [(l, i) for l in range(L) for i in range(i0[l], i0[l] + nd[l])]
        sizes = [rng.randint(2, 3) for _ in digits]
        probs = []
        for s in sizes:
            p = np.array([rng.random() + 0.05 for _ in range(s)]); probs.append(p / p.sum())
        m = rng.randint(1, 5)
        events = []
        for _ in range(m):
            v = []
            for l in range(L):
                v.append(rng.choice([0] + list(range(i0[l] + 1, i0[l] + nd[l] + 1))))
            if all(v[l] <= i0[l] for l in range(L)):
                l = rng.randrange(L); v[l] = i0[l] + 1
            fix = {}
            for k, (l, i) in enumerate(digits):
                if i < v[l]:
                    fix[k] = rng.randrange(sizes[k])
            events.append((v, fix))
        lam = [1 + rng.random() * rng.choice([0.05, 0.3, 1]) for _ in range(L)]
        for _ in range(60):
            mx = max(math.prod(lam[l] ** (2 * v[l]) for l in range(L)) for v, _ in events)
            if mx <= 2 + 1e-12: break
            lam = [x ** (math.log(2) / math.log(mx)) for x in lam]
        F = np.ones(sizes)
        for v, fix in events:
            ind = np.zeros(sizes); idx = [slice(None)] * len(digits)
            for k, s in fix.items(): idx[k] = s
            ind[tuple(idx)] = 1; F = F * (1 - ind)
        comps = es_components(F, sizes, probs)
        tot = 0.0
        for U, c in comps.items():
            w = 1.0
            for l in range(L):
                Ul = [digits[k][1] for k in U if digits[k][0] == l]
                if Ul: w *= lam[l] ** (1 + max(Ul))
            tot += w * norm2(c, probs)[0]
        worst = max(worst, tot)
        assert tot <= 1 + 1e-9, (tot, events, lam, i0)
    print("Thm 6.9 brute force: worst weighted energy =", worst)

if __name__ == "__main__":
    run()
