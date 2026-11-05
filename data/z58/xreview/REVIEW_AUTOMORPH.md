# z58 hostile cross-model review — AUTOMORPH

Reviewed `side-agent/z58-automorph` at `9bee2e0098b25ba1882d25c72bb889e973a8b007` (`Z58_AUTOMORPH.md`, scripts and data).
**Verdict: ACCEPT-WITH-FIXES.** Theorem A and Corollary A1 survive independent re-derivation. The escape taxonomy needs correction; no fatal gap in the scoped no-go was found. ES remains OPEN.

## Per-claim decisions

| Claim | Classification | Finding |
|---|---|---|
| Lemma S | CORRECT | Oddness, disjoint pole sets and properness force zero; pole multiplicities do not matter. |
| Definition of 𝓗 / coverage | CORRECT-WITH-FIX | The displayed arithmetic generators suffice; explicitly fix complex scalars, finite sums/orders and real evaluation points. Do not equate this class with every Hecke-finite automorphic object. |
| Theorem A.1 and A.2(a) | CORRECT | Parameter differentiation preserves properness; trivial characters give strictly positive real poles' reciprocals. |
| Theorem A.2(b) | CORRECT | Residual identity excludes algebraic/algebraic collisions; purity plus the Hecke-field ramification argument excludes the genuinely delicate mixed collisions. |
| Corollary A1(a–c) | CORRECT | Validity is on all admissible integers, not primes alone. The exact-identity contradiction uses a valid, compatible Chebotarev construction. Q3 is appropriately limited. |
| Collision examples / local sign example | CORRECT | Twist and CM examples are possible sources, not a classification; the local sign example fails globally as stated. |
| Props B1 and B2 | CORRECT | The global square inequality and the repaired logarithmic polynomial both check. These are not valid support/minorant proxies for R. |
| Prop C(a–b) | CORRECT AS CONDITIONAL | Requires (H_E), the cusp estimate and infinitely many squarefree zeros in the specified joint class. Finite tables establish none of these infinite hypotheses. |
| E1–E3 taxonomy | CORRECT-WITH-FIX | E1 can satisfy proper rationality with unavoidable ± poles. Poincaré/Rademacher packaging alone does not imply failure of Hecke-finiteness. H2 as written does not describe arbitrary real type-(iii) parameters. |
| E2 finite-C-support / nonmodularity remark | CORRECT | The bound is C ≤ (p+2)/4; a nonzero q-polynomial with zero constant term cannot be holomorphic modular. |
| E3 GL(n) local statement | CORRECT | For standard unramified Euler coefficients, the proper degree-n reciprocal Euler factor gives Lemma S. The global Galois step is correctly left unchecked. |
| “Dead” / “narrowed” verdict | CORRECT WITH SCOPE | Dead only for a single fixed finite 𝓗 support proxy that is both valid on integers and eventually nonzero at every 𝔐-prime. No no-go for prime-only identities, sign proxies, all mock forms, or ES follows. |

## Independent proof audit

1. **T1 input.** A solution gives d=4uC−1 and n≡−u (mod d). Here gcd(u,d)=1 and (u/d)=1: write u=2^s v, use d≡−1 (mod v), quadratic reciprocity, and (2/d)=1 when s>0. Since d≡3 (4), (−u/d)=−1, impossible for a square n. Thus R(m²)=0, including R(1)=0.
2. **Local algebra.** Vanishing of all even coefficients means A(T)=−A(−T). Every actual pole must therefore belong to both P and −P. If these are disjoint, A is polynomial; properness makes it zero. Neither distinct roots nor simple poles are required.
3. **Generators.** At p∤M each integral-weight generator has reciprocal quadratic Euler factor; n^j scales both roots by p^j. For type (iii), differentiate the reciprocal factor in its real exponent parameters. Locally at infinity it is O(T⁻²), with analytic parameter-dependent coefficients, so each finite derivative remains proper, including at coincident roots. Finite complex linear combinations preserve these properties. Away from the level, the simultaneous eigencomponent identity a_f(n)=λ(n)a_f(1) and vanishing of oldforms f(dz), d>1, give the asserted holomorphic coverage. The usual quasimodular derivative decomposition then reduces to these generators, with E₂ supplied by σ₁ in type (iii).
4. **Residual field.** Choose common embeddings into Q̄ℓ and stable lattices. Reduction has finite image. At primes split in the finite compositum F, every twisted algebraic Satake root reduces to 1; two such roots cannot sum to zero because ℓ is odd. Splitting in the cyclotomic factors trivializes all characters and makes p≡1 (mod ℓ).
5. **Mixed roots.** A type-(iii) root is positive real at these primes. If it is the negative of a cuspidal root γ, purity and determinant p^w force both cusp roots to equal −p^(w/2), w=k−1+2j. For even w the trace is −2 modulo ℓ, contradicting residual trace 2. For odd w its trace puts √p in the Hecke field, hence in F; p ramifies in Q(√p), contradicting complete splitting in F. Weight one uses finite-image purity and falls in the even case. Including the Hecke fields in F is essential to this proof as written.
6. **Density and quantifiers.** Chebotarev gives density 1/[F:Q]>0, all primes ≡1 (840). F depends on the chosen finite proxy/decomposition; there is no asserted universal positive-density set for all of 𝓗. Infinitely many such primes exceed any fixed effectiveness threshold. Restrict square inputs to gcd(m,M)=1, as required by the domain.
7. **Exact identity.** Choose q≡3 (4) unramified in F. Every nontrivial subfield of Q(ζ_q) ramifies at q, so F∩Q(ζ_q)=Q. Chebotarev therefore permits simultaneously splitting in F and p≡−4⁻¹ (mod q). For sufficiently large such p, q and (4p+1)/q are positive numbers ≡3 (4), giving C=1, u=(q+1)/4 and B=((4p+1)/q+1)/4. Hence R(p)>0, contradicting equality with the vanishing proxy. Equality only at primes does not supply T1.
8. **Sign examples.** Locally r(p^m)=m+1 at p≡1 (4), giving a(p)=p−1 and the stated negative even-power values. For B1, σ₂(m²)/m⁴<9/8 at a single odd prime and <3ζ(2)/4 in general; compare 2τ(m²)≥6 or ≥18. Thus a(m²)<0 for m>1 while a(p)=p²−1. For B2, summing j² and j(m−j) gives exactly m(m+1)(2−m)/2 times log²p. These arguments establish T1 compatibility only, not validity.
9. **Prop C.** Unary-theta support meets the squarefree integers in finitely many points. An infinite squarefree zero sequence in a fixed class is unbounded and eventually satisfies E(n)=−c(n). In the nonzero branch of (H_E), the quotient of the lower bound for |E(n)| by the upper bound for |c(n)| grows as n^(1/28−2ε), contradicting ε<1/56. The dichotomy then gives E≡0 on that class. Large primes in it have g(p)=c(p). Primes ≡1 (mod 8N·840) lie in the class of 1. No conclusion about cusp nonvanishing or a computed threshold follows.
10. **Finite C polynomial.** Both divisors are at least 4C−1, so (4C−1)²≤4Cp+1 gives the claimed bound. A finite q-polynomial is analytic across rational boundary points. Modularity transports exponential decay at infinity to infinite-order vanishing at such a point when its constant term is zero, forcing the polynomial to vanish identically. This excludes the nonzero polynomial, not nonholomorphic completions.

## Required fixes, in priority order

1. **Correct the structural escape explanation (§4).** For a weight-3/2 T(p²)-eigenform at p∤2N, set λ=λ(T(p²)). If its even p-power coefficients vanish, the standard recursion gives
   `Σ a(p^m)T^m = a(p)T / (1 − λT² + ψ(p)²pT⁴)`.
   This is proper rational and may have a(p)≠0; its nonzero poles occur in ± pairs. Thus E1 escapes collision-freeness / the integral-weight p-step mechanism, not necessarily H1 as actually defined. Also rewrite H2 to distinguish algebraic residual control from real-root positivity and purity. Nonintegral real powers need not even be algebraic, so they do not all admit the advertised reduction modulo 𝔪.
2. **Do not use representation formats as exclusion criteria.** A holomorphic fixed-weight Poincaré series is in the finite-dimensional modular space and hence covered by 𝓗 away from its level. E2 should say “constructions whose resulting coefficients are outside 𝓗,” not suggest that a Poincaré/Rademacher or Fourier–Jacobi presentation itself demonstrates that fact. The level-sum route remains an escape, not a new no-go.
3. **Keep the sign-form assessment conditional on effectiveness.** Checking validity at target primes is equivalent to (MS) only after a(p)>0 has been established at every such prime (with matching thresholds). The zero minorant is trivially valid and does not imply (MS). Replace “automorphy buys nothing” and “the only automorphic-native proxies” by statements about the examined constructions; B1–B2 do not exclude a structurally justified effective signed minorant.
4. **Make the definition and dependencies unambiguous.** State c_i∈C and fixed finite M,r,derivative orders; define type (iii) equivalently using ∂_a^r∂_b^s of Σψ₁(d)ψ₂(n/d)d^a(n/d)^b evaluated at real (a,b). Keep 𝓗 as the union of these fixed-level arithmetic classes, not a synonym for “Hecke-finite.” Write coprime odd m where needed. Add explicit purity and coefficient-bound references below; existence of Galois representations alone is not the purity input used in A.2(b).

## Numerical and falsifier checks

Both original scripts were inspected before execution and rerun from a branch archive in `/tmp/xrev_AUTOMORPH`, under `ulimit -v 4000000`; timeouts were 1200s and 900s. Both outputs were byte-identical to the committed outputs (`diff -u` clean). No new test script was needed: the existing scripts already cover the finite calculations.

| Screen / calculation | Independent review result |
|---|---|
| F1 odd squares | T1 re-derived above. The local nullspace runs force a(p)=0 for p≡1 (4), 3≤p<40; twist collisions allow nonzero a(p) at p≡3 (4). Generic, self-collision and 3-cycle outputs agree. These finite checks are sanity checks, not proof of the Galois step. |
| F2 C-even / numerator 8 | R₈≤R makes square vanishing automatic, so the same negative theorem applies without a false positivity claim. The 12 supplied R₈-zeros are constraints only on an R₈-proxy, not zeros of R. Table 1 counts 6,4,3,2,1 for P=3,7,13,19,23 reproduce. Nothing here proves eventual numerator-8 failure or full-family failure. |
| F3 285 composites | Table 1 composite counts 71,15,6,1,1 and squarefree counts 58,15,6,1,1 reproduce; big squarefree counts are 9,2,2,1,1. Single-prime-level Table 2 and decade counts 0,0,3,3,7,2 also reproduce. These are finite evidence for Prop C's premise, not an application establishing it. |
| F4 14 (★) / 38 𝔊* primes | All listed local-class counts reproduce. The three (★)-zeros claimed ≡1 (840) are correctly in that residue class. A proxy for R need not vanish at extra 𝔊*-zeros unless it is a proxy for R_𝔊*; the memo preserves this distinction. B1 is positive at every prime, hence invalid at all 14 supplied (★)-zeros. |
| Global sign check | For every odd m≤20001, B1 gives a(m²)≤0; maximum a(m²)/m⁴ is 0 at m=1, exactly as recorded. |

The supplied zero lists were not independently re-certified here; the reruns recompute their classifications and the sign calculations. No numerical census is needed for Theorem A. No HOT LEAD or “survives all four” claim is present.

## Literature and scope

- Checked [T. Saito, *Galois representations and modular forms*](https://www.ms.u-tokyo.ac.jp/~t-saito/talk/eep.pdf), Definition 1.2, Theorem 1.3 and Corollary 4.5: the Frobenius polynomial, all ℓ-adic places, and both roots' absolute values p^((k−1)/2), as used in A.2(b).
- Checked [G. Wiese, *Galois Representations*](https://math.uni.lu/wiese/notes/GalRep.pdf), Theorems 1.2.8 and 1.3.4–1.3.6: Chebotarev density and the weight-one characteristic polynomial. A continuous complex Galois representation has finite image, supplying weight-one purity.
- Checked [Duke 1988](https://www.math.ucla.edu/~wdduke/preprints/hyperbolic.pdf), Theorem 5 and the weight-3/2 discussion; also [arXiv:1706.09320](https://arxiv.org/html/1706.09320v1), equation (2) and Theorem 1. The latter explicitly covers arbitrary nebentypus; at fixed level and squarefree n it gives |c(n)|≪n^(13/28+ε), the exponent in Prop C. This supports (I), not (H_E).
- The Planck-scale discussion is inherited, scoped assessment for the examined certificate/CM dictionary, not a theorem excluding all half-integral-weight proxies. The paper's wedge and shrinking-target passages were checked for this scope; no universal impossibility is established there.

**Recording recommendation:** record A/A1 as a proved, fixed-class support no-go, relative to the stated standard inputs. Keep Prop C conditional, E1–E3 open in their stated unexcluded scope, and the lane verdict **narrowed**. Apply the explanatory fixes before propagating the memo's escape taxonomy or sign-form assessment to FRONTIER.
