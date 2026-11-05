# Z59_MSPLUS — the primality-free target (MS⁺): dead moduli, local means, zero law. (CHECKPOINT 1 — work in progress)

**ES is OPEN; (MS) and (MS⁺) are open.** Internal, unrefereed. Lane brief: `z52bbriefs/z59_lanes.md` §MSPLUS.
Notation: R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}; 𝔐 = {1, 121, 169, 289, 361, 529} ⊂ (ℤ/840)^×; L = log(n/4).
For fixed (u, B) the solutions form the progression n ≡ −(u + B) (mod 4uB), n ≥ 4uB − u − B; n ≡ 1 (4) ⟺ u + B ≡ 3 (4).
R(n) is even for odd n (the swap u ↔ B has no fixed point: u = B forces n even).

## 0. Falsifier table (for the *mechanism* studied here: local means + "dead moduli" + a zero law)

| Screen | Behaviour |
|---|---|
| F1 odd squares | The local mean (Thm 1) is **blind to squares**: an odd square m² coprime to 105 has the same 𝔖 as a prime. So no statement "mean large ⟹ R ≥ 1" can be proved by this mechanism; T1 (R(m²) = 0) is a Jacobi phenomenon invisible at the level of means. The zero law of §3 is fitted on non-squares only and is *not* claimed for squares. Non-squareness enters only through the fluctuation (zero) model — exactly the step no one can prove. |
| F2 C-even (R₈) | Thm 1 has a verbatim analogue for the C-even half (mean (𝔖/16)L², to be checked); the mechanism therefore cannot separate R from R₈, and R₈ has zeros at 𝔐-primes > 10¹⁰. So the mechanism is a *descriptive model*, not a proof route. Any (MS⁺)-type statement for R₈ is false (known zeros in 𝔐 ∩ [10¹⁰, 2.4·10¹⁰]). |
| F3 composites | This is the lane's subject. Dead moduli (gcd(d, n) > 1 ⟹ d is not a hit, PROVED) lower the **leading** coefficient of the mean by (q² − q + 1)/(q² + 1) per odd prime q | n (Thm 1, PROVED). The 285 composite zeros ≤ 8·10⁶ and the 486 to 10¹⁰ sit overwhelmingly in classes with 3 | n, 5 | n, 7 | n — where the mean is lowest (§2–3). |
| F4 known zeros | The model only gives probabilities; it predicts zeros (with the right order of magnitude, §3) at the known places and does not "prove" positivity anywhere. Threshold questions are answered by the census (§5), not by the model. |

## 1. Precise statements

* **(MS⁺) (CONJECTURE, z58):** R(n) ≥ 1 for every non-square n > 17 401 609 with n mod 840 ∈ 𝔐.
  Status: CERTIFIED to 10¹¹ (z58 LADDER, one engine); this lane extends the in-𝔐 census beyond 10¹¹ (§5).
* Variants compared in §6: (MS⁺₁₀₅) all non-square n ≡ 1 (4) coprime to 105 above a threshold; rough versions
  (all prime factors > y).

## 2. Theorem 1 — the local mean of R, and what "dead moduli" do to it (PROVED)

**Theorem 1 (PROVED).** Let Q be a positive integer with 4 | Q and Q/4 odd squarefree... (general form in §2.2), a mod Q with
a ≡ 1 (mod 4). Then, as X → ∞,
  (1/#{n ≤ X : n ≡ a (Q)}) Σ_{n ≤ X, n ≡ a (Q)} R(n) = (𝔖_Q(a)/8) log²X + O_Q(log X),
  𝔖_Q(a) = ∏_{q | Q, q odd} σ_q(a),  σ_q(a) = 1 + 1/q² if q ∤ a,  σ_q(a) = 1 − 1/q + 1/q² if q | a.
The 2-part contributes the factor 1 (the mean does not depend on a mod 8).

Consequences: (i) **the leading term is Jacobi-blind**: all unit classes mod Q have the same leading mean; 𝔐 is not
special at leading order. (ii) dead moduli lower the leading constant by the factor (q² − q + 1)/(q² + 1) per odd q | n
(q = 3: 0.700, 5: 0.808, 7: 0.860; 105 | n: 0.486). (iii) The 𝔐-deficit of the mean (z58: 0.1246 vs 0.1636 for
primes) is a **second-order** term c₁(a)·L (§2.3).

(Proof and the second-order term: in progress.)

## 3. Zero law (in progress)

First observation (CERTIFIED counts, exact census n ≤ 10⁹, `scripts/z59_msplus_strat.c`, `data/z59/msplus/strat_1e9.txt.gz`):
at fixed decade, P(R(n) ≤ 2) is to first order a function of the class mean alone, ≈ exp(−0.22·mean + const) across
the groups (𝔐, units, 3|n, 5|n, 7|n, 15|n, 21|n, 35|n, 105|n). A negative-binomial fit with group variance
under-predicts the zeros of the 3|n groups by factors 10–100 — the lower tail is heavier than a mean-variance model.

## 5. Census extension (running)

`scripts/z59_msplus_census.sh` (wraps the z58 LADDER exact decider `scripts/z58_ladder_mdec.c` unchanged), 3 lanes,
chunks of 5·10¹⁰ from 10¹¹ upwards; output `data/z59/msplus/census/`.
