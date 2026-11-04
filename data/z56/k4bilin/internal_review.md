# Hostile internal review — Z56_K4BILIN

## Decision: REJECT the claimed Type II frontier; retain the Type I/almost-prime work after repairs

**FATAL:** (TII*) is false for the stated comparison sequence. A fixed congruence modulo 7 supplies an explicit counterexample. Consequently Theorem V has an impossible hypothesis, (C4_N) is also false, and the proposed FRONTIER text must not be adopted. This is a local obstruction, not an inaccessible four-fold correlation estimate.

**Survives:** the arithmetic core of Lemma T*, its density, and Proposition P. The proof of T* needs a uniformity/endpoints repair; the Harman argument separately uses T* outside its stated squarefree-modulus scope. The prime-route budget and numerical computations are useful, but substantially weaker than some of their descriptions.

Reviewed the 311-line memo, the specified context and programs, FI 2009 Lemmas 4.1–4.2, the local Sedunova text, and the hypotheses of FI, *Asymptotic sieve for primes*, arXiv:math/9811186 (downloaded with a timeout). No memo or source code was edited. No commit was made.

## 1. Lemma T*: MAJOR presentation/uniformity repair; arithmetic core OK

### 1.1 Primitive expansion — OK

Every representation has a unique positive gcd, so

`r(N) = sum_{e²|N} r*(N/e²)`, hence `r*(N) = sum_{e²|N} mu(e) r(N/e²)`.

For odd N, a primitive representation excludes every inert prime; conversely an integer supported on split primes has `r*(N)=4·2^omega(N)`. This includes N=1. The product expansion and its signs are correct.

### 1.2 Coprimality and reduced residues — OK

On n=97 mod 120, `(n N1 N2,30)=1`. The identity `4N1-N2=15` gives `(N1,N2)=1` on this class, hence `(e1,e2)=1` and `(e1e2,30)=1`. For d|n with (d,30)=1, both shifts are units modulo d. Thus `(d,e1e2)=1`.

For k|v, `(k,30d)=1`. Also `(k,e1)=1`: a common prime would divide both shifts and therefore 15, which is excluded. Sharing primes between k and e2 is allowed and is correctly retained in the Euler product.

The moduli `d`, `e2²k`, `120` are pairwise coprime; the indicated classes are units. In particular `q=120 d e2²k` is divisible by 8, and its residue has chi(c)=1. The Smith main term must be doubled; the memo correctly doubles it.

### 1.3 Large-square-divisor tail — OK, with epsilon bookkeeping made explicit

The displayed reduction from a pair sum to a single e sum is justified by charging, for each n, the remaining square divisors to `tau(N1)tau(N2)`. Combine this and the two r-bounds into ONE `x^eta` allowance; do not spend the full epsilon independently on every bound.

CRT then gives at most `x/(d e²)+1` choices. There are `O(sqrt(x))` possible e, not `O(sqrt(x)/d)`; the separate `x^(1/2+eta)` term is essential and is present. With E=x^(8epsilon), the first term is `x^(1+epsilon)/(d sqrt(E)) = x^(1-3epsilon)/d`. Summing over d≤D gives `x^(1-3epsilon) log x + D x^(1/2+epsilon)`, which is harmless for D≤x^(1/6). No missing factor D belongs in the first tail term.

### 1.4 Smith input and interval endpoints — MAJOR as literally stated, repairable

The memo accurately transcribes FI 2009 (4.2), including the reduced-residue assumption, the factor `1+chi(c)`, and the distinction between an error estimate and the range in which it is an asymptotic. The quoted `q<y^(2/3-epsilon)` is the latter, not automatically a restriction on using an error bound.

However, the memo's unrestricted assertion “for (c,q)=1 and y≥1” cannot be literally uniform over all q. Take c=1, y=1 and q→infinity through multiples of 120: the sum is r(1)=4, whereas both the main term and the stated error tend to zero. The FI display must be used with its customary range understood, or supplemented by a trivial endpoint term. This matters when applying it at the LOWER endpoint `(k²e2²+15)/(4e1²)`, which can be smaller than q or smaller than 1.

A concrete repair suffices for this application. Work first with d≤x^(1/6). The upper endpoint Y=(x+4)/e1² satisfies q≤Y for small fixed epsilon, since `q/Y << d e1² e2 / sqrt(x) << x^(-1/3+16epsilon)`. At a lower endpoint y<q, count the at-most-one member of the reduced progression trivially, giving error `O(x^eta)`; if y<1 the sum is empty. At y≥q use the standard Smith bound. The extra errors over all small e and k total

`O(x^(1/2+eta) sum_{e1e2≤E} 1/e2) = O(x^(1/2+8epsilon+eta))`.

They are absorbed by `d^(-1/2) x^(11/12+epsilon)` in the working d-range. For larger d the pointwise assertion can instead be obtained from the trivial bound `A*_d << (x/d+1)x^eta`, with eta chosen sufficiently small. State this, or cite a precise uniformly valid version of Smith. The source's unqualified display is not a reason to assert a mathematically impossible all-q estimate.

### 1.5 Smith error sum and level — OK

After the two endpoints, the absolute error sum is bounded by

`d^(-1/2) x^(2/3+eta) sum e1^(-4/3-2eta) e2^(-1) sum_{k≤2sqrt(x)/e2} k^(-1/2)`

`<< d^(-1/2) x^(11/12+eta) sum e1^(-4/3) e2^(-3/2)`.

The double series converges. Summing d^(-1/2) to D=x^(1/6-4epsilon), using eta≤epsilon, gives x^(1-epsilon). The tail sums are smaller. This is a level **x^(1/6-o(1)) / any fixed exponent below 1/6**, not the exact endpoint x^(1/6) without loss.

### 1.6 Hyperbola boundary and completed sums — OK with clarification

Here v≡5 mod 8, so v is NEVER a square. The isolated square term in the hyperbola identity actually vanishes; the stated O(x^(1/2+epsilon)) is safe but unnecessary.

For the k² boundary, write the extra multiplicative k-weight as `1*nu`, with nu squarefree-supported and |nu(p)|≤1/p, omitting primes already in e2. Inclusion-exclusion for `(k,30de1)=1` gives a bound of the shape `2^omega(30de1) log(2K)` for the partial character sums. Partial summation gives `sum_{k≤K} chi(k)h(k) k << K x^eta`. After the prefactors, the e-sum is bounded by `x^(1/2+eta)/d` times a convergent e1 sum and a harmonic e2 sum.

Likewise, for FIXED e1,e2, completing the k-series costs

`<< x^(1/2+eta)/(d e1² e2)`.

This is the useful bound to print before summing e. The memo's loose `x^(1/2+epsilon)e2/d` suppresses those prefactors and does not explain the summation. Completing the e-product costs `<< x^(1+eta) log(2E)/(d E)` since `sum_{e1e2>E} 1/(e1²e2²) << log(2E)/E`. These estimates fit the claimed total error after allocating epsilon margins.

### 1.7 Euler factors, identity, positivity — OK, independently checked

For l∤30d the three allowed cases contribute respectively `1+chi/l`, `-1/l²`, `-1/l²`. Thus `E_l=1+chi/l-2/l²`. At l|d the factor is `(1/l)(1-chi/l)`. Their ratio is exactly

`(l-chi)/(l²+chi l-2)=1/(l+2chi)`.

SymPy simplified the difference to zero separately for chi=+1 and -1. I also independently enumerated all residue classes modulo each of 7,11,13,17,19,23,29,31: give a shift local multiplier 2 at a split prime dividing it, 0 at an inert prime dividing it, and 1 otherwise. The two roots are distinct, and the resulting weighted probability of n=0 is exactly `1/(l+2chi)` in each case. This checks the density without reusing the memo's Euler calculation.

All E_l for l≥7 are positive. The factorization into `(1+chi/l)` and `1-2/(l²+chi l)` is correct. The latter product is absolutely convergent and positive; the former is interpreted in the usual prime order and equals the stated positive L-value product. Hence c*>0. Do not describe the entire E-product as absolutely convergent.

## 2. Proposition P: OK after the T* uniformity repair; modest novelty only

The squarefree-modulus version of T* is enough for the linear sieve. The sequence is nonnegative, g*(l)<1, and `g*(l)=1/l+O(1/l²)` gives the dimension-one product axiom, uniformly after adjusting the constant for small primes. The missing primes 2,3,5 never divide an integer in the chosen class.

At s=2.1 the applicable lower function is `2 exp(gamma) log(s-1)/s`. Independently computed:

`f(2.1)=0.16167079276492338`.

The level and remainder saving dominate x/log x. To make the almost-prime bound explicit, take **0<epsilon<1/780** (and smaller if needed elsewhere). Then `(1/6-4epsilon)/2.1>1/13`, so z>x^(1/13) and every survivor n≤x has Ω(n)≤12. Multiplicity is counted: n need not be squarefree, and no squarefree-n hypothesis is being smuggled in.

For deweighting, retain the S indicators in the inequality:

`(a*_n)² ≤ 128[16^omega(N1) 1_S(N1)+16^omega(N2) 1_S(N2)]`.

The multiplicative mean has prime value 16 on half the primes and zero on the other half, giving exponent 8-1=7. Thus the second moment is `O(x(log x)^7)`, and Cauchy–Schwarz gives `(x/log x)²/[x(log x)^7]=x/(log x)^9`. Both the exponent and the use of all integers rather than squarefree integers are correct. The mean-value upper bound is sufficient; no asymptotic for it is needed.

**Statement as written:** the substantive conclusion is supported by this argument once T* is made literally valid. No additional conjectural input is needed. “Composite n” should read “n not required to be prime”: the proof does not assert that the counted integers are composite.

**Novelty assessment — MINOR qualification:** this is a useful dense-count, determinant-15, primitive/S refinement of a standard argument, not a new sieve mechanism. Sedunova's cited result uses r(n−2)r(n+2), squarefree n and a weighted count; its bound 7 is not directly comparable to this distinct-integer S-pair count. P415 Prop C already supplies infinitely many P2 values with both shifts in S, on a thin quadratic family (and a different class, 1 mod 120). The genuine additional feature here is the near-linear lower count and the explicit S-weighted distribution law, not the first unconditional almost-prime version of the target. P415 already anticipated a dense P_r version. Publication-level novelty has not been established by this search.

## 3. Theorem V: FATAL — its Type II hypothesis is impossible

### 3.1 Explicit local counterexample

Let M be a power of x inside the asserted Type II range, for example M=x^(1/3), and let N=x/(4M). Choose coefficients supported on

`M<m≤2M, m≡1 (mod 840)` and `N<n≤2N, n≡577 (mod 840)`.

These are 0/1 coefficients, hence allowed. All products satisfy

`mn≤x`, `mn≡97 (mod 120)`, `mn≡3 (mod 7)`.

Therefore **7 divides mn+4, so a*_(mn)=0 identically**, whereas w_(mn)=f(mn)>0. There are ≍MN/840² ≍x such pairs (the implied constant is fixed). For every prime l≥7,

`c_l ≥ (1-1/l)^3`,

so `f(t) ≥ (phi(t)/t)^3 >> (log log x)^(-3)` for t≤x. Since the scalar lambda is bounded below, the proposed Type II sum has absolute value

`lambda sum w_(mn) >> x/(log log x)^3`,

which is NOT `O(x(log x)^(-A))` for any fixed A>0.

The issue is conceptual: **matching densities for divisibility l|n does not match the densities of the shifted sequence in unit residue classes modulo l.** The model assigns positive mass to forbidden residues. No improvement of Type I or any four-fold correlation technology can prove (TII*) as stated.

An independent small-box check at x=10^9, M=3000, N=83333 found 396 such pairs: their a* mass is exactly zero and their model mass is 404.84879196545256. The proof above, not this finite experiment, establishes the contradiction.

A hypothetical model with growing local residue information, or a different sieve criterion with restricted/Möbius-type coefficients, would require a new statement and a new verification. Adding modulus 7 alone is not a repair: every inert prime supplies analogous forbidden residues.

### 3.2 Divisibility model W_d — OK for the proper domain

For squarefree d coprime to 30, the claimed density for W_d is correct. Expanding `f=1*h`, with h squarefree-supported and h(l)=c_l−1=O(1/l), gives the main term by counting a class modulo `120 lcm(d,k)`. The floor errors and completed-series tails are `O_epsilon(x^epsilon)` uniformly in the relevant d-range. This claim is not the fatal problem.

For GENERAL d, the density must be extended as

`g_tilde(d) = (1/d) product_{l|d} l/(l+2chi(l))`,

so `g_tilde(l^e)=g*(l)/l^(e-1)`. It is zero for d sharing a prime with 30. The squarefree product formula for g* cannot simply be used on all m in Harman's Type I hypothesis.

### 3.3 Harman ranges and Type I proof — MAJOR separate gap, otherwise reasonable

The secondary statement in lit_report.md supports the stated Type I form (arbitrary divisor-bounded coefficients on m) and the Type II interval `(x^alpha,x^(alpha+beta))`. With beta=1/2, alpha=alpha0−epsilon and M=x^alpha0, the strict M>x^alpha requirement is satisfied. A weighted version is plausible from the combinatorial proof, but should be stated/cited as such rather than justified merely by the word “linear”. The prime extraction at sqrt(x), including a negligible boundary/1 contribution, is harmless.

**Gap:** Lemma T* is stated and summed only for squarefree d; the proof of (I) sums over ALL m≤M. No squarefree assumption on n removes this gap. Prove the general-modulus extension with g_tilde above (the same CRT argument should provide it), or supply a correct squarefree-only variant of the required Harman theorem. Do not silently replace one by the other.

Once that extension exists, the Cauchy–Schwarz upgrade is valid: the first weighted error moment is bounded by divisor moments of a*, and the established second moment plus standard divisor-function moments gives x times a power of log x. Combining with the power-saving unweighted error sum gives a power saving, which is more than enough for the logarithmic Y used in (II). The same Y can be chosen for both estimates for sufficiently large x.

The asymptotic weighted-prime constant H* is formally consistent with the mean of f and PNT in the fixed class; with a valid prime-count asymptotic it follows by partial summation, rather than being an additional mysterious heuristic. But this does not rescue the impossible (TII*).

The FI alternative is accurately described as requiring level D>x^(2/3), far beyond T*. FI Theorem 1 also assumes squarefree support; its later extension has additional hypotheses. Its Möbius-type bilinear condition is not the impossible all-coefficient comparison asserted here.

## 4. Proposition D: inequality OK; FATAL as an attainable criterion; MAJOR overclaims

**OK:** Cauchy–Schwarz in m, followed by expansion and absolute values, gives the displayed inequality (with complex conjugation if coefficients are complex). `sum_{m≤x/N} tau(m)² << (x/N)(log x)^3`, so the stated scale xN with sufficiently many logarithms in the denominator is a sufficient condition for a Type II bound.

**FATAL:** (C4_N) cannot hold for the E in this memo. Swap the two factors in the congruence counterexample so that the smaller factor is called n and N≤sqrt(x). Cauchy–Schwarz using its 0/1 m-coefficients already forces the absolute correlation sum to be at least `>> xN/(log log x)^6`. This contradicts (C4_N) for the claimed logarithmic saving. The local covariance has not been subtracted.

**MAJOR:** evaluating the four-fold a*a* sum does not automatically give (C4_N). One must identify the pair-dependent singular series, compare it with BOTH mixed terms and the ww term, and show the residual absolute sum is small. Here it is not. “An asymptotic for almost all pairs” also needs a quantitative exceptional-set contribution and uniform weighted error bound; qualitative almost-all asymptotics are insufficient. The diagonal n1=n2 requires its own bound, though the available second-moment/divisor bounds make it negligible for N a fixed positive power of x.

**MAJOR:** the congruence indicators are missing from the displayed four-fold correlation. For simultaneous nonzero terms one needs compatible classes `mn1=mn2=97 mod120`; in particular n1,n2 must be units and congruent modulo 120. Preserve these restrictions in the correlation and its local factors.

**MAJOR:** “four pairwise affinely independent linear forms in one variable” is false. Any two nonconstant affine forms of one variable are affinely dependent. For n1≠n2 in the same dyadic interval, these forms have distinct roots and are pairwise nonproportional as coefficient/intercept pairs; that is NOT the finite-complexity hypothesis in the cited Matthiesen results. The memo itself correctly explains the affine-dependence issue a few lines later and thereby contradicts this phrase.

**MAJOR:** a*w is a TWISTED Type I problem, not supplied merely by an ordinary level N statement. Writing `f(mn2)=f(n2) sum_{h|m} h_{n2}(h)` introduces moduli n1 h (and fixed congruence restrictions). A truncation and uniform twisted error analysis are required; level N with no margin is not automatically enough.

**MAJOR:** the implication runs **C4_N => Type II**, not conversely. “Type II is at least as strong as four-fold correlations”, “needs Type I up to x^(1/2)”, and “in every version” reverse or overstate this sufficient Cauchy–Schwarz route. Such inputs might be one attempted proof strategy, not necessary conditions for a Type II theorem. Theorem V itself proposes to use the existing Type I level, not an assumed higher one.

**Literature — MAJOR scoping correction:** the sources support that general nondegenerate individual-shift triple/four-fold problems are difficult and that the cited finite-complexity theorems do not directly apply. They do not prove the universal statement “no one-variable correlation of ≥3 values of r or tau is known”: degenerate/proportional examples and local-zero cases already defeat that wording. Say no applicable uniform, nondegenerate, almost-all-coefficient estimate was found. An absence of individual-shift theorems also does not exclude the averaged estimate actually sought here. Grimmelt–Merikoski's ≈0.281 is a fixed-progression range for a divisor correlation, not a ready-made r-weighted averaged level.

The analogous “Route S is not a route” conclusion is also too strong. Cauchy–Schwarz exposes a difficult averaged binary-prime correlation as one sufficient input; it does not prove that every approach requires an individual twin-prime theorem. Label it a diagnosis of this particular dispersion attempt, not an impossibility result.

## 5. Prime-variable route: scoped budget OK; formula/literature qualifications MAJOR

### 5.1 The 3/4 budget — OK only with its stated architectural scope

If one retains the full k≤sqrt(x) hyperbola range and estimates the resulting prime progression errors through a total-modulus level, the budget is theta=1/2+theta_D. With fixed-power z>x^(1/4) and positive semi-linear lower function requiring D>z, this demands theta>3/4. This is elementary bookkeeping, not a lower bound for all prime-variable methods or all bilinear methods. Cancellation in k, other decompositions, or different switched estimates are outside the argument. Avoid calling it an intrinsic level barrier.

**MAJOR formula correction:** the overview writes `r*=4(1*chi)`, which is false; that is r. The body correctly supplies the square-divisor Möbius expansion. Its e² congruences must also be included in the displayed prime-modulus estimate (typically truncate e with a small power loss). The displayed (BFI_chi_lambda) is at best the e=1 schematic piece, not the complete sufficient input for primitive weights.

The CRT residue c_(k,d) is not defined for arbitrary k,d in the displayed sum. Require the relevant coprimalities with 30 and `(k,d)=1`; otherwise roots of the two shifts can conflict, since their determinant is 15. State the sieve-weight class, treatment of these exclusions, endpoints, and square-divisor tails before calling this the “exact missing” estimate.

### 5.2 Model reproduction — OK, not a theorem

Re-ran `scripts/z56_k4bilin_firoute.py` under uv with numpy. Its output matches `firoute.txt` byte for byte. The theta_D thresholds are:

| Loss | theta_D | total level |
|---|---:|---:|
| L=1 | 0.2570 | 0.7570 |
| 2 | 0.2816 | 0.7816 |
| 4 | 0.3847 | 0.8847 |
| 8 | 0.4459 | 0.9459 |
| 16 | 0.4737 | 0.9737 |
| 32 | 0.4871 | 0.9871 |
| 64 | 0.4936 | 0.9936 |
| 128 | 0.4968 | 0.9968 |
| 1000 | 0.4996 | 0.9996 |
| GEH pen=1 | 0.4081 | 0.9081 |
| GEH pen=2.35 | 0.4583 | 0.9583 |
| GEH pen=5 | 0.4800 | 0.9800 |

Every quoted rounded threshold agrees. These optimize the supplied inequality only. The 2000-point theta_z grid and tabulated floating-point sieve functions are not rigorous minimization/error certificates. The script's “none <1/2” for L=10000 is a resolution issue, not evidence of an actual barrier; the optimum approaches the endpoint.

P415 §2(b) indeed gives 0.9962 for ordinary-EH main distribution with BV switching and 0.9764 for its ADDITIONAL GEH-type switched model. The memo's numerical comparison is faithful if kept explicitly model-to-model. These are different weighted architectures; no theorem establishes the improvement 0.9764 to 0.9081.

### 5.3 Literature levels — MAJOR verification/scope corrections

The quoted 4/7, 3/5 and 66/107≈0.616822 are consistent with the cited fixed-residue/well-factorable line of work. The arithmetic difference `3/4-66/107=57/428≈0.133178` is correct. None is automatically applicable to the chi(k) times semi-linear-sieve weights here: well/triply-well-factorability must be proved, not inferred from a numerical level.

**Verification mismatch:** the memo says Lichtman Corollary 1.5 is “VERIFIED there”; the supplied lit_report.md Q4(c) labels arXiv:2309.08522 **ABSTRACT-ONLY**, and Q5 does not provide that corollary. Downgrade the tag or supply the actual checked theorem. “Current record/best” also needs a dated, scoped verification rather than a universal assertion from this search.

The report verifies Maynard III Theorem 1.2 with delta<1/1000 and strong factor-size/residue restrictions. Theorem 1.3 concerns an equidistributed **prime minorant of mass at least pi(x)/8**, not an asymptotic for all primes. Do not merge these into a blanket prime equidistribution statement for arbitrary mixed CRT moduli. The fixed-residue restriction applies to the specified spectral BFI line, not every dispersion theorem.

MPZ has smoothness/factorization restrictions; the report's extension from its stated monic polynomial to `(p+4)(4p+1)` is explicitly a derivation not checked in a source. Preserve that qualification. A numerical comparison with 0.617 is informative, not a proof that all existing techniques fall short by exactly that amount for every relevant weighted variant.

## 6. Numerics: integer computations OK; broad readings MAJOR/FATAL

### 6.1 Reproduction and independent checks — OK

All compiled/Python jobs ran with virtual-memory limits (at most 6,000,000 KB), all shell jobs with timeouts ≤700 seconds. Recompiled both C programs with `gcc -O2 -lm` and obtained byte-for-byte matches for:

- typeii: X=10^8, class 97, against `typeii_100000000_c97.txt`;
- spectrum: X=10^9, against `spectrum_1e9.txt`;
- additionally spectrum: X=10^10, against `spectrum_1e10.txt`;
- additionally typeii: X=4·10^8, class 97, against `typeii_400000000_c97.txt`.

An independent SymPy factorization loop over n=97 mod120 up to 10^6 gives:

| Quantity | Independent value |
|---|---:|
| sum a | 352832 |
| count a>0 | 2254 |
| S-pair count | 2037 |
| prime S-pair count | 535 |
| sum mu·a | −3904 |
| sum lambda_Liouville·a | −4800 |
| sum a* | 313920 |
| sum mu·a* | −576 |
| sum over primes a | 95296 |
| sum over primes a* | 82688 |
| sum w (double-precision independent computation) | 9068.067695811895 |

The C outputs at 10^6 agree, including prime spectrum ratio 0.9690. An independent divisor-enumeration implementation at N=999 gives `B_a=0.09813168873571558`, `T_a=0.16052965717395248`, and `B_control=0.15152629643251195`, agreeing with the C output. The local-density symbolic/enumeration check is in §1.7.

### 6.2 C logic — OK in the documented runs; precision qualifications MINOR

The factorization logic correctly distinguishes inert primes of odd exponent (r=0) from inert primes of any positive exponent (S false). Split-prime exponents give r's (e+1) factors; distinct split-prime counts give r*'s powers of 2. The n factorization correctly produces Ω, mu, lambda, and primality. The typeii program skips factoring 2 out of the shifts, which is safe for the supported odd class, though not a general-purpose factorization routine for unsupported even n.

In the spectrum code, spf is set at the first prime encountered; square detection and Ω=2 select distinct-prime semiprimes. In class 97 there are no squares anyway. A residual prime above 2^32 can truncate spf at X=10^10, but that field is used for binning only when Ω=2; then the smallest prime is ≤sqrt(X), so the reported bins are unaffected. The model multiplier is applied once per distinct prime, as required. The B code uses mu(mn), not an unjustified product mu(m)mu(n), and forms the stated sums correctly. The control has `mu(t)(1+lambda(t))=2` on squarefree even-Ω t and zero otherwise, explaining B=T exactly.

The a/a* integer totals in these runs are exactly representable in double. Spectrum model weights are stored as float, and logarithms, ratios, H and random-sign references are floating-point quantities, not certified exact real values. The spectrum output rounds even its integer masses in scientific notation. The code does not constitute an interval certificate for a sharp percentage cutoff. Floating accumulation of t makes the last printed N be 9999/19999 rather than exactly sqrt(X); harmless for these descriptive tests but worth correcting in a future implementation.

### 6.3 Audit of all quoted numerical groups

**OK:** all eight g-values in §2 match `spectrum_1e10.txt`. All nine P2 ratios, the prime ratio 1.0005, Ω=3 ratio 0.9997, S ratio 0.9996, and both Liouville ratios 1.0000 match that file and its rerun. The H*=3.44604 value, 105771 prime S-pairs at 4·10^8, and both sets of prime-log ratios agree with the files. At 10^6 the ratios are 0.9801 and 0.9722, consistent with the rounded memo values.

**MINOR correction:** the overview's “PNT prediction holds to 0.3% at 4·10^8” is too tight: the printed deviations are 0.33% for a and 0.38% for a*. Use approximately 0.4%.

**OK numbers, qualified reading:** at 4·10^8 and the balanced endpoint, `B_a=0.03624`, `R_a=0.03532`, `T_a=0.1663`; the S-indicator values are 0.02836 and 0.1706. At t=0.4 the values are 0.08698, 0.07975, 0.1655. These match the memo's rounding.

**MINOR/MAJOR wording correction:** “B=T=0.167 at every N” is false numerically. Equality B=T holds exactly, but the common value varies: 0.1766 at t=0.20, 0.1663 at t=0.25, 0.1680 at t=0.35, 0.1668 at t=0.50. At t=0.20 the ORIGINAL sequence also has B=T: there is no cancellation there. Claim random-sign-like behavior only for the tested sufficiently long inner ranges, not uniformly across all displayed scales.

**MAJOR:** this B-test is for a=r·r and for the S indicator, NOT for a*=r*·r*. The code calculates a* totals but no a* B-statistic. It tests only gamma=1 (C=1), not FI's full family `gamma(n,C)=sum_{d|n,d≤C} mu(d)`. FI explicitly excludes the endpoint N=sqrt(x) from its required range (`N<sqrt(x)/delta`, delta≥2), and warns that its full B estimate is unrealistic at that endpoint. The balanced numerical value is a diagnostic, not a verification of FI's hypothesis.

**FATAL interpretation:** positive prime/semiprime-band totals do not test all divisor-bounded coefficient sequences. They average away the forbidden-residue discrepancy in §3. “The missing Type II estimate looks true”, “exactly Harman's Type II pieces”, and “no hidden algebraic obstruction” must be removed. The literal estimate is false despite the excellent unconditioned spectrum. Call these prime/semiprime spectrum diagnostics, not validation of (TII*).

**OK:** the class-1 control file gives square mass 1.129%, Liouville ratio +0.008217 and prime-log ratio 0.9893; the class-97 file gives −0.002840. These match the text. The square contribution is thin and does not by itself obstruct scale-x estimates, although it does not justify ignoring the unrelated fixed-prime residue obstruction.

**OK:** independently factored all 15 listed FRONTIER test primes. The eleven claimed positive cases have both shifts in S, and all four negative cases have p+4 outside S. Only 577 and 329617 are 97 mod120. Note 193 is 73 mod120; “most are 1 or 49” is nevertheless correct. Transferring the theorem to classes where both shifts share 5 requires an actual separate local argument; “split off the 5-part” is not that proof. Nothing in the present conclusion needs that extension.

## 7. Labels and FRONTIER: FATAL proposed entry; narrowed verdict only after substantial revision

**OK:** nothing proves ES, and the equivalence of the prime target with K(4) is used only as provided by HCKILL. The kill-side/infinitude scope means the four discussed FRONTIER screens do not require a prescribed-p ES proof. Odd-square confinement, specificity to the line-4 shifts, and the absence of a claimed upper-side tied-modulus mechanism are accurately distinguished. “Passes trivially” should mean “not an applicable ES upper-side test here”, not that a route to ES has passed the hard screens.

**MAJOR:** the strong claims under PROVED are not all in the same state. T* has a correct-looking core with a repairable uniformity gap; P follows after that repair; the Cauchy–Schwarz inequality is proved but its advertised attainable correlation target is false. Theorem V is formally a conditional implication with an impossible antecedent, not a meaningful conditional advance toward K(4).

**FATAL:** the proposed FRONTIER entry repeats the impossible (TII*), reverses sufficiency into necessity for four-fold correlations, makes an overbroad literature nonexistence claim, and treats restricted positive spectra as evidence for an all-coefficient estimate. Do not install it. Exact level x^(1/6) should also be written with the usual epsilon loss.

A defensible “narrowed” verdict can cover the explicit Type I density, the dense P12 theorem, and the scoped prime-route model budget. It cannot presently cover “both formulations pinned down” or “no hidden obstruction”: this review exhibits a fixed local obstruction in the dense formulation. The analytic prime problem remains open; the proposed comparison formulation must first be redesigned.

## Required fixes, in priority order

1. **FATAL:** withdraw (TII*) as a plausible hypothesis and rewrite §§0, 4, 6, 8 around the explicit modulo-7 counterexample. Do not claim that its proof merely awaits stronger correlations. Any replacement comparison model/criterion needs a fresh local-residue audit.
2. **FATAL/MAJOR:** withdraw (C4_N) as an attainable estimate for this E. Keep only the valid Cauchy–Schwarz implication; include singular-series covariance, fixed-class indicators, quantitative exceptional sets and diagonal terms in any replacement.
3. **MAJOR:** repair Smith's all-q/endpoints formulation, document the completed k/e-tail sums, and prove the general-modulus density extension before invoking Harman Type I. Proposition P itself only needs squarefree moduli.
4. **MAJOR:** replace “affinely independent” by the appropriate distinct-root/nonproportional description; reverse the erroneous necessity claims to sufficient-strategy statements; scope literature nonexistence and Route S assessments to what was actually checked.
5. **MAJOR:** correct the primitive divisor identity in the overview and make (BFI_chi_lambda) explicitly schematic or include square-divisor moduli, compatible CRT restrictions, endpoints and weight hypotheses. Retain >3/4 only as this architecture's full-range level budget.
6. **MAJOR:** correct Lichtman's verification tag; distinguish Maynard's prime minorant from full-prime distribution, and retain the MPZ applicability qualification. Keep 0.908/0.976/0.996 explicitly model-dependent, not certified sufficient theorems.
7. **MAJOR/MINOR:** relabel the B-test and spectrum as restricted diagnostics, not evidence for the false uniform Type II claim; correct the 0.3% summary and the constant-at-every-N control claim; distinguish exact integers from floating-point weights/ratios.
8. **MINOR:** credit P415's existing thin P2 result when describing novelty; specify epsilon<1/780 for P12; avoid asserting compositeness or unproved transfer to all admissible classes. Only then draft a replacement FRONTIER entry limited to the surviving results.
