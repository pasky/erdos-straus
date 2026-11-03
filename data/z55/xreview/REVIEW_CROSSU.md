# CROSSU cross-model hostile review

Reviewed `side-agent/z55-crossu` at `9c4db73de828bfb3c282aa43c0c7a3a529b6f3c1` (`Z55_CROSSU.md`).
**Verdict: ACCEPT-WITH-FIXES.** The class-index reformulations survive; the numerical evidence reproduces.
One scope assertion is false: §4.1 denies growing minimum square-subgroup size on moving windows.
This does not invalidate the conclusion “inconclusive on (CU), narrowed only by elementary reformulations.”
**ES remains OPEN.** No estimate for (CU), (X-w), or positivity at all large primes is established.

## Per-claim audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| §1 shell and level formulas | CORRECT | `2wd=p+u`, oddness, and the coprimality hypotheses give odd `d`, `(d,u)=(d,p)=1`; `d>p/(2X)≥4U1`. The exact class is `d≡−1 (4u)`; its genus projection has weight `1/q_u`. |
| §1 conditional implication | CORRECT-WITH-FIX | `R=M+(G−M)+(R−G)≥c log²p+o(log²p)>0` on the **same admissible window**, with `c>0`. Correct the source “GX Thm U” to `Z53_GENUSLVAL.md`, Theorem U; GX cites, but does not contain, that theorem. Do not infer its hypotheses from the numerical window alone. |
| Lemma A(a,b) | CORRECT | `u a=1+jd`, `1≤a<d`, `u>1` imply integral `0<j<u`; reduction modulo `u` gives `jd=−1`. Hence hit iff `j=1`; inversion preserves the square subgroup, so genus iff `j∈□_u`. |
| Lemma A(c) | CORRECT | Multiplying `jd=−1 (u)` by `2w` gives `u | 2w+jp`. For `e=(2w+jp)/u`, `de=1+pa`; `0<2w<p` and `1≤j<u` imply `0<e<p`. Thus `e=d̄`, `a=(dd̄−1)/p`, and `j=⌊ud̄/p⌋`. Since `u<d`, the least residue of `−p` is `u`. In fact this works for the stated coprime composites too. |
| Lemma B | CORRECT | The first ceiling quotient is `2w`, remainder `u`; the second remainder is `r=−d mod u`, with `rj=1 (u)`. Three divisions terminate iff `r=1` (coprimality excludes any other final divisor of `u`). At a hit `d=tu−1`, and modulo 4 gives `4 | t`. Multiplication gives `M(2w)M(t)M(u)=[[p,−(2wt−1)],[d,−t]]` and determinant 1. |
| Lemma C, including signed identity | CORRECT | `j=c (u)` iff `cd+1=ut`; then `2wtu=cp+cu+2w`. Division by `2wtu·cp` gives exactly the three displayed fractions. For `c=−1`, writing `t=−t′` gives `2wt′u=p+u−2w` and the signed formula. For `c>0`, `t>0`; nonunits cannot occur. At fixed `u`, each shell point belongs to exactly one exact class and to `q_u` coset-weighted classes, proving both sums. |
| §3 reading / square-twisted average | CORRECT | Read fibrewise: `(1/q_u) Σ_{c∈□_u} N_c|_u=G_1|_u`; equivalently average over all unit `x` and `c=x²`. The averaging groups vary with `u`, so this is not a single unspecified average of global integers `c`. |
| §4.1 weight values and elementary bound | CORRECT | At hits `f=1−1/q_u`; at genus non-hits `f=−1/q_u`. When all `q_u≥3`, positive hit weight is at least `2/3`, negative magnitude at most `1/3`. Thus no weight-negating bijection at a hit; `k` negative points with `q_{u′}≥q` require `k≥q(1−1/q_u)`. The exception `u=5`, `q_u=2`, is real. |
| §4.1 “q_min→∞ … fails in every window (u=21)” | WRONG | Moving windows exclude every fixed `u` eventually. In fact `q_u≥(2/√15)√u` for every odd squarefree `u`; see fix 1. This also corrects the claim that bounded-size exact cancelling groups are unobstructed on the moving family. |
| §4.2 switching | CORRECT | On the stated switchable domain, `j′=−w⁻¹=2p⁻¹j⁻¹ (u)`; applying twice is identity. A hit stays a hit iff `p=2 (u)`; it becomes a genus non-hit iff `2p∈□_u` and `p≠2 (u)`. For weights on `S3`, both levels must be 3 modulo 4. Permuting a switch-closed multiset preserves its total genus count, even when the ambient map exchanges cosets. |
| §4.3 Vieta / conic identities | CORRECT | The positive-point equations determine the remaining coordinate linearly; a zero coefficient would leave a strictly positive right side for `c>0`, hence no such point. Swapping `x,y` preserves `S_p`, other coordinate permutations do not. Expanding `(zx−1)(zy−1)=zp+1` verifies the conic factorization. No assertion about simultaneous changes of coordinates follows. |
| §4.4 incidence identity | CORRECT | Substitution gives `d=(4Cp+1)/(4Ck−1)` and `u=(p+k)/(4Ck−1)`. Since `(4C,4Ck−1)=1`, integrality of the former implies that of the latter. The family restrictions must still be imposed on these pencil intersections. |
| §4.8 Dedekind identities and extremality | CORRECT | The defining sum is odd in its first argument and invariant under inverse residue (permute summation indices); thus `s(d,u)=−s(j,u)`. Reciprocity gives `s(d,u)+s(u,d)=(u/d+d/u+1/(ud))/12−1/4`, and `s(u,d)=−s(p,d)`. Cauchy–Schwarz on the two permuted sawtooth vectors gives `|s(h,u)|≤s(1,u)=(u−1)(u−2)/(12u)`; `d=−1 (u)` realizes the negative extreme. |
| §4.10 Jacobi identity | CORRECT | For odd `n=1 (4)`, `u=1 (4)`, `d=3 (4)`: `(j/u)=(−d⁻¹/u)=(d/u)=(u/d)=(−n/d)=−(n/d)=−(d/n)`. All symbols are units. Hence `(d/p)=−1` on genus support, and its inner product with `2f` is exactly `−(R−G)`, not a new cancellation estimate. |
| §5.1 square vanishing | CORRECT-WITH-FIX | At `n=m²`, `(d/n)=1`, so `(j/u)=−1`, excluding every coset with `(c/u)=1`. The seven listed classes vanish in all 150 runs. Insert “for every **coprime** `u≡1 (4)`” into the characterization of those classes: e.g. `(9/21)=0`, not +1. |
| §§4.5–4.7, 4.11 and §6 screens/verdict | CORRECT as Assessment | No uniform exclusion of Kloosterman hybrids, incidence methods, descent, or positivity transfer is proved. The entropy threshold uses the lower scale correctly. Failure to find a mechanism is not proof that it cannot exist. The final inconclusive verdict respects this distinction. |

The Dedekind reciprocity normalization was checked against [MathWorld, Dedekind Sum, (15)](https://mathworld.wolfram.com/DedekindSum.html), which states the two-term law with the required coprimality and −1/4 constant.
The other new PROVED claims above use elementary algebra and quadratic reciprocity, not the analytic method assessments.
The imported Theorem U is treated as the stated earlier result, not re-proved by these numerical tests.

## Numerical reproduction

Audit: `scripts/z55_xrev_crossu_check.py`; branch files extracted into `/tmp/xrev_CROSSU`.
All shell commands used `ulimit -v 6000000` and `timeout`; the audit also sets RLIMIT_AS and bounds child execution.
The C engine's arrays scale with `√n` and the `u`-window; the independent scan uses at most 2 MB for squarefree flags, finite unit sets, and one shell at a time. No Cartesian-product arrays.

- Recompiled the reviewed C source and replayed **all 1,339 rows**, comparing **every serialized field**: exact agreement.
- Total `S3` and `nA`: **3,014,093** each; all three mismatch counters remain zero. These are finite checks, not asymptotic certification.
- Independent enumeration scans odd `w`, computes `u=−n mod w`, and forms square subgroups by explicit unit squaring, rather than copying the C factorization/Legendre tests.
- Seven independent scans, at `n=1000345561,1007633689,10033405441,100020001,10257435857,409,10000000001`: all shell points and all 18 rational `N_c,G_c,E_c,V_c` totals agree to TSV rounding. Respective `(shell,S3)` counts: `(220,112),(236,121),(530,260),(86,43),(615,308),(0,0),(627,315)`.
- Independent prime-sample ranges: means **[−0.6733555,+0.5894336]**, sd-ratios **[0.8754101,1.1765153]**, z **[−2.4853289,+1.9144201]**: agree with the memo's rounding.
- Pooled z for `c=1,−1,2,4,12,25`: **−1.611455,+2.157839,−0.124502,−0.047323,+2.043449,+2.349833**: agree.
- Supplied statistics program reproduces `stats.txt` byte-for-byte, including histograms, correlations, hard-prime and control summaries. Square zero classes are exactly `{1,4,9,16,25,−1,−4}`.
- Regenerated all 300 pair dumps and reran the seeded set-valued null/bootstrap: **byte-for-byte agreement**, 769 hits, 967 distinct-`u` hit pairs; mean `u` 1205.9 versus 1401.7.
- Pair differences / bootstrap intervals (percentage points): gcd-u **+1.15 [−1.44,+3.99]**; gcd-d **+3.00 [−1.00,+7.58]**; near-u **+4.33 [−0.35,+8.77]**; divisibility **+0.60 [−0.34,+1.79]**. Each contains zero; that is not equivalence to the null.

Reproduce after extracting the reviewed source/data and compiling the engine:
`ulimit -v 6000000; timeout 900s uv run python scripts/z55_xrev_crossu_check.py /tmp/xrev_CROSSU /tmp/xrev_CROSSU/engine`

## Required fixes, priority order

1. **Correct §4.1 and its review-log disposition.** For squarefree odd `u`,
   `q_u/√u = ∏_{ℓ|u}(ℓ−1)/(2√ℓ) ≥ (1/√3)(2/√5)=2/√15`,
   because every prime factor `ℓ≥7` contributes more than 1, and 3 and 5 occur at most once.
   Consequently `q_min≥(2/√15)√U0→∞` whenever `U0→∞`, including the standard `U0≈p^(1/12)` window.
   For any fixed number `K` of genus non-hits, their total negative magnitude is at most `K/q_min`, while a hit has weight at least `1−1/q_min`.
   Thus a hit cannot be cancelled exactly by `K` such points once `q_min>K+1`; bounded-size exact zero-sum groups containing a hit are excluded there.
   Retain only the qualified statement that a fixed lower cutoff allowing `u=21` need not have growing `q_min`.
   This strengthens an elementary pointwise obstruction, **not** an obstruction to large groups, approximate cancellation, or positivity maps.
2. **Repair the two small qualifications** in the table: Theorem U's actual source / common-window hypotheses; and the coprime-`u` quantifier for square vanishing.
3. **Keep the evidence and exports scoped.** The independent-class maximum-correlation scale is a heuristic benchmark, not a calibrated null test; the pair null is descriptive. Preserve those caveats and the explicit statement that neither finite experiment establishes or refutes (CU).

With these edits, accept the reformulations and the negative search report; do not bank a cross-u cancellation theorem or a general mechanism-class closure.
