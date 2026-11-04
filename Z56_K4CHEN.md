# Z56_K4CHEN — Chen-type switching for K(4): p + 4 ∈ S exactly, few 𝒬-factors in 4p + 1

**ES is OPEN.** Nothing here proves or disproves it. All results are internal (internally reviewed only).
Lane K4CHEN (wave z56). Scripts `scripts/z56_k4chen_*`, data `data/z56/k4chen/`.

Notation (as in `Z55_P415.md`): 𝒬 = primes ≡ 3 (mod 4), 𝒬(z) = ∏_{q∈𝒬, q<z} q; S = {n ≥ 1 : every prime factor
≡ 1 (mod 4)}; N₁ = p + 4, N₂ = 4p + 1; Ω_𝒬(n) = number of 𝒬-prime factors of n with multiplicity (always even for
n ≡ 1 (4)); 𝒜 = {p ≤ x prime, p ≡ 1 (8)}, X = li(x)/4; W(z) = ∏_{q∈𝒬,q<z}(1 − 1/q); F, f = semi-linear (κ = 1/2,
β = 1) beta-sieve functions, A := (e^γ/π)^{1/2}, F(s) = 2A s^{−1/2} (0 < s ≤ 2), F(1) = 2A = 1.5056;
𝔊 = (9/8)∏_{q∈𝒬,q≥7} q²(q − 3)/(q − 1)³ (P415 Step 2). z₁ = x^{θ₁}, z₂ = x^ζ. **Unit 𝒰 := 𝔊·X·W(z₁)·W(z₂) ≍
x/(log x)²**; all "margins" below are in units of 𝒰.

## 0. Verdict: **strengthened (model level) + narrowed** — new mechanism; C(6) at BV level robustly in the model

Target family **C(r)** (r even): ≫ x/(log x)² primes p ≤ x, p ≡ 1 (8), with p + 4 ∈ S and Ω_𝒬(4p + 1) ≤ r.
C(0) = P(4,15) = K(4) (HCKILL Lemma 1.1). P415 Theorem U = C(r₀) for an unspecified r₀; its model gave r = 10.

1. **New mechanism (§2): Chen-type switching on the many-factor configurations of 4p + 1**, combined with a *direct*
   upper sieve that uses the 𝒬-parity of N₂/Q to force "one more 𝒬-factor" for free. The bad set
   {Ω_𝒬(N₂) ≥ r + 2, all 𝒬-factors ≥ x^ζ} has Buchstab mass decaying like (½ log 1/ζ)^{r+2}/(r+2)! (Poisson-type,
   §3), so switching it away costs only a bounded loss factor (2/a)(1/√b) ≈ 14.7 times a tiny mass — whereas any
   additive weight (Richert, Kuhn, or the LP-optimal one) pays ≍ log(1/ζ)/r. Exact combinatorial reduction:
   **Lemma D (PROVED)**.
2. **Model numerics (Assessment; §4)**, same model conventions as P415 §1.4 (pen = 1 = standard asymptotic evaluation
   of switched main terms), BV level 1/2 everywhere:
   | target | best margin (pen 1) | robustness | P415 model |
   |---|---|---|---|
   | C(8) | +0.37 | +0.20 at pen 2.35 | — |
   | **C(6)** | **+0.29** | **+0.19 at pen 1.5, +0.07 at pen 2.35** | — |
   | C(4) | +0.045 | +0.004 at pen 1.1; **fails** at pen 1.2 (knife-edge) | — |
   | C(10) | — | — | Richert, r < 10.44 |
   So the model bound improves **10 → 6 robustly** (any switched-constant inflation up to the P415 illustrative
   multiplier 2.35 is absorbed) and **→ 4 only in the exact pen = 1 model** (needs the switched constants within 10 %).
3. **Conditional theorem (§2.3).** C(6) holds **CONDITIONAL on Hypothesis MT** (the asymptotic main terms of the
   upper/switched sieves equal the stated model values up to a factor ≤ 2.35 for switched sums and ≤ 1 + o(1) for
   unswitched vector upper sieves; this is the standard Chen-type evaluation, not written out here) and otherwise
   relative only to BV, Nath–Xie's vector sieve and Bombieri–Vinogradov for convolutions. Not a PROVED explicit
   constant: Hypothesis MT is exactly the "constant audit" P415 flagged as missing.
4. **Additive weights are exhausted (§1, EVIDENCE/Assessment).** An LP over *all* additive weights w ≥ 0 with the
   parity covering constraint reproduces P415's Richert number (C(10) yes, C(8) no at BV; the optimum *is* a Richert
   linear weight). Improvements must come from switching/products, as in item 1.
5. **Level ledger (§5; best sufficient levels found on grids, not barriers).** C(4): BV (thin), ≥ 0.55 comfortable;
   **C(2) — the Chen analogue: level ≈ 0.675 with BV-level switching, ≈ 0.645 if the switched sums also have that
   level** (grid between 0.67/0.68 resp. 0.64/0.65); Lichtman's 66/107 = 0.617 does not suffice even if it were
   applicable (it is not: §5.2). **C(0) = K(4): this scheme fails at every level ≤ 1**; the best sufficient level
   found remains P415's product-linear-sieve value ≈ 0.996 (ordinary EH, BV switching).
6. **PROVED side lemma (§3.1):** the semi-linear upper function at s = 2 equals the Landau-type density of S exactly,
   C_S = (A/2)·c_W = (∏_{q∈𝒬}(1 − q^{−2})/8)^{1/2} — the normalisation on which all "truth" masses of the model rest.

**Bottom line (Assessment).** In the P415 model, the 𝒬-anatomy deficit of 4p + 1 drops from ≤ 10 to ≤ 6 robustly
and to ≤ 4 on a knife-edge, at BV level, by switching away the many-factor configurations of 4p + 1 (a Chen-type use
of switching on the *second* shift that P415/Nath–Xie did not make). The Chen analogue C(2) needs level ≈ 0.65–0.68
and K(4) itself is untouched (≈ 0.996). Everything numerical is model-level; the only PROVED items are the exact
reduction (Lemma D), the normalisation lemma and the (P415) qualitative Theorem U. No step toward ES.

## 0.1 Statements attacked; why not already closed

* C(r) for r = 8, 6, 4, 2, 0 as above; the ledger L(r) = smallest level θ (primes in the CRT classes of
  (p + 4)(4p + 1); switched sums at level 1/2 or θ) for which the model proves C(r).
* Not closed: P415 proved only "bounded" (δ unspecified) and gave a Richert-weight model number 10; no weight
  optimisation, no switching on N₂, no ledger for r ≥ 2. Nath–Xie (arXiv:2501.16723 v2, Thm 1.1: Ω(p + 2) ≤ 11 for
  primes p = m² + n² + 1; §5 parameters θ₂ = 0.011, θ = 0.23, λ = 0.14; BV level; Richert weights; Remark 1.1: Ω ≤ 3
  under EH — `data/z56/k4chen/lit_report.md`, VERIFIED) is the closest precedent; it also uses Richert weights on the
  second shift and switching only for the half-dimensional shift.

## 1. First falsifier: the LP over additive weights (EVIDENCE, grid-limited)

`scripts/z56_k4chen_lp.py`. Weighted sum Σ_{p: (N₁,𝒬(z₁))=(N₂,𝒬(z₂))=1} (1 − Σ_{q|N₂, q∈𝒬, q≥z₂} w(log q/log x)) with
w ≥ 0 piecewise constant on cells of width h, zero from α_max = 0.48 on. Cost (P415 §1.4 model):
½∫ w(α)U(1/2 − α)dα/α, U(λ) = min_{t₁θ₁+t₂ζ=λ} F(t₁)F(t₂). Constraint (parity): every multiset of r + 2 numbers
α_i ≥ ζ (left cell endpoints, conservative) with Σα_i ≤ 1 has Σw(α_i) ≥ 1 — then W > 0 forces Ω_𝒬(N₂) ≤ r (it is
even). Solved by cutting planes with an exact knapsack separation oracle; the final w is re-checked by the oracle
and rescaled (constraints are homogeneous), so every reported cost is feasible.
* Margin = fvec − T₁ − cost: r = 10: +0.046 (θ₁ = 0.42, ζ = 0.008); r = 8: best −0.019 (θ₁ = 0.42, ζ = 0.008,
  h = 0.002) over θ₁ ∈ {0.41, 0.42, 0.43} × ζ ∈ {0.006, 0.008, 0.01}; cost converges in h
  (0.3035, 0.3022, 0.3015 at h = 0.004, 0.002, 0.001). `data/z56/k4chen/lp_bv.txt`.
* The optimal w is linear, w(α) = λ(1 − α/y)₊ with y ≈ 0.34 (r = 8) — Richert's weight.
Reading: additive weights reproduce P415 and cannot reach C(8) in this model. (Why: covering configurations of r + 1
tiny factors plus one huge one forces w(ζ) ≥ 1/(r + 1), and the cost ½∫_ζ w/α grows like log(1/ζ)/r.)

## 2. The switching scheme

### 2.1 Lemma D (PROVED; exact reduction)

Let x be large, θ₁ ∈ (1/4, 1/2), ζ ∈ (0, 1/4), r ≥ 0 even, k = r + 2, τ ∈ [0, 1/2). Put
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
𝒬-factors and Q = q₁⋯q_{k−1}. If Q ≤ x^τ, then Q | N₂ and N₂/Q is free of 𝒬-primes < z₂ (its 𝒬-factors are
q_k, …, q_j ≥ z₂) and (N₁, 𝒬(z₁)) = 1, so p is counted in the Q-term of T^dir. If Q > x^τ, N₂ ∈ 𝒩_k(τ) and p is
counted in T^sw. Hence S(z₁,z₂) ≤ LHS + T₁ + T^dir + T^sw + E. Finally E ≤ Σ_{z₂≤q≤√(4x+1)} (4x/q² + 1) ≪ x^{1−ζ} + √x. ∎

*Remarks.* (i) In T^dir the odd 𝒬-parity of N₂/Q (N₂ ≡ 1, Q ≡ 3 (mod 4) as k − 1 is odd) makes "N₂/Q has a further
𝒬-factor" automatic: an *upper* sieve that only asks (N₂/Q, 𝒬(z₂)) = 1 already lives on configurations with ≥ k
factors. This is why products Q of k − 1 primes (not single primes as in Richert's weights) can be used. (ii) By
P415 Step 1, since z₁⁴ > x + 4, N₁ ∉ S in T₁ means N₁ = m q q′ with m ∈ S, q, q′ ∈ 𝒬, q, q′ ≥ z₁.

### 2.2 The four asymptotic bounds (status of each)

Let ε > 0 be small, s₁, s₂ ≥ 1 with θ₁s₁ + ζs₂ = 1/2 − ε; a + b = 1/2 − ε for each switched sum.

(i) **Main term (PROVED relative to BV and Nath–Xie Prop. 3.10; = P415 Step 2):**
S(z₁, z₂) ≥ (fvec(s₁, s₂) − o(1))𝒰, fvec = f(s₁)F(s₂) + F(s₁)f(s₂) − F(s₁)F(s₂).

(ii) **Direct term (Hypothesis MT(a): standard upper vector sieve, Nath–Xie-type evaluation):** for each Q the count
is primes p ≡ −4̄ (mod Q) with N₁ sifted by 𝒬-primes < z₁ and N₂/Q by 𝒬-primes < z₂ (moduli Q·d₁d₂ ≤ x^{1/2−ε}:
BV); the product of two beta upper sieves gives
T^dir(τ) ≤ (D(τ) + o(1))𝒰, D(τ) = (1/((k−1)! 2^{k−1})) ∫_{α_i ≥ ζ, Σα_i ≤ τ} U(1/2 − Σα_i) ∏dα_i/α_i
(the 2^{−(k−1)} is the density 1/2 of 𝒬 among primes; the q | Q are ≥ z₂, so the N₁-sieve densities at q | Q change
by 1 + O(1/z₂)). The same evaluation is used for P415's Richert terms.

(iii) **T₁ (Hypothesis MT(b), switching; P415 model):** T₁ ≤ (pen·(2/a)F(b/ζ)B(θ₁) + o(1))𝒰,
B(θ) = F(1/θ) − F(1)√θ (the two-𝒬-factor Buchstab mass of N₁; P415 §1.4 check). Switched variable n = N₁ = mqq′
(counted as ½ × ordered pairs q ≠ q′ ≥ z₁: no cross-condition), sieve n − 4 for primality (linear upper sieve,
level x^a, sifting only primes < x^{a/3} < z₁, main term V(z)F_lin(3) = 2/(a log x) × local factors, loss 2/a) and
4n − 15 for 𝒬-primes < z₂ (semi-linear upper sieve, level x^b). Remainders: BV for convolutions at total level
x^{1/2−ε} (β = primes q′ ∈ 𝒬 on dyadic ranges, Siegel–Walfisz). *Correction to P415's model:* P415 also imposed
a ≤ θ₁; this is unnecessary (the linear upper sieve's main term V(D^{1/s})F(s) = 2/log D is the same for every
s ≤ 3, so one may sift only below x^{a/3} < z₁, and the bilinear BV has no constraint linking the level to the size
of q′). With the cap, the pure-switching C(4) margin would be −0.007 instead of +0.030 (§4).

(iv) **T^sw (Hypothesis MT(b), Chen-type switching on N₂):** switched variable n = N₂ ∈ 𝒩_k(τ), n ≡ 5 (mod 32);
sieve (n − 1)/4 for primality (linear, level x^a, loss 2/a) and (n + 15)/4 for 𝒬-primes (semi-linear upper sieve at
level x^b; for a level x^b with b ≤ 2θ′ the bound F(b/θ′)W(x^{θ′}) = 2A√(θ₁/b)·W(z₁)(1 + o(1)) is independent of the
sifting limit, i.e. (1/√b) × the S-density F(1)√θ₁·W(z₁) of §3.1). Hence
T^sw(τ) ≤ (pen·L·F(1)√θ₁·Unc(τ) + o(1))𝒰, L = min_{a+b=1/2}(2/a)b^{−1/2} = 6^{3/2} = 14.697 (a = 1/3, b = 1/6),
Unc(τ) = Σ_{j≥k, j even} (1/(2^j j!)) ∫_{α_i≥ζ, Σα_i≤1, σ_{k−1}(α)>τ} F(1)√(ζ/(1 − Σα_i)) ∏_{i≤j} dα_i/α_i,
σ_{k−1} = sum of the k − 1 smallest α_i. Equidistribution of 𝒩_k(τ) to level x^{1/2−ε}: every n ∈ 𝒩_k(τ) is a
product of a Siegel–Walfisz factor in [x^{ε′}, x^{1−ε′}] (either the S-part s, or the largest 𝒬-prime) and a
cofactor; BV for convolutions applies after the standard dyadic separation of the cross-conditions (as for Chen's
switched set {p₁p₂p₃}). Main term: |𝒩_k(τ) ∩ [1, 4x+1], n ≡ 5 (32)| is an integer count with a Selberg–Delange
asymptotic (S-part) and PNT (𝒬-primes), equal to (x/8)·W(z₂)·(mass)·(1 + o(1)) with the masses of §3.

**Hypothesis MT.** (a) (ii) holds with the stated main term; (b) (iii), (iv) hold with some pen ≤ 2.35.
*Assessment:* in a Chen-type evaluation the switched main term is exactly (loss) × (the local-density product of the
same event computed from the n-side); the 2-adic bookkeeping matches (n ≡ 5 (32) ⇔ p = (n − 1)/4 ≡ 1 (8); x/8
values times 2/log x for the odd number (n − 1)/4 gives X = x/(4 log x)), and at odd ℓ both sides are the CRT
density of the triple (p, N₁, N₂), giving pen = 1 + o(1). This is standard but **not written out here**; P415's
pen = 2.35 is Nath–Xie's *majorised* constant for their problem (and their v1 has internal constant
inconsistencies, P415 §1.4), not an evaluation.

### 2.3 Conditional theorem

**Theorem K6 (CONDITIONAL on Hypothesis MT; otherwise relative to BV, Nath–Xie Prop. 3.10, BV for convolutions and
standard upper sieves).** C(6) holds: ≫ x/(log x)² primes p ≤ x, p ≡ 1 (8), have p + 4 ∈ S and Ω_𝒬(4p + 1) ≤ 6.
*Proof.* Lemma D with θ₁ = 0.44, ζ = 0.006, s₁ = 1.0951, s₂ = 3.025, τ = 0.42 (the pen = 1.5 optimum; at
pen = 2.35 use θ₁ = 0.46, s₁ = 1.049, s₂ = 2.9125, τ = 0.45) and (i)–(iv): the margin is
fvec − pen(T₁⁰ + K·Unc) − D ≥ +0.07 (pen = 2.35) > 0 in units 𝒰 (§4; floating-point evaluation with Monte-Carlo
masses, relative MC error ≲ 1 %, i.e. ≲ 10⁻³ in the margin). Since 𝒰 ≫ x/(log x)², the count is ≫ x/(log x)². ∎
*Not claimed:* C(4) (its margin +0.045 at pen = 1 is below every plausible slack; it disappears at pen = 1.2).

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
(Every n ≡ 1 (4) with no 𝒬-prime below √y lies in S by parity, so this is the classical statement that the
parity-even sequence is extremal for F; P415's check B(θ) = (F(1)/4)√θ·C(θ) is the two-factor version.)

### 3.2 Configuration masses

For the integers n ≡ 1 (4) of size x^u free of 𝒬-primes below z₂ = x^ζ, the density (relative to n ≡ 1 (4), in
units W(z₂)) of those with exactly j 𝒬-factors is d_j(u): d₀(u) = F(1)√(ζ/u) (§3.1 at scale u), and
d_j(u) = (1/(2j))∫_ζ^u d_{j−1}(u − α)dα/α (each 𝒬-prime has density ½ dα/α; ordered/j). Floating-point check
(`z56_k4chen_mass.py`): Σ_{j even} d_j(1) = F(1/ζ) to 5·10⁻⁵ at ζ = 0.3, 0.1, 0.03, 0.008 (extremality, consistent
with §3.1). Values of d_j(1):

| ζ | j = 0 | 2 | 4 | 6 | 8 | 10 |
|---|---|---|---|---|---|---|
| 0.1 | 0.476 | 0.507 | 1.73e−2 | 3.2e−5 | 7e−10 | 0 |
| 0.03 | 0.261 | 0.617 | 0.117 | 5.1e−3 | 7.4e−5 | 4.1e−7 |
| 0.008 | 0.135 | 0.567 | 0.261 | 3.6e−2 | 2.1e−3 | 6.5e−5 |

The tail Σ_{j≥k} d_j decays like a Poisson tail with mean ≈ ½ log(1/ζ) — the quantitative reason switching beats
weights. Monte-Carlo implementation for Unc(τ) (`z56_k4chen_direct.py`, last factor integrated by Gauss–Legendre after
the substitution α_j = 1 − σ − t²) agrees with the grid masses to ≤ 1 % (`validate` mode of
`z56_k4chen_mixed.py`: e.g. ζ = 0.01, k = 6: 0.02978 vs 0.02988).

## 4. Results at BV level (Assessment: model numerics; floating point + MC)

Pure switching (τ = 0; `z56_k4chen_opt.py`, Nelder–Mead multistart; `data/z56/k4chen/opt_bv_pen.txt`):
r = 8: +0.373 (pen 1), +0.293 (1.5), +0.212 (2.35); r = 6: +0.296, +0.186, +0.060; r = 4: +0.030 (pen 1; −0.007
with P415's cap a ≤ θ₁); r = 2: −1.02.
Direct + switching (`z56_k4chen_direct.py`, grid θ₁ × ζ × τ; files `data/z56/k4chen/direct_*.txt`):

| r | pen | margin | θ₁ | ζ | s₁ | s₂ | τ | main | T₁ | D | K·Unc |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | 1 | +0.366 | 0.42 | 0.002 | 1.174 | 3.438 | 0.28 | 0.562 | 0.182 | 0.002 | 0.011 |
| 8 | 2.35 | +0.205 | 0.46 | 0.002 | 1.072 | 3.375 | 0.41 | 0.384 | 0.152 | 0.008 | 0.019 |
| 6 | 1 | +0.291 | 0.40 | 0.006 | 1.203 | 3.154 | 0.38 | 0.594 | 0.261 | 0.012 | 0.031 |
| 6 | 1.5 | +0.187 | 0.44 | 0.006 | 1.095 | 3.025 | 0.42 | 0.429 | 0.183 | 0.019 | 0.042 |
| 6 | 2.35 | +0.070 | 0.46 | 0.006 | 1.049 | 2.913 | 0.45 | 0.311 | 0.156 | 0.026 | 0.058 |
| 4 | 1 | +0.045 | 0.38 | 0.02 | 1.174 | 2.688 | 0.43 | 0.543 | 0.371 | 0.040 | 0.088 |
| 4 | 1.1 | +0.004 | 0.40 | 0.02 | 1.12 | 2.6 | 0.43 | 0.454 | 0.311 | 0.041 | 0.099 |
| 4 | 1.2 | −0.034 | 0.40 | 0.02 | 1.12 | 2.6 | 0.43 | 0.454 | 0.339 | 0.041 | 0.108 |
| 4 | 1.5 | −0.140 | | | | | | | | | |

(T₁ and K·Unc include the factor pen; D does not.) Weighted (Richert/Kuhn) + switching mixtures were also tried
(`z56_k4chen_mixed.py`): the weights never improved on pure switching at r = 4.
Reading: the switched bad-configuration cost K·Unc is 3–20 % of the budget; what limits r is the exact-N₁ machinery
(main − T₁ ≈ 0.17–0.33 of a "truth" F(1)√θ₁ ≈ 0.95: efficiency 18–35 %).

## 5. Level ledger (best sufficient levels found; Assessment, model, pen = 1)

Main/direct sums at level θ; switched sums at 1/2 ("BV") or θ ("same", needs GEH-type input for convolutions).
`z56_k4chen_ledger.py`, `data/z56/k4chen/ledger2/`.

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

* **L(2) ≈ 0.675 (BV switching), ≈ 0.645 (switching at θ).** **L(0): not reached by this scheme at θ ≤ 1**; the best
  sufficient level found for K(4) remains P415 §2(b) (product linear sieve + switching, ≈ 0.996 under ordinary EH).
* With switched sums at level 4/7 (a Fouvry–Grupp-type input, see §5.2) and θ = 1/2: C(4) margin +0.113 (pen 1),
  −0.063 (pen 1.5).

### 5.2 Which known levels apply (Assessment; literature `data/z56/k4chen/lit_report.md`)

BFI (4/7, well-factorable weights, fixed residue), Maynard II (3/5 triply well-factorable; 7/12 for linear-sieve
upper weights), Lichtman arXiv:2309.08522 (66/107; Thm 1.7 uniform for 0 < |a| < x^ε, triply well-factorable weights)
all require **fixed (or small) residues and specific weight structure**. Our main sieve has residue classes
p ≡ −4 (d₁), p ≡ −4̄ (d₂) — CRT-varying, not small — and semi-linear beta weights, for which no well-factorability
result was located. The switched linear sieves have fixed residues (n ≡ 4 (d) in T₁, n ≡ 1 (4d) in T^sw) and
linear upper weights (Maynard II Thm 1.2 type), but carry a second (semi-linear) sieve with a different residue; a
twist by characters of the small modulus would be needed. So none of these levels is available to us as stated;
the ledger values > 1/2 are CONDITIONAL hypotheticals. (Lichtman's 66/107 would not reach C(2) even if applicable.)

## 6. FRONTIER §4 hard screens (best item: Lemma D + switching scheme)

1. **T1 squares.** Kill side; the squares satisfy N₁, N₂ ∈ S identically (P415 §5), so Ω_𝒬 bounds are consistent
   with them; no upper-side claim is made.
2. **8/131, 8/241.** The target is the 4-specific line (HCKILL Lemma 1.1); inherited.
3. **Tied modulus.** Not applicable (kill side, fixed character χ₋₄).
4. **Fixed p.** Density statement only; nothing about a prescribed p.

## 7. Proposed FRONTIER §7.2 text (do not edit FRONTIER here)

> *(z56, `Z56_K4CHEN.md`; kill side, model level.)* **Chen-type switching on 4p + 1.** Exact reduction (Lemma D,
> PROVED): the configurations of 4p + 1 with ≥ r + 2 factors ≡ 3 (4) (all ≥ x^ζ) are split into a *direct* part
> (product Q of the r + 1 smallest ≤ x^τ; parity forces the extra factor) and a *switched* part (Chen switching with
> 4p + 1 as the variable). Their Buchstab mass is a Poisson-type tail, so in the P415 model the deficit improves from
> Ω_𝒬(4p + 1) ≤ 10 to **≤ 6 robustly** (margin survives switched constants inflated by 2.35) and **≤ 4 on a
> knife-edge** (pen ≤ 1.1), at BV level; additive weights (LP-optimal = Richert) cannot go below 10. Theorem K6
> (C(6)) is CONDITIONAL on the standard evaluation of switched main terms (Hypothesis MT). **Ledger** (sufficient
> levels found, not barriers): C(2) (the Chen analogue) at ≈ 0.675 (≈ 0.645 with switched sums at the same level);
> C(0) = K(4) not reached by this scheme at θ ≤ 1 — P415's ≈ 0.996 stands. Known beyond-1/2 levels (BFI, Maynard,
> Lichtman) do not apply as stated (CRT-varying residues, semi-linear weights).

## 8. Reproduction (all under `timeout`, `ulimit -v 4000000–6000000`)

* LP: `uv run --with numpy --with scipy python scripts/z56_k4chen_lp.py demo|scan θ λ pen r-list` → `lp_bv.txt`.
* Masses: `uv run --with numpy python scripts/z56_k4chen_mass.py 0.3 0.1 0.03 0.008` (§3.2 table).
* Pure switching: `… scripts/z56_k4chen_switch.py 8,6,4 0.5 0.5 1.0` (grid) → `switch_bv.txt`;
  `… scripts/z56_k4chen_opt.py r θ λ pen` (continuous; `K4CAP=1` restores P415's a ≤ θ₁) → `opt_bv_pen.txt`.
* Direct + switching: `K4ZETA=… K4TH1=… K4NS=20000 … scripts/z56_k4chen_direct.py r θ λ pen` → `direct_*.txt`.
* Ledger: `K4NS=20000 … scripts/z56_k4chen_ledger.py r bv|same θ-list` → `ledger2/`.
* Mixed weights + switching and MC validation: `… scripts/z56_k4chen_mixed.py validate | r θ λ pen`.
All sieve functions come from `scripts/z55_p415_sieve.py` (F, f by the delay-differential system, step 10⁻⁴).

## 9. Review log

(pending)
