# Final faithfulness review, round 4

**Overall verdict: MAJOR (remaining faithfulness defects, not a failure of the main theorems).**

Reviewed `EXSET_FUNCTION_FIELD.md` at HEAD `c3c0f72e`, against every requested MAJOR/MINOR repair in R2 and R3. I read §0, §§3.8–3.9, §§4–5 in full, and inspected the other repair locations and §6. The central repairs to C2, Proposition 3.8, and Theorem 3.9 are present. No new obstruction to their substantive conclusions was found. However, the summary still strengthens an image-group conclusion, and the integer lower-tail discussion still asserts an unjustified equivalence and uses an impossible cumulative formulation in the presence of the acknowledged sporadic exceptions.

Line numbers below refer to the reviewed manuscript. Only this report was created; no existing file was changed and no commit was made. All shell invocations used `ulimit -v 8000000` and explicit timeouts. Previously SOUND computations/proofs were not rerun. The newly quoted q=43 moments match `data/z51_ffield/moments.txt`; this is a provenance check, not independent numerical certification.

## Remaining defects and exact repairs

### 1. MAJOR: the summary upgrades a statement about an image to a subgroup of the full group

Line 20, row 7′:

> “mixed transitivity plus Goursat give ∏ Alt ⊆ G_n.”

Line 730 repeats this in the review history. Theorem 3.9(ii), lines 501 and 513–522, correctly proves containment in **G\***, the image of G_n on the selected small-shape fibres. A quotient/image containing a product of alternating groups does not, without an additional splitting argument, establish an embedded copy of that product in the original group. No such argument is supplied. This is a literal strengthening under a PROVED label, not the already repaired issue of residual sign correlations.

**Exact repair:** in lines 20 and 730 replace `∏ Alt ⊆ G_n` by `∏ Alt ⊆ G*, where G* is the image of G_n on the selected small-shape fibres`. In §5.2, lines 666–667, likewise say “the joint image on the selected fibres contains ∏ Alt.” The density bound uses only this image, so neither its proof nor its constants change.

### 2. MAJOR: the integer lower-tail repair is incomplete, and the displayed cumulative bound excludes even the known exceptions

Lines 693–695:

> “#{non-square n ≤ N failing U} ≤ N exp(−c(log N)²) … would give a finite non-square exceptional set, but it is a restatement of the desired conclusion”

The right side tends to zero. The left side is nondecreasing and includes every fixed exceptional integer for all sufficiently large N. Thus the displayed hypothesis forces **no non-square exceptions at all**, not merely eventual absence. It contradicts the six sporadic exceptions acknowledged in §§2 and 4.1. Also, the requested sufficient-hypothesis wording has not removed “a restatement”: no equivalence to T1-min, or to a quantitative witness lower bound, is established. The citation does not fix this: `LOWERTAIL_DEEP_ASTRA.md`, Theorem 7.1, explicitly uses **dyadic blocks** and states a **sufficient implication** for a negative-part moment hypothesis.

Line 652 repeats the cumulative bound and “would be the conclusion itself.”

**Exact repair:** replace both counting formulations by

> “A sufficient quantitative lower-tail hypothesis is #{non-square N < m ≤ 2N failing U} ≤ N exp(−c(log N)²) for every sufficiently large N. Since the right side tends to zero, this implies eventual absence of non-square failures. No such estimate or transfer is proved here; a qualitative Poisson heuristic does not imply it.”

Delete “a restatement of the desired conclusion” and “would be the conclusion itself.” If an equivalence to another precisely defined target is intended, state and prove it separately. This completes R2 §9 rather than merely changing the introductory label.

### 3. MINOR: CRT/EH and integer-theorem scope remain inconsistent in §5

Lines 683–685 retain:

> “level-1 distribution (analogue of exact CRT). Both hold in F_q[T] … An implication ‘GRH + EH ⇒ T1-min’ …”

The repaired table at line 649 correctly distinguishes elementary residue-class counting from EH. The paragraph again slides from one to the other without specifying a separate prime-distribution hypothesis. Its “best bounds proved in this document are the CRT ones” also needs to say **using the RH/congruence estimates alone**, given Theorem 3.9.

**Exact repair:** replace §5.3(a) by:

> “RH for Dirichlet L-functions and exact residue-class counts through degree n hold in F_q[T]. The RH/congruence estimates used in Proposition 3.7 give the CRT bounds; Theorem 3.9 uses additional geometric and group-theoretic input. No derivation of FF-T1-min from the former estimates is supplied. This does not prove a non-implication over either ring. EH concerns averaged prime-distribution errors and is not the analogue of elementary CRT.”

Line 653 still places “k = 2 and odd k known only log-averaged” beside “Chowla / Elliott for restricted-divisor indicators, uniform in k.” The standard logarithmically averaged Möbius/Liouville results are not results for that restricted-divisor input, nor uniform growing-k statements. “Odd k … only” also includes k=1, where ordinary cancellation is classical.

**Exact repair for that status cell:** “The required restricted-divisor and growing-k hypothesis is not supplied. For standard Möbius/Liouville correlations, fixed-k logarithmic-average results include k=2 and odd k≥3; these are different statements.” This avoids asserting an exhaustive current classification of unweighted results.

Finally, lines 669–671 say “there is no fibre X_σ over a varying base, no G_σ.” Replace this by “No corresponding coefficient-space family and usable word/orbit correspondence for integer targets is supplied here.” The surrounding qualification “in this framework” is appropriate; retain it rather than momentarily reverting to an absolute absence claim.

### 4. MINOR: the rewritten census still contains a false range and overbroad trend

Lines 569–570:

> “3, 3, 0, 3, 0, 0, 0 at n = 5, 6, 7, 8, 10, 12, 14 … and none at odd n ≤ 15 (no failures at all there)”

This contradicts the n=5 entry in the same sentence. **Replace** “odd n ≤ 15” by “odd n = 9, 11, 13, 15”. The summary's “none beyond n=8 in the tested range” is otherwise correct.

Line 562 says “Even n: decreasing,” although the displayed even-degree counts begin 6, 21, 21, 12, 7, 3. **Replace** with “For the tested even degrees n=8,10,12,14, the counts decrease: 21,12,7,3.”

### 5. MINOR: R2's equal-factor diagonal correction is still missing

Lines 343–344:

> “W_c adds both orientations … must be halved before comparing with the Poisson means 1 and 1/2.”

For a=b, simply halving the ordered count is not the integer-valued unordered-class count: a word with u=v is counted once, not twice. This is precisely the finite-q correction requested in R2 §5(3). Section 3.8 correctly includes it in the mass, but §3.6 does not.

**Exact repair:** append/replace the normalization sentence with:

> “For a≠b the quotient count is W_c/2. For a=b, if Δ_c(f) counts diagonal words with u=v, the unordered count is (W_c+Δ_c)/2, with mean 1/2+1/(2q^a). Its limiting mean is 1/2. These changes leave the zero events unchanged.”

The finite zero-probability ratios remain valid.

### 6. MINOR: two elementary proof-wording leftovers and one false exclusivity claim

* **C2 line 436:** “N_γ ≤ q^{γ−1}·τ(h)²…” leaves h free after counting all h. R3 §1.1 explicitly requested a uniform bound. **Replace** with `N_γ ≤ 4^γ q^{(a+b)+(a′+b′)−γ−1}`, using `τ(h)≤2^γ`. This does not reopen the SOUND overlap argument.
* **Theorem 3.9, lines 528–529:** “which is 1/4 of the pairs when n is even” is false as an exact finite count (at n=12 the sole pair is {1,2}, and none is excluded). **Replace** with “which is asymptotically 1/4 of the pairs when n is even; the exact excluded count is F(⌊m/2⌋).” The newly added exact formula and all-n constants are correct.
* **§4.3, lines 635–637:** “The only U-events that are factorisation-type functions of a single polynomial are the v=1 events” contradicts §3.6: t=1 also gives `f+1=(u−1)(v−1)`. **Replace** with “The degenerate shapes discussed in §3.6 are governed by the factorisation of f+1; no comparable reduction of the genuine shape events is supplied here.” Do not claim an unproved classification of all possible reductions.

### 7. MINOR: summary and depth-language qualifications are not fully faithful

* **Row 7, line 19:** “Sampled joint/product ratios approach 1” retains convergence language that §3.6 carefully disclaims. **Replace** with “Sampled ratios are consistent with approach to 1; convergence is not proved.”
* **Row 9, line 22:** “Large q cannot give depth in N” is broader than the proved error identity and the two hypothetical budgets. **Replace the heading** with “Limits of the stated large-q error bound; conditional hybrid budgets.” In §3.7(d), line 382, replace “A depth breaker would need” by “One proposed route would require”; the specified cohomological hypothesis is not proved necessary for every approach.
* **Row 5, line 17:** “in any characteristic” correctly describes Lemma 3.2, but the following density sentence should not inherit that scope. **Replace its opening** with “For q≡3 (mod 4), in each fixed characteristic p≡3 (mod 4), the U_q exceptional density…” The all-odd-p formal group statistic is separately and correctly defined in §3.9; that is not a U_q density in characteristic 2 or in the colour-free normalization.
* **Row 13 / §6:** do not certify all repairs as completed before fixing the residual items above. **Replace** “repairs applied, residual caveats listed in §6” with “principal repairs applied; residual faithfulness corrections are recorded in R4,” and add R4 to §6 when the manuscript is next revised. The historical “CONDITIONAL” entry at line 725 is understandable as the R1-stage status, but “at the R1 stage” would avoid its literal “now” conflicting with the current PROVED label.

## R2 repair checklist

“Applied” means the requested change is present and correctly scoped; it does not mean a fresh rederivation of a result already judged SOUND. The grouping below covers the R2 requests, including the residual R1 items listed there.

| R2 request | R4 finding |
|---|---|
| §1/§2: proper-degree converse; normalization; nesting; exact mass; finite-flat weight; per-characteristic limit; boundary explanation; prime scaling | Applied and retained (§§1–3.5). |
| §1/§2: nontrivial-word wording; square counts by parity | Applied (§§3.5, 4.1); separate odd-degree census error remains, defect 4. |
| §1/§3: odd-degree-only mass proof and trimming | Applied, lines 406–414. |
| §4.1: μ_D(q) versus its limit; admissibility of either orientation | Applied, lines 416–418 and 454–456. |
| §4.3: replace distinct words by distinct unordered classes in E₂ | Applied, lines 424–432; Proposition 3.8 uses exactly that distinction. |
| §4.5: ordered/unordered numerical normalization | Applied, lines 449–451. |
| §5: sampled evidence, not convergence/product theorem | Applied in body; summary wording remains, defect 7. |
| §5: n=6 extra class; count normalization including diagonal | Extra-class scope applied; diagonal incomplete, defect 5. |
| §5: false modulus bound; lcm condition; geometric justification | False bound removed; uv and lcm used, lines 345–348; Proposition 3.8 supplies the geometric argument in its stated range. |
| §6: absolute density error, sufficient condition, explicit m_n≍n²; hypothetical budgets | Applied, lines 369–381; universal-sounding headline/direction still need defect 7. |
| §7: tested-range zeros; floor(n/s); O(1) ratio only conjectural | Floor and asymptotic qualification applied; census range incomplete, defect 4. |
| §7: consequence through μ, separate κ hypothesis, 1.03 extrapolation | Applied, lines 592–595. |
| §8: Weil nondegeneracy; count/indicator distinction; hypothetical Betti bound; rank-one arithmetic; theorem-specific shift range | Applied, lines 617–635. The baseline is now unambiguous. |
| §9: elementary integer CRT, not EH; analogy not equivalence | Table applied; §5.3(a) incomplete, defect 3. |
| §9: open is not impossible; no optimality/non-implication claim; no invented abelian quotient | Applied in §§3.8, 4.2, and transfer verdict. Row 9 still needs defect 7. |
| §9: true density remains conjectural; no universal absence of integer nonabelian information | Θ(n²) correctly remains conjectural; missing-family language mostly applied, with residual sentence in defect 3. |
| §9: Chowla error and integer status; sufficient lower-tail implication, not equivalence | Power-saving correction applied; status and lower-tail repairs incomplete, defects 2–3. |
| §10: summary k, scope, labels, review-completion claim | k and most labels repaired; remaining rows audited below. |

## R3 repair checklist

| R3 request | R4 finding |
|---|---|
| §1.1: uniform divisor bound in nonsquarefree-h count | Not applied literally; defect 6. |
| §1.2: class-based E₂ throughout | Applied, including the swap counterexample and asymmetric-shape explanation. |
| §1.3: ordered versus unordered pair numerics | Applied. |
| §2: k=1 endpoint; mixed-shape lcm rather than global 2D condition | Applied, lines 487–493. |
| §§3.1–3.2: CFSG and full Ribet references | Applied, lines 511–512 and 520. |
| §3.4: exact class formula, analytic all-n completion, all-odd-p notation | Applied, lines 470–472 and 503–508. The prose fraction still needs defect 6. |
| §4: finite moments certified; interpretation/correction heuristic; n=5 outside theorem; exact d_30/30! prediction | Applied, lines 531–540. |
| §§5.1–5.2: upper bound only, no Θ conclusion or unconditional independence | Applied in theorem and discussion; full-group/image summary mismatch remains, defect 1. |
| §5.3: integer CRT error, no missing-cover impossibility claim, methodological GRH assessment | Main repair applied; residual §5 wording in defect 3. |
| §5.4: iterated-limit scope in headline; no fixed-q/N-uniform breakthrough; numerical inequality not approximation | Applied to §3.9 and row 7′. |

## Every summary row checked

| Row | Faithfulness to body |
|---|---|
| 1–3 | Matches §§1.2–1.3 under the stated monic/q normalization. |
| 4 | Matches Proposition 3.1; k is now defined. “Every q” is within the standing q≡3 (mod 4) setting. |
| 5 | Finite-flat claim matches; density scope needs defect 7. |
| 6 | Matches Theorem 3.5/Corollary 3.5′ after absorbing errors and adjusting positive constants/threshold. |
| 7 | EVIDENCE/CONJECTURE is appropriate; remove residual convergence wording, defect 7. |
| 7′ | Upper bound, constants, odd-characteristic and iterated-limit qualifications match; subgroup/image assertion does not, defect 1. |
| 8 | Matches Proposition 3.7 as exponent-scale shorthand, not a claim of optimality or exact unit prefactors. |
| 9 | Error identity and hypothetical budgets match; categorical heading does not, defect 7. |
| 10 | Sample counts and tested-range claim match the tables; body needs defect 4. Ratios are rounded summaries, not asymptotic bounds. |
| 11 | Matches the proved fixed-q baseline and explicitly approach-specific assessment in §4.3. |
| 12 | Correctly labelled Assessment and restricted to no derivation supplied; residual transfer prose needs defects 2–3. |
| 13 | Historical verdicts match; blanket repair-completion wording needs defect 7. |

**Disposition:** retain the main theorems and their PROVED labels. Repair the two substantive faithfulness errors and the listed local wording errors before acceptance. No additional numerical experiment or rederivation of the already SOUND monodromy chain is required for these repairs.
