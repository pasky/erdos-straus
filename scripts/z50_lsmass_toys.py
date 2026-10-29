"""z50 lsmass: toy prime-slice families for the mass criterion (Theorem 2.1).

Random forbidden residues at primes; three profiles:
  A  fixed dimension kappa: omega(l) = kappa for 3 <= l <= z
  B  log-growing:           omega(l) = round(a log l) for 3 <= l <= z      (the ES5/U shape)
  C  high band:             omega(l) = ceil(rho l) only for l in (Q^{1/2}, Q]  (single-prime regime)
For each: true sifted count in [1,N] (exact sieve), Haar prediction, Montgomery's bound
(N+Q^2)/L(Q) with Q = sqrt(N), the achievable lower bound of Lemma 2.2 (tilted Chebyshev:
saving >= mass*(y) - log 4 at the largest y with Lam(y)+sqrt(2V(y)) <= log Q), and the
Rankin functional Psi(lambda) = inf_a [a lambda + sum p_l l^-a] at lambda = log N (THETA (2.5)).
"""
import math, json, sys
import numpy as np

def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = False
    return [int(p) for p in np.nonzero(s)[0]]

def run(N, family, rng, **kw):
    Q = int(math.isqrt(N))
    P = primes_upto(max(Q, kw.get("z", 0)) + 1)
    om = {}
    for l in P:
        if l < 3: continue
        if family == "A":
            if 4 * kw["kappa"] <= l <= kw["z"]: om[l] = kw["kappa"]
        elif family == "B":
            if l <= kw["z"]: om[l] = max(0, min(l // 4, int(round(kw["a"] * math.log(l)))))
        elif family == "C":
            if math.isqrt(Q) < l <= Q: om[l] = max(1, math.ceil(kw["rho"] * l))
    alive = np.ones(N + 1, dtype=bool); alive[0] = False
    haar = float(N)
    for l, w in om.items():
        if w == 0: continue
        for r in rng.choice(l, size=w, replace=False):
            alive[int(r)::l] = False
        haar *= (1 - w / l)
    true = int(alive.sum())
    # Montgomery L(Q)
    h = np.zeros(Q + 1); h[1] = 1.0
    # build multiplicatively over primes in om (squarefree products)
    for l, w in sorted(om.items()):
        if l > Q or w == 0: continue
        g = w / (l - w)
        # h[q*l] += h[q]*g for q coprime to l (process q descending to avoid reuse)
        idx = np.arange(Q // l, 0, -1)
        h[idx * l] += h[idx] * g * (idx % l != 0)
    LQ = float(h.sum())
    mont = (N + Q * Q) / LQ
    # achievable lower bound (Lemma 2.2)
    best_ach = 0.0
    mass = lam = V = 0.0
    for l, w in sorted(om.items()):
        p = w / l
        mass_n = mass - math.log1p(-p); lam_n = lam + p * math.log(l); V_n = V + p * math.log(l)**2
        if lam_n + math.sqrt(2 * V_n) <= math.log(Q):
            mass, lam, V = mass_n, lam_n, V_n
            best_ach = max(best_ach, mass - math.log(4))
        else:
            break
    # Rankin functional at lambda = log N
    lamb = math.log(N)
    psi = min(a * lamb + sum((w / l) * l**(-a) for l, w in om.items()) for a in np.linspace(0.005, 2, 400))
    full_mass = sum(-math.log1p(-w / l) for l, w in om.items())
    return {"family": family, "params": kw, "N": N, "full_mass": full_mass,
            "true_saving": math.log(N / max(true, 1)), "haar_saving": math.log(N / haar),
            "montgomery_saving": math.log(N / mont), "achievable_lemma22": best_ach,
            "rankin_Psi_at_logN": psi, "true_count": true}

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
    rng = np.random.default_rng(20261029)
    out = []
    for kappa in (1, 2, 4):
        for z in (100, 3000):
            out.append(run(N, "A", rng, kappa=kappa, z=z))
    for a in (0.5, 1.0, 2.0):
        for z in (100, 3000):
            out.append(run(N, "B", rng, a=a, z=z))
    for rho in (0.002, 0.01, 0.03):
        out.append(run(N, "C", rng, rho=rho))
    for r in out:
        print({k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items()})
    json.dump(out, open("data/z50_lsmass/toys.json", "w"), indent=1)

def L_profile(Qmax, omega_fn):
    """Exact Montgomery L(Q)=sum_{q<=Q sqfree} prod g(l) for a deterministic omega profile,
    together with the full Euler mass up to Q; returns rows at Q = 10^k."""
    P = primes_upto(Qmax)
    h = np.zeros(Qmax + 1); h[1] = 1.0
    massQ = 0.0
    rows = []
    marks = [10**k for k in range(2, 9) if 10**k <= Qmax]
    pts = []
    for l in P:
        w = omega_fn(l)
        if w <= 0 or 4 * w > l: continue
        g = w / (l - w)
        idx = np.arange(Qmax // l, 0, -1)
        h[idx * l] += h[idx] * g * (idx % l != 0)
    cum = np.cumsum(h)
    for Q in marks:
        m = sum(-math.log1p(-omega_fn(l) / l) for l in P if l <= Q and 0 < 4 * omega_fn(l) <= l)
        rows.append({"Q": Q, "logL": float(math.log(cum[Q])), "mass": m, "deficit": m - float(math.log(cum[Q]))})
    return rows

if __name__ == "__main__" and len(sys.argv) > 2:
    Qmax = int(sys.argv[2])
    prof = {}
    for kappa in (1, 2, 4):
        prof[f"A_kappa{kappa}"] = L_profile(Qmax, lambda l, k=kappa: k)
    for a in (0.5, 1.0, 2.0):
        prof[f"B_a{a}"] = L_profile(Qmax, lambda l, a=a: int(round(a * math.log(l))))
    for k, rows in prof.items():
        print(k, [(r["Q"], round(r["logL"], 2), round(r["mass"], 2), round(r["deficit"], 2)) for r in rows])
    json.dump(prof, open("data/z50_lsmass/toys_L.json", "w"), indent=1)
