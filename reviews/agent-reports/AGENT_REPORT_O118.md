# AGENT_REPORT_O118 — paper update: unconditional result in es-typei-heegner-note

Branch `side-agent/heegner-note-v2`. Files: `paper/es-typei-heegner-note.tex` / `.pdf` (32 pp., two clean pdflatex
runs: no errors, no undefined refs, no overfull boxes), `paper/README.md`, `reviews/es-typei-heegner-note-referee.md`
("Post-referee addition (O118)").

## Changes
* **Title/abstract** rewritten. Theorem 1 is unconditional; Theorem 2 is (SEL)-or-(EFF) conditional. The abstract
  keeps the caveats: relative to cited inputs, internal review only.
* **Intro.** Thm 1 (= Thm 9.9(i), PROVED rel. DI Thm 7 + Drappeau Lemma 4.10): `≤ Cε₀N L² log L + O_{ε₀}(N L²)`.
  (SEL) is stated as before. (EFF) is described in words, with a forward reference to Hyp 9.8.
  Thm 2 (`≪ N L²`) holds under (SEL) (Thm 8.1) or under (EFF) (Thm 9.9(ii)). There is a new paragraph explaining the
  level-average remedy. The status paragraph lists the new cited inputs: DI Thm 7; Drappeau L4.10, uniform in q₀
  (our reading); and the residual spectrum of congruence groups (Iwaniec §11, Huxley 1984; locators unverified).
  Intro theorems are now numbered 1, 2 (`\arabic`).
* **New §9 "The exceptional spectrum on average over the level"** (write-up of EXCEPTIONAL_TYPEI_LOGLOG2):
  - DI Thm 7 is quoted verbatim from the scan p. 233, together with the Σ^{(q)} definition. The scan shows `√N X`;
    the paper notes Y = X² and the DI (8.18) misprint. Drappeau Lemma 4.10 is quoted verbatim from arXiv p. 16, with
    the definition of `E_{q,a}` (§4.2.3) and the setting (`N ≥ 1/2`, Prop 4.7).
  - Cor 9.1: prefix sums. Lemma 4.10 is applied directly to the sub-intervals `(2^{i−1}, min(2^i,t)]`, which uses
    the fact that Lemma 4.10 allows any interval inside (N,2N]; no prefix differences are needed.
  - Lemma 9.2: partial summation. Lemma 9.3: the shifted line `σ_j + 1/L`.
  - Prop 9.4: the d-averaged exceptional variance, with the n-dependent weight `w(t)`.
  - Remark 9.5: why the crude weight fails in case (iii), and why DI Thm 5/6 are insufficient.
  - Unconditional `V^gen` (9.1), Thm 9.6: averaged per-d count, Cor 9.7: cases (ii)–(iv) give `q²N^{−δ/4}`.
  - Hyp 9.8 (EFF) and Thm 9.9 (i)/(ii)/(iii), with full strip/ε₀ bookkeeping. Remark (D ≥ A never used SEL).
    Assessment 9.11 on effectivity. Remark 9.12 on MN4.
* **ε bookkeeping differs cosmetically from the source.** The source uses `ε = w/128` with `N^{4ε}`. The paper
  uses `ε = w/64` with `N^{2ε}`: `(M₀/λ₋)^{ε/2} ≤ N^{3ε/2}`. The exponent is the same `−11δ/64`. (iii) is then
  stated with `log G(64/w) ≤ wL/16`. I re-derived all three term computations of Thm 3.1 in the paper's notation.
* **§10** is renamed "Single-level exceptional estimates". It now only explains why single-level bounds leave a
  fixed-width strip, and points to §9. The old "no unconditional improvement" conclusion is removed.
* **Open problems.** "Unconditional removal" and "weighted exceptional density" are replaced by "effective constants
  (EFF)" and "quantified rate". The general-numerators problem now cites MN4 under (SEL_m).
* **Prop 5.1** no longer attributes "no nonconstant residual spectrum" to (SEL). The paragraph after it points to §9.
* **TTL (b3) erratum.** The paper already had `N^{−δ/4}` in case (iii). A parenthetical now records the source
  note's R117 erratum. New bib entries: TTL, TTL2, MN2, MN4, Hux.

## Points for the referee
1. **Residual spectrum without (SEL).** The source note did not discuss this, and the paper's old text attributed
   it to (SEL). I now cite it as a standard fact about congruence subgroups (Γ_{M,q} ⊇ Γ₁(M)). Please check the
   locator; Huxley 1984 was not accessed.
2. **Drappeau's q₀.** The paper applies Lemma 4.10 with `q₀ = q`, the modulus of χ, at the levels `4dq²`. This is
   uniform in q₀ only under our reading of his `≪_ε`.
3. **Cor 9.7 in case (ii).** It uses the paper's `(A/E)^{1/2} ≪ N^{δ/4}` for `k ≥ 2j`, and in case (iv) it uses
   `k' ≤ k/2`. It also relies on `F' ≤ 3A√D` in all three cases.
4. **Section 9 has not been reviewed as written.** Its mathematical source has had two reviews.

Status labels are unchanged from (D)32/(D)32a: Thm 1 is PROVED (relative to the cited inputs), Thm 2 is CONDITIONAL,
and (EFF) is an Assessment. ES is not claimed anywhere.
