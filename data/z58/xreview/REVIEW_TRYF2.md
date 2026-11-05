# z58 cross-model hostile review — TRYF2

Reviewed `side-agent/z58-tryf2` at `dbcede37d8f016625d73b89e61cfe68234e5f592`, including memo, scripts and data.
**Verdict: ACCEPT-WITH-FIXES.** Theorem A survives; the positivity target remains INCONCLUSIVE. ES is OPEN.
The contribution is an alternative square-sensitive surrogate and proof, not a new reduction of the missing positivity statement.

## Per-claim audit

| Claim | Classification | Independent check / qualification |
|---|---|---|
| Lemma 1.1, five bijections | CORRECT | Expand the product; invert by `u=(d+1)/(4C)`, `B=(N_C/d+1)/(4C)`. In (e), `0<u<d` forces the unique residue; `d∤n` is essential. The implicit bound is `d≤(4n+1)/3`. These forms are prior. |
| Remark 1.2, regular/HJ fractions and count | CORRECT | The displayed Euclidean divisions give the stated words, including the merged final digit at `u=2`. `u=B=1` is impossible for odd n, so the two boundary counts are disjoint. Replayed all `n≡1 (4), 5≤n<3000`: zero mismatches. CF dictionary is prior. |
| Lemma 1.3, reciprocity, square obstruction, coset size | CORRECT | `(-nC/d)=1`, reciprocity and coprimality give `(d/n)=(-C/d)`; the target has symbol −1. The character modulo `4C` is nontrivial already because its value at −1 is −1. No primality is needed for the coset-size assertion. |
| Proposition 2.1, local obstruction and Λ lower bound | CORRECT | All three congruences miss `n≡1`; Dirichlet supplies primes. `log L_U=O(U²)` and Linnik give `log p_U=O(U²)`. Also `p_U≥840L_U+1→∞`, supplying infinitely many distinct primes. Scope is two uniformly bounded coordinates. |
| Data 2.2's exclusion of Λ≤2 on 𝔐 | CORRECT | The divisor moduli are exactly 3, 7, 15; the other pair gives moduli 4, 8, 16. The listed Mordell congruences exclude all cases. |
| §3 pair correction, finite sum and exact split | CORRECT | A diagonal hit would have `n=4Cu²−2u` even, so every hit really has two distinct partners. `4C−1<√(4nC+1)` forces `C<(n+2)/4`; no infinite-tail issue. `E₂=R−M₂` makes the split tautological, not an error estimate. |
| Theorem A, including `c₀=1/300` eventually | CORRECT | All six steps checked below. It is a lower bound for this surrogate only; neither an asymptotic for R nor a bound on E₂ is proved. |
| §4(b), even-C main-term analogue | CORRECT | Substitute `C=2C′`, use `16X≤D≤√(2pX)`, modulus `8p`, CRT factor ≤4, and weight `4/φ(8C′)≥1/(4X)`. The same triangular collection of boxes gives a positive constant times `log²p`, not necessarily the same constant. |
| `R≥1 ⇔ E₂>−M₂` | CORRECT | Exactly equivalent because R is a nonnegative integer; Theorem A is not needed for this equivalence. This logical observation is prior in SYNTH Lemma 1.2. |
| §4 analytic/zero-sum limitations and §5 sieve heuristics | CORRECT-WITH-FIX | Honest as descriptions of failed attempts, not impossibility theorems. An odd-character kernel can avoid −1 for arbitrarily long multisets. Shifted-prime failure densities are heuristics, not pointwise or uniform lower bounds. Narrow the “all dead” heading and final exclusion language. |
| §6 “no per-C or per-parity argument … valid down to 10¹⁰” | GAP | F2 excludes an argument proving positivity of the **even subfamily** there. It does not exclude parity-dependent bounds whose sum proves full R positivity, or a successful odd-C contribution. The carefully qualified §4(b) does not imply this broader sentence. |
| Numerical summaries | CORRECT-WITH-FIX | Decisive values reproduced below; “40 000+” Jacobi pairs is false for the supplied run, and percentile convention should be stated. |

## Theorem A: proof and citation audit

1. The box inequalities give `4C−1<d<√N_C`, and each counted divisor has weight at least `1/(2X)`. Boxes are disjoint as pairs, including their half-open boundaries; different divisors at one C are supposed to add.
2. `8X≤D≤√(pX)` implies `X≤p/64`, `2D≤p/4`; odd d are units modulo `4p`. The C-window contains at most one representative of `−(4p)⁻¹ mod d`. The smaller fixed interval `I_j` is indeed contained in every moving interval in its block.
3. Reciprocal reciprocity has the correct sign: `−(4p)⁻¹/d ≡ d⁻¹/(4p)−1/(4pd)`. The perturbing factor's variation is ≤`4h/(pD)≤1` for the frequencies used.
4. CRT reduces to a factor ≤2 and prime Kloosterman/Salié sums. Here `1≤h<p`, so the inverse coefficient is nonzero even when k vanishes modulo p. The latter case is an elementary sum of size 1 or a Gauss sum of size √p. Thus completion and partial summation really give `O(√p log p)` uniformly on the blocks.
5. Odd QNRs have mass `ηD_j/4+O(√p log p)` by PV (subtract the even subsequence). ET with `H=ceil(p^(ε/4)D_j/X)≤D<p` gives block count at least `ηX(1−3η)/4−O(√p log²p)`. The extra margin `η²X≥p^(1/2+ε/2)` absorbs the error uniformly. Summing `K≈log(2)/η` blocks gives `S≥X/6` eventually; no unaccounted accumulation over blocks occurs.
6. The dyadic box count is ≥`(Λ−6)²/4`, hence `M₂≥(Λ−6)²/48`. At ε=0.1 the limiting natural-log coefficient is about 0.00694, strictly above 1/300. The threshold remains uncomputed. No estimate for E₂ is hidden in this argument.

Decisive external inputs checked against accessible sources, not just citation names:
- [Harcos, Theorem 1](https://www.renyi.hu/~gharcos/weil.pdf): prime-modulus Weil bound with both coefficients nonzero; the zero-coefficient case above completes the needed scope.
- [Kowalski, Salié evaluation](https://blogs.ethz.ch/kowalski/2010/03/07/the-computation-of-salie-sums/): at most two quadratic roots times a Gauss sum, hence `2√p`; again handle k=0 separately.
- [Martin–Sitar §2.4](https://www.math.ubc.ca/~gerg/papers/downloads/ETMTERRQDQ.pdf) quotes Montgomery Eq. (23): coefficient `2/(H+1)+min(|I|,2/(πh))≤3/h`, validating the exact ET version used.
- [Tao, Linnik Theorem 1](https://terrytao.wordpress.com/2015/02/22/254a-notes-7-linniks-theorem-on-primes-in-arithmetic-progressions/): a prime `≪q^O(1)` in every primitive progression, enough for Proposition 2.1. The prime Legendre character in PV is primitive and nonprincipal.

## Recomputations and falsifiers

All shell runs used `ulimit -v 4000000` and timeouts ≤1800 seconds; allocations were inspected first. No full-range factor sieve was attempted at the 10¹⁰ primes.
`z58_xrev_tryf2_audit.py` independently trial-divides eight small n with exact rational weights, replays 128 main-term output rows, and invokes inspected constant-memory three-region enumerators on every supplied F2/𝔊* prime.
The lane Λ sieve at 4·10⁶ is byte-identical; its subfamily sieve at 2·10⁶ reproduces every stated zero count. The repository zero sieve at 9·10⁶ reproduces the 14 primes and all 285 supplied composites.

| Screen / number | Result |
|---|---|
| F1 odd squares | Algebra gives `R=M₂=0`. Independent full-range checks at 841, 1225, 2209 agree. The nonprincipal-character step fails at squares, as stated. |
| F2 all 12 even-C zeros | Full enumerations reproduce **all** supplied `(R,R₈)` pairs, including R=18 at 10868474401 and R=56 at 10156800001. The four truncated rows at `C≤1500` match exactly: even M₂=11.085,15.607; odd `(R,M₂)=(10,17.057),(38,36.571)`. The finite threshold warning is correct; eventual even-C positivity is not refuted. |
| F3 all 285 non-square composite zeros | Exact list agreement through 7999801. Independent `M₂(57)=M₂(105)=0`; `M₂(2305)=2.249605554…` (2.25 is rounded). No uniform composite theorem is established or needed. |
| F4 full-family zeros | All 14 checked as zeros; all 14 truncated M₂ rows match, ranging from 1.067 to 16.444. Independently `M₂(409)=57121/25520`, `M₂(577)=322807/223860` on the full range. |
| F4 𝔊*-zeros — OMITTED by memo | All 38 supplied primes have `R_𝔊*=0`; 14 also have R=0 and **24 have R>0**. Examples: `R(37)=2`, `R(1621)=4`, `R(564661441)=2`. Thus the full-family theorem is not contradicted; it supplies no restricted 𝔊* theorem. Add this explicit entry, not an undifferentiated “F4 passed”. |
| Λ census | 141502 primes, 87.5747% with Λ≤2, 769 with `20≤Λ<255`. Independent uncapped enumeration at 1426489 finds only `(3,356,334)` and its mirror: Λ=334. |
| 90-prime main-term sample | All 90 rows match: R min/median=4/22; M₂ min/median/max=10.403/17.062/39.745; E₂/M₂ min/median/max=−0.626/0.1935/1.625. Memo q10/q90 agree with **lower empirical order statistics**, not interpolated quantiles. |
| Jacobi script | Zero failures in 34709 pairs, including a duplicated n=1225 run; only **32374 distinct pairs** for the listed twelve n, not “40 000+”. |

These reruns verify the supplied falsifiers, not exhaustiveness of the 10¹⁰ interval censuses. Those remain inherited certificates.

## Novelty against the repository

`git grep Z56_FAMTRY`, `Z57_SYNTH`, `Z57_BFII` and the cited passages establish:
- **Prior:** all five elementary hit faces and their bijections (`Z56_FAMTRY` Lemmas 1.1–1.4; `Z57_SYNTH` A.1); Jacobi/square obstruction; fixed finite solvable-class covering obstruction (`FAMTRY` Prop. 2.2); QNR supply not forcing the exact residue (`FAMTRY` §4.2).
- **Prior:** the exact “main term + remainder; positivity iff remainder > −main term” architecture (`SYNTH` Lemma 1.2), C-even/numerator-8 identity and these twelve counterexamples (`SYNTH` §2.1), and separation of full R from 𝔊* (`SYNTH` ladder).
- **Prior:** pointwise square-sensitive `log²p` main-term lower bounds (`Z56_FAMDESIGN` Theorem V, discussed in `SYNTH`); `Z57_BFII` Theorem G already gives a `log³p` genus term for the larger Type II family while explicitly leaving its remainder uncontrolled. M₂ is a different surrogate: no comparison showing improvement over those genus terms is proved.
- **Also prior:** the regular/HJ CF dictionary (`Z53_HYP2CYCLE` §3, with k=4C; `Z55_CROSSU` Lemma B). `Z52_BANKED` Cor. 1(f) already records a stronger infinite-prime median obstruction for certifying words `(t,u,v)`. A (★) hit has `t=4C`; `med(4C,u,B)≤4 med(C,u,B)`, so that recorded obstruction applies here too. Proposition 2.1 is a simpler reproof, not a new nonlocality barrier.
- **Incremental:** the particular cutoff/pair-corrected `M₂=Σ4m₂,C/φ(4C)`, its reciprocal-Kloosterman/Salié box proof, and these Λ/M₂ diagnostics. I found no identical construction in the named prior memos; this is not a claim of literature novelty. The generalized C-divisor Jacobi identity is useful packaging of the existing reciprocity obstruction.

## Required fixes, priority order

1. Replace §6's blanket per-C/per-parity exclusion by: “any argument that also proves even-C positivity at all primes ≥10¹⁰ is false”; retain the explicit transfer hypothesis and threshold qualification from §4(b).
2. Complete F4 with all 38 𝔊*-zeros and the full/restricted distinction above. Do not transfer Theorem A to a restricted family without defining its surrogate and checking the new cutoffs.
3. Add the prior-attribution paragraph; describe the result as an alternative main-term proof/diagnostic. Restrict “polynomial identities impossible” to a fixed finite menu covering all target primes, and “all dead” to the attempted implementations. No general sieve, CF, fixed-u or analytic impossibility follows.
4. Correct the Jacobi pair count and state the quantile convention. Keep M₂ decimals marked approximate and distinguish full from truncated sums (the 102001 row is already footnoted).
5. Explicitly record the no-diagonal parity argument in §3. Call M₂ a model/surrogate main term: equidistribution in the coset and a small E₂ are not proved; “roughly centred” is sample evidence only.

After these fixes: accept Theorem A and the diagnostics, but record **no progress on the required pointwise remainder bound** and no HOT LEAD.
