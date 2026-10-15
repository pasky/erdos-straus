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

---------------------------------------------------------------------------------------------------------------------------
# Round 2 (R231): STERILE_LOWER §6–7 (Thm 6.3, r₀ = 2^{21.4375})

**Repairs applied (round 2, author quiet ≥ 3 h):** r2-m1 in `scripts/zl_r1.py` (exact endpoints, exit on mismatch, contiguity
check; all nine r1 logs reproduced byte-identically; a corrupted-endpoint file and a file with a missing cell now exit 1) + MANIFEST
note; r2-m3 and r2-m5 as wording in STERILE_LOWER §6.3 and §7, marked '(R231 repair …)'. Not applied: r2-m2 (sweep header — needs
a zl_sweep change and re-runs), r2-m4 (zl_boxa comment — would change a certified binary's sha for a comment).

Merged `side-agent/sterile-lower` at cf13d705 (checkpoint 2). New scripts (from scratch): `scripts/review_zl_pern.c` (per-n
level-1 counter), `scripts/review_zl_r1.py` (certificate re-check); `review_zl_pbox.py` gained in-cell validation for N = r^K.

## 6.1 Splitting the level-1 count
Re-derived. (a) Q-data with ad ≤ Y: at most 2 per (a, d) — M17C Lemma 2.1(iv): f | t = 4a²d + 1, f ≡ −F (mod s), s = 4ad,
s² > t, gcd(t, s) = 1; a divisor f ≤ √t < s is the least residue of its class, a divisor f > √t is fixed by its cofactor t/f < s in
the class t·(−F)^{−1}: ≤ 1 of each kind. Correct (and c, hence the datum, is fixed by f). (b) Q-data with a ≥ A: zl_boxa skips a
box only if its upper a-enclosure a₁ = UP((λP + F₁)/(4CD)) < ACUT, so all a ≥ A data stay in non-skipped boxes; row aggregation
min(agg, inner) still bounds them (agg bounds the whole row). Correct. (c) Range facts: a ≤ b ⇒ f ≤ F + 2/e ≤ F + 2 (from
f − 1/e ≤ 2acd, shown in round 1) and 4acd = f + F ⇒ acd ≤ (F + 1)/2 — the sweep's d ≤ (2X₁+2)/(4a), f ≤ X₁ + 1, and the
'none' criterion (no Q-datum has a > (F+1)/2) follow. The AD and engine pieces may double-count data with ad ≤ Y and a ≥ A: harmless.
**Verdict 6.1: SOUND.**

## 6.2 zl_sweep.c (code reading)
P: triples (a, c, d) with 4a² − 2a < X₁, 4a²d − 2a < X₁; progression N ≡ −4a²d (mod f), start ⌈4a²d − 2a/c⌉ = 4a²d − ⌊2a/c⌋
(a ≤ b ⇔ cN ≥ 4a²cd − 2a), odd N only (f odd ⇒ step 2f); c-loop stops once f > 4a²d and f − 4a²d ≥ X₁ (least positive member).
Correct. Q: rows a < A, d ∈ [⌊Y/a⌋ + 1, ⌊(2X₁+2)/(4a)⌋] (⇔ ad > Y), sieve root d ≡ −(4a²)^{−1} (mod p) for odd p ∤ a up to
√m_max (prime table size checked, exit 3), leftover cofactor prime (two leftover factors > √m_max would exceed m); short rows by
trial division < 2^10 + deterministic MR (12 bases ≤ 37, valid < 3.3·10²⁴) + Brent ρ; at most one prime factor ≥ 2^32 (m < 2^64);
divisors f ≤ X₁ + 1, c from ⌈(X₀ + f)/(4ad)⌉, condition na + c ≥ af (b ≥ a). Overflow paths (MF, dv, sieve root) exit non-zero;
16-bit counters saturate at 65535 and zl_r1 fails on mp or mq = 65535. Correct as read.

## 7. r = 17: conic Γ_{c,d,z} (Assessment)
Re-derived: with X = qa − pb = zW, cX² = cz²rN and 4rcdz²ab − rz²(a + b) = rz²c(4abd − e) = rz²cN, so Γ holds; conversely
N := X²/(rz²), e := (a+b)/c give N = 4abd − e. `scripts/review_zl_conic.py`: Γ and N = X²/(rz²) hold on 1132 (datum, p, q)
instances over r ∈ {3, 5, 7, 17}, r | X always. "Γ forces r | X and r | N" tacitly needs r ∤ c (in-cell); then
v_r(X²) = 1 + 2v_r(z) + v_r(4abcd − a − b) forces v_r(4abcd − a − b) odd, so r | N also when r | z — fine, say "r ∤ c".
Vieta partners a′ = bV/(cq²) = 748098/81 = 83122/9, b′ = aU/(cp²) = 3/121 confirmed (a·a′ = (cp²b² + rz²b)/(cq²)). The S-unit
remarks (ii) are Assessment and labelled so. **Verdict §7: SOUND as Assessment** (nit: hypothesis r ∤ c).

## 6.2 (cont.) Exact counts: sweep vs independent per-n enumeration
`scripts/review_zl_pern.c` (from scratch; P by loops over (a, b, d); Q by loops over (c, d) and the progression f ≡ −n (mod 4cd),
1 ≤ f ≤ n + 2, a = (f + n)/(4cd), b = (an + c)/f, checking b ≥ a, c | a + b and 4abcd = n(a + b) + c in 128-bit) — it never lists
divisors of 4a²d + 1 and does not use Lemma 3.1. It splits Q into a < A ∧ ad > Y (= the sweep's JQ), ad ≤ Y, a ≥ A ∧ ad > Y, and
records the largest number of Q-data sharing one (a, d). Sanity: n ∈ [300, 600): 3301 + 4909 data (= round 1).
I recompiled `zl_sweep.c` (gcc -O2 -march=native) and re-ran the certified octaves with ZL_BIN dumps, with the MANIFEST parameters:
* octave 21 (ZL_SHORT=8, A = 2097154, Y = 300): cell file **identical** to `data/zl/sweep_21.txt`;
* octave 24 as a split run (ZL_SHORT=8, A = 330000, with P) + (ZL_NOP, ZL_ALO = 330000, A = 524288, sieve rows), merged by
  `zl_merge.py`: **identical** to `data/zl/sweep_24.txt`.
Samples (`scripts/review_zl_sample.py` reads the uint16 dumps itself, sums split runs itself, and takes the argmax-(JP + JQ) prime of
every cell — the number the certificate uses — plus seeded random primes):
| octave | primes compared | of which cell argmax | JP, JQ mismatches | max #Q-data per (a, d) | max Q(ad ≤ Y) vs 2#{ad ≤ Y} | max Q(a ≥ A) |
|---|---|---|---|---|---|---|
| [2^21, 2^22) incl. all cells j = 686..703 of [2^{21.4375}, 2^22) (100 random in it) | 218 | 18 | **0** | 2 | 1402 ≤ 3534 | 0 |
| [2^22, 2^23) (A = 4194306, Y = 1048; file identical to sweep_22) | 112 | 32 | **0** | 2 | 3334 ≤ 14900 | 0 |
| [2^24, 2^25) (split run) | 132 | 32 | **0** | 2 | 8260 ≤ 71276 | 117 (≪ engine row ≈ 10⁶) |
| [2^27, 2^28) (A = 32768, Y = 134217, max-S octave; file identical to sweep_27) | 62 | 32 | **0** | 2 | 38743 ≤ 3210940 | 3079 (≪ engine 2.6·10⁷) |
So the per-cell maxima entering the certificate are exact counts, independently confirmed at the argmax primes; and the AD bound
"≤ 2 per (a, d)" is attained but never exceeded in 524 primes. The reproduced files cover every binary version listed in MANIFEST
(octave 27: original source; 24: sweep2 + sweep3 features; 21, 22: sweep4), so the uncommitted older sources are immaterial.

## 6.3 Certificate (zl_r1.py) and the deeper terms
Code reading of `zl_r1.py`: level-1 term 2(maxPQ_j + 2·Dsum(Y) + eng_j)/2^{j/32} — weight 2r^{−1} for both P (K = 1) and Q (k = 1),
maximal at r = 2^b, maxima over all primes of the cell: correct; Dsum is the exact divisor-sum count; engine rows ×(1 + 10⁻⁹), header
ACUT checked, missing row ⇒ exit; saturated counters ⇒ FAIL; 'none' requires A > (X₁ + 1)//2 + 1 — correct since no Q-datum of F
has a > (F + 1)/2 and every row a < A is swept (rows with a > (X₁+1)/2 are empty anyway). Deeper terms (K, k ≥ 3, tails) are the
zl_r0 loop started at 3, with the extra tables P_q32_k3 (se_box) and, for octave 21, P_q32_k3_l2 / P_q32_k5_l2 (zl_box).
From-scratch re-check `scripts/review_zl_r1.py` (exact integer cell endpoints ⌈2^{j/32}⌉ computed by integer powers — mismatch is an
error, contiguity asserted; brute-force Dsum; deeper terms in 40-digit arithmetic with min over covering cells and a rigorous geometric
remainder; tails from my round-1 dumps):
| octave | cells | max S (mine) | author |
|---|---|---|---|
| 21 (l2 K = 3/5 tables), j ≥ 686 | 686..703 | 0.48324804 | 0.483248 |
| 22 / 23 | 704..735 / 736..767 | 0.41731622 / 0.2536038 | 0.417317 / 0.253604 |
| 24 (my own split-run merge) | 768..799 | 0.28907003 | 0.289070 |
| 25 / 26 / 27 | 800..831 / 832..863 / 864..895 | 0.31304676 / 0.37862811 / 0.47317016 | 0.313047 / 0.378628 / 0.473171 |
| 28 / 29 | 896..927 / 928..964 | 0.3583574 / 0.32656367 | 0.358358 / 0.326564 |
Cells 686..964 are present and contiguous, joining Thm 2.1 at j = 965 (r₀ = 2^{965/32} = 2^{30.15625}); 2·Dsum(Y) matches the MANIFEST
Y in every octave (3534, 14900, 32722, 71276, 154190, 1512438, 3210940, 6794016, 14332240). Cells 672..685 of octave 21 fail
(0.4997 at 681 passes but is not contiguous), as the theorem says.
Binding term now: P at K = 3 (0.44 of S = 0.483 at j = 686; margin 0.017 ≈ 4 % of that term). Tables: rows 2058, 2059 (P_q32_k3_l2),
2058 (P_q32_k3), 3430 (P_q32_k5_l2), 864 (Qa_32768, zl_boxa ACUT=32768) regenerated **bit-identical**. Independent engines:
* **K = 3**, my P engine (now with a τ₃ route: e ≡ −N (mod 4) in the e-window × explicit τ₃ envelope C₃(η)n^η, and validated on in-cell
  data of N = 101³, 127³, 131³, 23⁵, 10⁶+3, 3·10⁶+17 — 0 window/box/row violations) for all 54 N-cells 2058..2111 (K = 3 of r-cells
  686..703): my bound / author's ℓ² table = 0.49 … 0.57. With *only* my K = 3 table, SE's P_q4/P_q1 for K ≥ 5 and the exact sweep:
  **max S = 0.2883 on cells 686..703** (`MYK3=…`, log `data/zl_review/myr1_21_myk3.txt`).
* **Engine part a ≥ A** (octave 27, the max-S octave): my Q engine with the same box-skipping rule (skip boxes whose exact a-upper bound
  < ACUT) gives 0.974 … 0.982 × the `Qa_32768_q32` rows in all 32 cells; with my rows instead of the author's, max S = 0.4629.
So Thm 6.3's binding terms are independently re-certified with margin.
**Verdict Thm 6.3: SOUND.**

## Round-2 suggestion (not a defect): the existing sweep already reaches 2^21 with a tighter K = 3 bound
I ran my P engine (ℓ², exact windows incl. e ∈ [(N₀ + 4A²D)/f_max, (N₁ + 4(2A−1)²(2D−1))/f_min], τ₃ route) on all 96 N-cells 2016..2111
(K = 3 for r-cells 672..703): 0.48–0.57 × the zl_box table. With it, the author's own exact sweep of [2^21, 2^22) and SE's tables for
K ≥ 5: **all 32 cells 672..703 pass, max S = 0.3653 (j = 672)** (`data/zl_review/myr1_21_myk3_all.txt`). So porting the exact e-window
(SE Lemma 1.2's e ≤ N/(ACD) is ≈ 4× loose) into zl_box would extend Thm 6.3 to r ≥ 2^{21} with no new sweep, and with S ≈ 0.37 at 2^21
the next octave [2^20, 2^21) (a ~1-minute sweep) is a realistic target. As it stands this is R231 EVIDENCE from a reviewer engine
(validated by exhaustive enumeration, exact (Cop₂) checks), not part of the author's certificate.

## Round-2 defects (no FATAL, no MAJOR)
* **r2-m1 (MINOR) zl_r1.py fails open on cell endpoints:** a sweep cell whose (lo, hi) does not match the float-computed
  ⌈2^{j/32}⌉ (or +1) is silently skipped (`continue`), and there is no contiguity check — a skipped cell would leave a gap that the
  text ("the cells are contiguous") does not detect. No gap exists (my exact re-check asserts endpoints and contiguity for 686..964).
  *Repair:* skip only the documented partial cells (lo ≠ rlo at a range start, hi = X₁ ≠ rhi at the end), exit 1 otherwise, and assert
  that the certified j form one interval ending at 964.
* **r2-m2 (MINOR) provenance of A, Y:** sweep files carry no header; zl_r1 takes A, Y from the command line, and both the AD term and the
  'none' criterion depend on them. Verified externally (identical re-runs with MANIFEST parameters; ADY values) — but *repair:* zl_sweep
  should print "# X0 X1 A Y q env…" and zl_r1/zl_merge check it.
* **r2-m3 (MINOR, wording) remainder of the K-series below 2^32:** the 10⁻²⁰ charge after the first term < 10⁻³⁰ was justified in SE
  (R223) by "ratio < 1/2 for b ≥ 32"; at b ≈ 21.4 the per-step ratio is ≈ 2^{2·0.48·b − b}·((K+2)/K)^p ≈ 0.6–0.65, still < 1, so the
  remainder is ≤ 2·10⁻³⁰ and the charge stays valid. Say so in §6.3 (my combiner uses an explicit geometric bound and agrees).
* **r2-m4 (nit):** zl_boxa.c still says "Lemma 2.1"; P_q32_k3_l2 / P_q32_k5_l2 headers read "# se_box" (both already noted in MANIFEST).
* **r2-m5 (nit) §7:** "Γ forces r | X and r | N" needs r ∤ c (in-cell); with it, v_r(X²) = 1 + 2v_r(z) + v_r(4abcd − a − b) shows r | N
  even when r | z.
* **6.2 text:** "16-bit, saturation ⇒ failure" — true in zl_r1; zl_merge sums in Python ints and rejects saturated inputs: fine.

Round-1 repairs (author commit 403e272b) checked: m1–m9 applied as suggested, computation unchanged (zl_box.c only comments/header).

## Round-2 summary
| claim | verdict |
|---|---|
| 6.1 splitting (sweep + 2·#{ad ≤ Y} + engine for a ≥ A; 'none' when all rows swept) | SOUND |
| 6.2 zl_sweep exact counts (P AP sweep, Q sieve/ρ), split-run merge | SOUND — 524 primes in octaves 21, 22, 24, 27 match an independent per-n counter exactly; four octave files reproduced bit-identically |
| 6.3 combiner zl_r1.py | SOUND-AFTER-REPAIRS (r2-m1, r2-m2: fail-open/provenance hardening; no actual error) |
| Thm 6.3, (S) for r ≥ 2^{21.4375} | **SOUND** — reproduced cell by cell; binding K = 3 and engine terms re-certified with own engines (max S 0.288 / 0.463) |
| §7 conic Γ / descent (Assessment) | SOUND (nit r2-m5) |
