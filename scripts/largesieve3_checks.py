"""Sanity checks for EXCEPTIONAL_LARGESIEVE3.md (EVIDENCE only).

1. Theorem 1.1 core inequality  R_{p'}(pi) <= rho * E_{pi_s} R_{p'}(pi_c)
   for pi = sum_c pi_s(c) delta_c x pi_c on a toy rough-slice mixture.
2. Theorem 3.1 product formula  R_{p'}(pi_c) = prod_l (1 + sum_{a!=0}|phi|^{p'})
   and the bound sum_{a!=0}|phi|^{p'} <= g^{1+2beta}.
3. Lemma 4.1: P_S = E_{x,y} prod h_l and R_{p'} <= sum_S s_S^{2beta} P_S
   for a random (non-product) measure.
Run: PYTHONPATH=scripts uv run --with numpy python scripts/largesieve3_checks.py
"""
import itertools
import numpy as np

rng = np.random.default_rng(59)
SMOOTH = [3, 5, 7]
ROUGH = [11, 13]
M_s = int(np.prod(SMOOTH))
M_r = int(np.prod(ROUGH))
M = M_s * M_r


def crt(c, r):
    # n mod M with n = c mod M_s, n = r mod M_r
    for n in range(c, M, M_s):
        if n % M_r == r:
            return n
    raise ValueError


def R_pp(meas, pp):
    f = np.fft.fft(meas)  # f[k] = sum_n meas[n] e(-nk/M); |.| same as pi-hat
    return float(np.sum(np.abs(f) ** pp))


def toy_family():
    """classes (b, G): smooth-only classes and rough-slice classes G = G_s * l."""
    fam = []
    divs_s = [d for k in range(1, 4) for d in map(lambda t: int(np.prod(t)), itertools.combinations(SMOOTH, k))]
    for _ in range(4):
        G = int(rng.choice(divs_s))
        fam.append((int(rng.integers(G)), G))
    for l in ROUGH:
        for _ in range(3):
            G = int(rng.choice(divs_s + [1])) * l
            fam.append((int(rng.integers(G)), G))
    return fam


def check_thm11(trials=20, beta=0.25):
    pp = 2 + 2 * beta
    worst = 0.0
    for _ in range(trials):
        fam = toy_family()
        A = np.ones(M, bool)
        for b, G in fam:
            A[np.arange(M) % G == b % G] = False
        As = [c for c in range(M_s) if not any(all(G % l for l in ROUGH) and c % G == b % G for b, G in fam)]
        if not As:
            continue
        pi = np.zeros(M)
        Ec = 0.0
        ok = True
        for c in As:
            # rough-slice fibre: forbidden residues per rough prime
            allowed = {}
            for l in ROUGH:
                F = {b % l for b, G in fam if G % l == 0 and c % (G // l) == b % (G // l)}
                allowed[l] = [x for x in range(l) if x not in F]
                if not allowed[l]:
                    ok = False
            if not ok:
                break
            pc = np.zeros(M_r)
            for r in range(M_r):
                if all(r % l in allowed[l] for l in ROUGH):
                    pc[r] = 1.0
            pc /= pc.sum()
            Ec += R_pp(pc, pp) / len(As)
            for r in np.nonzero(pc)[0]:
                pi[crt(c, int(r))] += pc[r] / len(As)
        if not ok:
            continue
        assert np.all(A[pi > 0]), "pi not supported on A"
        rho = M_s / len(As)
        lhs, rhs = R_pp(pi, pp), rho * Ec
        worst = max(worst, lhs / rhs)
    print(f"Thm 1.1: max R(pi)/(rho E R(pi_c)) = {worst:.4f} (must be <= 1)")
    assert worst <= 1 + 1e-9


def check_product(beta=0.3):
    pp = 2 + 2 * beta
    l = 31
    for f in range(1, 8):
        F = rng.choice(l, f, replace=False)
        u = np.ones(l)
        u[F] = 0
        u /= u.sum()
        phi = np.abs(np.fft.fft(u))
        s = np.sum(phi[1:] ** pp)
        g = f / (l - f)
        assert s <= g ** (1 + 2 * beta) + 1e-12
        assert abs(np.sum(phi[1:] ** 2) - g) < 1e-9
    print("Thm 3.1 local bound sum|phi|^{p'} <= g^{1+2beta}, Parseval sum|phi|^2 = g: ok")


def check_lemma41(beta=0.2):
    pp = 2 + 2 * beta
    primes = [3, 5, 7]
    m = 105
    sig = rng.random(m) ** 6
    sig /= sig.sum()
    fh = np.fft.fft(sig)
    bound = 0.0
    for S in itertools.chain.from_iterable(itertools.combinations(primes, k) for k in range(4)):
        # support of den(t/m): primes p with p not dividing t
        idx = [t for t in range(m) if set(p for p in primes if t % p != 0) == set(S)]
        P = float(np.sum(np.abs(fh[idx]) ** 2))
        x = np.arange(m)
        H = np.ones((m, m))
        for p in S:
            H *= p * (x[:, None] % p == x[None, :] % p) - 1
        P2 = float(sig @ H @ sig)
        assert abs(P - P2) < 1e-10, (S, P, P2)
        s = float(np.max(np.abs(fh[idx])))
        bound += s ** (2 * beta) * P
    R = float(np.sum(np.abs(fh) ** pp))
    assert R <= bound + 1e-12
    print(f"Lemma 4.1: two-copy identity ok; R={R:.4f} <= sum_S s^2b P_S = {bound:.4f}")


if __name__ == "__main__":
    check_product()
    check_lemma41()
    check_thm11()
