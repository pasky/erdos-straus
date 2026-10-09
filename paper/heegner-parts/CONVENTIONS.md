# Conventions for paper/es-typei-heegner-note.tex (task O114)

Fragments: paper/heegner-parts/partA.tex (§§1–3), partB.tex (§§4–6), partC.tex (§§7–10),
bibliography entries in bibA.tex / bibB.tex / bibC.tex (plain `\bibitem[KEY]{KEY} ...` lines only).
Fragments contain only body text starting with `\section{...}`; no preamble. The master file
`paper/es-typei-heegner-note.tex` holds the preamble (copy below) and is assembled by the parent agent.

## Sections and section labels
1 Introduction `sec:intro` (A) — 2 The Type I sum and the bad region `sec:reduction` (A) —
3 SL_2 / Heegner reformulation and separation `sec:heegner` (A) — 4 Sobolev duality `sec:sobolev` (B) —
5 The spectral large sieve and the variance of box Poincaré series `sec:sieve` (B) —
6 Per-d counts `sec:perd` (B) — 7 The per-a Weil count `sec:pera` (C) — 8 Assembly `sec:assembly` (C) —
9 What is unconditional `sec:uncond` (C) — 10 Open problems `sec:open` (C).

## Result labels (cross-references between fragments)
Every result taken from EXCEPTIONAL_TYPEI_LOGLOG.md numbered x.y gets label `L:x.y` (e.g. Lemma 2.2 →
`\label{L:2.2}`, Theorem 8.1 → `L:8.1`, Lemma 1.1 → `L:1.1`, Prop 5.1 → `L:5.1`, Theorem 6.2 → `L:6.2`,
Prop 7.1 → `L:7.1`, Lemmas 8.2–8.4 → `L:8.2`… ). Results from EXCEPTIONAL_MN3.md numbered x.y get `M:x.y`
(Lemma 3.1 → `M:3.1`, Lemma 3.2 → `M:3.2`, Prop 3.3 → `M:3.3`, Thm 3.8 → `M:3.8`, Prop 2.3 → `M:2.3`).
The fragment that *states* the result defines the label; others just `\ref` it. Location of each:
L:1.1 in §8 (C); M:2.3, M:3.1, M:3.2, M:3.3, M:3.8, L:8.2, L:8.3, L:8.4 in §2 (A) [8.0 BT-outside material
belongs to the reduction section]; L:2.1, L:2.2 in §3 (A); L:4.1–L:4.4 in §4 (B); L:5.1 (and any spectral
input statements) in §5 (B); L:6.1–L:6.3 in §6 (B); L:7.1 in §7 (C); L:8.1 in §8 (C).
Main theorem in the introduction: `\begin{introthm}\label{thm:main}` (Theorem A), equals L:8.1.
The hypothesis: `\label{hyp:sel}` — a displayed named hypothesis (SEL) stated in §1 (A) by
`\begin{hypothesis}[SEL]` ... ; refer to it as (SEL).
New labels inside a fragment: prefix with the part letter, e.g. `A:eq:weight`, `B:lem:kernel`.

## Notation (use exactly)
`N` large, `\mathcal L = \log N` written `\cL`; primes `p\le N`; `f_I(p)` = ET's Type I count;
w_c-tuple `(c,a,d,f)`, `e=(4a^2d+1)/f`, `b=ce-a`, `n=4acd-f`; exponents `a=N^\alpha`, `c=N^\gamma`,
`b=N^\beta`; Heegner forms `\cF_d`; points `w_Q`; `\Gamma_0(M)`, `M=4dq^2`; hyperbolic plane `\HH`;
Laplacian `\Delta`; `\langle\cdot\rangle` mean over the fundamental domain; `\mu` measure; `g(x)=x/\varphi(x)`.
Macros available (defined in preamble): \Z \N \Q \R \C \HH \cL \cF \cS \Gam (=\Gamma) \SL \PSL \ind \e
\vol \disc \lcm \status{...} (small caps label, e.g. \status{proved}, \status{conditional}).
Theorem environments: theorem, lemma, proposition, corollary, definition, remark, assessment, hypothesis,
problem, introthm (lettered), conjecture.

## Citation keys (use these; add new ones in your bib file with the same key style)
ET (Elsholtz–Tao, Counting the number of solutions to the Erdős–Straus equation on unit fractions,
J. Aust. Math. Soc. 94 (2013) 50–105, arXiv:1107.1010), DI (Deshouillers–Iwaniec, Kloosterman sums and
Fourier coefficients of cusp forms, Invent. Math. 70 (1982) 219–288), Dr (Drappeau, Sums of Kloosterman
sums in arithmetic progressions, and the error term in the dispersion method, Proc. LMS 114 (2017)
684–732, arXiv:1504.05549), KS (Kim–Sarnak, appendix to Kim, JAMS 16 (2003)), Sel (Selberg 1965),
Iw (Iwaniec, Spectral methods of automorphic forms, 2nd ed., AMS 2002), IK (Iwaniec–Kowalski 2004),
MV (Montgomery–Vaughan, The large sieve, Mathematika 20 (1973) — Brun–Titchmarsh), Weil (Weil 1948),
Jia (Jia, Sci. China Math. 55 (2012) 465–474), LMY (Liu–Masri–Young), Duke (Duke, Invent. Math. 92
(1988)), MN3 (internal: EXCEPTIONAL_MN3.md, cite as "internal note"), Shiu (Shiu 1980), PV (Pólya–Vinogradov,
cite IK). Verify bibliographic data you add; if unsure, give less detail rather than wrong detail.

## Status discipline
Labels: \status{proved}, \status{conditional} (on (SEL)), \status{evidence}, Assessment. The main theorem
is CONDITIONAL on (SEL) and proved relative to cited results; internal review only (R111 rounds 1–2);
the inherited ET / MN3 reduction steps were not re-checked by the R111 reviewer (MN3 had its own review
R108). Never claim ES or OPEN-I unconditionally. No unconditional improvement of ET from this method.
