"""R116 from-scratch checks of the elementary analytic steps of EXCEPTIONAL_TYPEI_LOGLOG2 §1–§2.

(a) Lemma 1.2 / Prop 2.2 partial summation + Cauchy–Schwarz:
    |Σ c(n)ρ(n)|² ≤ (∫|c'|) ∫ |c'| |S(t)|² dt, with c(t) = λ φ̂(λt) (πtY)^{-s}, s = σ+1/L+iv complex,
    random ρ(n) of size n^{1/2} (worst case for convergence).
(b) The majorant |c'(t)| ≤ e²(2+|v|) Φ(t) w(t)^σ with w(t) = max(1, 1/(πtY0)), Y ∈ [Y0/√2, Y0].
(c) Lemma 2.1 Gamma bound |Γ((s−σ)/2)Γ((s+σ)/2)| ≤ C L² e^{−π|v|/2} on Re s = σ+1/L, σ ∈ (0, 1/4].
(d) ∫_1^∞Φ ≪ L λ₋ and λ₋^{a} ∫_1^∞ Φ(t) t^{1+a} dt ≪ 1 (a ∈ {0,1/2,1}).
Concrete Schwartz profile: φ̂(ξ) = exp(−ξ²)·(1+ξ) (not even, to test both signs).
"""
import numpy as np
import mpmath as mp

rng = np.random.default_rng(116)

def phihat(x):
    return np.exp(-x * x) * (1 + x)

def phihat_d(x):
    return np.exp(-x * x) * (1 - 2 * x * (1 + x))

def check_a(trials=40):
    worst = 0.0
    for _ in range(trials):
        lam = 10 ** rng.uniform(-3, 0.5)
        Y = 10 ** rng.uniform(-6, -1)
        sig = rng.uniform(1e-3, 0.25)
        L = 20.0
        v = rng.uniform(-5, 5)
        s = sig + 1 / L + 1j * v
        T = int(min(4e5, 12 / lam + 50))
        n = np.arange(1, T + 1, dtype=float)
        rho = (rng.normal(size=T) + 1j * rng.normal(size=T)) * np.sqrt(n)
        c = lam * phihat(lam * n) * (np.pi * n * Y) ** (-s)
        lhs = abs(np.sum(c * rho)) ** 2
        # integrals on a fine grid: S(t) is a step function constant on [n, n+1)
        S = np.cumsum(rho)
        sub = 16
        t = 1 + np.arange((T - 1) * sub) / sub + 0.5 / sub
        idx = np.floor(t).astype(int) - 1
        cp = (lam ** 2 * phihat_d(lam * t) - lam * phihat(lam * t) * s / t) * (np.pi * t * Y) ** (-s)
        dt = 1 / sub
        I1 = np.sum(np.abs(cp)) * dt
        I2 = np.sum(np.abs(cp) * np.abs(S[idx]) ** 2) * dt
        worst = max(worst, lhs / (I1 * I2))
    print(f"(a) max |Σcρ|²/((∫|c'|)∫|c'||S|²) over trials = {worst:.4f}  (must be ≤ 1, up to quadrature)")

def check_b(trials=2000):
    worst = 0.0
    for _ in range(trials):
        lam = 10 ** rng.uniform(-4, 1)
        Y0 = 10 ** rng.uniform(-8, -1)
        Yd = Y0 * rng.uniform(2 ** -0.5, 1)
        L = max(np.log(2 + 1 / Y0), 1.0)  # 𝓛 ≥ log(1/Y0) as required
        sig = rng.uniform(1e-4, 0.25)
        v = rng.uniform(-30, 30)
        s = sig + 1 / L + 1j * v
        t = 10 ** rng.uniform(0, 8)
        cp = abs((lam ** 2 * phihat_d(lam * t) - lam * phihat(lam * t) * s / t) * (np.pi * t * Yd) ** (-s))
        Phi = lam ** 2 * max(abs(phihat_d(lam * t)), abs(phihat_d(-lam * t))) + lam * max(abs(phihat(lam * t)), abs(phihat(-lam * t))) / t
        w = max(1.0, 1 / (np.pi * t * Y0))
        bound = np.e ** 2 * (2 + abs(v)) * Phi * w ** sig
        if Phi > 0 and bound > 0:
            worst = max(worst, cp / bound)
    print(f"(b) max |c'|/(e²(2+|v|)Φ w^σ) = {worst:.4f}  (must be ≤ 1)")

def check_c():
    worst = 0.0
    for L in [5, 20, 100, 1000]:
        for sig in [1e-6, 1e-3, 0.05, 0.25]:
            for v in np.concatenate([np.linspace(-60, 60, 241), [0.0]]):
                s = mp.mpf(sig) + mp.mpf(1) / L + 1j * mp.mpf(v)
                G = abs(mp.gamma((s - sig) / 2) * mp.gamma((s + sig) / 2))
                r = float(G / (L ** 2 * mp.e ** (-mp.pi * abs(v) / 2)))
                worst = max(worst, r)
    print(f"(c) max |G|/(L² e^(-π|v|/2)) over L,σ,v grid = {worst:.3f}  (bounded ⇒ OK)")

def check_d():
    from scipy.integrate import quad
    rows = []
    for lam in [1e-4, 1e-3, 1e-2, 0.1, 1.0, 3.0, 10.0]:
        Phi = lambda t: lam ** 2 * max(abs(phihat_d(lam * t)), abs(phihat_d(-lam * t))) + lam * max(abs(phihat(lam * t)), abs(phihat(-lam * t))) / t
        lm = min(lam, 1.0)
        L = np.log(2 / lm) + 1
        brk = [1, max(1.0, 1 / lam), max(1.0, 10 / lam), max(1.0, 100 / lam)]
        def integ(f):
            tot = 0
            for a, b in zip(brk[:-1], brk[1:]):
                if b > a:
                    tot += quad(f, a, b, limit=400)[0]
            tot += quad(f, brk[-1], np.inf, limit=400)[0]
            return tot
        I0 = integ(Phi) / (L * lm)
        Ia = [integ(lambda t, a=a: Phi(t) * t ** (1 + a)) * lm ** a for a in (0, 0.5, 1)]
        rows.append((lam, I0, *Ia))
    print("(d) λ, ∫Φ/(Lλ₋), λ₋^a∫Φt^{1+a} for a=0,1/2,1  (all must stay bounded):")
    for r in rows:
        print("    " + "  ".join(f"{x:9.3g}" for x in r))

if __name__ == "__main__":
    check_a()
    check_b()
    check_c()
    check_d()
