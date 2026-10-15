# R247 — hostile review of O227 (FF_THIRDS_CORNER.md, branch side-agent/ff-thirds-corner)

Reviewer: R247. Status: IN PROGRESS (round 1). From-scratch scripts: scripts/review_r247_*.

## Summary verdicts
(filled in claim by claim below)

## Claim-by-claim

### Setting / "covers at level N" (FUNCTIONFIELD_ES3 Lemmas 1.1, 2.1, 3.1)
Re-derived: a family (L', j, γ, g', E) has s = N + 1 + γ, 0 ≤ γ ≤ j = N + 1 − k, so a tuple of parameter s lives on the
levels N(s) = ⌈(s + k − 2)/2⌉ ≤ N ≤ s − 1; the cylinders are nested decreasing in N, so "tuple covers x_u" ⟺
E ≡ −u (mod T^{N(s)+1}). (B) gives T ∤ m', g', w₁, C₁ and v₁(0) ≠ 0. SOUND.

### Lemma 1.1 (R3 identity) — SOUND
Re-derived: E·C₁ = (Tg'm'w₁ − 1)C₁ = Tg'(T^{s−2} + v₁) − C₁ = g'T^{s−1} + w₁; symmetric for E'. Also re-derived
EE' = 1 + T^sL'g' (used in Prop 2.1) and R4: Ev₁ = m'w₁(w₁ + C₁) − v₁ = T^{s−2} + m'w₁² (used in Prop 5.1).

### Lemma 1.2 (Liouville lemma) — SOUND
Re-derived line by line. Mod T^m (m ≤ s − 1) EC₁ ≡ w₁, so E ≡ −u gives T^m | w₁ + uC₁, a polynomial of degree
≤ max(a − 1, b − 1 + h); nonzero ⇒ degree ≥ m. Exact case for u = 1 + cT: monic w₁, C₁ force c = −1, w₁ = (T − 1)C₁,
TC₁ = Tg'v₁, gcd(C₁, v₁) = 1 (a common prime divides T^{s−2}, and T ∤ C₁ by (B)) ⇒ v₁ = 1, then (T − 1)m'g'² = T^{s−2} + 1,
0 = 2 at T = 1. Correct. Numerical confirmation: brute-force census (own code `review_r247_census.c`, enumerates all
(m', w₁, C₁), no CRT/Liouville input) — see the census section below.

### Cor 1.3 — SOUND (one MINOR)
Correct for k = 2 (s ≥ 4). The cyclotomic paragraph is correct: v₁ = −1 ⇒ lc(w + C) = −lc g' = 2 ⇒ a = b (unequal degrees
give lc 1) ⇒ 2(a − 1) ≤ s − 2 ⇒ max(a − 1, b) = a ≤ s/2 < N(s) + 1. Every equal-degree tuple misses x*_c. (Note: the
conclusion is not w ↔ C symmetric — correct, because covering is E ≡ −u while E' ≡ −u^{−1} is not a polynomial point.)
* MINOR-1 (statement): "k ≥ 2, s ≥ 4 so that N(s) + 1 ≤ s − 1" is only right for k = 2; in general N(s) + 1 ≤ s − 1 ⟺
  s ≥ k + 2 (as the proof says). E.g. k = 3, s = 4: N = 3, N + 1 = 4 > s − 1. Repair: write "s ≥ k + 2".

### Prop 1.4 (exact tuples) — SOUND-AFTER-REPAIRS (MINOR)
The forward direction is correct (re-derived: C₁ | g' from gcd(C₁, Tv₁) = 1; g₂v₁ = −(u − 1)/T; lc u = −1;
E = Tg₂(T^{s−2} + v₁) − 1 = g₂T^{s−1} − u). The h = 1 reading (T ≡ 1 mod u ⇒ 2 ≢ 0) is correct.
* MINOR-2: the converse ("iff … then the displayed data satisfy (B₁)") omits needed side conditions: T ∤ g₂ (else T | g'),
  deg v₁ < s − 2 (else the product has the wrong degree/leading coefficient and the tuple's parameter is not s), and
  T ∤ (T^{s−2} + v₁)/u, i.e. v₁(0) ≠ 0 (automatic when u'(0) ≠ 0 and T ∤ g₂, not in general since Prop 1.4 does not assume
  u'(0) ≠ 0). Repair: add "T ∤ g₂, deg v₁ < s − 2, v₁(0) ≠ 0" to the converse.
Numerics: my full search (no Liouville input) finds exact tuples (w₁ = −uC₁) only at points with lc u = −1 (levels 3..8,
54 points), consistent with Prop 1.4.

### Prop 2.1 (complete search) — SOUND (one MINOR on the hypothesis N ≥ 3)
Re-derived every step:
* Covering in both orientations: Ê = TMg' − 1 in A (M = m'w₁) and B (M = m'C₁); EE' = 1 + T^sL'g' (re-derived), s ≥ N + 1,
  so E ≡ −u ⟺ E' ≡ −u^{−1} (mod T^{N+1}) ⟺ Mg' ≡ α (mod T^N). Correct.
* Orientation choice: non-exact ⇒ b − 1 + h ≥ N + 1 (A: deg M = s − b − 1 ≤ s − N − 3 + h) or a ≥ N + 2 (B: deg M =
  s − a − 1 ≤ s − N − 3). Correct. Exact tuples are excluded only by Lemma 1.2(ii) and are impossible at x*_c.
* Case 1 (y ≤ N − 1): g' = unique polynomial of degree < N with Mg' ≡ α; X₁ ≡ −g'T^{s−1} (mod Ê) with deg X₁ ≤ deg M <
  deg Ê, so X₁ is the least residue. Correct; the tuple is a function of (M, s).
* Case 2 (y ≥ N): deg M + deg v₁ = s − 3 − y + max(0, ±(a − b)) re-derived from y + t = max(a, b) (which I re-derived:
  deg(w₁ + C₁) = max(a, b) − 1 in odd characteristic). Sign analysis: A, h = 1: b ≥ N + 1, a ≤ s − b ≤ N − 1 (s ≤ 2N,
  true for k ≥ 2); A, h ≥ 2: a − b ≤ s − 2b ≤ 2h − 4; B: b ≤ s − a ≤ N − 2 < a. Correct. v₁ must range over ALL nonzero
  polynomials (any leading coefficient) in the class −T^{s−2} mod M — the code does so (checked by my independent run).
* MINOR-3: Lemma 1.2 needs N + 1 ≤ s − 1 with s ≥ 2N − k + 1, i.e. N ≥ k + 1, not "N ≥ 3": for k = 3, N = 3, s = 4 the
  Liouville step is not available. Harmless (the k = 3 search starts at N = 4), but the hypothesis must read N ≥ k + 1.
* Independent confirmation of completeness: see "Independent search" below — my enumerator does not split on deg g'
  at all (it enumerates the small side as a PAIR (m', X₁), fixes v₁ by CRT modulo T^{min(N+1, s−2)}·m'X₁ from the two
  necessary congruences v₁ ≡ −T^{s−2} (mod m'X₁) and v₁ ≡ −m'w₁²u^{−1} (A) / −um'C₁² (B) (mod T^{n₀}), and enumerates
  every v₁ of that class with deg v₁ ≤ max(a, b) − 2), and in "full" mode drops the Liouville bound entirely (A only,
  deg M ≤ s − 2, which reaches every tuple). A missed case in Prop 2.1 would show up as a full-mode hit not found by zt_lop.

### Lemma 3.1 — SOUND
Re-derived: E ≡ w₁/C₁ (mod T^{s−1}); C₁ ≡ v₁/(m'w₁) and w₁ ≡ v₁/(m'C₁) (mod T^{s−2}); multiply by the T-units m'w₁,
m'C₁ (T ∤ m', w₁, C₁ by (B)). Valid for N + 1 ≤ s − 2. Numerically confirmed on the brute-force census (below).

### Cor 3.2 — SOUND
Re-derived both exact cases (q = 3, c² = 1): (1) v₁ = λ, m' = T + c, (−c)^{s−2} = c ⇒ c = 1, s even, then
1 + C₁ = T(T^{s−3} + 1)/(T + 1) = −Tg' ⇒ lc g' = −1; (2) C₁ = 1, m' = 1, lc g' = −c ⇒ c = −1, (1 − T) | T^{s−3} + 1
false at T = 1. Degree bookkeeping correct. The case-1 consequence: deg M + y ≤ N − 1 ⇒ Mg' = −c ⇒ M = g' = 1,
E = T − 1 (not a tuple); so y ≥ N − d, t = b − y ≤ s − N − 1 ≤ N − 1, hence d + (a − 1) ≥ N + 1. Correct (needs N ≥ 4 for
N + 1 ≤ s − 2 — stated). The q-general remark is honest.

### Prop 5.1 (Bezout form) — SOUND (MINOR wording)
Re-derived: cMg' = T^NZ − 1 ⇒ Mg' ≡ −c (mod T^N), deg g' = N + deg Z − d < N, so g' is the case-1 g'; E = cT^{N+1}Z − u;
R4 gives Ev₁ = T^{s−2} + m'w₁². Converse (my derivation): if g' is monic and E | T^{s−2} + m'w₁², put
v₁ := (T^{s−2} + m'w₁²)/E, C₁ := Tg'v₁ − w₁; then E·C₁ = g'T^{s−1} + w₁ (direct expansion), m'w₁C₁ = T^{s−2} + v₁ and C₁ is
monic of degree s − 2 − d (since d < s − 2). So the "iff" holds once lc Z = c is imposed.
* MINOR-4: the "iff" sentence should include "lc Z = c" (stated earlier in the display but not in the iff), and the
  final "E | u² + m'(T²Zw₁)²" is only a consequence (⇒): the converse needs Z to be a unit mod E, i.e. gcd(Z, 1 + cT) = 1
  (gcd(E, u) = gcd(Z, u)). As written ("and then") it is a one-way statement, which is correct; just don't use it as a test.

### Independent search and census (R247 from-scratch code)
* `scripts/review_r247_census.c`: brute-force census of ALL Case B tuples, s ≤ 16, by enumerating every triple (m', w₁, C₁)
  of monic T-free polynomials with deg sum s − 2 and testing Tv₁ | w₁ + C₁, g' monic T-free (no CRT, no Liouville, no case
  split). Counts per s = 4..16: 2, 4, 10, 8, 8, 4, 24, 12, 14, 36, 104, 48, 38 (312 tuples; author's census has 348 for
  s ≤ 17, consistent). Log: `data/review_r247_census_s16.txt`.
* `scripts/review_r247_census_checks.py` on all 312 tuples × 80 polynomial points (deg 1..4, u(0) = 1): EE' = D for all;
  0 violations of Lemma 1.2, of Lemma 3.1 (agreement depths of E + u, m'w₁² + uv₁, um'C₁² + v₁ capped at s − 2), of the
  depth-generalised Cor 3.2 inequalities (h = 1), of the parity laws (z ≡ t ≡ s mod 2, deg E, deg E' even);
  24 exact (tuple, u) pairs, all with lc u = −1 (Prop 1.4).
* `scripts/review_r247_search.c` (enumeration described under Prop 2.1). `scripts/review_r247_census_vs_search.py`: at all
  54 points (deg 1..4, u(0) = 1, u'(0) ≠ 0), k = 2 levels 3..8 and k = 3 levels 4..8, the census coverings minus exact
  ones coincide with my lop-mode hits: 156 covering records (46 exact), 0 mismatching (k, u). **Positive control: 110
  non-exact coverings at polynomial points are found by both methods.**

### EVIDENCE claim "no Case B tuple covers x*_c at N ≤ 20 (k = 2), N ≤ 18 (k = 3)" — SOUND as EVIDENCE (reproduced to 17 / 16)
My searcher (lop mode; completeness of lop mode = Lemma 1.2 only, which I re-proved and which is confirmed against the
Liouville-free census and full mode) at u = 1 + cT: **0 hits at every level 3 ≤ N ≤ 17 for k = 2, c = 1 and c = 2, and
4 ≤ N ≤ 16 for k = 3, c = 1, 2** (`data/review_r247_xstar_k*_c*.txt`; candidate counts grow ×3 per level, e.g. 2.27·10⁷ v₁-
candidates at N = 17). This is an independent reproduction well beyond the requested 12–14 / 11–12. Levels 18..20 (k = 2)
and 17..18 (k = 3) rest on zt_lop alone, whose correctness I have cross-checked against my code at 54 polynomial points to
level 12 (below). I did not re-run zt_lop at N = 20; the logs `data/zt_lop_xstar_c*.txt` do show "hits this level 0"
for every level through 20 (checked by grep).
* The consequence "no linear family of level ≤ 20 (k = 2) is valid at x*_c" follows from this EVIDENCE plus the Case A
  theorem (FUNCTIONFIELD_ES2 §0.2 proof R166-D1, which I re-read: it is a proof at u = 1 + cT exactly, all levels) and the
  A/B dichotomy of FUNCTIONFIELD_ES3 Lemma 1.1. Label EVIDENCE is correct (not PROVED: computer search, one code beyond 17).
* MINOR-5 (provenance): the k = 2, c = 2 log `data/zt_lop_xstar_c2.txt` is NOT committed on side-agent/ff-thirds-corner
  (it exists untracked in the author's worktree, complete through N = 20 with 0 hits; a zt_lop process for N = 21 was still
  running at review time). The committed c1 log ends at N = 20 (0 hits each level). Repair: commit the c2 log (and
  record whether level 21 finished).
