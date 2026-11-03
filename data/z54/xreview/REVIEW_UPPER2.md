# Z54 UPPER2 — independent hostile review

**Verdict: ACCEPT-WITH-FIXES.** No gap or counterexample found in the numbered PROVED results.
The pointwise target remains **inconclusive/open**, not dead; the computational range is strengthened.
The prime exceptional-set and obstruction results largely reprove existing repo results, sometimes more weakly.
ES remains open. Required fixes concern novelty and the scope/labels of methodological judgments.

Reviewed `side-agent/z54-upper2` at `2a630b1da865b50102220b3f925ef41ae9ec257a`,
`Z54_UPPER2.md` plus all five scripts and their data. Novelty baseline: repo HEAD `4bcd9b5`.
All shell invocations used a virtual-memory ulimit, CPU limit, and command timeouts; computations used ≤6,000,000 KB.

## Per-claim audit

| Claim | Classification | Independent derivation/check |
|---|---|---|
| Lemma 1.1 | CORRECT | Expand `(tu−1)v−u` and `(tu−1)(tv−1)=t(tuv−u−v)+1`; divide only by positive t. |
| Lemma 1.2 (R), HC minimum, x=4 criterion | CORRECT | U reconstructs `t=(d+1)/x`, `v=(n+x)/d`; T has cofactor `d*≡−1 (x)` and reconstructs both endpoints. Conversely choose the appropriate numerator. Divisor class 3 mod 4 occurs iff a prime factor has that class. |
| Coordinate bound in §1 | CORRECT | `t≤n+2`; for `t≥2`, `(t−1)u≤n+1`; for `t=1`, `(u−1)(v−1)=n+1`, with both factors positive. Symmetry bounds v. |
| Lemma 2.1 (J) | CORRECT | `gcd(x,d)=1` gives `gcd(n,d′)=1` in U and T. Both symbols reduce to `(−x/d′)`. For `4∣x`, d is odd, 3 mod 4; reciprocity gives `(x/d)=1`. For `x≡7 (8)`, reciprocity gives `(−x/d′)=(d′/x)=−1`, using `(2/x)=1`. No primality of n is needed. |
| Proposition 3.1(a–c) | CORRECT | Least C-coordinate is 3 or 4. The six words have `tx−1=3,7,20` or `t=x=4,7`; the stated congruences give integral positive cofactors. CRT gives exactly the six residual classes mod 840. |
| Lemma 4.1 | CORRECT | Use U with `d=q`; distinct multiples of 4 dividing q+1 differ by less than q. Thus `ω≤(q+1)/4≤q/2` for odd q. |
| Lemma 4.2 | CORRECT | Rankin bounds the omitted mass by `Q^(−1/log z)G(z)^e`; the hypothesis makes this ≤G/2. Nonnegative squarefree weights justify restriction to divisors of P(z). |
| Theorem 4.3 | CORRECT | Fixed-modulus Mertens gives `Σω/q=κ log log z+O_K(1)`; bounded `Σg²` gives `log G≥κ log log z−O_K(1)`. The chosen z yields `J≥G/2`, hence `S≪N(log log N/log N)^κ`; `κ≥K+1` gives the stated result. Small p add only O_K(1). |
| Theorem 4.4 | CORRECT | BT gives `log G=O(L₂²)` uniformly in the window. SW applies from `T_x=exp(x^(1/40))`; its integrated errors sum over x to a finite constant. Thus `Σω/q≥(19/20−o(1))L₂²`. The divisor bound makes `Σg²=O(1)` uniformly in N; Rankin and LS then give the advertised 0.8. |
| Corollary 4.5 | CORRECT | For `p>√N`, `(log p)³>(log N)³/8≥(log N)²` once `log N≥8`; the remaining primes contribute ≤√N. |
| §4 remarks, sieve ceiling | CORRECT within the stated sieve | `J(Q)≤G(Q)≤exp(O((log log N)²))` for a fixed polylog window and `Q≤N`; this limits this LS estimate, not arbitrary sieves. Odd squares provide the separate integer-survivor obstruction. |
| §6.1 equivalence (★) | CORRECT | Apply R and remove the already settled class 5 mod 8; this is equivalent to the HC target, not asserted equivalent to full ES. |
| Proposition 6.2 | CORRECT | Odd squares are 1 mod 8, while `(m²/d′)` cannot equal −1. Includes m=1 and does not need word coprimality. |
| Proposition 6.3(a) | CORRECT | `n≡1 (8L)` makes each odd-part Jacobi symbol +1, contradicting J. Dirichlet applies to the reduced class 1. |
| Proposition 6.3(b) | CORRECT | For `M=8 lcm(1,…,⌊y⌋)`, Linnik gives `p≡1 (M)`, `log p≤2L₀y` eventually. Every negative-symbol prime factor of d exceeds y. Also `p≥M+1→∞`, so infinitely many distinct p result. |
| §0/§6.5 implications to eventual ES | CORRECT | Finite HC supplies a coordinate certificate and hence ES; the forward implication alone is used. No finite computation settles an eventual assertion. |
| §5, §3 covering counts, §6.4 numbers | CORRECT in tested ranges | Full decisive reruns agree; details below. |
| §0 “cannot be expected”, §6.1 methodological prose | CORRECT-WITH-FIX | Label Assessment and scope the claims to the actual methods; neither ES being open nor the proved obstructions establishes impossibility of a future pointwise argument. |

Analytic detail checked: `log log z=L₂−2 log L₂−O(1)` in 4.4, while `log log T_x≤L₂/20`.
The summed main coefficient is at least `(L₂−log 2)(19L₂/20−2 log L₂−O(1))`.
The bound `ω(q)≤τ(q+1)≪(q+1)^(1/4)` gives a convergent majorant `Σq^(−3/2)` for `Σg²`.
Thus the reductions from 0.95 to 0.9 to 0.8 have genuine asymptotic slack; N₀ is correctly ineffective.

## Source checks

- LS: Kowalski, *The principle of the large sieve*, Theorem 5.2, pp. 16–17, explicitly gives `(N−1+L²)/H`, with squarefree H and factors `|Ω_q|/(q−|Ω_q|)`; the memo's weaker `N+Q²` is valid. Source opened: https://people.math.ethz.ch/~kowalski/principle-large-sieve.pdf
- BT: Maynard, *On the Brun–Titchmarsh theorem*, Theorem 1.1, p. 2, gives exactly `2x/(φ(q)log(x/q))` for x>q. Source opened: https://ora.ox.ac.uk/objects/uuid:f34a2af4-c36d-4f9b-bad7-016a7a989203/files/m22685a8edf2e5142a452f7a8fd0f6ea3
- SW: the exponential-error formulation for π, polylog modulus range, and ineffectivity agree with https://en.wikipedia.org/wiki/Siegel%E2%80%93Walfisz_theorem (opened). Independently, Evertse Theorem 7.10 supplies the polynomial-log error version, already sufficient here: with error `t/(log t)^B`, integration from T_x costs `O(x^((1−B)/40))`, summable for B>41.
- Linnik: Evertse Theorem 7.9 gives absolute c,L with `P(q,a)≤cq^L` for every reduced class; Theorem 7.10 records SW ineffectivity. Source opened: https://pub.math.leidenuniv.nl/~evertsejh/ant16-7.pdf

## Reproduction

Extracted the branch scripts/data under `/tmp/xrev_UPPER2`; compiled C with `gcc -O2` and ran Python via `uv run --with sympy`.
The commands/results below are reruns, not merely readings of submitted data.

- `hc 1000000000`: **byte-identical** to `hc_1e9.txt`; 25,423,491 primes; unique HC=64 at 21,841; ratio maximum 0.7196 at 5; zero target violations. All 21 histogram bins agree and sum to the prime count; no `NOHC` or anomaly output.
- `z54_upper2_lemmas.py 4000`: **byte-identical** to `lemmas_4000.txt`; 50,968 words / 0 R mismatches; 29,820 J pairs / 0 violations; 7,744 sieve constructions and 9,745 Mordell words / 0 failures; all tested squares have no certificate.
- `z54_upper2_cover.py`: `(m,X)=(105,100000),(1155,9241),(15015,120121)` reproduces uncovered counts **6/48, 38/480, 242/5760**, all QR inclusions and least-coordinate histograms, maximum covering x=71.
- `mu all 100000000`: **byte-identical** to the census portion of `mu.txt`; max 2320 at 58,649,809; mean exponent 0.0876; all record lines agree.
- `mu sample 10^k 100000`, k=10,12,14,16,18: **byte-identical** to all five submitted sample lines; maxima **693,1302,1524,576,635**. These remain EVIDENCE, not a universal bound.
- Independent SymPy divisor enumeration of every admissible x≤(log p)³ at the two key records: `p=21841: HC=64, μ=67`, μ-word `(327,1,67)`; `p=58649809: HC=4, μ=2320`, μ-word `(116,20,25291)`. Every reconstructed word was checked in the defining equation. The submitted factorization cross-check to 10⁶ was inspected but not rerun.

The HC scan's `NOHC` branch does not increment its violation counter; therefore that counter alone would not certify success.
This does not invalidate this run: no such line occurs, and the full histogram accounts for every prime.

## Novelty audit and required fixes (priority order)

1. **Major: add an explicit prior-results comparison to §0.** `git grep HC` and direct proof comparison show:
   - R, the coordinate bound, HC=3/4, and the precise missing pointwise statement are already in `Z53_UPPER.md` §§1–2, 5; the coordinate reformulation and HC criterion originate in `LOWERTAIL_ROUND2_FABLE.md` §§1.2, 3.1.
   - J for primes, finite-level avoidance, and the stronger-constant smooth-support/Linnik obstruction are already `Z53_UPPER.md` Lemma 3.1, Corollary 3.2, Proposition 3.3; `FOREST_DEEP_FABLE.md` §§3.1–3.2 contains earlier covering versions. The general-n Jacobi proof is useful packaging, not a new prime obstruction.
   - The **identical odd-square theorem** is already `LOWERTAIL_ROUND2_FABLE.md` §1.3, with a larger square census. Do not record Proposition 6.2 as new.
   - `Z53_UPPER.md` Theorem 4.2 already gives the fixed-window prime bound `N/(log N)^(1+2Σ1/φ(4k))`, stronger than 4.3 at the same window. Its Theorem 4.3 gives the polylog-window exponent `(1−ε)A`, stronger than the current 0.8 for primes: take A=2, ε=1/4 and split at √N to obtain an exponent 1.5 with the target `(log p)³`.
   - The present integer-survivor formulation is a modest scope/presentation change, not a new sieve mechanism: removing the zero residue from the old U+T sieve makes the old argument apply to these integers too. The current proof uses only U, losing strength.
   - The ≤10⁸ HC census is already Fable §3.2 and Z53 §6. Creditable additions here are the extension to 10⁹, the μ statistic/data, explicit covering tabulations and a self-contained reproof; Mordell's six residue classes themselves are classical and already in the repo.
2. **Scope/labels:** explicitly mark §0's “cannot be expected” and §6.1's “cannot even guarantee” / “exactly how far sieve upper bounds go” as Assessment. Say “no uniform pointwise argument is supplied”; distinguish eventual emptiness of the **prime** exception tail from impossible emptiness of the **integer** survivor set. Fixed-level tests alone are excluded; growing-level congruence arguments and prime-sensitive sieves are not.
3. **Minor reproducibility hardening:** a future census should fail nonzero or count failures on `NOHC` rather than report zero violations after silently excluding that p from the histogram. The present numerical claims need no correction.

**Final assessment:** accept the mathematics and verified computations after attribution/scope fixes.
Do not promote this as a new exceptional-set milestone or a kill of the HC target. It is principally an independent
confirmation of existing theory plus extended numerical evidence; the all-large-prime HC and ES problems remain open.
