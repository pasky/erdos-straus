# SIGN cross-model DELTA review

**Verdict: ACCEPT-WITH-FIXES (one local wording fix; mathematics and decisive counts pass). ES remains OPEN.**
Scope: `git diff e2f66fdfa..83d90a366 -- Z68_SIGN.md`, not a re-review of §§1–8. The prior ACCEPT names `e2f66fdfa`; reviewed tip is `83d90a3664e4d2cb9e461cb61d2ab56ea797d336`.
No provider/auth/quota errors occurred. Computation used `ulimit -v 6000000`, timeouts ≤1800 s, one sequential checker child, single-thread settings, and O(n+E) graph storage (largest n=991633).

| Delta claim | Decision | Independent finding |
|---|---|---|
| §9 provenance / registration | PASS | §9 correctly limits the previous ACCEPT to the old memo. Commit c6224708d registers the types/threshold before graph-code/data commit 0942a8b31; exact starts and tie-breaks are disclosed as later implementations. |
| Forward/inverse moves and labels | PASS | Rebuilt every generated target word; checked numerator, full HJ equality, oriented denominator congruence, and character label on 12,527,878 generating instances. Inverse traversal reverses the congruence exponent, not the character. |
| Proposition 9 | PASS | Derivation below; valid for every walk, not just strict descents. Every closed walk has label product +1; no sign obstruction/no-go follows. |
| Prime-level kill counts | PASS | Independently summed all 2,384 archived prime rows: 987, 987, 2138, 2139, 2139, 1870, 2141 in table order. Checked completeness/primality of the index set. All seven rates are below 99%. |
| Independent subsample | PASS | Fresh graphs at 91 primes ≤10⁵ give 34, 34, 70, 71, 71, 47, 50 successes in the same order, exactly matching those archived rows. This deliberately edge-case-enriched sample is not a population-rate estimate. |
| Rising S3 band trend | PASS as finite evidence | Archived existential-D counts are 6/37, 168/258, 440/501, 652/695, 875/893, then 30/30 near 10⁶; Rmin has 28/30 there. Larger ensembles with falling per-word rates do not establish independence, eventual success, or a useful selector. |
| Components, heights, squares | PASS | All 138 fresh graphs match exact component counts, largest-component fractions to printed precision, and both minimax heights. All 36 square controls have no good vertices. Prime-square giant fractions reproduce 850/1640, 6172/9312, 76782/97656; a giant is not a non-square certificate. |
| 21841 | PASS | Good L₃ denominators exactly {575,2431}; S1=11 ends at 22, S2=22; neither is in D. Exactly 2/1014 S3 starts descend. S2 minimax heights are 6 in E and 8 in E⁺. |
| 409 | PASS, specifically S2 | Eight good L₃ denominators are {7,13,21,39,59,63,104,117}; none lies in the 19-vertex component of S2=22. Do not generalize to every registered start: S1=7 is already good L₃. |
| 881 / plateau distinction | PASS | Verified both E⁺ edges 12→444→111, the stated words, D(12)=0 and h(12)=4. Strict descent can fail without any need to climb. |
| F3 editorial delta | PASS | Exhaustive HJ enumeration gives L₃(105)=∅; the added existential-(S) qualification is necessary and correct. |
| Scope of negatives | PASS with wording fix below | Failed registered rules do not exclude plateau/climbing moves, alternative starts, unbounded menus or weighted hitting estimates. KG3's final discussion correctly declines an exclusion; bounded k alone is insufficient. |

## Independent derivation
At a cut, n=bXY−XY′−X′Y. A right move replaces (X,b,Y′) by (kX,b/k,Y′/k), preserving n; its divisibility, gcd and b/k≥2 predicates give reduced valid HJ pieces, including the empty tail.
Moreover n≡−X′Y (mod k), and gcd(k,X′)=gcd(k,Y)=1, so every admissible multiplier is a unit even for composite n.
For an original prefix matrix [[X,−X′],[Z,−Z′]] and its rebuilt prefix [[kX,−X′],[T,−T′]], determinant one gives T−Z=tX and kT′−Z′=tX′ for an integer t. Substitution into the denominator formula gives kA_new=A+tn. This proves the right congruence without illicit cancellation of X at composites.
Reversal inverts the word denominator modulo n, so the reflected left move gives A_new≡kA. Backward moves invert these factors. Multiplying along a prime-modulus walk yields A_m≡A_0∏k_i^{ε_i}; multiplicativity and χ(k⁻¹)=χ(k) give Prop 9 exactly.
The label product depends only on the endpoints, and equals +1 on cycles. This identity supplies neither a good endpoint nor a hitting theorem.

## Required fix
**R1 (wording only):** §10.2 “Signed reachability” says “S1 then lies in a small component” immediately after reporting successful reachability. Delete this parenthetical assertion or explicitly restrict it to the intended failure cases. At 21841, S1=11 is in the largest E-component, of size 15104/21840≈69.2%, and reaches both good L₃ vertices. The existing “not necessarily isolated” example at 17 is valid but does not repair the ambiguous/false general assertion.
No numerical or theorem repair is required. Keep “registered strict-descent rules fail” rather than “rescaling transport is impossible”; keep 409 explicitly tied to S2.

## Concrete untried direction
Pre-register a deterministic restarted, plateau-saturating search over S3 (in increasing A): explore the current equal-length E⁺ component, then choose a shorter exit with fixed tie-breaks, restarting when stuck. This is different from Rmin and strict D, and the 881 example proves the distinction matters.
Test it on a complete held-out interval beyond 10⁵, recording work per prime, failures, and ensemble sizes; the rising 16%→98%→30/30 band trend motivates this experiment but does not prove it will succeed. Any eventual theorem must separately handle the finite exceptional primes, not retroactively change the registered all-primes threshold.
An alternative analytic target is a uniform bound on the fraction/mass of bounded-digit starts whose first-hit distribution reaches good L₃, with correlations between starts controlled. Counting “tickets” alone is not that bound.

## Reproduction
Reviewer-owned scripts import no lane graph code. Selection: all 37 primes ≤1000, 12 evenly spaced indices in each later band, named difficult cases and the Rmin/Rmin⁺ discrepancy; 91 distinct primes ≤10⁵ in total, plus 589681, the two endpoints of the near-10⁶ sample, and all 44 controls (138 graphs).
The checker uses traversal components, reverse strictly-increasing reachability for D/D⁺, dynamic greedy endpoints, and bottleneck Dijkstra for heights. All exact COUNTS fields agree; full-range totals/trend aggregation is distinguished from fresh subsample computation above.
```
ulimit -v 6000000; export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
timeout 60 g++ -std=c++17 -O2 -Wall -Wextra -Werror scripts/z68_xrev_sign2_graph.cpp -o /tmp/z68_sign2_graph
timeout 1800 uv run python scripts/z68_xrev_sign2_check.py /tmp/z68_sign2_graph
```
Result: **PASS, 138 graphs, 36 squares, 12,527,878 rebuilt generating moves; zero discrepancies.**
