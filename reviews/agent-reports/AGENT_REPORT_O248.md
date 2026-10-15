# AGENT_REPORT_O248 — cubic norm-form rung (spark relay Z13)

**SHARP:**
1. **Type I unit-group criterion (PROVED, NORMFORM_CUBIC Thm 3.1).** Writing Type I as C(4ABD − 1) = P(A + B): if P is prime in
   ℚ[x] and ℚ[x]/(P) has only constant units (every homogeneous prime form), every polynomial Type I family valid at ONE
   point is in ℚ[P] (the only other solution is an explicit never-valid family). No cone, no positivity region, no Hecke.
   Together with Type II (Thm 1.1′): **every polynomial ET family for any norm form (any degree, any signature) or any
   irreducible binary form, valid anywhere, is an ET identity in n.** Closes POINTWISE_BINARYFORM §4.3 (indefinite cusps)
   for ET families. Dictionary (Assessment): non-collapsing Type I families need units of the zero-fibre algebra ℚ[x]/(P) —
   for one-variable menus this is exactly MENU_STERILITY Thm A's algebra ℚ[u]/(φ).
2. **The "degree-3 step fails" remark of SYNTHESIS_SPARKS7 Cor 1.3 is wrong** (§1): Thms 1.1/1.2 only use that the leading
   form is prime in a UFD; they hold verbatim for every irreducible leading form (Thms 1.1′, 1.2′).

## Answers to the goals
(1) Collapse extended: binary cubic forms, ternary cubic norm forms, all norm forms; the cubic rung collapses (Cor 1.3′,
Cor 3.2). No non-collapsing family exists to construct. The point where degree-2 arguments looked degree-specific (Q on a
rational line; a degree count) has UFD replacements (Remark 1.4).
(2) n/a (no non-collapsing family). Units/cusps checked separately: Lemma 2.1 (orbit finiteness via Skolem–Mahler–Lech;
any family, incl. (x, y, z)-families, valid at infinitely many points of a unit orbit is constant on {N = n}) and Cor 2.2
(such families collapse). T1 not needed; on square classes the old T1 argument also applies (N(α²) = N(α)²).
(3) The relevant double cover is w² = n, not w² = N(u, v): the norm-form menu equals rung 0 ∘ N, so its sterile set is the
pull-back of profinite unit squares (§4).

## Iterations (constructing vs refuting)
I1 looked for the degree-3 failure → none. I2 cusps/unit orbits (every prime's orbit enters every cusp) → killed by
finiteness of 4/n + SML. I3 power-cusp shells (weighted leading part c·l₁l₂l₃ is reducible over ℚ̄, so F1 fails there) →
attempted shell families, which led to the algebraic Thm 3.1 killing all of them. I4 O_K-structured windows
p + m = N(α + γ): window size ≥ p^{2/3} (balanced α minimises max|p/σ_i(α)|), so B3 lottery; not run.

## Files
NORMFORM_CUBIC.md (§1–4); BRAINSTORM/z20_degree_free_collapse.md, z20_orbit_finiteness.md, z20_unit_criterion.md;
scripts/z20_collapse_check.py (sympy checks of every rearrangement in Thms 1.1′/1.2′/3.1 + degenerate family; random
search over u³ + 2v³ and the ℚ(∛2) ternary norm form: 143 resp. 110 Type II families, all in ℚ[P]; the random Type I
search found no families at all, so it is uninformative there).

## Labels
Thm 1.1′, 1.2′, Cor 1.3′, Lemma 2.1, Cor 2.2, Thm 3.1, Cor 3.2, §4 identification: PROVED (unreviewed). Remark 3.3 last
sentence and the "B2" readings: Assessment. Numerics: EVIDENCE only for consistency.

## Sparks (not pursued)
* Type II analogue of the unit criterion for P with reducible leading form but no units mod P (Thm 1.1′ needs irreducible top).
* Rational-function families in cusps: Lemma 3.3 of POINTWISE_BINARYFORM counts points, not orbits; a rational family could
  in principle be valid at one point per orbit at depth ≍ log p. Its validity is a divisibility B(x) | A(x) (B2-shaped).
* Lines in K-space give one-parameter menus with algebra ℚ[u]/(φ) ≅ K: Theorem A's sterile sets are then governed by the
  square classes of O_K^× — a family over a growing set of lines is an H-A family whose sterility is unit-square data of K.
* (x, y, z)-families for norm forms whose ET coordinates are not polynomial: Lemma 2.1 handles orbits; the cone/shell case
  would need POINTWISE_BINARYFORM §8's descent in k variables.
