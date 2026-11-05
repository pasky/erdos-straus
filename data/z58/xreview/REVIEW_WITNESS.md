# z58 cross-model hostile review — WITNESS

Reviewed `side-agent/z58-witness` at `207f959b5cc53c921dcc930a91217f26d034b089`.
**Verdict: ACCEPT-WITH-FIXES (minor wording/reproducibility fixes; no substantive theorem defect found).**
The verdict **narrowed; W is a target, not a HOT LEAD** follows. ES remains OPEN.

## Per-claim audit

| Claim | Classification | Finding |
|---|---|---|
| §1 equivalence of the four orderings | CORRECT | Algebraic bijections; independent complete enumeration agrees at all 1,125 primes p ≡ 1 (4) ≤ 20,000. |
| Lemma 1.1, including q_min ≥ 8n_p | CORRECT | Prime hypothesis and p ≡ 1 (8) suffice; proof below. No coordinate-only lower bound follows. |
| Modulus rule ⇒ least-non-residue bound | CORRECT | On the rule's stated prime domain, not automatically a theorem for all prime congruence classes. |
| Fixed-congruence selector impossibility, §0 F1 | CORRECT | Dirichlet in class 1 modulo lcm(M,840,d) defeats the output assigned to 1 modulo M. |
| Full four-ordering census ≤ 10⁹ | CORRECT | Entire source scan rerun: 25,423,491 primes, exactly 14 zeros, no capped/missing minima at positive cases. All five advertised record maxima agree. |
| W certified through 10¹⁰ | CORRECT, computational | Independent full prime counts, all 21 saved large-s rows, and 46,232 extension-slice primes agree. Full extension witness scan was not independently repeated. |
| Fixed-D law and proper limiting distribution | CORRECT | PNT-AP plus CRT tightness; does not prove mean convergence or a growing-D asymptotic. |
| d-survival fit / non-Poisson reading | CORRECT as EVIDENCE | Independent full rescan of both stated ranges and independent density sums agree. Clustering is an interpretation, not an association theorem. |
| Semi-local fit | CORRECT as EVIDENCE | Recounted retained u/s tails reproduce coefficients; tiny counts and non-uniformity preclude an asymptotic law. |
| Proposition 3.1 | CORRECT, CONDITIONAL | Admissible distinct linear forms; fixed S only. All nine numerical instances independently verified. |
| Farey / minus-continuant identities | CORRECT | Determinant = 1 iff p = 4uBC−u−B; matrix product has this (1,1) entry. No witness-selection mechanism follows. |
| “No deterministic witness rule was found” | CORRECT-WITH-FIX | Must mean no useful structural selector with a proved eventual guarantee, not no deterministic algorithm; the least-witness searches themselves are deterministic. |
| W_size versus W; survival of W | CORRECT | Positivity-conditional size statement is not existence. Neither fixed-S Dickson nor the direct modulus inequality refutes W. |

## Proof re-derivations

**Lemma 1.1.** At a solution, d = 4uC−1 divides p+u and gcd(d,u)=1.
Write u=2ᵃv, v odd. If a>0 then d≡7 (8), so (2/d)=1. Reciprocity and d≡−1 (v), d≡3 (4)
give (v/d)=(−1/v)(−1)^((v−1)/2)=1. Thus (p/d)=(−u/d)=−1.
Some prime ℓ|d has (p/ℓ)=−1; p≡1 (4) gives (ℓ/p)=−1. Interchange u,B for the other d.
For the pair modulus, u+B is odd and gcd(u,B)=1: a common factor divides p, whereas
u,B≤(p+1)/3<p. Put χ=(−4uB/·). Since −4uB≡(u−B)² modulo u+B and this square is a unit,
χ(u+B)=1, χ(−1)=−1, and p≡−(u+B) modulo 4uB yields χ(p)=−1.
Therefore (uB/p)=−1. For p≡1 (8), 2 is a residue, so an odd non-residue prime divides uB;
uB is even, hence uB≥2n_p and q_min≥8n_p. Also d≥n_p gives uC,BC≥(n_p+1)/4.
This independently verifies the decisive elementary identity in `BM_CORRECTED_COUNT.md` Thm 1.1(2)
and `Z57_SYNTH.md` Lemma A.1(b); no unverified Brauer-theoretic theorem is needed here.

**Other PROVED statements.** From d and r=(−p mod d), recover u=r, C=(d+1)/(4r), B=(p+r)/d.
The C-form follows from (4Cu−1)(4CB−1)=4Cp+1; the pair form follows directly from the equation.
If a modulus shares a prime factor with n, n≡−u (d) contradicts gcd(d,u)=1: F3's dead-modulus assertion is correct.
For fixed D, avoidance is periodic modulo lcm(840,{d≤D:d≡3 (4)}). PNT-AP gives its relative unit-class density.
For each prime ℓ≡3 (4), ℓ∤840, the hit −1 modulo ℓ removes proportion 1/(ℓ−1), independently by CRT.
The reciprocal-prime sum diverges in this progression, so the displayed product tends to zero: tightness holds.
No interchange involving growing D or unbounded log d is justified or needed.

**Prop. 3.1.** For u≤S, q_u is prime, greater than u+1, and 1 modulo 4u;
all divisors of (u+1)q_u are congruent to divisors g of u+1, where g≤u+1<4u−1.
For C≤S, r_C is prime, greater than 4C+1, and 1 modulo 4C.
The only candidate g≤4C+1 congruent to −1 modulo 4C is 4C−1, which cannot divide 4C+1.
These exclude u,B,C≤S. The coefficients of p,q_u,r_C are positive and distinct:
L, L/(u+1)≤L/2, and 4CL/(4C+1)≥4L/5, respectively. Every form equals 1 at k=0,
so their product has no fixed prime divisor. Dickson applies for each fixed S, with infinitely many positive k.
This neither supplies positive R nor a variable-S conclusion. The memo explicitly acknowledges both limitations.

## Computational audit

Independent scripts: `scripts/z58_xrev_witness_check.py`, `scripts/z58_xrev_witness_count.cpp`.
All execution commands used `ulimit -v 4000000`, timeout ≤1800, and at most two compute processes.
The Python checker uses SymPy prime generation/divisor enumeration, not the lane's Pollard–Brent engine.
Complete solution sets are obtained by enumerating u- and C-levels through ⌊(n/2)^(1/3)⌋:
4uBC−u−B≥2uBC, so every solution has some coordinate within that bound; u↔B handles the third coordinate.

* Full original four-ordering rescan: d_max=2,953,943@85,664,329; u_max=469@53,325,721;
  C_max=76,141@564,661,441; q_max=37,223,480@743,804,881; m3_max=193,763@413,490,001.
  s_max=201@413,490,001; max s/log²p=0.510630. All positive cases have all four minima, not sentinel −1.
* Independent complete record solutions: 413,490,001 has exactly (241,2134,201),(458,1101,205).
  At 1,708,503,889: seven unordered solutions, u_min=97,C_min=118,s=97. Other displayed record primes also agree.
* Independent extension slices: [1,000,000,001,1,001,000,000] has 24,076 primes (max s=8);
  [9,999,000,001,10,000,000,000] has 21,691 (max s=11);
  [1,708,493,889,1,708,513,889] has 465 (max s=97). Every u/C minimum agrees, with no failed bounded search.
* Separate progression sieve counts 25,423,491 primes ≤10⁹ and 202,099,784 in (10⁹,10¹⁰].
  Every extension chunk count agrees with the saved DONE counts (saved order is lexicographic, not numerical).
  All 21 saved s≥30 rows independently checked: 18 in 𝔐, maximum 97. This supports, not independently duplicates,
  the full extension certification. Audited code searches both coordinates monotonically and counts only successful cases.
* Independent d rescan: in (3·10⁶,3·10⁷], 51,111 𝔐-primes, 833 survive D=1000 (1.62979%).
  In (10⁸,10⁹], 1,408,113 𝔐-primes; survivor counts at D=1000,3162,10000,100000 are 23985,4934,809,14.
  Corresponding −log S/log²D: 0.0853484,0.0870536,0.0879633,0.0869025. Independent E(1000,10000,100000)
  =4.8628030,9.7250855,16.2008432, confirming −log S/E≈0.84,0.77,0.71.
* Semi-local recount: u>32 counts by decade are 28,46,193; s>32 counts are 1,2,11;
  u coefficients at U=32–128 span 0.1237–0.1349. These tails are wholly retained by the hard-file criterion.
  The raw six full scan files are not archived; exploratory CF/KS/control-dispersion statistics were not independently rerun.

## Falsifiers

| Screen | Independent result / interpretation |
|---|---|
| F1 odd squares | Jacobi proof holds for every square; complete enumeration also empty for odd squares through 51². Both u- and C-form obstructions are sound. |
| F2 C-even | Complete enumeration of all 12 listed primes reproduces every R count and zero even-C solutions. Least-coordinate histogram is eleven s=1, one s=5. Odd C is essential. |
| F3 composites | Complete enumeration confirms all 285 zeros; least-factor counts 214 at 3, 36 at 5, 15 at 7; a zero with least factor 443 exists. Coprimality alone is manifestly insufficient. |
| F4 zeros | All 14 star zeros and all 38 gstar screen primes independently enumerated: exactly 24 positive; s(564661441)=9. W excludes the 14 by its explicit threshold, not by an existence proof. |

## Required fixes, priority order

1. **Minor scope:** replace “no deterministic witness rule” by “no structural/non-exhaustive witness selector with a proved eventual guarantee.” Keep the actual impossibility claims restricted to fixed congruence selectors and, conditionally, fixed-coordinate menus. Finite large records and failed invariant tests do not rule out arbitrary deterministic rules.
2. **Minor reproducibility:** make `z58_witness_runbig.sh` propagate scan timeout/failure (its current pipeline reports awk's status), assert each expected chunk count and zero NOS rows, and archive labelled chunk bounds/counts. The independently matched totals rescue the recorded run; the runner alone is not fail-closed certification infrastructure.
3. **Nit:** in the F4 prose use “cutoff ≥8,813,281” when the domain is p>cutoff, not “threshold >8,813,281.” The formal W statement already has the correct cutoff.

These fixes do not change any verified number or theorem. W's empirical success is substantial finite evidence, not a uniform tail estimate or a new route around the divisor-in-class difficulty.
