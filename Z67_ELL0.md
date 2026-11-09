# Z67_ELL0 — making Z66_UCOVER's Theorem T explicit. Verdict: strengthened ((S) closed for every ℓ ≥ 11; explicit ℓ₀ for ET) + narrowed (ET gap ℓ < ℓ₀ not closed by the counting bounds tested); HOT LEAD: no

Lane ELL0, wave z67 (brief `z52bbriefs/z67_lanes.md` §ELL0; common rules `z58_lanes.md`, `z53_depth.md`).
**ES is OPEN. Nothing here proves or disproves ES or any case of it.** Internal, unrefereed; internal hostile review:
§8. Scripts `scripts/z67_ell0_*`, data `data/z67/ell0/`. Builds on `Z66_UCOVER.md` (cited UCOVER: Lemma 1, §2.2,
Thm T, Cor T.1, Lemmas S1, S2, S2′, Thm S) and Elsholtz–Tao (`sources/elsholtz-tao-1107.1010.pdf`, cited ET).

**Results in one paragraph.**
* **(S-all) (PROVED, computer-assisted).** For **every prime ℓ ≥ 11** the good-word caught set has Haar measure
  μ_ℓ^S < 1/2, so some non-residue g has e_{ℓ,g} ∈ U_S; for ℓ = 3, 5, 7 none does (UCOVER Thm S(c)). The gap
  101 < ℓ < 10⁵ of UCOVER Thm S is closed: all 9566 primes pass a global certificate (exact levels ≤ K, K ≤ 2, plus
  UCOVER's Lemma S2′ tail), worst bound 0.4932 (ℓ = 379). The same certificate re-proves 11 ≤ ℓ ≤ 101 (K ≤ 7). §3.
* **Lemma D (PROVED, new).** The I-1 (A) events need only k₂ = 1: every (A) cylinder with k₂ ≥ 3 sits inside one of
  level k − 1 (ET's dilation (2.10)). So the A-term of level k is a single count at n = ℓ^{2k−1}. §2.
* **Theorem T-expl (PROVED, computer-assisted: an explicit inequality enclosed in interval arithmetic).** For every
  prime ℓ ≥ e^{2950} (< 10^{1282}), μ_ℓ ≤ 0.0408: at least 91.8 % of the non-residues g (Haar) have e_{ℓ,g} ∈ U, and
  Cor T.1 holds for all but ≤ 0.0408(ℓ − 1) of the classes g₀ mod ℓ. All constants are explicit (ET §3 split with ET
  Lemma 2.8 re-derived; divisor maxima as finite Euler products). §4.
* **(T-all) for 17 ≤ ℓ < e^{2950}: not closed (narrowed).** The binding term is the I-1 family at level k ≈ 29. Its
  a′ = 1 events at level k are in bijection with the solutions counted by the campaign's (★)/(MS) number R(ℓ^{2k−1})
  (Prop R, PROVED). Upper bounds on such counts at all odd powers ℓ^{2k−1}, *together with* bounds for the a′ > 1
  analogues (or another control of the remaining A-events), would be one sufficient route to a certified tail. The counting bounds tested here do not close the gap. Divisor-free box counting, as explored, gives
  only ≈ n^{2/3} (Assessment, grid computation). Divisor maxima give ℓ₀ = e^{2950}. §5.
* **(T-all) EVIDENCE.** No prime 17 ≤ ℓ < 10⁵ has all non-residues caught at level 1 (only ℓ = 3, 5, 7, 11, 13 do);
  for every tested prime 2000 ≤ ℓ < 10⁵ at least 84 % of the non-residue mass survives level 1. All 72 primes
  17 ≤ ℓ < 400 keep survivors after level 2 (min mass 0.059, ℓ = 23), the 10 primes 59 ≤ ℓ ≤ 101 after level 3 (min
  0.154, ℓ = 59). §6.

## 0. Falsifier table (mandatory)

This lane is about coverings of unit profiles by polynomial identities; it makes no positivity claim for ES.

| screen | behaviour |
|---|---|
| **F1 odd squares** | Square profiles lie in U and in U_S (ET Prop 1.6, SDEEPF Prop 3.5). All caught residues are quadratic non-residues mod ℓ (UCOVER Lemma 1 / S1; asserted again in every script here). Every bound here is a bound on the *caught* mass inside the non-residues. |
| **F2 C-even / numerator 8** | No positivity claim, so no contradiction (only the numerator-4 ET families and SDEEPF good words). Via Prop R the campaign's C is d′. The 12 R₈-zeros remove only the even-d′, a′ = 1, level-1 subfamily of A-events at such n, not all A-events (the cross-model reviewer reports full R ≥ 12 there). |
| **F3 composites** | Not applicable: profiles are units of Ẑ, not integers. |
| **F4 known zeros** | No positivity claim. Via Prop R, the 14 R-zero primes p have no a′ = 1 A-events at n = p. The 38 𝔊*-zeros remove only that restricted representation subfamily. Neither implies that all ET events vanish, nor controls the higher odd powers p^{2k−1}. |

**Pre-registered kill tests (checkpoint 1) and outcomes.**
* **K1 ((S)-gap).** Dies at a prime 101 < ℓ < 10⁵ if (exact caught mass of the computed levels) + (Lemma S2′ tail)
  ≥ 1/2 at every feasible depth. **Did not fire:** all 9566 primes pass with K ≤ 2.
* **K2 (ET, explicit tail).** Dies if the I-1 events at level k cannot be bounded by c·ℓ^{θ(2k−1)}, θ < 1/2, without
  divisor-function maxima (then ℓ₀ is astronomically large and the gap cannot be closed by computation).
  **Fired for the methods tried** (§5). The divisor-free box bounds explored give θ ≈ 2/3 (a grid Assessment, not a
  theorem about all methods). With divisor maxima, ℓ₀ = e^{2950}.

## 1. Precise statements

Notation as UCOVER §1: e_{ℓ,g} is the profile g at ℓ, 1 elsewhere; C_ℓ = {g ∈ ℤ_ℓ^× : e_{ℓ,g} ∉ U} (open), μ_ℓ its
Haar measure normalised on ℤ_ℓ^× (the non-residues have mass 1/2); C_ℓ^S, μ_ℓ^S the same for the (S) good-word
classes (U_S, UCOVER §6). Since every caught residue is a non-residue, μ_ℓ < 1/2 implies that some non-residue g has
e_{ℓ,g} ∈ U (the complement of an open set of smaller mass in the non-residues is non-empty).
* **(T-expl)** An explicit ℓ₀ with μ_ℓ < 1/2 for every prime ℓ ≥ ℓ₀. **PROVED, ℓ₀ = e^{2950}** (§4).
* **(T-all)** μ_ℓ < 1/2, or at least C_ℓ ⊉ non-residues, for every prime ℓ ≥ 17. **OPEN** (EVIDENCE §6; what the tested
  methods miss: §5).
  (ℓ = 3, 5, 7, 11, 13: every non-residue profile is caught at level 1; CERTIFIED, §6.)
* **(S-all)** μ_ℓ^S < 1/2 for every prime ℓ ≥ 11. **PROVED, computer-assisted** (§3 + UCOVER Thm S(b)).

## 2. Lemma D (dilation; PROVED, new) — the I-1 events need only k₂ = 1

**Lemma D.** In UCOVER Lemma 1 (A), every generator cylinder with k₂ ≥ 3 lies inside a generator cylinder of level
k − 1 with (k₁, k₂) replaced by (k₁ + 1, k₂ − 2). Hence the (A)-generators can be restricted to k₂ = 1, k₁ = k − 1:
the level-k (A) events are the ℕ-points (C, w, a′, d′) of ΣII at the single value n = ℓ^{2k−1} (UCOVER §2.2, K′ = 2k − 1)
with ℓ ∤ a′d′, and R_A(k) ≤ P_II(ℓ^{2k−1}).

*Proof.* The (A) event of type (k₁, k₂, a′, d′, C) is the I-1 class (a, d, f) = (ℓ^{k₁}a′, ℓ^{k₂}d′, 4a′d′C − 1),
n ≡ −f (mod 4ad), f | 4a²d + 1 (ET Prop 1.9, first Type I family; no side conditions). If k₂ ≥ 2 then
(a, d) ↦ (ℓa, d/ℓ²) (ET's dilation (2.10) with λ = ℓ) keeps a²d, so f | 4(ℓa)²(d/ℓ²) + 1, and (ℓa, d/ℓ², f) is an
I-1 triple whose modulus 4ad/ℓ divides 4ad. So the class −f mod 4ad lies in the class −f mod 4ad/ℓ. The prime-to-ℓ part
of both moduli is 4a′d′, so the catch condition f ≡ −1 (mod 4a′d′) is the same, and the caught cylinder
−f + ℓ^kℤ_ℓ lies in −f + ℓ^{k−1}ℤ_ℓ. Since k₂ is odd (UCOVER Lemma 1 parity), iterating reaches k₂ = 1, with
K′ = 2k₁ + k₂ unchanged. ∎

*Check (CERTIFIED for the listed cases; `scripts/z67_ell0_dilation_check.py`, `data/z67/ell0/dilation_check.txt`).*
For ℓ ∈ {17, 19, 23}, k ∈ {3, 4}: every (A) event with k₂ ≥ 3 (64, 242; 104, 230; 142, 543 events) reduces
mod ℓ^{k−1} to a level-(k−1) (A) residue. (For ℓ = 17 the counts match the bijection: 64 = #level-2 (A) events,
242 = #level-3 (A) events with k₂ = 1.)

*Consequence.* UCOVER's union bound becomes
  **μ_ℓ ≤ Σ_{k odd} [P_I(ℓ^k) + 2P_II(ℓ^k)]/φ(ℓ^k) + Σ_{k≥1} P_II(ℓ^{2k−1})/φ(ℓ^k)**   (★T)
(one A-term per level instead of k). The A-term still lives at n = ℓ^{2k−1}; that cannot be reduced (§5).

## 3. (S-all): the (S)-gap 101 < ℓ < 10⁵ (PROVED, computer-assisted)

**Theorem S′.** For every prime ℓ ≥ 11, μ_ℓ^S < 1/2. Hence for every prime ℓ ≥ 11 there is a non-residue class g₀
mod ℓ containing some g with e_{ℓ,g} ∈ U_S, and for every q prime to ℓ the class {n ≡ 1 (mod q), n ≡ g₀ (mod ℓ)} is not
finitely coverable by SDEEPF good words (UCOVER §6 compactness). For ℓ = 3, 5, 7 every non-residue profile is caught at
level 1 (UCOVER Thm S(c)).

*Proof.* ℓ ≥ 10⁵: UCOVER Thm S(b) (Σ_k T_k(ℓ) ≤ 0.3655). 11 ≤ ℓ < 10⁵: by sub-additivity,
  μ_ℓ^S ≤ Σ_{k≤K} |E_k|/φ(ℓ^k) + Σ_{k>K} T_k(ℓ),  T_k = ℓ/(ℓ−1)(k + 2)(2.44 k ln ℓ + 10.15)ℓ^{−k/2},
where E_k is the exact set of good caught unit residues at level k (UCOVER Lemma S1, enumerated completely by
`scripts/z66_ucover_swords.c`, UCOVER Lemma S2) and T_k majorises the candidate count of that enumeration divided by
φ(ℓ^k) whenever ℓ^k ≥ 10⁵ (UCOVER Lemma S2′; the script also asserts candidates ≤ majorant at every computed level with
ℓ^k ≥ 10⁵). `scripts/z67_ell0_sgap.py` increases K from 1 until the right side is < 1/2.
* The first sum uses exact fractions.
* The tail is evaluated in mpmath interval arithmetic: terms to K + 80, then a geometric remainder with ratio bound
  ρ < 1 (the construction of UCOVER `z66_ucover_stree.tail_upper`).
* The interval's upper endpoint is read exactly from mpmath's raw (sign, mantissa, exponent) tuple.
  * The first version went through `mpf(tot.b)`, which re-rounds to 53 bits and can round down. The internal review
    exhibited an undershoot of 2.3·10⁻¹⁷ at ℓ = 37, K = 3.
  * Fixed, and both ranges were rerun. Every per-prime line is identical.
  * The same `mpf(…).man_exp` conversion occurs in UCOVER's `z66_ucover_stree.py`. Its margins (≥ 0.0099) dwarf the
    effect, and §3 re-proves its existence statements independently, but the script should be fixed by its owner.

Results:
* 101 < ℓ < 10⁵ (`data/z67/ell0/sgap_102_1e5.txt`): all 9566 primes CERTIFIED; K = 1 for 9517 primes, K = 2 for 49;
  worst bound 0.4932 (ℓ = 379, K = 1); e.g. ℓ = 99991: 0.0033.
* 11 ≤ ℓ ≤ 101 (`sgap_11_101_global.txt`): all 22 primes CERTIFIED with K ≤ 7 (ℓ = 11: K = 7, bound 0.390); worst
  0.4877 (ℓ = 37, K = 3). This re-proves the existence part of UCOVER Thm S(a) without the branch tree. ∎

*Independent cross-check* (`scripts/z67_ell0_scross.py`, `data/z67/ell0/scross.txt`): UCOVER's literal brute force
(`z66_ucover_sbrute.py`, Jacobi symbols on explicit representatives) with A, uv ≤ 2·10⁵ at ℓ = 103, 379, 1009, levels
≤ 2: brute = exact (13, 15, 10 residues).

## 4. Theorem T-expl: an explicit ℓ₀ (PROVED, computer-assisted: an explicit inequality enclosed in interval arithmetic)

**Theorem T-expl.** For every prime ℓ ≥ e^{2950} (in particular every ℓ ≥ 10^{1282}), μ_ℓ ≤ 0.0408 < 1/2. Hence at
least a fraction 1 − 0.0816 of the non-residues g ∈ ℤ_ℓ^× (by Haar measure) have e_{ℓ,g} ∈ U, and UCOVER Cor T.1 holds
with an explicit count: all but ≤ 0.0408(ℓ − 1) of the non-residue classes g₀ mod ℓ meet U (a class fully inside C_ℓ
has mass 1/(ℓ − 1)).

**Inputs** (all elementary; no unproved ET constant is used).
* **(I1) Union bound** (★T) of §2, with R_F(k) ≤ P_I(ℓ^k) (F events ↪ ℕ-points of ΣI_{ℓ^k}, one residue −a/c each),
  R_E(k) ≤ 2P_II(ℓ^k) (pure E/D events ↪ ΣII_{ℓ^k}; two residues per point; mixed ones are redundant, UCOVER §2.1),
  R_A(k) ≤ P_II(ℓ^{2k−1}) (Lemma D). F and E events exist only for odd k (UCOVER Lemma 1).
* **(I2) Reflection.** P_I(n) ≤ 2B_I(n), P_II(n) ≤ 2B_II(n), where B counts ℕ-points with a ≤ b. ET's reflections
  (Remark 2.4 and its ΣII analogue) send an ℕ-point with a > b to one with a < b. The new f is the quotient
  (n² + 4c²d)/f = 4bcd − n (ΣI, by (2.9)) resp. (4c²dn + 1)/f = 4bcd − 1 (ΣII, by (2.21)). Both are positive
  integers: positive quotients of positive integers, integral by the defining equations. (The first version argued via
  "4bcd − n > 4acd − n", which is false for a > b; cross-model review. Example: n = 7, sextuple (2, 1, 3, 1, 1, 17),
  reflected f = 5 < 17.)
* **(I3) Size bounds** (ET Lemma 2.8, re-derived from the equations alone, a ≤ b).
  * ΣII: from (2.15), nc < 4abcd = a + b + nc ≤ nc + 2abcd, so n/4 < abd ≤ n/2; with b < ce ≤ 2b this gives
    acde ≤ n and e²(ad)(ac)(cd) = (acde)² ≤ n².
  * ΣI: ef = 4a²d + 1 ≥ 5 (2.7), so bf = na + c ≤ na + 2b/e ≤ na + (2/5)bf (2.8), i.e. bf ≤ 5na/3 and f ≤ 5n/3;
    4acd = n + f (2.6) gives n/4 < acd ≤ 2n/3; hence e·f·(cd)²·(ac) = (acd)²(ce/b)(bf/a) ≤ (2n/3)²·2·(5n/3) ≤ (15/8)n³.
* **(I4) ET §3 case split, explicit.** With X = n^{2/5}, one of e, ad, ac, cd is ≤ X (ΣII); with
  Y = ((15/8)n³)^{1/5}, one of e, f, cd, ac is ≤ Y (ΣI). In each case the fixed quantities and one divisor determine
  the point:
  * ΣII. e ≤ X: (a, b, d) is an ordered factorisation of (n + e)/4 (2.13), c = (a + b)/e. ad ≤ X: e | n + 4a²d
    (2.19), then b (2.13), c. ac ≤ X: b | nc + a (2.20), then f, d (2.18), e. cd ≤ X: f | 4c²dn + 1 (2.21), then a
    (2.18), b (2.21).
  * ΣI. e ≤ Y: factorisation of (ne + 1)/4 (2.1). f ≤ Y: factorisation of (n + f)/4 (2.6). cd ≤ Y: f | n² + 4c²d
    (2.9), then a (2.6), b (2.8). ac ≤ Y: b | na + c (2.8), then f, d (2.6), e.
  With T(x) = max_{m≤x} τ(m), T₃(x) = max_{m≤x} τ₃(m), D(X) = X(1 + ln X) ≥ #{(u, v) ∈ ℕ² : uv ≤ X}, and
  a²d ≤ (ad)², c²d ≤ (cd)² (the simplification n² + 4Y² ≤ 2n² needs n ≥ 8; here n ≥ ℓ is huge):
  * B_II(n) ≤ X·T₃(n/2) + D(X)[T(5n) + T(2n^{7/5}) + T(5n^{9/5})];
  * B_I(n) ≤ Y[T₃(nY) + T₃(n)] + D(Y)[T(2n²) + T(2nY)].
* **(I5) Divisor maxima.** τ(m) ≤ C(ε)m^ε and τ₃(m) ≤ C₃(ε)m^ε for all m ≥ 1, where
  ln C(ε) = Σ_{p < 2^{1/ε}} max_{a≥0}[ln(a + 1) − aε ln p] and
  ln C₃(ε) = Σ_{p < 3^{1/ε}} max_{a≥0}[ln binom(a+2, 2) − aε ln p]
  (multiplicativity; for larger p the maximum is at a = 0, since a + 1 ≤ 2^a and binom(a+2, 2) ≤ 3^a).
  * For fixed p, f(a) = ln binom(a+r−1, r−1) − aε ln p is concave: f(a) − f(a−1) = ln((a+r−1)/a) − ε ln p decreases.
    Its maximum sits at the last a with a non-negative difference. That a is < 29 (τ, ε ≥ 0.05) resp. < 36 (τ₃,
    ε ≥ 0.08).
  * With ε = num/den as an exact rational, the script decides everything in exact integers:
    * the cutoff: p contributes iff r^den > p^num, and the first excluded prime is asserted to satisfy p^num ≥ r^den;
    * the maximiser: the largest a with (a+r−1)^den ≥ a^den·p^num.
    Then f(a*) is enclosed in outward interval arithmetic and the upper endpoints are summed.
  * This fixes a cross-model review finding: the previous version located a* in floating point within a ±2 window,
    which concavity alone does not justify. The constants and the final bound are unchanged.
  * Results: ln C(0.05) ≤ 4526.2143, ln C(0.06) ≤ 683.54, ln C(0.1) ≤ 24.455, ln C₃(0.08) ≤ 6471.13,
    ln C₃(0.09) ≤ 1850.52.

**Proof.** `scripts/z67_ell0_tbound.py 2950 300` encloses (I1)–(I5) at L = ln ℓ = 2950. It works in the log domain
with outward-rounded interval arithmetic (mpmath.iv, 50 digits), and every reported bound is an upper endpoint.
* For each level k ≤ 300 and each of the 12 case terms it takes the best ε from a grid: τ from 0.05 to 0.10 in steps
  of 0.002, then 0.11 to 0.50; τ₃ from 0.08 to 0.10 in steps of 0.002, then 0.11 to 0.50.
* Levels k > 300 are bounded with fixed ε = 0.05 (τ) and 0.09 (τ₃). Each ln-term is then const − β(k)L, plus
  ln(1 + ln X) in the pair cases, with β linear in k.
  * Grouping levels in pairs, term(k+2)/term(k) ≤ e^{−(β(k+2)−β(k))L}·(1 + 4/(2·300 + 1)). The last factor bounds the
    growth of 1 + ln X.
  * The exponential part gains at least 0.02L per level, so the pair ratio is ≤ 5.8·10⁻⁵².
  * A geometric series then bounds the whole tail by 3.1·10^{−6369}.
* Total: Σ_{k≤300} ≤ 0.040798, and the tail is negligible. So **μ_ℓ ≤ 0.0408** (`data/z67/ell0/tbound_L2950.txt`).
  The largest single term is the A family, case cd, at level 29: < 0.03803.
* An earlier double-precision version gave 0.0421 using looser margins; the internal review asked for the interval
  version.

*All ℓ ≥ e^{2950}.* Fix the ε's at their L = 2950 choices. Each term is then
exp(const − βL + ln(1 + c·L))/(1 − e^{−L}) with β ≥ 0.192 > 2/2950 (checked by the script). Since
d/dL ln(1 + cL) ≤ 1/L, every term decreases in L for L ≥ 2950. The ε-minimised bound at larger L is no larger. ∎

*Where the size comes from.*
* The binding term is the I-1 (A) family at level k ≈ 29 (n = ℓ^{57}), case cd ≤ X. Its divisor argument is ≈ n^{9/5}.
* Its exponent (2k−1)(2/5 + (9/5)ε) − k is negative only for ε < (k/(2k−1) − 2/5)·(5/9). This tends to 1/18 as
  k → ∞, and C(ε) ≥ e^{4500} at ε = 0.05.
* The F and E families are harmless: their exponents are ≈ −2k/5 and −3k/5.
* Optimising the case thresholds, or using Lenstra's bound in the "ad" case, moves the constant but not the nature:
  ℓ₀ stays astronomical (Assessment; §5).

## 5. Why (T-all) is not closed for 17 ≤ ℓ < e^{2950} (narrowed)

**Prop R (PROVED).** For n = ℓ^{2k−1} the level-k (A) events with a′ = 1 are in bijection with *all* solutions of
  4·d′·C·w − C − w = n  (C, w, d′ ≥ 1),
i.e. with the campaign's (★)/(MS) representations n = 4uBC − u − B (`Z57_SYNTH.md` §1; R(n) := #{(u, B, C) ∈ ℕ³ : …}),
via (u, B, C) = (C, w, d′). So their number is exactly R(ℓ^{2k−1}). The caught residue is −f = 1 − 4d′C (mod ℓ^k),
f := 4d′C − 1. In general the level-k (A) events are the solutions of a′ℓ^{2k−1} = 4a′d′Cw − C − w with ℓ ∤ a′d′.
*Proof.* UCOVER §2.2 (A) with K′ = 2k − 1 (Lemma D) and a′ = 1 reads a′(4d′Cw − ℓ^{K′}) = C + w. It remains to see that
the side condition ℓ ∤ d′ is automatic.
* For any solution, f·w = n + C, gcd(C, f) = 1 and f ≡ −1 (mod 4C).
* UCOVER's Jacobi fact (J) gives (−C/f) = −1, hence (n/f) = (−C/f) = −1. As n is an odd power of ℓ, (ℓ/f) = −1.
* By reciprocity (f ≡ 3 mod 4) this is (−f/ℓ) = −1.
* If ℓ | d′C we would have −f ≡ 1 (mod ℓ), a square. Hence ℓ ∤ d′C, and every solution is an event whose residue is
  a non-residue. ∎

(Prop R counts *events*, not distinct residues: different solutions can give the same residue mod ℓ^k, and cylinders
of different levels overlap. Upper bounds on R are therefore *sufficient* for bounding the A-mass, not necessary.)

**What the tested certificate methods would need (Assessment, with a computation).**
* A certificate in the style of §3 must bound the event mass (or the union mass) of all levels k > K for the K one can
  compute. For ℓ = 17, UCOVER's code reaches K = 4 (n = 17⁷).
* One sufficient route is an upper bound for R(ℓ^{2k−1}) and its a′ > 1 analogues that is summable against ℓ^{−k}
  uniformly enough in k. Examples: c·n^{1/2−δ}, or c·n^{1/2}/(log n)^{1+η}, with usable constants. A bound c·n^{1/2}
  alone gives a constant per level and does not suffice.
* Counting by dyadic boxes in (d′, C, a′, s) (s = 4d′Cw − n) without divisor-function input (`scripts/z67_ell0_boxlp.py`,
  `data/z67/ell0/boxlp.txt`; a 1/60-mesh grid search, not a certified optimisation) uses three tools: the trivial
  residue count (ρ = 1 − 4m, m = a′d′C ≤ n/s), fixing three coordinates, and Lenstra's "≤ 11 divisors in a residue
  class mod q > X^{1/3}" for the five pair fibrations where it applies. The worst sampled box then costs n^{2/3}.
  * That box is s = O(1), d′ ≈ C ≈ a′ ≈ n^{1/3}. Here s = 1 alone contributes every factorisation
    (n + 1)/4 = d′Cw with ℓ ∤ C + w.
  * Restricted to s ≥ n^{0.2}, the mesh still finds n^{0.65}, near the box a′ = O(1), d′ ≈ C ≈ s ≈ n^{1/3}: the
    a′ = 1, i.e. (★), sub-family. The reviewer found a feasible off-mesh box costing n^{0.66}, and nearby boxes
    approach n^{2/3}.
* With divisor maxima τ ≤ C(ε)m^ε the exponent is 2/5 + O(ε) (ET). But C(ε) is astronomically large for the ε
  required, which is what §4 pays.
* So the counting bounds tested here do not close the gap 17 ≤ ℓ < e^{2950}. This is not a theorem that no
  measure-counting certificate can. Escape hatches the tested methods leave open:
  * better deduplication: counting distinct residues or cylinder unions, not events;
  * further arithmetic constraints on the events;
  * explicit Shiu-type bounds for Σ τ over progressions whose modulus is large compared with their length. These are
    needed in the a′ = O(1) box, where the sum is Σ_{d′} τ(4d′n + 1) over d′ ≈ n^{1/3}.
  * a structured choice of g. Rational g are dangerous: e.g. for ℓ ≡ 3 (mod 4), g = −1 is caught at level 1 (F:
    a = c = 1, d = (ℓ + 1)/4; also A: C = w = 1, a′ = 2, d′ = (ℓ + 1)/4).
  * a König-tree argument: survivors at every finite level would suffice, by compactness.

## 6. (T-all): EVIDENCE and the CERTIFIED small-ℓ facts

`scripts/z67_ell0_etlow.py LO HI K` runs UCOVER's exact generator enumeration (`z66_ucover_levels.c`) for levels ≤ K
and the ℓ-adic survivor tree (UCOVER §3).
* **Level 1, 3 ≤ ℓ < 10⁵** (`etlow_L1_3_2000.txt`, `etlow_L1_2000_1e5.txt`; CERTIFIED as stated). All non-residues
  are caught at level 1 exactly for ℓ ∈ {3, 5, 7, 11, 13}. For every other prime ℓ < 10⁵ some non-residue class
  g₀ mod ℓ survives level 1. The smallest surviving masses are 0.091 (ℓ = 23) and 0.125 (ℓ = 17). For the tested
  primes 2000 ≤ ℓ < 10⁵ the surviving mass is ≥ 0.421 (min at ℓ = 2237, 176 caught non-residues out of 1118).
* **Level 2, 17 ≤ ℓ < 400** (`etlow_L2_17_400.txt`): all 72 primes keep survivors; min surviving mass 0.0593 (ℓ = 23).
* **Level 3, 59 ≤ ℓ ≤ 101** (`etlow_L3_59_101.txt`; 17–53 are in UCOVER §3): all keep survivors; the loss from level 2
  to 3 is about 0.001 (0.00045–0.00124); min mass 0.154 (ℓ = 59).
* *Reading (EVIDENCE, not proof).* The new loss per level falls by roughly a factor ℓ^{1/2} or more per level (UCOVER
  §3; e.g. ℓ = 59: 0.0169, 0.00098). A Prop-R-type tail that behaves like its average would leave every ℓ ≥ 17 with
  survivors.
* But survival at the finitely many levels computed here does not prove survival at all levels. If survival at every
  finite level could be proved, compactness (König's lemma) would give an uncovered profile.
* The plain event-mass sum Σ_k|E_k|/φ(ℓ^k) (no tree) already exceeds 1/2 for ℓ = 17, 23, 31 at level 2
  (0.544, 0.589, 0.501). So a certificate that *adds* event masses, as in §3, is impossible for these ℓ even with a
  perfect tail. Any proof there has to use the union of cylinders or the survivor tree, branch by branch.

## 7. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: strengthened + narrowed.**
* Strengthened:
  * (S-all) is proved for every prime ℓ ≥ 11, closing the brief's (S) gap.
  * Theorem T now has an explicit threshold: ℓ₀ = e^{2950}. "Mordell–Schinzel beyond squares" holds with an explicit
    count for every prime above 10^{1282}.
  * Lemma D shrinks the A-term to one ΣII count per level.
* Narrowed:
  * The gap 17 ≤ ℓ < ℓ₀ for ET is not closed by the counting bounds tested here (§5).
  * The binding family is identified: the level-k I-1 events with a′ = 1 are exactly the (★)/(MS) representations
    of ℓ^{2k−1} (Prop R). Good upper bounds for such counts, together with bounds for the a′ > 1 analogues, would be
    one sufficient route.
* No bearing on ES itself; no HOT LEAD.

**Hard screens (FRONTIER §4).**
* *T1 squares.* Built in: square profiles are uncovered, every caught residue is a non-residue.
* *8/131.* Not applicable (numerator 4 only).
* *Tied modulus (B2).* Not moved. Prop R points to *upper* bounds on (★)-counts at prime powers as one route to an
  explicit Theorem T at small ℓ. B2 needs *lower* bounds at primes, the opposite direction.
* *Fixed p.* Not applicable.

**Proposed FRONTIER text** (do not edit FRONTIER here).
> *(z67 ELL0.)* UCOVER's Theorem T made explicit: for every prime ℓ ≥ e^{2950} (< 10^{1282}) the ET-caught non-square
> ℓ-profiles have Haar mass ≤ 0.0408 (`Z67_ELL0.md` Thm T-expl; explicit ET §3 split + Euler-product divisor maxima,
> interval arithmetic; new Lemma D: the I-1 events of level k live only on ΣII_{ℓ^{2k−1}}). The (S)-analogue is now
> PROVED for every prime ℓ ≥ 11 (gap 101 < ℓ < 10⁵ closed by a global certificate, computer-assisted). For ET at
> 17 ≤ ℓ < e^{2950} the question stays open (EVIDENCE: every prime 17 ≤ ℓ < 10⁵ has level-1 survivors; 17 ≤ ℓ < 400
> have level-2 survivors). The binding family: the level-k I-1 events with a′ = 1 are exactly the (★)
> representations of ℓ^{2k−1} (Prop R). Summable upper bounds for these counts *and* for their a′ > 1 analogues, with
> usable constants, are one sufficient route to a certified tail; the counting methods tested do not supply them.

**Bottom line.**
* Two of the brief's three asks are done. The (S)-families now provably escape finite good-word coverings beyond the
  squares at every prime ℓ ≥ 11. Theorem T has an explicit ℓ₀ — but it is e^{2950}.
* The third ask, every ℓ ≥ 17 for the ET families, is not reached. The binding I-1 events at level k include the
  (★)-type equation at n = ℓ^{2k−1}. The tested ways of counting them below √n use divisor maxima, and their
  constants explode. Below ℓ₀ only EVIDENCE remains, and it is uniformly positive at the computed levels.
* Nothing here touches ES; B2 is unchanged.

## 8. Review log and replay

**Internal hostile review** (deep-mode subagent; `data/z67/ell0/internal_review.md`). Verdict on the first version:
REJECT as written, repairable. It confirmed Lemma D, the ET embeddings and multipliers, the reflections, the size
bounds, all eight case reconstructions, Prop R's equation, the g = −1 example, all certificate counts and the evidence
numbers. It reran the (S) certificates in full and the T-expl evaluation, and found no provider error. Findings and
fixes:
* **(1) MAJOR.** The (S) tail's upper endpoint went through a 53-bit `mpf`, which can round down (undershoot
  2.3·10⁻¹⁷ at ℓ = 37). Fixed by reading the raw interval endpoint. All certificates were rerun and are unchanged
  (§3). The same pattern in UCOVER's `z66_ucover_stree.py` is flagged there.
* **(2) MAJOR.** T-expl's numerics (double-precision divisor constants with an ad-hoc margin; 60-digit non-interval
  sums) were not a rigorous enclosure. The script was rewritten in outward interval arithmetic, with a proved window
  for the maximising exponent; the bound is now ≤ 0.0408 (§4). During the rewrite an intermediate version truncated
  the prime list for ε = 0.05 (ln C 4496.7 instead of 4526.2); this was caught by comparison with the float value, and
  the script now asserts that the list reaches the cutoff.
* **(3) MAJOR.** §5's "cannot be closed" / "needs n^{1/2−δ}" language overclaimed. Prop R counts events, not distinct
  residues. A power saving is sufficient, not necessary. The box search covers only the tested methods. All of this was
  rephrased as "not closed by the counting bounds tested", including the title, the summary, K2, the FRONTIER text
  and the bottom line.
* **(4) MAJOR.** The compactness sentence in §6 was false: survivors at every finite level do imply an uncovered
  profile. Corrected.
* **(5) MINOR.** The 0.65 restricted-box exponent is a grid value; it is now labelled as such, with the reviewer's
  off-mesh 0.66.
* **(6) MINOR.** The tail ratio in §4 now quotes the pairwise ratio including the affine factor.
* **(7) MINOR.** Prop R's parity aside: the coprimality ℓ ∤ d′C is automatic for every (★) solution at an odd power
  of ℓ (reviewer's argument, now in the proof). Hence the bijection with *all* R(ℓ^{2k−1}) solutions.
* **(8) MINOR.** Domain n ≥ 8 for the ΣI simplification; loss range 0.00045–0.00124; "for the tested primes" in the
  evidence statements.

**Cross-model review** (`data/z67/xreview/REVIEW_ELL0.md`): ACCEPT-WITH-FIXES. The reviewer independently reran the
full (S) certificate and the T-expl evaluation with independently rebuilt constants (total < 0.040797735431250). It
also confirmed Lemma D, Prop R (R(17³) = 24, R(19³) = 16, R(23³) = 10) and the §6 minima. Fixes applied:
* (1) Euler-product constants are now decided in exact integers: exact rational ε, exact cutoff r^den > p^num and an
  exact maximiser, followed by an interval enclosure. The script was rerun; output unchanged.
* (2) §4(I2): the reversed reflection inequality was replaced by the positive-quotient argument. "≤ 0.0380" is now
  "< 0.03803".
* (3) The summary, §7 and the FRONTIER text now say that R-bounds must be combined with bounds for the a′ > 1 analogues.
* (4) The F2/F4 rows now state their Prop R subfamily interpretation.

**Replay** (each under `ulimit -v 4000000`, `timeout 1800`; all runs take seconds to two minutes, except the level-3
run, about ten minutes):
```
gcc -O2 -o /tmp/zlev scripts/z66_ucover_levels.c
gcc -O2 -o /tmp/zsw  scripts/z66_ucover_swords.c -lm
uv run python scripts/z67_ell0_dilation_check.py 17 4                                   # dilation_check.txt
uv run --with mpmath --with sympy python scripts/z67_ell0_sgap.py 102 100000 4 /tmp/zsw 5  # sgap_102_1e5.txt
uv run --with mpmath --with sympy python scripts/z67_ell0_sgap.py 11 102 7 /tmp/zsw 5      # sgap_11_101_global.txt
uv run python scripts/z67_ell0_scross.py 379 200000 200000 2                             # scross.txt
uv run --with mpmath --with numpy python scripts/z67_ell0_tbound.py 2950 300             # tbound_L2950.txt
python3 scripts/z67_ell0_boxlp.py                                                        # boxlp.txt
uv run --with sympy python scripts/z67_ell0_etlow.py 3 2000 1 /tmp/zlev 5                 # etlow_L1_3_2000.txt
uv run --with sympy python scripts/z67_ell0_etlow.py 2000 100000 1 /tmp/zlev 5            # etlow_L1_2000_1e5.txt
uv run --with sympy python scripts/z67_ell0_etlow.py 17 400 2 /tmp/zlev 5                 # etlow_L2_17_400.txt
uv run --with sympy python scripts/z67_ell0_etlow.py 59 102 3 /tmp/zlev 5                 # etlow_L3_59_101.txt
```
