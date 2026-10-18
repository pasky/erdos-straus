# R276 — hostile review of O266 (ZAREMBA_TRANSFER.md, z36 memos/scripts)

Reviewer: R276 side agent (branch side-agent/review-zaremba, merged side-agent/zaremba-transfer @ O266 cp1).
Sources checked: Shkredov arXiv:2603.14116v2 (full PDF downloaded from arxiv.org, pdftotext + bbox font check);
Rickards–Stange arXiv:2401.01860v3 (excerpt in repo + arXiv PDF, see §1); Chang preprint excerpt in repo;
Zhang arXiv:2605.02518v2 (excerpt in repo). From-scratch scripts: `scripts/review_r276_*.py`.

## Summary verdicts (filled in claim by claim)

| # | Claim | Verdict |
|---|---|---|
| 1 | Rickards–Stange dictionary (§5), Question R | SOUND-AFTER-REPAIRS: sources exact; rows 1, 3, 4 are analogies (D3); row 2 made exact here (RS Def 2.4 holds for the ES slice numerator sets, PROVED) |
| 2 | Method extraction, threshold 1 − w ≤ κ/8, constants | SOUND-AFTER-REPAIRS (D1 MAJOR: M = 22000 is a misreading of M = 2^{2000}; D4) |
| 3a | Theorem A + Chang/Larcher attribution | SOUND-AFTER-REPAIRS (D2: “=” → “≤”); bound re-checked at all 78 495 primes ≤ 10⁶ |
| 3b | Lemma C / Lemma D | SOUND / SOUND (wording D6) |
| 3c | ZQ evidence, Theorem B, Zaremba(M) ⟹ ZQ_{4Mn_p} | evidence SOUND except the “costs nothing” claim (D5); Thm B SOUND-AFTER-REPAIRS (D2); reduction SOUND |
| 3d | numerator-free recount (12 exceptions ≤ 2·10⁶, max 510) | SOUND (memo wording D8) |
| — | §2.2 ladder table | GAP: computed with a false HJ-length formula (D2), must be rerun |
| — | Labels | SOUND (every preprint use CONDITIONAL/Assessment; no ES overclaim) |

No FATAL defects. MAJOR: D1, D2 (D2 is inherited from DEDEKIND_ES §2 and must also be repaired there).
Repairs to the author's files: **not applied** (author's last commit 16 min before this review finished; parent to
forward).

## Defects

**D1 (MAJOR) — Shkredov's constant is M = 2^{2000}, not 22000.** Locations: ZAREMBA_TRANSFER.md §1.4 ("M = 22000
suffices"), §4 Reading ("constant M ≥ 22000 (Shk (158))"), BRAINSTORM/z36_density_threshold.md line 10,
AGENT_REPORT_O266 SHARP 2. In the arXiv PDF (p. 38, eq. (158)) the "2000" is a superscript: pdftotext -bbox gives the
glyph "2" at baseline (yMin 221.96, height 9.7) and "2000" raised and smaller (yMin 219.49, height 7.1). pdftotext
-layout flattens this to "22000". Internal consistency confirms 2^{2000}: (157) bounds the digits by
max{10(κε)^{−1}, 100δ^{−60}}, and with κ ≥ 2^{−1656}, ε < 1/18 this is ≈ 180·2^{1656} ≈ 2^{1663.5}; Theorem 38
(1 − w_M ≥ 1/(4M) … ) plus M∗ ≥ 40M then lands below 2^{2000}. Moreover the author's own threshold 1 − w ≤ κ/8 with
1 − w_M ≥ 1/(4M) (Shk Thm 38) forces M ≥ 2/κ ≥ 2^{1657}, which is flatly incompatible with M = 22000 — the document
contradicts itself in §1.3 vs §1.4. Repair: replace "M = 22000" by "M = 2^{2000}" everywhere, and add the one-line
consistency check (threshold ⇒ M ≳ 2/κ). The qualitative conclusions of §4 ("negligible contribution") only get
stronger.

### Claim (1): the Rickards–Stange dictionary (§5, AGENT_REPORT SHARP 1)

**Source check.** arXiv:2401.01860v3 downloaded; published as Duke Math. J. 174(15) (2025), doi
10.1215/00127094-2025-0017 (Project Euclid / Colorado experts listing found by web search). Every cited statement
matches the paper: Def 2.1/Prop 2.2 (Ψ = {γ ∈ Γ₁(4)_{≥0} : (a/b) = 1}); Def 2.4; Thm 2.5; Thm 2.8 (non-numerators of
Ψ(2,3) = squares ∪ {3,6,7,10,12,15,18,19,27,31,34,55,63,99,115}, 15 values — counted); Prop 2.9 (δ(Ψ) = 1, not f.g.);
Thm 2.10 (any ε > 0: f.g. Γ ⊆ SL₂(ℤ)_{≥0} with 1 − ε < δ < 1 and reciprocity obstructions); Thm 2.20 (BK alphabet
local–global false; A = {4,…,128}, δ_A = 0.500890640842); Conj 2.15 (n > 10569, Ψ₁ = ⟨[[1,1],[0,1]],[[1,0],[4,1]]⟩,
δ₁ ≈ 0.719); Conj 2.22 (v > 7968219670470). Proof mechanism of Thm 2.6: Lemma 4.1/4.3 (lattice line ux + vy = n, a
run of ⌊n/8xy⌋ consecutive integers must contain both symbol values) + Lemma 5.2 via the explicit Pólya–Vinogradov
bound of Frolenkov–Soundararajan — the author's "line + Pólya–Vinogradov" is accurate.
Note: Thm 2.10's *statement* only gives Γ ⊆ SL₂(ℤ)_{≥0}; Γ ⊆ Ψ (as used in Question R) comes from its *proof*
(Ψ₁ ⊆ Γ′_n ⊆ Ψ, RS p. 24). Cite "proof of Thm 2.10".

**Is the dictionary exact?** Row by row (from-scratch checks in `scripts/review_r276_dict.py`):
* Row 1 (Ψ preserves the Kronecker symbol ↔ Cor 4.1 genus character): **analogy, same mechanism** (Jacobi reciprocity
  run along Euclid). Not equivalent statements: RS is a length-free invariance under a semigroup; Cor 4.1 is a
  fixed-length formula mod 8. Neither implies the other as stated.
* Row 2 (Thm 2.5 ↔ Prop 3.1/Thm 4.5): **can be made exact, and I did** (PROVED here). Let
  X_T = {n ≡ 1 (4) : n = tuv − u − v with t, u, v ≥ 2, 4 | t} (the (A)3 slice numerators). Then X_T satisfies *both*
  clauses of RS Def 2.4: (2) no square (Prop 3.1); (1) for every modulus m, X_T contains n ≡ 1 (mod m), namely
  (t,u,v) = (4, 4m−1, 4m) gives n = 64m² − 24m + 1 ≡ 1 (mod 8m). Same for the 4 | A slice with the family
  (t,u,v) = (3, 8m−1, 8m) (A = 24m − 4, n ≡ 1 mod 8m). Checked for m < 2000 (Jacobi symbol −1, n ≡ 1 mod 8m). So *the ES five-slice numerator sets exhibit a
  reciprocity obstruction in the exact sense of RS Def 2.4* — except that Def 2.4 is formulated for semigroup orbits,
  and the length-3 slice set is not (known to be) one. The closer RS analogue is Thm 2.18/Cor 2.19 (a
  congruence-restricted alphabet with fixed tail has constant symbol), not Thm 2.5 (the Ψ invariance).
* Row 3 (Thm 2.8 ↔ DEDEKIND 4.4): **shape analogy, label mismatch**. Thm 2.8 is a PROVED statement about a fat
  (δ = 1) orbit; DEDEKIND 4.4 is a CONJECTURE about two fixed-length slices. The label-matched counterpart of 4.4 is
  RS Conj 2.14/2.15 (thin, conjectured explicit exceptional set), not Thm 2.8.
* Row 4 ("length-3 words: dimension 0"): **wrong normalisation**. In the BK/RS normalisation (#orbit points of norm
  ≤ X ≍ X^{2δ}), the length-3 HJ words with numerator ≤ X number ≍ X log² X (from-scratch count: ratio to X log² X =
  0.270, 0.311, 0.341 at X = 2·10³, 2·10⁴, 2·10⁵), i.e. **critical exponent δ = 1/2, exactly the BK threshold**, with a
  log² excess. This also contradicts the author's own memo z36_density_threshold ("ES-five has effective dimension
  w = 1/2 exactly"). Repair below (D3).
* Row 5 (line + PV ↔ hyperbola, log² n points): SOUND.

**Verdict (1): SOUND-AFTER-REPAIRS.** The source facts are right; "same source / same obstruction / same conjecture
shape" (AGENT_REPORT SHARP 1) is an analogy at rows 1, 3, 4 and must be labelled Assessment; row 2 is exact at the
level of RS Def 2.4 (my repair above). Question R is well posed (RS proof of Thm 2.10 gives Γ ⊆ Ψ with δ → 1).

### Claim (2): method extraction ("M1⁺: density, not power count")

Checked against the full Shkredov PDF: Lemma 13, §5.1 (130)–(133), Lemma 17/(40), §4 first paragraph ((61), (99),
(119) bound ε), (134)–(135), (151) ε < 1/18, (156), (157), Appendix (158)–Lemma 40 (c ≥ 1/1640, k = 1641,
κ ≥ 2^{−1656}); Shkredov's own intro remark (better M "provided uniform distribution results can be obtained for A^{−1},
A an arbitrary collection of intervals of length q^{1/9−o(1)}") — which independently confirms the author's
window-conflict reading. Zhang (3.1)–(3.8), Rem 1.3, 1.4 match the excerpt.
Re-derivation: |A| ≍ q^{w}N^{1−w}, N = q^{2ε}; |A|N^κ ≫ q ⟺ 2ε(1 + κ − w) > 1 − w; with ε ≤ ε₀:
(1 − w)(1 − 2ε₀) ≤ 2ε₀κ, and ε₀ = 1/18 gives 1 − w ≤ κ/8. Arithmetic correct. w₅ ≈ 0.8368 ⇒ |Z∗| ≈ q^{2w−1} = q^{0.674}: correct.

**Verdict (2): SOUND-AFTER-REPAIRS** (as an Assessment of *this* proof architecture). Defects: D1 (M = 2^{2000}), D2, D4.

### Claim (3a): Theorem A, Chang/Larcher attribution

Re-proved line by line. Remainder/convergent identities q_iρ_{i−1} + q_{i−1}ρ_i = p and aq_i ≡ (−1)^iρ_i: correct
(induction). c_i ≤ ρ_{i−2}/ρ_{i−1} ≤ p/(q_{i−1}ρ_{i−1}) uses q_{i−1}ρ_{i−2} ≤ p: correct. Injectivity of
(a, i) ↦ (x, y, σ): correct (x = q_{i−1} < p; q₀ = q₁ only if c₁ = 1, separated by σ). Tail count
2(p/k)(1 + log p), Markov step, (p − 1) − 2p/5 > (p − 1)/2 ⟺ p > 5: correct. From scratch
(`scripts/review_r276_thmA.py 1500 1000000`): the tail inequality #{(a,i): c_i ≥ k} ≤ 2#{xy ≤ p/k} for every k and
#good a > (p − 1)/2 hold exhaustively at all primes 7 ≤ p < 1500; Thm A bound vs a non-residue witness A < 400 at all
78 495 primes 7 ≤ p ≤ 10⁶: 0 violations (worst witness r = 4, p = 2351).
**One false step**: the last line "r(p/A) = 1 + Σ_{i odd} a_i(p/A)" — the formula is wrong (D2); only "≤" holds, which
suffices. Attribution: Chang Thm 5 (most primitive roots x have Σ a_i(x/p) ≲ log p log log p; primitive roots are
QNRs) gives λ(p) ≪ log p log log p for large p — "known in substance" is fair; Larcher (1.1) gives *some* b, not a QNR,
and the author words this correctly. Theorem A's explicit all-p > 5 constant is the author's.
**Verdict (3a): SOUND-AFTER-REPAIRS** (replace "=" by "≤", D2).

### Claim (3b): Lemma C, Lemma D
Lemma C re-proved (⇒: p | u forces p | v and then p = tuv − u − v ≥ uv ≥ p²; ⇐: multiply by uv; 0 < n < 2p).
From scratch: all 441 702 triples t,u,v ≥ 2 with tuv − u − v < 3p, primes p < 400: 0 mismatches. **SOUND.**
Lemma D: correct up to wording — the congruence-defined enlarged set is the set of length-3 words of kp, k ≤ K, *with
p ∤ uv* (not "exactly the length-3 certificates of kp"; words of kp with p | u are not produced). The conclusion "no
information about p" is an Assessment, fine. **SOUND (MINOR wording, D6).**

### Claim (3c): ZQ_M evidence, Theorem B, the Lemma-10 reduction
* EVIDENCE recheck (`scripts/review_r276_zq.py`): ZQ₄ for all 2259 primes 7 ≤ p < 2·10⁴, ZQ₃ for all except 277
  (zq(277) = 4): confirmed. ZQ₃ windows: all 174 primes in [10⁵, 1.02·10⁵) and all 75 primes in [10⁶, 1.001·10⁶):
  confirmed. **But** "In every case except 277 the QNR restriction costs nothing (min over non-residues of the max digit
  = Zaremba's min)" is **false**: at 358 of the 2259 primes the QNR minimum exceeds the Zaremba minimum (357 times
  2 → 3, e.g. p = 43: the only a with digits ≤ 2 is a = 31, a residue; plus 277: 2 → 4). The author's own script
  prints this (`z36_zq.py 7 300`: worst (4, 2, 277), and many (3, ·) with mz = 2). D5.
* Theorem B: r ≤ 1 + Σ_{j even} c_j ≤ 1 + M⌊s/2⌋, p = q_s ≥ F_{s+1} ≥ φ^{s−1}: correct (again "=" → "≤", D2);
  arithmetic checked for all A/p, p < 1500. CONDITIONAL label correct. **SOUND-AFTER-REPAIRS.**
* Zaremba(M) ⟹ ZQ_{4Mn_p}: re-derived. If a has digits ≤ M, Shk Lemma 10(ii) gives x|y| ≥ q/(4M) for all solutions
  of ax ≡ y; for (ca)x ≡ y put x' = cx mod q ∈ [1, q), then ax' ≡ y and x' ≤ cx, so cx|y| ≥ q/(4M); Lemma 10(i) with
  M' = 4cM gives digits of ca/q ≤ 4cM. If a is a QR, n_p·a is a QNR. **SOUND** (Lemma 10 is elementary/classical; the
  input Zaremba(M) for all large primes is CONDITIONAL on Shkredov). GRH ⇒ λ ≪ M log³ p: correct.
* Window conflict (§4 item 1): correct for *per-interval* character-sum input (Burgess needs N > q^{1/4+δ} ⟺ ε > 1/8;
  Shkredov's own intro says the same about q^{1/9} intervals). "Incompatible" is overstated: averaged inputs over the
  T ≍ t^{2w} intervals (moments/large sieve) are not excluded by this argument. MINOR (D7).

### Claim (3d): numerator-free rung recount
From scratch (loop over (t, u ≤ v), `scripts/review_r276_lemmaC_numfree.py`): exceptions ≤ 2·10⁶ are exactly
{1, 2, 3, 5, 6, 9, 11, 14, 15, 35, 105, 510} — 12 values, max 510. **SOUND.** Memo wording "odd squares are *not*
exceptions here" is contradicted by 1 and 9 in that very list (should read "no odd square > 9"). MINOR (D8).

## Numbered defects (continued; D1 above)

**D2 (MAJOR, definitional; inherited from DEDEKIND_ES §2 R169 repair) — "r(p/A) = 1 + Σ_{i odd} a_i" is false for
half of all A.** Location: ZAREMBA_TRANSFER Notation line; Thm A last line; Thm B proof; `scripts/z36_ladder.py`
docstring/implementation (and `z36_lambda_witness.py`). Counterexample: 7/2 = 4 − 1/2 = [[4, 2]] has HJ length 2, but
7/2 = [3; 2] gives 1 + 2 = 3. From scratch (`scripts/review_r276_hjformula.py`), over all coprime 0 < A < n < 400:
24 258 of 48 516 pairs mismatch; the corrected formula **r(n/A) = 1 + Σ_{i odd} a_i − [s odd]** (canonical CF
[a₀; …, a_s], a_s ≥ 2) has 0 mismatches (equivalently: use the expansion whose last index is even). Consequences:
(i) Thm A and Thm B survive verbatim with "≤" (the formula is always ≥ the true length). (ii) The §2.2 ladder table is
mis-measured: at n = 10009 the true |S₃|, |S₄|, |S₆|, |S₈| are 69, 263, 827, 1791 (table: 63, 229, 685, 1594 — exactly
the formula values); QNR shares 0.70/0.73/0.53 (table 0.70/0.75/0.54); λ = 2 unchanged. The other rows must be
recomputed; qualitative readings (polylog vs power) unaffected. (iii) Upstream: DEDEKIND_ES §2 ("(R169 repair:) …
r(n/A) = 1 + Σ_{i odd} a_i") and the Cor 4.6 parenthetical carry the same error — the parent should route a repair to
DEDEKIND_ES (the length-3 pattern [v−1; 1, t−2, 1, u−1] is correct only for u ≥ 3; for u = 2 the canonical CF is
[v−1; 1, t−2, 2] with odd last index). Repair: state r via the HJ recursion (or the corrected formula), and rerun the
ladder table with true HJ lengths.

**D3 (MINOR→MAJOR for the SHARP claim) — RS dictionary overstated / mis-normalised.** Locations: §5.2 table rows 1, 3,
4; AGENT_REPORT SHARP 1 ("same source … same obstruction … same conjectural shape"). Repairs: (a) label rows 1, 3, 4
Assessment/analogy; (b) row 2: insert the exact Def-2.4 statement proved in this review (slice numerator sets X_T, X_A
with families (4, 4m−1, 4m), (3, 8m−1, 8m)), and name RS Thm 2.18/Cor 2.19 as the closest RS analogue; (c) row 3: pair
DEDEKIND 4.4 (CONJECTURE) with RS Conj 2.14/2.15, not with the PROVED Thm 2.8; (d) row 4: replace "dimension 0" by
"BK-normalised exponent δ = 1/2 (≍ X log² X words of numerator ≤ X), i.e. exactly the BK threshold" — consistent with
memo z36_density_threshold; (e) Question R: cite "proof of RS Thm 2.10 (Ψ₁ ⊆ Γ′_n ⊆ Ψ)" for Γ ⊆ Ψ.

**D4 (MINOR) — §1 notation slips.** (a) "density q^{−o_κ(1)}" (§1.3, §6, memo) should be "density ≥ N^{−κ} = q^{−2κε}"
(a fixed tiny power, not o(1)). (b) "1 − w ≤ κ/8" is the §5.1/(151) idealisation; in the Thm 8 proof the counting is at
scale N∗ = N^{1/10} with M∗ ≥ 40M (Shk §5.4, Appendix), so the true threshold carries different constants — write
"1 − w = O(κ)" or explain. (c) Zhang's g_j = [[2j, 1−4j²], [−1, 2j]] equals −T^{−2j}ST^{−2j}, not ±T^{2j}ST^{2j}
(checked symbolically, `review_r276_dict.py` (d)); the "large HJ letters" remark then concerns letters −2j.

**D5 (MINOR) — false "QNR restriction costs nothing except at 277".** Location §4 ZQ EVIDENCE, memo
z36_chi_twist_window l. 27–28. 358/2259 primes < 2·10⁴ have QNR-min > Zaremba-min (357 cases 2 → 3). Repair: "the QNR
restriction never pushes the minimum above 3 except at 277 (it raises 2 → 3 at 357 primes)".

**D6 (MINOR) — Lemma D wording.** "exactly the length-3 HJ certificates of the multiples kp" → "the length-3 words of
kp, k ≤ K, with p ∤ uv".

**D7 (MINOR) — window conflict overstated.** §4 item 1: "incompatible" holds for per-interval (Burgess) input only;
say so, and note averaged character-sum inputs are not excluded by this argument.

**D8 (MINOR) — memo z36_numerator_free_rung**: "odd squares are not exceptions here" — 1 and 9 are; say "> 9".

**D9 (MINOR) — §5.3 non sequitur.** "…which is why RS's counterexample does not contradict Shkredov/Zhang": there was
never a conflict to explain — Zaremba's alphabet {1,…,M} has no reciprocity obstruction (RS p. 7, discussion after
Cor 2.17), and Shkredov/Zhang assert nothing about 4ℤ⁺-alphabets. A sharper and simpler point: every 4ℤ⁺-alphabet
semigroup has δ bounded away from 1 (all digits ≥ 4), so it can never meet the near-full-dimension threshold of §1.3;
any growth proof for such alphabets needs a different counting step regardless of reciprocity.

**Labels.** Every use of the 2026 preprints is labelled CONDITIONAL — checked: §1 (Assessment from sources), §4 item 3
("CONDITIONAL on the preprints"), Theorem B (CONDITIONAL on ZQ_M, which is not a preprint consequence). No overclaim of
ES found; "ES is not solved" stated. Theorem A PROVED: correct after D2.
