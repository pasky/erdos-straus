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

## 3. Plan / status (checkpoint 1)
* **(S)-gap: CLOSED** (CERTIFIED, `scripts/z67_ell0_sgap.py`, `data/z67/ell0/sgap_102_1e5.txt`): all 9566 primes
  101 < ℓ < 10⁵ pass the global certificate Σ_{k≤K}|E_k|/φ(ℓ^k) + Σ_{k>K} T_k < 1/2 (K = 1 for 9517 primes, K = 2 for
  49; worst bound 0.4932 at ℓ = 379, K = 1). The same certificate also passes for every prime 11 ≤ ℓ ≤ 101
  (`sgap_11_101_global.txt`, K ≤ 7; worst 0.4877 at ℓ = 37), re-proving UCOVER Thm S(a)'s existence part
  independently of the branch tree. With UCOVER Thm S(b) (ℓ ≥ 10⁵): **(S-all) holds for every prime ℓ ≥ 11.**
* (T-expl): explicit P_I, P_II bounds (ET §3 split + rigorous divisor-function maxima computed as finite Euler
  products) → explicit ℓ₀. In progress. First assessment (exponent LP over dyadic boxes, `/tmp` exploratory): the
  (A) count needs divisor-function maxima in some boxes (box s = O(1), d′ ≈ C ≈ a′ ≈ n^{1/3}: s = 1 alone contributes
  every factorisation of (n + 1)/4), so K2 is expected to fire and ℓ₀ to be astronomically large.
