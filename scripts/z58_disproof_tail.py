# z58 DISPROOF §6.3: model zero tail of (MS) including local heterogeneity (Assessment; model only).
# Ingredients (all measured in this lane):
#  (i) zero law P(R = 0 | local mean mu) = kappa * exp(-a mu^beta), fitted on cells <= 2e8 (scripts/z58_disproof_zerolaw.py):
#      R8 law a = 0.398, beta = 1.014; kappa = model-error factor (the R8 law under-predicts the R zeros <= 2e8 by x2.5).
#  (ii) base mean of the class of one mod 840 (hardest Mordell class): mu_1(x) = c1 * L^2, c1 = 0.1286 (exact, 42 353
#      primes at 1e10, data/z58/disproof/runA/D1a.txt).
#  (iii) square-mimicking slices: a prime with p = 1 (840) and n_p = l (least quadratic non-residue = l >= 11) is a
#      square modulo every (l-1)-smooth modulus, hence (Lemma 2.2) keeps only the solutions none of whose three
#      moduli is (l-1)-smooth.  Its mean is modelled as mu_1(x) * surv(l-1, x)/surv(7, x) with surv from a Monte-Carlo of
#      the log-uniform solution density (validated at 1e10 against exact enumeration and against the design D2 = n_p > 31).
#      Share of the slice among p = 1 (840): 2^-(k) where l is the k-th prime >= 11 (heuristic independence of Legendre
#      symbols; exact on average by CRT).
# Output: for x = 1e8 .. 1e30, the expected number of (MS)-zeros among p = 1 (840) in [x, 10x] (all 6 Mordell classes
# modelled as the class of one: pro-zero), the dominant n_p, and E(> x).
# Run: uv run --with sympy python scripts/z58_disproof_tail.py [Nsamples]
import sys, math, random
from sympy import primerange, primepi
PR = list(primerange(2, 3000))
def min_lpf(ms, ycap=2999):
    """smallest y such that some modulus in ms is y-smooth (inf if none is ycap-smooth)."""
    best = math.inf
    for m in ms:
        while m % 2 == 0: m //= 2
        lp = 1
        for q in PR[1:]:
            if q > ycap or q >= best: break
            if m % q == 0:
                lp = q
                while m % q == 0: m //= q
            if m == 1: break
            if q * q > m:            # m is prime now
                if m <= ycap: lp = max(lp, m); m = 1
                break
        if m == 1 and lp < best: best = lp
    return best
def sample_s(p, n, rng):
    X = math.log(p / 4); out = []
    while len(out) < n:
        a, b = rng.random() * X, rng.random() * X
        if a + b > X: continue
        u = int(math.exp(a)); B = int(math.exp(b))
        if (u + B) % 2 == 0: continue
        C = (p + u + B) // (4 * u * B)
        if C < 1: continue
        out.append(min_lpf((4 * u * B, 4 * u * C - 1, 4 * B * C - 1)))
    return out
def surv_fn(ss):
    base = sum(1 for s in ss if s > 3)
    return lambda y: sum(1 for s in ss if s > y) / base
if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 40000
    rng = random.Random(5858)
    a, beta, c1 = 0.398, 1.014, 0.1286
    # measured class-1 mean R/L^2: 0.1146 at L ~ 15.0 (cells 1e6-1e7), 0.1206 at L ~ 17.3 (1e7-1e8), 0.1286 at L = 23.0
    # (runA D1a); linear in L below 1e10, frozen at 0.1286 above (pro-zero: no further growth assumed)
    c1eff = lambda L: min(c1, 0.1146 + (c1 - 0.1146) * (L - 15.0) / (23.0 - 15.0))
    print(f"# zero law kappa*exp(-a mu^beta), a={a}, beta={beta}; mu_1 = {c1} L^2; MC samples per decade = {N}")
    odd_np = [l for l in PR if l >= 11]
    rows = []
    for e in range(int(sys.argv[2]) if len(sys.argv) > 2 else 4, 31):
        x = 10.0 ** e; pmid = 10 ** e * 3
        ss = sample_s(pmid, N, rng); sv = surv_fn(ss)
        L = math.log(pmid); mu1 = c1eff(L) * L * L
        nprimes = (10 * x / math.log(10 * x) - x / math.log(x)) / 192.0  # p = 1 (840) in [x, 10x]
        tot = 0.0; best = (0, None, None)
        for k, l in enumerate(odd_np[:120], start=1):
            yprev = PR[PR.index(l) - 1]
            mu = mu1 * sv(yprev) / sv(7)
            share = 2.0 ** (-k)
            term = nprimes * share * math.exp(-a * mu ** beta)
            tot += term
            if term > best[0]: best = (term, l, mu)
        slices = [(nprimes * 2.0 ** (-k), mu1 * sv(PR[PR.index(l) - 1]) / sv(7)) for k, l in enumerate(odd_np[:120], start=1)]
        rows.append((e, tot, best, sv(31) / sv(7), sv(199) / sv(7), slices))
        print(f"[1e{e},1e{e+1}): E(zeros, kappa=1) = {tot:.3e}  dominant n_p = {best[1]} (mu = {best[2]:.1f}, term {best[0]:.2e});"
              f" rho(31) = {rows[-1][3]:.3f} rho(199) = {rows[-1][4]:.3f}; mu_1 = {mu1:.1f}", flush=True)
    print("# sensitivity (all six Mordell classes modelled as the class of one: x6): E[1e7,1e10) is CERTIFIED to be 0 observed")
    print("#   a     beta   E[1e5,1e7)   E[1e7,1e10)   E(>1e10)    E(>1e17)")
    for aa, bb in [(0.398, 1.014), (0.30, 1.0), (0.25, 1.0), (0.20, 1.0), (0.16, 1.0), (0.12, 1.0), (0.80, 0.70), (1.2, 0.6), (2.0, 0.5)]:
        E = lambda lo, hi: 6 * sum(sh * math.exp(-aa * mu ** bb) for r in rows if lo <= r[0] < hi for sh, mu in r[5])
        print(f"  {aa:5.3f} {bb:5.2f}  {E(5, 7):10.3e}  {E(7, 10):10.3e}  {E(10, 99):10.3e}  {E(17, 99):10.3e}")
    for e0 in (4, 6, 7, 8, 10, 12, 14, 17):
        print(f"E(> 1e{e0}) = {sum(r[1] for r in rows if r[0] >= e0):.3e}  (x kappa; kappa ~ 2.5 measured)")
