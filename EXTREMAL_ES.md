# The closest nonexact ES triple need not admit a monotone repair

Result: for n ≡ 1 (mod 24) with no prime factor 3 (mod 4), the closest nonexact three-term approximation of 4/n is unique and explicit (the strict-greedy triple). A monotone repair must be a single move through X or Y. At n=73 both gates are closed, and the min-max error of any repair path is about 4591× the optimum (exactly 148665133/32382).   Label: PROVED (§1–§2); CERTIFIED (§3, exact rational enumeration)
Scope: only the extremal nonexact seed and moves that keep a denominator. Nothing about solvability of ES, and no universal climb bound.
Review: cross-lab (Opus) `data/z74/xreview/REVIEW_Z72PHASE_OPUS.md` (P8–P11 CORRECT)
Triage: METHOD-CX
STATUS delta: none
*(§0 block: z74 Opus xreview fix)*

**PROVED:** For every prime `n ≡ 1 (mod 24)`, the unique closest *nonexact* three-unit-fraction approximation to `4/n` (absolute error, repetitions allowed, up to permutation) is explicit. In particular its error is strictly smaller than that of every other nonexact triple, from either side. Only two denominator fibres can possibly repair it; both can fail. **CERTIFIED:** the first trap for this rule is `n = 73`, where the least possible peak error on a path to any solution is about 4591 times the starting error. ES remains open.

Fix `n ≥ 2`. Write a sorted triple as `u = (x,y,z)`, and put

    E(u) = |4/n − 1/x − 1/y − 1/z|.

One **move** retains at least one denominator (possibly in a different sorted position) and allows the other two to change by arbitrary amounts. Thus a failure applies also to moves changing only one denominator or only refactoring a pair. We allow arbitrary paths, not just one-step tests. No assertion about moves changing all three denominators, or about monotonicity in other energies, follows. Unlike a walk starting from an exact solution, the starting triple below needs no witness. The optimum is over nonexact triples only: its calculation does not decide ES.

## 1. A uniform extremal inequality (PROVED)

Let `n ≡ 1 (mod 24)`, `n ≥ 25`, with `4/n` **not** expressible in two positive unit fractions. This last hypothesis holds if and only if `n` has no prime factor `3 (mod 4)`: the two-term factorization is `(4x−n)(4y−n)=n²`, with both factors positive and `3 (mod 4)`. Conversely any such prime divisor and its complement give a split.

Set

    X = (n+3)/4,  B₀ = nX,  Y = (B₀+2)/3,  T = B₀Y,  Z = (T+1)/2.

Here `X ≡ 1 (mod 6)`, `B₀ ≡ 1 (mod 6)`, and `Y,T` are odd. The remainders after `1/X` and `1/X+1/Y` are `3/B₀` and `2/T`, respectively. Hence `(X,Y,Z)` is an underapproximation with error `e₀ = 1/(TZ)`. *(z74 Opus xreview fix: `X=⌊n/4⌋+1`, `Y=⌊B₀/3⌋+1`, `Z=⌊T/2⌋+1`, so `(X,Y,Z)` is exactly the strict-greedy (Fibonacci–Sylvester) 3-term underapproximation. The theorem says that here greedy is optimal from both sides. Related literature on best Egyptian underapproximations: V. Kovač, J. Number Theory (2025), and Kovač–Tang, arXiv:2607.28387, on eventually greedy best underapproximations of every rational. Neither appears to contain this explicit two-sided 3-term statement, but no full search was done, so no priority is claimed.)* **Theorem:** every other nonexact sorted triple has strictly greater error.

*Proof.* Suppose `E(x,y,z) ≤ e₀`. Since `T > n⁴/48`, we have `e₀ < 2/T² < 1/(3n⁴)` for `n ≥ 25`. If `x ≤ n/4` then `1/x−4/n ≥ 1/(nx)` (odd `n`), which is too large. Also `3/x ≥ 4/n−e₀ > 3/n`, so `x<n`. Put `A=4x−n`, `B=nx`, `s=Ay−B`, `t=By`. As `A/B ≥ 1/n² > 3e₀`, we get `2/y ≥ A/B−e₀ > (2/3)A/B`, hence `y ≤ 3B/A`, `t ≤ 3n⁴`. If `s<0` the error exceeds `1/t > e₀`; `s=0` is excluded by the two-term hypothesis. Thus `1 ≤ s ≤ 2B`, and the last target is `s/t`.

For any positive `z` with `s/t ≠ 1/z`,

    |s/t − 1/z| ≥ 1/[t(t/s + 1)].                                 (1)

For `z ≤ t/s+1` use `|sz−t| ≥ 1`; for larger `z` the difference is increasing and at the real boundary `z=t/s+1` it equals `s/[t(t/s+1)]`. So it suffices to show `t²/s+t < TZ` off the first pair `(X,Y)`.

Write `F(A)=(n+A)²/[A(n+3)²]`. Since `t=B(B+s)/A`, `T=B₀(B₀+2)/3`,

    t/T ≤ 3F(A)(1+s/B),
    t²/(sT²) ≤ 9F(A)² (1/s + 4/B).                                (2)

The last bound uses `s ≤ 2B`. Either `A=3` with `F=1/3`, or `7 ≤ A ≤ 3n` with `F ≤ 1/5`: indeed `(n+A)²/A` is convex in `A`, and the endpoint values of `F` are `((n+7)/(n+3))²/7` and `16n/[3(n+3)²]`, both `< 1/5` for `n ≥ 25`. In all cases `t/T ≤ 3` and `B>n²/4`. When `A≥7`, (2) gives

    (t²/s+t)/T² ≤ (9/25)(1+16/n²)+3/T < 1/2.

When `A=3`, `s ≡ 2 (mod 3)`; except at `y=Y` it is at least 5, giving the even smaller upper bound `1/5+16/n²+3/T < 1/2`. But `TZ > T²/2`. This proves the desired separation in (1). At `(X,Y)` the target is `2/T` for odd `T`; monotonicity on each side of `T/2` leaves the two adjacent integers, with `(T+1)/2` strictly closer in reciprocal error than `(T−1)/2`. ∎

## 2. Exactly which extremal triples admit a monotone move? (PROVED)

Under the hypotheses of §1, no exact triple contains `Z`. Indeed the bounds (2) apply to exact triples too, and their largest denominator is `z=t/s`. One always has `s ≠ 1`: `s=1` would give `n² ≡ −4 (mod A)` via `(4y−n)A = n²+4s`, impossible at a prime `3 (mod 4)` dividing `A ≡ 3 (mod 4)`. For `A≥7` this gives `z/T ≤ (3/5)(1/2+1/B) < 1/2`; for `A=3` an exact triple cannot have `s=2` since `T` is odd, and `z/T ≤ 1/5+1/B < 1/2`. Thus `z<Z`.

Since the optimum is unique, a non-increasing path from it can do nothing until it reaches zero in a single move. The following is an **if and only if** test for such a move:

* **Keep `X`:** `B₀` has a prime divisor `q ≡ 2 (mod 3)`. Indeed the required factor pair `(3y−B₀)(3z−B₀)=B₀²` has both factors `2 (mod 3)`; conversely take `q` and `B₀²/q`. For prime `n` this gate depends only on `X`.
* **Keep `Y`:** `(nY)²` has a positive divisor `d ≡ 2 (mod M)`, `M=4Y−n=(n²+8)/3`. Indeed `3Y=nX+2` gives `MX−nY=2`, so `nY ≡ −2 (mod M)` and `gcd(nY,M)=1` (`M` odd). For a split of `M/(nY)` the transformed pair must have product `(nY)²`; if one factor is `2 (mod M)` its complement is too. Explicitly, a divisor `d` passing the second test gives denominators `(d+nY)/M` and `((nY)²/d+nY)/M`; the same formula with `B₀,3` in place of `nY,M` works in the first test.

A convenient negative certificate for the second gate at a prime `n` is that `Y` itself is prime. Here `n<Y`, `M>Y` and `M>n`, and it suffices by complementation to check `d ≤ nY`: the only possibilities are `1,n,Y,n²,nY` (discard any too large). Neither of the first three equals 2, and the last two have residues `−8,−2` modulo `M>10`. For example both gates are closed at `73` (`X=19,Y=463`), and at `2521` (`X=631,Y=530251`); no unsolved prime-pattern assertion is used. The criterion is only for repairing this particular extremum, not for excluding solutions.

## 3. Smallest counterexample and sharp repair (CERTIFIED)

For `n=73`, the extremum is `(19,463,321091)`, of error `1/206198539471`. To repair it one must *increase* the error. The minimum, over all paths to any exact solution retaining a denominator at each step, of the maximum error visited is exactly `H=1/44913834`. An optimal path is

    (19,463,321091) → (19,514,4599) → (20,351,514) → (20,210,30660).

Its errors are `e₀, H, 1/131702220, 0`, respectively. For the lower bound the checker enumerates the **strict** band `E<H` (6,939 vertices) and floods the component from the extremum using *all* common-denominator edges; it contains no exact triple. Thus the factor `H/e₀ = 148665133/32382` is necessary even for a path of unbounded length, not just for the displayed path length. This is a repair for this prime, not a universal bound on a climb.

Minimality over `n ≥ 2` is restricted only by the definition of a closest nonexact triple. If `4/n` is a sum of two units, appending `1/z` gives arbitrarily small nonzero error, so there is no minimizer. This includes every even `n` (two copies of `1/(n/2)`) and every odd `n` with a divisor `d ≡ 3 (mod 4)`: for `n ≡ 1 (mod 4)` use the above factorization, and for `n ≡ 3 (mod 4)` use the factors `1,n²`. For the remaining `n<73` the checker starts with the greedy strict underapproximation (at each step take `floor(1/remainder)+1` as denominator). It enumerates its full closed error band and checks uniqueness of the closest nonexact triple and adjacency to a solution. The surviving `n` are `5,13,17,25,29,37,41,53,61,65`; each passes. Thus `73` is smallest for this extremal rule, not a counterexample to ES.

**Enumeration justification (PROVED):** for an error cap `h`, residual `r` and `k` terms left with least denominator `a`, `a ≤ k/(r−h)` when `r>h`. If `r ≤ −h` there is no completion. The script asserts `r>h` in *every* non-discarded one- or two-term suffix here, so no infinite fibre is truncated. The last denominator interval is `[1/(r+h),1/(r−h)]`, intersected with the ordering constraint. All ceilings, floors and error comparisons use exact rationals.

**Alternative energy (CERTIFIED):** clearing denominators gives the integer `D=4xyz−n(xy+yz+zx)`. In the entire `|D|≤1` graph the first trapped nonexact component is already at `n=17`: `(7,11,654)` and `(7,11,655)` (defects `−1,+1`). They remain trapped at cap 2, but `(7,11,655) → (9,11,30) → (5,30,510)` attains cap 3 and solves. The other endpoint can first move to `(7,11,655)`. For `h<n`, `|D|≤h` implies `4x>n` (otherwise `D≤−nx(y+z)`), `4x≤3n+h` by division by `yz`, `s>0` (otherwise `D=sz−By≤−n`), `Ay≤2B+h` by division by `z`. For each such pair the allowed `z` satisfy `|sz−By|≤h`; hence the finite search is exhaustive. This is a different extremum from §1: it need not minimize reciprocal error.

## 4. Falsifier checks and limits

| Screen | Result |
|---|---|
| F1 odd squares | **PROVED / CERTIFIED:** the result is for original ES, not (★). `n=25` satisfies §1 and the `X` gate opens through 5; `n=49` has an exact two-term split and no closest nonexact triple. |
| F2 C-even / numerator 8 | **CERTIFIED / scope:** at the listed numerator-8 zero `p=10156800001`, §1 applies to `4/p` and the `X` gate closes (`X=13·199·981523`, all primes `1 (mod 3)`). Estimate (1) is general, but the level `s=2` at `X` uses numerator 4; no numerator-8 or even-C solution is inferred. |
| F3 composites | **PROVED:** §1 uses no primality beyond excluding two-term splits. The gate is on `nX`, not just `X`, as `n=25` illustrates. |
| F4 known restricted zeros | **CERTIFIED:** at the (★)-zeros `409,577` the two gate outcomes are respectively `(false,false)` and `(true,false)`; `2521` gives `(false,false)`. Neither gate is a claim about all representations or a generative class map. |

Reproduce: `ulimit -v 1000000; timeout 60 uv run --no-sync python scripts/check_extremal_es.py`. Context: `FRONTIER.md` z70 I17 (moves on already good classes do not produce a first witness); `BRAINSTORM/z52_lit_unitfrac_cover.md` (eventual greedy approximation does not force three-term equality). Here the obstruction survives starting from a globally extremal *nonexact* seed and allowing two denominators to change arbitrarily. **Assessment:** §1 gives an exact inequality, but neither it nor the repair at 73 forces an exact triple for general `n`.
