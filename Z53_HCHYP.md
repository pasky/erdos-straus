# Z53_HCHYP — which hypothesis could give HC(p) ≪ (log p)^A? (wave z53, lane HCHYP)

**ES is open. Nothing here proves or disproves ES, conditionally on a standard conjecture or otherwise.**
Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. All results are internally reviewed
only. Scripts `scripts/z53_hchyp_*`, data `data/z53/hchyp/` (4 MB). Kickoff: `z53_lanes.md` §HCHYP (FRONTIER §7.2/§7.4).

## 0. Verdict first

**Verdict (Assessment): NARROWED.** No standard conjecture is shown to give HC(p) ≪ (log p)^A, and none is found to. No
hypothesis that is both natural and not ES-specific survives review in a form known to be free of counterexamples. What
this lane adds:

1. **The model scale is (log p)^{2 log 2} (Theorem M, PROVED in an explicit Kubilius model 𝔐).** In 𝔐, almost surely
   HC(p) ≤ (log p)^A for all large p when A > 2 log 2 ≈ 1.386, and HC(p) > (log p)^θ for infinitely many p when
   θ < 2 log 2. The boundary A = 2 log 2 is not decided.
   * So Fable's Conjecture 3.4 (HC ≤ C log p) has 𝔐-probability 0, and the model-consistent form of the FRONTIER §7.2
     target is S_A with A > 2 log 2.
   * This is a model statement; it neither refutes Conjecture 3.4 for actual primes nor fixes the arithmetic exponent.
   * The deviation from linear growth is invisible at accessible heights. In the model's upper-bound surrogate, X*/log p
     moves only from 2.5 to 4.3 between log p = 18 and 1600. In the data, X*/log p = 3.42–3.45 for log p ∈ [18, 36]
     (EVIDENCE, §6).
2. **Two barriers for properties of model line data (Cor M3, M4, PROVED; scope stated there).**
   * *Model-null barrier.* No property that 𝔐 satisfies with positive probability formally implies S_θ for
     θ < 2 log 2. This covers every "typical-behaviour" (Erdős–Hall-regime) statement about line data.
   * *Planted barrier.* No block-robust 𝔐-almost-sure property implies S_A. This is B6 made exact for S_A,
     and covers asymptotic-error averaged statements (error scale → ∞) read as properties of line data.
3. **Fixed windows: Theorem U (PROVED modulo Henriot).** #{p ≤ y : HC(p) > X} ≪_X y (log y)^{−1−ℓ(X)/2}, where ℓ(X) is
   the number of lines with coordinate ≤ X. This extends Fable's Thm 3.2 (X = 4).
   * A version uniform in X with constants C^{ℓ(X)} would imply an 𝔐-null statement (Remark U).
   * In 𝔐 the confinement rate (log p)^{−1/2} is the right per-line rate only for small x; beyond, failure is driven by
     too few prime factors, and beyond (log p)^{log 2} it is generic.
4. **Hypothesis catalogue (§5).**
   * Erdős–Hall-type statements: blocked by M3.
   * Uniform high-dimensional Landau sieve: controls confinement only.
   * Averaged Kubilius/Elliott/Chowla/Hardy–Littlewood statements: blocked by M4, as properties of line data.
   * ES-specific lower tails: sufficient, but their content is about the ES lines alone. The count version LT(A, c),
     with event HC(p) > (log p)^A, is S_A restated (Prop 5.1).
   * A *general* lottery lower-tail principle: the first draft was **refuted in review** by a local-obstruction family.
     Any correct form needs three features: local admissibility with local-factor-conditioned masses, dependence
     control, and a quadratic-alignment clause of either parity (§5.3).
   * Prop 5.5 (CONDITIONAL on Hardy–Littlewood F) shows the alignment clause is necessary: T1 transports to the primes
     m² + 1.
   * Lemma N (PROVED): a fixed quadratic aligns only O_f(√X) ES lines, and quadratics of height ≤ (log x)^{1/10} align
     o(mass). Uniform unalignment is open.
   * Nearest standard-type relative (Assessment): Cramér's prime-gap conjecture.
5. **Numerics (EVIDENCE; CERTIFIED controls).** Primes p ≡ 1 (8): 20 000 each at 10⁸, 10¹⁰, 10¹², 10¹⁴, 10 000 at
   4·10¹⁵, all lines x ≤ 2048.
   * Per-line success follows 𝔐's shape: P_x ≈ c·log p/x in the mean regime (c ≈ 1.3 endpoint, 0.7 level), with an onset
     that moves out with p.
   * Counts of successful lines are overdispersed at large X. The deep lower tail is untested.
   * Integers and near-squares are harder (X*/log p ≈ 4.1 and 5.5). Every forced near-square failure observed is an
     aligned line.
   * Odd squares: all 1536 lines fail at all 5 000 squares tested (CERTIFIED T1 control).

**Promise (Assessment):** 1/5 as a conditional route (no natural general hypothesis survives in a counterexample-free
form); 3/5 as calibration. It changes the model-consistent §7.2 target and blocks two broad classes of hypothesis shapes.

## 1. The statement attacked

**Notation (PROVED equivalences; `LOWERTAIL_ROUND2_FABLE.md` Thm 1, Cor 1.1).** Let p ≡ 1 (mod 8) be prime. For p ≡ 5 (8),
HC(p) = 3 always. Put 𝒞 := {x ≥ 4 : x ≡ 0 (mod 4) or x ≡ 7 (mod 8)}. For x ∈ 𝒞 define the two **lines**:
* E_x(p): **p + x has a divisor A ≡ −1 (mod x)** (endpoint line). The word is (t, x, v) with A = tx − 1, v = (p + x)/A.
* L_x(p): **xp + 1 has a divisor d ≡ −1 (mod x)** (level line). The word is (x, u, v) with d = xu − 1.

E_x is Fable's "∃ v : xv | p + x + v". Given A, put v = (p+x)/A and t = (A+1)/x; then p + x + v = v(A+1) = xvt.
Conversely take A = tx − 1 with t = (p + x + v)/(xv). Then
  **HC(p) = min{x ∈ 𝒞 : E_x(p) or L_x(p)}**, and HC(p) < ∞ ⟺ ES₅(p) ⟹ ES(p).
The program `z53_hchyp_lines.c` reproduces Fable's HC values at 193, 409, 577, 2521, 3361, 5569, 9601, 21841, 66529, 83449
and 8813281: 7, 4, 4, 15, 7, 7, 7, 64, 8, 39, 8 (CERTIFIED). At odd squares every line fails (T1, Fable §1.3).

**Target S_A (FRONTIER §7.2).** ∃ p₀ ∀ prime p > p₀, p ≡ 1 (8): HC(p) ≤ (log p)^A.

**Lane question.** Find a hypothesis 𝐇, as weak and as natural as possible and *not ES in disguise*, with 𝐇 ⟹ S_A (or
𝐇 ⟹ R(p) ≥ 1 for large p). For each candidate give (i) the implication, (ii) T1, (iii) numerator 8 (8/131), (iv) numerics,
and (v) honest strength. Also: does GRH / GLH / EH / Chowla–Elliott / Hooley R* imply such an 𝐇, and if not, at which
step does it fail?

## 2. Why this is not already closed

The existing conditional statements are all *ES-specific*:
* H⁻_BM (BM_CORRECTED §3.1; "ES-(★) in disguise");
* Astra's H⁻mom (negative-part moments of order L/log L; LOWERTAIL_DEEP_ASTRA §7);
* MF₁ (EXSET_CHAR_FORCING Cor 5.4);
* Fable's hierarchy (§4/§6 there; every member is ES₅ plus a size tag);
* Conjecture 3.4 (HC ≪ log p).

None of the closed items calibrates *which lines and which scale* a hypothesis must control. None separates the hypothesis
shapes that could possibly work from those that provably cannot (as properties of model line data), and none asks for a *general* principle with ES as an
instance. Those three questions are the content here. (`git grep`: the Sathe–Selberg "random box" computation exists
for forced windows with 3^ω in EXSET_CHAR_FORCING §3.2. It is not applied to HC, its extreme-value scale, or hypotheses.)

## 3. The calibration: a Kubilius model for the six lines

### 3.1 The model 𝔐 (definition)

For each prime p ≡ 1 (8) put λ_p := log log p. For each line ι = (x, E) or (x, L) with x ∈ 𝒞, take
* k_ι ~ Poisson(λ_p), and
* given k_ι, i.i.d. g_{ι,1}, …, g_{ι,k_ι} uniform in G_x := (ℤ/x)^×.

Line ι succeeds iff −1 ∈ Σ_ι := {∏_{i∈I} g_{ι,i} : I ⊆ [k_ι]} (the empty product is 1). All variables are independent across
lines and primes. HC_𝔐(p) := min{x ∈ 𝒞 : a line at x succeeds}.

**What 𝔐 keeps.** It keeps the ω-distribution: E[2^{ω(N)}] ≍ log N, and P(ω(N) ≈ α log log N) = (log N)^{−Q(α)+o(1)}
with Q(α) = α log α − α + 1 (Sathe–Selberg; Ford, *Anatomy of integers*, 2025 notes, Thm 1.23 and Cor 1.15). It also
keeps the Erdős–Hall threshold: for a single modulus k = (log x)^{log 2}e^{(c+o(1))√(log log x)}, the proportion of n < x
with a divisor in every class prime to k tends to a Gaussian tail in c (R. R. Hall, *Acta Arith.* 29 (1976) 191–196, main
theorem; Erdős 1965 for k < 2^{(1−ε)log log x}).

**What 𝔐 drops.** It drops:
* prime powers and the prime 2;
* the non-uniform residues of small primes;
* the BM parity, which is free at primes (FRONTIER §2.4) but forced at squares — so 𝔐 is a model for primes, not
  squares;
* correlations between lines through p mod small ℓ.

§6 shows that the per-line success curve of actual primes has the qualitative shape of a cyclic surrogate of 𝔐, with the
same onset (EVIDENCE).

### 3.2 One line

**Lemma M1 (PROVED).** Let G be a finite abelian group of order n, h ∈ G∖{1}, k ≥ 0, and g₁, …, g_k i.i.d. uniform in G.
Then ½·min(1, (2^k − 1)/n) ≤ P(h ∈ Σ) ≤ min(1, (2^k − 1)/n).

*Proof.* Let Z := #{∅ ≠ I ⊆ [k] : g_I = h}, where g_I := ∏_{i∈I} g_i. Since h ≠ 1, h ∈ Σ ⟺ Z > 0.
* For I ≠ ∅, g_I is uniform, so EZ = (2^k − 1)/n. The upper bound is P(Z > 0) ≤ min(1, EZ).
* For distinct non-empty I, J, the events {g_I = h} and {g_J = h} are independent. Indeed, if J ⊄ I, pick j ∈ J∖I.
  Conditionally on (g_i)_{i≠j}, the element g_J is uniform, so P(g_I = h, g_J = h) = P(g_I = h)/n = 1/n². If J ⊂ I,
  swap the roles.
* Hence EZ² = EZ + (2^k − 1)(2^k − 2)/n² ≤ EZ + (EZ)².
* For k ≥ 1, Paley–Zygmund then gives P(Z > 0) ≥ (EZ)²/EZ² ≥ EZ/(1 + EZ) ≥ ½ min(1, EZ). For k = 0 both sides are 0. ∎

Write U(λ, n) := E min(1, (2^k − 1)/n) for k ~ Poisson(λ).

**Lemma M2 (PROVED; Chernoff bounds for the Poisson law).**
(i) If n = e^{aλ log 2} with 1 ≤ a ≤ 2, then U(λ, n) ≤ 2e^{−λQ(a)}.
(ii) If n ≥ e^{(2 log 2 + δ)λ} with δ > 0, then U(λ, n) ≥ (e^λ/2 − 1)/n for λ ≥ λ₀(δ).

*Proof.* (i) Split U at k = aλ:
  U ≤ E[2^k 1(k ≤ aλ)]/n + P(k > aλ) = e^λ P(Poi(2λ) ≤ aλ)/n + P(Poi(λ) > aλ).
The Chernoff bounds P(Poi(μ) ≥ bμ) ≤ e^{−μQ(b)} (b ≥ 1) and P(Poi(μ) ≤ bμ) ≤ e^{−μQ(b)} (b ≤ 1) give
  U ≤ e^{λ − 2λQ(a/2) − aλ log 2} + e^{−λQ(a)},
and 1 − 2Q(a/2) − a log 2 = −Q(a).
(ii) U ≥ E[(2^k − 1)1(2^k ≤ n)]/n ≥ (e^λ P(Poi(2λ) ≤ log₂ n) − 1)/n. Here log₂ n ≥ (2 + δ/log 2)λ, so
P(Poi(2λ) > log₂ n) ≤ e^{−2λQ(1 + δ/(2 log 2))} ≤ ½ for large λ. ∎

Reading: for x = (log p)^θ (so φ(x) = (log p)^{θ+o(1)}), P(line succeeds) ≤ (log p)^{−Q(θ/log 2)+o(1)} for
log 2 ≤ θ ≤ 2 log 2. The matching lower bound follows from the single term k = ⌈aλ⌉ (Stirling and M1); it is not needed
below. For θ ≥ 2 log 2 + δ the probability is ≍ log p/φ(x), carried by the N with ω(N) ≈ 2 log log N, which carry the
mean of τ.

### 3.3 The extreme-value scale of HC

**Theorem M (PROVED for 𝔐).**
(a) For every θ < 2 log 2: 𝔐-almost surely HC(p) > (log p)^θ for infinitely many p.
(b) For every A > 2 log 2: 𝔐-almost surely HC(p) ≤ (log p)^A for all but finitely many p.
More precisely:
* for log 2 < θ < 2 log 2, −log P(HC(p) > (log p)^θ) ≤ (log p)^{max(log 2 + η, θ − Q(θ/log 2)) + o(1)} for every η > 0;
* for A > 2 log 2 + 2δ, P(HC(p) > (log p)^A) ≤ exp(−(3/40)(A − 2 log 2 − 2δ) log p log log p + O(log p)).
The boundary case A = 2 log 2 is not decided, even in 𝔐.

*Proof.* Put λ = λ_p, X = (log p)^θ, and P_ι := P(line ι succeeds). For x ≥ 3 we have −1 ≠ 1 in G_x.

(a) Since the event in (a) is monotone in θ, it suffices to treat log 2 < θ < 2 log 2.
*Small lines.* For every line, 1 − P_ι ≥ P(k_ι = 0) = e^{−λ}. Fix 0 < η < 1 − log 2 and Y := (log p)^{log 2 + η}.
The ≤ 2Y lines with x ≤ Y contribute at most 2Yλ to −log ∏_ι(1 − P_ι).

*Middle lines, Y < x ≤ X.* By Rosser–Schoenfeld, φ(x) ≥ x/(e^γ log log x + 3/log log x). So
a_x := log φ(x)/(λ log 2) satisfies 1 + η/(2 log 2) ≤ a_x ≤ θ/log 2 < 2 for large p. Lemmas M1 and M2(i) give
P_ι ≤ 2e^{−λQ(a_x)} → 0. In particular P_ι ≤ ½, hence −log(1 − P_ι) ≤ 2P_ι.

Q is increasing and (log 2)-Lipschitz on [1, 2]. Replacing a_x by log x/(λ log 2) therefore costs a factor
≤ 2 log log x, and
  Σ_{Y<x≤X} P_ι ≤ 8 log log X · Σ_{j ≤ log₂X + 1} 2^{j+1} e^{−λQ(j/λ)} ≤ O(λ²)·(log p)^{θ − Q(θ/log 2)}.
This uses dyadic blocks x ∈ [2^j, 2^{j+1}) with j = βλ/log 2, each contributing 2e^{λ(β − Q(β/log 2))}. Also
β ↦ β − Q(β/log 2) has derivative 1 − log(β/log 2)/log 2 > 0 for β < 2 log 2.

*Conclusion of (a).* The two bounds give the stated estimate. Since θ − Q(θ/log 2) < 1 for θ < 2 log 2 (it equals 1 at
θ = 2 log 2) and log 2 + η < 1, we get P(HC(p) > X) ≥ exp(−(log p)^{1−ε}) ≥ 1/p for large p. The events for different p
are independent, and Σ_p 1/p = ∞ over primes p ≡ 1 (8). The second Borel–Cantelli lemma gives (a).

(b) Fix δ > 0 with 2 log 2 + 2δ < A, and put Y := (log p)^{2 log 2 + 2δ}, X := (log p)^A. For x ∈ 𝒞 ∩ (Y, X] and large p,
φ(x) ≥ (log p)^{2 log 2 + δ}. Lemmas M1 and M2(ii) give, for the endpoint line alone,
  P_{(x,E)} ≥ ½(e^λ/2 − 1)/φ(x) ≥ (¼ − 1/(2 log p))·log p/x ≥ log p/(5x)   (e^λ = log p ≥ 20, φ(x) ≤ x).
Also Σ_{x∈𝒞, Y<x≤X} 1/x = (1/4 + 1/8) log(X/Y) + O(1) = (3/8)(A − 2 log 2 − 2δ)λ + O(1). Hence
P(HC(p) > X) ≤ ∏(1 − P_{(x,E)}) ≤ exp(−(3/40)(A − 2 log 2 − 2δ) log p log log p + O(log p)), which is summable over p.
The first Borel–Cantelli lemma gives (b). ∎

**Remark M (the scale is invisible in practice; EVIDENCE).** Let X*(p) be the least X with Σ_{x∈𝒞, x≤X} (P_E + P_L) ≥ log p.
This is the Poisson scale: P(all lines ≤ X fail) ≈ e^{−Σ P} reaches 1/p there. For 𝔐 we compute it with the
*upper-bound surrogate* P_ι := U (M1's upper value; `z53_hchyp_xstar_model.py`): X*/log p = 2.55, 2.46, 2.48, 2.68, 2.96,
3.33, 3.79, 4.33 at log p = 18.4, 27.6, 50, 100, 200, 400, 800, 1600. With the half-surrogate P_ι := U/2 the values are
7.4 → 17.8. The finite-difference slopes Δ log X*/Δ log log p are 0.91 → 1.20 (U) and 1.10 → 1.25 (U/2). The estimates behind
Theorem M place the mass-crossing scale between (log p)^{2 log 2 − ε} and (log p)^{2 log 2 + ε} for large p, for either
surrogate. So log X*/log log p → 2 log 2. Convergence of the finite-difference slopes themselves is not proved; the
table only shows that the approach is slow. The data (§6) give X*/log p = 3.42, 3.43, 3.44, 3.44, 3.45 at log p = 18.4, 23.0, 27.6,
32.2, 35.9. The census maximum of HC over all p ≤ 10⁸ is 64 (Fable §3.2), against X*(10⁸) = 63. So the data look like 𝔐's
pre-asymptotic regime, where HC_max looks linear in log p. Fable's linear Conjecture 3.4 describes the observable range
well, but by Theorem M(a) it is an 𝔐-null statement asymptotically. This is a statement about the model; it does not
refute Conjecture 3.4 for actual primes (Assessment).

**Corollary M3 (model-null barrier; PROVED).** Let 𝒲 be the space of *line data*: for each prime p ≡ 1 (8) and each line ι,
a finite sequence in G_x. Give 𝒲 the law of 𝔐. For θ < 2 log 2, the set S_θ := {w : HC_w(p) ≤ (log p)^θ for all large p}
has 𝔐(S_θ) = 0 by Theorem M(a). Hence **every measurable 𝐇 ⊆ 𝒲 with 𝔐(𝐇) > 0 satisfies 𝐇 ⊄ S_θ**: no property of line
data that the Kubilius model satisfies with positive probability formally implies S_θ. This applies in particular to
Conjecture 3.4.
*Scope.* "Formally implies" means inclusion of subsets of 𝒲. An argument that uses arithmetic of actual primes not
encoded in the line data is not covered. Such an argument would have to show that actual primes are *less random than
𝔐 in the direction of success*.

**Corollary M4 (planted barrier; PROVED).** Fix A. Let 𝔐^♯ be 𝔐 modified at one prime per dyadic block (say the least
prime ≡ 1 (8) in (2^j, 2^{j+1}]) by setting k_ι = 0 for every line with x ≤ (log p)^A. Then S_A fails surely under 𝔐^♯.
Call 𝐇 *block-robust* if changing w at ≤ 1 prime per dyadic block keeps w in 𝐇. A block-robust 𝐇 with 𝔐(𝐇) = 1 has
𝔐^♯(𝐇) = 1 (the coupling changes one prime per block). Therefore no block-robust 𝔐-almost-sure 𝐇 implies S_A.
*Which averaged statements are block-robust (corrected after cross-model review).* "Holds 𝔐-a.s. with slack ≥ 1" is
**not** enough. A sliding interval (y, 2y] can meet two dyadic blocks, so planting can change its count by 2. Moreover,
almost-sure slack concerns typical members of 𝐇, not invariance of all members.

What does work is the class of *asymptotic error statements*. Take statements "#{p ∈ I : E_p} = M(I) + O(E(I))" over
intervals I = (y, 2y] or [1, y], with E_p depending only on the line data at p and the O-constant arbitrary. Planting
changes such a count by ≤ 2 (sliding interval) or ≤ log₂ y + 1 (initial segment). So the statement is invariant under
planting whenever E(I) → ∞ (for (y, 2y]), resp. E(I)/log y → ∞ (for [1, y]): the changed error is still O(E). Statements
of this class are block-robust in the sense of M4.

Whether a given standard conjecture, *as an arithmetic statement*, can be encoded as such a property of line data is a
separate question that is not addressed here.
*Reading (Assessment).* This is B6 made exact for S_A: a useful hypothesis of this kind must bound the joint failure of all
lines up to ≳ (log p)^{2 log 2} with frequency < 1 per block.

## 4. The fixed-window (Kneser) regime

**Lemma K (PROVED; the argument of LONGSHOT_PIGEONHOLE Prop 1.4).** Let x ≥ 3, G = (ℤ/x)^×, and N = ∏ℓ_i^{a_i} coprime to
x. If no divisor of N is ≡ −1 (mod x), then there is a subgroup H ≤ G with −1 ∉ H and
#{i : ℓ_i mod x ∉ H} ≤ [G:H] − 2.

*Proof.* Let A_i := {ℓ_i^t : 0 ≤ t ≤ a_i} ⊂ G. Then Σ := A₁⋯A_r is the set of divisor residues; let H := Stab(Σ).
* 1 ∈ Σ gives H ⊂ Σ. Since −1 ∉ Σ, we get −H ∩ Σ = ∅, hence −1 ∉ H and |Σ/H| ≤ [G:H] − 1.
* In G/H every partial product of the images X_i has trivial stabiliser, because a stabiliser of a partial product
  stabilises Σ/H. Kneser's theorem with trivial stabiliser gives |Σ/H| ≥ 1 + Σ_i(|X_i| − 1) ≥ 1 + #{i : ℓ_i ∉ H}. ∎

**Theorem U (PROVED modulo Henriot's uniform Nair–Tenenbaum bound, New Thm 5 of the 2014 erratum, in the form used in
EXSET_CHAR_FORCING Thm 3.1 / Prop 4.1).** For each fixed X ≥ 4 let ℓ(X) := 2·#(𝒞 ∩ [4, X]), the number of lines with
coordinate ≤ X. Then
  #{p ≤ y prime : p ≡ 1 (8), HC(p) > X} ≪_X y (log y)^{−1−ℓ(X)/2}.
For X = 4 this is Fable's Theorem 3.2 (two lines, y/(log y)²).

*Proof.* *Reduction to confinement.* Let p > X with HC(p) > X. Every line ι at x ∈ 𝒞 ∩ [4, X] fails, and N_ι(p) ∈ {p + x,
xp + 1} is coprime to x. Its odd part also has no divisor ≡ −1 (mod x), being a sub-collection of divisors. Lemma K
gives H_ι ≤ G_x with −1 ∉ H_ι and ω_{H_ι}(N_ι(p)) ≤ r_ι − 2, where r_ι := [G_x : H_ι] ≥ 2 and ω_H counts the odd primes
whose residue mod x lies outside H. There are finitely many tuples (H_ι); fix one.

*Rankin weights.* For s_ι ∈ [0, 1] (with 0⁰ := 1), 1[ω ≤ r − 2] ≤ s^{ω − (r−2)}. The function f_ι := s_ι^{ω_{H_ι}} is
multiplicative, takes values in [0, 1], and satisfies f(ℓ^a) = f(ℓ) and f(2^a) = 1.

*The linear forms.* Write p = 8m + 1 and use:
* Q₀(m) = 8m + 1, with the weight 1[P⁻(Q₀(m)) > √M];
* for x ≡ 0 (4): E: 8m + 1 + x and L: 8xm + x + 1;
* for x ≡ 7 (8): E: m + (x+1)/8 and L: xm + (x+1)/8 (= N_ι/8).

These forms are primitive and pairwise non-proportional. For example E_x vs L_{x'} would need x'(1 + x) = x' + 1, and
L_x vs L_{x'} would need x(x'+1) = x'(x+1).

*The sieve bound.* As in EXSET_CHAR_FORCING Prop 4.1, Henriot's theorem with the k + 1 forms gives
  Σ_{m≤M} 1[P⁻(Q₀) > √M] ∏_ι f_ι(Q_ι(m)) ≪_X (M/log M) exp(−Σ_ι Σ_{ℓ≤M, ℓ∤2x}(1 − f_ι(ℓ))/ℓ).
The bad primes (divisors of 2∏x and of the resultants) cost O_X(1). By Mertens in progressions,
Σ_{ℓ≤M, ℓ mod x∉H} 1/ℓ = (1 − 1/r) log log M + O_x(1).

*Choice of weights.*
* For r_ι = 2, take s_ι = 0 (f = 1[ω_H = 0]; New Thm 5 needs no lower bound on F). This gives the factor (log y)^{−1/2}.
* For r_ι ≥ 3, take s_ι = 1/log log y. This gives ≪ (log log y)^{r_ι−2}(log y)^{−(1−1/r_ι)} ≤ (log y)^{−2/3+o(1)}.

Multiplying over the ℓ(X) lines and summing over the finitely many tuples gives the claim. Primes p ≤ √y contribute
O(√y). ∎

*Sharpness (Assessment).* Every line has an index-2 subgroup without −1: χ₋₄ for 4 | x, and an odd Legendre character
for x ≡ 7 (8), since such x has a prime factor ≡ 3 (mod 4). So (log y)^{−1/2} per line is the expected confinement rate.
EVIDENCE: P(HC > 4) = 0.083 → 0.042 from 10⁸ to 4·10¹⁵ (§6). Over that range log p only doubles, so the decay rate
cannot be read off. A matching lower bound would need a half-dimensional lower-bound sieve for primes in several forms,
which is not attempted here.

**Remark U (a uniform Landau saving would be model-null).** Suppose the implied constant in Theorem U were ≤ C^{ℓ(X)} uniformly
for X ≤ log y. With X = 8 log y/log log y this would give a count < 1, i.e. HC(p) ≤ 8 log p/log log p for all large p.
That is S_θ for every θ > 1, which 𝔐 violates almost surely (Theorem M(a)). So such uniformity would be a statement
the Kubilius model violates. This is *not* an arithmetic impossibility: M3 cannot rule out a uniform estimate for actual
primes. The proof shows where the estimate breaks: Lemma K allows r − 2 exceptional primes, and for H = {1} that is
φ(x) − 2. Once φ(x) ≫ log log p this exceeds the typical ω(N), and the Rankin factor s^{−(r−2)} makes the Kneser–Rankin
estimate ineffective.

*Heuristic picture in 𝔐 (Assessment, not proved).* The line still succeeds with probability → 1 up to
x ≈ (log p)^{log 2 − ε} (Erdős–Hall regime). Write a = log φ(x)/(λ log 2) < 1. The ω-deficit alone (k < aλ) gives a
failure probability of order (log p)^{−Q(a)+o(1)}; this is a lower bound for failure. On (0, 1), Q is decreasing with
Q(0) = 1, so (log p)^{−Q(a)} exceeds the confinement rate (log p)^{−1/2} as soon as Q(a) < ½, i.e. for a **above**
a* ≈ 0.187, i.e. φ(x) ≳ (log p)^{0.13}. So the per-line saving (log p)^{−1/2} of Theorem U should be the right rate
only for small x (fixed x, or x up to a small power of log p in 𝔐). The precise transition at (log p)^{0.13}, and the
claim that the ω-deficit *dominates* beyond it, would need a matching upper bound for failure, which is not supplied.
Above (log p)^{log 2}, failure is the generic outcome (the lottery; PROVED in 𝔐 via Lemma M2(i)). This is the precise form of the dimension barrier for HC. It also disposes of the
"high-dimensional Landau" hypothesis of §5.2.

## 5. Hypotheses: what each shape can and cannot do

### 5.1 The regimes of a line, and what it takes

For a line at x and a prime p (λ = log log p) there are three regimes. They are described in 𝔐 (Assessment for actual
primes):
* **Small x (Kneser/Landau regime): fixed x, and heuristically x up to about (log p)^{0.13}.** Failure comes through
  confinement (Lemma K). Theorem U gives the upper rate (log y)^{−1/2} per line for fixed X.
* **Typical regime, up to (log p)^{log 2−ε}.** Success is typical (Erdős–Hall). Heuristically, failure comes mainly from
  an ω-deficit (Remark U; the domination is not proved).
* **Lottery regime, beyond (log p)^{log 2+ε}.** Failure is typical. Success has probability ≤ (log p)^{−Q(θ/log 2)+o(1)}
  up to θ = 2 log 2, and ≍ log p/x beyond.

**What S_A needs.** About log p expected successes, i.e. lines up to (log p)^{2 log 2+o(1)} in 𝔐 (Theorem M). These lines
are deep in the lottery regime, where success comes from the *rare* integers N with ω(N) ≈ 2 log log p.

**Proposition 5.1 (PROVED, elementary logic).** Let E_p be events and B(y) ≥ 0 with B(y) → 0. Then the count statement
"∀ large y: #{p ∈ (y, 2y] : E_p} ≤ B(y)" is equivalent to "E_p fails for all large p".
*Proof.* A count is a non-negative integer, so it is < 1 iff it is 0. ∎
So the *particular* hypothesis "the joint-failure count of the ES lines tends to 0" is just S_A restated. Stronger
quantitative hypotheses — moments, relative lower tails such as H⁻_BM, H⁻mom, MF₁ — are not equivalent to S_A. They are
sufficient strengthenings whose extra content concerns the ES lines alone. This is the sense in which they are "ES in
disguise" (Assessment).

### 5.2 Catalogue

Columns: (i) implication; (ii) T1; (iii) 8/131; (iv) numerics; (v) strength.

**H_EH — Erdős–Hall-type equidistribution.** "The divisors of N are equidistributed mod q for most q", or "for most N",
or "for most lines x ≤ (log p)^θ at every p".
* (i) As a statement about line data that 𝔐 satisfies, it cannot formally imply S_θ for θ < 2 log 2 (Cor M3). It is
  also tied-modulus: the ES shape is not one N with many q, since each line has its own N (B2).
* (ii) At squares every line fails, but H_EH speaks only of typical N, and squares have density 0. So squares do not
  refute it, and it cannot see T1.
* (iii) n/a. (iv) The per-line rates have 𝔐's shape (§6).
* (v) Blocked by M3 (scope as stated there).

**H_Lan — uniform high-dimensional Landau sieve ("MLD").** "Joint confinement of k lines has frequency ≤ C^k ∏(log)^{−1/2},
uniformly for k up to log x/log log x."
* (i) It bounds confinement only. Beyond small x, failure is mostly not confinement (Remark U), so it does not imply S_A.
  Read as a bound on *failure*, it would imply HC ≪ log p/log log p, which is 𝔐-null.
* (ii) Over integers it is false at squares (all levels are BM-confined, and √x squares exceed the bound).
* (iii) — (iv) — (v) Does not reach S_A.

**H_Kub — joint Kubilius / Elliott / Chowla / Hardy–Littlewood with error terms.**
* (i) Their averaged *asymptotic-error* forms, read as properties of line data, are block-robust in the corrected sense
  of M4. So in that reading they cannot formally imply S_A. The actual arithmetic conjectures have not been encoded as
  such properties; this is an Assessment, not a non-implication theorem.
* (ii) Fine. (iii) Fine. (iv) —
* (v) Blocked by M4 in the line-data reading only.

**LT(A, c) — ES-specific joint lower tail.** Fix c > 0 and A > 2 log 2, so that the bound below tends to 0 by the
Theorem M(b) mass computation. The statement is: for all large x,
  #{p ∈ (x, 2x] prime, p ≡ 1 (8) : HC(p) > (log p)^A} ≤ x·exp(−c·𝓜_A(x)),
where 𝓜_A(x) is the 𝔐-mass of the lines x′ ∈ 𝒞, x′ ≤ (log x)^A.
* (i) Implies S_A, and in this form it is S_A restated (Prop 5.1; the event uses (log p)^A, as S_A does).
  The variant with "all lines ≤ (log x)^A fail" inside the count is strictly stronger: evaluating at x = p/2 gives
  HC(p) ≤ (log(p/2))^A eventually. For abstract HC values (e.g. the largest element of 𝒞 below (log p)^A) this stronger
  statement fails while S_A holds. The variant still suffices for S_A, but it is not equivalent to it.
* (ii) Fine (stated for primes). (iii) Has a threshold.
* (iv) No deep-tail event observed (§6). That cannot test it.
* (v) ES in disguise.

**GLT — a general lottery lower-tail principle (§5.3).**
* (i) A correct general formulation would imply S_A through its instance LT. **No formulation known to be free of
  counterexamples is available.** The first draft was refuted in review (§5.3).
* (ii) Necessarily false over integers (squares). It needs a quadratic-alignment clause (Prop 5.5).
* (iii) Has a threshold.
* (iv) —
* (v) Its role is motivation for LT, not a hypothesis one can adopt.

### 5.3 Toward a general principle, and why it is delicate

The kickoff asks for a hypothesis that is *not* ES in disguise. The natural candidate is a general far-lower-tail
principle for *divisor lotteries*: families of events "F(n) has a divisor in a prescribed class mod q", evaluated at
primes. LT would be its instance for the ES family.

**Lotteries and model mass.** A *lottery line* is λ = (F, q, c) with F(n) = an + b ∈ ℤ[n], a ≥ 1, q ≥ 3, and
c ∈ (ℤ/q)^× ∖ {1}. Its event at n is W_λ(n): "F(n) is coprime to q and has a divisor ≡ c (mod q)". Its *model mass* at
height x is P^𝔐_λ(x) := U(log log x, φ(q)) (Lemma M1's upper value), and a family has mass 𝓜(𝓕; x) := Σ_λ P^𝔐_λ(x). The
ES lines are E_x = (n + x, x, −1) and L_x = (xn + 1, x, −1).

**First draft (refuted).** The first draft of this memo stated GLT(c, η): for every η-unaligned family (definition
below), #{p ∈ (x, 2x] : no line holds} ≤ x·e^{−cη𝓜}.

*Counterexample (from the review).* Take λ_j = (5jn, 5, 4), j ≤ (log x)²/5. Every event fails at every prime, because
5 | F_j(p). No line is aligned with any quadratic, since no odd quadratic character has conductor dividing 5. Yet
𝓜 ≍ (log x)², so GLT would predict < 1 failure against ≍ x/log x actual failures.

The defect is that the model mass ignores *local admissibility*. Nested or proportional lines cause a similar problem:
the forms 5jn are pairwise proportional. A constant c < 1 cannot absorb a local obstruction of probability 1.

**Necessary features of any correct formulation (Assessment; partly PROVED).**
1. *Local admissibility.* For every prime n coprime to q, F(n) must be coprime to q. The model mass must then be computed
   conditionally on the residues of n modulo small primes, i.e. a local-factor mixture. The ES lines satisfy the
   coprimality: for r | x, p + x ≡ p and xp + 1 ≡ 1 (mod r).
2. *Dependence control.* The forms must be primitive and pairwise non-proportional, so that their large prime factors
   are private (SYNTHESIS_SPARKS8 Lemma 2.3). Nested targets (q | q′, c′ ≡ c mod q on the same F) must be merged.
   The ES forms are primitive and pairwise non-proportional (Theorem U's proof).
3. *Quadratic alignment, of either parity.* Let f ∈ ℤ[m] be an irreducible quadratic and G := F∘f, with non-square
   discriminant Δ. Let χ_Δ be the primitive character of ℚ(√Δ). The line λ is *aligned with f* if cond(χ_Δ) | q and
   χ_Δ(c) = −1. If so, for every m with G(m) coprime to 2·lead(G)·Δ, every prime factor of G(m) has χ_Δ = 1, because
   Δ is a square mod ℓ. So W_λ(f(m)) fails.
   * For c = −1 (the ES case) only odd χ_Δ (Δ < 0) can align.
   * For general c, even characters can align as well. The review's example: F(n) = n, q = 5, c = 2, f = m² − 5.
   * Exceptional primes (those dividing 2·lead·Δ; for ES lines with x ≡ 7 (8), the prime 2) can let a line escape.
     Alignment forces failure only on the m for which these primes do not help.
4. *What alignment captures (PROVED, elementary + Dirichlet).* Suppose a character ψ mod q contains, in its kernel,
   almost all prime divisors of the values of G. Then ψ ∈ {1, χ_Δ}. Indeed, for ℓ ∤ 2·lead(G)·Δ, ℓ divides some G(m)
   iff χ_Δ(ℓ) = 1. Every class of the subgroup K = {χ_Δ = 1} contains infinitely many primes, so ψ is trivial on K.
   This classifies *character confinement of all values along f*. It does not classify every possible cause of joint
   divisor-class failure.

**Proposition 5.5 (CONDITIONAL on Hardy–Littlewood Conjecture F for m² + 1, in the weak form
#{m : m² + 1 ∈ (x, 2x] prime} ≫ √x/log x).** A principle with features 1–2 but without feature 3 is false.

*Proof.* Take 𝓕 := {λ_a = (a(n − 1) + 1, a, −1) : a ∈ 𝒞 ∩ [4, (log x)^A]}, A > 2 log 2. The forms are primitive and pairwise
non-proportional.
* Local admissibility: for r | a, F_a(n) ≡ 1 (mod r).
* At a prime p = m² + 1 (so m is even), F_a(p) = am² + 1 is odd and coprime to a.
* Let χ be the primitive character of ℚ(√−a). For a ∈ 𝒞 it is odd with conductor dividing a: for a = 4b it is that of
  ℚ(√−b), of conductor dividing 4b; for a ≡ 7 (8) the discriminant is −sqfree(a), which divides a.
* Every prime ℓ | am² + 1 has −a ≡ (m⁻¹)² mod ℓ, hence χ(ℓ) = 1. So every divisor d has χ(d) = 1 ≠ χ(−1), and no divisor
  is ≡ −1 (mod a). Every line fails at every such prime.
* The mass of 𝓕 is that of the level lines, ≫ log x log log x (Theorem M(b) computation).
* So any bound x·e^{−c𝓜} = o(1) contradicts the ≫ √x/log x failures. ∎

Each λ_a is aligned with f = m² + 1 (Δ = −4a), so feature 3 removes exactly this family. T1 transported to near-squares is
what the alignment clause is for.

**Lemma N (PROVED; how much of the ES family a quadratic can align).** Let f(m) = αm² + βm + γ with α ≥ 1 and
D = β² − 4αγ ≠ 0. Among x ∈ 𝒞 ∩ [4, X]:
* the endpoint lines E_x aligned with f number ≤ τ(|D|)(2√(αX) + √|D| + 1);
* the level lines L_x aligned with f number ≤ τ(4α)(2√α + √(X|D|) + 1) if D < 0, and ≤ 4α/D if D > 0.
For fixed f this is O_f(√X).

*Proof.*
*E_x.* Here G = f + x and Δ = D − 4αx. Alignment needs Δ < 0 and cond(χ_Δ) | x. The squarefree kernel c of |Δ| divides
the conductor, hence x, hence D (because c | 4αx − D). Write 4αx − D = cs² with c | D squarefree. For x ≤ X we need
s ≤ √((4αX + |D|)/c). Summing over c | D gives the bound.

*L_x.* Here G = xf + 1 and Δ = x(xD − 4α). Alignment needs xD < 4α and conductor | x. Then every prime with odd exponent
in x(4α − xD) divides x. Primes dividing both x and 4α − xD divide 4α, so 4α − xD = ds² with d | rad(4α).
* If D < 0, then x = (ds² − 4α)/|D| ≤ X forces s ≤ √((4α + X|D|)/d).
* If D > 0, then x < 4α/D. ∎

*Mass of the aligned lines.* Use mass ≤ 1 per line below Y := (log x)^{log 2}, and above Y the trivial bound
U ≤ log x/φ(x) ≤ 2 log x log log x/x.
* The aligned E-lines x = (cs² + D)/(4α) are quadratically spaced in s. Above Y, Σ 1/x ≪ τ(|D|)√(α/Y).
* The aligned L-lines with D < 0 are x = (ds² − 4α)/|D|. Above Y, Σ 1/x ≪ τ(4α)√(|D|/Y).
* For fixed f the aligned mass is O_f(√Y + log x·log log x·Y^{−1/2}) = O_f((log x)^{1−(log 2)/2+o(1)}).
* For height ≤ (log x)^{1/10} (so α ≤ (log x)^{0.1}, |D| ≤ 5(log x)^{0.2}) the lines below Y number
  ≤ (log x)^{(log 2)/2+0.1+o(1)}, and the lines above Y have mass ≤ (log x)^{1+0.1−(log 2)/2+o(1)} ≤ (log x)^{0.76}.

Both are o(𝓜(𝓕_X; x)) = o(log x log log x). So against every fixed quadratic, and every quadratic of height
≤ (log x)^{1/10}, the ES family is unaligned in mass. For larger heights the bounds above become vacuous (the congruence
conditions on s would be needed), and **uniform unalignment (UA) is not proved.**

**What survives (Assessment).**
* LT (§5.2) implies S_A trivially (Prop 5.1), but it is ES-specific.
* A general principle would need features 1–3 *and* a proof that these exhaust the conspiracies. No such formulation
  is available.
* A candidate shape is: *for locally admissible, dependence-controlled families that are unaligned in mass with every
  irreducible quadratic, the joint-failure frequency is ≤ x·exp(−c·𝓜_loc)* (𝓜_loc the local-factor-conditioned mass).
  It is offered as a research target. It is not offered as a plausible hypothesis, because the review's counterexample
  shows how easily such statements fail.
* *Analogy (Assessment).* The closest standard-type relative is Cramér's conjecture: every interval [y, y + C(log y)²]
  contains a prime. That conjecture is pointwise, has a polylog window, and has expected count ≍ log y. Granville's
  model predicts that the maximal gap constant is at least 2e^{−γ}, a correction coming from small primes — the analogue
  of local factors here.
* Like Cramér's conjecture, this target is currently unproved and beyond known methods. Unlike Cramér's, it must also
  exclude quadratic conspiracies, because ES lotteries carry T1.

### 5.4 Standard conjectures: why no implication is established (Assessment)

This table is an Assessment. It records why the *known implementations* of each conjecture do not supply the needed
lower tail. It is not a non-implication theorem: Cor M3/M4 concern formal implications between properties of model line
data, and no standard conjecture has been represented as such a property.

| conjecture | what it controls | where the known implementations stop |
|---|---|---|
| GRH (Dirichlet, Dedekind) | sums over n at fixed χ; least QNR ≤ 2 log²p | Pointwise only in the colour layer. The BM layer is pointwise free: some level 4 \| t ≤ 4ℓ(p) has M_t^lev(p) > 0 ((J)103), and GRH gives ℓ(p) ≤ 2 log²p. But a line that is not BM-forced still fails generically beyond x ≈ (log p)^{log 2} in 𝔐 (§5.1). The lottery needs the class of a divisor, which no character sum at one p fixes (CLASS_FORCING Thm 2.1). |
| GLH | subconvexity / moments of L at fixed conductor | Same as GRH: values of L-functions control averages of line events over p (the block-robust shape of M4). |
| EH / BFI (level x^{1−ε}) | divisor functions in APs averaged over q ≤ x^{1−ε} | Gives single-line statistics on average over p (Titchmarsh-type). The joint law of k lines needs k-fold divisor correlations, and already Σ τ(n)τ(n+h₁)τ(n+h₂) has no individual-shift asymptotic (Blomer, BLMS 49 (2017), "challenging open problem"; Browning's conjecture proved only on average over h). As averaged statements they have the block-robust shape of M4. |
| Chowla / Elliott (MRT 2015; Tao 2016) | k-point correlations of bounded multiplicative functions, k fixed | Fixed k with o(x) error: the block-robust shape of M4. No uniformity in k growing with x is known or stated (checked: MRT, Tao, Tao–Teräväinen all have k fixed). |
| Hooley R* / Kloosterman bounds | Σ_c S(m,n;c)/c at fixed (m,n) | No fixed-(m,n) Kloosterman sum arises at one p (SINGLE_P_COUNT Prop 6.1); tied modulus. |
| Hardy–Littlewood k-tuples / Bateman–Horn | prime values of fixed forms, k fixed | Fixed k: the block-robust shape of M4. In the uniform-in-k direction, Maier (Michigan Math. J. 32 (1985)) and Friedlander–Granville (Ann. Math. 129 (1989), Cor 2) show relative-error uniformity fails at polylog length. HL-F *refutes* a principle without the alignment clause (Prop 5.5). |
| Inverse large sieve (Green–Harper GAFA 2014 Conj 1.7; Walsh Duke 2012) | sets occupying ≤ (p+1)/2 classes are quadratic images or small | Philosophically the same clause as feature 3 of §5.3 ("quadratic = the only conspiracy"), but for a different regime: the failure set of the ES lines is not a set with few residues mod every p. No implication. |
| Cramér / Granville gap conjecture | primes in windows of length (log y)² | No implication either way. The analogy is of shape only (§5.3, Assessment). |

**Answer to the kickoff's last question (Assessment).** No implication from GRH, GLH, EH, Chowla–Elliott or Hooley R* to S_A
(or to R(p) ≥ 1) is established here, and none is known.
* Every implementation of these conjectures that this lane or the campaign found produces either typical-behaviour
  statements about line data or averaged statements of the block-robust shape.
* Cor M3/M4 show that statements of those two kinds, *as properties of line data*, cannot formally give S_θ
  (θ < 2 log 2) or S_A respectively.
* What is missing in every case is a far-lower-tail input for the joint failure of ≳ (log p)^{2 log 2} lines.

## 6. Numerics (EVIDENCE unless marked CERTIFIED)

Program `scripts/z53_hchyp_lines.c` (C, exact factoring by trial division + Pollard–Brent + deterministic Miller–Rabin;
divisor-residue BFS). For each n and each x ∈ 𝒞 ∩ [4, 2048] it tests E_x and L_x. Files `data/z53/hchyp/*_X2048.txt`
(per-x counts) and `.hc` (per n: HC, Z(64), Z(256), Z(1024), Z(2048), where Z(X) = number of successful lines ≤ X).

**Per-line rates, x·P_x/log p** (mean over x ∈ 𝒞 in the dyadic bin; endpoint / level):

| bin | 10⁸ (L = 18.4) | 10¹² (27.6) | 10¹⁴ (32.2) | 4·10¹⁵ (35.9) | integers 10¹² |
|---|---|---|---|---|---|
| [4,8) | 0.26 / 0.24 | 0.18 / 0.17 | 0.15 / 0.14 | 0.14 / 0.13 | 0.17 / 0.15 |
| [16,32) | 0.65 / 0.47 | 0.50 / 0.38 | 0.45 / 0.35 | 0.41 / 0.33 | 0.46 / 0.34 |
| [64,128) | 1.06 / 0.62 | 0.96 / 0.59 | 0.91 / 0.56 | 0.87 / 0.54 | 0.84 / 0.50 |
| [256,512) | 1.17 / 0.63 | 1.25 / 0.68 | 1.24 / 0.68 | 1.23 / 0.68 | 1.04 / 0.56 |
| [1024,2048) | 1.08 / 0.59 | 1.29 / 0.68 | 1.34 / 0.70 | 1.37 / 0.72 | 1.07 / 0.56 |

A *cyclic surrogate* of 𝔐 (`z53_hchyp_model.py`: Monte Carlo in the additive group ℤ/φ(x) with target φ(x) − 1, not in
(ℤ/x)^× with target −1) gives the same normalisation at the single points x = 4, 16, 64, 256, 1024 and log p = 27.6 as
0.12, 0.33, 0.69, 1.09, 1.42. These are point values, not bin averages. Shape and onset agree qualitatively; the
level-line constant is ≈ ½ the endpoint one. The plateau (P_x ∝ log p/x) is the mean regime,
and its onset moves out with p as Theorem M says.

**HC and the Poisson scale X*** (X* = least X with Σ_{x≤X}(P_E + P_L) ≥ log p, from the empirical P_x):

| sample | N | max HC (at) | P(HC>4) | P(HC>8) | P(HC>16) | X* | X*/log p |
|---|---|---|---|---|---|---|---|
| primes from 10⁸ | 20 000 | 23 (100 150 681) | 0.0832 | 1.6e−3 | 1.5e−4 | 63 | 3.42 |
| primes from 10¹⁰ | 20 000 | 20 | 0.0659 | 1.05e−3 | 1.0e−4 | 79 | 3.43 |
| primes from 10¹² | 20 000 | 20 | 0.0558 | 6.0e−4 | 5e−5 | 95 | 3.44 |
| primes from 10¹⁴ | 20 000 | 15 | 0.0513 | 7.0e−4 | 0 | 111 | 3.44 |
| primes from 4·10¹⁵ | 10 000 | 12 | 0.0421 | 2.0e−4 | 0 | 124 | 3.45 |
| non-square integers ≡ 1 (8) from 10⁸ | 20 000 | 36 | 0.1215 | 5.7e−3 | 4.5e−4 | 76 | 4.13 |
| integers from 10¹² | 20 000 | 23 | 0.0827 | 1.95e−3 | 1e−4 | 111 | 4.02 |
| primes m² + 24, m ≥ 10⁵ | 5 000 | 23 | 0.0616 | 2.0e−3 | 8e−4 | 132 | 5.43 |
| primes m² + 120, m ≥ 10⁵ | 5 000 | 31 | 0.0734 | 2.54e−2 | 1.6e−3 | 135 | 5.60 |
| odd squares m², m ≥ 10001 | 5 000 | ∞ (all lines fail) | 1 | 1 | 1 | — | — |

The odd-square row is **CERTIFIED** (T1 control): 0 successes in 5 000 × 768 × 2 line tests.

**Joint failure vs independence.** We compare F(X) with ∏_{x≤X}(1 − P_x). Here F(X) is the observed number of primes with
no success up to X, and P_x := P̂(E_x ∨ L_x) is the empirical probability that *either* line at x succeeds. So the two
lines at the same x are not treated as independent. The ratios are:
* X = 7: 2.66–3.25 (all five prime samples);
* X = 8: 2.12–4.98;
* X = 12: 1.7–9.3;
* X = 15–16: 9.7–50 where the count is non-zero (counts 1–4; zero at 10¹⁴ and 4·10¹⁵).
So there is excess cumulative joint failure relative to the independence benchmark at small X. This is consistent with a
shared local factor (p mod small primes; y8 "clean levels"). Any lower-tail principle must allow for it (Assessment).

**Lower tail of Z(X)** (successful lines up to X):

| sample | X | mean Z | var/mean | min Z (min/mean) | P(Z ≤ mean/3): data / Poisson |
|---|---|---|---|---|---|
| primes 10⁸ | 64 | 19.0 | 0.72 | 6 (0.32) | 5.0e−4 / 5.3e−4 |
| primes 10⁸ | 2048 | 60.2 | 2.18 | 22 (0.37) | 0 / 1.8e−9 |
| primes 10¹² | 64 | 22.4 | 0.57 | 7 (0.31) | 5e−5 / 1.5e−4 |
| primes 10¹² | 2048 | 87.6 | 1.56 | 49 (0.56) | 0 / 3e−13 |
| primes 4·10¹⁵ | 2048 | 108.6 | 1.30 | 68 (0.63) | 0 / 5e−16 |
| integers 10⁸ | 2048 | 51.3 | 3.22 | 14 (0.27) | 2.5e−4 / 2.6e−8 |
| near-squares m²+24 | 2048 | 61.3 | 1.24 | 31 (0.51) | 0 / 8e−10 |

At X = 64 the observed near tail of primes is close to the Poisson value. At X = 2048 the variance/mean ratios
(2.18, 1.56, 1.30) show **overdispersion**. No event with Z ≤ mean/3 was observed, but 10⁴–2·10⁴ samples cannot test
probabilities of 10⁻⁹–10⁻¹⁶. The deep tail is therefore untested.

Integers have a visibly heavier tail. The five integers with Z(2048) ≤ 17 in the 10⁸ sample (100010625, 100041825,
100062081, 100100265, 100105281) are all divisible by 3. For such n, xn + 1 is never divisible by 3, a local situation
primes cannot have. A local-factor mixture is the natural explanation (Assessment); it is why §5.3 requires
local-factor-conditioned masses.

**Near-square forcing (Lemma N in the data; recomputed by the reviewer).** For p = m² + 24 and x ≤ 2048:
* *Endpoint lines.* 55 are aligned with f = m² + 24 by the conductor criterion (x + 24 = c·s², c | 24,
  disc ℚ(√−(x+24)) | x). Of these, 40 have zero successes in 5 000 primes; E_8, E_12, E_24, E_40, E_48, E_72, E_76, E_84
  are among them. For example, x = 12: 36 = 6², ℚ(i); x = 24: 48 = 3·4², ℚ(√−3).
* *Level lines.* 27 are aligned (24x + 1 a square), and 12 have zero successes: x = 15, 92, 376, 392, 551, 672, 876, 1247,
  1335, 1520, 1552, 1855.
* *Containment.* Every zero-success line is aligned. The converse fails because of exceptional primes. E_172 is aligned
  yet has 122 successes, and E_176 has 389. L_7, L_12, L_40 (24x + 1 = 13², 17², 31²) have 377, 197, 45 successes. In
  the sample, the numbers of m divisible by 13, 17, 31 are 377, 288, 156. For L_7 the residual successes match the
  exception 13 | m (13 ≡ −1 mod 7). For L_12 and L_40, divisibility is necessary but not sufficient.

So the aligned set is sparse (O(√X)), and alignment explains every observed forced failure. The near-square X* (5.4 log p)
is larger than for generic primes (3.4 log p), but finite.

## 7. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict (Assessment): NARROWED.**
* *Blocked* (scoped theorems; scope as stated in each):
  * properties of line data that 𝔐 satisfies with positive probability, for any S_θ with θ < 2 log 2, including
    Conjecture 3.4 (Cor M3);
  * block-robust 𝔐-almost-sure properties, for any S_A (Cor M4);
  * a general lottery principle without a quadratic-alignment clause (Prop 5.5, CONDITIONAL on HL-F), and the first-draft
    principle with it but without local admissibility (review counterexample, §5.3).
* *Survives:* ES-specific far-lower-tail hypotheses (LT, H⁻mom, H⁻_BM type). They are sufficient but ES-specific. A
  research target for a general principle is described in §5.3, with three necessary features, the alignment Lemma N, and
  the open uniform-alignment gap.
* *Strengthened* (small, PROVED): Theorem U, the fixed-window bound with exponent ℓ(X)/2, extending Fable Thm 3.2; and
  Theorem M with Cor M3/M4, the model calibration and the barriers.

**The four hard screens (for "LT-type hypothesis ⟹ S_A").**
1. *T1 squares.* Square-sensitive: stated for primes, and the integer versions fail at squares (CERTIFIED for 5 000
   squares). As a mechanism there is nothing to test, because the hypothesis *assumes* the lottery's tail.
2. *8/131.* Any such hypothesis has a threshold. Whether a numerator-8 analogue holds, and whether 131 and 241 lie below
   its range, is not established here.
3. *Tied modulus.* FAILS as a mechanism. The hypothesis does not break the tied modulus; it postulates the far tail of
   the tied lottery.
4. *Fixed p.* Formally passes. The step that recovers one p is "count < 1", legitimate only because the bound is < 1 per
   block (M4 is the matching barrier).

**Proposed FRONTIER §7.2 addendum (text for the curator; do not edit FRONTIER here).**
> *(z53, `Z53_HCHYP.md`.)*
> * **Model scale (Thm M, PROVED in the model).** In the uniform-residue Kubilius model, almost surely
>   HC(p) ≤ (log p)^A for all large p when A > 2 log 2, and HC(p) > (log p)^θ infinitely often when θ < 2 log 2. So
>   Conjecture 3.4 (HC ≪ log p) is model-null, and the model-consistent target is A > 2 log 2. This does not refute
>   Conj 3.4 for actual primes.
> * **Invisible in practice (EVIDENCE).** X*/log p = 3.42–3.45 for log p ∈ [18, 36].
> * **Barriers (PROVED, as properties of model line data).** Model-typical properties cannot formally imply
>   HC ≤ (log p)^θ for θ < 2 log 2, and block-robust properties cannot imply S_A.
> * **Fixed windows (PROVED mod Henriot).** #{p ≤ y : HC(p) > X} ≪_X y(log y)^{−1−ℓ(X)/2}.
> * **General principles.** A general "lottery lower-tail" principle needs local admissibility, dependence control and a
>   quadratic-alignment clause. Without the last it is false given Hardy–Littlewood F, because T1 lives on m² + 1.
>   No counterexample-free formulation is known. Uniform unalignment of the ES lines is open beyond height (log x)^{1/10}.
> * **Standard conjectures.** No implication from GRH, GLH, EH, Chowla–Elliott, Hooley R* or HL is established, and none
>   is known.

**Bottom line (Assessment).**
* The conditional route to HC(p) ≪ (log p)^A is now mapped in the Kubilius model. The model-consistent exponent is
  > 2 log 2, and the lines that carry the conclusion lie deep in the lottery regime, where success comes from rare highly
  factorable values of p + x and xp + 1.
* Properties of line data that the model satisfies with positive probability cannot formally give HC ≤ (log p)^θ for
  θ < 2 log 2. Properties robust to one changed prime per dyadic block cannot give S_A at all.
* The standard conjectures, through every implementation known here, supply only such properties. What remains is a
  far-lower-tail input.
* Its ES-specific forms are sufficient but are ES restated with extra quantitative content. A general form must at least
  respect local admissibility, control dependence, and exclude quadratic conspiracies (T1 and its near-square
  deformations). Review showed how easily a natural-looking formulation fails.
* So no conditional theorem "ES ⟸ standard conjecture" emerges. The live questions are:
  * a counterexample-free general formulation;
  * the uniform alignment lemma (UA);
  * a lower-bound sieve showing Theorem U is sharp;
  * any far-tail input for a single lottery family.

## 8. Reproduction

```sh
ulimit -v 6000000
gcc -O2 -o /tmp/z53lines scripts/z53_hchyp_lines.c -lm
for e in 8 10 12 14; do timeout 1800 /tmp/z53lines stat $(python3 -c "print(10**$e)") 20000 2048 data/z53/hchyp/stat_1e${e}_X2048.txt; done   # ~3-6 min each
timeout 1800 /tmp/z53lines stat 4000000000000000 10000 2048 data/z53/hchyp/stat_4e15_X2048.txt
timeout 1800 /tmp/z53lines int 100000000 20000 2048 data/z53/hchyp/int_1e8_X2048.txt          # also 1e12
timeout 1800 /tmp/z53lines near 24 100000 5000 2048 data/z53/hchyp/near_k24_1e10_X2048.txt    # also k = 120
timeout 900  /tmp/z53lines sq 10001 5000 2048 data/z53/hchyp/sq_1e8_X2048.txt                 # T1 control: 0 successes
timeout 60   /tmp/z53lines list 128 /dev/stdout 193 409 577 2521 3361 21841 83449 8813281      # test primes
python3 scripts/z53_hchyp_analyze.py data/z53/hchyp/stat_1e12_X2048.txt                         # per-line tables
python3 scripts/z53_hchyp_ztail.py data/z53/hchyp/stat_1e12_X2048.txt.hc                        # Z lower tails
python3 scripts/z53_hchyp_model.py                     # model curves (Monte Carlo, ~10 min)
cd scripts && python3 z53_hchyp_xstar_model.py         # model X* and local exponent (~20 min)
```

## 9. Review record

Hostile internal review (deep-mode subagent, 2026-11-01; read the memo, re-ran the T1 control and test primes, recomputed
tables). Verdict before repair: MAJOR-REPAIRS-NEEDED; the model theorem and Theorem U "largely survive". Repairs made:
* **GLT refuted as first stated.** Counterexample: lines (5jn, 5, 4), a local obstruction with probability 1. GLT's status
  is withdrawn and §5.3 is rewritten as necessary features plus a research target.
* Alignment widened to characters of either parity (example F = n, q = 5, c = 2, f = m² − 5); the primitive character is
  made explicit; exceptional primes, including 2, are discussed.
* The claimed "only primes near scaled squares can be heavily aligned" is deleted.
* Prop 5.5: the even-m argument is supplied (Fable's T1 statement assumes m odd).
* Statements about standard conjectures are relabelled Assessment; M3/M4 are scoped to properties of model line data.
* The model exponent is no longer stated as an arithmetic necessity; "boundary undecided" is added.
* The M4 block-robustness application was restricted (later corrected again by the cross-model review, see below).
* Remark U corrected: failure is not generic right after x ≫ log log p. Only the Kneser–Rankin estimate becomes
  ineffective there; failure becomes generic beyond (log p)^{log 2}.
* Prop 5.1 restricted to the bare count statement with B ≥ 0.
* Lemma N mass now keeps the log log factor.
* M1 k = 0 case; M2 lower bound noted; M(a) small θ by monotonicity; M(b) error O(log p) made explicit.
* "Sub-Poissonian" withdrawn: the large-X counts are overdispersed and the deep tail is untested.
* Near-square statement changed from equality to containment, with the reviewer's counts.
* Independence-ratio ranges corrected.
* The cyclic Monte Carlo and the X* computations are labelled as surrogates.
* One table entry corrected (10¹⁴ [4,8): 0.15 / 0.14).
* "Low-Z" defined; Cramér analogy labelled Assessment ("currently unproved"; Granville's constant as a lower-bound
  prediction).
* Section cross-references fixed.
* Scripts now decode HC = 0 as censored (no success ≤ X_max) and handle all-zero samples.

The review confirmed: Lemma K and Theorem U (forms primitive and non-proportional, index-2 subgroups, exponent, X = 4
check); M1/M2 calculations; Theorem M(a)/(b) up to the listed completions; Remark U arithmetic; the HC/X* and Z-tail
numbers; T1 control 300/300 squares with 0 successes in 57 600 line tests; HC test values 7, 4, 15, 64, 39. A cross-model
review is expected to follow.

**Cross-model review** (`data/z53/xreview/REVIEW_HCHYP.md`, script `scripts/z53_xrev_hchyp_check.py`; verdict
ACCEPT-WITH-FIXES).

*Confirmed.* M1, M2, Theorem M(a)/(b), M3, the M4 theorem, Lemma K, Theorem U (Henriot 2012 / 2014 erratum New Thm 5
checked from the primary source), Prop 5.1, Prop 5.5 (conditional), Lemma N and its mass bounds, and the §1 dictionary.

*Reproduced.* The reviewer reran the full odd-square and 10⁸ samples byte-identically and reproduced all X* and Z
summaries, the near-square counts, and the surrogate tables.

*Fixes applied:*
1. The M4 application now uses asymptotic-error statements. "Slack ≥ 1" was false for sliding intervals, which can meet
   two blocks. H_Kub is narrowed to the line-data reading.
2. LT is stated with explicit c > 0, A > 2 log 2 and the event HC(p) > (log p)^A, so that it is equivalent to S_A. The
   "(log x)^A inside the count" variant is noted as strictly stronger.
3. Remark U is retitled "model-null", not arithmetic impossibility. The direction is corrected (Q(a) < ½ for a *above*
   ≈ 0.187), and the (log p)^{0.13} transition and the ω-deficit domination are marked heuristic (also in §5.1).
4. The surrogate X* claim is weakened to log X*/log log p → 2 log 2; finite-difference slopes are not claimed to
   converge. The independence benchmark is defined with P_x = P̂(E_x ∨ L_x).
