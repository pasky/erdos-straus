# Z56_CENTRAL — depth lane CENTRAL (wave z56, gap 1): how hard is the central slice?

ES is OPEN. Nothing here proves or disproves it. This lane is **upper-bound calibration work** on FRONTIER §7.1 (balanced
block / 2-cycles). Even full success would say nothing about positivity. Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment, one per claim. Results are internal.

Brief: `z52bbriefs/z53_depth.md` (rules), kickoff `z52bbriefs/z56_lanes.md` §4 CENTRAL. Predecessors: `Z55_TDCAL.md`
(Lemma S(a), Thm B, Prop C, Prop D), `Z54_BILINJAC.md` (Thm R, §5), `Z55_TDO.md` §6, `Z55_TDF.md` §3. Scripts
`scripts/z56_central_*`, data `data/z56/central/` (< 1 MB). Literature: `data/z56/central/LIT_CHECK.md` (research
subagent, every statement quoted from the source with page/number; the items this memo relies on were re-read by the
author in the fetched PDFs: dlB–T Cor. 1.2, Saito et al. Lemma 19, Trudgian–Yang p. 2 and Lemma 1.1, Ivić–Zhai Thm 1
and p. 6).
Checkpoint 1: commit 0cede3da.

## 0. Summary and verdict

**Verdict: narrowed (calibrated two-sidedly; under EPC an equivalence with the small-twist x^{1/4} short-interval
divisor problem), with one small pointwise strengthening.** No pointwise power saving for
the central slice is proved; none is refuted. What is new:

1. **Hardness (Theorem L).** (PROVED) The
   short-interval divisor sum splits *exactly* (up to O(1)) as D(x, y) − Main = E_band(δ) − 2F_L, where E_band is the
   central band m ∈ (x^{1/2−δ}, x^{1/2+δ}] and F_L a sum of ψ-differences over m ≤ x^{1/2−δ} (CONDITIONAL on the exponent pair
   conjecture EPC) F_L ≪ x^{1/4−δ/2+ε}. Consequently, **under EPC** (CONDITIONAL):
   * SID (a pointwise power-saving asymptotic for Σ_{x<n≤x+x^{1/4}} d(n)) ⟺ a power saving for some central band;
   * CNT_unif ⟹ SID, where CNT_unif is the central-slice asymptotic for every real x, with the length y ≍ x^{1/4}
     decoupled from the slice position A, uniformly for A ∈ [x^{1/2−δ}, x^{1/2+δ}] (Cor. L1);
   * likewise CNT_poly ⟹ SID (Cor. L1′): the same, with constants allowed to grow polynomially in the position A/√x.
   These hypotheses are stronger than TDCAL's CNT, which is restricted to primes and to the tied choice
   x = p + 2U, y = 2U, A = U²; passing from CNT to CNT_unif or CNT_poly is an additional requirement, not automatic.
   SID: Assessment (search-limited, LIT_CHECK §3), not established in the checked sources: the cited Ivić–Zhai
   estimates improve on the trivial bound only for lengths ≥ x^{1/3} (the global Δ exponent 0.31448… helps only for
   lengths ≥ x^{0.3145}), and Jutila's conjecture is listed as open. Since Δ(x) = Ω(x^{1/4}), the endpoint route
   |Δ(x+y) − Δ(x)| ≤ |Δ(x+y)| + |Δ(x)| cannot give SID, even with the conjectural sup bound x^{1/4+ε}.
   Unconditionally (PROVED, with the Trudgian–Yang exponent pair (715/10238 + ε, 7955/10238 + ε)), the same equivalence
   holds for bands of width x^{±δ} with δ > 6387/28960 ≈ 0.2205 (Cor. L3).
2. **Upper calibration (Theorem U, PROVED implication).** CNT_unif (sharp bands at every position
   A ∈ [x^{1/2−δ}, x^{1/2+δ}], δ < 1/4) follows from power-saving short-interval asymptotics for the *twisted* divisor
   functions τ_t(n) = Σ_{de=n}(d/e)^{it} (coefficients of ζ(s+it)ζ(s−it)), uniformly for |t| ≤ x^c. The case t = 0 is
   SID. So CNT_unif is sandwiched: {SID_t}_{|t|≤x^c} ⟹ CNT_unif ⟹ (EPC ⟹ SID).
   **Theorem E (CONDITIONAL on EPC)** gives the converse: CNT_unif ⟹ the twisted family. Hence (Cor. E1), *under
   EPC, CNT_unif is equivalent to power-saving short-interval asymptotics at length x^{1/4} for the coefficients of
   ζ(s+it)ζ(s−it), |t| ≤ x^c* (some exponents), whose t = 0 member is SID.
3. **Pointwise upper bound of the right order up to log log (Prop P, PROVED relative to de la Bretèche–Tenenbaum 2025,
   Cor. 1.2).** |E1(p, U)| ≪ U(log log U)^{5/2} pointwise, improving the campaign's ≪ U^{1+ε} (BILINDIV §2; TDF §3.3).
   The same holds for every band (A, θA], θ ≤ e², and every length y ≥ x^{ε}. With a localized Fejér argument
   (Cor. P2, PROVED implication) TD(η) ⟹ DC(2U^{−η}) with a (log log U)^{5/2} loss instead of U^{ε}.
4. **Degenerate-Hessian remark (§7).** (PROVED) The phase 2√(xhn) is homogeneous of degree 1, so its Hessian
   *determinant* vanishes identically (the Hessian has rank one). (Assessment) It is the natural two-variable dual phase
   of the central slice, so two-dimensional exponential-sum methods requiring a non-degenerate Hessian do not apply
   directly.
5. **EVIDENCE (`data/z56/central/slices_*.txt`).** Exact slice decompositions at x ≈ 10¹⁰, 10¹², 10¹⁴, 10¹⁶ (generic
   primes, odd squares, near-squares, test primes). The identity of Theorem L(i) holds with residual ≤ 0.632 (direct
   check at 10¹⁰, 2400 cases). Dyadic slice errors have rms ≈ 0.52–2.56·√(y log 2), broadly growing with M; no slice is
   distinguished. Odd squares and near-squares have a negative mean error in every dyadic slice (§8).

**Answers to the kickoff.** (a) A hardness calibration is proved *modulo EPC and a uniform, length-decoupled form of
CNT*: CNT_unif (or CNT_poly) ⟹ SID under EPC, and SID is a statement beyond the Ω-barrier of the Dirichlet divisor
problem that is not established in the checked literature. An unconditional reduction to a named open statement for the
*fixed* tied band is not obtained; Theorem U shows CNT_unif is no harder than the twisted SID family. (b) The central
slice is not easier in any way found: under EPC it is exactly the part of the x^{1/4} short-interval divisor problem
that per-frequency methods cannot reach (TDCAL Prop C), and the only pointwise statement obtained is the upper bound of
Prop P. **For gap 1 (Assessment):** the count enters TD/NC only as a zero mode, for which Prop P suffices up to
(log log U)^{5/2}; a CNT-type asymptotic should not be on the route to gap 1.

## 1. Notation and statements attacked

* x ≥ 3 real, 1 ≤ y ≤ x^{1/2}. For A > 0 and 1 < θ ≤ 4:
  S(x, y; A, θ) := #{(k, m) ∈ ℕ² : x < km ≤ x + y, A < m ≤ θA},  E(x, y; A, θ) := S − y·Σ_{A<m≤θA} 1/m.
  When A ≥ y each m contributes 0 or 1, so S counts the m in (A, θA] with a multiple in (x, x + y].
* ψ(t) := t − ⌊t⌋ − ½. d(n) the divisor function; D(x, y) := Σ_{x<n≤x+y} d(n);
  Main(x, y) := (x+y)log(x+y) − x log x + (2γ − 1)y = y log x + 2γy + O(y²/x).
* TDCAL Lemma S(a): with x = p + 2U, y = 2U one has |E1(p, U)| = S(x, y; U², 4). In the fourth-root range
  (c₁p^{1/4} ≤ U ≤ c₂p^{1/4}, 16U³ ≤ p) the slice position U² is ≍ √x.
* **CNT(η)** (TDCAL): |E1(p, U)| = 2U log 4 + O(U^{1−η}) uniformly in the fourth-root range (primes p only; tied
  x = p + 2U, y = 2U, A = U², θ = 4). Status: Assessment, not established (TDCAL §7).
* **CNT_unif(η, δ; K)** (band-uniform, length decoupled from position): there is C with |E(x, y; A, θ)| ≤ C y^{1−η}
  for all large x, all y ∈ [x^{1/4}/K, Kx^{1/4}], all A ∈ [x^{1/2−δ}, x^{1/2+δ}] and all θ ∈ (1, 4].
  Status: Assessment, not established. CNT_unif is *stronger* than CNT: it asks for all real x, y decoupled from A,
  and uniformity in the position; at A = U², y = 2U, θ = 4, x = p + 2U it contains CNT provided K is large enough for the fixed
  fourth-root range, e.g. K > max(1, 2c₂, 1/(2c₁)) (since y/x^{1/4} = 2U/(p + 2U)^{1/4} tends to values in [2c₁, 2c₂]);
  for K = 1 the inclusion is not literal.
* **SID(η)**: D(x, y) = Main(x, y) + O(x^{(1−η)/4}) for all large x and y ∈ [x^{1/4}/K, Kx^{1/4}].
  *Status (Assessment, search-limited; LIT_CHECK §3, VERIFIED-PRIMARY quotes):* not established in the checked sources.
  * Ivić–Zhai (arXiv 1209.0872, Thm 1): Δ(x+U) − Δ(x) ≪ x^{1/4+ε}U^{1/4} and ≪ x^{2/9+ε}U^{1/3}; at U = x^{1/4} these
    are x^{5/16+ε} and x^{11/36+ε}, above the trivial x^{1/4+ε}; their p. 6 remark: these estimates improve on the trivial one only for U ≥ x^{1/3}. (The global bound
    Δ ≪ x^{0.31448…+ε} of Li–Yang already helps for U ≥ x^{0.3145}; neither reaches U = x^{1/4}.)
  * Jutila's conjecture Δ(x+h) − Δ(x) ≪ x^ε√h (x^ε ≤ h ≤ x^{1/2−ε}) is stated as a conjecture by Ivić (JTNB 21 (2009),
    (1.13)) and by Ivić–Zhai (Conj. 3). Ivić (1.12): Δ(x+h) − Δ(x) = Ω(√h log^{3/2}(√x/h)), so SID(η) can hold only for
    η < 1/2 (the logarithm excludes η = 1/2).
  * Δ(x) = Ω(x^{1/4}) (Hardy; VERIFIED-SECONDARY via Li–Yang (1.3) and Cramér's mean square quoted by Ivić–Zhai). Hence
    the endpoint route |Δ(x+y) − Δ(x)| ≤ |Δ(x+y)| + |Δ(x)| can never give SID, even with the conjectured sup bound
    x^{1/4+ε}.
* **EPC** (exponent pair conjecture; CONJECTURE): (ε, ½ + ε) is an exponent pair for every ε > 0. Named as a conjecture by
  Trudgian–Yang (arXiv 2306.05599, p. 2). Exponent pairs as in Saito et al. (arXiv 2312.15642, Def. 18).

**Targets (kickoff).** (a) Prove that a pointwise power-saving asymptotic for the central slice implies a known open
statement. (b) Or show the central slice is genuinely easier and prove a pointwise result.

## 2. Why this is not already closed

* TDCAL proved the identity (Lemma S(a)) and per-frequency deficits (Prop C), and explicitly established no
  implication between CNT/TD and short-interval divisor statements, in either direction (TDCAL §0, answer 1).
* TDO §6 and TDF §3.1 record self-duality as Assessment only. No reduction theorem exists in the repo.
* The campaign-wide pointwise bound for |E1| is ≪ U^{1+ε} (BILINDIV §2), and TDF §3.3 notes that the ε-free
  implication TD ⇒ DC fails for exactly this reason. `git grep` finds no use of Hooley's Δ or Nair–Tenenbaum for E1.
* None of the closed items of the brief is redone: Theorem L uses exponent pairs only for the *non-central* slices,
  and is a reduction, not a bound by Erdős–Turán with max|S_h|.

## 3. Theorem L: the central band is the EPC-resistant core of SID

**Theorem L.** Let 0 < δ < 1/4, K ≥ 1, L := x^{1/2−δ}, L′ := x/L = x^{1/2+δ}, and y ∈ [1, Kx^{1/4}]. Put
  E_band(x, y; δ) := #{(k, m) : x < km ≤ x + y, L < m ≤ L′} − 2δ·y log x,
  F_L(x, y) := Σ_{m≤L} [ψ((x+y)/m) − ψ(x/m)].
(i) *(PROVED, exact up to O(1).)* For x ≥ x₀(δ, K):
  D(x, y) − Main(x, y) = E_band(x, y; δ) − 2F_L(x, y) + O(1).
(ii) *(CONDITIONAL on (κ, λ) being an exponent pair.)* F_L(x, y) ≪_{κ,λ} x^{(κ + (λ−κ)(1/2−δ))/(κ+1)}·log x + 1.
(iii) *(CONDITIONAL on EPC.)* For every ε > 0, F_L(x, y) ≪_{ε,δ} x^{1/4−δ/2+ε}; hence
  D(x, y) − Main(x, y) = E_band(x, y; δ) + O_{ε,δ,K}(x^{1/4−δ/2+ε}).

*Proof.* (i) Let P := {(k, m) ∈ ℕ² : x < km ≤ x + y}, so D(x, y) = |P|. Split P by m ≤ L, L < m ≤ L′, m > L′ into
P₁, P₂, P₃.
* Since ⌊t⌋ = t − ψ(t) − ½, |P₁| = Σ_{m≤L}(⌊(x+y)/m⌋ − ⌊x/m⌋) = y·H(L) − F_L with H(L) := Σ_{m≤L}1/m.
* Let Q := {(k, m) ∈ P : k ≤ L}. If (k, m) ∈ Q then m > x/k ≥ x/L = L′, so Q ⊂ P₃. If (k, m) ∈ P₃ ∖ Q, then k > L,
  m > L′ and km ≤ x + y, so k < (x + y)/L′ = L(1 + y/x). As Ly/x ≤ Kx^{−1/4−δ} < 1 for large x, at most one integer k
  qualifies, and for it m lies in an interval of length y/k < y/L < 1 (since y ≤ Kx^{1/4} < x^{1/2−δ} = L for large x).
  So |P₃ ∖ Q| ≤ 1. By the symmetry (k, m) ↦ (m, k) of P, |Q| = |P₁|.
* |P₂| = E_band + 2δy log x by definition, and Σ_{L<m≤L′}1/m is not needed.
* Hence D(x, y) = E_band + 2δy log x + 2yH(L) − 2F_L + O(1). With H(L) = log L + γ + O(1/L) and log L = (½ − δ)log x:
  2δy log x + 2yH(L) = y log x + 2γy + O(y/L) = Main(x, y) + O(y/L + y²/x) = Main + O(1). ∎
(ii) Cover (0, L] by the blocks (L/2^{i+1}, L/2^i], i = 0, 1, …, I, with L/2^{I+1} < 1. For N := L/2^{i+1} ≥ 1 and
z ∈ {x, x + y}, Saito et al. Lemma 19 (VERIFIED-PRIMARY; q = 1, δ = η = 0 there) gives
Σ_{N<m≤2N}ψ(z/m) ≪ z^{κ/(κ+1)}N^{(λ−κ)/(κ+1)} + N²/z. Blocks with N < 1 contain ≤ 1 integer. Since λ ≥ ½ ≥ κ, the
exponent of N is ≥ 0; summing over the ≤ log₂L + 2 blocks gives ≪ x^{κ/(κ+1)}L^{(λ−κ)/(κ+1)}log x + L²/x + 1, and
L²/x = x^{−2δ} ≤ 1. Inserting L = x^{1/2−δ} gives (ii).
(iii) Take (κ, λ) = (ε′, ½ + ε′) in (ii): the exponent is (ε′ + ½(½ − δ))/(1 + ε′) ≤ ¼ − δ/2 + ε′. Choose ε′ < ε/2
and absorb log x. Then combine with (i). ∎

**Corollary L1 (hardness; CONDITIONAL on EPC).** If CNT_unif(η, δ; K) holds for some η > 0 and δ ∈ (0, 1/4), then
SID(η′) holds for every η′ < min(η, 2δ).
*Proof.* Cover (L, L′] by the consecutive bands (A_i, θ_iA_i] with A_i = 4^iL, θ_i = 4, except the last, which has
θ ∈ (1, 4]. There are J ≤ 1 + δ log x/log 2 of them, all with A_i ∈ [L, L′]. Their main terms add up to
yΣ_{L<m≤L′}1/m = 2δy log x + O(y/L). So |E_band| ≤ JCy^{1−η} + O(1) ≪ y^{1−η}log x. By Theorem L(iii),
D − Main ≪ y^{1−η}log x + x^{1/4−δ/2+ε}. With y ≍ x^{1/4} this is O(x^{(1−η′)/4}) for η′ < min(η, 2δ). ∎

**Corollary L1′ (fixed bands with polynomial uniformity suffice; CONDITIONAL on EPC).** For η > 0, B ≥ 0 call CNT_poly(η, B; K)
the statement: there is C with |E(x, y; λ√x, θ)| ≤ C(λ + λ^{−1})^B y^{1−η} for all large x, y ∈ [x^{1/4}/K, Kx^{1/4}],
θ ∈ (1, 4] and λ ∈ [x^{−1/8}, x^{1/8}]. (This is a uniform statement for all real x, with y decoupled from the position and a common threshold; it is
implied by CNT_unif(η, 1/8; K) with B = 0. It is *not* implied by fixed-band CNT for each fixed λ, whose constants and
thresholds could depend on λ arbitrarily.) Then CNT_poly(η, B; K) ⟹ SID(η′) for every η′ < min(η/(2B + 1), 1/4).
*Proof.* Take δ := min(η/(4B + 2), 1/8). On the band of Corollary L1 every A_i = λ_i√x has λ_i + λ_i^{−1} ≤ 2x^{δ}, so
|E(x, y; A_i, θ_i)| ≤ C2^Bx^{Bδ}y^{1−η} ≪ y^{1−η+4Bδ} (y ≍ x^{1/4}). Summing over J ≪ log x bands and using Theorem
L(iii): D − Main ≪ y^{1−η+4Bδ}log x + y^{1−2δ}x^{ε}. Since 1 − η + 4Bδ ≤ 1 − 2δ (equality if δ = η/(4B + 2)), both terms are ≪ y^{1−2δ}x^{ε}, and 2δ = min(η/(2B + 1), 1/4). ∎
*Reading (Assessment).* CNT_poly allows the constant to deteriorate polynomially as the band leaves √x, which is
weaker than CNT_unif. Obtaining it from a proof of TDCAL's CNT would additionally require removing the restriction to
primes and to the tied choice of (x, y, A), and uniform thresholds; these are extra requirements, not consequences.

**Corollary L2 (converse; CONDITIONAL on EPC).** SID(η) implies |E_band(x, y; δ)| ≪ x^{(1−η)/4} + x^{1/4−δ/2+ε} for
y ≍ x^{1/4}. So under EPC: SID ⟺ "for some δ > 0, the central band of width x^{±δ} has a power saving".
(Immediate from Theorem L(iii).) It gives nothing for a *fixed* sub-band: sub-bands could cancel.

**Corollary L3 (unconditional range; PROVED).** (715/10238 + ε, 7955/10238 + ε) is an exponent pair for every ε > 0
(Trudgian–Yang, arXiv 2306.05599, Lemma 1.1, (1.6); VERIFIED-PRIMARY, read by the author in the PDF). In (ii) the
exponent is < 1/4 iff ½ − δ < θ(κ, λ) := (1 − 3κ)/(4(λ − κ)), and at ε = 0 this pair has θ = 8093/28960 ≈ 0.27945.
So, **unconditionally**, for δ ∈ (6387/28960, 1/4) (6387/28960 ≈ 0.22055; ε small enough), F_L ≪ x^{1/4−c(δ)} with
c(δ) > 0; hence SID ⟺ a power saving for the band (x^{1/2−δ}, x^{1/2+δ}], and CNT_unif(η, δ) ⟹ SID.
* *Finite search (CERTIFIED for the stated finite set; exact rational arithmetic, `scripts/z56_central_pairs.py`).*
  Over all A/B-words of length ≤ 9 applied to the seeds (0, 1), Bourgain's (13/84, 55/84) and the four pairs of
  Trudgian–Yang (1.6), the largest θ is 8093/28960 (the TY pair itself), then 14848/53141 ≈ 0.27941 (another TY pair)
  and 155/556 ≈ 0.27878 (A(Bourgain) = (13/194, 76/97)). No claim is made that this is the best known pair for θ.
  With EPC, θ → ½.

*Reading (Assessment).*
* Under EPC, per-frequency methods control every dyadic slice m ≍ M with M ≤ x^{1/2−δ}; the slice error is ≪ M^{1/2}x^ε.
  At the central band they give only the benchmark ≍ U (TDCAL Prop C). So, modulo EPC, the *whole* difficulty of SID is
  concentrated in the central band, and the central band is where per-frequency technology is blind.
* Uniformity is the price of the reduction. Heuristically, a method proving CNT at A ≍ √x for all real x would have no
  reason to fail at A = x^{1/2±δ} for small δ (moving off the self-dual point only lengthens the dual sums, which
  per-frequency methods exploit). This is Assessment, not a theorem: TDCAL's CNT (primes, tied parameters, fixed band)
  might in principle be easier than CNT_unif.
* Unconditionally the central band is *not* the only obstacle: slices with x^{0.2795} ≲ M ≤ x^{1/2−δ} are not reached by
  the exponent pairs searched (Cor. L3). Under EPC they are.
* Proving CNT_unif would therefore prove "EPC ⟹ SID". No argument for that implication is given in the checked sources
  (Assessment): EPC gives
  Δ(x) ≪ x^{1/4+ε}, which falls short of SID by the Ω-barrier, and EPC applied per frequency stops at the benchmark.

## 4. Theorem U: CNT follows from twisted short-interval divisor asymptotics

For real t put τ_t(n) := Σ_{de=n}(d/e)^{it} (so |τ_t(n)| ≤ d(n) and τ_0 = d), D_t(x, y) := Σ_{x<n≤x+y}τ_t(n), and
  M_t(x, y) := ∫_x^{x+y}[ζ(1+2it)u^{it} + ζ(1−2it)u^{−it}]du (t ≠ 0),  M_0(x, y) := ∫_x^{x+y}(log u + 2γ)du.
(The integrand of M_t is the u-derivative of the residues of ζ(s+it)ζ(s−it)u^s/s at s = 1 ± it, so M_t is the
difference of those residue main terms between x + y and x; the integrand is continuous at t = 0 because the poles
cancel.)

**Hypothesis TW(η, c; K).** There is C with |D_t(x, y) − M_t(x, y)| ≤ C y^{1−η} for all large x, all
y ∈ [x^{1/4}/K, Kx^{1/4}] and all real |t| ≤ x^c. (TW contains SID(η) as t = 0. Status: Assessment, search-limited: not established in
the checked sources; LIT_CHECK §5 found no pointwise short-interval result for τ_t.)

**Theorem U (PROVED implication).** Let η, c > 0. Then TW(η, c; K) implies CNT_unif(η′, δ; K) for every
0 < δ < 1/4 and every η′ < min(η, 2c).
*Parameter reduction.* TW(η, c; K) contains SID(η), which by Ivić's Ω-result (1.12) forces η < 1/2; and TW(η, c)
implies TW(η, min(c, 1/2)) while min(η, 2 min(c, 1/2)) = min(η, 2c) for η < 1/2. So we may and do assume
0 < η < 1/2 and 0 < c ≤ 1/2; then η′ < 1/2 and all O(1)-type errors below are absorbed.

*Proof.* Fix A ∈ [x^{1/2−δ}, x^{1/2+δ}], θ ∈ (1, 4], y in range, and put a := log(A/√x), b := log(θA/√x), so
|a|, |b| ≤ δ log x + log 4.
* *Mellin form.* For smooth compactly supported g let ĝ(t) := ∫g(v)e^{−itv}dv (a Schwartz function) and
  S_g := Σ_{x<n≤x+y}Σ_{de=n} g(log(d/√n)). Since log(d/√n) = ½log(d/e), Fourier inversion gives
  g(log(d/√n)) = (1/2π)∫ĝ(t)(d/e)^{it/2}dt, hence S_g = (1/2π)∫ĝ(t)D_{t/2}(x, y)dt (finite sum, Fubini).
* *Main term.* Claim: (1/2π)∫ĝ(t)M_{t/2}(x, y)dt = y∫g + O(y x^{−1/2}e^{V}(‖g‖₁ + ‖g′‖₁)) if supp g ⊂ [−V, V] and
  V < ½ log x − 1. Proof: by Fubini (the integrand is bounded near t = 0 and ≪ log(2 + |t|) elsewhere) it is
  ∫_x^{x+y}(∫g + b(u))du, where b(u) := (1/2π)∫ĝ(t)[ζ(1+it)u^{it/2} + ζ(1−it)u^{−it/2}]dt − ∫g. Use
  ζ(s) = 1 + 1/(s − 1) − s∫_1^∞{v}v^{−s−1}dv (Re s > 0) at s = 1 ± it, and L₀ := ½log u:
  * the constant 1 gives g(L₀) + g(−L₀) = 0, since L₀ ∉ supp g;
  * the two 1/(±it) terms combine to (1/2π)∫ĝ(t)·2sin(tL₀)/t dt = ∫_{−L₀}^{L₀}g = ∫g;
  * the integral terms give −∫_1^∞{v}v^{−2}[(g + g′)(L₀ − log v) + (g − g′)(log v − L₀)]dv, using
    (1/2π)∫ĝ(t)e^{itw}dt = g(w) and (1/2π)∫ĝ(t)(it)e^{itw}dt = g′(w). Substituting v = e^{L₀∓w}, this is bounded by
    u^{−1/2}∫(|g| + |g′|)(w)(e^{w} + e^{−w})dw ≤ 2u^{−1/2}e^{V}(‖g‖₁ + ‖g′‖₁).
* *Sandwich.* Let w := x^{−c/2} (≥ y/(2x) for large x, since c ≤ 1/2). Choose smooth g₊, g₋ with values in
  [0, 1], monotone on each transition region (each of length w), |g_±^{(j)}| ≪_j w^{−j} (so ‖g_±^{(j)}‖₁ ≪_j w^{1−j}
  for j ≥ 1, uniformly in θ), g₊ = 1 on [a − w, b + w], supp g₊ ⊂ [a − 2w, b + 2w]; and, if b − a > 4w,
  g₋ = 1 on [a + 2w, b − 2w], supp g₋ ⊂ [a + w, b − w] (else g₋ := 0). For n ∈ (x, x+y],
  log(m/√n) = log(m/√x) − ½log(n/x) with 0 ≤ ½log(n/x) ≤ y/(2x) ≤ w. Hence
  g₋(log(m/√n)) ≤ 1[A < m ≤ θA] ≤ g₊(log(m/√n)) for every divisor m of n, and S_{g₋} ≤ S(x, y; A, θ) ≤ S_{g₊}.
* *Error.* For g = g_±: S_g − y∫g = (1/2π)∫ĝ(t)[D_{t/2} − M_{t/2}]dt + O(y x^{δ−1/2}).
  * |t| ≤ 2x^c: by TW, ≤ Cy^{1−η}(1/2π)∫|ĝ| ≪ y^{1−η}log(2/w), since |ĝ(t)| ≤ min(‖g‖₁, ‖g′‖₁/|t|, ‖g″‖₁/t²) with
    ‖g‖₁ ≤ 2, ‖g′‖₁ ≤ 2, ‖g″‖₁ ≪ 1/w.
  * |t| > 2x^c: |D_{t/2}| ≤ D(x, y) ≪ y x^{ε} and |M_{t/2}| ≪ y log(2 + |t|), while |ĝ(t)| ≤ ‖g^{(j)}‖₁|t|^{−j}
    ≪_j w^{1−j}|t|^{−j}. With w = x^{−c/2} the contribution is ≪_j y x^{ε}(x^{c}w)^{1−j} = y x^{ε−(j−1)c/2},
    negligible for j large.
* *Main terms.* y∫g_± = y(b − a) + O(yw) = y log θ + O(yw), and yΣ_{A<m≤θA}1/m = y log θ + O(y/A).
* Altogether |E(x, y; A, θ)| ≪ y^{1−η}log x + yx^{−c/2} + yx^{δ−1/2} + y/A. With y ≍ x^{1/4}, δ < 1/4 and
  A ≥ x^{1/4}: this is ≪ y^{1−η′} for every η′ < min(η, 2c). ∎

*Reading (Assessment).* Theorems L and U sandwich the central slice between two forms of the short-interval divisor
problem at length x^{1/4}: (SID with all small twists t) ⟹ CNT_unif ⟹ (EPC ⟹ SID). The twisted family is the natural
home of the central slice: a band of divisors in log-scale is a Fourier integral over t of τ_t. Nothing indicates that
the central restriction makes the problem easier.

### 4.1 Theorem E: the converse under EPC, hence an equivalence

**Theorem E (CONDITIONAL on EPC).** Let η > 0 and 0 < δ < 1/4. Then CNT_unif(η, δ; K) implies TW(η″, c; K) with
c := min(η/16, δ/4) and every η″ < min(δ, η/4).
**Corollary E1 (CONDITIONAL on EPC).** With Theorem U: for every fixed K ≥ 1, under EPC,
"∃η > 0, ∃δ ∈ (0, 1/4): CNT_unif(η, δ; K)" ⟺ "∃α > 0, ∃c > 0: TW(α, c; K)" (exponents are not preserved). In words: modulo EPC, the uniform central-slice asymptotic is *equivalent* to
power-saving short-interval asymptotics at length x^{1/4} for the coefficients of ζ(s+it)ζ(s−it), |t| ≤ x^c; the
member t = 0 is SID.

*Proof of Theorem E.* Fix y ∈ [x^{1/4}/K, Kx^{1/4}] and real t with |t| ≤ x^c; L, L′, P, P₁, P₂, P₃, Q as in the proof
of Theorem L(i). D_t(x, y) = Σ_{(k,m)∈P}(m/k)^{it}, since τ_t(n) = Σ_{km=n}(m/k)^{it} (τ_t is real, being symmetric).
* *Non-central part.* As P₃ = Q up to ≤ 1 point and Q is the image of P₁ under (k, m) ↦ (m, k), the contribution of
  P₁ ∪ P₃ is Σ_{(k,m)∈P₁}2cos(t log(m/k)) + O(1). For km = n ∈ (x, x+y], log(m/k) = log(m²/x) − log(n/x) with
  0 ≤ log(n/x) ≤ y/x, so this equals Σ_{m≤L}c_m(⌊(x+y)/m⌋ − ⌊x/m⌋) + O(|t|(y/x)|P|), c_m := 2cos(t log(m²/x)).
  Write the floor difference as y/m − [ψ((x+y)/m) − ψ(x/m)]. On each dyadic block (N, 2N], |c_m| ≤ 2 and the total
  variation of c_m is ≤ 4|t|log 2, so by Abel summation and Saito et al. Lemma 19 with (κ, λ) = (ε′, ½ + ε′) (any
  N < N′ ≤ 2N), |Σ_{N<m≤2N}c_m ψ(z/m)| ≪ (1 + |t|)x^{ε}N^{1/2}. Summing over blocks as in Theorem L(ii)–(iii): the
  ψ-part is ≪ (1 + |t|)x^{1/4−δ/2+ε}. Also |P| = D(x, y) ≪ yx^{ε}.
* *Central part.* Let w := x^{−η/8} and cut (L, L′] into consecutive bands B_j = (A_j, θ_jA_j], A₀ = L,
  A_{j+1} = θ_jA_j, θ_j = e^{w} except the last (θ ∈ (1, e^{w}]); there are J ≤ 2δ log x/w + 1 bands, all with
  A_j ∈ [L, L′] and θ_j ∈ (1, 4]. For m ∈ B_j and n = km ∈ (x, x+y], log(m/k) = log(m²/n) lies within 2w + y/x of
  φ_j := 2log A_j − log x, so (m/k)^{it} = e^{itφ_j} + O(|t|(w + y/x)). By CNT_unif, S_j := S(x, y; A_j, θ_j) =
  yΣ_{m∈B_j}1/m + O(y^{1−η}). Also |(m²/x)^{it} − e^{itφ_j}| ≤ 2|t|w on B_j. Hence
  Σ_{P₂}(m/k)^{it} = yΣ_{L<m≤L′}(m²/x)^{it}/m + O(Jy^{1−η} + |t|(w + y/x)yx^{ε} + |t|wy log x).
* *Main term.* Altogether D_t(x, y) = Main_t + (errors above), where
  Main_t := y[Σ_{m≤L}((m²/x)^{it} + (m²/x)^{−it})/m + Σ_{L<m≤L′}(m²/x)^{it}/m]
          = y[x^{−it}Σ_{m≤L′}m^{−1+2it} + x^{it}Σ_{m≤L}m^{−1−2it}].
  Euler–Maclaurin, Σ_{m≤X}m^{−s} = ζ(s) − X^{1−s}/(s − 1) + O(|s|X^{−σ}/σ + X^{−σ}) (σ = Re s > 0, s ≠ 1), at
  s = 1 ∓ 2it gives Main_t = y[ζ(1−2it)x^{−it} + ζ(1+2it)x^{it}] + y[(L′²/x)^{it} − (x/L²)^{it}]/(2it) + O(y(1 + |t|)/L),
  and L′²/x = x/L² = x^{2δ}, so the middle term vanishes. (At t = 0 read the bracket as its limit log x + 2γ; all
  error terms are uniform in t.) Finally G(u) := ζ(1+2it)u^{it} + ζ(1−2it)u^{−it} has G′(u) ≪ (1 + |t|)log(2 + |t|)/u
  (for |t| ≤ 1 use ζ(1+2it) = 1/(2it) + γ + O(|t|)), so M_t(x, y) = yG(x) + O(y²(1 + |t|)log(2 + |t|)/x).
* *Bookkeeping.* With |t| ≤ x^c, w = x^{−η/8} and y ≍ x^{1/4}, the errors are
  ≪ y^{1−2δ+4c+4ε} + y^{1−η+η/2}log x + y^{1−4(η/8−c)+4ε} + (lower order). With c = min(η/16, δ/4) these are
  ≪ y^{1−min(δ, η/4)+4ε}. ∎

*Reading (Assessment).* Corollary E1 is the cleanest form of the calibration: modulo EPC, a uniform central-slice
asymptotic *is* the x^{1/4} short-interval divisor problem for the small-twist family τ_t, nothing less and nothing
more. Its t = 0 member is SID. Removing EPC leaves the two implications of Theorems U (unconditional) and E (needs the
non-central slices).

## 5. Proposition P: a pointwise upper bound of the right order up to log log

Let Δ_H(n) := max_{v∈ℝ} #{d | n : e^v < d ≤ e^{v+1}} (Hooley's Δ-function; notation Δ_H to avoid clashing with the
divisor-problem error Δ(x)).

**Proposition P (PROVED relative to de la Bretèche–Tenenbaum, arXiv 2512.05652, Corollary 1.2).** Fix ε₀ > 0. For
x ≥ x₀(ε₀), x^{ε₀} ≤ y ≤ x, every A > 0 and 1 < θ ≤ e²:
  S(x, y; A, θ) ≤ 2Σ_{x<n≤x+y}Δ_H(n) ≪_{ε₀} y(log log x)^{5/2}.
In particular |E1(p, U)| ≪ U(log log U)^{5/2} for every prime p and U in the fourth-root range, and also
|E1⁺| ≪ U(log log U)^{5/2}.
*Proof.*
* S(x, y; A, θ) = Σ_{x<n≤x+y}#{m | n : A < m ≤ θA}, since for each n the pairs (k, m) with km = n are the divisors m.
* (A, θA] ⊂ (A, eA] ∪ (eA, e²A], and each piece is of the form (e^v, e^{v+1}], so #{m | n : A < m ≤ θA} ≤ 2Δ_H(n).
* dlB–T Cor. 1.2 (VERIFIED-PRIMARY, p. 2): for F ∈ ℤ[X] irreducible with no fixed prime divisor, t ≥ 1, ε > 0,
  Σ_{x<n≤x+y}Δ_H(|F(n)|)^t ≪ y(log x)^{β(t,1)−1}(log₂x)^{t+1+δ(t,1)/2} for x^ε ≤ y ≤ x, where β(t, z) = 2^t z − t and
  δ(t, z) = 1_{z=z_t}, z_t = t/(2^t − 1). With F(X) = X (irreducible, no fixed prime divisor) and t = 1: β = 1, z₁ = 1,
  δ = 1, giving y(log log x)^{5/2}.
* For E1: x = p + 2U, y = 2U ≥ x^{1/5} for large p, A = U², θ = 4 < e². ∎

*Remarks.*
* An alternative route with exponent 11/4 is Nair–Tenenbaum (VERIFIED-SECONDARY via Henriot) applied to Δ_H, which lies
  in their class because Δ_H(mn) ≤ τ(m)Δ_H(n) (Hall–Tenenbaum Lemma 61.1, VERIFIED-SECONDARY), together with
  Koukoulopoulos–Tao Thm 1 (VERIFIED-PRIMARY).
* The dominating sum ΣΔ_H cannot be O(y) uniformly: on long intervals Σ_{n≤x}Δ_H(n) ≫ x(log log x)^{1+η−ε}
  (Ford–Koukoulopoulos–Tao Thm 2, VERIFIED-PRIMARY). This limits the Δ_H route only; it does not disprove |E1| ≪ U,
  which is not established here (Assessment: no mechanism for concentration in every short interval is visible).
* *What it buys for gap 1.*
  * The zero mode of every Fourier argument on E1⁺ is now ≪ U(log log U)^{5/2}.
  * Cor. P2 below: TD(η) ⇒ DC(2U^{−η}) up to a (log log U)^{5/2} loss. (TDF §3.3's Erdős–Turán proof of TD ⇒ DC_ε
    would keep a factor log U from Σ_h 1/h; a localized Fejér argument removes it.)
  * TDCAL Prop D(iii): Σ_{|τ|≤T}N^{[τ]} ≤ |E1| + 2TΣD^{−1/2} ≪ U(log log U)^{5/2} + TU^{1/2+ε}. The second term is
    unchanged, so the gap to the model order T persists for T ≤ U^{1/2}.
  * N₂ itself gains nothing: N₂ ≤ (1 − log 2 + o(1))U is already known (TDCAL Remark A‴).

**Corollary P2 (PROVED implication; uses Prop P).** Let 0 < η < 1, put H := ⌊U^η⌋, and assume TD(η) at (p, U):
|T(h)| ≤ C₀U^{1−η} for 1 ≤ h ≤ U^η, where T(h) = Σ_{k∈E1⁺}e(hw_k) (TDCAL §1). Then for every interval I ⊂ ℝ with
|I| ≥ 1/H, #{k ∈ E1⁺ : w_k mod 1 ∈ I} ≪ (1 + C₀)·U|I|(log log U)^{5/2}, the implied constant absolute (U ≥ U₀).
*Proof.*
* Fejér kernel F_H(v) := Σ_{|h|<H}(1 − |h|/H)e(hv) = H^{−1}(sin πHv/sin πv)² ≥ 0. For ‖v‖ ≤ 1/(2H), sin(πH|v|) ≥ 2H|v|
  (concavity of sin on [0, π/2]) and |sin πv| ≤ π|v|, so F_H(v) ≥ 4H/π².
* For an interval J of length 1/H with centre α: #{k : w_k mod 1 ∈ J} ≤ (π²/4H)Σ_{k∈E1⁺}F_H(w_k − α)
  = (π²/4H)Σ_{|h|<H}(1 − |h|/H)e(−hα)T(h) ≤ (π²/4H)(|E1⁺| + 2Σ_{1≤h<H}|T(h)|) ≤ (π²/4)(|E1⁺|/H + 2C₀U^{1−η}).
* By Prop P, |E1⁺| ≪ U(log log U)^{5/2}; with H ≥ U^η/2 the right side is ≪ (1 + C₀)U^{1−η}(log log U)^{5/2}.
* Cover I by ⌈H|I|⌉ ≤ 2H|I| intervals of length 1/H and multiply: ≪ (1 + C₀)H|I|U^{1−η}(log log U)^{5/2}
  ≤ (1 + C₀)U|I|(log log U)^{5/2}. ∎

## 6. Where the proofs stop (escape hatches)

* Theorem L uses EPC only to discard non-central slices; the central band is untouched. Any unconditional hardness
  theorem for the *fixed* band would need a mechanism that moves divisors between positions. ℤ-linear maps cannot do
  this: the form km has square discriminant, so its integral automorphism group is finite (Assessment; standard).
* Theorem U's hypothesis is a *family* statement. Its t = 0 member is SID. Whether finitely many t suffice is not
  addressed here.
* Prop P is first-order: it bounds the count, not its fluctuation. A pointwise O(U) bound, and any pointwise lower
  bound |E1| ≫ U, are open (Assessment: the elementary near-diagonal families (M − j)(M + j + t) give only O(1) points
  at every x).

## 7. Degenerate-Hessian remark

*Context (Assessment).* After Vaaler truncation in ψ and the B-process in m (stationary phase at m ≍ √x), the
frequency-h piece of the central slice has dual variable n ≍ h and phase ±2√(xhn) (standard; this is the
self-duality of TDO §6 / TDF §3.1, not re-derived here with error terms).

**Remark H (PROVED).** The function Φ(h, n) := 2√(xhn) is
homogeneous of degree 1 in (h, n), so by Euler's relation its Hessian annihilates (h, n) and det ∇²Φ ≡ 0 (the
Hessian itself has rank one for h, n > 0). Explicitly,
Φ_hh = −½√x h^{−3/2}n^{1/2}, Φ_nn = −½√x n^{−3/2}h^{1/2}, Φ_hn = ½√x(hn)^{−1/2}, and Φ_hhΦ_nn − Φ_hn² = 0.
*Reading (Assessment).* Double-exponential-sum methods that need a non-degenerate Hessian (two-dimensional exponent
pairs, Huxley–Kolesnik double sums) do not apply directly. Along the degenerate rays h/n = const the phase is linear.
*Formally* (not a derivation: Vaaler and stationary phase leave (h, n)-dependent weights, so grouping by N = hn gives a
weighted, restricted divisor coefficient to which no standard Voronoi formula applies as is), the sum collapses to
Σ_N τ_c(N)e(2√(xN)) with τ_c a central divisor count, and the Voronoi dual of the unrestricted analogue has its
stationary point at n = x, i.e. back at the short interval of length ≍ x^{1/4}. This formal picture is consistent with
Theorem L: the central band sits at the fixed point of the duality.

## 8. Computations (EVIDENCE; `scripts/z56_central_slices.c`, `data/z56/central/slices_*.txt`, summary `stats.txt`)

*Setup.* Inputs `data/z56/central/inputs.txt` (from `scripts/z56_central_inputs.py`): U = ⌊p^{1/4}⌋, x = p + 2U,
y = 2U (TDCAL's convention), so the central band (U², 4U²] is exactly E1. Families: `gen` = first prime after
10^k + i·10^{k/2+1} (windows far apart); `sq` = odd squares x = N² (U = ⌊x^{1/4}⌋); `nsq` = near-squares p = N² − c,
c ∈ (2U, 4U] the least with p prime (the interval (x, x + y] then contains N²); `test` = FRONTIER §4 item-14 primes
(409, …, 8 813 281) and 193, 2521, 66529, 3361, 5101441. For each x the program computes D(x, y) exactly by the
hyperbola identity, the fixed band error Ec := E(x, y; U², 4) = |E1| − yΣ1/m, F_L and E_band for δ ∈ {0.05, 0.10,
0.15, 0.20}, and the dyadic slice errors E_M over (M, 2M], M = y·2^j ≤ √x. Output conventions are in the header of
the C file: it prints FLc = −F_L, and, outside the direct runs, the *proxy* Derr − 2FLc = E_band + O(1) (Theorem L(i))
in place of E_band. Exactness was checked against a direct
sympy enumeration at x = 10⁸ + 7 (D − Main = −247.0226, Ec = −60.2514 both ways).

*Identity check (CERTIFIED for these inputs).* At 10¹⁰ (600 inputs) E_band was also computed directly (loop to
x^{1/2+δ}); the residual D − Main − (E_band − 2F_L) has max |·| = 0.632 over all 2400 (x, δ) pairs (attained at x = 10000000651,
δ = 0.20), as Theorem L(i) predicts: the exact residual is R + 2y(H(L) − log L − γ) − [(x+y)log(1 + y/x) − y] with
R ∈ {0, 1}, which is O(1 + y/L + y²/x). (With harmonic centring of the band the maximum is 0.316; the first draft
reported that variant by mistake.) At larger x the program prints the proxy Derr − 2FLc = E_band + O(1) instead.

**Table 8.1** (rms and mean in units of √y, each observation normalised by its own y; n = number of x; the y and model
columns give the first sample only — the full ranges are in `stats.txt`: sq10/nsq10 span x ≈ 10¹⁰–2.5·10¹¹,
y = 632–1410, model 10.26–12.80; sq12/nsq12 have y = 2000–2188 (9.4 % spread); the remaining families have y within 0.5 % of the first). E_band columns at 10¹² and above are
the proxy.

| family | n | y | mean (D−Main) | rms (D−Main) | Ivić leading model √((8/π²)log³(√x/y)) | mean Ec | rms Ec | rms F_L, δ = .05/.10/.15/.20 |
|---|---|---|---|---|---|---|---|---|
| gen 10¹⁰ | 200 | 632 | −0.22 | 11.49 | 10.26 | +0.11 | 2.37 | 4.04 / 2.61 / 1.53 / 0.85 |
| gen 10¹² | 100 | 2000 | +3.40 | 16.92 | 13.95 | +0.64 | 2.84 | 6.09 / 3.91 / 2.20 / 1.03 |
| gen 10¹⁴ | 50 | 6324 | +6.58 | 22.23 | 18.00 | +1.62 | 3.87 | 7.22 / 4.34 / 2.56 / 1.18 |
| gen 10¹⁶ | 24 | 20000 | −8.98 | 22.96 | 22.38 | −0.96 | 2.80 | 8.23 / 5.56 / 3.04 / 1.04 |
| sq 10¹⁰ | 200 | 632 | −10.30 | 16.47 | 10.26 | −1.12 | 2.54 | 6.32 / 4.56 / 2.92 / 1.59 |
| sq 10¹² | 100 | 2000 | −11.70 | 19.17 | 13.95 | −0.92 | 2.69 | 7.35 / 5.26 / 3.39 / 1.83 |
| sq 10¹⁴ | 50 | 6324 | −18.86 | 26.03 | 18.00 | −1.22 | 2.95 | 10.09 / 7.45 / 4.72 / 2.44 |
| sq 10¹⁶ | 24 | 20000 | −16.88 | 23.17 | 22.38 | −0.51 | 2.28 | 9.65 / 7.21 / 4.43 / 2.12 |
| nsq 10¹⁰ | 200 | 632 | −3.53 | 13.34 | 10.26 | −0.18 | 2.49 | 4.80 / 3.33 / 2.09 / 1.10 |
| nsq 10¹² | 100 | 2000 | −4.32 | 16.77 | 13.95 | −0.30 | 2.70 | 6.01 / 3.95 / 2.26 / 1.17 |
| nsq 10¹⁴ | 50 | 6324 | −12.87 | 22.79 | 18.00 | −1.15 | 3.13 | 8.28 / 5.40 / 3.24 / 1.53 |
| nsq 10¹⁶ | 24 | 20000 | −16.84 | 30.47 | 22.38 | −0.98 | 3.47 | 11.40 / 7.32 / 3.93 / 1.87 |

**Table 8.2** (dyadic slice errors, rms / mean in units of √(y log 2), the Bernoulli-model sd; first and last slices).

| family | slices | rms, first … last common slice (min–max over slices) | mean (min … max over slices) |
|---|---|---|---|
| gen 10¹⁰ | 8 | 0.56 … 1.54 (0.56–1.54) | −0.19 … +0.18 |
| gen 10¹⁴ | 11 | 0.54 … 2.56 (0.54–2.56) | −0.05 … +1.14 |
| gen 10¹⁶ | 13 | 0.52 … 1.69 (0.52–1.86) | −0.74 … +0.05 |
| sq 10¹⁰ | 8 | 0.85 … 1.66 (0.85–1.66) | −0.67 … −0.60 |
| sq 10¹⁶ | 13 | 0.67 … 1.55 (0.67–1.63) | −1.12 … −0.29 |
| nsq 10¹⁰ | 8 | 0.65 … 1.60 (0.65–1.60) | −0.37 … −0.12 |
| nsq 10¹⁶ | 13 | 0.84 … 2.00 (0.84–2.22) | −1.09 … −0.46 |
(Slices are indexed j = 0, 1, … up to the largest index common to all inputs of the family; full rows in `stats.txt`.)

*Readings (EVIDENCE unless marked).*
* The central fixed band has error rms ≈ 2.3–3.9·√y at every scale tested, with no visible growth from 10¹⁰ to 10¹⁶; this
  matches TDCAL §10.4 (sd ≈ 2.2–3.3·√U = 1.6–2.3·√y there, other sample). Nothing distinguishes the central band from
  other slices except its position.
* Slice rms values broadly grow (not monotonically in every row) from ≈ 0.52–0.56 at M = y in the generic families
  (the independent-Bernoulli value there is √((log 2 − ½)/log 2) ≈ 0.53) to ≈ 1.5–2.6 near √x: the m's are positively
  correlated (integers with many divisors), not independent.
* The sample rms of F_L decreases with δ in every family (fewer slices); individual values of F_L are not monotone in δ.
* **Squares and near-squares (T1 controls).** Both families have a negative mean in *every* dyadic slice, between
  −0.12 and −1.12·√(y log 2), and a total mean of −3.5 to −19·√y. The central band carries −0.18 to −1.22·√y of it.
  *Heuristic (Assessment):* at x = N² the Voronoi terms with square index n = r² have aligned phases
  e(2√(nx)) = e(2rN) = 1; those with r ≍ x^{1/4} feel the shift y, and their coherent sum is of size
  ≍ x^{1/8}(log x)^{O(1)} ≍ √y·polylog. This is consistent with Ivić's Ω(√h log^{3/2}) and does not threaten CNT(η) for
  η < 1/2. No test of the polylog exponent was made.
* Test primes (`slices_test.txt`, U = 3–54; p = 193 has U = 3, outside TDCAL's U ≥ 4 convention, the count is still
  well defined): max |Ec| = 19.30 (p = 5101441, y = 94); max |Ec|/√y = 2.55 (p = 329617, Ec = +17.26, y = 46). These scales are too small to say anything; they are recorded as the required control.

## 9. FRONTIER §4 hard screens

1. **T1 (odd squares).** All statements are about integers x, not primes, and hold at squares; they are upper-bound or
   calibration statements, silent on positivity by design. EVIDENCE: odd squares have a negative mean slice error
   (§8), within the √y scale.
2. **8/131.** Numerator-blind (counts strip points of E1 only); not an ES step.
3. **Tied modulus.** Not touched: the statements concern the count of the strip, not the tie (w ∈ ℤ).
4. **Fixed p.** Every statement is pointwise in x: Thm L(i) is an identity, L(ii)–(iii) and U are pointwise
   implications, Prop P is a pointwise bound. No averaging over p, n or U anywhere.

## 10. Proposed FRONTIER §7 text (do NOT edit FRONTIER here)
Append to §7.1 after the z55 TDCAL bullets:
> * **How hard is the central slice? (`Z56_CENTRAL.md`, z56; internal; calibration, upper-bound only.)**
>   * Thm L (PROVED identity): D(x, y) − Main = E_band(δ) − 2F_L + O(1), where E_band is the band
>     m ∈ (x^{1/2−δ}, x^{1/2+δ}] and F_L = Σ_{m≤x^{1/2−δ}}[ψ((x+y)/m) − ψ(x/m)]. Under EPC, F_L ≪ x^{1/4−δ/2+ε}.
>   * Hence (CONDITIONAL on EPC) SID ⟺ a power saving for some central band, and CNT_unif ⟹ SID; so does CNT_poly
>     (constants polynomial in the band position). Here SID = pointwise power saving for Σ_{x<n≤x+x^{1/4}}d(n); it is
>     not established in the checked sources (the cited Ivić–Zhai bounds help only for lengths ≥ x^{1/3}, Jutila's
>     conjecture is open, and Δ = Ω(x^{1/4}) blocks the endpoint route). CNT_unif/CNT_poly are stronger than TDCAL's
>     CNT (all real x, length decoupled from position, uniform thresholds).
>   * Unconditionally (PROVED; Trudgian–Yang pair (715/10238, 7955/10238)) this argument gives the equivalence for
>     δ > 6387/28960 ≈ 0.2205.
>   * Thm U (PROVED implication): power-saving short-interval asymptotics for τ_t(n) = Σ_{de=n}(d/e)^{it}, uniformly in
>     |t| ≤ x^c, imply CNT_unif. Thm E (CONDITIONAL on EPC): the converse. So under EPC, CNT_unif ⟺ the x^{1/4}
>     short-interval asymptotic for the small-twist family τ_t (t = 0: SID).
>   * Prop P (PROVED rel. de la Bretèche–Tenenbaum 2025 Cor. 1.2): |E1(p, U)| ≪ U(log log U)^{5/2} pointwise (was
>     U^{1+ε}). Cor. P2 (PROVED implication, localized Fejér): TD(η) ⟹ DC(2U^{−η}) with a (log log U)^{5/2} loss.
>   * Assessment: the count enters gap 1 only as a zero mode; CNT-type asymptotics are SID-hard (modulo EPC and
>     uniformity) and should not be on the route to TD/NC.

## 11. Bottom line
The central slice of the x^{1/4} short-interval divisor problem is, modulo the exponent pair conjecture, the whole of
that problem: everything outside a band of width x^{±δ} around √x is per-frequency-easy under EPC, and the band carries
the rest exactly (Theorem L). A uniform, length-decoupled version of CNT (CNT_unif, or CNT_poly with constants
polynomial in the band position) would thus prove SID given EPC: a pointwise statement beyond the Ω-barrier of the
Dirichlet divisor problem that no checked source reaches. In the other direction, CNT_unif follows from twisted versions
of SID (Theorem U), and under EPC is equivalent to them (Theorem E). So CNT is SID-hard, up to EPC and uniformity, and no easier structure was found. What is pointwise
and unconditional is an upper bound of the right order up to (log log U)^{5/2} (Prop P), which is all that the zero mode
of the gap-1 Fourier arguments needs (Cor. P2). Nothing here touches positivity, and ES remains open.

## 12. Reproduction
All runs under `ulimit -v 2000000`, each with the shown `timeout`; one core each; total ≈ 1 h CPU.
```
cd $REPO; D=data/z56/central; ulimit -v 2000000
timeout 120 uv run python scripts/z56_central_pairs.py                                  # Cor. L3 table
timeout 600 uv run --with sympy python scripts/z56_central_inputs.py /tmp/in.txt        # = $D/inputs.txt
gcc -O2 -o /tmp/z56sl scripts/z56_central_slices.c -lm
for t in 10 12 14 16; do grep -E " (gen|sq|nsq)$t\$" /tmp/in.txt > /tmp/in$t.txt; done; grep " test$" /tmp/in.txt > /tmp/intest.txt
Z56_DIRECT=1 timeout 1800 /tmp/z56sl < /tmp/in10.txt > $D/slices_e10.txt                # direct E_band (identity check)
timeout 1800 /tmp/z56sl < /tmp/in12.txt > $D/slices_e12.txt
timeout 1800 /tmp/z56sl < /tmp/in14.txt > $D/slices_e14.txt
for f in gen sq nsq; do grep " ${f}16$" /tmp/in16.txt > /tmp/${f}16; timeout 1800 /tmp/z56sl < /tmp/${f}16 > $D/slices_e16_$f.txt; done  # ~25 min each, run in parallel
timeout 600 /tmp/z56sl < /tmp/intest.txt > $D/slices_test.txt
timeout 120 uv run python scripts/z56_central_stats.py $D/slices_e1*.txt > $D/stats.txt
```
The stored e12–e16 and test files were produced by the first version of `z56_central_slices.c` (four band columns
Eband Eband_h FLc resid_h; non-direct runs print the proxy in both Eband columns and nan residuals); the current
version adds the Theorem-L residual column. All shared columns are identical (the review reran three e10 inputs
byte-identically with the first version; `slices_e10.txt` was regenerated with the current version).

## 13. Review log
**Hostile review 1** (deep-mode subagent; `reviews/z56_central_review1.md`). Verdict **CORRECT-WITH-FIXES**
(4 MAJOR, 8 MINOR, 1 NIT). Confirmed: Theorem L(i)–(iii) and Cor. L1/L1′/L2/L3 as quantified; Theorem U (Fourier
normalisation, ζ-identity signs, b(u) bound, sandwich direction, ĝ bounds); Prop P (covering, dlB–T Cor. 1.2 exponent
5/2 re-read in the PDF); Remark H derivatives; all Table 8.1 entries (stats regenerated byte-identically; three e10
inputs rerun identically; sympy check reproduced). Fixes applied:
1. (MAJOR) Cor. L1′: the claim that any proof of fixed-band CNT gives CNT_poly is deleted; CNT_poly is now stated as a
   uniform all-x, length-decoupled hypothesis (B ≥ 0), stronger than TDCAL's prime/tied CNT; the gap is listed as an
   extra requirement (§0, §3, §10, §11).
2. (MAJOR) Unconditional range: Trudgian–Yang Lemma 1.1 (1.6) pair (715/10238, 7955/10238) gives θ = 8093/28960 and
   δ > 6387/28960 ≈ 0.2205 (re-read in the PDF); the search now includes the TY pairs as seeds and is labelled a finite
   search with no optimality claim.
3. (MAJOR) TD ⇒ DC with a loglog loss now has its own proof (Cor. P2, localized Fejér kernel); the "same proof" claim
   is withdrawn.
4. (MAJOR) Identity residual: the program now computes the Theorem-L residual (log-centred band); the reported max is
   0.632 (was 0.316, the harmonic-centred variant). The C header's equations are corrected and the large-x band column
   is called a proxy.
5. Sup-norm and literature wording narrowed ("endpoint route"; "the cited Ivić–Zhai estimates"; Li–Yang reaches
   x^{0.3145}; "not established in the checked sources"; SID(η) needs η < 1/2).
6. Pair search evaluates all words of length ≤ 9.
7.–9. Table 8.2 corrected (gen16 last common slice 1.69; ranges), readings corrected (rms of F_L decreases, not F_L;
   bias ranges −0.12 … −1.12), first-sample labelling and full ranges for Table 8.1, test-prime U range 3–54 and the
   normalisation of the "largest" value.
10. Remark H: "Hessian determinant vanishes" (rank one); the τ_c/Voronoi collapse is labelled a formal analogy.
11. Theorem U: η, c > 0 explicit; reduction to η < 1/2, c ≤ 1/2 justified; taper construction uniform in θ.
12. Label pass: EPC is CONJECTURE; Cor. L3 PROVED with the finite search CERTIFIED; CNT/TW/SID statuses are
    Assessment; the sandwich is written {SID_t} ⟹ CNT_unif ⟹ (EPC ⟹ SID).
13. M_t described as a difference of residue main terms.

**Hostile review 2** (deep-mode subagent; `reviews/z56_central_review2.md`), on Theorem E / Cor. E1 and on the
review-1 fixes. Verdict **CORRECT-WITH-MINOR-FIXES**, no MAJOR. Theorem E verified line by line (decomposition, Abel
summation with Lemma 19 partial sums, thin bands, Euler–Maclaurin signs and exact cancellation, uniformity at t = 0,
exponent bookkeeping); all 13 review-1 fixes confirmed. Fixes applied: composite labels split (§0 items 1 and 4,
Remark H); FRONTIER text says "this argument gives the equivalence for δ > …" instead of "only"; Cor. E1 states the
fixed K and the existential quantifiers explicitly.

**Cross-model review** (`data/z56/xreview/REVIEW_CENTRAL.md`; checker `scripts/z56_xrev_central_check.py`). Verdict
**ACCEPT-WITH-FIXES** (two minor). All of L(i)–(iii), L1–L3, U, E/E1, P, P2 and H confirmed against independently read
primary sources; stats and inputs reproduced byte-identically; all 2400 identity residuals recomputed in 60-digit
arithmetic (max 0.631850…). Fixes applied: (1) §1: "CNT_unif contains CNT" now requires K > max(1, 2c₂, 1/(2c₁));
(2) §8: the y-spread of sq12/nsq12 (9.4 %) is stated instead of "within 1 %".
