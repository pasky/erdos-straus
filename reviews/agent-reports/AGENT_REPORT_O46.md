# Agent report O46 (branch side-agent/haar-exponent) — checkpoint 1

Deliverable: `POINTWISE_HAAR.md` (new), `scripts/haar_fit.py`,
`scripts/haar_janson_check.py`, `data/haar/`.

## Main result
**Theorem 2.1: `log(1/δ*(T)) ≫ 𝓛³/log𝓛`** (PROVED modulo the sieve
fundamental lemma only; no BV, no ET). Previous lower bound: `𝓛²` (OMEGA8
Prop 6.6, modulo the shifted-prime divisor lower bound (D'), proved there via
Brun–Titchmarsh + Bombieri–Vinogradov). So the Haar exponent `a ≥ 3`.
Now known: `𝓛³/log𝓛 ≪ Φ ≪ 𝓛^5 log𝓛` (upper: OMEGA12 Thm 6.3, modulo ET).
`T_0` is astronomically large (`𝓕 ≠ ∅` needs `T ≳ e^{90}`): purely asymptotic.

Ingredients:
1. Thm 1.4: a Janson-type inequality `−log P(no event) ≥ μ − KΔ` for
   *atomic* (partial-assignment) events on product spaces, where Δ counts only
   bit-sharing (compatible overlapping) pairs and K is a lopsided-LLL
   inflation factor. Harris fails for one-hot variables, so the classical
   Janson inequality does not apply directly; Lemma 1.1 (compatible events)
   + lopsided LLL (Lemma 1.3) replace it. Brute-force sanity check passes.
2. Family 𝓕: events `(M,D)` with M squarefree, `𝓛^5`-rough, `M ∈ [√T,T]`,
   `D* ∈ [𝓛², T^{1/10}]`. Mass `≫ 𝓛³/log𝓛` (fundamental lemma); per-prime
   loads `≤ 𝓛³/q` so the lopsided LLL holds; `Δ ≪ 𝓛²` by elementary counting
   (`M ≥ √T ≥ (D*)^5` kills progression first terms; `D* ≥ 𝓛²` kills the
   small-D hubs; `D≠D'` pairs need `g | D−D'`, averaged with (F5)).
3. Prop 1.5: *singleton* NA bounds (Lemma 1.2 with one event per group,
   squarefree moduli) give at most `S1 + O(log𝓛) ≍ 𝓛²` (S1 upper bound: standard,
   sketched). Grouped uses of Lemma 1.2 are not covered.

## Reconciliation (EVIDENCE)
The POINTWISE_SIZE §7.2 Monte Carlo has `Φ/(𝓛³/log𝓛) = 0.0691–0.0699` for
`1023 ≤ T ≤ 32767` — *consistent with* a = 3 plus a slowly decaying
correction, but the test discriminates weakly (spread 1.16% vs 1.85% for
`𝓛^{2.5}`), and the `log𝓛` of Thm 2.1 is a proof artefact. Conjecture 3.1:
`a = 3` (order `𝓛³/log𝓛` vs `𝓛³` left open).

## Prime side
Haar-only. Rigorous fixed-T density corollary via Prop 7.1(a); under RA the
one-exceedance level is `log T_N ≍ (log N log log N)^{1/3}` (Assessment; RA
does not control records); class-of-one constructions have
`log φ(Q) + log(1/μ) ≥ Φ − O(1)` (no exponent ceiling claimed from this).

## Self-review (deep reviewer, round 1)
Core proofs (Thm 1.4 single-value version, Lemmas 2.2–2.4, Thm 2.1): no
fatal flaw. Repairs applied: literal vs compatible overlap distinguished
(Lemma 1.2, Prop 1.5); prime-power remark withdrawn (single-value events
only); BRW ceiling claim withdrawn; RA "record" wording fixed; MC bias
direction and "consistency only" wording; Haar on `Ẑ^×`, `3∤M`; summation
cutoffs; OMEGA12 status.

## Not done / next
Upper bound below `𝓛^5` (Haar side). Diagnosis so far: class-of-one
quarantine inflates the residual mass from `S_tot ≍ 𝓛³` (elementary) to
`S♯ ≈ 𝓛^4` (factor ≈ τ(M)); a quarantine with non-unit classes whose residual
mass stays `≈ S_tot` would give `≈ 𝓛^4` via the OMEGA11 cost formula. The
obstruction is controlling atomic-event inflation under the small-prime
avoider measure. 

## Hostile review R46 (`reviews/pointwise-haar-review.md`)
Thm 1.4 and Thm 2.1 SOUND (re-derived, brute-forced exactly, scaled family
check). Minors applied: D1 (Prop 1.5 scope, S1 upper bound sketched), D2
("explaining" → "consistent with", Conj. 3.1 as `a = 3`), D3 (T_0 ≳ e^{90}
stated), D4 (constant 16→8; why `y ≥ 𝓛^{4+ε}`; harmonised what OMEGA8's 𝓛²
depends on); upper-bound reference updated to OMEGA12's `𝓛^5 log𝓛`.

## Open
Haar upper bound below `𝓛^5 log𝓛`; diagnosis in "Not done / next" above.
