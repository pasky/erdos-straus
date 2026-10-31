# RESIDUE_HARDNESS — the full residue-class factor E[count | p mod q] (depth lane Z0199, wave z52c)

Status: depth lane Z0199, complete pending review. **ES is open; nothing here proves or claims it.** Labels as in DISCOVERIES.md (PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment). Scripts `scripts/z52c_rh_*`, data `data/z52c/rh/`.
Builds on BRAINSTORM/z52b_pass1_H00.md §Z0199 (Pass-1 record), BM_CORRECTED_COUNT.md (M_BM), FRONTIER.md §2.

## 0. Summary
1. **CERTIFIED** Type I/II tuple counts = solution counts (U = k₁ + k₂) at all 30 198 primes p ≡ 1 (4) in (2·10⁵, 10⁶] (§1.1).
2. **PROVED** Lemma 1 (level-cell counts) and Lemma 2 (shift alignment: for p ≡ 1 (q) each q-divisible-modulus Type I/II certificate
   needs shift ≡ −1 (mod 4q), the latest class; in (★) shift ≡ −1 (mod q); §1.2, §3).
3. **CONJECTURE** (★) closed form F_q(r) = 1 + 2q/((q²+1)L)·(Ψ_q(r) − Ψ̄_q), Ψ = −ψ(⟨−(4r)⁻¹⟩/q) − 2ψ(⟨−r⟩/q): a 1/L secondary term, invisible to M₀/M_BM/M_gen.
4. **EVIDENCE** The parameter-free local-density model fits all class means mod 3, 5, 7, 8, 11, 13, 16, 840 for U, (★), Types I/II:
   mean squared standardized discrepancy 0.75–1.13 vs 29–2 800 for "no class effect" (to 157 987 primes). Class 1 is lowest of 96 mod 840.
5. **EVIDENCE** In the Pass-1 regression, 1[7 | p−1]: −0.131(6) → +0.010(5); all indicators |·| ≤ 0.02 (≤ 0.009 out of sample to 10⁷).
   log F adds R² 0.11–0.19 beyond 25 characters. It absorbs the mod-840 ordering and 67–100 % of Z0900 (practical p − 1) (§2.2).
6. **EVIDENCE** (★) model M′ = M_BM·F_S/F_MBM: corr with log R 0.49 → 0.71, z-sd 1.37 → 1.07 (better mean model); zero law mixed:
   [10⁵, 10⁶) 3 zeros vs 3.2 expected (M_BM: 0.5), but < 10⁵ 4 vs 21.9. All 14 (★) failures ≤ 10⁷ are ≡ 1 (24), mostly in low-F classes.
7. **Assessment** p ≡ 1 (Q) forces x ≡ (m+1)/4 (Q) for the p-free denominator x = (p+m)/4, so cheap windows lose small-prime
   divisors. Main-term refinement only; B3/B6 untouched. Verification should oversample p ≡ 1 (mod 840·16) (§3–4).

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
(2·10⁴, 3·10⁴] and all 30 198 primes p ≡ 1 (4) of (2·10⁵, 10⁶] — exact equality of k₁, k₂ and U;
`scripts/z52c_rh_crosscheck.py`, counter output `data/z52c/rh/U_counter_2e5_1e6.txt.gz`); and the c = 1 coprime part equals
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
  Σ_{C ≡ c (q), C ≤ X} (1/C) log(X/C) = (1/(2q)) L² − ((log q + ψ(c/q))/q) L + O(1) (ψ = digamma, c ∈ {1, …, q}), the
  r-dependent part is ∝ −ψ(⟨c*⟩/q) (the log q cancels between classes).
* **pairs with q | u (or q | B) ("pair term").** The AP v ≡ −(u + B) (mod 4uB) is constant mod q, ≡ −B (resp. −u): such a pair
  hits only the class r ≡ −B. Its expected contribution is ≍ X/(4uB) per pair (all C), so the class-r total is
  Σ_{q | u} Σ_{B ≡ −r (q)} 1/(uB), whose r-dependent constant is −ψ(⟨−r⟩/q)/q (Σ_{B ≡ b (q), B ≤ Y} 1/B = (log Y − log q − ψ(b/q))/q + o(1)).
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
local density of its AP — weight ∏ over the *distinct* primes ℓ > 13 of the AP modulus of ℓ/(ℓ − 1), and weight 0 if the AP contains
no units (Type II with gcd(s, 2ab) > 1); each *ordered* tuple uses its own AP (Type I (a, b, e, d): modulus 4ad; its mirror
(b, a, e, d): 4bd) — then average over the **13-rough composite** v ≡ 1 (4) in the class r (the factors at ℓ ≤ 13 are
implemented exactly by the roughness; composites only, so that model and prime data share no samples). This is
"Σ over parameter tuples of the local density of the congruence p ≡ a(tuple) (mod m(tuple)), restricted to the class r" with
no free parameter. Programs: `scripts/z52c_rh_star.c` ((★), all n ≤ 10⁷), `scripts/z52c_rh_types.c` (Types I, II, (★) on a
window), `scripts/z52c_rh_model.py` (class tables → `data/z52c/rh/model_tables.json`).

**Predicted factors** (model, window p ∈ [10⁶, 2·10⁶], L = 14.2; ■ = square class; the full tables for q = 3, 5, 7, 8, 11, 13,
16, 840 and the windows 10⁵, 10⁶, 5·10⁶ are in the json):

| Q | r | U model (data) | (★) model (data) | Type I model | Type II model |
|---|---|---|---|---|---|
| 3 | 1■ | 0.929 (0.930) | 0.881 (0.883) | 0.934 | 0.917 |
| 3 | 2 | 1.071 (1.070) | 1.119 (1.117) | 1.066 | 1.083 |
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
| 11 | 3■ | 0.992 (0.995) | 0.941 (0.940) | 0.999 | 0.974 |
| 11 | 4■ | 1.016 (1.017) | 0.985 (0.983) | 1.013 | 1.024 |
| 11 | 5■ | 0.953 (0.952) | 0.945 (0.954) | 0.955 | 0.948 |
| 11 | 6 | 0.983 (0.983) | 0.970 (0.971) | 0.983 | 0.980 |
| 11 | 7 | 1.058 (1.054) | 0.972 (0.967) | 1.066 | 1.035 |
| 11 | 8 | 1.129 (1.123) | 1.108 (1.104) | 1.118 | 1.158 |
| 11 | 9■ | 0.946 (0.952) | 1.014 (1.023) | 0.946 | 0.949 |
| 11 | 10 | 1.008 (1.008) | 1.179 (1.170) | 1.002 | 1.020 |
| 13 | 1■ | 0.953 (0.955) | 0.969 (0.956) | 0.950 | 0.962 |
| 13 | 2 | 1.015 (1.012) | 0.948 (0.951) | 1.020 | 1.000 |
| 13 | 3■ | 0.975 (0.975) | 1.046 (1.050) | 0.968 | 0.992 |
| 13 | 4■ | 1.011 (1.004) | 0.969 (0.968) | 1.024 | 0.976 |
| 13 | 5 | 0.970 (0.974) | 0.954 (0.954) | 0.972 | 0.966 |
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
| 840 | 169 (Mordell sq.) | 0.581 (0.591) | 0.693 (0.704) | 0.548 | 0.662 |
| 840 | 289 (Mordell sq.) | 0.599 (0.617) | 0.676 (0.723) | 0.570 | 0.673 |
| 840 | 361 (Mordell sq.) | 0.589 (0.596) | 0.665 (0.682) | 0.553 | 0.679 |
| 840 | 529 (Mordell sq.) | 0.612 (0.632) | 0.690 (0.718) | 0.577 | 0.699 |

mod 840 (96 classes p ≡ 1 (4)): U-model range 0.542 (r = 1) … 1.612 (r = 557); mean over the 6 Mordell squares 0.583.

Reading: the model predicts the data class means (in brackets) to within their noise — §2.1. **Class 1 is the lowest admissible
class of all 96 classes mod 840** (U factor 0.54; the other five Mordell squares 0.57–0.61; the easiest class 1.61), and the
lowest square class mod 5, 7, 11, 13 for U, with p ≡ 1 (16) the lowest class mod 16. Factors for the Pass-1 window (p ≤ 2·10⁵)
are larger by ≈ L(10⁶)/L(p) (the 1/L law; `scripts/z52c_rh_regress.py` prints (F − 1)·L per window: constant to ≈ 5–10 % from 10⁵ to 5·10⁶, e.g. U, q = 7, r = 1: −1.02, −1.10, −1.11).
Typical sizes at p ≈ 10⁶: one small prime q | p − 1 costs 5–10 %; p ≡ 1 (840) costs a factor ≈ 0.54.

## 2. Predictions against data

Data = exact counts at every prime p ≡ 1 (4) in (100, 2·10⁶] and [5·10⁶, 10⁷] (U, T_I, T_II from `z52c_rh_types.c`, 74 405 + 157 987 primes; cross-checked with
the solution counter, §1.1) and R at all primes ≤ 10⁷ (`z52c_rh_star.c`). Pass-1 used 8 966 primes ≤ 2·10⁵.

### 2.1 Class means (EVIDENCE; `scripts/z52c_rh_model.py`)

Over all 136 admissible classes for Q ∈ {3, 5, 7, 8, 11, 13, 16, 840} and the four families, (data − model)/SE, with SE the
combined sampling error of the prime means and of the (composite-sample) model means. MSSD = mean of the squared standardized
discrepancies — a *descriptive* statistic, not a calibrated χ² test: the SEs treat class means as independent, ignore the
error of the normalising mean, and classes of different Q overlap; 96 of the 136 classes are the thin mod-840 ones (R-review).

| window | primes | family | rms(data − model) | rms SE | MSSD (model) | MSSD (flat F ≡ 1) |
|---|---|---|---|---|---|---|
| [10⁵, 2·10⁵] | 4 194 | U | 0.034 | 0.034 | 1.07 | 92 |
| | | (★) | 0.047 | 0.050 | 0.85 | 29 |
| | | Type I / II | 0.037 / 0.036 | 0.035 / 0.040 | 1.13 / 0.86 | 115 / 42 |
| [10⁶, 2·10⁶] | 35 241 | U | 0.0097 | 0.0114 | 0.80 | 593 |
| | | (★) | 0.015 | 0.016 | 0.76 | 185 |
| | | Type I / II | 0.011 / 0.010 | 0.012 / 0.013 | 0.84 / 0.78 | 721 / 263 |
| [5·10⁶, 10⁷] | 157 987 | U | 0.0049 | 0.0053 | 0.86 | 2 315 |
| | | (★) | 0.0062 | 0.0073 | 0.75 | 729 |
| | | Type I / II | 0.0048 / 0.0059 | 0.0054 / 0.0062 | 0.78 / 0.98 | 2 823 / 988 |

**The local-density model accounts for the class means of every family to within sampling error** (MSSD ≈ 1 against
hundreds for “no class dependence”). Without the 96 mod-840 classes (40 classes, q ≤ 16) the MSSD is 0.44–0.85 (U: 0.85, 0.48,
0.72 in the three windows), so the agreement is not an artefact of the thin classes; the q ≤ 16 rows of the §1.3 table match to
≈ 0.005. The (★) closed form of §1.2 (first order only) is cruder:
at 10⁶ it gives 0.888 / 0.894 / 0.971 for r = 1 / 2 / 4 mod 7 against model 0.902 / 0.909 / 0.954 and data 0.901 / 0.922 / 0.958 —
right ordering and size, ≈ 0.01–0.02 off (attributed to the neglected higher-order terms; not verified to be O(L⁻²)).

### 2.2 The Pass-1 regression with the factor added (EVIDENCE; `scripts/z52c_rh_regress.py` → `data/z52c/rh/regress.json`)

Pass-1 design: y = log(U + 1) on 1, log p, log log p, (q/p) for primes q < 80, plus the indicators 1[q | p − 1] (q = 5, 7,
11, 13) and 1[16 | p − 1]. "After" = the same fit to y − log F(p), with **no fitted parameter in F**: log F(p) =
log F_840(p mod 840) + log F_16 − log F_8 + log F_11 + log F_13 from the 10⁶-window model table, each factor rescaled to p by
the 1/L law (F − 1 ∝ 1/log p; across the windows 10⁵ and 10⁶ (F − 1)·L is constant to 5–10 % across the windows 10⁵, 10⁶, 5·10⁶).

| p range (primes ≡ 1 (4)) | 1[5\|p−1] | 1[7\|p−1] | 1[11\|p−1] | 1[13\|p−1] | 1[16\|p−1] | R² gain of indicators | coefficient of log F if free |
|---|---|---|---|---|---|---|---|
| ≤ 2·10⁵ (Pass-1 set), before | −0.058(6) | **−0.131(6)** | −0.057(8) | −0.052(8) | −0.095(6) | 0.0208 | |
| ≤ 2·10⁵, after | +0.012(5) | +0.010(5) | −0.007(6) | +0.019(6) | +0.020(5) | 0.0006 | 0.814(9) |
| (2·10⁵, 2·10⁶], before | −0.049(2) | −0.106(2) | −0.042(3) | −0.047(3) | −0.078(2) | 0.0293 | |
| (2·10⁵, 2·10⁶], after | +0.002(2) | +0.003(2) | −0.002(2) | +0.005(2) | +0.009(2) | 0.0002 | 0.918(5) |
| [5·10⁶, 10⁷], before | −0.045(1) | −0.095(1) | −0.036(2) | −0.042(2) | −0.070(1) | 0.0334 | |
| [5·10⁶, 10⁷], after | −0.002(1) | +0.001(1) | −0.002(1) | +0.002(2) | +0.005(1) | 0.00006 | 0.958(3) |

* **Yes: the factor predicts the −0.13 at q = 7** (and every other indicator): 96–99 % of the indicators' explained variance
  is absorbed with no fitted parameter. The leftover +0.01–0.02 in the small-p range is an overshoot of the 1/L extrapolation
  below 10⁴ and the log(U+1) attenuation (free coefficient 0.82 rather than 1; 0.92 out of sample).
* log F explains **R² = 0.114** beyond the 25 characters (≤ 2·10⁵; 0.168 on (2·10⁵, 2·10⁶], 0.187 on [5·10⁶, 10⁷]), five times what the
  indicators did (0.021): the full residue factor contains the character *interactions* (all of p's characters mod 3, 5, 7, 8
  jointly) that a linear character model cannot represent. With the prime-by-prime product F₃F₅F₇F₁₆F₁₁F₁₃ instead of the joint
  mod-840 table the indicators are absorbed equally well but the gain is only 0.046 and the Mordell squares stay ≈ −0.25 too low.
* Square classes mod 7, mean residual before → after (≤ 2·10⁵): r = 1: −0.087 → +0.006, r = 2: +0.008 → +0.004, r = 4: +0.079 → −0.010.
* The six Mordell squares mod 840 (≤ 2·10⁵, 79–90 primes each): before −0.37 (r = 1), −0.31, −0.26, −0.21, −0.27, −0.22;
  after +0.11, +0.03, +0.08, +0.08, +0.04, +0.04; out of sample ((2·10⁵, 2·10⁶], ≈ 665 each): before −0.29 (r = 1) … −0.16,
  after +0.006 … +0.022; [5·10⁶, 10⁷] (≈ 1 630 each): before −0.245 (r = 1), −0.196, −0.187, −0.152, −0.180, −0.135,
  after −0.003 … +0.008. **The class-1-lowest ordering mod 840 is predicted** (model: r = 1 is the lowest of all 96 classes) and
  removed by the factor.
* Number of q ∈ {3, 5, 7, 11, 13} dividing p − 1 (0 … 4), mean residual before: +0.014, +0.029, −0.037, −0.132, −0.279;
  after: −0.003, −0.002, +0.004, +0.022, −0.031 (n = 49 at 4). Out of sample, 4 divisors: −0.214 → −0.028 (n = 332) and −0.198 → −0.038 (n = 768, [5·10⁶, 10⁷]).
* **Unexplained variance.** Residual sd of log(U+1) after characters: 0.209; after characters + log F (free coefficient): 0.150
  (≤ 2·10⁵); 0.197 → 0.154 on (2·10⁵, 2·10⁶], 0.190 → 0.156 on [5·10⁶, 10⁷] (the prime-product variant gives only 0.209 → 0.187).
  What remains is not explained by the tested residue factors or indicators (adding the five indicators back gains R² ≤ 0.0006);
  presumably mostly prime-specific (T(p)-type Legendre sums, higher-order characters, X_BM), though untested moduli (9, 17, 19, …)
  and further interactions remain possible.

**Z0900 ("p − 1 practical" correlates with hardness; Pass-1 U01) is the same effect.** In the same design, the coefficient
of 1[p − 1 practical] is −0.098(12) → −0.004(9) after the factor for p ≤ 3·10⁴, −0.088(5) → −0.015(4) for p ≤ 2·10⁵ and
−0.067(2) → −0.018(1) on (2·10⁵, 2·10⁶], −0.061(1) → −0.020(1) on [5·10⁶, 10⁷]: 67–100 % explained. Practicality of p − 1 means p − 1 divisible by 2 and by many small primes,
i.e. p close to 1 in Ẑ; a small leftover (−0.015) presumably comes from moduli beyond 16·840·11·13 (e.g. 9, 17, 19 | p − 1, not in F).
*Correction to the Z0900 record:* its "0 of the top-30 hardest primes have practical p − 1" ranks by *largest* U
(`sorted(..., key=-U4)` in `scripts/z52b_p1_U01_practical.py`), i.e. the 30 *easiest*; in our design 29 of the 30 primes with the
lowest residual have practical p − 1 (22 after the factor), consistent with the sign of the mean effect.

### 2.3 The factor in the (★) hardness model (EVIDENCE; `scripts/z52c_rh_hard.py` → `data/z52c/rh/hard.json`)

M_BM already contains part of the class dependence (the Brauer character χ_{−4uB}(p) through T(p)), so the refinement is
**M′(p) := M_BM(p)·F_S(p)/F_MBM(p)**, F_S the (★) model factor (840·16/8·11·13, 1/L-rescaled) and F_MBM the class factor of
M_BM itself (class means of M_BM over primes in [2·10⁵, 10⁶], same components; no R data enters M′). (Using F_S without the
division double-counts the Brauer part: expected zeros 40 instead of 25 below.) 39 095 primes p ≡ 1 (4) in (10³, 10⁶]:

| statistic | M_BM | M′ = M_BM·F_S/F_MBM |
|---|---|---|
| corr(log(R + 1), log M) | 0.486 | **0.712** |
| swap-Poisson log-likelihood Σ log P(R/2 \| M/2) | −122 716 | **−110 967** |
| sd of z = (R − M)/√(2M) | 1.37 | **1.07** |
| min z (argmin) | −3.31 (329 617) | −2.86 (963 481) |
| share of primes with R < M/2 | 2.8 % | 1.1 % |
| free fit log(R+1) ~ a + b log M_BM + c log F | | b = 0.88, c = 0.96 |

So the factor removes most of the excess dispersion that BM_CORRECTED_COUNT §3.2 recorded (sd 1.37 → 1.07, i.e. close to
swap-Poisson), and its coefficient in a free fit is ≈ 1. **Zero law by range** (swap-Poisson, P(R = 0) = e^{−M/2}):

| p range | primes | (★) zeros observed | expected under M_BM | expected under M′ |
|---|---|---|---|---|
| [10³, 10⁴) | 529 | 2 | 6.1 | 12.9 |
| [10⁴, 10⁵) | 4 174 | 2 | 2.4 | 9.0 |
| [10⁵, 3·10⁵) | 8 197 | 1 | 0.35 | 2.1 |
| [3·10⁵, 10⁶) | 26 195 | 2 | 0.14 | 1.1 |

**The zero law under M′ is mixed** (R-review repair). Above 10⁵ the failures are no longer surprising under M′ (3 observed vs
3.2 expected; 0.49 under M_BM) — but that is only 3 events, i.e. limited evidence. Below 10⁵ the swap-Poisson zero law with M′
is **sharply rejected**: 4 observed vs 21.9 expected (P(N ≤ 4) ≈ 4·10⁻⁶ under independent Poisson); likely causes are the 1/L
extrapolation of F from L ≈ 14 down to L ≈ 7–11 (overshoot) and under-dispersion there (sd z = 0.76–0.92), but explaining the
failure does not make it uninformative: M′ is a better *mean* model, not a validated *zero* model. (BM_CORRECTED §3.2's
"possibly fatter far tail" was measured on odd non-squares with M_BM8, not on this prime/M_BM sample, so it is not directly
the quantity compared here.)

**The 14 (★) failures p ≡ 1 (4) ≤ 10⁷** (409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201,
5212561, 8813281; recomputed from `z52c_rh_star.c`, = the FRONTIER census list ≤ 10¹⁰): all 14 are ≡ 1 (mod 24) (p ≡ 1 mod 8
and mod 3), 10 of 14 are ≡ 1 (16), 9 lie in a Mordell class mod 840, three in class 1 itself (712321, 1726201, 8813281 —
p − 1 divisible by 3·5·7), and 11 have a second odd prime ≤ 19 dividing p − 1 (base rates among p ≡ 1 (4): 1/4 for ≡ 1 (24), 0.54 for the latter among p ≡ 1 (24)). The refined factor F_S/F_MBM at the failures is 0.57–0.82 (409, 577 excluded: p < 10³); the 7 failures in (10³, 10⁶] sit at the 0.2, 1.1, 1.5, 3.8, 4.1, 18.6, 22.6 % quantiles of F among those primes (median 3.8 %). Total surprise Σ M/(2 log 10) of the 12 failures > 10³: 48.5 decades under M_BM,
36.2 under M′. The hard primes by U are similar: F_U = 0.17 at 2521 (= lcm(1..10) + 1, the hardest prime ≤ 2·10⁵),
0.37 / 0.39 at the Type-A failures 193 / 66529, 0.31 at 5569 and 9601. Among the 1 % of primes with the lowest R/M_BM the mean
log F is −0.33 (all primes: −0.03); 5 of the 7 zeros in (10³, 10⁶] are in the lowest-F decile, which carries 67 % of the
expected zeros under M′ (33 % under M_BM).

Reading (Assessment): the residue factor is the dominant *predictable* component of hardness beyond M_BM; the failures are not
explained away (they still sit 1.5–5 decades into the Poisson tail individually), but their location is: the (★)-failures
and the U-hard primes are, almost without exception, p ≡ 1 modulo 8 and modulo several small odd primes.

## 3. Why the class of 1 is hardest

**Lemma 2 (shift alignment; PROVED, elementary).** Let q be an odd prime, p ≡ 1 (4) a prime with q ∤ p. In each family
consider the tuples whose AP modulus is divisible by q ("pair term": q | u or q | B in (★); q | ab in Type II; q | ad in
Type I). Such a tuple hits p only if its *shift* σ — σ = B resp. u in (★), σ = s = (a+b)/c in Type II, σ = g in Type I
(v = 4acd − g) — satisfies σ ≡ −p (mod q); in Types I and II moreover σ ≡ 3 (mod 4). Hence for p ≡ r (mod q):
(a) Types I/II: σ ≡ σ_r (mod 4q), σ_r the unique class with σ_r ≡ 3 (4), σ_r ≡ −r (q). As r runs over the units mod q,
⟨σ_r⟩_{4q} runs over {t ≤ 4q − 1 : t ≡ 3 (4), q ∤ t}, and **⟨σ_r⟩_{4q} = 4q − 1, the maximum, iff r = 1**.
(b) (★): σ ≡ −r (mod q), and ⟨−r⟩_q = q − 1, the maximum, iff r = 1.
*Proof.* (★): if q | u then 4uBC − u − B ≡ −B. Type II: if q | ab then v = 4abd − s ≡ −s (mod q), and v ≡ −s (mod 4).
Type I: if q | ad then v = 4acd − g ≡ −g (mod q), and v ≡ −g (mod 4). With v = p ≡ 1 (4): σ ≡ 3 (4). The rest is CRT. ∎

Since the pair-term weight of the shift class is Σ_{σ ≡ σ_r} 1/σ (times smooth factors), whose class-dependent part is
−ψ(⟨σ_r⟩/(4q)) — decreasing in ⟨σ_r⟩ — **the pair term is smallest for r = 1, in every family and for every q**:
the "first" pair-term certificate in class 1 has shift 4q − 1 instead of 3, 7, 11, … (Assessment for the size statement;
Lemma 2 itself is PROVED). The same in the divisor language of the p-free denominator x = (p + m)/4, m = 4x − p ≡ 3 (4):
**q | x ⟺ m ≡ −p (mod q)**, so for p ≡ 1 (mod q) the windows m = 3, 7, …, 4q − 5 never have q | x. More globally, if
p ≡ 1 (mod Q) (Q odd) then x ≡ (m + 1)/4 (mod Q): **the p-free denominator of the m-th window is congruent mod Q to the
small integer k = (m + 1)/4**, so its divisibility by the primes of Q is exactly that of k — deterministic and minimal for
small k — instead of the random 1/q of a generic p. A random x gains a factor ≈ (3q − 1)/(q − 1) in divisor-type counts from
q | x; class 1 forfeits this gain in all the cheap windows. This is "p ≡ 1 (q) makes p + m ≡ 1 + m".

*Decomposition check* (EVIDENCE, `scripts/z52c_rh_decomp.py`, q = 7, window [10⁶, 2·10⁶]; contributions to F_7(r) for U):

| r mod 7 | 1■ | 2■ | 3 | 4■ | 5 | 6 |
|---|---|---|---|---|---|---|
| least shift ⟨σ_r⟩_{28} | 27 | 19 | 11 | 3 | 23 | 15 |
| pair term (7 \| modulus) | **0.148** | 0.228 | 0.218 | 0.295 | 0.201 | 0.200 |
| level term (rest) | 0.774 | 0.766 | 0.802 | 0.777 | 0.794 | 0.796 |
| total F_7 | 0.922 | 0.994 | 1.020 | 1.073 | 0.994 | 0.996 |

The class-1 deficit (−0.078 against the mean) is ≈ 85 % pair term (−0.067), and the pair term orders the extreme classes as
Lemma 2 says (largest least-shift 27 → lowest; least-shift 3 → highest); the middle classes are also shaped by
the Type-I shift g being a divisor of 4a²d + 1 (not a free variable). The level term (q | 4Cp + 1 at level C ≡ −(4r)⁻¹ in (★),
Lemma 1) is a different function of r and nearly flat for U.

**Relation to Mordell's square classes and to p − 1 (Assessment).** Mordell's identities cover every class mod 840 except the
six squares {1, 121, 169, 289, 361, 529}; a polynomial identity is a certificate AP whose modulus divides 840, i.e. pair terms
for q | 840 with a tiny shift. The quadratic (Brauer) character explains why the *square coset* is uncovered (χ_{−4uB}(p) = −1
is forced at every hit, BM_CORRECTED Thm 1.1); Lemma 2 explains the ordering *inside* the coset: class 1 has, for every q | 840,
the largest least shift, so it is the last class that cheap families reach — the count-level, graded form of the
class-of-one sterility of ident_numerators Lemma 3.1 (Pass-1 Z0199). Since the effect is multiplicative over q at first order
(plus interactions captured by the joint mod-840 table), the hardness grows with the number of small q | p − 1: the
"highly composite / practical / smooth p − 1" observations (Z0199's monotone table, Z0900, fingerprint item 11 on
lcm(1..k) + 1) are all this one factor (§2.2: the monotone −0.28 at four divisors becomes −0.03). Note the effect is not
about p − 1 being smooth per se but about p − 1 being divisible by the *small* primes (and by 16): a large prime factor of p − 1
is irrelevant at this order.

## 4. Scope and consequences

* **This is a main-term refinement, not an existence argument.** The factor is a secondary term of relative size O(1/L) for
  each fixed q (§1.2; (F − 1)·L stable across windows): for fixed Q it tends to 1, so Theorem 2.2 of BM_CORRECTED (M_BM ≫ L²)
  and the scale of every main term are unchanged. It says nothing about the single-integer lower tail: H⁻_BM is exactly as
  open as before (barrier B3), and nothing here averages over p in a way that bears on a fixed p beyond prediction (B6
  respected: the factor is a deterministic function of p mod 840·16·11·13 and of log p, evaluated pointwise).
* **Uniformity in Q is not established.** For p ≡ 1 modulo all primes ≤ y the first-order factors multiply to
  ≈ ∏_{q ≤ y}(1 − c_q/L); for (★), §1.2 gives c_q = (2q/(q²+1))·(Ψ̄_q − Ψ_q(1)) = (6 + o(1))·(log q)/q (Ψ̄_q ∼ 3 log q, Ψ_q(1) = O(1)), so log F ≈ −(6 + o(1))·log y/L;
  for lcm(1..k) + 1 primes (y ≈ log p) this is −O(log log p/log p) → 0, but the first-order expansion is not justified when the
  product is far from 1 (2521: F_U = 0.17 at L = 7.8). Whether F_Q stays bounded below uniformly in Q is open (CONJECTURE: yes,
  F ≥ c > 0 for p ≥ p₀, because the deficit is confined to the shifts below 4q).
* **Heuristic P(ES false).** Under the swap-Poisson heuristic with M′ = M_BM·F_S/F_MBM the expected number of (★) failures beyond
  X is Σ_{p > X} exp(−M′(p)/2) with M′ ≥ (1 − o(1))·M_BM·(min F) — still summable (M′ ≍ L² since F → 1), so the qualitative
  conclusion "finitely many (★) failures, expected count beyond 10¹⁰ ≪ 1" is unchanged, while the expected tail mass moves
  into the low-F classes (§2.3: 67 % of the expected zeros in the lowest-F decile). The refinement *raises* the heuristic
  failure probability at the hardest classes by a factor exp(M_BM(1 − F)/2) — e.g. ≈ e^{3.3} ≈ 27 at 8 813 281 — and makes the
  observed failures above 10⁵ consistent with the model (3 vs 3.2 expected) where M_BM alone expected 0.5 — three events only,
  and below 10⁵ the same zero law overpredicts (4 vs 21.9), so this is not a validated failure model. (Assessment;
  this is a statement about a heuristic, not about ES, and the full Type I ∪ II count U ≫ R is not modelled for zeros here.)
* **Which primes a verification must stress-test.** Rank candidates by M_BM·F (or by F alone): primes p ≡ 1 (mod 840·16) with
  further small q | p − 1 (11, 13, 17, 19, …), i.e. p = 1 + (highly divisible number): lcm(1..k) + 1, primorial-type
  1 + 2⁴·3·5·7·…·m, and p ≡ 1 (mod 2⁵·3·5·7·11·13 = 480480). Concretely, a sieve-and-test search for (★)/U failures beyond the
  census should oversample p ≡ 1 (mod 840) (≈ 1/96 of primes p ≡ 1 (4), carrying a factor ≈ 0.54 in the expected count) and
  especially the intersection with p ≡ 1 (16), 1 (11), 1 (13). Fingerprint item 12's candidate 232 792 561 = lcm(1..19) + 1 is the
  extreme example; its F is far outside the fitted range and it should be computed directly, not predicted.
* **What is new here (Assessment).** The repo's main terms (M₀, M_BM, M_gen) are leading-order singular series and are blind to
  the full residue class by construction (M₀ depends on p only through its size; M_BM, M_gen only through characters). The
  residue factor is the next term of the local-density expansion; it is not a new character, it is the boundary of the
  hyperbolic parameter region (digamma constants) meeting the congruence class of p.

## 5. Reproduction

```
mkdir -p /tmp/rh; ulimit -v 8000000
gcc -O2 -o /tmp/rh/star scripts/z52c_rh_star.c && /tmp/rh/star 10000000 /tmp/rh/s1e7          # (★) R, RW for n ≤ 1e7 (3 s)
scripts/z52c_rh_runtypes.sh   # all Types I/II/(★) windows (20-way parallel, ≈ 10 min) -> /tmp/rh/{t2e5full,t1e6,t2e6,q7e6,t1e7}_*
gcc -O2 -o /tmp/rh/mbm scripts/z38_mbm.c -lm && /tmp/rh/mbm 3 1000000 0 > /tmp/rh/mbm_1e6.txt     # M_BM (≈ 15 min)
for p in 1134241 1724209 1726201 5212561 8813281; do /tmp/rh/mbm $p $p 0; done > /tmp/rh/mbm_fail.txt
scripts/z52c_rh_runU.sh   # independent solution counter, (2e5, 1e6] (≈ 30 min on 20 cores); then scripts/z52c_rh_crosscheck.py
uv run --with numpy --with scipy python scripts/z52c_rh_model.py     # §1.3/§2.1 -> data/z52c/rh/model_tables.json
uv run python scripts/z52c_rh_table.py                                # §1.3 table
uv run --with numpy --with sympy python scripts/z52c_rh_regress.py   # §2.2 -> data/z52c/rh/regress.json
uv run --with numpy --with scipy python scripts/z52c_rh_hard.py      # §2.3 -> data/z52c/rh/hard.json
uv run --with numpy python scripts/z52c_rh_decomp.py                 # §3 -> data/z52c/rh/decomp_q7.json
```

## 6. Review log

**Cross-model hostile review** (openai-codex/gpt-6-astra, 2026-10-31; no CRITICAL findings; all reruns reproduced the committed
json; Lemma 1 brute-forced for q ≤ 31; Lemma 2 checked on 746 tuples; cross-check 30 198/30 198 re-run). Findings and repairs:
* MAJOR — Type I weights counted a prime common to a and d twice, and gave the mirror tuple (b, a, e, d) the AP weight of
  (a, b, e, d). *Fixed* (`z52c_rh_types.c`: distinct-prime weights, mirror weighted by its own modulus 4bd and pair predicate);
  all windows regenerated (`scripts/z52c_rh_runtypes.sh`) and every table, regression and decomposition number in this file
  updated. Effect: ≤ 0.001 on the q ≤ 16 factors, ≤ 0.004 mod 840; conclusions unchanged.
* MAJOR — §2.3 zero law: "tests neither model sharply" below 10⁵ was wrong (4 observed vs 21.9 expected is a sharp rejection).
  *Rewritten*: M′ is a better mean model, not a validated zero model; the > 10⁵ agreement is 3 events.
* MAJOR — `z52c_rh_runU.sh` did not parse. *Fixed* (bash -n clean; creates dirs, waits on PIDs, assembles the gz);
  `z52c_rh_crosscheck.py` now asserts.
* MINOR — "χ²/class" renamed MSSD and qualified as descriptive; added the q ≤ 16-only values (0.44–0.85).
* MINOR — residual sds were taken from the prime-product variant; corrected (0.209 → 0.150 etc.); "not residue-class structure"
  softened to "not explained by the tested factors".
* MINOR — failure quantiles used the wrong 9 primes (`ff[:9]`); now by value, the 7 failures in (10³, 10⁶].
* MINOR — harmonic-sum identities lacked the −log q constants; restored (they cancel between classes).
* MINOR — summary item 2 overgeneralised Lemma 2's mod-4q statement to (★); restricted.
Reviewer verdict (paraphrased): effect well supported; the closed form is conjectural (its discrepancies from the model are
not shown to be O(L⁻²) — §1.2's "O(L⁻²)" is the derivation's claim, not verified); no progress on B3/B6; ES open.
