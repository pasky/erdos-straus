# Z53_HYPKLOOST — summing over conductors and frequencies before bounding (FRONTIER §7.1, analytic/spectral)

ES is OPEN. Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Internal results are internally reviewed only.

Lane brief: `z52bbriefs/z53_depth.md`, `z52bbriefs/z53_lanes.md` § HYPKLOOST. Scripts `scripts/z53_hypkloost_*`, data
`data/z53/hypkloost/`. Builds on `Z52D_HYPERBOLA.md` (cited as HYP; its Thm 1, Prop 2, Thm 3, Thm 5, Thm 6) and
`PARITY_AUDIT.md` §§1–2.

**Status: CHECKPOINT 1** (skeleton; statements, why open, first falsifier). Later sections are filled in below as they are
completed.

## 1. Statements attacked

Notation as in HYP §2. p ≥ 5 prime; block 𝔅 = (U,2U] × (V,2V]; pair π = (u,B); q = 4uB; s = u + B; n ∈ ℤ;
N(n) = N_𝔅(n) = #{π ∈ 𝔅 : q | n + s}. Level C = (n+s)/q; typical level C̄ = p/(4UV). Balanced block U = V ≈ p^{1/4}
(C̄ ≍ p^{1/2}); cube block U ≍ V ≍ C̄ ≍ p^{1/3}. The elementary bound is N ≤ p^{o(1)}·min(U, V, C̄ + 1) (HYP Thm 1).

The conductor (Ramanujan) dual of the block count is the exact identity

  N(n) = Σ_{d ≥ 1} Σ*_{a mod d} e(an/d)·D(d,a),  D(d,a) := Σ_{π ∈ 𝔅 : d | q} q⁻¹ e(a s/d),          (1.1)

i.e. N, as a function of the integer n, is a trigonometric polynomial whose spectrum is the set of Farey fractions a/d with
d ≤ 16UV. "Summing over conductors before bounding" means: evaluate Σ_{(d,a)∈𝒮} w(d,a) e(ap/d) D(d,a) for a set or weight
𝒮/w of frequencies that couples different d, and bound that, instead of bounding each conductor (HYP Thm 5).

* **(S1) Cross-conductor / cross-frequency power saving at fixed p.** ∃ η > 0: for every large prime p, |N_bal(p) − M| ≤
  p^{1/4−η} (M ≈ 0.146 the block mean; since M = O(1) this is the upper bound N_bal(p) ≪ p^{1/4−η}), by an argument that
  sums the dual (1.1), the sawtooth frequencies S_h (HYP (E3)), or a Kloosterman-fraction form over conductors/moduli
  before bounding. Same for any other block with its own trivial bound min(U, V, C̄).
* **(S2) Benchmark.** ∃ η > 0: |E(p)| = |R(p) − M(p)| ≤ p^{1/3−η} for all large p, by *any* known theorem.
* **(S3) Implementation classes**, each to be settled by a power saving or a scoped theorem:
  (K) bilinear/trilinear Kloosterman-fraction bounds (Duke–Friedlander–Iwaniec 1997, Bettin–Chandee 2018) applied to the
  KF form of the block count; (L) linear (and minorant/majorant) functionals of the dual (1.1) or of the S_h, i.e. weighted
  sums over conductors and frequencies; (Q) sums of Kloosterman sums over moduli (Kuznetsov, Deshouillers–Iwaniec) where
  the averaged modulus is not attached to p.

## 2. Why this is not already closed

HYP closes only (i) one-step dualization *at a fixed conductor* (Thm 5), (ii) Erdős–Turán/Fejér with max_h |S_h| input
(Thm 6), (iii) Cauchy–Schwarz in the function variable (Prop 2), (iv) low-conductor/class-model main terms (Thm 3, Cor 4).
Its open list keeps (R0) "cancellation across conductors or across frequencies; no method known". (K), (L), (Q) are exactly
the implementations of (R0) that the literature offers: they sum over conductors/moduli/frequencies jointly. None of them
was evaluated in HYP or PARITY_AUDIT beyond a one-line remark (PARITY_AUDIT B7: "the Kloosterman fraction degenerates";
BRAINSTORM/s8_volume_dfi R268: DFI trivial for MN = o(p^{36/37})).

## 3. First falsifier (F1): do conductor pieces cancel against each other at a fixed prime? (EVIDENCE)

`scripts/z53_hypkloost_conductor.c` computes, for each n, the exact Ramanujan expansion of N_bal(n) (sharp balanced block),
grouped into relative-depth bins k = ⌊log₂(q/d)⌋ (k = 0 is the top conductor d = q) and absolute bins j = ⌊log₂ d⌋, and
checks that the bins sum to N(n) (exact in every case: max |Σ bins − N| = 0 at double precision). Analysis:
`scripts/z53_hypkloost_cond_analyze.py` → `data/z53/hypkloost/cond_stats.txt`; per-n rows `data/z53/hypkloost/c_*.tsv.gz`.

Data sets: 3000 consecutive primes from 10¹² (U = 1000) and from 10¹⁰ (U = 316); controls: 600 odd squares m² ≥ 10¹²
(and ≥ 10¹⁰), 600 near-square primes m² + k (k ≤ 40) above 10¹², 1500 random n ≡ 1 (4) at each scale.

"Square-root prediction" here = the orthogonal model: under n uniform modulo L (L a common multiple of all q), distinct
Farey fractions are orthogonal, so the conductor pieces are uncorrelated and Var(N) = Σ_k Var(P_k) (PROVED, Parseval; §5).
Cross-conductor cancellation would show up as a negative covariance share (Σ_{k≠l} Cov)/(Σ_k Var).

| set | Σ_k Var(P_k) | Var(N) | cross-cov share (95 % bootstrap CI) |
|---|---|---|---|
| primes 10¹² | 0.276 | 0.315 | **+0.14** [+0.03, +0.26] |
| random n 10¹² | 0.257 | 0.243 | −0.05 [−0.20, +0.09] |
| near-square primes 10¹² | 0.269 | 0.296 | +0.10 [−0.14, +0.37] |
| primes 10¹⁰ | 0.261 | 0.270 | +0.04 [−0.07, +0.15] |
| random n 10¹⁰ | 0.261 | 0.271 | +0.04 [−0.20, +0.27] |
| **odd squares 10¹²** | 0.175 | **0** | **−1.000** (exact) |

* At primes the conductor pieces are individually of size ≈ 0.3 (top bins k = 0, 1, 2: sd 0.30, 0.27, 0.22; the variance
  is spread over q/d ≤ 2⁶) and they do **not** cancel against each other: the cross-covariance is ≈ 0 or slightly positive.
  This is the orthogonal (square-root) behaviour. corr(N, top k bins) = 0.61, 0.76, 0.88, 0.94, 0.97 for k ≤ 0…4.
* Absolute bins d < 2¹⁰ ≈ U are constant at primes (sd ≤ 0.003; HYP Thm 3 in sharp form) but not at random n (sd 0.019 in
  bin j = 1), as Thm 3 predicts (it needs gcd(n, d) = 1).
* **At odd squares the pieces are as large as at primes (Σ Var = 0.175) but cancel exactly** (Σ = N = 0, T1). So exact
  cross-conductor cancellation exists — at squares, where it is forced by T1 — and is absent at primes. A method that
  bounds conductor ranges separately (uniformly in n) cannot see T1; a method that exploits cross-conductor cancellation
  would be exploiting the square conspiracy, the opposite of what positivity at p needs.

Reading (Assessment). At fixed p there is no cross-conductor cancellation for a bounding argument to harvest: the dual sum is
an orthogonal superposition of pieces of size O(1), its total fluctuation is the sum of theirs, and the only exact
cancellation in sight is T1's. This is the falsifier the lane asked for; it does not by itself close (S1) (a pointwise
argument might still find cancellation that is invisible in the variance), which is what §§4–6 address by theorems.

## 4–8. (to be completed: Kloosterman-fraction form and numerator obstruction; frequency/conductor duality; Kuznetsov;
(S2) benchmark check incl. determinant method; screens; FRONTIER text; bottom line)
