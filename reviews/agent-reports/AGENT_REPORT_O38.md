# AGENT REPORT O38 (branch side-agent/esw-suppression): ESW via a generating function

Deliverable: `POINTWISE_OMEGA10.md`, `scripts/omega10_*.py`. Checkpoint 1,
not self-reviewed by a subagent yet. Merged `side-agent/omega9-exponent` first.

## Results

1. **Check of O9 §4 (§1).** Lemma 4.1 and Cor 4.2 are correct as stated
   (Cor 4.2's second bullet is a valid necessary condition; EL is even
   stronger in the limit since `m→∞`). Arithmetic slip: `kS*𝓛≍𝓛^6`, not
   `𝓛^6/log𝓛`. Scope caveat: the "1/6 ceiling" charges every junta
   coordinate `≍𝓛`. The lower-bound juntas are unions of event supports,
   costing `≤Σlog r_E ≤ j𝓛` in modulus, so a **modulus-weighted** argument
   has floor `≍S𝓛` (≈1/5 under ET), not `kS𝓛`.
2. **New tool: the energy generating function** `G_F(λ)=Σ_U∏_{v∈U}λ_v‖F^{=U}‖²`.
   The natural target is **C-1**: `G_F≤1` whenever every event has
   `w_E=∏_{v∈E}λ_v≤2`. It has no mass, codegree or quarantine hypothesis, and
   applies verbatim to the restricted systems `F^{(j)}`. With
   `λ_v=2^{log m_v/𝓛}` it gives a modulus-weighted EL at modulus
   `e^τ`, `τ≍𝓛(S+k𝓛)`, hence `log Z ≪ log Q_Π + 𝓛^5log𝓛` under ET
   (§4, PROVED implication). With `λ=2^{1/k}` it gives the energy form of
   ESW, `energy(F;t)≤2^{−t/k}`.
3. **One-event monotonicity (MONO) is FALSE** (explicit counterexample, §2),
   so C-1 cannot be proved by adding events one at a time.
4. **Lemma 3.1 (PROVED): `G_F ≤ E_x Q_μ(𝓗(x))`.** Here 𝓗(x) is the
   hypergraph of supports of the events that hold at x, and
   `Q_μ(𝓗)=Σ_Vμ^V τ̂(V)²` is the μ-weighted squared Möbius mass of 𝓗's
   transversal indicator. Suppression is built in: the term vanishes when
   an event avoiding V holds at x. That is O9 §4.3's missing condition (b),
   now exact. At O9's hub the bound is `O(S_hub)`, not `e^{M/q}`.
5. So C-1 reduces to the **pointwise, purely combinatorial Conjecture Q**:
   `w_E≤2 ∀E ⟹ Q_μ(𝓗)≤1`. Stronger forms Q′ (`≤min w_E−1`), QM
   (`≤∏_{E∈𝓜}(w_E−1)` for any matching) and FM (fractional matchings) are
   also supported. No counterexample turned up in ~10⁵ random and
   hill-climbed instances (n≤10), and FM is often an equality.
   * Proved special cases: single edge, disjoint edges, two edges, `{0,1}`
     weights.
   * The natural induction (vertex deletion/contraction) closes exactly
     when a cross term X is ≥0. X<0 occurs, at triangles.

## Decision needed / next

* **Conjecture Q is the crux.** If it is proved, ESW's bit factor is gone
  and the junta term becomes `≪𝓛^5log𝓛`. The exponent then hinges on the
  quarantine: we need `log Q_Π≪𝓛^5log𝓛`. Today it is `𝓛^7/log𝓛`, which
  now dominates, so without a quarantine improvement there is no exponent
  gain.
* Suggested: (a) continue the proof of Q. Candidate routes: a better
  inductive potential (FM's equality cases), the variational form
  `Q=τᵀK^{−1}...`, and topological bounds on `N(V)=±χ̃` (non-transversal
  complex). (b) In parallel, task item (2), the per-prime quarantine bound
  `w_ℓ≪𝓛^{O(1)}/ℓ`. Not started.
* Things to attack in review: Lemma 3.1's proof (restriction/top-component
  step, and multiplicity of events with equal support); §4's claim that
  digit coordinates make every ES event single-value with modulus product
  `r_E≤T`, and that restricted events keep `w≤2`.
