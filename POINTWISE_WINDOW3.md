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
