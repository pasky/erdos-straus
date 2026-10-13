# SIGNLAYER_DEEP — deep dive of spark brainstorm B (task O175)

Status: in progress. **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Memos: `BRAINSTORM/bsB_*.md`; scripts `scripts/bsB_*`.

Chosen topic (from the memos): the function-field sterile point x*_c (FUNCTIONFIELD_ES2 §0.2, Conjecture 0.2),
read through the sign layer (`bsB_sterile_pretentious.md`: x* is a profinite square, maximally pretentious; its
only sign-layer constraint is a degree parity). Goal: decide whether x*_c (q = 3, A = T²) is covered by a Case B
family, construction-first; if not, find the structural reason.

## 1. Case B at the slice x ≡ 1 off T is a finite search for each level (PROVED, elementary)

Setting (FF2 §0.2, q = 3, k = 2; everything holds for odd q with the obvious changes noted). A point of the slice
is x_u (≡ 1 at every prime ≠ T, ≡ u mod T^∞), u = 1 + Tv, v(0) ≠ 0. FF2's Case B reduction: for monic L'
(T ∤ L'), j ≥ 1, g = T^γ g' (g' | L' monic, 0 ≤ γ ≤ j), N := j + 1, D := 1 + T^{N+1}L'g, a Case B family valid at
x_u exists iff D = E·E' with E, E' monic, E ≡ −u (mod T^{N+1}), E ≡ −1 (mod L').

**Lemma 1.1.** Put K := N + γ − 1 (so N − 1 ≤ K ≤ 2N − 2) and L' = g'L''. Case B families valid at x_u with
these (N, γ) correspond bijectively to tuples (h₁, h₁', g', L'', r) of polynomials, h₁, h₁', g', L'' monic with
nonzero constant term, such that
* (I) `h₁ + h₁' = T·g'·r`,
* (II) `h₁·h₁'·L'' = T^K + r`,
* (III) `h₁·L' ≡ −v (mod T^N)`, L' = g'L''
(E = −1 + T h₁ L', E' = −1 + T h₁' L'). Moreover deg r < deg(h₁h₁'), so **L'' = quo(T^K, h₁h₁') and
r = L''h₁h₁' − T^K are determined by (h₁, h₁', K)**, and deg h₁ + deg h₁' + deg L'' = K. In particular, for each
K the set of Case B families on the slice is finite (deg L' ≤ K + max deg h ≤ 2K), and each family covers the
cylinder `u ≡ 1 − T·h₁·L' (mod T^{N+1})`.

*Proof.* E ≡ −1 (mod L') ⟺ E = −1 + L'h; E monic and deg(L'h) ≥ 1 (else E = 1, impossible mod T²) give
lc h = 1; same for E' = −1 + L'h'. EE' = D ⟺ L'hh' − h − h' = T^{N+1}g (cancel L'). E ≡ −u (mod T^{N+1}) ⟺
L'h ≡ −Tv; so h = Th₁ with h₁L' ≡ −v (mod T^N) (III), h₁(0) ≠ 0. Then T h₁h₁'L' − h₁ − h₁' = T^{K+1}g' (*).
Mod T: h₁'(0) = −h₁(0) ≠ 0. Leading terms: the left side has degree 1 + a + b + deg L' (a, b = degrees of
h₁, h₁') because h₁ + h₁' has degree ≤ max(a, b); so a + b + deg L'' = K. Writing (*) as
g'(T h₁h₁'L'' − T^{K+1}) = h₁ + h₁' shows g' | h₁ + h₁' and T | h₁ + h₁'; define r by (I); dividing (*) by Tg' gives
(II). deg r = deg(h₁ + h₁') − 1 − deg g' ≤ max(a, b) − 1 < a + b (if min(a, b) = 0 then deg r ≤ a − 1 < a + b
still). Conversely (I)–(III) give (*) and hence E, E' with all properties; the congruence E' ≡ −u⁻¹ is then
automatic (EE' = D ≡ 1 mod T^{N+1}). ∎

*Check against FF2:* the known cylinder family E = T² − cT − 1 (a0 = b0 = T, j = 1, D = 1 + T⁴) is
h₁ = T − c, h₁' = T + c, g' = L'' = 1, r = −1, K = 2, N = 2, covering u ≡ 1 + cT + 2T² (mod T³), as FF2 states.

*Consequence for the heuristic (Assessment).* FF2 §0.2 argued that the expected number of covering Case B
families diverges (sum over deg L'). Lemma 1.1 shows deg L' ≤ 2K is forced, so at fixed level the count is
finite, and the naive expected number of solutions at a fixed point is Σ_K poly(K)·3^{−K}-type, **convergent**.
So the heuristic no longer predicts that x* (or a generic slice point) is covered: sterility of individual
slice points is the heuristically expected behaviour, and Conjecture 0.2 is a "convergent lottery" statement.

## 2. Complete enumeration through level K = 17 (CERTIFIED by exhaustive computation; EVIDENCE beyond)

`scripts/bsB_caseB.c` enumerates, for each K ≤ KMAX, **all** solutions of Lemma 1.1 (I)–(II) (all monic h₁, h₁'
with h₁(0) = −h₁'(0) ≠ 0 and deg h₁ + deg h₁' ≤ K; then L'', r, g' are forced), and prints w = h₁L' mod T^{K+1}.
A solution covers the slice points v ≡ −w (mod T^{N₀}), N₀ = max(2, ⌈K/2⌉ + 1) (the largest cylinder over the
admissible N ∈ [N₀, K + 1]). `scripts/bsB_caseB_cover.py` takes the union. Run `bsB_caseB 17` (155 s):
* solutions per K = 2, …, 17: 2, 4, 10, 8, 8, 4, 24, 12, 14, 36, 104, 48, 38, 36, 148, 124 (620 in total) — bounded
  in size, nothing like 3^K;
* sanity: the two K = 2 solutions are FF2's cylinder family (v ≡ c + 2T, i.e. u ≡ 1 + cT + 2T²), and FF2's
  check family E = T² + 2T + 2 (a0 = 1, b0 = T²) is the K = 2, N = 3 instance of h₁ = T + 2;
* **x*_1 and x*_2 (v = c) are not covered by any Case B family with K ≤ 17**, i.e. with N ≤ 18 (j ≤ 17) and every
  admissible L', g — by Lemma 1.1 this search is *complete* through K = 17 (FF2's search was deg L' ≤ 7, j ≤ 8, and
  incomplete in L' for j ≥ 4). Closest approach: the first nonzero digit of w − w₀ sits at index z with
  max z = 1, 1, 1, 2, 1, 1, 3, 2, 2, 2, 3, 3, 4, 5, 6, 4 for K = 2..17, versus the required z ≥ N₀ = 2..10.
* **Covered measure of the slice** (Haar measure on v ∈ F₃[[T]]^*, cumulative in K): 0.333 (K ≤ 4), 0.407 (≤ 7),
  0.457 (≤ 9), 0.465, 0.471, 0.479, 0.481, 0.483, 0.485, 0.488, **0.489 (K ≤ 17)**. Increments ≈ 0.002–0.003 per
  level and decreasing: the Case B-covered part of the slice appears to converge to ≈ 0.5, not 1. Random slice
  points: 48.7 % covered (20000 samples). By digit prefix (v₀, v₁): (c, 2) is fully covered (the K = 2 family);
  (c, 0) and (c, 1) only 23.4 % each. Symmetry T ↦ −T (v(T) ↦ −v(−T)) is visible in the table.
* Case A on the slice: FF2's brute-force checker `ff2_caseA_check.py 3 2 3 u` finds **0** Case A families at four
  further slice points (u low digits 1 + T + T² + T³ + …, 1 + T + 2T² …, 1 + 2T + …; deg a0, b0 ≤ 3) — EVIDENCE that
  Case A is absent on the whole slice, not only at x* (FF2 proves it at x* only).

**Reading (Assessment).** With Lemma 1.1 the old divergence heuristic is gone; the data say the slice is split
roughly half/half by Case B, and Case A seems absent. If both persist, O(3, T²) ∩ slice has positive measure and
x*_c is just one of uncountably many sterile slice points; FF2's Conjecture 0.2 ("no finite linear covering for
q = 3, A = T²") would then hold for a "convergent-lottery" reason, not for a structural property of x*. A *proof*
still needs one explicit point excluded at every level K; §3 tries to find a point where this is provable.
