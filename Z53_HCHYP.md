# Z53_HCHYP — which hypothesis could give HC(p) ≪ (log p)^A? (wave z53, lane HCHYP)

**ES is open. Nothing here proves or disproves ES, conditionally on a standard conjecture or otherwise.**
Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. All results are internally reviewed
only. Scripts `scripts/z53_hchyp_*`, data `data/z53/hchyp/` (4 MB). Kickoff: `z53_lanes.md` §HCHYP (FRONTIER §7.2/§7.4).

## 0. Verdict first

**Verdict: NARROWED.** No standard conjecture is shown to give HC(p) ≪ (log p)^A, and none is found to. What this lane
adds:

1. **The target's scale is (log p)^{2 log 2}, not log p (Theorem M, PROVED in an explicit Kubilius model 𝔐).** In 𝔐, almost
   surely HC(p) ≤ (log p)^A for all large p when A > 2 log 2 ≈ 1.386, and HC(p) > (log p)^θ for infinitely many p when
   θ < 2 log 2. So Fable's Conjecture 3.4 (HC ≤ C log p) has 𝔐-probability 0, and the correct form of the FRONTIER §7.2
   target is S_A with A > 2 log 2. The deviation from linear growth is invisible at accessible heights. In 𝔐 the Poisson
   scale X*(p) has local exponent 0.9–1.0 at log p ≈ 18–28 and only 1.2 at log p = 1600. In the data
   X*/log p = 3.42–3.45 is constant for log p ∈ [18, 36] (EVIDENCE, §6).
2. **Two barriers for hypotheses (Cor M3, M4, PROVED).**
   * *Model-null barrier.* No property of line data that 𝔐 satisfies with positive probability can imply S_θ for
     θ < 2 log 2. This disposes of every "typical-behaviour" (Erdős–Hall-regime) hypothesis.
   * *Planted barrier.* No hypothesis robust under changing one prime per dyadic block implies S_A. This is B6 made exact
     for this target: a hypothesis must bound the joint failure of ≳ (log p)^{2 log 2} lines with frequency < 1 per block.
3. **Fixed windows: the Landau saving is (log y)^{−1/2} per line (Theorem U, PROVED modulo Henriot).**
   #{p ≤ y : HC(p) > X} ≪_X y (log y)^{−1−ℓ(X)/2}, where ℓ(X) counts the lines with coordinate ≤ X. This generalises Fable's
   Thm 3.2 (X = 4). A version uniform in X with constants C^{ℓ(X)} would be 𝔐-false (Remark U): beyond x ≍ log log p, line
   failure is generic and not confinement.
4. **Hypothesis catalogue (§5).** Five candidate shapes, each given (i)–(v).
   * Erdős–Hall-type equidistribution: dead by M3.
   * Uniform high-dimensional Landau sieve: controls confinement only, so irrelevant beyond the Kneser regime.
   * Kubilius/Elliott/Chowla/Hardy–Littlewood with error terms: dead by M4.
   * ES-specific lower tails (H⁻_BM, H⁻mom, the joint-failure bound LT): imply S_A trivially but are ES in disguise
     (Prop 5.1).
   * The general principle **GLT**, "the Cramér–Granville principle for divisor lotteries": the weakest *non-ES-specific*
     principle found. It implies S_A for every A > 2 log 2 (Thm 5.3, modulo a stated alignment gap) and is false over
     integers (squares).
   * Prop 5.5 (CONDITIONAL on Hardy–Littlewood F): the unrestricted GLT is false. T1 transports to the primes m² + 1, so
     the principle must exclude quadratically aligned families. Lemma N shows that every fixed quadratic family aligns only
     O_f(√X) ES lines.
   * GLT is not implied by GRH/GLH/EH/Chowla–Elliott/Hooley R*/Hardy–Littlewood (each fails at an identified step, §5.6).
     Its nearest standard relative is Cramér's prime-gap conjecture: same shape (pointwise, polylog window, expected
     count ≍ log x, local-factor correction), same unprovability.
5. **Numerics (EVIDENCE, CERTIFIED controls).** Primes p ≡ 1 (8): 20 000 each at 10⁸, 10¹⁰, 10¹², 10¹⁴, 10 000 at
   4·10¹⁵, all lines x ≤ 2048.
   * Per-line success is P_x ≈ c·log p/x in the mean regime (c ≈ 1.3 endpoint, 0.7 level), with a rising onset, as 𝔐
     predicts.
   * The lower tail of the number of successful lines is *sub-Poissonian* at primes (min/mean ≥ 0.3).
   * Integers and near-squares are heavier: X*/log p ≈ 4.1 and 5.5. Near-squares lose exactly the lines Lemma N predicts.
   * Odd squares: all 2·768 lines fail at all 5 000 squares tested (CERTIFIED T1 control).

**Promise:** 1/5 as a conditional route (the principle is clean but non-standard, and no route to it is visible); 3/5 as
calibration (it changes the §7.2 target and kills a class of hypotheses in one stroke).

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
shapes that could possibly work from those that provably cannot, and none asks for a *general* principle with ES as an
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

§6 shows the per-line success curve of actual primes has 𝔐's shape, within a factor ≈ 0.6–1.0 (EVIDENCE).

### 3.2 One line

**Lemma M1 (PROVED).** Let G be a finite abelian group of order n, h ∈ G∖{1}, k ≥ 0, and g₁, …, g_k i.i.d. uniform in G.
Then ½·min(1, (2^k − 1)/n) ≤ P(h ∈ Σ) ≤ min(1, (2^k − 1)/n).

*Proof.* Let Z := #{∅ ≠ I ⊆ [k] : g_I = h}, where g_I := ∏_{i∈I} g_i. Since h ≠ 1, h ∈ Σ ⟺ Z > 0.
* For I ≠ ∅, g_I is uniform, so EZ = (2^k − 1)/n. The upper bound is P(Z > 0) ≤ min(1, EZ).
* For distinct non-empty I, J, the events {g_I = h} and {g_J = h} are independent. Indeed, if J ⊄ I, pick j ∈ J∖I.
  Conditionally on (g_i)_{i≠j}, the element g_J is uniform, so P(g_I = h, g_J = h) = P(g_I = h)/n = 1/n². If J ⊂ I,
  swap the roles.
* Hence EZ² = EZ + (2^k − 1)(2^k − 2)/n² ≤ EZ + (EZ)².
* Paley–Zygmund then gives P(Z > 0) ≥ (EZ)²/EZ² ≥ EZ/(1 + EZ) ≥ ½ min(1, EZ). ∎

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

Reading: for x = (log p)^θ (so φ(x) ≈ x), P(line succeeds) = (log p)^{−Q(θ/log 2)+o(1)} for log 2 ≤ θ ≤ 2 log 2. For
θ ≥ 2 log 2 + δ it is ≍ log p/φ(x); there the probability is carried by the N with ω(N) ≈ 2 log log N, which carry the
mean of τ.

### 3.3 The extreme-value scale of HC

**Theorem M (PROVED for 𝔐).**
(a) For every θ < 2 log 2: 𝔐-almost surely HC(p) > (log p)^θ for infinitely many p.
(b) For every A > 2 log 2: 𝔐-almost surely HC(p) ≤ (log p)^A for all but finitely many p.
More precisely:
* for log 2 < θ < 2 log 2, −log P(HC(p) > (log p)^θ) ≤ (log p)^{max(log 2 + η, θ − Q(θ/log 2)) + o(1)} for every η > 0;
* for A > 2 log 2 + 2δ, P(HC(p) > (log p)^A) ≤ exp(−(3/40)(A − 2 log 2 − 2δ) log p log log p) for large p.

*Proof.* Put λ = λ_p, X = (log p)^θ, and P_ι := P(line ι succeeds). For x ≥ 3 we have −1 ≠ 1 in G_x.

(a) *Small lines.* For every line, 1 − P_ι ≥ P(k_ι = 0) = e^{−λ}. Fix 0 < η < 1 − log 2 and Y := (log p)^{log 2 + η}.
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
  P_{(x,E)} ≥ ½(e^λ/2 − 1)/φ(x) ≥ log p/(5x)   (e^λ = log p ≥ 20, φ(x) ≤ x).
Also Σ_{x∈𝒞, Y<x≤X} 1/x = (1/4 + 1/8) log(X/Y) + O(1/Y) = (3/8)(A − 2 log 2 − 2δ)λ + o(1). Hence
P(HC(p) > X) ≤ ∏(1 − P_{(x,E)}) ≤ exp(−(3/40)(A − 2 log 2 − 2δ) log p log log p), which is summable over p. The first
Borel–Cantelli lemma gives (b). ∎

**Remark M (the scale is invisible in practice; EVIDENCE).** Let X*(p) be the least X with Σ_{x∈𝒞, x≤X} (P_E + P_L) ≥ log p.
This is the Poisson scale: P(all lines ≤ X fail) ≈ e^{−Σ P} reaches 1/p there. In 𝔐 (with the
M1-upper value, `z53_hchyp_xstar_model.py`) X*/log p = 2.55, 2.46, 2.48, 2.68, 2.96, 3.33, 3.79, 4.33 at
log p = 18.4, 27.6, 50, 100, 200, 400, 800, 1600. The local exponent d log X*/d log log p is 0.91 → 1.20, and it tends to
2 log 2 only extremely slowly. The data (§6) give X*/log p = 3.42, 3.43, 3.44, 3.44, 3.45 at log p = 18.4, 23.0, 27.6,
32.2, 35.9. The census maximum of HC over all p ≤ 10⁸ is 64 (Fable §3.2), against X*(10⁸) = 63. So the data are in 𝔐's
pre-asymptotic regime, where HC_max looks linear in log p. Fable's linear Conjecture 3.4 is a correct description of the
observable range but, by Theorem M(a), an 𝔐-null statement asymptotically.

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
Averaged statements whose error term exceeds 1 per dyadic block are block-robust. This is B6 made exact for S_A: a useful
hypothesis must bound the joint failure of all lines up to ≳ (log p)^{2 log 2} with frequency < 1 per block.

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
The data (P(HC > 4) = 0.083 → 0.042 from 10⁸ to 4·10¹⁵, §6) decay as slowly as (log)^{−1}-type laws do. A matching lower
bound would need a half-dimensional lower-bound sieve for primes in several forms, which is not attempted here.

**Remark U (why the Landau saving cannot be uniform).** Suppose the implied constant in Theorem U were ≤ C^{ℓ(X)} uniformly
for X ≤ log y. With X = 8 log y/log log y this would give a count < 1, i.e. HC(p) ≤ 8 log p/log log p for all large p.
That is S_θ for every θ > 1, which Cor M3 says 𝔐 violates almost surely. The proof shows the culprit: Lemma K allows
r − 2 exceptional primes, and for H = {1} that is φ(x) − 2. Once x ≫ log log p, this exceeds ω(N), the Rankin factor
s^{−(r−2)} explodes, and failure becomes the generic outcome (the lottery) rather than confinement. So **the per-line
saving (log p)^{−1/2} is real only in the Kneser regime x ≲ log log p.** This is the precise form of the dimension barrier
for HC. It also kills the "high-dimensional Landau" hypothesis of §5.2.

## 5. Hypotheses: what each shape can and cannot do

### 5.1 The regimes of a line, and what it takes

For a line at x and a prime p (λ = log log p) there are four regimes:
* **Kneser regime, x ≲ λ.** Failure is confinement up to boundedly many primes (Lemma K). It has Landau probability
  ≍ (log p)^{−1/2} (Theorem U).
* **Typical regime, λ ≪ x ≤ (log p)^{log 2−ε}.** Success is typical (Erdős–Hall). Failure comes from an ω-deficit or from
  confinement.
* **Lottery regime, x ≥ (log p)^{log 2+ε}.** Failure is typical. Success has probability (log p)^{−Q(θ/log 2)} up to
  θ = 2 log 2, and ≍ log p/x beyond.
* **S_A needs** about log p expected successes, i.e. lines up to (log p)^{2 log 2+o(1)} (Theorem M). These lines are deep
  in the lottery regime, where success comes from the *rare* integers N with ω(N) ≈ 2 log log p.

**Proposition 5.1 (PROVED, logic: "ES in disguise").** For events E_p, the statement
"∀ large y: #{p ∈ (y, 2y] : E_p} ≤ B(y)" with B(y) → 0 is equivalent to "E_p fails for all large p". So an averaged
hypothesis *about the ES lines* implies S_A only if it is equivalent to S_A, up to a finite census.

### 5.2 Catalogue

Columns: (i) implication; (ii) T1; (iii) 8/131; (iv) numerics; (v) strength.

**H_EH — Erdős–Hall-type equidistribution.** "The divisors of N are equidistributed mod q for most q", or "for most N",
or "for most lines x ≤ (log p)^θ at every p".
* (i) Cannot imply S_θ for θ < 2 log 2: it is 𝔐-typical (Cor M3). It is also tied-modulus: one N with many q is not the
  ES shape, since each line has its own N (B2).
* (ii) At squares every line fails, but H_EH speaks only of typical N, and squares have density 0. So squares do not
  refute it, and it cannot see T1.
* (iii) n/a. (iv) Data: P_x matches 𝔐 (§6).
* (v) Dead (M3).

**H_Lan — uniform high-dimensional Landau sieve ("MLD").** "Joint confinement of k lines has frequency ≤ C^k ∏(log)^{−1/2},
uniformly for k up to log x/log log x."
* (i) It bounds confinement only. Beyond x ≍ λ, failure ≠ confinement (Remark U), so it does not imply S_A. Taken as a
  failure bound, it would be 𝔐-false.
* (ii) Over integers it is false at squares (all levels are BM-confined, and √x squares ≫ the bound).
* (iii) — (iv) — (v) Irrelevant or false.

**H_Kub — joint Kubilius / Elliott / Chowla / Hardy–Littlewood with error terms.**
* (i) Block-robust, so no implication (Cor M4).
* (ii) Fine. (iii) Fine. (iv) —
* (v) Dead (M4).

**LT — ES-specific joint lower tail.** "#{p ∈ (x, 2x] : all lines ≤ (log x)^A fail} ≤ x exp(−c𝓜)", with 𝓜 the 𝔐-mass.
H⁻_BM, H⁻mom and MF₁ are of this kind.
* (i) Implies S_A trivially. Every count bound → 0 is equivalent to the conclusion (Prop 5.1).
* (ii) Fine (stated for primes). (iii) Has a threshold.
* (iv) Near tail consistent (§6).
* (v) ES in disguise.

**GLT — general lottery lower-tail principle (§5.3).**
* (i) Implies S_A for A > 2 log 2 (Thm 5.3, modulo the alignment gap).
* (ii) False over integers (squares) and false unrestricted (Prop 5.5, conditional on Hardy–Littlewood F). It needs a
  quadratic-alignment clause, which is exactly T1.
* (iii) Has a threshold. The 8/n analogue follows eventually, with no contradiction at 131 or 241.
* (iv) Consistent: sub-Poissonian tail, X* tracks 𝓜 (§6).
* (v) Not ES-specific. Logically stronger than ES. Not implied by any standard conjecture (§5.6).

### 5.3 The principle GLT ("Cramér–Granville for divisor lotteries")

**Lotteries.** A *lottery line* is λ = (F, q, c) with F(n) = an + b ∈ ℤ[n], a ≥ 1, q ≥ 3, and c ∈ (ℤ/q)^× ∖ {1}. Its event at
n is W_λ(n): "F(n) is coprime to q and has a divisor ≡ c (mod q)". Its model mass at height x is
P^𝔐_λ(x) := U(log log x, φ(q)) (Lemma M1's upper value). A family 𝓕 has mass 𝓜(𝓕; x) := Σ_{λ∈𝓕} P^𝔐_λ(x). The ES lines are
the lottery lines E_x = (n + x, x, −1) and L_x = (xn + 1, x, −1).

**Quadratic alignment.** Let f ∈ ℤ[m] be quadratic and put G := F∘f. The line λ is *aligned with f* if:
* the discriminant Δ of G is not a square;
* the Kronecker character χ_Δ is odd (Δ < 0);
* χ_Δ has conductor dividing q; and
* χ_Δ(c) = −1.

Then for every m with G(m) coprime to 2·lead(G)·Δ, every prime factor ℓ of G(m) has χ_Δ(ℓ) = 1, because Δ is a square
mod ℓ. Hence every divisor has χ_Δ = 1 ≠ χ_Δ(c), and W_λ(f(m)) fails: **λ is forced to fail along f.**

Conversely, suppose the prime factors of the values of G lie, up to finitely many, in ker ψ for a character ψ mod q. For
ℓ ∤ 2·lead(G)·Δ we have ℓ | G(m) for some m ⟺ Δ is a square mod ℓ ⟺ χ_Δ(ℓ) = 1. So ψ(ℓ) = 1 for almost all primes in
the index-≤2 subgroup K = {χ_Δ = 1} of (ℤ/lcm(q, cond χ_Δ))^×. Every class of K contains infinitely many primes
(Dirichlet), so ψ is trivial on K, i.e. ψ ∈ {1, χ_Δ}. Hence the definition captures *every* way a quadratic family can
force a line (PROVED; elementary plus Dirichlet).

**GLT(c, η) [CONJECTURE shape; nonstandard].** Let x be large and let 𝓕 be a family of lottery lines with a, |b|, q ≤ (log x)^B.
Suppose 𝓕 is *η-unaligned*: for every quadratic f ∈ ℤ[m] with non-square discriminant, the lines of 𝓕 aligned with f
carry mass ≤ (1 − η)𝓜(𝓕; x). Then
  #{p ∈ (x, 2x] prime : no line of 𝓕 holds at p} ≤ x·exp(−c·η·𝓜(𝓕; x)),
for x ≥ x₀(c, η, B).

The two clauses match the two known reasons for joint failure: *local factors* (absorbed in c < 1) and *quadratic
alignment* (T1 and its deformations, excluded explicitly).

**Theorem 5.3 (PROVED implication).** Suppose GLT(c, η) holds for some c, η > 0 and B ≥ A. Suppose also that

  **(UA)** the ES family 𝓕_X := {E_x, L_x : x ∈ 𝒞 ∩ [4, X]}, X := (log x)^A, is η-unaligned for all large x.

Then S_A holds for every A > 2 log 2, hence ES(p) for all large p.

*Proof.* 𝓕_X has a, |b|, q ≤ X. The computation in Theorem M(b) gives
𝓜(𝓕_X; x) ≥ (1/5 − o(1))(3/8)(A − 2 log 2 − 2δ) log x log log x. GLT bounds the number of p ∈ (x, 2x] at which every line
fails by x·exp(−cη𝓜) < 1 for large x. So the count is 0, i.e. HC(p) ≤ (log x)^A ≤ (log p)^A for all p ∈ (x, 2x]. ∎

**Lemma N (PROVED; the partial verification of (UA)).** Let f(m) = αm² + βm + γ with α ≥ 1 and D = β² − 4αγ ≠ 0. Among
x ∈ 𝒞 ∩ [4, X]:
* the endpoint lines E_x aligned with f number ≤ τ(|D|)(2√(αX) + √|D| + 1);
* the level lines L_x aligned with f number ≤ τ(4α)(2√α + √(X|D|) + 1) if D < 0, and ≤ 4α/D if D > 0.

In particular, for fixed f there are O_f(√X) aligned lines. Their mass is O_f((log x)^{(log 2)/2+o(1)}) + O_f(log x/(log x)^{(log 2)/2}),
which is o(𝓜(𝓕_X; x)). Hence (UA) holds against every *fixed* quadratic, and against every quadratic of height
≤ (log x)^{1/10}.

*Proof.*
*E_x.* Here G = f + x and Δ = D − 4αx. Alignment needs Δ < 0 and conductor | x. The squarefree kernel c of |Δ| divides
the conductor, hence x, hence D (c | 4αx − D). Write 4αx − D = cs² with c | D squarefree. For x ≤ X we need
s ≤ √((4αX + |D|)/c). Summing over c | D gives the bound.

*L_x.* Here G = xf + 1 and Δ = x(xD − 4α). Alignment needs xD < 4α and conductor | x. Then every prime with odd exponent
in x(4α − xD) divides x. Primes dividing both x and 4α − xD divide 4α, so 4α − xD = d s² with d | rad(4α).
* If D < 0, then x = (ds² − 4α)/|D| ≤ X forces s ≤ √((4α + X|D|)/d).
* If D > 0, then x < 4α/D.

*Mass.* Use the trivial bound U(λ, φ(x)) ≤ E[2^k]/φ(x) = log x/φ(x) ≤ 2 log x·log log x/x for the lines above
Y := (log x)^{log 2}, and mass ≤ 1 per line below Y.
* Aligned E-lines are x = (cs² + D)/(4α), quadratically spaced in s. Those ≤ Y number ≤ τ(|D|)(2√(αY) + √|D| + 1). Those
  > Y have Σ 1/x ≤ Σ_{c|D} Σ_{s ≥ s₀(c)} 4α/(cs² + D) ≪ τ(|D|)√(α/Y), since s₀(c) ≫ √(4αY/c).
* Aligned L-lines with D < 0 are x = (ds² − 4α)/|D|. Those > Y have Σ 1/x ≪ τ(4α)√(|D|/Y). With D > 0 there are
  < 4α/D of them in total.

For fixed f this is O_f(√Y + log x·log log x·Y^{−1/2}). For height ≤ (log x)^{1/10} we have α ≤ (log x)^{0.1}
and |D| ≤ 5(log x)^{0.2}. Then the lines below Y number ≤ (log x)^{(log 2)/2 + 0.1 + o(1)}, and the lines above Y have mass
≤ (log x)^{1 + 0.1 − (log 2)/2 + o(1)} ≤ (log x)^{0.76}. Both are o(log x), while 𝓜(𝓕_X; x) ≫ log x log log x.
(For larger heights the congruence conditions on s, ignored here, would have to be used.) ∎

*The gap in (UA).* For quadratics of large height the bounds above become vacuous. Heavy alignment needs |D| small
compared with X²α. Each prime lies on quadratics f = αm² + βm + γ with D = M² − 4αp, so only primes within O(αX²) of a
scaled square αm² can be heavily aligned. A uniform version of Lemma N over (α, D) is **not proved here**. The spacing
argument (squares near |D| are ≥ 2√(c|D|) apart) suggests it holds (Assessment).

**Proposition 5.5 (CONDITIONAL on Hardy–Littlewood Conjecture F for m² + 1, in the weak form
#{m : m² + 1 ∈ (x, 2x] prime} ≫ √x/log x).** The unrestricted principle, GLT without the alignment clause, is false for
every c > 0.

*Proof.* Take 𝓕 := {λ_a = (a(n − 1) + 1, a, −1) : a ∈ 𝒞 ∩ [4, (log x)^A]}.
* At p = m² + 1 we get F_a(p) = am² + 1. By T1 in the coordinate form (Fable §1.3, the level-line case; a ∈ 𝒞), am² + 1
  has no divisor ≡ −1 (mod a). So every line fails at every such prime.
* The mass of 𝓕 is that of the level lines, ≫ log x log log x for A > 2 log 2 (Theorem M(b) computation).
* So the unrestricted bound x·exp(−c𝓜) = o(1) contradicts ≫ √x/log x failures. ∎

Each λ_a here is aligned with f = m² + 1 (Δ = −4a, χ_{−4a} with conductor | a for a ∈ 𝒞), so GLT itself is not
contradicted. T1 transported to near-squares is exactly what the alignment clause must remove.

**(ii) T1.**
* Over integers, every GLT-type bound fails at squares: 5 000 odd squares ≈ 10⁸, all lines fail, CERTIFIED §6; there
  are √x squares against the bound x·e^{−c𝓜} = x^{−ω(1)}.
* The statement is for primes. The step false at squares is the joint-failure bound itself, since at squares failure is
  forced by alignment with f = m².

**(iii) 8/131.**
* The numerator-8 level lines (8Cn + 1 has a divisor ≡ −1 (mod 8C), giving 8/n = 1/(uBC) + 1/(nBC) + 1/(nuC)) are
  lottery lines.
* So GLT gives 8/p for p > p₀. At p = 131 and 241 the bound x·e^{−c𝓜} exceeds 1, so there is no contradiction: GLT is
  numerator-uniform *with a threshold* (screening line 2's allowed escape).
* It says nothing 4-specific. That is consistent with it being a statement about lotteries, not about Egyptian fractions.

**(v) Strength (honest).**
* GLT is logically stronger than ES (it bounds counts at every height).
* It is not ES-specific: it would equally give eventual 8/n, ES₅, I3-type and U-type statements, any finite union of
  tied-class divisor lotteries with model mass ≫ log x.
* It is consistent with 𝔐 (Theorem M(b) is its 𝔐-shadow), with every computation here, and with the near-square
  deformations (Lemma N, §6).
* Its closest standard relative is **Cramér's conjecture** (every interval [y, y + C(log y)²] contains a prime). That
  conjecture is also pointwise, has a polylog window, and has expected count ≍ log y. In Granville's corrected form the
  maximal gaps are ≈ 2e^{−γ}(log y)², a constant-factor correction coming from small primes — the analogue of c < 1 here.
* Like Cramér's conjecture, GLT is beyond GRH and every known method. Unlike Cramér, it needs an explicit exclusion of
  quadratic conspiracies, because ES lotteries carry T1.

### 5.4 Standard conjectures: the exact failing step

| conjecture | what it controls | failing step for S_A |
|---|---|---|
| GRH (Dirichlet, Dedekind) | sums over n at fixed χ; least QNR ≤ 2 log²p | Pointwise only in the colour layer. The BM layer is pointwise free: some level 4 \| t ≤ 4ℓ(p) has M_t^lev(p) > 0 ((J)103), and GRH gives ℓ(p) ≤ 2 log²p. But a line that is not BM-forced still fails generically beyond x ≍ log log p (Remark U). The lottery needs the class of a divisor, which no character sum at one p fixes (CLASS_FORCING Thm 2.1). |
| GLH | subconvexity / moments of L at fixed conductor | Same as GRH: values of L-functions control averages of line events over p (block-robust, M4). |
| EH / BFI (level x^{1−ε}) | divisor functions in APs averaged over q ≤ x^{1−ε} | Gives single-line statistics on average over p (Titchmarsh-type). The joint law of k lines needs k-fold divisor correlations, and already Σ τ(n)τ(n+h₁)τ(n+h₂) has no individual-shift asymptotic (Blomer, BLMS 49 (2017), "challenging open problem"; Browning's conjecture proved only on average over h). Block-robust in any case (M4). |
| Chowla / Elliott (MRT 2015; Tao 2016) | k-point correlations of bounded multiplicative functions, k fixed | Fixed k with o(x) error: block-robust (M4). No uniformity in k growing with x is known or stated (checked: MRT, Tao, Tao–Teräväinen all have k fixed). |
| Hooley R* / Kloosterman bounds | Σ_c S(m,n;c)/c at fixed (m,n) | No fixed-(m,n) Kloosterman sum arises at one p (SINGLE_P_COUNT Prop 6.1); tied modulus. |
| Hardy–Littlewood k-tuples / Bateman–Horn | prime values of fixed forms, k fixed | Fixed k: block-robust. In the uniform-in-k direction, Maier (Michigan Math. J. 32 (1985)) and Friedlander–Granville (Ann. Math. 129 (1989), Cor 2) show relative-error uniformity fails at polylog length. Bateman–Horn/HL-F *refutes* the unrestricted principle (Prop 5.5). |
| Inverse large sieve (Green–Harper GAFA 2014 Conj 1.7; Walsh Duke 2012) | sets occupying ≤ (p+1)/2 classes are quadratic images or small | Philosophically the same clause as GLT's alignment ("quadratic = the only conspiracy"), but for a different regime: the failure set of the ES lines is not a set with few residues mod every p. No implication. |
| Cramér / Granville gap conjecture | primes in windows of length (log y)² | No implication either way. The analogy is of shape only (§5.3 (v)). |

**Answer to the kickoff's last question:** none of GRH, GLH, EH, Chowla–Elliott, Hooley R* implies any hypothesis of the
needed shape. By Cor M3/M4, each of them is either 𝔐-typical (it cannot give S_θ for θ < 2 log 2) or block-robust (it
cannot give S_A at all). Each of them would have to be supplemented by a far-lower-tail statement of GLT type.

## 6. Numerics (EVIDENCE unless marked CERTIFIED)

Program `scripts/z53_hchyp_lines.c` (C, exact factoring by trial division + Pollard–Brent + deterministic Miller–Rabin;
divisor-residue BFS). For each n and each x ∈ 𝒞 ∩ [4, 2048] it tests E_x and L_x. Files `data/z53/hchyp/*_X2048.txt`
(per-x counts) and `.hc` (per n: HC, Z(64), Z(256), Z(1024), Z(2048), where Z(X) = number of successful lines ≤ X).

**Per-line rates, x·P_x/log p** (mean over x ∈ 𝒞 in the dyadic bin; endpoint / level):

| bin | 10⁸ (L = 18.4) | 10¹² (27.6) | 10¹⁴ (32.2) | 4·10¹⁵ (35.9) | integers 10¹² |
|---|---|---|---|---|---|
| [4,8) | 0.26 / 0.24 | 0.18 / 0.17 | 0.15 / 0.15 | 0.14 / 0.13 | 0.17 / 0.15 |
| [16,32) | 0.65 / 0.47 | 0.50 / 0.38 | 0.45 / 0.35 | 0.41 / 0.33 | 0.46 / 0.34 |
| [64,128) | 1.06 / 0.62 | 0.96 / 0.59 | 0.91 / 0.56 | 0.87 / 0.54 | 0.84 / 0.50 |
| [256,512) | 1.17 / 0.63 | 1.25 / 0.68 | 1.24 / 0.68 | 1.23 / 0.68 | 1.04 / 0.56 |
| [1024,2048) | 1.08 / 0.59 | 1.29 / 0.68 | 1.34 / 0.70 | 1.37 / 0.72 | 1.07 / 0.56 |

In 𝔐 (Monte Carlo in ℤ/φ(x), `z53_hchyp_model.py`) the same normalisation at log p = 27.6 is 0.12, 0.33, 0.69, 1.09, 1.42.
Shape and onset agree; the level-line constant is ≈ ½ the endpoint one. The plateau (P_x ∝ log p/x) is the mean regime,
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

**Joint failure vs independence.** F(X)/∏_{x≤X}(1 − P_x) = 2.6–3.3 at X = 7–8 and 10–50 at X = 15–16 (counts 1–20; all
scales). Line failures are *positively associated* at small X, consistent with a shared local factor (p mod small primes;
y8 "clean levels"). GLT's constant c < 1 is designed for exactly this.

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

At primes the near tail is Poisson-like (X = 64) and the observed spread at large X is sub-Poissonian. Integers have a
much heavier tail. All of the low-Z integers in the 10⁸ sample are divisible by 3. Then xn + 1 is never divisible by 3,
which is a local factor that primes cannot have (p ∤ 3). This is a local-factor mixture effect, the reason GLT is stated
for primes with c < 1.

**Near-square forcing (Lemma N in the data).** For p = m² + 24 the lines with zero successes in 5 000 primes include:
* L₁₅, L₉₂, L₃₉₂ (24x + 1 = 19², 47², 97²);
* L₇, L₁₂, L₄₀ with only 1/13, 1/17, 1/31-type residual success. Those are the m divisible by s, where the gcd exception
  of the alignment applies: 13 | m makes 13 ≡ −1 (mod 7) a divisor of 7p + 1;
* E_8, E_12, E_24, E_40, E_48, E_72, E_76, E_84, … These are exactly the x with x + 24 = c·s², c | 24, and
  disc ℚ(√−(x+24)) | x. For example, x = 12: 36 = 6², ℚ(i); x = 24: 48 = 3·4², ℚ(√−3).

The aligned set is sparse (O(√X)), and the near-square X* (5.4 log p) is larger than for generic primes (3.4 log p), but
finite.

## 7. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: NARROWED.**
* *Killed* (scoped theorems):
  * every hypothesis shape that 𝔐 satisfies with positive probability, for any target S_θ with θ < 2 log 2, including
    Conjecture 3.4 itself (Cor M3);
  * every block-robust (averaged) hypothesis, for any S_A (Cor M4);
  * the uniform high-dimensional Landau sieve beyond the Kneser regime (Remark U);
  * the unrestricted general lottery principle (Prop 5.5, CONDITIONAL on HL-F).
* *Survives:* a general far-lower-tail principle with a quadratic-alignment clause (GLT). It implies S_A for every
  A > 2 log 2, modulo the uniform-alignment gap (UA). It is the divisor-lottery analogue of Cramér's conjecture, and no
  standard conjecture implies it.
* *Strengthened* (small, PROVED): Theorem U, the fixed-window bound with exponent ℓ(X)/2, extending Fable Thm 3.2;
  Theorem M, the model scale (log p)^{2 log 2}.

**The four hard screens (for GLT ⟹ S_A).**
1. *T1 squares.* PASSES as a hypothesis: stated for primes; the integer version is false at squares, and the alignment
   clause is T1. As a mechanism there is nothing to pass: GLT *assumes* the lottery.
2. *8/131.* PASSES by threshold: numerator-uniform, with x₀; at 131 and 241 the bound is > 1.
3. *Tied modulus.* FAILS as a mechanism. GLT does not break the tied modulus; it postulates the far tail of the tied
   lottery. This is the honest reading: the hypothesis is where the tied modulus is hidden.
4. *Fixed p.* Formally PASSES. The step that recovers one p is "count < 1", which is legitimate only because the bound is
   < 1 per block (M4 is the matching barrier). Every hypothesis that reaches a fixed p must have this shape or be
   pointwise.

**Proposed FRONTIER §7.2 addendum (do not edit FRONTIER here; text for the curator).**
> *(z53, `Z53_HCHYP.md`.)* The right scale for HC is (log p)^{2 log 2}, not log p. In the uniform-residue Kubilius model
> almost surely HC(p) ≤ (log p)^A eventually for A > 2 log 2, and HC(p) > (log p)^θ infinitely often for θ < 2 log 2
> (PROVED in the model, Thm M). So Conjecture 3.4 (HC ≪ log p) is model-null, and the target should read A > 2 log 2.
> Numerically the difference is invisible: X*/log p = 3.42–3.45 for log p ∈ [18, 36], and in the model the local exponent
> is still 1.2 at log p = 1600.
> Barriers (PROVED): no hypothesis that the model satisfies with positive probability formally implies HC ≤ (log p)^θ for
> θ < 2 log 2 (this kills Erdős–Hall-type statements), and no block-robust averaged hypothesis implies S_A at all.
> Fixed windows: #{p ≤ y : HC(p) > X} ≪_X y(log y)^{−1−ℓ(X)/2} (PROVED mod Henriot; uniformity in X is model-false beyond
> x ≍ log log p).
> The weakest non-ES-specific sufficient principle found is a "Cramér–Granville principle for divisor lotteries" (GLT):
> joint failure of a quadratically unaligned family of tied-class divisor events has frequency ≤ x·e^{−c·(model mass)}.
> Over integers it is false (squares); unrestricted it is false given Hardy–Littlewood F (near-squares m² + 1 carry T1),
> so it needs a quadratic-alignment clause. It implies S_A given uniform unalignment of the ES lines, which is proved
> only for quadratics of bounded height. No standard conjecture (GRH, GLH, EH, Chowla–Elliott, Hooley R*, HL) implies it.

**Bottom line.**
* The conditional route to HC(p) ≪ (log p)^A is now fully mapped. The exponent must exceed 2 log 2. The lines that carry
  the conclusion lie deep in the lottery regime, where success comes from rare highly factorable values of p + x and
  xp + 1.
* Every hypothesis that is "typical" in the Kubilius sense, or robust to one exceptional prime per dyadic block, provably
  cannot do it. That covers all standard conjectures.
* What remains is a far-lower-tail principle. Its only natural general form is a Cramér-type conjecture for divisor
  lotteries, with an explicit clause excluding quadratic conspiracies (the T1 family and its near-square deformations).
* It is clean and plausible, and every test here agrees with it. It is also as far beyond current technology as Cramér's
  conjecture.
* So no conditional theorem "ES ⟸ standard conjecture" emerges, and one now knows exactly why. The live mathematical
  questions it leaves are: the uniform alignment lemma (UA), a lower-bound sieve showing Theorem U is sharp, and any
  far-tail input for a single lottery family.

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

TODO (hostile review pending).
