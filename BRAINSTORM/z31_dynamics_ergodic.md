# z31 — Dynamics and ergodic theory: Furstenberg correspondence, Hecke orbits, Euclid/Gauss/Rényi maps, transfer operators (O261 field memo 13)

Labels as in DISCOVERIES.md. No new sources beyond memo 1 (BK's transfer-operator major arcs, read). Builds on DEDEKIND_ES §5.4
(Euclid recursion, Rényi map with an indifferent fixed point), SYNTHESIS_SPARKS8 Prop 1.4, nonab_homogeneous_dynamics.md.

## (a) Counterparts
1. **Furstenberg correspondence** (density ⇒ recurrence; Szemerédi via ergodic theory). Counterpart: "a set of positive
   density of n has ES" — true and known (Vaughan; ET), useless for a single p.
2. **Equidistribution of Hecke orbits / periodic torus orbits** (Clozel–Oh–Ullmo; ELMV, memory): pointwise in the orbit
   parameter, with orbits of power size (see memo 4).
3. **Euclid/Gauss/Rényi dynamics and Ruelle transfer operators**: B2 at p is a statement about the backward-CF (Rényi) orbit
   of p/A: a_r(n) = Σ_{A<n} 1_{L_{r−1}(A)}(−n mod A) (DEDEKIND_ES §5.4, PROVED); the Rényi map has an indifferent fixed point.
   In BK, transfer-operator renewal theory gives the *major-arc main term* of Zaremba counts (BK p. 7–8, read) — pointwise,
   but only for the main term.

## (b)/(c) Status and transfer
* (1): averages only (F1).
* (2): power-size orbits and region targets (F2, F3; memo 4).
* (3): the Euclid recursion is exact, and linearising the least residue returns the window form (SYNTHESIS_SPARKS8 Prop 1.4) —
  no information gained. Transfer operators give main terms; the pointwise step in every thin-orbit theorem is an
  *error-term* bound at the individual target (BK (1.37): only on average; Shkredov/Zhang: by growth in SL₂(ℤ/qℤ) with power
  sets — memo 1). At criticality (2δ = 1) the Rényi map's indifferent fixed point makes the relevant transfer operator have
  no spectral gap on the natural space (the "log" in log² p is the infinite-measure effect) (Assessment).

## (d) Verdict: ANALOGUE (B2 = a fixed-target count for the Rényi/Euclid dynamics at critical exponent). **NOT SHARP.**
