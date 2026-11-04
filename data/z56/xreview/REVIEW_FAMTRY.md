# Z56 FAMTRY hostile cross-review

Reviewed `side-agent/z56-famtry` at `4fdc551d5c5fe7490946af7b315dccc373a09465`, especially Theorem A.
**Verdict: ACCEPT-WITH-FIXES. Theorem A is CORRECT; the eventual-positivity target remains INCONCLUSIVE. ES is OPEN.**
The valid exceptional-set estimate does not establish novelty, eventual positivity, or a universal obstruction to other methods.

## Per-claim audit

| Claim | Classification | Independent check / qualification |
|---|---|---|
| Lemmas 1.1–1.2, exact counts | CORRECT | Solve `B(4uC−1)=n+u`; substitute `m=uC`, `d=4m−1`. The factorization `(4uC−1)(4BC−1)=4Cn+1` is bijective, including ordered factors. |
| Lemma 1.3, square/Jacobi obstruction | CORRECT | `gcd(u,d)=1`; odd-part reciprocity gives `(u_odd/d)=1`; if u is even, `d≡7 (8)` gives `(2/d)=1`. Thus `(n/d)=−1`, excluding squares; reciprocity gives `(d/p)=−1` for p≡1 (4). |
| Lemma 1.4, bounded divisor test | CORRECT-WITH-FIX | `u≤(d+1)/4<d`, and `d≤n+u` implies `3d≤4n+1`; converse reconstructs positive B,C. Define the residue in `[0,d−1]` and explicitly require it nonzero: the displayed `[1,d−1]` residue is undefined when d divides n. |
| Proposition 2.1 | CORRECT | Substitution verifies the three small-modulus constructions; divisor classes are distinct and have Jacobi symbol −1. |
| Proposition 2.2 and finite polynomial menus | CORRECT | Any solvable class congruent to 1 modulo its modulus contains arbitrarily large odd squares. Therefore every finite such menu misses all primes 1 modulo `8·lcm(q_i)`; Dirichlet applies. Polynomial menus require eventual positive integral validity on the stated/refined classes. |
| Remark 2.3, “any proof ... not a congruence condition” | GAP | Only fixed finite solvable coverings are excluded. Growing/infinite congruence families and prime-sensitive arguments are not excluded. |
| Lemma 3.1, prime-modulus hit implies R>0 | CORRECT | Divisibility makes `(n+u)/ℓ` a positive integer for every positive n; there is no hidden `n>ℓ` hypothesis. |
| Lemma 3.2, dyadic mass ≥1/25 | CORRECT | BV is applied to distinct moduli `4d≤4Y^(1/3)`, with coprime residue −1; the aggregate error is `O(Y/log²Y)`, not multiplied by the number of d. Details below. |
| Lemma 3.3, exponential lower bound for L | CORRECT | Disjoint dyadic blocks force squarefreeness; unique factorization prevents overcounting; the chosen k,m meet the product cutoff eventually. Floors and the −3 loss are valid. |
| Theorem A, c=0.08, odd sifted set, uniform intervals | CORRECT | The cited large-sieve form has precisely this denominator and is translation-uniform. The exact pre-absorption exponent is `0.08837364810457118>0.08`; no primality input or interval-position-dependent BV is needed. |
| §3.5(i), §4.4(i), square floor | CORRECT-WITH-FIX | The full integer avoider set up to X contains `(1/2+o(1))√X` odd squares. This obstructs bounds on that set alone, not every sieve counting primes, prime weights, or off-square refinements. |
| §4.4(ii), `log L(Q)≍√log Q` | CORRECT | Divisor pairing plus Brun–Titchmarsh gives `Σ_{ℓ≤t}ω(ℓ)≪t`; partial summation and Rankin give the upper bound, Lemma 3.3 the lower. Optimality concerns this specific denominator/large-sieve bound only. |
| §3.5(ii), sharper `(1+o(1))κ√log Q` assertion | GAP | The supplied proof gives two-sided order, not an asymptotic constant. Prove/cite the additional asymptotic analysis, or replace this assertion by `Θ(√log Q)`. |
| Lemma 4.1(a)–(f) | CORRECT | Small classes give p≡1 (24). Divisor exclusion gives (b),(f); subset products in the two Klein-four unit groups give (c)–(e), with the factor 3 in 8p+1 selecting `{1,3}`. The structural file also reproduces. |
| §4.5 three-modulus bound | CORRECT | `3(u+B)≤p+4` follows from `uB≥u+B−1`; the product of the three actual moduli is below `4(p+u+B)²`. Thus their minimum is `<1.93(p+1)^(2/3)`. |
| §4.5 headline finite data | CORRECT | Reproduced q-min maximum 6,627,800 at 92,722,897; corrected d-min computation retains 2,953,943 at 85,664,329 and prime-d maximum 50,015,899 at 99,986,329. These are finite observations only. |
| `dmin_1e8.txt` lower-decade maxima | WRONG | Running maxima are reset to zero by no-hit primes; concrete corrected values below. |
| Summary / §4.5 “any proof must use composite moduli”, modulus ≍p necessity | GAP | The 422 observed prime-modulus failures and finite large-modulus examples do not refute eventual prime-modulus sufficiency or establish infinitely many linear-size minima. §5 correctly acknowledges eventual sufficiency remains open; make the summary agree. |
| §3.5(iii), §4.2, §5 universal methodological exclusions | GAP | Failure of a product-class implementation is not non-applicability of all large/Selberg sieves or all equidistribution arguments. §4.4(iii)'s explicit “unsolved obstacle, not ... impossibility” is the appropriate label throughout. |
| §4.6 EH/GRH and random model | CORRECT-WITH-FIX | No conditional theorem is established. GRH alone does not supply EH's level `1−ε`; prime-only first moments are `Θ(log p)`, not `Θ(log²p)`, so the stated random-model failure rate is wrong. |

## Theorem A: proof reconstruction and source checks

1. Let `T(Y)=Σ_{Y<ℓ≤2Y}ω(ℓ)`. Each divisor `d≤Y^(1/3)` with `ℓ≡−1 (4d)` contributes a distinct counted divisor.
2. BV at scale 2Y therefore gives `T(Y)≥(li(2Y)−li(Y))Σ_{d≤Y^(1/3)}1/φ(4d)−O(Y/log²Y)`.
3. `Σ1/φ(4d)≥H_floor(Y^(1/3))/4≥log Y/12` and `li(2Y)−li(Y)≥Y/log(2Y)`.
   Consequently `liminf T(Y)/Y≥1/12>1/12.5`; dividing by 2Y yields the eventual `A(Y)≥1/25`.
4. Put `J=floor(log₂Q)`, `k=floor(√(c₀J/2)/e)`, `m=floor(J/k)−j₀`.
   For sufficiently large J, `m≥J/(2k)≥k` and `k(j₀+m)≤J`. Selecting k different blocks gives
   `L(Q)≥binom(m,k)c₀^k≥(mc₀/k)^k≥exp(2k)≥exp(√(2c₀)√log Q/(e√log 2)−3)`.
5. At `Q=√X`, the large sieve bounds the entire avoider set by
   `2e³X exp(−a√log X)`, `a=1/(5e√log 2)=0.08837364810457118`.
   The extra √X term in the memo is unnecessary and harmless; either bound is ≤`X exp(−0.08√log X)` eventually.
6. An interval of length X has the identical large-sieve numerator, regardless of its starting point.
   BV only constructs the fixed sifting weights as a function of Q; no short-interval distribution theorem is invoked.

Decisive sources actually visited:
- Kedlaya, [Theorems 16.1, 16.4 and Lemma 16.5](https://kskedlaya.org/ant/chap-largesieve2.html): translated-interval inequality and the exact squarefree product `ω(ℓ)/(ℓ−ω(ℓ))` denominator.
- Kedlaya, [Theorem 17.1](https://kskedlaya.org/ant/chap-bombieri.html): BV in ψ form; partial summation on `[Y,2Y]` gives the π estimate needed here. Prime-power errors over `O(Y^(1/3))` moduli are `O(Y^(5/6)log Y)`, negligible. The stronger max-y formulation is not needed.
- The original Montgomery–Vaughan download was CAPTCHA-blocked; the exact LNM chapter/theorem locator was not independently verified. This does not affect the checked mathematical statement.

## Numerical audit

All shell invocations used `ulimit -v 6000000` (or stricter), CPU limits, and per-command timeouts.
Sources/data were extracted from the pinned branch to `/tmp/xrev_FAMTRY`; C runs used `gcc -O3` and ≤220-second run timeouts.
Allocation audits: census ≈434 MB; L/dmin/qmin ≈0.9–0.95 GB; dyadic sum ≈806 MB; unclipped census ≈734 MB.
- `census 100000000`: byte-identical output, all 14 listed zeros (last 8,813,281), 2,880,504 primes ≡1 (4), 659 prime-d zeros, 32,971 sqrt-prime-d zeros, and 4,999 tested odd squares with no hit.
- Top decade: 1,273,994 primes ≡1 (8), no R-zeros, 422 prime-d zeros, 13,533 sqrt-prime-d zeros. The preceding decade's 143 and 2,958 also agree.
- Replacing R's byte counter with `uint32_t` and removing saturation gives identical printed output: the rounded mean 49.5238 and ratio 0.1459 survive an unclipped run. Original zero/nonzero certification is unaffected by saturation.
- `L 100000000`, `c0 29`, `qmin 100000000`, and `uv run --with sympy .../z56_famtry_struct.py`: all byte-identical to their stored files. Thus L(10⁴)=11.03 (rounded), the ≈0.95 log-L ratio, and dyadic masses near 0.43 reproduce.
- `dmin` was rerun after replacing the two updates by `if(dm[p]>md){md=dm[p];ad=p;}` and `if(dp[p]>mp){mp=dp[p];ap=p;}`. No-hit cases must not overwrite a finite maximum.
  Correct prime-d maxima in decades 10³–10⁴, 10⁴–10⁵, 10⁵–10⁶ are respectively **4759 @ 9433**, **44563 @ 89113**, **483619 @ 943057**, not 79, 359, 1019.
  Correct all-d maxima in 10⁵–10⁶ and 10⁶–10⁷ are **64255 @ 706801** and **60759 @ 4617649**, not 12847 and 14559. Top-decade values and histogram are unchanged.
- The 10¹⁰ census is inherited from `FRONTIER.md` §2.1, not newly certified here; this review reran through 10⁸ only.

## Required fixes, priority order

1. Narrow all universal claims: only fixed finite solvable coverings and the displayed whole-integer/product-class sieves are obstructed. No theorem here forces composite moduli eventually, linear-size moduli infinitely often, or one particular missing ingredient for every proof.
2. Repair the `dmin` maximum updates and regenerate the erroneous lower-decade table; preserve no-hit counts separately. The headline examples remain valid.
3. Correct §4.6: prime-only independence with probabilities `2ω(ℓ)/(ℓ−1)` has cumulative mass `Θ(log p)`, hence polynomial-scale survival after handling finitely many small primes, not `exp(−c log²p)`. Summability needs its actual constant; a model's almost-sure conclusion is not a deterministic theorem. Separate EH from GRH.
4. Replace the unsupported precise log-L asymptotic with the proved two-sided order, and make the residue-zero convention in Lemma 1.4 explicit. Keep novelty unverified.

**Bankable:** Theorem A (including uniform intervals), the elementary identities/obstructions, and the explicitly scoped denominator-growth theorem. **Not bankable:** eventual (★), a universal sieve barrier, or a proof that composite moduli are eventually necessary.
