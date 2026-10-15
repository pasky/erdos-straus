# Independent audit of R247: FF_THIRDS_CORNER

Scope: the R247 review, scripts, evidence and reviewer-applied repairs through a5c4ccb1, compared with side-agent/ff-thirds-corner. The revision range also brings in extensive unrelated merged work; this report does not certify that unrelated history.

**Verdict:** the three requested focal claims survive: Lemma 3.3 is correct, MAJOR-1 identifies a genuine two-dimensional critical region, and the independent search's mathematical enumeration is complete in full mode for each parameter it visits. No fatal defect found in those arguments or in the reported linear-point exclusions. The review nevertheless overlooks two substantive qualifications and contains an overstatement of its own.

## Findings

### 1. Calibration is complete for unstructured hits, not all structured hits

Locations: `scripts/review_r247_calib.py:19`, `reviews/ff-thirds-corner-review.md:176–180`, `FF_THIRDS_CORNER.md:148–160,239–241`.

The calibration driver calls **lop**, which intentionally may omit exact tuples `w₁ = −uC₁`. Its 42 structured hits at levels 5..12 are therefore found hits, not a complete structured census. The review explicitly exempts exact tuples in its comparison scripts but fails to carry that qualification into its endorsement of the calibration and the main document's “complete search” wording.

This is not merely hypothetical. Comparing the committed independent census with a freshly compiled R247 lop search at k=2, all relevant polynomial points and levels 3..8 gives 98 census coverings versus 76 lop coverings: 22 omitted exact coverings, **16 at levels 5..8**. These 16 are additional to the calibration log's 42 found structured hits at levels 5..12; the actual total for that interval is consequently **at least 58**.

A concrete omitted example is

- q=3, k=2, s=13, N=7, u=1+T−T²;
- C₁=g'=1, w₁=−u, v₁=T−1;
- m'=−(T¹¹+T−1)/u, a monic polynomial of degree 9.

The division is exact (also present in the independent census: low-to-high coefficient string `1101220211` for m'). Here E=T¹²−u, so the tuple covers and is structured. Orientation A has deg(m'w₁)=11>5; orientation B has deg(m'C₁)=9>3. Neither lop bound reaches it.

**Repair:** say the search is complete for non-exact tuples, hence for unstructured hits, and label 42 as the number of structured hits found; alternatively include the exact classification in the calibration enumeration. The 2 unstructured hits, their leading-coefficient split, and the linear-point absence evidence are unaffected. Missing exact tuples all have lc(u)=−1, so this does not refute the reported sign pattern.

### 2. Prop. 1.4's “every level it lives on” remains false after repair

Locations: `FF_THIRDS_CORNER.md:65`, endorsed at `reviews/ff-thirds-corner-review.md:61–70`.

The repaired hypotheses include T∤g₂, and the proposition itself gives E+u=g₂T^{s−1}. Thus v_T(E+u)=s−1 exactly. Among its admissible family levels, the tuple covers precisely those with **N≤s−2**, not the top level N=s−1.

For example, q=3, k=2, u=1+T−T², s=5, m'=T+1, g'=C₁=1, w₁=T²−T−1, v₁=T−1 satisfy both tuple identities. They give E=T⁴−u. The tuple covers at N=3 but not N=4, although both are admissible family levels (at N=4, j=3 and γ=0).

**Repair:** replace the sentence by “covers at each admissible level N≤s−2.” This is an inherited defect that R247's SOUND-AFTER-REPAIRS verdict missed, not a failure of the new converse side conditions. It does not affect the minimum-level search at x*_c.

### 3. MAJOR-1's conclusion should say “part,” not “entire boundary”

Location: `reviews/ff-thirds-corner-review.md:156–163`.

The phrase “critical along the entire boundary of the Liouville region” is false. For example, (a,z,y,t)=(0.1,0.4,0.3,0.2) satisfies the restrictions and lies on b=1/2, but the implemented route minimum is 0.4 (R3c), hence the excess is −0.1. The repaired main document correctly says a two-dimensional region of that face; retain that qualification in the review too.

Likewise, “these are non-degenerate patterns with w,m',g' all of linear degree” applies to an interior portion of the b=1/2 zero region, not every listed point: the off-face segments explicitly have a=0 or z=0. Neither correction weakens MAJOR-1.

## Focal proof audit

### Lemma 3.3: sound, including s=5

Write n=s−2≥3, r=−c. Lemma 1.2 excludes the exact alternative. Since a,b≥1, z≥0 and a+b+z=s, max(a−1,b)≥s−2 leaves exactly:

1. b=s−1, a=1, z=0;
2. b=s−2, (a,z)=(1,1) or (2,0);
3. a=s−1, b=1, z=0.

There is no missing balanced or small-degree case. In cases 1 and 2, the tuple identity gives deg(v₁)=max(a,b)−2−y, hence ≤n−1 and ≤n−2 respectively. The covering congruence modulo T^n therefore determines v₁ uniquely as the truncation of −m'w₁²/u. This step uses only the congruence version of Lemma 3.1, not its stronger covering-level hypotheses elsewhere.

In case 1, v₁=−sum_{j=0}^{n−1}r^jT^j, so uv₁=−1+r^nT^n and deg(v₁)=n−1>0. The second tuple equation implies v₁ divides T^n+1. If r^n=1, this would force v₁|2. If r^n=−1, it gives g'=−c; monicity requires c=−1, which instead gives r=1 and r^n=1. Both alternatives are impossible.

In case 2, put the nonconstant small factor equal to T+d, d∈{±1}. The coefficient of T^{n−1} in the forced truncation must vanish. For m'=T+d, w₁=1 this coefficient is −r^{n−2}(dr+1), so d=c. For m'=1, w₁=T+d it is −r^{n−3}(r²+2dr+1), again forcing d=c. These formulas are valid at n=3, the s=5 endpoint. The first subcase gives v₁=−c and the first impossible exact configuration from Cor. 3.2's proof; the second gives v₁=−u and a common nonconstant factor with w₁.

In case 3, monicity and w₁+u≡0 mod T^n force w₁=T^n−u, v₁=−u. This is the second impossible exact configuration from Cor. 3.2's proof. Those algebraic exclusions apply at s≥5; referring to the proof, rather than the N≥4 statement of that corollary, is legitimate.

The exclusion s=4 is necessary. The census has the two tuples m'=g'=1, {w₁,C₁}={T+1,T−1}, v₁=−1, attaining depth s−2=2. In case 2 the coefficient calculation changes at n=2, so the proof correctly does not extend there.

Editorial improvement only: explicitly write b=s−1 in case (i), and spell out that c=−1 makes (−c)^n=1. The current compressed proof is correct but unnecessarily difficult to check.

### MAJOR-1: supported, with an analytic two-dimensional witness

A bounded rerun of `review_r247_rate_face.py` reproduces **314/961** zero points on b=1/2 and **12** off that face. The script calls the original route table, so this is an independent exploration of the optimiser's geometry, not an independent verification of the underlying route inequalities.

A grid by itself would not prove dimension. Here that gap is easily closed: at

    (a,z,y,t)=(1/10,2/5,9/20,1/20)

the only binding route is R4c=a+z=1/2; every other active route is ≥0.55. The inactive R5/R6/R10 activation tests have strict margins. On a sufficiently small open neighbourhood within b=1/2, all these margins persist while R4c remains exactly 1/2. This proves a genuine relatively open, two-dimensional zero patch, with a,z,y,t all positive.

One can also prove the restricted upper bound ≤1/2 directly for the implemented routes. If t≥1/2, use T0=1−t. Otherwise the restriction gives z+2a≥1/2, whence ρ=a+z≥1/4. For ρ>1/4 the Coppersmith test activates R4c because dE(1−dE)≤1/4. At equality, a=1/4,z=0 and t<1/2 imply dE=a+y>1/2, so the activation remains strict. Thus R4c=1−b≤1/2. Together with the open patch, the q=3 supremum is exactly 1/2, not merely a sampled zero.

### Independent search: complete mathematical enumeration

For every actual tuple, deg(v₁)=max(a,b)−2−deg(g')≤max(a,b)−2. The equality uses monicity and odd characteristic: even when a=b, the leading coefficient of w₁+C₁ is 2, not zero.

For a fixed pair (m',X₁), M=m'X₁ is T-free. The two necessary congruences used in the code are valid modulo M and T^{n₀}, with n₀=min(N+1,s−2). The explicit CRT representative

    v₀ = B + M*((A−B)M^{-1} mod T^{n₀})

has degree <deg(M)+n₀. Every solution is uniquely v₀+K·T^{n₀}M. Therefore rejecting v₀ when its degree exceeds vmax cannot lose a solution: the higher-degree multiple cannot cancel its leading term. The loop enumerates every possible K of degree ≤vmax−deg(M)−n₀, with arbitrary coefficients, including zero; it does not accidentally assume v₁ monic.

Full mode enumerates every monic T-free pair (m',w₁) with deg(m'w₁)≤s−2, reconstructs C₁ and g', and checks the original identities and covering condition. Every tuple of that s reaches such a pair. Lop mode instead needs Lemma 1.2 and is complete only modulo its explicitly permitted exact exception. At x*_c the exception is impossible, so the reported absence runs are not compromised by finding 1.

“Every tuple” here means every covering tuple of the two parameters assigned their *minimum* level N. The program does not list again the same tuple at all larger family levels; that is sufficient for the claimed exclusion through a level cutoff.

Implementation hardening remains advisable: no validation of mode strings (anything except `full` silently selects lop), no polynomial-input length check against MX=96, no capacity check on found[4096], and unchecked integer powers in candidate counts. These do not invalidate the documented small-degree/low-level runs, but the binary should not advertise unrestricted full-search reliability without domain/capacity guards. The compressed C also produces `-Wmisleading-indentation` warnings.

## Checks performed

All computational checks were sequential, with a 1 GiB process-memory limit, numerical-library thread counts set to one, and short timeouts. No existing search process or output file was touched.

- Recompiled the searcher and brute-force census under distinct `/tmp/review0029_*` names.
- Fresh brute-force census s=4..10: 60 tuples, identical to the corresponding archived records.
- Full search versus that census: all 54 points of degrees 1..4 with u(0)=1,u'(0)≠0, k=2, N=3..5; 64 coverings, exact set equality.
- Lop versus committed census, k=2, N=3..8: quantified the 22 omitted exact coverings, including 16 at N=5..8.
- Structured-depth checker on all 312 archived s≤16 tuples: no s≥5 exception; only the two s=4 boundary tuples.
- Face-grid rerun and direct route evaluation at the positive-dimensional witness and the counterexample to “entire boundary.”

No long exclusion search, N=20 replay, h=3/4 cyclotomic enumeration, or unrelated merged theorem audit was performed. The main document's pre-existing “80 points with u'(0)≠0” at line 99 should also read 54 (80 counts all derivative choices); R247's own comparison correctly uses 54.
