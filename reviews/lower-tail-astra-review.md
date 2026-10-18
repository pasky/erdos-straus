# R285 — hostile review of O275 (LOWER_TAIL_ASTRA.md, GPT-Astra lower-tail attack)

Reviewer: R285 side agent, branch `side-agent/review-tail-astra` (merged `side-agent/lower-tail-astra` at dbb88f9b-era head).
Scope: LOWER_TAIL_ASTRA.md §§1–6, BRAINSTORM/z43_astra_word_forest.md, AGENT_REPORT_O275.md, the author's self-review.
Every lemma was re-derived by hand; all numerics were recomputed with reviewer-written code that does not reuse
`z43_astra_*`:

* `scripts/review_lta_forest.c` (C, `gcc -O2 … -lm`; run `review_lta_forest 1000000 200000`, ≈11 s, one core,
  `ulimit -v 8000000`; output `logs/review_lta_forest_1e6.txt`). Edges by divisor enumeration of n+u for u with
  (u−1)u ≤ n+1; checks (per edge) unique parent, parent = (−n mod v), acyclicity by union–find, word identity,
  unit endpoints at primes, (A/n) = χ(u)χ(v), (A*/n) = (A/n), and (A/n) = −1 ⟺ five 2-adic conditions; and, for every
  odd prime/odd square ≤ 2·10⁵ (18 206 inputs), an **edge-by-edge** comparison with the O(n) residue-parent scan
  v = 2..n+2, r = −n mod v.
* `scripts/review_lta_counts.py` (sympy): O(n) scan vs divisor scan for all odd n ≤ 2000; edge totals.
* `scripts/review_lta_fixtures.py` (sympy): exhaustive component BFS (neighbours of x = divisors v of n+x with
  xv | n+x+v) for the Thm 3.1, 3.2, 5.1 and Prop 4.2 families.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 2.1 (forest, unique parent −n mod v, vertex bound, diagonal words) | **SOUND** |
| Lemma 2.2 (sign = χ(u)χ(v); bichromatic ⟺ five-slice for n ≡ 1 (4), unit endpoints) | **SOUND** (sign identity and five-slice equivalence imported, correctly cited) |
| Thm 3.1 (four forms ⇒ closed 8-vertex all-residue component of 1) | **SOUND** (one MINOR wording point, D1) |
| Thm 3.2 (fixed finite roots fail; CONDITIONAL on Dickson) | **SOUND** |
| Lemma 4.1 (continued-fraction recurrence, Fibonacci growth) | **SOUND** |
| Prop 4.2 (arbitrarily long all-residue paths, Dirichlet) | **SOUND** (MINOR wording, D2) |
| Thm 5.1 (p = 2521+9240a, q = 211+770a: ℓ(p) = 11 isolated) | **SOUND** |
| §6 census figures | **SOUND** — every figure reproduced exactly |
| Novelty / attribution | **SOUND-AFTER-REPAIRS** (D4, D5) |
| Labels | **SOUND** |

No FATAL or MAJOR defect. Details follow claim by claim.

## 1. Lemma 2.1 — SOUND

*Re-derivation.* If u < v are adjacent, uv | n+u+v ⇒ v | n+u ⇒ u ≡ −n (mod v), and 1 ≤ u < v forces u = r_v (so r_v > 0).
A cycle's maximal vertex would have two distinct smaller neighbours: impossible. If gcd(v,n) = 1 then gcd(v,r_v) = 1,
v | n+v+r_v already, so v·r_v | n+v+r_v ⟺ r_v | n+v+r_v ⟺ r_v | n+v. Vertex bound: t ≥ 1 gives (u−1)(v−1) ≤ n+1; for
u ≥ 2, v ≤ (n+u)/(u−1) ≤ n+2; for u = 1, v(t−1) = n+1 with t ≥ 2, so v ≤ n+1. Diagonal u = v ⇒ u | n; at prime p > 3
only u = 1 (t = p+2), A = p+1, sign +1; u = p forces tp = 3. All correct.

*Numerics (from scratch).* At all 78 497 odd primes ≤ 10⁶ and all 499 odd squares 9..999²: every edge's larger
endpoint has exactly one smaller neighbour, equal to −n mod v; union–find finds no cycle. For all odd primes/squares
≤ 2·10⁵ and all odd n ≤ 2000 the O(n) residue-parent scan reproduces the divisor-enumerated edge set edge-for-edge.

## 2. Lemma 2.2 — SOUND

Av = (tu−1)v = n+u, so A ≡ u v⁻¹ (mod n) when gcd(uv,n) = 1, and (A/n) = χ(u)χ(v); also A* = tv−1 ≡ v u⁻¹, same sign.
This is SIGN_IDENTITY Lemma 1.1 (χ(w) = (−A/n) = (−uv/n)); for n ≡ 1 (4) the minus sign is invisible, so the
author's sign convention is consistent. The equivalence "(A/n) = −1 ⟺ 4 | t, u, v, tu−1 or tv−1" is DEDEKIND_ES Thm 4.5
(as restated in SYNTHESIS_SPARKS9 after Cor 1.2), correctly cited; I did not re-prove the 512-cell enumeration but
re-checked the equivalence on every edge at every prime p ≡ 1 (4) ≤ 10⁶ (3 028 437 edges, 0 failures).
At primes p > 3 every non-diagonal edge has unit endpoints (vertex p has no non-loop neighbour, 2p > p+2): confirmed
in code (assertion gcd(uv,p) = 1 on all edges, all odd primes ≤ 10⁶). The composite-n restriction is stated correctly.
Path-product telescoping: trivial.

## 3. Theorem 3.1 — SOUND (MINOR D1)

Re-derived every step: p+1 = 2r, p+2 = 3s, p+3 = 4w. Vertex 1: divisors of 2r other than 1 ⇒ {2, r, 2r}. Vertex 2:
2v | p+2+v ⟺ v | 3s and v odd ⇒ {1,3,s,3s}. Vertex 3: v | 4w, v ≡ 2 (3); w ≡ 1 (3) ⇒ {2, 2w}. Leaf r: v | 3r−1,
v ≡ 1 (r): r+1 | 4, 2r+1 | 5 impossible for r ≥ 13. Leaf s: v | 4s−2, v ≡ 2 (s): s+2 | 10, 2s+2 | 6, 3s+2 | 14
impossible for s ≥ 9. Leaf 2w (=: V): v | 3V−3, v ≡ 3 (V): V+3 | 12, 2V+3 | 15 impossible for V ≥ 14. Leaves 2r = p+1 and
3s = p+2: their smaller neighbours are −p mod (p+1) = 1 and −p mod (p+2) = 2; their only possible larger neighbour
(p+2, resp. none) fails since (p+1)(p+2) ∤ 3p+3. Residues: p ≡ 1 (24) ⇒ (2/p) = (3/p) = 1, and r ≡ 1/2, s ≡ 2/3,
2w ≡ 3/2, 2r ≡ 1, 3s ≡ 2. Admissibility: all four forms equal 1 at k = 0 ⇒ no fixed prime divisor; Dickson ⇒ infinitely
many k. CONDITIONAL label correct.

*Numerics.* Exhaustive BFS of the component of 1 for every k ≤ 20 000 with all four forms prime (20 fixtures): edge
set equals the stated seven edges exactly, all eight vertices residues. The first eight are 12721, 16921, 19441, 24481,
49681, 61561, 104161, 229321 — exactly the list in the document.

## 4. Theorem 3.2 — SOUND

p+i = (i+1)L_i ✓; i(i+1) | M gives L_i ≡ 1 (mod i) and p ≡ 1 (mod i). A neighbour of i divides p+i and is ≡ −1 (mod i);
divisors of (i+1)L_i (L_i prime, L_i > i+1) are d, dL_i ≡ d (mod i) with d | i+1, and the only d ≤ i+1 with d ≡ −1
(mod i) is i−1, which divides i+1 only for i ≤ 3. This covers smaller and larger neighbours simultaneously; the
self-review's "smaller-neighbour gap" was indeed not a gap. With k′ = Mk/24, L₁ = 12k′+1, L₂ = 8k′+1, L₃ = 6k′+1, so the
component of {1,2,3} is Thm 3.1's. Admissibility (all forms = 1 at k = 0) ✓, CONDITIONAL ✓. (Remark: "k large enough
that L_i > H+1" is automatic for k ≥ 1, since L_i ≥ 1 + M/(H+1) and H(H+1) | M.)

*Numerics.* H = 6, M = 840: first three fixtures p = 5 516 281, 18 164 161, 51 755 761; roots 4–6 isolated, component
of {1,2,3} has 8 vertices / 7 edges, all residues. (H = 8, M = 2520: no 9-fold prime tuple with k ≤ 3·10⁶ — only
rarity, not a defect.)
