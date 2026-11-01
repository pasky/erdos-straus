# Z53_HYPKLOOST — summing over conductors and frequencies before bounding (FRONTIER §7.1, analytic/spectral)

ES is OPEN. Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Internal results are internally reviewed only.

Lane brief: `z52bbriefs/z53_depth.md`, `z52bbriefs/z53_lanes.md` § HYPKLOOST. Scripts `scripts/z53_hypkloost_*`, data
`data/z53/hypkloost/` (≈ 3.3 MB). Builds on `Z52D_HYPERBOLA.md` (cited as **HYP**; its Thm 1, Prop 2, Thm 3, Thm 5,
Thm 6) and `PARITY_AUDIT.md` §§1–2. Literature statements used here were re-read from the sources
(`data/z53/hypkloost/LIT_CHECK.md`, research subagent; caveats there).

## 0. Summary

**Verdict: narrowed.** The three implementations of "sum over conductors/frequencies before bounding" that the literature
offers are evaluated; each ends in a scoped theorem. No power saving was found in any block, and no known theorem gives one.
At fixed p, every averaged variable in these implementations turns out to be attached to p.

1. **F1 falsifier (EVIDENCE, §3).** At 3000 primes near 10¹² (U = 1000) and 10¹⁰ (U = 316), the exact conductor pieces of
   the balanced-block count are individually O(1) (sd ≈ 0.3 in each of the top relative-depth bins). They are orthogonal:
   the cross-covariance share is +0.14 [+0.03, +0.26] at 10¹² and +0.04 [−0.07, +0.15] at 10¹⁰. So there is no
   cross-conductor cancellation to harvest. **At odd squares the pieces are as large (Σ Var = 0.175) but cancel exactly**
   (share −1, forced by T1). The only exact cross-conductor cancellation is T1's.
2. **Thm B (PROVED). Frequency truncation is short-window averaging, and lower bounds need the full spectrum.**
   * (a) Every linear combination Σ_{|h|≤H} ĝ(h)S_{−h}(n) of the sawtooth sums S_h equals a g-weighted count of block
     solutions at the integers n + ℓ, |ℓ| ≲ q/H (exact Poisson identity).
   * (b) A frequency *certificate* of N(p) ≥ 1 built from degree-H trigonometric polynomials has nonpositive mean once
     H < q_max/2 = 8UV. Its expected value in the residue model is ≤ 0 once H < q_min ≈ 4UV.
   * (c) The threshold q_max/2 is sharp (Selberg minorant).
   * So "cancellation between frequencies" can certify positivity only with frequencies up to ≍ 8UV, where square-root
     input reproduces the trivial bound (HYP Thm 6). Otherwise it certifies existence in a window of integers around p
     (B6).
3. **Thm C (PROVED). Conductor truncation is class averaging, and divisibility needs the primitive conductor.**
   * (a) A dual truncated to conductors dividing M is exactly the average of N over the residue class n mod M (B1 data).
   * (b) Every minorant f ≤ 1[q | ·] on ℤ/q whose spectrum avoids the primitive frequencies a/q, gcd(a,q) = 1, has mean
     ≤ 0. This holds even if the lcm of the conductors used is q.
   * So a pairwise conductor certificate must use each contributing pair's top conductor d = q_π. There each conductor
     carries ≤ K·p^{o(1)} pairs (HYP Thm 5), and the dual is one complete Ramanujan sum per pair.
4. **Thm K (PROVED; part (c) relative to the quoted DFI/Bettin–Chandee statements). Kloosterman fractions.**
   * (a) In the two-sided Kloosterman-fraction expansion of 4uB | p+u+B, reciprocity kills the second fraction: what is
     left is the one-sided detector of B | p+u times a Dirichlet kernel in the archimedean phase (p+u+B)/(uB).
   * (b) Any bound through one divisibility relation has main term Σ 1/B ≥ min(U,V)/2. So it is never better than half
     the elementary bound min(U, V, C̄+1), in any block.
   * (c) The numerator of every fraction is a = bp ≥ p ≥ UV. Hence DFI Thm 1 never beats the trivial bound, DFI Thm 2 only
     if C̄ < p^{1/37}, and Bettin–Chandee only if C̄ < p^{1/20}.
   * EVIDENCE (F3): the fixed-p KF sums are square-root size (rms 0.57–0.99·√(#pairs)). The one-relation count equals
     Σ 1/B ≈ U log 2 ± 17 at 10¹² (U = V = 1000), so even exact knowledge of it gives ≈ 0.69·U.
5. **Prop Q (PROVED bookkeeping; reading Assessment). Kuznetsov.**
   * In the SL₂ form, the (★) condition at level c selects one Bruhat double coset of the Kloosterman sum S(·,·;c),
     d ≡ −1 (mod c). Inside that coset it imposes a lattice condition (top-right entry = p), not a Fourier coefficient.
   * In every normalisation the Kloosterman modulus is either p itself (no sum over moduli; Weil only) or the level c,
     with one integer cp + 1 per level (as in Z1480).
6. **(S2) benchmark (Assessment, with the determinant-method computation PROVED from Heath-Brown Thm 14 as quoted).** No
   known theorem gives R(p) ≪ p^{1/3−η}. Heath-Brown's Theorem 14 on the cubic surface 4xyz − x − y = p yields
   ≍ V^{2/(3√3)} ≈ p^{0.385} auxiliary curves, which is already worse than p^{1/3}. The elementary p^{1/3} equals the
   dimension-growth exponent for this surface.
7. **Thm E (PROVED).** HYP Thm 6(b,c) holds in all three coordinate systems, (u,B), (u,C) and (B,C), and in every block:
   square-root exponential-sum input never beats HYP Thm 1.

What survives (§7): an upper bound N ≪ U^{1−η} via beyond-square-root cancellation (HYP R1, R2). Note that (S1) itself is
an upper bound, worth nothing for ES. For positivity, only arguments that inject the arithmetic of p (its primality or
quadratic character) into the *top* of the spectrum survive: frequencies ≥ 4UV, conductor d = q_π. There the dual is one
Ramanujan sum per pair and the variance is orthogonal. No such method is known.

## 1. Statements attacked

Notation as in HYP §2:
* p ≥ 5 prime; block 𝔅 = (U,2U] × (V,2V]; pair π = (u,B); q = q_π = 4uB; s = s_π = u + B; n ∈ ℤ.
* N(n) = N_𝔅(n) = #{π ∈ 𝔅 : q | n + s}.
* q_min = 4(U+1)(V+1) and q_max = 16UV are the extreme moduli of the block.
* C̄ = p/(4UV) is the typical level. The balanced block is U = V ≈ p^{1/4} (C̄ ≍ p^{1/2}); the cube block is
  U ≍ V ≍ C̄ ≍ p^{1/3}.
* HYP Thm 1 (elementary): N ≤ p^{o(1)}·min(U, V, C̄ + 1).

The conductor (Ramanujan) dual of the block count is the exact identity (HYP (2.1))

  N(n) = Σ_{d ≥ 1} Σ*_{a mod d} e(an/d)·D(d,a),  D(d,a) := Σ_{π ∈ 𝔅 : d | q_π} q_π⁻¹ e(a s_π/d),          (1.1)

So N, as a function of the integer n, is a trigonometric polynomial whose spectrum lies in the Farey fractions a/d with
d ≤ q_max. The archimedean (sawtooth) form is HYP (E3): N(n) = #{π : F_π(n) ∈ ℤ} with F_π(n) = (n + s_π)/q_π, and
S_h(n) := Σ_π e(hF_π(n)).

"Summing over conductors (frequencies) before bounding" means the following. Evaluate a weighted sum of the dual (1.1), or
of the S_h, or of a Kloosterman-fraction form of N, that couples different conductors, frequencies or moduli, and bound
that, rather than each conductor separately (that is HYP Thm 5).

* **(S1) Cross-conductor / cross-frequency power saving at fixed p.** ∃ η > 0 such that for every large prime p,
  |N_bal(p) − M| ≤ p^{1/4−η}, by an argument of the kind just described.
  * M ≈ 0.146 is the block mean. Since M = O(1), this is the *upper bound* N_bal(p) ≪ p^{1/4−η}.
  * The same question is asked for every other block, against its trivial bound min(U, V, C̄).
  * Positivity (N ≥ 1, the direction ES needs) is treated alongside (§§5–6).
* **(S2) Benchmark.** ∃ η > 0 with |E(p)| = |R(p) − M(p)| ≤ p^{1/3−η} for all large p, by *any* known theorem.
* **(S3) Implementation classes**, each to be settled by a power saving or by a scoped theorem:
  * (L) linear and minorant/majorant functionals of the dual (1.1) or of the S_h, i.e. weighted sums over conductors and
    frequencies;
  * (K) bilinear/trilinear Kloosterman-fraction bounds (Duke–Friedlander–Iwaniec 1997, Bettin–Chandee 2018) applied to a
    Kloosterman-fraction form of the block count;
  * (Q) sums of Kloosterman sums over moduli (Kuznetsov, Deshouillers–Iwaniec) in which the averaged modulus is not
    attached to p.

## 2. Why this was not already closed

HYP closes only these four implementations:
* (i) one-step dualization *at a fixed conductor* (Thm 5);
* (ii) Erdős–Turán/Fejér with max_h |S_h| input (Thm 6);
* (iii) Cauchy–Schwarz in the function variable (Prop 2);
* (iv) low-conductor and class-model main terms (Thm 3, Cor 4).

Its open list keeps (R0), "cancellation across conductors or across frequencies; no method known". (L), (K) and (Q) are
exactly the implementations of (R0) that the literature offers, since they sum over conductors, moduli or frequencies
jointly. Earlier treatment of them amounts to two remarks:
* PARITY_AUDIT B7: "the Kloosterman fraction degenerates";
* BRAINSTORM/s8_volume_dfi R268: DFI is trivial for MN = o(p^{36/37}).

## 3. Falsifier F1: do conductor pieces cancel against each other at a fixed prime? (EVIDENCE)

**Program.** `scripts/z53_hypkloost_conductor.c` computes, for each n, the exact Ramanujan expansion of N_bal(n) (sharp
balanced block).
* c_d(m) is computed multiplicatively from v_ℓ(m): for ℓ^e ∥ d, c_{ℓ^e}(m) = φ(ℓ^e), −ℓ^{e−1} or 0 according as
  ℓ^e | m, ℓ^{e−1} ∥ m, or neither.
* The terms are grouped into relative-depth bins k = ⌊log₂(q/d)⌋ (k = 0 is the top conductor d = q) and into absolute
  bins j = ⌊log₂ d⌋.
* The program checks that the bins sum to N(n). This holds in all 10 800 cases: |Σ bins − N| < 5·10⁻¹⁰, i.e. zero at the
  9 printed decimals.

Analysis: `scripts/z53_hypkloost_cond_analyze.py` → `data/z53/hypkloost/cond_stats.txt`. Per-n rows are in
`data/z53/hypkloost/c_*.tsv.gz`.

**Data sets.**
* 3000 consecutive primes from 10¹² (U = 1000) and from 10¹⁰ (U = 316).
* Controls: 600 odd squares m² ≥ 10¹² and ≥ 10¹⁰; 600 near-square primes m² + k (k ≤ 40) above 10¹²; 1500 random
  n ≡ 1 (4) at each scale.

**"Square-root prediction" = the orthogonal model.** Under n uniform modulo L = lcm{q_π}, distinct Farey fractions are
orthogonal. So the conductor pieces are uncorrelated and Var(N) = Σ_k Var(P_k) (PROVED by Parseval: E_n[e(an/d)·
\overline{e(a′n/d′)}] = 1[a/d = a′/d′]). Cross-conductor cancellation would show up as a negative covariance share
(Σ_{k≠l} Cov(P_k, P_l))/(Σ_k Var P_k).

| set | Σ_k Var(P_k) | Var(N) | cross-cov share (95 % bootstrap CI, 400 resamples) |
|---|---|---|---|
| primes 10¹² | 0.276 | 0.315 | **+0.14** [+0.03, +0.26] |
| random n ≡ 1 (4), 10¹² | 0.257 | 0.243 | −0.05 [−0.20, +0.09] |
| near-square primes 10¹² | 0.269 | 0.296 | +0.10 [−0.14, +0.37] |
| primes 10¹⁰ | 0.261 | 0.270 | +0.04 [−0.07, +0.15] |
| random n ≡ 1 (4), 10¹⁰ | 0.261 | 0.271 | +0.04 [−0.20, +0.27] |
| **odd squares 10¹²** | 0.175 | **0** | **−1.000** (exact) |
| odd squares 10¹⁰ | 0.198 | 0 | −1.000 (exact) |

* **Primes.** The pieces are individually O(1): the sd of bins k = 0, 1, 2, 3 is 0.30, 0.27, 0.22, 0.17. The variance is
  spread over relative depths q/d ≤ 2⁶. The pieces do **not** cancel against each other; the cross-covariance is ≈ 0 or
  slightly positive. This is orthogonal behaviour.
* **Capture.** corr(N, P₀ + … + P_k) = 0.61, 0.76, 0.88, 0.94, 0.97 for k = 0…4 (10¹²).
* **Low conductors.** Absolute bins d < 2¹⁰ ≈ U are essentially constant at primes (sd ≤ 0.003; HYP Thm 3, here in sharp
  form). They are not constant at random n (sd 0.019 in bin j = 1), as HYP Thm 3 predicts: it needs gcd(n, d) = 1.
* **Odd squares.** The pieces are as large as at primes, but they cancel exactly: Σ = N = 0 by T1.
  * So exact cross-conductor cancellation exists. It occurs at squares, where T1 forces it, and it is absent at primes.
  * A method that bounds conductor ranges separately, uniformly in n, cannot see T1.
  * A method that harvested cross-conductor cancellation would be harvesting the square conspiracy, which is the opposite
    of what positivity at p needs.

**Reading (Assessment).** At a fixed prime the dual sum is an orthogonal superposition of O(1) pieces, and its total
fluctuation is the sum of theirs. The only exact cancellation in sight is T1's. The falsifier does not by itself close
(S1): a pointwise argument could still find cancellation that is invisible in the variance. §§5–6 address that by theorems.

**Falsifier F3: Kloosterman-fraction sums at fixed p (EVIDENCE).** Program: `scripts/z53_hypkloost_kf.c`; data:
`data/z53/hypkloost/kf_*.tsv`.
* Quantity: K(b) = Σ_{u∼U, B∼V, (u,B)=1} e(bp ū/B), with ū the inverse of u mod B and 1 ≤ b ≤ 16. This is the DFI-type
  bilinear sum that detects B | p + u.
* Windows: the first 200 primes ≥ 10¹² (U = V = 1000) and the first 100 primes ≥ 10¹² in two skew blocks (100, 10⁴) and
  (10⁴, 100).
* Size: |K(b)|/√(#coprime pairs) has rms 0.567, 0.988 and 0.786 (max 1.66, 2.86, 2.19). This is square-root size, i.e.
  the best that any bilinear KF bound could give.
* The one-relation count N₁ = #{π : B | p + u} equals its zero-frequency term Σ_π 1/B (= U·(H_{2V} − H_V) ≈ 693 for
  U = V = 1000) within sd 16.8, 11.4 and 4.4 in the three blocks. For comparison N ∈ {0, 2, 4}.

## 4. Exact objects

**(O1) Ramanujan dual.** This is (1.1). Grouped by pairs, N(n) = Σ_π q⁻¹ Σ_{d | q} c_d(n + s). The conductor-d piece is
Σ_{π : d | q} q⁻¹ c_d(n + s), and by HYP Thm 5 it is attached to ≤ K·p^{o(1)} pairs once d ≥ q/K.

**(O2) Two-sided Kloosterman-fraction form** (Thm K(a) below). For coprime u, B ≥ 2:

  1[u | p+B]·1[B | p+u] = (uB)⁻¹ Σ_{a=0}^{u−1} e(a·(p+u+B)/(uB)) · Σ_{c mod B} e(c(1 + p ū)/B),               (4.1)

where ū is the inverse of u mod B.
* The archimedean factor is a Dirichlet kernel of length u in F′ = (p+u+B)/(uB) = 4C (the level, up to the factor 4).
* The arithmetic factor is the one-sided Kloosterman-fraction detector of B | p + u, with numerator c·p.
* Summed over 𝔅 this gives the coupled form N = Σ_π (uB)⁻¹ D_u(F′_π) Σ_c e(c(1+pū)/B), with D_u(x) = Σ_{a<u} e(ax).
* No pair of free moduli carries a Kloosterman fraction with a numerator independent of p.

**(O3) One-sided bilinear sum.** N₁ := #{π : B | p + u} = Σ_π B⁻¹ + Σ_{b ≥ 1} Σ_{B > b} B⁻¹ e(b/B) Σ_{u : (u,B)=1}
e(bp ū/B), up to the non-coprime pairs.
* This is a DFI form Σ α_u β_B e(a ū/B), with α_u = 1, β_B = 1[B > b]e(b/B)/B and numerator a = bp. These are exactly the
  "coefficients you control".
* Non-coprime pairs are handled by the same formula with u/g, B/g. They never contribute to N (HYP Lemma 0).

**(O4) Unbalanced blocks V ≥ 2U.** For fixed u the admissible B run through the progression B ≡ −p (mod u) in (V, 2V],
which has ⌊V/u⌋ or ⌊V/u⌋ + 1 terms. Then N = Σ_u Σ_{B ≡ −p (u)} 1[B | p+u] (with the 4-condition). Detecting the
progression by characters mod u gives phases e(aB/u + b(p+u)/B). Detecting B | p+u by Kloosterman fractions gives (O2)
again.

**(O5) Trial form, single modulus variable.** R(p) = #{m ≡ 3 (mod 4) : r_m := (−p mod m) ≥ 1 and 4r_m | m + 1}. The
moduli m = 4uC − 1 range freely; p enters only through p mod m.
* Proof: m = 4uC − 1 | p + u forces u ≡ −p (mod m), and 0 < u < m, so u = r_m.
* The Kloosterman fraction of this form is degenerate: \overline{4C} ≡ u (mod m). This is PARITY_AUDIT B7.

## 5. Linear functionals of the dual (class L)

### 5.1 Theorem B — frequency truncation is window averaging; lower bounds need frequencies ≥ q_max/2 (PROVED)

Let H ≥ 0 be an integer. Let G(x) = Σ_{|h|≤H} ĝ(h)e(hx) be a real trigonometric polynomial of degree ≤ H. Let g: ℝ → ℝ be
any continuous function with g(t) = O((1+|t|)⁻²) whose Fourier transform ĝ(ξ) = ∫g(t)e(−ξt)dt is continuous, supported in
[−H, H], and agrees with the coefficients of G at the integers. Example: the Fejér pair
g(t) = (H+1)(sin π(H+1)t/(π(H+1)t))², ĝ(ξ) = (1 − |ξ|/(H+1))₊.

**(a) Window identity.** For every integer n,

  Σ_{|h|≤H} ĝ(h)·S_{−h}(n) = Σ_{π∈𝔅} Σ_{ℓ ∈ ℤ : q_π | n+ℓ+s_π} g(ℓ/q_π).                           (5.1)

So every linear combination of the S_h with |h| ≤ H equals a g-weighted count of block solutions at the integers n + ℓ.
The weight attached to ℓ is g(ℓ/q_π). For the Fejér pair it is ≥ 4(H+1)/π² for |ℓ| ≤ q/(2H+2) and ≤ q²/(π²(H+1)ℓ²) for
all ℓ ≠ 0.

All of (a)–(c) hold verbatim for any finite set 𝒫 of pairs in place of 𝔅 (a union of blocks, or all pairs of R(p)), with
q_min, q_max the extreme moduli of 𝒫.

**(b) Sharp threshold for certificates.** Call G a *frequency certificate* (for 𝔅) if G(0) > 0 and G(x) ≤ 0 at every
x ∈ T_𝔅 := ∪_{π∈𝔅}(q_π⁻¹ℤ ∖ ℤ). For such G, (5.1) in periodic form gives
Σ_π G(−F_π(n)) ≤ G(0)·N(n) for all n, so positivity of the frequency side certifies N(n) ≥ 1. Then:
* if H < q_max/2, the mean ĝ(0) = ∫₀¹G is ≤ 0;
* if H < q_min, then for n uniform modulo L = lcm{q_π}, E[Σ_π G(−F_π(n))] = ĝ(0)·|𝔅| ≤ 0. The frequency side of every
  certificate then has nonpositive expectation. It can be positive at a given p only through a deviation of the
  oscillatory part Σ_{0<|h|≤H} ĝ(h)S_{−h}(p) above its mean, never as "main term > error".

**(c) Sharpness.** For every δ < 1/q_max and every H with H + 1 > 1/(2δ), the Selberg minorant of the arc [−δ, δ] (mod 1)
is a frequency certificate with ĝ(0) = 2δ − 1/(H+1) > 0. So positive-mean certificates exist exactly from H ≈ q_max/2 on,
up to the choice of δ < 1/q_max.

*Proof.*
(a) Fix π and put F = F_π(n).
* Poisson summation applied to t ↦ g(t − F) gives Σ_{k∈ℤ} g(k − F) = Σ_h ĝ(h)e(−hF). Both sides converge absolutely,
  because g = O(t⁻²) and ĝ is continuous with compact support.
* k − F = (kq − n − s)/q. Putting ℓ := kq − n − s is a bijection from ℤ onto {ℓ : q | n + ℓ + s}, and k − F = ℓ/q.
* Sum over π. The left side becomes Σ_h ĝ(h) S_{−h}(n), since S_{−h}(n) = Σ_π e(−hF_π(n)) and ĝ(h) = 0 for |h| > H.

The periodic form: G(x) = Σ_k g(x + k), so Σ_π G(−F_π(n)) is the same quantity.

(b), first claim.
* Let π₀ be a pair with q₀ := q_{π₀} = q_max, which is even, and put Q′ := q₀/2. Since Q′ > H, the (Q′)-point quadrature
  is exact for trigonometric polynomials of degree ≤ H, because e(hx) with 0 < |h| ≤ H < Q′ averages to 0 over any
  coset of Q′⁻¹ℤ/ℤ. Hence ĝ(0) = (1/Q′)Σ_{k mod Q′} G((k + 1/2)/Q′).
* Each sample point is (2k+1)/q₀ ∈ q₀⁻¹ℤ ∖ ℤ ⊆ T_𝔅, because the numerator is odd and q₀ is even. So every sample value
  is ≤ 0, and ĝ(0) ≤ 0.

(b), second claim.
* n mod q_π is uniform, so E[G(−F_π(n))] = q_π⁻¹ Σ_{r mod q_π} G(r/q_π) = Σ_{j∈ℤ} ĝ(j q_π).
* For q_π ≥ q_min > H only j = 0 survives, so the expectation is ĝ(0) for every pair. Since q_min ≤ q_max, ĝ(0) ≤ 0
  by the first claim.

(c) The Selberg minorant S⁻ of a closed arc I of length 2δ satisfies three things:
* S⁻ ≤ 1_I;
* ∫S⁻ = 2δ − 1/(H+1);
* degree ≤ H.

(Montgomery, *Ten Lectures*, Ch. 1; Vaaler, BAMS 12 (1985); as quoted in HYP Thm 6(a).) For δ < 1/q_max the arc
[−δ, δ] meets ∪_π q_π⁻¹ℤ only at 0 mod 1. So S⁻ ≤ 0 on T_𝔅 and S⁻(0) ≤ 1, and S⁻(0) > 0 because its mean is positive
and S⁻ ≤ 0 off the arc. ∎

*Check of (b)–(c) by linear programming* (`scripts/z53_hypkloost_certificate_lp.py` →
`data/z53/hypkloost/certificate_lp.txt`). For the blocks (U,V) = (2,2), (2,3), (3,3) (q_max = 64, 96, 144), we maximise
ĝ(0) over even certificates of degree H, subject to G ≤ 0 on T_𝔅 and G(0) ≤ 1.
* The maximum is 0 for every H < q_max/2 tested (H = 30, 31; 46, 47; 63, 70, 71).
* It is positive from H = q_max/2 on (0.0053, 0.0017, 0.0007 at H = 32, 48, 72).
* So the threshold q_max/2 is attained exactly in these cases.

*Check of (a).* `scripts/z53_hypkloost_window_check.py` → `data/z53/hypkloost/window_check.txt`.
* (5.1) holds in 5 cases (n up to 4·10⁶, H up to 200) to within the truncation tail of the ℓ-sum: the differences
  1.2·10⁻³–5.4·10⁻³ are below the stated tail bounds 2.0·10⁻³–1.1·10⁻².
* E_n S_h = Σ_{π : q_π | h} e(hs/q) was checked by exact averaging over n mod L (L = 2880) for h ∈ {1, 2, 5, 47, 48, 96}.
  It vanishes for 0 < h < q_min = 48.

**Reading.**
* With frequencies |h| ≤ H, a linear method sees the count only through window averages of length ≍ q/H ≍ UV/H. For
  H ≤ (UV)^{1−η} that is an average over ≥ (UV)^η consecutive integers around p, almost all of them composite: B6 in its
  archimedean form.
* Proving N(p) ≥ 1 by a frequency certificate needs H ≥ q_max/2 = 8UV for every block that is to contribute positive
  mean. In that range HYP Thm 6(b) gives max_{h≤H}|S_h| ≥ (UV)^{1/2}/2.
* The arithmetic part of the block mean, M = Σ_π 1/q_π over admissible pairs, sits at the resonant frequencies
  h ≡ 0 (mod q_π), all ≥ q_min. For q_min ≤ H the expectation of a certificate is Σ_π q_π⁻¹Σ_r G(r/q_π) ≤ G(0)·Σ_π 1/q_π.
  So it is at most the block's mean count; it can never exceed it, since a certificate is ≤ N pointwise.
* In the balanced block this is ≈ 0.146, while N = 0 for ≈ 93 % of primes (HYP R4). So a single-block certificate fails
  for most primes.
* For R(p) the theorem applies to the set of all pairs. There q_max ≈ 4p/3, and a certificate for R(p) as a whole needs
  frequencies up to ≍ p.
* Assessment. A frequency certificate is a statement about an atypically large value of its oscillatory part
  Σ_{h≠0} ĝ(h)S_{−h}(p) at the given p, and that statement is the problem itself.
* Theorem B concerns *lower* bounds. Majorants (upper bounds, (S1)) with small H are not affected: HYP Thm 6(a) with
  beyond-square-root input on a short segment (R1) stays sufficient.

### 5.2 Theorem C — conductor truncation is class averaging; divisibility needs the primitive conductor (PROVED)

**(a) Class averages.** Let M ≥ 1. Restrict (1.1) to the frequencies a/d with d | M:
Λ_M(n) := Σ_{d|M} Σ*_{a mod d} e(an/d)D(d,a). Then for every integer n,

  Λ_M(n) = Σ_π gcd(q_π, M)/q_π · 1[gcd(q_π, M) | n + s_π] = E[N(n′) | n′ ≡ n (mod M)],

with n′ uniform over the residues mod L′ := lcm(M, all q_π) that are ≡ n (mod M). In particular Λ_M(p) depends only on
p mod M. Any implementation whose conductor support is divisor-closed with lcm M uses congruence data only (B1). For
M = lcm(1, …, D) with D ≤ min(U,V)^{1−ε} and smooth weights, HYP Thm 3 shows it is a constant up to O(min^{−A}).

**(b) Lemma (primitive conductor).** Let q ≥ 2. Let f: ℤ/q → ℝ satisfy f ≤ 1_{0}, and suppose f has no primitive
frequency: f̂(a) := q⁻¹Σ_m f(m)e(−am/q) = 0 whenever gcd(a, q) = 1. For f of the Ramanujan form m ↦ q⁻¹Σ_{d|q} λ(d)c_d(m) this
means exactly λ(q) = 0, since c_q carries the primitive frequencies and c_d (d < q) only non-primitive ones. Then
mean(f) = f̂(0) ≤ 0.

**(c) Consequence.** Call pairwise conductor weights {f_π} a *conductor certificate* if f_π: ℤ/q_π → ℝ, f_π ≤ 1_{0} and
Λ(n) := Σ_π f_π(n + s_π) ≥ 1 is to be shown. Then Λ ≤ N, and every pair whose f_π omits the top conductor d = q_π
contributes ≤ 0 in mean.
* So positive mean requires, for each contributing pair, the primitive conductor q_π. That is the top of the dual, where
  HYP Thm 5 applies: ≤ K·p^{o(1)} pairs per conductor ≥ q/K, and one complete Ramanujan sum c_{q_π}(p + s_π) per pair.
* (b) is stronger than requiring lcm(supp) = q. Example: q = ℓ₁ℓ₂ with supports {1, ℓ₁, ℓ₂}. Here the lcm is q, but every
  minorant a + b·1[ℓ₁|m] + c·1[ℓ₂|m] ≤ 1[q|m] has mean ≤ max(0, 1/ℓ₁ + 1/ℓ₂ − 1) = 0. The optimum is the Bonferroni
  minorant, or 0.

*Proof.*
(a) For a pair π, Σ_{d | gcd(q,M)} c_d(m) = Σ_{d | g} c_d(m) = g·1[g | m], with g = gcd(q, M). (The frequencies a/d with
d | M that occur in π's expansion are those with d | g.) Dividing by q gives the first formula. For n′ uniform on its
class mod M inside ℤ/L′, P(q | n′ + s) = 1[g | n + s]·(g/q), by CRT on q and M. Summing over π gives the second formula.

(b) Write q = ∏_{i=1}^k ℓ_i^{e_i}. Let H_i ⊂ ℤ/q be the subgroup of order ℓ_i, i.e. the multiples of q/ℓ_i.
* *f is a sum of H_i-invariant functions.* A non-primitive frequency a has some ℓ_i | a, so m ↦ e(am/q) has period
  q/ℓ_i, i.e. it is invariant under translation by H_i. Hence f = Σ_i g_i with each g_i H_i-invariant.
* *A test measure.* Let u be the uniform probability measure on ℤ/q. In the CRT coordinates ℤ/q = ∏ ℤ/ℓ_i^{e_i}, put
  a_i := ℓ_i^{e_i−1} (an element of order ℓ_i in the i-th factor) and

    ν := u + (−1)^{k+1} q⁻¹ ⊗_{i=1}^k (δ_{a_i} − δ_0).

* *ν is a probability measure with ν(0) = 0.* The signed part takes values in {±1/q} on the 2^k points with i-th
  coordinate in {0, a_i}, and 0 elsewhere. At 0 its value is (−1)^{k+1}(−1)^k/q = −1/q. Hence ν(0) = 0. Every value of ν
  lies in {0, 1/q, 2/q}, and the total mass is 1 because each factor δ_{a_i} − δ_0 has mass 0.
* *ν integrates H_i-invariant functions like u.* In the i-th coordinate, δ_{a_i} − δ_0 has zero mass on every H_i-coset,
  because 0 and a_i lie in the same coset. So Σ_m (ν − u)(m) g_i(m) = 0 for every H_i-invariant g_i.
* *Conclusion.* mean(f) = Σ_m u(m)f(m) = Σ_m ν(m)f(m) ≤ Σ_m ν(m)1_{0}(m) = ν(0) = 0.

(c) is (b) applied pair by pair, with E[f_π(n+s_π)] = mean(f_π) for n uniform mod q_π. ∎

*Check (q = ℓ₁ℓ₂ example).* The four constraints a ≤ 0, a + b ≤ 0, a + c ≤ 0, a + b + c ≤ 1 bound the mean
a + b/ℓ₁ + c/ℓ₂ by max(0, 1/ℓ₁ + 1/ℓ₂ − 1) (a linear programme over a cone; vertices a = b = c = 0 and a = −1, b = c = 1),
so by 0 for ℓ₁, ℓ₂ ≥ 2.

**Reading.**
* Conductor truncation with lcm M is the class average of N over n ≡ p (mod M): congruence data, or with low conductors a
  universal constant (HYP Thm 3).
* A pairwise lower bound must use every contributing pair's primitive conductor q_π. That is the regime of HYP Thm 5, where
  the dual has nothing to sum.
* F1 locates the fluctuation of N there too: the top relative depths carry it, and they are orthogonal.
* (b) is the conductor analogue of Theorem B(b). Both are uncertainty statements: a minorant of a point mass needs the
  top of the spectrum.

### 5.3 Theorem E — the square-root ceiling holds in every coordinate system (PROVED)

Take the coordinate pairs (X, Y) ∈ {(u,B), (u,C), (B,C)} of a block, with phase functions
* F(u,B) = (p+u+B)/(4uB) (HYP),
* G(u,C) = (p+u)/(4uC − 1),
* G′(B,C) = (p+B)/(4BC − 1),

so that hits are the points where the phase is an integer. Let 𝒫 be the box of pairs, |𝒫| = XY in the obvious sense.
Put S_h := Σ_{𝒫} e(h·phase) and Δ_H := max_{1≤h≤H}|S_h|.

(a) N ≤ |𝒫|/(H+1) + H·Δ_H/(H+1) for every H ≥ 1.

(b) For H + 1 ≥ 2|𝒫|, Δ_H ≥ |𝒫|^{1/2}/2.

(c) Hence square-root input Δ_H ≍ |𝒫|^{1/2} yields only N ≪ |𝒫|^{1/2} = (XY)^{1/2}. The C-side of a block has length
≍ C̄ (C ranges over [p/(16UV), (p+2U+2V)/(4UV)]). Hence (XY)^{1/2} ≥ min(X,Y) ≫ min(U, V, C̄ + 1), and square-root input
never beats HYP Thm 1 in any block or coordinate system. In each system it equals the trivial bound up to constants exactly
when the two coordinate sides are comparable.

*Proof.*
* A hit is a point of 𝒫 whose phase is an integer (for (u,C) and (B,C) the size condition on the third coordinate is
  dropped, which only increases the count).
* (a) is HYP Thm 6(a), Fejér form: 1[t ∈ ℤ] ≤ K_H(t)/(H+1), with K_H ≥ 0 and K_H(0) = H + 1. Sum over 𝒫 and use
  |S_h| ≤ Δ_H for 0 < |h| ≤ H.
* (b) is HYP Thm 6(b) verbatim. Σ_{|h|≤H}(1 − |h|/(H+1))|S_h|² = Σ_{x,x′∈𝒫} K_H(phase(x) − phase(x′)) ≥ (H+1)|𝒫|;
  subtract the h = 0 term |𝒫|² ≤ (H+1)|𝒫|/2 and divide by 2H. Nothing in the proof uses the specific phase. ∎

## 6. Kloosterman fractions (class K) and Kuznetsov (class Q)

### 6.1 Theorem K (PROVED; (c) relative to the quoted statements)

(a) **Reciprocity collapse.** Let u, B ≥ 2 be coprime. Let B̄ ∈ [1, u) be the inverse of B mod u and ū ∈ [1, B) the
inverse of u mod B. Then B̄/u + ū/B = 1 + 1/(uB). Hence, for all integers a, b,

  e(ap B̄/u + bp ū/B) = e(ap/(uB))·e((b − a)p ū/B),

and identity (4.1) holds.

(b) **One-relation ceiling.** Let N₁ := #{π ∈ 𝔅 : B | p + u} and N₁′ := #{π ∈ 𝔅 : u | p + B}. Their zero-frequency terms
are Σ_π 1/B = U·(H_{2V} − H_V) ≥ U/2 and Σ_π 1/u ≥ V/2.
* An argument of the form N ≤ N₁ ≤ (zero-frequency term) + |error bound|, or the same with N₁′, therefore outputs a bound
  ≥ min(U,V)/2 ≥ min(U, V, C̄+1)/2.
* An argument that evaluates N₁ exactly outputs N₁. Deterministically, N₁ ≥ Σ_{B∼V}⌊U/B⌋ ≥ U/2 − V, which is ≥ U/4 once
  U ≥ 4V; symmetrically for N₁′. In the balanced block there is no deterministic lower bound, but EVIDENCE (F3) gives
  N₁ = Σ1/B ± 17 ≈ 0.69·U at 10¹².
* A bilinear Kloosterman-fraction bound with coefficients α_u, β_B can only see such one-relation counts. The second
  relation is a coupling 1[u | p+B], not a product α_uβ_B. Once it is expanded as well, (a) turns it into the archimedean
  kernel D_u(F′), i.e. the sawtooth route. In the balanced block that is the 2-cycle count R2 of HYP Prop 2, now summed
  over the graph 𝓛₂.

(c) **Numerator obstruction.** For K(b) = Σ_{u∼U, B∼V, (u,B)=1} α_u β_B e(bp ū/B) with b ≥ 1, the numerator is a = bp ≥ p.
In a block that contains a hit, 4UV < p + 4U + 4V, so a ≥ UV up to a factor 1 + O((U+V)/(UV)). Write ‖·‖ for ℓ²-norms. The
Cauchy–Schwarz trivial bound is ‖α‖‖β‖(UV)^{1/2}.
* DFI Thm 1 gives ‖α‖‖β‖(U+V)^{1/2}(1 + a/UV)^{1/2}min(U,V)^{1/2}(UV)^ε. Since (U+V)min(U,V) ≥ UV, this is
  ≥ ‖α‖‖β‖(UV)^{1/2}(a/UV)^{1/2}. It is **never** below the trivial bound.
* DFI Thm 2 gives ‖α‖‖β‖(a + UV)^{3/8}(U+V)^{11/48+ε}. With a ≥ p and U + V ≥ 2(UV)^{1/2}, it is below the trivial bound
  only if UV > c·p^{36/37}, i.e. C̄ < p^{1/37}.
* Bettin–Chandee Thm 1 (trilinear, a = b ∈ [A/2, A], ϑ = p) gives ‖α‖‖β‖‖ν‖(1 + pA/UV)^{1/2}[(AUV)^{7/20+ε}(U+V)^{1/4} +
  …]. Against the trivial ‖α‖‖β‖‖ν‖(AUV)^{1/2} the ratio is ≥ (4C̄)^{1/2}A^{7/20}(UV)^{−1/40}. So it is nontrivial only if
  4C̄ < (UV)^{1/20} ≤ p^{1/20}.
* In every block, any route through (b) loses anyway; (c) adds that even the KF sums themselves are out of reach except in
  blocks with C̄ < p^{1/20}.

*Proof.*
(a) B B̄ + u ū ≡ 1 modulo u and modulo B, hence modulo uB. Also B + u ≤ B B̄ + u ū < 2uB, so B B̄ + u ū = 1 + uB. Divide
by uB and multiply by ap: ap B̄/u = ap/(uB) + ap − ap ū/B. Then:
* Expand 1[u | p+B] = u⁻¹Σ_{a=0}^{u−1} e(a(1 + p B̄)/u) and 1[B | p+u] = B⁻¹Σ_{b mod B} e(b(1 + p ū)/B).
* Substitute b = a + c with c running over residues mod B (for fixed a this is a bijection of residues).
* Collect: e(a/u + ap/(uB) − ap ū/B)·e((a+c)(1 + p ū)/B) = e(a(p+u+B)/(uB))·e(c(1 + p ū)/B).

(b)
* The zero-frequency term of 1[B | p+u] is 1/B, and Σ_{B=V+1}^{2V} 1/B ≥ V·(1/(2V)) = 1/2.
* For each B ∼ V the number of u ∈ (U, 2U] with u ≡ −p (mod B) is ≥ ⌊U/B⌋ ≥ U/B − 1 ≥ U/(2V) − 1. Summing over V values
  of B gives ≥ U/2 − V.

(c) This is arithmetic on the quoted bounds (`LIT_CHECK.md` §3; DFI (1.4), (1.5); BC (1.2)), with M = U, N = V, a = bp.
* DFI Thm 2: p^{3/8}(2(UV)^{1/2})^{11/48} < (UV)^{1/2} ⟺ (UV)^{37/96} > 2^{11/48}p^{3/8} ⟹ UV > p^{36/37}.
* BC: (1 + pA/UV)^{1/2}(AUV)^{7/20}(U+V)^{1/4} ≥ (4C̄A)^{1/2}(AUV)^{7/20}(UV)^{1/8} (using p/(UV) ≥ 4C̄); divide by
  (AUV)^{1/2}. ∎

**Coordinates (u, C), (B, C) and the trial form.** Here the class condition determines the inverse: \overline{4C} ≡ u
(mod 4uC − 1). The Kloosterman fraction is then a rational phase in the summation variables (O5; PARITY_AUDIT B7). In no
coordinate system does (★) present a Kloosterman fraction with two free moduli and a numerator below their product.
* (u,B): numerator bp ≥ p ≥ UV, and the second relation collapses by (a).
* (u,C), (B,C), (C, x): the fraction degenerates.

### 6.2 Proposition Q — the Kloosterman modulus is always attached to p (PROVED bookkeeping; reading Assessment)

(i) **SL₂ form** (FRONTIER §2.1). R(p) = Σ_{c ≡ 0 (4), c > 0} r_c(p), where r_c(p) = #{γ = [[a, p],[c, d]] ∈ SL₂(ℤ) :
a, d ≥ 1, a ≡ d ≡ −1 (mod c)} = #{(u, B) ∈ ℕ² : cuB − u − B = p}.

(ii) **One double coset.** For fixed c > 0, the double cosets Γ_∞\{γ : lower-left entry c}/Γ_∞ (Γ_∞ = ±[[1, ℤ],[0, 1]])
are indexed by d mod c with gcd(d, c) = 1, and the upper-left entry is a ≡ d̄ (mod c). The Kloosterman sum
S(m, n; c) = Σ_{d mod c}* e((m d̄ + n d)/c) is the sum of one exponential per double coset.
* (★) at level c keeps only the double coset d ≡ −1. Its term in S(m,n;c) is e(−(m+n)/c).
* Inside that coset (★) imposes the lattice condition "top-right entry = p". The elements of the coset are
  [[cu − 1, ·],[c, cB − 1]] with top-right entry cuB − u − B.
* So r_c(p) is not a Fourier coefficient attached to the coset. It is a representation number of the one integer cp + 1
  (as (cu−1)(cB−1)).

(iii) **Kuznetsov is attached to p.**
* Conjugation by [[0, −1],[1, 0]] makes the lower-left entry −p. With p as the Kloosterman modulus there is **one**
  modulus: no sum over moduli to average, and the class condition becomes the height-tied congruence of HYP (E5). There
  Weil's p^{1/2+o(1)} is the benchmark.
* In the original orientation the sum over moduli is the sum over levels c, and each level contributes one integer cp + 1
  (Z1480; HYP §3.7).
* Detecting d ≡ −1 inside S(·,·;c) by characters needs nebentypus mod c varying with c, which is not a Kuznetsov family
  at fixed level.

**Reading (Assessment).** A Kuznetsov/Deshouillers–Iwaniec average needs Σ_c over moduli with fixed Fourier indices
(m, n). (★) offers either a single modulus p, or moduli c whose "coefficient" is one integer each. Neither is an average
over a variable free of p.

### 6.3 Ledger of averaged variables (B6 check)

| implementation | averaged variable | what averaging it means at fixed p | status |
|---|---|---|---|
| sawtooth frequencies h ≤ H | h | window average of N over n ∈ p + [−L, L], L ≍ UV/H (Thm B(a)) | attached (archimedean B6); certificates need H ≥ 8UV (Thm B(b,c)) |
| conductors d with d \| M | (d, a) | class average of N over n ≡ p (mod M) (Thm C(a)) | attached (B1); certificates need d = q_π (Thm C(b)) |
| conductors d ≤ D ≤ min(U,V)^{1−ε} | (d, a) | universal constant (HYP Thm 3) | blind |
| KF moduli B, inverse ū | (u, B) free | one-relation count N₁ ≈ Σ1/B ≥ min(U,V)/2 (Thm K(b)) | free, but the ceiling is the trivial bound; numerator bp ≥ UV (Thm K(c)) |
| two-sided KF | (u, B, a, c) | collapses to sawtooth × one-sided KF (Thm K(a)) | reduces to rows 1 and 4 |
| Kuznetsov moduli | c | levels with one integer cp + 1 each, or single modulus p (Prop Q) | attached |
| trial moduli m = 4uC − 1 | m | the original count, through p mod m (O5) | no averaging |

## 7. (S2): is any known theorem below p^{1/3}? (Assessment; the HB computation is PROVED from the quoted statement)

| tool | output for R(p), or for the cube / balanced block |
|---|---|
| divisor bound (HYP Thm 1) | p^{1/3+o(1)} (cube block); balanced block ≤ U = p^{1/4} |
| Lenstra / Coppersmith–Howgrave-Graham–Nagaraj (PARITY_AUDIT A1–A2) | O(1) divisors of p + u ≡ −1 (mod 4u) when 4u ≥ (p+u)^{1/4+ε}: the same O(1) per u as Thm 1(a); the balanced block u ≍ p^{1/4} sits exactly at the excluded exponent 1/4 |
| Heath-Brown, Ann. Math. 155 (2002), Thm 14, applied to the homogenisation 4xyz − xw² − yw² − pw³ (box B₁, B₂, B₃, B₄ = 1) | T = max over monomials = B₁B₂B₃ = V (the product of the sides, ≍ p in every block containing a hit), so (V^d/T)^{1/d^{3/2}} = V^{2/(3√3)} ≈ p^{0.385} auxiliary curves, times (log p)⁵ (height factor) — already above p^{1/3}, before counting points per curve |
| Weil / modular hyperbola (Shparlinski Thm 13; KSWX) | error p^{1/2+o(1)} per box (PARITY_AUDIT B1, B4) |
| DFI / Bettin–Chandee | trivial unless C̄ < p^{1/37}, resp. p^{1/20} (Thm K(c)); and ≥ min(U,V)/2 via any one relation (Thm K(b)) |
| exponential sums with square-root input, any coordinates | ≥ (XY)^{1/2} ≥ trivial (Thm E) |
| KMS 2017/2020, Blomer–Pascadi, Bourgain–Garaev | Type II savings q^{1/64}…M^{1/4} of trivial bounds at one modulus; no unit-coefficient bilinear structure in (★) (PARITY_AUDIT B2–B5) |

* **Reading (Assessment).** The elementary p^{1/3} = B¹ (box side B = p^{1/3}) is the dimension-growth exponent of an
  affine surface. Beating it needs ES-specific structure.
* The one general-purpose method that exploits degree, the determinant method, produces more auxiliary curves (p^{0.385})
  than the target.
* The literature search (`LIT_CHECK.md` §4) found no sub-n^{1/3} result for the Type II c = 1 family. The best general
  pointwise bounds are f(n) ≪ n^{3/5+ε} (Elsholtz–Tao for primes; Elsholtz–Planitzer arXiv:1805.02945 for all n) and
  f_II ≪ n^{2/5+o(1)} (ET Prop 1.7). The search is not exhaustive.
* **(S2) stays open.** It is an upper-bound question and worth nothing for ES (HYP R3). It is recorded here because the lane
  brief asks it and because FRONTIER §3 uses p^{1/3} as the benchmark.

## 8. Verdict, hard screens, survivors

**Verdict: narrowed.**
* **(S1)** (an upper bound N_bal ≪ p^{1/4−η}) is not obtained. No known theorem gives it.
  * The KF route is capped at min(U,V)/2 (Thm K).
  * Square-root input in any coordinate system is capped at the trivial bound (Thm E).
  * The conductor pieces at fixed p are orthogonal O(1) pieces with no cross-cancellation (F1).
  * Open: HYP R1 (beyond-square-root short segments) and R2 (the 2-cycle bound).
* **Positivity** (the ES direction), for linear and minorant implementations of "sum over conductors/frequencies before
  bounding":
  * frequency certificates need H ≥ 8UV (sharp), and below q_min ≈ 4UV they have nonpositive expected value (Thm B);
  * pairwise conductor certificates need each pair's primitive conductor (Thm C(b));
  * truncations otherwise reduce to window averages (archimedean B6) or class averages (B1);
  * Kuznetsov's modulus is p or the level (Prop Q).

**Hard screens for the best surviving idea.** That idea is the following: beyond-square-root control of the top of the
spectrum (frequencies ≥ 4UV, primitive conductors q_π) that uses the arithmetic of p.

| screen | pass/fail | note |
|---|---|---|
| T1 (odd squares) | must use primality; the no-go theorems above hold for every integer n, so they are consistent with T1 | F1: at squares the top-of-spectrum pieces conspire to cancel exactly. A surviving idea must explain why they do not at primes. No mechanism is known |
| 8/131 | FAIL as stated | Thms B, C, E and the KF analysis are numerator-uniform (replace 4 by M). A surviving route must name where 4 enters |
| tied modulus | the top conductor *is* the tied modulus q = 4uB | the averaged variables either are p-attached or collapse (§6.3) |
| fixed p | Thms B and C identify exactly where p stops being fixed (windows, classes) | a survivor must stay at H ≥ 8UV and conductor q_π |

**What survives** (precisely):
* (i) Beyond-square-root cancellation in Σ_{q_min ≤ |h| ≤ H} ĝ(h)S_{−h}(p) for H ≍ q_max, with ĝ a certificate. This is
  equivalent to the problem.
* (ii) For the upper bound (S1): HYP R1/R2.
* (iii) Nonlinear uses of the dual, for instance products of S_h or amplification, are not covered by Thms B and C.
  * Assessment: by (5.1), any polynomial in {S_h(p)}_{|h|≤H} is a function of window data of length ≍ UV/H. The
    information-theoretic content is the same.
* (iv) Methods that do not pass through a Fourier expansion of the divisibility indicator are untouched.

## 9. Proposed FRONTIER §7.1 addition (do not edit FRONTIER here)

> *(z53, `Z53_HYPKLOOST.md`, internally reviewed.)* Summing over conductors/frequencies before bounding was evaluated in its
> three standard forms. Each is closed by a scoped theorem (PROVED):
> * (L) Frequency truncation at H is a window average of the count over n ∈ p + [−L, L], L ≍ UV/H, by an exact Poisson
>   identity. A frequency certificate of positivity needs frequencies up to q_max/2 = 8UV (sharp), and below q_min ≈ 4UV
>   its expected value is ≤ 0.
> * (L′) Conductor truncation with lcm M is the class average over n ≡ p (mod M). Every minorant of 1[q | ·] without the
>   primitive conductor q has mean ≤ 0, so a pairwise certificate must use each pair's top conductor (where HYP Thm 5
>   leaves nothing to sum).
> * (K) In the Kloosterman-fraction form, reciprocity collapses the second fraction into the archimedean phase. Any
>   one-relation bound is ≥ min(U,V)/2. The numerator is bp ≥ UV, so DFI is never/only for C̄ < p^{1/37} nontrivial,
>   and Bettin–Chandee only for C̄ < p^{1/20}.
> * (Q) Kuznetsov's modulus is p (single) or the level (one integer each).
>
> EVIDENCE (3000 primes at 10¹⁰ and 10¹²): the exact conductor pieces are O(1) and orthogonal (cross-covariance share
> +0.04/+0.14). At odd squares the same-size pieces cancel exactly (T1). (S2) "|E(p)| ≤ p^{1/3−η}" has no known proof:
> Heath-Brown's determinant method gives p^{0.385} auxiliary curves.
>
> Open: beyond-square-root control at the top of the spectrum using the arithmetic of p, and HYP R1/R2 for upper bounds.

In FRONTIER §3 "Tied modulus", after the p^{1/3} sentence, add: "(No known theorem improves p^{1/3}. It is the
dimension-growth exponent of the surface 4xyz − x − y = p, and Heath-Brown's determinant method gives p^{0.385} auxiliary
curves; `Z53_HYPKLOOST.md` §7.)"

## 10. Bottom line

The lane asked whether summing the dual of the (★) block count over conductors or frequencies *before* bounding, using
Kloosterman fractions, bilinear forms or Kuznetsov, can beat the elementary bound at a fixed prime.
* At 10¹⁰–10¹² the conductor pieces are O(1) and mutually orthogonal, so there is no cross-conductor cancellation to
  harvest. The one exact cancellation in the data is T1's at odd squares.
* Exact identities show that each averaged variable in these methods is attached to p:
  * frequency truncation is averaging over a window of integers around p;
  * conductor truncation is averaging over a residue class of p;
  * Kloosterman fractions collapse by reciprocity into the sawtooth phase, with a numerator bp too large for DFI or
    Bettin–Chandee;
  * Kuznetsov's modulus is p or the level.
* Two uncertainty lemmas make the positivity direction sharp: certificates need frequencies up to 8UV and each pair's
  primitive conductor. That is exactly the top of the spectrum, where HYP's theorems leave nothing to sum and square-root
  input is trivial.
* No known theorem, determinant method included, beats p^{1/3} for R(p).

The route is narrowed to beyond-square-root control of the top of the spectrum that uses the primality of p. No tool for
that is known. ES remains open.

## 11. Reproduction

```
ulimit -v 8000000; mkdir -p /tmp/hk && cd /tmp/hk
gcc -O2 -fopenmp -o cond $REPO/scripts/z53_hypkloost_conductor.c -lm
gcc -O2 -fopenmp -o kf   $REPO/scripts/z53_hypkloost_kf.c -lm
# inputs: p12/p10 = 3000 consecutive primes after 1e12/1e10 (sympy nextprime); sq12/sq10 = 600 odd squares from
# (10^6+1)^2 / (10^5+1)^2 step 2 in m; ns12 = 600 primes m^2+k (m > 10^6, first k in (1,4,8,...,40) with p = 1 mod 4);
# rn12/rn10 = 1500 random n = 1 mod 4 (seed 53) — generator inlined in the session, see cond_stats.txt header ranges
for f in p12 sq12 ns12 rn12; do OMP_NUM_THREADS=20 timeout 1700 ./cond 1000 1000 < $f.txt > c_$f.tsv; done
for f in p10 sq10 rn10;      do OMP_NUM_THREADS=20 timeout 1700 ./cond 316 316  < $f.txt > c_$f.tsv; done
uv run --with numpy python $REPO/scripts/z53_hypkloost_cond_analyze.py /tmp/hk > cond_stats.txt
head -200 p12.txt | ./kf 1000 1000 16 > kf_bal12.tsv; head -100 p12.txt | ./kf 100 10000 16 > kf_unb12.tsv
head -100 p12.txt | ./kf 10000 100 16 > kf_unb12b.tsv
cd $REPO && uv run python scripts/z53_hypkloost_window_check.py
```
Runtimes: `cond` ≈ 0.75 s per n at U = 1000 (one core); all F1 runs ≈ 15 min on 20 threads; `kf` 6 s for 200 primes.

## 12. Review log

(pending)
