# I3_DEEP_ASTRA — a prime-modulus sieve and three short-interval wedges

**Status: PARTIAL. Conjecture I3 and Erdős–Straus remain open.** All proofs here are internal and unrefereed. PROVED means proved below, relative to explicitly named classical theorems where indicated; CERTIFIED denotes only finite checks; Assessment denotes interpretation. No OAI manuscript hypothesis is used.

## 0. Results and limits

Let `I3(n)=#{(t,u,v)∈Z³ : t,u,v≥3, tuv−u−v=n}`, counting ordered endpoints.

* **PROVED, relative to Bombieri–Vinogradov, Brun–Titchmarsh and the large sieve (§3):**
  `#{3≤n≤N : I3(n)=0} ≪ N exp(−c√log N)` for an absolute c>0.
  This is an I3 result, not a new improvement to Vaughan's ES exponent 2/3. The direct prime-modulus detector has only log X aggregate class mass, versus Vaughan's log²X.
* **PROVED, elementary (§4):** uniformly for integers H≥3 and n≥H²,
  `Σ_{n<m≤n+H} I3(m) ≥ (3/2)H log²H − O(H log H)`.
  Thus arbitrarily slowly growing H is allowed, with log H, **not log n**, in the main term. At H=n^θ, 0<θ≤1/2, this gives `(3θ²/2−o(1))H log²n`. No pointwise lower bound follows.
* **PROVED, elementary (§2):** a single balanced cube `[B,2B)³` misses at least `(3/4−O(1/B))` of the integers in `[2B³,4B³)`, despite real solvability throughout that central range. A positive per-cube lower bound at every n is therefore false, not merely beyond Kloosterman technology. Also `I3(n)≪ε n^{1/3+ε}`, improving the elementary `n^{1/2+o(1)}` upper bound recorded in z48; this is divisor enumeration, not cancellation.
* **PROVED (§5):** for all-integer Haar density δ₃(H) of no word with both endpoints in [3,H],
  `exp(−(2+o(1))H) ≤ δ₃(H) ≪ exp(−c√log log H)`.
  The upper bound uses Siegel–Walfisz and is ineffective. An explicit finite Euler-product upper bound is also given. These bounds are far from proving the proposed `exp(−(log H)^{2+o(1)})` survival law.
* **CERTIFIED (§6):** independent factorization-based enumeration at every 3≤n≤100,000 reproduces all 111 zeros in that range; it also verifies I3(2,433,600)=0 separately. It does **not** recertify the entire 10⁹ census. All nine hard-prime controls have interior words.

**Assessment / novelty scope.** The infinite conclusions above strengthen the z48 I3 record (which supplies the main term, a census, and a trivial pointwise upper bound but no quantitative exceptional estimate or short-interval bound). They are modest applications of classical counting and sieving, not new general sieve technology or literature-priority claims. The missing pointwise step is still positivity of the full tied-class count at a prescribed n. The stronger uniform `c log²n` lower bound off a thin set is not proved; the short-interval alternative in the brief is obtained instead.

**Prior work not repeated.** `LOWERTAIL_DEEP_FABLE` §§4–7 supplies the free/interior split, main term `½log²n+O(log n)`, Dickson obstruction for bounded least endpoint, square-level depletion, and the 112-zero census. `LOWERTAIL_DEEP_ASTRA` §§2–4 supplies the exact local Fourier budget, pedestal and one-point large-sieve obstructions. `PARITY_AUDIT` §2 and `SINGLE_P_COUNT` supply the single-integer analytic ledger. Those results are cited, not re-proved here.

## 1. Normalization and the published benchmark

**PROVED / definition and exact identity.** Each representation is counted once by

`I3(n)=Σ_{t,u≥3; 3(tu−1)≤n+u} 1[tu−1 | n+u]`.

The principal additive-frequency sum in these coordinates is `½log²n+O(log n)` (z48). This is an all-integer density main term; it is **not** a pointwise asymptotic, and no prime-density constant is silently substituted. The endpoint swap produces two words unless u=v, which can occur at composite n.

**Published theorem, verified through a secondary mathematical source.** R. C. Vaughan, *On a problem of Erdős, Straus and Schinzel*, **Mathematika 17 (1970), 193–198**, DOI [10.1112/S0025579300002886](https://doi.org/10.1112/S0025579300002886), proves the ES exceptional estimate `E(N)≪N exp(−c(log N)^{2/3})`. Elsholtz–Tao, [arXiv:1107.1010](https://arxiv.org/abs/1107.1010), introduction p. 3 and reference [82], explicitly confirms both exponent and attribution. I re-extracted and read these passages from `sources/elsholtz-tao-1107.1010.pdf`; see the existing text `sources/lit2026/audit-elsholtz-tao-1107.1010.txt`. The original Vaughan paper remains inaccessible in the repository's lawful-access audit, `sources/vaughan-1970-access-log.md`. **I did not read its original proof.** The attempted fresh HTML retrieval returned an SVG description, not the paper, and is not used as evidence.

**Assessment / benchmark qualification.** Vaughan is the published benchmark documented here, not an assertion that the repository has no stronger internal claims. `paper/es-threequarter-note.tex` claims an internally reviewed 3/4 exponent for ES. Neither that theorem nor Vaughan automatically bounds I3 exceptions: their general Egyptian-fraction certificates need not be interior words. Conversely sign-free I3 positivity does not imply ES or ES₅. Section 3 constructs its own detector rather than transferring either bound without a witness map.

## 2. Pointwise attempt: balanced cubes, then the level average

### Theorem 2.1 — a balanced cube cannot cover every central integer

**PROVED.** Let B≥3 be an integer. Among integers `2B³≤n<4B³`, at most `B²(B+1)/2` have a word with all three coordinates in `[B,2B)`. In particular at least `(3/4−1/(4B))` of these integers have no such word.

*Proof.* There are B choices of t and B(B+1)/2 unordered pairs u≤v in the box. Each determines exactly one n. There are 2B³ integers in the displayed interval. This upper bound on the image proves the claim, regardless of additional collisions. For real feasibility, solve `s³−2s=n`; for B≥3 and `2B³≤n≤4B³`, its positive root lies strictly between B and 2B. Thus this is not a boundary-of-real-support phenomenon. ∎

**Assessment / what is actually ruled out.** This excludes a uniform positive lower bound supplied by this one balanced box; it does not exclude an n-adapted union of boxes, or positivity of the full count. The infinite empty-box inputs occur at arbitrarily large sizes. They are not asserted to be primes or I3 zeros.

**Exact analytic blocking step.** With `m=tu−1`, a balanced box count is

`C_B(n)=Σ_{(t,u)∈D_n} [1/m + (1/m)Σ_{h=1}^{m−1} e(h(n+u)/m)]`,

where `D_n={(t,u)∈[B,2B)² : B≤(n+u)/(tu−1)<2B}`. Its positive zero-frequency sum is O(1), since |D_n|≤B² and m≥B²−1. On the empty-box inputs of Theorem 2.1 the nonzero frequencies cancel it **exactly**. Thus dispersion cannot establish positivity uniformly for this box. To use many boxes one needs a joint one-sided estimate for their exact remainders, not a per-box estimate followed by summation. This is a sharper negative target test than merely noting that a power error exceeds a constant main term.

### Theorem 2.2 — the elementary pointwise upper bound improves

**PROVED.** For every ε>0, `I3(n)≪ε n^{1/3+ε}`.

*Proof.* For any interior word,

`n/(tuv)=1−1/(tv)−1/(tu)≥7/9`.

Hence at least one coordinate is ≤K=`⌊(9n/7)^{1/3}⌋`. Words with t≤K are at most `Σ_{t≤K} τ(tn+1)` by `(tu−1)(tv−1)=tn+1`. Words with u≤K are at most `Σ_{u≤K}τ(n+u)`, and the same holds for v. Dropping overlaps only increases the bound. Apply the classical divisor bound, adjusting its ε for `tn+1≪n^{4/3}`. ∎

**Assessment.** This bounds `|I3−M|` by a power without proving cancellation or a lower bound. It should not be advertised as a new class-aware exponential-sum estimate.

### Second round: average divisor classes along {tn+1}

**PROVED bookkeeping.** At a fixed level t≥3 its interior count is

`#{d | tn+1 : d≡−1 (mod t), 3t−1≤d≤(tn+1)/(3t−1)}`.

The cofactor automatically has the same class, but the class cannot be dropped. At T≈n^{1/3}, the class-free family `{tn+1:t≤T}` is an AP of modulus n and length nT. The sufficient Selberg–Hooley regime recorded in `PARITY_AUDIT` is `n≤(nT)^{2/3−ε}`, requiring roughly T>n^{1/2}, not the balanced T. Even in that longer regime it controls the total divisor sum, not the divisors `−1 mod t` whose modulus changes with the AP index.

**Assessment / stopping point.** Keeping the restriction produces exactly the coupled class average above. Removing it produces many non-certifying divisors. Neither step supplies a bilinear form with independent modulus and class variables to which the cited fixed-modulus bounds apply. The earlier kernel lemmas already exclude the termwise Fourier-shortening repair. No new pointwise estimate is claimed from this round. We therefore change the quantified target to exceptions in n, where prime-modulus sieve averaging is legitimate.

## 3. Exceptional integers: a direct I3 sieve

### Lemma 3.1 — prime-modulus interior classes

**PROVED.** For a prime q≥7 define

`D(q)={u : u|(q+1), 3≤u≤(q+1)/3}`,
`Ω(q)={−u mod q : u∈D(q)}`, `ρ(q)=|Ω(q)|`.

Then `ρ(q)=τ(q+1)−4`, and every n≥3q in a class Ω(q) has an interior word.

*Proof.* The four excluded divisors of the even number q+1 are `1,2,(q+1)/2,q+1`, distinct for q≥7. The retained divisors lie strictly between 0 and q, hence give distinct classes. Put `t=(q+1)/u≥3`, `v=(n+u)/q≥3`. Then `tu−1=q` and `(tu−1)v−u=n`. ∎

The prime q here is a **side modulus**, not n. This is an all-integer sieve, including nonunits n at other primes.

### Lemma 3.2 — the detector mass has order log X

**PROVED relative to Bombieri–Vinogradov and Brun–Titchmarsh.** For large X,

`c₁ log X ≤ A(X):=Σ_{√X<q≤X, q prime} ρ(q)/q ≤ c₂ log X`,

and `max_{√X<q≤X}ρ(q)/q=o(1)`.

*Proof.* First show `Σ_{x<q≤2x}ρ(q)≍x`.

For the lower bound retain divisors `3≤u≤x^{1/4}` of q+1; all are in D(q) once x is large. Bombieri–Vinogradov for π in the dyadic interval gives

`Σ_{u≤x^{1/4}} |π(2x;u,−1)−π(x;u,−1)−(Li(2x)−Li(x))/φ(u)| ≪_A x/log^A x`.

Thus the retained count is at least a constant times
`(x/log x)Σ_{3≤u≤x^{1/4}}1/φ(u) ≫x`.
The progression is reduced for every u; no primality assumption on u is used.

For the upper bound, divisor pairing gives
`τ(q+1)≤2Σ_{u≤√(2x+1)}1[u|q+1]`.
Brun–Titchmarsh (and the ordinary prime bound for u=1) gives
`π(2x;u,−1)≪x/(φ(u)log x)` in this range. Since `Σ_{u≤z}1/φ(u)≪log z`, the upper count is O(x).

Each full dyadic block inside (√X,X] consequently contributes between two positive constants to A(X). There are ≍log X blocks; the possible partial block affects only the upper constant. Finally `ρ(q)≤τ(q+1)≪ε q^ε`, so the maximum density tends to zero. ∎

### Theorem 3.3 — an exponential-square-root exceptional bound

**PROVED relative to the inputs in Lemma 3.2 and the large sieve.** For some absolute c>0,

`E₃(N):=#{3≤n≤N:I3(n)=0} ≪ N exp(−c√log N)`.

*Proof.* Use only primes `P=(√X,X]`. Apart from at most 3X initial integers, every exception avoids Ω(q) for every q∈P. The standard large-sieve bound for integers avoiding ρ(q)<q classes is

`#avoiders in an interval of length N ≤ (N+Q²)/S(Q)`,
`S(Q)=Σ_{d≤Q, d squarefree, p|d⇒p∈P} g(d)`,
`g(q)=ρ(q)/(q−ρ(q))`, with g multiplicative on squarefree integers.

For completeness the needed truncation is explicit. Write
`G=Π_{q∈P}(1+g(q))`, `s=1/log X`. Then

`(G−S(Q))/G ≤ Q^{−s} Π_q (1+g(q)q^s)/(1+g(q))`
`                 ≤ exp(−log Q/log X +(e−1)Σ_q g(q))`.

By Lemma 3.2, `Σg(q)≪log X` and
`log G=Σ−log(1−ρ(q)/q)≥A(X)≥c₁log X`.
Choose `Q=⌊√N⌋`, `X=exp(a√log N)` with a sufficiently small fixed positive constant. The tail ratio is <1/2 for large N, so
`S(Q)≥G/2≥(1/2)exp(c₁a√log N)`.
The sieve bound is then as claimed. The discarded `3X` is negligible compared to the asserted upper bound. ∎

**PROVED extension.** The same proof counts exceptions in any integer interval of length H lying above `3 exp(a√log H)`, with bound `≪H exp(−c√log H)`. This uses shift-uniformity of the ordinary large sieve, not primes in short intervals.

### What prevents 2/3, and what does or does not transfer?

**Assessment, scoped to this architecture.** For this direct detector, `A(X)≍log X`. The full Euler product is only `exp(Θ(log X))`, while its typical weighted product modulus has log-size Θ(log²X): every selected q has log q comparable to log X, and the mean number selected is Θ(log X). The displayed Rankin/large-sieve construction budgets `log Q≍log N`, hence uses `log X≍√log N`. This proves neither an optimality theorem for all sieves nor a barrier for all I3 arguments. It locates the exact cost of **this** proof. Vaughan's ES classes use ratios of factors in a three-factor decomposition, not just divisors u of q+1; their square-log aggregate mass does not come for free for I3.

**Attempted multiplier repair, not a theorem.** With `tu−1=kq`, fixing n mod k=c retains only divisors `u|(kq+1)` satisfying `u≡−c mod k`; if gcd(c,k)>1 there are none, since u is a unit mod k. Thus the unconditional prime-class lemma does not persist fibre by fibre when multipliers are added. One would need a uniform lower bound for the *distinct* retained classes and a distribution bound after conditioning on the small-prime part of n. No such estimate is established here. Simply summing `τ(kq+1)` ignores both this zero-fibre issue and collisions, so it cannot justify an improved exponent.

**PROVED / limited ES transfer.** If instead `q=4Cu−1`, choose primes q≡3 mod4 and divisors `u≥3` of `(q+1)/4`. The same proof works: its lower mass uses primes `q≡−1 mod4u`, `u≤x^{1/4}`, and BV; its upper mass is bounded by Lemma 3.2. Hits give t=4C and hence explicit ES certificates. Thus the square-root-log bound also holds for failure of this interior star subfamily. It is **weaker** than Vaughan, not an ES or ES₅ improvement. Odd squares may all survive this sieve; `√N` exceptions are fully consistent with `N exp(−c√log N)`.

**PROVED / numerator-8 control.** Replacing 4 by fixed 8 in the preceding paragraph gives the same weak exceptional estimate with q≡7 mod8 and `u|(q+1)/8`. It makes no assertion at n=17 or 241, and no assertion that the exceptional set is empty. The word identity needs **8|t**, not just an arbitrary interior word, to certify 8/n in this subfamily. No numerator-blind existence claim is used.

## 4. Uniform short-interval lower bound: keep three disjoint wedges

This is an alternative to a pointwise `c log²n` lower bound outside a thin set. It uses no sieve or character cancellation.

Define, for real Y≥3,

`P(Y)={(a,b):a,b≥3, ab≤Y}`, `K(Y)=|P(Y)|`,
`S₀(Y)=Σ_{P(Y)}1/(ab)`, `S₁(Y)=Σ_{P(Y)}1/(ab−1)`.

### Theorem 4.1 — an exact finite inequality

**PROVED.** For positive integers H,n and Y≥3 satisfying `n≥3Y` and `n>Y²/3`,

`Σ_{n<m≤n+H} I3(m) ≥ H(S₀(Y)+2S₁(Y))−3K(Y)`.

*Proof.* Retain the three sets of interior words defined respectively by `uv≤Y`, `tu≤Y`, `tv≤Y`. For fixed (u,v) in the first set, the represented integers form the AP `m≡−u−v mod uv`; all members of our interval correspond to t≥3 because its onset `3uv−u−v≤3Y≤n`. Its count is at least `H/(uv)−1`. For fixed (t,u) in the second set the AP is `m≡−u mod tu−1`, with onset `3(tu−1)−u≤3Y`; it contributes at least `H/(tu−1)−1`. The third set is symmetric.

These sets are pairwise disjoint over this interval. If, for example, tu≤Y and uv≤Y, then `tuv≤Y²/u≤Y²/3`, whence `m=tuv−u−v<Y²/3<n`. The other two overlaps have the identical product bound with the shared coordinate t or v. Sum the three AP lower bounds. ∎

### Corollary 4.2 — arbitrarily short growing intervals

**PROVED.** Uniformly for integers H≥3 and n≥H²,

`Σ_{n<m≤n+H} I3(m) ≥ (3/2)H log²H − O(H log H)`.

*Proof.* Set Y=H. Elementary harmonic summation gives
`K(Y)=O(Y log Y)` and `S₀(Y)=½log²Y+O(log Y)`.
Moreover
`0≤S₁(Y)−S₀(Y)=Σ_{P(Y)}1/[ab(ab−1)]=O(1)`
by comparison with `Σ_{a,b≥3}a^{−2}b^{−2}`. Insert these into Theorem 4.1. ∎

**Assessment / scope.** The factor 3 is not double counting: the three pairs of small coordinates cannot coexist at n≥H². This improves the one-wedge `½H log²H` lower bound. The statement is useful quantitatively for large H; positivity somewhere in a fixed-length interval is already trivial from the AP with u=v=3, so that is not claimed as progress. For polylog H the conclusion involves `(log log n)²`, not `log²n`. It gives no almost-all individual `c log²n` lower bound: the sum can be concentrated on a few integers. Nor does it prove either endpoint is small at a given n; two of the three wedges allow one endpoint to be very large.

## 5. CRT/sieve model with both endpoints bounded

Use **all-integer Haar**, not the prime-unit Haar model for H₄. The distinction matters at noncoprime endpoints and at diagonals.

For integer H≥3 let `L_H=lcm(1,…,H)`, `Q_H=L_H²`. For n≥3H², an interior word with 3≤u,v≤H exists exactly when

`n≡−u−v (mod uv)` for some such pair.

Thus avoidance is eventually periodic, and its ordinary natural density δ₃(H) is exactly the avoiding fraction modulo Q_H. Independent uniform prime-power residues give precisely this same probability; independence of the *word events* is not asserted.

### Proposition 5.1 — finite bounds and mean

**PROVED.** For every H≥3,

`δ₃(H)≥1/Q_H>0`,

and the expected unordered word count is

`μ_H=½[(Σ_{u=3}^H 1/u)²+Σ_{u=3}^H 1/u²]=½log²H+O(log H)`.

For any fixed y≥3 with H>y, let `P_y=Π_{3≤r≤y, r prime}r`. For `a mod P_y`, a≠0, let r(a) be the least prime factor r of P_y with r∤a. Then the explicit upper bound is

`δ₃(H) ≤ 1/P_y + (1/P_y)Σ_{a=1}^{P_y−1} Π_{y<q≤H, q prime, q≡−a mod r(a)}(1−1/q)`.

*Proof.* The residue 0 modulo Q_H avoids every pair, since `0<u+v<uv` for u,v≥3; so does residue 1, though only one is needed. Each unordered pair has Haar hit probability 1/(uv), including u=v, proving the mean.

Condition on n≡a mod P_y. When r=r(a) exists, restrict to pairs (r,q) with q>y prime, q≤H, q≡−a mod r. The mod-r part of the pair event is then automatic. The remaining part is `n≡−r mod q`, of probability 1/q, independently for distinct q and independently of n mod P_y. Avoiding all words implies avoiding this subfamily. The single class a=0 is bounded trivially. Average over a. ∎

**PROVED consequences.** PNT in each fixed progression gives, for fixed y,

`δ₃(H)≤1/P_y+O_y((log H)^{−1/(y−1)})`.

In particular δ₃(H)→0: first send H→∞ and then y→∞. The lower bound and the prime number theorem give `δ₃(H)≥exp(−(2+o(1))H)`.

### Proposition 5.2 — a weak uniform decay rate

**PROVED relative to Siegel–Walfisz and PNT; ineffective.** For some c>0,

`δ₃(H)≪exp(−c√log log H)`.

*Proof.* Put `L=log log H`, `y=√L`, `z=exp(y⁴)`. For all large H, y<z<H. Siegel–Walfisz, uniformly for prime r≤y and units b mod r, followed by partial summation gives

`Σ_{z<q≤H, q≡b mod r}1/q = (log log H−log log z)/(r−1)+o(1)`.

Here one can use its usual error `O(x exp(−c₀√log x))` for moduli ≤log x: r≤y≤log z, and the integrated error above z tends to zero uniformly. Since `log log z=4log y=2log L`, the main term is at least `(1−o(1))√L`. Every product in Proposition 5.1 is consequently at most `exp(−(1−o(1))√L)`, even using only primes q>z. Also `log P_y=(1+o(1))y` by PNT. Insert these two bounds; no enumeration of the exponentially many classes a is needed. ∎

**Assessment / exact missing survival-law step.** These upper and lower bounds are enormously separated. The mean `μ_H∼½log²H` does not prove `−log δ₃(H)∼μ_H`, nor its exponent 2. Pair events sharing a prime divisor of an endpoint are dependent; pairs sharing an endpoint are especially correlated. The proof uses only independent auxiliary primes after conditioning on a small endpoint. Reaching log-square decay would require a quantitative joint avoidance estimate for the full overlapping family, not another mean calculation. No Janson/Poisson assumption is used, and the parent's prime-Haar calibration is not promoted to an all-integer theorem.

## 6. Exact checks and controls

**CERTIFIED, finite scope.** `scripts/z49_i3astra_census.c` factors each n+u for `3≤u≤(1+√(1+3n))/3`, enumerates its divisors A, and checks `A≥3u−1`, `A≡−1 mod u`, `(n+u)/A≥u`. The endpoint symmetry supplies multiplicity two except on the diagonal. This is independent of z48's progression sieve over endpoint pairs. It reproduces **111 zeros on [3,100000]**, last 36078; the list agrees exactly with the restriction of `data/z48_ltfable/big_1e9.txt`. The remaining known zero 2433600 is checked individually. No assertion about the intervening unswept range is made by this verification.

`z49_i3astra_verify.py` additionally performs direct triple enumeration, checks all 498 counts at n=3,…,500, checks the factor identity and product bound on all enumerated words through 3000, checks 152 exact short-interval inequalities (including wedge disjointness), and constructs 2566 prime-modulus witnesses. It enumerates the complete CRT period for H=3,…,7 and checks central balanced cubes for B=5,10,20,40. No floating-point equality is used. Results: `data/z49_i3astra/checks.json`; raw census: `census.txt`.

| n | 193 | 409 | 577 | 2521 | 3361 | 5569 | 9601 | 66529 | 8813281 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| I3(n), ordered | 4 | 4 | 12 | 4 | 12 | 20 | 18 | 30 | 84 |

**Square control, CERTIFIED and structural.** I3(49)=I3(1225)=I3(1600)=I3(19600)=I3(2433600)=0, but I3(121)=2. Thus no square-exactness is assumed for I3. The z48 square-level depletion remains in force; the unrestricted sieve uses other levels. The ES-slot variant in §3 may miss every odd square without violating its exceptional estimate.

**Numerator-8 control.** I3(17)=0 and I3(241)=2; the latter words are `(9,4,7)` and its endpoint swap. They have t=9, so the t-divisibility identity supplies no 8/241 solution. The independently established numerator-8 failures at 17 and 241 (PR-B L9901 / existing tests) are not rerun as if they were new tests. None of the infinite conclusions here asserts pointwise ES or 8/n existence.

**CERTIFIED CRT examples (all integers, unordered pairs).**

| H | Q_H | avoiding residues | δ₃(H) |
|---:|---:|---:|---:|
| 3 | 36 | 32 | 8/9 |
| 4 | 144 | 108 | 3/4 |
| 5 | 3600 | 2207 | 2207/3600 |
| 6 | 3600 | 1699 | 1699/3600 |
| 7 | 176400 | 70807 | 70807/176400 |

Reproduction (under 50 MB for C; small bounded Python arrays):

```sh
ulimit -v 8000000
timeout 20 cc -O2 -Wall -Wextra -Werror scripts/z49_i3astra_census.c -o /tmp/z49_i3astra_census
timeout 180 /tmp/z49_i3astra_census 100000 > data/z49_i3astra/census.txt
timeout 120 uv run python scripts/z49_i3astra_verify.py
```

## 7. Final gap and review

**Assessment.** The full pointwise target survives every partial result: force a class hit in at least one of the growing family of levels or endpoint slices at one specified n. Balanced cubes individually cannot do this uniformly; combining them needs a joint one-sided estimate. The sieve averages over n and leaves an infinite-size allowable exceptional set. The short-interval theorem averages over m and cannot identify its successful members. The CRT estimate concerns eventual periodic densities, not a growing-H theorem at each n. No finite-check reduction of I3, ES, or ES₅ is obtained.

**Hostile internal review completed (fresh deep-mode subagent).** The reviewer independently inspected all five infinite results, the classical-input hypotheses, endpoint multiplicities, the ES/8 transfers, and the scripts/data. Verdict: **no fatal or major mathematical defect**. Its sole minor finding was that the balanced-box script asserted only the weaker ordered-triple bound; the existing assertion now checks the exact `B²(B+1)/2` bound of Theorem 2.1. Verification passes after this repair. Review session: `2026-10-28T21-52-52-051Z_01a18480-6f53-70b7-bfc8-e0d0e942bd82` (parent harness session archive). This remains internal review, not external refereeing.
