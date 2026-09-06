VERDICT: DEFECTIVE

The signed-product lemma and the two conditional exceptional-set implications survive. The section's advertised negative conclusions do not: there is a false proved identity, an invalid multiplicity proof, a second calibration root, an empty calibration event, and a broken moment calculation. Assessment labels do not cure false calculations or turn a restricted model into a universal obstruction.

## Defects and concrete repairs

1. **HIGH — Assessment 75.2 does not follow from (EQ); its upper-bound argument reverses the union bound, and its claimed rate is false in part of the stated iid model.**

   The sentence beginning “Upper bound: … under (EQ) the second is … for every fixed A by (75.2)” is invalid. An upper bound on hit probability exceeding one gives no upper bound on miss probability. (EQ) is also only stated below `(1-epsilon) log log H`, not throughout the upper tail, and unquantified asymptotic equidistribution cannot transfer arbitrarily small probabilities. Conditioning additionally on squarefreeness needs to be included in the equidistribution input used for the lower bound.

   There is a concrete structured-block counterexample to the asserted superpolynomial negligibility. Take primes `a = 7 (mod 12)` and the subgroup `K < G_a` of index six. It has odd order. Let exactly one of the m classes be a generator of G_a and all others lie in K. In `G_a/K = C_6`, the signed spectrum is contained in `{0,1,-1}`, while -1 has image 3. Thus these are full-generation blocks, for arbitrarily large m. Their iid probability is

   `m [phi(a-1)/(a-1)] 6^{-(m-1)}`.

   For `m = O(log log H)` this is a fixed power of `log H`, not smaller than every such power. Moreover, taking `m ~ (log log H)/6` and using squarefree Sathe–Selberg gives block mass at least

   `H (log H)^{-[delta(1/6) + (log 6)/6]+o(1)} = H (log H)^{-5/6+o(1)}`.

   Therefore (75.4) itself is incompatible with this model when `delta(theta/log 3) > 5/6`, namely `theta < 0.0432335221...` along these prime moduli. At theta = .01 its asserted exponent is .9481234820, greater than 5/6.

   **Replace Assessment 75.2, including its derivation, by:**

   > **Assessment 75.2 (a lower bound in the random-residue model).** Assume (EQ) quantitatively in the squarefree ensemble used below. Restricting to squarefree h with omega(h) = floor(log_3 a) - C, Lemma 75.1 and Sathe–Selberg predict
   > `# {h <= H : BLK_a(h)} >= H (log H)^{-delta(lambda_theta)+o(1)}`. (75.4)
   > Indeed the miss probability is bounded below by a positive constant for fixed sufficiently large C, and non-generation has probability at most omega(a-1) 2^{-m} = o(1). No matching upper bound, or superpolynomial bound on STR, follows from Lemma 75.1. The index-six construction described here gives an additional lower bound with exponent 5/6 for a = 7 (mod 12), so the equality version of (75.4) cannot hold for all theta. Any use below of an equality block-rate law requires a separate hypothesis (BR), restricted to the theta-range in which it is invoked.

   Include the index-six construction above immediately after this replacement. Replace “the structured blocks, heuristically negligible by Assessment 75.2” by “the structured blocks, whose joint contribution is separately assumed in (75.9)”. Replace the corresponding “genuinely rare” claim after Theorem 75.4 by an explicit additional coverage assumption, not a consequence of (EQ).

2. **HIGH — (75.6) has TWO roots, not one; “every theta > theta_1” is false even under the proposed rate law.**

   Set `v(t) = delta(t/log 3) - (1-t)/2`. Then

   `v'(t) = log(t/log 3)/log 3 + 1/2`, and `v''(t) = 1/(t log 3) > 0`.

   We have v(0+) = 1/2, v(.75) < 0, but v(1) = .0041547514974 > 0. The two roots in (0,1) are

   `theta_1 = .335711417418075`, `theta_hi = .989860615252697`.

   **Replace (75.6) and its uniqueness sentence by:**

   > `delta(lambda_theta) < (1-theta)/2 iff theta_1 < theta < theta_hi`, (75.6)
   > where theta_1 = 0.3357114174... and theta_hi = 0.9898606153... are the two roots of delta(theta/log 3) = (1-theta)/2. This calibration does not contradict the hypothesis for theta >= theta_hi.

   Replace every section-level headline/status assertion “false for every theta > theta_1” by “in tension with the independent bulk-block lower-bound model for theta_1 < theta < theta_hi”. Replace “covers every theta >= 2/3” by “includes 2/3 <= theta < theta_hi”. Replace “the literal (73.43) is the case delta_B=(1-theta)/2” by “up to a change in C absorbing O(J log log L), (73.43) is equivalent to this case”. The latter is not a literal identity because Delta_N is not exactly `(1-theta) log L`.

3. **HIGH — The proposed all-block calibration event is identically empty.**

   `A = empty, B = P_Z` really IS an instance of (73.43). But 3 belongs to P_Z, and `BLK_3` is empty: generation of `G_3 = {1,-1}` requires a prime class -1, which itself is a signed witness. Thus this instance has count zero for every N, and cannot falsify anything. Applying a growing-modulus block law independently to all these coordinates conceals this exact obstruction.

   **Replace “Take A=empty, B=P_Z” and the subsequent comparison through (75.5) by:**

   > Take A = P_{Z/log L}, B = P_Z minus A, and select F1 at every coordinate of A. Then |A| = o(J), |B| = (1-o(1))J, and every b in B has log b = (theta+o(1)) log L. The hypothesis bounds this mixed event by (75.5). Assume, separately, a joint-independence lower-bound model uniform over these growing families, with the F1 conditions on A costing exp(-o(J log L)). The bulk-coordinate lower bound (75.4) then predicts joint mass at least N exp(-(delta(lambda_theta)+o(1)) J log L). These two predictions conflict precisely in the interval (75.6). The all-block instance on P_Z cannot be used, since BLK_3 is empty.

   This names the extra mixed-coordinate assumption rather than treating marginal estimates as a growing-dimensional joint estimate. The prefactor calculation itself is correct: `C J log log L = o(J log L)`, so it cannot repair a fixed strict exponent gap.

4. **MEDIUM — The explanation of (75.9) changes its quantifiers and its counting variable. The choice of lambda is not logically forced.**

   With the stipulated full partition, `A=B_2=empty` forces `B_1=P_Z`; it gives no estimate for arbitrary subsets after dropping the other conditions. Also `n=24t+1` gives `h_b(n)=6t+(b+1)/4`, not an unrestricted `n+j_b` with the same cutoff. Equivalently use `m=(n-1)/4`, with `m=0 (mod 6)` and `0 <= m <= (N-1)/4`.

   **Replace the paragraph beginning “Its instance A=B_2=empty” by:**

   > Its instance A=B_2=empty is the pure joint lower tail on the full family B_1=P_Z, with the original condition n=1 (mod 24). On writing m=(n-1)/4, this is the family omega(m+j_b) <= lambda log L for m=0 (mod 6), 0 <= m <= (N-1)/4. An unrestricted-shift estimate, or an estimate for every proper subfamily without conditions on the complement, is a stronger hypothesis and is not asserted by this instance.

   **Replace “The choice lambda=lambda_theta+epsilon is forced by Lemma 75.1” and the rest of that paragraph by:**

   > The proved implication works for every lambda: STR is defined to cover the omitted blocks. Taking lambda above lambda_theta is a modeling choice intended to put most block mass into LT; it requires an additional block-coverage estimate. The natural lower-tail constant delta(lambda) concerns 0<lambda<1 only.

   Theorem 75.4 itself is correct: the events in the 2^{|B|} splittings cover the block event, and `2^{|B|} <= e^J` is absorbed by increasing C.

5. **HIGH — Assessment 75.5 computes a restricted product-model rate, not a ceiling for every sieve. It also gives an incorrect small-theta marginal failure rate.**

   `F_a subseteq M_a` supplies a valid particular majorant. It does not prove that every level-D majorant is at least M_a. Primes above z are not invisible to level-D divisibility statistics: a single such prime, or a product supported on a few coordinates, can have product <= D. For example a factor `1-1_{r|h_a}` with r=-1 (mod a), z<r<=D, is a failure majorant using a witness wholly outside the z-smooth part. The proposed universal optimality would require precisely the missing duality theorem, not just the inclusion of ratio spectra.

   With independent coordinates, `prod_a Pr(M_a)` is the expectation of this particular product majorant. For small success probabilities its logarithm is `-(1+o(1)) sum_a Pr(M_a^c)`, not automatically `-(1+o(1)) J Pr(M_a^c)` for an unspecified moving a. Its exponent f can be computed in the homogeneous iid-Poisson model, but provides no lower bound on all possible sieve majorants. Changing to composite moduli or Type I also changes the local group/witness model, not just J; no invariance of the exponent is established.

   Additionally the claimed `Pr(M_a)=L^{-(1-theta)delta(rho_theta)+o(1)}` fails when confinement dominates. In the iid-Poisson model, all classes lie in the quadratic-residue subgroup with probability `exp(-mu/2) = L^{-(1-theta)/2}`, and this always implies M_a. At theta=.1 the displayed prediction has exponent .6004154751, whereas this lower bound has exponent .45. This defect affects theta < .1701874772..., although it does not change the power f(theta)=theta for this branch.

   **Replace the opening of Assessment 75.5 through “Then:” by:**

   > We assess the specific product majorant prod_a 1_{M_a}, with the common smooth cutoff (73.36). Assume an iid-Poisson residue model for its smooth prime factors and joint independence at the logarithmic scale of the resulting product expectation. This is a restricted architecture, not an optimality theorem for level-N^{O(1)} majorants. In this model the hit probability is estimated at exponent scale by E min(1,3^K/a), K Poisson of mean (1-theta) log L. Such a two-sided hit estimate requires a random signed-product second-moment argument (compare (14.15)), not Lemma 75.1 alone. Then:

   Replace the first bullet's exact marginal formula by “For theta<theta_*, the model gives a positive power saving per coordinate (the exact failure exponent must include confinement), yielding power f(theta)=theta.” Replace the second bullet's “joint bound is at best” by “expectation of this product majorant has logarithm `-(1+o(1)) sum_a Pr(M_a^c)` and has power f(theta) in the model”. Replace the conclusion and coordinate-family sentence by:

   > The modeled product-majorant power has maximum 0.5823062800..., below 2/3. This does not exclude other sieve majorants, different allocations of level, or other coordinate families. No universal sieve ceiling is established.

   Also replace the last sentence “below f(theta) throughout” by “The proposed large-prime comparison in Assessment 75.7 is not established.” Independently, its formula `g(theta)=theta(1+1/log 3)-1` is NOT below f throughout (theta_*,1): the two meet at theta_tilt, and at theta=.9 they are .719215304 and .2. The machine check tests only the smaller interval below theta_2.

6. **HIGH — Proposition 75.5, as an exact proved statement, is false because the shifted endpoints are omitted.**

   Expansion produces the sum of F(m) over `h_0 < m <= N+h_0`, not `m<=N`. Counterexample: put q_0=3 so h_0=1, take every G_i identically one and D_i=1, put all local densities equal to zero, and take `F=1_{N+1}`. Then all the stated errors `E_F(N;d,b)` vanish; the claimed main term and remainder are zero; the left side is one.

   **Replace the definition of the error for use in Proposition 75.5 by:**

   > `E_F^{[h_0]}(N;d,b) = sum_{h_0 < m <= N+h_0, m=b (mod d)} F(m) - varrho_F(d,b) N`.

   Replace E_F by this interval error in (75.12) and its proof. If retaining the original error instead, add explicitly `2 h_0 sum_{d<=N^{1-eta}} m(d)` to the remainder bound, since endpoint removal costs at most 2h_0 per compatible tuple. This term is negligible at the eventual target scale once the repaired multiplicity bound is supplied, but it is not identically zero.

7. **HIGH — The proof of (75.13) misquotes Brun–Titchmarsh and then absorbs a term of the wrong order. The bound itself can be repaired.**

   For Z=1000, J=87. The shifts from q=31 and q=827 are 8 and 207, in the same class modulo p=199. The claimed maximum is `2J/(p-1)+1 = 1.878787... < 2`. This is an explicit counterexample. Brun–Titchmarsh involves `log(Z/(4p))`, not uniformly log Z. Also the displayed `exp(O(J sum 1/p + Z))` cannot be changed to `exp(O(J log log L))`: `Z asymp J log L`, which is larger.

   **Replace the last three sentences of the multiplicity proof by:**

   > Let t_p be the largest occupancy of a residue class modulo p among the shifts. The number of possible nonempty compatible index sets at p is at most J 2^{t_p-1}, since sum_r (2^{r}-1) <= sum_r r 2^{t_p-1}. For p>Z, t_p=1. For odd p<=Z/8, Brun–Titchmarsh in the progression modulo 4p, allowing the possible exceptional prime q=p, gives t_p << 1+Z/(p log(Z/(4p))). For p=2 use t_p<=J, and for Z/8<p<=Z the elementary spacing bound gives t_p=O(1). Summing for p<=sqrt Z costs O(J log log Z). For sqrt Z<p<=Z/8, split into p of size Z/2^k: the prime-count upper bound is O(Z/(2^k log Z)), and t_p=O(2^k/k+1). Summation over k costs O((Z/log Z) log log Z)=O(J log log Z). The remaining primes cost O(J). Hence sum_{p<=Z}(t_p-1) << J log log Z, and multiplication gives m(d)<=J^{omega(d)} exp(O(J log log Z)), which is (75.13).

   This proof is unconditional and does not require a heuristic about the prime shifts. The restriction to tuples satisfying the D_i bounds only decreases m(d).

8. **MEDIUM — The declared coefficient class does not include squared Selberg weights as asserted.**

   Squaring a divisor sum need not leave coefficients of absolute value <=1. For distinct primes r,s,

   `(1-1_{r|m}-1_{s|m})^2 = 1-1_{r|m}-1_{s|m}+2 1_{rs|m}`.

   It is nonnegative but has coefficient 2. Standard squared Selberg sums generally need divisor-function coefficient bounds; nonnegativity does not fix this.

   **Replace “Brun, Bonferroni, Rosser--Iwaniec, and (after squaring) Selberg weights are of this type” by:**

   > This definition covers bounded-coefficient divisor sums, including the relevant Brun/Bonferroni and linear-sieve weights. Squared Selberg weights need not belong to this class; their use requires a separate coefficient-weighted version of the remainder estimate.

9. **HIGH — Assessment 75.6 turns a sufficient absolute-error estimate into a necessary condition and a universal exclusion.**

   Proposition 75.5 is an expansion, not “the only way” distribution information can enter a correlation. Its upper bound on |R| does not imply that the displayed weighted-error sum must be small: coefficients can vanish, errors can cancel, and the multiplicity bound need not be sharp. Fixed-power EH estimates alone indeed do not supply the displayed exponential-scale sufficient bound, but this does not prove every EH-type input useless in every possible argument. The original W2 explicitly and correctly limited itself to evaluation-based technology.

   **Replace “is the only way” by “describes one standard absolute-error expansion through which”. Replace the sentence introducing the error condition by:**

   > Using the absolute-value multiplicity bound, a sufficient condition for an error at most N exp(-cJ log L) is the following weighted exponential-saving estimate (with the interval-error convention of Proposition 75.5).

   **Replace the categorical sentences beginning “an exponential saving; every Elliott--Halberstam-type hypothesis” and the final “task's conditional question” conclusion by:**

   > Fixed-power logarithmic level-of-distribution bounds alone do not establish this sufficient estimate. The expansion also leaves J-1 sieve coordinates, so removing one factor does not resolve this particular dimension-versus-level problem. This is an obstruction to this absolute-error evaluation architecture, not a theorem excluding every use of a level-of-distribution hypothesis. H^+_LT is a separately stated sufficient joint-correlation hypothesis.

   The integer-frame estimate at the end is valid at exponent scale: `sum_{d<=X} J^{omega(d)} <= sum_{d<=X} d_J(d) <= X(1+log X)^{J-1} = N^{1-eta+o(1)}` for X=N^{1-eta}. This does not validate the necessity/universality language.

10. **HIGH — Assessment 75.7 has a square-root error and a false moment-problem ingredient. Its theta_2 and large-prime obstruction are unsupported, not merely unproved arithmetic gluing.**

    From its own `k=O(e^w)`, `mu asymp J`, and `epsilon lesssim sqrt(k/mu)`, the scale is `e^{w/2}/sqrt J`, NOT `e^w/sqrt J`. With this corrected profile,

    `integral_0^{log J} min(1,c e^{w/2}/sqrt J) dw = O_c(1)`,

    not `(1/2+o(1)) log J`. The latter integral is correctly evaluated for the incorrectly chosen profile. The formula for theta_2 solves the stated deficit equality, but that equality has lost its premise. Likewise, writing the residual length as `(.5 log J)-w_1` algebraically gives `w_1=[theta(1+1/log 3)-1]log L`; this is not a derivation of a certifiable exponent without the missing statistical extremum.

    More fundamentally, “k moments cannot detect” is not a general theorem with the stated meaning. Matching even the first moment detects a changed mean. If the intended meaning is that a matching-moment measure can place substantial mass at a deficient value, its permissible mass must be quantified. The claimed classical ingredient, mass `>>1/k` ANYWHERE within `mu +/- c sqrt(k mu)`, is false. In a Poisson law with mu sufficiently large compared with k, the centered 2r-th moment is `(1+o(1))(2r-1)!! mu^r`. A measure matching the first k moments and putting mass alpha at `mu-c sqrt(k mu)` obeys, for 2r<=k,

    `alpha <= (1+o(1))(2r-1)!!/(c^2 k)^r`.

    Taking `r=floor(c^2 k/4)` (fixed small c>0) makes this exponentially small in k, not `>>1/k`. This already defeats the alleged univariate theorem before multivariate gluing or size constraints arise.

    **Replace Assessment 75.7, including both bullets and the claimed classical ingredient, by:**

    > **Assessment 75.7 (an unresolved statistics-model obstruction).** At prime parameter w, a product-level D=N^{O(1)} permits O(e^w) prime indicators. This does not by itself identify the optimal probability of a joint lower-tail event among measures matching all available divisibility statistics. A proof would require a correctly quantified truncated-moment extremum and a compatible multivariate construction respecting the size constraints. Neither is supplied here. In particular, no free deficit of (theta/2) log L, no threshold theta_2, and no exponent theta(1+1/log 3)-1 is established.

    Delete the status claim that the deficit is “invisible to every majorant”, the corresponding section heading, and any assertion that this is “sharper than” the existing walls. Merely adding “heuristic” does not repair the false univariate calculation.

11. **HIGH — Assessment 75.9 does not establish the claimed pointwise short-interval necessity.**

    There are several independent errors:

    * The worst-case bound `omega(h) << log p/log log p` yields `3^{omega(h)} = p^{O(1/log log p)}`, not `(log p)^{log 3+o(1)}`. The latter uses a typical-value assertion, and replacing a typical value by an expectation is another unjustified step (`E 3^{omega(h)}` has logarithmic exponent 2 in the usual integer model, not log 3).
    * Lemma 75.1 is squarefree/iid. Actual h_q can have repeated factors, for which the signed alphabet has `prod_{r^e || h_q}(2e+1)` choices, and higher exponents need not be uniform modulo q. The claimed pointwise `3^{omega(h_q)}/q` bound does not follow.
    * A polylogarithmic EXPECTED NUMBER of successful moduli among q<=p says nothing about their locations. They could all occur at q of polynomial size. It does not imply a witness with q<=polylog(p), or force every equidistribution strategy into an interval of polylogarithmic length.
    * The blanket statement about no factorization information below x^.525 confuses a prime-gap benchmark with arbitrary factorization statements. Even intervals of length O(sqrt x) contain a square; much narrower or differently formulated factorization questions cannot all be excluded by this benchmark.

    **Replace Assessment 75.9 from “By Lemma 75.1 and omega(h) ...” to its end by:**

    > Restricting the Type II search to q<=Q=(log p)^{O(1)} makes it a factorization/witness problem in this polylogarithmic interval. Restricting the Type I parameter similarly gives a polylogarithmic number of terms of its progression. We know no pointwise result establishing the required witness for every p in these restricted searches. This does not show that every pointwise a-frame argument must use such a short search. A sparse expected total number of representations, even if separately justified, imposes no bound on the location of a witness and is not an impossibility theorem.

12. **MEDIUM — check_bw is green but misses precisely the false extrapolations; its coverage description needs correction.**

    The exact enumeration and finite a=43 inequalities are correctly implemented. The echo is explicitly empirical, not an application of iid probability to actual factor classes. The numerical f calculation is internally consistent. But the bisection brackets only the first root, its sign checks stop at .9, and the g<f checks use only four points below theta_2. They cannot validate the assertions “unique root”, “all theta>theta_1”, or “below f throughout (theta_*,1)”. The theta_2 identity verifies algebra on an invalid premise, not the moment claim.

    **For the later repair of verify.py:** add a second root computation on (.9,1), assert both sign changes (including theta=.99), and change the (75.6) comment to the bounded interval. Remove theta_2 and the large-prime comparison from the list of validated mathematical conclusions, or clearly label them as calculations of withdrawn candidate formulas. Add the finite endpoint and Z=1000,p=199 regression counterexamples from items 6–7 if those propositions are replayed. Do not preserve the currently false assertions merely because the selected grid points pass.

    **Replace Computational 75.1(ii) by:**

    > (ii) numerical evaluation of the two calibration roots, theta_* and theta_tilt, and of the explicitly defined restricted-model function f; continuity checks and a fine-grid maximum calculation. These checks validate the formulas as numerical formulas, not the proposed universal sieve or truncated-moment obstruction.

13. **LOW — Local scope/label cleanup.**

    The deterministic parenthesis after Lemma 75.1 states `Rat={g^j:|j|<=omega(h)}` without retaining squarefreeness. **Replace “all prime factors in {g,g^{-1}}” by “for squarefree h, all prime-factor classes in {g,g^{-1}}”**. With multiplicities the endpoint is Omega(h), not omega(h). Lemma 75.1 and its explicitly squarefree corollary themselves are correct.

    **Replace the Status sentence listing Assessments by “All items labelled Assessment are heuristic/model discussions; only the explicitly labelled conditional implications and elementary statements are proved, after the repairs recorded here.”** The current list omits Assessments 75.5 and 75.9. Distinguish the duplicate “Assessment 75.5” and “Proposition 75.5” numbering. In check_bw's m=1 comment replace “exactly the two classes” by “the two exponent choices refer to the same class”.

## Independent checks and surviving mathematics

* I read §73, (73.34)–(73.44), Lemma 70.1, §§14.4–14.5 (also the relevant signed second-moment lemma in §14.6), Outcome 35, and the prime-to-integer Rankin transfer in the cited paper.
* Lemma 75.1 is valid: in every nonzero vector there is an exponent +1 or -1, each a bijection on the group; conditioning on all other independent factors gives exactly uniform product. The zero vector cannot hit -1 for odd a. The squarefree corollary and its `1-3^{-C}` lower bound are correct under their stated random-residue assumption. Pairing epsilon with -epsilon even improves the union bound by a factor two, but is not required.
* Corollary 75.3 is a valid proved implication, independent of (EQ), (BR), or any heuristic assessment. From (73.34), `kappa>=|A|/2`; Delta_N is positive eventually and equals `(1-theta)log L+O(log log L)`. Thus its exponent is at least `[min((1-theta)/2,delta_B)+o(1)] J log L`. The union cost is `exp(O(J log log L))`, and `J log L=(1+o(1))L^theta/(2theta)` gives exactly (75.8). The O(Z) small-prime exceptions are absorbable. The cited Rankin transfer works for every fixed 0<theta<1 because u^{theta-1} decreases and the resulting exponential-tail integral converges. Theorem 75.4 is also valid, as explained in item 4. No heuristic is smuggled into either proof; their hypotheses are explicitly open.
* In the homogeneous iid-Poisson hit model, `E 3^K/a = exp(2mu)/a = L^{2(1-theta)-theta}` at exponent scale. Maximizing the truncated tilted moment puts its saddle at K=3mu, giving theta_tilt and f(theta)=2(1-theta) beyond it. At theta_* the middle branch has delta(1)=0. At theta_tilt it has rho=3 and equals 2(1-theta_tilt). Both continuity claims for this defined function are correct.
* Independent SciPy computations: theta_* = .523494641959496; theta_tilt = .767216486288474; maximum f = .582306280029209 at theta=.634815405644086; f(2/3)=.576610329954092; f(3/4)=.496883936376947; delta(lambda_{3/4})=.0567214332658671. The withdrawn candidate theta_2 evaluates to .709099549295553. These agree with the text's displayed truncations/roundings; the substantive failures are not roundoff.
* I ran the requested isolated check_bw command successfully. All exact enumeration and finite-echo assertions pass. The a=43 rows `(count, block share, empirical floor)` are `(2261,.2941,.2465)`, `(4958,.7096,.5558)`, `(3598,.7504,.3423)` for m=1,2,3. No dense arrays or unbounded computation were used.

No edits to notes.md or verify.py are made by this review. The verdict remains DEFECTIVE rather than SOUND-AFTER-REPAIRS because repairing the section requires withdrawing/restricting several advertised conclusions, not merely correcting their proofs or constants.
