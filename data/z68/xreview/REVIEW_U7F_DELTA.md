# Z68 U7F — hostile cross-model DELTA review

**Verdict: ACCEPT-WITH-FIXES. ES is OPEN.** The new finite census survives; the negative-method rhetoric still needs correction.
Scope: `side-agent/z68-u7f` at `62ec79363`; only original required fixes and §9 (including its §6/§8 summaries).
Base: review commit `390f9c5a6` explicitly names lane tip `11cd0e4da1e2c8a69cb05713e5562df4ac7a650d`; its own Git parent is the unrelated common base `8e5ecfaa8`.
Audited delta: `git diff 11cd0e4da..side-agent/z68-u7f -- Z68_U7F.md`. This is not a second full review.

## Per-claim audit

| Claim | Result | Independent finding |
|---|---|---|
| Original fix 1: composite boundary / prime-only B | PASS | F3, §4.3, §6 now record 196065 correctly. Exhaustive rescan gives only (f,r,y,z)=(13079,120,109,15), c=319; all eight Z₇ controls remain empty. The inherited 276-control count is not re-audited. |
| Original fix 2: §3.4 maps / complement move | PARTIAL | T₇ and the p=17 exit from U₇ are correctly added. But the replacement still asserts “no map n↦cn preserves T_f for all f”; its Jacobi necessary condition does not prove that assertion (and c=1 is an immediate counterexample). |
| Original fix 3: §6 strategy scope / omitted residue | PASS | Prop 3.6 is now limited to the small-outer-letter strategy on its progression. For n≡5 (8), f=n+2, r=2 indeed works; this does not establish the ω≤2 refinement there. |
| §9.1 exhaustiveness / x-form / cofactor convention | PASS | r≤(f+1)/2 gives f≤2p+1. The x-form has the three exceptions restored and is sufficient; if r=f+1, replace by canonical residue 1. The sole six-family convention overlap needing attention is f=15. |
| §9.1 full six-family census | PASS | Independent unordered-outer-letter enumeration, including y=1, reproduces every decisive count below through 10⁹. It does not reuse the lane's (f,r,t) sieve. |
| §9.1 κ / powers / exceptions | PASS | Every witness list for all 231 prime-witness-free primes matches. κ counts are 1:12710989, 3:220, 5:8, 7:1, 9:1, 25:1; restricting to c·q gives the same minima. The 11- and 3-prime exception lists match exactly. |
| §9.1 K3 / shift statistics | PASS, clarify | All 38 witness lists match; minimum-family counts are 35/2/1 for c=1/3/7; no U⁽⁸⁾ words, including y=1. The printed shift histogram uses minimum r among minimum-c witnesses, not the engine's first/least-f minimum-c witness. |
| §9.1 C / heuristic | SCOPED | C remains a prime-only conjecture, not a proved eventual theorem. Exponents ≈0.67/0.25/0.165 are compatible with the counts; independence and summability are model assumptions. Prop 3.6 applies only after fixing R and its progression, not uniformly to an arbitrary moving r. |
| §9.2 relation count | PASS WITH BUG | Independently regenerate the 43 hard primes, all unordered words, and representations. Maximum is indeed 6/43, solely (A,abs(u−v)/2,y), with either exact rational arithmetic or lane floors. Floors nevertheless introduce 11 half-integer matches; they are not the advertised formulas. |
| §9.2 simultaneous/admissible rules | NOT TESTED | Each candidate uses one representation of one shifted integer. No mixed-shift formula, valuation/gcd admissibility rule, or prime-only construction is searched. The square-class argument is explicitly conditional on an unproved lifting statement and cannot close this gap. |
| §9.3 growing k | IDENTITY ONLY | Fixing y gives (xy−1)(zy−1)=py+1; equivalently yk²−4(p+k)=y(x−z)². This correct re-indexing does not rule out a method using growing k. |
| §9.3 cancellation / weights | OVERCLAIM | The Jacobi filter vanishes on coprime squares and equals 1 on hits. But failure of a single-modulus indicator to depend only on (p/f) proves neither a no-go for correlations across f nor that variance can only give almost-all results. The asserted necessary error alternatives are unsupported. |
| §8 ISPRIME(1) fix | PASS FOR COUNTS | Pre/post cfam outputs are byte-identical at 10⁹; pre/post wit outputs at 10⁸. The old cfam erroneously adds F₇ membership to f=7 (q=1), already in F₁, so no reported failure count changes. Square n=1 cannot be a hit; final p loops start at 17. Internal masks, unlike reported counts, need not be identical. |

Independent census columns: N; primes; no F₁; no F₁∪F₃; no F₁∪F₃∪F₅; no six-family witness; no F₃; no F₅.
```text
10000000    165976    66   9  3  0   3572   11002
100000000  1439970   118   9  3  0  17354   64881
1000000000 12711220  231  11  3  0  87479  393373
```

## Required fixes

1. **MAJOR, §3.4:** Delete the universal multiplicative-map assertion or prove a precisely qualified version. Retain only the necessary Jacobi condition and “no nontrivial uniform symmetry was found.” For example, c=4 satisfies that condition for every odd f but fails at f=23: 19∈T₂₃, 4·19≡7∉T₂₃.
2. **MAJOR, §9.3:** Replace “would need … either”, “almost-all statements only”, and “none … can” by the actual finding: no pointwise lower bound was obtained. A character vector across moduli is not one local Jacobi symbol; the three directions remain open. Relabel the displayed sum a heuristic proxy, or normalize conditional hit probability as w_f·2(τ(f+1)−1)/φ(f), w_f=(1−(p/f))/2, on units; w_f·(τ(f+1)−1)/f is not that conditional expectation.
3. **SCOPE, §9.2:** Describe the experiment as single-representation formula matching, not a search exhausting simultaneous/admissibility rules. Reject nonintegral half-expressions instead of floor-dividing (or explicitly describe the different floor search). The corrected maximum remains 6.
4. **MINOR, §9.1:** Specify the minimum-r tie-break for the shift histogram; the engine's minimum-(c,f) rule instead gives r=2:48, 8:40, 4:31, 20:24. Restrict “Prop 3.6 applies verbatim” to its fixed-R progression hypotheses. Keep “prime powers never needed” finite-range/model-qualified and specific to the variable q exponent (cofactors 9 and 25 are needed).

## Reproduction / limits

Independent code: `scripts/z68_xrev_u7f2_census.c` and `scripts/z68_xrev_u7f2_checks.py`; all compute runs use `ulimit -v 6000000`, `timeout 1800`, one compute process at a time (no subagents).
Extract the reviewed memo/scripts/data under ROOT; compile the C checker with `gcc -O3 -Wall -Wextra -Werror`. Run `census 1000000000 > ROOT/independent_census.txt` (59.7 s, 2,076,344 KiB peak RSS).
Run `census 0` separately with stdin from each of `noprime_primes_1e9.txt`, `u8zero_primes_1e8.txt`, and the nine K2 controls; concatenate outputs into `ROOT/independent_witnesses.txt`. Then run `uv run --with sympy python scripts/z68_xrev_u7f2_checks.py ROOT` (≈59 MiB; PASS).
The checker compares all supplied witness lists, independently regenerates the 43-prime relation dataset and words, and compares exact versus floored formulas. Separate pre/post builds use `2d0683c94` and `62ec79363`; byte comparisons pass at the bounds stated above.
No provider/auth/quota error occurred. No merge performed. Acceptance is conditional on the scope fixes, not on discovering a new mechanism or resolving ES.
