# Z56_K4CHEN — Chen-type switching for K(4): p + 4 ∈ S exactly, few 𝒬-factors in 4p + 1

**ES is OPEN.** Nothing here proves or disproves it. All results are internal (internally reviewed only).
Lane K4CHEN (wave z56). Scripts `scripts/z56_k4chen_*`, data `data/z56/k4chen/`.

Notation (as in `Z55_P415.md`): 𝒬 = primes ≡ 3 (mod 4), 𝒬(z) = ∏_{q∈𝒬, q<z} q; S = {n ≥ 1 : every prime factor
≡ 1 (mod 4)}; N₁ = p + 4, N₂ = 4p + 1; Ω_𝒬(n) = number of 𝒬-prime factors of n with multiplicity (always even for
n ≡ 1 (4)); 𝒜 = {p ≤ x prime, p ≡ 1 (8)}, X = li(x)/4; W(z) = ∏_{q∈𝒬,q<z}(1 − 1/q); F, f = semi-linear (κ = 1/2,
β = 1) beta-sieve functions, A := (e^γ/π)^{1/2}, F(s) = 2A s^{−1/2} (0 < s ≤ 2), F(1) = 2A = 1.5059;
𝔊 = (9/8)∏_{q∈𝒬,q≥7} q²(q − 3)/(q − 1)³ (P415 Step 2). z₁ = x^{θ₁}, z₂ = x^ζ. **Unit 𝒰 := 𝔊·X·W(z₁)·W(z₂) ≍
x/(log x)²**; all "margins" below are in units of 𝒰.

## 0. Verdict: **strengthened at model level + narrowed** — new mechanism; C(6) at BV level, robust in the model

Target family **C(r)** (r even): ≫ x/(log x)² primes p ≤ x, p ≡ 1 (8), with p + 4 ∈ S and Ω_𝒬(4p + 1) ≤ r.
C(0) is a quantitative strengthening of P(4,15), hence implies K(4) (HCKILL Lemma 1.1). P415 Theorem U is C(r₀) for an
unspecified r₀; its model gave r = 10.

1. **New mechanism (§2): Chen-type switching on the many-factor configurations of 4p + 1**, plus a *direct* upper
   sieve over products Q of the r + 1 smallest 𝒬-factors in which the 𝒬-parity of N₂/Q forces the extra factor for
   free. The bad set {Ω_𝒬(N₂) ≥ r + 2, all 𝒬-factors ≥ x^ζ} has a small Buchstab mass (factorial suppression,
   Poisson-like with mean ≈ ½ log(1/ζ) in the tested range, §3.2), so switching it away costs a bounded loss factor
   (2/a)b^{−1/2} ≈ 14.7 times a tiny mass, while the tested additive weights (finite LPs, which return Richert's
   weight) pay ≍ log(1/ζ)/r. Exact combinatorial reduction: **Lemma D (PROVED)**.
2. **Model numerics (Assessment; §4).** P415's model conventions; "pen" multiplies the *switched* main terms
   (pen = 1 is the locally consistent evaluation, P415's 2.35 an illustrative inflation); BV level 1/2 everywhere.
   | target | direct + switching (MC) | pure switching, deterministic witness (ε = 10⁻³) | P415 model |
   |---|---|---|---|
   | C(8) | +0.366 (pen 1), +0.204 (pen 2.35) | +0.189 (pen 2.35) | — |
   | **C(6)** | **+0.291 (1), +0.186 (1.5), +0.071 (2.35)** | **+0.278 (1), +0.163 (1.5), +0.037 (2.35)** | — |
   | C(4) | +0.047 (1), +0.006 (1.1), **−0.031 (1.2)** | +0.0135 (1) | — |
   | C(10) | | | Richert, r < 10.44 |
   So the model bound improves **10 → 6, with margin surviving any inflation of the switched constants up to 2.35**,
   and **→ 4 only on a knife-edge** (needs the switched constants within ≈ 10 % of the model).
3. **Conditional theorem (§2.3).** **Theorem K6:** C(6) holds, CONDITIONAL on **Hypothesis MT** (remainder control
   by BV-type theorems for the structured switched sets, and upper bounds whose main terms are at most 2.35 × the
   model values) and otherwise relative to BV and Nath–Xie's vector sieve. The numerical inequality is a
   deterministic floating-point computation with grid-refined masses and an explicit tail bound (not
   interval-certified). Not an unconditional explicit constant: MT is the "constant audit" P415 flagged as missing,
   *plus* the convolution remainder input.
4. **Additive weights (§1, EVIDENCE).** The tested finite LPs (piecewise-constant w ≥ 0, conservative covering
   constraints, finite parameter grids) return Richert's linear weight and, under P415's T₁ convention (cap a ≤ θ₁),
   no C(8) witness; with the cap removed (§2.2(iii)) the same weights give a knife-edge C(8) witness (+0.018). This is
   evidence, not a theorem about all additive weights.
5. **Level ledger (§5; grid witnesses, not barriers).** C(4): BV (thin), comfortable from 0.55. **C(2) — the Chen
   analogue: positive witnesses at θ = 0.68 with BV-level switching and θ = 0.65 with switched sums at level θ**
   (grid crossings ≈ 0.675 / ≈ 0.645). Lichtman's 66/107 = 0.617 would not suffice on the tested grids even if it
   applied (it does not as stated, §5.2). **C(0): no witness found on the tested grids through θ = 1**; the best
   recorded model witness for K(4) remains P415's product-linear-sieve ≈ 0.996.
6. **PROVED side lemma (§3.1):** the semi-linear upper function at s = 2 equals the Landau-type density of S exactly,
   C_S = (A/2)·c_W = (∏_{q∈𝒬}(1 − q^{−2})/8)^{1/2} — the normalisation of all "truth" masses in the model.

**Bottom line (Assessment).** In the P415 model, switching away the many-factor configurations of 4p + 1 — a use of
Chen's switching on the *second* shift that P415 and Nath–Xie did not make — lowers the 𝒬-anatomy deficit of
4p + 1 from ≤ 10 to ≤ 6 with a margin that survives a 2.35-fold inflation of every switched constant, and to ≤ 4 only
on a knife-edge, at BV level. The Chen analogue C(2) needs level ≈ 0.65–0.68 in the tested implementations, and K(4)
itself is untouched (≈ 0.996). PROVED: Lemma D and the normalisation lemma; Theorem K6 is CONDITIONAL on MT; all
numbers are model-level. No step toward ES.

## 0.1 Statements attacked; why not already closed

* C(r) for r = 8, 6, 4, 2, 0 as above; grid witnesses for C(r) at level θ (primes in the CRT classes of
  (p + 4)(4p + 1)) with switched sums at level 1/2 or θ.
* Not closed: P415 proved only "bounded" (δ unspecified) and gave a Richert-weight model number 10; no weight
  optimisation, no switching on N₂, no ledger for r ≥ 2. Nath–Xie (arXiv:2501.16723 v2, Thm 1.1: Ω(p + 2) ≤ 11 for
  primes p = m² + n² + 1; §5 parameters θ₂ = 0.011, θ = 0.23, λ = 0.14; BV level; Richert weights; Remark 1.1: Ω ≤ 3
  under EH — `data/z56/k4chen/lit_report.md`, VERIFIED) is the closest precedent located; it also uses Richert
  weights on the second shift and switching only for the half-dimensional shift. (Coverage-limited comparison, not a
  novelty claim.)

## 1. First falsifier: finite LPs over additive weights (EVIDENCE, grid-limited)

`scripts/z56_k4chen_lp.py`. Weighted sum Σ_{p: (N₁,𝒬(z₁))=(N₂,𝒬(z₂))=1} (1 − Σ_{q|N₂, q∈𝒬, q≥z₂} w(log q/log x)) with
w ≥ 0 piecewise constant on cells of width h, zero from α_max = 0.48 on. Cost (P415 §1.4 model):
½∫ w(α)U(1/2 − α)dα/α, U(λ) = min_{t₁θ₁+t₂ζ=λ} F(t₁)F(t₂). Constraint (parity): every multiset of r + 2 numbers
α_i ≥ ζ (left cell endpoints, conservative) with Σα_i ≤ 1 has Σw(α_i) ≥ 1 — then W > 0 forces Ω_𝒬(N₂) ≤ r for
𝒬-squarefree N₂ (repeated 𝒬-primes ≥ z₂ are O(x^{1−ζ}) exceptions). Solved by cutting planes with a knapsack
separation oracle (DP; checked against exhaustive enumeration on 200 random small instances by the internal review);
the final w is re-checked by the oracle and rescaled (homogeneous constraints), so every reported cost is feasible
(numerical LP tolerances, not a formal certificate).
* Margin = fvec − T₁ − cost with P415's capped T₁: r = 10: +0.046 (θ₁ = 0.42, ζ = 0.008); r = 8: best −0.019
  (θ₁ = 0.42, ζ = 0.008, h = 0.002) over θ₁ ∈ {0.41, 0.42, 0.43} × ζ ∈ {0.006, 0.008, 0.01}; the r = 8 cost
  converges in h (0.3035, 0.3022, 0.3015 at h = 0.004, 0.002, 0.001). `data/z56/k4chen/lp_bv.txt`.
* The returned w is linear: max(0, 0.14237 − 0.42373α) at h = 0.002 (y = 0.336) — Richert's weight.
* With the cap removed: r = 8 margin +0.018 (θ₁ = 0.40, ζ = 0.008; T₁ = 0.264 instead of 0.314;
  `lp_nocap.txt`) — a knife-edge, far below the switching margins of §4.
Reading: on the tested discretisations, additive weights reproduce P415 and reach C(8) at best marginally. (Heuristic
reason: configurations of r + 1 tiny factors plus one huge one force w(ζ) ≳ 1/(r + 1), and the cost ½∫_ζ w/α then
grows like log(1/ζ)/r.)

## 2. The switching scheme

### 2.1 Lemma D (PROVED; exact reduction)

Let x be large, θ₁ ∈ (1/4, 1/2), ζ ∈ (0, 1/4), r ≥ 0 even, k = r + 2, τ ≥ 0. Put
* S(z₁, z₂) = #{p ∈ 𝒜 : (N₁, 𝒬(z₁)) = (N₂, 𝒬(z₂)) = 1};
* T₁ = #{p ∈ 𝒜 : (N₁, 𝒬(z₁)) = 1, N₁ ∉ S, (N₂, 𝒬(z₂)) = 1};
* T^dir(τ) = Σ_{Q} #{p ∈ 𝒜 : Q | N₂, (N₁, 𝒬(z₁)) = 1, (N₂/Q, 𝒬(z₂)) = 1}, Q over products of k − 1 distinct
  𝒬-primes ≥ z₂ with Q ≤ x^τ;
* 𝒩_k(τ) = {n : (n, 𝒬(z₂)) = 1, n 𝒬-squarefree, Ω_𝒬(n) ≥ k, product of its k − 1 smallest 𝒬-factors > x^τ},
  T^sw(τ) = #{p ∈ 𝒜 : N₁ ∈ S, N₂ ∈ 𝒩_k(τ)};
* E = #{p ∈ 𝒜 : q² | N₂ for some q ∈ 𝒬, q ≥ z₂}.
Then
  #{p ∈ 𝒜 : N₁ ∈ S, Ω_𝒬(N₂) ≤ r} ≥ S(z₁, z₂) − T₁ − T^dir(τ) − T^sw(τ) − E,   E ≪ x^{1−ζ}.

*Proof.* Let p be counted in S(z₁, z₂) but not on the left. Since (N₂, 𝒬(z₂)) = 1, every 𝒬-factor of N₂ is ≥ z₂,
so "not on the left" means N₁ ∉ S or Ω_𝒬(N₂) ≥ r + 1, i.e. ≥ k (even). If N₁ ∉ S, p is counted in T₁. Otherwise
N₁ ∈ S and Ω_𝒬(N₂) ≥ k. If N₂ is not 𝒬-squarefree, p is counted in E. Otherwise let q₁ < … < q_j (j ≥ k) be the
𝒬-factors and Q = q₁⋯q_{k−1}. If Q ≤ x^τ, then Q | N₂, N₂/Q is free of 𝒬-primes < z₂ (its 𝒬-factors are
q_k, …, q_j ≥ z₂) and (N₁, 𝒬(z₁)) = 1, so p is counted in the Q-term of T^dir. If Q > x^τ, N₂ ∈ 𝒩_k(τ) and p is
counted in T^sw. Hence S(z₁,z₂) ≤ LHS + T₁ + T^dir + T^sw + E. Finally E ≤ Σ_{z₂≤q≤√(4x+1)} (4x/q² + 1) ≪ x^{1−ζ}
(as ζ < 1/2). ∎

*Remarks.* (i) In T^dir the 𝒬-parity of N₂/Q (N₂ ≡ 1 and Q ≡ 3 (mod 4) as k − 1 is odd, so N₂/Q ≡ 3 (mod 4)) makes
"N₂/Q has a further 𝒬-factor" automatic: an *upper* sieve that only asks (N₂/Q, 𝒬(z₂)) = 1 already lives on
configurations with ≥ k factors (the further factor may repeat one of Q — such p are in E anyway). This is why
products Q of k − 1 primes (not single primes, as in Richert's weights) can be used. (ii) By P415 Step 1, since
z₁⁴ > x + 4, N₁ ∉ S in T₁ means N₁ = m q q′ with m ∈ S, q, q′ ∈ 𝒬, q, q′ ≥ z₁ (q = q′ allowed; these contribute
O(x^{1−θ₁} + √x) = o(𝒰), after which T₁ is ½ × the count over ordered pairs q ≠ q′). (iii) τ is arbitrary; only the
analytic bound (ii) of §2.2 needs τ < θ − ε (θ the level).

### 2.2 The four asymptotic bounds (status of each)

Fix ε > 0 small, s₁, s₂ ≥ 1 with θ₁s₁ + ζs₂ = 1/2 − ε, and a + b = 1/2 − ε for each switched sum.

(i) **Main term (PROVED relative to BV and Nath–Xie Prop. 3.10; = P415 Step 2):**
S(z₁, z₂) ≥ (fvec(s₁, s₂) − o(1))𝒰, fvec = f(s₁)F(s₂) + F(s₁)f(s₂) − F(s₁)F(s₂).

(ii) **Direct term (part of Hypothesis MT):** for each Q the count is primes p ≡ −4̄ (mod Q) with N₁ sifted by
𝒬-primes < z₁ and N₂/Q by 𝒬-primes < z₂ (total moduli Q·d₁d₂ ≤ x^{1/2−ε}; BV summed over Q and the sieve moduli
with divisor weights); the product of two beta upper sieves gives
T^dir(τ) ≤ (D(τ) + o(1))𝒰, D(τ) = (1/((k−1)! 2^{k−1})) ∫_{α_i ≥ ζ, Σα_i ≤ τ} U(1/2 − Σα_i) ∏dα_i/α_i
(an unordered product of k − 1 primes is counted (k − 1)! times by the ordered integral; each 𝒬-prime has density
½ dα/α; 1/φ(Q) ~ 1/Q; at q | Q the N₁-sieve density changes from 1/(q − 1) to 0, a factor 1 + O(1/q)). This is the
same evaluation P415 uses for its Richert terms (Nath–Xie-type upper vector sieve).

(iii) **T₁ (part of Hypothesis MT; P415 model):** T₁ ≤ (pen·(2/a)F(b/ζ)B(θ₁) + o(1))𝒰, B(θ) = F(1/θ) − F(1)√θ
(the two-𝒬-factor Buchstab mass of N₁; P415 §1.4 check). Switched variable n = N₁ = mqq′ (½ × ordered pairs
q ≠ q′ ≥ z₁, no cross-condition), sieve n − 4 for primality (linear upper sieve, level x^a, loss 2/a) and 4n − 15 for
𝒬-primes < z₂ (semi-linear upper sieve, level x^b). *Cap removal (justified at the main-term level, conditional on
the remainder input):* P415 also imposed a ≤ θ₁. The linear upper sieve's main term V(D^{1/s})F_lin(s) ~ 2/log D is
the same for every 0 < s ≤ 3, so one may sift only below x^{a/3} < z₁, and both convolution factors (q′ ≥ x^{θ₁},
mq ≥ x^{θ₁}) are power-sized; no reason for the cap remains at BV level. (At general switched levels keep a/3 < θ₁.)
With the cap the pure-switching C(4) margin is −0.016 instead of +0.020 (§4).

(iv) **T^sw (part of Hypothesis MT; Chen-type switching on N₂):** switched variable n = N₂ ∈ 𝒩_k(τ), n ≡ 5
(mod 32); sieve (n − 1)/4 for primality (linear, level x^a, loss 2/a relative to the reference density 2/log x of the
odd number (n − 1)/4) and (n + 15)/4 for 𝒬-primes (semi-linear upper sieve at level x^b: for b ≤ 2θ′ one has
F(b/θ′)W(x^{θ′}) = 2A√(θ₁/b)·W(z₁)(1 + o(1)) independently of θ′, i.e. b^{−1/2} × the S-density F(1)√θ₁·W(z₁) of
§3.1). Hence
T^sw(τ) ≤ (pen·L·F(1)√θ₁·Unc(τ) + o(1))𝒰, L = min_{a+b=λ}(2/a)b^{−1/2} = 3√3·λ^{−3/2} (a = 2λ/3), = 6^{3/2} = 14.697
at λ = 1/2 (14.741 at λ = 1/2 − 10⁻³);
Unc(τ) = Σ_{j≥k, j even} (1/(2^j j!)) ∫_{α_i≥ζ, Σα_i≤1, σ_{k−1}(α)>τ} F(1)√(ζ/(1 − Σα_i)) ∏_{i≤j} dα_i/α_i,
σ_{k−1} = sum of the k − 1 smallest α_i. 2-adic bookkeeping: x/8 + O(1) values n ≤ 4x + 1 in the class 5 (mod 32),
times 2/log x, gives X ~ x/(4 log x). Local check (internal review #8): at q ∈ 𝒬, q ≥ 7, starting from n 𝒬-rough, the
two forbidden residues give survival (q − 3)/(q − 1), reproducing 𝔊; at q = 3 the coincident root gives 9/8;
split-prime marginals of the S-part have divisibility probability 1/ℓ. These checks support pen = 1 locally.

**Hypothesis MT.** For the parameters used, T₁, T^dir(τ), T^sw(τ) are bounded above by pen × (the main terms in
(ii)–(iv)) + o(𝒰), with some pen ≤ 2.35. This contains two genuinely unproved inputs: (a) *remainder control* — a
Bombieri–Vinogradov theorem at level x^{1/2−ε} for the switched structured sets with the sieve coefficients
(for 𝒩_k(τ), take the largest 𝒬-prime as the Siegel–Walfisz factor: for j ≥ k ≥ 2 it lies in
[x^ζ, O(x^{1−(k−1)ζ})], so both factors are power-sized; its fixed residue mod 4 must be split off explicitly — note
1_S itself is supported on 1 mod 4, so "SW for the S-part" in the naive sense is false; ordered-factor and
product constraints need the usual dyadic/Perron separation); (b) *main-term evaluation* — Selberg–Delange
asymptotics uniform in the sieve moduli, and local-factor averaging. **pen = 1 is the locally consistent candidate,
not established here.** P415's pen = 2.35 is Nath–Xie's *majorised* constant for their problem, not an evaluation.

### 2.3 Conditional theorem

**Theorem K6 (CONDITIONAL on Hypothesis MT; otherwise relative to BV and Nath–Xie Prop. 3.10).** C(6) holds:
≫ x/(log x)² primes p ≤ x, p ≡ 1 (8), have p + 4 ∈ S and Ω_𝒬(4p + 1) ≤ 6.
*Proof.* Lemma D with τ = 0 (so T^dir = 0, pure switching), ε = 10⁻³, θ₁ = 0.45, ζ = 0.008, s₁ = 1.058539,
s₂ = 2.832187 (θ₁s₁ + ζs₂ = 0.499), a + b = 0.499. By (i) S ≥ (0.33513 − o(1))𝒰; by MT with pen = 2.35,
T₁ ≤ (0.22094 + o(1))𝒰 and T^sw(0) ≤ (2.35·14.7411·F(1)√0.45·M + o(1))𝒰 = (0.07700 + o(1))𝒰, where
M = Σ_{j≥8 even} d_j(1) at ζ = 0.008 is taken as the largest of the grid values 2.2002·10⁻³ (n = 2000), 2.1974·10⁻³
(4000), 2.1959·10⁻³ (8000), with the j ≥ 27 tail bounded by Σ_j F(1)ζ^{−1/2}(log(1/ζ)/2)^{j−1}/j! = 1.5·10⁻¹⁷ (included).
Margin 0.33513 − 0.22094 − 0.07700 = +0.0372 > 0 (`z56_k4chen_k6.py`, `data/z56/k4chen/k6_witness.txt`;
floating point, sieve functions from the P415 DDE solver with step 10⁻⁴, whose errors are ≲ 10⁻⁷ per the internal
review's independent quadrature; not interval-certified). As 𝒰 ≫ x/(log x)², the count is ≫ x/(log x)². ∎
*Not claimed:* C(4) (margins +0.047 MC / +0.0135 deterministic at pen = 1 vanish by pen = 1.2).

## 3. Masses (the "truth" side of the model)

### 3.1 Normalisation lemma (PROVED)

Let C_S = lim y^{−1}√(log y)·#{n ≤ y : n ∈ S} and c_W = lim √(log z)·W(z). Then C_S = (A/2)c_W, i.e.
#{n ≤ y : n ∈ S} ~ (y/4)·W(√y)·F(2): the semi-linear upper sieve is asymptotically exact for S at s = 2.
*Proof.* Σ_{n∈S} n^{−s} = ∏_{p≡1(4)}(1 − p^{−s})^{−1} = [ζ(s)L(s,χ₋₄)(1 − 2^{−s})∏_{q∈𝒬}(1 − q^{−2s})]^{1/2}, so by
Selberg–Delange C_S = [L(1,χ₋₄)·½·P]^{1/2}/Γ(1/2) = (P/8)^{1/2}, P := ∏_{q∈𝒬}(1 − q^{−2}). On the other side
∏_{q<z}(1 − 1/q)² = ∏_{q<z}(1 − 1/q)(1 + 1/q)^{−1}·∏_{q<z}(1 − q^{−2}) = [∏_{2<p<z}(1 − 1/p)(1 − χ₋₄(p)/p)^{−1}]·
∏_{q<z}(1 − q^{−2}) ~ (2e^{−γ}/log z)(π/4)P (Mertens; L(1,χ₋₄) = π/4), so c_W = (πe^{−γ}P/2)^{1/2} and
(A/2)c_W = ½(e^γ/π)^{1/2}(πe^{−γ}P/2)^{1/2} = (P/8)^{1/2}. Finally (y/4)W(√y)F(2) ~ (y/4)c_W√2(log y)^{−1/2}·2A/√2
= (A/2)c_W·y(log y)^{−1/2}. ∎
(Every n ≡ 1 (4) with no 𝒬-prime below √y lies in S by parity; this is the classical extremality of the
parity-restricted integer sequence for F — not a statement about arbitrary half-dimensional sequences. P415's check
B(θ) = (F(1)/4)√θ·C(θ) is the two-factor version.)

### 3.2 Configuration masses

For the integers n ≡ 1 (4) of size x^u free of 𝒬-primes below z₂ = x^ζ, the density (relative to n ≡ 1 (4), in
units W(z₂)) of those with exactly j 𝒬-factors (j even) is d_j(u): d₀(u) = F(1)√(ζ/u) (§3.1 at scale u), and
d_j(u) = (1/(2j))∫_ζ^u d_{j−1}(u − α)dα/α (each 𝒬-prime has density ½ dα/α; removing one of j factors). Odd j are
auxiliary masses (integers ≡ 3 (4)), used only inside the recursion. `z56_k4chen_mass.py` (grid aligned with ζ,
h = ζ/m — the internal review found that an earlier non-aligned grid dropped a partial cell; fixed) gives
Σ_{j even} d_j(1) = F(1/ζ) to ≤ 5·10⁻⁵ at ζ = 0.1, 0.03, 0.008, 0.00601, 0.00667 (2.7·10⁻⁴ at 0.00201 with jmax 14).
Values of d_j(1):

| ζ | j = 0 | 2 | 4 | 6 | 8 | 10 |
|---|---|---|---|---|---|---|
| 0.1 | 0.476 | 0.507 | 1.73e−2 | 3.2e−5 | 7e−10 | 0 |
| 0.03 | 0.261 | 0.617 | 0.117 | 5.1e−3 | 7.4e−5 | 4.1e−7 |
| 0.008 | 0.135 | 0.567 | 0.261 | 3.6e−2 | 2.1e−3 | 6.5e−5 |

The factorial coefficients 1/(2^j j!) give Poisson-like suppression of the tail Σ_{j≥k} d_j in the tested range (not
an asymptotic claim). Tail bound used for omitted j: d_j(1) ≤ F(1)ζ^{−1/2}(log(1/ζ)/2)^{j−1}/j! (last factor:
∫_ζ^H (H − a)^{−1/2}da/a ≤ 2/ζ; others ≤ log(1/ζ) each). Monte-Carlo Unc(τ) (`z56_k4chen_direct.py`: j − 1
log-uniform factors, last factor integrated analytically, ∫_l^H (H − a)^{−1/2}da/a = 2 atanh(√(1 − l/H))/√H,
l = max(ζ, τ − S_{k−2})) agrees with the grid at τ = 0 to ≤ 1 % (ζ = 0.01, k = 6: 0.029661 vs 0.029871; ζ = 0.03,
k = 4: 0.12264 vs 0.12242; ζ = 0.006, k = 8: 3.558e−3 vs 3.534e−3; NS = 60000).

## 4. Results at BV level (Assessment: model numerics)

**Direct + switching** (`z56_k4chen_direct.py`, grid θ₁ ∈ {0.36,…,0.46} × ζ × τ ∈ {0, 0.01, …}, MC with NS = 40000
samples, sampling error ≈ 1–3 % of D and K·Unc per the internal review; files
`data/z56/k4chen/direct_r*_th0.5_sw0.5_pen*.txt`; s₁, s₂ at ε = 0). pen multiplies T₁ and K·Unc, not D:

| r | pen | margin | θ₁ | ζ | s₁ | s₂ | τ | main | T₁ | D | K·Unc |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | 1 | +0.366 | 0.42 | 0.002 | 1.174 | 3.438 | 0.22 | 0.562 | 0.182 | 0.001 | 0.013 |
| 8 | 2.35 | +0.204 | 0.46 | 0.002 | 1.072 | 3.375 | 0.43 | 0.384 | 0.152 | 0.010 | 0.018 |
| 6 | 1 | +0.291 | 0.40 | 0.006 | 1.203 | 3.154 | 0.36 | 0.594 | 0.261 | 0.010 | 0.033 |
| 6 | 1.5 | +0.186 | 0.44 | 0.006 | 1.095 | 3.025 | 0.42 | 0.429 | 0.183 | 0.019 | 0.041 |
| 6 | 2.35 | +0.071 | 0.46 | 0.006 | 1.049 | 2.913 | 0.45 | 0.311 | 0.156 | 0.026 | 0.058 |
| 4 | 1 | +0.047 | 0.38 | 0.02 | 1.174 | 2.688 | 0.42 | 0.543 | 0.371 | 0.035 | 0.091 |
| 4 | 1.1 | +0.006 | 0.40 | 0.02 | 1.12 | 2.6 | 0.43 | 0.454 | 0.311 | 0.040 | 0.098 |
| 4 | 1.2 | −0.031 | 0.40 | 0.02 | 1.12 | 2.6 | 0.43 | 0.454 | 0.339 | 0.040 | 0.107 |

(With D also inflated by 2.35, the r = 6, pen 2.35 row gives ≈ +0.036.)
**Pure switching, deterministic** (`z56_k4chen_k6.py`, τ = 0, ε = 10⁻³, grid masses n ≤ 8000 + tail bound;
`k6_witness.txt`, `k6_scan.txt`): r = 6: +0.0372 (pen 2.35; θ₁ = 0.45, ζ = 0.008), +0.163 (pen 1.5), +0.278 (pen 1);
r = 4: +0.0135 (pen 1; θ₁ = 0.39, ζ = 0.02); r = 8: +0.189 (pen 2.35).
**Pure switching, continuous optimiser** (`z56_k4chen_opt.py`, Nelder–Mead, corrected masses, ε = 0;
`opt_r*_pen*.txt`): r = 8: +0.367 (pen 1), +0.198 (2.35); r = 6: +0.286, +0.044; r = 4: +0.020 (−0.016 with P415's
cap, `opt_r4_pen1.0_cap.txt`); r = 2: −1.03.
**Weights + switching** (`z56_k4chen_mixed.py`, Richert/Kuhn families λ ∈ {0.05,…,0.5}, y ∈ {0.1,…,0.4},
`mixed_r4.txt`): at r = 4 no tested weight improved on pure switching (best +0.017 on that grid). Restricted to
those families and samples.
Reading: the switched bad-configuration cost K·Unc is ≈ 2–22 % of the main term; what limits r is the exact-N₁
machinery (main − T₁ ≈ 0.15–0.38 against the "truth" F(1)√θ₁ ≈ 0.93–1.02, efficiency ≈ 15–39 %).

## 5. Level ledger (grid witnesses; Assessment, model, pen = 1)

Main/direct sums at level θ; switched sums at 1/2 ("BV") or θ ("same" — needs an additional GEH/convolution-type
input, distinct from ordinary EH(θ)). `z56_k4chen_ledger.py`, `data/z56/k4chen/ledger2/` (computed with the earlier
quadrature version of `direct.py`, which agrees with the current analytic version to ≈ 1–3 %; τ up to θ − 0.02,
allowed by Lemma D(iii)).

| θ | C(4) BV / same | C(2) BV / same | C(0) BV / same |
|---|---|---|---|
| 0.5 | +0.046 / +0.046 | −0.885 / −0.885 | −2.66 / −2.66 |
| 0.55 | +0.227 / +0.258 | −0.602 / −0.491 | −2.27 / −2.14 |
| 4/7 | +0.289 / +0.332 | −0.474 / −0.354 | −2.13 / −1.96 |
| 0.6 | +0.373 / +0.412 | −0.332 / −0.186 | −1.94 / −1.76 |
| 66/107 | +0.415 / +0.455 | −0.246 / −0.104 | −1.85 / −1.65 |
| 0.64 | | −0.144 / −0.004 | |
| 0.65 | | −0.101 / +0.038 | |
| 0.67 | | −0.017 / +0.113 | |
| 0.68 | | +0.023 / +0.148 | |
| 0.7 | | +0.094 / +0.210 | −1.43 / −1.24 |
| 0.8 | | +0.386 / +0.464 | −1.05 / −0.87 |
| 1.0 | | +0.699 / +0.729 | −0.43 / −0.30 |

* **C(2): positive witnesses at θ = 0.68 (BV switching) and θ = 0.65 (switching at θ)**; grid crossings ≈ 0.675 /
  ≈ 0.645 (interpolated, not minimal levels). Negative entries are grid failures, not barriers.
* **C(0): no witness found on the tested grids through θ = 1** (C(0) here needs the direct term with single primes,
  D ≈ 0.9–1.9, which is expensive). The best recorded model witness for K(4) remains P415 §2(b) (product linear sieve +
  switching, ≈ 0.996 under ordinary EH with BV switching).
* Hypothetical switched level 4/7 with θ = 1/2 (no source supplies this for our switched convolutions): C(4) margin
  +0.115 (pen 1, current code), −0.063 (pen 1.5, earlier code).

### 5.2 Which known levels apply (Assessment; literature `data/z56/k4chen/lit_report.md`)

BFI (4/7, well-factorable weights, fixed residue), Maynard II (3/5 triply well-factorable; 7/12 for linear-sieve
upper weights), Lichtman arXiv:2309.08522 (66/107; Thm 1.7 uniform for 0 < |a| < x^ε, triply well-factorable weights)
are statements about **primes**, with **fixed (or small) residues and specific weight structure**. Our main sieve has
residue classes p ≡ −4 (d₁), p ≡ −4̄ (d₂) — CRT-varying, not small — and semi-linear beta weights, for which no
well-factorability result was located. The switched sums run over **structured composite convolutions** (mqq′, or
s·q₁⋯q_j), not primes; their linear sieves have fixed residues (n ≡ 4 (d) in T₁, n ≡ 1 (4d) in T^sw), but they carry
a second, semi-linear sieve with a different residue. So none of these levels is available as stated; the ledger
values > 1/2 are hypotheticals. (66/107 would not reach C(2) on the tested grids even if applicable.)

## 6. FRONTIER §4 hard screens (best item: Lemma D + switching scheme)

1. **T1 squares.** Kill side; the squares satisfy N₁, N₂ ∈ S identically (P415 §5), so Ω_𝒬 bounds are consistent
   with them; no upper-side claim is made.
2. **8/131, 8/241.** The target is the 4-specific line (HCKILL Lemma 1.1); inherited.
3. **Tied modulus.** Not applicable (kill side, fixed character χ₋₄).
4. **Fixed p.** Density statement only; nothing about a prescribed p.

## 7. Proposed FRONTIER §7.2 text (do not edit FRONTIER here)

> *(z56, `Z56_K4CHEN.md`; kill side, model level.)* **Chen-type switching on 4p + 1.** Exact reduction (Lemma D,
> PROVED): the configurations of 4p + 1 with ≥ r + 2 factors ≡ 3 (4) (all ≥ x^ζ) split into a *direct* part
> (product Q of the r + 1 smallest ≤ x^τ; 𝒬-parity forces the extra factor) and a *switched* part (Chen switching with
> 4p + 1 as the variable); their Buchstab mass is small (factorial suppression). In the P415 model the deficit improves
> from Ω_𝒬(4p + 1) ≤ 10 to **≤ 6** (margin survives a 2.35-fold inflation of all switched constants) and to **≤ 4 on
> a knife-edge** (pen ≤ 1.1), at BV level; the tested finite LPs over additive weights return Richert's weight and reach
> ≤ 8 at best marginally. **Theorem K6** (C(6)) is CONDITIONAL on Hypothesis MT (BV-type remainder control for the
> structured switched sets + switched main terms ≤ 2.35 × model). **Grid witnesses** (not barriers): C(2) (the Chen
> analogue) at level 0.68 (0.65 with switched sums at the same level); no C(0) = K(4)-type witness through level 1 in
> this scheme — P415's ≈ 0.996 stands. Known beyond-1/2 levels (BFI, Maynard, Lichtman) do not apply as stated
> (CRT-varying residues, semi-linear weights, composite switched sequences).

## 8. Reproduction (all under `timeout ≤ 1800`, `ulimit -v 4000000–6000000`, `uv run --with numpy --with scipy`)

* LP: `python scripts/z56_k4chen_lp.py demo` (and the inline runs recorded in `lp_bv.txt`, `lp_nocap.txt`).
* Masses: `python scripts/z56_k4chen_mass.py 0.1 0.03 0.008` (§3.2 table and Σ_even check).
* K6 witness: `python scripts/z56_k4chen_k6.py` → `k6_witness.txt` (≈ 10 min).
* Pure switching: `python scripts/z56_k4chen_switch.py 8,6,4 0.5 0.5 1.0` (grid) → `switch_bv.txt`;
  `python scripts/z56_k4chen_opt.py r θ λ pen` (continuous; `K4CAP=1` restores P415's cap) → `opt_r*.txt`.
* Direct + switching: `K4ZETA=… K4TH1=… K4NS=40000 python scripts/z56_k4chen_direct.py r θ λ pen` → `direct_*.txt`
  (files in `old_quadrature/` are the pre-review version, kept for the record).
* Ledger: `K4NS=20000 python scripts/z56_k4chen_ledger.py r bv|same θ-list` → `ledger2/`.
* Weights + switching and MC validation: `python scripts/z56_k4chen_mixed.py validate | r θ λ pen`.
All scripts default to the uncapped T₁ (`K4CAP=1` for P415's convention); sieve functions from
`scripts/z55_p415_sieve.py` (F, f by the delay-differential system, step 10⁻⁴).

## 9. Review log

* **Internal hostile review** (deep-mode subagent; `data/z56/k4chen/internal_review.md`): MAJOR REVISION, no FATAL;
  Lemma D, the normalisation lemma, D(τ)'s normalisation, the switched loss L and 2-adic bookkeeping, the cap removal
  (main-term level), the MC prefactors and order statistic, the LP oracle and the §3.2 table confirmed; required
  runs reproduced. Fixes applied: (1) **mass-grid bug** (non-aligned cutoff cell, exploited by the optimiser) fixed
  in `z56_k4chen_mass.py`; all pure-switching numbers recomputed (old file removed); cache keys include the
  truncation order; (2) Theorem K6 now rests on a deterministic pure-switching witness with explicit level slack
  ε = 10⁻³, grid-refined masses and a tail bound (+0.0372 at pen 2.35), labelled floating point, not
  interval-certified; MC error statements corrected (≈ 1–3 %); (3) Hypothesis MT restated to include the
  convolution remainder input and the uniform main-term evaluation; "pen = 1 standard" → "locally consistent
  candidate"; the SW remark for 1_S corrected; (10) odd d_j declared auxiliary, Poisson language weakened; (12) last
  factor of Unc integrated analytically, tail bound added; (14) "additive weights exhausted" → finite-LP evidence,
  §7 now retains the uncapped C(8) LP witness; (16) ledger values stated as grid witnesses / crossings, "fails at
  every level ≤ 1" withdrawn, τ-range of Lemma D extended; (17) cap convention unified (all scripts uncapped by
  default), mixed scan saved; (18) unsupported "Fouvry–Grupp-type" attribution removed, composite switched sequences
  noted; (19) F(1) = 1.5059, C(0) vs P(4,15) wording, percentage ranges corrected; Lemma D diagonal q = q′ noted.
