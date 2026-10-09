# AGENT REPORT O116 — making (D)32 unconditional (the exceptional-eigenvalue strip)

Branch `side-agent/ttl-unconditional`. Main file: `EXCEPTIONAL_TYPEI_LOGLOG2.md`.

## Results
1. **Thm 4.1(i) — PROVED (no SEL).** It is relative to TTL's cited inputs, DI 1982 Thm 7 and Drappeau 2017 Lemma 4.10.
   For every `ε₀ > 0`: `Σ_{p≤N} f_I(p) ≤ Cε₀ N log²N log log N + O_{ε₀}(N log²N)`. Hence
   `Σ_{p≤N} f_I(p) = o(N log²N log log N)`. The improvement is unconditional but unquantified.
2. **Thm 4.1(ii) — CONDITIONAL on (EFF).** `Σ_{p≤N} f_I(p) ≪ N log²N`. (EFF) asks that the `≪_ε` constant of DI Thm 7
   and of Drappeau Lemma 4.10 be `≤ exp(exp(A/ε))`.
   * The deep audit (§5, `scripts/ttl2_di7_effectivity_audit.md`) finds that the proofs give (EFF): divisor bounds, logs,
     an induction with threshold `Q₀(ε)`, and an order-`1/ε` integration by parts that is effective once DI's unspecified
     cutoff is chosen Gevrey-2. No Siegel-type input occurs.
   * Label: Assessment. (EFF) is not written as a proof.
3. **Thm 4.1(iii).** Any explicit `C_ε ≤ G(1/ε)` gives an explicit bound `N L²(1 + w_N log L)`.

## Key idea
The exceptional term of TTL Prop 5.1 has coefficients `λφ̂(λn)(π|n|Y)^{−s}`. These are a smooth function of n, so
partial summation (Lemma 1.2) reduces them to `a_n = 1`. The level is `M = 4dq²`, and TTL's assembly already averages
over d (Remark D11). That is exactly the setting of **DI Thm 7**, the level-averaged exceptional large sieve for
`a_n = 1` with bracket `Q + N + X√N`. Drappeau Lemma 4.10 is the version with nebentypus χ mod q.
* With the n-dependent weight `(nY)^{−2σ_j}`, the exceptional variance is the regular size up to `C_ε N^{O(ε)}`
  (Prop 2.2, Thm 3.1, Cor 3.2).
* The cost of the residual strip `δ < w` is `≪ w N L² log L`. This is fine for `w ≍ 1/log L`, which is what (EFF) gives.
* TTL checked DI Thm 5/6 and Humphries (that negative claim is correct as stated) but not Thm 7.

## Corrections / caveats
* **My first draft misread DI (1.41).** I wrote `√(NX)`. The correct bracket is `X√N`, i.e. `√(NY)` with weight
  `Y^{2σ}`, as in DI (8.17) and Drappeau 4.10.
  * With the correct reading, the crude weight `Y^{−2σ}` fails in TTL (b3). The n-dependent weight fixes it.
  * The grid check `scripts/ttl2_exponents.py` gives 0 violations; the crude weight gives excess +0.06 in (b3).
* DI misprint below (8.18): `Y₁ = √(Q+N)` should be `Y₁ = Q+N`.
* **Not re-derived:** the internals of DI Thm 7 and Drappeau Lemma 4.10 (cited), and Drappeau's twisted trace formulae.
* **Statements eyeballed by me:** DI pp. 232–233 and 273–278, and Drappeau p. 16 together with his normalisation (4.7).
* **Uniformity:** Drappeau's constant is assumed uniform in the character modulus q₀. That is how he states it (`≪_ε`).
* Theorem 4.1 inherits everything TTL Thm 8.1 relies on, except (SEL).

## Questions for the parent
* Is (EFF) worth a dedicated follow-up? That would be a written effective-constant pass through DI §§5, 7.1, 8 and
  Drappeau §4.2.3, which would make 4.1(ii) PROVED.
* Should we look for a published version of DI Thm 7 with an explicit loss?

## Self-review round (review tool, deep; "R116")
No FATAL. Three MAJOR bookkeeping errors in §3–§4, all repaired:
1. **The sieve exponent.** `Q³` with `Q = N^{δ/16}` was miscounted. The sieve level is now `Q = N^{δ/64}` (`κ = 1/16`).
2. **The false range `δ ≤ 0.35`.** It came from the D ≥ A side. The repair has two parts:
   * Cor 3.2 now holds for every δ > 0. Since `F' ≤ 3A√D` in all three cases, the terms T2 and T3 are `≪ (D/A)^{1/4}`.
   * Bad layers are now `δ < w ≤ 1/4`, where TTL (b4) is valid.
3. **The ε of the regular-spectrum large sieve.** It is now a fixed `ε₁ = 1/100`, so its constant is absolute.

Minor repairs:
* Thm 3.1 cusp-term typo.
* The condition `M₀/(λ₋Y₀) ≤ N³` is now stated explicitly.
* `(q,2d) = 1` instead of the wrong coprimality condition.
* Logarithms are integrated rather than absorbed pointwise, uniformly in ε.
* The Mellin weight now has a common majorant.
* Lemma 1.2 now assumes Schwartz decay.
* The note on DI (1.41) is corrected; the misprint claim there was a misreading of mine.
* The nebentypus part of (EFF) is toned down to "very plausible".

The reviewer confirmed:
* the corrected normalisation, interval coefficients and positivity restriction to levels `4dq²` (checked against DI pp. 233, 276–278 and Drappeau p. 16);
* the core of Prop 2.2 (weight `w(t)^{2σ}`, Cauchy–Schwarz with `Φdt`, the moments);
* that SEL is not needed for the regular spectrum;
* the case exponents of Cor 3.2, including `δ ≥ 2γ` in (b2).
