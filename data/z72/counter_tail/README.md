# z72: first small-support shifts beyond 10^18

Result: on a prescribed cohort of Mordell-hard primes above 10¹⁸, shifts 3, 7, 11 are blocked, and the first support-≤2 shift is delayed relative to matched controls (max 127 against 31 and 87).   Label: PROVED (local blocking lemma); CERTIFIED (cohort computation, GNU factor + independent audit)
Scope: a cohort comparison (DATA). It does not refute the unrestricted small-support conjecture, and it does not extend contiguous verification. The “cap 123” refutation is **not new**: see the erratum.
Review: cross-lab (Opus) `data/z74/xreview/REVIEW_Z72PHASE_OPUS.md` (P14 CORRECT, P15 overstated)
Triage: DATA
STATUS delta: none
*(§0 block: z74 Opus xreview fix)*

> **Erratum (z74 Opus xreview fix):** a uniform cap of 123 on the first support-≤2 shift fails already at small primes. At p=66529 the first shift is 323. Among primes with p ≡ 1 mod 840 and (p+1)/2 prime it is 1551, at p=370228321. That is the 840-level family; the target progression p ≡ 1 mod L, with its Q_t conditions, has no primes below 5·10⁸. The maximum below 5·10⁸ is 2695, at p=44407609 (`scripts/z74_xrev_z72phase_bypsieve.py`, `data/z74/xreview/z72phase_bypsieve.log`). These small-prime maxima exceed the cohort maximum of 127, and no growth trend is inferred either way. The content of this file is the certified target/control contrast and the blocking lemma, not a new refutation of a uniform cap.

**CERTIFIED (finite).** Every target and control has an actual z72 Type II witness. The latest target first succeeds at 127, compared to 31 in its size/840 control cohort and 87 in its size/full-progression control cohort. This refutes a **uniform cap of 123** on the first such shift, not the unrestricted small-support conjecture, much less ES. No extension of contiguous verification.

**Construction.** Set `L=4 lcm(1,…,25)=107084577600`. Take successive `p=1+Lk` above the indicated base with both `p` and `h=(p+1)/2` prime. Thus `p≡1 mod 840` is Mordell-hard and `h≡1 mod 4` has no 3 mod 4 prime factors. Pilot starts at `10^18`, cluster at `2·10^18`. After the pilot failed to enrich the median or the extreme, the cluster added three exact primality conditions: `Q_t=1+Lk/(4t)` prime for `t=1,2,3`. There is no infinitude assumption: computations find individual primes, all below `2^64` (deterministic SymPy `isprime` range).

**PROVED (local only).** At `c=4t−1` one has `K=(p+c)/4=t Q_t` and `Q_t≡1 mod c` for these three `t`. For coprime `AB|K`, removing `Q_t` from whichever side it divides leaves `A+B` unchanged mod `c`, but the remaining product divides `t`; hence the remaining sum is at most `t+1<c`. This rules out shifts `3,7,11` even at *unrestricted* support. The conditional construction doesn't itself delay the fourth shift.

**Exact search.** In increasing `c=3,7,11,…` (including composites), fully factor `K`, verifying prime factors and their product. For support one try `(1,q^i)`; for support two try both `(1,q^i r^j)` and `(q^i,r^j)`, all powers up to their valuations. The zero-support pair cannot work. Accept exactly `c|A+B`, then `D=K/(AB), E=(A+B)/c` give `x=K, y=pADE, z=pBDE`. The primary search checks `4xyz=p(xy+xz+yz)`. Caps 1023 (pilot) and 2047 (cluster and controls) never bind on prime cohorts. CSVs contain all cases, not selected examples; `pair` matches target and control within a stage.

| cohort | rows | median first c | 90th | 99th | max |
|---|---:|---:|---:|---:|---:|
| Pilot targets |512|3|11|23|43|
| Pilot next prime with prime h in same 840 class |512|3|11|19|51|
| Cluster targets |2048|15|27|47|127|
| Cluster next prime with prime h in same 840 class |2048|3|11|19|31|
| Cluster next prime with prime h in same L class |2048|3|15|31|87|

Quantiles are nearest rank. Controls are deterministic matches, not independent random samples. Six of the 2,048 full-progression control primes also occur as targets; these are retained rather than selecting controls on the outcome. The cluster's 840-matched gaps are ≤510720.

**Independent check.** For every one of 7168 CSV rows the audit reads the literal triple and sums three `Fraction` values, independently checking positivity, support and `4/p`. For every row with `c>63`, the audit enumerates `A|K, B|(K/A)` using SymPy's divisor engine, testing gcd, support and `c|A+B` at every eligible earlier shift and at the first hit. All pass. Late targets: `(2019030344657726401,79)`, `(2650016366384587201,83)`, `(5091403384022155201,111)`, `(3127054922239248001,127)`; at the last, even a single prime `B=39276714758833` suffices with `A=1`. Late full-progression control: `(2170275209960457601,87)`.

**Falsifier screens** (all shifts ≤127, numerator 4): F1 odd squares 0/50 hits; F2 R8 zeros 12/12; F3 composite line zeros 280/285; F4 star 13/14 and gstar 37/38. Composite results test only the integer construction, not prime-specific forcing. A bounded miss here is not a nonexistence claim.

Replay on one core with GNU `factor` (9.7 used):

```
(ulimit -v 2000000; for s in pilot cluster controls; do timeout 240 uv run --no-sync python scripts/z72_counter_tail.py "$s" || exit 1; done; timeout 120 uv run --no-sync python scripts/z72_tail_audit.py)
```
