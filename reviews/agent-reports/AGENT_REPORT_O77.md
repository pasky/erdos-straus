# AGENT_REPORT_O77 — `paper/es-subexp-note.tex` v6 (branch `side-agent/subexp-paper-v6`)

Status: checkpoint 1 (all deliverables written, compiled, committed). Not merged.

Compile: `pdflatex` ×2 on the branch — 61 pp., 0 undefined references, 0 overfull boxes.

Sources: `POINTWISE_TAIL.md` (ledger (H)33, review R76), `POINTWISE_MN.md` / `POINTWISE_MN2.md`
((H)32, reviews R63/R74), `reviews/novelty-audit-2026-10b.md` and the (H)25–(H)27 updates.
§§2–11 and §§13–14 (old §§12–13) mathematically unchanged.

## Numbering changes (for cross-checking against R64)
* New intro Theorem 1.3 (tail); old Thms 1.3–1.5 are now 1.4–1.6.
* New §12 "The distribution of W over primes"; old §12 (Wiener) → §13, old §13 (LS) → §14.
* New §15 "Other numerators m/n"; Summary of status → §16.

## Change list for the referee

**C1 (§12, new; source POINTWISE_TAIL §§1–3).**
* Thm 12.1 (lower tail): `N_h(x,T) ≥ π(x)exp(−C𝓛³(log𝓛)³)` for `log x ≥ C𝓛⁴log𝓛`. Label: proved modulo
  Thms G (incl. Landau–Page 6.1) and NT. (Source label adds OMEGA10 Thm 3.4 = the energy bound, proved
  in this paper, §7, so it disappears from the label.)
* Cor 12.2 (= intro Thm 1.3): `c𝓛³ ≤ log(π(x)/N(x,T)) ≤ C𝓛³(log𝓛)³` for `𝓛 ≤ c'(log x/loglog x)^{1/4}`;
  label adds [TQ] and Page (from Thm 11.2). Range constants `c' ≤ min(1,c₁,(4/C)^{1/4})` as in R76 D2.
* Lemma 12.3 (quantitative transfer) = TAIL Lemma 1.1, written as a reading of the proof of Thm 6.1
  (paper's own case structure: Case 0 / exceptional χ_1 not in support / Case B / Case A).
  Deviations from the source: λ written with the paper's Landau–Page constant,
  `λ = min(1, 8c₂^{-1}q₁^{-1/2}(log q₁)^{-2})` (source: `c_P = 16c'`, `log 3q₁`); check
  `0.98·min(u,1)/2 ≥ λ/3` with `u ≥ 16c₂^{-1}q₁^{-1/2}(log q₁)^{-2}`. No extra `B ≤ 1` hypothesis is needed
  (the hypothesis `B ≤ 1[W>T]` on `n ≡ r`, coprime to the d_i, already gives it at the counted primes).
* One-fibre paragraph (TAIL Thm 2.1, exponent `(log𝓛)^5`) given as a remark-paragraph, not a theorem.
* Lemma 12.4 (leaves, `P_proc(L) = 4·2^{k_L}/φ(Q_L)`, disjoint fibres) = TAIL Lemma 3.1, full proof.
* Lemma 12.5 = TAIL Lemmas 3.2 and 3.2′ (R76 S1) in one statement, with the NT-twist arguments.
  Deviations: rad includes the prime 2 (constant `log 210` instead of `log 105`; harmless);
  `ω_Y ≤ (1+loglogY)t^{ω_Y}` uses `1/log t ≤ t/(t−1)`; class constant for the rad-twist stated as
  `6e < 17` (source: A = 12; any absolute A works).
* Proof of Thm 12.1 = TAIL Thm 3.3 proof (good leaves (i)–(v), `P(good) ≥ 1/4`, sum over leaves).
  Deviation (deliberate): the source says "the exceptional zero of (G) depends only on x"; in the paper
  `Q_G = x^{1/(κL)}` with `L` depending on `A`, which may differ between leaves, so I removed the claim;
  the proof only needs `q₁ | Q_L ⇒ q₁ ≤ 8·rad(Q_L)` for whatever exceptional character occurs in that
  leaf's application. Please check this is sufficient.
* Remark 12.6: losses (Assessment) + conditional improvement `(log𝓛)²logloglog` under
  `1−β ≥ c₀/log q` for real zeros (R76 D4), labelled conditional.
* Paragraph after Cor 12.2: range gap `(loglog x)^{1/4}` (Assessment via Prop 11.3), and ET Remark 1.2.

**C2 (§11, paragraph after Thm 11.2).** The v5 sentence "We expect (Assessment, not checked) that a
matching lower bound … we have not pursued this" is replaced by a pointer to Thm 12.1.

**C3 (§15, new; sources POINTWISE_MN, MN2).**
* Setting: identity (15.1) for `m/n`, `R_m(M)`, `W_m`, `δ*_m`, Type-II-hard; explicit scope sentence
  (family (15.1) only; nothing on ES/Sierpiński).
* Lemma 15.1 (Jacobi dichotomy) = MN Lemma 1.1, **full proof**.
* Prop 15.2 (square classes fire for `m ≢ 0 (4)`) = MN Prop 2.1, **full proof**.
* Thm 15.3 (`m ≡ 0 (4)`: Haar exponent 3, exponent 1/4) = MN Thm 3.1; label "proved in [MN] modulo
  G, NT (+ fundamental lemma for the lower bound)"; substitution proof summarised (items (1)–(5)).
* Prop 15.4 (Haar lower bound every m) = MN Prop 3.2, summary.
* Thm 15.5 (every m, exponent 1/5, mod G + ET Prop 1.4/Thm 7.1/Cor 7.4/(7.10)) = MN Cor 6.1, substitution
  list (MN §6b, the R63 MAJOR-1 repair) summarised; output primes `≡ 1 (Q)`, Type-II-hard only.
* Lemma 15.6 (transfer for arbitrary r) = MN Lemma 4.1, **full proof** (as a modification of the proof
  of Thm 6.1).
* ADM_m (definition), Thm 15.7 (conditional on ADM_m) = MN Thm 5.1; MN2 Lemma 1.1 (any `s₀ > 0`);
  "Towards ADM_m" paragraph: MN §6 numerics (Evidence), MN2 Thm 3.1 (mod Henriot Thm 5, checked to
  exist in `sources/henriot-1102.1643.pdf`), SI ⇒ ADM_m (MN2 Prop 5.1), SI a conjecture, prefix
  circularity an Assessment (MN2 §4, R74 D3/D4 wording kept: "does not obviously close").
* New bib entries [MN], [MN2] (working notes, internally reviewed).

**C4 (abstract, intro).** Abstract: two-sided tail sentence and an m/n sentence (with "proved in
internally reviewed working notes and summarised here"). Intro: Thm 1.3 + paragraph; "Altogether"
sentence updated; new paragraph "Other numerators"; "Versions" paragraph adds v6; date "Draft v6".

**C5 (Relation to the literature, per audit 10b).**
* β-weighted LLL: "standard per-coordinate form of the asymmetric LLL … we claim no novelty; the
  point specific to this note is β = 1+1/log𝓛" (audit §3).
* Janson-type inequality: "routine combination of Boppana–Spencer with the HSS inflation bound;
  Lu–Székely closest suspected prior art, unchecked" (audit §2).
* Planting lemma: explicit comparison with BGP Thm 27 — `n_c(k,p) ≤ (k+1)p/(1−p)+2k+2`, removes the
  `log(1/(1−p))` factor and the prime-power restriction, within ≈2 of BGP's lower bound; later
  literature unchecked (audit §4, (H)27 update). The v5 "we claim no novelty" is replaced.
* Transfer theorem: "convenient packaging of Gallagher's proof of Linnik's theorem, not a new transfer
  principle" (audit §5).
* New paragraph "The exponent 3": ET Remark 1.2 (heuristic `1−O(exp(−c log³p))`) anticipates the exponent;
  Thm 1.4 is its rigorous profinite version (new: the lower bound / exactness up to logs); Thm 11.2 is
  Vaughan's method applied to W (audit §6, (H)25 update); Mordell's qualitative obstruction vs
  Lemmas 3.2/15.1. I did not add Yamamoto / Fridlender / Graham–Ringrose / Granville–Pomerance citations
  (not in the bibliography and not verified; audit §6 suggests them — referee may want them).

**C6 (status conventions, §16).** Working notes [MN, MN2] added; ET and Henriot enter §15; §16 lists
all new items with labels; "Not claimed" adds Sierpiński, representations outside (15.1), ADM_m, SI;
"ET … no longer used" corrected (ET enters Thm 15.5).

**C7 (`paper/README.md`).** v6 entry.

## Points I would like the referee to check
1. Lemma 12.3: that every case of the proof of Thm 6.1 indeed yields `S(x) ≥ λμx/(3φ(Q))` with the stated λ
   (in particular the "exceptional χ₁ not in the support" case and Case B).
2. Proof of Thm 12.1: uniformity of `C₃` over good leaves (τ built from `S₁ = 2C𝓛³log𝓛`), and the removal
   of the "exceptional zero depends only on x" sentence (C1).
3. Lemma 12.5: the NT class conditions for the twisted `f₂` and the Euler-ratio bounds.
4. §15 summaries: that "proved in [MN]" labels are not stronger than MN/MN2's own labels.

## Self-review (reviewer subagent, deep mode) and repairs
Verdict: Lemmas 12.3–12.5, Thm 12.1, Lemma 15.1, Prop 15.2, Lemma 15.6 sound; leaf-dependent
exceptional character harmless; no ES/Sierpiński claim. Four defects, all repaired:
* SR1 (§15 "Towards ADM_m"): MN2 Thm 3.1 is for the *ordered* process (prefix, forced stage A in
  increasing prime-power order up to `Z = 𝓛³(log𝓛)^B`, then adaptive stage B, stopped before
  `Λ > K`), not for the adaptive process as defined. Now described explicitly.
* SR2 (Thm 15.7 summary): for odd m the forms `n, mn−1` have the fixed prime divisor 2, so NT does
  not apply verbatim; parity split (`t, 2mt−1` / `2t+1, mt+(m−1)/2`) added, flagged as **not written
  out in [MN]** (an inherited gap in MN §5; affects only the conditional Thm 15.7 for odd m; Thm 15.3
  has m even). The parent may want this repaired in POINTWISE_MN.md as well.
* SR3: "Only atoms with M ≡ 7 (8) are never fired" overstated; now "sufficient, not necessary"
  (example m = 5, M = 19, D = 1).
* SR4: planting vs BGP: "within a factor 3 of their lower bound (about 2 as p → 1)" (at p = 1/2:
  3k+3 vs k+1).
