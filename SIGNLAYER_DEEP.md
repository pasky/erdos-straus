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

## 3. Symmetries of the covered set; the orbit of x* (PROVED, elementary; checked on the K ≤ 17 data)

**Lemma 3.1.** The set C ⊂ slice of Case-B-covered points is invariant under (i) u ↦ u⁻¹ and (ii) u(T) ↦ u(−T).
*Proof.* (i) (I)–(II) are symmetric in (h₁, h₁'); swapping them swaps E = −1 + Th₁L' and E' = −1 + Th₁'L', and E'
≡ −u⁻¹ (mod T^{N+1}) (EE' = D ≡ 1), so the swapped solution covers u⁻¹ with the same (K, N). (ii) T ↦ −T is a
ring automorphism of F₃[T] fixing A = T², the slice condition and monicity up to the sign (−1)^{deg}, which is
restored by multiplying h₁, h₁', g', L'', r by the units (−1)^{deg}; (I)–(II) are homogeneous under this. ∎
*Check:* on the K ≤ 17 data the length-4 prefixes (1, 0, x, y) and (1, 1, x + 1, 1 − x − y) carry identical
K-lists (e.g. (1,0,0,0) and (1,1,1,1): K ∈ {14, 15, 16, 17}), which is the composite ι(u) := 1/u(−T).
So x*_c = 1 + cT is paired with ι(x*_c) = 1/(1 − cT) = Σ (cT)^k (v = (c, c², c³, …)); both are uncovered through
K = 17. The x* orbit is {1 ± T, 1/(1 ± T)}: the four slice points whose u is a **rational function of height 1**.

*Assessment.* The only visible special feature of x* in the Case B system is "height 1" (a degree-1 rational
point of the T-adic slice). Lemma 1.1 says a covering family at level K is a pair of monic h₁, h₁' with
h₁h₁'L'' = T^K + r and small r — a **best rational approximation of T^K at ∞** — while (III) is a T-adic
approximation condition at 0. Covering x* thus asks for simultaneous good approximation at the two places 0
and ∞ of P¹ by polynomials of controlled degree; for height-1 targets, the product formula (|·|₀|·|_∞ ≤ 1 for
nonzero polynomials) is the natural tool. I have not turned this into a proof (next step if resumed).

*Cross-validation with FF2's independent searcher (`scripts/ff2_caseB.py`).* (a) At u ≡ 1 + T + 2T² + … both find the
K = 2 cylinder family E = T² + 2T + 2. (b) At the slice point u = 1 + T + T² + 2T³ + T⁵ + T⁶ + 2T⁸ + T⁹ + 2T¹⁰ + T¹²
(digits `1021201102111`), FF2 reported 0 Case B families for deg L' ≤ 4, j ≤ 4; my enumeration predicts coverage
by a K = 10, N = 6 (j = 5) solution, and `ff2_caseB.py 3 2 1 4 5 1021201102111` indeed finds exactly the pair
E/E' with L' = T⁴ + 2T³ + 2T² + 2T + 1, j = 5, g = T⁵(T² + 2T + 1). So FF2's "generic control points" are
covered once j is large enough — consistent with the ≈ 49 % coverage, and confirming the reformulation.

**Lemma 3.2 (degree imbalance at x*; PROVED, elementary).** Let a Case B solution (Lemma 1.1) cover x*_c at level N,
a = deg h₁, b = deg h₁'. Then T^N | h₁ + (1 + cT)h₁' ≠ 0, hence **N ≤ max(a, b + 1)**, and with K ≤ 2N − 2:
either a ≥ b + deg L'' + 2, or b ≥ a + deg L''.
*Proof.* (III) at v = c: h₁L' = −c + T^N y. Insert in (*) T h₁h₁'L' − h₁ − h₁' = T^{K+1}g':
−(1 + cT)h₁' − h₁ = T^{K+1}g' − T^{N+1}h₁'y ≡ 0 (mod T^N) since K + 1 ≥ N. If h₁ = −(1 + cT)h₁', comparing
leading coefficients gives c = −1 and a = b + 1; (I) gives g'r = −ch₁' = h₁', and (II) gives
h₁' | T^K + r with r | h₁', r(0) ≠ 0, so r = 1, h₁' = g', and (II) reads (T − 1)g'²L'' = T^K + 1, false at T = 1.
So the sum is non-zero and its degree ≤ max(a, b + 1) is ≥ N. Finally K = a + b + deg L'' ≤ 2N − 2. ∎
So a covering family at x* is necessarily lopsided (one of E, E' has much larger degree): this is the "two-place
approximation" shape of §3 made concrete, and it allows a targeted deep search at x* (enumerate the small
factor, solve for the large one) — not done in this session.

**Update (K ≤ 19, `bsB_caseB 19`, ≈ 25 min).** Solutions at K = 18, 19: 224, 192 (1036 in total). x*_{±1} still
uncovered (complete through K = 19, i.e. all N ≤ 10 and all admissible L', g). Covered slice measure 0.4906
(K ≤ 19; 0.489 at K ≤ 17); random slice points 48.9 % covered. Counts grow by ≈ 1.3–1.5 per two levels while each
new cylinder has measure ≈ 3^{−K/2}, so the increments keep shrinking (EVIDENCE for a limit ≈ 0.5).
Counts archived in `data/bsB_caseB_K19_counts.txt`.
