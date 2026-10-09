# Hostile review A of EXCEPTIONAL_TYPEI_LOGLOG3.md (task R121A)

Reviewer: side agent R121A (independent of reviewer B). Branch reviewed: `side-agent/eff-di7` (merged into
`side-agent/review-ttl3-a`). Work in progress; sections filled one at a time.

## Verdicts (summary)
(to be filled)

## §2 (induction (8.19), Prop 2.1, Thm 2.2, Cor 2.3) — verdict: SOUND (relative to (P1)–(P3))

Re-derived line by line; from-scratch sweep `scripts/review_r121a_induction.py` (log-space, 2·10⁵ random
`(δ, c, K₁, K₂, Q, N)` per case, δ down to 10⁻³, constants up to e³⁰) finds no violation of cases (A), (B), (C) of
Prop 2.1 or of Cor 2.3 (max of `log log H − (B+3)/δ` over the grid is −27.6).
* (P2) is a faithful transcription of DI (8.5) (scan p. 271: `S(Q,Y,N,0) ≤ c(ε)∫S(πNYQ⁻¹,Y,N,it)dt/(t⁴+1) +
  c(ε)(YN)^ε(Q+N+NYQ⁻¹)‖a‖²`, S as in (8.4) with `Q<q≤16Q`), with ‖a‖² ≤ 2N for closed intervals absorbed.
* (M) needs only `0 < 2σ_j ≤ 1/2` (Selberg 3/16) ✓. (PS): Abel summation and Cauchy–Schwarz in `dξ/ξ` over
  `[N,N₁] ⊂ [N,2N]` give `|·|² ≤ 2|A(N₁)|² + 2t²(log 2)∫|A|²dξ/ξ`; after weighting/summing,
  `≤ 2S* + 2t²(log 2)²S*` ✓. The intervals `[N,ξ]` are admissible (closed, `ξ ≤ 2N`) ✓.
* Case (C): `Q₁ = πQ^{1−2δ}` satisfies `N ≤ Q₁ ≤ Q/2` exactly when `Q^{2δ} ≥ 2π` and `N ≤ Q^{1−2δ}` ✓; the main term
  is in fact `2√2π·π^{5δ}·cH·Q^{1+4δ−10δ²}N` (the text's `π^{1+4δ}` overestimates harmlessly), the error term
  `≤ 3cQ^{1+2δ}N` ✓, and `H/2 + 3c ≤ H` because `H ≥ 6c` ✓. **No accumulation**: the same H is reproduced at every
  dyadic step, so the number of induction steps (≍ log Q) does not enter the constant. This is the crux of the
  double-exponential claim and it is correct: `log Q₀ ≍ δ^{−2}log c(δ)`, `log H ≤ log(2K₂) + log Q₀`, so
  `log log K₇ ≤ max(log log K_i) + 2 log(1/δ) + O(1)` ✓ (Cor 2.3).
* Thm 2.2: both branches re-derived ✓ (`Y₂ = Q^{2−2δ}/N ≥ Q^{1−2δ} ≥ 1`).
* Non-circularity: (P1), (P3) are non-inductive; (P2) is applied only with `Q₁ ≤ Q/2` and `N ≤ Q₁` ✓.
Cross-check with DI's own proof (scan pp. 276–278): DI inducts with `Q₁ ≤ Q − 1`; the dyadic variant is
equivalent. DI's step "extend q from [Q,2Q] to [Q,16Q] by applying the estimate at (2^lQ, 2^lY)" (p. 273) is
the place where C is held fixed; that is inside (P2) (§4), not here.

Minor (§2): m1 below.

## §1 (toolkit) — verdict: SOUND
From scratch (`scripts/review_r121a_toolkit.py`): Lemma 1.3(a) `max_p≤15 sup|h^{(p)}|/(9^p p!²) = 0.905`; `I = 4.85·10⁻⁵ ≥
e^{−16}/4`; `|ρ^{(p)}|` (p ≤ 8) at most `2·10⁻⁷` of the stated bound. Lemma 1.1 brute force (`τ^B`, B ∈ {1,2},
δ ∈ [1/4,1], n ≤ 2·10⁵): ratio ≤ 0.25. Proofs re-read: Cauchy-circle argument, Leibniz sum
`Σ C(p,k)k!²(p−k)!² ≤ (p+1)p!²`, convolution formula for η^{(p)} — all correct. Lemma 1.2 ✓.

## §4 / `ttl3_lemma81_effective.md` (P1), (P2) — verdict: SOUND (modulo un-re-derived absolute numerals; see m2)
Checked against DI pp. 271–273, 276–277 (scan).
* Support repair (§3.2) re-computed exactly: with `q ∈ [3Q/4,9Q/4]`, `xY ∈ [11/12,17/12]`, `√mn ∈ [N,2N]` one gets
  `c/C ∈ [64/51, 128/11]` ⊂ (1,16]; DI's pictured supports give `[16/25, 32]` — the author's observation of a
  (harmless) gap in DI's printed bookkeeping is correct. k-range in (P1): `k/(NY) ∈ [8.87, 27.42]` ⊂ (8,32) ✓.
* Positivity (c): independent mpmath evaluation of the exact kernel `π/(2 sin πσ)(J_{−2σ}−J_{2σ})` (with the
  sign that makes it positive, i.e. DI (8.1), not printed (1.22)) for `Y ∈ {2³²,2⁴⁰}`, `σ ∈ [10⁻⁶,1/4]`:
  kernel positive on the whole support, and `φ̂(−iσ)/cos πσ ≥ 0.67·Y^{2σ}` using only the plateau — far above
  1/64 ✓. The σ → 0 uniformity argument (MVT on the order *difference* before dividing by `sin πσ`) is right; the
  limit is a `log(2/x)` kernel, which is why (d) carries `L_Y` ✓.
* Mellin separation, the `m^{−it/2}n^{−it/2}` twists, the Cauchy–Schwarz `|A(t/2)||A(−t/2)| ≤ (|A(t/2)|²+|A(−t/2)|²)/2`,
  substitution `t = ±2u` ✓; the second trace formula's spectral side carries **no** `1/c` weight, so the regular
  error is `Σ_{c∈(C,16C]}K_{T2}(1+N^{1+e}/c)‖a‖² ≤ K_{T2}(16C+4N^{1+e})2N` ✓ (matches DI (8.10)).
* Exceptional split at σ = e: the `1/sin πσ ≤ 1/(2e)` loss for σ > e and `Y^{2e}L_Y` for σ ≤ e are polynomial
  in 1/δ — consistent with `c(δ) = Aδ^{−2}[1+K_{T2}(δ/4)]` ✓. Four blocks `(2^lQ,2^lY)` keep C fixed ✓ (DI p. 273).
* Small-Y branch (`Y < 2³²`) and `C < 1` branch: re-derived; with `Q > πNY` one has `Y^{1/2}N^{1+e} ≤ QN^e` ✓.
* (P1) partial summation with a k-independent majorant measure and prefix rectangles, then Thm 14 in the
  U-form for each prefix — correct and indeed necessary (sup over prefixes inside the k-sum would not follow).
  Two-variable Abel summation on `[N,N₁]²` needs `|∂_m w|, |∂_n w| ≤ H/N`, `|∂_m∂_n w| ≤ H/N²` ✓ (u ∈ [11/12,17/12]).
* Transform bound (a): heuristically re-derived (normalised kernel `≍ r^{−1/2}` via `|Γ(1+2ir)|² = 2πr/sinh 2πr`;
  Bessel ODE `(D_x²+x²)J_{2ir} = −4r²J_{2ir}` ✓), constants plausible, B = 2^{2048} generous. The claim
  "H = 2^{512} bounds D_x^j-norms, j ≤ 12" re-estimated: ≈ 2^{212} ✓.
No growing-order step occurs in §4; the only δ-dependence is `δ^{−2}`, `K_{T2}(δ/4)`, `D(δ/4)`, `K₁₄(δ/4)` ✓.
