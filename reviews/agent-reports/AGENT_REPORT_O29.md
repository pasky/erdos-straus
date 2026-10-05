# AGENT REPORT O29 — window-parity (branch `side-agent/window-parity`)

Deliverable: `POINTWISE_WINDOW2.md`; scripts `scripts/window2_{blockfake,treefake,lp,feas,polish,verify}.py`;
data `data/window2/fake_eps0.1_K8_theta0.5.json.gz`; archived sources `sources/window2/`
(FI09 Acta Math 2009, Sedunova arXiv:2609.28200, Nath–Xie arXiv:2501.16723).

## Outcome
* **Goal 1 (unconditional a_min≥11): NOT reached.** Routes (ii) well-factorable level,
  (iv) Maynard–Tao, (v) sub-families are closed (Assessment, with reasons in §4).
  Route (i), Type-II/Chen switching, is open but I found no foothold. The problem is
  exactly FI09-shaped (Lemma 1.2: `n, n+1` primitive norms from `Q(√−3)`,
  `Q(√−7)`, `p=4n−3`). FI09's lower bound is still open unconditionally (Sedunova 2026).
* **Goal 2 (parity obstruction as a theorem):**
  1. Thm P1 (PROVED mod BV/EH, actual primes): the classes `(p/3)=±1` have identical sieve
     data, and the `−1` class never has window 3 clean. So parity input is necessary.
     This is Selberg's example realised by primes.
  2. Model 𝒯𝒫(θ): Type-I correlations of level θ, plus both parities. One window:
     fakes for θ<1/2 (Model-PROVED); positive LP at θ=1/2 (EVIDENCE), matching W1.
  3. **Prop 3.7 (CERTIFIED in a discrete model, ε=0.1, K=8):** at θ=1/2 there is a fake with
     no both-clean mass. Check: residual 2.6e-15, all 89 support weights ≥0.154, and
     an independent brute-force verifier. So Type-I + parity at BV level does not
     yield two windows in the model. This covers all β/vector/Buchstab sieves without switching.
  4. Two-block, tree and product fakes (Lemmas 3.2, 3.6) do *not* explain this. They reach
     only ≈43% (MC, ε-stable). The LP fake is genuinely joint: the window marginals couple.
  5. The coarse-model threshold is θ_2∈(0.6,0.7] (EVIDENCE, grid-dependent; at θ=0.7 the
     value decreases as the grid is refined).
* Goal 3: not attempted.

## Caveats a reviewer should hit
* The "true law" of §3.3 is heuristic: half-dimensional density `∏1/(2t)·(1−Σt)^{−1/2}`,
  windows independent, bad primes <x^ε assumed sifted. Prop 3.7 is a statement about this
  discrete model, not about primes.
* The certified fake puts up to 9.3·10⁴ times the true mass on some configurations. Whether
  it is realisable by an integer sequence with bounded weights (capacity) was not checked.
  Primality information (switching, as in W1's T_2 and W2's T^{(q)}) is outside the model.
* At θ=0.6 the fake is LP-feasible (5e-4) but not certified. θ≥0.9 LPs hit numerical trouble.
* The continuum (ε→0, K→∞) threshold is not determined.

## Suggested next steps (for the parent's decision)
1. Larger and finer grids for the LP (ε≤0.07, K≥12; memory ~8 GB is the limit), with certified
   polish at θ=0.6, 0.7, 0.8, to locate θ_2 in the continuum.
2. Add a capacity constraint ν≤C·μ_int and a "switching" constraint family to the model.
   This tests whether primality info restores positivity at θ=1/2, i.e. whether an
   unconditional route exists in principle.
3. Extract an analytic description of the joint fake (marginal coupling, §3.5) and
   prove a continuum Model-theorem.
