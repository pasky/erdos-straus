# R273 — hostile review of O261 (B2_ACROSS_FIELDS.md, BRAINSTORM/z31_*.md, sources/lit2026g/)

Reviewer: R273 side agent (branch side-agent/review-b2-fields), merged side-agent/b2-across-fields at review start.
Status: complete (round 1).
Repairs applied (author quiet at checkpoint): (R273 repair) edits in B2_ACROSS_FIELDS.md (§4.1 Zhang dependence + versions; table rows 1, 7; §5 pattern table M1a/M1b/M5, Graham), BRAINSTORM/z31_quadratic_forms.md (Bhargava–Hanke venue), sources/lit2026g/{bhargava_hanke,ghosh_sarnak}.txt, AGENT_REPORT_O261.md (Lemma 7.1 wording, size, "first pointwise", pattern). Defects 2, 5, 10 (partly), 15 (symbol fixes) left to the author.

## Claim (1) — headline: Zaremba claimed proved pointwise (Shkredov 2603.14116 Cor 1; X. Zhang 2605.02518 Thm 1.2)

**Verdict: SOUND** (as a literature report; label "claimed, 2026 preprints, proofs not checked" is the right grade).

What I checked independently (fresh downloads of export.arxiv.org abs pages and arXiv PDFs, pdftotext, 2026-10-17/18):
* **arXiv:2603.14116** exists: I. D. Shkredov, "On some results of Korobov and Larcher and Zaremba's conjecture";
  v1 14 Mar 2026, **v2 24 Jun 2026 (latest version; no v3)**. v2 comment: "41 pages. 1. Some minor typos have been corrected,
  and clarifications have been made. 2. … the proof of technical Lemma 32 has been broken down into three auxiliary lemmas,
  simplified, and clarified. 3. In the appendix, we provide a crude upper bound for the absolute constant M in the case of a
  prime denominator". Not withdrawn. Verbatim (v2 p. 2, l. 65–69 of pdftotext):
  > Corollary 1. There is an absolute constant M ⩾ 2 such that for any prime (or square–free) number p there exists a,
  > (a, p) = 1 such that a/p = [0; c1, …, cs], cj ⩽ M, j = 1, …, s.
  Abstract: "We prove, in particular, the well-known Zaremba conjecture … for any prime denominator." Thm 8 (all M ≥ M₀,
  all q ∈ Z: ≥ q^{2w_M−1−o(1)} numerators with cj ≤ 100M) matches the excerpt file.
* **arXiv:2605.02518** exists: Xin Zhang, "Expansion in SL₂(ℤ/qℤ) and Zaremba's conjecture"; v1 4 May 2026, **v2 8 May 2026
  (latest; comment "Typos in v1 corrected")**. Verbatim: "In this paper we prove / Theorem 1.2. Zaremba's conjecture holds."
  with Conjecture 1.1 = "∃ M ∀ q ∈ ℕ ∃ a < q, gcd(a, q) = 1, all partial quotients ≤ M". Remark 1.3: M effectively computable
  but large.
* **Disputes / reception:** web search found no withdrawal, erratum or published objection. Positive signals: Shkredov v2
  itself cites Zhang ([64]: "now possess a proof of Zaremba's conjecture in full generality"); A. Kontorovich (X, 5 May 2026)
  publicly announced Zhang's proof "based on a breakthrough of Ilya Shkredov"; Stanford seminar (3 Jun 2026); Google Scholar
  "cited by 3" for Shkredov. Still unrefereed as far as I could find → "claimed" is correct.
* **Mechanism (from the papers, Zhang §4 outline + Shkredov §§1,3–4):** Diophantine reformulation (MMS26 Lemma 2): bounded
  partial quotients ⟺ x‖ax/q‖·q ≫ q/M for all 1 ≤ x < q. Small x (< t) are controlled by a ∈ Z_M(t), a Cantor/Ahlfors–David set
  containing K = Λ₁ ∔ [1, N] with |Λ₁| ≍ t^{2w_M}, t²N ≍ q, t ≈ q^{1/2−τ}; large x by a⁻¹ (mod q) ∈ Z_M(t). So one counts
  a ∈ K ∩ K⁻¹, i.e. solutions of (a + 2j)(b + 2j) ≡ 1 (mod q) — an equation g_j·a = −b for g_j ∈ SL₂(ℤ/q) with a generating set of
  size ≈ q^{2τ} (Zhang Rem 1.4: this is why Bourgain–Varjú does not suffice and a Helfgott-type product theorem for general q
  is needed). The remaining middle range x ∈ [t, q/(4Mt)] is handled by Shkredov's "critical denominators" Diophantine idea.
  Expected count |K|²/q ≍ q^{2w_M−1} = q^{1−O(1/M)}.
  The author's summary ("growth in SL₂(ℤ/qℤ) on two Cantor half-sets of size q^{w_M}, count q^{2w_M−1}") is accurate.

Defects:
1. **MINOR** (B2_ACROSS_FIELDS §4.1 / table row 1): Zhang's theorem is *not independent* of Shkredov — Zhang supplies the
   SL₂(ℤ/qℤ) growth input (his Thm 3.6) and explicitly runs "the framework provided by the proof of Theorem 8 in [Shk26]".
   A gap in Shkredov's Thm 8 framework would sink both. Repair: add "(Zhang = Shkredov's Thm 8 framework + new expansion for
   general q; not an independent proof)".
2. **MINOR** (§4.1): the mechanism summary omits the middle range x ∈ [t, q/(4Mt)] (Shkredov's new "critical denominators"
   idea) — this, not the growth input alone, is what makes M absolute rather than O(log q/log log q) (MMS26). Relevant for the
   "M1+M2" attribution in §5: the pointwise theorem also needs an Ahlfors–David *structure* input, which the §5 spark already
   hints at. Repair: one sentence.
3. **MINOR** (§6 ledger): record arXiv version status (Shkredov v2 24 Jun 2026, Zhang v2 8 May 2026, latest as of
   2026-10-18; not withdrawn; unrefereed).

## Claim (3) — PROVED dictionaries: Lemma 7.1 (z31_logic_divisibility) and Lemma 4.1 (z31_duke_equidistribution)

**Verdict: Lemma 4.1 SOUND. Lemma 7.1 SOUND (as stated), but MINOR wording overreach in B2_ACROSS_FIELDS table row 7.**

From-scratch script: `scripts/review_r273_dictionaries.py` (no reuse of scripts/o261/). Run:
`PYTHONPATH=scripts uv run python scripts/review_r273_dictionaries.py 200000` (≈ 1 min).

*Lemma 7.1.* Re-derived. (i) For w | p + 4d the largest variable must occur only on the right ⇒ d ≻ w; for 4d | w + 1 ⇒ w ≻ d;
contradiction, so Φ_p is not in increasing form under any ordering. ✓ (ii) Local witnesses: d = 1, w = 3 (unit in ℤ_ℓ, ℓ ≠ 3) and
d = 1, w = 7 (unit in ℤ₃); 4 | 4, 4 | 8. ✓ Trivially correct (any divisibility f | g with f a free variable is ℓ-adically solvable
by making f a unit). Global: my search, with **no** a-priori bound on d (all d ≤ p, all divisors of p + 4d), finds E2 failing
among p ≡ 1 (4), p ≤ 2·10⁵ at **exactly {193, 2521, 66529}** ✓, and independent brute force gives ES(193) = (50, 1380, 1331700),
ES(2521) = (636, 69748, 131876031) ✓ (so E2-failure ≠ ES-failure, as the doc says). The author's d ≤ (p + 3)/8 is right
(p + 4d odd ⇒ proper divisor w ≤ (p + 4d)/3, and w ≥ 4d − 1). The 10¹¹ census is (J)90's, not re-checked.

*Lemma 4.1.* Re-derived by hand: ρ = (2k)⁻¹ mod g gives ρ² ≡ 1/(4k²) ≡ −p (mod g) because 4k²p ≡ −1; det γ = −gs + 2kρ = 1;
γz = i√p·g/(1 − 2ki√p) = (−2kp + i√p)/m' ✓; z is the Heegner point of the primitive form (g, 2ρ, (ρ² + p)/g), disc −4p ✓.
Ideal side: ℤ[√−p] is maximal (−p ≡ 3 mod 4); α = 1 + 2k√−p is primitive, so for each ℓ^e ‖ g | Nα only one prime above ℓ
divides α and the ideal divisor of norm g exists and is unique: (g, √−p + ρ). ✓ Numerically: brute-force enumeration of *all*
ideals I = c(aℤ + (b + √−p)ℤ) of ℤ[√−p] containing α (p < 1200, k ≤ 6) — every ideal divisor has c = 1, one ideal per divisor
of Nα, and the norms ≡ −1 (mod 4k) coincide exactly with the shot moduli g (522 shots, 0 mismatches). I also re-derived the
explicit ES triple of a shot, y = ph, x = (ph + (h/k)²)/g, z = p(h + pk²)/g (h = (g + 1)/4), and checked 4/p = 1/x + 1/y + 1/z
exactly on all 522 shots — so "shot" is a genuine ES solution family. (J)36 re-check: p = 13, 37, 97 have no shot with
k ≤ p + 2 (finite k-range evidence; the full claim is (J)36's).

Defects:
4. **MINOR** (B2_ACROSS_FIELDS table row 7 and §5 "its LGP fails"): Lipshitz's LGP is a *theorem* about increasing-form
   systems; it cannot "fail". What Lemma 7.1 shows is that the naive local-global statement for Φ_p itself (no reduction to
   increasing form) is false, and that this is unsurprising: local solvability of Φ_p is vacuous (any divisibility with a free
   variable divisor is ℓ-adically solvable by a unit). Repair: "Φ_p is not in increasing form, and the naive LGP for Φ_p is
   false (local solvability is vacuous; global fails at 193, 2521, 66529)". Also say explicitly that Lipshitz's procedure
   *does* produce an equi-satisfiable increasing-form Ψ (by case splits), so "not increasing form" is not an obstruction to
   decidability — memo 7 says this, the main doc table does not.
5. **MINOR** (z31_duke Lemma 4.1 statement): the converse direction should state that g ≡ −1 (mod 4k) automatically gives
   g ≡ 3 (mod 4), gcd(g, p) = 1, g ≠ 1, g ≠ Nα (since Nα ≡ 1 mod 4k) — all true, but these are the E4 side conditions and the
   ⟸ direction silently needs them. One line.

## Claim (2) — citation accuracy of other rows

**Verdict: SOUND-AFTER-REPAIRS** (no hallucinated paper or theorem found; one publication-venue error, a few garbled /
truncated excerpts). Checked against fresh arXiv PDFs (pdftotext) unless stated.

| item | doc claim | my check | status |
|---|---|---|---|
| Bourgain–Kontorovich arXiv:1107.3776, Ann. Math. 180 (2014), Thm 1.8 | δ_A > δ₀ ⇒ a.e. admissible d ∈ D_A, multiplicity ≫ N^{2δ−1001/1000}; p. 8 quote on individual errors | verbatim match (Thm 1.8, (1.9), (1.37) paragraph). Zaremba-specific statement is Thm 1.2 (alphabet {1,…,A}, "almost every") | ✓ (see defect 7) |
| W. Chen arXiv:2011.12940 (Ann. Math. 199 (2024)) Thms 1.2.3, 1.2.5, 1.2.6 | BGS a.a./giant component; orbit sizes ≡ 0 mod p (p ≥ 3); E_bgs finite, explicitly bounded; strong approx. for p ∉ E_bgs | verbatim match, pp. 6–7 | ✓ |
| Colliot-Thélène–Wittenberg arXiv:0911.3539 (Amer. J. Math. 134 (2012)) | no BM obstruction to x³+y³+z³ = a for a ≢ 4, 5 (mod 9) | abstract matches | ✓ |
| Bright–Loughran arXiv:1908.02526 Thms 1.6, 1.8, 1.9 | Br U_n/Br ℚ ≅ ℤ/2; (U_n(ℝ)₊ × ∏U_n(ℤ_p))^Br ≠ ∅; no density of integral points in the Br-set | local PDF: Thm 1.6 ✓ (transcendental quaternion algebra), Thm 1.8 (1.4) ✓ and (1.5) (the Br set is a *proper* subset), Thm 1.9 ✓ ("does not have dense image"); "log K3" p. 3 ✓ | ✓ |
| Harpaz arXiv:1511.04876 (Ann. Inst. Fourier 67 (2017)) Thm 1.0.1 | S-integral points on conic log K3 pencils (c₁t+d₁s)(c₂t+d₂s)x² + (c₃t+d₃s)(c₄t+d₄s)y² = 1 under seven independent square classes; 2, ∞ ∈ S | verbatim match (l. 60–69) | ✓ |
| Lipshitz LGP via DHMP arXiv:2308.13609 pp. 2–3 | increasing form; LGP over a finite set of difficult primes | excerpt matches DHMP's report; Lipshitz 1978 itself not accessed (author says so) | ✓ |
| Bloom arXiv:2112.03726 Thm 2 | positive upper density ⇒ finite S, Σ1/n = 1 | verbatim match | ✓ |
| Heath-Brown three cubes via Booker–Sutherland arXiv:2007.01209 | conjecture n(B) ~ ρ_sol log B for k ≢ ±4 (9) | matches excerpt and PDF (p. 1/5) | ✓ |
| Duke–Schulze-Pillot Invent. Math. 99 (1990) | ternary: sufficiently large n primitively represented by the spinor genus (bounded divisibility at anisotropic primes) are represented; ineffective | not re-read by me either (no PDF access attempted beyond metadata); memo's (memory) statement agrees with my recollection of the theorem; correctly flagged NOT verified | ✓ as flagged |
| Bhargava–Hanke 290-theorem | "Invent. Math. 2012"; universal iff represents the 29 critical integers ≤ 290 | statement ✓ (for integer-*valued* forms). **Venue wrong/unverified**: the paper is a preprint (2005/2011; PDF at math.stanford.edu/~vakil/files/290-Theorem-preprint.pdf, HTTP 200); Alladi (Phil. Trans. 2020) still lists it as "in press"; I found no published Invent. Math. record (one low-quality web page claims Invent. 197 (2014), unconfirmed). The saved excerpt's wording "represents every integer above 290" is garbled | defect 6 |
| Ono–Soundararajan Invent. Math. 130 (1997) | GRH ⇒ x²+y²+10z² represents all eligible odd n except 18 | agrees with my recollection; flagged (memory); excerpt's "4(16μ+6)" should be 4^λ(16μ+6) | MINOR |
| Ghosh–Sarnak arXiv:1706.06712 | on the Markoff family axis pointwise HP is FALSE | abstract (fetched): "for almost all k the Hasse Principle holds … and that there are infinitely many k's for which it fails" ✓ — but the saved excerpt truncates the failure clause, so the doc's claim is not supported by its own excerpt | defect 8 |
| Moshchevitin–Shkredov (q = O(p³⁰), p | q) | — | excerpt matches arXiv:1911.07487 | ✓ |

Defects:
6. **MINOR** (z31_quadratic_forms.md item 3; sources/lit2026g/bhargava_hanke.txt): "Invent. Math. 2012" is not verified and
   probably wrong; cite as "Bhargava–Hanke, Universal quadratic forms and the 290-Theorem, preprint (2011)". Replace the
   garbled excerpt by the correct statement: an integer-valued positive-definite quadratic form represents every positive
   integer iff it represents the 29 critical integers 1, 2, 3, 5, …, 290. Also, B2 table row 3 "(iii) Eisenstein main term
   ≍ n^{1/2}" is right for ternary forms but the 290-theorem concerns ≥ 4 variables (main term ≍ n^{k/2−1} ≥ n); harmless for
   the M1 classification, but the row conflates them.
7. **MINOR** (B2 table row 1): Zaremba-for-a.e.-q is BK **Thm 1.2** (alphabet {1,…,A}, "almost every positive integer");
   Thm 1.8 is the general-alphabet version with the multiplicity bound. Both are cited correctly in substance; add Thm 1.2.
8. **MINOR** (sources/lit2026g/ghosh_sarnak.txt): add the second half of the abstract ("… and that there are infinitely many
   k's for which it fails"), which is what row 2 relies on.

## Claim (5) — Zaremba → ES-five transfer ("no M1")

**Verdict: SOUND-AFTER-REPAIRS** (conclusion right; can be partly upgraded from Assessment to a theorem-backed statement;
one internally inconsistent phrase).

Re-derivation. DEDEKIND_ES Cor 4.6 (stated for p ≡ 1 (8); for p ≡ 5 (8), A = 2 already gives λ ≤ 2): the five X/e-slices of ES(p)
hold ⟺ some QNR A lies in L_{≤3}(p) = {A ∈ [1, p) : HJ-length(p/A) ≤ 3}. Writing the negative CF, length 3 means
p = b₁b₂b₃ − b₁ − b₃ (b_i ≥ 2), A = b₂b₃ − 1; length 2 means A | p + 1. So |L_{≤3}(p)| is a 3-fold divisor-type count.
From-scratch check `scripts/review_r273_hjcount.py` (fast enumerator validated against brute-force HJ length for every
p ≡ 1 (4) < 3000; then 12 random primes p ≡ 1 (8) per decade):

| p ≈ | mean \|L≤3\| | min | mean #QNR | min #QNR | mean/log²p |
|---|---|---|---|---|---|
| 10⁴ | 65 | 51 | 45 | 38 | 0.72 |
| 10⁶ | 151 | 119 | 100 | 74 | 0.74 |
| 10⁸ | 256 | 207 | 180 | 132 | 0.71 |
| 10¹⁰ | 398 | 315 | 280 | 190 | 0.71 |

So |L_{≤3}(p)| ≈ 0.7 log² p, stable ratio — confirms "≍ log² p" (EVIDENCE) and that the menu is polylog, not a power.
(Side observation: the QNR fraction is ≈ 0.68–0.70, not 1/2 — the length-2 part A | p + 1 and the A = b₂b₃ − 1 structure
bias the symbol; irrelevant to the verdict, but a heuristic "each A is a QNR with probability 1/2" undercounts.)

Is the "no M1" argument right? Yes, and more strongly than stated:
* The Shkredov/Zhang input is a power-size gluing count q^{2w_M−1} (I confirmed in Zhang §4 that the count of a ∈ K ∩ K⁻¹ is
  the quantity Thm 3.6 asymptotically evaluates; growth/expansion gives main term ≫ error only when |K|²/q is a power).
  The ES-five count is ≈ 0.7 log² p at every sampled p, so a power-saving asymptotic cannot be the mechanism. ✓
* **The "no power main term" claim is in fact provable for almost all p, not merely an Assessment**: by Elsholtz–Tao
  (Thm 1.7 of "Counting the number of solutions to the Erdős–Straus equation on unit fractions", J. Aust. Math. Soc. 2013;
  from memory, not re-read here) Σ_{p≤N} f(p) ≪ N log²N log log N, so the average of f(p) over primes is (log p)^{3+o(1)} and
  #{p ≤ N : f(p) ≥ p^ε} = o(π(N)) for every ε > 0. Each ES-five certificate A yields an ES solution, and the map
  A ↦ solution is finite-to-one with bounded fibres (a solution determines its slice data up to O(1) choices — to be
  confirmed against DEDEKIND_ES Cor 1.2 / Thm 4.5 before upgrading the label); then the certificate count is < p^ε for
  almost all p. Hence for ES there is *provably* no pointwise power-size
  main term to exploit (along a density-one set of p); only the "every p" lower bound remains open.
* "No alphabet knob" ✓: Cor 4.6 is an equivalence for the five slices; enlarging the HJ length beyond 3 produces fractions
  that are not ES certificates in that dictionary. The author correctly withdrew the earlier "halves have p^{o(1)}" claim
  (prefix sets with one unbounded letter can be power-size).

Defects:
9. **MINOR** (B2_ACROSS_FIELDS §4.1, "dimension 0, critical exponent 2δ = 1"): self-contradictory parenthetical — a
   finite-length word set has dimension 0, while "2δ = 1" is the critical exponent δ = 1/2 at which the BK count
   N^{2δ−1} becomes N^{o(1)}. Repair: "(a finite-length word set: its count ≍ log² p sits at the critical regime
   2δ − 1 = 0 of the BK count N^{2δ−1}, i.e. no power)". Same for memo 1 l. 75–77 ("polylog regime is δ = 1/2 exactly" — at
   δ = 1/2 the count is N^{o(1)}, not necessarily polylog).
10. **MINOR (strengthening)** (§5 pattern table row M1 and memo 1 (c)): add the Elsholtz–Tao average bound as the rigorous
   reason M1 is unavailable for almost all p (with the Elsholtz–Tao statement verified in the source, or marked (memory)).
   Without it, "B2 lacks M1" rests on EVIDENCE at sampled p.

## Claim (4) — the M1–M4 pattern table (§5; Assessment)

**Verdict: GAP (Assessment is defensible in spirit, but M1 is defined ambiguously and the table's "B2 lacks M1 because F2"
does not follow; one mechanism class is missing).** Not FATAL: the label is Assessment and no downstream claim depends on it.

Search for a counterexample (pointwise existence, polylog or O(1) expected count, none of M1–M4):
* **Fermat p = x² + y² via Thue's lemma / Minkowski** — final count exactly 8 (O(1)), pointwise for every p ≡ 1 (4). The
  mechanism is a pigeonhole on ≍ p pairs (x, y) ∈ [0, √p]² against p residues: a *power-size auxiliary* count, not a power-size
  count of the final objects. Likewise **Pell** (solutions of height ≤ X: ≍ log X; Dirichlet pigeonhole + unit group) and
  **Gauss's class-number-one / one-class-genus representations** (row 3(i)). So "polylog final count ⇒ no M1" is false as a
  principle: M1 can live on an auxiliary set. The table's M1 row reads "B2 lacks it because F2: ≍ (log p)²–(log p)³" —
  but F2 is about the final certificate count. What actually blocks the Thue/Minkowski route for B2 is F3 (the exact height /
  tied modulus; memo 12 (c)(1), SYNTHESIS_SPARKS8 Prop 1.5) and (J)85's sub-power windows — the memos know this, the §5 table
  does not say it. These examples are all M1-auxiliary (+ M3 lattice), so the table is *not refuted*, but its "B2 lacks it
  because" column is wrong for M1.
* **Count-congruence mechanisms** — Chevalley–Warning, Erdős–Ginzburg–Ziv, Alon's Combinatorial Nullstellensatz,
  Zagier's parity, Chen's "orbit sizes ≡ 0 (mod p)". These prove existence from a congruence on the number of solutions,
  with no main term and no transitivity; final counts can be O(1). The table files Zagier and Chen under M3 ("homogeneity /
  group action"), which mislabels them: Chen's Thm 1.2.5 is a degree congruence on Hurwitz spaces, used *together with* BGS's
  giant component; Chevalley–Warning has no group action at all. Not a counterexample to "B2 offers none" (the campaign's T1
  and (J)2 Thm 6.1 cover parity/involution routes), but the pattern as stated omits a whole class.
* **Least witnesses under GRH** (M2) ✓; **2^k + p covering** (failure side) ✓ correctly used as the converse phenomenon.
* I found no pointwise theorem with polylog *final and auxiliary* counts that avoids M2/M3/M4. So the qualitative message
  ("every known pointwise theorem has a power-size count somewhere, a fixed-modulus character/group, a homogeneity, or object
  freedom") survives.

Defects:
11. **MAJOR** (B2_ACROSS_FIELDS §5 pattern table, row M1, and the sentence "B2 offers none"): split M1 into
   M1a "power-size count of the final objects" (Duke, ternary, Borwein–Choi, BGS, Shkredov/Zhang, HBP) and M1b "power-size
   auxiliary set + pigeonhole/volume" (Thue, Minkowski, Dirichlet/Pell). B2 lacks M1a by F2 (and, per defect 10, provably for
   almost all p); B2 lacks M1b only by F3/(J)85 (no fixed target class before the point is chosen; sub-power covering
   windows). State this in the "B2 lacks it because" column.
12. **MINOR** (same table, row M3): add **M5 count-congruence** (parity / mod-p count: Zagier, Chevalley–Warning, EGZ, Chen
   Thm 1.2.5) with "B2 lacks it because: T1 (the Type I/II count is 0 at every odd square m² ≡ 1 (4), so a count-congruence
   forcing a non-zero count must use primality / the quadratic character, F6) and (J)2 Thm 6.1 (finite-menu affine involutions barred,
   conditional)". Move Zagier and Chen there.
13. **MINOR** (row M1 "Graham"): Graham's 77-theorem is an inductive construction (n ↦ 2n + 2, 2n + 9 from a finite base),
   not a power-size main term; it belongs to M4 only (where it is already listed).

## Claim (6) — hygiene of sources/lit2026g

**Verdict: SOUND.** 32 text files, **22.8 KB of text in total** (largest: Shkredov excerpt 4.5 KB); the "136K"/"≈ 130 KB" figure is
disk-block usage, not content. Every file starts with a source line (arXiv id / URL / venue) and a read-by note; no full-text
copies of papers; no PDFs added. Excerpts I compared with fresh PDFs (Shkredov Cor 1/Thm 8/Lemma 13, Zhang Thm 1.2/Rem 1.3–1.4,
BK Thm 1.8/(1.37), Chen Thms 1.2.3/1.2.5/1.2.6, Harpaz Thm 1.0.1, Bloom Thm 2, Booker–Sutherland) are faithful (pdftotext
fragments, some with dropped symbols, e.g. Shkredov "bounded by √" truncated, Harpaz "[d2,3]]" for [Δ₂,₃]).

Defects:
14. **MINOR** (AGENT_REPORT_O261 header, "≈ 35 tiny text files, ≈ 130 KB"): 32 files, ≈ 23 KB of text. Also the report's
   "first pointwise result in the thin-orbit family" should read "first pointwise result with an *absolute* alphabet" —
   Korobov (M = O(log q)) and Moshchevitin–Murphy–Shkredov (M = O(log q / log log q), all primes) were pointwise already,
   with growing alphabets (Zhang p. 1 and Shkredov p. 2 say so).
15. **MINOR** (excerpt files): fix the garbled symbols noted above and the truncated Ghosh–Sarnak / Bhargava–Hanke excerpts
   (defects 6, 8).

## Summary verdicts

| claim | verdict |
|---|---|
| (1) Zaremba pointwise preprints (existence, statements, status, mechanism) | **SOUND** (minor: Zhang depends on Shkredov's framework) |
| (2) citation accuracy (13 items) | **SOUND-AFTER-REPAIRS** (Bhargava–Hanke venue; truncated excerpts) |
| (3) Lemma 7.1, Lemma 4.1 | **SOUND** (Lemma 4.1 fully re-derived + 522-shot ideal enumeration; Lemma 7.1 wording) |
| (4) M1–M4 pattern | **GAP** (MAJOR 11: M1 conflates final vs auxiliary counts; missing count-congruence class) |
| (5) Zaremba → ES-five "no M1" | **SOUND-AFTER-REPAIRS** (can be upgraded via Elsholtz–Tao for a.a. p) |
| (6) sources hygiene | **SOUND** |

No FATAL defects. One MAJOR (11). MINOR: 1–10, 12–15.
