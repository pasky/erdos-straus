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

## Defects

**D1 (MINOR) — Lemma 2.1, "N + γ ≥ 3".** Location: Lemma 2.1, last sentence of the statement, and the report
("N + γ ≤ 2 impossible"). Part (c) only gives l ≤ s − 3, i.e. N + γ ≥ 2 (from l ≥ 0). N + γ = 2 (s = 3) needs a
separate argument. Here it is. (c) forces l = 0, min(a, b) = 1, a + b = 3, so L' = g' = m' = 1 and v = λT². With
a = 1 we get w = T and C = T(T + β), and w + C = λT² gives λ = 1, β = −1. Then wC = T³ − T² ≠ T³ + T² (q odd), a
contradiction. Repair: add these two lines to the proof. Only "j = 0 impossible for k = 2" (s = 2) follows directly
from (c). The k = 2 case j = 1, γ = 0 (s = 3) needs the extra argument.

**D2 (MINOR) — Lemma 1.2, "deg ρ, deg ρ' > deg L'".** This is false if u ≡ 1 (mod T^{N+1}): then ρ = −1, or
ρ' = −1 for the other branch. The proof mentions this in a parenthesis, but the statement does not. It is harmless:
that branch then has no monic candidate, it never happens at x*_c, and the C code skips non-monic ρ. Repair:
"… > deg L' whenever ρ (resp. ρ') is monic of positive degree; otherwise that branch is empty."

**D3 (MAJOR for the narrative; labels) — the "corrected heuristic" Σ_N poly(N)·q^{−N}.** Locations: §2 Remark after
Lemma 2.1 ("expected number ≈ Σ_N poly(N)·q^{−N}"); §3 Control paragraph ("≈ poly(N)·3^{−N}"); §3 Assessment
("(Heuristically the count is poly(N).)"); report SHARP 1 and the Results bullet "(B) looks unlikely … poly(N)·3^{−N}".
(a) What is right. FF2's argument summed poly(N + ℓ)·q^{−N} over all ℓ = deg L' at fixed N. Lemma 2.1 proves that
every term with ℓ > 2N − k − 1 is zero, so the *divergence argument* is invalid. Flipping the (J)12 sentence "generic
lifts are heuristically covered (divergent expected count)" is justified to that extent.
(b) What is not supported. The replacement count "poly(N) families per level" is asserted with no derivation. The
only proved bound is the elementary one, ≈ q^{N+1−k/2+o(N)} cylinders per level (§3), and it gives **no** decay of
the expected count. Exact data, R173 census (Lemma 2.1 enumeration over all u, s ≤ 15, `data/review_ff3_census_s15.txt`),
reproducing R175/O175 counts:
  #(L', g', E) at s = 4..15: 2, 4, 10, 8, 8, 4, 24, 12, 14, 36, 104, 48 (R175 continues K = 14, 15: 38, 36);
  #fam(N) (all γ) for N = 2..7: 2, 16, 30, 54, 70, 202; #fam(N)·3^{−N}: 0.22, 0.59, 0.37, 0.22, 0.096, 0.092;
  #cyl(N)·3^{−N}: 0.22, 0.15, 0.12, 0.12, 0.049, 0.034.
A least-squares fit of log₃ #sol over K = s − 2 = 2..15 gives slope 0.21, i.e. ≈ 3^{0.21K} ≈ 3^{0.42N}, which is R175's
"3^{0.4N}". **But the same 14 noisy points fit a power law K^{1.6} equally well.** #fam(N) = 16 → 202 for N = 3 → 7
also matches N³. So the data neither confirm poly(N) nor establish exponential growth. R175's word "contradicted"
is itself an extrapolation.
(c) Answer to the orchestrator's question: does convergence survive with 3^{0.4N} families of mass ≈ 3^{−N}? **Yes,
as EVIDENCE.** The relevant sum is Σ_N #fam(N)·q^{−N}, more precisely the union-relevant (Lemma 3.1) cylinders,
Σ_s #(L', g', E)(s)·q^{−⌈(s−k)/2⌉−1}. It converges iff the growth exponent per level is < 1, with a summable excess
(#fam(N) = o(q^N/N^{1+ε}) suffices). With 3^{0.4N} the terms decay like 3^{−0.6N}; with K^{1.6} they decay like
3^{−N/2}. The observed per-level expected counts do decay (0.59 → 0.09 over N = 3..7), but **much more slowly than
the claimed poly(N)·3^{−N}**. The covered sub-slice mass rises 1/3, 11/27, 37/81, 113/243, 349/729 (N ≤ 3..7, R173 =
R175), with increments 0.074, 0.049, 0.008, 0.014, and is 0.4906 at K ≤ 19 (R175). This is consistent with a limit
well below 1. None of this is proved, and the a priori bound allows growth q^{N+o(N)}, at which the sum diverges.
Repair: replace each occurrence of "≈ poly(N)·q^{−N}" by "Σ_N #fam(N)·q^{−N}, which converges iff #fam(N) grows
slower than q^N (summably). Exact counts to s ≤ 17 (R173/R175) give per-level expected counts decaying roughly like
3^{−0.4N}…3^{−0.6N}, i.e. #fam(N) ≈ 3^{0.4–0.6N} or a power of N (the data cannot tell). Convergence is EVIDENCE,
not a consequence of Lemma 2.1." Delete "(Heuristically the count is poly(N).)". (J)12 should record: "FF2's divergence
argument is invalid (Lemma 2.1); convergence of the expected count is data-driven (Assessment)".

**D4 (MINOR) — "mass ≈ q^{−k/2}·q^{o(N)} per level — no decay".** Location: §3 after Lemma 3.1; report SHARP 2
("i.e. mass ≈ q^{−k/2} per level, no decay"). This is the elementary *upper bound*, not the mass. The census shows
the actual union-relevant mass per level decaying (D3). Repair: "the elementary bound only gives mass ≤ q^{−k/2+o(N)}
per level, which does not decay."

**D5 (MINOR) — Control wording.** "this settles R166 D6 in the negative direction" overclaims for a 40-point
experiment with a truncated j-range. Note also the direction of the truncation bias: control points are searched
only with j ≤ 4l − 2, which is complete only at x*. Their counts are lower bounds, which makes them look *more* like
the empty x*. The bias is probably small, because a family with large N at fixed l has cylinder mass q^{−N−1}, but it
should be stated. Repair: "is consistent with R166 D6: x*_c is not distinguishable from points of its T⁶-cylinder in
this range". The rest of the paragraph's wording ("consistent with … typical", "does not prove there is none") is
honest.

**D6 (MINOR) — unlogged numbers.** No data file backs (I2) (200 random slice points, "hits at large deg L' all have
large N and γ close to j"), the §1 sanity "51/300", or the control table (7/40, 0.35; 1/40, 0.025). Repair: commit
the outputs (`data/ff3_ctl_m4.txt`, `_m6.txt`, `data/ff3_I2.txt`, …).

**D7 (MINOR) — "Under T ↦ 1/T this becomes a factorisation T^s + v = m'wC"** (report SHARP 2; Sparks "Reversal
T ↦ 1/T"). The parametrisation of Lemma 2.1 is direct algebra (EE' = D divided by L'g'); no reversal is involved.
T^s + v with deg v ≤ s/2 is already a short-interval polynomial. Repair the wording.

**D8 (MINOR) — elementary count.** The q^{o(N)} needs the divisor bound d₃(f) ≤ q^{O(deg f/ log deg f)} in F_q[T].
This is standard (analogue of Wigert's bound) but should be cited or stated, together with the factor ≤ s from
summing over t. The number of v with deg v = t and T² | v is (q − 1)q^{t−2} ≤ q^{t−1} (fine). The cylinder count
uses min(deg E, deg E') = s − t exactly. R173 checked this (deg(w + C) = max(a, b) also when a = b, since
lc = 2 ≠ 0, q odd). The report's label "PROVED, sketched" should read "PROVED (sketch; standard divisor bound)".

**D9 (MINOR, label) — search claims.** As written ("EVIDENCE, computer search with independent cross-check"), the
"independent cross-check" (`ff3_check.py`) covers only deg L' ≤ 5, j ≤ 9 at x*. State that range. After R173 the
finite statements "no Case B family with deg L' ≤ 11 at x*_c, c = 1, 2 (k = 2), hence no linear family of level
N ≤ 7", and "deg L' ≤ 10 for k = 3 (levels N ≤ 7)", are reproduced by two independent programs with identical
candidate counts. They may be labelled CERTIFIED (computer, two independent codes, given Lemmas 1.1–2.3 and the
ES2 Case A theorem). The deg L' = 12, 13 layers (level N = 8 for k = 2) and deg L' = 11 for k = 3 remain single-code
(EVIDENCE, or CERTIFIED (single code) if the campaign's convention allows).

**D10 (MINOR) — measure-route Assessment.** T(m) should sum over N > m (families of level > m). The Haar
normalisation should be fixed once: a cylinder mod T^{N+1} has mass q^{−N} relative to {u(0) = 1}, or q^{−(N+1)} in
F_q[[T]]. U(m) and T(m) must use the same normalisation. The criterion itself (union bound: uncovered mass
≥ U(m) − T(m) > 0 ⇒ some slice point is uncovered ⇒ O(3, T²) ≠ ∅) is correct. It needs Case A families on the
slice in T(m) and in U(m), as the text says.
