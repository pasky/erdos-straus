# THIN15 — independent hostile cross-model review

Reviewed `side-agent/z53-thin15` at `e9d188f88ed5905919c5b2c27d6f7ee98220494c`, including its scripts/data and cited dependencies.
**Verdict: ACCEPT-WITH-FIXES.** The substantive verdict **narrowed** survives; one progression/μ = 0 scope correction is required. ES remains OPEN, both for the full thin family and in general.

## Per-claim classification

| Claim | Classification | Independent finding |
|---|---|---|
| §1 specialisation; §3 Capelli shapes | CORRECT | Integrality criterion is existential in the shrunk modulus L (with D dividing L); Capelli gives exactly the stated odd-power/SG alternatives. |
| Lemma 1, B/B′ normal forms and converses | CORRECT | Both rescalings and both reciprocal identities check; rational auxiliary parameters are allowed. |
| S2 / normalisation remark: all two-constant menus | CORRECT | Exhausting constant pairs up to a ↔ b gives A, A′, B, B′, C and the stated degeneracies. |
| Lemma 2, including B′ odd-prime argument | CORRECT | Divisibility and reciprocal-polynomial Gauss lemma give a finite D-independent **superset**, not a realisation criterion. |
| Proposition 3(a), reciprocal numerator and integer exclusions | CORRECT | Odd numerator primes are impossible; the two 2-adic units force 4 dividing 1/a. The a = 1/4 endpoint is excluded by Capelli. |
| Proposition 3(b), four Thue equations and Bennett | CORRECT | The h = 1,3,5,15 transformations preserve positivity; Bennett applies separately for each fixed p and coefficient pair. |
| Proposition 3(c), SG exclusion | CORRECT (computer-assisted) | Reduction to r⁴ − 13500k⁴ = 1 is valid; unconditional Thue replay gives only (±1,0). |
| Proposition 4(a), odd integer u | CORRECT | Local divisibility gives both residue conditions, the jj′ equation, the magnitude bound and v₂(φ+1) ≥ E+2. |
| Proposition 4(b), even integer u and integer w | CORRECT | Proper-factor valuation 1 ≤ τ ≤ v₂(K)−1 gives incompatible upper/lower bounds for a. |
| Proposition 4(c), dyadic shapes | CORRECT | X is an odd integer; clearing 2-adic denominators gives the stated divisor equation and bound. |
| Proposition 4(d), u = 1 and u = 1/2 | CORRECT | Only limit pairs (6,5) and (27,5/8); their possible φ values all fail the local conditions. Positivity restricts u = 1/2 to p = 3. |
| §3.2 Ridout-finiteness for each p, including 3 | CORRECT | The integer-approximation exponent threshold is 1, not 2; the conclusion is ineffective and non-uniform in p. |
| §3.3 PID parametrisation and normalisations | CORRECT | Irreducibility of n and gcd extraction give Type I/II; common factors of a,b,c can be removed without changing coordinates. |
| Lemma 5 and even-D gap addendum | CORRECT | Largest-root sign argument forces a common algebraic root of a,b,c if n is positive there; d is positive everywhere for even D. |
| Theorem 6, D = 2 sterility | CORRECT | Bounding parameters in the smallest coordinate, not all parameters, makes the case split exhaustive. C, constant-gap/ratio and polynomial-in-n dependencies apply. |
| Theorem 6 remarks, D = 4 and D = 6 | CORRECT | Type II degree bookkeeping checks. The surviving B-SG/A′-SG heights are retained; the Type I D = 4 list is explicitly non-exhaustive. |
| §3.4 II-c and II-a exclusions | CORRECT | Linear roots are rational, so cannot be roots of irreducible n; the strict sign contradictions are justified. |
| §3.4 II-d parametrisation | CORRECT | Vanishing at ζ and α gives the stated d, κ and polynomial quotients b,c; sign survival is not existence. |
| Proposition 7, finite congruence coverings | CORRECT | A sufficiently large multiple of lcm(60,P₁,…,Pᵣ) selects a residue-0 rule; arbitrary non-congruence architectures are not excluded. |
| Proposition 8, extra-base collapse | CORRECT-WITH-FIX | Polynomial collapse is correct. Its last identification with a root family **through μ = 0** needs a residue-0 progression hypothesis; see required fix. |
| §6 T1 square screen | CORRECT | For s ≥ 1 the only odd squares occur at s = 3,6; n₀ = 16 is separate. No prime-method transfer follows. |

## Proof audit and decisive citations

1. For Type II write y/n = ga, z/n = gb with gcd(a,b)=1. The identity gives ab dividing x, hence x=abd, then d dividing g and c=g/d. For Type I apply the same argument to y=ga,z=gb: ab divides x/n, then d divides g. If n divides all coordinates, their quotients satisfy a constant reciprocal sum; degree comparison plus positivity makes all quotients constant.
2. B follows from b(4ad−1)=n+a after c=1. B′ follows from (4bcd−1)(4acd−1)=4c²dn+1. Expanding the coordinate formulas gives the identity without auxiliary integrality assumptions. Remaining constant pairs reduce as claimed; I-ad uses g dividing (1+4a²d)n.
3. Lemma 2: the coordinate containing (1+φ)/4 makes φ a unit congruent to 3 mod 4. The Y=1 coordinate makes X dyadic. At each odd prime dividing X, local integrality bounds X′; in B′ a negative valuation of a would contradict the positive valuation of X. Reciprocal primitive factors give ρ=ℓ/g₁ with ℓ dividing A and g₁ dividing A+B, so v₂(X)=−v₂(ρ).
4. B′: at an odd numerator prime of a, X and X′ would make XX′=16+a divisible by that prime, impossible. At 2, φ and φ′/a are both 3 mod 4, giving 1/a=G with 4 dividing G. Coprimality in 15rᵖG=vᵖ(G+1) yields m dividing 15 and h=15/m. In the SG case m is odd because G is even; reduction mod 16 forces h=15 and then v₁=15k with k even.
5. B: odd numerator prime powers of a divide X+1 and X′+16. Substituting their positive multiples gives the two jj′ equations. For v₂(K)>0, v₂(X)=−v₂(K)deg(P)/D; for v₂(K)<0 it is zero. These establish the bounds and integer exclusions without assumptions on D beyond a proper factor. At u=1, φ is 6 or 3; at u=1/2 it is 27,9 or 3, and each fails.
6. For β=15^(−1/p) in Q₂, the odd-power map is an isometry on Z₂ units, so |u−β|₂=2^(−E). The bound gives |u−β|₂ ≪ u^(−p/2). Ridout with targets α∞=∞, α₂=β gives product |u−β|₂/u ≪ u^(−1−p/2); choose 0<ε<p/2−1. Thus finiteness holds for every fixed odd p, without any effective height bound.
7. At the largest real root ρ of abcd, all four parameters are nonnegative. If n(ρ)>0 the relation forces a(ρ)=b(ρ)=c(ρ)=0, contradicting their gcd. For D=2 all parameter degrees are even and the smallest coordinate has degree 2. Type II leaves an ET/constant-gap case; Type I leaves constant ratio, C, I-ad or A′. C is excluded by Z52D Proposition 3's Jacobi argument; A′ needs a reducible positive quadratic unless degenerate.
8. In cubic II-c, evaluating at the roots α,β forces both α>β and β>α. In II-a, evaluating at δ gives ζ<δ; evaluating at ζ then forces d(ζ)>0 although ζ<δ. For II-d, the displayed choices kill the remainders at ζ and α, so both quotients are genuinely polynomials.
9. Proposition 8: distinct positive exponential bases make a nonzero polynomial identity impossible on an unbounded progression (its largest nonzero exponential term dominates). At Z=∞, three positive coordinate degrees contradict the nonzero constant reciprocal sum; two force x=−y; one forces a zero reciprocal. Positivity excludes cancellation. This proves independence of every extra Z, not the μ = 0 assertion on an arbitrary progression.

Sources actually inspected: [Bennett, original paper, Theorem 1.1](https://personal.math.ubc.ca/~bennett/B-Crelle2.pdf) states at most one positive solution for fixed nonzero integer a,b and n≥3; it supplies exactly the required four-per-p bound. [Bilu, §2.1](https://arxiv.org/html/0907.2098v1#S2.SS1) states Ridout with algebraic local targets, including ∞; §2.2 also gives the equivalent two-dimensional subspace-theorem argument. [Capelli criterion, Theorem 1](https://arxiv.org/html/2012.07568v1#Thmtheorem1) confirms the rational binomial alternatives. The local paper's specialisation, T1, sterile, W, ratio and 60∤s arguments, and Z52D's C/shape lemmas, were inspected rather than inferred from the earlier review's approval.

## Computation replay

All shell jobs had `ulimit -v` ≤ 6000000, a CPU limit and `timeout`; long jobs used 1800 seconds. Branch files were extracted to `/tmp/xrev_THIN15`. No large Cartesian-product arrays were allocated. Every completed replay below exited successfully; the source p=13 Thue timeout is not treated as evidence.

| Replay | Independently observed result |
|---|---|
| New `scripts/z53_xrev_thin15_certificates.py` | All 50,000 certificates in strict order, no gaps/duplicates/failures. Modular checks prove both divisibilities without constructing every n; 10,004 literal product identities also pass, including t=50,000. |
| Certificate statistics | max m=167; m=3: 21,285; m=7: 14,393. For t≤10,000: max m=131, counts 4,250 and 2,904. All agree. |
| `z53_thin15_menuB.py int 3000` | 0 candidates with u≥3; one u=1 limit pair; 0 exact survivors, 0 flags. |
| `z53_thin15_xcheckB.py 200001 13` | Only u=1 for p=3,5,7,11,13, always (X,X′)=(6,5). |
| `z53_thin15_menuB.py dyadic 72` | 10,696,791 windows; one limit solution; 0 exact survivors, 0 flags. |
| `z53_thin15_menuB.py sgdyadic 90` | 3,106,120 windows; 0 limit solutions/survivors/flags. |
| `z53_thin15_thue.py 3 11 SG` | All 16 Thue solution lists agree, none with r,v>0 and v even; SG gives only (−1,0),(1,0). PARI uses unconditional `thueinit(...,1)`. |
| `z53_thin15_sweep.py 15 40 19` | 5,221 tests; 0 limit hits. |
| Menu positive controls; H=12, P=13 control sweeps | Cubic c₀=3 B family and c₀=63 A family recovered; full sweeps give respectively 11 and 4 hits, matching the memo. |
| `z53_thin15_iid3.py 32 16` and symbolic self-test | 5,055 rationals, 12,773,985 pairs, 0 passing Y=1. Separately checked that the floating endpoint selects exactly the rational inequality 15α³+1<0 on this grid. |
| `z53_thin15_census.py 3000 1000000` | 2,154 with a small prime factor (71.8%), 846 without; 0 failures of n≡121 mod 840. Frequencies agree. |
| `scripts/c1_expfam_verify.py --smax 1000` | Existing paper verifier passes, including W's exclusions/positive controls and the complete period-60 covering with residue 0 excluded. |

The checker is reproducible with `uv run --with gmpy2 python scripts/z53_xrev_thin15_certificates.py /tmp/xrev_THIN15/data/z53/thin15` under the same limits. Other replays use the branch scripts with `uv run --with gmpy2 --with cypari2 python ...` (sympy for the symbolic check). The conjunction of the 50,000 certificates, the 60∤s theorem and the elementary solution for n₀=16 establishes precisely the advertised range 0≤s≤3,000,000.

## Required fix, in priority order

1. **Scope, Proposition 8 and its summaries:** conclude “x,y,z belong to Q[Y], valid on the original progression.” Add “If that progression contains all sufficiently large multiples of a modulus, this is a root family through μ = 0.” Do not silently identify an arbitrary progression with such a neighbourhood.
   Concrete counterexample to that identification: take n=15Y+1 and x=(2n+1)/7, y=2n, z=2n(2n+1)/7, independent of every Z. These satisfy the identity and are positive integers at Y=2^s for s≡1 mod 3. But x(1)=33/7 is not dyadic, so this certificate is not through μ = 0. The residue-0 hypothesis supplied by Proposition 7 repairs its use in the covering discussion; the collapse theorem itself needs no change.

Optional exposition improvement: include the two-line Ridout specialisation in item 6 above, to prevent confusing the integer threshold 1 with unrestricted rational approximation's threshold 2.

## Labels and verdict

The finite-range and finite-height CERTIFIED labels are supported by exact, completed computations. The rational-height sweep and II-d search are honestly EVIDENCE, not global exclusions; unrealised limit candidates are correctly called a superset. Bennett/Ridout finiteness is not emptiness and is not uniform in p. The high-height, odd-denominator, non-binomial and Laurent/rational escapes remain explicitly open. After the Proposition 8 scope fix, **ACCEPT-WITH-FIXES; narrowed**, with no implication for ES on general primes and no all-s theorem for 15·2^s+1.
