# SIGN cross-model hostile review

**Verdict: ACCEPT. ES and (S) remain OPEN.** The repaired memo supports **NARROWED**, not a general no-go for a sign-retaining ladder.
Reviewed `side-agent/z68-sign` at `e2f66fdfa92d3af2f39f24500827fd0c7e69ab1e`; independent derivations and reviewer-written checks, not reliance on the internal review's verdict.
No provider/auth/quota errors occurred. Every command had timeout ≤ 1800 s and virtual-memory limit 6000000 KiB; compute was sequential, numerical-library threads limited to one.

## Per-claim decisions

| Claim | Classification | Finding |
|---|---|---|
| Lemma 1, cut identity and sign | CORRECT | Matrix multiplication gives the exact identity, including endpoints. Cancelling the Jacobi factor requires a unit; omitting it really fails at 21. |
| Lemma 2, rescaling | CORRECT | Reducedness, empty-tail convention and size inequalities suffice. Sign correction is χ(k), not automatic sign preservation. |
| Theorem 3 | CORRECT | Numerator identity and length exactly three hold; full stated coprimality suffices and is automatic at primes. The 137 sign flip is genuine. |
| Proposition 4 | CORRECT | Bijection is between **marked cuts** and **factorisations attached to oriented triples**, not unmarked words or L₃ alone. Trivial length-three refinements are essential to the asserted full support. |
| Proposition 5 | CORRECT | The continuant lower bound gives r ≤ M′/2+2. The repaired regular-CF terminal conventions and M+2 digit bound are valid. This blocks only direct contraction. |
| Families/profiles | CORRECT | The applicability congruence, reciprocity sign, and level-one condition follow under the stated unit and n≡1 (8) hypotheses. |
| Theorem 6 | CORRECT, relative to UCOVER S(a) | The cited theorem has the required quantifiers. All 22 branch intersections check; the enlarged prime-to-ℓ modulus legitimately clears thresholds. This excludes finite output-family menus, not general algorithms. |
| Proposition 7 | CORRECT as CERTIFIED | All 2,189 length-five witnesses independently pass, with full coverage at every prime 11≤ℓ≤211. Length-four failures remain bounded-search statements. |
| Proposition 8 | CORRECT | A positive-weight change of indexing at primes; false as an identity at general composites. It is **not** an impossibility theorem for weighted analytic estimates. |
| KT3 | CORRECT as EVIDENCE | ρ=0.64576998 over 4,171 primes reproduced. Corrected interior-only NOOUT still has positive association; all-cut NOOUT has weak negative association. Withdrawal of the causal interpretation is necessary and adequate. |
| Gate / “not excluded” / labels | CORRECT, scoped | No usable universal bridge was obtained. NARROWED is justified; “all bridges fail” or “ladder dead” would not be. Post-hoc choices and finite-range qualifications are disclosed. |
| F1–F4 | CORRECT | Actual screen data and cited witnesses agree; no false “survives all screens ⇒ positivity” inference remains. Details below. |

## Independent derivations and hostile cases

1. Write the prefix matrix as P=[[X,−X′],[Z,−Z′]]. Its determinant gives X′Z−XZ′=1.
   Multiplication by the suffix first column (bY−Y′,Y) gives n=X(bY−Y′)−X′Y and A=Z(bY−Y′)−Z′Y.
   Subtraction yields XA−Zn=Y exactly. Since A is a unit, χ(X)χ(A)=χ(Y); cancellation requires gcd(X,n)=1.
   Reversal symmetry identifies X/X′ with the reversed prefix; uniqueness of the ceiling Euclidean algorithm proves the converse.
2. Rescaling (X,b,Y′) to (kX,b/k,Y′/k) leaves all three terms of n unchanged.
   gcd(k,X′)=1 preserves reducedness; the other fraction remains reduced. Lemma 1 gives kXA′≡XA; unit cancellation proves the sign rule.
   Reflecting the word gives the left move, including its endpoint case. Intermediate words need not retain sign or decrease length.
3. With t=b/(X′Y′), u=X′Y, v=XY′, direct substitution gives tuv−u−v=n and t,u,v≥2.
   n=v(tu−1)−u gives χ(A₃)=χ(u)χ(v)=χ(A)χ(X′Y′) under the stated unit hypotheses.
   At primes all proper continuants lie strictly between 0 and p. At 137, 95 is negative but the output 11 is positive, with correction χ(3)=−1.
4. Each admissible factorisation reconstructs precisely one prefix and suffix by HJ uniqueness, hence one marked cut; reversing the construction recovers all its data.
   Distinct cuts may belong to the same word, and the same output has many refinements: neither invalidates the marked bijection.
   The trivial choice (X,X′,Y,Y′)=(v,1,u,1) proves full output support, **not reachability from a prescribed long witness**.
5. K of L letters ≥2 is at least L+1, so X′≥j and Y′≥r−j−1.
   Therefore M′≥2j(r−j−1)≥2(r−2). Regular-to-HJ conversion bounds each HJ letter by M+2; K≤(M+2)^r gives the advertised large-n exclusion.
6. At level one, ℓ∥XY and s=X′Y+XY′≡−1 (mod XY/ℓ) put the family on the required profile; reciprocity reduces its sign to (g/ℓ).
   UCOVER S(a) supplies a surviving ℓ-adic lift of the selected g, not a claim that every lift survives.
   If a selector existed, its finite menu would cover the witness family's CRT subclass after threshold enlargement, contradicting S(a).
   Reading UCOVER §6 and replaying its rigorous survivor calculation confirms that this is the cited theorem, not an extrapolation from finite-depth survivors.
7. Proposition 8 follows by summing the bijection with the sign rule. Positivity equivalence uses **strictly positive weights on every contractible pair**, including trivial refinements.
   An arbitrary restricted bounded-digit input ensemble is not covered by that equivalence. Re-indexing alone says nothing against useful weights or a different transfer operator; the memo now acknowledges this.

Explicit unit failures, independently found (cut indices below are zero-based):
- n=21, w=(6,2,2,2), cut 1: A=4, X=6, Y=3; χ(A)=1 but χ(XY)=0.
- n=333, w=(3,2,18,2,2,2), cut 2: A=134, output (t,u,v)=(2,12,15), A₃=23, X′Y′=9. Both actual signs are −1; the unqualified product is 0.
- n=2025, w=(3,4,27,3,2,2), cut 2: A=737, output (3,21,33), A₃=62, X′Y′=9. Actual denominator signs are +1, while χ(9)=0.
- At n=333 the unrestricted composite version of Proposition 8 with μ=1 gives **32 versus 34**, independently reproduced.

## Recomputations / screens

- Reviewer script `scripts/z68_xrev_sign_check.py`: all reduced fractions for every odd 3≤n≤201, plus 333 and 2025; **120,925 cuts, 4,782 right-rescaling moves, 1,143 contractions**, zero failures under the stated hypotheses; complete refinement-set equality at all 102 numerators.
- Replayed the lane's entire ≤200000 length census and contraction census byte-for-byte: **447,996 contractions**. Independent direct fraction enumeration also reproduces the 21841 row: L₃=20 with 2 good, L₄=154 with 100 good, L₅=272 with 110 good.
- Independently rebuilt and evaluated all **1,575 length-four and 2,189 length-five stored witnesses** at three integer representatives each; verified full length-five coverage and all 22 UCOVER intersections.
- Reran enumeration at ℓ=41, R=4, B=2000000 and ℓ=211, R=5, B=2000000; exact rows/witnesses match. At 41 the length-four misses are {11,15}, with 287 events; this is not an unrestricted nonexistence certificate.
- Reran UCOVER S(a) certificates at (ℓ,K₁,K₂)=(11,6,11),(17,5,9). Surviving branches {2,6} and {3,5,6,7} agree; positive lower bounds >0.09556 and >0.06062 respectively. Remaining UCOVER primes are used as the explicitly stated prior input, not independently recertified here.
- Replayed KT3 and all-cut move census/reports byte-for-byte. Independent `scripts/z68_xrev_sign_interior.c` gives interior NOOUT share **0.301087**, ρ=**0.271363**, residue-controlled **0.352830**, over 4,171 primes. All-cut NOOUT replay gives 3,895 filtered primes, ρ=−0.158, controlled −0.075. These statistics do not establish reachability to L₃ or a causal mechanism.
- **F1:** actual HJ denominators are always units, so every square has sign +1 at every length. The 2025 example confirms why the correction factor cannot replace this argument.
- **F2:** all 26 KT2 inputs replay byte-for-byte. For the 12 R₈-zero primes, the ranges 110–191 pairs, 63–131 good, 6–28 with 4∣t, and zero with 8∣t agree. Adding boundary contributions 2·#{d∣n+1:d≡−1 (mod 4 or 8)} to twice the interior pair counts independently reproduces every stored R/R₈ value.
- **F3:** independently checked the cited good words at **284 of the 285 composite zeros**; the remaining 105 has L₃ empty by direct enumeration. The memo claims identities, not composite positivity; its coprimality warnings are indispensable.
- **F4:** checked witnesses against all 14 star, 38 gstar and 12 R₈ screen entries (overlap retained). At 21841, (64,9,38) is the sole good reversal pair among ten. Nothing in the proposed bridge explains this deficit.

## Scope, gate, and fixes

**Required fixes, in priority order: none.** The earlier decisive defects have actually been repaired, not merely relabelled.
Optional editorial tightening: say “the output family's fixed letters vary with n” rather than merely “output letters vary”; even an excluded fixed family already has one varying letter. Explicitly naming 105 in F3 would also make that screen easier to audit.

The gate failed **operationally** (no sufficient bridge demonstrated), not mathematically (no general impossibility proved).
Concrete untried directions remain:
1. Build the sign-labelled graph of forward **and inverse** rescalings and seek a terminating multi-step descent to a good L₃ vertex; one-step NOOUT statistics are no substitute for component/reachability analysis.
2. Use an n-dependent cut or divisor search with an unbounded output-family menu, tracking the accumulated correction character rather than requiring every step to preserve sign.
3. Study a weighted refinement/first-hitting operator whose mass reaches the contractible locus; Proposition 8 does not forbid analytic leverage, although bare ZQ_M supplies no such hitting estimate.
These are specific missing mechanisms, not claims that they work. Stopping this implementation is fair; declaring the entire skew-product or p-adaptive programme dead would be premature.

Reproduction artifacts: `/tmp/xrev_SIGN/` (archived lane, replay outputs, `independent_checks.txt`); committed reviewer scripts only. With that archive/replay directory, run under `ulimit -v 6000000` and `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`:
```
timeout 60 cc -O2 -Wall -Wextra -Werror scripts/z68_xrev_sign_interior.c -o /tmp/xrev_SIGN/interior
timeout 300 /tmp/xrev_SIGN/interior > /tmp/xrev_SIGN/independent_interior.txt
timeout 300 uv run --with sympy --with scipy python scripts/z68_xrev_sign_check.py /tmp/xrev_SIGN
```
All independent checks passed; no claim about ES's resolution is warranted.
