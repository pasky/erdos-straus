# z32 memo 5: adversarial search at 10¹⁸–10²⁵ (O262; DISPROOF_AVENUES §5)

Labels as in DISCOVERIES.md. ES is not solved; no counterexample is known. All numbers EVIDENCE (primes are
BPSW-probable via python-flint; every reported least solution is checked in exact rational arithmetic).

**Idea.** Push O154's 10¹⁶ adversaries to 10¹⁸–10²⁵ with an engine that is exact on a complete sub-family: the
1024 cheapest e-slices (Types I and II, e ≤ 2047; `scripts/z32_adv.py`, validated against bs_adv_count and brute
force).

**Designs.** Random p ≡ 1 (24); class of one (y = 37, 43, 53); + quadratic residue at every ℓ ≤ 97; Prop 3.1
shadow on e = 3, 7, 11; selection of the lowest S(127) among 300/3000 class-of-one primes. 86 primes.

**Results.**
* Hardest prime relative to controls: **p = 2054098191162848070241** (≈ 2·10²¹): S = 870 (0.26 × controls),
  least slice W = 11. Smallest absolute S: 612 (≈ 2·10¹⁸). All W ≤ 19 (W = 15–19 forced by the shadow design).
* The depression saturates at ≈ 0.32–0.36 (selected) / 0.35–0.48 (class of one) at every size.
* S overstates the true depression: at 10¹², S/C0 = 0.49–0.63 while exact f_II/C0 = 0.80–0.82.
* Distance to failure: ≥ 600 independent-looking solutions in the cheap families alone; the calibrated zero law
  (memo 4) gives P(f_II = 0) < e^{−200} for such μ.

**Barrier screen.** B1 (congruence-only adversaries, saturating), B2 (finite slice kills), B6 (designs are
averages; single-prime claims only for the 86 primes).

**Viability (Assessment).** As a disproof search: COLLAPSES (the model expects < 10⁻⁸⁰ hits). As a stress test:
passed — no H-A/H-E "missing force" signal, no drift towards failure from 10¹² to 10²⁵. Promise 0/5 for disproof.
