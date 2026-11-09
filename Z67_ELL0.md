# Z67_ELL0 — making Z66_UCOVER's Theorem T explicit (checkpoint 1; work in progress)

Lane ELL0, wave z67 (brief `z52bbriefs/z67_lanes.md` §ELL0; common rules `z58_lanes.md`, `z53_depth.md`).
**ES is OPEN. Nothing here proves or disproves ES or any case of it.** Internal, unrefereed. Scripts
`scripts/z67_ell0_*`, data `data/z67/ell0/`. Builds on `Z66_UCOVER.md` (cited UCOVER: Lemma 1, §2.2, Thm T, Lemmas
S1, S2, S2′, Thm S) and Elsholtz–Tao (`sources/elsholtz-tao-1107.1010.pdf`, cited ET).

## 0. Falsifier table (mandatory)

This lane is about coverings of unit profiles by polynomial identities; it makes no positivity claim for ES.

| screen | behaviour |
|---|---|
| **F1 odd squares** | Square profiles lie in U and in U_S (ET Prop 1.6, SDEEPF Prop 3.5). All caught residues are quadratic non-residues mod ℓ (UCOVER Lemma 1 / S1). Every bound here is a bound on the *caught* mass inside the non-residues. |
| **F2 C-even / numerator 8** | Not applicable (no positivity claim; only the numerator-4 ET families and SDEEPF good words). |
| **F3 composites** | Not applicable: profiles are units of Ẑ, not integers. |
| **F4 known zeros** | Not applicable (no positivity claim). |

**Pre-registered kill tests.**
* **K1 ((S)-gap).** The clean statement "for every prime ℓ ≥ 11 some non-residue ℓ-profile is in U_S" dies (as a
  global-mass certificate) at a prime 101 < ℓ < 10⁵ if (exact caught mass of the computed levels) + (the rigorous
  UCOVER Lemma S2′ tail) ≥ 1/2 at every feasible depth; such ℓ would then need a branch-by-branch certificate.
* **K2 (ET, explicit tail).** Making Thm T explicit with usable constants dies if the I-1 (A) events at level k cannot
  be bounded by c·ℓ^{θ(2k−1)} with θ < 1/2 *without* divisor-function maxima (then ℓ₀ is astronomically large and the
  gap ℓ < ℓ₀ cannot be closed by computation).

## 1. Precise statements attacked

Notation as UCOVER §1: e_{ℓ,g} is the profile g at ℓ, 1 elsewhere; C_ℓ = {g ∈ ℤ_ℓ^× : e_{ℓ,g} ∉ U}, μ_ℓ its Haar
measure (normalised on ℤ_ℓ^×); C_ℓ^S, μ_ℓ^S the same for the (S) good-word classes (U_S).
* **(T-expl)** Find an explicit ℓ₀ with μ_ℓ < 1/2 for every prime ℓ ≥ ℓ₀ (then some non-residue g has e_{ℓ,g} ∈ U).
* **(T-all)** The same for every prime ℓ ≥ 17 (ℓ = 3, 5, 7, 11, 13: every non-residue profile is caught at level 1).
* **(S-all)** For every prime ℓ ≥ 11 some non-residue g has e_{ℓ,g} ∈ U_S. Known: ℓ ∈ {11, 13}, 17 ≤ ℓ ≤ 101,
  ℓ ≥ 10⁵ (UCOVER Thm S). Gap: 101 < ℓ < 10⁵.

## 2. Lemma D (dilation; PROVED, new) — the I-1 events need only k₂ = 1

**Lemma D.** In UCOVER Lemma 1 (A), every generator cylinder with k₂ ≥ 3 lies inside a generator cylinder of level
k − 1 with (k₁, k₂) replaced by (k₁ + 1, k₂ − 2). Hence the (A)-generators can be restricted to k₂ = 1, k₁ = k − 1,
i.e. to the ℕ-points of ΣII at the single value n = ℓ^{2k−1} (K′ = 2k − 1).

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

*Consequence.* UCOVER's bound becomes μ_ℓ ≤ Σ_{k odd} [P_I(ℓ^k) + 2P_II(ℓ^k)]/φ(ℓ^k) + Σ_{k ≥ 1} P_II(ℓ^{2k−1})/φ(ℓ^k):
one A-term per level instead of k. The A-term still lives at n = ℓ^{2k−1} (that cannot be reduced).

## 4. Theorem T-expl: an explicit ℓ₀ (PROVED, with a computer-evaluated explicit inequality)

**Theorem T-expl.** For every prime ℓ ≥ e^{2950} (in particular every ℓ ≥ 10^{1282}), μ_ℓ ≤ 0.0422 < 1/2. Hence at
least a fraction 1 − 0.0844 of the non-residues g ∈ ℤ_ℓ^× (by Haar measure) have e_{ℓ,g} ∈ U, and UCOVER Cor T.1 holds
for these ℓ: all but ≤ 0.0422·(ℓ − 1) of the non-residue classes g₀ mod ℓ meet U.

**Inputs** (all elementary; no ET constant is used unproved).
* **(I1) Union bound** (UCOVER Lemma 1 + Lemma D). C_ℓ is the union of the generator cylinders, so
  μ_ℓ ≤ Σ_{k odd} [R_F(k) + R_E(k)]/φ(ℓ^k) + Σ_{k≥1} R_A(k)/φ(ℓ^k) with R_F(k) ≤ P_I(ℓ^k), R_E(k) ≤ 2P_II(ℓ^k)
  (pure E/D events; two residues per point) and R_A(k) ≤ P_II(ℓ^{2k−1}) (Lemma D; injective embeddings of UCOVER §2.2).
  F and E events exist only for odd k (UCOVER Lemma 1).
* **(I2) Reflection.** P_I(n) ≤ 2B_I(n), P_II(n) ≤ 2B_II(n), where B counts ℕ-points with a ≤ b. ET's reflections
  (Remark 2.4 and its ΣII analogue) send an ℕ-point with a > b to one with a < b: the new f is 4bcd − n > 4acd − n > 0
  (ΣI, by (2.9), (2.6)) resp. 4bcd − 1 > 0 (ΣII, by (2.21)).
* **(I3) Size bounds** (ET Lemma 2.8, re-derived from the equations only, a ≤ b).
  ΣII: n/4 < abd ≤ n/2 (from (2.15): nc < 4abcd = a + b + nc ≤ nc + 2abcd) and b < ce ≤ 2b, so acde ≤ n and
  e²(ad)(ac)(cd) = (acde)² ≤ n².
  ΣI: ef = 4a²d + 1 ≥ 5 (2.7), so bf = na + c ≤ na + 2b/e ≤ na + (2/5)bf, bf ≤ 5na/3; f ≤ 5n/3; 4acd = n + f gives
  n/4 < acd ≤ 2n/3; hence e·f·(cd)²·(ac) = (acd)²(ce/b)(bf/a) ≤ (2n/3)²·2·(5n/3) ≤ (15/8)n³.
* **(I4) ET §3 case split, explicit.** With X = n^{2/5} one of e, ad, ac, cd is ≤ X; with Y = ((15/8)n³)^{1/5} one of
  e, f, cd, ac is ≤ Y. In each case the fixed quantities and a divisor determine the point:
  * ΣII, e ≤ X: (a, b, d) is an ordered factorisation of (n + e)/4 (2.13), c = (a + b)/e. ad ≤ X: e | n + 4a²d (2.19),
    then b, c. ac ≤ X: b | nc + a (2.20), then f, d, e. cd ≤ X: f | 4c²dn + 1 (2.21), then a (2.18), b.
  * ΣI, e ≤ Y: factorisation of (ne + 1)/4 (2.1). f ≤ Y: factorisation of (n + f)/4 (2.6). cd ≤ Y: f | n² + 4c²d
    (2.9), then a (2.6), b (2.8). ac ≤ Y: b | na + c (2.8), then f, d (2.6), e.
  Hence, with T(x) = max_{m≤x} τ(m), T₃(x) = max_{m≤x} τ₃(m), D(X) = X(1 + ln X) ≥ #{(u, v) : uv ≤ X}:
  B_II(n) ≤ X·T₃(n/2) + D(X)[T(5n) + T(2n^{7/5}) + T(5n^{9/5})],
  B_I(n) ≤ Y[T₃(nY) + T₃(n)] + D(Y)[T(2n²) + T(2nY)].
* **(I5) Divisor maxima.** τ(m) ≤ C(ε)m^ε and τ₃(m) ≤ C₃(ε)m^ε for all m ≥ 1, with
  ln C(ε) = Σ_{p < 2^{1/ε}} max_{a≥0}[ln(a + 1) − aε ln p], ln C₃(ε) = Σ_{p < 3^{1/ε}} max_{a≥0}[ln binom(a+2, 2) − aε ln p]
  (multiplicativity; for larger p the maximum is at a = 0 since a + 1 ≤ 2^a, binom(a+2, 2) ≤ 3^a). Computed in double
  precision with an added margin 10⁻⁶·#primes + 10⁻³. E.g. ln C(0.05) ≤ 4526.3, ln C(0.1) ≤ 24.5, ln C₃(0.09) ≤ 1850.6.

**Proof.** `scripts/z67_ell0_tbound.py 2950 300` (mpmath, 60 digits, log domain) evaluates the bound of (I1)–(I5) at
L = ln ℓ = 2950, choosing for each level k ≤ 300 and each of the 12 case terms the best ε from a grid
(τ: 0.05–0.10 step 0.002, then 0.11–0.50; τ₃: 0.08–0.10 step 0.002, then 0.11–0.50). Levels k > 300 are bounded with
fixed ε = 0.05 (τ), 0.09 (τ₃): each term is then exp(α + βk)(1 + γk)-shaped with β < 0, the per-level decay is ≥ e^{−0.02L},
and a geometric series gives ≤ 3.4·10^{−6369}. Total: Σ_{k≤300} = 0.04213…, tail negligible: **μ_ℓ ≤ 0.0422**
(`data/z67/ell0/tbound_L2950.txt`). *All ℓ ≥ e^{2950}:* with the ε's fixed at their L = 2950 choices, each term is
exp(const − βL + ln(1 + c·L))/(1 − e^{−L}) with β ≥ 0.192 > 2/2950 (checked by the script), hence decreasing in L for
L ≥ 2950; the ε-minimised bound at larger L is no larger. ∎

*Where the size comes from.* The binding term is the I-1 (A) family at level k ≈ 28 (n = ℓ^{55}), case cd ≤ X, whose
divisor argument is ≈ n^{9/5}: its exponent (2k−1)(2/5 + (9/5)ε) − k is negative only for ε < (k/(2k−1) − 2/5)·(5/9),
→ 1/18 as k → ∞, and C(ε) ≥ e^{4500} at ε = 0.05. The F and E families are harmless (exponents −2k/5, −3k/5).
Optimising the case thresholds or using Lenstra's divisors-in-residue-classes bound in the "ad" case moves the
constant, not the nature: ℓ₀ stays astronomical (Assessment; §5).

## 3. Plan / status (checkpoint 1)
* **(S)-gap: CLOSED** (CERTIFIED, `scripts/z67_ell0_sgap.py`, `data/z67/ell0/sgap_102_1e5.txt`): all 9566 primes
  101 < ℓ < 10⁵ pass the global certificate Σ_{k≤K}|E_k|/φ(ℓ^k) + Σ_{k>K} T_k < 1/2 (K = 1 for 9517 primes, K = 2 for
  49; worst bound 0.4932 at ℓ = 379, K = 1). The same certificate also passes for every prime 11 ≤ ℓ ≤ 101
  (`sgap_11_101_global.txt`, K ≤ 7; worst 0.4877 at ℓ = 37), re-proving UCOVER Thm S(a)'s existence part
  independently of the branch tree. With UCOVER Thm S(b) (ℓ ≥ 10⁵): **(S-all) holds for every prime ℓ ≥ 11.**
* **(T-expl): DONE**, ℓ₀ = e^{2950} < 10^{1282} (§4). First assessment (exponent LP over dyadic boxes, `/tmp` exploratory): the
  (A) count needs divisor-function maxima in some boxes (box s = O(1), d′ ≈ C ≈ a′ ≈ n^{1/3}: s = 1 alone contributes
  every factorisation of (n + 1)/4), so K2 is expected to fire and ℓ₀ to be astronomically large.
