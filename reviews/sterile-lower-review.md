# Hostile review R231 of STERILE_LOWER.md (O228, checkpoint 1) — round 1

Reviewer: R231 (independent hostile review #1). Branch `side-agent/review-sterile-lower-2`, merged `side-agent/sterile-lower`.
Scripts (from scratch): `scripts/review_zl_*.py`; data `data/zl_review/`. Status: round 1 complete. Repairs applied: none (author active).

## Summary verdicts
See the table at the end. No FATAL, no MAJOR; 8 MINOR + 1 nit.

## Claim-by-claim

### Lemma 3.1 (joint parametrisation of level-1 data)
Re-derived (i): with f = 4acd − 1 and f | N + 4a²d, Nc + a ≡ −4a²cd + a = −a·f ≡ 0 (mod f); b := (Nc+a)/f,
e := (N+4a²d)/f; 4abd = (4acdN + 4a²d)/f = ((f+1)N + 4a²d)/f = N + e;
ce = (cN + 4a²cd)/f = (cN + a(f+1))/f = b + a. a ≤ b ⇔ Nc + a ≥ af = 4a²cd − a ⇔ cN ≥ 4a²cd − 2a. Converse by ef = N + 4a²d
(SE Lemma 1.1(i)). (ii): e·f = 4a²d + 1, na + c ≡ 4a²cd + c = c(4a²d+1) ≡ 0 (mod f); 4abcd = (n+f)b = nb + na + c. Converse:
4acd > n is forced (4abcd = n(a+b) + c > nb gives 4acd > n), and ef = 4a²d + 1 with e = (a+b)/c. All correct.
Brute force (`scripts/review_zl_joint.py`, own per-n loops over (a, b, d) for P and (a, c, d) for Q, compared as SETS of
tuples, not counts): X = 100: 685 + 1010 data, 0 mismatches; X = 300: 3301 + 4909, 0 mismatches (same totals as the author).
The divisibility f | na + c was asserted for every (a, d, f, c) in the joint loop: never failed.
Minor: "a ≤ b ⇔ b ≥ a" in (ii) is vacuous as written (presumably meant "⇔ c(4a²d+1) ≥ af·… " or simply "require b ≥ a").
**Verdict: SOUND** (cost-model Consequence is Assessment, correctly labelled).

### Computation 4.1 (level-1 survivors)
Re-derived the level-1 box set from M17 directly: level-1 boxes in non-residue cells are P-boxes from N = r (K = 1; K = 2
has no data by M17 Lemma 1.3), residues −(4acd − 1), −(4bcd − 1) with r ∤ cd, and Q/Q⁻¹-boxes from F = r (k = 1),
residues −4a²d, −4b²d with r ∤ e; U-boxes of level 1 lie in P-boxes of level ≤ 1 (M17 Lemma 5.2, case (α, β) = (1, 0)),
so they add nothing. From-scratch enumerator `scripts/review_zl_level1.py` (own loops: P over (a, b, d), Q over (a, c, d)
with the bound c(4ad − 1) ≤ 2r derived from b ≥ a). Result for all 302 primes 3 ≤ r < 2000: **identical** (r, #NR, #survivors)
to `data/zl/level1_survivors.txt`; r ≤ 13 no survivors; r = 17 survivors {5, 7}; r = 19 {2, 3, 10, 13}; r = 23 {5, 14};
least surviving fraction for 17 ≤ r < 2000 is 2/11 at r = 23. With all r-conditions dropped (LOOSE=1) the survivor sets are
unchanged (the dropped data have residue 1 or 0, as checked by hand: r | c forces −a/b ≡ 1). Extended to **all 2261 primes
3 ≤ r < 20000**: identical to the author's file line by line (e.g. r = 19993: 9898 of 9996 survive); no r ≥ 17 without survivors.
Note on label: "CERTIFIED by exhaustive exact enumeration" is fine; the claimed *dichotomy* is only about level 1 (stated).

### Lemma 4.3 (U–V factorisation)
Re-derived: with ce = a + b, 4abd = N + e, N = r^{2L−1}, (qa − pb)² = z²r^{2L}:
e·[c(p²b + q²a) + rz²] − ab[(p+q)² + 4rdz²] = (a+b)(p²b + q²a) − ab(p+q)² + erz² − (N+e)rz² = (qa − pb)² − Nrz² = 0.
So Gab = c(p²b + q²a) + rz² holds over ℚ with G := ((p+q)² + 4rdz²)/e, and G ∈ ℤ follows *without* M17D: eG ∈ ℤ, abG ∈ ℤ and
gcd(e, ab) = 1 (a prime dividing e and ab divides N = r^K, excluded by r ∤ ab). Ub, Va, UV identities: correct
(UV·ab = c²p²q²ab + rz²(cq²a + cp²b + rz²) = ab(c²p²q² + rz²G)). Size claim: correct, using c ≤ 2b/e, |qa − pb| ≤ (|p| + q)b,
r/W² = 1/N; it tacitly needs q ≥ 1 (u = −p/q in lowest terms with q > 0) — state it.
Brute force (`scripts/review_zl_lemma43.py`): 7650 random (datum, p, q) instances over 10 (r, L) pairs + 54 small-(p, q)
instances satisfying the size hypothesis: all identities hold, G always integral, U, V > 0, e ≤ 4q²a never violated.
**Defect (MINOR):** the worked check says "u = 11/9 ∈ C₇"; but 11/9 ≡ 5 (mod 17) and the box −f = −63 ≡ 226 (mod 289) ≡ 5
(mod 17), so u ∈ **C₅**. The numbers (z = 3, G = 124, U = 3, V = 9591, UV = 28773) are right.
**Verdict: SOUND** (after the C₅ typo and explicit q ≥ 1).

### Lemma 1.1 (ℓ²-Minkowski form of (Cop))
Re-derived. The lattice of coefficient vectors (g_l X^l)_{l<w} has the triangular basis of SE Lemma 1.3, determinant
Δ = n₁^{m(m+1)/2} X^{w(w−1)/2}. Minkowski for a compact symmetric convex body (closed ball, vol ≥ 2^w Δ suffices) gives g ≠ 0
with ‖v‖₂ ≤ ρ, ρ^w = 2^w Γ(w/2+1) Δ / π^{w/2}. For |y| ≤ X: |g(y)| ≤ Σ|g_l|X^l = ‖v‖₁ ≤ √w‖v‖₂ ≤ μ_w Δ^{1/w}, with
μ_w = 2√w Γ(w/2+1)^{1/w}/√π; (Cop₂) makes this < D₀^m ≤ E^m. Rest (E^m | g(y) ⇒ g(y) = 0, ≤ w − 1 roots, injectivity) as in SE.
Constants (`scripts/review_zl_cop2.py`, 60-digit mpmath): μ₁ = 1, μ₂ = 1.5958, μ₁₀ = 5.7593, μ₂₄ = 12.713 (author: 1.60, 5.76, 12.7);
μ_w < w for 2 ≤ w < 200; μ_w/w → √(2/(eπ)) ≈ 0.484. Random test of the *lemma itself* (not of the engine): 2509 random
(smooth n ≤ 10¹³, s, σ, window) instances, (Cop₂) held in 232 632 (w, m) cases (w ≤ 24), **0 violations** of "≤ w − 1
divisors", 789 tight. Cor 1.4 (window splitting with common D₀) transfers verbatim.
Engine: `diff se_box.c zl_box.c` is exactly the header, the table LMK[w] = ½ln w + ln 2 + lgammal(w/2+1)/w − ½ln π padded up by
a relative 10⁻¹² and capped at ln w, and `w*logl(w)` → `w*LMK[w]` in lhs0. This is (Cop₂) in logs. The only new numerical
dependency is glibc `lgammal` (a few ulp) — absorbed by the 10⁻¹² pad and by se_box's 10⁻¹² (Cop) margin.
SHA-256 of se_box.c, zl_box.c, zl_tail.py, zl_r0.py, se_r0.py match MANIFEST.txt; se_box.c / se_tail.py / se_r0.py identical to main.
**MINOR (numbering):** zl_box.c header, its inline comment and zl_r0.py call this "Lemma 2.1"; the document calls it Lemma 1.1.
**Verdict: SOUND.**

### Lemma 1.2 (value-selected tail routes)
Logic re-derived: SE §3.3 proves, for *each* box of the normalised mesh and *each* route, a term list Σ c N^e (ln N)^p valid for
all N ≥ N₀ (the Coppersmith conditions are checked at L₀ with slope ≤ 0, so they depend on N₀ but not on which route is later
chosen). Any per-box choice that is fixed (independent of N) gives a valid bound for D(N), N ≥ N₀. Monotonicity: d/dL[(e − h)L + p ln L]
= (e − h) + p/L ≤ 0 for L ≥ L₀ iff p ≤ (h − e)L₀ — exactly the admissibility test; for the r-weights,
d/d(ln r)[(Ke − (K+1)/2) ln r + p ln(K ln r)] ≤ Ke − (K+1)/2 + K(1/2 − e) = −1/2 < 0 once K ln r ≥ L₀. Correct.
Independent numerics (`scripts/review_zl_tail.py`): imports SE's *reviewed* `se_tail.py` (unchanged from main), intercepts its
per-box route choice, re-selects with my own admissibility test and 50-digit mpmath values, and recomputes G:
| N₀ | G (new selection) | max e | G (SE selection) |
|---|---|---|---|
| 2^600 (P, M=32, SE_W=40) | 7.2603701 | 0.495954 | 873.569 |
| 2^800 (P) | **0.013618405** | 0.479688 | **1.0108** |
| 2^1000 (P) | 4.096·10⁻⁵ | 0.479688 | 1.256·10⁻³ |
| 2^100 (Q, M=16) | 9.0188·10⁻⁶ | 0.750000 | 9.167·10⁻⁶ |
All selected terms admissible; no box lacks an admissible route. The author's 7.26 / 1.36·10⁻² / 4.1·10⁻⁵ / 0.4797 are reproduced.
**MINOR (attribution, §0 (I4), §1, report "873 → 0.0136"):** the comparison mixes two changes. At the same N₀ = 2^800, SE's own
selection already gives G = 1.01; moving N₀ from 2^600 to 2^800 (made possible by the new table `P_q1_hi`, rows 600..799) accounts
for ×860, value-selection for ×74. Both are legitimate, but the text should say so. Also, at N₀ = 2^600 the new selection raises the
max exponent from 0.4797 to 0.4960 (harmless, still < 1/2; worth a word since SE quotes 0.4797 as "the" tail exponent).
Consequence (see Thm 2.1 below): with tails from 2^800 the P tail term at r ≈ 2^30 is ≲ 10⁻⁴ even with G = 1.01, so Thm 2.1 does
not actually *need* Lemma 1.2's new selection — only SE's §3.3 at N₀ = 2^800 plus the extra table.
**Verdict: SOUND** (MINOR attribution fix).

### Theorem 2.1 — combiner and certificate (independent re-certification)
From-scratch combiner `scripts/review_zl_combine.py` (does not import zl_r0/se_r0; reads only the certified tables and tail
term lists): exact Fraction cell endpoints; all reals in 40-digit mpmath inflated by a relative 10⁻³⁰; at each point of an
N-range it takes the *smallest* covering table cell (any covering cell is valid), tails at the top of the N-range (after
rounding exponents up to a 10⁻⁵ grid, capping e < 0 at 0, and re-checking e < h, p ≤ (h − e)L₀), weights at r = 2^b; and,
instead of the author's "charge 10⁻²⁰ after the first term < 10⁻³⁰", a rigorous geometric remainder (per-term ratio
2^{2b⁺e − b}((K+2)/K)^p resp. 2^{2b⁺e − 2b}(…)^p, required < 1/2). Tails: P from `review_zl_tail.py` (SE's reviewed term
lists, my selection) at N₀ = 2^800; Q at 2^100. Results:
| variant | B0 | max S (mine) | author | first failing cell (mine) |
|---|---|---|---|---|
| ℓ² tables + se tables (ZL_L2) | 30.15625 | **0.49782559** (b = 30.15625; Q₁ 0.45626, P₁ 0.03599, P₃ 0.00548) | 0.497826 | b = 30.125: 0.50415 |
| se_box tables only | 30.34375 | **0.49424867** (b = 30.34375) | 0.494249 | b = 30.3125: 0.50075 |
Both certificates are reproduced to all printed digits, 0 failures over b up to 800 (r ≥ 2^800 by monotonicity).
Table provenance: recompiled `se_box.c`/`zl_box.c` (gcc 14, x86-64 long double) reproduce the rows j = 965 (Q, P; ℓ²), 965 (Q, se),
971 (P, Q, se) **bit-for-bit**; full regeneration of `P_q32`, `Q_q32` (se_box, j = 768..1087) and `P_q32_l2`, `Q_q32_l2`
(zl_box, j = 928..1023) with the MANIFEST parameters is **bit-identical** to the committed tables (all 832 rows).
ℓ² gain measured at j = 965: Q −6.6 %, P −6.1 % (author: −5 % to −7 %).
Combiner checks (zl_r0.py, by reading): the r-cell rule is sound — within [2^b, 2^{b+1/32}) no monotonicity in r is used:
the weight 2r^{−k} resp. 2r^{−(K+1)/2} is maximal at r = 2^b and the table maximum is over all N-cells meeting
[2^{Kb}, 2^{K(b+1/32)}); straddling ranges take max(table part, tail at top); fails closed on gaps (exit 1), on
non-admissible tails, and on non-finite terms. Rounding: tables ×(1 + 10⁻⁹), S ×(1 + 10⁻⁶) — ample (margin 2·10⁻³).
**MINOR (provenance):** the `_l2` tables carry the header "# se_box …" (zl_box.c did not change its printf); only MANIFEST
distinguishes them. Suggest zl_box print "zl_box" in the header.
`P_q1_hi` rows j = 600, 700, 799 regenerated with se_box: bit-identical.

### Independent re-certification of the level-1 table cells (own engines)
The tables are produced by se_box (reviewed by R222/R223) and zl_box (se_box + Lemma 1.1). To make the dominant terms independent
of that code I wrote two box engines from scratch, `scripts/review_zl_qbox.py` (D_Q(F)) and `scripts/review_zl_pbox.py` (D_P(N)),
for primes in [2^{j/32}, 2^{(j+1)/32}) (k = K = 1, the only cells taken from the new 1/32 tables). Own derivations:
* Q: f = 4acd − F ∈ [1, F + 2] (b ≥ a gives f ≤ F + 2/e), ef = 4a²d + 1, fb = aF + c, 4abd = eF + 1, f(4bcd − F) = F² + 4c²d,
  c ≡ −aF, 4a²d ≡ −1 (mod f); boxes (c, d, f) dyadic with exact integer a-, b-, e-windows; routes H, AC (f | aF + c, class −F mod 4ac),
  CD (f | F² + 4c²d, class −F mod 4cd), Ea (pairs (e, a), b or d in a unit class mod e), Ed (pairs (e, d), 2^{ω(e)} root classes),
  fac, fca; row aggregation by τ(F² + 4c²d). (No AD, fa, τ₃, fda — fewer routes only weakens my bound.)
* P: f = 4acd − 1, ef = N + 4a²d, bf = Nc + a, ff' = 4c²dN + 1, gcd(e, abd) = 1, b ≤ N/(4ad − 2), 4a²d ≤ 2N; exact windows
  e ∈ [(N₀ + 4A²D)/f_max, (N₁ + 4(2A−1)²(2D−1))/f_min]; routes H, A, C, D, E, F, G, I, J; row aggregation by τ(N + 4a²d) (≤ τ-envelope at 3N).
* Class-divisor counts: min(trivial, explicit τ envelope C₂(η)n^η (η = 0.10, …, 0.50), Lemma 1.3/Cor 1.4) where (Cop) resp. (Cop₂) is
  **verified in exact rational arithmetic** for the chosen (w, m, J) (μ_w^{2w} = 4^w w^w Γ(w/2+1)² π^{−w} bounded with a rational π_lo < π;
  w ≤ 24). Pair counts/harmonic sums in 40-digit mpmath inflated by 10⁻²⁵.
* Validation (`validate` mode): for primes 17, 1009, 10007, 65537, 100003, 1000003, 3000017 all P- and Q-data are enumerated exactly; every
  datum lies inside the computed windows of its box, every box bound and every row bound dominates the true count: 0 violations.
Results: P (K = 1), j = 965..970 with (Cop₂), 971..1087 with (Cop): my bound / author's table = 0.44 … 0.56 in every one of the 123 cells
(my e-window is ≈ 4× tighter than SE Lemma 1.2's N/(ACD)). Q (k = 1): see the next paragraph.
Q (k = 1): my bound / author's table = **0.936 … 0.951** in all 123 cells (j = 965..970 against the ℓ² table, 971..1087 against
se_box); e.g. j = 965: 2.5706·10⁸ (ℓ²) vs 2.7297·10⁸, and 2.7502·10⁸ (cube) vs 2.9240·10⁸.
**Fully independent certificate:** `MINE_ONLY=1 review_zl_combine.py 965/32 …` replaces *all* of the author's new 1/32-octave tables by my
engines' tables (`data/zl_review/myP_q32.txt`, `myQ_q32.txt`) and keeps only SE's reviewed tables (P_q4, P_q1, Q_q4) plus the regenerated
P_q1_hi: **max S = 0.45311 at b = 30.15625, 0 failures up to 2^800** (Q₁ 0.4297, P₁ 0.0179, P₃ 0.0055). So Thm 2.1 does not hinge on
the author's table code; it has a margin of ≈ 0.047 under my engines. Logs in `data/zl_review/*.log`.
Robustness: with the *SE-selected* tail at N₀ = 2^800 (G = 1.01 instead of 0.0136) the author's tables still give max S = 0.49788 (0 failures),
i.e. Lemma 1.2's re-selection is not needed for Thm 2.1.
**Verdict on Thm 2.1: SOUND** — both the ℓ² variant (r ≥ 2^{30.15625}) and the se_box-only variant (r ≥ 2^{30.34375}), labels
"PROVED, computer-assisted" appropriate (same standard as SE Thm 3.4; floating point in the C tables assumes glibc x87 libm, as in SE).

### Assessments 3.0, 4.2 and the r = 17 outcome
Labels are right (Assessment; "undecided"). Numbers checked against `data/se/P_q4.txt`: G = 931 (2^{38.75}), 894 (2^{39}), 538 (2^{61}), 98 (2^{91}),
7·10⁻¹¹ (2^{600}, P_q1_hi). Off-by-10⁴ at K = 15: bound 538·17^{7.5} ≈ 9·10¹¹ vs allowed 2.5·17^{6} ≈ 6·10⁷ — correct. Max τ(n ≤ 2^64) = 184320 and
the envelope 1.874·10⁵ (my own C₂(η) code) — correct.

## Defects
No FATAL, no MAJOR.
* **m1 (MINOR) §4 Lemma 4.3, Check line:** "u = 11/9 ∈ C₇" — 11/9 ≡ 5 (mod 17) and the box −63 ≡ 226 (mod 289) lies in C₅. *Repair:* "∈ C₅".
* **m2 (MINOR) Lemma 4.3 statement:** the size claim needs q ≥ 1 (u = −p/q, q > 0); say so. Optionally note G ∈ ℤ follows directly from
  eG ∈ ℤ, abG = c(p²b + q²a) + rz² ∈ ℤ and gcd(e, ab) = 1, without M17D Remark 2.4.
* **m3 (MINOR) Lemma 3.1(ii):** "a ≤ b ⇔ b ≥ a" is vacuous. *Repair:* "a ≤ b ⇔ f ≤ n + c/a" (from fb = na + c), or just "keep those with b ≥ a".
* **m4 (MINOR) numbering:** `zl_box.c` (header and inline comment) and `zl_r0.py` call the ℓ²-lemma "Lemma 2.1"; the document has Lemma 1.1.
* **m5 (MINOR) attribution of the tail gain** (§0 (I4), §1 Lemma 1.2, report "873 → 0.0136"): at the same N₀ = 2^800 SE's own route choice gives
  G = 1.01; the move N₀: 2^600 → 2^800 (new table P_q1_hi) accounts for ×860, value-selection for ×74, and Thm 2.1 holds even without the
  re-selection (max S 0.49788). Also: at N₀ = 2^600 the value-selection raises the max exponent 0.4797 → 0.4960. *Repair:* one sentence each.
* **m6 (MINOR) §0 (I3) and §3.0, report:** "Q₁ bound ≈ 10·F^{0.6}·ln F" — on the certified tables it is ≈ **50**·r^{0.6}·ln r
  (48.8, 50.0, 50.3, 51.1, 50.5 at b = 24, 26, 28, 30, 32; ratio to r^{0.65} ≈ 360). The interpretation "(# (c, d) pairs) × (Coppersmith
  constant ≈ 4)" should be re-examined accordingly (it was presumably derived from the 10× smaller constant).
* **m7 (MINOR) provenance:** `_l2` tables have header "# se_box …" (zl_box's printf unchanged); only MANIFEST tells them apart. *Repair:*
  print "zl_box" in zl_box.c, or annotate MANIFEST explicitly (it does name zl_box — so this is cosmetic).
* **m8 (nit) Assessment 4.2:** "G < 1 only from ≈ 2^{159} on" — in P_q4 the last cell with G ≥ 1 is 2^{156.75}; "≈ 2^{157}".
* **m9 (MINOR) report SHARP bullet:** "a joint sweep would move r₀ … to ≈ 2^{22.5}" sits next to PROVED items; tag it "(Assessment)" as §3 does.

## Suggestion (not a defect)
Tighter exact windows lower the engine bounds: my P engine uses e ∈ [(N₀ + 4A²D)/f_max, (N₁ + 4(2A−1)²(2D−1))/f_min] (ratio ≈ 8 instead of
SE Lemma 1.2's 32) and integer windows [P, 2P − 1]; it gives D_P bounds 0.44–0.56× and D_Q bounds 0.94–0.95× the tables, i.e. S(2^{30.15625})
≤ 0.453 instead of 0.498. Worth porting into the engine if uniform bounds are pushed further.

## Scope note
This round covers checkpoint 1 (author commit cd1939f0: §§0–5). The author has since pushed new material (commits 5b52f3bd, 89552e24,
ced7e8b9: "§6 sweep certificate, r ≥ 2^27"), which is **not** reviewed here. Since the author is active, no repairs were applied by R231.

## Summary verdicts
| claim | verdict |
|---|---|
| Lemma 1.1 (ℓ²-Minkowski (Cop₂)) | SOUND |
| Lemma 1.2 (value-selected tails; G = 0.0136 at 2^800) | SOUND (m5) |
| Thm 2.1, ℓ² variant, r ≥ 2^{30.15625} | **SOUND** — reproduced (0.497826) and independently re-certified with own engines (0.4531) |
| Thm 2.1, se_box-only variant, r ≥ 2^{30.34375} | **SOUND** — reproduced (0.494249) |
| 1/32-octave r-cells / combiner zl_r0.py (fail-closed, rounding) | SOUND |
| Lemma 3.1 (joint parametrisation) | SOUND (m3) |
| Comp 4.1 (r ≤ 13 covered; 17 ≤ r < 20000 survivors; r = 17: {5, 7}) | SOUND — recomputed for all r < 20000 |
| Lemma 4.3 (UV = c²p²q² + Grz², e ≤ 4q²a) | SOUND (m1, m2) |
| Assessments 3.0 / 4.2, r = 17 "undecided", labels | SOUND (m6, m8, m9) |
