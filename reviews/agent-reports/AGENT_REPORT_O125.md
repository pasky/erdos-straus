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

## Phase 2, item 1: O127 (section 5 of reviews/redteam-automorphic.md)
Verdict: the negative conclusions of CONDITIONAL_ES survive; X_slice is a *surviving target* (E1; passes
T1/T4/T8), not a route.
* New (PROVED): no slice solution at an odd square with gcd(n,c)=1 (ET Prop 1.6); EVIDENCE: no slice solution at
  all at odd squares m ≤ 61 (complete) / m ≤ 151 (g ≤ 3000). So `|S_1| < S_0` fails at every odd square, and any
  bound must use primality.
* New (PROVED via notes Lemma 77.6): every slice solution has (d/p) = (b/p) = −1, so m = 4d has a prime ≥ n_p.
* Under H, g_min is unbounded (Theorem C). At approximants of the special points (p up to 10³¹) g_min ≤ 19
  (EVIDENCE), so the special points are invisible to the slice.
* Prop 2.3 (O127) and my Prop 2.4 are the same inequality and both correct. O127 has a power-sparse exceptional
  set; mine has an every-p bound (p^{3/5}) and a polylog density-1 bound. Merged in §5.5. Both are blind to
  coarse (non-injective) encodings.
* Repairs requested:
  - (a) §3.2's "each χ at one argument" is false: a primitive χ* mod q recurs at ~p/q arguments in an AP of
    modulus ≍qp. The conclusion holds anyway, since the GRH error p^{1+ε} exceeds the p/q terms.
  - (b) "OMEGA13 kills polylog Chebotarev witnesses" is Type II only; for Type I/X_slice nothing beyond
    `ck_min ≫ log p log₃p` is known.
  - (c) The `μ ≤ p^{o(1)}` qualifier is missing in the §5 table and report item 3.
  - (d) Add the odd-square fact to Prop 3.1.

## Phase 2, item 2: O124 escape hatches (§6 of reviews/redteam-automorphic.md)
* New PROVED facts:
  - Prop 6.1: a valid recipe is constant on every irreducible curve carrying infinitely many admissible points,
    because Sol(p) is finite. So lines and Pell orbits are coarse invariants: one curve gives one solution.
  - Prop 6.2: a (Q_d) point with 4ad | f+1 is a Type II witness of modulus f, so f ≥ W(p) and X5 applies.
  - Lemma 6.3: (Q_d) points correspond to forms [de, 4ad, f] of discriminant −4dp. The side condition is not
    Γ₀(d)-invariant (Assessment); it selects orbit representatives at cusp height ≍ √p.
* Verdicts:
  - H1 (growing families) collapses to ET-class coverings with growing moduli. The exceptional-level loophole
    is a parameter search (Assessment).
  - H2 (thin side conditions, Q_d) is live only as a Planck-scale cusp-excursion problem (Kuznetsov on
    Γ₀(4ad), DFI roots), which is O128's domain.
  - H3 (split ternary level sets) collapses (Prop 6.1, Hasse–Minkowski, O(√N) primes).
  - H4 (k ≥ 4 indefinite) reduces to H5.
  - H5 (fixed level set ef − 4a²d = 1, p only in the side condition f ≡ −p mod 4ad) is outside O124's
    Def 1.1 entirely. It is the live automorphic route (O123 / (D)32); x̂₉ is its binding sterile candidate.
* Minor points on O124: Cor 7.1 covers mild inputs only. The §8 numerics bound the small parameters, not the
  witness modulus f.
