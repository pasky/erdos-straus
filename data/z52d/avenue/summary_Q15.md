# z52d avenue — batch Q15 (113 items) summary
ES is OPEN. `out_Q15.jsonl`. Rows are Assessments unless they cite PROVED/CERTIFIED. Batch: lens-space/knot "translate" items, lattice and
geometry-of-numbers leads, logic/computability/automata items, history/primary-source checks and meta items. 57 rows are calibration-only.

**Status × plausibility** (columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 0 | 0 | 1 | 54 | 55 |
| circular | 24 | 0 | 0 | 0 | 24 |
| unclear | 6 | 8 | 0 | 1 | 15 |
| known-false | 15 | 0 | 0 | 0 | 15 |
| open-plausible | 0 | 1 | 2 | 0 | 3 |
| harder-than-open (corrected packing local–global) | 1 | 0 | 0 | 0 | 1 |
Novelty: 0 → 40, 1 → 72, 2 → 1 (Z3005, multiscale induction; plausibility 1). Every plausibility-3 row is a calibration lemma (yield none).

**Plausibility ≥ 2 AND novelty ≥ 1**: none has ES yield. The non-trivial ones:
* **Z0189** (plausibility 2): *some discretely ordered ring model of IOpen contains n (e.g. 840T + 1) with no positive solution*, so ES is unprovable in open induction.
  This is the logic shadow of POINTWISE_SIZE Thm M; Z1843 adds that a nonstandard counterexample must lie in the sterile set K.
* **Z2797** (plausibility 2): sharper transference for the balanced-lattice cap route (CONDITIONAL on Hypothesis W; caps, not ES).
* Z1770 (Buss witnessing: ES ∈ S¹₂ ⇒ poly-time certificate finder, not known) and the rest (Z2660, Z1378, Z1414, Z1778, …) are calibration.

**Recurring missing theorems**
1. *ES₅ restated in lens-space/knot/quantum language* (circular): Z2657, Z2658, Z2661, Z2672, Z2683, Z2685, Z2719, Z2720, Z2783, Z2839, Z2848, Z2849.
   The common fact is that the ES sign (A/p) is the linking-form class of L(p,A) (Q14 Z2800). No invariant beyond it (σ, Jones at i or e^{iπ/3}, Honda weights, d) helps.
2. *Topological/count-congruence existence* (Smith, Morse/Euler char., Tucker, Borsuk–Ulam): Z2764, Z2765, Z3027, Z3117. All 'unclear', plausibility ≤ 1;
   the step that must fail at odd squares (T1/M5) is never identified.
3. *Fixed menus, programs, automata, identities* (B1, known-false under H): Z0291, Z1060, Z1082, Z1094, Z1090, Z1773, Z1798, Z1516, Z1465.
4. *Single-integer lower tail in disguise* (circular): Z3050 (ε-saving = H⁻_BM), Z0922 (low-dispersion family f(p)), Z2502, Z2532, Z1800, Z1625, Z1978.
5. *Geometry of numbers / pigeonhole / B3*: Z2923, Z2891 (area cannot force colour: T1), Z2738 (CM shrinking targets, B3 Cor 4.1), Z2506 (ternary, T1), Z0474 (Janson).
6. *Logic*: Z0189, Z0191, Z0192, Z0205, Z0326, Z1378, Z1472, Z1770, Z1843, Z1844, Z1911, Z1912.

**New in this pass** (Assessment-level checks by hand; no new scripts)
* **Z2660 (PROVED, elementary):** every linking form on ℤ/m² is metabolic (mℤ/m² is isotropic), which is T1's topological face. Lisca's rational-ball condition is strictly finer.
* **Z2661:** the 'orthogonal complement class = ES sign' test is a tautology of Nikulin gluing. **Z2849:** Honda weight (v−1)(t−1)(u−1) = p + O(vt + tu), so W± ≈ p·count.
* **Z1414 correction:** unbounded C_min is not merely empirical. It is CONDITIONAL on H (each level C is one fixed slice, B2 Thm 2.2(iii)); OMEGA13 bounds only 4uC − 1.
* **Z1911:** the linear u = 1 line '(4C−1) | p+1' fails at p = 73, 193, 313, 337, 409, 457, 577, 673 (< 1000), so Lipshitz-type LGP cannot apply.
* **Z1842:** K = Ẑ ∖ ∪(identity classes) is strictly larger than the closure of the squares ((J)70 sterile points); Haar(K) = 0.
* **Z1378 + Q14 Z0954:** every solution at a prime has max ≥ p^{3/2}/2, and (★) solutions have max ≤ n²/2.
**Assessment.** Q15 has no proof architecture beyond B1/B2/B3/B6/M1a/T1. The topology cluster closes on the linking-form identity, and the logic cluster
yields one plausible meta-theorem (Z0189: ES unprovable in IOpen) and no route. Main outputs are calibration facts and two corrections (Z1414, Z1917 in Q14).
