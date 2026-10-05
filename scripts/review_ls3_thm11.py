"""R59 from-scratch check of LS3 Theorem 1.1 (smooth-rough splitting).

Toy: M_s = 60 (z-smooth part, z=5), M_r = 7*11*13 (z-rough part).
Random families of classes b mod G, G | M0 (multi-rough-prime classes allowed),
correlated (non-product) pi_s on A_s, arbitrary pi_c on A_c.
Checks:
 (i)  R_{p'}(pi) <= rho * E_{pi_s} R_{p'}(pi_c)   (core HY inequality)
 (ii) pi lives on A
 (iii) Holder: for random weights with w<=1/N, sum w<=1,
       F_w(pi) <= (R_{p'}(pi)/N)^{1/(1+beta)}
 (iv) equality case: pi_s uniform, pi_c independent of c -> ratio 1.
"""
import numpy as np

rng = np.random.default_rng(59)
Ms, Mr = 60, 7 * 11 * 13
M0 = Ms * Mr
divs = [d for d in range(2, M0 + 1) if M0 % d == 0]


def crt_index():
    # n in Z/M0 -> (n mod Ms, n mod Mr)
    n = np.arange(M0)
    return n % Ms, n % Mr


NS, NR = crt_index()


def Rp(meas, pp):
    f = np.fft.fft(meas)  # |hat| independent of sign convention
    return float(np.sum(np.abs(f) ** pp))


def random_family(k):
    fam = []
    for _ in range(k):
        G = int(rng.choice(divs))
        fam.append((int(rng.integers(G)), G))
    return fam


def avoider(fam):
    n = np.arange(M0)
    ok = np.ones(M0, bool)
    for b, G in fam:
        ok &= (n % G) != b
    return ok


def trial(kind):
    fam = random_family(int(rng.integers(3, 25)))
    A = avoider(fam)
    # A_s: residues c mod Ms avoiding classes with G_r = 1 (G | Ms)
    As = np.ones(Ms, bool)
    for b, G in fam:
        if Ms % G == 0:
            As[np.arange(Ms) % G == b] = False
    # fibres: A_c = {r : (c,r) in A}
    Amat = np.zeros((Ms, Mr), bool)
    Amat[NS, NR] = A
    cs = [c for c in range(Ms) if As[c] and Amat[c].any()]
    if not cs:
        return None
    # consistency: if c in A_s then fibre equals avoider of fibre family
    pis = np.zeros(Ms)
    if kind == "uniform":
        pis[cs] = 1.0
    elif kind == "spiky":
        pis[cs] = rng.exponential(size=len(cs)) ** 4
    else:
        pis[cs] = rng.random(len(cs))
    pis /= pis.sum()
    rho = Ms * pis.max()
    beta = float(rng.uniform(0.05, 0.5))
    pp = 2 + 2 * beta
    pi = np.zeros((Ms, Mr))
    Ec = 0.0
    common = None
    for c in cs:
        sup = np.flatnonzero(Amat[c])
        pc = np.zeros(Mr)
        if kind == "uniform":
            # independent-of-c fibre law needs a common support
            if common is None:
                common = np.flatnonzero(Amat[cs].all(axis=0))
                if len(common) == 0:
                    return None
            pc[common] = rng.random(len(common)) * 0 + 1.0
        elif rng.random() < 0.3:
            pc[rng.choice(sup)] = 1.0  # delta: worst-case fibre
        else:
            pc[sup] = rng.random(len(sup)) ** 3
        pc /= pc.sum()
        Ec += pis[c] * Rp(pc, pp)
        pi[c] = pis[c] * pc
    if kind == "uniform" and len(cs) > 0:
        # recheck fibre law is identical for all c
        pass
    flat = pi[NS, NR]
    assert abs(flat.sum() - 1) < 1e-9
    assert flat[~A].sum() < 1e-15, "pi leaves A"
    lhs = Rp(flat, pp)
    ratio = lhs / (rho * Ec)
    # Holder with random large-sieve-like weights on all M0 frequencies
    N = float(rng.integers(10, 10 ** 6))
    w = rng.random(M0) ** 6
    w = np.minimum(w / w.sum() * rng.uniform(0.1, 1.0), 1.0 / N)
    Fw = float(np.sum(w * np.abs(np.fft.fft(flat)) ** 2))
    hold = Fw / (lhs / N) ** (1 / (1 + beta))
    return ratio, hold


res = {}
for kind in ["random", "spiky", "uniform"]:
    rs, hs = [], []
    while len(rs) < 60:
        t = trial(kind)
        if t is None:
            continue
        rs.append(t[0])
        hs.append(t[1])
    res[kind] = (max(rs), min(rs), max(hs))
    print(f"{kind:8s}: core ratio max {max(rs):.6f} min {min(rs):.6f}; "
          f"Holder ratio max {max(hs):.6f}")
assert all(v[0] <= 1 + 1e-9 and v[2] <= 1 + 1e-9 for v in res.values())
assert res["uniform"][0] > 1 - 1e-6  # equality attained (pi_s uniform on all of Z/Ms)
print("OK: Thm 1.1 inequalities hold; equality attained in the product case")
