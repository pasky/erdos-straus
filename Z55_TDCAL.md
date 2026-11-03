# Z55_TDCAL — depth lane TDCAL (wave z55, gap 1): how hard is TD?

ES is OPEN. Nothing here proves or disproves it. This lane is **upper-bound calibration work only** (FRONTIER §7.1,
balanced block / 2-cycles); even full success would say nothing about positivity. Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Results are internal.

Brief: `z52bbriefs/z53_depth.md` (rules), kickoff `z52bbriefs/z55_lanes.md` §TDCAL. Predecessors: `Z54_BILINDIV.md`
(Thm T, TD(η), Prop 4.3, Remark 4.1), `Z54_BILINJAC.md` (Thm R, TS, Prop R′, §5 Jutila comparison), `Z53_HYP2CYCLE.md`
(MIX), `Z53_SQSIEVE.md`. Scripts `scripts/z55_tdcal_*`, data `data/z55/tdcal/` (≈ 0.3 MB). Literature:
`data/z55/tdcal/LIT_CHECK.md`. Checkpoint 1: commit 06ccc2ba.

## 0. Summary and verdict

**Verdict: narrowed (calibrated), with one weaker sufficient condition.** No power saving for the balanced block is
proved, and none of TD, TS, MIX is proved or refuted. What is new:

1. **Averaging over n is free (Prop A, PROVED).** For every window of Y consecutive integers,
   Σ_n N₂(n, U) ≤ Σ_{M} τ(M)² over an M-window of length Y + 2U. So R2 holds on average over any p^{η/4+ε} consecutive
   n, and fails for at most O(X^{(3+η)/4+ε}) primes p ≤ X. Every "on average over p" form of TD or R2 is therefore
   worthless for the balanced block; the whole difficulty is a single n.
2. **Band localization (Theorem B, PROVED).** Expand everything in the remainder phases θ_m = {−p/m}, m ≍ U² (one strip
   point per m). The strip count and the twisted sums TS use only frequencies |ν| ≤ U^{1+ε}. The TD sums at w ≍ W use only
   ν ∈ [hU³/(2W), 64hU³/W] ⊂ [hU²/8, ∞). These bands are disjoint, up to O(U^{−A}). The count and TS are window-resolution
   statements about p mod m; TD is a *unit-resolution* statement about the remainders r_m themselves.
3. **Calibration ladder (Prop C, PROVED as computations of bound expressions).** In the common currency "per-frequency
   square root" (the strength of the exponent-pair conjecture used frequency by frequency), each target needs a further
   *joint* saving:
   * the central-slice count CNT(η) needs U^η;
   * square-root cancellation in the central slice (the slice analogue of Jutila's conjecture) needs U^{1/2};
   * TD(η) at the top piece needs h^{1/2}U^{1/2+η}.
   The untwisted count |E1| is *exactly* the central slice (divisors in (U², 4U²] ≍ √x) of the short-interval divisor
   problem D(x+2U) − D(x) at length ≍ x^{1/4} (Lemma S(a)). That problem is open pointwise; the best checked pointwise
   input needs length ≥ x^{0.3145}.
4. **The weakest input on the Theorem-T route is one-sided (Prop D, PROVED).** Theorem T only ever uses the
   near-integer count 𝒜(δ) = #{k : ‖w_k‖ ≤ δ}. This is sandwiched: 𝒜(δ) ≤ Σχ_δ(w_k) ≤ 𝒜(2δ). So
   NC(η): 𝒜(U^{−η}) ≪ U^{1−η+ε} suffices, and TD(η) ⇒ NC(η) ⇒ N₂ ≪ U^{1−η+ε}. NC is an *upper bound* for an
   approximate-tie count, a sum over |τ| ≲ U^{1−η} of τ-perturbed 2-cycle counts at the same p. Contrast:
   * windows in the target integer n reach sharp order elementarily at length ≳ U (Prop A);
   * windows in the tie tolerance τ at fixed p do not, at any length: the elementary bound is
     ≪ U^{1+ε} + T·U^{1/2+ε} against an expected ≍ T (Prop D(iii)).
   Frequency averaging in ℓ² is the pair correlation of {w_k} (second order), and N₂² ≤ P(δ) for every δ.
5. **Level averaging / Kuznetsov (Prop E).**
   * In the (k, m) and (m, s) parametrizations no Kloosterman sum arises: the complete sums are Ramanujan-type and
     collapse to 1[m | p + s] (PROVED identity).
   * Kloosterman structure appears only in the (u, B)-CRT form, i.e. the DFI/HYPKLOOST setting already closed there for
     the displayed bounds.
   * Per-frequency spacing bounds (Bombieri–Iwaniec type) cannot supply the joint saving of item 3 (Assessment).
6. **EVIDENCE.**
   * T(h)/√|E1⁺| is complex-Gaussian (Rayleigh tail) to within sampling error at 10¹⁰, over 96 000 (p, h) pairs and four
     special prime shapes (no falsifier).
   * The count error carries extra "arithmetic" variance: its sd is 2.2–3.3·√U, against exactly 1·√|E1⁺| for T(h).

**Answer to the kickoff questions (Assessment, built on the PROVED items).**
1. *Does TD imply a pointwise short-interval divisor statement?*
   * No band-limited reduction can link TD to the count, TS or Jutila-type statements: they use disjoint frequency bands
     (Thm B).
   * A logical non-implication between two possibly-true statements cannot be proved, so this is a statement about
     methods.
   * TD is not weaker than the count in any tested currency. It is a unit-resolution, self-dual problem and needs more
     joint cancellation (per frequency) than square-root Jutila on the central slice.
2. *Partial results.* Averages over n are free and therefore empty (Prop A); averages over U are reweightings (Prop A″);
   smoothing does not move the bands. The missing pointwise piece is NC(η) at one p, a sharp-order upper bound for the
   approximate-tie count at tolerance U^{1−η}.
3. *Beyond Voronoi at one p.*
   * h-averaging is a Fourier proof of NC, and its ℓ² form is a second-order pair correlation (Prop D).
   * k-averaging produces no Kloosterman sums for spectral methods (Prop E).
   * Nothing here beats Voronoi at a single p.

## 1. Notation (as in Z54_BILINDIV)

* p is an odd prime (n is a general positive integer where stated) and U ≥ 2 an integer. The fourth-root range is
  c₁p^{1/4} ≤ U ≤ c₂p^{1/4}, with 16U³ ≤ p. Implied constants may depend on c₁, c₂ and the fixed test functions.
* N₂(n, U) := #{{u, B} ⊂ (U, 2U], u ≠ B : uB | n + u + B}. This is the product-divisibility definition, valid for every
  n; at primes it equals the 2-cycle count.
* E1 = E1(p, U) := {(k, m) ∈ ℕ² : p + 2U < km ≤ p + 4U, U² < m ≤ 4U²}. Put s := km − p ∈ (2U, 4U] and D := s² − 4m.
  Then E1⁺ := {D ≥ 1}, w := √D and T(h) := Σ_{E1⁺} e(hw).
* For m ∈ ℕ with m ∤ p: r_m := (−p mod m) ∈ [1, m) and θ_m := r_m/m = {−p/m}.
  * Since m ≤ 4U² < p and 4U < U² < m, each m ∈ (U², 4U²] carries at most one strip point.
  * That point exists iff r_m ∈ (2U, 4U], and then s = r_m and k = ⌈p/m⌉.
  * Hence |E1| = #{m ∈ (U², 4U²] : r_m ∈ (2U, 4U]}.
* TD(η), BILINDIV: |T(h)| ≤ C₀U^{1−η} for 1 ≤ h ≤ U^η, uniformly for primes p and U in the fourth-root range.
  Theorem T (BILINDIV, PROVED): TD(η) ⇒ N₂ ≪ U^{1−η+ε}.
* CNT(η) (untwisted count): |E1(p, U)| = 2U log 4 + O(U^{1−η}) uniformly in the fourth-root range. OPEN.
* Δ(x) := Σ_{n≤x} d(n) − x log x − (2γ − 1)x, and D(x, y) := Σ_{x<n≤x+y} d(n).

## 2. Statements attacked

* **(Q1) Calibration.** The exact relation of TD, CNT, TS and Jutila's conjecture
  Δ(x+y) − Δ(x) ≪_ε x^ε√y (x^ε ≤ y ≤ x^{1/2−ε}; Ivić, JTNB 21 (2009), (1.13), a CONJECTURE, verified in LIT_CHECK)
  at y ≍ x^{1/4}. Targets: identities, band localization, per-frequency deficits.
* **(Q2) Partial results.** R2 or TD on average over n, over U, or smoothed, and the exact missing pointwise piece.
* **(Q3) Beyond Voronoi at one p.** Frequency averaging in TD, level averaging, Kuznetsov, spacing methods.

## 3. Why this is not already closed

* BILINDIV §4.2 records "TD vs MIX: neither shown to imply the other" and gives a stationary-phase *Assessment* of a
  double dual. It proves no comparison with the count or with Jutila's conjecture, and has no band statement.
* BILINJAC §5 calls square-root TS "a twisted analogue of Jutila's conjecture" and explicitly proves no implication.
  Its §5.3 computes exponent-pair bound expressions for TS only.
* No memo treats averages over n or over U for R2/TD. `git grep` on "average over p" finds only unrelated B6 items.
* No memo isolates the one-sided near-integer count (NC) as the actual input of Theorem T.

## 4. Averaging over n and over U is free (Prop A)

**Proposition A (PROVED).** For all integers X ≥ 0, Y ≥ 1 and U ≥ 2,

  Σ_{X<n≤X+Y} N₂(n, U) = #{(u, B, M) : U < u < B ≤ 2U, uB | M, X < M − u − B ≤ X + Y}
                       ≤ Σ_{X+2U < M ≤ X+Y+4U} τ(M)².

Consequently, for X ≍ U⁴ and every ε > 0:
* (a) the mean of N₂(n, U) over any Y consecutive integers n ∈ (X, X + Y] is ≪_ε (1 + U/Y)U^ε;
* (b) for every η ∈ (0, 1), at most O_ε(U^{η+ε}) integers in any window of U consecutive integers have
  N₂(n, U) > U^{1−η};
* (c) more precisely, Σ_{X<n≤X+Y} N₂(n, U) = Y·Σ_{U<u<B≤2U} 1/(uB) + O(U²). So for Y ≥ U^{2+ε} the window mean is
  ½(log 2)² + o(1).

*Proof.*
* The map (n, {u < B}) ↦ (u, B, M := n + u + B) is injective and lands in the displayed set. Conversely each such
  (u, B, M) gives n := M − u − B with uB | n + u + B. Since 2U < u + B ≤ 4U, M ∈ (X + 2U, X + Y + 4U].
* For fixed M, the pairs with uB | M have u | M and B | M, so there are at most τ(M)² of them.
* (a) follows from τ(M) ≪_ε M^{ε/8} with M ≍ U⁴, and (b) from (a) with Y = U by Markov's inequality.
* (c): for each pair, the M ≡ 0 (mod uB) in an interval of length Y number Y/(uB) + O(1). There are < U² pairs, and
  Σ_{U<u<B≤2U} 1/(uB) = ½[(Σ1/u)² − Σ1/u²] = ½(log 2)² + O(1/U). ∎

**Corollary A′ (PROVED; exceptional primes).** Fix η ∈ (0, 1) and ε > 0, and put U_p := ⌊p^{1/4}⌋. Then
#{p ≤ X prime : N₂(p, U_p) > U_p^{1−η}} ≪_{η,ε} X^{(3+η)/4+ε}.
*Proof.*
* Split (X^{1/2}, X] into dyadic ranges (Z, 2Z]. Inside each, U_p takes O(Z^{3/4}) distinct values.
* Each value U is taken on an interval of n of length ≍ U³, which we cover by O(U²) windows of length U.
* Apply Prop A(b) to every window: the range contributes O(Z^{3/4}·U^{2}·U^{η+ε}) = O(Z^{(3+η)/4+ε}) exceptions.
* Primes p ≤ X^{1/2} number ≤ X^{1/2}. Sum over the dyadic ranges. ∎

**Remark A″ (averaging over U is a reweighting; PROVED identity).** For a prime p and U₀ ≥ 2,
Σ_{U₀≤U<2U₀} N₂(p, U) = Σ_{2-cycles {u<B}} #{U ∈ [U₀, 2U₀) : U < u, B ≤ 2U}.
* Each cycle counted lies in (U₀, 4U₀)² with B < 2u.
* Each is counted at most min(u, ⌊(u − B/2)⌋ + 1) ≤ U₀ + 1 times.
So the U-average is a weighted count of the same objects in a box of twice the size; it cannot yield a pointwise saving
that the larger box does not already have. (Assessment: "TD for a positive-density set of U" has the same status.)

*Reading (Assessment).*
* R2 is elementary on average over any window of U^{η+ε} = p^{η/4+ε} consecutive n.
* It can fail for at most a U^{η−1+ε} proportion of every window of length U, and for at most X^{(3+η)/4+ε} primes
  p ≤ X.
* Any argument that proves R2 or TD "on average over p", with averaging length ≥ p^{δ}, gives nothing for the
  balanced block. Averaged TD is therefore not proved here: Prop A makes it moot.
* The missing piece is to exclude a sparse exceptional set at a single n. Prop D makes this precise.

**EVIDENCE (`scripts/z55_tdcal_window.c`, `data/z55/tdcal/window.txt`).**
* n ∈ (10⁸, 10⁸ + 20000], U = 100: ΣN₂ = 4662, mean 0.233, max 4. The (u, B, M) count with the window's M-range is 4707.
* n ∈ [10¹², 10¹² + 2000), U = 1000: ΣN₂ = 461, mean 0.231, max 3; histogram 0:1599, 1:347, 2:48, 3:6.
* These are means over all integers, not only primes; ½(log 2)² = 0.2402.

## 5. Structural forms (Lemma S)

**Lemma S (PROVED).** Let p be prime, U ≥ 2 and 16U³ ≤ p.

**(a) Central-slice identity.** Put x := p + 2U and y := 2U. Then
  |E1| = #{(m, M) : x < M ≤ x + y, m | M, U² < m ≤ 4U²} = 2U log 4 + E(p, U), with
  E(p, U) = Σ_{U²<m≤4U²} [ψ(x/m) − ψ((x + y)/m)] + O(1/U), where ψ(t) = t − ⌊t⌋ − ½.
Since D(x, y) = #{(m, M) : x < M ≤ x + y, m | M}, |E1| is the part of the short-interval divisor sum D(x, y), at length
y ≍ x^{1/4}, whose divisor lies in (U², 4U²] — a dyadic-type slice at m ≍ √x (U² ≍ √p up to c₁², c₂²).
*Proof.* By §1, each m ∈ (U², 4U²] has ⌊(x+y)/m⌋ − ⌊x/m⌋ ∈ {0, 1} multiples in (x, x+y], and its unique strip point is
(⌈p/m⌉, m) exactly when that count is 1. Then sum ⌊t⌋ = t − ψ(t) − ½ over the 3U² values of m, and use
Σ_{U²<m≤4U²} 2U/m = 2U log 4 + O(1/U). ∎

**(b) Two-shift form.** N₂(p, U) = #{(u, w) ∈ ℕ² : U < u < u + w ≤ 2U, u | p + w, u + w | p − w}.
*Proof.*
* Put B = u + w.
* Then u | p + B ⟺ u | p + w, and B | p + u ⟺ B | p + B − w ⟺ B | p − w.
* At a prime p > 2U, gcd(u, B) | p forces gcd(u, B) = 1, so the two divisibilities are equivalent to uB | p + u + B. ∎

**(c) Discriminant form.** If (s, m) ∈ E1 then m | p² − D. Consequently, for every X ≥ 1,
  #{(k, m) ∈ E1 : 1 ≤ D ≤ X} ≤ Σ_{1≤D≤X} τ(p² − D) ≪_ε X p^ε,
and in particular the part of T(h) with w ≤ U^{(1−η)/2} is ≪_ε U^{1−η+ε} for every h (TD holds trivially there).
*Proof.*
* m | p + s gives p ≡ −s and hence p² ≡ s² = D + 4m ≡ D (mod m).
* For fixed D, s = √(4m + D) is determined by m, so (s, m) ↦ m is injective on {D fixed}.
* Finally 0 < p² − D because D ≤ 16U² < p². ∎
On a 2-cycle (D = w², w = B − u), (c) reads uB | (p − w)(p + w), matching (b). The free range in (c) for TD itself
(w ≤ U^{(1−η)/2}) is smaller than BILINDIV Remark 4.1's free range for N₂ (w ≤ U^{1−η}), which counts only 2-cycles.

## 6. Theorem B: band localization of CNT, TS and TD

*Setting.*
* Fix φ ∈ C_c^∞((1, 4)), Φ ∈ C_c^∞((2, 4)) and Ψ ∈ C_c^∞((½, 2)), with values in [0, 1].
* Let W ∈ [U^{1/2}, 4U] and h ∈ [1, U].
* Define the smoothed count and the smoothed W-piece of T:
  C(p, U) := Σ_m φ(m/U²)Φ(r_m/U),
  T_W(h) := Σ_m φ(m/U²)Φ(r_m/U)Ψ(w_m/W)e(hw_m),  with w_m := √(r_m² − 4m) (the term is 0 if r_m² ≤ 4m).
* By §1 these are smooth versions of |E1| and of the w ≍ W part of T(h). A smooth dyadic partition in w recovers T(h) up
  to the free range of Lemma S(c), as in BILINDIV Remark 4.1 (smooth form).
* *TS in this strip.* T_Q(a, b) := Σ_m φ(m/U²)Φ(r_m/U)e((a k_m + b m)/Q), with k_m = ⌈p/m⌉ the level and Q ≥ 1. This is
  the N₂-strip analogue of BILINJAC's T_Q: there (C, k) = (level, product), with BILINJAC's own normalization.

*Expansion (PROVED identity, as in BILINDIV §4.3).*
* For each m define G_m(θ) := φ(m/U²)Φ(mθ/U)Ψ(W_m(θ)/W)e(hW_m(θ)) on [0, 1), where W_m(θ) := √(m²θ² − 4m).
* Its support lies in (2U/m, 4U/m) ⊂ (0, 1), so it extends to a smooth 1-periodic function.
* With ĉ_m(ν) := ∫₀¹ G_m(θ)e(−νθ)dθ and e(νθ_m) = e(−νp/m) (since r_m ≡ −p mod m),
  T_W(h) = Σ_{ν∈ℤ} Σ_m ĉ_m(ν) e(−νp/m),  and likewise C(p, U) = Σ_ν Σ_m ĉ⁰_m(ν)e(−νp/m),
  where ĉ⁰_m(ν) = φ(m/U²)(U/m)Φ̂(νU/m) exactly.

**Theorem B (PROVED).** Fix the test functions, ε > 0 and A > 0. For U ≥ U₀, every W ∈ [U^{1/2}, 4U], every
1 ≤ h ≤ U and every Q ≥ 1, (a, b) ∈ ℤ²:
(i) C(p, U) = Σ_{|ν|≤U^{1+ε}} Σ_m ĉ⁰_m(ν)e(−νp/m) + O(U^{−A});
(ii) T_Q(a, b) = Σ_{|ν|≤U^{1+ε}} Σ_m κ_m ĉ⁰_m(ν)e(−νp/m) + O(U^{−A}), where κ_m := e((a⌈p/m⌉ + bm)/Q) depends on m only;
(iii) with λ_W := hU³/W, T_W(h) = Σ_{λ_W/2 ≤ ν ≤ 64λ_W} Σ_m ĉ_m(ν)e(−νp/m) + O(U^{−A}).
Since λ_W/2 ≥ hU²/8 > U^{1+ε} for U ≥ U₀, the bands in (i)–(ii) and (iii) are disjoint.

*Proof.*
(i) |Φ̂(ξ)| ≪_A (1 + |ξ|)^{−A}, and |ν|U/m ≥ |ν|/(4U) for m ≤ 4U². So
Σ_{|ν|>U^{1+ε}}Σ_m|ĉ⁰_m(ν)| ≪ Σ_m (U/m) Σ_{|ν|>U^{1+ε}} (|ν|/4U)^{−A′} ≪ U·U^{(1+ε)(1−A′)}U^{A′}, and this is O(U^{−A}) for A′
large.

(ii) For m ∈ (U², 4U²] we have m ∤ p (as m < p), so p + r_m = m⌈p/m⌉ and k_m = ⌈p/m⌉ is a function of m alone. Hence
T_Q(a, b) = Σ_m κ_m G⁰_m(θ_m) with G⁰_m(θ) = φ(m/U²)Φ(mθ/U). Its coefficients are κ_mĉ⁰_m(ν) with |κ_m| = 1, and the
tail estimate of (i) applies verbatim. The same holds for *any* coefficients κ_m with |κ_m| ≤ 1, e.g. a sharp cutoff in m
(equivalently in the level ⌈p/m⌉, as in BILINJAC's ω). Only the cutoff in s must be smooth: a sharp window in s has
Fourier coefficients decaying like 1/|ν|, and the sharp counts are handled by smooth upper/lower majorants.

(iii) *Derivative bounds.* On the support write s = mθ ∈ (2U, 4U), m ∈ (U², 4U²) and W_m ∈ (W/2, 2W).
* Let g(s) := (s² − 4m)^{1/2}. Faà di Bruno gives g^{(j)}(s) = Σ_{⌈j/2⌉≤i≤j} c_{j,i}s^{2i−j}(s² − 4m)^{1/2−i}.
* Each term is ≪ W(U/W)^{2i}U^{−j}, which is largest at i = j (because U/W ≥ 1/4). So g^{(j)} ≪_j U^jW^{1−2j}.
* Hence W_m^{(j)}(θ) = m^jg^{(j)}(mθ) ≪_j Wρ^{−j}, with ρ := W²/U³.
* For the amplitude: (d/dθ)^jΦ(mθ/U) ≪ (m/U)^j ≤ (4U)^j ≤ (64/ρ)^j, since ρ ≤ 16/U. By Faà di Bruno and the bound on
  W_m^{(j)}, (d/dθ)^jΨ(W_m/W) ≪_j ρ^{−j}. So the amplitude a_m(θ) satisfies a_m^{(j)} ≪_j ρ^{−j}.

*First derivative of the phase.* Put F(θ) := hW_m(θ) − νθ. Then W_m′ = m²θ/W_m = ms/W_m, so on the support
hW_m′ ∈ (hU²·2U/(2W), h·4U²·4U/(W/2)) = (λ_W, 32λ_W). Hence, with Λ := max(|ν|, λ_W):
* if ν < λ_W/2 (including ν ≤ 0), then F′ ≥ λ_W − ν ≥ Λ/2;
* if ν > 64λ_W, then −F′ ≥ ν − 32λ_W ≥ Λ/2.
For j ≥ 2, F^{(j)} = hW_m^{(j)} ≪_j hWρ^{−j} = λ_Wρ^{1−j} ≤ Λρ^{1−j}.

*Non-stationary phase.*
* Let L_F g := (g/(2πiF′))′. Repeated integration by parts gives ∫a_m e(F) = (−1)^A∫(L_F^A a_m)e(F).
* By induction on A, with |F′| ≥ Λ/2, F^{(j)} ≪ Λρ^{1−j} and a^{(j)} ≪ ρ^{−j}, each application of L_F costs a factor
  ≪ (Λρ)^{−1} at every derivative order. So (L_F^A a_m)^{(j)} ≪_{A,j} (Λρ)^{−A}ρ^{−j}.
* Hence |ĉ_m(ν)| ≪_A (Λρ)^{−A} (the support has length ≤ 1).
* Here λ_Wρ = hW ≥ U^{1/2}. Summing over ≤ 4U² values of m and over ν outside [λ_W/2, 64λ_W] (for |ν| > 64λ_W use
  (|ν|ρ)^{−A}, whose ν-sum is ≪ ρ^{−1}(hW)^{1−A} with ρ^{−1} ≤ U³) gives O(U^{5}(hW)^{1−A} + U^{6}(hW)^{−A}).
  This is O(U^{−A′}) once A is large.
* Disjointness: λ_W/2 = hU³/(2W) ≥ hU²/8. ∎

**Corollary B1 (PROVED, reading of the bands).**
* C and T_Q depend on the remainder sequence (θ_m) only through its Fourier modes |ν| ≤ U^{1+ε}. That is, through the
  distribution of θ_m at resolution ≍ U^{−1−ε}, which is the scale of the window (2U/m, 4U/m] of width ≍ 1/U.
* T_W(h) depends only on modes ν ≍ hU³/W ≥ hU²/8, i.e. on θ_m at resolution ≤ 8/(hU²). In terms of the integer
  r_m = mθ_m (m ≍ U²) that is resolution O(1/h): the exact remainder.
* The two expansions share the same exponential sums S(ν; c) = Σ_m c_m e(−νp/m) but on disjoint sets of ν.

*Reading (Assessment).*
* TD is not a twisted *count*. It asks how the exact remainders r_m distribute *inside* the window.
* CNT and TS ask how many r_m fall in the window, and in which classes mod Q.
* Any reduction that passes through the remainder spectrum (θ-expansion, Poisson in m, Voronoi) keeps the bands apart,
  so it cannot turn a bound for one into a bound for the other.
* A logical non-implication between two statements that may both be true cannot be proved; this is the method-level
  statement.
* MIX (HYP2CYCLE) lives on a different family altogether: the remainders p mod u at moduli u ≍ p^{1/4}, at second order.

## 7. Proposition C: the per-frequency calibration ladder

**Currency.** After Theorem B every target is Σ_ν Σ_m c_m(ν)e(−νp/m) over a band of ν.
* A *per-frequency bound* bounds each inner m-sum by some β_ν and then sums β_ν over the band (triangle inequality in
  ν).
* *Per-frequency square root* means β_ν = ‖c(ν)‖₂ := (Σ_m |c_m(ν)|²)^{1/2}, the random-phase size of the m-sum.
* This is what the exponent-pair conjecture (0, ½) delivers frequency by frequency, up to U^ε. Compare BILINJAC §5.3:
  the bound expression V^{κ+2λ} equals V at (0, ½).

**Proposition C (PROVED as computations of the bound expressions; fourth-root range, U ≥ U₀).**
(i) *Count.* For the smoothed count, Σ_{1≤|ν|≤U^{1+ε}} ‖ĉ⁰(ν)‖₂ ≍ U, with both inequalities.
* So per-frequency square root gives C − main term ≪ U, the trivial order, since C ≍ U.
* CNT(η) needs Σ_ν β_ν ≤ U^{1−η}: a further *joint* saving U^η over the band.
(ii) *Central-slice square root.* The slice analogue of Jutila's conjecture, C − main ≪ U^{1/2+ε} (y = 2U, so √y ≍ U^{1/2}),
needs a joint saving U^{1/2}.
(iii) *TD, top piece* (BILINDIV Prop 4.3, PROVED there, for W ≍ U with its supports). Per-frequency square root gives
Σ_{|ν|≥hU}‖c_ν‖₂ ≫ h^{1/2}U^{3/2}. TD(η) needs U^{1−η}, a joint saving h^{1/2}U^{1/2+η}.
(iv) *TD, piece W* (Assessment; computed by the same Parseval/second-derivative argument, constants not tracked). The
per-frequency square-root total is ≍ h^{1/2}W^{1/2}U against a target U^{1−η}, a joint saving h^{1/2}W^{1/2}U^η. The
inputs are:
* |ĉ_m(ν)| ≪ (hU⁶/W³)^{−1/2}, from |hW_m″| = 4hm³/W_m³;
* Σ_ν|ĉ_m(ν)|² ≍ W²/U³ per contributing m.

*Proof of (i).*
* *Upper bound.* ‖ĉ⁰(ν)‖₂² = Σ_m φ(m/U²)²(U/m)²|Φ̂(νU/m)|² ≪_A U²·U^{−2}(1 + |ν|/(4U))^{−2A}. So
  Σ_ν‖ĉ⁰(ν)‖₂ ≪ Σ_ν(1 + |ν|/4U)^{−A} ≪ U.
* *Lower bound.* Φ̂(0) = ∫Φ > 0 and Φ̂ is continuous, so |Φ̂(ξ)| ≥ Φ̂(0)/2 for |ξ| ≤ ξ₀. For 1 ≤ |ν| ≤ ξ₀U and
  m ≥ U², |νU/m| ≤ ξ₀. Hence ‖ĉ⁰(ν)‖₂² ≥ (Φ̂(0)/2)²Σ_m φ(m/U²)²(U/m)² ≥ c > 0, using φ ≢ 0 on (1, 4).
* Summing over 1 ≤ |ν| ≤ ξ₀U gives ≫ U. ∎
(ii) and (iii) are restatements (the target sizes; BILINDIV Prop 4.3).

**Table 7.1 (exponents in U; the trivial size of every target is U).**

| target | band (Thm B) | per-freq. square root gives | target size | joint saving needed beyond per-freq. √ |
|---|---|---|---|---|
| CNT(η) (untwisted central slice) | \|ν\| ≤ U^{1+ε} | U (trivial) | U^{1−η} | U^{η} |
| central-slice square root (Jutila-type, y ≍ x^{1/4}) | same | U | U^{1/2} | U^{1/2} |
| TS(δ) (BILINJAC, twisted low band) | same, κ-twisted | U (BILINJAC §5.3: V^{κ+2λ} = V) | U^{1−δ} | U^{δ} |
| TD(η), top piece W ≍ U | ν ≍ hU² | h^{1/2}U^{3/2} | U^{1−η} | h^{1/2}U^{1/2+η} |
| TD, square root | same | h^{1/2}U^{3/2} | U^{1/2} | h^{1/2}U |
| TD(η), piece W (Assessment) | ν ≍ hU³/W | h^{1/2}W^{1/2}U | U^{1−η} | h^{1/2}W^{1/2}U^{η} |

*Reading (Assessment).*
* In this currency, TD(η) for any η > 0 asks for more joint cancellation than square-root Jutila on the central slice
  (U^{1/2+η} > U^{1/2}).
* Measured instead against the random model of the whole double sum, every target in the table needs the same thing:
  a power saving U^{1/2−η} above joint square root.
* So "TD is harder than Jutila" holds only in the per-frequency currency. This is the currency in which the known
  tools (exponent pairs, B-process, per-frequency spacing) work.
* All targets are beyond the exponent-pair conjecture used frequency by frequency (PROVED for the bound expressions).
  None is reachable by known pointwise short-interval results: the checked best pointwise exponent for D(x, y) is
  y ≥ x^{θ*+ε}, θ* = 0.31448… (Li–Yang 2023, Thm 1.2, VERIFIED-PRIMARY), against y ≍ x^{1/4} here.

## 8. Proposition D: what Theorem T actually uses — the one-sided near-integer count

For 0 < δ ≤ 1/4 put 𝒜(δ) := #{k ∈ E1⁺ : ‖w_k‖ ≤ δ}, where ‖·‖ is the distance to ℤ, and
P(δ) := #{(k, k′) ∈ (E1⁺)² : ‖w_k − w_{k′}‖ ≤ δ}.

**Proposition D (PROVED).**
(i) *Sandwich.* With χ_δ as in BILINDIV Thm T (ψ supported in (−2, 2), 0 ≤ ψ ≤ 1, ψ = 1 on [−1, 1]):
  𝒜(δ) ≤ Σ_{k∈E1⁺} χ_δ(w_k) ≤ 𝒜(2δ).
* Theorem T bounds N₂ by the middle term, and evaluates it by Fourier analysis. Any bound for T(h) that is fed into
  Theorem T is therefore a means of bounding 𝒜(2δ).
* Define **NC(η)**: 𝒜(U^{−η}) ≪_ε U^{1−η+ε} for primes p and U in the fourth-root range. Then
  TD(η) ⇒ NC(η) ⇒ N₂ ≪ U^{1−η+ε}.
(ii) *Approximate ties.* 𝒜(δ) ≤ #{((s, m), j, τ) : (s, m) ∈ E1⁺, j ∈ ℕ, τ ∈ ℤ, |τ| ≤ 13Uδ, s² − 4m − j² = τ}. For
fixed τ, the summand #{((s, m), j) : s² − 4m − j² = τ} =: N^{[τ]}(p, U) is the "τ-perturbed tie count":
* for τ = 0 it is Lemma A's tie (D a square), so N₂ ≤ N^{[0]};
* for τ ≠ 0 it counts divisors m of p + s within |τ|/4 of the product ((s − j)/2)((s + j)/2).
(iii) *Window bounds in τ: the elementary bound never reaches sharp order.* For every T ≥ 0,
  Σ_{|τ|≤T} N^{[τ]}(p, U) = Σ_{(s,m)∈E1⁺} #{j ∈ ℕ : |D − j²| ≤ T} ≤ |E1| + 2T·Σ_{(s,m)∈E1⁺} D^{−1/2}
                        ≪_ε U^{1+ε} + T·U^{1/2+ε}.
* In the random model (D spread over [1, 16U²] among ≍ U points) the left side is ≍ T for 1 ≤ T ≤ U (Assessment).
* At T = 13U^{1−η}, NC(η) asks for U^{1−η+ε}; the elementary bound is ≫ U^{1+ε}.
* Contrast Prop A: in the shift n the elementary bound (Y + 2U)U^ε is of sharp order as soon as Y ≥ U.
(iv) *Pair correlation.* N₂² ≤ P(δ) for every δ > 0. With the Fejér kernel F_H(x) = Σ_{|h|<H}(1 − |h|/H)e(hx) ≥ 0,
  Σ_{|h|<H}(1 − |h|/H)|T(h)|² = Σ_{k,k′}F_H(w_k − w_{k′})   (the h = 0 term is |E1⁺|²).
* So an ℓ²-in-h input is a statement about the pair correlation of {w_k} mod 1 at scale 1/H.
* Theorem T with δ ≍ U^{−η} needs Σ_{1≤h≤H}|T(h)| ≪ HU^{1−η} with H ≍ U^{η}. Via Cauchy–Schwarz and the weights
  (1 − |h|/2H) ≥ ½ on |h| ≤ H, that needs Σ_{k,k′}F_{2H}(w_k − w_{k′}) = |E1⁺|² + O(HU^{2−2η}).
* Since |E1⁺|² ≍ U² (EVIDENCE), this is a pair-correlation asymptotic with relative error U^{−η} — a power-saving
  *second-order* statement, the same order as MIX.

*Proof.*
(i) For δ ≤ 1/4 at most one translate ψ((x + j)/δ) is nonzero at any x, and it is ≤ 1 and supported in
‖x‖ < 2δ. So χ_δ ≤ 1[‖x‖ < 2δ]. Also χ_δ(x) = 1 if ‖x‖ ≤ δ. The chain then follows from Theorem T's majorant (Lemma A:
2-cycle levels have w ∈ ℤ) and its Fourier evaluation; for TD ⇒ NC use the BILINDIV Corollary T computation with
δ := U^{−η}.
(ii) Let ‖w‖ ≤ δ with nearest integer j ≥ 1; j ≤ w + 1 ≤ 4U + 1. Then |D − j²| = |w − j|(w + j) ≤ δ(2w + 1) ≤ 13Uδ,
since w ≤ 4U and U ≥ 2. The map k ↦ ((s, m), j, D − j²) is injective.
(iii) The equality is the definition (τ = D − j²). For fixed (s, m), the j ≥ 1 with |D − j²| ≤ T lie in
[√(max(D − T, 0)), √(D + T)], an interval of length ≤ 2T/√D: if D ≥ T it is 2T/(√(D+T) + √(D−T)) ≤ 2T/√D, and if
D < T it is ≤ √(2T) ≤ 2T/√D. So there are ≤ 1 + 2T/√D of them. For Σ D^{−1/2}, split E1⁺ dyadically by D ∈ (X, 2X]:
by Lemma S(c) such a piece has ≪ min(XU^ε, |E1|) ≪ min(X, U)U^{ε} points, and contributes ≪ min(X, U)U^εX^{−1/2}.
Summing over dyadic X ≤ 16U² gives ≪ U^{1/2+ε} log U. Finally |E1| ≪ U^{1+ε}.
(iv) A 2-cycle k has w_k ∈ ℤ, so every ordered pair of 2-cycle levels lies in P(0) ⊂ P(δ). The Fejér identity is the
expansion of |Σ_k e(hw_k)|². ∎

*Reading (Assessment).*
* Theorem T converts R2 into NC — a sharp-order *upper bound* at tolerance U^{1−η} in the perturbation τ, at a fixed p.
* Averaging the *target integer* n is free once the window has length ≳ U (Prop A). Averaging the *tie tolerance* τ at
  fixed n is not free at any length (Prop D(iii)): it moves the divisor constraint, not the integer.
* So TD/NC sit inside the non-elementary regime. R2 itself is the extreme case T = 0.
* An upper bound is enough for NC, so sieve-type upper bounds are not excluded. But any such bound must see the
  near-square condition at a single p. The free bounds (divisor counts, Lemma S(c)) lose the s ↔ m link and give only
  ≍ U.
* NC is formally weaker than TD: one-sided, only near 0, and ε-lossy. Whether it is easier is open.

## 9. Proposition E: level averaging, Kuznetsov, spacing methods

**Proposition E (PROVED identities; Assessment readings).**
(i) *No Kloosterman sums in the strip forms.*
* Detecting m | p + s additively gives (1/m)Σ_{a mod m}e(a(p+s)/m). Summing over s ∈ (2U, 4U] against a smooth phase
  g(s, m) gives (1/m)Σ_a e(ap/m)Σ_s e(as/m)g(s, m).
* Poisson in a then returns Σ_ν ĝ-type coefficients times e(−νp/m), i.e. the θ-expansion of §6.
* The only arithmetic in the coefficients is "p mod m" (equivalently ⌊p/m⌋). No modular inverse of p, or of any other
  variable, appears, so there are no Kloosterman sums S(·, ·; m) whose sum over m Kuznetsov could treat.
* The same holds in the (k, s) parametrization with "p mod k".
(ii) *Where Kloosterman sums do appear.* Detecting u | p + B and B | p + u by CRT over uB produces Kloosterman fractions
e(pū/B)-type. This is the DFI / Bettin–Chandee setting of Z53_HYPKLOOST, whose necessary conditions (C̄ ≲ p^{1/37},
resp. p^{1/21}, for their displayed bounds to save) fail at the balanced block; see FRONTIER §7.1.
(iii) *Spacing / Bombieri–Iwaniec (Assessment; no double-sum theorem is quoted, LIT_CHECK Q6 UNVERIFIED).*
* BI-type first-spacing bounds for Σ_{ν~N}|Σ_{m~M}e(νF(m))| give per-frequency square root times a power loss on
  average over ν. That is how they yield Δ(x) ≪ x^{θ*} with θ* > 1/4, where per-frequency square root suffices because
  of the 1/ν amplitudes.
* Table 7.1 shows that CNT already needs a joint saving *beyond* per-frequency square root (flat amplitudes 1/U over
  |ν| ≤ U), and TD needs U^{1/2+η} beyond it.
* So no per-frequency spacing bound can supply the targets. Only a genuinely joint (ν, m) estimate below the
  per-frequency square root could.
(iv) *Huxley-type near-curve counts.* Already Assessment in BILINDIV §5.5. Derivative-based bounds have a
second-derivative term U^{4/3} > U for f = p/m at N ≍ U², δ ≍ 1/U, so they do not even reach the count's trivial order.

So Q3 has a negative answer at the level of the specified tools. The surviving candidates are joint (ν, m) estimates
below per-frequency square root, and arithmetic upper-bound arguments for NC that use the near-square condition.

## 10. Computations (EVIDENCE; scripts `scripts/z55_tdcal_*`, data `data/z55/tdcal/`)

**10.1 Window averages** (§4): `z55_tdcal_window.c`, `window.txt`.

**10.2 TD falsifier on special prime shapes** (`z55_tdcal_inputs.py` generates the inputs; `z54_bilindiv_td.c` with
H = 32; outputs `td_*.out`). Columns as in BILINDIV §6.1. Here U = ⌊p^{1/4}⌋ ≈ 316–339, near 10¹⁰.

| sample | n | mean \|E1⁺\|/U | mean rms_h \|T\|/√\|E1⁺\| | max_h \|T\|/√\|E1⁺\| |
|---|---|---|---|---|
| 3000 consecutive primes after 10¹⁰ | 3000 | 1.539 | 0.994 | 3.19 |
| near-squares below: p = N² − c, c ∈ (2U, 4U] (puts the point (N, N) in E1; rich (1, −1) line) | 600 | 1.522 | 0.994 | 3.16 |
| near 4th powers p = N⁴ + c (U = N exactly), N = 300..339 | 400 | 1.526 | 0.990 | 2.73 |
| near rational multiples of squares p = (bN² − c)/a, (a, b) ∈ {(1,2),(2,3),(1,3),(3,4),(2,5)} | 500 | 1.514 | 0.996 | 3.04 |
| odd squares (2i+1)², i = 50000..50599 (control) | 600 | 1.522 | 0.999 | 3.68 |

**10.3 Distribution of T(h)** (`z55_tdcal_tail.c`, `tail.txt`). P(|T(h)|/√|E1⁺| > t) over all (n, 1 ≤ h ≤ 32), next to
the complex-Gaussian value e^{−t²}:

| t | primes 10¹⁰ (96 000) | Rayleigh | odd squares (96 000, second set) |
|---|---|---|---|
| 1.0 | 0.3653 | 0.3679 | 0.3690 |
| 2.0 | 0.01842 | 0.01832 | 0.01930 |
| 2.5 | 1.875e−3 | 1.930e−3 | 1.979e−3 |
| 3.0 | 1.146e−4 | 1.234e−4 | 1.458e−4 |
| 3.5 | 0 | 4.8e−6 | 1.04e−5 |

Mean |T|²/|E1⁺| is 0.996 at primes and 1.006 at squares. At primes the normalized sums are complex-Gaussian with
variance exactly 1 — the random-phase model with independent terms. The odd squares have a marginally heavier tail
(t = 2: +5 %, ≈ 2σ, with samples correlated across h). This is not significant evidence of square structure.

**10.3′ Exact checks** (`z55_tdcal_check.py`, `check.txt`; 200 consecutive primes after 10⁸, U = 100; CERTIFIED for
these inputs: exact integer arithmetic). Lemma S(a) (slice count = |E1|), S(b) (two-shift form = N₂), S(c)
(m | p² − D on every strip point) and N^{[0]} ≥ N₂: 0 failures. Prop D(iii) (EVIDENCE): the mean of
Σ_{|τ|≤T}N^{[τ]} is 1.70, 2.76, 5.72, 19.9, 73.8 at T = 0, 1, 4, 16, 64, i.e. ≈ 1.15–1.4·T for T ≥ 4 — the model order
T, far below the elementary bound. NC count: mean 𝒜(δ) = 6.44, 15.4, 30.8 against 2δ|E1⁺| = 6.05, 15.1, 30.3 at
δ = 0.02, 0.05, 0.1.

**10.4 Count error vs twisted sums** (`td_gen*.out`, column |E1|). (|E1| − 2U log 4)/√U has sd 2.79 (10⁸, U = 100,
1500 consecutive primes), 3.31 (10¹⁰), 2.75 (10¹², 600 primes) and 2.17 (10¹⁴, 150 primes). Consecutive primes have
overlapping windows at the larger scales, so these sds are rough.
* In units of √|E1| ≈ 1.66√U, this is 1.3–2.0.
* rms_h|T|/√|E1⁺| is 0.998–1.006 at all four scales.
* The low band carries arithmetic variance (cf. Ivić's log³ factor for the full short-interval mean square); the high
  band behaves as independent phases.

## 11. Hardness calibration theorem (collecting the PROVED parts)

**Theorem H (PROVED; the labels of the parts are as above).** In the fourth-root range, U ≥ U₀:
1. (Averages) R2's conclusion holds on average over every window of U^{η+ε} consecutive n, and for all but
   O(X^{(3+η)/4+ε}) primes p ≤ X (Prop A, Cor A′).
2. (Identity) |E1| is the central slice m ∈ (U², 4U²] of D(p + 2U, 2U) (Lemma S(a)).
3. (Bands) Smoothed CNT and TS involve only remainder frequencies |ν| ≤ U^{1+ε}. Smoothed TD at w ≍ W involves only
   ν ∈ [hU³/(2W), 64hU³/W] (Thm B).
4. (Ladder) Per-frequency square root yields exactly the trivial order U for CNT and h^{1/2}U^{3/2} for TD's top piece
   (Prop C(i), BILINDIV Prop 4.3).
5. (Weakest Theorem-T input) TD(η) ⇒ NC(η) ⇒ N₂ ≪ U^{1−η+ε}. The elementary bound for the near-tie count at
   tolerance T is ≪ U^{1+ε} + TU^{1/2+ε}, never of the sharp order T (Prop D).

## 12. FRONTIER §4 hard screens (best idea: NC / the calibration)

1. **T1 (odd squares).** Everything is an upper-bound statement and holds verbatim at odd squares (Prop A for every n;
   Lemma S(a) for every n; Thm B for every n with m ∤ n replaced by the obvious edge case). EVIDENCE: T(h) at odd
   squares is Rayleigh (§10.3). Silent on positivity by design.
2. **8/131.** Numerator-blind (N₄ ≤ N₂); not an ES step.
3. **Tied modulus.** NC is the tie relaxed to tolerance U^{1−η}. The tie is not broken; it is bounded from above.
4. **Fixed p.** Prop A and Cor A′ are averages, and are presented as calibration, not as a fixed-p result. Thm B, Prop C,
   Prop D and NC are pointwise in p.

## 13. Verdict

**Narrowed (calibrated), with one weaker sufficient condition.**
* *Strengthened (small):*
  * NC(η), a one-sided near-zero upper bound, is a sufficient condition weaker in form than TD (TD ⇒ NC ⇒ R2).
  * R2 holds on average over windows of length U^{η+ε}, and off an exceptional set of ≪ X^{(3+η)/4+ε} primes.
  * Neither moves the pointwise problem.
* *Narrowed (scoped):*
  * averages over n or U give nothing pointwise (Prop A, A″);
  * TD and CNT/TS/Jutila-type statements live on disjoint remainder-frequency bands (Thm B), so no band-limited reduction
    links them;
  * per-frequency methods (exponent pairs, spacing) fall short by the joint savings of Table 7.1;
  * strip forms contain no Kloosterman sums for Kuznetsov (Prop E).
* *Answer to "how hard is TD?"* (Assessment)
  * TD is a unit-resolution statement about the exact remainders r_m inside the window.
  * In the per-frequency currency it needs more than square-root Jutila on the central slice. Measured against the
    joint random model, it needs the same power saving as every other target.
  * It is numerically perfectly random (Rayleigh).
  * Its untwisted relative CNT is already open, being a central slice of the short-interval divisor problem at length
    x^{1/4}, below the checked pointwise threshold x^{0.3145}.
* *Survives:* joint (ν, m) estimates below per-frequency square root; arithmetic upper bounds for NC that use the
  near-square condition at a single p; MIX and TS on their own families.

## 14. Proposed FRONTIER §7 text (do NOT edit FRONTIER here)
Append to §7.1 under the z54 bullets:
> * **How hard is TD? (`Z55_TDCAL.md`, z55; internal; calibration, upper-bound only.)**
>   * Prop A (PROVED): Σ_{X<n≤X+Y}N₂(n, U) ≤ Σ_M τ(M)² over an M-window of length Y + 2U. So R2 holds on average over
>     every window of p^{η/4+ε} consecutive n, and fails for ≪ X^{(3+η)/4+ε} primes p ≤ X. Averaged forms of R2/TD are
>     worthless; the difficulty is one n. Averaging over U is a reweighting.
>   * Lemma S (PROVED): |E1| is the central slice (divisors in (U², 4U²]) of D(p + 2U, 2U), a short-interval divisor
>     sum at length x^{1/4}. Also N₂ = #{(u, w) : u | p + w, u + w | p − w}, and strip points satisfy m | p² − D.
>   * Thm B (PROVED): in the remainder phases θ_m = {−p/m} (m ≍ U²), smoothed CNT and TS use only |ν| ≤ U^{1+ε}, and
>     smoothed TD at w ≍ W only ν ∈ [hU³/2W, 64hU³/W]. The bands are disjoint: TD is a unit-resolution statement about
>     the remainders, CNT/TS window-resolution ones. No band-limited reduction links them.
>   * Prop C: per-frequency square root gives exactly the trivial order for CNT and h^{1/2}U^{3/2} for TD. Beyond it,
>     CNT(η) needs a joint saving U^η, central-slice square root U^{1/2}, and TD(η) h^{1/2}U^{1/2+η}.
>   * Prop D (PROVED): Theorem T only uses 𝒜(δ) = #{‖w_k‖ ≤ δ}, sandwiched by Σχ_δ(w_k). So NC(η): 𝒜(U^{−η}) ≪ U^{1−η+ε}
>     suffices, with TD ⇒ NC ⇒ R2. NC is a sharp-order upper bound for τ-perturbed tie counts over |τ| ≲ U^{1−η} at
>     fixed p. Unlike n-windows (free at length ≳ U), τ-windows have elementary bound U^{1+ε} + TU^{1/2+ε}, never
>     sharp. ℓ² in h is pair correlation (second order).
>   * Prop E: the strip forms contain no Kloosterman sums (Kuznetsov n/a); Kloosterman fractions occur only in the
>     closed (u, B)-CRT form.
>   * EVIDENCE: T(h)/√|E1⁺| is complex-Gaussian (Rayleigh tail) at 10¹⁰ over 96 000 (p, h), with no anomaly at
>     near-squares, near-4th-powers, near-rational-multiples of squares or odd squares.
>   * Missing: a joint (ν, m) estimate below per-frequency square root, or an arithmetic proof of NC at one p.
In §6 add: "R2/TD on average over p (free, Z55_TDCAL Prop A); per-frequency spacing/exponent-pair methods for TD or the
central-slice count (Z55_TDCAL Prop C/E)".

## 15. Bottom line
TD asks how the exact remainders p mod m, m ≍ √p, fall *inside* the window that defines the strip. The strip count and
the twisted sums TS only ask *whether* they fall in it.
* Expanded in the remainder phases, the two questions use disjoint frequency bands. So TD neither contains nor is
  contained in a short-interval divisor statement by any band-limited reduction.
* Its untwisted relative is a central slice of the short-interval divisor problem at length x^{1/4}, which is open.
* In the per-frequency currency TD needs more joint cancellation than square-root Jutila on that slice. Numerically it
  is as random as a sum can be.
* Averaging over p is free and useless.
* The real input of Theorem T is weaker than TD: an upper bound NC for near-ties at tolerance U^{1−η} at one p.
  Elementary bounds stop short of it by at least U^{η}: averaging over the tie tolerance, unlike averaging over p, is
  not free.
Nothing here touches positivity, and ES remains open.

## 16. Reproduction
Every command uses `timeout ≤ 1800` and `ulimit -v 4000000`.
```
cd $REPO; D=data/z55/tdcal; I=/tmp/z55in; mkdir -p $I
gcc -O2 -o /tmp/z55win scripts/z55_tdcal_window.c
timeout 600 /tmp/z55win 100000000 20000 100; timeout 600 /tmp/z55win 1000000000000 2000 1000      # window.txt
timeout 900 uv run --with sympy python scripts/z55_tdcal_inputs.py $I        # gen10 nsq10 n4p10 nrat10 sq10
python3 -c "print('\n'.join(str((2*i+1)**2) for i in range(50600,53600)))" > $I/sq10b.txt
uv run --with sympy python -c "from sympy import nextprime ..."              # gen8/gen12/gen14: 1500/600/150 consecutive primes after 10^8/10^12/10^14
gcc -O2 -o /tmp/z54td scripts/z54_bilindiv_td.c -lm; gcc -O2 -o /tmp/z55tail scripts/z55_tdcal_tail.c -lm
for f in gen10 nsq10 n4p10 nrat10 sq10; do timeout 1200 /tmp/z54td 32 < $I/$f.txt > $D/td_$f.out; done   # ~1 min
for e in 8 12 14; do timeout 1500 /tmp/z54td 16 < $I/gen$e.txt > $D/td_gen$e.out; done
for f in gen10 sq10 nsq10 nrat10 n4p10 sq10b; do timeout 1500 /tmp/z55tail 32 < $I/$f.txt; done          # tail.txt
timeout 1500 uv run --with sympy python scripts/z55_tdcal_check.py 100000000 200                       # check.txt (~5 min)
```

## 17. Review log
(pending)
