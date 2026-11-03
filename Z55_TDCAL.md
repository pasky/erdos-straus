# Z55_TDCAL — depth lane TDCAL (wave z55, gap 1): how hard is TD?

ES is OPEN. Nothing here proves or disproves it. This lane is **upper-bound calibration work only** (FRONTIER §7.1,
balanced block / 2-cycles); even full success would say nothing about positivity. Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Results are internal.

Brief: `z52bbriefs/z53_depth.md` (rules), kickoff `z52bbriefs/z55_lanes.md` §TDCAL. Predecessors: `Z54_BILINDIV.md`
(Thm T, TD(η), Prop 4.3, Remark 4.1), `Z54_BILINJAC.md` (Thm R, TS, Prop R′, §5 Jutila comparison), `Z53_HYP2CYCLE.md`
(MIX), `Z53_SQSIEVE.md`. Scripts `scripts/z55_tdcal_*`, data `data/z55/tdcal/`. Literature: `data/z55/tdcal/LIT_CHECK.md`.

*Status: CHECKPOINT 1 skeleton.*

## 0. Notation (as in Z54_BILINDIV)

* p odd prime (n a general positive integer where stated), U ≥ 2 an integer, fourth-root range c₁p^{1/4} ≤ U ≤ c₂p^{1/4}
  with 16U³ ≤ p.
* N₂(n, U) := #{{u, B} ⊂ (U, 2U], u ≠ B : uB | n + u + B} (product-divisibility definition, valid for every n).
* E1 = E1(p, U) := {(k, m) ∈ ℕ² : p + 2U < km ≤ p + 4U, U² < m ≤ 4U²}; s := km − p ∈ (2U, 4U]; D := s² − 4m;
  E1⁺ := {D ≥ 1}; w := √D. T(h) := Σ_{E1⁺} e(hw).
* TD(η): |T(h)| ≤ C₀U^{1−η} for 1 ≤ h ≤ U^η, uniformly for primes p and U in the fourth-root range. Theorem T
  (BILINDIV, PROVED): TD(η) ⇒ N₂ ≪ U^{1−η+ε}.
* Δ(x) := Σ_{n≤x} d(n) − x log x − (2γ − 1)x; D(x, y) := Σ_{x<n≤x+y} d(n) = y log x + 2γy + Δ(x+y) − Δ(x) + O(y²/x).

## 1. Statements attacked

**(Q1) Calibration.** Does TD (or TS, MIX) imply a pointwise short-interval divisor statement known to be open (e.g.
Jutila's conjecture Δ(x+y) − Δ(x) ≪ x^ε√y at y = x^{1/4}, Ivić JTNB 21 (2009) (1.13), or a power-saving asymptotic
for the untwisted strip count |E1|), or is TD genuinely different because of the phase and the strip restriction?
Precise targets:
* CNT(η) (untwisted count): |E1(p, U)| = 2U log 4 + O(U^{1−η}) uniformly in the fourth-root range (OPEN).
* The exact relation of CNT, TD, TS and Jutila's conjecture, as theorems about which frequency bands of one common
  family of exponential sums each statement involves.

**(Q2) Partial results.** TD (or R2 itself) on average over n in short windows, for many U, or smoothed — and the exact
missing pointwise piece.

**(Q3) Beyond Voronoi at one p.** Can level-averaging (k) or frequency-averaging (h) give anything at a single p?

## 2. Why this is not already closed

* BILINDIV §4.2 records TD vs MIX as "neither shown to imply the other" and gives a stationary-phase *Assessment* of a
  double dual; it proves no comparison with the untwisted count or with Jutila's conjecture.
* BILINJAC §5 calls square-root TS "a twisted analogue of Jutila's conjecture" and explicitly proves no implication.
* No memo treats averages over p for R2/TD (`git grep` on "average over p" finds only unrelated B6 items).

## 3. First result (checkpoint 1): averaging over n is free (PROVED)

**Proposition A.** For all integers X ≥ 0, Y ≥ 1, U ≥ 2:
  Σ_{X<n≤X+Y} N₂(n, U) = #{(u, B, M) : U < u < B ≤ 2U, uB | M, X < M − u − B ≤ X + Y}
                       ≤ Σ_{X+2U < M ≤ X+Y+4U} τ(M)² .
Consequently, for n ≍ U⁴ and every ε > 0:
(a) the mean of N₂(n, U) over any Y consecutive integers n is ≪_ε (1 + U/Y)U^ε;
(b) for every η ∈ (0, 1), among any U consecutive integers n at most O_ε(U^{η+ε}) have N₂(n, U) > U^{1−η};
(c) more precisely, Σ_{X<n≤X+Y} N₂(n, U) = Y·Σ_{U<u<B≤2U} 1/(uB) + O(U²), so for Y ≥ U^{2+ε} the window mean is
    ½(log 2)² + o(1).
*Proof.* The map (n, {u < B}) ↦ (u, B, M := n + u + B) is injective and lands in the displayed set, and conversely each
such (u, B, M) gives n = M − u − B with uB | n + u + B. Since U < u < B ≤ 2U, M ∈ (X + 2U, X + Y + 4U]. For fixed M, the
number of pairs with u | M and B | M is ≤ τ(M)². This gives the identity and the inequality; (a) follows from
τ(M) ≪_ε M^{ε/8} with M ≍ U⁴, and (b) from (a) with Y = U by Markov. For (c), count multiples of uB in an interval of
length Y: Y/(uB) + O(1) for each of the < U² pairs, and Σ_{U<u<B≤2U} 1/(uB) = ½(log 2)² + O(1/U). ∎

*Reading (Assessment).* R2 is elementary on average over any window of U^{η+ε} = p^{η/4+ε} consecutive integers n, and
fails on at most a U^{η−1+ε} proportion of every window of length U. Hence any argument that proves R2 or TD "on
average over p", with averaging length ≥ p^{δ}, is worth nothing for the balanced block: the whole difficulty is
the single-n bound. In particular averaged forms of TD (Q2) are not a partial result toward R2 in any useful sense.

**EVIDENCE (`scripts/z55_tdcal_window.c`).** n ∈ (10⁸, 10⁸ + 20000], U = 100: Σ N₂ = 4662, mean 0.233, max 4;
the (u, B, M) count with the window's M-range is 4707. n ∈ [10¹², 10¹² + 2000), U = 1000: Σ N₂ = 461, mean 0.231,
max 3; histogram 0:1599, 1:347, 2:48, 3:6. (Mean over all integers, not only primes; ½(log 2)² = 0.2402.)

## 4. Plan (remaining)
1. Band-separation theorem (Q1): smoothed CNT and smoothed TD expanded in the remainder phase θ_m = {−p/m}: the count
   lives on |ν| ≤ U^{1+ε}, T(h) on ν ≍ hU²; consequences for implications; comparison ladder with Jutila.
2. Conic/Pell form of the strip by D (m | p² − D) and the two-shift form of N₂; what each gives.
3. Q3: test level/frequency averaging; scoped statements.
