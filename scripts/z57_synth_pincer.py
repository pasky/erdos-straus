# z57 SYNTH §3.I: hypothetical effectivity calibration (Assessment-level arithmetic, no theorem about proofs).
# (1) Numerical evaluation (scipy quad) of the exact area integral of the part of Theorem V's region G_lambda (Z56_FAMDESIGN §1; coordinates x = min(a,b), y = max(a,b),
#     both orders counted) whose Burgess margin y - (1+x)/4 is >= mu, and the margin set S_mu (0 < margin < mu) in G.
# (2) The optimistic slice-exponent envelope delta(x, mu) = mu^2/(1+x) of Lemma E1: area kept when every kept slice has
#     saving >= delta0, i.e. margin >= sqrt((1+x) delta0).
# (3) Envelope crossovers: smallest p with m L^2 > K L^k p^{-delta} (Prop E3's normalisation), m := (3/pi^2) * kept area.
# usage: uv run --with scipy python scripts/z57_synth_pincer.py
import math
from scipy.integrate import quad
from scipy.optimize import brentq
LAM = 1 / 15
def kept_area(margin, lam=LAM):  # margin: function of x giving the required margin
    f = lambda x: max(0.0, (1 - x) - max(x, (1 + x) / 4 + margin(x)))
    return 2 * quad(f, lam, 0.5, limit=200, points=[1 / 3])[0]
A0 = kept_area(lambda x: 0.0)
print(f'area(G_1/15) = {A0:.10f} (29/90 = {29/90:.10f}); Burgess-only constant (3/pi^2)*area = {3/math.pi**2*A0:.6f}')
def Smu(mu):  # area of {(a,b) in G : 0 < margin < mu}, lam = 0
    return kept_area(lambda x: 0.0, 0.0) - kept_area(lambda x: mu, 0.0)
for mu in (0.01, 0.05, 1 / 12):
    print(f'S_mu area at mu={mu:.4f}: {Smu(mu):.10f}  vs 2mu/3+4mu^2/3 = {2*mu/3+4*mu*mu/3:.10f}')
for frac in (0.5, 0.9):
    target = frac * A0
    mu = brentq(lambda m: kept_area(lambda x: m) - target, 0.0, 0.5)
    d0 = brentq(lambda d: kept_area(lambda x: math.sqrt((1 + x) * d)) - target, 1e-9, 0.2)
    print(f'keep {frac:.0%} of area(G_1/15): uniform margin mu = {mu:.10f}' + (f' ((8-sqrt29)/12 = {(8-math.sqrt(29))/12:.10f})' if frac == 0.5 else '') +
          f'; envelope delta0 = {d0:.10f}')
    m = 3 / math.pi ** 2 * target
    for K, k in ((1, 2), (10, 3), (100, 3)):
        # solve delta*ln p = ln(K/m) + (k-2) ln ln p for the large root
        g = lambda lp: d0 * lp - (math.log(K / m) + (k - 2) * math.log(lp))
        lp = brentq(g, max(10.0, (k - 2) / d0 + 1e-6) if k > 2 else 1.0, 1e7)
        print(f'   m = {m:.5f}, (K,k) = ({K},{k}): envelope crossover log10 p = {lp/math.log(10):.1f}')
# Prop E3 table (m = 0.10, observed minimum of M_gen/L^2 on the tested primes)
print('E3 table (m = 0.10): delta > [ln(K/m) + (k-2) ln L]/ln p')
for K, k in ((1, 2), (10, 2), (10, 3), (100, 4)):
    print(f'  (K,k)=({K},{k}): ' + '  '.join(f'p=1e{N}: {(math.log(K/0.10)+(k-2)*math.log(N*math.log(10)))/(N*math.log(10)):.4f}' for N in (17, 18)))
# (4) crossover as a function of the kept fraction of area(G_1/15) (optimistic envelope; m = (3/pi^2) * kept area)
print('kept fraction -> envelope delta0, m, crossover log10 p for (K,k) = (1,2), (100,3)')
for frac in (0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.75, 0.9):
    target = frac * A0
    d0 = brentq(lambda d: kept_area(lambda x: math.sqrt((1 + x) * d)) - target, 1e-9, 0.45)
    m = 3 / math.pi ** 2 * target
    out = []
    for K, k in ((1, 2), (100, 3)):
        g = lambda lp: d0 * lp - (math.log(K / m) + (k - 2) * math.log(lp))
        lp = brentq(g, max(1.0, (k - 2) / d0 + 1e-6), 1e7)
        out.append(f'{lp/math.log(10):.1f}')
    print(f'  {frac:.2f}: delta0={d0:.4f} m={m:.5f} crossover log10 p: (1,2) {out[0]}, (100,3) {out[1]}')
# (5) the uniform-margin families F_mu of scripts/z57_synth_trimargin.c: kept fraction, smallest envelope exponent over kept
# slices (margin exactly mu at the largest admissible x), envelope crossovers.  Compare with zerofitm.txt (model x*).
print('uniform-margin families F_mu: kept fraction, delta_min = inf over kept slices of the envelope = mu^2/(1+x_max),\n'
      '  x_max = min((1+4mu)/3, (3/4-mu)/(5/4)) (the furthest x on the margin-mu boundary); crossovers (1,2), (100,3)')
for mu in (0.0533114024, 0.1, 0.12, 0.2179029330):
    A = kept_area(lambda x: mu); frac = A / A0; m = 3 / math.pi ** 2 * A
    # largest x with (1-x) - max(x, (1+x)/4 + mu) > 0
    # points at margin exactly mu: y = (1+x)/4 + mu needs y >= x (x <= (1+4mu)/3) and x + y < 1 (x < (3/4 - mu)/(5/4))
    xmax = min((1 + 4 * mu) / 3, (0.75 - mu) / 1.25)
    d = mu * mu / (1 + xmax)
    out = []
    for K, k in ((1, 2), (100, 3)):
        g = lambda lp: d * lp - (math.log(K / m) + (k - 2) * math.log(lp))
        out.append(f'{brentq(g, max(1.0, (k - 2) / d + 1e-6), 1e8) / math.log(10):.1f}')
    print(f'  mu={mu:.4f}: kept fraction {frac:.3f}, m={m:.5f}, x_max={xmax:.4f}, delta_min={d:.5f}, crossover log10 p: (1,2) {out[0]}, (100,3) {out[1]}')
