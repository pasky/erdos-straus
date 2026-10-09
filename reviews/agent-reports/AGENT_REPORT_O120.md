# AGENT REPORT O120 — es-mn-short-note: sharp-order transition under SEL

Branch `side-agent/mn-note-sel`. Paper: `paper/es-mn-short-note.tex` (29 pp, two clean compiles: no warnings,
no undefined refs, no overfull boxes; 10 pre-existing underfull bibliography lines).

## Changes
* **New §9 "Under Selberg's eigenvalue conjecture"** (source EXCEPTIONAL_MN4.md, review R117):
  Def 9.1 (SEL_m) = MN4 §2.2; Thm 9.2 = MN4 Thm 4.1 (CONDITIONAL); Thm 9.3 = MN4 Thm 5.1 (conditional for
  m ≤ L⁵, PROVED for m > L⁵ via Thm L′ / Lemma 8.9; full proof written out); Cor 9.4 = MN4 Thm 5.2 (lower half
  CONDITIONAL, upper = Theorem U); proof *sketch* of Thm 9.2 with exact pointers to MN4 (Lemma 0.1, 1.1, §§2.1,
  2.2, 2.6, Lemma 6.1_m, Thm 6.2_m, §3, §3.2(c), §3.4, Thm 4.1) and to the Heegner note [HN] in its compiled
  numbering (Hyp 1.1, Lemmas 3.1–3.2, Prop 5.1, Thm 6.2, Prop 7.1, Lemma 8.1, Thm 8.2, Thm 9.9, §§9–10).
* **Remark 9.5 (unconditional transfer).** Checked: neither EXCEPTIONAL_MN4 nor EXCEPTIONAL_TYPEI_LOGLOG2 treats
  general m by the level-averaged (DI Thm 7 / Drappeau) route of (D)32a; MN4 §6 only records that the single-level
  Kim–Sarnak strip transfers unchanged. So the m-uniform unconditional analogue is stated as **open** (also in
  Problem 2). Added the (elementary) observation that even such a transfer gives only an unquantified o(1) gain
  over Thm L′; an m-uniform (EFF) version would make Cor 9.4(a) conditional on (EFF) instead of SEL_m.
* Remark 8.10 rewritten (extension now done → §9); §8.4 gap paragraph; abstract (conditional sharp order + status
  sentence; "every unconditional result except…"); intro paragraph after Thm L′; status/novelty; organisation;
  Problem 2 labelled and updated. Bib: [HN], [MN4].
* `reviews/es-mn-short-note-referee.md`: "Post-referee addition (O120)". `paper/README.md` updated.

## Points for the referee
* Thm 9.2 statement carries MN4's attribution "relative to inputs of [HN, Thm 8.2] and MN3"; MN4 used TTL
  numbering — I mapped TTL Prop 5.1/Thm 6.2/Prop 7.1/Lemma 1.1/Thm 8.1 to HN Prop 5.1/Thm 6.2/Prop 7.1/Lemma 8.1/
  Thm 8.2 by label names in the HN source (labels L:5.1, L:6.2, L:7.1, L:1.1, L:8.1); worth a spot check.
* Claim "(SEL_4) is exactly HN Hyp 1.1": MN4 (q,2md)=1 squarefree, χ even mod q vs HN q odd squarefree,
  (q,d)=1, χ even mod 2q; I read these as identical families.
* No new mathematics beyond the case analysis of Thm 9.3 (copied from MN4 Thm 5.1, adapted to the paper's
  Prop 8.5 / Lemma 8.9 / Thm L′).
