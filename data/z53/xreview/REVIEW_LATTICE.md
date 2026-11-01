# Z53 LATTICE — independent hostile cross-review

Reviewed `side-agent/z53-lattice` at `cda31d139f7c374187ced4129ee81b454f3bc311`.
**Verdict: ACCEPT-WITH-FIXES.** The central no-go theorems survive. The scoped verdict **narrowed** follows, not a general death of geometry of numbers. ES remains OPEN.
Review performed independently from the proofs and executable sources; no reliance on the R1 verdict.

## Per-claim audit

| Claim | Classification | Independent check / qualification |
|---|---|---|
| Def. 1.1 / Thue mechanism | CORRECT | Covering forces every lattice translate to meet K; centred compact Minkowski at volume ≥8D′ gives a noncentral point. V1 is only a weaker necessary volume condition, as explicitly stated. For the illustrative sum-of-squares disc, shrink its radius slightly to exclude 2p while retaining area >4p. |
| Facts 2.1–2.2 | CORRECT | Vanishing of both first gradient coefficients forces u,B,C units, making 4uB nonzero; at 2 the first coefficient is odd. The two coefficients of the C-linear polynomial are coprime, so Gauss's lemma excludes any plane. |
| Prop. 2.3 / A1 | CORRECT | Re-derived coefficient extraction, Smith-form bounds, the 3-adic loss, the unimodular 2-adic pairing, and CRT multiplication; details below. Oddness of n is essential in the 2-adic step and is a standing hypothesis. |
| Coset CERTIFIED table | CORRECT | All stated modulus/residue types checked: full reruns at q=2,…,9,11; valuation representatives at 25,27; independent upper/lower proof at 16. No extrapolation to arbitrary q justified. |
| Lemma 2.4 / V | CORRECT | Midpoint shell comparison gives R≤(n+D)/(n−D); the displayed polynomial inequality gives α²+β²≤4D/(n−D). Logarithmic projection widths and fibre integration yield (128/9)D²/(n−D), then (136/9)D²/n. |
| Lemma 2.5 | CORRECT | C≥1 and u,B≥1 force uB≤(n+D)/2. Integrating D/(2uB) over that product triangle gives D log²((n+D)/2)/4. |
| Lemma 2.5′ | CORRECT | Interval length plus one bounds each integer fibre; harmonic-sum and divisor-summatory upper bounds give exactly the stated count. |
| Lemma 2.5″ | CORRECT | Symmetry confines K to the box with side lengths 2c_i; 4c_uc_Bc_C≤c_u+c_B+n+D and c_u,c_B≤(n+D+1)/3 imply the stated (slightly loose) bound. |
| Thm. 2.6 / A, all thresholds | CORRECT | All four comparisons recomputed. Covering's integer-point count handles bodies approaching coordinate planes; it does not incorrectly apply Lemma 2.5 to real points below 1. Numerical thresholds are conservative. |
| Rank-3 affine reduction | CORRECT | AΛ has finite index and Φ(K)+AΛ=R³. Rank 3 and integral affine coefficients are necessary; the memo explicitly excludes lower rank. |
| Thm. 3.1 / A′ | CORRECT | Local index ≥D^(3/2)/(sqrt(gcd(D,N_C)) sqrt(32C)); the one-dimensional midpoint/area bound gives 9N_C/4096 for D≤n/7. The thick bound and uniform O(log²n) conclusion follow; independently checked 2,277 finite local cases. |
| Prop. 3.2 / D | CORRECT | Vertical multiples of D′ force X=−1, then a horizontal multiple contradicts that value. Requires the class condition on the whole coset, not only on points found inside K; this scope is present. |
| §3.3 nonconvex sub-count | CORRECT | G≡0 mod D and |G|<D force G=0, so the count is ≤R(n). The displayed volume expression is only a heuristic for a lattice-point count, honestly labelled. |
| Lemma 4.1 | CORRECT | Degree comparison forces two coordinates constant unless u+B+n=0; the latter forces one factor CuB zero. The five lines and their five-cycle, including the n=0 degeneration, check directly. |
| Cor. 4.2 / Thm. 4.3 / B | CORRECT | Restriction to affine lines plus the absence of a triangle in the intersection graph forces a single image line. Degree <ℓ in each variable upgrades finite-field vanishing to a polynomial identity; passing to the algebraic closure is legitimate. |
| §5.1 Lenstra / Coppersmith regimes | CORRECT | Source-checked Lenstra and Coron's statement of Coppersmith. P_C is primitive and irreducible since its bilinear determinant is −(4Cn+1)≠0. A root-containing positive box has W=4CXY, hence precisely XY<16C² for this sufficient guarantee. |
| §5.1 CHN boundary / count bound | CORRECT in the cited fixed-ε sense; source limitation | Boundary visibility s⁴>N is not a uniform fixed-ε complexity promise; the memo says so. Bernstein corroborates the fixed-ε regime and −3/2 rank exponent; the CHN full paper was blocked, so its exact count statement was not primary-source verified here. |
| §5.1 density integrals | CORRECT | Triangle-area ratios give 1/4,4/9,9/16; the all-Lenstra-invisible corner has relative area 1/36. These are model integrals, not pointwise proportions of R(n). |
| §5.1 every triple CHN-visible | CORRECT | If both u and B slices are invisible, n+m≥256m⁴. C-Lenstra invisibility implies 4C<uB≤m² and n+m=4CuB−min(u,B)<m⁴: contradiction. |
| §5.2 no existence content | CORRECT-WITH-FIX | Root propagation does not prove a root. The odd-square obstruction is valid for positive admissible triples, not for the entire integer root set of P_C; clarify the wording (fix 2). |
| §§5–6 EVIDENCE | CORRECT as observations | All four sample files reproduced byte-for-byte; prime sample selection independently verified. Correlations and binomial tail agree. Lack of detected correlation is not a theorem of independence. |
| §§7–8 screens / narrowed verdict | CORRECT within scope | Numerator generalization is explicitly unchecked Assessment. Surviving nonconvex, nonlinear, lower-rank and non-positive-octant approaches are retained. No ES conclusion follows. |
| §9 proposed FRONTIER text | CORRECT-WITH-FIX | Its fixed-C ≥N_C/456 claim drops D≤n/7. The actual theorem only supplies N_C/O(log²n) in the other regime; restore that distinction before adoption. |

## Proof reconstruction: sensitive steps

1. From s=±1,2 obtain 2Q=0, 2(L+T)=0, 6T=0. For ℓ≥5, H lies in a primitive rank-2 kernel W. With Smith exponents a≤b, some coefficient of Q or T on W is a unit, since otherwise t+W is a plane on V_n. Its weighted divisibility forces a+b≥f/3; thus |H|≤ℓ^(5f/3). No division by 3 is used in the subsequent coefficient extraction on W.
2. At ℓ=3 reduce to f−1 and pay a kernel of size 3³, giving index ≥3^((4f−4)/3). At 2 reduce to g=f−3; Q/4 has odd cross coefficient u+B on W_g, hence a perfect polar pairing. Isotropy gives |H̄|≤2^g; lifting costs at most 2⁹, giving index ≥2^(2f−6). Small f bounds are trivial. CRT then gives c₀=64·3^(4/3).
3. The shell midpoint argument uses convexity of 1/u and 1/B, not an unjustified global Euclidean thickness estimate. For D≤n/17, σ≤1/2 and each logarithmic projection width is ≤(8/3)σ. Integrating the actual vertical thickness D/(2uB) gives Lemma V.
4. For covering, each of the D′ integer cosets supplies a distinct integer point in K. For Minkowski, the centre is a positive integer point, so its symmetric box has controlled volume even when K contains real coordinates below 1. These are the crucial repairs that make the large-D cases valid.
5. Fixed C, good primes: isotropy bounds |H|≤ℓ^f when f≤v_ℓ(N_C). Otherwise v(X_t)+v(Y_t)=e and projection/kernel counting bounds |H|≤ℓ^((f+e)/2). Bad primes: L has unit coefficients and h_B=−κh_u modulo the required precision; the quadratic condition forces a square-divisibility bound. The losses multiply to sqrt(32C), including primes dividing C but not D harmlessly.
6. Fixed-C thin-shell area ≤(4sqrt(2)/3)D^(3/2)/(C sqrt(n′)), divided by the index bound, gives gcd≥9Cn′/1024=9N_C/4096. In the thick case area ≤D log(2(n+D+1))/(2C) gives gcd≥CD/(8log²). Since gcd≤4Cn+1, D/log²(2(n+D+1))=O(n), forcing D≤n² eventually, uniformly in C.
7. Odd-square control can be checked without trusting the repo's T1: if d=4Cu−1 divides m²+u, then gcd(d,u)=gcd(d,m)=1, but the Jacobi symbol (−u/d)=−1 because d≡−1 mod 4u, contradicting (m²/d)=1. This excludes positive triples, not signed polynomial roots.

## Reproduction / numerical agreement

All shell commands had memory/CPU ulimits and explicit timeouts. The existing 1999² NumPy grid was inspected before execution (bounded, far below 6 GB); other audits stream or use small finite groups.
Sources were extracted to `/tmp/xrev_LATTICE/`; no memo or lane data modified.

- Rebuilt both C programs with `gcc -O2 -Wall -Wextra`. Coset code has only unused-variable warnings; its depth-3 subgroup enumeration is complete because subgroups of (Z/q)³ admit ≤3 generators.
- Exhaustive q=2,…,9,11 reruns reproduce every n-residue row. For q=25, n=0,1,5 give max |H|=125,25,125; for q=27, n=0,1,3,9 give 81,27,81,81. The scaling automorphism covers remaining residues.
- A 70-second q=16 DFS and the initial 75-second q=27,n=3 DFS hit their caps. The latter completed under a deliberate 200-second cap; the former was replaced by an independent exact argument, not treated as a successful rerun.
- For q=16,n=1, V has 256 points but is not an affine coset: t=(0,15,0), a=(1,14,0), b=(0,15,1) lie in it while a+b−t does not. Any coset larger than 128 would equal V. Conversely C even and u+B≡−1 mod16 defines an exact coset of size 128. Scaling handles every odd n.
- `z53_lattice_checks.py`: c₀=276.911917499; grid minimum 0; thick-case roots D₁=7.83485·10¹⁴, D₂≈3.954·10¹⁶, D₃≈8.958·10⁹. Their 17-fold n bounds are ≈1.332·10¹⁶,6.721·10¹⁷,1.523·10¹¹; all published thresholds round outward. Thin-case 2.6·10⁸ passes the exclusion comparison.
- Reran 2,000 primes near 10⁷, 400 near 10⁹, 400 near-squares and 200 odd squares: byte-identical to all four stored regime files. Means R: 37.54,62.38,33.14,0; normalized means .1443,.1452,.1228,0. Every displayed regime fraction and prime correlation agrees.
- Independently regenerated both consecutive p≡1 mod24 prime samples using `sympy.nextprime`; exact list agreement. All 14 zero-prime controls have R=0; five additional controls have R=4,2,8,2,10 as claimed. The five small Thue angles give tail .1342.
- The summary script emits a harmless NumPy zero-variance warning for the all-zero square sample; its undefined square correlations are not used in the memo.
- New independent audit: `scripts/z53_xrev_lattice_independent.py` verifies 2,277 exact fixed-C subgroup/coset cases at q=3,5,8,9 and C=1,…,6 by HNF enumeration, the q=16 upper/lower bounds, and all seven regime counts for 250 odd n≤501 by direct (u,B) enumeration (no factorization). All assertions pass.
- Reproduce that audit after building the extracted regime executable: `ulimit -v 6000000; ulimit -t 65; timeout 60s uv run python scripts/z53_xrev_lattice_independent.py /tmp/xrev_LATTICE/regimes`.

## Required fixes, priority order

1. **Before recording §9:** change “At a fixed level C … ≥(4Cn+1)/456” to “if D≤n/7 … ≥(4Cn+1)/456; otherwise … ≥(4Cn+1)/O(log²n).” Retain the quantitative-modulus interpretation, not a factorization requirement. The unrestricted fixed-C claim is not supplied by Theorem 3.1.
2. **Clarify §5.2(b), and its summary:** say “empty positive admissible target-root set,” not simply “empty root set.” For example n=9,C=1 has the integer polynomial root (u,B)=(0,−9); even its box X=1,Y=9 meets XY<16C². This does not undermine the intended no-positive-existence argument.
3. **Editorial:** the summary's q² sentence must attach ℓ∤n explicitly to q=25,27 as well as q=9; the later alternatives/table are correct. Keep empirical lack of correlation phrased as “no detected correlation,” not mathematical independence.

## Citation checks and limits

- Read [Coron, EUROCRYPT 2004](http://www.jscoron.fr/publications/bivariate.pdf), Theorem 2 and §2: the quoted bivariate Coppersmith theorem is correct. Distinguish this cited theorem from Coron's own simplified algorithm, which needs an ε loss; the memo does distinguish them.
- Read [Lenstra 1984](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1984b/art.pdf), printed p.331 theorem: 0<r<s<N, gcd(r,s)=1, s>N^(1/3), at most 11 positive divisors, polynomial enumeration. Here r=s−1 is coprime; any out-of-range s≥N case is trivial direct enumeration.
- CHN [ePrint 2004/339](https://eprint.iacr.org/2004/339) abstract opened, but its equations disappear in extraction; ePrint/AMS/full-text mirrors blocked the PDF. Read [Bernstein §6, History after Theorem 6.4](https://pub.math.leidenuniv.nl/~stevenhagenp/ANTproc/old/13djb.pdf), which explicitly corroborates the CHN fixed-ε regime and total rank O(ε^(−3/2)). The exact CHN count citation remains a disclosed verification limit, not a premise of Theorems A, A′, B or D.

**Final assessment:** accept the scoped mathematical narrowing after fixes 1–3; do not record the unqualified fixed-C sentence or any global geometry-of-numbers impossibility. No central proof gap or counterexample found.
