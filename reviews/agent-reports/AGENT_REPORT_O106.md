# AGENT REPORT O106 — es-coverings-note update (2026-10-08/09 results)

Branch `side-agent/coverings-note-v3`. Paper: `paper/es-coverings-note.tex` / `.pdf`, 25 → 29 pp (+4, the cap).
Build: two pdflatex passes, 0 overfull boxes, 0 undefined references/citations; remaining: the pre-existing underfull
hbox in Prop 6.2 ("Put") and one underfull vbox at a page break.

## What was added (all from merged + reviewed sources; labels/engine scopes as there)
* §4.6 (TYPEI6, review R99): Prop 4.17 (PROVED, sketch) no norm-one polynomial unit in δ (or c_o) for L ≥ 7; Schinzel
  period criterion cited (via van der Poorten, as in source); TYPEI6 Lemma 3.1 inequality Y > 64c_o⁴δ⁸/T⁴ in regime (v)
  (PROVED) + "generic large-unit regime" (Assessment); Thm 4.18 (CONDITIONAL on abc; finiteness per level only; explicit
  abc forms do not give emptiness, Assessment); Comp 4.19 (CERTIFIED: L = 7–10, v_7(k) ≤ 15, any height; two engines
  except (9,15), (10,14), (10,15)); so v_7(k) ≥ 16 and c_oδ > 10⁶ remain; naive model < 10⁻¹¹ (EVIDENCE).
  TYPEI5 (Lemma 1.1, Thm 3.7) was already in the paper (Prop 4.15, Thm 4.16) — unchanged.
* §5 (MORDELL13C, review R100): Thm 5.2 (PROVED by finite computation; 35459 open classes, 8.42·10⁻⁵ of the six classes,
  three checkers; no class closes); witness-engine EVIDENCE 1399/1499/1412; Comp 5.6 extended (II3/I3/I1/II2 to 2·10⁹,
  I2/II1/I4 to 2·10⁸, one engine; caps vacuous); "Data" paragraph: Comp 3.1 (CERTIFIED: (2,2) cell at 11²13² exactly
  {2,57,79}×{15,28,54,132,145}); only class 473761 has known uncovered T-generic points (EVIDENCE).
* §6 (MORDELL17B/17C, reviews R93/R98b): D_P(11) = 836, D_P(13) = 1463 (CERTIFIED, two engines); ρ₁ = 16344335/24137569;
  Thm 6.7 (PROVED reduction, cumulative hypothesis via Abel summation; C ≤ 1.497 at θ = 2/5; pointwise 1.409);
  Conj 4.2 of 17B (D_P ≤ K⁵ etc., CONJECTURE); Q large-c bound (PROVED, cost 4.3·10⁻³); Assessment 6.8 extended by the
  discrete-log window obstruction (PROVED class structure; EVIDENCE E_∞ ≈ B(log B)^{0.4–0.5}; θ ≈ 1 for dlog-blind arguments).
  The old "constant 1 leaves 0.84" sentence is kept but marked as the crude Thm 6.4 form, pointing to Thm 6.7.
* Abstract, intro Results (r = 7, 13, 17), Problems 2 and 4, date, acknowledgements, bibliography (PT6, PM13C, PM17B, PM17C).
* `reviews/es-coverings-note-referee.md`: "Post-referee addition (O106)" with numbering shifts; `paper/README.md` updated.

## Points for the parent's review
* Thm 6.7 uses 1.411·10⁻³ (strict upper bound for T_Q = 1.4106·10⁻³) and the factor 32/17 = 2·16/17; check against
  17C Lemma 1.1 / table (1.497 is the floor-rounded cumulative threshold there; not recomputed by me).
* Thm 4.18's sketch compresses TYPEI6 Thm 3.2; "the other regimes and the case 2y > T7^b are finite" cites TYPEI5 Prop 3.3
  and TYPEI6 §3 (case A for general L is TYPEI6's R99 D1 repair).
* No new mathematics, no new computations; nothing re-run except LaTeX.
