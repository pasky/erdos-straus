# RESIDUE_HARDNESS — the full residue-class factor E[count | p mod q] (depth lane Z0199, wave z52c)

Status: working draft (skeleton). **ES is open; nothing here proves or claims it.** Labels as in DISCOVERIES.md (PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment). Scripts `scripts/z52c_rh_*`, data `data/z52c/rh/`.
Builds on BRAINSTORM/z52b_pass1_H00.md §Z0199 (Pass-1 record), BM_CORRECTED_COUNT.md (M_BM), FRONTIER.md §2.

## 0. Summary
(to be written last)

## 1. Derivation of E[count | p ≡ r (mod q)] from local densities

Throughout p ≡ 1 (mod 4) is prime, Q is a modulus, r a unit class mod Q compatible with p ≡ 1 (4), L = log p.
The class factor is F_Q(r) := E[count(p) | p ≡ r (Q)] / (average over the admissible classes r), "count" one of
R = (★), T_II (Type II), T_I (Type I), U = (T_I + T_II)/2 (= the number of unordered solutions, see §1.1).

### 1.1 The certificate families as congruence families (PROVED; CERTIFIED identification)

Elsholtz–Tao parametrisations, written as "v lies in an arithmetic progression attached to a parameter tuple":
* **(★)** (u, B, C) ∈ ℕ³, v = 4uBC − u − B. For fixed (u, B): the AP v ≡ −(u + B) (mod 4uB), C the running index.
* **Type II** (a, b, c, d), gcd(a, b) = 1, c | a + b, s := (a + b)/c, v = 4abd − s (4/v = 1/(abd) + 1/(acdv) + 1/(bcdv)).
  For fixed (a, b, c): the AP v ≡ −s (mod 4ab), d running. (★) is c = 1.
* **Type I** (a, b, e, d), gcd(a, b) = 1, e | a + b, e·v = 4abd − 1 (4/v = 1/(abdv) + 1/(acd) + 1/(bcd), c = (a+b)/e).
  Since e | a + b, e | 4abd − 1 ⟺ e | M := 4a²d + 1; writing b = ec − a and g := M/e this is **v = 4acd − g with
  g | 4a²d + 1** — for fixed (a, d, g) the AP v ≡ −g (mod 4ad), c running (subject to b = ec − a ≥ 1).

For a prime p ≡ 1 (4) every solution of 4/p = 1/x + 1/y + 1/z has exactly one or exactly two denominators divisible by p
(k₃ = 0), and the tuple counts with gcd(a, b) = 1 are the *ordered-(y, z)* solution counts: T_I(p) = 2k₁(p),
T_II(p) = 2k₂(p), U(p) = k₁ + k₂ (no y = z solutions occur for p ≡ 1 (4)). **CERTIFIED**: `scripts/z52c_rh_types.c`
(exact tuple enumeration, Pollard-ρ factorisation of 4a²d + 1) agrees with the independent solution counter
`scripts/z52c_rh_count.c` (= z52b_fingerprint_count.c + a p ≡ 1 (4) filter) on **every** prime compared (486 primes in
(2·10⁴, 3·10⁴] and all 18 380 primes p ≡ 1 (4) of (2·10⁵, 10⁶] the counter finished — exact equality of k₁, k₂ and U); and the c = 1 coprime part equals
R from `scripts/z52c_rh_star.c`. (Without gcd(a, b) = 1 the tuples (ka, kb, kc, d/k²) repeat solutions.) So E[U | p ≡ r]
is literally a sum over parameter tuples of "probability that the tuple's AP hits p".

### 1.2 The (★) family in closed form: a secondary term of relative size 1/L (derivation; formula = CONJECTURE, EVIDENCE §2)

**Local-density sum.** For a random prime p ≈ X in class r (mod q), q an odd prime, sum over tuples the probability that the
tuple's value is p. The primes ℓ ∤ q contribute an r-independent factor (CRT), so only the distribution of tuples mod q matters.
Two kinds of pairs (u, B):

* **pairs with q ∤ uB ("level term").** As C runs, 4uBC − u − B runs through all classes mod q; the class r is hit at
  C ≡ c₀(u, B; r) := (r + u + B)(4uB)⁻¹ (mod q). If C ranged over complete periods this would be flat in r; but C starts at 1
  and the weight of level C decays like 1/C (the number of pairs with 4uBC ≤ X is ≍ (X/C) log(X/C)), so the class of c₀ matters.
  **Lemma 1 (PROVED, elementary).** For r ≢ 0 the map (u, B) ∈ (𝔽_q^×)² ↦ c₀ has fibre size 2q − 3 at c* := −(4r)⁻¹,
  q − 2 at 0, and q − 3 at every other class. *Proof.* c₀ = 0 ⟺ u + B ≡ −r: q − 2 solutions with u, B ≠ 0. For c ≠ 0,
  c₀ = c ⟺ (4cu − 1)(4cB − 1) ≡ 4cr + 1 =: k with 4cu − 1, 4cB − 1 ≠ −1. If k ≢ 0 the hyperbola xy = k has q − 1 points, of
  which those with x = −1 or y = −1 (2 points; x = y = −1 would need 4cr ≡ 0) are excluded: q − 3. If k ≡ 0 (c = c*):
  2q − 1 points on xy = 0, minus the two with x = −1 or y = −1: 2q − 3. (Total (q−2) + (q−2)(q−3) + (2q−3) = (q−1)².) ∎
  So level c* = −(4r)⁻¹ carries q extra cells: that is the level C with **q | 4Cp + 1** (divisor form of FRONTIER §2.1). With
  Σ_{C ≡ c (q), C ≤ X} (1/C) log(X/C) = (1/(2q)) L² + (−ψ(c/q)/q) L + O(1) (ψ = digamma, c ∈ {1, …, q}), the r-dependent part is
  ∝ −ψ(⟨c*⟩/q).
* **pairs with q | u (or q | B) ("pair term").** The AP v ≡ −(u + B) (mod 4uB) is constant mod q, ≡ −B (resp. −u): such a pair
  hits only the class r ≡ −B. Its expected contribution is ≍ X/(4uB) per pair (all C), so the class-r total is
  Σ_{q | u} Σ_{B ≡ −r (q)} 1/(uB), whose r-dependent constant is −ψ(⟨−r⟩/q)/q (Σ_{B ≡ b (q), B ≤ Y} 1/B = (log Y − ψ(b/q))/q + o(1)).
  (Averaging over u mod 4 — the constraint u + B ≡ 3 (4) — does not change this: by Gauss multiplication the four classes
  mod 4q above b average to −ψ(b/q) + log 4.)

Collecting densities (pairs: density 4/π², of which a fraction (q−1)/(q+1) has q ∤ uB and 1/(q+1) each has q | u, q | B; the
prime normalisation multiplies both terms and the main term by the same q/(q − 1)·∏_{ℓ|4uB, ℓ≠q} ℓ/(ℓ−1)):

  **F_q^(★)(r) = 1 + (2q/((q² + 1)·L))·(Ψ_q(r) − Ψ̄_q) + O(L⁻²),   Ψ_q(r) := −ψ(⟨−(4r)⁻¹⟩_q/q) − 2ψ(⟨−r⟩_q/q),**

⟨x⟩_q ∈ {1, …, q − 1} the least positive residue, Ψ̄_q = 3(γ + q log q/(q − 1)) (Gauss: Σ_{k<q} ψ(k/q) = −(q−1)γ − q log q).
The main term is ∝ L² (FRONTIER §2.1), so **the full-residue dependence is a secondary term, relative size 1/L**, which is why
it is invisible to every leading-order singular series (M₀, M_BM, M_gen) and decays only logarithmically.

Values of (2q/(q²+1))·(Ψ_q(r) − Ψ̄_q) (so F − 1 ≈ this/L; squares mod q marked ■, the coset that p ≡ 1 (mod q) lives in):

| q | r = 1 | others |
|---|---|---|
| 5 | ■ −0.21 | 2: −1.21, 3: −0.03, 4■: +1.45 |
| 7 | ■ −1.59 | 2■: −1.50, 3: −1.01, 4■: −0.41, 5: +1.73, 6: +2.76 |
| 11 | ■ −1.27 | 2: −0.89, 3■: −1.19, 4■: −0.18, 5■: −0.79, 6: −0.55, 7: −0.55, 8: +1.72, 9■: +0.61, 10: +3.08 |
| 13 | ■ −0.62 | 2: −1.05, 3■: +0.84, 4■: −0.64, 5: −0.95, 6: −0.72, 7: −0.55, 8: +0.33, 9■: −0.31, 10■: −0.03, 11: +0.97, 12■: +2.74 |

The pair term −2ψ(⟨−r⟩/q) is **minimal exactly at r = 1** for every q (⟨−1⟩ = q − 1 is the largest residue; −ψ is
decreasing); the level term is an unrelated function of r (c* = −(4r)⁻¹), which is why for (★) alone class 1 is the lowest
square class mod 7 and 11 but is beaten by r = 4 mod 13 at first order (§2 shows the data agree with the exact model there).
*Rigour.* Lemma 1 is PROVED. For integer averages Σ_{n ≤ X, n ≡ r} R*(n) the expansion is standard hyperbola-method lattice
counting (Assessment: provable, not written out here). For primes it needs primes in APs to moduli 4uB up to X (beyond
Bombieri–Vinogradov), so the prime statement is a CONJECTURE, tested in §2.

### 1.3 All families at once: the exact local-density model (definition; evaluated numerically)

For Types I/II the same two mechanisms operate (a shift parameter must lie in a class mod q; a level parameter starts at 1),
but the parameter space is 4-dimensional and a closed form was not derived. Instead the local-density sum is evaluated
**exactly** as a lattice sum: for every integer v in a window, enumerate all tuples hitting v and give each tuple the prime
local density of its AP — weight ∏_{ℓ | modulus, ℓ > 13} ℓ/(ℓ − 1), and weight 0 if the AP contains no units (Type II with
gcd(s, 2ab) > 1) — then average over the **13-rough composite** v ≡ 1 (4) in the class r (the factors at ℓ ≤ 13 are
implemented exactly by the roughness; composites only, so that model and prime data share no samples). This is
"Σ over parameter tuples of the local density of the congruence p ≡ a(tuple) (mod m(tuple)), restricted to the class r" with
no free parameter. Programs: `scripts/z52c_rh_star.c` ((★), all n ≤ 10⁷), `scripts/z52c_rh_types.c` (Types I, II, (★) on a
window), `scripts/z52c_rh_model.py` (class tables → `data/z52c/rh/model_tables.json`).

**Predicted factors** (model, window p ∈ [10⁶, 2·10⁶], L = 14.2; ■ = square class; the full tables for q = 3, 5, 7, 8, 11, 13,
16, 840 and the windows 10⁵, 10⁶, 5·10⁶ are in the json):

| Q | r | U model (data) | (★) model (data) | Type I model | Type II model |
|---|---|---|---|---|---|
| 3 | 1■ | 0.929 (0.930) | 0.881 (0.883) | 0.933 | 0.917 |
| 3 | 2 | 1.071 (1.070) | 1.119 (1.117) | 1.067 | 1.083 |
| 5 | 1■ | 0.902 (0.906) | 0.990 (0.990) | 0.882 | 0.953 |
| 5 | 2 | 1.101 (1.100) | 0.914 (0.914) | 1.109 | 1.083 |
| 5 | 3 | 1.050 (1.047) | 1.013 (1.016) | 1.075 | 0.986 |
| 5 | 4■ | 0.947 (0.947) | 1.083 (1.080) | 0.934 | 0.979 |
| 7 | 1■ | 0.922 (0.922) | 0.902 (0.901) | 0.931 | 0.900 |
| 7 | 2■ | 0.994 (1.000) | 0.909 (0.922) | 1.019 | 0.930 |
| 7 | 3 | 1.021 (1.016) | 0.944 (0.942) | 1.005 | 1.060 |
| 7 | 4■ | 1.073 (1.076) | 0.954 (0.958) | 1.069 | 1.082 |
| 7 | 5 | 0.994 (0.993) | 1.117 (1.111) | 0.991 | 1.003 |
| 7 | 6 | 0.996 (0.993) | 1.174 (1.166) | 0.985 | 1.025 |
| 8 | 1 | 0.874 (0.876) | 0.984 (0.983) | 0.851 | 0.933 |
| 8 | 5 | 1.126 (1.124) | 1.016 (1.017) | 1.149 | 1.067 |
| 11 | 1■ | 0.940 (0.940) | 0.934 (0.938) | 0.942 | 0.935 |
| 11 | 2 | 0.976 (0.975) | 0.952 (0.950) | 0.976 | 0.977 |
| 11 | 3■ | 0.991 (0.995) | 0.941 (0.940) | 0.999 | 0.974 |
| 11 | 4■ | 1.016 (1.017) | 0.985 (0.983) | 1.013 | 1.024 |
| 11 | 5■ | 0.953 (0.952) | 0.945 (0.954) | 0.955 | 0.948 |
| 11 | 6 | 0.983 (0.983) | 0.970 (0.971) | 0.984 | 0.980 |
| 11 | 7 | 1.057 (1.054) | 0.972 (0.967) | 1.066 | 1.035 |
| 11 | 8 | 1.129 (1.123) | 1.108 (1.104) | 1.118 | 1.158 |
| 11 | 9■ | 0.946 (0.952) | 1.014 (1.023) | 0.946 | 0.949 |
| 11 | 10 | 1.008 (1.008) | 1.179 (1.170) | 1.002 | 1.020 |
| 13 | 1■ | 0.953 (0.955) | 0.969 (0.956) | 0.950 | 0.962 |
| 13 | 2 | 1.015 (1.012) | 0.948 (0.951) | 1.020 | 1.000 |
| 13 | 3■ | 0.975 (0.975) | 1.046 (1.050) | 0.968 | 0.992 |
| 13 | 4■ | 1.011 (1.004) | 0.969 (0.968) | 1.024 | 0.976 |
| 13 | 5 | 0.971 (0.974) | 0.954 (0.954) | 0.972 | 0.966 |
| 13 | 6 | 1.046 (1.053) | 0.962 (0.966) | 1.044 | 1.051 |
| 13 | 7 | 1.003 (0.998) | 0.977 (0.978) | 1.013 | 0.977 |
| 13 | 8 | 0.973 (0.972) | 1.027 (1.033) | 0.975 | 0.969 |
| 13 | 9■ | 0.972 (0.974) | 0.980 (0.974) | 0.965 | 0.991 |
| 13 | 10■ | 1.087 (1.080) | 0.978 (0.982) | 1.069 | 1.134 |
| 13 | 11 | 1.019 (1.018) | 1.066 (1.065) | 1.030 | 0.992 |
| 13 | 12■ | 0.975 (0.986) | 1.125 (1.124) | 0.970 | 0.989 |
| 16 | 1 | 0.838 (0.839) | 0.971 (0.970) | 0.813 | 0.900 |
| 16 | 5 | 1.095 (1.093) | 1.021 (1.020) | 1.128 | 1.010 |
| 16 | 9 | 0.911 (0.914) | 0.996 (0.997) | 0.889 | 0.966 |
| 16 | 13 | 1.157 (1.154) | 1.011 (1.013) | 1.170 | 1.123 |
| 840 | 1 (Mordell sq.) | 0.542 (0.557) | 0.648 (0.657) | 0.509 | 0.627 |
| 840 | 121 (Mordell sq.) | 0.574 (0.592) | 0.669 (0.701) | 0.541 | 0.657 |
| 840 | 169 (Mordell sq.) | 0.580 (0.591) | 0.693 (0.704) | 0.548 | 0.662 |
| 840 | 289 (Mordell sq.) | 0.599 (0.617) | 0.676 (0.723) | 0.569 | 0.673 |
| 840 | 361 (Mordell sq.) | 0.588 (0.596) | 0.665 (0.682) | 0.553 | 0.679 |
| 840 | 529 (Mordell sq.) | 0.612 (0.632) | 0.690 (0.718) | 0.577 | 0.699 |

mod 840 (96 classes p ≡ 1 (4)): U-model range 0.542 (r = 1) … 1.612 (r = 557); mean over the 6 Mordell squares 0.583.

Reading: the model predicts the data class means (in brackets) to within their noise — §2.1. **Class 1 is the lowest admissible
class of all 96 classes mod 840** (U factor 0.54; the other five Mordell squares 0.57–0.61; the easiest class 1.61), and the
lowest square class mod 5, 7, 11, 13 for U, with p ≡ 1 (16) the lowest class mod 16. Factors for the Pass-1 window (p ≤ 2·10⁵)
are larger by ≈ L(10⁶)/L(p) (the 1/L law; `scripts/z52c_rh_regress.py` prints (F − 1)·L per window: constant to ±5–10 %).
Typical sizes at p ≈ 10⁶: one small prime q | p − 1 costs 5–10 %; p ≡ 1 (840) costs a factor ≈ 0.54.

## 2. Predictions against data
(TODO)

## 3. Why the class of 1 is hardest
(TODO)

## 4. Scope and consequences
(TODO)

## 5. Review log
(TODO)
