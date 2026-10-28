# I3_DEEP_ASTRA — a prime-modulus sieve and three short-interval wedges

**Status: PARTIAL. Conjecture I3 and Erdős–Straus remain open.** All proofs here are internal and unrefereed. PROVED means proved below, relative to explicitly named classical theorems where indicated; CERTIFIED denotes only finite checks; Assessment denotes interpretation. No OAI manuscript hypothesis is used.

**Round-2 update:** §8 strengthens both Haar bounds, proves growing-endpoint avoiders among actual integers, and improves the all-integer exceptional estimate to a log-loss 2/3 exponent. Sections 0–7 retain the first-round record; their bounds are superseded where §8 says so.

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

## 8. Round 2 — quantitative survival, integer avoiders, and a stronger exceptional sieve

### 8.1 Outcomes and scope

Write `L=log H`. The following replace the first-round bounds, for sufficiently large H or N and absolute positive constants c,C:

* **PROVED (Haar):**
  `c L²/(log L)² ≤ −log δ₃(H) ≤ C L⁶/log L`.
  The lower estimate for `−log δ₃` uses a separated-endpoint atomic Janson argument; the upper estimate uses an adaptive asymmetric local lemma. The desired comparison with L² remains open.
* **PROVED (actual integers):** if `log x≥C L⁶/log L`, at least `x exp(−C L⁶/log L)` integers in `(x/2,x]` avoid every bounded-endpoint congruence. In particular, for each fixed `0<κ≤1/6`, this holds with `H=⌊exp((log x)^κ)⌋` for all sufficiently large x. These integers have **no interior word with both endpoints ≤H**, not necessarily no interior word at all.
* **PROVED (exceptional set):**
  `E₃(N) ≪ N exp(−c (log N)^{2/3}/(log log N)^{1/3})`.
  On prime inputs, the same construction gives `#{p≤N:I3(p)=0}≪N exp(−c(log N)^{2/3})`. No 3/4 exponent, or exact all-integer 2/3 exponent without the log loss, is established.
* **PROVED (a proposed transfer premise is false):** the raw factorial-moment bound `E binom(Z,j)≤(C E Z)^j/j!` does not hold uniformly for the bounded-endpoint events, even after fixing n=1 at all primes ≤`(log H)^A`, for fixed A>1. Explicit compatible divisor clusters violate it at `j=O(log log H)`. The actual-integer lower bound therefore uses an Efron–Stein/BRW minorant instead of this invalid Bonferroni premise.

**Dependencies.** The lower Haar argument is elementary apart from the classical asymmetric LLL. The integer lower bound uses the general product-space energy lemma proved in `POINTWISE_OMEGA10.md`, Corollaries 3.5/4.1, and the elementary BRW identity in `POINTWISE_OMEGA8.md`, Lemma 3.1; their proofs were inspected, and their general hypotheses are checked below. The upper Haar argument uses the atomic Janson lemma proved in `paper/es-subexp-note.tex`, Theorem “Janson-type inequality for atomic events”, not its ES-specific pair estimate. The exceptional bound uses BV, Brun–Titchmarsh and Mertens, adapting the conditional-CRT architecture of `paper/es-threequarter-note.tex` to a new, explicitly verified I3 atom family. These are internal proofs, not externally refereed theorems or literature-priority claims.

### 8.2 A uniform envelope for conditioning on the class of one

For `3≤u≤v≤H`, put `M=uv`, `a_E=−u−v`,

`g(u,v)=gcd(uv,u+v+1)`, `s_uv=g(u,v)/(uv)`.

Let Q divide `Q_H=lcm(1,…,H)²`, and condition on `n≡1 mod Q`. Put `D=gcd(M,Q)`. The event E survives iff `D|u+v+1`, and then its conditional probability is exactly `D/M`. Therefore, at **every stage** of further conditioning on the class of one,

`P_Q(E)≤s_uv`.                                                   (8.1)

This envelope controls the inflation caused by conditioning; the unconditional mean `½log²H` cannot simply be reused.

**Lemma 8.1 (PROVED).**

`S♯:=Σ_{3≤u≤v≤H}s_uv ≪ L⁴`.                                   (8.2)

*Proof.* The elementary valuation identity is

`g(u,v)=gcd(u,v+1) gcd(v,u+1)`.

A prime common to u,v divides neither side; a prime dividing only one endpoint gives the identity directly, including its exponent. Expanding `gcd(a,b)=Σ_{d|a,d|b}φ(d)`, fix `a|u`, `b|u+1`. Then `(a,b)=1`, and the eligible v satisfy `v≡−1 mod a`, `v≡0 mod b`. These form one progression modulo m=ab. Crucially, `m|u+v+1`. For its first member v_*≥u, this implies `m≤2v_*+1`. Hence, whenever the progression is nonempty,

`m Σ_{u≤v≤H, v≡−1(a), v≡0(b)}1/v ≤ m/v_*+log(H/v_*) ≤3+log(H/u)`.

Since `φ(a)φ(b)≤ab`,

`S♯ ≤ Σ_{u=3}^H [τ(u)τ(u+1)/u] [3+log(H/u)]`.

The elementary bound `Σ_{u≤X}τ(u)τ(u+1)≪X log²(2X)` follows by applying the divisor hyperbola inequality to both factors: small divisors d≤√X,e≤√(X+1) must be coprime, and their simultaneous congruences have at most `X/(de)+1` solutions. Sum these bounds, then use partial summation twice in the preceding display. ∎

**Lemma 8.2 (PROVED; fixed smooth conditioning).** If Q_Y contains the full powers from Q_H at every prime ≤Y, then the surviving conditional event mass satisfies

`S_Y≪L² log(2Y)`.                                               (8.3)

*Proof.* Write the exact Y-smooth parts of u,v as a,b. A surviving event requires `(a,b)=1`, `a|v+1`, `b|u+1`, and its probability is `ab/(uv)`. Fix u, hence a; sum over Y-smooth divisors b of u+1, dropping the requirement that b be the exact smooth part of v. The progression estimate in Lemma 8.1 gives

`S_Y≤Σ_{u=3}^H [τ_Y(u+1)/u][3+log(H/u)]`.

Here `τ_Y(m)` counts Y-smooth divisors. Writing u+1=kb and using `1/u≤2/(u+1)`,

`Σ_{u≤H}τ_Y(u+1)/u ≪ L Σ_{P⁺(b)≤Y}1/b ≪ L log(2Y)`

by Mertens' product theorem. ∎

**Assessment / the fixed-cutoff stopping point.** Equation (8.3) is not a per-prime bound. It does not show that every remaining prime has sufficiently small incident mass. The adaptive step below supplies exactly that missing inequality, rather than assuming it or invoking an unspecified distortion theorem.

### 8.3 Adaptive quarantine and the Haar lower bound

**Theorem 8.3 (PROVED).** `δ₃(H)≥exp(−C L⁶/log L)`.

*Proof.* Let `f_p=2⌊log H/log p⌋`. Start with `Q=Q_Y`, `Y=L²`, and subsequently write `Q=Π_{p≤H}p^{a_p}`, `0≤a_p≤f_p`. The initial cost is `log Q_Y≤2YL=O(L³)`. On the fibre n=1 mod Q, the independent remaining coordinates are the unrevealed p-adic digits. A surviving event has free support

`supp_Q(E)={p:v_p(uv)>a_p}`.

It never has empty support: otherwise `uv|u+v+1`, whereas `0<u+v+1<uv` for u,v≥3. Define

`w_p(Q)=Σ_{E surviving, p∈supp_Q(E)}P_Q(E)`.

Fix `c₀=1/16`. Whenever

`w_p(Q)>c₀(a_p+1)log p/(2L)`,                                (8.4)

increase a_p by one, fixing the next digit to that of 1. There are finitely many digits, so this terminates. At termination every surviving E satisfies

`Σ_{p∈supp_Q(E)}w_p(Q) ≤ [c₀/(2L)]Σ_{p|uv}v_p(uv)log p ≤c₀`.   (8.5)

To bound the cost, a step from a_p=j−1 to j obeys, by (8.1),

`log p < [2L/(c₀j)]w_p(Q) ≤ [2L/(c₀j)]Σ_{p^j|uv}s_uv`.

Each (p,j) is used at most once. With `h(m)=Σ_{p|m}H_{v_p(m)}`, this gives

`log Q≤log Q_Y+(2L/c₀)Σ_E s_E h(uv)`.

Uniformly for m≤H², `h(m)≪L/log L`: primes ≤√L contribute `O(√L log L)`; for larger primes use `H_e≤e` and `Σ e log p≤2L`. Lemma 8.1 now gives

`log Q≪L⁶/log L`.                                             (8.6)

Apply the ordinary dependency-graph LLL to the remaining cylinder events, joining events sharing a free prime. Set `x_E=2P_Q(E)`. Since each event has nonempty support, (8.5) implies `P_Q(E)≤c₀`, and its total neighbor x-mass is at most 2c₀. Thus

`Π_{E'∼E}(1−x_E') ≥ exp(−2c₀/(1−2c₀)) >1/2`,

which verifies the LLL inequalities. Writing `S=ΣP_Q(E)≤S♯`, its quantitative lower bound gives

`P_Q(no event)≥Π_E(1−2P_Q(E))≥exp(−3S)`.

The unconditional fibre has probability 1/Q. Combine this with (8.2) and (8.6). ∎

This argument allows adaptive extra primes and partial prime powers beyond Y. It does **not** prove that the original fixed smooth cutoff alone satisfies the LLL. The role of the class of one is structural: it is outside every event, so no pinning step can create an unavoidable event.

### 8.4 Almost log-square decay: the opposite Haar bound

**Theorem 8.4 (PROVED).** `δ₃(H)≤exp(−c L²/(log L)²)`.

*Proof.* Set `Y=L⁸`. Retain only endpoint pairs in

`H^{1/16}≤u≤H^{1/8}`, `H^{1/2}≤v≤H`,

with u,v squarefree, Y-rough, and coprime. Squarefreeness makes these atomic events on the coordinates n mod p. They are distinct: identical events would have the same modulus uv and residue, hence the same integer sum u+v because `0<u+v<uv`; the product and sum determine the unordered pair, and the separated ranges fix its orientation. Denote this family by F and its mean by μ.

**Mass.** In any fixed logarithmic interval `[H^α,H^β]`, α<β,

`Σ_{m squarefree, P⁻(m)>Y}1/m ≫ L/log Y`.

One may use the fundamental lemma. Alternatively, on each dyadic interval of length X≥H^α, truncate inclusion–exclusion over primes ≤Y at odd order `k=C log L`. The factorial tail `Σ_{j>k}(Σ_{p≤Y}1/p)^j/j!` is negligible relative to `1/log Y`, whereas the progression errors number at most `Y^{k+1}=exp(O((log L)²))=H^{o(1)}`. This gives ≫X/log Y rough integers. Removing multiples of p² for p>Y costs `O(X/Y+√X)`, which is negligible. Sum reciprocals over the dyadic intervals. The harmonic mass of pairs sharing a prime is at most

`Σ_{p>Y}[(1+L)/p]²≪L²/Y`.

It follows that `μ≫L²/(log Y)²`.

**Local loads.** For p>Y,

`w_p:=Σ_{E∈F, p|uv}1/(uv)≤2(1+L)²/p`.

Every event meets at most `2L/log Y` primes. Thus its total conflict-neighbor mass is `O(L³/(Y log Y))=o(1)`. The atomic Janson lemma cited above applies with `x_E=2P(E)` and inflation factor `K≤e^{1/3}`. It remains to bound the compatible-pair sum Δ; the following calculation is I3-specific.

**Shared modulus.** For a distinct compatible pair (u,v),(u',v'), define

`g=(u,u')`, `h=(v,v')`, `j=(u,v')`, `k=(v,u')`.

Squarefreeness and within-pair coprimality make these four numbers pairwise coprime. Write

`u=gja`, `v=hkb`, `u'=gkc`, `v'=hjd`, `D=(uv,u'v')=ghjk`.

Put the endpoints into dyadic intervals u≈U,v≈V,u'≈U',v'≈V', and orient the pair so V'≥V. If the sums differ, compatibility implies `D|u+v−u'−v'`, hence `D≤4V'`. If the sums agree, distinctness implies u≠u', and `h|u−u'`; consequently

`D=(gj)(gk)h/g≤uu'|u−u'|≤H^{3/8}≤V'`.

Thus in both cases `1<D≤4V'`. Endpoint separation is essential for this equal-sum case.

**Pair sum.** The four compatibility congruences are

`kb≡jd (g)`, `ja≡kc (h)`, `gc≡hb (j)`, `ga≡hd (k)`.

For fixed g,h,j,k,a,b, CRT puts c in one class modulo hj and d in one class modulo gk. Their dyadic harmonic sums are at most

`O(1/(hj)+gk/U')`, `O(1/(gk)+hj/V')`,

respectively. The harmonic sums over a,b in their dyadic ranges are O(1). Since the joint probability is `1/(Dabcd)`, a fixed quadruple g,h,j,k contributes at most

`O(1/D²+1/(DU')+1/(DV')+1/(U'V'))`.

There are `4^{ω(D)}` assignments of the prime factors of squarefree D to the quadruple. Use

`Σ_{D>1, squarefree, Y-rough}4^{ω(D)}/D²≪1/Y`,
`Σ_{D≤z}4^{ω(D)}/D≪(1+log z)⁴`,
`Σ_{D≤z}4^{ω(D)}≪z(1+log z)³`.

The last two follow from `4^{ω(D)}≤τ₄(D)`; the first follows from its convergent Euler product. Retaining the crucial cutoff D≤4V', each dyadic box contributes `O(Y^{-1}+L⁴H^{-1/16})`. There are O(L⁴) boxes, so

`Δ≪L⁴/Y+L⁸H^{-1/16}=o(1)`.                                  (8.7)

The atomic Janson inequality gives `−log P(Av(F))≥μ−KΔ≫L²/(log L)²`. Avoiding all interior pairs implies avoiding F, proving the theorem. ∎

**Assessment.** This obtains the requested upper-tail exponent `2−o(1)`, not a constant-factor comparison with L². Roughness removes a factor log Y from each endpoint harmonic sum; recovering those two factors while preserving the pair control is still open here. Ordinary monotone-event Janson cannot simply be cited for these categorical prime residues: incompatible assignments are negatively correlated. The explicitly checked atomic variant handles this through its conflict graph and the small local loads.

### 8.5 Why raw Bonferroni cluster bounds fail, even after smooth pinning

Let Z count all the unordered endpoint events, or all their surviving restrictions after n=1 mod Q_Y. Write `S_j=E binom(Z,j)` and `μ=EZ`.

**Proposition 8.5 (PROVED).** Fix A>1 and `Y=(log H)^A`. There is no absolute constant C (even depending on A) making

`S_j≤(Cμ)^j/j!`                                                (8.8)

hold for all sufficiently large H and all j, in the product law conditioned on n=1 mod Q_Y. It fails already at some `j=O(log log H)`.

*Proof.* Choose `k=⌊L/(2log(2Y))⌋` distinct primes `q_i∈(Y,2Y]`, all 2 mod3; PNT in this fixed progression supplies them. Put `P=Πq_i≤√H`, with `log P=(1/2+o(1))L`. Among its divisors, exactly `2^{k−1}` are 2 mod3. All are ≥3 and ≤H. For each such divisor v, the event with endpoints (3,v) is, on our fibre, exactly `n≡−3 mod v`: its mod-3 requirement n=1 is already satisfied. All these events occur simultaneously on `n≡−3 mod P`, of conditional probability 1/P. Put `M=2^{k−1}`. Then

`S_j≥P^{-1} binom(M,j)`.

Take `j=⌈4log P/(k log2)⌉=O(log L)`. Since j≪M,

`log S_j≥−log P+j(log M−log(2j))≥(3−o(1))log P`.

But Lemma 8.2 gives `μ≪L²log Y`, so the logarithm of the proposed right side of (8.8) is at most `O((log L)²)`, a contradiction. The family uses only rough primes beyond Y in its free support, so smooth pinning does not remove this cluster. ∎

**Assessment.** This disproves the stated **raw event** cluster hypothesis, not every cluster expansion with cancellations, resummed connected components, or pruning of logically redundant events. In particular, many large-divisor events in this cluster imply a smaller-divisor event; a carefully pruned Bonferroni approach is not ruled out. Nor does it contradict LLL: LLL controls avoidance, not high positive moments on extremely rare, densely occupied fibres. A direct raw Bonferroni transfer at degree comparable with μ cannot be justified using (8.8). The next subsection avoids that premise altogether.

### 8.6 Transfer of the lower bound to actual integers

**Theorem 8.6 (PROVED relative to the general energy lemma cited in §8.1).** For sufficiently large H, if `log x≥C L⁶/log L`, then

`#{x/2<n≤x: n∉E_uv for all 3≤u≤v≤H} ≥ x exp(−C L⁶/log L)`.

*Proof.* Work on the final fibre n=1 mod Q of Theorem 8.3. Its product coordinates are the unrevealed prime-power digits, grouped by prime; each alphabet has at most H² elements, and there are at most H coordinates. Every event has width

`k≤2L/log Y=O(L/log L)`,

since all primes ≤Y=L² are already fully pinned. Split each remaining cylinder into assignments of the **full** coordinate values on its support. This preserves F=`1[no event]`, the widths, and total mass `S≤CL⁴`. The number m of split events satisfies `m≤H²(H²)^k`, hence `log m=O(L²/log L)`. If m=0 the fibre itself gives the result directly.

The general energy lemma says that a good-indicator f of a width-k single-value system on any finite product probability space obeys

`Σ_{|U|>d} ||f^{=U}||₂² ≤2^{−(d+1)/k}`.                        (8.9)

It also applies to every prefix system after pinning an event. This is `POINTWISE_OMEGA10`, Corollary 4.1: the stronger generating-function inequality `Σ_U 2^{|U|/k}||f^{=U}||₂²≤1` follows there by polarization and the deletion–contraction bound for weighted hypergraphs. No ES parameters, unit-residue hypothesis, local loads, or alphabet-size bound enter that lemma.

For an ordering A₁,…,A_m of the split event indicators, let u_j be the degree-d Efron–Stein truncation of `Π_{i<j}(1−A_i)` after pinning A_j. The BRW polynomial is

`B=1−Σ_i A_i(1−Σ_{j<i}A_j u_j)²≤F` pointwise,

and its elementary sum-of-squares identity gives

`E(F−B)≤m² Σ_j P(A_j)2^{−(d+1)/k}`.

Choose

`d=O(k[S+log m+log(S+1)])=O(L⁵/log L)`

with a sufficiently large absolute constant. Since Theorem 8.3 gives `EF≥e^{−3S}`, this yields `EB≥0.99EF≥0.99e^{−3S}`.

We need **unweighted** absolute coefficients for integer counting. Expanding

`f^{=U}=Σ_{W⊆U}(−1)^{|U\W|}E(f|X_W)`

and each conditional expectation into coordinate cells gives an absolute coefficient sum `exp(O(dL))` for a truncation: there are at most H coordinates, each with at most H² values, and each cell coefficient has absolute value ≤1 before summing the truncations. Products of cells are empty or cells, so the BRW polynomial has a cell expansion with

`A(B):=Σ_i|b_i|≤exp(O(dL+log m))≤exp(O(L⁶/log L))`.             (8.10)

Intersect each cell with n=1 mod Q. It is one ordinary congruence class, with Haar density equal to `(1/Q)` times its conditional cell probability. Counting each class in `(x/2,x]` has error O(1), irrespective of its modulus. Therefore

`Σ_{x/2<n≤x, n≡1(Q)}B(n)=x(EB)/(2Q)+O(A(B))`.

Equations (8.6), (8.10) and the positive mean make the main term exceed twice the error when `log x≥C L⁶/log L` with C large enough. Since B≤F, the assertion follows after enlarging C. ∎

**PROVED corollary.** For each fixed `0<κ≤1/6`, put `H=⌊exp((log x)^κ)⌋`. Then `L⁶/log L=o(log x)`, so the theorem applies and supplies `x^{1−o(1)}` avoiders in `(x/2,x]`. Here n≥3H² eventually, so congruence avoidance is exactly absence of interior words with both endpoints ≤H. Thus infinitely many actual integers require a larger endpoint than `exp((log n)^κ)` in every interior word, if they have a word at all. This is an unconditional all-integer conclusion relative to the proved general product-space lemma, **not** a conclusion about primes or about I3 zeros.

### 8.7 Auditing Vaughan and the 3/4 note: a failed map and a working replacement

The note's basic certificate has

`M=4abw−1`, `nb+a=Ms`.

**PROVED obstruction to direct transfer.** Its immediate word is

`bn=(4bw)as−a−s`,

a word of **bn**, not n. Dividing by b would require the rational endpoints a/b and s/b at level `4b²w`. For the reduced pairs `(a,b)=1`, `s≡−a mod b`, so neither endpoint is integral when b>1. Taking b=1 restores words but loses the second factor-ratio parameter.

**CERTIFIED counterexample to the unrestricted witness map.** At

`n=6336`, `(a,b,w,M,s)=(3,5,3,179,177)`,

we have `180=4·3·5·3` and `5·6336+3=179·177`; this is a valid Vaughan identity, but I3(6336)=0 in the independently verified first-round census. The word is of 31680, not 6336. The residue needed for a same-modulus I3 endpoint is `−6336≡108 mod179`, and 108 does not divide 180. This tests the algebraic identity, not the note's later asymptotic atom cutoffs.

**PROVED obstruction to its all-denominator scaling step.** I3 is not upward-closed under multiplication: `21=3·3·3−3−3`, while I3(42)=0 (independent census). Thus the note's ES scaling/semigroup argument cannot promote an I3 prime-exception theorem to all integers. Both gaps must be repaired, not omitted.

Here is a replacement which keeps the conditional-CRT machinery but changes the atoms.

**Lemma 8.7 (PROVED relative to BV and Brun–Titchmarsh; uniform direct supply).** Put `T=log X`, `K=⌊X^{1/480}⌋`, `U₀=K^{10}`. In each dyadic prime block `(x,2x]⊂(√X,X]`, put `z=x^{1/6}`. For an arbitrary multiplier family `1∈B⊂[1,K]`, take atoms

`(k,q,u): k∈B, q∈(x,2x] prime, U₀<u≤z, u|(kq+1)`,

with event `n≡−u mod kq`. Every hit at n≥3KX gives the interior word

`((kq+1)/u, u, (n+u)/(kq))`.

Condition on c=n mod `L_B=lcm_{k∈B}k`, put `J_c={k∈B:(k,c)=1}`, and write `h(J)=Σ_{k∈J}1/k`. If f_c(q) counts active atoms at q, then

`μ_c:=Σ_q f_c(q)/q ≍ T h(J_c)`                                (8.11)

uniformly in B and c. Moreover the active residues at each q are distinct, so conditionally on c the number Z_X of atom hits is a sum of independent Bernoulli variables.

*Proof.* An atom is active iff `u≡−c mod k`. Since `u|(kq+1)`, `(u,k)=1`, so activity forces `(c,k)=1`. Conversely those conditions suffice. Distinct same-q classes force equal u because u<q; then u divides k−k', and u>U₀>K forces k=k'. Also `f_c(q)≤Kz=o(q)` uniformly, so the Bernoulli probabilities are <1/2 for large X.

For `d≤K²`, `(c,d)=1`, and `Λ=log(z/U₀)≍T`, elementary progression summation gives

`Σ_{U₀<u≤z, u≡−c(d)}1/u=Λ/d+O(U₀^{-1})`,
`Σ_{U₀<u≤z, u≡−c(d)}1/φ(u)≪Λ/d`.

For the second estimate expand `u/φ(u)=Σ_{a|u}μ²(a)/φ(a)`; the error is `O(log U₀/U₀+Λ/√U₀)`, absorbed uniformly since d≤K² and U₀=K^{10}. For `r(u)=#{k∈J:k|u+c}`, expand the square to obtain

`Σ_{U₀<u≤z}r(u)²/φ(u) ≪ T Σ_{k,k'≤K}1/[k,k'] ≪T(log K)³≪T⁴`.

The final estimate follows by writing k=ga,k'=gb and dropping `(a,b)=1`.

Count primes in the reduced classes `q≡−k^{-1} mod u`. Brun–Titchmarsh and the progression sums give an upper block count `O(xh(J))`; the principal terms give a lower block count `≫xh(J)`. For the error let E_x^*(u) be the maximum dyadic π-discrepancy over reduced classes. Then BT bounds `E_x^*(u)≪x/(φ(u)log x)`, and BV, at moduli u≤x^{1/6}, gives `Σ_uE_x^*(u)≪_R xT^{−R}`. Cauchy–Schwarz bounds the total weighted error by

`(Σ_u r(u)² E_x^*(u))^{1/2}(Σ_u E_x^*(u))^{1/2} ≪ (xT³)^{1/2}(xT^{−30})^{1/2}=o(x)`.

Since 1∈J_c, h(J_c)≥1. Divide by q≈x and sum over the ≍T full blocks; an incomplete last block is harmless for the upper bound. This proves (8.11). Conditional independence is CRT, because q>√X>K, hence q∤L_B. ∎

### 8.8 A log-loss 2/3 exceptional bound for all integers

**Theorem 8.8 (PROVED relative to Lemma 8.7 and Mertens).**

`E₃(N) ≪ N exp(−c (log N)^{2/3}/(log log N)^{1/3})`.

*Proof.* In Lemma 8.7 choose

`y=T²/log T`, `B={k≤K:(k,P_y)=1}`, `M₀=T²/log T`,

where `P_y=Π_{p≤y}p`. The multiplier harmonic sum satisfies

`h(B)≍log K/log y≍T/log T`.                                   (8.12)

The upper bound follows from the Euler product over y<p≤K. For a lower bound restrict prime factors to y<p≤K^η with a sufficiently small fixed η>0. Its harmonic Euler product is ≍`log(K^η)/log y`; a Rankin tail at exponent `1/log(K^η)` shows that terms k>K contribute at most half this product. Indeed the tail/product ratio is at most `exp(−1/η+O(1))`, using `Σ_{p≤z}log p/p=log z+O(1)`. This proves (8.12).

For uniform Haar c mod L_B put

`Z(c)=Σ_{p>y, p|L_B, p|c}1/p`.

CRT makes these divisibility indicators independent with probabilities 1/p. Since y/p<1,

`E exp(y Z)≤Π_{p>y}(1+(exp(y/p)−1)/p)≤e⁴`,

so `P(Z>1/2)≤e^{4−y/2}`. Furthermore

`Σ_{k∈B,p|k}1/k≤h(B)/p`

because k/p belongs to B when p>y. By the union bound on removed multipliers,

`h(J_c)≥h(B)(1−Z(c))`.

On Z≤1/2, (8.11) gives `μ_c≫M₀`; for every c it gives `μ_c≪M₀`. The conditional Bernoulli product therefore yields

`P(Z_X=0)≤exp(−cM₀)`,
`E (Z_X)_j≤(CM₀)^j` for every j≥1.                            (8.13)

Unlike the full endpoint family in Proposition 8.5, these specially constructed atoms have mutually exclusive same-q classes and independent different-q indicators after conditioning. Thus (8.13) is proved, not a Poisson assumption.

Take the even Bonferroni polynomial `Q_r(z)=Σ_{j=0}^r(−1)^j binom(z,j)`, with even `r=O(M₀)` chosen sufficiently large. It is a nonnegative majorant of `1[z=0]`, and

`Q_r(z)≤1[z=0]+binom(z,r+1)`.

Equation (8.13) and Stirling's elementary factorial bound give `E Q_r(Z_X)≤e^{−c'M₀}`. There are at most `KX·X^{1/6}=exp(O(T))` atoms. Expanding Q_r into intersections consequently has unweighted absolute coefficient sum at most `exp(O(rT))=exp(O(T³/log T))`. Each intersection is empty or one congruence class. Thus ordinary integer counting gives

`E₃(N)≪N exp(−c'T²/log T)+exp(CT³/log T)+O(KX)`.

The last term removes n<3KX. There is **no** expansion into all L_B fibres, and no multiplicative closure of I3 is used. Choose

`T=α(log N log log N)^{1/3}`

with fixed α>0 sufficiently small. The second term is at most N^{1/2}, the last is N^{o(1)}, and the first has the claimed exponent. ∎

**PROVED prime/rough-input refinement.** With B=[1,K], condition instead on `(n,P_y)=1`, `y=B₀T²` for a sufficiently large fixed B₀. Then h(B)≈log K≈T; the identical exponential-moment argument gives a conditioned void `exp(−cT²)` and uniform factorial moments `(CT²)^j`. The selector has an exact inclusion–exclusion expansion with `2^{π(y)}` terms. The Bonferroni coefficient ledger is therefore `exp(O(T³))`, including the selector. Taking `T=α(log N)^{1/3}` bounds I3 exceptions among these rough inputs, in particular primes above the small cutoff, by `≪N exp(−c(log N)^{2/3})`. The onset n≥3KX only adds N^{o(1)}. It cannot be extended to all integers by ES scaling, as §8.7 proves.

**Assessment / remaining exponent losses.** The direct I3 atom supply is `T h(J)`, whereas the ES ratio family has `T² h(J)`. That lost factor T is precisely the missing second factor-ratio parameter. For all integers, selecting only y-rough multipliers avoids the zero fibres but loses another factor log y in h(B); optimizing the coefficient ledger yields the `(log log N)^{1/3}` loss above. Removing that loss requires a better treatment of the nonunit fibres, not an unjustified prime-to-composite step. Recovering 3/4 requires additional class supply or a different architecture; no universal impossibility theorem is claimed.

### 8.9 Checks, controls, and round-2 review

**CERTIFIED finite checks.** `scripts/z49_i3astra_round2.py` checks the gcd envelope identity, exact conditioning probabilities, and terminal LLL neighborhood masses at H=12,24,48,80; all terminal mass inequalities are checked as rational inequalities, independent of the floating-point choice of pinning order. It streams compatible pairs in separated endpoint ranges, checking the four gcd factors, all CRT congruences, the joint-density formula, and both equal/unequal-sum modulus bounds. It constructs an explicit divisor cluster surviving small-prime pinning, verifies direct multiplier words and the exact average of their fibre means, and reuses the independent first-round census for 6336 and 42. It also checks the Vaughan Egyptian-fraction identity at 6336. Data: `data/z49_i3astra/round2_checks.json`. No dense pair-product array is allocated.

**Controls and quantifiers.** Square inputs are permitted in every all-integer theorem; neither I3 nor its avoidance density is claimed square-exact. The numerator-free multiplier hit is an interior word, not an ES certificate. Neither the 6336 ES witness nor the known interior words at 241 imply 8/241; no numerator-8 representation is asserted. The hard-prime counts in §6 remain unchanged. The new integer avoiders are allowed to have words beyond H, and the improved exceptional estimate still allows infinitely many total I3 zeros. Neither I3 nor ES is reduced to a finite computation.

Reproduce the new checks with:

```sh
ulimit -v 8000000
timeout 120 uv run python scripts/z49_i3astra_round2.py
```

**Round-2 hostile review completed (fresh deep-mode subagent).** Verdict: **no fatal or major flaw**, one minor proof-writing repair. The reviewer independently checked the envelope and adaptive conditioning, both cases of the Janson shared-modulus bound, the raw-moment counterexample, the full proof chain of the generic energy lemma and BRW coefficient accounting, and every uniformity/Bonferroni step in the multiplier sieve. It also replayed the round-2 script read-only and independently checked the 42/6336 counterexamples. The sole repair clarifies that squarefreeness establishes atomicity, while equal product and residue establish distinctness of the upper-bound event family; this justification is now explicit in §8.4. Review session: `2026-10-28T22-34-20-799Z_01a184a6-68ff-70b7-bfc8-e0e244ed9fea`. The results retain their stated internal, unrefereed status.
