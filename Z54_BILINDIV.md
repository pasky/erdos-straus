# Z54_BILINDIV — depth lane BILINDIV (FRONTIER §7.1, gap 1, divisor/geometry angle): the balanced block by divisor sums and strip geometry

ES is OPEN. Nothing here proves or disproves it, and nothing here is progress on the *existence* of a solution of 4/p.
Everything here is an **upper-bound** question (a power saving for one block); it cannot give positivity, and its value
is the §7.1 benchmark and method. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Internal results, internally reviewed only.

Brief: `z52bbriefs/z53_depth.md` (wave z54), kickoff `z52bbriefs/z54_lanes.md` §BILINDIV (target as §BILINJAC).
Scripts `scripts/z54_bilindiv_*`, data `data/z54/bilindiv/`.

*Status: CHECKPOINT 1 (skeleton; statements, why open, first lemma + first falsifier).*

## 0. Notation

p an odd prime (most statements hold for odd n ≥ 5), U ≥ 2 an integer, 16U³ ≤ p. 𝔅 = (U, 2U]².
* N₂(p, U) := #{{u, B} ⊂ (U, 2U], u ≠ B : uB | p + u + B} (2-cycles of the remainder map; Z53_HYP2CYCLE);
  N₄ ⊆ N₂ the sub-count with 4 | k, k := (p+u+B)/(uB); the balanced (★) block is N(U, U) = 2N₄ (Z52D Prop 2).
* Trivial bound N₄ ≤ N₂ ≤ U/2 (each u has at most one partner). Expected size O(1) (E N₂ ≈ 0.36).
* **Target (FRONTIER §7.1, R2).** ∃ η > 0: N₂(p, U) ≪ U^{1−η} for all primes p and U ≍ p^{1/4}.
* Strip variables (Z53_HYP2CYCLE Lemma A): for a level k put s_k := (−p mod k), m_k := (p + s_k)/k,
  D_k := s_k² − 4m_k. **E1** := {k : s_k ∈ (2U, 4U], m_k ∈ (U², 4U²]} — the lattice points (k, m) of the thin hyperbolic
  strip p + 2U < km ≤ p + 4U with m ∈ (U², 4U²]; E1⁺ := {k ∈ E1 : D_k ≥ 1}; w_k := √D_k.
  Lemma A: N₂ = #{k ∈ E1⁺ : D_k = w² (w ∈ ℕ), (s_k ± w)/2 ∈ (U, 2U]}.

## 1. Statements attacked (precise)

(A) **Target R2** above (OPEN). The divisor/geometry tool classes of the kickoff, each to be either turned into a power
saving or closed by a scoped no-go with the exact exponent deficit:
1. divisor function in APs (Selberg–Hooley, Friedlander–Iwaniec beyond √);
2. divisors in short intervals (Heath-Brown, Fouvry–Iwaniec; Dirichlet-divisor exponent θ_D);
3. Tenenbaum H(x, y, z) / Ford anatomy (has a divisor in a range);
4. determinant method (Bombieri–Pila, Heath-Brown) with occupancy pruning / specific curves;
5. lattice points near curves in the thin strip (Huxley, Huxley–Sargos, Branton–Sargos), exponent pairs / Bombieri–Iwaniec.

(B) **Theorem T (new sufficient condition; PROVED reduction).** N₂ is bounded by the δ-neighbourhood count of the
fractional parts {w_k}, k ∈ E1⁺, so a *power saving* (not beyond-square-root) in the strip sums
  T(h) := Σ_{k ∈ E1⁺} e(h·w_k) = Σ_{(k,m) ∈ ℤ²: p+2U < km ≤ p+4U, U² < m ≤ 4U², D ≥ 1} e(h√((km − p)² − 4m))
for 1 ≤ h ≤ U^η suffices (hypothesis **TD(η)**). This is a *first-order* statement — a smooth phase summed over the
≍ U lattice points of the thin strip (equivalently over the divisors near √n of the integers n of an interval of length
n^{1/4}) — in contrast with Z53_HYP2CYCLE's MIX, which is second order in the remainder map.

(C) **Quadratic-order reading (PROVED, elementary).** k ∈ E1 ⟺ the quadratic integer α = (s_k + √D_k)/2 (norm m_k,
trace s_k) satisfies α | p + ᾱ in ℤ[α]: E1 is the set of "2-cycles over quadratic orders", and N₂ counts the split ones
(D a nonzero square). The first filter E1 has ≍ U elements; the split condition has probability ≍ 1/U.

## 2. Why this is not already closed

* Z52D closed one-step dualization at fixed conductor, ET/Fejér with max|S_h| and square-root input, and Cauchy–Schwarz
  in the function variable; R1 (beyond-square-root 2D sums) is numerically false at 10¹². None of these is a strip or
  divisor-sum argument.
* Z53_HYP2CYCLE closed the *black-box* determinant method (HB14/HB15 bound × uniform per-curve bound, full box or full
  grid) and reduced R2 to MIX (second order). Occupancy pruning, specific curves, and every first-order strip formulation
  were left open (Prop D scope).
* Z53_SQSIEVE Prop B2 closed the k-Poisson square sieve with triangle inequality over frequencies; it points at
  "χ_Q-twisted divisor sums near √m of integers in an interval of length m^{1/4}" — the *same* strip as here, but with
  multiplicative twists; this lane uses additive twists e(h·w) and pure counting tools.
* Divisor-in-AP, short-interval divisor, H(x,y,z) and lattice-points-near-curves tools have not been evaluated on this
  block in the repo (`git grep` for Huxley–Sargos, Shiu, Tenenbaum, Selberg–Hooley in z52d/z53 memos: only passing
  mentions, no scoped statements).

## 3. First lemma and first falsifier

**Theorem T (PROVED; full proof in §5).** Fix ψ ∈ C_c^∞(−2, 2), 0 ≤ ψ ≤ 1, ψ = 1 on [−1, 1]. For 0 < δ ≤ 1/2, ε > 0,
A ≥ 2 and H := U^ε/δ:
  N₂(p, U) ≤ 4δ|E1⁺| + 8δ·Σ_{1 ≤ h ≤ H} |T(h)| + C_{A,ε}·|E1⁺|·U^{−εA}.
*Corollary T (CONDITIONAL on TD(η)).* If |T(h)| ≤ C₀U^{1−η} for 1 ≤ h ≤ U^η uniformly for primes p and
c₁p^{1/4} ≤ U ≤ c₂p^{1/4}, then N₄ ≤ N₂ ≪ U^{1−η/2} log p.

**Falsifier F1 (EVIDENCE; `scripts/z54_bilindiv_td.c`, `data/z54/bilindiv/td_falsifier.txt`).** If |T(h)| were of
size ≍ U for small h (a bias of {w_k} towards integers or any fixed point), TD would be false and Theorem T useless.
Measured, 1 ≤ h ≤ 20: rms_h |T(h)|/√|E1⁺| = 0.79–1.26 and max 1.31–2.62 at 20 primes ≡ 1 (24) near 10¹² (U = 1000,
|E1⁺| ≈ 1 450–1 640), 10 at 10¹⁴ (U = 3162), 6 at 10¹⁶ (U = 10⁴, |E1⁺| ≈ 15 000); the same at 10 odd squares and 10
near-squares m² + 4 at 10¹², 3 odd squares at 10¹⁶, and at the 14 FRONTIER §4 item-14 test primes. Square-root scale
everywhere: **F1 does not falsify TD.** The script's N₂ agrees with brute force at 300 primes near 10⁸
(`scripts/z54_bilindiv_brute.py`).

## 4. (to come) Tool-by-tool scoped no-gos with exponent deficits; §5 proofs; §6 computations; §7 screens; §8 verdict.
