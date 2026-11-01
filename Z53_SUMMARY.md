# Z53_SUMMARY — wave z53 (hard · fast · wide · deep) on the open FRONTIER §7 targets

**ES is OPEN.** Nothing in wave z53 proves or disproves it. Every result below is internal. Every memo had an internal
hostile review and a cross-model (GPT-6 Astra) hostile review, with fixes applied before merge. The reviews are in
`data/z53/xreview/REVIEW_<LANE>.md`; the consistency review of this summary and the FRONTIER export is
`data/z53/xreview/REVIEW_FRONTIER_Z53.md`.

Briefs: `z52bbriefs/z53_depth.md`, `z53_lanes.md`, `z53_upper.md`, `xreview_z53.md`. The wave had 18 lanes: 14 in the
first wave, plus 2 follow-ups on strengthened lanes and 2 side targets in z53b. Memos are `Z53_<LANE>.md`.

## 0. Bottom line

**The core barrier B2 did not move.** No lane produced a mechanism that forces a single tied divisor event at a
prescribed prime. Assessment: no lane supplied single-prime positivity; the scoped obstructions leave undeveloped
survivors, including those retained by WILDCARD and LIT. For the genus route, GENUSX Lemma 4.1 rewrites the exact
subfamily counts R_𝔉 and G_𝔉 as sums over free w of functions of (p mod w, ⌊p/w⌋), the shape of §7.1. Assessment: the
unresolved layers are B2-shaped gaps connected to §7.1, not a proved B2 equivalence or universal convergence theorem.

What did move is real but peripheral:

* **Genus main term (GENUSLVAL Thm U; PROVED, unconditional, effective).** M_gen(p) ≥ (2/(3π⁴) − o(1)) log²p at every
  sufficiently large prime p ≡ 1 (4). This closes FRONTIER §7.4. Transfer to R(p) still needs control of the order-≥3
  part X(p) (B2).
* **Upper bound (SQSIEVE Thm A; PROVED rel. Weil + vdC).** R(n) ≪ n^{12/37+ε} for every n, by tie-detecting square-sieve
  sums. It is preceded by R(n) ≪ n^{1/3−1/225}(log n)² for n ≥ 2 (HYPSUMPROD Thm 1), the first power saving in this
  campaign over the previous elementary p^{1/3} benchmark; external priority is unverified. An upper bound valid at
  squares, silent on positivity.
* **Almost-all lower bound (PZ Thm A; PROVED rel. BV).** For each fixed ε ∈ (0,1/64), R(p) ≥ (1/64 − ε) log²p for all
  but O_ε(π(X)/log X) primes p ≤ X, once X is large (ineffective). Compare ET Thm 1.8's (log p)^{0.549}. An average
  statement (B6).
* **Density-level class control (GENUSX Thm X; PROVED, unconditional, effective).** On the Thm U subfamily under (C1),
  (C2*), (C4), with integer Burgess parameter r ≥ 1, T_u = O(p^{−δ} log p); adding (C3) gives
  M^cls_𝔉 ≥ (c − o(1)) log²p. This is density-level class control only; both exact-divisor layers remain unresolved.
* **B1 with oracles (NONCRTLOGIC Thms A, T).** For each correct witness-producing procedure in the stated formal
  language, with a defined finite formal tree at the specified trap point, Thms A/T prove failure at every sufficiently
  large admissible input; infinitely many prime failures are CONDITIONAL on H for the augmented finite polynomial
  family. Arbitrary finite-valued oracles are allowed; Boolean/counting certificates and growing searches are not
  excluded. The odd-square principle extends to nonlinear traps P with P(0) = 1 and no positive real root. Closes
  POINTWISE_SIZE item E3 in that scope.
* **§7.6 joint factor multisets (GENUSREDEI).** For a fixed finite family of lines satisfying §1 and an admissible datum Π
  in a fixed finite Galois field, five necessary pointwise laws are PROVED; completeness for complete decorated
  configurations with squarefree rough parts is CONDITIONAL on BHC (Thm JRT); under BHC, bounded-level forcing from Π
  alone is exactly B1, while prescribed factor decorations can additionally force events. Scoped no-go, conditional (details in §1, T3).
* **HC (HCSHIFTS Thm W; PROVED + Assessment).** Fixed-family certification wall: for each fixed polynomial family
  satisfying W's prime-valued factorisation hypotheses throughout a fixed window X, p is constant modulo every odd prime
  ℓ ≤ ⌊X/4⌋+1, and every member except possibly the least satisfies log p > (1/4+o(1))X. This bounds the certified
  window, not actual HC(p). Model-motivated target HC(p) ≤ (log p)^A with A > 2 log 2; equality is also consistent with
  HCSHIFTS's occupancy model, but undecided in HCHYP.
* **Lattice (LATTICE Thm A; PROVED).** For odd n ≥ 6.8·10¹⁷, no Def. 1.1 full-rank convex Thue scheme in (u,B,C), with
  its exactness/size conditions and positive-octant covering or Minkowski hypothesis, exists. Scopes the M1b Assessment.
* **Side target (CERTIFIED).** ES(15·2^s + 1) for s ≤ 3·10⁶; class 60 | s still open beyond.

## 1. Per target

**T1, hyperbola cancellation (§7.1)**
* Lanes: HYPKLOOST (Kloosterman/Kuznetsov, across conductors), HYP2CYCLE (dynamics), HYPSUMPROD → SQSIEVE (square
  sieve, sum-product), NONCRTSMOOTH (fixed-modulus multiplicative representation), LATTICE.
* *Proved:* the upper-side benchmark moved, p^{1/3} → p^{12/37+ε}.
* *Narrowed (scoped theorems):*
  * Fejér-weighted frequency sums are window-smoothed counts; the full unweighted projection onto conductors dividing M
    is a class average. Arbitrary weighted cross-conductor sums are not covered.
  * The stated λ-uniform box and shift-uniform class-blind fibre majorants have trivial-scale floors; other uses of the
    tools are not excluded.
  * Proposition B2 excludes a balanced-block power saving only for the §4 k-Poisson implementation with Q = qq′ ≤ W,
    triangle inequalities over frequencies and residue classes, Abel summation, and C-sum majorants
    e_ℓ(W/Q) ≥ c√(W/Q) for |ℓ| ≥ 16W²/n. Other implementations remain unexcluded.
  * Under (H) and ν(a) ≤ P₀−1 on the support of nonnegative weights, quadratic σ-minorants have no positive diagonal
    main term. (H) is checked on finite strips only, not proved for general application weights. Signed auxiliary-sum
    inputs remain open.
  * R2 (2-cycles): PROVED reduction; R2 is CONDITIONAL on the uniform equidistribution hypothesis MIX, for which no
    method is known.
  * For fixed η > 0 and one q = q(X) ∈ 4ℕ with q ≤ X^{1/2}, prescribed independently of p, all but o(π(X)) primes p ≤ X
    have no E(q,κ) with κ ≤ q/(log X)^{2+η}. This limits an almost-all guarantee at that q, not simultaneously over q;
    for fixed q the threshold eventually falls below 1. Aggregation over q is the remaining Type II route (Assessment),
    not a necessity for every ES proof: ES is Type I or Type II.
  * For odd n ≥ 6.8·10¹⁷, no Def. 1.1 full-rank convex Thue scheme in (u,B,C), with its exactness/size conditions and
    positive-octant covering or Minkowski hypothesis, exists.
* *Remains:* a bilinear (ℓ, C) cancellation (balanced block); positivity from the top of the spectrum using primality;
  signed or nonlinear methods.

**T2, one-coordinate polylog bound for HC (§7.2)**
* Lanes: HCSHIFTS (anatomy, growing windows), HCHYP (conditional route), UPPER (just prove HC ≪ p^θ; user-requested,
  unprimed).
* *Proved:*
  * Fixed-family certification wall: for each fixed polynomial family satisfying W's prime-valued factorisation
    hypotheses throughout a fixed window X, p is constant modulo every odd prime ℓ ≤ ⌊X/4⌋+1. Every member except
    possibly the least satisfies log p > (1/4+o(1))X. This bounds the certified window, not actual HC(p); a sequence of
    families contributing their least members and other certification mechanisms are not excluded.
  * At infinitely many primes there is a window X ≥ (1/10.4−o(1))log p in which every certificate with coordinate
    x ∈ 𝒞, x ≤ X splits the (X+1)-rough part nontrivially (PROVED relative to Linnik). No exclusion at larger
    polylogarithmic coordinates follows.
  * Exceptional-set bounds over primes p ≡ 1 (4) for HC ≤ p^θ and HC ≤ (log p)^A (ineffective constants), correct but
    not a new rate.
* *Assessment (model-based recalibration):* HCSHIFTS's occupancy model, with independent draws across primes for the
  infinitely-often conclusion, predicts HC > C log p infinitely often and eventual HC ≤ (log p)^A for A ≥ 2 log 2.
  HCHYP's distinct uniform-residue model proves failure below 2 log 2 and eventual success above it; equality is
  undecided there. Its Cor M3 is a non-implication in the model's line-data space, not an arithmetic non-implication or
  refutation of Conjecture 3.4. No standard conjecture is shown to imply the target.
* *UPPER, honestly:* for fixed 0 < θ < 1, pointwise HC(p) ≪ p^θ is open and would imply ES for sufficiently large
  primes. UPPER §5.4 heuristically estimates ≍ log X·log p certificate pairs up to coordinate X, hence ≍ θ log²p at
  X = p^θ; this supplies no pointwise lower bound.
* *Remains:* the target itself (B2 with a growing window).

**T3, beyond the BM/genus layer (§7.3, §7.4, §7.6)**
* Lanes: GENUSLVAL → GENUSX (explicit L-values, Burgess), GENUSREDEI (Rédei, governing fields, joint multisets).
* *Proved:*
  * §7.4 closed (Thm U), at every sufficiently large prime p ≡ 1 (4).
  * For squarefree u ≡ 1 (4), u ≤ p^α with fixed α < 3/5, Prop C gives an L-value approximation to S_u with
    power-saving additive error. The nonprincipal sum runs over η ≠ 1 and has prefactor 1/(2φ(u)); the principal term
    retains L′ and H′ terms. EVIDENCE: maximum relative error 0.1292 % in 18 tested slices with X_u ≥ 10⁵, including
    (★)-zero primes; net cross terms remove about 38 % in one displayed slice. Aggregate M_gen(p) = o(log²p) is
    excluded by Thm U.
  * On the Thm U subfamily under (C1), (C2*), (C4), with integer Burgess parameter r ≥ 1, T_u = O(p^{−δ} log p); adding
    (C3) gives M^cls_𝔉 ≥ (c−o(1)) log²p (Thm X; PROVED, unconditional, effective). This is density-level class control
    only; both exact-divisor layers remain unresolved.
  * GENUSREDEI: for a fixed finite family of lines satisfying §1 and an admissible datum Π in a fixed finite Galois
    field, five necessary pointwise laws are PROVED. Unconditionally, finite partial configurations satisfying (L3),
    (L5) occur on a positive-lower-density set of primes; residual cofactors need not be prime or squarefree (U).
* *CONDITIONAL on BHC:* completeness for complete decorated configurations with squarefree rough parts (JRT). Under
  BHC, bounded-level forcing from Π alone is exactly B1 (F); prescribed factor decorations can additionally force
  events. Growing levels, p-dependent class-group data and repeated large factors are not covered.
* *Remains:* the two exact-divisor layers T_w = G_𝔉 − M_𝔉 and T_uw = R_𝔉 − G_𝔉 − T_u (Lemma 4.1; they also subtract
  density terms). Assessment: B2-shaped gaps connected to §7.1, not a proved B2 equivalence. EVIDENCE in standard-window
  samples outside Theorem X's hypotheses, at scales 10⁹–10¹²: var(R_𝔉 − G_𝔉) is about 88–93 % and var(G_𝔉 − M̂) about
  9–10 % of var(R_𝔉 − M̂). Only the former is compared with swap-Poisson, with variance/(2·mean G_𝔉) ≈ 0.81–1.02.
  These proxy statistics do not validate Theorem X.

**T4, growing or p-dependent roots in F_p**
* Lanes: FORESTCLASS (class-group roots), NONCRTLOGIC (oracle taxonomy).
* *CONDITIONAL on Dickson:* the bounded menus enumerated in FORESTCLASS Cor 1.1 fail infinitely often, even with
  unrestricted component exploration. Arbitrary bounded class-group functions, other p-dependent split classes and
  individual real-cycle prefixes are not covered.
* *Proved:*
  * The full reduced-form minimum set of discriminant −4p cannot be enumerated by a fixed finite list of
    polynomial-valued roots (PROVED relative to Siegel). No corresponding cardinality/escape result is established for
    truncated SM, SMN or SP, positive discriminants, or polynomially indexed growing enumerations.
  * Lemma G: for a ∈ SM, a ≥ 3, the target genus coset contains at least τ(p+a)/[G:G²] divisors. This removes the
    genus obstruction, not the exact-class obstruction; arbitrary SP roots are not covered.
  * NONCRTLOGIC Thms A/T: for each correct witness-producing procedure in the stated formal language, with a defined
    finite formal tree at the specified trap point, failure at every sufficiently large admissible input; infinitely
    many prime failures are CONDITIONAL on H for the augmented finite polynomial family. Arbitrary finite-valued oracles
    are allowed; Boolean/counting certificates and growing searches are not excluded.
* *CERTIFIED for primes p ≡ 1 (8), p ≤ 10⁸:* SP has no failures; SM fails only at 19441. SP/SM are the filters
  a ≤ ⌊√p⌋+1 with p/−p square mod a, respectively; failure means no root reaches a bichromatic component.
* *EVIDENCE:* the measured SM advantage is consistent with a genus explanation; genus-conditioned MH point estimates
  are 0.930–1.081, without an established confidence interval or detection threshold.
* *Remains:* growing windows (HC-type).

**T5, lower bound not built from CRT data (E1/E2)**
* Lanes: NONCRTLOGIC, NONCRTSMOOTH, LATTICE.
* *Necessary condition (PROVED; NONCRTLOGIC Cor T3(c), Prop S):* for a witness procedure to succeed at admissible primes
  of every trap point, it must escape a fixed finite formal menu and produce non-formal integers carrying non-residue
  prime factors (necessary, not sufficient; non-formality alone does not supply them). This is a pointwise
  trap/admissibility statement; prime infinitude is conditional on H. The least non-residue supplies a fully factored
  non-residue, and its bounded finite-tree procedures reduce value by value to the r-generic line (§7.9).
* *Remains:* E1/E2 with factorisation control, i.e. B2.

**Wildcard and literature**
* WILDCARD (Fable, from scratch): inconclusive. The cross-review rejected its first draft's "no survivor / no false
  kill" claims, and the repaired memo lists unexcluded ideas: the full Type II family as target, the converse of T1 for
  the family (II), r-spectrum forest edges, and varying ray-class fields.
* LIT (Assessment, coverage-limited): the sweep found no published tool supplying B2; (J)103 survives only in the
  scoped wording of LIT §6.4. Garaev–Shparlinski's Linnik-lcm construction (arXiv:2304.07953) is an existential-prime
  template controlling a positive fraction of a window; its class −1 makes (★) easy, so a kill needs another class.
  Pascadi (arXiv:2511.08445) informs LIT's fixed-power error-envelope comparison for Poisson plus length-independent
  bilinear bounds, not a universal fixed-modulus limit.

## 2. Side targets
* PZ (Z2362): proved in a stronger, density-one form (Thm A; for each fixed ε ∈ (0,1/64), all but O_ε(π(X)/log X)
  primes p ≤ X). The full second moment is not proved.
* THIN15 (§7.8): certified s ≤ 3·10⁶.
  * In B′'s odd-power shape, each fixed odd prime exponent p gives four Thue equations, each with at most one positive
    solution (Bennett); SG shape is separately excluded.
  * B's odd-integer-u branch is Ridout-finite for each fixed odd prime exponent p, including 3, ineffectively and
    non-uniformly in p; general rational-u finiteness is not proved. B is certified empty for integer u with E ≤ 3000,
    dyadic u with ip ≤ 72, integer w, and dyadic SG w with 4i−2 ≤ 90.
  * Sign lemma: no rule polynomial in 2^{s/2} reaches μ = 0.
  * ET/divisor-class coverings alone fail: residue 0 survives. A general finite congruence covering must include a rule
    valid on all sufficiently large multiples of a modulus; such coverings are not excluded. Polynomial dependence on
    multiplicatively independent extra exponential bases collapses to the 2-power variable, giving a μ=0 root family
    only on a residue-0 progression. Laurent/rational dependence, binomial menus beyond certified ranges and
    non-binomial patterns including D=3 II-d and D=6 remain open.

## 3. FRONTIER changes applied
* §3 tied-modulus benchmark;
* §5.1 PZ;
* §5.2 THIN15;
* §5.3 NONCRTLOGIC and LATTICE;
* §6 z53 dead-end lines;
* §7.1, §7.2, §7.3 updates;
* §7.4 marked CLOSED;
* §7.6 closed relative to BHC (CONDITIONAL);
* §7.8 update.

The exports must retain each source theorem's hypotheses and cross-review restrictions.

## 4. Honest assessment
Wave z53 was wide (18 lanes, five targets, every angle in the brief) and moderately deep: most lanes finished within
1–1.5 h with scoped theorems rather than running the full time box (descriptive Assessment, not a completeness
certificate). The quantitative gains are genuine:
* the genus main term at every sufficiently large prime p ≡ 1 (4);
* a power saving on the upper benchmark;
* almost-all R(p) ≫ log²p.

These three main-term, upper-bound or average results alone do not imply positivity at a prescribed prime; no
impossibility of combining them with further arithmetic input is proved. The single-prime lower tail, R(p) ≥ 1 forced
at every large p, is exactly as open as before.

*The most concrete remaining well-posed gaps:*
* a bilinear (ℓ, C) cancellation estimate, which would extend the square sieve to the balanced block (upper side only);
* control of the exact-divisor layers T_w and T_uw on the Thm U family (Assessment: B2-shaped gaps, not a proved B2
  equivalence; separate bounds suffice but are not individually necessary, since they could compensate);
* the model-motivated growing-window HC target HC(p) ≤ (log p)^A with A > 2 log 2; equality is also consistent with
  HCSHIFTS's occupancy model, but undecided in HCHYP.
