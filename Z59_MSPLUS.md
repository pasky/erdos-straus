# Z59_MSPLUS — the primality-free target (MS⁺): dead moduli, local means, and a zero law. Verdict: narrowed / strengthened (target choice); no HOT LEAD

**ES is OPEN; (MS) and (MS⁺) are open.** Everything here is internal and unrefereed. Lane brief: `z52bbriefs/z59_lanes.md`
§MSPLUS. Notation: R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}; 𝔐 = {1, 121, 169, 289, 361, 529} ⊂ (ℤ/840)^× (the unit
squares mod 840); L = log(n/4). For fixed (u, B) the solutions form the progression n ≡ −(u + B) (mod 4uB),
n ≥ 4uB − u − B. For n ≡ 1 (4) this forces u + B ≡ 3 (4). R(n) is even for odd n (the swap u ↔ B has no fixed point).
"Group" of n ≡ 1 (4): 𝔐 if n mod 840 ∈ 𝔐, otherwise gcd(n, 105) ("unit" = 1, g3, g5, …, g105). P = prime, C = non-square
composite.

## 0. Falsifier table (for the mechanism studied: local means + dead moduli + an empirical zero law)

| Screen | Behaviour |
|---|---|
| F1 odd squares | The local mean (Thm 1) is **blind to squares**: an odd square coprime to 105 has the same leading mean as a prime. So no "mean large ⟹ R ≥ 1" statement can come from this mechanism; T1 is a Jacobi phenomenon that means cannot see. The zero law (§3) is fitted on non-squares only and is not claimed for squares. Incidental control: the "semi" batch of the structured search (§4.1) contained 6 squares p², produced by a generator version without the p ≠ q check (fixed before commit). The engine found no hit for any of them, as T1 requires. Non-squareness enters only through the fluctuation (zero) model, which is exactly the step nobody can prove. |
| F2 C-even (R₈) | Thm 1 holds verbatim for R₈ with leading mean exactly half (Remark 2.3, PROVED): **the dead-moduli structure is identical for R and R₈.** So the mechanism cannot separate R from R₈ (Assessment: it is not a proof route by itself). R₈ has zeros at 𝔐-primes above 10¹⁰. Over all primes p ≡ 1 (4) near 10¹⁰, their observed rate is several times (≈ 5×) what the R-zero law gives at equal mean (§3.5). Only 4 of the 12 are in 𝔐, where the excess is larger. So the zero law is problem-specific, not a function of the mean alone. |
| F3 composites | This is the lane's subject. A hit modulus d is coprime to n (dead moduli, PROVED, z58 LOGIC). Each odd q ∣ n lowers the **leading** mean coefficient by (q² − q + 1)/(q² + 1) (Thm 1). The composite zeros sit in the groups with 3 ∣ n, 15 ∣ n, 21 ∣ n, 105 ∣ n, where the mean is lowest. One law in the local mean m(n) reproduces their counts in the four large groups (g3, g15, g21, g105) within a factor ≈ 1.5. In the small groups it is right only within a factor 2–6 (§3). |
| F4 known zeros | The model only gives probabilities. It predicts zeros with the right order of magnitude where they occur, and it "proves" nothing anywhere. It **under-predicts** the 𝔐-prime zeros of 10⁶–10⁷ by ≈ 6× (§3.3). This is unexplained: their Jacobi depths k = 11–19 are ordinary. Thresholds come from the census (§6), not from the model. |

## 1. Precise statements

* **(MS⁺) (CONJECTURE, z58 LOGIC/LADDER).** R(n) ≥ 1 for every non-square n > 17 401 609 with n mod 840 ∈ 𝔐.
  * Status: CERTIFIED to 10¹¹ (z58 LADDER, one engine). This lane extends it to **10¹²** (§6, same engine, all 18
    chunks exit = 0), with no new zero.
* **(MS⁺₁₀₅)** (new formulation, CONJECTURE). R(n) ≥ 1 for every non-square n ≡ 1 (4) with gcd(n, 105) = 1 and
  n > 29 210 401.
  * This is all classes, not only 𝔐. It implies (MS⁺) once the finite range (17 401 609, 29 210 401] of 𝔐 is
    added, and the census covers that range. It also covers every prime p ≡ 1 (4) above the threshold. It is a
    strictly stronger statement.
  * Status: CERTIFIED to 10¹⁰ by the z58 LOGIC all-n census (`data/z58/logic/zeros_1e10.txt.gz`).
* **(R⁺_y) (rough version, CONJECTURE).** R(n) ≥ 1 for every non-square n ≡ 1 (4) > 8 813 281 all of whose prime factors
  exceed y, for y ≥ 47.
  * Status: CERTIFIED to 10¹⁰ (same census; §5.3). Stated for y ≥ 47; for y = 47 the last zero is 8 813 281, the
    last (★)-zero prime. For 11 ≤ y ≤ 43 the threshold must be 17 401 609 = 47·370 247, for y = 7 it must be
    29 210 401, and for y < 7 zeros continue to 9.9·10⁹.
* Out of scope: ES and (MS) themselves. Nothing here moves the B2 wall.

## 2. The local mean of R — what dead moduli do (PROVED) and what 𝔐 does (second order)

**Lemma 2.0 (PROVED; z58 LOGIC §4).** Every hit modulus d (d ≡ 3 (4), r = −n mod d, r ∣ (d+1)/4) has gcd(d, n) = 1.
In the (u, B) form: if a prime q divides n, then the pairs with q dividing exactly one of u, B are dead.
(If g ∣ d and g ∣ n, then g ∣ r ∣ (d+1)/4, so g ∣ 1. The (u, B) form follows from n ≡ −(u + B) (mod q).)

**Theorem 1 (PROVED).** Let Q = 2^k·Q′ with k ≥ 2 and Q′ odd squarefree, and let a mod Q with a ≡ 1 (mod 4). As X → ∞,

  (1/#{n ≤ X : n ≡ a (Q)}) · Σ_{n ≤ X, n ≡ a (Q)} R(n) = (𝔖_Q(a)/8)·log²X + O_Q(log X),

where 𝔖_Q(a) = ∏_{q ∣ Q′} σ_q(a), with σ_q(a) = 1 + 1/q² if q ∤ a, and σ_q(a) = 1 − 1/q + 1/q² if q ∣ a.
The power of 2 contributes the factor 1.

*Proof.*
1. Swap the sums: Σ_{n ≤ X, n ≡ a (Q)} R(n) = Σ_{(u,B)} N_{u,B}(X), where N_{u,B}(X) counts the n ≤ X with n ≡ a (Q),
   n ≡ −(u + B) (mod 4uB) and n ≥ 4uB − u − B.
2. Put g = gcd(4uB, Q). By CRT the two congruences are compatible iff a ≡ −(u + B) (mod g). In that case they define one
   class modulo lcm(4uB, Q) = 4uBQ/g. Hence N_{u,B}(X) = [cons]·g·(X − 4uB + u + B)⁺/(4uBQ) + O(1).
3. The O(1) terms sum to ≪ #{(u, B) : 4uB − u − B ≤ X} ≪ X log X.
4. The weight f(u, B) := [cons]·g/4 depends only on (u mod Q, B mod Q), because gcd(4uB, Q) does.
   * For a function f that is periodic mod Q in each variable, Σ_{uB ≤ Y} f(u, B)/(uB) = (f̄/2)·log²Y + O_Q(log Y),
     where f̄ is the mean of f over (ℤ/Q)². This is the hyperbola method applied to each of the Q² residue pairs.
   * The cut-off (X − 4uB + u + B)⁺/X differs from 1_{uB ≤ X/4} only in a range that costs O(log X) after division by X.
   * Hence the class mean is (X/Q)^{−1}·(X/Q)·f̄·(1/2)log²X·(1 + o(1)) = (f̄/2)·log²X + O(log X). The density of the
     class is 1/Q.
5. f̄ = E[[cons]·g]/4 factorises over the primes of Q (CRT). For odd q ∣ Q′ (exponent 1), split by how many of u, B are
   divisible by q:
   * neither (probability (1 − 1/q)²): g_q = 1, no condition, contribution (1 − 1/q)²;
   * exactly one (probability 2(1/q)(1 − 1/q)): g_q = q, and the condition a ≡ −(unit) (mod q) holds for exactly one
     value of the unit residue of the other variable, so the contribution is 2(1/q)(1 − 1/q)·q·[q ∤ a]/(q − 1) = (2/q)[q ∤ a];
   * both (probability 1/q²): g_q = q, condition a ≡ 0 (mod q), contribution (1/q²)·q·[q ∣ a] = [q ∣ a]/q.
   So σ_q(a) = (1 − 1/q)² + (2/q)[q ∤ a] + (1/q)[q ∣ a], which gives the two stated values.
6. For q = 2 (2^k ∥ Q, k ≥ 2, a ≡ 1 (4)), put j = v₂(u) + v₂(B) and m = min(2 + j, k), so g₂ = 2^m and the condition
   is u + B ≡ −a (mod 2^m), with −a ≡ 3 (mod 4).
   * If u and B are both odd or both even (probability 1/2), u + B is even and the condition fails, since m ≥ 2.
   * If exactly one is even (probability 1/2), u + B is odd. Conditioned on the even one, u + B is uniform over the odd
     residues mod 2^m, so the condition holds with probability 2^{−(m−1)}. The contribution is (1/2)·2^m·2^{1−m} = 1.
   So the 2-adic factor is 1 for every a ≡ 1 (4) and every k; the exact enumeration in `scripts/z59_msplus_local.py`
   agrees for k ≤ 5. With the normalisation 1/4 from step 4 this gives f̄ = 𝔖_Q(a)/4 and mean (𝔖_Q(a)/8)·log²X. ∎

*Remark 2.1 (higher prime powers; CERTIFIED by exact enumeration).* With q² ∥ Q, …, q^e ∥ Q (q = 3, e ≤ 4; q = 5, e ≤ 3;
q = 7, 11, e ≤ 2), σ_q still takes only the two values above, depending on q ∣ a. So the higher valuation of q in n does
not matter at leading order.

**Corollary 1.1 (PROVED, reading of Thm 1).**
* (i) **The leading term is Jacobi-blind.** All unit classes mod Q have the same leading mean, so 𝔐 is *not* special at
  leading order, and neither is the residue class mod 8.
* (ii) **Dead moduli are a leading-order effect.** Each odd q ∣ n multiplies the leading constant by
  (q² − q + 1)/(q² + 1): 0.700 for q = 3, 0.808 for 5, 0.860 for 7, 0.486 for 105 ∣ n.
* (iii) This item is about the constant only, not the class mean, because Thm 1's error term is not uniform in Q.
  * For any n, the product of the dead factors over the odd primes q ∣ n is at least ∏_{q ≤ y}(1 − q/(q² + 1)) ≫ 1/log y,
    where y is the size of the ω(n)-th prime. Since y ≲ log n, 𝔖 restricted to the primes q ∣ n is ≫ 1/log log n.
  * The heuristic leading mean 𝔖·L²/8 is therefore ≫ L²/log L → ∞. This is used only as an input to the heuristic
    of §3.5.

**Proposition 2.2 (second-order term; derivation in outline, EVIDENCE).**
* Using Σ_{u ≤ x, u ≡ α (Q)} 1/u = (log x)/Q + c_α + o(1), with c_α = −(log Q + ψ(α/Q))/Q, and a Mellin computation,
  the class mean is (𝔖_Q(a)/8)L² + c₁(a)L + c₀(a) + o(1). Here
  * c₁(a) = 2Σ_α W̄(α)c_α, with W̄(α) = Q^{−1}Σ_β f(α, β);
  * c₀ collects c_αc_β and the boundary term 2Σ_u u^{−1}log(4u/(4u − 1))W̄(u).
  The remainder is asserted, not proved.
* c₁ is where n's residues enter. For odd q ∤ n the u-marginal is W̄_q(u) = 1 − 1/q + [u ≡ −n (q)] (unit u), and 1 for
  q ∣ u. So c₁ rewards n ≡ −r (mod q) with small r, i.e. small shifts n + r with many small factors (the u-form).
* Numbers (Q = 840, `data/z59/msplus/coef840.txt`): c₁ = −0.137 (a = 1), −0.026 (a = 121). For non-𝔐 unit classes
  c₁ ranges up to +2.20 (a = 209, 629, i.e. n ≡ −1 (mod 105)), consistent with the small-r reading.

*Check (CERTIFIED means, EVIDENCE fit; `scripts/z59_msplus_mean.py`, `data/z59/msplus/means_1e9.txt`).* Exact R(n)
for all n ≡ 1 (4) ≤ 10⁹ (`scripts/z59_msplus_strat.c`). On n ∈ [5.6·10⁸, 10⁹], observed vs model mean (no fitted
parameter):

| group | count | mean R | model | ratio |
|---|---|---|---|---|
| C 𝔐 | 2 455 910 | 51.93 | 52.24 | 0.994 |
| P 𝔐 | 668 417 | 54.24 | 52.24 | 1.038 |
| P unit (non-𝔐) | 10 026 464 | 68.66 | 61.91 | 1.109 |
| C unit (non-𝔐) | 36 865 536 | 66.13 | 61.91 | 1.068 |
| C g3 | 25 008 164 | 43.12 | 41.28 | 1.045 |
| C g15 | 6 252 040 | 34.38 | 32.88 | 1.046 |
| C g105 | 1 042 007 | 28.99 | 28.10 | 1.032 |

* The 𝔐 deficit is captured. The P-𝔐 / P-unit ratio is 0.79 observed and 0.84 modelled; the leading term alone gives 1.
* The residual 1–11 % is not explained here. At leading order the primes q ≥ 11 contribute only ∏(1 + 1/q²) ≈ 1.02
  for primes, so most of it must be second-order terms at q ≥ 11 (unverified hypothesis).

**Remark 2.3 (R₈, PROVED by the same proof).** R₈ counts the solutions with C even, i.e. n ≡ −(u + B) (mod 8uB). The
proof of Thm 1 goes through with 4uB replaced by 8uB. The odd factors σ_q are identical. The 2-adic factor is again 1
(exact enumeration mod 2^e, e ≤ 6). The leading mean is (𝔖_Q(a)/16)·log²X, exactly half that of R.

## 3. The zero law

### 3.1 Data
* Census: exact R(n) for all n ≡ 1 (4) ≤ 10⁹ (`scripts/z59_msplus_strat2.c`). Each n gets the local mean
  m(n) = lead(a)·K(n)·L² + c₁(a)L + c₀(a), with a = n mod 840 and K(n) = ∏_{11 ≤ q ≤ 2000, q ∣ n}(q² − q + 1)/(q² + 1)
  (dead moduli at q ≥ 11).
* Each n also gets its Jacobi depth k(n), the least odd prime ℓ ∤ n with (n/ℓ) = −1.
* The results are binned in `data/z59/msplus/h_1e9.txt` (CERTIFIED counts).
* Cells with k(n) = 3 are excluded: n ≡ 2 (3) gives the hit d = 3 (PROVED).

### 3.2 Fit (EVIDENCE)
Poisson GLM on the cells with n ∈ [10⁶, 10⁹] (261 non-square zeros), `scripts/z59_msplus_zerofit.py`,
`data/z59/msplus/zerofit_1e9.txt`:
* model A: log P(R = 0) = α − κm + β log₁₀n, with κ = 0.351 ± 0.019 and β = −0.46 ± 0.12;
* model B: model A plus dummies for k(n) ∈ {7, 11, 13, 17–23, 29–47, > 47}. Here κ = 0.288 ± 0.018, and the
  dummies rise monotonically with the depth k (+0.45, +1.23, +1.54, +2.05 for k = 11, 13, 17–23, 29–47);
* the same law for R = 2 (2302 events) gives κ = 0.272 ± 0.006.

Reading: P(R = 0) ≈ e^{−0.3·m}, with an n-dependence and a Jacobi-depth dependence of up to e^{2.05} ≈ 8×. This is a
Poisson rate of about 0.6 per expected *unordered* hit pair, not Poisson in R.
* The k > 47 dummy in model B is degenerate: −24.9 ± 10⁶, because that bucket has no events. The deepest
  pseudo-squares therefore get essentially zero probability, which is a mis-specification.
* Pooling k > 47 with 29–47 (`zerofit_1e9_pooled.txt`) changes every quoted prediction by < 1 %.

### 3.3 Goodness of fit by group (model B, in sample, observed / predicted zeros per decade)

| group | 10⁶ | 10⁷ | 10⁸ |
|---|---|---|---|
| C g105 | 16 / 16.0 | 11 / 16.8 | 10 / 14.5 |
| C g15 | 23 / 35.5 | 31 / 30.3 | 15 / 20.5 |
| C g21 | 20 / 16.1 | 20 / 12.3 | 9 / 7.3 |
| C g3 | 40 / 34.5 | 20 / 20.5 | 12 / 9.2 |
| C g35 | 3 / 3.4 | 4 / 2.0 | 1 / 0.9 |
| C g5 | 3 / 6.3 | 2 / 2.9 | 3 / 0.9 |
| C g7 | 3 / 2.8 | 2 / 1.1 | 2 / 0.3 |
| C 𝔐 | 3 / 2.4 | 2 / 0.8 | 0 / — |
| C unit | 0 / 1.6 | 1 / 0.5 | 0 / — |
| P 𝔐 | 4 / 0.6 | 0 / — | 0 / — |
| P unit | 1 / 0.45 | 0 / — | 0 / — |

* **In the four large groups (g3, g15, g21, g105), one law in m(n) reproduces the composite zero counts within a factor
  ≈ 1.5.** The rare groups are right only within 2–6×: g5 and g7 are under-predicted at 10⁸ (3 / 0.9, 2 / 0.3).
* A negative-binomial model with the group mean and variance under-predicts the zeros of the 3 ∣ n groups by factors
  ≈ 20–90 at 10⁷–10⁸ (`scripts/z59_msplus_nb.py`, `data/z59/msplus/nb_1e9.txt`). The local mean m(n) is the
  better covariate; the group variance is not.
* **Not explained:** the 𝔐-prime zeros of 10⁶–10⁷ (4 vs 0.6 at 10⁶; Poisson tail ≈ 0.003). Their Jacobi depths
  (k = 13, 19, 11, 17 for 1 724 209, 1 726 201, 5 212 561, 8 813 281) are ordinary and already inside the model. The
  excess is an open question, with no attribution claimed.

### 3.4 Pre-registered out-of-sample test (predictions committed in `85a4fa37` before the results existed)
* Exact census of the classes 105 ∣ n, 15 ∣ n, 21 ∣ n and 3 ∣ n-only on [10¹⁰, 10¹¹] (`scripts/z59_msplus_cdec.c`, the
  z58 LADDER decider on chosen classes; `scripts/z59_msplus_oos.sh`, `data/z59/msplus/oos/`). The 3 ∣ n-only row was
  run by the internal reviewer (`data/z59/msplus/review_g3/`).
* Engine check (internal review): on (10⁶, 10¹⁰] the engine's zero sets for 105 ∣ n, 15 ∣ n 7 ∤ n, 21 ∣ n 5 ∤ n and
  3 ∣ n-only equal the z58 LOGIC zero sets exactly (48 / 87 / 55 / 76). All 17 + 1 OOS zeros were confirmed R = 0 by
  an independent divisor-based engine.
* **No pass/fail criterion was pre-registered.** Every pre-registered row is reported:

| group | pred. A | pred. B | observed [10¹⁰, 10¹¹] | Poisson tail (B) |
|---|---|---|---|---|
| 105 ∣ n | 5.51 | 6.05 | **9** | P(≥ 9) ≈ 0.15 |
| 15 ∣ n, 7 ∤ n | 4.36 | 4.80 | **4** | — |
| 21 ∣ n, 5 ∤ n | 1.09 | 1.32 | **4** | P(≥ 4) ≈ 0.045 |
| 3 ∣ n only | 0.57 | 0.83 | **1** (10 234 561 689) | — |
| total of the four | 11.53 | 13.00 | **18** | P(≥ 18) ≈ 0.11 (A: 0.047) |
| 𝔐 composites | 3.7·10⁻⁴ | 2.6·10⁻³ | **0** (z58 census) | — |

* The 18 zeros are composite. Several carry further small factors 11, 13, 19, …, i.e. further dead moduli.

*Sensitivity (EVIDENCE, `scripts/z59_msplus_sens.py`, `data/z59/msplus/zerofit_beta0.txt`).* Refitting model B with
the log₁₀n term removed (β = 0) predicts 15.8 / 7.8 / 1.8 for the first three rows (total 25.4). The observed 17 lies
between the two fits (12.2 and 25.4), only marginally so: P(≤ 17 | 25.4) ≈ 0.05. Per row the law is right within a factor ≈ 2–3. The 21 ∣ n row is
under-predicted (4 against 1.3–1.8; Poisson tail ≈ 0.05–0.1); the 15 ∣ n row is slightly over-predicted by both.
So the decline in n is real, but its rate is uncertain.

The previous decade [10⁹, 10¹⁰] was held out of the fit. It is not blind, since the z58 zero list predates the model
design:
* total: 42 observed against 27.0 (A) and 28.2 (B), P(≥ 42 | 28.2) ≈ 0.009;
* by group: g105 11 / 9.8, g15 18 / 11.1, g21 6 / 3.4, g3 4 / 3.2, g35 2 / 0.31, g7 1 / 0.06, g5 0 / 0.22, 𝔐 0 / 0.03,
  unit 0 / 0.01 (B).

Reading (EVIDENCE):
* The law matches the order of magnitude and the group ranking.
* It **under-predicts the totals by ≈ 1.4–1.5× in two consecutive decades**: p ≈ 0.11 under B and 0.05 under A on the
  pre-registered decade, and 0.009 on the held-out one. The 21 ∣ n row is ≈ 3× too low.
* The fitted decline β log₁₀n is too steep: the 105 ∣ n zero counts are flat (10, 11, 9 per decade at 10⁸, 10⁹,
  10¹⁰).
* This is a successful order-of-magnitude prediction, not a passed test.

### 3.5 Extrapolation and the finiteness question (Assessment)
* If log P(R = 0) ≤ −κ·m(n) + O(log log n) with κ > 0, then Σ_n P(R(n) = 0) < ∞ over all non-square n ≡ 1 (4). This
  follows from m(n) ≫ L²/log L (Cor 1.1(iii)). The heuristic therefore predicts **finitely many non-square zeros in
  total**, in every group.
* Model B's expected numbers beyond the census:
  * 𝔐 composites: 2.6·10⁻³ in [10¹⁰, 10¹¹] and 1.7·10⁻⁴ beyond 10¹¹;
  * 𝔐 primes: ≈ 10⁻⁴;
  * non-𝔐 composites coprime to 105: ≈ 1.4·10⁻³ beyond 10¹⁰;
  * 105 ∣ n and 15 ∣ n: ≈ 11 in [10¹⁰, 10¹¹] (13 observed), 5 in [10¹¹, 10¹²], 1.6 in [10¹², 10¹³], 0.5 in
    [10¹³, 10¹⁵]. The β = 0 fit gives ≈ 12, 4 and 1.2 for the last three ranges.
  * So the 105 ∣ n tail plausibly runs to 10¹³–10¹⁵; it is finite under either fit.
  * For 𝔐 the two fits give 4·10⁻⁴ (β = 0) and 2.7·10⁻³ (B) expected composite zeros beyond 10¹⁰.
* The finiteness prediction rests on extrapolating an exponential law in m from m ∈ [10, 45] to m ≈ 75 (𝔐 at 10¹¹)
  and beyond. Nothing proves this.
* The R₈ zeros warn that the law is problem-specific. With R₈ ≈ R/2 in mean (Remark 2.3), model A at m/2 ≈ 35
  predicts an R₈-zero rate of ≈ 10⁻⁷ among primes p ≡ 1 (4) near 10¹⁰. The observed rate is ≈ 5·10⁻⁷: 12 zeros among
  ≈ 2.2·10⁷ such primes in [10¹⁰, 1.1·10¹⁰] (rough Assessment).
* Answer to brief (1):
  * **dead moduli + the local mean account for the composite zeros in and out of 𝔐 at the level of counts per group,
    within ≈ 1.5× in the large groups and 2–6× in the small ones**, with a systematic ≈ 1.4× under-prediction in
    later decades. They do not account for the 𝔐-prime zeros of 10⁶–10⁷;
  * the heuristic predicts finitely many non-square zeros in 𝔐 and among n coprime to 105 (with the ones already
    found most likely all of them), and a long but finite tail for 105 ∣ n and 15 ∣ n.

## 4. Near-squares and the twisted T1 question (brief (3))

**Lemma 4.1 (PROVED, no positive-density twisted T1 for (★)).** Let s be a positive non-square integer with
s ≡ 1 (mod 4). Then the set of odd m with R(s m²) = 0 has natural density 0 among odd m.

*Proof.*
1. Let 𝒫 be the set of primes ℓ ≡ 3 (mod 4), ℓ ∤ s, with (s/ℓ) = −1. Write s = s₀t² with s₀ > 1 squarefree. Then
   s₀ ≡ 1 (4), and (s/ℓ) = (ℓ/s₀) by reciprocity. The characters χ₋₄ and (·/s₀) are independent: their conductors
   are 4 and s₀ > 1, s₀ odd. By Dirichlet, 𝒫 has relative density 1/4 among primes.
2. Fix ℓ ∈ 𝒫. Then −1 is a non-residue mod ℓ, so −s^{−1} is a residue. Hence s m² ≡ −1 (mod ℓ) has exactly 2 solutions
   m mod ℓ.
3. For such m, d = ℓ, u = 1, C = (ℓ + 1)/4 and B = (s m² + 1)/ℓ give a solution, provided s m² ≥ ℓ − 1 (true for all
   large m).
4. By CRT, the density of odd m avoiding these classes for every ℓ ∈ 𝒫, ℓ ≤ z, is ∏_{ℓ ∈ 𝒫, ℓ ≤ z}(1 − 2/ℓ) → 0, since
   Σ_{ℓ ∈ 𝒫} 1/ℓ = ∞. ∎

So, unlike numerator K ≥ 8 (z58 WILDCARD Lemma 4.3, where R ≡ 0 on whole families s m²), the (★) count has no
fixed-core family s m² of positive relative density with R = 0 besides the squares. Thin infinite subfamilies (m in a
sieve-thin set avoiding all hit classes) are not excluded by the lemma.

*Data (CERTIFIED, z58 LOGIC zeros to 10¹⁰; `scripts/z59_msplus_twist.py`, `data/z59/msplus/twist.txt`).*
* For the 723 non-square s ≡ 1 (4) with 5 ≤ s < 3000, the odd m with s m² ≤ 10¹⁰ number 913–22 361 per s.
* At most 3 of them give R(s m²) = 0: the maximum is attained by s = 33 (m = 7, 35, 45) and s = 105 (m = 1, 11, 57).
  The distribution over s of the number of zeros is 668 / 49 / 4 / 2 for 0 / 1 / 2 / 3.
* For the 10 such s with s mod 840 ∈ 𝔐, at most 1 of the 932–1574 values of m gives a zero.
* Zeros are not inherited under n ↦ q²n or n ↦ n/q²: for q = 3, 5, 7, 11, 13 there are 1, 1, 0, 2, 0 coincidences
  (out of 388–460 zeros n with q²n ≤ 10¹⁰).

### 4.1 Structured search beyond the census (CERTIFIED hits, `scripts/z59_msplus_gen.py`, `z59_msplus_dec.c`)
* Families, all non-square with n mod 840 ∈ 𝔐 and 10¹¹ < n < 4·10¹⁸:
  * **sm2:** n = s m² (s non-square in 𝔐);
  * **deadsq:** n = s (P_y k)², with P_y = ∏_{11 ≤ q ≤ y} q and y ≤ 43;
  * **dead:** n ≡ 0 (mod P_y) for y ≤ 47, half of them also a non-zero square modulo every further prime the CRT
    modulus allows (pseudo-squares);
  * **msq:** n = m² + 840t, t < 50;
  * **semi:** balanced semiprimes.
* Distinct inputs (seed 2): 99 220 (sm2), 24 378 (deadsq), 86 330 (dead), 50 000 (msq), and 49 998 for semi, of which
  49 992 are non-squares. Seed-1 batches add more (`data/z59/msplus/struct/EVAL.txt`).
* **Every non-square input has a verified (u, B, C) with least hit modulus ≤ 211 403.** The internal reviewer re-verified
  all 460 000 output lines.
* The six squares p² in "semi" seed 2 came from a generator version without the p ≠ q check. That check was added
  before the generator's first commit, so the committed generator does not reproduce them. They gave no hit up to
  10⁷, as T1 requires.
* Assessment: these families have local means m ≥ 57.6, so the model expects < 10⁻⁸ zeros in total. They therefore test
  for rigid algebraic obstructions, not the zero law. None was found.

## 5. What (MS⁺) admits that (MS) does not (brief (2), (4))

### 5.1 Closure (PROVED / CERTIFIED)
**Lemma 5.1 (scaling, PROVED).** For b ≥ 1, the solutions (u, B, C) of R(bn) with b ∣ gcd(u, B) correspond bijectively
to the solutions (u/b, B/b, bC) of R(n) with b ∣ C. (Divide 4uBC − u − B = bn by b.)
So R(n) ≥ 1 with a solution having b ∣ C implies R(bn) ≥ 1. There is no unconditional inheritance either way:
* products: 12 538 801 = 517·24 253 with R(517) = 4 and R(24 253) = 32, but R(12 538 801) = 0 (CERTIFIED);
* divisors: R(4545) = 0 while R(101) = 6 and R(45) = 2. Conversely, odd squares have R = 0 with non-square cofactors.
(MS⁺) is closed under nothing obvious. It implies (MS) (primes in 𝔐 are non-squares), and nothing in the other direction
is known.

### 5.2 Kinds of proof (Assessment)
* **Primality enters (MS) through two properties: roughness and non-squareness.** In the u-form,
  R(n) = Σ_u #{d ∣ n + u : d ≡ −1 (4u), d ≥ 4u − 1}.
  * Roughness: gcd(n, u) = 1 and gcd(n, d) = 1 (Lemma 2.0).
  * Non-squareness: the Jacobi structure. Rough squares p² have R = 0 (T1), so roughness alone cannot suffice.
  So an argument for (MS) that uses primality only through these two properties also proves the rough statement
  (R⁺_y) on 𝔐. (MS⁺) adds the composites with small factors q ≥ 11, which are dead-moduli inputs of lower mean
  (Cor 1.1).
* **Arguments allowed by (MS⁺) but useless for (MS):** descent or induction on n that maps a non-square zero n to a
  smaller non-square zero n′ (Vieta-, Markoff- or Hasse-type descents land on composites). Also algebraic identities
  for factored n (n = xy with structure in x, y), and generic-integer (sieve-of-all-n) arguments that need no prime
  input.
  * No descent of the scaling type exists (§4: zeros are not inherited under n ↦ q²n or n ↦ n/q²).
  * The zero law says the zeros are sporadic (rate e^{−0.3m}), with no visible algebraic family, so a descent would
    have to be non-scaling.
* **Barriers that are the same for both:** T1 (squares) and B1 (fixed covering congruences fail, since every class mod M
  that is a square class mod M contains squares). Also LOGIC Thm 6.2 (pseudo-squares defeat IOpen for (MS⁺)), and F2:
  Remark 2.3 shows the dead-moduli structure of R₈ is identical, and R₈ is false on 𝔐 above 10¹⁰.

### 5.3 Target comparison by the screens (CERTIFIED thresholds from the z58 LOGIC all-n census to 10¹⁰)

| target (non-square n ≡ 1 (4) ≤ 10¹⁰ with …) | zeros | last zero | model B, expected zeros beyond 10¹⁰ |
|---|---|---|---|
| (MS): primes in 𝔐 | 9 | 8 813 281 | ≈ 10⁻⁴ |
| (MS⁺): n mod 840 ∈ 𝔐 | 27 (9 P + 18 C) | 17 401 609 | ≈ 3·10⁻³ |
| (MS⁺₁₀₅): gcd(n, 105) = 1, all classes | 38 | 29 210 401 | ≈ 4·10⁻³ |
| (R⁺_y), y = 11 | 30 | 17 401 609 | — |
| (R⁺_y), y = 43 | 21 | 17 401 609 | — |
| (R⁺_y), y = 47 | 19 | **8 813 281** | — |
| all non-squares (3 ∣ n allowed) | 500 | 9 919 520 121 | ≈ 20 (finite tail, 105 ∣ n, 15 ∣ n) |

Assessment (brief (4)):
* **(MS⁺₁₀₅) is, by the screens, as good a target as (MS⁺)** (a judgement call, since it is strictly stronger). It drops
  the Mordell-class hypothesis and so needs no Mordell input. Its F3 screen is equally clean beyond 2.9·10⁷, and the
  zero law gives it the same negligible tail.
* **(R⁺_y) for y ≥ 47 is the cleanest primality-free statement:** same threshold as the prime statement itself
  (8 813 281), all classes, CERTIFIED to 10¹⁰.
* Versions that allow 3 ∣ n are worse. Their zeros continue (9 with 105 ∣ n in [10¹⁰, 10¹¹], §3.4), so any proof must
  depend on the dead-moduli factor 𝔖(n), i.e. be quantitative in the small prime factors.
* All versions inherit F1 (squares must be excluded by hypothesis) and F2 (identical dead-moduli structure for R₈).
  None is easier than (MS) in any known technique; (MS⁺) is logically stronger.

## 6. Census extension (CERTIFIED, one engine)
`scripts/z59_msplus_census.sh` runs the z58 LADDER exact decider `scripts/z58_ladder_mdec.c` unchanged, in chunks of
5·10¹⁰. Output: `data/z59/msplus/census/`.
* All 18 chunks covering (10¹¹, 10¹²] finished with exit = 0. Early chunks with stale exit = 126 status files (a binary
  race at launch) were re-run and overwritten.
* Every non-square n with n mod 840 ∈ 𝔐 in (10¹¹, 10¹²] was decided: **no zero** among **1 046 544 177 primes and
  5 381 870 962 non-square composites**.
  * The internal review checked that the total 6 428 415 139 equals 6·9·10¹¹/840 minus the 156 291 odd squares in
    these classes.
  * The largest least-hit modulus is 1 470 759, at n = 475 715 523 361.
* With z58 LADDER this gives: **the non-square zeros of R in 𝔐 up to 10¹² are exactly the 9 primes and 18 composites
  ending at 17 401 609** (one engine; no second full-range engine).

## 7. Verdict, screens, proposed FRONTIER text

**Verdict: narrowed, and strengthened as a choice of target; no HOT LEAD.**
* *Strengthened (understanding, PROVED part).* Theorem 1 gives the exact leading local mean of R on any class. Dead moduli
  act at leading order through σ_q = (q² − q + 1)/q² against (q² + 1)/q². Mordell's classes act only at second order
  (c₁L). R₈ has the identical dead-moduli structure (Remark 2.3). Lemma 4.1: there is no positive-density
  twisted-T1 family for (★).
* *Strengthened (target choice, CERTIFIED + EVIDENCE).*
  * The composite zeros are quantitatively a dead-moduli phenomenon. One zero law in the local mean reproduces their
    group distribution to within ≈ 1.5× in the large groups.
  * Its pre-registered out-of-sample prediction on [10¹⁰, 10¹¹] had the right order of magnitude and group ranking:
    18 observed vs 13.0 (B) / 11.5 (A); p ≈ 0.11 / 0.05; 21 ∣ n about 3× high. There was no pre-set pass criterion,
    and the law under-predicts systematically by ≈ 1.4× (§3.4).
  * The primality-free targets (MS⁺), (MS⁺₁₀₅) and (R⁺_{47}) have negligible predicted tails. The (MS⁺) census now
    reaches 10¹² (§6). (R⁺_{47}) has exactly the prime threshold 8 813 281.
* *Narrowed.*
  * PROVED: the leading mean is square-blind (Thm 1) and R₈ has the same dead-moduli structure (Remark 2.3).
  * CERTIFIED: unconditional product, divisor and q²-scaling closures of R(n) ≥ 1 fail (§5.1 examples).
  * Assessment, not a theorem: the means mechanism is therefore not a proof route on its own. Naive, unconditional
    closure-based reductions between (MS) and (MS⁺) are unavailable. Reductions conditioned on the shape of the witness
    (as in Lemma 5.1, b ∣ C) are not excluded.
* *Not explained:* the excess of 𝔐-prime zeros at 10⁶–10⁷ (≈ 6× the law). Their Jacobi depths are ordinary, and the
  cause is open.

**Screens for the best idea here (the "use (MS⁺₁₀₅)/(R⁺_{47}) as the target" recommendation).**
* T1 squares: excluded by hypothesis; the mechanism itself is square-blind, so any proof must find its non-square
  input elsewhere.
* 8/131 and numerator 8: fails as a mechanism, because the dead-moduli structure is identical for R₈. The R₈
  statements are false (zeros above 10¹⁰), so a proof must use C odd somewhere.
* Tied modulus (B2): untouched.
* Fixed p: the model is a probability for each n and certifies nothing at a fixed p.

**Proposed FRONTIER §7 text (do not apply without review).**
> *(MS⁺) and dead moduli (z59 MSPLUS).*
> * The class mean of R is (𝔖(a)/8)log²X + O(log X), with σ_q = 1 + 1/q² (q ∤ a) and 1 − 1/q + 1/q² (q ∣ a), and no
>   2-adic or quadratic-residue dependence at leading order (PROVED). Mordell's classes lower the mean only at order L.
> * One empirical zero law, P(R(n) = 0) ≈ exp(−0.3·m(n)) in the local mean m, reproduces the group distribution of
>   the composite zeros (3 ∣ n, 15 ∣ n, 105 ∣ n, …) within ≈ 1.5× in the large groups.
> * A pre-registered prediction for [10¹⁰, 10¹¹] got the order of magnitude right: 9/4/4/1 zeros observed against
>   6.1/4.8/1.3/0.8 for 105 ∣ n, 15 ∣ n, 21 ∣ n, 3 ∣ n-only. It under-predicts by ≈ 1.4×, with no pre-set criterion.
> * The law predicts finitely many non-square zeros, with a negligible tail on 𝔐 and among n coprime to 105
>   (EVIDENCE/Assessment).
> * There is no positive-density twisted-T1 family for (★) (PROVED). (MS⁺) is CERTIFIED to 10¹² (one engine).
> * Primality-free targets with clean screens: (MS⁺₁₀₅) (gcd(n, 105) = 1, all classes, threshold 29 210 401) and
>   (R⁺_{47}) (all prime factors > 47, threshold 8 813 281), both CERTIFIED to 10¹⁰.
> * The dead-moduli structure of R₈ is identical, so these are statements, not mechanisms. B2 is untouched.

**Bottom line.**
* The composite zeros of the (★) count are not mysterious. Each odd prime q ∣ n kills the moduli divisible by q, which
  lowers the leading mean by the exact factor (q² − q + 1)/(q² + 1). A single zero law in that mean predicts where
  composite zeros occur and, to within ≈ 1.5×, how often. That includes a pre-registered decade beyond the old census,
  where it was right in order of magnitude and ranking but systematically low.
* In Mordell's classes, the residue structure enters only at second order. The law says the composite tail there is
  already exhausted, which is consistent with the census, now to 10¹².
* For 105 ∣ n the tail is long but finite.
* None of this is a proof device. The mechanism is square-blind and does not distinguish R from R₈.
* (MS⁺) is a logically stronger target without unconditional closure properties, so naive "reduce to primes"
  arguments are unavailable (Assessment). Its value is as a cleaner *statement*.
* The variants (MS⁺₁₀₅) and (R⁺_{47}) are consistent (census to 10¹⁰) with primality mattering only through "no small
  prime factor" plus non-squareness.
* The B2 wall is untouched.

## 8. Reproduction
* Local factors: `uv run python scripts/z59_msplus_local.py`.
* Class means: `gcc -O2 -o strat scripts/z59_msplus_strat.c -lm && ./strat 1000000000 1000000 > s.txt`, then
  `uv run --with numpy --with scipy python scripts/z59_msplus_mean.py s.txt` (`data/z59/msplus/strat_1e9.txt.gz`,
  `means_1e9.txt`; ≈ 90 s, 1 GB).
* Zero law:
  * `scripts/z59_msplus_coef.py > coef840.txt`;
  * `gcc -O2 -o strat2 scripts/z59_msplus_strat2.c -lm && ./strat2 1000000000 coef840.txt > h_1e9.txt` (2.2 GB);
  * `uv run --with numpy --with scipy --with sympy python scripts/z59_msplus_zerofit.py h_1e9.txt coef840.txt 200000`;
  * sensitivity: `scripts/z59_msplus_sens.py`.
* Out-of-sample: `scripts/z59_msplus_oos.sh` (`scripts/z59_msplus_cdec.c`).
* Structured search: `scripts/z59_msplus_struct.sh FAM COUNT SEED` (`z59_msplus_gen.py`, `z59_msplus_dec.c`), then
  `scripts/z59_msplus_structeval.py`.
* Census: `scripts/z59_msplus_census.sh LANE 3 10 100` (three lanes).
* Data: `data/z59/msplus/` (< 20 MB).

## 9. Internal review
A hostile internal review (`data/z59/msplus/internal_review.md`, on commit 803f068d) found 4 MAJOR, 11 MINOR and 7 NIT
issues.
* It verified independently: Theorem 1 (exact enumeration and a separate sieve), Remarks 2.1/2.3, Lemmas 2.0, 4.1 and
  5.1, the closure examples, the §5.3 thresholds, all OOS zeros (second engine), the engine's agreement with the z58
  zero sets on (10⁶, 10¹⁰], all 460 000 structured-search witnesses, and the completeness of the 10¹² census.
* All findings were fixed in this version:
  * M1: §6 rewritten after all chunks finished; the census files are committed.
  * M2: "passed" withdrawn. All five pre-registered rows are reported (the 3 ∣ n-only row was run by the reviewer),
    with p-values and the statement that no criterion was pre-set.
  * M3: §5.2 corrected to "roughness **and** non-squareness".
  * M4: the closure and no-proof-route statements are relabelled Assessment and scoped to unconditional closures.
  * Minor fixes: OOS count 17 + 1; the §4 data restated with a committed script; "positive-density" in Lemma 4.1 and
    its reading; the c₁ range; the scope of the 1.5× claim; the 𝔐-prime excess left unattributed; the degenerate k > 47
    dummy (pooled refit, < 1 % change); Cor 1.1(iii) restricted to the constant 𝔖; the provenance of the semi_2
    squares; the R⁺_y thresholds by range of y; the artefacts for the NB claim (`nb_1e9.txt`); the residual 1–11 %
    marked as an unverified hypothesis.
  * Nits fixed.
* Not re-reviewed after the fixes. A cross-model review is expected.
