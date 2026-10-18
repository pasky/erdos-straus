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

## 5. Lemma 4.1 and Proposition 4.2 — SOUND (MINOR D2)

Lemma 4.1: v_{i−1} = r_{v_i} ≡ −n (mod v_i) and, from v_i v_{i+1} | n+v_i+v_{i+1}, v_{i+1} ≡ −n (mod v_i); hence
v_i | v_{i+1} − v_{i−1} > 0. Since each vertex has ≤ 1 smaller neighbour, every tree path is "descending then
ascending" (no interior local maximum), so the depth (distance to the component minimum, along the parent chain) is
O(log n). Census: max depth 7, first at 7867 (a prime ≡ 3 mod 4; the document correctly says "over selected inputs").

Prop 4.2: moduli 8 and the distinct odd primes v₂, v₃, … are pairwise coprime, residues −v_{i−1} mod v_i are units;
CRT + Dirichlet give p. Edge {v_{i−1}, v_i}: v_i | p+v_{i−1} by prescription; v_{i−1} | p+v_i because p ≡ −v_{i−2} and
v_i ≡ v_{i−2} (mod v_{i−1}); coprimality gives the product. Edges {1,2}, {2,v₂} ✓. Reciprocity chain:
(v_i/p) = (p/v_i) = (−v_{i−1}/v_i) = (v_{i−1}/v_i) = (v_i/v_{i−1}) = (v_{i−2}/v_{i−1}) = (v_{i−1}/p) — all steps valid
because all odd v_i ≡ 1 (8) and p ≡ 1 (8); base (v₂/p) = (−2/v₂) = 1. ✓ Dirichlet is a theorem, so PROVED is right.

*Numerics.* Reviewer construction: path (1, 2, 17, 257, 4129, 33289, 1335689) (one step longer than the self-review's),
p = 110378207809425376169 prime; all six word divisibilities and all seven residue symbols verified.

## 6. Theorem 5.1 — SOUND

9240 = 2³·3·5·7·11; 2521 = 105·24+1 = 360·7+1 = 504·5+1 = 229·11+2. So p ≡ 1 (24), 1 (5), 1 (7), 2 (11): 2,3,5,7 residues,
(11/p) = (p/11) = (2/11) = −1 ⇒ ℓ(p) = 11. 12q = p+11 ✓; q ≡ 211 ≡ 2 (11). A neighbour of 11 divides 12q and is
≡ −p ≡ 9 (11); divisor residues {1,2,3,4,6,1}·{1,2} = {1,2,3,4,6,8} ∌ 9 ✓. Admissibility: at 2,5,7,11 both forms are
nonzero constants; at 3 the first is ≡ 1, the second 1+2a vanishes only at a ≡ 1; at ℓ ≥ 13 at most two classes
excluded ✓. CONDITIONAL on Dickson (two forms) ✓.

*Numerics.* 226 values a ≤ 3000 with p, q both prime (first 2521, 30241, 104161, 196561, …): ℓ(p) = 11 and N(11) = ∅
in every case. Observation (not a defect): 104161 lies in both the Thm 3.1 and Thm 5.1 families, and 196561 — the census
maximiser of the least mixed-component root (17) — is a Thm 5.1 member; a natural combined CONDITIONAL family (24k+1,
12k+1, 8k+1, 6k+1, (p+11)/12 prime with p ≡ 2 mod 11, 1 mod 35) would kill roots 1,2,3 and the least non-residue
simultaneously, which is consistent with these records.

## 7. §6 census — SOUND (every figure reproduced)

Reviewer code, independent algorithms (see header):

| Figure | Document | R285 |
|---|---|---|
| odd primes ≤ 10⁶ / p ≡ 1 (4) | 78 497 / 39 175 | 78 497 / 39 175 |
| edges at p ≡ 1 (4) / bichromatic | 3 028 437 / 1 964 805 | 3 028 437 / 1 964 805 |
| primes with no bichromatic edge | 0 | 0 |
| root-1 failures, first 16 | 285; 409, 1201, …, 27241 | 285; identical list |
| ℓ(p) has smaller neighbour | 38 097 | 38 097 |
| ℓ(p)-component failures, first 6 | 769; 1201, 2521, 3361, 5569, 7561, 9769 | 769; identical |
| max least mixed root | 17 at 196561 | 17 at 196561 |
| max depth | 7 at 7867 | 7 at 7867 |
| odd n ≤ 2000 edges / odd-square edges | 24 389 / 17 372 | 24 389 / 17 372 |
| five-slice hits at odd squares; 8-test hits at 131, 241 | 0; 0 | 0; 0 (36 edges) |

Overlap: 110 primes fail both the root-1 and the ℓ(p)-component test (see D5).
I did not re-check the 21 135 exact unit-fraction reconstructions (imported DEDEKIND Thm 4.5 formulas; not needed for
any claim here).
