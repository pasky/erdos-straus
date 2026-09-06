VERDICT: SOUND-AFTER-REPAIRS

Reviewed third-draft detached HEAD `50ad74e` in `/tmp/es-sec75` only. The four proved results are sound. The principal second-round mathematical repairs work; no HIGH defect remains. The current text still needs the three MEDIUM and two LOW corrections below. In particular, the new gap-widening sentence does not remove the residual-fluctuation obstruction. This verdict does not endorse the unconstructed joint model.

## A. N1–N9 disposition

| Round-2 item | Disposition | Current text and reason |
|---|---|---|
| N1: index-six squarefreeness | REPAIRED | §75.1(ii) now says “for squarefree h and primes a congruent to 7 modulo 12”; K has odd order. One generator and all remaining classes in K gives quotient support `{0,±1}`, excluding the involution 3. The probability, minimum 5/6 at lambda=1/6, and threshold .0432335221… are correct in the squarefree iid model. |
| N2: product-log branches | REPAIRED | Assessment 75.5 distinguishes fixed rho<1 (“no exact failure exponent is asserted”), rho=1 (“constant order”), and rho>1, where alone it uses `log(product expectation)=-(1+o(1))sum hit probabilities`. The first two branches give the same power g=theta' despite different logarithmic factors. |
| N3: unrestricted g<=f | REPAIRED | Computational 75.1(ii) now restricts `g<=f` to the sampled grid below `2 log 3/(1+2 log 3)` and compares g with `max f` on the whole sampled grid. This agrees with the code. A separate “throughout” wording issue remains in R5. |
| N4: false exact moment templates | REPAIRED | The rigorous assertion is now the minimum of the actual centered-even-moment ratios. The Gaussian costs are explicitly leading asymptotics requiring uniform moment asymptotics. The lower direction is explicitly assumption (CM), on nonnegative real counts, with even k=o(mu), feasible x, and t² much larger than k. The Poisson endpoint Christoffel formula and its stated logarithmic scale are correct. |
| N5: gap-model obstruction | PARTIALLY | The gap is correctly positive-width for every theta, below the boundary precisely for fixed theta>theta_*, and uses one or two large primes. The cost is now a “candidate exponent”; the text explicitly denies a joint LT/BLK mass, optimality, or statistics-model ceiling. However, the added O(sqrt(log L)) fluctuation repair is insufficient (R1), and the nearby assertion that a block “needs” this deficit retains an invalid necessity claim (R3). |
| N6: pointwise saturated expectation | REPAIRED | The all-integer-modulus proxy is explicit; the three branches of r(beta), including r(2)=1.7298309898…, are correct. The prime-modulus total is correctly `(log p)^2 log log p`. Arithmetic representation counts and witness locations are no longer identified with these expectations. |
| N7: finite occupancy wording | REPAIRED | `check_bw` now asserts `t199==2`. It computes and prints 227 and asserts the displayed finite upper inequality; it does not assert equality to 227 separately. The text correctly says the asymptotic occupancy bound comes from the proof. |
| N8: Status, BR, withdrawals | PARTIALLY | Status (d) now says “sufficient”; (e) says “candidate exponent” and “no matching joint … obstruction”; (f) explicitly says “proxy” without a location consequence. BR is now only a total-rate proposal, and the paragraph after Theorem 75.4 correctly demands separate structured-block coverage. But the replacement review-history claim is false (R2), and the withdrawal/input inventory is incomplete (R4). |
| N9: convexity, diameter, labels | REPAIRED | §75.2 explicitly defines v and gives `v''=1/(theta log 3)>0`, v(0+)>0, v(3/4)<0, v(1)>0. The spacing argument now uses diameter `(Z-3)/4<2p`. All references to the proved proposition in §75 use “75.5P”, distinct from Assessment 75.5. |

## B. Remaining/new defects

### R1. MEDIUM — Boundedly many standard deviations do not make the per-shift success probability tend to one

At `notes.md:30042–30045`:

> “Widening the gap by O(sqrt(log L)) units of w pushes the residual small-prime mean far enough below lambda_theta log L that the per-shift fluctuation cost is not log 2 per coordinate, at no change of the exponent in (75.14).”

Put s=log L and lambda=lambda_theta. After widening by Delta, the residual Poisson mean is `lambda*s-1-Delta`; adding one or two large prime factors changes the threshold by only O(1). For `Delta=c sqrt(s)` with fixed c>0, the per-shift success probability tends to

`Phi(c/sqrt(lambda)) < 1`,

not one. For arbitrary `Delta=O(sqrt(s))`, bounded standardized displacement likewise cannot give convergence to one. The literal phrase “not log 2” can be true: the new cost is a *different positive constant*. That does not resolve the round-2 objection. Across independent residual coordinates the logarithmic cost remains Theta(J), of power theta, exceeding the candidate power `1-lambda` when theta>theta_*.

One can make the per-shift probability tend to one without changing (75.14)'s power, but needs `Delta/sqrt(s) -> infinity` and `Delta=o(s)`. Even that does not repair the independent joint event: its one-coordinate failure probability is `exp(-o(s))`, so the simultaneous cost still has power theta. To reduce this joint cost to power `1-lambda`, one needs a fixed-power-of-L reduction of the one-coordinate failure probability, requiring widening of order s in this independent Poisson picture, which changes the gap-cost power.

**Exact repair:** replace the quoted sentence by:

> Write s=log L. Widening by Delta=c sqrt(s), with fixed c>0, changes the residual per-shift LT probability to Phi(c/sqrt(lambda_theta))+o(1), not to one. Widening by Delta=s^(2/3) makes that probability tend to one and leaves the candidate exponent in (75.14) unchanged. Nevertheless, under independent residual Poisson coordinates, this still incurs a simultaneous-event cost exp{-L^(theta+o(1))}; no sublinear-in-s widening removes the joint fluctuation obstruction at the candidate power 1-lambda_theta. This is another reason the scalar gap calculation does not establish a joint LT or BLK mass.

The subsequent disclaimer must remain. This is not a demand that the missing multivariate construction now be supplied.

### R2. MEDIUM — The new review-history sentence misreports round 1

At `notes.md:29564–29567`:

> “both DEFECTIVE on the model subsections, with the proved core confirmed each time”

Round 1 explicitly found a **false proved identity** in Proposition 75.5 and an **invalid proof** of its multiplicity bound (items 6–7, both HIGH). Only the lemma and conditional implications survived then. The proposition was confirmed after the round-2 rewrite. The new sentence incorrectly restricts the first verdict to model subsections and retroactively certifies a false theorem.

**Exact repair:** replace the parenthetical beginning “both DEFECTIVE” by:

> both DEFECTIVE: round 1 also rejected the then-stated Proposition 75.5 and its multiplicity proof; round 2 confirmed the repaired proved core but rejected several model conclusions

The reference to “reviewed twice” is correct as a description of the two reviews preceding this draft; it is the characterization of their findings that is wrong.

### R3. MEDIUM — Withdrawn block-necessity language survives; size alone does not force a bounded-w prime

Two passages remain incompatible with the section's explicit structured-block examples:

* `notes.md:29718–29720`: “a block is a lower tail of omega with exponent delta(lambda_theta)”.
* `notes.md:30024–30028`: “A block … needs, by Lemma 75.1 and (75.4), a per-shift deficit … . The size constraint sum_i e^(-w_i)=1 per shift forces prime factors at bounded w but nothing else.”

Lemma 75.1 supplies a block-producing *sufficient family*, not a necessary deficit or a complete rate law. The repaired index-six family has full-generation blocks at arbitrarily large omega. Thus the second quotation is not licensed by either cited result; the first silently reinstates the withdrawn total-rate identification.

The size assertion is also false as a standalone implication: a primorial of size exp(L) has all its prime factors O(L), hence all w tending to infinity, while satisfying the logarithmic size constraint. Repeated factors give even simpler examples. For actual n+h the exact right side is `log(n+h)/log N`, with multiplicities counted; it is only `1+o(1)` on n asymptotic to N. Large primes are a possible size-feasible choice for this candidate, not forced by size alone.

**Exact repairs:**

1. Replace “whereas a block is a lower tail of omega with exponent delta(lambda_theta), which decreases” by:

   > whereas the low-omega block-producing family in (75.4) already has model exponent delta(lambda_theta), which decreases

2. Replace the sentences beginning “A block at modulus” and “The size constraint” by:

   > To model the low-omega family used in (75.4), seek a per-shift deficit (1-lambda_theta) log L while retaining a typical residual small-prime count. This is not a necessary condition for BLK. The exact size identity, counting prime factors with multiplicity, is sum_i e^(-w_i)=log(n+h)/log N=1+o(1) when n is asymptotic to N; it does not by itself force a prime at bounded w.

Keep the next sentence's one-/two-large-prime configuration as a **candidate**. Its size feasibility, positive gap width, boundary threshold, and candidate exponent are correct.

### R4. LOW — §75.9 omits important inputs/withdrawals and mislabels Assessment 75.5 as an equation

At `notes.md:30159–30161`, “and (75.5) on the specific product architecture” points to equation (75.5), not Assessment 75.5. The inventory also omits (CM), the principal new scalar-moment assumption. The withdrawal list covers the main HIGH failures but not all substantive restrictions now advertised as listed there.

**Exact repairs:** replace §75.9 item 1's first sentence by:

> Assessment 75.2 uses (EQ); Assessment 75.5 uses the specified iid-Poisson residue model, joint independence and restricted product architecture; Assessment 75.7 additionally assumes (CM), without a joint matching construction; Assessment 75.9 uses an explicitly artificial all-modulus Poisson witness proxy. None of these model transfers to the required arithmetic joint law is proved.

Append to item 2:

> Also withdrawn are the confinement-blind exact marginal failure law, the unrestricted comparison g(theta,theta')<=f(theta), the claim that the weighted absolute-error condition is necessary for every distribution-based argument, the inclusion of general squared Selberg weights in the bounded-coefficient class, and the identification of proxy successful-modulus counts with arithmetic representations.

The sentence about (EQ) being plausibly provable remains an assessment, not an input to any proved result.

### R5. LOW — “f<2/3 throughout” is broader than the computational assertion

At `notes.md:30143`, Computational 75.1 says “f<2/3 throughout”. The code asserts this only on its 19,999-point theta grid. The continuous global maximum is justified by the analytic branch calculation, not exhaustive real-variable computation.

**Exact repair:** replace that clause by:

> f<2/3 on the sampled theta grid

The rest of §75.8 matches the code. The index-six enumeration fixes the generator first, which is exhaustive up to permutation symmetry. The new r(beta) assertions are additional checks, not contradictory coverage claims.

## C. Independent verification

The requested isolated `check_bw` extraction passes, with block runtime **0.46 seconds**. It checks both calibration roots/signs, the finite signed-product and index-six enumerations, the restricted g comparisons, the formula crossing, the pointwise proxy samples, and both regressions. Output includes:

* theta_1=.335711; theta_hi=.989861; theta_*=.523495; theta_tilt=.7672; subfamily transition=.6872.
* grid max f=.58231 at theta=.6348; crossing with 1-lambda=.91763; index-six threshold=.04323.
* index-six tuple counts `{7:8, 19:240, 31:1248, 43:4800}`.
* a=43 echo `(count, block share, floor)`: `(2261,.2941,.2465)`, `(4958,.7096,.5558)`, `(3598,.7504,.3423)`.
* J=87, t_199=2, occupancy sum=227.

I separately checked the residual Poisson calculation using only scalar CDF calls under a 1 GiB address-space limit and one BLAS thread. With theta=3/4 and Delta=sqrt(s), the limit is .8869173322, not one; at s=100,1000,10000 the probabilities of residual+2<=lambda*s are .886996, .883248, .885448.

The other requested formula checks pass analytically:

* For rho<1 the polynomial failure bounds give logarithmic cost of order `L^(theta'+o(1)) log L`; at rho=1 it is `L^(theta'+o(1))`; for rho>1 the small-hit product expansion is valid. Differentiation gives `partial g/partial theta'=2-rho` in the middle branch, the optimum rho=2 beyond .6872287…, and the claimed global maximum. The confinement threshold .170… in the parenthesis is a sufficient range also for theta'<=theta; no false universal g<=f survives in the mathematical assessment.
* For the Poisson endpoint and k=2d, orthogonal-polynomial minimization gives atom at zero at most `(sum_{j=0}^d mu^j/j!)^(-1)`. For d=o(mu), the last term dominates and Stirling gives cost `d log(e mu/d)+O(log(d+1))`. This supports a scale, not the asserted existence in (CM), correctly left as an assumption.
* In the pointwise proxy, setting s=log log p gives `Q E min(1,3^K/Q)` with exponent beta, beta-delta(beta/log 3), or 2 according as beta is below log 3, between log 3 and 3 log 3, or above 3 log 3. Both endpoints are continuous. For prime moduli, writing u=log Q, the saturated high-scale contribution sums like `(log p)^2 integral du/u` from u of order log log p to u of order log p, hence order `(log p)^2 log log p`. Neither calculation asserts an arithmetic count or location theorem.

## D. Proved core: confirmed without heuristic input

* **Lemma 75.1:** condition on all but one nonzero signed coordinate. Its exponent is ±1, so the remaining factor is exactly uniform. Union over the 3^m-1 nonzero vectors proves the stated bound; squarefreeness gives the ratio-spectrum corollary.
* **Corollary 75.3:** the exact mechanism/subgroup union in §73 costs `exp(O(J log log L))`; (73.34) gives kappa>=|A|/2. Every hypothesis term therefore saves at least `[min((1-theta)/2,delta_B)+o(1)]J log L`. Using `J log L~L^theta/(2theta)` proves (75.8), absorbing the O(Z) exceptions. I rechecked the cited semigroup proof: replacing u^(3/4) by u^theta works for every fixed 0<theta<1 because u^(theta-1) decreases and `integral exp(-c u^theta) du` converges. No EQ or BR enters.
* **Theorem 75.4:** the defining inclusion BLK subset LT union STR yields at most 2^J events, all covered directly by (75.9). Absorbing this factor gives the corrected block hypothesis for every lambda>0. It uses neither block coverage nor a model estimate.
* **Proposition 75.5P:** compatible CRT tuples give exactly the shifted interval in the definition of the error. Bounded coefficients justify the absolute remainder. At p the assignment count is at most `J 2^(t_p-1)`. Brun–Titchmarsh with denominator `log(Z/(4p))`, the separate p=2 bound, the small-/medium-prime split, and diameter spacing for p>Z/8 give `sum(t_p-1)=O(J log log Z)`. This proves (75.13) and hence the proposition unconditionally. No assumed distribution estimate or moment model enters.

No changes to `notes.md` or `verify.py` are made. The remaining corrections are local: retain the proved core and qualified candidate calculations, but remove the false necessity/history assertions and state exactly what gap widening can and cannot accomplish.
