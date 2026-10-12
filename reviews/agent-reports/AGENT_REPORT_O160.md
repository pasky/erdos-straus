# AGENT REPORT O160 — errata + index for the BRAINSTORM/ phase

Branch `side-agent/brainstorm-errata`. Hygiene task only. No new mathematics is claimed. ES is not solved.

## Deliverables
1. **`BRAINSTORM/README.md`**: an index of all 51 memos (24 in half A, 27 in half B). Columns: file · task · angle ·
   memo verdict · triage validity · calibrated verdict (half B) · promise · hatch · by-products with labels · errata
   flag.
   * Triage B §0.1 is applied. Every DISAGREE (9 memos), and every PARTIAL where triage says the "COLLAPSES" wording
     overreaches, now reads "PARTIAL → H-x (displayed instantiation collapses)".
   * The table header records the recommendation's basis: the narrow scopes of Thm 2.2(iii), CONDITIONAL_ES
     Prop 2.3, PIGEONHOLE Thm 2.2 and FIBRED Thm 3.1.
   * The README also contains the brief-template error note and a script-fix section.
2. **Errata sections**: `## Errata (triage O156/O157)` is appended at the end of **32 memos**. Memo bodies are not
   edited.
   * 26 memos come from half B. They cover every row of the triage-B §0.3 table, plus concrete errors from the
     per-memo paragraphs:
     * corr_parity §1 partition overlap;
     * tech_smooth BFI/Zhang conflation;
     * the adv_stacked SE/duplicate-prime notes;
     * thin_group, tropical, other_rings, logic_ominimal, logic_complexity and logic_weak_arithmetic scope fixes.
   * 6 memos come from half A, covering the full "overclaims" list: anal_dirichlet A.2, gon_lll label, ident_invariants
     scope, hardness_law exponent, elliptic under-claim, and the ff B3 screen statement.
   * The README ✓ column matches the set of files that have an Errata section. I checked this mechanically.
3. **`scripts/errata_check.py`**: 17 checks, under 1 min, and all pass. Each computational counterexample is
   re-verified independently:
   * D3 (p=433, e=19), including the corrected prime-N rule "X_e > 0 ⇔ N ≡ −1 (e)". This rule was checked on all
     15 181 prime-N_e cases with p < 2·10⁴ and e < 200.
   * the frame (p=73), including a brute-forced correct equivalence "4AB | p+A+B ⇔ B | p+A ∧ 4A | (p+A+B)/B";
   * item 13 (the ratio set {1,2,7,8,11,13} misses −1, yet 2²·11 ≡ −1 mod 15);
   * LGP (d=9 and d=1);
   * A₅ (45 of 60 elements are squares), and the Type I congruence p ≡ −e⁻¹ (p=13, e=3, ℓ=5);
   * U_n point counts in characteristic 2 (F₂, F₄), with Prop 3.1 confirmed at q = 3, 5, 7;
   * H1 ⇒ Type I (3,6,14) at p=7;
   * Prop B: 38 primes p_k ≡ −7 mod 2^k, plus 4/9 = 1/3+1/12+1/36;
   * the F₅[T] square counterexample (sympy);
   * q = xy rounding;
   * the LLL toy example;
   * the lottery double count;
   * W1 (h(−76) = 3);
   * F5's d ≤ (p+2)/4;
   * Q = 4;
   * the corr_parity overlap.

   Non-computational errata (citation and scope errors) are marked as such in their headers.

## Script defects (3)
* **`bs_adv_count.c`.** Solutions found in part B did not update `emin` or `Xsmall`.
  * Symptom: `emin` was reported as 0 when all slices e ≤ E were empty, and X_e for E < e ≤ 31 was dropped when
    E < 31. Example: p=433, E=3 gave `emin 0`; it now gives `emin 7`, and its X_e row matches the E=1000 run.
  * Fixed and annotated. The f_II totals were always correct.
  * No O154 data are affected: all 351 log records use the default E ≈ 2√p and have part A > 0.
* **`bs_adv_drivers.py:60`.**
  * Renamed the feature to `log (p-1)_{100-smooth part}`, which is what it computes. Added a correct
    `log tau((p-1)_{100-smooth part})`.
  * Re-ran it (≈ 2 min, 1 core, 8 GB ulimit). Every other number in the memo reproduces exactly.
  * The corrected feature has corr −0.322 and partial corr −0.038 (the mislabelled one: −0.263 / −0.060).
  * Substituting it into stage 2 gives R² 0.457 (was 0.458), and the global partial correlations stay at
    +0.003 / −0.009 / −0.010.
  * **No conclusion changes.** Both features are congruence data at prime powers. `prob_lottery_model.md` does not
    use this feature.
  * The erratum is in `adv_new_drivers.md`.
* **Brief-template B2 error** (Σ_{p≤N} f(p) ≍ N log³N should be N log²N over primes). Status by memo:
  * The wrong form appears explicitly in `tech_maynard_theta.md` §2 (erratum added).
  * `nonab_homogeneous_dynamics.md` l.46 is ambiguous: no range is given, so it is correct only over integers n
    (noted in its erratum).
  * The correct form is used in `adv_stacked_primes`, `prob_lottery_model`, `anal_dirichlet_series`, `addcomb` and
    `cayley_markoff_cm`.
  * The template in `/tmp/es-briefs/*` still carries the wrong form. That is a parent-side fix.

## Judgement calls for the parent to check
* **Hatch assignment** is my reading of the triage text, and it is not always unique. Examples:
  * tech_maynard: H-A or H-B;
  * the windmill / form-family identities: assigned H-E (the O132 "exact identity" hatch);
  * rational_to_integral, markoff, thin, tropical and padic_adelic: assigned H-F, read as "integral geometry beyond
    BM", following triage B §0.1.
* **Corrected item-13 statement.** I rewrote the triage's "divisor ≡ −1" phrasing as "−1 ∉ {a·b⁻¹ : ab | N}", the
  PIGEONHOLE Lemma 1.1 ratio-set form. This is what the triage's {1,2,7,8,11,13} set actually is.
* **logic_weak_arithmetic C4 counter-model** (from triage) is quoted without a machine check, because it is
  model-theoretic.
