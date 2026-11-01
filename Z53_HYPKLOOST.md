# Z53_HYPKLOOST — summing over conductors and frequencies before bounding (FRONTIER §7.1, analytic/spectral)

ES is OPEN. Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Internal results are internally reviewed only (hostile review, §12).

Lane brief: `z52bbriefs/z53_depth.md`, `z52bbriefs/z53_lanes.md` § HYPKLOOST. Scripts `scripts/z53_hypkloost_*`, data
`data/z53/hypkloost/` (≈ 3.4 MB). Builds on `Z52D_HYPERBOLA.md` (cited as **HYP**; its Thm 1, Prop 2, Thm 3, Thm 5,
Thm 6) and `PARITY_AUDIT.md` §§1–2. Literature statements were re-read from the sources by a research subagent
(`data/z53/hypkloost/LIT_CHECK.md`, with its caveats); results that use them are labelled "relative to the quoted
statement".

## 0. Summary

**Verdict: narrowed.** The lane evaluated the three standard implementations of "sum over conductors/frequencies before
bounding" that we checked: linear/minorant functionals of the dual, Kloosterman-fraction bilinear bounds, and Kuznetsov.
* Each ends in a scoped theorem, or in a computation showing that the checked theorem, applied in the displayed way, gives
  no saving.
* No power saving was found in any block. None of the checked theorems gives one.
* The obstructions proved here are to **positive-mean ("main term") arguments** and to **specific implementations**. They
  do not exclude cancellation in general, negative-mean certificates that are nevertheless positive at p (their
  oscillatory part must then exceed the negative constant term), or joint/nonlinear methods (§8).

1. **F1 falsifier (EVIDENCE, §3).** At 3000 primes near 10¹² (U = 1000) and 10¹⁰ (U = 316) we computed the exact conductor
   pieces of the balanced-block count.
   * Their sample sds are of order one (≈ 0.3 in each top relative-depth bin).
   * They show no aggregate variance reduction: the cross-covariance share is +0.14 [+0.01, +0.26] (relative bins) and
     +0.15 [+0.02, +0.28] (absolute bins) at 10¹², and +0.036 (relative) / +0.018 (absolute), CI containing 0, at 10¹⁰.
   * At odd squares the pieces have comparable variance (Σ Var = 0.175) but the total is identically 0 (share −1). This is
     forced by T1 for every square. At primes the total is also 0 for 92 % of the rows, but not identically.
2. **Thm B (PROVED). Frequency weights and positive-mean certificates.**
   * (a) Every linear combination Σ_{|h|≤H} ĝ(h)S_{−h}(n) of the sawtooth sums equals an exact pair-weighted
     periodisation, Σ_π Σ_{ℓ: q_π | n+ℓ+s_π} g(ℓ/q_π). For the Fejér kernel it is localised on a window
     |ℓ| ≲ q_π/(2H+2) around n.
   * (b) A frequency certificate of N(n) ≥ 1 of degree H < q_max/2 has mean ≤ 0.
   * (c) The threshold q_max/2 is sharp: positive-mean certificates of degree q_max/2 exist.
   * For H < min(q_min, q_max/2) the expectation of the frequency side (n uniform modulo all q_π) is |𝒫|·ĝ_0 ≤ 0, where
     ĝ_0 is the mean of G.
   * A low-degree certificate can still be positive at a particular n: an explicit example is given in §5.1.
3. **Thm C (PROVED). Conductor projections and the primitive-conductor lemma.**
   * (a) The full unweighted projection of the dual onto conductors dividing M is the class average of N over n mod M.
   * (b) Every minorant f ≤ 1[q | ·] on ℤ/q with no primitive Fourier frequency (no a/q with gcd(a,q) = 1) has
     mean ≤ 0.
   * So in a pairwise conductor certificate, every pair that contributes positive mean must use primitive frequencies;
     a positive-mean certificate needs at least one such pair. Negative-mean certificates without them exist
     (explicit example, §5.2).
4. **Thm K (PROVED; (c) relative to the quoted DFI/Bettin–Chandee statements). Kloosterman fractions.**
   * (a) In the Kloosterman-fraction expansion of the two relations u | p+B, B | p+u, reciprocity eliminates the second
     fraction. What is left is the one-sided detector of B | p+u times a Dirichlet kernel in (p+u+B)/(uB).
   * (b) A bound of the form N ≤ N₁ ≤ (zero-frequency term) + (absolute error) through one relation outputs
     ≥ min(U,V)/2 for the ordinary additive detector. For the coprime Kloosterman-fraction detector it outputs
     ≥ (6/π²)log 2·min(U,V)(1 + o(1)).
   * (c) The numerator is bp ≥ p, which exceeds UV in a block with hits.
     * DFI Thm 2 can save only if C̄ ≲ p^{1/37}, and Bettin–Chandee only if C̄ ≲ p^{1/21}.
     * DFI Thm 1 *does* save in skew blocks with max(U,V) > (bp)^{1/2+δ} and min(U,V) → ∞, e.g. U ≈ p^{1/5}, V ≈ p^{3/5},
       b ≪ 1, a saving of p^{1/10}. (An earlier version misquoted Thm 1 as a product; corrected after the cross-model
       review.)
     * Such a saving is for the KF sum K(b) only, not for N. The one-relation ceiling (b) still applies, and coupling
       the second relation or summing over all b < 2V would need further work.
   * EVIDENCE (F3): fixed-p KF sums for b ≤ 16 are square-root size (rms 0.57–0.99·√(#pairs)). N₁ equals its
     zero-frequency term with sd ≈ 17 at U = V = 1000.
5. **Prop Q (PROVED bookkeeping; reading Assessment).** In the SL₂ form, (★) at level c selects one Bruhat double coset of
   S(·,·;c), d ≡ −1, and inside it imposes the lattice condition "top-right entry = p". In the two natural orientations
   the Kloosterman modulus is p itself (single modulus) or the level c (one integer cp + 1 per level). No direct
   fixed-index Kuznetsov application is exhibited.
6. **(S2) benchmark.** The checked tools do not give R(p) ≪ p^{1/3−η}, and the literature search found no such result
   (not exhaustive).
   * Heath-Brown's Theorem 14, applied directly to 4xyz − x − y = p, gives an upper bound
     ≪_ε V^{2/(3√3)+ε}(log p)⁵ ≈ p^{0.385+ε} on the number of auxiliary curves (relative to the quoted statement). This
     black-box application does not reach p^{1/3}.
7. **Thm E (PROVED).** HYP Thm 6(a,b) holds in all three coordinate systems (u,B), (u,C), (B,C). Square-root max-input
   in the Fejér route gives ≫ (two-side product)^{1/2} ≥ min of those two sides, so it never beats HYP Thm 1.

**What survives (§8).** For the upper bound (S1): HYP R1/R2, and joint/nonlinear estimates. For positivity, all of the
following remain open. This investigation found no uniform method for any of them; isolated examples at single primes
exist.
* arguments with a positive main term that inject the arithmetic of p (primality, quadratic character) at the top of the
  spectrum: frequencies ≥ q_max/2 or primitive conductors;
* negative-mean certificates shown to be positive at the given p, i.e. with oscillatory part A(p) > −|𝒫|·ĝ_0;
* methods not passing through a linear Fourier expansion of the divisibility indicator.

## 1. Statements attacked

Notation as in HYP §2:
* p ≥ 5 prime; U, V ≥ 1 integers; block 𝔅 = (U,2U] × (V,2V] ∩ ℤ²; pair π = (u,B); q = q_π = 4uB; s = s_π = u + B;
  n ∈ ℤ.
* N(n) = N_𝔅(n) = #{π ∈ 𝔅 : q | n + s}. This includes the 4-condition, since q = 4uB.
* q_min = 4(U+1)(V+1) and q_max = 16UV are the extreme moduli, attained at (U+1, V+1) and (2U, 2V).
* C̄ = p/(4UV) is the typical level. The balanced block is U = V ≈ p^{1/4} (C̄ ≍ p^{1/2}); the cube block is
  U ≍ V ≍ C̄ ≍ p^{1/3}.
* HYP Thm 1 (elementary): N ≤ p^{o(1)}·min(U, V, C̄ + 1).
* The blocks with U or V = 1/2 (coordinate 1) are excluded here.

The conductor (Ramanujan) dual of the block count is the exact identity (HYP (2.1))

  N(n) = Σ_{d ≥ 1} Σ*_{a mod d} e(an/d)·D(d,a),  D(d,a) := Σ_{π ∈ 𝔅 : d | q_π} q_π⁻¹ e(a s_π/d).          (1.1)

So N, as a function of the integer n, is a trigonometric polynomial whose spectrum lies in the Farey fractions a/d with
d ≤ q_max. The archimedean (sawtooth) form is HYP (E3): N(n) = #{π : F_π(n) ∈ ℤ} with F_π(n) = (n + s_π)/q_π, and
S_h(n) := Σ_π e(hF_π(n)).

"Summing over conductors (frequencies) before bounding" means the following. Evaluate a weighted sum of the dual (1.1), or
of the S_h, or of a Kloosterman-fraction form of N, that couples different conductors, frequencies or moduli, and bound
that, rather than each conductor separately (that is HYP Thm 5).

* **(S1) Cross-conductor / cross-frequency power saving at fixed p.** ∃ η > 0 such that for every large prime p,
  |N_bal(p) − M| ≤ p^{1/4−η}, by an argument of the kind just described.
  * M ≈ 0.146 is the block's prime-model mean (HYP M₀).
  * Since M = O(1), this is the *upper bound* N_bal(p) ≪ p^{1/4−η}.
  * The same question is asked for every other block, against its trivial bound min(U, V, C̄).
  * Positivity (N ≥ 1, the direction ES needs) is treated alongside (§§5–6).
* **(S2) Benchmark.** ∃ η > 0 with |E(p)| = |R(p) − M(p)| ≤ p^{1/3−η} for all large p, by *any* known theorem.
* **(S3) Implementation classes**, each to be settled by a power saving or by a scoped statement:
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
the standard implementations of (R0) named in the lane brief, since they sum over conductors, moduli or frequencies
jointly. Earlier treatment of them amounts to two remarks:
* PARITY_AUDIT B7: "the Kloosterman fraction degenerates";
* BRAINSTORM/s8_volume_dfi R268: DFI is trivial for MN = o(p^{36/37}).

## 3. Falsifiers (EVIDENCE)

### 3.1 F1: do conductor pieces cancel against each other at a fixed prime?

**Program.** `scripts/z53_hypkloost_conductor.c` computes, for each n, the exact Ramanujan expansion of N_bal(n) (sharp
balanced block) in long double.
* c_d(m) is computed multiplicatively from v_ℓ(m): for ℓ^e ∥ d, c_{ℓ^e}(m) = φ(ℓ^e), −ℓ^{e−1} or 0 according as
  ℓ^e | m, ℓ^{e−1} ∥ m, or neither.
* The terms are grouped into absolute bins j = ⌊log₂ d⌋ and into relative-depth bins k = ⌊log₂(q/d)⌋ (k = 0 is d = q).
* The internally accumulated total equals N(n) to the 9 printed decimals in all 10 800 cases (floating-point evidence).
  The reviewer re-checked the program against a direct Ramanujan-sum computation at 8 small n (U = 2, V = 3); the maximal
  discrepancy was 4·10⁻¹¹.

**Inputs and analysis.**
* Inputs: `scripts/z53_hypkloost_inputs.py`, which reproduces the lists byte-for-byte; the n are also column 1 of
  `data/z53/hypkloost/c_*.tsv.gz`.
* Statistics and bootstrap: `scripts/z53_hypkloost_cond_analyze.py` → `data/z53/hypkloost/cond_stats.txt`. The bootstrap
  draws 400 percentile resamples with numpy default_rng(53), processing the sets in a fixed order.
* Data sets: 3000 consecutive primes from 10¹² (U = 1000) and from 10¹⁰ (U = 316). Controls: 600 odd squares m² ≥ 10¹²
  and ≥ 10¹⁰; 600 near-square primes m² + k (k ≤ 40) above 10¹²; 1500 random n ≡ 1 (4) at each scale.

**What orthogonality does and does not predict.**
* PROVED (Parseval): under n uniform over *all* residues mod L = lcm{q_π}, pieces supported on disjoint sets of reduced
  conductors are uncorrelated, so Var(N) = Σ_j Var(P_j^{abs}) for the absolute bins.
* Relative-depth bins share conductors across pairs. They are not orthogonal even in that model (reviewer's exact check at
  U = V = 2: cross share −0.018).
* Primes and n ≡ 1 (4) are conditioned measures, for which no exact orthogonality holds.
* So the table below reports an empirical quantity: the cross-covariance share (Σ_{k≠l} Cov)/(Σ Var). A large negative
  share would indicate aggregate cancellation between conductor ranges.

| set | Σ Var (rel. bins) | Var(N) | cross share, relative bins [95 % bootstrap] | cross share, absolute bins [95 % bootstrap] |
|---|---|---|---|---|
| primes 10¹² | 0.276 | 0.315 | +0.142 [+0.013, +0.263] | +0.149 [+0.019, +0.278] |
| random n ≡ 1 (4), 10¹² | 0.257 | 0.243 | −0.053 [−0.238, +0.106] | −0.027 [−0.208, +0.135] |
| near-square primes 10¹² | 0.269 | 0.296 | +0.103 [−0.136, +0.342] | +0.097 [−0.163, +0.375] |
| primes 10¹⁰ | 0.261 | 0.270 | +0.036 [−0.071, +0.148] | +0.018 [−0.089, +0.139] |
| random n ≡ 1 (4), 10¹⁰ | 0.261 | 0.271 | +0.039 [−0.189, +0.295] | +0.054 [−0.185, +0.301] |
| **odd squares 10¹²** | 0.175 | **0** | **−1** (N ≡ 0) | −1 |
| odd squares 10¹⁰ | 0.198 | 0 | −1 | −1 |

(The bootstrap treats rows as exchangeable. Consecutive primes are not an established i.i.d. sample, so the intervals are
rough uncertainty indications, not certified coverage.)

* **Primes.**
  * Sample sds of the relative bins k = 0, 1, 2, 3 are 0.30, 0.27, 0.22, 0.17. The variance is spread over q/d ≤ 2⁶.
  * The cross share is near 0 or positive. There is no aggregate variance reduction between conductor ranges in these
    samples.
  * corr(N, P₀ + … + P_k) = 0.61, 0.76, 0.88, 0.94, 0.97 for k = 0…4 (10¹²). N = 0 in 92.4 % of the rows.
* **Low conductors (10¹², U = 1000).** Absolute bins d < 2¹⁰ ≈ U have sd ≤ 0.003 at primes, consistent with HYP Thm 3 (here sharp
  cutoffs). At random n they have sd 0.019 in bin j = 1; HYP Thm 3 needs gcd(n, d) = 1.
* **Odd squares.** The pieces have comparable variance, but the total is identically 0 (T1, at every square). At primes
  the total is 0 in 92 % of rows too; the difference is that T1 makes it 0 universally.
  * A method that bounds conductor ranges separately, uniformly in n, cannot see this.
  * Aggregate cancellation between conductor ranges is exactly what squares exhibit, and what these prime samples do not.

**Reading (Assessment).** In these samples the conductor decomposition of N at primes behaves like a superposition of
order-one pieces without aggregate cancellation. The one universal exact cancellation in sight is T1's. This is evidence,
not a theorem: a pointwise argument could still find cancellation that the variance does not show, and individual
covariances could cancel each other.

### 3.2 F3: Kloosterman-fraction sums at fixed p

Program: `scripts/z53_hypkloost_kf.c`; data: `data/z53/hypkloost/kf_*.tsv`.
* Quantity: K(b) = Σ_{u∼U, B∼V, (u,B)=1} e(bp ū/B), with ū the inverse of u mod B and 1 ≤ b ≤ 16. This is the DFI-type
  bilinear sum in the detection of B | p + u.
* Windows: the first 200 primes > 10¹² (U = V = 1000) and the first 100 primes > 10¹² in the skew blocks (U,V) =
  (100, 10⁴) and (10⁴, 100).
* Size: |K(b)|/√(#coprime pairs) has rms 0.567, 0.988 and 0.786 (max 1.66, 2.86, 2.19). This is square-root size for
  these b and these primes. It is not a lower bound for what a KF estimate could give.
* N₁ = #{π : B | p + u} versus the full additive zero-frequency term Σ_π 1/B:
  * the zero-frequency terms are 692.90, 69.31 and 6906.53 in the three blocks;
  * N₁ − Σ_π 1/B has sd 16.8, 11.4 and 4.4 (range −42.9…+37.1 in the balanced block).
* Observed N ∈ {0, 2} (balanced) and {0, 1, 2} (skew).

## 4. Exact objects

**(O1) Ramanujan dual.** This is (1.1). Grouped by pairs, N(n) = Σ_π q⁻¹ Σ_{d | q} c_d(n + s).

**(O2) Two-relation Kloosterman-fraction form** (Thm K(a) below). For coprime u, B ≥ 2:

  1[u | p+B]·1[B | p+u] = (uB)⁻¹ Σ_{a=0}^{u−1} e(a·(p+u+B)/(uB)) · Σ_{c mod B} e(c(1 + p ū)/B),               (4.1)

where ū is the inverse of u mod B.
* For coprime pairs and p prime, the left side is 1[uB | p+u+B]. It does **not** contain the 4-condition
  4 | (p+u+B)/(uB): for p = 17, (u,B) = (3,4) satisfies both relations but not the 4-condition (HYP (E4)).
* The block count is N = Σ_{π coprime} (4.1)·1[4 | (p+u+B)/(uB)]. Non-coprime pairs never contribute (HYP Lemma 0).
* The archimedean factor is a Dirichlet kernel of length u in F′ = (p+u+B)/(uB). The arithmetic factor is the one-sided
  Kloosterman-fraction detector of B | p + u, with numerator c·p.

**(O3) One-sided bilinear sum.** Assume 2U, 2V < p. For coprime pairs, 1[B | p+u] = B⁻¹Σ_{b mod B} e(b(1 + pū)/B).
Non-coprime pairs have B ∤ p + u, since gcd(u,B) | p would force gcd = 1 when u, B < p. (Without 2U, 2V < p this fails:
for p = 5, U = 10, V = 5 the pair (15,10) has gcd 5 and 10 | 20.) Hence

  N₁ = Σ_{π : (u,B)=1} B⁻¹ + Σ_{b ≥ 1} Σ_{B > b} B⁻¹ e(b/B) Σ_{u : (u,B)=1} e(bp ū/B).

* The first term is the coprime zero mode. With m := min(U,V) it equals (6/π²)log 2·U + O(U log(2m)/m).
  * For U ≥ V use #{u ∈ (U,2U] : (u,B) = 1} = Uφ(B)/B + O(τ(B)) and Σ_{V<B≤2V}φ(B)/B² = (6/π²)log 2 + O(log V/V).
  * For V ≥ U reverse the roles: Σ_{B∈(V,2V], (B,u)=1} 1/B = (φ(u)/u)log 2 + O(τ(u)/V) (Möbius and partial summation),
    and Σ_{U<u≤2U}φ(u)/u = (6/π²)U + O(log U).
* The second term is a family of DFI forms Σ α_u β_B e(a ū/B), with α_u = 1, β_B = 1[B > b]e(b/B)/B and numerator a = bp.
  These are the "coefficients we control".

**(O4) Unbalanced blocks V ≥ 2U.** For fixed u the admissible B run through the progression B ≡ −p (mod u) in (V, 2V],
which has ⌊V/u⌋ or ⌊V/u⌋ + 1 terms. Then N = Σ_u Σ_{B ≡ −p (u)} 1[4uB | p+u+B]. Detecting the progression by additive
characters mod u gives phases e(aB/u + b(p+u)/B), and detecting B | p+u by Kloosterman fractions gives (O2) again.

**(O5) Trial form, single modulus variable.** R(p) = #{m ≡ 3 (mod 4) : r_m := (−p mod m) ≥ 1 and 4r_m | m + 1}. The
moduli m = 4uC − 1 range freely; p enters only through p mod m.
* Proof: m = 4uC − 1 | p + u forces u ≡ −p (mod m), and 0 < u < m, so u = r_m. Conversely r_m and C = (m+1)/(4r_m)
  determine B = (p + r_m)/m.
* The Kloosterman fraction of this form is degenerate: \overline{4C} ≡ u (mod m). This is PARITY_AUDIT B7.

## 5. Linear functionals of the dual (class L)

### 5.1 Theorem B — frequency weights, periodisation, and positive-mean certificates (PROVED)

Let 𝒫 be a nonempty finite set of pairs of positive integers (a block 𝔅, a union of blocks, or a finite candidate set
for R(p)). Put q_π = 4uB, F_π(n) = (n + s_π)/q_π, S_h(n) = Σ_{π∈𝒫} e(hF_π(n)), and let q_min, q_max be the least and
largest q_π.

Let H ≥ 0 be an integer and G(x) = Σ_{|h|≤H} ĝ_h e(hx) a real trigonometric polynomial. Let g: ℝ → ℝ be continuous with
g(t) = O((1+|t|)⁻²), whose Fourier transform ĝ(ξ) = ∫g(t)e(−ξt)dt is continuous, compactly supported, and satisfies
ĝ(h) = ĝ_h for integers |h| ≤ H and ĝ(h) = 0 for integers |h| > H.
* Such g exists for every G: interpolate the coefficients by smooth bumps around the integers, respecting
  ĝ(−ξ) = \overline{ĝ(ξ)}.
* The Fejér pair g(t) = (H+1)(sin π(H+1)t/(π(H+1)t))², ĝ(ξ) = (1 − |ξ|/(H+1))₊ is an example. Its support is [−H−1, H+1]
  and it vanishes at ±(H+1).

**(a) Periodisation identity.** For every integer n,

  Σ_{|h|≤H} ĝ_h·S_{−h}(n) = Σ_π G(−F_π(n)) = Σ_{π∈𝒫} Σ_{ℓ ∈ ℤ : q_π | n+ℓ+s_π} g(ℓ/q_π).                (5.1)

* The right side is a pair-weighted count: pair π contributes g(ℓ/q_π) at each integer n + ℓ where π is a solution.
* For the Fejér pair the weights are ≥ 4(H+1)/π² for |ℓ| ≤ q_π/(2H+2) and ≤ q_π²/(π²(H+1)ℓ²) for all ℓ ≠ 0. For this
  kernel (5.1) is a smoothed count over a window of length ≍ q_π/H around n.
* For general g no localisation is claimed: g is not determined by G.

**(b) Positive-mean threshold.** Call G a *frequency certificate* (for 𝒫) if G(0) > 0 and G(x) ≤ 0 at every
x ∈ T_𝒫 := ∪_{π∈𝒫}(q_π⁻¹ℤ ∖ ℤ). For such G, Σ_π G(−F_π(n)) ≤ G(0)·N(n) for all n. So positivity of the frequency side at
n certifies N(n) ≥ 1. Then:
* if H < q_max/2, the mean ĝ_0 = ∫₀¹G is ≤ 0;
* if H < min(q_min, q_max/2), then for n uniform modulo L = lcm{q_π}, E[Σ_π G(−F_π(n))] = |𝒫|·ĝ_0 ≤ 0.

**(c) Sharpness.** There is a frequency certificate of degree H₀ = q_max/2 with ĝ_0 > 0, and it remains one for every
degree allowance H ≥ H₀.

*Proof.*
(a) Fix π and put F = F_π(n).
* Poisson summation applied to t ↦ g(t − F) gives Σ_{k∈ℤ} g(k − F) = Σ_{h∈ℤ} ĝ(h)e(−hF) = Σ_{|h|≤H} ĝ_h e(−hF). Both
  sides converge absolutely, because g = O(t⁻²) and ĝ is continuous with compact support.
* k − F = (kq − n − s)/q. Putting ℓ := kq − n − s is a bijection from ℤ onto {ℓ : q | n + ℓ + s}, and k − F = ℓ/q.
* The left side is G(−F) by definition. Sum over π.

(b), first claim.
* Let π₀ attain q_max =: q₀, which is a multiple of 4. Put Q′ := q₀/2, an integer > H.
* The Q′-point quadrature is exact in degree ≤ H: for 0 < |h| ≤ H < Q′, e(hx) sums to 0 over any coset of Q′⁻¹ℤ/ℤ.
  Hence ĝ_0 = (1/Q′)Σ_{k mod Q′} G((k + 1/2)/Q′).
* Each sample point is (2k+1)/q₀ ∈ q₀⁻¹ℤ ∖ ℤ ⊆ T_𝒫, because the numerator is odd and q₀ is even. So every sample value
  is ≤ 0, and ĝ_0 ≤ 0.

(b), second claim.
* n mod q_π is uniform, so E[G(−F_π(n))] = q_π⁻¹Σ_{r mod q_π}G(r/q_π) = Σ_{j∈ℤ} ĝ_{jq_π}.
* For q_π ≥ q_min > H only j = 0 survives, so the expectation is ĝ_0 for every pair. It is ≤ 0 by the first claim, since
  H < q_max/2.

(c)
* Put H₀ = q_max/2 and choose δ with 1/(q_max + 2) < δ < 1/q_max.
* The Selberg minorant S⁻ of the arc [−δ, δ] (mod 1) of degree H₀ satisfies S⁻ ≤ 1_{[−δ,δ]} and
  ∫S⁻ = 2δ − 1/(H₀+1) = 2δ − 2/(q_max+2) > 0. (Montgomery, *Ten Lectures*, Ch. 1; Vaaler, BAMS 12 (1985); as quoted in
  HYP Thm 6(a).)
* Every point of T_𝒫 is at distance ≥ 1/q_max > δ from ℤ, so S⁻ ≤ 0 on T_𝒫.
* Since H₀ < q_max, quadrature on the full q_max-grid is exact: q_max∫S⁻ = Σ_{r mod q_max}S⁻(r/q_max) ≤ S⁻(0), because
  every r ≢ 0 gives a point of T_𝒫. Hence S⁻(0) > 0, and S⁻ is a certificate with positive mean. ∎

*Check of (b)–(c) by linear programming (EVIDENCE).* `scripts/z53_hypkloost_certificate_lp.py` →
`data/z53/hypkloost/certificate_lp.txt`.
* For the blocks (U,V) = (2,2), (2,3), (3,3) (q_max = 64, 96, 144) we maximise ĝ_0 over even polynomials of degree H
  with G ≤ 0 on T_𝔅 and G(0) ≤ 1. This is the closed relaxation of the certificate condition, which admits G(0) = 0.
  Below q_max/2 the solver returns mean 0, with G(0) = 0 at H = 30, 46, 63, 70 but G(0) = 1 at H = 31, 47, 71. The
  theorem only forces nonpositive mean.
* The solver is floating-point HiGHS with its default tolerances, and we impose the artificial box bound
  |coefficients| ≤ 10. The outputs are approximate.
* The maximum is 0 for every H < q_max/2 tested (H = 30, 31; 46, 47; 63, 70, 71).
* It is positive from H = q_max/2 on (0.0053, 0.0017, 0.0007 at H = 32, 48, 72).
* For H ≥ q_max the box bound is hit (an artefact: T is finite).
* The (2,2) row at H = 32 also shows that the expectation claim needs H < q_max/2 and not merely H < q_min = 36.

*Check of (a) (EVIDENCE).* `scripts/z53_hypkloost_window_check.py` → `data/z53/hypkloost/window_check.txt`.
* (5.1) holds with the Fejér pair in 5 cases (n up to 4·10⁶, H up to 200), up to the truncation tail of the ℓ-sum:
  differences 1.2·10⁻³–5.4·10⁻³, below the tail bounds 2.0·10⁻³–1.1·10⁻².
* E_n S_h = Σ_{π : q_π | h} e(hs_π/q_π) was checked by exact averaging over n mod L (L = 2880) for
  h ∈ {1, 2, 5, 47, 48, 96}. It vanishes for 0 < h < q_min = 48.

**Low-degree certificates can still be positive at a given n.** Take U = 1, V = 2, p = 19, so the pairs are (2,3) and
(2,4), q ∈ {24, 32}, q_max/2 = 16. Put c = cos(2π/32), t = cos(2π·25/32) and

  G(x) = (cos 2πx − c)(cos 2πx − t)².

* G has degree 3, G ≤ 0 on T (checked: max_T G = 0), and G(0) = 0.01245 > 0.
* At p = 19 the phases are F = 1 and 25/32, so Σ_π G(−F_π) = G(0) > 0, certifying N(19) ≥ 1. Indeed 24 | 19 + 2 + 3.
* Its mean is negative, as (b) requires.
* So (b) obstructs *positive-mean* certificates only. Write the frequency side as |𝒫|ĝ_0 + A(p), with
  A(p) = Σ_{0<|h|≤H} ĝ_h S_{−h}(p). A low-degree certificate with A(p) > −|𝒫|ĝ_0 is not excluded. (Example due to the
  hostile reviewer.)
* A(p) > 0 alone is not enough. For the same G at p = 17, A(17) = 1.215 > 0 but −2ĝ_0 = 1.446, so the frequency side is
  −0.231, and indeed N(17) = 0 (second-pass review).

**Reading.**
* With the Fejér kernel and frequencies |h| ≤ H, the frequency side is a smoothed count over windows of length ≍ q/H ≍ UV/H
  around p. For H ≤ (UV)^{1−η} these windows contain ≥ (UV)^η integers, almost all composite. This is the archimedean form
  of B6, for this kernel.
* Positive-mean certificates for a block need H ≥ q_max/2 = 8UV. For q_min ≤ H the expectation of a certificate is
  q_π⁻¹Σ_r G(r/q_π) per pair, which is ≤ G(0)/q_π. So for G(0) = 1 the expectation is at most E N under n uniform mod L,
  which equals Σ_{all π} 1/q_π = (H_{2U} − H_U)(H_{2V} − H_V)/4 → (log 2)²/4 ≈ 0.120.
  * That is the unconditioned model. The prime model gives ≈ 0.146 (HYP M₀ = Σ_adm 1/φ(q)).
  * In the balanced block N = 0 at ≈ 92–93 % of primes (HYP R4; F1). So a single-block positive-mean certificate cannot
    work for most primes. For R(p), (b) applied to the candidate set {(u,B) : 4uB ≤ p + u + B} (q_max ≈ 4p/3) requires
    degree ≍ p for a positive-mean certificate.
* What (b) leaves open (Assessment): certificates whose positivity at p comes from the oscillatory part, i.e. a lower
  bound for a signed exponential sum at one p. No method for such lower bounds is known here. HYP Thm 6's max-|S_h| floor
  does not apply to signed weighted sums (HYP §3.6).
* Theorem B concerns *lower* bounds. Majorants with small H (the upper bound (S1)) are unaffected: HYP Thm 6(a) with
  beyond-square-root input on a short segment (R1) stays sufficient.

### 5.2 Theorem C — conductor projections and the primitive-conductor lemma (PROVED)

**(a) Class averages.** Let M ≥ 1. Let Λ_M(n) := Σ_{d|M} Σ*_{a mod d} e(an/d)D(d,a) be the full, unweighted projection of
(1.1) onto all conductors dividing M. Then for every integer n,

  Λ_M(n) = Σ_π gcd(q_π, M)/q_π · 1[gcd(q_π, M) | n + s_π] = E[N(n′) | n′ ≡ n (mod M)],

with n′ uniform over the residues mod L′ := lcm(M, all q_π) that are ≡ n (mod M).
* Any weighted sum over frequencies with denominators dividing M depends only on n mod M (congruence data, B1). Only the
  full unweighted projection is literally the class average.
* (Example: keeping only d ∈ {1, 2, 3} for a pair with q = 24 gives 1/6 at m = 0, while the M = 6 projection gives 1/4.)
* The low-conductor statement of HYP Thm 3 is for the cutoff d ≤ D ≤ min(U,V)^{1−ε}, with smooth weights and gcd(n, d) = 1
  for d ≤ D. It is not a statement about all divisors of lcm(1, …, D).

**(b) Lemma (primitive conductor).** Let q ≥ 2. Let f: ℤ/q → ℝ satisfy f ≤ 1_{0}, and suppose f has no primitive
frequency: f̂(a) := q⁻¹Σ_m f(m)e(−am/q) = 0 whenever gcd(a, q) = 1. Then mean(f) = f̂(0) ≤ 0.
* For f of the Ramanujan form m ↦ q⁻¹Σ_{d|q} λ(d)c_d(m), the hypothesis means exactly λ(q) = 0, since c_q carries the
  primitive frequencies and c_d (d < q) only non-primitive ones.

**(c) Consequence.** Call functions f_π: ℤ/q_π → ℝ with f_π ≤ 1_{0} a *pairwise conductor certificate*. Then
Λ(n) := Σ_π f_π(n + s_π) ≤ N(n), and E[f_π] = mean(f_π) for n uniform mod q_π.
* By (b), every pair whose f_π has no primitive frequency contributes ≤ 0 in mean. A positive-mean pairwise certificate
  needs, for each pair contributing positive mean, primitive frequencies a/q_π.
* For Ramanujan-form weights this is the top conductor d = q_π. There the dual term is one complete Ramanujan sum
  λ_π(q_π)c_{q_π}(n + s_π)/q_π per pair. By HYP Thm 5 each conductor ≥ q/K carries ≤ K·max_{t≤4UV}τ(t) pairs, which is
  K·p^{o(1)} when UV ≤ p.
  * That is a fixed-conductor count. It does not exclude summation across many conductors.
* For general f_π the primitive component is an arbitrary combination of the e(am/q_π), gcd(a, q_π) = 1, not necessarily
  a multiple of c_{q_π}.
* Negative-mean certificates without primitive frequencies can be positive at a given n. For the pair (2,3), q = 24, put
  f(m) = 1[8 | m] + 1[3 | m] − 1 ≤ 1[24 | m]. Its expansion is −13/24 + (c₂ + c₄ + c₈)/8 + c₃/3, so its conductors are 1, 2, 3, 4, 8 (not 24). It has f(24) = 1 and
  mean −13/24. At p = 19 it
  certifies the hit (2,3). (Example due to the hostile reviewer.)
* (b) is stronger than requiring the lcm of the support to be q. Example: q = ℓ₁ℓ₂ with distinct primes and support
  {1, ℓ₁, ℓ₂}. The lcm is q, but every minorant a + b·1[ℓ₁|m] + c·1[ℓ₂|m] ≤ 1[q|m] has mean ≤ max(0, 1/ℓ₁ + 1/ℓ₂ − 1) = 0.

*Proof.*
(a) For a pair π, the frequencies a/d with d | M occurring in π's expansion are those with d | g, g := gcd(q, M). Hence
Σ_{d | g} c_d(m) = g·1[g | m]. Dividing by q gives the first formula. For n′ uniform on its class mod M inside ℤ/L′,
P(q | n′ + s) = 1[g | n + s]·(g/q), by CRT on q and M. Summing over π gives the second formula.

(b) Write q = ∏_{i=1}^k ℓ_i^{e_i}. Let H_i ⊂ ℤ/q be the subgroup of order ℓ_i, i.e. the multiples of q/ℓ_i.
* *f is a sum of H_i-invariant functions.* A non-primitive frequency a has some ℓ_i | a, so m ↦ e(am/q) has period q/ℓ_i,
  i.e. it is invariant under translation by H_i. Assign each such term to one such i. Then f = Σ_i g_i with each g_i
  H_i-invariant.
* *A test measure.* Let u be the uniform probability measure on ℤ/q. In the CRT coordinates ℤ/q = ∏ ℤ/ℓ_i^{e_i}, put
  a_i := ℓ_i^{e_i−1} (an element of order ℓ_i in the i-th factor) and

    ν := u + (−1)^{k+1} q⁻¹ ⊗_{i=1}^k (δ_{a_i} − δ_0).

* *ν is a probability measure with ν(0) = 0.* The signed part takes values ±1/q on the 2^k points with i-th coordinate in
  {0, a_i}, and 0 elsewhere. At 0 its value is (−1)^{k+1}(−1)^k/q = −1/q. Hence ν(0) = 0. All values of ν lie in
  {0, 1/q, 2/q}. The total mass is 1, because each factor δ_{a_i} − δ_0 has mass 0.
* *ν integrates H_i-invariant functions like u.* In the i-th coordinate, δ_{a_i} − δ_0 has zero mass on every H_i-coset,
  because 0 and a_i lie in the same coset. So Σ_m (ν − u)(m)g_i(m) = 0 for every H_i-invariant g_i.
* *Conclusion.* mean(f) = Σ_m u(m)f(m) = Σ_m ν(m)f(m) ≤ Σ_m ν(m)1_{0}(m) = ν(0) = 0.

(c) is (b) applied pair by pair. For the ℓ₁ℓ₂ example, the constraints are a ≤ 0, a + b ≤ 0, a + c ≤ 0 and a + b + c ≤ 1,
and the objective is a + b/ℓ₁ + c/ℓ₂. The maximum is attained at a vertex: either 0 (at a = b = c = 0) or
1/ℓ₁ + 1/ℓ₂ − 1 < 0 (Bonferroni, a = −1, b = c = 1). ∎

**Reading.**
* Unweighted conductor truncation to the divisors of M is the class average of N over n ≡ p (mod M): congruence data.
* A positive-mean pairwise lower bound must use primitive frequencies of the pairs it relies on, i.e. the top of the
  divisor lattice.
* (b) is the conductor analogue of Theorem B(b). Both are uncertainty statements about minorants of a point mass, and both
  constrain positive-mean arguments only. A negative-mean certificate must overcome its negative constant term.

### 5.3 Theorem E — the max-input Fejér ceiling in every coordinate system (PROVED)

Take a coordinate pair (X, Y) ∈ {(u,B), (u,C), (B,C)} of a block with integer sides. The phase functions are
* F(u,B) = (p+u+B)/(4uB) (HYP),
* G(u,C) = (p+u)/(4uC − 1),
* G′(B,C) = (p+B)/(4BC − 1).

Let 𝒫 be the box of integer pairs: for (u,C), u ∈ (U, 2U] and C in the block's level range
[p/(16UV), (p+2U+2V)/(4UV)], which has O(C̄ + 1) integers. Put S_h := Σ_{𝒫} e(h·phase) and Δ_H := max_{1≤h≤H}|S_h|.

(a) N ≤ |𝒫|/(H+1) + H·Δ_H/(H+1) for every H ≥ 1.

(b) For H + 1 ≥ 2|𝒫|, Δ_H ≥ |𝒫|^{1/2}/2.

(c) Hence square-root max-input Δ_H ≍ |𝒫|^{1/2} yields only N ≪ |𝒫|^{1/2} ≥ min(sides of 𝒫), which is ≫ min(U, V, C̄ + 1).
So, in the Fejér/max-Δ implementation, square-root input never beats HYP Thm 1 in any block or coordinate system. It
matches the trivial bound up to constants only when the two sides of 𝒫 are comparable *and* the third side is not
smaller in order.

*Proof.*
* A hit is a point of 𝒫 whose phase is an integer. For (u,C) and (B,C) the size condition on the third coordinate is
  dropped, which only increases the count.
* (a) is HYP Thm 6(a), Fejér form: 1[t ∈ ℤ] ≤ K_H(t)/(H+1) for all real t, with K_H ≥ 0 and K_H(0) = H + 1. Sum over 𝒫 and
  use |S_h| ≤ Δ_H for 0 < |h| ≤ H; the nonzero Fejér weights sum to H.
* (b) is HYP Thm 6(b) verbatim. Σ_{|h|≤H}(1 − |h|/(H+1))|S_h|² = Σ_{x,x′∈𝒫} K_H(phase(x) − phase(x′)) ≥ (H+1)|𝒫|;
  subtract the h = 0 term |𝒫|² ≤ (H+1)|𝒫|/2 and divide by 2H. The proof does not use the specific phase. ∎

## 6. Kloosterman fractions (class K) and Kuznetsov (class Q)

### 6.1 Theorem K (PROVED; (c) relative to the quoted statements)

(a) **Reciprocity collapse.** Let u, B ≥ 2 be coprime. Let B̄ ∈ [1, u) be the inverse of B mod u and ū ∈ [1, B) the
inverse of u mod B. Then B̄/u + ū/B = 1 + 1/(uB). Hence, for all integers a, b,

  e(ap B̄/u + bp ū/B) = e(ap/(uB))·e((b − a)p ū/B),

and identity (4.1) holds.

(b) **One-relation ceiling, for the implementation "zero-frequency term + absolute error".** Let N₁ := #{π ∈ 𝔅 : B | p+u}
and N₁′ := #{π ∈ 𝔅 : u | p+B}.
* With the ordinary additive detector B⁻¹Σ_{b mod B}e(b(p+u)/B), the zero-frequency term is
  Σ_π 1/B = U(H_{2V} − H_V) ≥ U/2. Symmetrically Σ_π 1/u ≥ V/2 for N₁′.
* With the coprime Kloosterman-fraction detector (O3, assuming 2U, 2V < p), it is
  Σ_{(u,B)=1} 1/B = (6/π²)log 2·U + O(U log(2m)/m), m = min(U,V).
* So a bound N ≤ N₁ ≤ (zero-frequency term) + (nonnegative error allowance), or the same through N₁′, outputs
  ≥ min(U,V)/2 (additive), resp. ≥ (6/π²)log 2·min(U,V) − O(min(U,V)·log(2m)/m) (KF). Both are ≫ min(U, V, C̄ + 1)
  once m is large.

The ceiling does **not** apply to every use of one relation.
* An argument that evaluates N₁ exactly outputs N₁. Deterministically N₁ ≥ Σ_{B∼V}⌊U/B⌋ ≥ U/2 − V (≥ U/4 once U ≥ 4V;
  symmetrically for N₁′). In the balanced block there is no useful deterministic lower bound: N₁ = 0 for U = V = 2,
  p = 19. EVIDENCE (F3): at U = V = 1000, p ≈ 10¹², the sample sd of N₁ − Σ1/B is 16.85.
* Genuinely coupled estimates are not covered: the second relation decomposed into separable pieces, further averaging,
  or weighted joint bounds.

(c) **Numerator constraints (relative to the source statements as re-checked by the cross-model review; necessary
conditions only, except the DFI Thm 1 saving, which is an actual saving for K(b)).** Consider
K(b) = Σ_{u∼U, B∼V, (u,B)=1} α_u β_B e(bp ū/B) with b ≥ 1.
* The numerator is a = bp ≥ p. In a block containing a hit, 4UV < 4uB ≤ p + u + B ≤ p + 2U + 2V, so a ≥ UV(1 + o(1)).
* Write ‖·‖ for ℓ²-norms. The Cauchy–Schwarz trivial bound is ‖α‖‖β‖(UV)^{1/2}.
* *DFI Thm 1* (source (1.4), printed p. 24, a *sum*) gives ‖α‖‖β‖[(U+V)^{1/2} + (1 + a/UV)^{1/2}min(U,V)](UV)^ε.
  * Write s = min(U,V) and L = max(U,V). Up to (UV)^ε, the ratio to the trivial bound is √(1/s + 1/L) + √(s/L + a/L²).
  * This is < 1 (a power saving) iff s → ∞ polynomially, s/L → 0 and a ≤ L^{2−δ}. With a = bp that requires
    L ≥ (bp)^{1/2+δ′}.
  * Example: U ≈ p^{1/5}, V ≈ p^{3/5}, b ≪ 1 gives ratio ≍ p^{−1/10}. Here both sides are < p, UV ≪ p and C̄ ≈ p^{1/5}/4.
  * The saving disappears for b ≳ L²/p, so it does not cover all detection frequencies b < 2V.
  * It is a bound for the KF sum K(b), not for N. A route through N₁ alone is still capped by (b).
  * The earlier statement "never below the trivial bound" rested on a misquotation (product instead of sum) in
    LIT_CHECK.md and is retracted.
* *DFI Thm 2* gives ‖α‖‖β‖(a + UV)^{3/8}(U+V)^{11/48+ε}. With a ≥ p and U + V ≥ 2(UV)^{1/2}, it is below the trivial
  bound only if UV > 2^{22/37}p^{36/37}, i.e. C̄ < p^{1/37}.
* *Bettin–Chandee Thm 1* (trilinear, a = b ∈ [A/2, A], ϑ = p) gives ‖α‖‖β‖‖ν‖(1 + pA/UV)^{1/2}[(AUV)^{7/20+ε}(U+V)^{1/4}
  + (AUV)^{3/8+ε}(AU+AV)^{1/8}]. The second term was corrected from LIT_CHECK's (AUV)^{1/4+ε} by the cross-model
  review; that term only adds restrictions. Against the trivial ‖α‖‖β‖‖ν‖(AUV)^{1/2}, the first summand alone gives the ratio
  ≥ (4C̄)^{1/2}A^{7/20}(UV)^{−1/40}. So it can be nontrivial only if 4C̄ < (UV)^{1/20}; with UV = p/(4C̄) this means
  C̄ ≲ p^{1/21}.
* The DFI Thm 2 and BC items are limitations of the displayed upper bounds, not lower bounds for the KF sums. They are
  necessary, not sufficient, conditions for a saving (ε-losses ignored).

*Proof.*
(a) BB̄ + uū ≡ 1 modulo u and modulo B, hence modulo uB. Also B + u ≤ BB̄ + uū ≤ B(u−1) + u(B−1) < 2uB, so
BB̄ + uū = 1 + uB. Divide by uB and multiply by ap: apB̄/u = ap/(uB) + ap − apū/B. Then:
* Expand 1[u | p+B] = u⁻¹Σ_{a=0}^{u−1} e(a(1 + pB̄)/u) and 1[B | p+u] = B⁻¹Σ_{b mod B} e(b(1 + pū)/B).
* Substitute b = a + c with c running over residues mod B (for fixed a this is a bijection of residues).
* Collect: e(a/u + ap/(uB) − apū/B)·e((a+c)(1 + pū)/B) = e(a(p+u+B)/(uB))·e(c(1 + pū)/B).

(b)
* Σ_{B=V+1}^{2V} 1/B ≥ V/(2V) = 1/2.
* The coprime sum: #{u ∈ (U,2U] : (u,B) = 1} = Uφ(B)/B + O(τ(B)). Also Σ_{V<B≤2V}φ(B)/B² = (6/π²)log 2 + O(log V/V), by
  Σ_{B≤x}φ(B)/B² = (6/π²)log x + C + O(log x/x).
* For each B ∼ V the number of u ∈ (U, 2U] with u ≡ −p (mod B) is ≥ ⌊U/B⌋ ≥ U/(2V) − 1.

(c) This is arithmetic on DFI (1.4), (1.5) and BC (1.2) as corrected in `LIT_CHECK.md` §3, with M = U, N = V, a = bp.
* DFI Thm 1: (U+V)^{1/2}/(UV)^{1/2} = √(1/s + 1/L), and (1 + a/UV)^{1/2}s/(UV)^{1/2} = √(s/L + a/L²).
* DFI Thm 2: p^{3/8}(2(UV)^{1/2})^{11/48} < (UV)^{1/2} ⟺ (UV)^{37/96} > 2^{11/48}p^{3/8} ⟺ UV > 2^{22/37}p^{36/37}.
* BC: (1 + pA/UV)^{1/2}(AUV)^{7/20}(U+V)^{1/4} ≥ (4C̄A)^{1/2}(AUV)^{7/20}(UV)^{1/8}; divide by (AUV)^{1/2}. ∎

**Other coordinates (observation).** In (u,C), (B,C), (C, x) and the trial form, the class condition determines the
inverse: \overline{4C} ≡ u (mod 4uC − 1). The Kloosterman fraction is then a rational phase in the summation variables
(O5; PARITY_AUDIT B7). We found no coordinate system in which (★) presents a Kloosterman fraction with two free moduli and
a numerator below their product. Whether some reorganisation does is not decided here (Assessment).

### 6.2 Proposition Q — Kloosterman moduli in the SL₂ form (PROVED bookkeeping; reading Assessment)

(i) **SL₂ form** (FRONTIER §2.1). R(p) = Σ_{c ≡ 0 (4), c > 0} r_c(p), where r_c(p) = #{γ = [[a, p],[c, d]] ∈ SL₂(ℤ) :
a, d ≥ 1, a ≡ d ≡ −1 (mod c)} = #{(u, B) ∈ ℕ² : cuB − u − B = p}, via a = cu − 1, d = cB − 1 and ad − pc = 1.

(ii) **One double coset.** For fixed c > 0, the double cosets Γ_∞\{γ : lower-left entry c}/Γ_∞ (Γ_∞ = ±[[1, ℤ],[0, 1]])
are indexed by d mod c with gcd(d, c) = 1, and a ≡ d̄ (mod c). The Kloosterman sum S(m, n; c) = Σ*_{d mod c}
e((m d̄ + n d)/c) has one term per double coset.
* (★) at level c keeps only the double coset d ≡ −1, whose term is e(−(m+n)/c).
* Inside that coset (★) imposes the lattice condition "top-right entry = p". The elements are [[cu − 1, ·],[c, cB − 1]],
  with top-right entry cuB − u − B.
* So r_c(p) is a representation number of the one integer cp + 1 as (cu − 1)(cB − 1).

(iii) **The two natural orientations.**
* Conjugation by w = [[0, −1],[1, 0]] gives wγw⁻¹ = [[d, −c],[−p, a]], so the lower-left entry becomes −p. With p as the
  Kloosterman modulus there is one modulus. The class condition becomes the height-tied congruence of HYP (E5), where
  Weil's p^{1/2+o(1)} is the benchmark.
* In the original orientation the moduli are the levels c, and each level carries the single integer cp + 1 (Z1480;
  HYP §3.7).
* Detecting d ≡ −1 inside S(·,·;c) can be done additively: 1[d ≡ −1 (c)] = c⁻¹Σ_{k mod c}e(k(d+1)/c) turns the restricted
  term into combinations of ordinary sums S(m, n + k; c) with k-dependent indices. Character detection would need
  nebentypus mod c. Either way the parameters vary with c.

**Reading (Assessment).** We did not find a direct standard Kuznetsov / Deshouillers–Iwaniec application (sum over moduli
c with fixed Fourier indices) to which (★) reduces. Nothing here excludes a spectral treatment jointly in the level and
the integer cp + 1. It is only that none is exhibited, and HYP §3.7 / Z1480 record the bookkeeping obstacle.

### 6.3 Ledger of averaged variables (B6 check)

| implementation | averaged variable | what it amounts to at fixed p | scope of the statement |
|---|---|---|---|
| sawtooth frequencies, Fejér weights, h ≤ H | h | smoothed count over windows of length ≍ UV/H around p (Thm B(a)) | archimedean B6 for this kernel; positive-mean certificates need H ≥ q_max/2 (Thm B(b,c)) |
| full projection onto conductors d \| M | (d, a) | class average of N over n ≡ p (mod M) (Thm C(a)) | B1 data; positive-mean pairwise certificates need primitive frequencies (Thm C(b)) |
| conductors d ≤ D ≤ min(U,V)^{1−ε}, smooth weights | (d, a) | universal constant up to O(min^{−A}) (HYP Thm 3), for n coprime to every d ≤ D (e.g. primes p > D) | blind |
| KF moduli B, inverse ū | (u, B) free | one-relation count N₁; zero mode ≫ min(U,V) (Thm K(b)) | ceiling for main + absolute-error bounds. DFI Thm 1 saves on K(b) in skew blocks with max side > (bp)^{1/2+δ}; this does not lift to N (Thm K(c)) |
| two-relation KF | (u, B, a, c) | sawtooth kernel × one-sided KF (Thm K(a)) | reduces to rows 1 and 4 for these expansions |
| Kuznetsov moduli | c | levels with one integer cp + 1 each, or the single modulus p (Prop Q) | no direct fixed-index application exhibited |
| trial moduli m = 4uC − 1 | m | the original count, through p mod m (O5) | no averaging |

## 7. (S2): is any checked theorem below p^{1/3}? (Assessment; computations relative to the quoted statements)

| tool | what it gives for R(p), or for the cube / balanced block |
|---|---|
| divisor bound (HYP Thm 1) | p^{1/3+o(1)} (cube block); balanced block ≤ U = p^{1/4} |
| Lenstra / Coppersmith–Howgrave-Graham–Nagaraj (PARITY_AUDIT A1–A2) | O(1) divisors of p + u ≡ −1 (mod 4u) when 4u ≥ (p+u)^{1/4+ε}: the same O(1) per u as HYP Thm 1(a). The balanced block u ≍ p^{1/4} sits at the excluded exponent 1/4 |
| Heath-Brown, Ann. Math. 155 (2002), Thm 14 (as quoted in LIT_CHECK §1), on the homogenisation 4xyz − xw² − yw² − pw³ with box B₁, B₂, B₃ ≥ 1, B₄ = 1 | The form is irreducible over ℚ: it is linear in z with coprime coefficients 4xy and −w²(x+y+pw), so Gauss's lemma applies. The monomial weights are B₁B₂B₃, B₁, B₂, 1, so T = B₁B₂B₃ = V (the coefficient p does not enter T). Hence k ≪_ε (V³/T)^{1/3^{3/2}}V^ε(log p)⁵ = V^{2/(3√3)+ε}(log p)⁵ auxiliary forms, with 2/(3√3) = 0.3849. In a block with hits V ≍ p, so this upper bound is ≈ p^{0.385+ε}, above p^{1/3} before points per curve are counted. This direct application does not give a saving. It does not show that a better determinant-method argument is impossible |
| Weil / modular hyperbola (Shparlinski Thm 13; KSWX) | error p^{1/2+o(1)} per box (PARITY_AUDIT B1, B4) |
| DFI / Bettin–Chandee | DFI Thm 2 and BC need C̄ ≲ p^{1/37}, resp. p^{1/21}. DFI Thm 1 saves on the KF sum K(b) in skew blocks (max side > (bp)^{1/2+δ}), but main + absolute-error bounds for N through one relation are ≫ min(U,V) (Thm K(b,c)) |
| Fejér/max-Δ with square-root input, any coordinates | ≫ min(U, V, C̄ + 1) (Thm E) |
| KMS 2017/2020, Blomer–Pascadi, Bourgain–Garaev | Type II savings q^{1/64}…M^{1/4} of trivial bounds at one modulus. No unit-coefficient bilinear structure in (★) was identified (PARITY_AUDIT B2–B5) |

* **Reading (Assessment).** The elementary p^{1/3} = B¹ (box side B = p^{1/3}) coincides with the dimension-growth exponent
  of an affine surface. This is an analogy that calibrates the target, not a lower bound for this surface.
* The literature search (`LIT_CHECK.md` §4) found no sub-n^{1/3} result for the Type II c = 1 family. The best general
  pointwise bounds found are f(n) ≪ n^{3/5+ε} (Elsholtz–Tao for primes; Elsholtz–Planitzer arXiv:1805.02945 for all n)
  and f_II ≪ n^{2/5+o(1)} (ET Prop 1.7). The search is not exhaustive.
* **(S2) stays open.** It is an upper-bound question and worth nothing for ES (HYP R3). It is recorded because the lane
  brief asks it and because FRONTIER §3 uses p^{1/3} as the benchmark.

## 8. Verdict, hard screens, survivors

**Verdict: narrowed** (an Assessment built on the scoped theorems above).
* **(S1)** (an upper bound N_bal ≪ p^{1/4−η}) is not obtained, and none of the checked theorems gives it:
  * main + absolute-error one-relation KF bounds are ≫ min(U,V) (Thm K);
  * Fejér/max-Δ with square-root input is ≫ min(U,V,C̄+1) in every coordinate system (Thm E);
  * the F1 samples show no aggregate cancellation between conductor ranges at primes.
  Open: HYP R1, R2, and joint or nonlinear estimates.
* **Positivity** (the ES direction), for *positive-mean* linear certificates:
  * frequency certificates need degree ≥ q_max/2 = 8UV (sharp), and for H < min(q_min, q_max/2) their expectation is ≤ 0
    (Thm B);
  * pairwise conductor certificates need primitive frequencies (Thm C(b));
  * the full conductor projection onto divisors of M is a class average (Thm C(a)), and Fejér-weighted frequency sums are
    window-smoothed counts (Thm B(a)).
  Negative-mean certificates that are positive at p (oscillatory part exceeding the negative constant term) are not
  excluded (explicit examples, §§5.1–5.2).
* **Kuznetsov.** The two natural orientations give the single modulus p or levels carrying one integer each (Prop Q). No
  direct application was exhibited; none is excluded.

**Hard screens for the best surviving idea.** That idea is: positivity at p from the top of the spectrum (frequencies
≳ q_max/2, primitive conductors), or from a low-degree certificate proved positive at p (oscillatory part exceeding
|𝒫|·|ĝ_0|), using the arithmetic of p.

| screen | pass/fail | note |
|---|---|---|
| T1 (odd squares) | undecided; must use primality | the theorems here hold for every integer n and are consistent with T1. F1: at squares the pieces' total vanishes identically, and a survivor must explain why it does not at primes |
| 8/131 | FAIL as stated | Thms C, E and the KF analysis transfer to numerator M (replace 4 by M). B's exact threshold q_max/2 uses even moduli; for odd moduli a parity-dependent version holds (e.g. odd q: a degree-(q−1)/2 Dirichlet kernel already has positive mean). So B transfers qualitatively, not verbatim. A survivor must name where 4 enters |
| tied modulus | not broken | the top conductor *is* the tied modulus q = 4uB; the averaged variables are p-attached or collapse (§6.3) |
| fixed p | partly | Thms B(a), C(a) identify the smoothing (Fejér windows) and congruence (class average) content of specific truncations. They do not show that a successful method must avoid them, e.g. in combination with a complementary remainder |

**What survives.**
* (i) Positive-mean certificates of degree ≳ q_max/2 (or using primitive conductors), with a beyond-square-root bound for
  the remaining oscillatory part at the given p.
* (ii) Negative-mean certificates of lower degree, with a proof that the whole certificate is positive at the given p,
  i.e. A(p) > −|𝒫|ĝ_0. That is a lower bound for a signed exponential sum at one point. This investigation found no
  uniform method for it.
* (iii) For the upper bound (S1): HYP R1/R2, and joint-conductor or weighted estimates not of the forms analysed here.
* (iv) Nonlinear uses of the dual (products of S_h, amplification, moments). These are not covered here.
* (v) Methods that do not pass through a linear Fourier expansion of the divisibility indicator, and other spectral or
  determinant-method reorganisations. These are untouched.

## 9. Proposed FRONTIER §7.1 addition (do not edit FRONTIER here)

> *(z53, `Z53_HYPKLOOST.md`, internally reviewed.)* "Summing over conductors/frequencies before bounding" was evaluated in
> three standard forms. It is narrowed by scoped results (PROVED unless marked):
> * (L) Frequency weights. Σ_{|h|≤H}ĝ_h S_{−h}(p) is an exact pair-weighted periodisation of the solution counts at the
>   integers p + ℓ. A frequency certificate of N(p) ≥ 1 with positive mean needs degree ≥ q_max/2 = 8UV, and this is
>   sharp; below min(q_min, q_max/2) its expectation is ≤ 0.
> * (L′) Conductors. The full conductor projection onto divisors of M is the class average over n ≡ p (mod M). Every
>   minorant of 1[q | ·] without primitive frequencies has mean ≤ 0.
> * (K) Kloosterman fractions. Reciprocity turns the second Kloosterman fraction into the archimedean phase.
>   Main + absolute-error bounds through one relation are ≫ min(U,V). The numerator is bp ≥ UV:
>   * DFI Thm 2 can save only if C̄ ≲ p^{1/37}, and Bettin–Chandee only if C̄ ≲ p^{1/21};
>   * DFI Thm 1 does save on the KF sum in skew blocks with max side > (bp)^{1/2+δ}, but that does not yield a saving
>     for the block count.
> * (Q) Kuznetsov. In the two displayed natural orientations of the SL₂ form the moduli are p (single) or the levels
>   (one integer each). No direct fixed-index application was found.
>
> The obstructions B(b) and C(b) constrain positive-mean ("main term") arguments only. Low-degree certificates can be
> positive at a given p, but then their oscillatory part must exceed the negative constant term. Proving that is a
> signed lower-bound problem, and this investigation found no uniform method for it.
>
> EVIDENCE (3000 primes at 10¹⁰ and 10¹²): the exact conductor pieces have sample sd ≈ 0.3 and no aggregate cancellation
> (cross-covariance share +0.02…+0.15). At odd squares the total vanishes identically (T1).
>
> (S2) "|E(p)| ≤ p^{1/3−η}" is not given by any checked theorem: Heath-Brown's Thm 14 applied directly gives
> ≪ p^{0.385+ε} auxiliary curves.

In FRONTIER §3 "Tied modulus", after the p^{1/3} sentence, add: "(No checked theorem improves p^{1/3}. A direct application
of Heath-Brown's determinant method, Thm 14, gives ≪ p^{0.385+ε} auxiliary curves; `Z53_HYPKLOOST.md` §7.)"

## 10. Bottom line

The lane asked whether summing the dual of the (★) block count over conductors or frequencies *before* bounding, using
Kloosterman fractions, bilinear forms or Kuznetsov, can beat the elementary bound at a fixed prime. In the forms we could
make precise, it does not.
* At 10¹⁰–10¹², the exact conductor pieces at primes have order-one sample sd and show no aggregate cancellation. The one
  universal exact cancellation in sight is T1's at odd squares.
* Exact identities identify the smoothing or congruence content of specific truncations:
  * Fejér-weighted frequency sums are smoothed counts over windows of integers around p;
  * the full conductor projection is a class average;
  * Kloosterman fractions collapse by reciprocity into the sawtooth phase.
  * The numerator bp is too large for DFI Thm 2 and Bettin–Chandee outside tiny-level blocks.
  * DFI Thm 1 saves on single KF sums in skew blocks, but no saving for N follows.
* Two uncertainty lemmas show that positive-mean certificates need frequencies up to q_max/2 = 8UV (sharp), resp.
  primitive frequencies for every pair that contributes positive mean.
* What remains:
  * positivity from the top of the spectrum using the primality of p;
  * proving a low-degree certificate positive at one prime, i.e. its oscillatory part larger than its negative constant
    term;
  * nonlinear or joint methods.

This investigation found no uniform method for any of them. ES remains open.

## 11. Reproduction

```
ulimit -v 8000000; mkdir -p /tmp/hk && cd /tmp/hk
gcc -O2 -fopenmp -o cond $REPO/scripts/z53_hypkloost_conductor.c -lm
gcc -O2 -fopenmp -o kf   $REPO/scripts/z53_hypkloost_kf.c -lm
uv run --with sympy python $REPO/scripts/z53_hypkloost_inputs.py /tmp/hk        # p12 p10 sq12 sq10 ns12 rn12 rn10 (.txt)
for f in p12 sq12 ns12 rn12; do OMP_NUM_THREADS=20 timeout 1700 ./cond 1000 1000 < $f.txt | gzip > c_$f.tsv.gz; done
for f in p10 sq10 rn10;      do OMP_NUM_THREADS=20 timeout 1700 ./cond 316 316  < $f.txt | gzip > c_$f.tsv.gz; done
cd $REPO && uv run --with numpy python scripts/z53_hypkloost_cond_analyze.py /tmp/hk > /tmp/hk/cond_stats.txt
cd /tmp/hk && head -200 p12.txt | ./kf 1000 1000 16 > kf_bal12.tsv; head -100 p12.txt | ./kf 100 10000 16 > kf_unb12.tsv
head -100 p12.txt | ./kf 10000 100 16 > kf_unb12b.tsv
cd $REPO && uv run python scripts/z53_hypkloost_window_check.py
uv run --with numpy --with scipy python scripts/z53_hypkloost_certificate_lp.py
```

* Runtimes: `cond` ≈ 0.75 s per n at U = 1000 on one core, ≈ 15 min for all of F1 on 20 threads; `kf` 6 s for 200
  primes.
* `z53_hypkloost_inputs.py` was checked to reproduce the original input lists byte-for-byte.

## 12. Review log

**Hostile internal review** (deep-mode subagent, 2026-11-01; `data/z53/hypkloost/REVIEW_internal.md`).

The first version read "major revision": 2 CRITICAL, 15 MAJOR and 4 MINOR findings. They were addressed in the second
version. A second pass then found 12 FIXED and 9 PARTLY, plus S01–S08. Those are addressed in the third version, below.

CRITICAL:
* F01: positive mean was conflated with pointwise positivity. Every spectrum necessity is now qualified "positive-mean",
  and the reviewer's two explicit low-degree / low-conductor certificates are included (§§5.1–5.2). The "equivalent to the
  problem" claim was removed.
* F02: the expectation claim of B(b) needed H < min(q_min, q_max/2), not H < q_min. Corrected; the memo's own LP output for
  U = V = 2 is the counterexample.

MAJOR:
* F03: Fourier support. ĝ(h) = 0 is now required only at integers |h| > H, so the Fejér example is admitted.
* F04: the Selberg sharpness proof now proves G(0) > 0 by full-grid quadrature (reviewer's repair).
* F05: (5.1) is now called a pair-weighted periodisation. Localisation is claimed only for the Fejér kernel, and the
  information-theoretic claim was removed.
* F06: only absolute-conductor bins are Parseval-orthogonal, in the unconditioned model. Both bin families are now
  reported as empirical shares.
* F07: the evidence is no longer promoted to impossibility, and the T1 wording is corrected (92 % of prime rows also have
  total 0).
* F08: the uniform-residue mean ≈ 0.120 is now separated from the prime-model mean 0.146, and certificates are normalised.
* F09: "divisor-closed with lcm M" is replaced by the full unweighted projection.
* F10: the HYP Thm 3 misapplication to lcm(1, …, D) was removed.
* F11: complete Ramanujan sums are claimed only for Ramanujan-form weights.
* F12: (4.1) is now called the two-relation form, and the 4-condition is restored.
* F13: the coprime zero mode (6/π²)log 2·U is now given and the non-coprime reduction stated.
* F14: the K(b) ceiling is scoped to main + absolute-error bounds. The balanced N₁ = 0 example and the uncovered coupled
  estimates are noted.
* F15: the nebentypus necessity was replaced by additive detection, and the Kuznetsov reading was narrowed.
* F16: Heath-Brown's Thm 14 is stated as an upper bound with V^ε and the irreducibility check, and no impossibility is
  claimed.
* F17: literature and exhaustion claims were scoped to "checked".

MINOR:
* F18: the equality criterion in E(c) now requires the third side not to be smaller in order.
* F19: the LP is labelled EVIDENCE, with the box bound disclosed.
* F20: sample labels, "sd ≈ 17", the saved bootstrap (seed 53), the saved input generator, and .gz reproduction.
* F21: integer U, V ≥ 1, nonempty positive-integer pair sets, and a candidate set for R(p).

The reviewer confirmed as correct:
* the Poisson signs and the half-shifted quadrature;
* the Fejér weight bounds and the class-projection identity;
* the entire primitive-conductor measure proof;
* the reciprocity identity and (4.1) for two relations;
* the additive one-relation inequalities and Theorem E;
* the Bruhat bookkeeping and the conjugation by w;
* the DFI/BC exponent arithmetic against the quotations, and the HB exponent 2/(3√3) = 0.3849.

The reviewer recomputed all F1 moments and the KF statistics, and checked the C program against a direct Ramanujan-sum
computation. Its independent bootstrap intervals are compatible with ours.

A cross-model review is to follow.

**Second pass** (deep-mode subagent; appended to `REVIEW_internal.md`). It rechecked the repaired proofs of B and C, the
BC threshold, the additive detection in Q and the HB arithmetic, and reproduced `cond_stats.txt` byte-for-byte. Its
findings S01–S08 are addressed in this third version:
* S01 (MAJOR): positivity of a negative-mean certificate needs A(p) > −|𝒫|ĝ_0, not A(p) > 0. The survivor lists now say
  so, and the reviewer's p = 17 example is added.
* S02: the expectation is |𝒫|·ĝ_0, and the pairwise quantifier is "every pair contributing positive mean".
* S03: the conductor example's support is {1, 2, 3, 4, 8}. This also corrects the first review's slip.
* S04 (MAJOR): the coprime KF expansion now assumes 2U, 2V < p (counterexample p = 5, (15,10) recorded). The zero mode is
  given with its uniform error O(U log(2m)/m), with a proof sketch for both aspect ratios.
* S05: HYP Thm 5's τ-bound needs UV ≤ p; the ledger row now carries the coprimality hypothesis.
* S06: the global "no method known" and "survivor must avoid them" claims are removed, and the Kuznetsov FRONTIER bullet
  is scoped to the two displayed orientations.
* S07: the 8/131 screen now says that B transfers only qualitatively to odd moduli.
* S08: the p10 share order, the p12-only sd claim, the sd 16.85 replacing O(17), and the LP's status as a closed
  relaxation with default tolerances.

**Cross-model review** (GPT/Astra, `data/z53/xreview/REVIEW_HYPKLOOST.md`; checker `scripts/z53_xrev_hypkloost_check.py`).
Verdict ACCEPT-WITH-FIXES.
* The reviewer independently re-derived and confirmed B (including a citation-free sharpness construction for B(c)), C,
  E, the reciprocity identity, the one-relation ceiling, Q's bookkeeping, and the Heath-Brown Thm 14 specialisation.
* It reproduced all numerics: `cond_stats.txt` byte-for-byte, the KF moments, the LP and the window checks.

Fixes applied:
1. **MAJOR. DFI Thm 1 was misquoted** (a product instead of the sum [(M+N)^{1/2} + (1+a/MN)^{1/2}min(M,N)]). The claim
   "DFI Thm 1 is never below the trivial bound" is retracted. Thm 1 does save on the KF sum K(b) in skew blocks with
   max(U,V) > (bp)^{1/2+δ}, e.g. U ≈ p^{1/5}, V ≈ p^{3/5}. This is not a saving for N; the one-relation ceiling K(b)
   stands.
   Corrected in K(c), §0, the §6.3 ledger, the §7 table, §9, §10 and LIT_CHECK §3. The C̄ ≲ p^{1/37} restriction now
   refers to DFI Thm 2 only.
2. Bettin–Chandee's second term is corrected to (AMN)^{3/8+ε}(AN+AM)^{1/8} in LIT_CHECK and K(c). The first-term
   restriction C̄ ≲ p^{1/21} stands.
3. LP prose: below q_max/2 the solver returns mean 0, with G(0) = 0 or 1 depending on the row.
4. The verdict remains "narrowed". The memo now distinguishes the skew-range saving for a KF sum from the absence of any
   saving for the block count.
