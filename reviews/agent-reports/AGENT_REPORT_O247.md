# AGENT_REPORT_O247 — Synthesis VII (cross-combinations of wave Z, (J)64–(J)77)

Branch side-agent/synthesis-seven. Deliverables: SYNTHESIS_SPARKS7.md (deep file), 8 memos BRAINSTORM/s7_*.md (indexed in
BRAINSTORM/README.md), scripts/s7_*. ES is not solved; no infinite case of ES at primes is claimed. One self-review pass
(reviewer subagent) was run and its repairs applied (marked "R-O247 review fix").

SHARP:
* **The binary-form (norm-form, degree-2) rung of the menu ladder collapses (PROVED, elementary; SYNTHESIS_SPARKS7 §1).**
  Thm 1.1: every polynomial Type II family (ET coordinates A, B, C, D ∈ ℚ[u, v]) for an irreducible binary quadratic form Q,
  valid at one point, has A, B, C, D ∈ ℚ[Q] — no cone, no definiteness. Thm 1.2: the same for Type I families valid on a coset
  in an open cone, at ANY level (C, D non-constant allowed). This answers negatively the open question of POINTWISE_BINARYFORM
  §5–6 / O145 (genuinely two-variable Type I families with non-constant level) on cones, and removes the hypotheses of its
  Prop 5.2. It closes the "norm-form data remain" hatch of (J)76 Prop 7.1 / MENU_STERILITY §5 for degree 2. Natural next
  target: degree-3 norm forms (the top-part step fails there).
* Parity law on r-generic lines (PROVED): the r-exponent c of a fixed-window witness is odd (Jacobi reciprocity) — the exact
  ℤ-twin of (J)67's root-product law, as (J)67's Assessment predicted.

## Answers to the mandatory items
(i) Forced budgets × primes. m₀(p) (least Type II window) is exactly the e-slice/B2 event on consecutive integers near p/4.
Mordell's theorem = "m₀ ∈ {3, 7} off the six classes mod 840" (PROVED, checked to 10⁷). A conditional permutation test finds
all inter-window correlation explained by shared small-prime (congruence) data (EVIDENCE, four shuffles). Records: m₀ ≤ 107
for p ≤ 10⁷. Explicit all-fail classes for windows ≤ 99 (CONDITIONAL on Dickson). Positive-density forced budgets exist only
at windows ≍ p (Gaussian K = S²; fires at random rate 10⁻⁴), and polynomial binary-form families collapse (Thm 1.1/1.2).
(ii) Certified caps (forced witness + forced small primes, PROVED per class): cap ≤ 1 on Haar ≈ 0.93–0.96 of the first undecided
line lnr = 17; but cap 0 already holds on Haar-almost all of it, and the forced mechanism is blind at the r-generic points.
(iii) No finite certificate for r = 17 obtained; fixed windows give explicit balls (incl. P-boxes), deep levels reduce to ES
solutions of 4/17^c (M17D wall); char-3 Frobenius is exactly critical (iterates approach the T1 point 1 at the same rate as
levels grow).
(iv) Over F_q[T], thin (nowhere-dense) menus cannot help an open covering problem (Baire); lifted Frobenius-digit identities are
Galois conjugation; general digit identities left open.
(v) Thm 1.1/1.2; enlarged T1 control set (non-squares with f_II = 0: 103 ≤ 2·10⁵, e.g. 3985 = 5·797; Lemma: Type II has
x ≤ n/2); L(1, χ_p) dictionary (Spearman 0.35).

## Self-review repairs (applied)
m₀ definition (Type I solutions can have p ∤ x; counterexample 4/16921); fixed-window balls are not M17's U-boxes (they include
P-boxes); digit map is continuous; Spearman ties (0.199 → 0.349); indefinite-form density caveat; softened "exactly / closed /
no certificate" wording.

## Files
SYNTHESIS_SPARKS7.md; BRAINSTORM/s7_{window_lottery, certified_caps, sibling_certificate, ff_nonlinear, normform_collapse,
gaussian_square_windows, lvalue_proxy, typeII_free_controls}.md; scripts/s7_{window_excess, window_shuffle, window_controls,
dickson_classes, cap_density, certified_cap, rgeneric_windows, window_mass, typeII_free, gauss_lvalue, normform_check}.py.
Reproduce: `PYTHONPATH=scripts uv run python scripts/s7_window_excess.py 1000000`, `s7_window_shuffle.py 1000000 47 4`,
`s7_window_controls.py 10000000 400`, `s7_normform_check.py` (all < 1 min).

## Sparks (not pursued)
* Degree-3 norm forms: does the Theorem 1.2 argument extend, or is this the first rung that does not collapse?
* Type I families near finitely many directions for indefinite forms (cusp regions).
* m₀ records vs extreme values of L(1, χ_p).
* Exact dictionary between fixed-window balls on r-generic lines and M17's P/Q/U box types.
