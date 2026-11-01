# Z53_SUMMARY — wave z53 (hard · fast · wide · deep) on the open FRONTIER §7 targets

**ES is OPEN.** Nothing in wave z53 proves or disproves it. Every result below is internal. Every memo had an internal
hostile review and a cross-model (GPT-6 Astra) hostile review, with fixes applied before merge. The reviews are in
`data/z53/xreview/REVIEW_<LANE>.md`.

Briefs: `z52bbriefs/z53_depth.md`, `z53_lanes.md`, `z53_upper.md`, `xreview_z53.md`. The wave had 18 lanes: 14 in the
first wave, plus 2 follow-ups on strengthened lanes and 2 side targets in z53b. Memos are `Z53_<LANE>.md`.

## 0. Bottom line

**The core barrier B2 did not move.** No lane produced a mechanism that forces a single tied divisor event at a
prescribed prime. Every route ended either at B2 or at the x ↦ −p mod x structure of §7.1. GENUSX Lemma 4.1 makes that
convergence explicit for the genus route.

What did move is real but peripheral:

| result | label | what it buys |
|---|---|---|
| **M_gen(p) ≥ (2/(3π⁴) − o(1)) log²p** for every large prime p ≡ 1 (4) (GENUSLVAL Thm U) | PROVED, unconditional, effective | closes FRONTIER §7.4; the genus main term is now unconditionally log²-sized at every prime; transfer to R(p) still needs control of the order-≥3 part X(p) (B2) |
| **R(n) ≪ n^{12/37+ε}** for every n (SQSIEVE Thm A; first saving 1/3 − 1/225 in HYPSUMPROD Thm 1) | PROVED rel. Weil + vdC | first power saving over the elementary p^{1/3} benchmark, by tie-detecting square-sieve sums; an upper bound valid at squares, silent on positivity |
| **R(p) ≥ (1/64 − ε) log²p for all but O(π(X)/log X) primes p ≤ X** (PZ Thm A) | PROVED rel. BV | almost-all R(p) ≫ log²p (vs ET Thm 1.8's (log p)^{0.549}); an average statement (B6) |
| order-≥3 characters mod 8u contribute only their genus value at density level on the Thm U family (GENUSX Thm X) | PROVED, unconditional | density-level class control; the exact-divisor layers stay open |
| B1 extends to programs with any finite-valued oracle, and the odd-square principle to nonlinear trap polynomials (NONCRTLOGIC Thms A, T) | PROVED / CONDITIONAL on H | barrier strengthening; closes POINTWISE_SIZE item E3 for bounded procedures |
| §7.6 joint factor multisets closed relative to BHC at bounded levels (GENUSREDEI Thm JRT) | PROVED laws + CONDITIONAL realisation | scoped no-go |
| HC kills stop at X ≍ log p (HCSHIFTS Thm W); Conjecture 3.4 (HC ≪ log p) predicted false in the fitted model | PROVED + Assessment | target recalibrated to HC ≤ (log p)^A with A ≥ 2 log 2 |
| no convex Thue/Minkowski scheme for (★) at n ≥ 6.8·10¹⁷ (LATTICE Thm A) | PROVED | scopes the M1b Assessment |
| ES(15·2^s + 1) for s ≤ 3·10⁶ | CERTIFIED | side target; class 60 \| s still open beyond |

## 1. Per target

**T1, hyperbola cancellation (§7.1)**
* Lanes: HYPKLOOST (Kloosterman/Kuznetsov, across conductors), HYP2CYCLE (dynamics), HYPSUMPROD → SQSIEVE (square
  sieve, sum-product), NONCRTSMOOTH (fixed-modulus multiplicative representation), LATTICE.
* *Proved:* the upper-side benchmark moved, p^{1/3} → p^{12/37+ε}.
* *Narrowed (scoped theorems):*
  * cross-conductor sums reduce to smoothed counts or class averages;
  * λ-uniform and class-blind majorants are floored at the trivial bound;
  * square-sieve implementations do not reach the balanced block;
  * unsigned quadratic minorants have no positive diagonal;
  * R2 (2-cycles) follows from the equidistribution hypothesis MIX, but no method for MIX is known;
  * one prescribed class modulus gains at most (log p)^{2+η};
  * convex lattice schemes are excluded.
* *Remains:* a bilinear (ℓ, C) cancellation (balanced block); positivity from the top of the spectrum using primality;
  signed or nonlinear methods.

**T2, one-coordinate polylog bound for HC (§7.2)**
* Lanes: HCSHIFTS (anatomy, growing windows), HCHYP (conditional route), UPPER (just prove HC ≪ p^θ; user-requested,
  unprimed).
* *Proved:*
  * Dickson/H kills cannot certify windows beyond (4 + ε) log p;
  * smooth-part certificates die at X ≍ log p (rel. Linnik);
  * exceptional-set bounds for HC ≤ p^θ and HC ≤ (log p)^A, correct but not a new rate.
* *Assessment:* Conjecture 3.4 should give way to A ≥ 2 log 2. No standard conjecture is shown to imply the target.
* *UPPER, honestly:* pointwise HC ≪ p^θ is open. It already implies ES for large p, and a power window still has only
  ≍ θ² log²p expected hits, so it does not escape the lottery.
* *Remains:* the target itself (B2 with a growing window).

**T3, beyond the BM/genus layer (§7.3, §7.4, §7.6)**
* Lanes: GENUSLVAL → GENUSX (explicit L-values, Burgess), GENUSREDEI (Rédei, governing fields, joint multisets).
* *Proved:*
  * §7.4 closed (Thm U);
  * genus slices in closed form (Prop C);
  * density-level order-≥3 control on the family (Thm X);
  * §7.6 closed relative to BHC at bounded levels.
* *Remains:* the two exact-divisor layers. The bigger one carries ≈ 90 % of the variance and looks swap-Poisson
  (EVIDENCE); it is the §7.1 structure again.

**T4, growing or p-dependent roots in F_p**
* Lanes: FORESTCLASS (class-group roots), NONCRTLOGIC (oracle taxonomy).
* *Proved:*
  * bounded class-group roots die under Dickson;
  * unbounded ones escape B1;
  * a class-group root never has a genus obstruction to a neighbour (Lemma G);
  * every bounded oracle procedure is killed under H.
* *CERTIFIED:* the all-cycles root set never fails to 10⁸.
* *EVIDENCE:* the advantage of class-group roots is explained by the genus layer.
* *Remains:* growing windows (HC-type).

**T5, lower bound not built from CRT data (E1/E2)**
* Lanes: NONCRTLOGIC, NONCRTSMOOTH, LATTICE.
* *Necessary condition (PROVED):* a procedure must generate integers outside finitely many polynomials that carry a
  non-residue prime factor. The cheapest such input with full factorisation control is the least non-residue, which
  reduces to the r-generic line (§7.9).
* *Remains:* E1/E2 with factorisation control, i.e. B2.

**Wildcard and literature**
* WILDCARD (Fable, from scratch): inconclusive. The cross-review rejected its first draft's "no survivor / no false
  kill" claims, and the repaired memo lists unexcluded ideas: the full Type II family as target, the converse of T1 for
  the family (II), r-spectrum forest edges, and varying ray-class fields.
* LIT: no published tool supplies B2, and nothing contradicts (J)103. The Garaev–Shparlinski Linnik-lcm construction
  (arXiv:2304.07953) is a template for kill-side growing-window constructions. Pascadi (arXiv:2511.08445) quantifies the
  fixed-modulus Type II limit.

## 2. Side targets
* PZ (Z2362): proved in a stronger, density-one form (Thm A). The full second moment is not proved.
* THIN15 (§7.8): certified s ≤ 3·10⁶.
  * Menu II-cd reduces to Thue equations, and menu II-ac is Ridout-finite for every p, now including p = 3.
  * Sign lemma: no rule polynomial in 2^{s/2} reaches μ = 0.
  * Covering congruences alone fail.

## 3. FRONTIER changes applied
* §3 tied-modulus benchmark;
* §5.1 PZ;
* §5.2 THIN15;
* §5.3 NONCRTLOGIC and LATTICE;
* §6 two z53 dead-end lines;
* §7.1, §7.2, §7.3 updates;
* §7.4 marked CLOSED;
* §7.6 closed relative to BHC;
* §7.8 update.

All of these come from cross-reviewed memos, with the reviewers' scope fixes.

## 4. Honest assessment
Wave z53 was wide (18 lanes, five targets, every angle in the brief) and moderately deep: most lanes finished within
1–1.5 h with scoped theorems rather than running the full time box. The quantitative gains are genuine:
* the genus main term at every prime;
* a power saving on the upper benchmark;
* almost-all R(p) ≫ log²p.

All three are main-term, upper-bound or average statements, which the barrier map (B3, B6, T1) predicts cannot reach
positivity at a prescribed prime. The single-prime lower tail, R(p) ≥ 1 forced at every large p, is exactly as open as
before.

*The most concrete remaining well-posed gaps:*
* a bilinear (ℓ, C) cancellation estimate, which would extend the square sieve to the balanced block (upper side only);
* control of the exact-divisor layer R − G on the Thm U family, which is B2 in its cleanest current form;
* the growing-window HC target at A ≥ 2 log 2.
