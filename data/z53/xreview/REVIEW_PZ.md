# Cross-model hostile review — PZ

**Verdict: ACCEPT-WITH-FIXES.** Theorem A survives independent re-derivation: the positive-proportion target is strengthened to density one. The full second moment of R is NOT proved. ES remains OPEN; nothing here forces a solution at any prescribed prime.
Reviewed `side-agent/z53-pz` at `cde92cff3d4ca0d3df5852dbf17094e1da2f41ff`, `Z53_PZ.md`, on 2026-11-01.
Scope: direct audit of every PROVED component, independent deep review of §§4–7, primary-source literature checks, and bounded numerical replication. Research findings and the independent proof review were checked by the reviewing agent before this verdict.

## Per-claim findings

| Claim | Classification | Independent finding / required qualification |
|---|---|---|
| §1, R injects into labelled Type II | CORRECT | Recover u=px/y, B=px/z, then C=x/(uB). For prime p, u,B,C<p, so p∤x. ET counts labelled, not sorted, triples. |
| Lemma 2.1, R≥2N | CORRECT | Swap u and B; the two sets are disjoint when p≥(Q+1)²/4. Their weights are at most one. No multiplicity loss. |
| Lemma 2.2 and mean asymptotic | CORRECT | Harmonic summation gives M≥log²Y/8 and M=log²Y/8+O(log Y); replacing 4uC by 4uC−1 changes the weighted sum by O(1). |
| Lemma 3.1, first moment | CORRECT | Residues −u are units; Cauchy–Schwarz with r(m)≤τ(m+1), trivial error ≤3X/φ(m), and BV gives error O(XL⁻⁹⁷⋅⁵), stronger than stated. |
| Lemma 3.2, second moment | CORRECT | CRT compatibility is u≡u′ mod gcd(m,m′); compatible residues are units modulo lcm. The multiplicity exponents 159,161,9,170 and final −15 check. |
| Lemma 4.1, character variance | CORRECT | φ(lcm)φ(gcd)=φ(m)φ(m′); unique primitive induction gives the identity with no missing conductor weights. Principal term is exactly M². |
| Lemma 4.2 and one-cell structure | CORRECT | Nonprincipal Parseval permits arbitrary centering; odd d gives u≡−r, C≡−(4r)⁻¹, exactly one cell. Even d contributes zero. |
| Lemmas 5.1–5.2 | CORRECT | Integral comparisons, empty progressions, J=0, Y<d², and representatives equal to d all work; see derivation below. |
| Proposition 6.1 / Corollary 6.2 | CORRECT | Denominator correction and spike sums are bounded correctly. a=5.017719170532, 256a=1284.536107656130<1285. A simpler stronger spike bound is available below. |
| Theorem A / §7 | CORRECT-WITH-FIX | κ=1/64 and C=6000 are valid. Write O(η⁻²XL⁻¹²), or O_η(XL⁻¹²), in Chebyshev and explicitly absorb it using the strict numerical margin. |
| §7 fixed reduced classes | CORRECT | Restrict the global exceptional set and use π(X;W,b)∼π(X)/φ(W), with W fixed. No uniformity in growing W follows. |
| §9.1 first-moment constant c₁ | CORRECT relative to quoted repo asymptotics | Three disjoint BV regions give c₁=3·(3/(2π²))·(1/2)²=9/(8π²). This is a proof sketch relying on the cited pair/trial main terms, not a proof of the full-mean constant. |
| §9.5 validity, injectivity, mean | CORRECT with the large-p cutoff understood | Use p≥(Q+1)²/4, hence a<p; gcd(a,b) divides p and is <p. Recover coprime a,b from y/z, then d=x/(ab), c=y/(adp). Dirichlet series ζ(1+s)³/ζ(2+2s) gives M_II∼log³Y/(4π²). |
| §8 variance data / §9.5 evidence | EVIDENCE, replicated in part | Exact rational Q=100 trial check and supplied-engine Q=3000 trial / Q=1000 Type-II reruns agree; details below. Finite data do not prove asymptotic lower variance bounds. |
| §§0,10 literature comparisons | CORRECT-WITH-FIX | ET's almost-all exponent is correctly reported. The claim that BOTH f_II and f have prime mean ≍log³ is not established by ET; only f_II has that proved order. |
| §§7,12 variance-rate “cannot” assertion | GAP as a rigorous limitation | V≪log³Q is proved; V≍log³Q is only numerical evidence. Downgrade the asserted impossibility of improving Chebyshev's rate, or prove V≫log³Q. |
| §9.2 upgrades; §9.5 Conjecture B | Honest Assessment / CONJECTURE | Neither the unweighted/pair upgrades nor the cross-c estimate is proved. Do not promote their constants or the cheap c≤log X sketch into theorem statements. |
| §§0,11,12 strengthened verdict / screens | CORRECT with wording fixes | Density-one lower multiplicity is genuinely stronger than positive proportion, but does not control the full count's upper tail or solve ES. |

## Re-derivation of the decisive estimates

Put L=log X, Q=X^(1/4)L^(−B₀/2), Y=(Q+1)/4. BV is needed for both moments of N, NOT for an untruncated second moment of R.
For ν(n)=#{(P,P′):lcm(m,m′)=n}, let ρ(n)=Σ_{m|n}r(m). Then ν²≤ρ⁴≤τ(n)³Σ_{m|n}τ(m+1)⁴.
Consequently Σ_{n≤Q²}ν(n)²/φ(n)≪L¹⁷⁰: Cauchy–Schwarz on τ(m+1)⁴τ(m)³ gives exponent (255+63)/2=159, and partial summation plus n/φ(n) costs at most two logarithms; the other factor costs nine.
Thus weighted BV error ≤(XL¹⁷⁰)^(1/2)(XL⁻²⁰⁰)^(1/2)=XL⁻¹⁵. All lcms satisfy lcm(m,m′)≤Q², within BV. Sharing a modulus or a large gcd creates no unaccounted multiplicity.

For Lemma 5.1, removing the first progression point leaves d⁻¹Σ_{j=1}^J(j+C₀/d)⁻¹; integral comparison gives error <2/d from d⁻¹log⁺(Z/d).
For Lemma 5.2, set λ=log⁺(Y/d²), δ=log(d/u₀). Separating the first C-point and applying this estimate yields H=H₁+H₂+H₃ with the memo's H₁,H₃ bounds.
The decreasing function g(t)=log(Y/(td))/t gives
`|H₂−Λ| ≤ (λ+δ)/(du₀) + (λδ+δ²/2+λ log 2)/d²`.
Using λ+δ≤log(4Y), δ≤log d gives exactly the claimed cell bound, including λ=0 and empty sums.
Next 0≤1/(4uC−1)−1/(4uC)≤1/(12u²C²); the displayed 1/3 envelope absorbs this correction. Squaring the four terms, summing the two unit permutations, and using Σ1/u₀²<ζ(2) yields Proposition 6.1.
**Optional simplification:** retain φ(d) in its spike term T, rather than bounding it by d:
`T ≤ Σ_{u,C≤Q}(uC)⁻² Σ_{d|4uC−1}φ(d) = Σ_{u,C≤Q}(4uC−1)/(uC)² ≤ 4(1+log Q)²`.
This uses Σ_{d|n}φ(d)=n and improves the bound; it is not needed to validate the memo's constants.

Since M≥log²Y/8, V/M²≤(256a+o(1))/L. Chebyshev at ηM/2 has leading coefficient 1024a=5138.144430624518 divided by η².
The moment error contributes O(η⁻²XL⁻¹²); π(√X)=o(π(X)/L). Both fit below 6000·π(X)/(η²L) for X≥X₀(η).
Outside these exceptions, `R≥2N≥(1−η/2)log²Y/4≥(1−η)L²/64≥(1−η)log²p/64`.
The coefficient is exactly 2·(1/8)·(1/4)²=1/64. X-dependent truncation causes no quantifier problem because the final bad-set condition depends only on p.

## Large-modulus tail and Paley–Zygmund

No upper estimate for the omitted tail is needed: R≥2N is pointwise for the retained large primes. The full second moment remains unproved, explicitly as acknowledged in §§1,9.1.
The original BV-first-moment + Brun–Titchmarsh/upper-bound-sieve full-second-moment route has NOT been completed; the theorem bypasses it, rather than repairing its tail.
Paley–Zygmund already applies to N: E(N²)=M²+V+o(M²), so P(N≥θM)≥(1−θ)²/(1+o(1)) for fixed 0<θ<1. Chebyshev gives the stronger density-one statement.
For §9.1, with H=X^(1/2)L⁻ᴮ the products `(4uC−1)(4BC−1)=4Cp+1` and `(4uB)(4uC−1)=4u(p+u)` establish disjointness for p>H²; symmetry gives the third comparison.
Subtracting p≤H² uses max-in-y BV (with exponent enlarged if necessary), not an unjustified pointwise count. The central triangle and full mean asymptotic remain unproved.
ET Remark 1.3 is an analogy for this obstacle, NOT a theorem that all divisor-sum methods fail or that the particular R-second moment is known impossible.

## Numerical checks

Every executed shell batch used `ulimit -v 2097152`, a CPU limit, and `timeout` for subprocesses. Existing pairwise engines were inspected before execution: O(Q+#family) storage, streamed quadratic time; no dense pair array.
`gcc -O2 .../z53_pz_exactV_trial.c -lm` followed by `trial 3000 1`: #family=5089, M=7.708021, V=10.887322, V/M²=0.183246; agrees with §8.
`gcc -O2 .../z53_pz_exactV_typeII.c -lm` followed by `typeII 1000`: #family=3914, M=13.043438, V=15.326990, V/M²=0.090089; agrees with §9.5.
Independent exact checker: `scripts/z53_xrev_pz_exact.py`, run with `timeout 90s uv run --no-project python` under the same limits.
At Q=11, direct averaging over all 120 units modulo 231 agrees EXACTLY with the CRT formula: M=185/231, V=21697/53361.
At Q=100, exact rational pair summation gives M=2.552337757, V=2.098849026, V/M²=0.322184698 (#family=87), agreeing with the floating-point table.
The window data, Q=30000 quadratic sum, 10¹⁰ zero census, and full Type-II Parseval table were not rerun; none is required for Theorem A or this verdict. These remain reported evidence, not independently recertified here.

## Sources, novelty, and required fixes (priority order)

1. **Correct §0's f-average claim:** ET Theorem 1.1 proves Σf_II(p)≍Xlog²X, but only Xlog²X≪Σf(p)≪Xlog²Xlog log X. The extra log log cannot be silently removed. [ET v6](https://arxiv.org/pdf/1107.1010v6), pp. 4–5, checked directly.
2. **Downgrade the rate-optimality assertions** in §7(i) and proposed §12(c) to evidence; the proof supplies only an upper variance bound. Keep both the full-second-moment and full-mean-constant claims explicitly unproved.
3. **Restrict novelty wording:** say “improves the verified ET almost-all lower bound”; do not assert a literature-wide priority result. [ET Theorem 1.8](https://arxiv.org/pdf/1107.1010v6), p. 7, gives (log p)^((log 3)/2−o(1)); [Elsholtz–Planitzer](https://arxiv.org/pdf/1805.02945v1), Theorems 3–4, improve density-one INTEGERS / infinitely many primes, not density-one primes. Both source texts checked. The unresolved Akaka lead prevents a priority conclusion.
4. **Scope ET Remark 1.3 accurately:** it concerns full f_I,f_II and “our methods”, not an impossibility theorem for R or all divisor-sum methods. Type-II parametrisation should cite Proposition 2.6 / equations (2.13)–(2.22), not Proposition 2.3 (Type I).
5. **Minor proof hygiene:** restore η-dependence and explicit error absorption in §7; state p≥(Q+1)²/4 before §9.5's a<p/injectivity argument. No change to Theorem A's constants is necessary.

BV source checked directly: [Tao, 254A Notes 3, Theorem 17](https://terrytao.wordpress.com/2015/01/10/254a-notes-3-the-large-sieve-and-the-bombieri-vinogradov-theorem/#bv-thm), with supremum over reduced residues and level X^(1/2)log⁻ᴮX. The π/max-in-y variant used here is standard; partial summation and enlarging B preserve the needed arbitrary logarithmic saving.
Repo comparison: `ES_CONNECTIONS_TODO.md` Z2362, `data/z52d/avenue/summary_P03.md`, and `BRAINSTORM/z52b_signature.md` propose the positive-proportion moment route; `BRAINSTORM/anal_moments_structured.md` suggests the 1/log variance rate empirically. They do not supply this truncated one-cell proof. `FRONTIER.md` §2.2 and `BM_CORRECTED_COUNT.md` supply normalisations, not a density-one theorem.
**Assessment:** genuine strengthening relative to the inspected repo and verified published benchmark; external priority remains unresolved. Accept the core theorem after the listed presentation fixes, not the unproved extensions or full-second-moment route.
