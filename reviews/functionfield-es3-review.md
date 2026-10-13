# R173 — hostile review of FUNCTIONFIELD_ES3.md (O173)

Reviewer: R173 (side agent). Reviewed: FUNCTIONFIELD_ES3.md, reviews/agent-reports/AGENT_REPORT_O173.md, scripts/ff3_*,
data/ff3_* (merged from side-agent/ff-sterile-point). Background: FUNCTIONFIELD_ES.md §6.2, FUNCTIONFIELD_ES2.md §0,
R166 review, DISCOVERIES (J)4/(J)12.
From-scratch scripts: `scripts/review_ff3_*.py` (own F_p[T] arithmetic, pure Python, 1 core). Logs `data/review_ff3_*`.

(in progress)

## Re-derivations (paper)

* Lemma 1.1: re-derived. A·L | P + E gives (i); T ∤ E, P ≡ 1, T^k X ≡ 1 (mod E), a0, b0 units mod E; the four type
  residues; mixed types give E | 1 + T^k a0 b0 = 1 + T^{N+1+γ}L'g' and lc(s) = 1. Converse (types 0 and 2,
  a0 = T^γ g', b0 = T^j L') checked: gcd/lcm are right because g' | L', γ ≤ j; s·T^k b0 ≡ D (mod E).
* Lemma 1.2: re-derived. deg D ≤ (N+1+γ) + 2l ≤ 2(N+1+l) − 2 since γ ≤ N − 1 (k ≥ 2); the class of E' is
  {−u^{−1} mod T^{N+1}, −1 mod L'} because D ≡ 1 modulo both; ρ + 1 = L'h, h const ⇒ T | L' (uses ρ(0) = −1, i.e.
  u(0) = 1). g' has degree ≤ l < deg ρ, so it equals the least residue.
* Lemma 2.1 (a)–(c): re-derived (see defect list for the N + γ ≥ 3 step).
* Lemma 2.2: re-derived line by line, including the Z' = −Z sub-case (c = −1, v_T(Z) = γ − 1, gcd(g', Z1) = 1,
  Z1 ∈ {1, T − 1}).
* Lemma 2.3: re-derived (i)–(iv). Degree of (****): deg(T^{N+1}ZZ') = N+1+z+z' > max(z, z'+1) since N ≥ 1.
  z + z' = γ + l + deg g' − N ≤ 2l − 1 (γ ≤ N − 1); N ≤ max(z, z'+1) + |z − z'|; hence N ≤ 4l − 1 − 3 min(z, z').
* Lemma 3.1: re-derived (needs γ + 1 ≤ j − 1, i.e. γ ≤ j − 2; D unchanged; cylinder mod T^{k+j−1} ⊇ mod T^{k+j}).

## Computations (from scratch)

* `scripts/review_ff3_poly.py`: own F_p[T] arithmetic (lists; trial-division factorisation; irreducible counts over
  F_3 for degree 1..8 = 3, 3, 8, 18, 48, 116, 312, 810, correct).
* `scripts/review_ff3_search.py`: independent Case B search at a slice point. Different algorithm from
  `ff3_caseB.c`. ρ_N = L'·h_N − 1 is read off one power series h = (1 − w)/L' per (L', branch). Every monic divisor
  g' of L' (found by factoring L') and every γ ≤ j is then tested directly via T^{N+1+γ}L'g' ≡ −1 (mod ρ). There is
  no modular inverse and no solving for g'. Mode `brute`: factor D completely for every (L', j, γ, g' | L') and test
  every monic divisor E. This mode needs neither Lemma 1.2 nor a CRT step.
* `scripts/review_ff3_cross.py` part 1 (`data/review_ff3_cross1_log.txt`): 19 *planted* slice points (each lies
  in the cylinder of a random Case B family; p = 3, 5, 7; k = 2, 3). Fast and brute family sets agree exactly
  (110 families). This confirms Lemma 1.2 empirically: there are no families outside {E = ρ} ∪ {E' = ρ'}.
* Part 2 (`data/review_ff3_cross2_log.txt`): 84 families at 50 random slice points (p = 3, k = 2, 3; p = 5). There are
  0 violations of Lemma 2.1(c) (l ≤ N + γ − 2 ≤ 2N − k − 1, N + γ ≥ 3). There are also 0 violations of Lemma 3.1:
  each family with γ ≤ j − 2 has its (j − 1, γ + 1) partner in the set.
* Part 3 (`data/review_ff3_cross3_log.txt`): x*_c for p = 3 (l ≤ 5), p = 5, 7 (l ≤ 3, every c), and k = 2, 3. The j-range
  was extended 6–8 beyond the Lemma 2.3 window so that a family violating the window would show up. **0 families
  in every case**, so this test of Lemma 2.3 is vacuous (no family exists at x*_c in these ranges for q = 5, 7
  either). Lemma 2.3 therefore rests on the proof, which R173 re-derived line by line (above).
* **Independent x*_c search (complete j-range, R173 algorithm):** `review_ff3_search.py 3 2 0 11 -1 fast 1 c` for
  c = 1, 2 and `review_ff3_search.py 3 3 0 10 -1 fast 1 c` (k = 3). Result: **0 Case B families** for deg L' ≤ 11 (k = 2)
  and deg L' ≤ 10 (k = 3), with every j ≤ 4l − k, every γ ≤ j, both branches, and every monic g' | L'. Logs:
  `data/review_ff3_xstar_k{2,3}_c{1,2}.txt` (k = 2, l = 11 layer ≈ 35 min per c). The cumulative counts of monic ρ
  agree exactly with the author's logs in every layer: c = 1: 7, 44, …, 2 185 650, 7 267 442; c = 2: …, 2 173 580,
  7 241 970; k = 3: 2 126 602 and 2 114 532 at l = 10. Two codes with different inner loops and arithmetic therefore
  enumerate the same candidate set and find nothing. The deg L' = 12, 13 layers (k = 2) and l = 11 (k = 3) were
  **not** re-run (≈ 2 h and ≈ 7 h per c in Python). They rest on `ff3_caseB.c` alone, which R173 read line by line
  (see "Completeness logic").
* **Census of all Case B families on the slice** (`scripts/review_ff3_census.py`): this enumerates the Lemma 2.1
  parametrisation (s, v, m', w, C) over all u. Every (L', g', E) with s = 4..14 was found
  (`data/review_ff3_census_s12.txt`, `_s15.txt`): 2, 4, 10, 8, 8, 4, 24, 12, 14, 36, 104 triples for s = 4..14.
  These counts agree exactly with R175's independent O175 enumeration (main: `data/review_sl_caseB_K15.txt`,
  K = s − 2). The covered slice masses for levels ≤ 2..6 are 0.2222, 0.2222, 0.2716, 0.3045, 0.3100 (normalised to
  u(0) = 1), i.e. ×3/2 = 1/3, 1/3, 11/27, 37/81, 113/243 on the sub-slice c ≠ 0, which is R175's sequence. Every
  family satisfies Lemma 2.1(c) (asserted in the script).

## Verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (Case B at slice points, converse) | SOUND |
| Lemma 1.2 (E = ρ or E' = ρ'; deg ρ > l; g' forced) | SOUND (MINOR D2); empirically confirmed by brute force (no divisor outside ρ/ρ') |
| Lemma 2.1 (m'wC = T^s + v, w + C = g'v; l ≤ N + γ − 2 ≤ 2N − k − 1; j = 0 impossible for k = 2) | SOUND-AFTER-REPAIRS (D1: the step "N + γ ≥ 3" is not proved as written; true) |
| Lemma 2.2 (Z, Z' ≠ 0, L' ∣ Z + Z', Z + Z' ≠ 0) | SOUND |
| Lemma 2.3 ((N+1)/4 ≤ l ≤ 2N − k − 1 at x*_c) and the completeness of the j-range | SOUND |
| Lemma 3.1 (only j − γ ∈ {0, 1} matters) | SOUND |
| EVIDENCE: no family with deg L' ≤ 13 / level ≤ 8 at x*_c (c = 1, 2); k = 3: deg L' ≤ 11 / level ≤ 7 | SOUND. Independently reproduced for deg L' ≤ 11 (k = 2) and ≤ 10 (k = 3) by a different code, with identical candidate counts. Label upgrade possible (D9) |
| Elementary count ≤ q^{(N+1+γ)/2+o(N)} | SOUND as a sketch (MINOR D8) |
| "O166/R166 divergent heuristic was wrong" | SOUND: the divergent sum ran over ℓ > 2N − k − 1, where Lemma 2.1 proves there are no families |
| "Corrected heuristic: Σ_N poly(N)·q^{−N}, convergent" | GAP (D3, MAJOR for the narrative): poly(N) is unsupported. Convergence survives only as EVIDENCE/Assessment from exact counts |
| Control (7/40, 1/40) and its wording | SOUND-AFTER-REPAIRS (D5, D6) |
| Measure-route criterion U(m) > T(m) ⇒ O(3, T²) ≠ ∅ | SOUND (union bound; MINOR D10) |
| Dictionary (Kloosterman / short-interval divisor problem) | acceptable as a labelled analogy (MINOR D4, D7) |

**No FATAL defects.** The lemmas are correct, and the completeness logic behind the search claims holds. The one
substantive problem is the heuristic family count (D3).

## Completeness logic (checked)

Every linear family valid at x*_c is of Case A (excluded by the ES2/R166 theorem, q odd, k ≥ 2, at u = 1 + cT
exactly) or Case B (Lemma 1.1; mixed types). A Case B family is a tuple (L', j, γ, g', E). By Lemma 2.3, j ≤ 4l − k.
By Lemma 1.2, E = ρ_{L',j} or D/E = ρ'_{L',j}, and g' is the unique residue of degree < deg ρ. `ff3_caseB.c`
loops over all monic L' with L'(0) ≠ 0 and deg L' ≤ LMAX, all 0 ≤ j ≤ 4l − k (JMAX = −1), both branches, and all
0 ≤ γ ≤ j. It accepts exactly the t_γ that are monic, of degree ≤ l, and divide L'. Checked in the code:
`pinvmod` cannot fail (gcd(ρ, T·L') = 1 since ρ ≡ −1 mod L' and ρ(0) = −1); the WARN branch deg ρ ≤ l is
unreachable (Lemma 1.2); the arrays are large enough (NMAX = k + 4·LMAX ≤ 54, products of degree ≤ 2·NMAX < 256);
v·T^{−1} mod ρ is implemented correctly. So every possible family is captured by the enumerated
(L', j, γ, branch). "No family with deg L' ≤ L0 at x*_c" plus Lemma 2.1 (l ≤ 2N − k − 1) gives "no family of level
N ≤ (L0 + k + 1)/2". That is N ≤ 8 for (k, L0) = (2, 13) and N ≤ 7 for (3, 11), as stated.
