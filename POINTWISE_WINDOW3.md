# POINTWISE_WINDOW3 — Chen–Wu switching for two windows (`a_min(p)≥11`): a faithful model

Task O39 (branch `side-agent/window-switching`). Builds on POINTWISE_WINDOW2.md
(model 𝒯𝒫(θ), Prop 3.7, §6.2 caps, §7.1) and POINTWISE_WINDOW.md (W1, W2).
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment;
Model-PROVED / Model-CERTIFIED = inside the discrete model of WINDOW2 §3.

Status: in progress (checkpoint 0).

## 1. What a real switched sieve provides (the faithful constraint)

Fix a hard-prime window q∈{3,7}, q' the other one. Chen's switching for a family
of configurations in which `n_q=(p+q)/4` has a q-bad prime factor r:
write `n_q=m·r`, so `p=4mr−q`, and count primes in the *switched sequence*
```
E = E_q(𝓜,I) = { 4mr−q : m∈𝓜, r∈I prime, mr≤(x+q)/4 },
```
where `𝓜` is an arbitrary set of integers (any prescribed factorisation type
for the rest of `n_q`), I a range of primes. E is a bilinear (convolution)
sequence `α*β` with `β=1_{primes}` (Siegel–Walfisz). By Bombieri–Vinogradov for
convolutions (Motohashi 1976; Bombieri–Friedlander–Iwaniec I, Thm 0; level
`x^{1/2−o(1)}` when `I⊂[x^η, x^{1−η}]`), the linear upper-bound sieve on E counts
its primes to within the factor `F(2)·e^{−γ}·2/θ·… = 2/θ = 4` of the expected count
(Selberg/Brun–Titchmarsh constant at level θ=1/2). The other window's condition
"`n_{q'}=mr+(q'−q)/4` has no q'-bad prime `<x^η`" can be imposed in the same
upper sieve by the fundamental lemma at negligible cost.

What this **cannot** see: the large-prime configuration of `n_{q'}` (a "has a
prime factor in bin k" condition is not a sieve upper-bound condition), and the
split of mass between individual joint configurations. So, in the model, a
switched sieve gives exactly the **marginal caps**
```
(SW_K)   Σ_{C_{q'}} ν(C_q, C_{q'}) ≤ K · Σ_{C_{q'}} μ(C_q, C_{q'})   for every window-q configuration C_q≠∅,
```
for both q, with `K=4` (BV level, Selberg) as the unconditional baseline. (Each
point of C_q may serve as the switched prime r; the bound holds per C_q as soon as
one point is switchable, and multiplicities cancel between the two sides.)
These are *aggregate* constraints: weaker than WINDOW2 §6.2's per-joint-configuration
caps `ν(C)≤Kμ(C)`, so the required K under (SW_K) is at most the §6.2 threshold.
LP duality: the dual of "min ν(∅,∅) s.t. Type-I correlations at level θ, parity,
ν≥0, (SW_K)" is exactly a Chen-type lower bound
`Σ_S y_S ρ(S) − K Σ_{q,C_q} λ_{q,C_q} μ_q(C_q)` with `λ≥0` — a Type-I sieve minus switched upper bounds.

Refinements a sieve *can* add (to be tested, §3): (a) restrict I to one bin and
𝓜 to a fixed factorisation type (already in SW_K: C_q is fixed); (b) impose
"no q'-bad prime `<z'`" with larger `z'` in the switched upper sieve, a dimension
`1+1/2` upper sieve with its own constant `K(z')`.

## 2. Model fidelity (repairing R29-M4)

### 2.1 The continuum heuristic law is parity-blind; the K=8 bias is a binning artefact (EVIDENCE, quadrature)
Continuum law of one window: Poisson points of intensity `dt/(2t)` on `[ε,1]`, cofactor weight
`(u−Σt)^{−1/2}`. The Type-I data of a visible S (sum s) are `∏(dt/2t)·½(F_+(1−s)±F_−(1−s))`,
sign `(−1)^{|S|}`, where `F_±(u)=Σ_k (±1)^k/k!∫∏dt_i/(2t_i)(u−Σt)^{−1/2}`. Real data
(BV + fundamental lemma, Thm P1) are `∝∏g(d)`, parity-blind: they need `F_+` constant and `F_−≈0`.
`/tmp`-free replay: `scripts/window3_cont.py EPS 4000` (grid quadrature, step 1/4000):

| ε | F_+(0.5) | F_+(1) | F_−(0.5)/F_+(0.5) | F_−(1)/F_+(1) |
|---|---|---|---|---|
| 0.10 | 4.145 | 4.161 | 3.1e-3 | 1.0e-3 |
| 0.05 | 5.864 | 5.887 | 1.4e-3 | 4.8e-4 |
| 0.02 | 9.287 | 9.325 | 5.3e-4 | 1.8e-4 |
| 0.01 | 13.17 | 13.23 | 2.6e-4 | 9e-5 |

So the continuum heuristic's data are product-form to 0.4% and parity-blind to 0.3% **already at
ε=0.1**. The R29 spread `r(S)∈[0.82,1.87]` comes from the discretisation of WINDOW2 (point
masses at bin centres, cofactor weight evaluated at the centre sum), not from ε.
**Repair adopted:** μ(C) := exact cell integral of the continuum law over the bin cell of C
(sub-grid quadrature, `scripts/window3_model.py`). Then ρ(S)=Σ_C emb(S,C)μ(C) are the exact
cell-aggregated continuum data, product-form and parity-blind to the accuracy above.

### 2.2 Cell-integrated law: data product-form and parity-blind to ≤0.27% (EVIDENCE, quadrature N=4000)
`scripts/window3_rcheck.py EPS K 0.5` computes `r(S)=ρ(S)/(∏w_k^{S_k}/S_k!)/ρ(∅)` for all visible S
(rep convention), for the even law and for the odd ("(p/3)=−1") law:

| (ε,K) | window configs (even) | r(S) range, even law | max \|r_even(S)−r_odd(S)\| |
|---|---|---|---|
| (0.1, 8) | 197 | [0.999993, 1.000004] | 2.7e-3 |
| (0.1, 12) | 685 | [0.999997, 1.000003] | 2.7e-3 |
| (0.07, 9) | 842 | [0.9999998, 1.0] | 2.2e-3 |
| (0.05, 10) | 4110 | [0.9999998, 1.0] | 1.9e-3 |

(Compare R29: [0.82,1.87] for WINDOW2's point-mass law.) The residual parity sensitivity is the
continuum `F_−` (it is ≍ the density of x^ε-smooth cofactors in reality, even smaller, but
≤0.3% either way). **R29-M4 is repaired for the data**: every LP below uses this law.
(The cell-integrated law includes configurations whose cell straddles Σ=1, with their mass
below 1; hence more configurations than WINDOW2 at the same grid.)
