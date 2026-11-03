# Z55_TDCAL — depth lane TDCAL (wave z55, gap 1): how hard is TD?

ES is OPEN. Nothing here proves or disproves it. This lane is **upper-bound calibration work only** (FRONTIER §7.1,
balanced block / 2-cycles); even full success would say nothing about positivity. Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment, one per claim. Results are internal.

Brief: `z52bbriefs/z53_depth.md` (rules), kickoff `z52bbriefs/z55_lanes.md` §TDCAL. Predecessors: `Z54_BILINDIV.md`
(Thm T, TD(η), Prop 4.3, Remark 4.1), `Z54_BILINJAC.md` (Thm R, TS, Prop R′, §5 Jutila comparison), `Z53_HYP2CYCLE.md`
(MIX), `Z53_SQSIEVE.md`. Scripts `scripts/z55_tdcal_*`, data `data/z55/tdcal/` (≈ 0.4 MB). Literature:
`data/z55/tdcal/LIT_CHECK.md`. Checkpoint 1: commit 06ccc2ba. Hostile review: `reviews/z55_tdcal_review1.md` (applied,
§17).

## 0. Summary and verdict

**Verdict: narrowed (calibrated), with one weaker sufficient condition.** No power saving for the balanced block is
proved, and none of TD, TS, MIX is proved or refuted. What is new:

1. **R2 holds on average over n (Prop A, PROVED).**
   * For every window of Y consecutive integers, Σ_n N₂(n, U) ≤ Σ_M τ(M)² over an M-window of length Y + 2U. So the
     *conclusion* of R2 holds on average over any p^{η/4+ε} consecutive integers n.
   * R2 fails for at most O(X^{(3+η)/4+ε}) primes p ≤ X (Cor A′).
   * An averaged conclusion therefore needs no TD-type input. This says nothing about whether averaged forms of TD
     itself hold, which is not addressed.
   * Pointwise, the first-order law of θ_u gives only N₂ ≤ (1 − log 2 + o(1))U ≈ 0.307U (Remark A‴).
2. **Central-slice identity (Lemma S(a), PROVED).** The untwisted strip count |E1| is *exactly* the part of the
   short-interval divisor sum D(p + 2U, 2U) with divisor in (U², 4U²]. That is a central slice (divisors ≍ √x) of the
   short-interval divisor problem at length ≍ x^{1/4}.
   * No checked source gives a power-saving pointwise asymptotic for it (Assessment, search-limited).
   * The checked global bound Δ(x) ≪ x^{0.31448…+ε} (Li–Yang) yields full-interval asymptotics only for lengths
     ≥ x^{0.31448…+ε}.
3. **Band localization of the natural smooth expansions (Theorem B, PROVED).** Expand smoothed pieces in the remainder
   phases θ_m = {−p/m}, m ≍ U², with all s-dependence put into the θ-function. Then:
   * the smoothed count, and the N₂-strip analogue TS_{N₂} of BILINJAC's twisted sums, carry only frequencies
     |ν| ≤ U^{1+ε};
   * the smoothed TD piece at w ≍ W (U^σ ≤ W ≤ 4U) carries only ν ∈ [hU³/(2W), 64hU³/W] ⊂ [hU²/8, ∞).
   These *particular expansions* have disjoint carrier bands. No implication between the statements is established
   either way. The band depends on the expansion chosen: an oscillatory m-coefficient can move TD into the low band
   (§6, Remark B2).
4. **Calibration arithmetic (Prop C).** Benchmark: the ℓ²-norm of the coefficients at each frequency. It is attained by
   per-frequency square root, and it is the bound class of BILINDIV Prop 4.3.
   * For the smoothed count the benchmark total is ≍ U, the trivial order (PROVED).
   * In the class "triangle inequality over ν with majorants β_ν ≥ c‖c(ν)‖₂", reaching U^{1−η} is impossible: the count
     falls short by U^η, central-slice square root by U^{1/2}, and the TD top piece by h^{1/2}U^{1/2+η} (the last from
     BILINDIV Prop 4.3).
5. **NC: what Theorem T's Fourier route actually delivers (Prop D, PROVED).**
   * With 𝒜(δ) := #{k ∈ E1⁺ : ‖w_k‖ ≤ δ}: 𝒜(δ) ≤ Σ_kχ_δ(w_k) ≤ 𝒜(2δ), and N₂ ≤ 𝒜(δ) for every δ.
   * Hence NC(η): 𝒜(U^{−η}) ≪ U^{1−η+ε} suffices for N₂ ≪ U^{1−η+ε}, and TD(η) ⇒ NC(η). NC is one-sided, localized at
     0 and ε-lossy, so it is weaker in form than TD.
   * A stronger sufficient condition for NC is a sharp-order bound for the τ-perturbed tie counts Σ_{|τ|≤13Uδ}N^{[τ]}.
   * The displayed elementary estimate for those counts, U^{1+ε} + T·U^{1/2+ε}, does not reach the model order T for
     1 ≤ T ≤ U. By contrast, the elementary bound for n-windows (Prop A) is of sharp order once the window length is ≥ U.
   * N₂² ≤ P(δ) (pair correlation). An ℓ²-in-h pair-correlation bound is one sufficient input (Assessment: second order,
     like MIX).
6. **Level averaging (Prop E, scoped).**
   * The direct untwisted completion of the strip condition m | p + s is plain orthogonality and exhibits no
     nondegenerate Kloosterman sum (PROVED identity).
   * Kloosterman-type sums do arise elsewhere: in the (u, B)-CRT form (DFI/Bettin–Chandee, scoped closures in
     HYPKLOOST), and from the discriminant character in the square sieve (BILINJAC (F3)).
   * No general statement about spectral or spacing methods is made.
7. **EVIDENCE.**
   * At 10¹⁰ the measured radial tails and second moment of T(h)/√|E1⁺| are compatible with the unit-second-moment
     complex-Gaussian (random-phase) model: 96 000 (p, h) at generic primes, 48 000 at three structured prime families,
     and 115 200 at odd squares. There is no falsifier.
   * The count error has sd ≈ 2.2–3.3·√U, against a pooled rms of ≈ 1.0·√|E1⁺| for T(h).

**Answers to the kickoff questions (Assessment, built on the PROVED items).**
1. No implication between TD and a pointwise short-interval divisor statement is established here, in either direction.
   * The natural smooth expansions of TD and of the untwisted count (a central slice of the x^{1/4} short-interval
     divisor problem) have disjoint carrier bands.
   * TD is about the exact remainders r_m inside the window. The count and TS_{N₂} are about window membership (and
     classes mod Q).
   * In the per-frequency benchmark TD's deficit is larger than square-root Jutila's on the central slice. Measured
     against the random model of the whole double sum, TD(η) asks for nothing more than CNT(η).
2. *Partial results.*
   * The averaged R2 conclusion and the exceptional-prime count are elementary (Prop A, Cor A′).
   * The pointwise first-order constant is 0.307 (Remark A‴).
   * Small-w pieces of TD are free (Lemma S(c)).
   * The pointwise input that the Theorem-T route needs is exactly an NC-type upper bound at one p.
   * Averaged TD, TD for many U and smoothed TD are not proved.
3. *Beyond Voronoi at one p.*
   * h-averaging inside Theorem T is a Fourier proof of an NC-type bound (Prop D).
   * Benchmark-class arguments cannot reach the targets (Prop C).
   * Nothing here beats Voronoi at a single p. Joint (ν, m) methods, spectral methods on other transforms, and
     arithmetic upper-bound arguments for NC are not excluded.

## 1. Notation (as in Z54_BILINDIV)

* p is an odd prime (n is a general positive integer where stated) and U ≥ 4 an integer. The fourth-root range is
  c₁p^{1/4} ≤ U ≤ c₂p^{1/4}, with 16U³ ≤ p. Implied constants may depend on c₁, c₂ and the fixed test functions.
* N₂(n, U) := #{{u, B} ⊂ (U, 2U], u ≠ B : uB | n + u + B}. This is the product-divisibility definition for every n; at
  primes it is the 2-cycle count.
* E1 = E1(p, U) := {(k, m) ∈ ℕ² : p + 2U < km ≤ p + 4U, U² < m ≤ 4U²}. Put s := km − p ∈ (2U, 4U] and D := s² − 4m.
  Then E1⁺ := {D ≥ 1}, w := √D and T(h) := Σ_{E1⁺} e(hw).
* For m ∤ p: r_m := (−p mod m) ∈ [1, m) and θ_m := r_m/m = {−p/m}. Since U ≥ 4, every m ∈ (U², 4U²] has m > 4U and
  m < p, so it carries at most one strip point. That point exists iff r_m ∈ (2U, 4U], and then s = r_m and
  k = (p + r_m)/m = ⌈p/m⌉.
* TD(η), BILINDIV: |T(h)| ≤ C₀U^{1−η} for 1 ≤ h ≤ U^η, uniformly for primes p and U in the fourth-root range. Theorem T
  (BILINDIV, PROVED): TD(η) ⇒ N₂ ≪ U^{1−η+ε}.
* CNT(η) (untwisted count): |E1(p, U)| = 2U log 4 + O(U^{1−η}) uniformly in the fourth-root range. Open.
* Δ(x) := Σ_{n≤x} d(n) − x log x − (2γ − 1)x, and D(x, y) := Σ_{x<n≤x+y} d(n).

## 2. Statements attacked

* **(Q1) Calibration.** The relation of TD to CNT, to TS and to Jutila's conjecture
  Δ(x+y) − Δ(x) ≪_ε x^ε√y (x^ε ≤ y ≤ x^{1/2−ε}; Ivić, JTNB 21 (2009), (1.13), a CONJECTURE, verified in LIT_CHECK)
  at y ≍ x^{1/4}. Targets: exact identities, band localization of natural expansions, per-frequency benchmark deficits.
* **(Q2) Partial results.** R2 on average over n, the first-order constant, free pieces of TD, and the exact missing
  pointwise input (NC).
* **(Q3) Beyond Voronoi at one p.** What frequency averaging in Theorem T amounts to, and what the direct completions of
  the strip condition contain.

## 3. Why this is not already closed

* BILINDIV §4.2 records "TD vs MIX: neither shown to imply the other" and gives a stationary-phase *Assessment* of a
  double dual. It makes no comparison with the count or with Jutila's conjecture, and has no band statement.
* BILINJAC §5 calls square-root TS "a twisted analogue of Jutila's conjecture" and proves no implication. Its §5.3
  computes exponent-pair bound expressions for its own T_Q(a, 0) expansion only.
* No memo treats averages over n or over U for R2. `git grep` on "average over p" finds only unrelated B6 items.
* No memo isolates the one-sided near-integer count (NC) as what Theorem T's Fourier route delivers.

## 4. Averages over n; the first-order constant

**Proposition A (PROVED).** For all integers X ≥ 0, Y ≥ 1 and U ≥ 2,

  Σ_{X<n≤X+Y} N₂(n, U) = #{(u, B, M) : U < u < B ≤ 2U, uB | M, X < M − u − B ≤ X + Y}
                       ≤ Σ_{X+2U < M ≤ X+Y+4U} τ(M)².

Consequently, for X ≍ U⁴ and every ε > 0:
* (a) the mean of N₂(n, U) over n ∈ (X, X + Y] is ≪_ε (1 + U/Y)U^ε;
* (b) for every η ∈ (0, 1), at most O_ε(U^{η+ε}) integers in any window of U consecutive integers have
  N₂(n, U) > U^{1−η};
* (c) Σ_{X<n≤X+Y} N₂(n, U) = Y·Σ_{U<u<B≤2U} 1/(uB) + O(U²). So for Y ≥ U^{2+ε} the window mean is ½(log 2)² + o(1).

*Proof.*
* The map (n, {u < B}) ↦ (u, B, M := n + u + B) is injective and lands in the displayed set. Conversely each such
  (u, B, M) gives n := M − u − B with uB | n + u + B. Since 2U < u + B ≤ 4U, M ∈ (X + 2U, X + Y + 4U].
* For fixed M the pairs with uB | M have u | M and B | M, so there are ≤ τ(M)² of them.
* (c): for each of the < U² pairs, the multiples of uB in an interval of length Y number Y/(uB) + O(1). Also
  Σ_{U<u<B≤2U} 1/(uB) = ½[(Σ1/u)² − Σ1/u²] = ½(log 2)² + O(1/U).
* (a): for Y ≤ U², every M in the range is ≪ U⁴, and τ(M) ≪_ε M^{ε/8} gives (Y + 2U)U^{ε}. For Y > U², (c) gives a
  mean O(1 + U²/Y) = O(1).
* (b): (a) with Y = U and Markov's inequality. ∎

**Corollary A′ (PROVED; exceptional primes).** Fix η ∈ (0, 1), ε > 0 and put U_p := ⌊p^{1/4}⌋. Then
#{p ≤ X prime : N₂(p, U_p) > U_p^{1−η}} ≪_{η,ε} X^{(3+η)/4+ε}.
*Proof.*
* Split (X^{1/2}, X] into dyadic ranges (Z, 2Z]. On such a range U_p takes O(Z^{1/4}) values U.
* Each value U is taken on an interval of O(U³) integers n, covered by O(U²) windows of length U.
* By Prop A(b) each window has O(U^{η+ε}) exceptional n. So the range contributes
  O(Z^{1/4}·U²·U^{η+ε}) = O(Z^{1/4}·Z^{(2+η)/4+ε}) = O(Z^{(3+η)/4+ε}).
* Sum over the dyadic ranges, and add ≤ X^{1/2} for p ≤ X^{1/2}. ∎

**Remark A″ (averaging over U; PROVED identity, Assessment reading).** For a prime p and an integer U₀ ≥ 2,
  Σ_{U₀≤U<2U₀} N₂(p, U) = Σ_{2-cycles {u<B}} μ(u, B),
  μ(u, B) := #{U ∈ [U₀, 2U₀) : B/2 ≤ U < u} = max(0, min(2U₀ − 1, u − 1) − max(U₀, ⌈B/2⌉) + 1) ≤ U₀.
Every cycle with μ > 0 lies in (U₀, 4U₀)² with B < 2u. So the U-average is a weighted count of the same objects in a
box of twice the size. (Assessment: this identity alone gives no pointwise saving. It does not rule out other uses of
several U.)

**Remark A‴ (the first-order constant; PROVED relative to Titchmarsh Thm 5.13 as used in BILINDIV Prop 5.3).** In the
fourth-root range, N₂(p, U) ≤ (1 − log 2)U + O(U^{1−3/56+ε}) ≈ 0.307U.
*Proof.*
* In a 2-cycle {B < u} we have B ≡ −p (mod u) and U < B < u, so B = r_u and θ_u = B/u > U/u. The larger element
  determines the cycle (B = r_u). Hence N₂ ≤ Z := #{u ∈ (U, 2U] : θ_u > U/u}.
* Split (U, 2U] into ≍ U^{1/2} blocks I of length L ≍ U^{1/2}. On a block, U/u varies by O(U^{−1/2}). So
  Z ≤ Σ_I [L(1 − min_I U/u) + L·𝒟_I] = U(1 − log 2) + O(U^{1/2}) + LΣ_I𝒟_I, where 𝒟_I is the discrepancy of
  (θ_u)_{u∈I}.
* Erdős–Turán: 𝒟_I ≪ 1/H + Σ_{h≤H}h^{−1}L^{−1}|Σ_{u∈I}e(hp/u)|.
* For f(u) = hp/u, f⁗ = 24hp/u⁵ ≍ h/U on I, with bounded ratio. The fourth-derivative test (k = 4, K = 8) gives
  |Σ_I e(f)| ≪ L(h/U)^{1/14} + L^{3/4}(U/h)^{1/14}.
* With H = U^{1/15}: 𝒟_I ≪ U^{−1/15}log U + U^{−1/8+1/14}log U ≪ U^{−3/56}log U.
* Summing over the ≍ U^{1/2} blocks gives the claim. ∎

The smaller elements satisfy the other first-order condition θ_B = (u − B)/B ≤ (2U − B)/B, which has density
2 log 2 − 1 ≈ 0.386. The pairing u ↔ B is second order (MIX). So ≈ 0.307U is what this first-order argument gives
(Assessment). It improves the trivial U/2 by a constant factor and has no bearing on a power saving.

*Reading (Assessment).*
* The *conclusion* of R2 is elementary on average over any window of U^{η+ε} consecutive n, and off a sparse set of
  primes. So an averaged R2 conclusion needs no TD-type hypothesis.
* Whether averaged forms of TD hold is not addressed. Prop A does not bound |T(h)|.
* The missing piece for R2 is a single-n bound. Prop D identifies the input that the Theorem-T route delivers there.

**EVIDENCE (`scripts/z55_tdcal_window.c`, `data/z55/tdcal/window.txt`; the script sums over n ∈ [X, X + Y)).**
* n ∈ [10⁸, 10⁸ + 20000), U = 100: ΣN₂ = 4662, mean 0.233, max 4. The (u, B, M) count over the M-range
  (X + 2U, X + Y + 4U] is 4707.
* n ∈ [10¹², 10¹² + 2000), U = 1000: ΣN₂ = 461, mean 0.231, max 3; histogram 0:1599, 1:347, 2:48, 3:6.
* These are means over all integers, not only primes; ½(log 2)² = 0.2402.

## 5. Structural forms (Lemma S)

**Lemma S (PROVED).** Let p be prime, U ≥ 4 and 16U³ ≤ p.

**(a) Central-slice identity** (valid for U ≥ 2). Put x := p + 2U and y := 2U. Then
  |E1| = #{(m, M) : x < M ≤ x + y, m | M, U² < m ≤ 4U²} = 2U log 4 + E(p, U),
  E(p, U) = Σ_{U²<m≤4U²} [ψ(x/m) − ψ((x + y)/m)] + O(1/U),  with ψ(t) = t − ⌊t⌋ − ½.
Since D(x, y) = #{(m, M) : x < M ≤ x + y, m | M}, |E1| is the part of D(x, y), at length y ≍ x^{1/4}, whose divisor lies
in (U², 4U²]. That is a slice at m ≍ √x, since U² ≍ √p up to the factors c₁², c₂².
*Proof.*
* Each m ∈ (U², 4U²] exceeds y, so it has ⌊(x+y)/m⌋ − ⌊x/m⌋ ∈ {0, 1} multiples M in (x, x + y].
* Each such multiple gives the strip point (M/m, m), and conversely; so |E1| is the displayed count.
* Write ⌊t⌋ = t − ψ(t) − ½ and use Σ_{U²<m≤4U²} 2U/m = 2U log 4 + O(1/U). ∎

**(b) Two-shift form** (primes only).
N₂(p, U) = #{(u, w) ∈ ℕ² : U < u < u + w ≤ 2U, u | p + w, u + w | p − w}.
*Proof.*
* Put B = u + w. Then u | p + B ⟺ u | p + w, and B | p + u ⟺ B | p + B − w ⟺ B | p − w.
* At a prime p > 2U, gcd(u, B) | p forces gcd(u, B) = 1. So the two divisibilities are equivalent to uB | p + u + B. ∎
At composites only "≥" holds. For example, at n = 10005², U = 100, the pair u = 126, B = 171 satisfies both
divisibilities but uB ∤ n + u + B (review 1, item 19).

**(c) Discriminant form** (valid for every n). If (s, m) ∈ E1 then m | p² − D. Consequently, for 1 ≤ X ≤ 16U²,
  #{(k, m) ∈ E1 : 1 ≤ D ≤ X} ≤ Σ_{1≤D≤X} τ(p² − D) ≪_ε X p^ε.
In particular the part of T(h) with w ≤ U^{(1−η)/2} is ≪_ε U^{1−η+ε} for every h: TD holds trivially there.
*Proof.*
* m | p + s gives p ≡ −s, hence p² ≡ s² = D + 4m ≡ D (mod m).
* For fixed D, s = √(4m + D) is determined by m, so (s, m) ↦ m is injective on {D fixed}.
* Finally 0 < p² − D, because D ≤ 16U² < p². ∎
On a 2-cycle (D = w², w = B − u), (c) reads uB | (p − w)(p + w), matching (b). This free range for T itself
(w ≤ U^{(1−η)/2}) is smaller than BILINDIV Remark 4.1's free range for 2-cycles (B − u ≤ U^{1−η}).

## 6. Theorem B: band localization of the natural smooth expansions

*Setting.*
* Fix φ ∈ C_c^∞((1, 4)), Φ ∈ C_c^∞((2, 4)) and Ψ ∈ C_c^∞((½, 2)), with values in [0, 1].
* Let 0 < σ ≤ 1 be fixed, W ∈ [U^σ, 4U] and h ∈ [1, U].
* Define the smoothed count and the smoothed W-piece of T:
  C(p, U) := Σ_m φ(m/U²)Φ(r_m/U),
  T_W(h) := Σ_m φ(m/U²)Φ(r_m/U)Ψ(w_m/W)e(hw_m),  with w_m := √(r_m² − 4m) (the term is 0 if r_m² ≤ 4m).
* These are smoothed pieces, not the sharp sums |E1| and T(h). This section says nothing about the sharp boundaries in s
  and m, or about the D ≥ 1 cutoff.
* *The N₂-strip analogue of TS.* Put TS_{N₂}: T_Q(a, b) := Σ_m κ_m φ(m/U²)Φ(r_m/U), with κ_m := e((a⌈p/m⌉ + bm)/Q),
  Q ≥ 1. This is an analogue of BILINJAC's T_Q, not BILINJAC's own sum: BILINJAC has the window 4Ck − n, the level
  cutoff C ∈ (W, 2W] and its own normalization. (For BILINJAC's sum the analogous expansion is in θ = {−p/(4C)}, with
  the same scale U; it is not carried out here.)

*Expansion (PROVED identity, as in BILINDIV §4.3).*
* For each m define G_m(θ) := φ(m/U²)Φ(mθ/U)Ψ(W_m(θ)/W)e(hW_m(θ)) on [0, 1), where W_m(θ) := √(m²θ² − 4m).
* Its support lies in (2U/m, 4U/m) ⊂ (0, 1), so it extends to a smooth 1-periodic function.
* Put ĉ_m(ν) := ∫₀¹G_m(θ)e(−νθ)dθ. Since e(νθ_m) = e(−νp/m) (r_m ≡ −p mod m),
  T_W(h) = Σ_{ν∈ℤ} Σ_m ĉ_m(ν) e(−νp/m),  and likewise C(p, U) = Σ_ν Σ_m ĉ⁰_m(ν)e(−νp/m),
  with ĉ⁰_m(ν) = φ(m/U²)(U/m)Φ̂(νU/m) exactly.

**Theorem B (PROVED).** Fix the test functions, σ ∈ (0, 1], 0 < ε < 1 and A > 0. For U ≥ U₀, every W ∈ [U^σ, 4U],
every 1 ≤ h ≤ U, and every family of coefficients (κ_m) with |κ_m| ≤ 1:
(i) C(p, U) = Σ_{|ν|≤U^{1+ε}} Σ_m ĉ⁰_m(ν)e(−νp/m) + O(U^{−A});
(ii) Σ_m κ_mφ(m/U²)Φ(r_m/U) = Σ_{|ν|≤U^{1+ε}} Σ_m κ_mĉ⁰_m(ν)e(−νp/m) + O(U^{−A}). This holds in particular for TS_{N₂}, and for
any sharp cutoff in m;
(iii) with λ_W := hU³/W, T_W(h) = Σ_{λ_W/2 ≤ ν ≤ 64λ_W} Σ_m ĉ_m(ν)e(−νp/m) + O(U^{−A}).
Since λ_W/2 ≥ hU²/8 > U^{1+ε} for U ≥ U₀, the ν-ranges in (i)–(ii) and in (iii) are disjoint.

*Proof.*
(i) |Φ̂(ξ)| ≪_{A′} (1 + |ξ|)^{−A′}, and |ν|U/m ≥ |ν|/(4U) for m ≤ 4U². So
Σ_{|ν|>U^{1+ε}}Σ_m|ĉ⁰_m(ν)| ≪ U·Σ_{|ν|>U^{1+ε}}(|ν|/4U)^{−A′} ≪ U^{2+A′}U^{(1+ε)(1−A′)}. This is O(U^{−A}) for A′ large in
terms of A and ε.
(ii) The m-sum is Σ_m κ_mG⁰_m(θ_m) with G⁰_m(θ) = φ(m/U²)Φ(mθ/U). Its coefficients are κ_mĉ⁰_m(ν) with |κ_m| ≤ 1, and the
tail estimate of (i) applies verbatim. For TS_{N₂}: m ∈ (U², 4U²] and m < p give m ∤ p, so p + r_m = m⌈p/m⌉, and the
level is a function of m alone.
(iii) *Derivative bounds.* On the support s = mθ ∈ (2U, 4U), m ∈ (U², 4U²) and W_m ∈ (W/2, 2W).
* Let g(s) := (s² − 4m)^{1/2}. Faà di Bruno (inner derivatives 2s, 2, 0, …) gives
  g^{(j)}(s) = Σ_{⌈j/2⌉≤i≤j} c_{j,i}s^{2i−j}(s² − 4m)^{1/2−i}.
* Each term is ≪ W(U/W)^{2i}U^{−j}. Since U/W ≥ 1/4, each term is bounded by the i = j scale up to a j-dependent
  constant. So g^{(j)} ≪_j U^jW^{1−2j}.
* Hence W_m^{(j)}(θ) = m^jg^{(j)}(mθ) ≪_j Wρ^{−j}, where ρ := W²/U³ ≤ 16/U.
* Amplitude: (d/dθ)^jΦ(mθ/U) ≪ (m/U)^j ≤ (4U)^j ≤ (64/ρ)^j, and Faà di Bruno gives (d/dθ)^jΨ(W_m/W) ≪_j ρ^{−j}. So the
  amplitude a_m(θ) satisfies a_m^{(j)} ≪_j ρ^{−j}.

*First derivative of the phase.* Let F(θ) := hW_m(θ) − νθ. Then W_m′ = m²θ/W_m = ms/W_m, so on the support
hW_m′ ∈ (hU²·2U/(2W), h·4U²·4U/(W/2)) = (λ_W, 32λ_W). Put Λ := max(|ν|, λ_W).
* If ν < λ_W/2 (including ν ≤ 0), then F′ ≥ λ_W − ν ≥ Λ/2.
* If ν > 64λ_W, then −F′ ≥ ν − 32λ_W ≥ Λ/2.
For j ≥ 2, F^{(j)} = hW_m^{(j)} ≪_j hWρ^{−j} = λ_Wρ^{1−j} ≤ Λρ^{1−j}.

*Non-stationary phase.*
* Let L_F g := (g/(2πiF′))′. Repeated integration by parts gives ∫a_m e(F) = (−1)^A∫(L_F^A a_m)e(F).
* Since |F′| ≥ Λ/2 and F^{(j)} ≪ Λρ^{1−j}, we have (1/F′)^{(j)} ≪_j Λ^{−1}ρ^{−j}. So by induction
  (L_F^A a_m)^{(j)} ≪_{A,j} (Λρ)^{−A}ρ^{−j}, and |ĉ_m(ν)| ≪_A (Λρ)^{−A} (the support has length ≤ 1).
* Here λ_Wρ = hW ≥ U^σ. Sum over ≤ 4U² values of m and over ν outside [λ_W/2, 64λ_W]:
  * |ν| ≤ 64λ_W: at most 129λ_W + 1 ≤ U⁵ terms, each ≪ (hW)^{−A};
  * |ν| > 64λ_W: Σ_ν(|ν|ρ)^{−A} ≪ ρ^{−1}(λ_Wρ)^{1−A}, with ρ^{−1} ≤ U³.
  The total is O(U^{7}(hW)^{1−A}) = O(U^{7−σ(A−1)}), which is O(U^{−A″}) for A large in terms of σ.
* Disjointness: λ_W/2 = hU³/(2W) ≥ hU²/8 > U^{1+ε} when ε < 1 and U ≥ U₀. ∎

**Remark B2 (the band depends on the expansion; PROVED observation).** Part (ii) allows arbitrary κ_m with |κ_m| ≤ 1.
* Choose κ_m := 1[r_m² > 4m]Ψ(w_m/W)e(hw_m). This depends only on m and p (through r_m), so the *same* T_W(h) also has a
  low-band expansion with the oscillation moved into κ_m.
* Moreover e((ν + jm)θ_m) = e(νθ_m) on the actual remainder grid.
* So Theorem B describes the carrier bands of two particular natural expansions: all s-dependence in the smooth
  θ-function, and smooth or bounded m-coefficients. It is not an intrinsic separation of the statements.

*Reading (Assessment).*
* In the natural expansions, the count and TS_{N₂} ask how many remainders r_m fall in the window (and in which classes
  mod Q). TD asks how the exact remainders are distributed *inside* the window: resolution 1/(hU²) in θ, i.e. O(1/h)
  in r_m.
* No implication between TD and CNT/TS/Jutila-type statements is established here, in either direction.
* MIX (HYP2CYCLE) is on a different family: remainders p mod u at moduli u ≍ p^{1/4}, at second order.

## 7. Proposition C: the per-frequency benchmark

**Benchmark.** In the expansions of §6 each target is Σ_ν Σ_m c_m(ν)e(−νp/m) over a band of ν. The *benchmark* is
Σ_ν ‖c(ν)‖₂, with ‖c(ν)‖₂ := (Σ_m |c_m(ν)|²)^{1/2}, the random-phase size of each m-sum.
* The *benchmark class* is that of BILINDIV Prop 4.3: arguments that apply the triangle inequality over ν with
  majorants β_ν ≥ c₀‖c(ν)‖₂ for the m-sums (c₀ > 0 fixed). Every argument in this class yields a bound at least
  c₀ × the benchmark.
* This is not a claim about what the exponent-pair conjecture gives for sums with arbitrary oscillatory coefficients:
  such coefficients may cancel the phase.

**Proposition C.**
(i) *Count (PROVED).* Assume φ ≢ 0 and Φ ≢ 0 (both nonnegative). Then Σ_{1≤|ν|≤U^{1+ε}} ‖ĉ⁰(ν)‖₂ ≍ U, both ways.
* The main term ĉ⁰(0)-part of C is ≍ U.
* So every argument in the benchmark class bounds C − main term only by ≫ U.
* CNT-type power savings, C − main ≪ U^{1−η}, lie outside the class: relative to the benchmark they need a further
  saving U^η.
(ii) *Central-slice square root (PROVED arithmetic).* The slice analogue of Jutila's conjecture, C − main ≪ U^{1/2+ε}
(y = 2U, so √y ≍ U^{1/2}), is U^{1/2} below the benchmark.
(iii) *TD, top piece (BILINDIV Prop 4.3, PROVED there for its level-parametrized weights T_φ).* In that class
Σ_{|ν|≥hU}b_ν ≫ h^{1/2}U^{3/2}. TD(η) needs U^{1−η}, i.e. h^{1/2}U^{1/2+η} below this.
(iv) *TD, piece W (Assessment).* Assume quantitative overlap of the supports, so that the piece carries ≍ W²/U strip
points. Then the Parseval mass ≍ W²/U and the pointwise bound |ĉ_m(ν)| ≪ (hU⁶/W³)^{−1/2} (from |hW_m″| = 4hm³/W_m³)
make the benchmark ≍ h^{1/2}W^{1/2}U, against a target U^{1−η}.

*Proof of (i).*
* *Upper bound.* ‖ĉ⁰(ν)‖₂² = Σ_m φ(m/U²)²(U/m)²|Φ̂(νU/m)|² ≪_A Σ_{U²<m<4U²}U^{−2}(1 + |ν|/(4U))^{−2A} ≪ (1 + |ν|/4U)^{−2A}.
  Hence Σ_ν‖ĉ⁰(ν)‖₂ ≪ U.
* *Lower bound.* Φ̂(0) = ∫Φ > 0 and Φ̂ is continuous, so |Φ̂(ξ)| ≥ Φ̂(0)/2 for |ξ| ≤ ξ₀. For 1 ≤ |ν| ≤ ξ₀U and
  m > U², |νU/m| ≤ ξ₀. Hence ‖ĉ⁰(ν)‖₂² ≥ (Φ̂(0)/2)²Σ_m φ(m/U²)²(U/m)² ≥ c > 0, since φ ≢ 0. Summing over
  1 ≤ |ν| ≤ ξ₀U gives ≫ U.
* *Main term.* Σ_m ĉ⁰_m(0) = Φ̂(0)Σ_m φ(m/U²)U/m ≍ U. ∎
(ii) and (iii) are the target arithmetic and BILINDIV Prop 4.3.

**Table 7.1 (exponents in U; trivial size U for every target; status of each row as in Prop C).**

| target | carrier band (Thm B, natural expansion) | benchmark | target size | factor below the benchmark |
|---|---|---|---|---|
| CNT(η) (untwisted central slice, smoothed) | \|ν\| ≤ U^{1+ε} | ≍ U | U^{1−η} | U^{η} |
| central-slice square root (Jutila-type, y ≍ x^{1/4}) | same | ≍ U | U^{1/2} | U^{1/2} |
| TS_{N₂}(δ) (κ-twisted low band) | same | ≤ ≍ U (\|κ\| ≤ 1) | U^{1−δ} | ≥ U^{δ} (if benchmark ≍ U) |
| TD(η), top piece (BILINDIV Prop 4.3 class) | ν ≍ hU² | ≫ h^{1/2}U^{3/2} | U^{1−η} | h^{1/2}U^{1/2+η} |
| TD, square root, top piece | same | same | U^{1/2} | h^{1/2}U |
| TD(η), piece W (Assessment) | ν ≍ hU³/W | ≍ h^{1/2}W^{1/2}U | U^{1−η} | h^{1/2}W^{1/2}U^{η} |

*Reading (Assessment).*
* Against the benchmark, TD(η) for any η > 0 needs a larger factor (U^{1/2+η}) than square-root Jutila on the central
  slice (U^{1/2}). The benchmark is the natural currency of per-frequency tools.
* Against the random model of the whole double sum (size ≍ U^{1/2} for every row), the power-saving rows (CNT(η), TD(η))
  *allow* a factor U^{1/2−η} above that model size, and TS_{N₂}(δ) allows U^{1/2−δ}. The square-root rows ask for the
  model size itself.
* So "TD is harder than Jutila" holds only in the per-frequency currency. In the whole-sum currency TD(η) and CNT(η) ask
  for the same thing.
* No checked source proves a power-saving pointwise asymptotic even for the untwisted central slice at length x^{1/4}.
  The checked global bound Δ(x) ≪ x^{θ*+ε}, θ* = 0.31448… (Li–Yang 2023, Thm 1.2; LIT_CHECK Q1) yields full
  short-interval asymptotics only for lengths ≥ x^{θ*+ε}. This is search-limited, not a non-existence claim.

## 8. Proposition D: what Theorem T's Fourier route delivers — the near-integer count

For 0 < δ ≤ 1/4 put 𝒜(δ) := #{k ∈ E1⁺ : ‖w_k‖ ≤ δ}, where ‖·‖ is the distance to ℤ, and
P(δ) := #{(k, k′) ∈ (E1⁺)² : ‖w_k − w_{k′}‖ ≤ δ}.

**Proposition D (PROVED).**
(i) *Sandwich and NC.* Let χ_δ be as in BILINDIV Thm T (ψ supported in (−2, 2), 0 ≤ ψ ≤ 1, ψ = 1 on [−1, 1]). Then
  𝒜(δ) ≤ Σ_{k∈E1⁺} χ_δ(w_k) ≤ 𝒜(2δ),  and  N₂ ≤ 𝒜(δ) for every δ.
* Theorem T's Fourier computation evaluates the middle term, so every bound obtained that way is in particular a bound
  for 𝒜(δ).
* Define **NC(η)**: for every ε > 0, 𝒜(U^{−η}) ≪_ε U^{1−η+ε}, uniformly for primes p and U in the fourth-root range.
* Then NC(η) ⇒ N₂ ≪ U^{1−η+ε}, and TD(η) ⇒ NC(η).
(ii) *Approximate ties.* With N^{[τ]}(p, U) := #{((s, m), j) : (s, m) ∈ E1⁺, j ∈ ℕ, s² − 4m − j² = τ},
  𝒜(δ) ≤ Σ_{|τ|≤13Uδ} N^{[τ]}(p, U).
* For τ = 0, N^{[0]} counts the strip points with D a square, and N₂ ≤ N^{[0]} (Lemma A also asks for roots in (U, 2U]).
* For τ ≠ 0, N^{[τ]} counts divisors m of p + s that lie |τ|/4 away from ((s − j)/2)((s + j)/2).
* A sharp-order bound Σ_{|τ|≤13Uδ}N^{[τ]} ≪ U^{1−η+ε} at δ = U^{−η} is therefore a *stronger* sufficient condition for
  NC(η). The converse fails: |w − j| = |τ|/(w + j), so points with small w in the τ-window need not be δ-near integers.
(iii) *The displayed elementary estimate for τ-windows.* For every T ≥ 0,
  Σ_{|τ|≤T} N^{[τ]}(p, U) = Σ_{(s,m)∈E1⁺} #{j ∈ ℕ : |D − j²| ≤ T} ≤ |E1| + 2T·Σ_{(s,m)∈E1⁺} D^{−1/2}
                        ≪_ε U^{1+ε} + T·U^{1/2+ε}.
* For 1 ≤ T ≤ U this estimate does not reach the model order ≍ T (Assessment for the model order; EVIDENCE in §10.3′).
* At T = 13U^{1−η} it gives ≫ U^{1+ε} where NC asks for U^{1−η+ε}.
* This concerns this estimate only. It is not a lower bound for the count, and not a barrier for other arguments.
* Contrast Prop A: in the shift n the elementary bound (Y + 2U)U^ε is of sharp order as soon as Y ≥ U.
(iv) *Pair correlation.* N₂² ≤ P(δ) for every δ > 0. With the Fejér kernel F_H(x) = Σ_{|h|<H}(1 − |h|/H)e(hx) ≥ 0,
  Σ_{|h|<H}(1 − |h|/H)|T(h)|² = Σ_{k,k′}F_H(w_k − w_{k′})   (the h = 0 term is |E1⁺|²).
* Consequently, a bound Σ_{k,k′}F_{2H}(w_k − w_{k′}) ≤ |E1⁺|² + O(H·U^{2−2η}), with H = U^{η}, gives
  Σ_{1≤h≤H}|T(h)|² ≪ HU^{2−2η}. Cauchy–Schwarz then gives Σ_{1≤h≤H}|T(h)| ≪ HU^{1−η}, which is the input of Theorem T
  with δ ≍ U^{−η+ρ} (H = U^{ρ/2}/δ ≤ U^{η}, as in Corollary T).
* So this pair-correlation bound is one *sufficient* input; it is not shown to be necessary.
* (Assessment: it is a power-saving second-order statement, comparable in kind to MIX; no implication is claimed.)

*Proof.*
(i) For δ ≤ 1/4 at most one translate ψ((x + j)/δ) is nonzero at any x; it is ≤ 1 and supported in ‖x‖ < 2δ. So
χ_δ ≤ 1[‖·‖ < 2δ], and χ_δ(x) = 1 when ‖x‖ ≤ δ. This gives the sandwich.
* N₂ ≤ 𝒜(δ): by Lemma A each 2-cycle gives a distinct level with w ∈ ℤ.
* NC ⇒ N₂: take δ = U^{−η}.
* TD(η) ⇒ NC(η): fix 0 < ρ < min(η, ε)/2 and run BILINDIV's Corollary T computation with δ′ := U^{−η+ρ} and
  H = U^{ρ/2}/δ′ = U^{η−ρ/2} ≤ U^η, inside TD's frequency range. It gives Σ_kχ_{δ′}(w_k) ≪ U^{1−η+ρ+ε/2}.
  Since 𝒜 is monotone, 𝒜(U^{−η}) ≤ 𝒜(δ′) ≤ Σ_kχ_{δ′}(w_k) ≪ U^{1−η+ε}.
(ii) Let ‖w‖ ≤ δ with nearest integer j. Then j ≥ 1 (since w ≥ 1 > δ) and j ≤ w + δ ≤ 4U + 1. So
|D − j²| = |w − j|(w + j) ≤ δ(2w + δ) ≤ 9Uδ ≤ 13Uδ. The map k ↦ ((s, m), j, D − j²) is injective. Lemma A gives
N₂ ≤ N^{[0]}.
(iii) The equality is the definition (τ = D − j²). For fixed (s, m), the j ≥ 1 with |D − j²| ≤ T lie in
[√(max(D − T, 0)), √(D + T)], an interval of length ≤ 2T/√D:
* if D ≥ T it is 2T/(√(D + T) + √(D − T)) ≤ 2T/√D;
* if D < T it is ≤ √(2T) ≤ 2T/√D.
So there are ≤ 1 + 2T/√D of them. For ΣD^{−1/2}, split E1⁺ dyadically by D ∈ (X, 2X], X ≤ 16U². By Lemma S(c) such a
piece has ≪ min(XU^ε, |E1|) ≪ min(X, U)U^{2ε} points, and so contributes ≪ min(X, U)U^{2ε}X^{−1/2}. Summing over dyadic X
gives ≪ U^{1/2+2ε}log U. Finally |E1| ≪ U^{1+ε}.
(iv) A 2-cycle level has w ∈ ℤ, so every ordered pair of 2-cycle levels lies in P(0) ⊂ P(δ). The Fejér identity is the
expansion of |Σ_k e(hw_k)|². For the consequence:
* on |h| ≤ H the weight satisfies 1 − |h|/(2H) ≥ ½, so Σ_{1≤|h|≤H}|T(h)|² ≤ 2(Σ_{k,k′}F_{2H} − |E1⁺|²);
* then apply Cauchy–Schwarz over 1 ≤ h ≤ H. ∎

*Reading (Assessment).*
* Theorem T's Fourier route proves upper bounds for 𝒜(δ). NC is exactly the pointwise statement this route needs, and
  any successful run of the route yields NC at the corresponding δ.
* NC is weaker in form than TD: one-sided, localized at 0 and ε-lossy. Whether it is easier on this arithmetic family
  is open.
* Averaging the *target integer* n is free once the window length is ≥ U (Prop A). The displayed τ-window estimate at
  fixed n does not reach the model order: it moves the divisor constraint, not the integer.
* An upper bound is enough for NC, so arguments of sieve type are not excluded. The free divisor counts used here
  (Lemma S(c)) lose the s ↔ m link and give only ≫ U.

## 9. Proposition E: the direct completion of the strip condition

**Proposition E.**
(i) *(PROVED identity.)* For m > 4U and any function g on (2U, 4U]:
  Σ_{s∈(2U,4U], m|p+s} g(s) = (1/m)Σ_{a mod m} e(ap/m) Σ_s e(as/m) g(s).
* This is orthogonality. If g = g(·, m) is smooth, Poisson summation in s turns the inner sum into Fourier transforms of
  g at the frequencies a/m + ℤ. Collecting terms reproduces the θ-expansion of §6: coefficients times e(−νp/m).
* The only arithmetic is "p mod m" (equivalently ⌊p/m⌋, ⌈p/m⌉). This direct untwisted completion exhibits no
  nondegenerate Kloosterman sum S(·, ·; m). The same holds in the (k, s) parametrization with "p mod k".
(ii) *(Scoped; references.)* Kloosterman-type structure does arise in other transforms of the same problem:
* in the (u, B)-CRT detection of u | p + B, B | p + u: Kloosterman fractions, the DFI / Bettin–Chandee setting of
  Z53_HYPKLOOST. There the displayed bounds need C̄ ≲ p^{1/37} (DFI Theorem 2), resp. p^{1/21} (Bettin–Chandee), to
  save — necessary conditions for those bounds only, which fail at the balanced block;
* from the discriminant character in the square sieve (BILINJAC (F3), via SQSIEVE Lemma W).
No statement about spectral methods (Kuznetsov) applied to such transforms is made here.
(iii) *(Assessment.)* Arguments in the benchmark class of §7 cannot reach the targets of Table 7.1 (Prop C). Whether
Bombieri–Iwaniec-type spacing estimates, or other joint (ν, m) methods, can do better than the benchmark here is not
decided. No BI theorem is quoted (LIT_CHECK Q6: UNVERIFIED).
(iv) *(Assessment, from BILINDIV §5.5.)* Derivative-based near-curve counts have a second-derivative term ≍ U^{4/3} > U for
f = p/m at N ≍ U², δ ≍ 1/U.

## 10. Computations (scripts `scripts/z55_tdcal_*`, data `data/z55/tdcal/`)

**10.1 Window averages** (§4): `z55_tdcal_window.c`, `window.txt`.

**10.2 TD falsifier on structured prime families (EVIDENCE).** Inputs: `z55_tdcal_inputs.py`. Sums:
`z54_bilindiv_td.c` with H = 32, outputs `td_*.out`, columns as in BILINDIV §6.1. Overall U = ⌊p^{1/4}⌋ ∈ [300, 339],
near 10¹⁰. The rms column is the mean over primes of the per-prime rms_h.

| sample | n | mean \|E1⁺\|/U | mean of per-prime rms_h \|T\|/√\|E1⁺\| | max_h \|T\|/√\|E1⁺\| |
|---|---|---|---|---|
| generic: 3000 consecutive primes after 10¹⁰ | 3000 | 1.539 | 0.994 | 3.19 |
| near-squares below: p = N² − c, c ∈ (2U, 4U] (puts (N, N) in E1; rich (1, −1) line) | 600 | 1.522 | 0.994 | 3.16 |
| near 4th powers p = N⁴ + c (U = N exactly), N = 300..339 | 400 | 1.526 | 0.990 | 2.73 |
| near rational multiples of squares p = (bN² − c)/a, (a, b) ∈ {(1,2),(2,3),(1,3),(3,4),(2,5)} | 500 | 1.514 | 0.996 | 3.04 |
| odd squares (2i+1)², i = 50000..50599 (control) | 600 | 1.522 | 0.999 | 3.68 |

**10.3 Distribution of T(h) (EVIDENCE;** `z55_tdcal_tail.c`, `tail.txt`**).** The table gives P(|T(h)|/√|E1⁺| > t) over
all (n, 1 ≤ h ≤ 32), next to e^{−t²}, the radial tail of a unit-second-moment complex Gaussian. The three structured
prime families (48 000 further pairs) are in `tail.txt`.

| t | generic primes 10¹⁰ (96 000) | e^{−t²} | odd squares, second set (96 000) |
|---|---|---|---|
| 1.0 | 0.3653 | 0.3679 | 0.3690 |
| 2.0 | 0.01842 | 0.01832 | 0.01930 |
| 2.5 | 1.875e−3 | 1.930e−3 | 1.979e−3 |
| 3.0 | 1.146e−4 | 1.234e−4 | 1.458e−4 |
| 3.5 | 0 | 4.8e−6 | 1.04e−5 |

* The empirical second moment of |T|/√|E1⁺| is 0.996 (generic primes) and 1.006 (squares, second set).
* These tails and moments are compatible with the unit-second-moment complex-Gaussian model, i.e. random phases with
  |E1⁺| unit terms. Sampling errors are not calibrated, since windows of consecutive primes overlap and h-values are
  correlated.
* The odd squares show a marginally heavier tail (t = 2: +5 %). This is not significant evidence of square structure.

**10.3′ Exact checks** (`z55_tdcal_check.py`, `check.txt`; 200 consecutive primes after 10⁸, U = 100).
* CERTIFIED for these inputs (exact integer arithmetic), with 0 failures:
  * Lemma S(a): slice count = |E1|;
  * S(b): two-shift form = N₂;
  * S(c): m | p² − D at every strip point;
  * N^{[0]} ≥ N₂.
* EVIDENCE: the mean of Σ_{|τ|≤T}N^{[τ]} is 1.70, 2.76, 5.72, 19.9, 73.8 at T = 0, 1, 4, 16, 64. For T ≥ 4 that is
  ≈ 1.15–1.4·T, the model order and far below the elementary estimate.
* EVIDENCE (NC count): mean 𝒜(δ) = 6.44, 15.4, 30.8 against 2δ|E1⁺| = 6.05, 15.1, 30.3 at δ = 0.02, 0.05, 0.1.

**10.4 Count error vs twisted sums (EVIDENCE;** `td_gen*.out`**).**
* (|E1| − 2U log 4)/√U has population sd 2.79 (10⁸, U = 100, 1500 consecutive primes), 3.31 (10¹⁰, 3000), 2.75
  (10¹², 600) and 2.17 (10¹⁴, 150). In units of √|E1| ≈ 1.66√U that is 1.3–2.0.
* Consecutive primes have overlapping windows at the larger scales, so these sds are rough.
* The *pooled* rms of |T(h)|/√|E1⁺| over all (p, h) is 0.998, 0.998, 1.001, 1.006 at the four scales. The means of the
  per-prime rms are 0.990, 0.994, 0.993, 0.999.
* So the count error is larger than random-phase size, as for the full short-interval mean square (Ivić's log³ factor),
  while T(h) is of random-phase size.

## 11. Collected PROVED statements (Theorem H)

**Theorem H (PROVED).** In the fourth-root range, U ≥ U₀:
1. *(Averages.)* The conclusion N₂ ≤ U^{1−η} holds on average over every window of U^{η+ε} consecutive n, and for all
   but O(X^{(3+η)/4+ε}) primes p ≤ X (Prop A, Cor A′). Pointwise, N₂ ≤ (1 − log 2)U + O(U^{1−3/56+ε}) (Remark A‴,
   relative to Titchmarsh Thm 5.13).
2. *(Identity.)* |E1| is the central slice m ∈ (U², 4U²] of D(p + 2U, 2U) (Lemma S(a)).
3. *(Bands.)* In the natural smooth expansions of §6, smoothed CNT and TS_{N₂} carry only |ν| ≤ U^{1+ε}, and smoothed TD at
   w ≍ W ∈ [U^σ, 4U] only ν ∈ [hU³/(2W), 64hU³/W] (Thm B).
4. *(Benchmark.)* For the smoothed count the per-frequency benchmark is ≍ U, the trivial order (Prop C(i)).
5. *(NC.)* TD(η) ⇒ NC(η) ⇒ N₂ ≪ U^{1−η+ε}. The τ-window bound Σ_{|τ|≤13UU^{−η}}N^{[τ]} ≪ U^{1−η+ε} implies NC(η). The
   elementary τ-window estimate is ≪ U^{1+ε} + TU^{1/2+ε} (Prop D).

## 12. FRONTIER §4 hard screens (best idea: NC / the calibration)

1. **T1 (odd squares).** Everything is an upper-bound statement, silent on positivity by design. Valid at every n:
   Prop A, Lemma S(a) and S(c), Prop D(i)–(iv) (with Lemma A's product-divisibility convention), and Thm B(i)/(iii)
   when no m ∈ (U², 4U²] divides n. Prime-only: S(b), and TS_{N₂}'s formula k = ⌈p/m⌉. EVIDENCE: T(h) at odd squares is
   compatible with the same Gaussian model (§10.3).
2. **8/131.** Numerator-blind (N₄ ≤ N₂); not an ES step.
3. **Tied modulus.** NC is the tie relaxed to tolerance U^{1−η} in w. The tie is not broken; it is bounded from above.
4. **Fixed p.** Prop A and Cor A′ are averages, presented as calibration and not as a fixed-p result. Thm B, Prop C,
   Prop D, Remark A‴ and NC are pointwise in p.

## 13. Verdict

**Narrowed (calibrated), with one weaker sufficient condition.**
* *New sufficient condition:* NC(η), a one-sided near-zero upper bound. TD ⇒ NC ⇒ R2 (PROVED), and NC is weaker in
  form than TD.
* *Small unconditional results:*
  * R2's conclusion on average over windows of length U^{η+ε}, and off ≪ X^{(3+η)/4+ε} primes;
  * the pointwise first-order constant N₂ ≤ 0.307U;
  * free small-w pieces of TD.
  None moves the pointwise power-saving problem.
* *Calibration (PROVED identities and bound computations, with Assessment readings):*
  * the untwisted count is a central slice of the x^{1/4} short-interval divisor problem;
  * natural expansions of TD and of the count/TS_{N₂} have disjoint carrier bands (no implication established);
  * benchmark-class arguments fall short by the factors of Table 7.1.
* *Not excluded:*
  * joint (ν, m) estimates below the benchmark;
  * spectral methods on other transforms;
  * arithmetic (sieve-type) upper bounds for NC at a single p;
  * averaged TD;
  * MIX and TS on their own families.

## 14. Proposed FRONTIER §7 text (do NOT edit FRONTIER here)
Append to §7.1 under the z54 bullets:
> * **How hard is TD? (`Z55_TDCAL.md`, z55; internal; calibration, upper-bound only.)**
>   * Prop A (PROVED): Σ_{X<n≤X+Y}N₂(n, U) ≤ Σ_M τ(M)² over an M-window of length Y + 2U. So the conclusion of R2 holds
>     on average over every window of p^{η/4+ε} consecutive n, and fails for ≪ X^{(3+η)/4+ε} primes p ≤ X; an averaged
>     conclusion needs no TD-type input. Remark A‴ (PROVED rel. Titchmarsh 5.13): N₂ ≤ (1 − log 2 + o(1))U pointwise.
>   * Lemma S (PROVED): |E1| is the central slice (divisors in (U², 4U²]) of D(p + 2U, 2U), the short-interval divisor
>     sum at length x^{1/4}. At primes N₂ = #{(u, w) : u | p + w, u + w | p − w}, and every strip point has m | p² − D,
>     so TD is trivial for w ≤ U^{(1−η)/2}.
>   * Thm B (PROVED): in the natural smooth expansions in θ_m = {−p/m} (m ≍ U²), smoothed CNT and the N₂-strip analogue of
>     TS carry only |ν| ≤ U^{1+ε}, and smoothed TD at w ≍ W only ν ∈ [hU³/2W, 64hU³/W]. These carrier bands are disjoint.
>     The band depends on the expansion, and no implication between the statements is established.
>   * Prop C (PROVED for the count; BILINDIV 4.3 for TD's top piece): in the class "triangle inequality over ν with
>     majorants ≥ c‖c(ν)‖₂", the count is bounded only by ≍ U. Relative to that benchmark, CNT(η) needs U^η, central-slice
>     square root U^{1/2}, and TD(η) h^{1/2}U^{1/2+η}.
>   * Prop D (PROVED): with 𝒜(δ) = #{k : ‖w_k‖ ≤ δ}, 𝒜(δ) ≤ Σχ_δ(w_k) ≤ 𝒜(2δ) and N₂ ≤ 𝒜(δ). So NC(η): 𝒜(U^{−η}) ≪ U^{1−η+ε}
>     suffices, and TD(η) ⇒ NC(η). A sharp-order bound for τ-perturbed tie counts over |τ| ≤ 13U^{1−η} implies NC. The
>     elementary τ-window estimate U^{1+ε} + TU^{1/2+ε} does not reach the model order T, unlike n-windows. N₂² ≤ P(δ),
>     and a pair-correlation bound is one sufficient ℓ² input.
>   * Prop E: the direct completion of m | p + s is orthogonality and exhibits no Kloosterman sum. Kloosterman structure
>     occurs in the (u, B)-CRT form (HYPKLOOST's scoped DFI/BC failures) and in the square sieve (BILINJAC (F3)). No
>     spectral-method exclusion is made.
>   * EVIDENCE: T(h)/√|E1⁺| has tails and second moment compatible with the unit complex-Gaussian model at 10¹⁰
>     (96 000 generic (p, h), plus structured prime families and odd squares). The count error has sd ≈ 2–3·√U.
>   * Missing: a joint (ν, m) estimate below the per-frequency benchmark, or an arithmetic proof of NC at one p.

## 15. Bottom line
In the natural expansion, TD asks how the exact remainders p mod m, m ≍ √p, fall *inside* the window that defines the
strip. The strip count and the twisted sums ask only *whether* they fall in it, and in which classes.
* These expansions have disjoint carrier bands. No implication between TD and a short-interval divisor statement is
  established, in either direction.
* The untwisted relative is exactly a central slice of the short-interval divisor problem at length x^{1/4}. No checked
  source gives a power saving for it.
* Against the per-frequency benchmark TD needs a larger factor than square-root Jutila on that slice. Against the
  whole-sum random model it asks the same as the untwisted count. Numerically T(h) is compatible with random phases.
* Averaging over n gives R2's conclusion for free and so needs no TD.
* What Theorem T's route really needs at one p is NC, an upper bound for near-ties at tolerance U^{1−η}, which is weaker
  in form than TD. The displayed elementary estimates stop short of it by at least U^{η}.
Nothing here touches positivity, and ES remains open.

## 16. Reproduction
All commands are run under `ulimit -v 4000000` (in the same shell), each with the shown `timeout`.
```
cd $REPO; D=data/z55/tdcal; I=/tmp/z55in; mkdir -p $I; ulimit -v 4000000
gcc -O2 -o /tmp/z55win scripts/z55_tdcal_window.c
(timeout 600 /tmp/z55win 100000000 20000 100; timeout 600 /tmp/z55win 1000000000000 2000 1000) > $D/window.txt
timeout 900 uv run --with sympy python scripts/z55_tdcal_inputs.py $I       # gen10 nsq10 n4p10 nrat10 sq10
timeout 900 uv run --with sympy python scripts/z55_tdcal_inputs2.py $I      # gen8 gen12 gen14
timeout 60 uv run python scripts/z55_tdcal_squares.py $I                    # sq10b
gcc -O2 -o /tmp/z54td scripts/z54_bilindiv_td.c -lm; gcc -O2 -o /tmp/z55tail scripts/z55_tdcal_tail.c -lm
for f in gen10 nsq10 n4p10 nrat10 sq10; do timeout 1200 /tmp/z54td 32 < $I/$f.txt > $D/td_$f.out; done   # ~1 min
for e in 8 12 14; do timeout 1500 /tmp/z54td 16 < $I/gen$e.txt > $D/td_gen$e.out; done                  # ~10 min
for f in gen10 sq10 nsq10 nrat10 n4p10 sq10b; do echo "== $f"; timeout 1500 /tmp/z55tail 32 < $I/$f.txt; done > $D/tail.txt
timeout 1500 uv run --with sympy python scripts/z55_tdcal_check.py 100000000 200 > $D/check.txt         # ~5 min
```
(The stored `tail.txt` has slightly longer section headers; the numbers are identical.)

## 17. Review log
**Hostile review 1** (deep-mode subagent; `reviews/z55_tdcal_review1.md`). Verdict **INCORRECT as written** (8 MAJOR,
14 MINOR, 1 NIT).
* *Confirmed.* Prop A identity and (c); Remark A‴ (constant and 3/56); Lemma S(a), S(b) at primes, S(c); Theorem B's
  derivative scale, band and tail estimates; the U^{1/2} central-slice deficit; Prop D's sandwich, tolerance, ΣD^{−1/2}
  bound and Fejér identity; the DFI/BC exponents.
* *Reproduced.* All numerical tables (window, TD rows, tails, sds, exact checks).
* *Fixes applied.*
  1. Band "no-go" claims withdrawn. Thm B is now explicitly about natural expansions, and Remark B2 records that the band
     depends on the expansion. "No implication established" replaces every non-implication claim.
  2. "Averaged TD worthless / free" withdrawn. Only the averaged R2 *conclusion* is claimed; averaged TD is listed as
     not addressed. The FRONTIER §6 entry was dropped.
  3. Thm B and Prop C scoped to smoothed pieces. The W-range is extended to [U^σ, 4U], so together with Lemma S(c) the
     smoothed pieces cover all w, and the sharp boundaries are stated as not covered.
  4. TD ⇒ NC reproved with δ′ = U^{−η+ρ}, H = U^{η−ρ/2}. The sandwich direction is corrected (Fourier bounds give
     𝒜(δ)).
  5. The τ-window bound is now a *stronger* sufficient condition for NC, not an equivalence. "R2 is T = 0" is replaced
     by N₂ ≤ N^{[0]}.
  6. The pair-correlation input is stated as sufficient only, with H = U^{ρ/2}/δ; the MIX comparison is Assessment.
  7. Prop E restricted to the direct completion (orthogonality, then Poisson in s). The general Kuznetsov exclusion is
     withdrawn; BILINJAC (F3)'s Kloosterman sums are noted; 1/37 is attributed to DFI Theorem 2.
  8. §7's "currency" is now a benchmark with an explicit class (as in BILINDIV Prop 4.3). The exponent-pair and BI
     claims are withdrawn or labelled Assessment.
  9. Cor A′ bookkeeping fixed: O(Z^{1/4}) values of U.
  10. Prop A(a) is proved for all Y (case split at U²).
  11. Remark A″ multiplicity is now exact (≤ U₀).
  12. U ≥ 4 is required for the r_m characterization.
  13. Lemma S(c) restricted to X ≤ 16U².
  14. ε < 1 for disjointness; Faà di Bruno wording fixed.
  15. Prop C(i) assumes φ, Φ ≢ 0 and uses "main term ≍ U"; (iv) has a support-overlap assumption and stays
      Assessment.
  16. TS renamed TS_{N₂} and distinguished from BILINJAC's T_Q.
  17. "Same saving" replaced by "allowance above the whole-sum model".
  18. "Not free at any length" restricted to the displayed estimate for 1 ≤ T ≤ U.
  19. T1 screen lists composite-valid and prime-only items; the S(b) counterexample at 10005² is recorded.
  20. Gaussian claims reworded to "compatible with".
  21. Metadata fixed: pooled vs per-prime rms, U range 300–339, generic vs structured samples, [X, X + Y) convention.
  22. Labels split. Theorem H contains PROVED items only, and the Li–Yang wording is corrected.
  23. Reproduction made exact, with input scripts added.
