# z45_critical_chaos — arithmetic overlap is not yet critical multiplicative chaos

## 0. Summary

**Assessment.** The proposed analogy does not currently identify a log-correlated field governing the ES hole event. There is a genuine random-multiplicative structure in the Brauer-character main term, but its natural weights are at the **1/ℓ, not 1/√ℓ, scale**: the centered random main term has uniformly bounded variance. In an explicit BM-gated Cox model I prove that the zero probability is a constant times exp(−M₀/2), hence summable over primes. This is a theorem about the model, not ES, and shows that shared Legendre signs alone do not manufacture an asymptotically stretched zero law. A separate, class-aware CRT/Bernoulli model distinguishes numerators 4, 8 and 15, and gives reasonable orders for known **single-line** failures, but does not reproduce the full three-unit-fraction failure sets. The apparent disproof signal from “0.97 log p hit levels” extrapolates a finite-range coefficient, mistakes expected hit levels for the no-hit hazard, and confuses failure of (★) with failure of ES. None is a sound disproof signal.

**Verdict: PARTIAL — a useful probabilistic diagnostic, but the exact open implication is from residue-class-aware inverse-moment/hole estimates to the actual arithmetic count. B2/B6 remain. Promise: 2/5.** ES remains open.

**Assessment, novelty audit.** Read FRONTIER §§2–7, the brainstorm index, SYNTHESIS_SPARKS9 §§1–3, DISCOVERIES (J)103, BM_CORRECTED_COUNT §3 and DISPROOF_AVENUES §4. Searches for “multiplicative chaos”, “random multiplicative”, “log-correlated” and “branching random” found no prior dedicated treatment. However `BRAINSTORM/anal_euler_product_law.md` already models shared Legendre symbols through an L(1,χ)-type Euler product, and `s9_janson_dependency`, `s9_ladder_thinning`, `z32_numerator_ladder` already discuss level and numerator thinning. Those ideas are not new here. The extra work is the squarefree-kernel covariance calculation, a bounded-variance and zero-law theorem for the explicit surrogate, and an arithmetic rather than geometric exposure-tree proposal.

## 1. Precise dictionary

### 1.1 What the random coordinates actually are

**PROVED (repository identities, with notation fixed).** For a prime p ≡ 1 (4), use unordered pairs

    P₄(p) = {(u,v): 1 ≤ u < v, gcd(u,v)=1, u+v odd,
                         4uv−u−v ≤ p}.

Then

    R(p)/2 = Σ_(u,v) 1[p ≡ −u−v (mod 4uv)],
    M_BM(p)/2 = Σ_(u,v) (1−χ_p(uv))/φ(4uv).

Write A_p = Σ 1/φ(4uv), and

    w_s(p) = Σ_{(u,v)∈P₄(p), sf(uv)=s} 1/φ(4uv),
    T_p = Σ_s w_s(p) χ_p(s).

Here sf means the squarefree kernel, so M_BM/2 = A_p−T_p. The principal term is
A_p ∼ 3(log p)²/(4π²), not (log p)²/16: primes require 1/φ(q), not 1/q.

**Assessment, correction to the brief.** The shared primes are not “prime factors of p” (p is prime). They are primes dividing auxiliary products uv or the shifted integers tp+1. Replacing χ_p(ℓ) by independent signs ε_ℓ models one family of quadratic characters as p varies, not randomness at a prescribed p.

**PROVED (finite-dimensional limiting law, relative to PNT in fixed arithmetic progressions).** For any fixed finite set of primes ℓ, the symbols (ℓ/p), with p restricted to 1 mod 4, become independent fair signs as p tends to infinity through primes, apart from explicitly imposed congruences. Mordell's six classes mod 840 fix ε₂=ε₃=ε₅=ε₇=+1. This statement does not permit a growing set of primes of arbitrary size, nor transfer an exponentially small tail.

**PROVED (elementary Walsh dictionary).** Extend the signs *completely multiplicatively*, so f(s²)=1. For squarefree s,t,

    E[f(s)f(t)] = 1[s=t],
    Var(Σ_s w_s f(s)) = Σ_{s>1} w_s².

A common prime factor by itself does not give covariance: f(2) and f(6) are uncorrelated. Conversely f(6), f(10), f(15) are pairwise independent but their product is identically 1. Thus the overlap structure is a multiplicative incidence hypergraph, not automatically a branching random walk. This model is not Harper's squarefree-supported Rademacher function: our f takes value 1 on squares rather than 0.

### 1.2 Levels require more information than signs

**PROVED (reciprocity; SS9 Prop 2.1).** At t ≡ 0 (4), ℓ | tp+1 implies

    (ℓ/p) = (p/ℓ) = (−t/ℓ),

for odd ℓ and p ≡ 1 (4). The same sign can therefore constrain many levels, but it neither determines which levels contain ℓ nor determines a divisor's class modulo t. A divisor is a bounded product of the actual prime factors of tp+1; its target is −1 in (Z/tZ)×.

**PROVED (arithmetic covariance toy).** Let A_ℓ be uniform in (Z/ℓZ)× and put I_t,ℓ=1[tA_ℓ+1=0 mod ℓ], for ℓ ∤ t. Then

    E I_t,ℓ = 1/(ℓ−1),
    Cov(I_t,ℓ,I_s,ℓ)
      = 1[t=s mod ℓ]/(ℓ−1) − 1/(ℓ−1)².

Proof: either the two required residues of A_ℓ agree or they are disjoint. Conditional on (A_ℓ/ℓ)=ε, the hit probability is 2/(ℓ−1) when ε=(−t/ℓ), otherwise 0. The *residue*, not just its sign, couples the levels. For ℓ=5, levels 4 and 24 have covariance 3/16, while 4 and 8 have covariance −1/16. Nearby or distant levels need not follow a monotone logarithmic-distance kernel.

**Assessment.** A valid model must preserve this arithmetic overlap, the total factor product tp+1, and large-factor privacy: gcd(tp+1,sp+1) | t−s. A sign-only model with independent level incidences conditioned on signs violates even this elementary compatibility. No natural log-correlated metric on the complete level system has been established here.

## 2. What multiplicative-chaos results actually provide

**PROVED (external theorem; verified abstract and corroborating primary exposition).** Adam J. Harper, *Moments of random multiplicative functions, I: Low moments, better than squareroot cancellation, and critical multiplicative chaos*, Forum Math. Pi **8** (2020), e1, [arXiv:1703.06654](https://arxiv.org/abs/1703.06654), proves in particular

    E |Σ_{n≤x} f(n)| ≍ √x/(log log x)^(1/4)

for the Steinhaus and squarefree-supported Rademacher models. These are expectations over random multiplicative functions. The underlying critical Euler fields have prime weights approximately 1/√ℓ and variance growing like log log x. The cancellation statistic is not a nonnegative divisor-class occupancy count.

**PROVED (external theorem, primary HTML checked).** K. Soundararajan and A. Zaman, *A model problem for multiplicative chaos in number theory*, [arXiv:2108.07264](https://arxiv.org/html/2108.07264v1), define independent standard complex Gaussians X(k) by

    exp(Σ_{k≥1} X(k) z^k/√k) = Σ A(N)z^N.

Their Theorem 2.1 states, uniformly for 0≤q≤1,

    E|A(N)|^(2q) ≍ (1+(1−q)√log N)^(−q).

The proof uses an exponential-scale Gaussian decomposition and barrier/ballot estimates (Lemma 2.3, §§5, 10–12). The logarithmic covariance comes from the explicit oscillatory factors e^(ikθ), not merely from products of independent variables.

**Assessment (literature scope).** Maxim Gerspach, *Almost sure lower bounds for a model problem for multiplicative chaos in number theory*, [arXiv:2202.00521](https://arxiv.org/abs/2202.00521), develops the almost-sure large-excursion analogue; its abstract was checked, and SSZ's introduction explains the underlying limsup question. “Almost sure lower bounds” here must not be read as a positive lower bound for every coefficient at every input. No theorem from this paper is invoked for ES. Arguin–Belius–Harper, *Maxima of a randomized Riemann zeta function, and branching random walks*, Ann. Appl. Probab. **27** (2017), 178–215, is a relevant comparison cited in SSZ, not an arithmetic transfer theorem used here.

**Assessment.** These tools operate on a probability space of functions/fields, sometimes with an additional spatial variable θ or varying cutoff. At one fixed p those random variables have already been specified arithmetically. Neither a moment theorem nor an almost-sure statement controls every such specification. Moreover, ES needs the atom at zero or growing negative moments, not merely low positive moments of a signed sum.

## 3. Attempts with mathematics and numerical output

### 3.1 BM-gated multiplicative Cox model: explicit and soluble

**Definition / EVIDENCE as an arithmetic model.** For k=4 or 8 use unordered coprime opposite-parity pairs with kuv−u−v≤H. Independently conditional on all prime signs, let each pair carry a Poisson number of hits of mean

    (1−f(uv))/φ(kuv).

Let Z_k,H be the total number. Equivalently it is Poisson with random intensity

    Λ_k,H = A_k,H − T_k,H,
    A_k,H = Σ_pairs 1/φ(kuv),
    T_k,H = Σ_s w_k,s(H) f(s).

This preserves the shared multiplicative products and the square-sign obstruction: setting *all* signs to +1 makes Z=0 identically. It does not preserve divisor-class dependencies, so is deliberately a BM-only surrogate. For k=4 it models R/2, not full ES. The Poisson choice is an assumption, not a consequence of reciprocity.

**PROVED, Lemma 1 (bounded variance; no critical chaos in this layer).** Uniformly in H,

    Var(T_k,H) ≤ C_k < ∞,  k=4,8.

Proof. For even m, all unordered coprime splittings m=uv are opposite-parity, number 2^ω(m)/2. Also φ(km)=kφ(m). Hence the coefficient at kernel s increases with H and is bounded by

    w_k,s(∞) = (1/(2k)) Σ_{m even, sf(m)=s} a(m),
    a(m)=2^ω(m)/φ(m).

For an odd prime q, the local even- and odd-exponent sums of this multiplicative weight are

    E_q = 1 + 2q/((q−1)(q²−1)),
    O_q = 2q²/((q−1)(q²−1)).

Thus E_q=1+O(q^−2), O_q/E_q=2/q+O(q^−2). At 2 use the positive-even sum E₂−1 and odd sum O₂. The sum of squares of all kernel coefficients is an absolute constant times

    Π_{q odd} (E_q²+O_q²),

which converges, since its factors are 1+O(q^−2). Walsh orthogonality proves the assertion. It also proves T_k,H converges in L² as H→∞. ∎

**Assessment.** This is a direct reason to reject “the BM main term is critical GMC”. It is compatible with the earlier 1/q-weighted L(1,χ) observations. It does not rule out log-correlated structure in the *residual class occupancy*, which is precisely the part missing from the model.

**PROVED, Lemma 2 (zero law of this model).** There is a finite positive constant C_k such that

    P(Z_k,H=0) ∼ C_k exp(−A_k,H),
    log P(Z_k,H=0) = −a_k(log H)²+O(log H),
    a₄=3/(4π²),  a₈=3/(8π²).

The same constant-factor assertion holds after fixing any finite collection of prime signs. In particular the model has finite expected total failures over primes, and almost surely only finitely many, regardless of dependence chosen between different heights with these marginals.

Proof. The limiting Walsh series is the L² Euler product

    T_k,∞ = [(E₂−1)+O₂ε₂]/(2k)
             · Π_{q odd} E_q(1+r_q ε_q),   r_q=O_q/E_q.

The odd-prime factors are positive, r_q=2/q+O(q^−2), and Σr_q²<∞. For every integer r≥1 its 2r-th norm is O_k((log(2r))²). To see this, separate q≤2r, where the product is bounded by Π(1+r_q) ≪ (log(2r))² (Mertens), from q>2r. On the latter range,

    log E(1+r_q ε_q)^(2r) ≪ r²/q²,

so the 2r-th root of their total contribution is O(1), even using Σ_{q>2r}q^−2=O(1/r). The finite 2-factor is harmless. The same moment bound holds for T_k,H: expansion of an even moment of a nonnegative-coefficient Walsh polynomial has nonnegative terms (each sign expectation is 0 or 1), and its coefficients are dominated by the infinite coefficients. Consequently

    sup_H E exp(b|T_k,H|) < ∞

for every fixed b>0: the moment expansion converges since (C_b log²r)^r/r! is summable. L² convergence and uniform exponential integrability imply E exp(T_k,H)→E exp(T_k,∞)=C_k. Finally,

    P(Z=0) = E exp(−Λ) = exp(−A_k,H) E exp(T_k,H).

The principal-term constants follow from BM_CORRECTED_COUNT §2 (and the factor 1/2 for unordered pairs); replacing 4 by 8 halves the leading constant. Fixed-sign conditioning changes the moment bounds by at most a fixed reciprocal conditioning probability. The summability and first Borel–Cantelli lemma finish the proof. ∎

**Assessment, limitation.** This is not a derivation of the observed zero law. Indeed it predicts only a bounded multiplicative excess over Poisson asymptotically. It cannot explain a persistent exponent β<1 at fixed arithmetic mean by BM heterogeneity alone. The measured finite-range fattening could be transient, reflect other genus characters, reflect full residue/factor correlations, or reflect unremoved heterogeneity. No option is decided here. The real count's large upper tail is also missing from this toy model.

### 3.2 Exact finite-sign computation, without rare-event Monte Carlo

**EVIDENCE (floating-point probabilities, exhaustive finite state space).** `scripts/z45_critical_chaos_model.py` enumerates the exact pair domains, aggregates their squarefree kernels, and computes the conditional expectation of Λ given ε_q for q≤31. A Walsh transform enumerates all 2¹¹=2048 sign states; the Mordell slice fixes the first four signs. It then computes E exp(−E[Λ|small signs]). This is a *lower bound* on the full Cox zero probability by conditional Jensen, not an unbiased estimate of the full model. No Monte Carlo claim at probabilities smaller than the sample resolution is made.

| H | Var(T₄,H), exact coefficient formula | projected P₄(0), p≡1 (4) sign model | projected P₄(0), Mordell signs |
|---:|---:|---:|---:|
| 10² | 0.31470 | 0.33651 | 0.91434 |
| 10³ | 0.59045 | 0.061064 | 0.34444 |
| 10⁴ | 0.78907 | 0.0049837 | 0.039625 |
| 10⁵ | 0.88717 | 0.00016648 | 0.0015515 |
| 10⁶ | 0.92981 | 0.0000022647 | 0.000022593 |

**Assessment.** Variance saturation is visible already; the proof, not the table, establishes it. The finite-sign projection is not T1-exact when unexposed signs are replaced by their mean. T1 belongs to the full model. Confusing those two would be a false square test.

### 3.3 A class-aware comparison model, also for numerator 15

**Definition / EVIDENCE as an arithmetic model.** Set Q=840 and choose A uniformly in its 192 unit classes, equivalently independent unit residues at its prime-power factors. For k∈{4,8,15}, take all unordered pairs u≤v with gcd(u,v)=1, gcd(u+v,k)=1 and kuv−u−v≤H. The only possible diagonal is (1,1). Set q=kuv, a=−u−v, g=gcd(q,Q). Given A, use independent Bernoulli hits of probability

    h_(u,v)(A) = 1[A=a mod g] · φ(g)/φ(q).

The probability h is **PROVED** to be the exact Haar conditional density of this *individual* prime congruence, by counting units modulo lcm(q,Q). Conditional independence of different pairs is the model assumption and is false for the full arithmetic system. The zero probability is explicitly

    P_k,H(0) = (1/192) Σ_{A∈(Z/Q)×} Π_pairs (1−h_pair(A)).

This keeps small-prime residues, not just signs. A Poisson alternative is recorded in the data as `crt_zero`; it is inferior because it gives positive probability of zero even when an exposed congruence guarantees a hit. The Bernoulli version assigns zero failure probability to such cells. For example it correctly guarantees the k=4 line at p=193, unlike the b=1 line which actually fails there.

**PROVED (why 15 needs its own class model).** The 4/8 parity gate cannot be extended blindly to 15: u=v=C=1 gives p=13 and

    15/13 = 1 + 1/13 + 1/13,

although (−uv/13)=+1. The general k pair congruence is valid; the “must have negative Brauer sign” restriction is not. We therefore do not call the k=15 CRT model a BM model.

**EVIDENCE (no fitted parameters; whole-class prime probabilities, not just 1 mod 4).**

| H | CRT-Bernoulli P₄(0) | P₈(0) | P₁₅(0) |
|---:|---:|---:|---:|
| 10² | 0.185145 | 0.583171 | 0.770833 |
| 10³ | 0.0247917 | 0.245644 | 0.486604 |
| 10⁴ | 0.00206021 | 0.0718906 | 0.247006 |
| 10⁵ | 0.0000809975 | 0.0146967 | 0.100804 |
| 10⁶ | 0.0000014824 | 0.00205358 | 0.0329580 |

**EVIDENCE (explicit cumulative prediction; coarse quadrature).** In this model

    expected #zero primes up to X = Σ_{p≤X} P_k,p(0)
                                 ≈ ∫₂ˣ P_k,t(0) dt/log t.

Log-linear interpolation of the five probabilities above, numerical integration from 100, gives:

| interval | k=4 line | k=8 line | k=15 line |
|---|---:|---:|---:|
| [100,10⁴] | 15.17 | 174.0 | 423.3 |
| [100,10⁵] | 18.21 | 405.2 | 1600.6 |
| [100,10⁶] | 18.94 | 721.8 | 5060.0 |

These are descriptive approximations, with interpolation and prime-density error, not validated rare-tail forecasts. The k=4 arithmetic census has 14 (★) failures among **all** primes in [100,10⁶], obtained by removing 7,31,79 from BM_CORRECTED_COUNT's 17 failures ≤10⁶. The k=8 line has 835 failures ≤10⁶ (same source); there are at most 25 primes below 100 to remove. The rough magnitude is credible, but the model is not a precision fit. No k=15 single-line census was supplied or manufactured here.

**EVIDENCE / Assessment (required failure controls, carefully separated).**

| actual input | CRT-Bernoulli probability of single-line failure, conditioned on p mod 840 | meaning |
|---|---:|---|
| k=8, p=11,17 | 1, 1 | consistent with genuine full failures |
| k=8, p=131,241 | 0.56250, 0.91042 | gives substantial mass to genuine full failures, does not predict their identities |
| k=15, p=20521 | 0.33715 | consistent with a genuine full failure, no exact explanation |
| k=4, p=409,577 | 0.47616, 0.098724 | consistent with the first (★) failures |
| k=4, p=193,2521,66529 | 0, 0.15521, 0.0011928 | these are b=1 failures, **not** failures of the modeled line |
| k=4, p=3361 | 0.12781 | no claim that the model supplies a split/prime-modulus Type II certificate |

**PROVED (target distinction).** Failure of the c=1 line is necessary, not sufficient, for failure of full k/p. PW Table 1 (`sources/pw.txt`, §6) lists 8/n failures {1,2,3,11,17,131,241} through 10¹³, and 32 failures of 15/n through 10¹², last 20521. The latter are **integers**, not 32 primes: they include 1,4,8,16,34,122,226. The task's “32 values ≤20521” is consistent with that table but is not the verification cutoff. The repository's Type-II-only data are different again: 21 numerator-8 failures through 10⁸, last 35569; 275 numerator-15 failures, last 5125871 (`logs/z32_universal.txt`, `z32_crossover.txt`).

**Assessment, answer to the reproduction question.** Neither surrogate reproduces the full failure sets. The quadratic Cox model predicts finitely many failures of the *4 and 8 single-line surrogates*. The three-numerator CRT model has the right finite-scale thinning direction and allows the named failures; it does not prove a complete asymptotic for k=15 here and does not model full Type I∪II. Claiming it explains exactly four nontrivial 8/n failures or exactly 32 failures of 15/n would be target substitution. Similarly, the 14 (★) failures through 10¹⁰, last 8813281, and the b=1 failures do not determine the joint all-slices hole law. No exact small failure set is expected from a probabilistic law without arithmetic conditioning that already contains the answer.

### 3.4 The alleged “critical ⇒ infinitely many counterexamples” tension

**PROVED (probability bookkeeping).** If each prime independently fails with probability p^−c, then

    E failures ≤X = Σ_{p≤X} p^−c ≈ ∫₂ˣ t^−c/log t dt.

There is no additional 1/log p inside the sum over primes. For c<1 this is asymptotic to X^(1−c)/((1−c)log X); for c=1 it diverges like log log X. Independence, or a sufficient substitute, is needed for the converse Borel–Cantelli conclusion. Divergent expected count alone does not prove infinitely many failures.

**PROVED (mean is not hazard).** Even for independent level hits of probabilities q_t,

    −log P(no hits) = Σ_t −log(1−q_t) ≥ Σ_t q_t.

The expected number of hit levels is therefore not enough to identify the no-hit exponent. A certain hit has expected contribution 1 but infinite no-hit hazard. Poisson substitution additionally requires diffuse probabilities. For a Cox mixture of total intensity Λ, Jensen gives E exp(−Λ)≥exp(−EΛ): adding latent positive heterogeneity cannot repair a truly subcritical fixed mean c log p.

**Assessment / EVIDENCE (the main empirical correction).** SS9 explicitly records NL≈0.40 R at every measured height. Together with E R≈0.152 L², this suggests NL≈0.061 L², so NL/L≈0.061 L, **not** an asymptotically fixed coefficient below 1. It crosses 1 near L≈16.4 (p≈1.4·10⁷), close in scale to the last observed (★) failure. This is a heuristic extrapolation, not a fitted theorem; the original SS9 already warns that NL/L→∞ is plausible. The fact that numbers 0.44–0.97 were measured does not establish probabilistic criticality in the GMC sense.

**PROVED (conditional summability criterion).** If a zero law has form exp(−a μ^β), μ∼c(log p)^d, then its prime sum converges when dβ>1 and diverges when dβ<1. At dβ=1 compare ac^β with 1, with the boundary 1 still divergent absent extra logarithmic savings. Thus β=.88 gives exponent 1.76 for a log² count and 2.64 for a log³ count: both summable. The full Type-II ladder's mean is log³, whereas (★)'s is log². The β≈.88 figure describes high-mean restricted refits; DISPROOF_AVENUES §4's pooled fit is .91–.93 and underpredicts top-bin zeros by factors 3–5.

**EVIDENCE (sensitivity, not extrapolated truth).** Using a₄=3/(4π²), at L=20,40 the baseline log P₄(0)=−a₄L² is −30.40, −121.59. Substituting the illustrative law exp(−.535(2a₄L²)^.88) gives −19.87, −67.29. The logarithm of the expected number per unit dL is L−log L+log P, respectively −13.39,−85.27 versus −2.86,−30.98. Both eventually decay; their finite-scale forecasts differ dramatically. The .88 law was fitted to another count, so these are sensitivity numbers only.

**Assessment.** There is no serious disproof signal from this calculation. Even infinitely many failures of (★), were they established, would not disprove ES. Conversely, finite expected failures of a model do not prove zero arithmetic failures, and the finite census cannot remove uncontrolled model risk.

## 4. FRONTIER §4 checklist — every line

**Assessment.** PASS below means the stated model or scope respects that screen, not that an ES proof exists.

| # | result | reason |
|---:|---|---|
| 1 | PASS for full BM surrogate | all + signs kill every gate; finite-sign projection and CRT model alone are not square-exact and are explicitly not proof mechanisms. |
| 2 | PASS as a probabilistic control | 8/131 and 8/241 retain large failure probabilities; no unconditional numerator-uniform success asserted. |
| 3 | PASS | 15 uses residue congruences, not the false 4/8 Brauer gate; no transport or square law. |
| 4 | **FAIL** | q=kuv, or level t for divisors of tp+1, moves with the solution; residual independence is unproved B2. |
| 5 | **FAIL with present inputs** | signs/residues and literature expectations are averaged; §5 states the exceptionally strong bound that would recover each p. |
| 6 | PASS | prime density 1/φ(q); a₄L² for unordered pairs, not a power-size main term. |
| 7 | PASS | only hole probabilities and one-sided targets; no two-sided claim about arithmetic R. |
| 8 | PASS in scope, unresolved in substance | pairs grow with H; Q=840 is diagnostic conditioning only, not a finite covering proof. Actual growing factorisations remain uncontrolled. |
| 9 | **FAIL** | BM signs see parity; CRT fixes some classes but unexposed class correlations are replaced by independent draws. |
| 10 | PASS | exact covariance respects arithmetic residue overlap; no pooling of private large primes. |
| 11 | N.A. | no signed-to-positive move. |
| 12 | N.A. | no infinite-shot relaxation or transport. |
| 13 | PASS | main-term positivity is not confused with existence; missing class occupancy is explicit. |
| 14 | **FAIL as a predictive/existence mechanism** | named exceptions are allowed, some probabilities computed, but not reproduced or excluded; no claim about a=1 at 5101441 or full coverage of all 14 failures. |
| 15 | **FAIL in near-square component** | Mordell signs/classes are imposed; bounded p−m² norm deformations are absent from both surrogate tails. |
| 16 | N.A. | no thin-family-to-prime transfer. |
| 17 | **FAIL if promoted to proof** | large-factor residues are neither controlled nor coupled correctly by the random completion. No covering theorem supplied. |

## 5. New-theory sketch and the first missing theorem

### 5.1 Arithmetic exposure trees, not an assumed Euclidean log-field

**Definition / Assessment.** Build an *arithmetic divisor-hole process*. Reveal p modulo successive prime powers, at exponential prime scales, with state consisting of (i) the quadratic signs, (ii) the actual residue incidences t≡−p^−1 mod ℓ, and (iii) bounded-product divisor-class measures on each group (Z/tZ)×. A level measure is

    ν_t = convolution over ℓ^a || tp+1 of Σ_{j=0}^a δ_[ℓ]^j;
    the hole predicate is ν_t(−1)=0 for every admissible t.

The factorisation equality and the size budget are part of the state, not independent random decorations. The residue revelation supplies a genuine filtration/tree; there is no claim that its covariance equals the Gaussian branching kernel. One may study martingales of conditional hole probabilities or inverse moments of aggregate occupancy. This extends the old Euler-product hardness proxy to an explicitly class-valued process, but may simply repackage B2.

**PROVED / EVIDENCE (toy case actually tested).** Project this process onto its single Brauer character and replace residual occupancies by conditional Poisson variables. This is exactly §3.1: the squarefree Walsh spectrum is orthogonal, its variance stays bounded, its exponential moments are finite, and its hole law is a constant multiple of Poisson. The exhaustive finite-sign computation tests that projection. Therefore any critical branching phenomenon in the proposed fuller theory must come from additional class/size correlations, not this projection by itself.

### 5.2 A precise inverse-moment target

**CONJECTURE-shaped target, not established or attributed to GMC theory.** Let Ω_X be primes in [X,2X], L=log X, c>0 fixed, and

    s_X = (1+δ)L/(2 log L),  δ>0.

Ask for the arithmetic bound

    (1/|Ω_X|) Σ_{p∈Ω_X} [cL²/(R(p)+1)]^s_X ≤ exp(o(L)).       (IM)

This must concern the *actual* count, not a conditional mean. A numerator-dependent version needs its own threshold and finite exceptions. Fixed-order negative moments are insufficient; the order grows like L/log L. The constant c can be chosen below the known unconditional BM lower-bound constant, but that main-term theorem does not imply (IM).

**PROVED (exact recovery of a single integer from this averaged hypothesis).** At R(p)=0 a summand is

    exp(s_X log(cL²)) = exp((1+δ+o(1))L).

Consequently (IM) implies

    # {p∈Ω_X:R(p)=0}
      ≤ |Ω_X| exp(−(1+δ+o(1))L) < 1

for all sufficiently large X. Integrality of this count then gives no exceptional primes. This is the explicit B6-recovery step, not an assertion that ordinary averaging suffices. A finite census up to the resulting threshold would still be required for ES.

**Assessment.** Harper/SSZ's low *positive* moments do not furnish (IM). A deterministic version at one p would instead need a class-aware inequality such as R(p)≥εM_BM(p), or a direct guarantee that one ν_t(−1)>0, for all sufficiently large primes. Those are precisely H⁻_BM/B2-strength statements. Calling them a “deterministic chaos lower bound” supplies no new arithmetic input. Near-square suppression and correlations of the full factor multisets are the first places a genuinely new theorem would have to act.

## 6. Verdict and next steps

**Assessment — PARTIAL, 2/5.** The direct import of critical-GMC lower-tail theory **collapses at the dictionary**: the explicit BM random-multiplicative field is bounded-variance and L(1)-like, not critical. This does not close all possible class-aware chaos models. The broader programme remains partial at B2 (full divisor-class correlations) and B6 (extreme arithmetic tails), with no calibrated theory predicting the complete 4/8/15 failure sets.

**Assessment, concrete next work.** Measure the conditional residual hole hazard after exposing *actual residues* at small primes, keeping square-distance strata separate; use disjoint controls to avoid SS9's earlier collider mistake. Increase exposure depth and height independently, and test whether the residual rate has a stable power dβ>1. Model the **same certificate family** for 4,8,15 before comparing its failure counts; a full ES model must include both types rather than reusing c=1 data. Only if a reproducible class-valued covariance/exposure structure emerges should one attempt a branching approximation. The theoretical milestone is a growing-order inverse-moment bound, not another fixed second moment.

**EVIDENCE, reproducibility.** New files are this memo, `scripts/z45_critical_chaos_model.py`, and `data/z45_critical_chaos/model.json`. Run with `ulimit -v 1500000; OPENBLAS_NUM_THREADS=1 timeout 180 uv run python scripts/z45_critical_chaos_model.py`. Allocation is O(H) with H≤10⁶, plus 2048 Walsh states and 192 CRT states, not a Cartesian product of samples and integers. Existing exact ES/numerator census tests were inspected and not duplicated. Computed probabilities are floating-point EVIDENCE, while Lemmas 1–2 and the inverse-moment implication have proofs above.
