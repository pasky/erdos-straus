# AGENT REPORT O122 — es-typei-heegner-note v3: the bound becomes unconditional

Branch `side-agent/heegner-note-v3`. Paper: `paper/es-typei-heegner-note.tex` / `.pdf`, **38 pp** (was 32). Two clean
pdflatex runs: no errors, no undefined references, no overfull boxes.

## Changes
* **Title/abstract:** "The Elsholtz–Tao Type I sum is O(N log²N)". The abstract states the result, the method, the
  effective DI7/Drappeau input with its repairs and nebentypus branch, the weaker o(·) and SEL variants, the
  dependence on classical inputs, and "reviewed internally only; needs expert scrutiny".
* **Intro:** Theorem 1 (`thm:main`) is `Σ_{p≤N} f_I(p) ≪ N log²N`, hence ≍ by ET's lower bound. It is PROVED
  relative to the cited inputs and (B1)–(B5), which are listed explicitly in the intro. Theorem 2 (`thm:uncond`)
  is the o(N log²N log log N) bound that uses only the *published* DI Thm 7 / Dr Lemma 4.10 (no appendix). The SEL
  route (Thm 8.2) is kept as an unnumbered restatement and alternative proof. There is a new paragraph sketching
  the appendix. "Status and dependencies" was rewritten: what each theorem uses, the review history of
  Appendix A, and that shape-checked majorants affect only the numerical A₀.
* **§9:** Hypothesis (EFF) became Theorem 9.8 (same number, label `hyp:eff` kept), proved by Appendix A. Thm 9.9(ii)
  is now PROVED. The Assessment became Remark 9.11 (history; mentions the small-C branch found later). The §9 intro
  and the end-of-§9 remark were adjusted.
* **New Appendix A** "Effective versions of DI Theorem 7 and Drappeau Lemma 4.10" (source EXCEPTIONAL_TYPEI_LOGLOG3):
  Thm A.1 (C_ε ≤ 200ε⁻¹K₇^χ(ε/6) ≤ exp(exp(A₀/ε)), explicit A₀ formula); black boxes (B1)–(B5); Lemma A.2
  (toolkit: divisor bound, log absorption, Gevrey-2 cutoff); (M), (PS), (P1)–(P3); Prop A.3 (effective (8.19)
  *with nebentypus small-C branch (C2)*, full proof); Thm A.4 (effective Thm 7 / Lemma 4.10 + growth); Props A.5–A.7
  (effective Thm 2, Thm 14, Lemma 8.1: statement, key mechanisms, precise pointers to `scripts/ttl3_*.md`); proof of
  Thm A.1 (constants and conversion to Cor 9.1); §A.6 the list of corrections to DI/Drappeau (six items, as in the
  source and the derivation files); §A.7 status (re-derived vs only shape-checked). Bib: [TTL3].
* **§10 / open problems:** Problem 1 is now independent verification plus a numerical A₀ (shape-checked majorants,
  certified C_W, B_W). Problem 2 is now the asymptotic `~ c_I N log²N` plus other routes. The m/n problem was
  updated: an m-uniform version would need §9 at levels mdq² plus Appendix A.
* Referee file `reviews/es-typei-heegner-note-referee-r2.md` has a "Post-referee addition (O122)" section;
  `paper/README.md` and the STATUS.md paper bullet were updated.

## Collateral fix (please check)
`paper/README.md` was **empty (0 bytes) on main**: the O120 commit cd68eb7 deleted all 548 lines (its report says
"README updated"). I restored it from cd68eb7^ and added a short O120 entry (separate commit 2nd on this branch).

## Numbering
All theorem numbers cited by the MN note ([HN] in es-mn-short-note: Hyp 1.1, Lemmas 3.1–3.2, Prop 5.1, Thm 6.2,
Prop 7.1, Lemma 8.1, Thm 8.2, Thm 9.9, §§9–10) are unchanged. I checked them against the v2 .aux. (EFF) keeps the
number 9.8 and E:ass keeps 9.11.

## For the referee
* Appendix A writes out complete proofs only for the induction and its nebentypus branch (Prop A.3, Thm A.4), the
  toolkit, and the assembly. Props A.5–A.7 are statements with mechanism summaries and pointers. Their proofs live
  in the derivation files, as in the source.
* (B3) constants are not certified. A₀ is numeric only modulo the shape-checked majorants. The form of the bound
  and Theorem 1 do not depend on either.
* The application only uses even χ. Thm A.1/Thm 9.8 are stated for even χ. Cor 9.1's statement still says "a
  character modulo q₀" (as Drappeau's lemma is cited for general χ).
* Theorem A.4's growth claim with H including 200cK₁ follows the source's "as in Cor 2.3" (not re-derived here).
* Not done: no re-derivation of the ttl3 computations (out of scope; reviewed in R121A/B).

Stopping here for the referee.
