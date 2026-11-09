# ELL0 internal hostile review

**Overall verdict: REJECT as written; repairable.** The structural arguments for Lemma D, Theorem S′ and the explicit ET bound survive inspection. However, the claimed exact (S) certificate has a reproducible downward-rounding bug, the ET numerical evaluation is not yet a rigorous upper-bound computation, and the memo overstates what its counting assessment rules out. These are not counterexamples to the intended theorems: repairing the (S) endpoint conversion in memory leaves **every claimed prime certified**. ES remains OPEN.

No model/provider/auth/quota error occurred. I did not edit the memo or any repository script or commit anything. Computations were memory-limited and timeout-bounded, with at most two concurrent workers.

## Numbered findings

### 1. MAJOR — the interval upper endpoint is not converted exactly

**Location:** `scripts/z67_ell0_sgap.py:66–67`, `tail_upper`; `Z67_ELL0.md` §3, “upper endpoint converted exactly.”

`mpf(tot.b)` converts the 40-decimal-digit interval endpoint to the ordinary mpmath context, whose precision here is **15 decimal digits / 53 bits**. Extracting `man_exp` afterward exactly converts the *rounded* number, not the interval endpoint. Rounding can go downward.

Concrete counterexample: at `(ell,K)=(37,3)`, the returned rational minus the actual infinite sum of the stated majorant terms is

```
-2.27932348811223106145921730433e-17.
```

I independently evaluated that infinite sum using the closed forms for sums of `q^j`, `j*q^j`, and `j^2*q^j`, at 100-digit precision. Thus the advertised tail upper bound is actually below the tail. This is not merely an unproved rounding convention.

**Fix:** Extract the interval endpoint's integer tuple directly, e.g. `sign, mantissa, exponent, bitcount = tot._mpi_[1]`, and construct the signed dyadic `Fraction` without an intervening finite-precision `mpf` conversion. Alternatively use a demonstrably outward exact endpoint API. Regenerate the certificates.

**Repair check already performed:** I substituted that direct extraction only in an in-memory copy and reran **all 9566 primes in [102,100000)** and **all 22 primes in [11,102)**. Every certificate passes, with identical printed per-prime rows and K distributions. The large-range summary changes only its last displayed binary floating-point digit (`0.4932075919274334` to `0.49320759192743335`). The theorem is readily salvageable, but the checked-in certificate is not exact as claimed.

### 2. MAJOR — Theorem T-expl's numerical upper bounds lack a certified rounding/error argument

**Location:** §4 (I5), §4 Proof; `scripts/z67_ell0_tbound.py:40–61`, `lnC_table`, and the ordinary-mpmath level/tail summation.

The Euler-product formula is correct, but `math.log`/floating-point cutoff calculations plus an asserted safety margin are not themselves a proof that the resulting constants are upper bounds. There is no documented error bound establishing that `1e-6 * #primes + 1e-3` covers every operation, nor an outward-rounded evaluation of the final exponential sum. Ordinary 60-digit `mpmath` is high precision, not interval arithmetic. For example, `log(1-exp(-2950))` rounds to zero in that context, making the computed reciprocal-phi factor slightly too small. The error is utterly negligible relative to the final slack, but its sign illustrates why the existing computation cannot simply be called a rigorous upper bound.

The finite exponent search is mathematically repairable: the ratio of consecutive local factors is

```
[(a+r-1)/a] / p^epsilon,     r = 2 or 3.
```

It decreases with `a`. The maximizing exponent is at most `1/(2^0.05-1) < 29` for tau and `2/(2^0.08-1) < 36` for tau_3. Thus 2000 is ample; state this rather than relying on an unexplained truncation/negative-60 stopping test.

**Fix:** Certify the constants with outward-rounded logarithms and a certified prime cutoff, using the above ratio to bound the maximizing exponents; then interval-evaluate the finite sum and tail, retaining exact rational epsilons (or explicitly their exact binary rational values). A documented, proved global numerical error budget would also suffice. Archive the actual upper endpoint below 0.0422. Until then label this as a high-precision evaluation of an explicit inequality, not a completed computer-assisted proof of the numerical threshold.

**Numerical reproduction:** The requested run agrees byte-for-byte with `tbound_L2950.txt`:

```
sum through 300 = 0.042133388
fixed-epsilon tail = 3.3441698e-6369
minimum displayed beta = 0.1920
log10(ell0) = 1281.2
```

The three quoted logarithmic constants reproduce as `4526.297276053828`, `24.455928880452678`, and `1850.5333733905147`. I found no erroneous analytical multiplier or divisor argument that would threaten the ample final slack.

### 3. MAJOR — the claimed necessity/no-go conclusion does not follow from Prop R or the box experiment

**Location:** title; results paragraph, fourth bullet; §0 K2 outcome; §5 “What a certificate ... would need”; §7 narrowed verdict, proposed FRONTIER text and bottom line.

The valid implication is that upper bounds for the *number of representations* provide sufficient upper bounds for event masses. The converse asserted here is false/unproved:

* Distinct representations can give the same residue modulo `ell^k`, and cylinders from different levels overlap. Prop R does not make representation counts inject into distinct caught residues, or force any certificate to bound the raw counts `R(n)`.
* A uniform power saving `n^(1/2-delta)` is sufficient, **not necessary** for summability along `n=ell^(2k-1)`. For example, `sqrt(n)/(log n)^(1+eta)` also yields a convergent tail for fixed ell. Suitable nonuniform-in-k bounds can work as well.
* A grid experiment over a specified menu of box bounds is not a theorem that “divisor-free counting tops out” at a given exponent, that bounds below sqrt(n) “need divisor maxima,” or that the entire remaining gap is “out of reach of measure counting.” Even within union-bound approaches, deduplication, cylinder unions, additional arithmetic constraints, and different summable majorants are not excluded.
* The one actual impossibility established in §6 is narrower: the unmodified sum of exact level-event masses already exceeds 1/2 for ell=17,23,31. That does rule out that particular global additive certificate there, regardless of its tail.

**Fix:** Everywhere, including the headline and FRONTIER proposal, replace necessity/impossibility language by “the counting bounds tested here do not close the gap.” State that power-saving bounds for the raw (★)-type counts are **one sufficient route**, not a necessary missing input. Preserve the demonstrated obstruction for the particular additive certificate at 17,23,31. Keep the box work explicitly an Assessment of the tested counting methods.

### 4. MAJOR — the explanation of finite-level evidence contradicts compactness

**Location:** §6, “Reading (EVIDENCE, not proof),” last sentence: the uncovered set “may be empty while every finite level leaves survivors.”

For a fixed prime, survivors after levels 1 through K form nested compact subsets of the compact non-residue part of `Z_ell^×`. If **every finite level** has survivors, their intersection is nonempty. Equivalently, a covering by open caught cylinders has a finite subcover. The quoted assertion is false.

The intended caution about finitely many computed levels is correct.

**Fix:** Say: “Survival at the finitely many levels computed here does not prove survival at all levels. If every finite level could be proved to have survivors, compactness/König's lemma would prove an uncovered profile.”

### 5. MINOR — the reported 0.65 is a grid maximum, not the worst continuous box exponent

**Location:** §5, restricted `s >= n^0.2` bullet; `scripts/z67_ell0_boxlp.py`, `worst`.

This is a mesh search with spacing 1/60, not an LP solver or a certified optimization. The result 0.65 is accurate for the sampled grid but is not the worst value of the stated cost function on its full feasible domain. The feasible box

```
(dl, g, a, s) = (17/50, 49/150, 0, 1/3)
```

has cost **0.66** under the script's own rules. Nearby boxes approach 2/3. Consequently “the worst cost is still n^0.65” is incorrect as an unrestricted assertion. The literal equal-third corner also activates the `(C,a')` test; “near the equal-third corner” is better than implying that the exact corner realizes the reported restricted maximum.

**Fix:** State “the 1/60 mesh finds a worst sampled exponent 0.65, near an a'=O(1) box,” or do a certified piecewise optimization with the strict Lenstra thresholds handled correctly. Do not promote this sampled value into a no-go theorem. The reproduced grid outputs otherwise agree with `boxlp.txt`: 2/3, 0.65, and 0.4/0.45/0.5 for epsilon=0/.05/.1.

### 6. MINOR — the memo drops the polynomial ratio factor in the ET tail

**Location:** §4 Proof, “The per-level decay is ≤ e^{-0.02L}”; compare `tbound.py:149–169`.

For the pair-count cases the affine prefactor grows with k. The exponential coefficient gains 0.02 per level in the slowest cases, but the whole term's ratio is not bounded by `exp(-0.02L)` alone. The code correctly includes the extra factor and groups levels in pairs:

```
rho2 = exp(-2*slow*L) * (1 + 4/(2*KMAX+1)).
```

**Fix:** Quote this pairwise ratio, or say “the exponential part gains at least 0.02L per level; the following affine-factor ratio is included.” This does not change the reproduced tail bound.

### 7. MINOR — Prop R's parity aside confuses a unit with a non-residue; clarify unrestricted R(n)

**Location:** §5 Prop R and its parenthetical aside, lines 166–174.

If ell divides C, the caught residue is 1 modulo ell, which **is a unit**. Thus ell not dividing C is not “needed for a unit residue”; it is forced here by the non-residue obstruction. The same distinction matters when describing the unrestricted campaign count R(n), since the displayed representation set initially includes an explicit restriction ell not dividing d'.

The stronger statement is true, and can be justified without circularly assuming that restriction. For any representation

```
n = 4*d'*C*w - C - w = ell^(2k-1),
f = 4*d'*C - 1,
```

we have `f*w=n+C`, `gcd(C,f)=1`, and `f=-1 mod 4C`. UCOVER's Jacobi fact gives `(n/f)=(-C/f)=-1`. Since n is an odd power of ell, reciprocity gives `(-f/ell)=-1`. Thus ell cannot divide `d'*C` (otherwise `-f=1 mod ell`). This proves that both coprimalities are automatic for the unrestricted R(n)-solutions.

**Fix:** Replace “needed for a unit residue” by “forced by the non-residue obstruction,” and add the short argument above if asserting equality with the unrestricted representation count. Keep parameter counts distinct from distinct residue counts, as in finding 3.

### 8. MINOR — small domain/rounding qualifications

**Locations:** §4 (I4); §6 level-3 loss range; results paragraph's large-prime evidence.

* The simplified Type-I argument bound `n^2+4Y^2 <= 2n^2`, with `Y=((15/8)n^3)^(1/5)`, requires `n >= sqrt(60)` (integer n >= 8). It is valid by an enormous margin in the theorem, but the displayed B_I inequality should state its domain rather than appear valid for every positive n.
* The actual level-2-to-3 losses in the ten recorded primes range from **0.0004489755906** (ell=101) to **0.001236226821** (ell=61), not literally 0.0005–0.0012. Use approximately 0.00045–0.00124.
* Qualify “for ell >= 2000” by “among the tested primes below 10^5” in the summary. The data establish the stated 84% survival only over that finite range.

These do not affect the central bounds.

## Verified correct

### Source and algebra audit

I read UCOVER §§1–4 and §6, the ELL0 brief, and the layout-extracted ET PDF at Proposition 1.9, equations (2.1)–(2.21), Remark 2.4, Lemma 2.8 and §3. I inspected all six `z67_ell0_*.py` scripts, the two underlying C enumerators and the relevant stored data.

* **Lemma D is correct.** ET's I-1 family has only positivity/integrality and `f | 4a^2 d+1`; it has no additional coprimality/normalization condition invalidating the dilation. With k2>=3, `(a,d)->(ell*a,d/ell^2)` preserves `a^2*d`, divides the modulus by ell, preserves its prime-to-ell part and the catch condition, and preserves K'=2k1+k2. Iteration reaches k2=1. All six stored dilation checks reproduced exactly, including the 64/242, 104/230 and 142/543 row counts. These are parameter-event counts, not distinct residue counts.
* **Union bound and embeddings:** The F, E/D and A maps in UCOVER §2.2 are injective into the stated positive-integer point sets; residues are functions of the points. Restricting to pure E/D and the dilated A generators preserves the caught union. The counts `R_F <= P_I`, `R_E <= 2P_II`, `R_A <= P_II(ell^(2k-1))` are valid. F/E only at odd k, the reflection factors, and `phi(ell^k)=ell^k(1-1/ell)` give exactly the code's multipliers **2/4/2**.
* **Reflection:** ET's two reflections are integer involutions preserving positivity and swapping a,b. Thus P<=2B holds for all positive-integer points, without Type-I/II solution coprimality assumptions.
* **Size bounds:** Both re-derivations in (I3) are valid for all such points with a<=b. In particular `f<=5n/3` gives `acd<=2n/3`, and the Type-I product is actually at most `(40/27)n^3 <= (15/8)n^3`. The Type-II product is at most n^2.
* **All eight ET cases determine the point.** For Type II: e plus an ordered factorization determines a,b,d and then c,f; (a,d,e) determines b,c,f; (a,c,b) determines f,d,e; (c,d,f) determines a,b,e. For Type I: e plus factorization determines a,b,d,c,f; f plus factorization determines a,c,d,b,e; (c,d,f) determines a,b,e; (a,c,b) determines f,d,e. Integrality tests can only reduce these upper bounds. The D(X) pair count is valid. All divisor-argument majorants match the implementation, subject to the harmless domain qualification in finding 8.
* **Divisor maxima:** Multiplicativity, the cutoffs p<2^(1/epsilon) and p<3^(1/epsilon), and the local formulas are correct. The issue is certification of their numerical evaluation, not the number theory.
* **ET tail/monotonicity algebra:** With the stated fixed epsilons the slowest beta gain is 0.02. The code's paired geometric ratio is valid. The explicit terms have positive beta, and each logarithmic affine factor has derivative at most 1/L; the reciprocal-phi factor also decreases. Fixed-epsilon tail terms likewise decrease for L>=2950. Thus the extension from a certified bound at L=2950 to all larger L is valid. The largest actual summand is A/cd at **k=29**, approximately **0.03930394589**; “k≈28” is an acceptable rough description.
* **Prop R's equation and residue formula are correct**, with the clarification above. The g=-1 example is correct in both families: for ell=3 mod 4, F has a=c=1 and d=(ell+1)/4, while the proposed A parameters satisfy the equation and give residue `-2ell-1=-1 mod ell`.

### (S) certificate logic and data

Apart from finding 1, the certificate is sound: sub-additivity needs no disjointness; residues are deduplicated within a level; non-units are discarded; W1 uses exactly odd k plus the non-residue condition; W2 uses the correct printed 2-adic goodness bit and checks the non-residue obstruction. The C code's t,u,v>=2 restrictions agree with the definition of SDEEPF words. The first uncomputed level is checked to satisfy ell^(K+1)>=10^5. The ratio used for the interval geometric remainder is the exact decreasing upper envelope of consecutive T-terms. The candidate-count assertion is a sanity check, not the proof of the infinite-level majorant.

I reran the requested spot checks, the entire 102–100000 gap, and the corrected-endpoint versions of both full ranges:

* **9566** distinct primes, exactly the primes in the advertised range; **9517 K=1**, **49 K=2**; worst **0.493207591927... at 379**; at 99991, **0.003339** to six decimals.
* **22** small primes; K distribution `{7:1, 6:1, 5:3, 4:2, 3:11, 2:4}`; ell=11 gives **0.389868**, worst ell=37 gives **0.487678**.
* All three independent brute-force comparisons reran successfully: **13/13**, **15/15**, **10/10** at ell=103,379,1009. The script itself reports counts and the set difference rather than asserting equality, but the recorded/rerun outputs do establish equality for those runs.

### ET finite-level evidence

I audited the supplied rows and exact survivor denominators, and spot-reran ell=3–37 through level 2.

* Level 1: only **3,5,7,11,13** are dead in the stored range. At ell=23 survival is **1/11=0.090909...**, at ell=17 **0.125**. The upper-range minimum is **0.4212880143112701 at ell=2237**, with **176 caught of 1118 non-residues**, i.e. more than **84.25%** of non-residue mass survives.
* Level 2: **72 primes**, all surviving; minimum **0.05928853754940711 at 23**.
* Level 3: **10 primes**, all surviving; minimum **0.15448394733974583 at 59**. At 59 the two successive losses are approximately **0.01695** and **0.00098069**.
* The raw event-mass sums through level 2 are **0.5441176471**, **0.5889328063**, **0.5010752688** at ell=17,23,31. The stated obstruction to that particular additive certificate is genuine.
* Finite-level completeness/emptiness statements can properly be labelled CERTIFIED; extrapolation to U at all levels remains EVIDENCE. No ES solution claim is made or warranted.

**Disposition:** Repair the two numerical-proof issues, the compactness sentence, and the overclaiming before using the proposed FRONTIER text. The evidence strongly supports retaining Lemma D and both intended positive results after those fixes; it does not support the claimed general no-go for the remaining ET gap.
