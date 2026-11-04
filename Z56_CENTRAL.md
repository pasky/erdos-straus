# Z56_CENTRAL — depth lane CENTRAL (wave z56, gap 1): how hard is the central slice?

ES is OPEN. Nothing here proves or disproves it. This lane is **upper-bound calibration work** on FRONTIER §7.1 (balanced
block / 2-cycles). Even full success would say nothing about positivity. Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment, one per claim. Results are internal.

Brief: `z52bbriefs/z53_depth.md` (rules), kickoff `z52bbriefs/z56_lanes.md` §4 CENTRAL. Predecessors: `Z55_TDCAL.md`
(Lemma S(a), Thm B, Prop C, Prop D), `Z54_BILINJAC.md` (Thm R, §5), `Z55_TDO.md` §6, `Z55_TDF.md` §3. Scripts
`scripts/z56_central_*`, data `data/z56/central/`. Literature: `data/z56/central/LIT_CHECK.md` (research subagent,
source-quoted; items re-read by the author where used).

**Status: CHECKPOINT 1 (skeleton).** Sections marked (TODO) are filled in later.

## 0. Summary and verdict (TODO)

## 1. Notation and statements attacked

* x ≥ 3, 1 ≤ y ≤ x^{1/2}. For A > 0 and 1 < θ ≤ 4:
  S(x, y; A, θ) := #{(k, m) ∈ ℕ² : x < km ≤ x + y, A < m ≤ θA},  E(x, y; A, θ) := S − y·Σ_{A<m≤θA} 1/m.
  (Since A > y in all ranges below, each m contributes 0 or 1, and S counts the m in (A, θA] with a multiple in (x, x+y].)
* TDCAL Lemma S(a): with x = p + 2U, y = 2U, |E1(p, U)| = S(x, y; U², 4). In the fourth-root range U² ≍ √x.
* **CNT(η)** (TDCAL): |E1(p, U)| = 2U log 4 + O(U^{1−η}) uniformly in the fourth-root range. Open.
* **CNT_unif(η, δ)** (band-uniform, decoupled version): for fixed K ≥ 1, all large x, all y ∈ [x^{1/4}/K, Kx^{1/4}],
  all A ∈ [x^{1/2−δ}, x^{1/2+δ}] and all θ ∈ (1, 4]: |E(x, y; A, θ)| ≤ C y^{1−η}.
* D(x, y) := Σ_{x<n≤x+y} d(n); Main(x, y) := (x+y)log(x+y) − x log x + (2γ − 1)y = y log x + 2γy + O(y²/x).
* **SID(η)** (pointwise short-interval divisor asymptotic at length x^{1/4} with power saving):
  D(x, y) = Main(x, y) + O(x^{(1−η)/4}) for y ≍ x^{1/4}. **Open** (Assessment, search-limited; LIT_CHECK §3: Ivić–Zhai's
  best pointwise bound Δ(x+h) − Δ(x) ≪ x^{1/4+ε}h^{1/4} beats the trivial bound only for h ≥ x^{1/3}; Jutila's
  conjecture Δ(x+h) − Δ(x) ≪ x^ε√h is listed as open by Ivić (JTNB 21 (2009), (1.13)) and Ivić–Zhai (Conj. 3).) Since
  Δ(x) = Ω(x^{1/4}) (Hardy), SID can never follow from a pointwise bound for Δ alone.
* **EPC** (exponent pair conjecture): (ε, ½ + ε) is an exponent pair for every ε > 0 (Trudgian–Yang, arXiv 2306.05599,
  p. 2, names it as a conjecture).

**Targets.** (a) A hardness calibration: CNT-type statements imply a known open statement. (b) Or: a genuinely easier
structure for the central slice and a pointwise result.

## 2. Why this is not already closed
* TDCAL proved the identity (Lemma S(a)) and per-frequency deficits (Prop C) but explicitly established *no implication*
  between CNT/TD and short-interval divisor statements in either direction (TDCAL §0, answer 1).
* TDO §6 / TDF §3.1 record self-duality as Assessment; no reduction theorem.
* The pointwise bound recorded campaign-wide for |E1| is ≪ U^{1+ε} (BILINDIV §2, TDF §3.3 remarks that the ε-free
  TD ⇒ DC fails for this reason). `git grep` finds no use of Hooley's Δ / Nair–Tenenbaum for E1.

## 3. First results (checkpoint)

**Theorem L(i) (PROVED, exact decomposition).** For 0 < δ < 1/4, L := x^{1/2−δ}, L′ := x/L = x^{1/2+δ}, and
1 ≤ y < L:
  D(x, y) − Main(x, y) = E_band(x, y; δ) − 2F_L(x, y) + O(1),
where E_band := #{(k, m) : x < km ≤ x + y, L < m ≤ L′} − y·2δ log x and
F_L := Σ_{m≤L}[ψ((x+y)/m) − ψ(x/m)] with ψ(t) = t − ⌊t⌋ − ½. (Proof in §4.)

**Theorem L(iii) (CONDITIONAL on EPC).** F_L ≪_ε x^{1/4−δ/2+ε}, so D(x, y) − Main(x, y) = E_band + O(x^{1/4−δ/2+ε}).
Hence, under EPC, SID(η) for some η > 0 ⟺ a power saving for the central band of some width x^{±δ}; and CNT_unif ⟹ SID.

**Prop P (PROVED relative to de la Bretèche–Tenenbaum 2025, Cor. 1.2).** |E1(p, U)| ≪ U(log log U)^{5/2} pointwise.

**First falsifier (running).** `scripts/z56_central_slices.c`: exact slice decomposition of D(x, y) at x ≈ 10¹⁰–10¹⁶,
checking the identity L(i) (residual O(1)) and comparing slice errors with the random model.
