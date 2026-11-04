# Z55_SUMMARY — wave z55 on the three best open gaps after z54

**ES is OPEN.** Every result here is internal. Wave z55 ran three structured lanes (P415, TDCAL, CROSSU; brief
`z52bbriefs/z55_lanes.md`) and six "tryhard" lanes, two per concrete open statement (TDO, TDF on problem TD; CROSSO,
CROSSF on problem CROSS; HCO, HCF on problem HC; brief `z52bbriefs/z55_tryhard.md`). Each memo had internal hostile
review(s) and a cross-model review; all nine were ACCEPT-WITH-FIXES and were merged after the fixes. Reviews:
`data/z55/xreview/REVIEW_<LANE>.md`. This summary carries scopes only loosely; each memo's own statement governs.

## 0. Bottom line

**No tryhard lane proved its target.** TD(η) (TDO, TDF), "R_𝔉(p) ≥ 1 for every large prime p ≡ 1 (4)" (CROSSO, CROSSF)
and "HC(p) ≤ (log p)^A for every large prime p ≡ 1 (4)" (HCO, HCF) all remain open. None of the three gaps closed.
What the wave did produce:

* **A certified recalibration of problem CROSS (CROSSF).** In the standard window, R_𝔉(p) = 0 at a large fraction of
  primes: 39 % near 10⁸, 9.4 % near 10¹², 5.4 % in a 10¹³ sample (CERTIFIED counts). At those primes positivity fails
  for this standard-window family. Failure of (H⁻_𝔉) of `Z53_GENUSX.md` additionally requires M_𝔉 > 0, certified at the
  192 469 recorded exhaustive-scan zeros. Under the stated Poisson model, the expected tail count crosses 1 near 10¹²⁴;
  this is not a certified last exception.
* **Averaged and positive-proportion versions.**
  * CROSSO Theorem P (PROVED): for fixed 0 < α₀ < α₁ < β < γ with α₁ + γ < 1/2, a positive proportion of primes
    p ≡ 1 (4) have R_𝔉(p) ≥ 2. Theorem A gives R_𝔉(p) ≫ log²p for almost all such primes on the same exponent windows,
    CONDITIONAL on HV (a prime-free variance bound).
  * TDO Theorem A (PROVED): almost all primes, simultaneously over admissible U, for 0 < η < 1/8. TDF Corollary 2.4
    (PROVED): for each fixed U, almost all primes in its fourth-root range, for 0 < η < 1/7; not simultaneous in U.
  * TDCAL Prop A (PROVED): R2's conclusion holds on average over n.
  * B6 applies to all of these: none says anything about a prescribed prime.
* **Kill side (P415 Theorem U, PROVED relative to standard sieve inputs).** Unconditionally, ≫ x/(log x)² primes p ≡ 1 (8)
  have p + 4 ∈ S exactly and Ω_𝒬(4p + 1) bounded by an absolute constant. This is one exact half of P(4,15), with a
  bounded deficit in the other half.
* **Upper side.**
  * HCO census (CERTIFIED): HC(p) ≤ 64 for primes p ≡ 1 (4) below 10¹².
  * HCF Theorem 3.1 / Cor 3.2 (PROVED): fixed finite certificate coverings fail even on classes that contain no squares.

## 1. Gap 1 — TD and the balanced block (TDCAL; tryhard TDO, TDF)

Setting of `Z54_BILINDIV.md`: p an odd prime, U in the fourth-root range c₁p^{1/4} ≤ U ≤ c₂p^{1/4}, 16U³ ≤ p. TD(η) is
|T(h)| ≤ C₀U^{1−η} for 1 ≤ h ≤ U^η, uniformly in p and U. By BILINDIV Cor T it gives N₂ ≪ U^{1−η+ε}. The gap is
upper-bound only and is silent on positivity.

**Tryhard outcome: TD(η) is not proved for any η > 0.** What was proved averages over n; primality is used nowhere.
* **Mean square (PROVED).**
  * TDO Theorem M: Σ_{N₀<n≤N₀+N}|T_n(h)|² ≤ C(N + 16U⁴)·hU·(1 + log(4U²)) for all U ≥ 5, h ≥ 1, N₀ ≥ 0, N ≥ 1. The input
    is Lemma V: the r-sums are ≪ √(hU) uniformly in the frequency.
  * TDF Theorem LS: Σ_{M<n≤M+N}|T_n(h)|² ≤ (N + 16U⁴)(2700h⁴U + 32U log 2U).
* **Almost all primes (PROVED).**
  * TDO Theorem A: fix 0 < η < 1/8 and 0 < c₁ ≤ c₂. For X ≥ X₀(η, c₁, c₂), all but ≪_{η,c₁,c₂} X^{1−η/4}
    primes p ∈ (X, 2X] satisfy |T_{p,U}(h)| ≤ 2U^{1−η} for *every*
    U in their fourth-root range and every 1 ≤ h ≤ U^η.
  * TDF Cor 2.4: for 0 < η < 1/7 and *each fixed* U, TD(η) with C₀ = 1 holds at all but ≪ U^{3+7η}log U of the primes in
    that U's range. No exceptional set uniform in U is claimed there.
* **Downstream value for the (★) block: none.** The almost-all bound on N₂ already follows from a first moment (TDO
  Remark 4.3, TDF §2.5, TDCAL Prop A). These results are statements about T itself.
* **Pointwise constant factors (PROVED, no power saving).** Both improve the trivial bound N₂ ≤ U/2:
  * TDF Prop 2.6: N₄ ≤ N₂ ≤ (log 2/2)U + O(U^{14/15});
  * TDCAL Remark A‴ (relative to Titchmarsh Thm 5.13): N₂ ≤ (1 − log 2)U + O(U^{1−3/56+ε}) ≈ 0.307U.
* **Weaker sufficient conditions (PROVED implications; both conditions open).**
  * TDF §3.3: TD(η) ⟹ DC_ε(U^{−η}) ⟹ N₂ ≪_ε U^{1−η+ε}. Here DC_ε(t₀) says #{k ∈ E1⁺ : w_k mod 1 ∈ I} ≪_ε U^{1+ε}|I| for
    every interval with |I| ≥ t₀.
  * The ε-free implication TD ⟹ DC is *not* claimed: the zero mode |E1⁺| is known only to be ≪ U^{1+ε}.
  * 2-cycle levels are a *subset* of the square-discriminant levels, not equal to them.
  * TDCAL Prop D: TD(η) ⟹ NC(η) ⟹ N₂ ≪ U^{1−η+ε}. NC(η) says 𝒜(U^{−η}) ≪_ε U^{1−η+ε}, where
    𝒜(δ) = #{k ∈ E1⁺ : ‖w_k‖ ≤ δ}. This one-sided near-integer count is what Theorem T's Fourier route actually delivers.
* **Assessment.**
  * Pointwise TD sits at a self-dual point (TDO §6, TDF §3.1).
  * TDF §3.2 applies a PROVED elementary inequality to a heuristic bound expression. The result: one-variable exponent
    pairs after the θ-expansion would give TD only for n < U³, outside the admissible range. This holds for every
    exponent pair, the conjectural (0, 1/2) included.
  * Joint (ν, k) arguments are not covered.

**TDCAL (structured; narrowed, i.e. calibrated).**
* **Prop A (PROVED).** For integers X ≥ 0, Y ≥ 1, U ≥ 2; the exceptional-set conclusions assume fixed 0 < η < 1 and
  ε > 0. Σ_{X<n≤X+Y}N₂(n, U) ≤ Σ_{X+2U<M≤X+Y+4U}τ(M)².
  * Cor A′: #{p ≤ X : N₂(p, U_p) > U_p^{1−η}} ≪ X^{(3+η)/4+ε}, with U_p = ⌊p^{1/4}⌋.
  * So R2's *conclusion* holds on average with no TD-type input. Whether averaged TD holds is not addressed by Prop A.
* **Lemma S(a) (PROVED central-slice identity).** |E1| is exactly the part of the short-interval divisor sum
  D(p + 2U, 2U) with divisor in (U², 4U²]: a slice at divisors ≍ √x, at length ≍ x^{1/4}.
  * Assessment (search-limited): no checked source gives a power-saving pointwise asymptotic for it. Li–Yang's
    Δ(x) ≪ x^{0.31448…+ε} gives full short-interval asymptotics only for lengths ≥ x^{0.31448…+ε}.
  * Lemma S(c) (PROVED): every strip point has m | p² − D. The contribution to T(h) from w ≤ U^{(1−η)/2} is
    O_ε(U^{1−η+ε}) for every integer h ≥ 1; this is not sharp TD(η) for the full sum.
* **Theorem B (PROVED; band localisation of the natural smooth expansions in θ_m = {−p/m}).**
  * Hypotheses: fix the smooth test functions of TDCAL §6, 0 < σ ≤ 1, 0 < ε < 1 and A > 0; take sufficiently large U
    and integer 1 ≤ h ≤ U.
  * The smoothed count and the N₂-strip analogue TS_{N₂} carry only |ν| ≤ U^{1+ε}.
  * A smoothed TD piece at w ≍ W ∈ [U^σ, 4U] carries only ν ∈ [hU³/(2W), 64hU³/W].
  * Both statements hold up to O(U^{−A}).
  * The bands depend on the expansion (Remark B2). No implication between TD and short-interval divisor statements is
    established in either direction.
* **Prop C (per-frequency benchmark).** PROVED for the smoothed count; the TD top piece follows from BILINDIV Prop 4.3
  (this uses BILINDIV's smoothed level-parametrized weights and 1 ≤ h ≤ U, not the sharp sum T(h)); part (iv) is
  Assessment.
  * The class is "triangle inequality over ν with majorants ≥ c‖c(ν)‖₂". In it, for nonzero nonnegative test
    functions φ, Φ, the nonzero-frequency benchmark is ≍ U, so every bound for the smoothed count minus its main term
    in this class is at least ≫ U.
  * Reaching the targets needs further factors: U^η for CNT(η), U^{1/2} for central-slice square root, and
    h^{1/2}U^{1/2+η} for TD(η) (top piece; same BILINDIV weights and range 1 ≤ h ≤ U, not the sharp sum T(h)).
* **Prop E (PROVED identity).** The direct completion of m | p + s exhibits no Kloosterman sum. No spectral-method
  exclusion is made.
* **EVIDENCE.** At 10¹⁰, T(h)/√|E1⁺| is compatible with a unit complex Gaussian: 96 000 generic (p, h), plus structured
  families and odd squares.

**Status.** TD, TS, MIX, NC and DC_ε are all open; all are sufficient and none is shown necessary. The proved averaged
forms concern T itself but add no almost-all N₂ bound beyond the elementary first moment. The missing piece is a single-p estimate.

## 2. Gap 2 — the exact layer and problem CROSS (CROSSU; tryhard CROSSO, CROSSF)

Problem CROSS: for some window admissible for `Z53_GENUSLVAL.md` Thm U, prove R_𝔉(p) ≥ 1 (or ≥ c·log²p) for every
sufficiently large prime p ≡ 1 (4). Each hit gives an ES solution. **Not proved by either lane.**

**CROSSF: certified failure on the standard window, and the model scale of p₀ (the wave's notable finding).**
* **Exact forms (PROVED; Lemmas 1.1–1.3).**
  * hits(p) = R_𝔉(p)/2 counts the same objects in four forms: u-form, w-form, C-form 4Cp + 1 = (4uC − 1)(8wC − 1), and
    d-form.
  * Every hit has (w″/p) = −1, so hits(m²) = 0 at odd squares.
  * Fixing all variables but one leaves a single-integer divisor-in-progression event.
  * Assessment (non-bankable): the averages found reach only density level or the principal character. Transformed or
    dispersion forms are not excluded.
* **§2.4(a) (PROVED; scoped to pointwise Fourier minorants).** No minorant of a class indicator whose Fourier support
  lies in a proper subgroup of characters (e.g. the genus characters) has positive mean.
* **CERTIFIED zero counts.**
  * Window: the z53 engine's standard window U₀ = round(p^{1/12} − ½), U₁ = ⌊p^{1/3}/2⌋, Y = ⌊p^{1/3}⌋, X = ⌊p^{2/3}/4⌋
    (X decreased until 8U₁X ≤ p). It is the boundary approached by strict Thm U windows.
  * Two independent scanners agree line by line on the 10⁸ range. The cross-review reran that range byte-identically,
    independently recounted 512 sampled primes at 10⁸ and 10¹⁰, and audited the remaining counts from saved data; it
    did not rerun the 10¹⁵ zeros.
  * Exhaustive ranges, primes p ≡ 1 (4) with hits(p) = 0:

    | range | zero primes | fraction |
    |---|---|---|
    | [10⁸, 1.02·10⁸] | 21 233 / 54 198 | 39.2 % |
    | [10⁹, 10⁹ + 10⁷] | 83 874 / 240 944 | 34.8 % |
    | [10¹⁰, 10¹⁰ + 10⁷] | 51 773 / 217 331 | 23.8 % |
    | [10¹¹, 10¹¹ + 10⁷] | 30 069 / 197 020 | 15.3 % |
    | first 58 878 primes above 10¹² | 5 520 / 58 878 | 9.4 % |

  * Samples, each counted prime certified:

    | scale | zero primes | fraction |
    |---|---|---|
    | 10¹³ | 444 / 8 290 | 5.4 % |
    | 10¹⁴ | 79 / 2 238 | 3.5 % |
    | 10¹⁵ | 9 / 535 | 1.7 % |
    | 10¹⁶ | 0 / 108 | 0 % |

  * Largest certified zero: 1 000 005 280 000 049, re-checked by an independent PARI script; the cross-review did not
    rerun the 10¹⁵ zeros.
* **Consequences of the counts (elementary).**
  * At each zero, CROSS fails for this family. Any threshold p₀ for "R_𝔉 ≥ 1 for p ≥ p₀" in this window therefore
    exceeds 1.000005·10¹⁵.
  * (H⁻_𝔉), X_𝔉 ≥ −(1 − ε)M_𝔉, is false at every zero with M_𝔉 > 0. The cross-model review certified M_𝔉 > 0 at all
    192 469 recorded exhaustive-scan zeros.
  * Eventual positivity with unspecified p₀ is *not* refuted.
* **EVIDENCE.**
  * The five exhaustive scans have approximately Poisson-shaped hit counts with resolved overdispersion,
    var/mean ≈ 1.03–1.07. The smaller samples at 10¹³–10¹⁶ have ratios ≈ 1.06, 1.02, 1.08, 0.83.
  * Across the nine datasets mean/log²p ranges approximately from 0.00249 to 0.00335, non-monotonically. The model
    constant 1/(3π⁴) ≈ 0.003422 is half of Thm U's *lower-bound* coefficient, not a proved mean.
* **Assessment (model only).** Model: hits ~ Poisson(c log²p) with c = 1/(3π⁴).
  * It predicts ≈ 5.6·10³⁰ zero primes in total, concentrated near p ≈ 10⁶³.
  * The expected tail count crosses 1 near p ≈ 10¹²⁴. This is an expected-count crossover for the standard-window model
    with its assumed c, not a certified last exception; no theorem forces a proof's p₀.
  * With c = 0.003 the crossover is ≈ 10¹⁴²; with the GRH coefficient it is ≈ 10^{39.9}.
  * For R_𝔉 ≥ a·c·log²p: log p₀ ≈ 1/(c·I(a/2)).
  * Recommendation: the family's constant is too thin. Enlarge the main term (≳ 0.1·log²p) or find another positivity
    mechanism before "all large p" has checkable content.

**CROSSO: averaged versions (strengthened on average; pointwise target not reached).**
* **Lemma 1.1 / Cor 1.2 (PROVED).** Both factors of 4Cp + 1 = de are non-residues mod p, and R(m²) = 0 for odd squares.
* **Theorem P (PROVED, unconditional; relative to BV, Brun–Titchmarsh and Mertens).**
  * Hypotheses: exponents 0 < α₀ < α₁ < β < γ with θ := α₁ + γ < 1/2.
  * Conclusion: a proportion ≥ 2μ(1 − 2θ)/(2(1 − 2θ) + 32μ) − o(1) of the primes p ≡ 1 (4) in every dyadic (x/2, x],
    x ≥ x₀, have R_𝔉(p) ≥ 2. Here μ = ¼·log(α₁/α₀)·log(γ/β).
  * Example: the Thm-U-admissible window (0.075, 0.1, 0.29, 0.39) gives μ ≈ 0.02131 and proportion ≈ 0.00118.
  * This is a different window from CROSSF's, and it gives a positive proportion, not all primes.
* **Theorem A (CONDITIONAL on HV).**
  * HV: V₈(x) = o(log³x), where V₈ is an explicit prime-free pair sum, the Haar variance of the family.
  * Conclusion: for the same fixed exponent windows and every 0 < ε < 1, all but o(x/log x) primes p ≡ 1 (4) in
    (x/2, x] satisfy R_𝔉(p) ≥ (1 − ε)M̃_x(p) ≫ log²p. Dyadic summation gives R_𝔉(p) ≫ log²p for all but o(π(x))
    primes p ≡ 1 (4), p ≤ x.
  * The reduction is PROVED (Lemma 4.1, dual large sieve; Lemma 4.2, M̃ ≥ c₀log²x).
  * EVIDENCE: finite prime samples in four fixed non-exponent windows are consistent with Poisson-scale variance, with
    sampling uncertainty (including a ratio 2.334 at 400 samples). They do not sample Haar units; HV remains untested
    asymptotically.
* **Theorem A′ (CONDITIONAL on HW).**
  * HW: W_z = o(log³x/(log log x)⁴) at z = (log x)². It is a sum of nonnegative terms, so only an upper bound is needed.
  * Conclusion: almost all p ≡ 1 (4) have R_𝔉(p) ≫ log²p/(log log p)².
  * The case analysis for HW is only sketched; its four-cycle multiplier was corrected by the review.

**CROSSU (structured; inconclusive on the target, narrowed only by reformulations).**
* **Target and conditional route.** Target (CU) (CONJECTURE, not proved): R_𝔉(p) − G_𝔉(p) = o(log²p) as p → ∞
  through primes p ≡ 1 (24), on a window with M_𝔉 ≫ log²p. CONDITIONAL: (CU), Z53_GENUSLVAL Theorem U and (X-w), on
  one common admissible window, give (★) for all sufficiently large primes in that progression.
* **Standing hypotheses** for these reformulations: U₀ ≥ 1, Y ≥ U₁, 8U₁X ≤ p, and the stated family restrictions.
  Here 𝔖₃ is the shell restricted to d ≡ 3 (4).
* **Lemma A (PROVED; class index).**
  * Definition: j := (u·(u⁻¹ mod d) − 1)/d ∈ [1, u), so j ≡ −d⁻¹ (mod u).
  * On 𝔖₃, an exact hit is equivalent to j = 1, and genus membership is equivalent to j ∈ □_u. At primes, j = ⌊u·(d⁻¹ mod p)/p⌋.
* **Lemmas B, C (PROVED).**
  * Lemma B: on 𝔖₃, exact hits are precisely the shell points whose ceiling Euclidean expansion of (p, d) has length 3.
  * Lemma C: for c > 0, N_c is twice the number of representations 1/(cp) = 1/(2wtu) + 1/(2wtp) + 1/(ctup), with
    positive integral t and (u, w) ∈ 𝔖₃; summands with gcd(c, u) > 1 are zero. Fibrewise,
    G|_u = q_u⁻¹ Σ_{c∈□_u} N_c|_u, where q_u = |□_u|. This is not an average over one fixed global set of c.
* **§4.1 (PROVED, scoped).**
  * For squarefree odd u, q_u = |□_u| ≥ (2/√15)√u.
  * Consequence: on moving windows (U₀ → ∞) and for each fixed K, a hit cannot be cancelled exactly by K genus non-hits
    for large p.
  * Large groups, approximate cancellation and positivity maps are not excluded.
* **§4.2, §4.3, §4.10 (PROVED).** On the switchable domain where d is odd squarefree in (Y, X] and gcd(d, up) = 1,
  swapping w and d gives j′ ≡ 2p⁻¹j⁻¹ (mod u); for a switch within 𝔖₃, both d and w must be 3 (mod 4). There is no one-coordinate Vieta involution
  on xyz = x + y + p. On 𝔖₃, (d/p) = −(j/u).
* **EVIDENCE.** At 10⁹–10¹⁴ (1 000 primes plus controls), the hit class is not distinguished among 18 index classes.
  These tests cannot support or falsify (CU).

**Status.** The standard-window family's exact count has certified zeros, so any eventual-positivity threshold for that
family exceeds every certified zero. The model's expected-tail-count crossover is near 10¹²⁴ (Assessment), not a
necessary proof threshold. Theorem P is unconditional; Theorems A/A′ remain conditional on HV/HW. Cross-u cancellation
(B2 in tied form, Assessment) remains unresolved.

## 3. Gap 3 — HC: the kill side P(4,15) (P415) and the upper side (tryhard HCO, HCF)

**Kill side: P415 (narrowed, with one unconditional strengthening, not P(4,15)).** Notation: S = {n : all prime factors
≡ 1 (4)}; 𝒬 = the primes ≡ 3 (4); Ω_𝒬 counts 𝒬-factors with multiplicity.
* **Theorem U (PROVED).** Name clash: this is `Z55_P415.md` Theorem U, not GENUSLVAL's.
  * Inputs: BV; Nath–Xie's vector-sieve Prop 3.10 (with FI *Opera de Cribro* Thm 11.12 as quoted there); a κ-dimensional
    upper-bound sieve; Shiu.
  * Statement: there are absolute, unspecified δ ∈ (0, 1/100] and c > 0 with
    #{p ≤ x : p ≡ 1 (8), p + 4 ∈ S, (4p + 1, 𝒬(x^δ)) = 1} ≥ c·x/(log x)².
  * Hence Ω_𝒬(4p + 1) < 1/δ + 1 (and even), a bound by an absolute constant. The same holds with the shifts exchanged.
  * Unaudited Assessment: the unweighted model suggests δ ≈ 0.031; a separate Richert-weighted model, using
    δ = 0.008, suggests Ω_𝒬(4p + 1) ≤ 10. Neither is proved.
  * Remaining deficit to K(4) = P(4,15): bring Ω_𝒬(4p + 1) from "bounded" down to 0.
* **Level ledger (Assessment; model numerics, sufficient levels found, not barriers, not audited).**
  * The product linear sieve with switching needs ≈ 0.996 under ordinary EH with BV switching. It needs ≈ 0.976 only
    with an additional GEH-type switched input.
  * The vector sieve with switching needs ≈ 1.22, which is above 1 and unusable.
  * Known levels are far short: BV 1/2; Lichtman 66/107, for fixed residues and well-factorable weights only.
* **Lemmas A1, A2 (PROVED).** Full-family confinement constructions are excluded for the listed prime-value theorems:
  a² + b⁴, a² + p⁴, x² + y² with y prime, x³ + 2y³, binary cubics, power-basis incomplete norm forms, and nondegenerate
  quadratics.
  * Lemma A1 requires a fully free square variable.
  * Lemma A2 requires F + 4 (respectively 4F + 1) to be nonconstant and absolutely irreducible, on a full-rank lattice
    coset in k ≥ 2 variables.
  * Not covered: rank-one quadratics (Theorem Q), thin restrictions, and other uses of those theorems.
* **Prop C (PROVED by citation of Lemke Oliver 2012, Thm 1).** There are infinitely many P₂ values n = 720k² + 1 with
  n + 4 ∈ S and 4n + 1 ∈ S. This has no ES content.
* **CERTIFIED (cross-model rerun exact).** Among the 22 280 854 primes p ≡ 1 (8), p ≤ 10¹⁰, with p + 4 ∈ S:

  | Ω_𝒬(4p + 1) | 0 | 2 | 4 | 6 | 8 | 10 |
  |---|---|---|---|---|---|---|
  | primes | 7 962 940 | 12 902 238 | 1 378 173 | 37 005 | 496 | 2 |

**Upper side (HCO, HCF): HC(p) ≤ (log p)^A is not proved.** The target is ES-sufficient for large primes; no converse is
established.
* **HCO census C3.1 (CERTIFIED).**
  * HC(p) ≤ 64 for every prime p ≡ 1 (4), p < 10¹² (18 803 924 340 primes). Before z55 this was certified to 10⁹ (UPPER2).
  * The value 64 occurs only at p = 21 841. The maximum on [10⁸, 10¹²) is 60, at p = 818 789 590 249.
  * Audit: a fresh rerun below 10⁸ agrees, π(10¹²) checks, and all 126 records with HC ≥ 44 were independently verified,
    certificate and minimality. The full 10¹² run was not repeated by the cross-review.
  * HCF independently reran the z53 program to 2·10⁹.
* **HCO, other results.**
  * Lemma 2.1 (PROVED): if (k/p) = −1, then p + 4k has an odd number of prime factors ℓ with (ℓ/p) = −1 (with
    multiplicity).
  * Prop 2.2 (PROVED): each certificate lies in a fixed-divisor or fixed-cofactor congruence family, with μ = min(d, ce)
    on U and μ = min(d, e) on T, e = N/d. For odd c, also impose p′ ≡ −c (mod 8); the full condition is then a class
    modulo lcm(μ, 8), not μ alone.
  * Cor 2.3 (PROVED given Linnik): infinitely many p have no certificate with μ ≤ log p/(1.02L₀) − O(1). This is a
    logarithmic obstruction only.
  * E4.1 (EVIDENCE): at c = HC(p), the 126 hardest primes have μ ∈ [p^{0.138}, p^{0.636}]. Over the window c, μ ≤ ⌊log²p⌋,
    however, 101/126 have a small-modulus certificate (cross-model review). It is open whether a polylog-modulus
    covering or control of mid-size divisors is what a proof needs.
  * E4.3 (EVIDENCE): among primes p ≡ 1 (8), P(HC > 4) is 0.087 on [0, 10⁸) and 0.056 on [9.52·10¹¹, 10¹²). The
    cumulative maximum stays 64; the maximum above 10⁸ is 60, and the final window's maximum is 47.
* **HCF Theorem 3.1 (PROVED; elementary plus Dirichlet).**
  * Inputs: a nonempty finite set S of primes ≥ 11, an integer 1 ≤ R < (min S − 1)/3, and arbitrary C ≥ 3, Y ≥ 2.
  * Conclusion: infinitely many primes p ≡ 1 (8) in an explicit CRT class have no certificate (c, d) with c ≤ C and d
    supported on S ∪ {primes ≤ Y}.
  * Cor 3.2: no finite family of certificate congruences covers {p ≡ 1 (840), p ≡ R (ℓ)}, for prime ℓ ≥ 11 and a
    non-residue R < (ℓ − 1)/3. Such a class **contains no squares**.
  * Cor 3.3 is the profinite form.
  * Prop 3.4 (Linnik): for every A ≥ 0, infinitely many p are non-residues mod every prime ℓ ≡ ±3 (8) in [11, κ′_A log p], and
    every certificate of such p with c ≤ κ_A(log p)^A has a prime factor > κ′_A log p.
  * Consequence: "HC(p) ≤ F(ℓ_p)" cannot be proved by a finite certificate family for each value of the least
    non-residue prime ℓ_p; ℓ_p = 11, p ≡ 2 (11) is already uncoverable. So the GRH route cannot be completed by fixed
    coverings.
  * Not excluded: growing moduli and unbounded certificate families. HC ≤ F(ℓ_p) itself is not refuted.
* **HCF, other results.**
  * L2.1 (PROVED): for prime p ≡ 1 (8), p > 15, and c ∈ {7, 15}, c is a word coordinate iff the odd part of p + c or
    cp + 1 has a prime factor q with (q/c) = −1.
  * P1.2 (PROVED): for c ∈ 𝒞_p, 3 ≤ c < p, and N = sq with q prime and q ∤ s: on U, success is equivalent to a divisor
    of s being −1 or −p modulo c; on T, it is equivalent to a divisor of s being −1 modulo c.
  * The large-CRT samples are EVIDENCE,
  since their primality is only probable (BPSW).

**Status.** On the kill side the gap is now explicit: one shift is exact and the other has a bounded number of 𝒬-factors,
which must go to zero. That needs EH-strength level in CRT-varying classes or Type II input for the det-15 shell
(suggested routes, not a necessity theorem). On the upper side the census moved to 10¹². Fixed coverings are excluded
even off the square classes. A pointwise mechanism is still missing.

## 4. Honest assessment

Wave z55 aimed six lanes directly at three ES-relevant statements; none fell. The durable outputs are:
* the CERTIFIED standard-window zero counts; they refute (H⁻_𝔉) wherever M_𝔉 > 0, including all 192 469 recorded
  exhaustive-scan zeros. The 10¹²⁴ figure is only the stated model's expected-tail-count crossover;
* averaged and positive-proportion theorems: CROSSO Thm P (unconditional), CROSSO Thms A and A′ (conditional on HV, HW),
  TDO Thms M and A, TDF Thm LS, TDCAL Prop A. All are B6 statements;
* an unconditional half of P(4,15) with bounded deficit (P415 Theorem U);
* calibration and weaker sufficient conditions on gap 1: the central-slice identity, band localisation, NC and DC_ε;
* on HC: the 10¹² census and the non-square-class covering obstruction (HCF T3.1/C3.2).

No unconditional positivity theorem at a prescribed prime, or for all sufficiently large primes, is obtained.
