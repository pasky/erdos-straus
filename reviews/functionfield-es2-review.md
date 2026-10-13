# R166 — hostile review of FUNCTIONFIELD_ES2.md (O166, branch side-agent/ff-extinction)

Reviewer: R166. Reviewed commit: merge of side-agent/ff-extinction as of review start.
From-scratch scripts: `scripts/review_ff2_*.py` (own F_q[T] arithmetic, no author code imported).

## Summary verdicts (filled in claim by claim)

| Claim | Verdict |
|---|---|
| §0.1 compactness criterion | (pending) |
| §0.1 tree plateau "partly an artefact" | (pending) |
| §0.2 Case A impossibility at x*_c | (pending) |
| §0.2 Case B normal form + searches | (pending) |
| Conjecture 0.2 labels | (pending) |
| Prop 1.1 | (pending) |
| Prop 3.1 | (pending) |
| Novelty / labels | (pending) |

## Defects

(numbered below as found)

### Claim §0.2 Case A impossibility at x*_c (odd q, A = T^k, k ≥ 2) — SOUND-AFTER-REPAIRS

Conclusion is TRUE (re-proved below), but the written sketch is not a proof and one intermediate assertion is
false as stated.

**D1 (MINOR→MAJOR for the label).** §0.2 "comparing EF = a1 + b1 with E ≡ −(1 + cT) (mod T^{α+2}) forces
b1 = 1, L' = a1' = 1, E = −(1 + cT)". False before the leading-coefficient condition is used: for α = 1 every
a1' ≡ c (mod T^{k+j−1}) gives a congruence-valid divisor E = −(T a1' + 1) = −(a1 + b1). Counterexample found by
`scripts/review_ff2_caseA.py 3 2 1,1 3`: q = 3, k = 2, c = 1, a0 = 1, b0 = T³ + T (L' = T² + 1 ≠ 1),
E = −(T³ + T + 1); it is killed only by lc(E) = −1 ≠ 1 = lc(s). Also "(−c)^α = −1" is not what the algebra
gives (see below: μ = (−c)^α and lc forces μ = c). The label "PROVED, sketch to be written out" is therefore
premature. Repair: replace by the proof below (R166 has checked every step), or relabel "CLAIM (sketch)".

*Repair proof (R166).* Setting: x ≡ u = 1 + cT (mod T^∞), x ≡ 1 at every prime ≠ T, q odd, k ≥ 2.
Validity forces T^{k+j} | u + E and L' | 1 + E, hence T ∤ E, x ≡ 1 (mod E), and in Case A E | a1 + b1
(a0 = g a1, b0 = g b1, gcd(E, L) = 1). Let s be the family sum: in Case A lc(s) = lc(a1 + b1) when the two
terms have equal type, else 1.
(1) E + 1 ≡ −cT (mod T^{k+j}), k + j ≥ 2, so E + 1 = T·L'·H with T ∤ H ≠ 0, hence deg E ≥ 1 + deg L'
= 1 + deg g' + deg a1' + deg b1'. With deg a1 ≥ deg b1 (WLOG) and deg E ≤ deg(a1 + b1) ≤ deg a1 = α + deg a1'
(T^α ∥ a1): α ≥ 1 + deg g' + deg b1' ≥ 1, so T ∤ b1 and v_T(L) = j = γ + α, k + j ≥ α + 2.
(2) F := (a1 + b1)/E has deg F ≤ α − 1 − deg b1 − deg g'. Mod T^α: −(1 + cT)F ≡ b1. Thus (1 + cT)F + b1 is
≡ 0 (mod T^α) and of degree ≤ max(α − deg b1, deg b1) ≤ α, so (1 + cT)F + b1 = μT^α, μ ∈ F_q, and μ = 0 if
deg b1 ≥ 1.
(3) a1 = EF − b1 = F(E + 1 + cT) − μT^α with T^{α+2} | E + 1 + cT, so a1' ≡ −μ (mod T²); T ∤ a1' gives μ ≠ 0,
hence b1 = 1 and (1 + cT) | μT^α − 1, i.e. μ = (−c)^α, F = (μT^α − 1)/(1 + cT), deg F = α − 1, lc F = μ/c.
(4) deg a1 ≥ 1 > deg b1, so lc(s) = 1 in all Case A type combinations; lc(E) = lc(s) = 1, and lc(E)lc(F) = lc(a1)
= 1 gives μ = c. Degrees: deg E = deg a1 − deg F = 1 + deg a1', so (1) forces g' = 1, deg H = 0, E = T a1' − 1.
(5) a1 = EF − 1 gives a1'(T^α − TF) = −(F + 1). Multiplying by (1 + cT) and using μ = c:
(1 + cT)(T^α − TF) = T(T^{α−1} + 1) and (1 + cT)(F + 1) = cT(T^{α−1} + 1). Hence a1' = −c, so c = −1 (a1' monic),
and then μ = (−c)^α = 1 ≠ −1 = c (q odd). Contradiction. ∎
Independent EVIDENCE (`scripts/review_ff2_caseA.py`, all monic a0, b0 of degree ≤ 4 (q = 3) / ≤ 3 (q = 5) / ≤ 2
(q = 7), all divisors E with every leading coefficient): congruence-valid Case A divisors exist (10, 4, 4, 5, 1, 1,
0 for the runs in `data/review_ff2_caseA_log.txt`), but **none** with admissible lc; sanity: u = 2 + T (q = 3)
yields admissible hits (e.g. a0 = T, b0 = T + 1, E = 2T + 1 with lc(a0 + b0) = 2).

### Claim §0.1 compactness criterion — SOUND (two MINOR wording defects)

Re-derivation. R̂ = lim R/W (W ≠ 0 ordered by divisibility) is profinite, R̂^* = lim (R/W)^* is a closed, hence
compact, subset. For a linear family F the validity set V_F ⊂ R̂^* is the preimage of a subset of (R/W_F)^*, so it is
clopen. That V_F is well defined needs validity at P to be independent of n ≥ n_F, not only "a function of P mod W"
(the literal statement of FUNCTIONFIELD_ES Lemma 6.2). R166 checked this from the proof of Lemma 6.2. The congruences
A·a0, A·b0 | P + E, the residue of s mod E (built from P mod E and X mod a0E, b0E, LE), the leading coefficient of s
(1 for distinct types, lc of a0 + b0 or of L/a0 + L/b0 for equal types) and "s ≠ 0" contain no n. So
O = R̂^* \ ∪_F V_F is closed. (⇐) If O = ∅, compactness gives a finite subcover. With W = lcm W_F, every
irreducible P of degree n ≥ max n_F has P ∤ W, so its class mod W is a unit class lying in some V_F, and F is valid
at P. (⇒) If x ∈ O and {F_i} is finite, put W = lcm W_{F_i}. The unit class x mod W meets no V_{F_i} and contains
monic irreducibles of every large degree (Fact 5.2, error term ≤ (D + 2)q^{n/2}/n). None of them is covered. ∎
Every step holds.

**D2 (MINOR).** §0.1 says a finite covering gives "hence a proof of ES_q(A,·) by Lemma 6.2 + a finite check". The
finite check can fail: for q = 3, A = T², ES fails at n = 3, 4, 5 (FUNCTIONFIELD_ES §6.3). Repair: "a proof of
ES_q(A, P) for all P of degree ≥ max n_F; the smaller degrees need a finite check, which may find failures".

**D3 (MINOR).** Make explicit that V_F does not depend on n ≥ n_F (the argument above). Lemma 6.2 as stated only
gives "depends on P mod W". Prop 3.1 rests on the same point.

### Claim §0.1 "the q = 3, A = T² tree plateau is (at least partly) an artefact" — SOUND as an Assessment (label it)

R166 confirmed from the code (`scripts/ff2_tree.c`, `find_family`, lines 36–55) that a leaf class r mod W is tested
only against families whose E is a unit multiple of a divisor of W/A and whose a0, b0 divide W/(A·E). So
W_F | W_leaf. With a fixed refinement list, a family whose E has a prime factor outside the list can never certify
a leaf. The plateau therefore bounds only the restricted search. The positive evidence is weak: the slice
x ≡ 1 off T has Haar measure 0, so Case B families found there show only that such families exist and cover some
classes. They do not show that the 1 % uncovered mass of the tree shrinks once large-prime E are allowed. The
author's own covered-mass numbers (§3: 0.04 → 0.23 of one cylinder, increments ≈ 0.01) fit either answer.

**D4 (MINOR, labels).** "the plateau ... is (at least partly) an artefact of E | W, not evidence of an obstruction
of positive measure" carries no label and reads as a finding. Repair: label it Assessment, and add "the tree data
are then neither evidence for nor against O(3, T²) having positive measure". Also, "families with E having large
prime factors are valid deterministically (P ≡ 1 mod E)" holds only on the measure-0 slice x ≡ 1 off T. At a
generic point of an uncovered leaf such a family is valid on a sub-class mod ℓ, not deterministically. Say so.

### Claim §0.2 Case B normal form and exact searches — SOUND (normal form); "consequences" GAP (unproved as written)

*Reduction (re-derived).* At x*, x ≡ 1 (mod E) and X ≡ T^{−k} (mod E). Mixed types give
E | a0 + (T^k b0)^{−1}, i.e. E | D := 1 + T^k a0 b0 = 1 + T^{k+j} g L'. lc(s) = 1 (distinct degrees), so E and
E' = D/E are monic. With M = T^{k+j}L', D ≡ 1 (mod M) and deg D ≤ k + 2j + 2 deg L' < 2 deg M. Hence E or E' is
the least residue of its class mod M (classes −u and (−u)^{−1} at T, −1 at L'). This is the author's ρ/ρ'
reduction, and it is correct. Every g | L occurs (a0 = L, b0 = g).
*Normal form (****) (re-derived).* E = T^{N+1}Z − (1 + cT) and (1 + cT)E' = T^{N+1}Z' − 1 with N + 1 = k + j.
Expanding (1 + cT)·D = E·(1 + cT)E' and dividing by T^{N+1} gives (1 + cT)L'g = T^{N+1}ZZ' − Z − (1 + cT)Z'
exactly. lc Z = 1, lc Z' = c. Correct.
*Independent search.* `scripts/review_ff2_caseB.py` uses its own arithmetic and enumerates (L', j, g) directly, not
via (****). A `brute` mode enumerates **all** monic divisors of D and asserts agreement with the ρ/ρ' reduction. It
agrees on every case with deg L' ≤ 2, j ≤ 3 for u = 1 + T, 1 + 2T, 1 + T + 2T². Sanity: at u = 1 + T + 2T² it
re-finds E = T² + 2T + 2 (L' = 1, j = 2, g = 1, D = T⁴ + 1) plus 7 other families. Full runs:
**0 Case B families at u = 1 + T and u = 1 + 2T for deg L' ≤ 7, j ≤ 8, all g | L** (557685 (L', j, g) cases each;
`data/review_ff2_caseB_log.txt`). This reproduces the author's search.

**D5 (MINOR).** "Consequences proved so far: j = 0 impossible; Z + Z' = 0 impossible; L' | Z + Z';
z ≠ z' ...; g = T·H'·Z − (Z + Z')/L'". No proofs are written. R166 did not re-derive them. They are used nowhere
else in the document. Repair: either write the proofs or relabel them "claimed (proof not written)".

*Quadratic-reciprocity parity (§3 paragraph, labelled PROVED, q = 3) — SOUND.* Re-derived: with E monic, E(0) = −1,
E ≡ −1 (mod L'), G := L'g' (T-free) and m := N + 1 + γ, T^m G ≡ −1 (mod E) gives (T/E)^m (G/E) = (−1/E) = (−1)^{deg E}.
Reciprocity (q ≡ 3 mod 4) gives (T/E) = (−1)^{deg E}(E(0)/T) = (−1)^{deg E + 1} and (G/E) = (−1)^{deg G·deg E}(E/G)
= (−1)^{deg G (deg E + 1)}. So (deg E + 1)·deg D ≡ deg E (mod 2), hence deg E and deg D are even. The argument
uses only u(0) = 1, so it holds at every slice point x ≡ 1 off T. Consistent with all 8 sanity families above
(deg E ∈ {2, 4, 6}, deg D ∈ {4, 6, 8}). This paragraph sits in §3 ("(d) Degree parity") although it belongs to
§0.2 (MINOR, placement).

### Conjecture 0.2 — labels SOUND (CONJECTURE + EVIDENCE)

The document labels it CONJECTURE/EVIDENCE consistently in §0.2, §3 and the report. **D6 (MINOR, framing).** The
author's own control (§3: two generic lifts in the same cylinders also get 0 Case B families in the same range)
shows that the search range does not distinguish x* from generic points. The "EVIDENCE" for Conjecture 0.2 is
therefore only "no counterexample in a range where generic points also have none". Repair: say this next to the
conjecture in §0.2, not only in §3. Also, "x*_c ∈ O(3, T²)" needs Case A (proved, see the repair above) **and**
Case B for all (L', j, g). The heuristic "expected number of covering Case B families diverges over ℓ" (§0.2, end)
points *against* the conjecture for generic u. The text should state that the conjecture asserts x* is
non-generic.
