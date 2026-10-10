# AGENT REPORT O134 — paper write-up of the automorphic/geometric wave (I)

**Deliverable.** `paper/es-automorphic-barrier-note.tex` + `.pdf` (18 pp; pdflatex twice, 0 errors, 0 warnings,
0 overfull boxes). Title: "Automorphic and geometric reformulations of the Erdős–Straus equation, and a
divisor-class barrier". Entries: `paper/README.md` (top), one bullet in STATUS.md ("Papers in `paper/`").
Branch `side-agent/automorphic-note`, one commit per section.

**ES is not proved; the paper says so in the abstract, intro and summary.** No new mathematics was added. Every
item is taken from the reviewed sources ((I)1–(I)8), with the repairs those reviews made.

## Structure and labels
* §1 Intro: congruence-covering obstructions ([PO], POINTWISE_SIZE Thm C) leave only non-congruence input open.
  Explicit "what this note does not contain", the label convention, and a mechanism-scope disclaimer.
* §2 Dictionaries (PROVED). Lemma 2.2 (Type I three shapes + SL₂ matrix; full proof). Prop 2.3 (T_p Hecke identity;
  full proof). Prop 2.4 (wedge, Planck width). Lemma 2.5 (genus condition). Prop 2.6 (Type II: det-1 level dp,
  separation, Gram data / shell, genus lemma; proofs of (a), (c), (d)). Prop 2.7 (Brauer class = genus character;
  **marked folklore / Yamamoto via BL App. A, not new**). Prop 2.8 (B_{p,∞} order; **GZ x = 2 is a formal analogy
  only**). Lemma 2.9 ((−d,−p)). Prop 2.10 (CM torus). Prop 2.11 (Q_d). Novelty of the quaternion dictionary is
  stated as unverified.
* §3 Lemma 3.1 (slice table, full proof, plus the machine check) and Thm 3.2. (i) and (ii) are PROVED, (iii) is
  CONDITIONAL on H. Remark 3.3 gives the scope (aggregation over growing Θ(p) is NOT excluded).
* §4 Negative results:
  * Thm 4.2 (ternary; proof sketch faithful to O124 Prop 2.2/Lemma 2.1), including the O124 "thin piece" caution
    example;
  * Prop 4.4 (scale constraint, merged form of O127 Prop 2.3 + RT1 Prop 2.4 / §5.5);
  * Prop 4.5 (O127 Prop 7.3, local data of moderate modulus);
  * Prop 4.6 (thickening);
  * Prop 4.7 (Q₀ at odd squares; wording uses "locally soluble and globally soluble up to one sign", NOT
    "genus/spinor solubility", per R128b);
  * Thm 4.8 (only lines carry infinitely many integral points);
  * Prop 4.9 (BM-only ⟺ ES(n) for n ≥ 2; n = 1 sanity case, with BL Thm 1.8 / 1.1 distinction);
  * Props 4.10/4.11 (H- resp. Dickson-conditional empty single targets/shells).
* §5 Gaps (all Assessment): Young/Humphries/HR exponents, Type II gap D^{4/9} (D^{1/3} under GLH), polylog
  accuracy, termwise GRH (O127 Prop 9.1). Verdict Assessment 5.1, anchored at n_p.
* §6 Hatches H-A, H-B, H-D, H-E as Problems; H-F as a cautionary remark; H-C/H-G as non-escapes; symmetry remark.
* §7 EVIDENCE: numbers copied from the sources (f_I, f_II ≥ 1 for 5 ≤ p ≤ 10⁸; minima; fixed-level failure counts;
  slice drop at 5101441).

## Points for the referee
1. Brief's "(Prop 2.4 merged form)": I used RT1 §5.5's three-bullet merged statement; the bound (a) is ET Prop 1.7 as
   RT1 reads it, and I did not re-check it in ET.
2. Remark 3.3 cites the W(p) Ω-result to `es-subexp-note` and the Type I height result to POINTWISE_OMEGA Thm 8.5
   (modulo Lau–Wu), both as summarised in RT2 §2.2. Thm 4.2 and Prop 2.6(b) are proof sketches with pointers.
3. External bibliographic details are copied from LITERATURE_AUTOMORPHIC / other notes and were not re-verified
   here: Young JEMS 2017, Humphries Math. Ann. 2018 (volume/pages from memory, **please verify**), HR CPAM 2022, GS
   Invent. 2022, Lenstra 1984, DFI 1995, FI/HB/Maynard, Sarnak–Tsimerman. Yamamoto is marked "not accessed".
4. In §5 the statement "GRH gives n_p ≪ 𝓛²" is the classical Ankeny/Bach bound; I removed an unsupported
   O132 remark that "n_p ≤ 𝓛² is open under GRH".
5. Length is 18 pp, within the ≤ ~25 pp target.
