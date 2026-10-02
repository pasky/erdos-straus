"""Independent check of EXCEPTIONAL_TWIN2 Theorem 1.4 (reviewer's own code).

log(Z2(rho)/Z1^2) <= (1+25 delta) [sum_e rho_l rho_m pi_e + sum_j rho_j q_j]
whenever every prime mass w_l <= delta <= 1/16.

Z1 by direct enumeration of the product space; Z2 by brute-force enumeration
of the *doubled* space (pairs (y,y')), independent of any contraction trick.
Also an adversarial hill-climb over nu, rho, edges.
Usage: thm14_check.py MODE SEED N
"""
import itertools, math, sys
import numpy as np
KMAX = int(sys.argv[4]) if len(sys.argv) > 4 else 4

def system_arrays(sizes, edges):
    # forbidden indicator over product space: f[y]=1 iff no edge occurs
    shape = tuple(sizes)
    f = np.ones(shape, dtype=bool)
    k = len(sizes)
    for (l, a, m, c) in edges:
        idx = [slice(None)] * k
        idx[l] = a; idx[m] = c
        f[tuple(idx)] = False
    return f

def exact(sizes, nus, edges, rho):
    k = len(sizes)
    f = system_arrays(sizes, edges)
    P = nus[0]
    for nu in nus[1:]:
        P = np.multiply.outer(P, nu)
    Z1 = float((P * f).sum())
    # doubled space brute force: axes (y_1..y_k, y'_1..y'_k)
    mu = [rho[l] * np.diag(nus[l]) + (1 - rho[l]) * np.outer(nus[l], nus[l]) for l in range(k)]
    # joint law over (Y_1..Y_k), Y_l=(y_l,y'_l): build as tensor with axes (y1,y1',y2,y2',...)
    J = mu[0]
    for l in range(1, k):
        J = np.multiply.outer(J, mu[l])
    # reorder f(y) f(y') into same axis order
    ff = np.multiply.outer(f, f)  # axes y1..yk, y1'..yk'
    perm = []
    for l in range(k):
        perm += [l, k + l]
    ff = np.transpose(ff, perm)
    Z2 = float((J * ff).sum())
    return Z1, Z2

def stats(sizes, nus, edges, rho):
    k = len(sizes)
    deg = [np.zeros(n) for n in sizes]
    w = np.zeros(k); diag = 0.0
    for (l, a, m, c) in edges:
        pi = nus[l][a] * nus[m][c]
        deg[l][a] += nus[m][c]; deg[m][c] += nus[l][a]
        w[l] += pi; w[m] += pi
        diag += rho[l] * rho[m] * pi
    q = np.array([float((nus[l] * deg[l] ** 2).sum()) for l in range(k)])
    return w, diag + float((rho * q).sum())

def rand_system(rng):
    k = int(rng.integers(2, KMAX + 1))
    sizes = [int(rng.integers(2, 6 if k <= 4 else 5)) for _ in range(k)]
    nus = [rng.dirichlet(np.full(n, rng.choice([0.3, 1, 5]))) for n in sizes]
    verts = [(l, a) for l in range(k) for a in range(sizes[l])]
    allpairs = [(l, a, m, c) for (l, a) in verts for (m, c) in verts if l < m]
    mode = rng.integers(3)
    if mode == 0:
        p = rng.uniform(0.05, 0.6)
        edges = [e for e in allpairs if rng.random() < p]
    elif mode == 1:  # hubs: one vertex per coord joined to everything
        hubs = {l: int(rng.integers(sizes[l])) for l in range(k)}
        edges = [e for e in allpairs if hubs[e[0]] == e[1] or hubs[e[2]] == e[3]]
    else:  # cycles / triangles through single vertices
        edges = [e for e in allpairs if e[1] == 0 or e[3] == 0 or rng.random() < 0.2]
    rho = rng.uniform(0, 1, k) if rng.random() < 0.5 else np.ones(k)
    return sizes, nus, edges, rho

def scale_to_delta(sizes, nus, edges, rho, delta):
    # concentrate nu: tilt so that max w <= delta by adding a big "safe" residue
    nus2 = []
    for l, nu in enumerate(nus):
        nus2.append(nu)
    return nus2

def ratio(sizes, nus, edges, rho):
    w, rhs = stats(sizes, nus, edges, rho)
    d = max(w.max(), 1e-15)
    Z1, Z2 = exact(sizes, nus, edges, rho)
    lhs = math.log(Z2 / Z1 ** 2)
    return lhs, rhs, d

def add_safe(nus, s):
    # append a residue of mass 1-s that is in no edge; scales other masses by s
    return [np.concatenate([nu * s, [1 - s]]) for nu in nus]

def main():
    mode, seed, N = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(seed)
    worst = 0.0; n_in = 0
    for t in range(N):
        sizes, nus, edges, rho = rand_system(rng)
        if not edges:
            continue
        # make delta small enough by adding a safe residue (shrinks masses)
        w, _ = stats(sizes, nus, edges, rho)
        target = rng.uniform(0.002, 1 / 16)
        s = min(1.0, math.sqrt(target / max(w.max(), 1e-12)))
        nus = add_safe(nus, s); sizes = [n + 1 for n in sizes]
        lhs, rhs, d = ratio(sizes, nus, edges, rho)
        if d > 1 / 16 + 1e-12:
            continue
        n_in += 1
        r = lhs / ((1 + 25 * d) * rhs)
        if mode == "adv":
            # hill-climb rho and nu to increase r
            best = (r, nus, rho)
            for it in range(60):
                _, nb, rb = best
                rho2 = np.clip(rb + rng.normal(0, 0.1, len(rb)), 0, 1)
                nus2 = [np.abs(nu * np.exp(rng.normal(0, 0.2, len(nu)))) for nu in nb]
                nus2 = [nu / nu.sum() for nu in nus2]
                w2, _ = stats(sizes, nus2, edges, rho2)
                if w2.max() > 1 / 16:
                    continue
                l2, r2, d2 = ratio(sizes, nus2, edges, rho2)
                rr = l2 / ((1 + 25 * d2) * r2) if r2 > 0 else 0
                if rr > best[0]:
                    best = (rr, nus2, rho2)
            r = best[0]
        if r > worst:
            l3, r3, d3 = ratio(sizes, best[1], edges, best[2]) if mode == "adv" else (lhs, rhs, d)
            info = (r, l3, r3, d3, len(edges), sizes, (best[2] if mode=="adv" else rho).round(3).tolist())
        worst = max(worst, r)
        if r > 1:
            print("VIOLATION", t, r, sizes, edges)
    print("worst info", info)
    print(f"mode={mode} seed={seed} trials_in_range={n_in} worst lhs/((1+25d)rhs)={worst:.4f}")

if __name__ == "__main__":
    main()
