# BRAINSTORM — Thin groups, orbits and the affine sieve for ES (O144, angle c)

Labels as in DISCOVERIES.md.

## 1. Idea

The thin-orbit programme (Bourgain–Gamburd–Sarnak; Kontorovich; Bourgain–Kontorovich) proves that some
polynomial f on an orbit O = Γ·v of a thin group Γ ⊂ GL_n(ℤ) takes almost all admissible values (Zaremba,
Apollonian), or almost-prime values (affine sieve). An ES route would need:
(i) an orbit O and a polynomial F with ES solutions attached to the points of O, and
(ii) a theorem that F(O) ∋ p for **every** large prime p (a full local-global statement for O).

## 2. Literature anchor

* Bourgain–Kontorovich, *On Zaremba's conjecture*, Ann. of Math. 180 (2014) (verified title/abstract). It gives
  density one. Huang, arXiv:1310.3772 (verified), gives A = 5.
* HKRS, Ann. of Math. 200 (2024), arXiv:2307.02749 (PDF read). The Apollonian local-global conjecture is
  *false*. Thin-orbit reciprocity obstructions are invisible to the Zariski closure. The repaired Conj 1.5 is open.
* From memory, unverified bibliographic details:
  * Bourgain–Gamburd–Sarnak, *Affine linear sieve, expanders, and sum-product*, Invent. Math. 179 (2010)
    (almost-prime values on orbits);
  * Salehi Golsefidy–Sarnak, *The affine sieve*, JAMS 26 (2013);
  * Kontorovich, *From Apollonius to Zaremba: local-global phenomena in thin orbits*, Bull. AMS 50 (2013);
  * Bourgain–Kontorovich, Apollonian density one, Invent. Math. 196 (2014).
* State of the art (Assessment): no full local-global theorem is known for any thin orbit with polynomial
  growth of the representation count, let alone one with polylogarithmic multiplicity.

## 3. What the natural group actually is (PROVED facts, from earlier ledger items)

* **Fixed n.** By BL Lemma 3.10 the integral points of U_n off the lines are finite. The equation
  `a(4bcd − 1) = b + nc` is linear in each variable, so there is no Vieta/Markoff involution group. No infinite
  group acts on the fixed-n solution set. (Contrast Markoff, where Γ is a thin-like nonlinear group and
  Ghosh–Sarnak's "almost all, but not all" holds: H-F.)
* **All n at once.** The universal Type I family is `X_d : ef − 4da² = 1`, together with a free variable c and the
  value `p = 4acd − f` (BRAINSTORM/farey_ford_cf.md; equivalently the SL₂ matrices `[[e,2a],[2ad,f]]`, or the
  3-step Farey paths of BRAINSTORM/farey_chain_frieze.md). The symmetry group SO(Q_d)(ℤ) is **arithmetic**, not
  thin, and strong approximation holds (DISCOVERIES (I)7). The ES condition `4ad | f + p` is a congruence
  modulo a coordinate.
* **Farey paths.** SL₂(ℤ) acts on 3-step Farey paths, but the span condition (Prop C.1: span ∈ (4/p)ℤ) is not
  SL₂(ℤ)-invariant. Only translations preserve it. So no group carries ES solutions of one p to ES solutions of
  the same p.

## 4. Barrier screen

* **B3 (decisive).** The BK circle method for thin orbits works because the representation number of a target
  is a power: R(n) ≍ n^{2δ−1}, with 2δ − 1 > 0 for Apollonian and for Zaremba with A large. The spectral gap
  then beats the error at a single target only on average (density one), never pointwise. For ES the
  per-target mass is ≍ log³ p (scale constraint, CONDITIONAL_ES Prop 2.3: main term ≤ p^{o(1)}). A thin
  sub-orbit Λ ⊂ SO(Q_d)(ℤ) of critical exponent δ < full only *removes* points: the per-target mass becomes
  ≪ p^{−(1−δ')} L³ → 0. So thinning is anti-productive, and the arithmetic orbit is already the ET lottery.
* **B6 / T7.** Every thin-orbit local-global theorem known is density one (an exceptional set O(N^{1−η})).
  ES's analogue is Vaughan/ET-type. H-F cautions that in the comparable Markoff and Apollonian families,
  "almost all" is the truth, not "all".
* **Affine sieve direction.** BGS/SGS give *some* orbit points with almost-prime F-values: lower bounds on the
  number of good points in a ball. ES needs, for a *prescribed* prime p, a point with F = p (a fibre of
  polylog size). The expander input is equidistribution mod q for q ≤ (ball size)^{c}. At a single fibre that is
  congruence data (B1), with the Planck-scale issue of (I)3.
* **B5/T1.** Odd squares are locally admissible. A thin-orbit theorem would have to *detect* the quadratic
  obstruction there. HKRS shows thinness creates such obstructions; it does not prove their absence. And in
  thin orbits the obstruction families have the form u·m^k, which contain no primes beyond u. This is
  consistent with ES at primes, but gives no mechanism.
* **B2.** Every orbit parametrisation found here (X_d, the SL₂ matrices, Farey paths) is a slice family. Fixing
  two coordinates leaves one divisor-in-class event (redteam-2 Lemma 2.1).

## 5. Experiment

None needed beyond the companion memos. The orbit structures are the ones already enumerated there
(Lemma A.1 reproduces f_I exactly; Prop C.1 covers all solutions).

## 6. Viability Assessment

**COLLAPSES to B3 at the step "pointwise local-global for an orbit".**
* Thin-orbit technology needs power-size multiplicity per target, and even then it yields only density one.
* ES has polylog multiplicity, and its natural orbit group (SO(Q_d)(ℤ) on X_d) is arithmetic, not thin.
  Passing to a thin subgroup lowers the main term below 1.
* No group acts on the solutions of a fixed p.

By-product (Assessment): the honest analogue of HKRS Conj 1.5 for ES is "Type I ∪ II exists for all odd
non-squares except finitely many sporadic n". In ET coordinates, the sporadic set to 2·10⁷ is {105}
(BRAINSTORM/apollonian_reciprocity.md §4). For primes this is ES itself.
