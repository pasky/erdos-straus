# Wave-31 paper v17 fidelity review

**Verdict: FAITHFUL-AFTER-REPAIRS.** Reviewed input commit `4b710ff69cd125bcaf1d90c72a67a5a55ba81c53` against the post-review `notes.md`, §§70–72 (lines 26888–28515, EOF), exclusively in `/tmp/es-w31C`, branch `wave31-unitC`. This is a consolidation-fidelity audit, not a new mathematical or external-source validation.

The initial PDF was not faithful despite compiling successfully: TeX comments silently removed numerical statements and INFO qualifications. All defects below are repaired. No theorem, hypothesis, table cell, or earlier status label is otherwise changed. Both the initial and repaired two-pass builds have **177 pages**.

## Numbered defects and exact repairs

Line numbers refer to `paper/espaper.tex` and remain unchanged by the surgical repairs. Quoted snippets are the defective input, not the repaired text.

1. **HIGH — line 130, abstract: missing unit hypothesis.** Exact quote: `\#\{h\leq H:-1\notin\operatorname {Rat}_a(h)\}`. Source §70 defines the event only for `(h,a)=1` (70.2), explicitly restricts the decomposition to units (Corollary 70.4), and uses that event in Corollary 70.8. The abstract instead counts unrestricted `h`, outside the ratio-spectrum domain. **Exact fix:** replace the quoted set by `\#\{h\leq H:(h,a)=1,\ -1\notin\operatorname {Rat}_a(h)\}`. The constant and asymptotic are unchanged.

2. **HIGH — line 10267, Computational 70.1: erased endpoint and caveat.** Exact quote: `20,000; their finite success proportions range from 44.37% to 100%, not yet`. The first `%` comments out `to 100%, not yet`, unlike the source's explicit 44.37%–100% range and “not yet near” qualification. **Exact fix:** replace this line by `20,000; their finite success proportions range from 44.37\% to 100\%, not yet`. The following line retains “near the asymptotic density one.”

3. **HIGH — line 10284, §70 honest walls: erased conditioning context.** Exact quote: `22% F3 share among the old-frame record-prime failures in source \S19.2 is an`. Everything after `22` disappears in the PDF; the source explicitly identifies a percentage, F3, the old frame, and record-prime conditioning. **Exact fix:** replace the initial `22%` by `22\%`, preserving the entire sentence and its empirical-warning status.

4. **HIGH — lines 11160, 11163–11164, §72.1: erased frequency and nonmonotonicity digits.** Exact quotes:
   - `19.3%, and among the displayed moduli it is 12.4%.  This is consistent with`
   - `the third window it is 53.6% at 19, 6.0% at 23, 73.2% at 43, 54.7% at 59,`
   - `69.3% at 103, and 63.7% at 199.  Larger coefficients often have a larger F3`

   TeX erases each line's suffix at its first `%`. The source retains all eight percentages, their associated moduli, and the limited consistency statement. **Exact fix:** replace all eight `%` characters on these three lines by `\%`; leave all wording, digits, and the no-scale-law caveat unchanged.

5. **HIGH — lines 11293–11296, §72.4: erased INFO labels and enrichment factor.** Exact quotes:
   - `for all 719,781 primes, 5,314 are F3 (1.429% INFO).  Among the corresponding`
   - `1,648 pairs for the 225 deep primes, 321 are F3 (19.478% INFO), a 13.63-fold`
   - `16 F3 (31.373% INFO).  This is the a-frame analogue of the source \S19.2`

   Unlike the source, the rendered paper loses all three local INFO labels, percent units, `13.63-fold`, and the old-frame analogy. The general section status does not excuse these local losses. **Exact fix:** replace the three `%` characters by `\%`, retaining the counts, analogy, and selection-free-distribution disclaimer verbatim.

6. **HIGH — lines 11318–11319, §72.5: erased budget-transition comparison.** Exact quotes:
   - `irregularly.  At fixed $\omega=3$, for example, the share moves from 54.7%`
   - `at $a=31$ to 77.7% at 127, but is already 88.1% at 43 and falls to 64.6%`

   The PDF loses percentage units and the 88.1%/64.6% countertrend, reducing the source's explicit nonmonotonic comparison to broken prose. **Exact fix:** replace these four `%` characters by `\%`. Retain the “visible only irregularly,” nonmonotonicity, no-transition-law, and exact-zero qualifications.

7. **LOW — README v17 change register: judgment calls were not actually declared.** TeX locations concerned: 10749 (71.24), the seven `\resizebox` sites listed below, and 10294 (reference mapping). There is no defective TeX statement to quote here: this is a documentation omission. Contrary to the task's description, the input README contains none of `judgment`, `terminator`, `resizebox`, or `mapping`; its v17 entry ends with “The build grows by 26 pages, from 151 to 177.” **Exact fix:** add the v17 bullet beginning “Typesetting/reference judgment calls (explicitly recorded by the fidelity review)” recording the row terminator, scaling, and Assessment 63.2 mapping, plus the requested short “Wave-31 v17 fidelity review” entry. No mathematical repair to those three choices is needed.

Defects 2–6 account for **18 unescaped percent signs on 10 lines**. PDF text extraction independently confirmed the losses before repair and restoration afterward; this was not merely a source-code cosmetic issue.

## Exhaustive source coverage

All paragraphs, definitions, proofs, quantifiers, hypotheses, status headings, quotations, and honest-wall registers in the three source sections were compared with paper Sections 32–34. A separate bounded-memory comparison extracted **all 100 tagged displays** from both versions: the tag sets coincide, and every expression/table agrees after only typography normalization, apart from the approved missing row terminator in (71.24). This includes every table cell, not just the highlighted entries. Whole-section text comparison also isolated the typography and reference remappings for inspection.

### Source §70 → paper Section 32 (lines 9657–10344)

- Status, Lemma 70.1, Corollaries 70.2–70.4, and (70.1)–(70.5): fixed prime `a=3 mod 4`, unit domain, unique-involution equivalences, exact disjoint F1/F3 split, F2 emptiness, and `a=7,h=17` bounded-budget warning all retained.
- Standard Fact 70.1 and Theorem 70.5, (70.6)–(70.14): automatic coprimality **and every nonprincipal twist having strictly smaller real pole exponent** appear explicitly at lines 9793–9801. The tied-twist/cancellation warning survives. The hard-progression proof checks the twists using CRT and handles `a=3` separately. Both positive constants, the Euler product, and all five hard-class factors `1,1/4,1/3,1/2,1/6` agree.
- Lemma 70.6, Theorem 70.7, Corollary 70.8, (70.15)–(70.23): inversion-orbit definition of `K_a`, multiplicity rather than distinct-count budget, correction class `-g^{-1}`, exponent `1/2+1/(a-1)`, `a=3` emptiness, fixed-beta quantifier, lower-order ratio, hard progression, and nonuniformity in `a` agree.
- Standard Fact 70.2 and Theorem 70.9, (70.24)–(70.28): primitive affine forms/nonzero determinant, content removal, fixed-K exception handling, prime-density factor, effective upper law, sharper F3 upper law, fixed compatible progression extension, and **no matching prime-frame lower bound/asymptotic** all survive.
- Theorems 70.10–70.11, (70.29)–(70.35): maximal avoiding kernels of cyclic `2^k` quotients, exact character count, `2^(omega(a)-1)` quadratic term, unit compatibility, every fixed compatible hard-prime progression, and density-one success agree. The explicit `a=15`, `C_2 x C_4`, `C_2 x {0}` counterexample and its nonquadratic quotient are preserved. No composite extrapolation is promoted to a theorem.
- Computational 70.1 and (70.36): all subgroup counts, every unit/F1/F3/failure cell, `h<=20000` versus gated `200000`, first 200 versus 2000 hard primes, and maxima 23/63 agree. The computational-only status remains; defects 2–3 repair rendered prose, not these tables.
- Heuristic 70.1, (70.37)–(70.39), and the complete closing register retain the all-coefficient versus prime-only distinction, extra assumptions about constants and quasi-independence, fixed-only perimeter, falsification alternatives, no lower bound/uniformity/joint tail/pointwise nonemptiness, and no evidence claim.

### Source §71 → paper Section 33 (lines 10346–11093)

- Status, Lemmas 71.1–71.2, and (71.1)–(71.7): prime-only selection, unit hypothesis, sufficient-not-necessary confinement, explicit F3 expansion, one-excluded-class majorant, `p>3Z/2`, O(Z) omission, enlarged integer frame, covering-endpoint quantifier, and effective-if-effective reduction agree.
- Facts 71.1–71.3, Assessment 71.1, and (71.8)–(71.15a): Shiu pp. 162–163, Nair–Tenenbaum pp. 123–126, and Henriot pp. 4–8 retain their source quotations, ranges, dependencies, discriminant conditions, and prime-input `1/log x` factor. No growth rate for the hidden `C(J)` is asserted. This checks transcription against the notes, not fresh authentication of the archived articles.
- Theorem 71.3, Corollary 71.4, and (71.16)–(71.28): fixed finite set of J primes, primitive/content-free indicators, the separate prime-input proof, `N/log N` factor, exact discriminant penalties, and F1-only versus genuine first-witness bounds all agree. The six exact additional exponents are **1/2, 2/3, 23/30, 37/45, 859/990, 446/495**. The F1-intersection exponent remains `1+J/2`, not an all-failure bound. Inserting moving Z without uniform constants is expressly forbidden; unconditional results remain weaker than the standing literature.
- Lemma 71.5 and Heuristic 71.1, (71.29)–(71.36): collision/deletion sets, `ell>=5`, squarefree C, exact local factor and `3/5,2/3,7/10,9/13` examples agree. Local zero factors, distinct sparse toy model, prime-only exponent of order Z, and absence of tensorization are explicit.
- Both **open** hypotheses, Theorem 71.6's **proved implication**, Fact 71.4, Assessment 71.2, and (71.37)–(71.47): all uniformity/effectivity/normalization quantifiers, F3 inclusion, both hypotheses, gamma branches, favorable `K<1/(2 theta)` clause, dyadic scope, strict comparison thresholds, equality caveat, inherited **CLAIMED/PROVISIONAL** status, stronger endpoint-uniformity premise, and `Z>(4+o(1))log N` correction agree. The `1.274... x 10^6` finite crossover remains a caveated assessment.
- All four honest walls and both falsification tests survive, including the insufficiency of one unfavorable finite sample and the finite-only scope of block (br).

### Source §72 → paper Section 34 (lines 11095–11350)

- The entire section remains **Computational/INFO**, exact only in stated finite half-open ranges. Method, Python-integer arithmetic, prime-only F1/F3 taxonomy, assertions, checkpointing, and all replay scopes agree.
- (72.1)–(72.6): all four exact windows and populations `1031/1817/1561/1355`, all 40 compact-panel cells, six marginal counts in each dependence window, and all 30 joint/product/ratio cells agree. The dependence highlights `1.335/1.320`, `1.144/1.153`, and minimum `0.761` are unchanged and not independence claims. Defect 4 repairs only the prose rendering.
- (72.7)–(72.9): every one of the 20 histogram counts, total **719781**, restricted totals **9732/82887**, unique maximum **107 at 8803369**, new **79 at 66222601** and composite **91 at 22605361**, and every upper-tail prime agree.
- (72.10)–(72.11): all eight strict-record paths and every F1/F3/sigma entry, all 225 deep-prime counts, the complete aggregate ledger, and canonical SHA-256 agree. The full/deep pair counts **371903/1648**, F3 counts **5314/321**, percentages **1.429%/19.478%**, enrichment **13.63-fold**, and strict-record **35 F1/16 F3, 31.373%** now render completely with their INFO labels.
- (72.12): all eight rows and five omega cells, dash convention, exact-zero exception at 43, nonmonotone comparisons, and no-transition-law caveat agree after defect 6's repair.
- All scanner/suite timings, memory figures, 100 chunks, default versus `ES_FULL_SCAN=1` coverage, and the entire final no-uniformity/no-decorrelation/no-threshold/no-next-prime wall agree. In particular, block (bs) **pins**, rather than independently recomputes, the full `10^8` histogram; the full census replay and the block's gated `10^7` scope remain distinct.

## Three judgment calls

1. **(71.24) row terminator: approved.** Source header `J&\operatorname{factor}(D^*)&\Delta_{D^*}\ \hline` lacks the row terminator. Paper line 10749 uses `J&\operatorname{factor}(D^*)&\Delta_{D^*}\\ \hline`. It separates the header from the rule without changing any cell, fraction, exponent, or label. It is the sole substantive token-level difference in the normalized tagged-display comparison, and is a necessary typesetting repair, not new mathematics.
2. **Scaling: approved.** The seven sites are lines 10596, 10747, 10926, 11141, 11180, 11218, 11250: displays (71.15), (71.24), (71.38), (72.4), (72.6), (72.7), (72.10). Two are formulas rather than tables. All are `\resizebox{\textwidth}{!}` wrappers only; every mathematical/table token and external tag is retained. PDF text extraction confirms the scaled tables' content is present. No row is dropped or transformed into an unlabelled assertion.
3. **Reference mapping: approved.** At line 10294 the source §70.7's “correlation warning in §63.2” becomes “in Assessment 63.2.” The actual warning about the shared moving p is in notes §63.5, Assessment 63.2 (notes lines 24578–24594; paper lines 7867–7880); source subsection §63.2 is instead the universal bounded-coefficient law. The mapping repairs the locator without changing the warning or its Assessment status. Other theorem/section remappings were checked against their labelled targets, including provisional source Theorem 39.7 → `thm:three-quarter`.

## Global consistency and validation

- Abstract (lines 127–144), introduction (258–267), section map (349–357), status register (384–393), global pedigree (2492–2509), and final status (11964–11982) consistently distinguish fixed-a proved results, fixed-J unconditional means, both open moving-J hypotheses, and finite Computational/INFO evidence. The abstract's unit-domain omission is repaired, not excused by the later definition.
- The two **CLAIMED/PROVISIONAL** record headlines and every earlier status label remain unchanged. Inspection of the v16→v17 diff shows additions to the global summaries/pedigree and insertion of Sections 32–34, not promotions in prior mathematical sections. This review changes no earlier theorem or status label.
- Wave-30 **SOUND-AFTER-REPAIRS / SOUND-AFTER-REPAIRS / CONFIRMED-AFTER-REPAIRS** attestations match the recorded Outcome 34 pedigree, remain internal-only, and terminate at **(bs)**, not (bp). The source sections do not claim external validation.
- The tracked TOC correctly places Sections **32/33/34** at pages **143/153/163**, followed by Sections 35/36. It remains byte-identical after rebuilding; no artificial TOC change is needed.
- The requested two-pass `pdflatex -interaction=nonstopmode espaper.tex` build succeeds before and after repairs: **177 pages**, no TeX errors, no undefined references/citations. Existing font-substitution and duplicate-destination warnings are allowed and are not unresolved mathematical references. The repaired PDF is regenerated.
- Extracted PDF text confirms the unit condition, all repaired percentages, three local INFO labels, `13.63-fold`, and both nonmonotonicity comparisons. No unescaped percent sign remains in Sections 32–34. No census rerun or new analytic claim was used to substitute for fidelity checking.
