VERDICT: DEFECTIVE

Reviewed detached HEAD `4e5fdf9` in `/tmp/es-sec75` only. Neither `notes.md` nor `verify.py` is changed.

The rewrite repairs the conditional theorems and the multiplicity argument. It does **not** repair every first-round item: the new moment assertion is false as a rigorous statement, the large-prime construction still does not establish its advertised statistics-model obstruction, and the new pointwise expectation calculation fails even in its own Poisson proxy. There are also several narrower scope/formula errors. Calling a calculation heuristic does not make an incorrect calculation correct.

## A. Disposition of all 13 first-round items

“PARTIALLY” means that the principal correction was made but a material remnant or replacement error remains. References N1–N9 below give exact repairs.

| First-round item | Disposition | Reason |
|---|---|---|
| 1. Block upper bound, EQ, structured blocks | PARTIALLY | Assessment 75.2 is now genuinely lower-bound-only; EQ names the squarefree ensemble, and the union bound/non-generation argument works. The index-six exponent and threshold are correct in that ensemble. But the new deterministic construction omits squarefreeness (N1), and the paragraph after Theorem 75.4 again attributes tail coverage to BR, which does not supply it (N8). |
| 2. Two calibration roots | REPAIRED | Both roots and the bounded conflict interval are correct; the absorption of the difference between Delta_N and `(1-theta) log L` is explicit. There is a minor ambiguity in which function is being described as convex (N9), not a wrong root or interval. |
| 3. Empty all-block calibration | REPAIRED | BLK_3 is indeed empty. The replacement `A=P_{Z/log L}`, all F1, and bulk B has `|A|=o(J)` and `|B|~J`. The indispensable mixed-coordinate lower-bound/independence assumptions are now explicitly additional assumptions, not consequences of marginal EQ. |
| 4. Full-family quantifiers, shift variable, lambda | REPAIRED | The full-family-only instance and `m=(n-1)/4`, `m=0 mod 6`, cutoff `(N-1)/4` are correct. Theorem 75.4 is valid for every stated `lambda>0`; no coverage estimate is needed for that implication. The subsequent BR modeling sentence remains defective, as recorded under item 1/N8. |
| 5. Universal sieve ceiling and marginal failure law | PARTIALLY | The assessment now explicitly restricts the architecture and withdraws the exact confinement-blind failure exponent. The formulas for g, its derivative and global maximum are correct. However, its product-log identity is false on the first branch, and its claim at rho=1 is false (N2). Computational 75.1 also asserts the false unrestricted inequality `g<=f` (N3). |
| 6. Shifted endpoint in Proposition 75.5 | REPAIRED | `E_F^[h0]` is defined on exactly the interval produced by expansion. The identity and absolute remainder bound are now correct. The endpoint regression passes. |
| 7. Brun–Titchmarsh/multiplicity proof | REPAIRED | The `J 2^(t_p-1)` bound, the `log(Z/(4p))` denominator, separate treatment of 2, dyadic medium-prime sum, and final `O(J log log Z)` bound are valid. The final spacing sentence needs “diameter” rather than “shifts are at most Z/4” (N9); this is not a failure of the bound. |
| 8. Squared Selberg coefficient class | REPAIRED | Bounded coefficients are part of the definition and squared Selberg weights are explicitly excluded unless a coefficient-weighted version is proved. |
| 9. Necessary vs sufficient absolute error; universality | PARTIALLY | The body now calls the weighted estimate sufficient and limits the conclusion to an absolute-error architecture. Status (d) nevertheless still says that this architecture “would need” exponential saving (N8), reintroducing the necessity language. |
| 10. Truncated-moment/large-prime argument | PARTIALLY | The square-root error, free-deficit formula and theta_2 are explicitly withdrawn. The two displayed moment-cost expressions are reasonable Gaussian exponent-scale templates, not the rigorous statement actually written (N4). The proposed gap has the stated *formal window-cost exponent* in the appropriate range, but neither a simultaneous lower-tail/block event nor a level-statistics matching measure has been constructed (N5). |
| 11. Pointwise witness/location argument | PARTIALLY | The worst-case omega bound and forced-polylogarithmic-interval conclusion are withdrawn. The replacement uses the right untruncated moment `E 3^omega ~ (log p)^2`, but incorrectly interchanges it with the saturated expectation at the lower advertised scales, and leaves the modulus family/counting object ambiguous (N6). |
| 12. check_bw coverage | PARTIALLY | The code now checks both roots/signs, the structured tuples, both regressions, and a finite occupancy sum. It passes. Its *correctly restricted* g comparison does not check the unrestricted g<=f claimed in §75.8; that latter assertion is false (N3). Numerical checks do not validate the new moment or pointwise claims. |
| 13. Local labels/squarefreeness/comments | PARTIALLY | The first deterministic example retains squarefreeness, the Assessment list is complete, and the m=1 comment is fixed. But the new second example loses squarefreeness (N1), Assessment/Proposition 75.5 still share a number, and Status's “every HIGH and MEDIUM” repair assertion is inaccurate (N8–N9). |

## B. New defects and exact repairs

### N1. MEDIUM — The new index-six construction needs squarefreeness explicitly

At `notes.md:29613–29623`, “exactly one prime class of h is a generator ... full-generation block for every omega(h)” is false without a valuation restriction. Take `a=7`, `K={1}`, `h=3^3=27`. There is exactly one prime-factor class, a generator, but `3^3=-1 mod 7` is in the ratio spectrum. The current paragraph puts “For squarefree h” inside example (i), not in the hypotheses of (ii).

Also `6 | a-1` implies odd order of K only with the standing `a=3 mod 4` convention. Under that convention there is no odd-order error: together these conditions say `a=7 mod 12`. If the passage were read for all odd primes, `a=13`, generator 2 and another class -1 in K would refute it.

**Exact repair:** replace the opening of (ii) through “then K(h)=G_a” by:

> (ii) For squarefree h and primes a congruent to 7 modulo 12, let K<G_a be the subgroup of index six. Its order (a-1)/6 is odd. If exactly one prime-factor class of h is a generator of G_a and every other prime-factor class lies in K, then K(h)=G_a.

Keep the subsequent probability and optimization explicitly in the squarefree iid-residue model. The quotient argument, probability `m phi(a-1)/(a-1) 6^{-(m-1)}`, minimum `5/6` at `lambda=1/6`, and threshold `0.043233522112864...` then pass.

### N2. MEDIUM — The product-log expansion is used where the hit probability is not small

At `notes.md:29824–29830`, `log E prod 1_M = -(1+o(1)) sum Pr(M^c)` requires `Pr(M^c)=o(1)`, hence fixed `rho>1`. For `rho<1`, Lemma 14.6 makes failure polynomially small, so hit tends to one: the displayed right side is of order minus the number of coordinates, while the left side is of order minus that number **times log L**. At `rho=1`, failure is not a positive power of L: a Poisson count below its mean by more than a slowly growing amount has asymptotic probability 1/2 and misses with probability tending to one. The opposite side of the Poisson transition hits with probability tending to one by (14.15), giving a nontrivial limiting failure probability, not polynomial decay.

These mistakes do not change g at power-of-L scale.

**Exact repair:** replace the sentence starting “for rho<=1” and the following product-log sentence by:

> For fixed rho<1, the iid model gives `L^{-C} << Pr(M_a) << L^{-c}` for some constants C>=c>0; no exact failure exponent is asserted. At rho=1 the failure probability stays of constant order. For fixed rho>1, the hit probability tends to zero and log E product_a 1_{M_a}=-(1+o(1)) sum_a Pr(M_a^c). For rho<1 use instead sum_a log Pr(M_a)=-L^{theta'+o(1)} log L, and for rho=1 use -L^{theta'+o(1)}. These all give the first branch g=theta' at power-of-L scale.

The low-dimensional single-class sieve remark has the correct dimension scale: `sum_{a in P_Z}1/(a-1)=(1/2)log log Z+O(1)`, hence its elementary product-density saving has logarithm of order `log L log log L`, not `L^c`. It illustrates the architectural restriction; it does not prove optimality for other sieves.

### N3. MEDIUM — §75.8 claims a false g<=f check which the code correctly does not perform

At `notes.md:30092`, the unqualified `g(theta,theta')<=f(theta)` is false. For example,

```
theta = .9
optimal theta' = 1 - .9/(2 log 3) = .590392...
g(theta,theta') = .43216322178569
f(.9) = .2.
```

On the middle branch, differentiation does give `dg/dtheta'=2-rho`. Thus full-family optimality ends at `theta_two=.68722872735041`, and the optimizing rho=2 thereafter is correct. The tilt branch `2-theta-theta'`, continuity, and the *global* maximum .58230628 are all correct. The code implements precisely these restricted comparisons; no bug in that implementation was found.

**Exact repair:** replace the clause in Computational 75.1(ii) by:

> g(theta,theta')<=f(theta) on the sampled grid for theta<2 log 3/(1+2 log 3), and g(theta,theta')<=max_u f(u) on the whole sampled grid.

### N4. HIGH — “Rigorous Chebyshev–Markov” is not a valid exact assertion as written

At `notes.md:29980–29989`, neither arbitrary independent-indicator moments nor a finite number k of matched moments automatically gives the two exact exponential bounds displayed there. Even for **k=2** there is an explicit sum-of-indicators counterexample.

Let M=9901. With probability .9901 choose uniformly a 100-element subset of `{1,...,M}` and set exactly its indicators to one; otherwise set every indicator to zero. The sum S has `E S=99.01` and the first two moments of `Binomial(9901,.01)` (indeed the indicators are pairwise independent). Set `mu=99.01`, `t^2=mu`, so the deficit event is S=0. Its probability is `.0099`, whereas the purported rigorous bound is

```
exp[-(2/2) log(e t^2/2)] = 2/(e*99.01) = .00743115728051.
```

Odd k is another unhandled issue, with more than a constant-factor consequence. For k=1 let all M indicators equal the same Bernoulli(1/2) variable. Their sum matches the first moment of the independent model, mu=M/2, but has probability 1/2 of being zero, whereas the displayed cost predicts `sqrt(2/(e M))`, tending to zero. The Gaussian moment/Stirling calculation explains the *leading costs*, with prefactors and regimes, but is not the written theorem. The lower-direction bullet is explicitly called a model ingredient, which is an improvement; it still needs a law, support and asymptotic regime. Its parenthetical “for t^2<=k the mass is Gaussian, e^{-t^2/2}” also suppresses relevant Christoffel prefactors: at the mean, the Gaussian degree-k Christoffel mass is of order `k^{-1/2}`, not one.

**Exact repair:** replace the two bullets by:

> (upper direction, rigorous) Write M_{2r}=E(S_ind-mu)^{2r} for the centered moments of the specified independent reference law. If S matches its first k moments with k>=2, then for t>0,
> `Pr(S<=mu-t sqrt(mu)) <= min_{1<=r<=floor(k/2)} M_{2r}/(t^2 mu)^r`.
> Gaussian moment asymptotics, only in a regime where they hold uniformly through the optimizing even order, give leading costs t^2/2 and (k/2)log(e t^2/k), with rounding, prefactors and asymptotic errors; these are not exact bounds for arbitrary indicator sums.
>
> (lower direction, additional model assumption CM) For the specified Poisson reference law, even k=o(mu), feasible x=mu-t sqrt(mu)>=0, and t^2 much larger than k, assume a measure on nonnegative real counts matching the first k moments and putting mass at least `exp[-(k/2)log(Ct^2/k)-O(log k)]` at x. This assumption is not a construction on integer residue patterns or a multivariate matching theorem. No prefactor-free formula is asserted in the central regime.

A useful independent check is the Poisson endpoint Christoffel bound: with `k=2d`, any matching measure has atom at zero at most `[sum_{j=0}^d mu^j/j!]^{-1}`. For `d=o(mu)` its logarithmic cost is `d log(e mu/d)+O(log(d+1))`. This supports the *scale* of the proposed deep-tail model input, not the general exact assertion.

### N5. HIGH — The gap arithmetic is valid only in a specified range, and is not a joint block-model obstruction

At `notes.md:29995–30023`, let `s=log L`, `lambda=theta/log 3`, and `w_b=1+(1-lambda)s`. Then

```
log J - w_b = (theta+lambda-1)s - log s - log(2 theta) - 1 + o(1).
```

For fixed `theta>theta_*`, the gap is below the sieve boundary and `e^{w_b}=e L^{1-lambda}=o(J)`. Integrating the proposed unit-window costs gives, up to constants,

```
(1/2) integral_1^{w_b} e^w (log J-w) dw
  ~ (1/2)e^{w_b}(log J-w_b+1)
  = L^{1-lambda+o(1)}.
```

Thus (75.14)'s **formal cost exponent** is correctly computed in that range. But the gap itself has positive width for **every** `0<theta<1`, since `1-lambda>0`. The threshold is the gap's position relative to `log J`, not its width.

Size feasibility alone is not a defect: two primes of sizes near `N^{1/2}` and a subpower cofactor can fit. Three primes all at least `N^{1/e}` cannot fit (`3/e>1`), but “at most three” includes the feasible one-/two-prime cases. It would be clearer to say at most two. Also size feasibility is not existence of the simultaneous arithmetic tuple.

The substantive gap remains: scalar moment-matching measures for aggregate window counts do not yield a measure matching **all weighted level-D joint divisibility statistics**, with the simultaneous block/lower-tail event having the asserted mass. The text acknowledges that gluing is undone, but still concludes a ceiling for “level-N^{O(1)} majorant methods” *in that very statistics model*, and calls the configuration “cheapest” without an optimization argument.

There is an additional missing event cost even in the simple independent residual Poisson picture: after deleting exactly this gap, each cofactor has mean `lambda log L-O(1)` small prime factors. With one or two large primes added, the probability of `omega<=lambda log L` tends to 1/2, not one. Across J independent residual coordinates this costs `exp[-(log 2+o(1))J]`, whose power is theta, larger than `1-lambda`. The gap imposes the requested deficit **in the mean**, not the simultaneous lower-tail event. The signed-product transition likewise prevents simply equating a mean deficit with a joint BLK event. A proposed adversarial coupling might change this, but constructing/assuming that coupling is an additional substantive ingredient.

**Exact repair:** replace the paragraph beginning “The cheapest” through the claimed whole-track ceiling by:

> A size-feasible candidate has one or two primes at least N^{1/e} per shift and a subpower cofactor, with a gap `[1,w_b]`, `w_b=1+(1-lambda_theta)log L`. This gap has positive width throughout 0<theta<1; it lies below the sieve boundary with k=o(J) precisely for fixed theta>theta_*. Summing the assumed scalar window costs in that range gives the candidate exponent `L^{1-lambda_theta+o(1)}`. This calculation does not establish the mass of a simultaneous LT or BLK event: residual small-prime fluctuations and all joint level-D constraints still have to be handled. Neither cheapest-configuration optimality nor a ceiling for the full statistics model follows here. Numerically, `1-lambda_theta<f(theta)` on `(theta_*,0.9176325891...)`; this is a comparison of candidate formulas only.

The statement that multivariate gluing is not done should remain. Remove Status (e)'s certifiability claim accordingly. The restricted product-majorant maximum in Assessment 75.5 survives independently.

### N6. HIGH — The replacement pointwise expectation calculation fails at its advertised lower endpoint

At `notes.md:30057–30070`, knowledge of `E 3^omega ~ (log p)^2` does not permit replacing `E min(1,3^omega/Q)` by `E 3^omega/Q` as soon as `Q>=(log p)^2`. This repeats, in a new setting, the untruncated-tilt error discussed earlier in the notes.

Even take the favorable **all-integer-modulus toy proxy**, so there are order Q candidate moduli in a dyadic interval, and put `s=log log p`, `K~Poisson(s)`, `Q=(log p)^beta`. Then the dyadic expected-success proxy has exponent

```
Q E min(1,3^K/Q) = (log p)^{r(beta)+o(1)},
r(beta) = beta                         (beta<=log 3),
          beta-delta(beta/log 3)       (log 3<beta<3 log 3),
          2                            (beta>=3 log 3).
```

At the stated lower endpoint beta=2, the exponent is `1.7298309898623`, **not 2**. The untruncated tilt sits at `K~3s`, and is not preserved until beta reaches `3 log 3=3.2958368660043`. Constant-asymptotic assertions also require more than exponent-scale modeling.

The passage must specify whether q ranges over prime coefficients of the section's a-frame or all integer moduli. For prime q, there are only order `Q/log Q` coordinates; for polynomial Q the dyadic expectation in this proxy is order `log p`, not `(log p)^2`. Summing the prime-modulus proxy across scales gives order `(log p)^2 log log p`, rather than `(log p)^3`. For all integer moduli, an additional composite-group/witness model is needed, and counting successful moduli is not automatically counting Elsholtz–Tao representations. The scalar all-modulus proxy does have total power 3 when polynomial scales are included, but that does not validate the asserted identity with the arithmetic count or “every scale.”

**Exact repair:** replace the expectation paragraph through the blanket “no analytic pointwise theorem” claim by:

> In an explicitly all-integer-modulus iid proxy, polynomial dyadic scales Q=p^alpha, with fixed 0<alpha<1, give order `(log p)^2` expected successful coordinates from the untruncated moment `E 3^omega ~ (log p)^2`. Extending this proxy over order log p such scales gives total order `(log p)^3`. This is not an identification with the number of arithmetic representations. At polylogarithmic Q the expectation must instead be computed with the truncation `min(1,3^omega/Q)`; it is not uniformly `(log p)^2`. Restricting to prime moduli also introduces their density factor. None of these expected counts gives a pointwise location theorem or forces a witness into a polylogarithmic interval. We know no pointwise theorem supplying the required moving-modulus witness for every p.

Retain the useful distinction between voluntarily choosing a polylogarithmic search and being forced to do so. Change the heading/Status (f) from an assertion that actual witnesses “are spread” to a description of this explicitly qualified proxy.

### N7. LOW — A finite occupancy check does not assert exact t_199=2

The repaired proof is valid. At Z=1000 the actual value is exactly 2, and the complete occupancy sum is 227. The code asserts `t199>=2`, which is sufficient to reproduce the old bound's counterexample, but not literally an exact-value assertion. It also tests the occupancy big-O inequality at only one Z, not an asymptotic theorem.

**Exact repair text for Computational 75.1(iv):**

> the occupancy counterexample t_199>=2 at Z=1000, and the finite check `sum_{p<=1000}(t_p-1)=227<6J log log 1000`; the asymptotic occupancy bound is supplied by the proof, not by this finite test.

Alternatively a later code revision can assert `t199==2` as well. Permuting the distinguished generator need not be enumerated in the index-six test: signed products and generation are symmetric, so its representative-first enumeration is exhaustive up to this harmless symmetry.

### N8. MEDIUM — Status and the BR paragraph still overstate what was repaired/assumed

At `notes.md:29796–29801`, BR was defined only as a possible equality for the **total** block rate. Such an equality does not say that the portion above `lambda_theta+epsilon` has negligible mass: both parts could have the same exponent. Also “nothing below uses BR” conflicts with the explicit subsequent “under BR” explanation.

Status (d)'s “would need” is still stronger than the sufficient absolute-error estimate proved in the body. Status (e) and (f) report the unsupported model conclusions in N5–N6, and the claim that every HIGH/MEDIUM first-round item is repaired is not accurate. These are not heuristics entering Corollary 75.3 or Theorem 75.4; they are inaccurate descriptions of the assessment outcomes.

**Exact repairs:**

* Replace the paragraph after Theorem 75.4 by: “The implication holds for every lambda>0. Taking lambda>lambda_theta includes the particular low-omega family used to prove the lower bound (75.4). It does not show that most blocks lie there: this needs a separate structured-block coverage estimate, not merely the proposed equality BR for the total block rate. The required joint STR estimate is assumed directly in (75.9). The natural lower-tail constant delta(lambda) concerns 0<lambda<1.”
* Replace Status (d)'s necessity clause by: “the absolute-error expansion gives a sufficient weighted exponential-saving condition; fixed-power logarithmic distribution estimates alone do not establish that condition.”
* Replace Status (e) by: “a formal scalar-window gap calculation suggests the candidate exponent 1-theta/log 3; no matching joint statistics-model obstruction is established.”
* Replace Status (f) by: “a qualified all-modulus proxy gives a polylogarithmic expected witness count, without a pointwise location consequence.”
* Replace “every HIGH and MEDIUM item there is repaired in this text” by: “the first draft's erroneous conclusions are withdrawn or restricted below; further unresolved model steps are explicitly separated from the proved implications.” Update §75.9 to include withdrawal of the unqualified moment bounds, gap-model certifiability claim, and uniform every-dyadic-scale witness count.

### N9. LOW — Three local wording/label repairs

1. At `notes.md:29697`, use the function whose sign is actually relevant: “For `v(theta)=delta(theta/log 3)-(1-theta)/2`, one has `v''=1/(theta log 3)>0`, `v(0+)=1/2`, `v(.75)<0`, and `v(1)=.0041547514974...>0`; hence there are exactly two roots.” The present “left side” is ambiguous between delta, which never becomes negative here, and v.
2. At `notes.md:29934`, replace “the shifts are at most Z/4<2p” by “the diameter of the shift set is at most `(Z-3)/4<Z/4<2p`.” Individual shifts are bounded by `(Z+1)/4`, not Z/4. The claimed `t_p<=2` still follows exactly from the diameter bound.
3. Distinguish the two 75.5 labels, e.g. rename “Proposition 75.5” to “Proposition 75.5P” consistently in §75 and the computational description. Do not claim this first-round label cleanup has already occurred.

## C. Independent verification and surviving results

### Proved statements

* Lemma 75.1 is correct: every nonzero signed vector contains an exponent +1 or -1, giving a uniform factor after conditioning. The zero vector cannot hit -1. Its squarefree corollary follows.
* For the intended `a=3 mod 4` primes, `6|(a-1)` gives `a=7 mod 12`, odd-order K, and the quotient involution is 3 in C_6. One generator and the other squarefree classes in K gives quotient support `{0,1,-1}`, so the corrected structured construction works.
* BLK_3 is empty, including nonsquarefree integers: generation requires a prime class -1, and exponent one is already a witness. Lemma 74.2's K_1 proof and Lemma 70.1 agree. There is no obstruction of this kind to the replacement mixed calibration instance.
* From (73.34), `kappa>=|A|/2`. Hence every term in Corollary 75.3 has saving at least `[min((1-theta)/2,delta_B)+o(1)] (|A|+|B|)log L`. The union costs `exp(O(J log log L))`; (73.38) gives `J log L~L^theta/(2theta)`. This proves exactly (75.8). The O(Z) exceptions are negligible. I checked the Rankin transfer in Section 8 of `paper/es-threequarter-note.tex`: replacing u^(3/4) by u^theta works for every fixed `0<theta<1`.
* Theorem 75.4 needs only the set inclusion defining STR. Summing at most `2^J` applications of (75.9) is absorbed into C for every lambda>0. No EQ, BR, moment heuristic or witness expectation enters either conditional proof.
* Proposition 75.5's compatible CRT expansion now has the correct shifted interval. Its local number of assignments is at most `J 2^(t_p-1)`. For odd `p<=sqrt Z`, BT gives `O(1+J/p)`; these sum to `O(J log log Z)`. For `sqrt Z<p<=Z/8`, the k-th dyadic range contains `O(Z/(2^k log Z))` primes, each with occupancy `O(1+2^k/k)`; summing costs `O((Z/log Z)log log Z)`. The remaining primes cost O(J), as does p=2. Thus (75.13) is valid, and `log log Z=log log L+O_theta(1)`. The coefficient restriction is now appropriate. No heuristic enters this proved proposition.

### Numerical and finite checks

I ran the requested isolated bw block successfully (using a heredoc for the exact extraction, to avoid shell escaping of the final print marker). Runtime reported by the block was **0.57 seconds**. An initial shell-quoted invocation failed only to locate that marker; it did not execute any mathematical check. All actual assertions passed.

Independent values:

| Quantity | Value |
|---|---:|
| theta_1 | .335711417418075 |
| theta_hi | .989860615252697 |
| theta_* | .523494641959496 |
| theta_tilt | .767216486288474 |
| full-family/subfamily transition | .687228727350410 |
| maximum f | .582306280029209 |
| maximizing theta | .634815405644086 |
| f(2/3) | .576610329954092 |
| f(3/4) | .496883936376947 |
| delta(lambda_(3/4)) | .0567214332658671 |
| crossing with 1-lambda on the tilt branch | .9176325891275 |
| index-six threshold | .043233522112864 |

The crossing is analytically `1/(2-1/log 3)`: on the tilt branch solve `2(1-theta)=1-theta/log 3`. Between theta_* and this second crossing, the claimed strict inequality between these **formulas** is correct. It says nothing about existence of the adversarial measure.

The bw index-six counts, with the distinguished generator placed first by symmetry, are `{7:8,19:240,31:1248,43:4800}`. The exact signed-product enumeration and the finite a=43 echo agree with the first-round results: `(count, block share, empirical floor)` equals `(2261,.2941,.2465)`, `(4958,.7096,.5558)`, `(3598,.7504,.3423)` for m=1,2,3.

I independently streamed occupancy computations; no Cartesian-product arrays were allocated:

| Z | J | sum_p(t_p-1) | ratio to J log log Z |
|---|---:|---:|---:|
| 1000 | 87 | 227 | 1.3501 |
| 10000 | 619 | 1992 | 1.4494 |
| 100000 | 4808 | 17750 | 1.5109 |

For the pointwise Poisson proxy at beta=2, direct truncated-Poisson evaluation gives `log(expected)/s=1.65458,1.69211,1.70763,1.71701` at `s=20,50,100,200`, tending to `1.72983099`, not 2. The pairwise-indicator moment identities in N4 were checked exactly with rational arithmetic. A supplementary SciPy launch under a 1 GiB address-space limit initially hit OpenBLAS thread allocation; it was rerun with one BLAS thread under the same limit, not with an increased/unbounded allocation.

**Bottom line:** the elementary/conditional proved core is sound after the rewrite. The section as a whole remains DEFECTIVE because N4–N6 invalidate or leave unsupported its newly advertised negative/model conclusions, and the Status assertion of complete repair is false.
