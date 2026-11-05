# Cross-model hostile review — COMPLEMENT

Reviewed `side-agent/z57-complement` at `56f7695500ad4d101f635a0dc9e7336404379661`.
**Verdict: REJECT as written for recording in FRONTIER.** The empirical narrowing is salvageable;
the five-family union assertion and a PROVED covariance formula are false. ES remains OPEN.

## Per-claim audit

| Claim | Classification | Finding |
|---|---|---|
| Lemma W(a), certificate dictionary | CORRECT | Substitution verifies all four rational identities, including boundary B1/I1 words; read CONDITIONAL_ES §1 and BM_CORRECTED_COUNT Prop 4.1(a). |
| Lemma W(b), Jacobi halves | CORRECT | Re-derived by quadratic reciprocity (details below); matches DEDEKIND_ES Thm 4.5. Fresh JAC run: 1045 primes, zero word-level failures. |
| Lemma W(c) | CORRECT | If 4 divides t, neither tu nor tv is 1 mod 4. |
| Lemma W(d),(e) | CORRECT | v(tu−1)=p+u proves the divisor bijection; odd m makes inversion mod 4 legitimate. The stated t=1 exception and fixed-u boundary handling are necessary. |
| Theorem C(i) | CORRECT | BV range, weighted errors, positive cubic-log lower bound and variance upper bound survive re-derivation; details below. |
| Theorem C(ii), displayed covariance identity | WRONG | Missing exclusion of divisors sharing primes with b. U=1, M=4, u=c=1, b=3 satisfies every stated hypothesis and contradicts the formula at order log²x. |
| C(ii), negative quadratic-log order | CORRECT-WITH-FIX | Add rad(b) dividing M, or restrict the second divisor sums by gcd(m′,b)=1 and redo the marginals. The bounded-shift case b=u′≤U is unaffected. |
| Corollary C1, exact class-count identity | WRONG | Misses v=1 at small p in the averaging range; explicit p=17 example below. |
| C1, asymptotic positive coupling | CORRECT-WITH-FIX | Remove the negligible initial-prime boundary contribution, apply corrected C(ii), and require the c-line residue moduli to divide M. |
| Proposition F, four prime-pair falsifiers | CORRECT | Fresh full prime census agrees; independent direct enumeration verifies 193, 577, 2521, 102001. Reversing either implication is also refuted. |
| F, nonsquare pair falsifiers and square census | CORRECT, finite scope | Independent parsing reproduces all pair counts and the 999 square zeros. Composite counts were checked from the archive, not fully regenerated. |
| §4.6 five-family union zero at 105 | WRONG | c2(105)=1. The script tests only STAR=B1=I1=0. The archived census has NO nonsquare five-family union zero. |
| §4.6 prime zero marginals / joint counts | CORRECT | All reproduced by fresh enumeration through 4,000,000, not merely by rereading the summary. |
| §4.6 positive dependence “beyond local data” | GAP if so interpreted | Decade-only independence does not control residues; G–K expected joint zeros change from 2.78 to 10.40 with mod-840 controls. |
| §4.3 correlations / low tails | CORRECT for independently rerun 10⁹ window | All 21 certificate-pair correlations and ratios reproduce. Higher windows and L-proxies were not independently rerun. |
| §5 Jacobi/ES₅ equivalence | CORRECT with stated p≡1 (8) restriction | Checked DEDEKIND_ES Cor 4.6: interior length 3 plus boundary length 2. This is STAR∪B1∪I1, not the five-family union including c2,c3. |
| “Only complementary partner”, “unions help only by adding main terms”, §8 dead-end prohibition | GAP / overclaim | The exact QR partition is valid; exclusivity as a route to a union theorem is not established by that partition, covariance, or finite data. |

## Decisive reruns

Freshly compiled the reviewed C engine and ran `range 5 4000000 3`: **141502 primes**.
All commands used timeout and ulimit; engine limits were 480 s wall / 450 s CPU / 6000000 KiB virtual memory.
The independent reproducer is `scripts/z57_xrev_complement_check.py`; its run used 200 s wall / 180 s CPU,
6000000 KiB virtual memory, single-thread BLAS, and `uv run --no-project --python .venv/bin/python`.
Archive and fresh outputs are in `/tmp/xrev_COMPLEMENT/`; the script accepts that directory and `--stats`.
The largest OLS design is only 48139×365 (140565880 bytes); census processing is streaming.

* Fresh prime zeros, STAR/B1/I1/c2/c3/G/K: **12/3/0/493/3088/31/3778**.
* Fresh c2&c3 joint zeros: **53**, decade prediction **33.078431**; G&K: **12**, prediction **2.781516**.
* With decade **and mod 840** strata: predictions **35.653352 / 10.399213**, respectively.
  Conditional fixed-margin hypergeometric SDs are **4.651466 / 2.000774** (descriptive z=3.729 / 0.800).
  Thus c2–c3 retains positive-zero evidence; the highlighted G–K excess does not persist under this stratification.
  Early strata are sparse; this comparison is not a proof of a local causal mechanism.
* Independent pair enumeration (no divisor engine imports) gives at 105: STAR/B1/I1/c2/c3 = **0/0/0/1/0**.
  Word (t,u,v)=(24,3,3) in W(210) gives **4/105 = 1/27 + 1/1890 + 1/1890**.
* Parsing the archived sparse census with independently sieved population denominators gives **one three-family**
  nonsquare zero (105), **zero five-family** nonsquare zeros, and all reported pair counts unchanged.
* Strictly ≤4,000,000 contains **857498**, not 857499, nonsquare composites; the original summary extends to 4000001.
  Its million-input count is therefore also off by one for the stated range. Zero counts are unaffected.
* At 10⁹, N=48139: residual r / 5%-tail ratio are STAR–B1 **0.494537 / 3.736282**,
  B1–I1 **0.624427 / 4.652311**, c2–c3 **0.066761 / 1.193717**, G–K **0.077355 / 1.404608**.
  All 21 rerun correlations are positive. This confirms the reported descriptive evidence, not a union obstruction.

## Proof details and required repairs, in priority order

1. **Correct the union and the verdict built around it.** `_census.py` names `Z[STAR]&Z[B1]&Z[I1]`
   a “five-slice union”; include c2 and c3 explicitly. Correct §§0,4.6 and any propagated union assertion.
   Pairwise nonsquare counterexamples do NOT imply a counterexample to their entire union.
   A positive covariance also cannot forbid pointwise coverage: equiprobable (A,B)=(1,0),(0,1),(10,10)
   has Cov(A,B)=179/9>0 while A+B≥1 always. Keep the four certified prime-pair exclusions;
   replace the bottom-line universal language with “no robustly negative full-pair count association observed”.
   The memo's explicit caveat preserving five prime-pair implications is honest but contradicts its broad bottom line.

2. **Repair Theorem C(ii) before retaining PROVED.** With U=1,M=4,u=c=1,b=3,q=q′=1, C=C′={0},
   c(cu−b)=−2 has no prime outside M. Nevertheless m′=3 requires p≡0 (3), impossible for primes p≡1 (4).
   The proof's assertion that −bc⁻¹ is a unit modulo every admissible m′ is false: inadmissible events cannot
   be promoted to unit classes. Correct BV expansion omits all m′ divisible by 3; the printed formula does not.
   The discrepancy includes all m,m′ divisible by 3 and is Ω(log²y), not O_A(log⁻ᴬx).
   Sufficient repair: require every prime dividing **bc(cu−b)** to divide M. Alternatively retain the original
   population but explicitly remove gcd(m′,b)>1 from the main terms (small exceptional primes are negligible).
   Prove Var(D′)≍log³x as well when asserting corr≍−1/log x; the same gcd expansion supplies it after repair.

3. **Repair C1's exact identity.** Take U=2,M=8,a=1,u=2,p=17,x=10⁸,θ=1/5.
   The QR residue classes are {1,3} mod 8 and eligible divisors of p+u=19 are {1,19}.
   Both words are boundary: (1,2,19) and (10,2,1). Actual QR=0, whereas D−δ=2−1=1.
   Restrict the identity to p>Uy (sufficient), then bound the discarded initial segment in the average;
   its contribution is o(1) using the divisor bound. The asymptotic corollary is repairable, not the exact equality.

4. **Separate statistical evidence from necessity claims.** Decade-only zero comparisons are not evidence
   beyond all local data. Report the local-stratified comparison above; do not treat 12 versus 2.8 as such evidence.
   “Within noise” uses nominal r√N, not a calibrated test for heavy-tailed counts and fitted residuals;
   especially at N=550, the hundreds of residue controls require a degrees-of-freedom/robust uncertainty treatment.
   No rerun here validates the untested three CRT attributions, the L-proxy causal gloss, or a universal negative verdict.
   Assessment labels on untested band mechanisms are appropriate; the mandatory “exact non-congruence relation”
   and “do not retry” recommendations are not logical consequences. Keep a scoped EVIDENCE conclusion instead.

For completeness, C(i) re-derivation: M y²=M x^{2θ} lies strictly inside BV's range; lcm multiplicity ≤τ(l)²
is absorbable by Cauchy–Schwarz and the τ⁴/φ logarithmic moment. Thus the first/second moments are S₁,S₂+o(1).
Writing m=gr,m′=gs, (r,s)=1, gives S₂≪log³y. In fixed unit classes Möbius inversion gives
Σ1/(rs)=α²∏_{ℓ∤M}(1−ℓ⁻²)log²z+O(log z+1); summing g⁻¹ with z=y/g gives a positive cubic-log term.
Subtracting S₁S₁′=O(log²y) proves the covariance lower bound; applying the upper bound diagonally controls variance.
The supplied proof is sound here, including disjoint class sets; no pointwise lower bound follows.

For W(b), put A=tu−1, B=tv−1; AB=tp+1 makes their symbols equal, allowing u,v to be swapped.
Quadratic reciprocity gives: if t is even, symbol −1 iff t≡0 (4) or the even side-letter is 0 (4);
if t is odd with one even side-letter, symbol −1 iff that letter is 0 (4) or t≡3 (4).
If all letters are odd, p≡1 (4) forces t≡3 (4), and the symbol is +1 exactly when u≡v≡1 (4).
These are precisely STAR/B1/I1 versus QR. This independently checks the cited cell law without relying on
DEDEKIND_ES's remembered Rademacher citation. None of these identities certifies positivity at every prime.
