# AGENT REPORT O125 — red team for the automorphic/geometric attack (Phase 1 checkpoint)

Branch `side-agent/redteam-automorphic`. Main file `reviews/redteam-automorphic.md`; script
`scripts/rt_modeltest.py`; data `data/rt/`. Nothing here proves or refutes any case of ES.

## Delivered (Phase 1)

* **§1 Admissibility checklist.** X1–X9 = what is excluded, each with source, label and exact scope
  (Thm M/C/Cor M1, Prop A, Lemma CT, OMEGA13 Thm 5.1, OMEGA14/15 ceilings, Haar avoider density,
  Bright–Loughran Thms 1.6/1.8/1.9, ET polylog counts). N1–N7 = input types *not* covered by any
  campaign obstruction (E1 searches, E2 non-formal integers, E3 non-abelian Frobenius [open],
  E4 counting certificates, automorphic-period equidistribution, L-function bounds, prime-measure
  support/non-linear certificates).
* **§2 Quantitative constraints** (all PROVED, short proofs, modulo cited theorems):
  * Prop 2.1 *integrality barrier*: pieces with main term ≤ 1/2 contribute ≤ 0 to any piecewise
    positivity argument; Lemma 2.2: all Type II multiplier pieces are such, so Type II routes must
    control the grouped "flipped" count `N_T(p)` collectively.
  * Prop 2.3 *range*: `N_T(p)=0` i.o. at `log T ≍ (log p)^{1/4}(log log p)^{−1/4}` (from X5), so no
    pointwise asymptotic/lower bound for Type II with exponent < 1/4; Type I analogue at heights
    `< n_p`. Assessment: the main term must carry local data at moduli `≈ p^c` (near-Planck).
  * Prop 2.4 *non-injectivity*: family of size `p^δ` with power saving ⇒ detection fibres of size
    `p^{δ(1−η)−3/5−o(1)}` (all p) / `p^{δ(1−η)−o(1)}` (density-1 p).
  * Prop 2.5 *non-residue*: every solution has a prime `≥ n_p` with `χ_p=−1`; y-smooth detection
    fails at p with `n_p > y ≥ (1/5.2−o(1)) log p`.
  * Prop 2.6 *congruence bookkeeping*: "p mod L(P)" inputs are covering statements per class.
* **§3 Model test (EVIDENCE).** At approximants of the square point, x\*\*, x̂₉ (p up to 10⁴⁴) the
  Type II count up to T = 2·10⁵ is typical up to a ≈30% loss of Q-smooth moduli; W(p) ≤ 359; x̂₉ has
  W = 7 (Type I-only test). Assessment: sterile candidates bind only covering-type routes; for
  counting/spectral routes the binding test is the OMEGA13 fibre (not computable; paper test T5).
* **§4 Pre-registered collapse tests T1–T8** (odd-square test, integrality, range, non-residue,
  fibre, covering, average leak, lifting) for Phase 2.

## Caveats
* Markoff/log-K3 Hasse-failure citations in X8 are from memory (sources not archived).
* §2.2's "main term must be high-conductor" and §3.3 are Assessments, not theorems.
* Not separately reviewed.

## Waiting for
Phase 2: checkpoints of O123, O124, O126, O127, O128 from the parent.
