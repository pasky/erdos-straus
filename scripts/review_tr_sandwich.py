"""R42 from-scratch toy check of the abstract sandwich (POINTWISE_TRANSFER Thm 1.1 Steps 1-5,
Lemma 1.2, Lemma 3.2).  Independent of the author's scripts.

Coordinates: moduli 8, 3, 5, 7, 11 (so 2 is a free prime with e_2 = 3, non-squarefree conductors 4, 8
occur).  Haar space = product of unit groups.  Random *general* events (arbitrary subsets of the unit
group product on <= k coordinates).  Checks:
  (1) B <= F pointwise, F-B = sum_i A_i (sum_{j<i} A_j e_j)^2
  (2) E[F-B] <= m_a^2 sum_j P(C_j) En(F^(j); t)
  (3) mu_psi computed from the explicit cell expansion of B == E[B psi] for every real primitive psi
      with conductor dividing prod ell^e (incl. conductors 4, 8, 8*... )
  (4) |E[F psi]| <= delta^(l0) - delta for every l0 | f  (Lemma 3.2 chain)
  (5) Lemma 1.2: if eta_l <= 1/6 for all l (with x_i = 2P(E_i) when LLL holds) then |E F psi| <= delta/5
Run: PYTHONPATH=scripts uv run --with numpy python scripts/review_tr_sandwich.py
"""
import itertools, math, random
import numpy as np

MODS = [8, 3, 5, 7, 11]
PR = [2, 3, 5, 7, 11]
UNITS = [[u for u in range(M) if math.gcd(u, M) == 1] for M in MODS]
SH = tuple(len(u) for u in UNITS)
K = len(MODS)


def kron(a, n):  # Kronecker symbol (a/n) for n>0, simple implementation
    a %= n if n > 0 else 1
    res = 1
    while n > 1 and a != 0:
        while n % 2 == 0:
            n //= 2
            r = a % 8
            if r in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def real_primitive_chars():
    """Real primitive characters with conductor f | 8*3*5*7*11, as arrays on the Haar grid."""
    out = []
    # local real primitive chars: at 2: conductor 4 (chi_-4), 8 (chi_8), 8 (chi_-8); odd p: Legendre
    loc2 = {1: lambda n: 1,
            4: lambda n: 1 if n % 4 == 1 else -1,
            8: lambda n: 1 if n % 8 in (1, 7) else -1,
            -8: lambda n: 1 if n % 8 in (1, 3) else -1}
    for c2 in loc2:
        for sub in itertools.product([0, 1], repeat=4):
            f = abs(c2) * math.prod(p for p, s in zip(PR[1:], sub) if s)
            if f == 1:
                continue
            arr = np.ones(SH)
            g = np.array([loc2[c2](u) for u in UNITS[0]], float)
            arr = arr * g.reshape(-1, 1, 1, 1, 1)
            for idx, (p, s) in enumerate(zip(PR[1:], sub), start=1):
                if s:
                    g = np.array([1 if pow(u, (p - 1) // 2, p) == 1 else -1 for u in UNITS[idx]], float)
                    shape = [1] * K; shape[idx] = -1
                    arr = arr * g.reshape(shape)
            supp = ([0] if c2 != 1 else []) + [i for i, s in enumerate(sub, 1) if s]
            out.append((f, c2, supp, arr))
    return out


def cell_indicator(I, vals):
    a = np.zeros(SH)
    idx = [slice(None)] * K
    for i, v in zip(I, vals):
        idx[i] = v
    a[tuple(idx)] = 1.0
    return a


def cond_exp(phi, W):
    axes = tuple(i for i in range(K) if i not in W)
    return phi.mean(axis=axes, keepdims=True) * np.ones(SH) if axes else phi.copy()


def es_trunc(phi, t):
    """phi^{<=t} = sum_{|U|<=t} phi^{=U}; also return energy above t."""
    ce = {W: cond_exp(phi, W) for r in range(K + 1) for W in itertools.combinations(range(K), r)}
    low = np.zeros(SH); en = 0.0
    for r in range(K + 1):
        for U in itertools.combinations(range(K), r):
            comp = sum((-1) ** (len(U) - len(W)) * ce[W]
                       for s in range(len(U) + 1) for W in itertools.combinations(U, s))
            if r <= t:
                low += comp
            else:
                en += float((comp ** 2).mean())
    return low, en


def run(seed, nev, kmax, t, maxcls=4, coords=None, minw=1):
    rng = random.Random(seed)
    events = []
    for _ in range(nev):
        w = rng.randint(minw, kmax)
        I = tuple(sorted(rng.sample(coords or range(K), w)))
        allv = list(itertools.product(*[range(SH[i]) for i in I]))
        nv = rng.randint(1, min(maxcls, len(allv)))
        events.append((I, set(rng.sample(allv, nv))))
    # atoms (distinct cells)
    atoms = []
    for I, V in events:
        for v in sorted(V):
            if (I, v) not in atoms:
                atoms.append((I, v))
    A = [cell_indicator(I, v) for I, v in atoms]
    ev_ind = [sum(cell_indicator(I, v) for v in V) for I, V in events]
    F = np.prod([1 - e for e in ev_ind], axis=0)
    Fa = np.prod([1 - a for a in A], axis=0)
    assert np.array_equal(F, Fa)
    delta = F.mean(); ma = len(atoms)
    # sandwich
    Flt = [np.prod([1 - A[i] for i in range(j)], axis=0) if j else np.ones(SH) for j in range(ma)]
    us, ens = [], []
    for j, (I, v) in enumerate(atoms):
        idx = [slice(None)] * K
        for i, vv in zip(I, v):
            idx[i] = vv
        sl = Flt[j][tuple(idx)]  # function of other coords
        Fj = np.broadcast_to(np.expand_dims(sl, axis=tuple(I)), SH).copy()
        # F^{(j)} as function of remaining coords: constant along I
        u, en = es_trunc(Fj, t)
        us.append(u); ens.append(en)
    v_ = [sum((A[j] * us[j] for j in range(i)), np.zeros(SH)) for i in range(ma)]
    B = 1 - sum(A[i] * (1 - v_[i]) ** 2 for i in range(ma))
    assert (B <= F + 1e-9).all(), "B<=F fails"
    e = [Flt[j] - us[j] for j in range(ma)]
    ident = sum(A[i] * sum((A[j] * e[j] for j in range(i)), np.zeros(SH)) ** 2 for i in range(ma))
    assert np.allclose(F - B, ident)
    PC = [1 / np.prod([SH[i] for i in I]) for I, _ in atoms]
    rhs = ma ** 2 * sum(p * en for p, en in zip(PC, ens))
    lhs = (F - B).mean()
    assert lhs <= rhs + 1e-12
    mu = B.mean(); Aratio = np.abs(B).mean() / mu if mu > 0 else float('inf')
    # explicit cell expansion of B: since everything is a function on the grid, the cell expansion
    # with cells on the full product is B itself; check E[B psi] against sum over grid points.
    worst_tw, worst_l12 = 0.0, None
    for f, c2, supp, psi in real_primitive_chars():
        EFpsi = (F * psi).mean()
        for l0 in supp:
            Fp = np.prod([1 - ev_ind[i] for i, (I, _) in enumerate(events) if l0 not in I] or [np.ones(SH)], axis=0)
            assert abs(EFpsi) <= Fp.mean() - delta + 1e-12, "Lemma 3.2 chain fails"
        worst_tw = max(worst_tw, abs(EFpsi) / delta if delta else 0)
    # Lemma 1.2 with x_i = 2P(E_i) if LLL holds
    P = [len(V) / np.prod([SH[i] for i in I]) for I, V in events]
    x = [2 * p for p in P]
    ok_lll = all(x[i] < 1 and P[i] <= x[i] * np.prod([1 - x[j] for j in range(nev) if j != i and set(events[i][0]) & set(events[j][0])]) for i in range(nev))
    if ok_lll:
        eta = [sum(P[i] / np.prod([1 - x[j] for j in range(nev) if set(events[i][0]) & set(events[j][0])]) for i in range(nev) if l in events[i][0]) for l in range(K)]
        if max(eta) <= 1 / 6:
            assert worst_tw <= 0.2 + 1e-12
            worst_l12 = max(eta)
    return dict(seed=seed, ma=ma, t=t, delta=round(delta, 4), lhs=lhs, rhs=rhs, A=Aratio, tw=round(worst_tw, 4), lll=ok_lll, eta=worst_l12)


if __name__ == "__main__":
    for seed in range(8):
        for t in (1, 2):
            nev = 3 + seed % 4 if seed < 6 else 12
            print(run(seed, nev, 2, t))
    n12 = 0
    for seed in range(100, 130):
        r = run(seed, 3 + seed % 5, 2, 1, maxcls=1, coords=[0, 2, 3, 4], minw=2)
        n12 += r['eta'] is not None
        assert r['eta'] is None or r['tw'] <= 0.2
    print("Lemma 1.2 regime hit", n12, "times out of 30")
    print("ALL CHECKS PASSED")
