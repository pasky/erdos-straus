# FOURIER hostile cross-review — ACCEPT-WITH-FIXES

Reviewed `side-agent/depth-fourier` at `342f262d91c3c028d6646ac063b715041095047a`.
Scope: `Z52D_FOURIER.md`, its scripts/data, and the cited local source statements.
**ES remains OPEN.** The core Fourier mathematics and decisive certificates survive independent checking.
The warranted verdict is **strongly narrowed**, not an unconditional collapse of every bounded-order or exceptional-character route.

## Per-claim audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| §1 box/coprime-pair bijection; Type II interpretation | CORRECT | Each signed exponent uniquely assigns its prime power to a or b. If a+b=et, then y=pNt/a and z=pNt/b are positive integers and 1/y+1/z=e/(pN)=4/p−1/N. |
| §2 exact identity (2.1) | CORRECT | Expand the product of Dirichlet kernels into the exponent box; character orthogonality selects the target. The inverse character at −1 equals the character itself. Multiplicity is retained. |
| Cor 2.2 and total obstruction mass | CORRECT | Add/subtract the two identities to obtain the even/odd sums. Divide by M and remove c(1)=−1; when r(−1)=0 the remaining signed sum is 1. |
| Lemma T; Cor T′ | CORRECT | For odd s, reciprocity gives (s/e)=(−e/s)=(p/s)=(s/p). For s=2 use e≡−p mod 8. Multiplication gives (N/p)=(e/p); applying the odd Jacobi character to a≡−b gives (ab/p)=−1. |
| Prop 1 and its killing/sign consequences | CORRECT | D_b(1)=2b+1 and D_b(−1)=(−1)^b. The product sign is (N/p)=(e/p); division by M gives the displayed exact rational formula. c=1 iff there are no nonresidue factors; forced windows have strictly negative c. |
| Prop 2(i)–(ii) | CORRECT | Divide any odd real character by the odd Jacobi character to get an even real character. Evaluation at N is evaluation at p·4⁻¹ mod e. A prime-power window has only one nontrivial real character, so nontrivial even real twists require composite e. |
| Prop 2(iii), all subgroup obstructions | CORRECT | In G/H, nonidentity −1 has order 2, so a character separates it from 1. Raising this odd annihilating character to the odd part of its order preserves oddness and annihilation and leaves 2-power order. Minimal killing order therefore is a power of 2. |
| Prop 3 | CORRECT | Forcedness supplies a nonsquare factor. Since q−1=2m with m odd, its order is even and its half-order power is the unique involution −1. |
| Thm B, character assertion | CORRECT | Any order d≤B dividing 2m has no odd prime divisor, while v₂(2m)=1. Thus d=2 for nontrivial characters, and Prop 1 gives negative c. |
| Thm B, stated L/L_abs consequence | CORRECT-WITH-FIX | Add H=G to the consequence: the lemmas being refuted quantify only over full-generated windows. This does not follow from Thm B's hypotheses plus obstruction; explicit example below. All reported decisive certificates do have H=G. |
| Prop B′ | CORRECT (CONDITIONAL) | CRT gives a reduced class for q modulo 8 times the small odd primes; Dirichlet supplies arbitrarily large q. Both linear forms are odd, nonzero mod q, and exclude at most two residues at every other prime. Dickson then gives prime p,N. A primitive-root residue forces the Jacobi sign and H=G; the three-point box misses −1. Take t sufficiently large for e<3p. |
| Prop B″ | CORRECT (CONDITIONAL) | Choose k positive odd and distinct fixed prime factors in the primitive-root class. At primes dividing C the p-form is nonzero; elsewhere the same local admissibility check works. Large Dickson solutions give k distinct factors, all nonresidues, hence c=−3⁻ᵏ. Their box exponents lie in [−k,k], short of (q−1)/2. Choosing k large proves the asserted conditional quantifiers. |
| Thm C | CORRECT | For positive integer k<m/2 and B≥2, the image is the integer interval [−k,k], without wraparound. A character of order d≤B has kernel magnitude ≤ρ_B<3, giving exponential decay after normalization. For χ₁ use cos x≥1−x²/2 and Bernoulli; m≥4 ensures the nonnegative base. This is an abstract counterexample, not arithmetic realization without B′/B″. |
| §3.2 “only individual-factor link,” citing CLASS_FORCING | GAP in the unqualified citation inference | The cited Prop 5.1(c) concerns a specified power-residue/Kummer setting for p+4d, explicitly retains ℓ mod n, and discusses specific n. It is not a universal uniqueness theorem for window-uniform character families. See required fix 3. |
| §3.6 any-order discussion | HONEST ASSESSMENT | Magnitude approximation does not control target parity/sign. The memo correctly leaves the arithmetic any-order inverse question open. |
| §4 sharing, exceptionality and repulsion | EVIDENCE ONLY | The computations reproduce, but cover a finite conductor/window/sample range and a finite-factor proxy for exceptionality, not exceptional L-function zeros. Absence of a measured correlation cannot exclude every Deuring–Heilbronn analogue. |

## Independent numerical checks

Added `scripts/z52d_xrev_fourier_check.py`; no imports from the lane library.
It streams the datasets, constructs exact modular box counts and subgroup closures, uses SymPy factorization/symbols,
and checks fresh CRT Fourier spectra on deterministic reservoir samples (400 windows from each scan).
Work is bounded by one window (e≤2000), 400 sampled records and per-prime aggregates.

| Quantity | Recomputed result / agreement |
|---|---|
| Scan sizes / obstructed total | 72,738 + 100,000 windows; 69,547 + 89,177 = **158,724** obstructed. Agrees. |
| Thm B certificates | Independently reconstructed **all 2,110 + 3,184** candidates: forced, target missed, H=G, exact BM value. **57 + 190** have M≥φ(e). Agrees. |
| Rational minima | Hard/control **1/27**; random **1/63**. Agrees. |
| Largest-bound signed certificate | (102001,1907): N=3·7·1237, M=27, image=27, H size=1906, c_BM=−1/3. Nontrivial orders≤952 have negative c. Agrees. |
| Large-image certificates | (5211721,479): M=1215, image **449/478**; (1714441,503): M=1053, image **455/502**. Both miss −1 and have H=G. Agrees. |
| Unsigned certificate | (1005913,587): N=3·5³·11·61, M=189, image=183, H size=586, c_BM=**−1/63**. Orders≤292 give the claimed refutation for η>1/63. Agrees. |
| 31121/43 | Largest masses **0.2002153**, both even/order 7; odd total **0.4666667**; odd maximum **0.09484537**, order 42. Agrees. |
| L(12,.1), forced obstructed H=G | Denominators **5036 / 19437 / 32117**; all-character rates **.612986 / .617431 / .626428**; odd rates **.516283 / .520142 / .516144**. Agrees. |
| Unsigned B=2,.1 / BM alone | **.992454/.980964/.933026** versus **.984114/.961208/.882243**; difference counts **42/384/1631**. Agrees. |
| Non-real-only subgroup kills | **846 / 912**; minimum orders only 4,8,16,32 (32 occurs only in random scan). Agrees. |
| Repulsion, independently recomputed | Hard/control partial **−.181519**, CI [−.335147,−.018489]; random partial **−.038691**, CI [−.136472,.059837]. Raw correlations −.391587 / +.039536. Agrees. |
| Original analysis reruns | Sharing at η=.15 and .3, both excess tables, and Thm C checks reproduce their stored outputs byte-for-byte. |

Every obstructed record passes the stored BM-sign/no-forced-kill checks; sampled spectra independently reproduce all
stored bounded-order maxima, the global maximum, and the Fourier/direct hit identity within rounding tolerance.
Reproduction used `ulimit -v 6000000`, `OPENBLAS_NUM_THREADS=1`, and timeouts on all execution commands:
`timeout 240s uv run --with sympy --with numpy python scripts/z52d_xrev_fourier_check.py /tmp/xrev_FOURIER`.
The full arithmetic scans and exhaustive small-group census were not regenerated; the decisive certificates were.

## Required fixes (priority order)

1. **Keep the verdict within its quantifiers and measurement scope.** Unconditionally the signed arithmetic lemma is
   refuted for B≤952, and the unsigned one for B≤292, η>1/63. Refutation for *every* fixed B (and every η) uses Dickson;
   the abstract theorem does not remove that hypothesis. Replace unqualified “dead/collapse” with this explicit scope.
   For sharing/repulsion, retain “no strong sharing/positive repulsion detected in the tested family and proxy.”
   In particular §6's “No non-BM character ... is shared” is literally too strong: the memo measures 10–16% coverage.
   State “no tested character covers more than about 16% of any surveyed hard/control prime's forced obstructions.”
   The x statistic is a QR-factor-kill rate, not an exceptional-zero measurement; classical OLS uncertainty also ignores
   matching, as already disclosed. Neither result kills all non-BM families, larger conductors, or genuine zero repulsion.
2. **Add H=G to Thm B's inverse-lemma consequence.** At p=61,q=31, N=23, B=2, q is forced and m=15 has all prime
   factors>B, yet the obstructed box is {1,23,27} and H has order 10<30. This window is outside L's domain.
   The character assertion remains true; the certified counterexamples and conditional constructions are unaffected.
3. **Narrow the CLASS_FORCING citation.** Retain the proved quadratic transfer, but label “no other individual-factor
   link/family” as Assessment within the specified reciprocity models, not a general theorem. Thm 5.2 has a valid
   window analogue: choose a large unramified ℓ≡a mod e and apply Chebotarev with p≡−e mod ℓ, p≡1 mod 4.
   State that adaptation rather than applying its p+4d formulation verbatim; it still does not prove uniqueness of families.

## Decision

**ACCEPT-WITH-FIXES.** No decisive numerical discrepancy or false core Fourier formula was found.
The arithmetic constructions are correctly conditional, and the surviving any-order question is honestly disclosed.
Accept the exact formulas, finite counterexamples, and conditional obstructions after fixing the missing domain condition;
record the empirical verdict as strong narrowing, not an unconditional theorem eliminating the whole cluster.
