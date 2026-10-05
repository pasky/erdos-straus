# Hostile review R44a of POINTWISE_OMEGA11.md (reviewer 1: §2 graded quarantine, Lemma 3.1 transfer)

Reviewed: branch side-agent/quarantine-bound @ 105a522 (merged into side-agent/review-omega11a).
Status: IN PROGRESS.

## Summary verdicts
(filled in as claims are checked)

## Defects

### Re-derivation notes: Setting 2.0, Lemma 2.1 (independent)

* Fibre law. On `n≡1 (Q)` (Haar on `(ℤ/N)^*`), CRT makes `n mod ℓ^{f_ℓ}` independent over ℓ,
  each uniform on `{x mod ℓ^f : x≡1 (ℓ^a)}` (`ℓ^{f−a}` points; units if a=0). For `v>a≥1`,
  `P(X≡c mod ℓ^v)=ℓ^{f−v}/ℓ^{f−a}=ℓ^{−(v−a)}`; for a=0, `1/φ(ℓ^v)` if c is a unit, else 0
  (ℓ|D: event impossible, still ≤ the bound). Both `≤(ℓ/(ℓ−1))ℓ^{min(v,a)}/ℓ^v`. CHECKED.
* Consistency: for `ℓ∈supp`, `ℓ^{a_ℓ}|gcd(M,Q)|4D+1`, so `−4D≡1 (ℓ^{a_ℓ})`. CHECKED.
* `P(E)≤(gcd(M,Q)/M)·M/φ(M)≤C loglogT·g/M`, using survival `gcd(M,Q)|g`. CHECKED.
* `S♯`: the O2 Lemma 4.1/11.1 proof sums `g/M` over *all* atoms; the only non-obvious step,
  the first term of the k-progression, is fine because `g|k+r'`, `k≥r'` force `k≥g/2`, so
  the first term is `≤2/g`. S♯ is Q-independent. CHECKED.
* (I): `n≡1 (Q)`, `n≡−4D (M)` ⇒ `gcd(M,Q)|4D+1`; `M|Q` contradicts Fact 1.1 (PO, `1∉𝓡(M)`);
  else `supp≠∅` (M odd, ℓ-part of Q is `ℓ^{a_ℓ}`) and E occurs, since `v_ℓ(M)≤f_ℓ`. CHECKED.

### Re-derivation notes: Lemma 2.2 (independent)

* Termination: each step raises some `a_ℓ<f_ℓ`; finite. Masses are NOT monotone in Q
  (raising `a_ℓ` multiplies `P(E)` at ℓ by ℓ for atoms with `v_ℓ>a_ℓ+1`), but neither
  termination nor the cost argument needs monotonicity: the cost uses only the Q-uniform
  majorant `w_ℓ(Q_i)≤Σ_{v_ℓ(M)≥a+1}s`. Survival is monotone decreasing in Q (not needed).
* (LLL): at the end, `ℓ∈supp E` ⇒ `a_ℓ<v_ℓ(M)≤f_ℓ`, so the stopping rule applies at ℓ:
  `w_ℓ≤c(a_ℓ+1)logℓ/𝓛≤c·v_ℓ(M)logℓ/𝓛`; summing, `≤c·logM/𝓛≤c`. CHECKED.
* Dependency structure with partial quarantine: E is measurable w.r.t. `{X_ℓ: ℓ∈supp E}`
  (quarantined digits are constants on the fibre); E is mutually independent of all events
  with disjoint support. Neighbours of E are among events with some `ℓ∈supp E∩supp E'`, whose
  total probability is `≤Σ_{ℓ∈supp E}w_ℓ` (w counts atoms, ≥ distinct events). With
  `x=2P`, `x_E≤2c≤1/4` and `∏_{E'∼E}(1−x_{E'})≥1−2c≥3/4≥1/2`. Then
  `−log(1−x)≤(4/3)x` gives `P(no event)≥exp(−(8/3)S_tot)≥exp(−4S♯)`. CHECKED.
* Cost: a step (ℓ,a→a+1) at stage `Q_i` has `logℓ<𝓛w_ℓ(Q_i)/(c(a+1))≤(𝓛/c)Σ_{v_ℓ(M)≥a+1}s/(a+1)`;
  each pair (ℓ,a) at most once; swap sums ⇒ `Σ s·Σ_{ℓ|M}H_{v_ℓ(M)}`. CHECKED.
  `H_v≤log₂(v+1)` (induction, `log₂(1+x)≥x` on [0,1]) and `Σ_ℓlog₂(v_ℓ+1)=log₂τ(M)`. CHECKED.
  Wigert: `log₂τ(M)≤(1+o(1))𝓛/log𝓛` uniformly for `M≤T`. CHECKED.
