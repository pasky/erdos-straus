# The window statistic from above (task O32)

Branch `side-agent/xwin-average`. Labels as in DISCOVERIES.md. Notation of
POINTWISE_SIZE §8: for a prime `p≡1 (4)` and `a≡3 (4)`, `x_a=(p+a)/4`,
`Rat_a(x)={u/v mod a : uv|x, gcd(u,v)=1}`; window a *fails* if
`Rat_a(x_a)∩{−1,−p}=∅`; `a_min(p)` = least non-failing a. Throughout
`p≡1 (24)` (other primes are Mordell-solved), and
`T(N,Z)=#{p≤N prime, p≡1 (24): a_min(p)>Z}`.

## 0. Results at a glance

| # | statement | status |
|---|---|---|
| 0.1 | `T(N,3)≪N/(log N)^{3/2}=o(π(N))`: "almost all p have `a_min(p)=3`" | PROVED (this is notes Thm 70.9; recorded so that Goal 1's "o(π)" form is seen to be trivial) |
| 1.1 | Half-set lemma: failure of window a ⇒ all prime factors of `x_a` lie in one of `2^{β(a)}` explicit sets `S_σ` of exactly half the classes mod a (any a≡3 (4), prime or composite) | PROVED |
| 1.3 | For every fixed finite set A of moduli ≡3 (4): `#{p≤N: all a∈A fail}≪_A N/(log N)^{1+|A|/2}`; hence `T(N,Z)≪_Z N/(log N)^{1+J(Z)/2}`, `J(Z)=⌊(Z+1)/4⌋` | PROVED (fixed-dimension upper sieve) |

See §1 for details and §5 for the comparison with known results.

## 1. Fixed window sets: the random-model exponent is an upper bound

### 1.1 The half-set lemma

Let `a≡3 (4)`, `a≥3`, `G=(Z/a)^×`. The Klein group `V={id, g↦g^{-1},
g↦−g, g↦−g^{-1}}` acts on G. Since `a≡3 (4)`, −1 is not a square mod a
(some prime factor of a is ≡3 (4)), so `g≠−g^{-1}`; and `g≠−g` as a is odd.
Hence every V-orbit is either
* a *4-orbit* `{g,g^{-1},−g,−g^{-1}}` (when `g²≠1`), or
* a *2-orbit* `{g,−g}` (when `g²=1`); one of them is `{1,−1}`.

Split every 4-orbit as `{g,g^{-1}} ⊔ {−g,−g^{-1}}` and every 2-orbit as
`{g} ⊔ {−g}`. A *selection* σ picks one half of every orbit, with the
constraint that it picks `{1}` from `{1,−1}`. Put `S_σ`= union of the
picked halves. Then `|S_σ|=φ(a)/2` exactly, and the number of selections is
`2^{β(a)}`, `β(a)=(φ(a)−2^{ω(a)})/4+2^{ω(a)−1}−1 ≤ φ(a)/4+2^{ω(a)-2}`.
(The elements with `g²=1` number `2^{ω(a)}` because a is odd.)

For an integer x prime to a let `C(x)⊆G` be the set of classes of the
prime factors of x.

**Lemma 1.1 (half-set lemma; PROVED).** If `−1∉Rat_a(x)`, then
`C(x)⊆S_σ` for some selection σ. In particular this holds whenever window
a fails.

*Proof.* `Rat_a(x)` contains `r` (u=r, v=1), `rs` (u=rs, v=1) and `r/s`
(u=r, v=s) for all distinct primes `r,s|x`. So `−1∉Rat_a(x)` gives:
`−1∉C(x)`; and no `g,h∈C(x)` (distinct classes; for equal classes
`g·g=g²≠−1`, `g/g=1≠−1`) satisfy `gh=−1` or `g/h=−1`, i.e.
`C(x)∩(−C(x))=∅` and `C(x)∩(−C(x)^{-1})=∅`.
Inside a 4-orbit, `g` excludes `−g` and `−g^{-1}`, and `g^{-1}` excludes
the same two elements; so `C(x)` meets the orbit inside one half. Inside a
2-orbit `{g,−g}` the two elements exclude each other, and `−1` is
excluded outright. Choose σ accordingly (arbitrarily on orbits that
`C(x)` misses). ∎

*Remarks.* (i) For prime a this contains notes Cor 70.2 (σ with
`S_σ=Q`, the squares) and the F3 case: F3 failures are confined to a
non-subgroup half-set, e.g. `a=7`, `x=17`: `C={3}⊆{1,3,5}`.
(ii) Unlike notes (71.4), the majorant has **no budget exception**: every
failure, F1 or F3 or the composite-modulus subgroup misses of notes
Thm 70.10, is a pure confinement event of density exactly 1/2. This is
what removes the obstacle that limited notes Cor 71.4 to the exponent
`δ_J=Σ1/(a−1)`.
(iii) Only the target −1 and products of at most two primes are used, so
everything below bounds the larger event "Type II fails at all windows of
A", a fortiori the window failure.

### 1.2 The stacking theorem for a fixed set of windows

**Sieve input (notes Lemma 12.1, PROVED there; standard large sieve).**
Let I be an interval of X integers, P a finite set of primes, and
`Ω_ℓ` a set of `ν(ℓ)<ℓ` classes mod ℓ for `ℓ∈P`. If `S⊆I` avoids every
`Ω_ℓ`, `V=∏_{ℓ∈P}(1−ν(ℓ)/ℓ)` and `Λ=Σ_{ℓ∈P}ν(ℓ)log ℓ/ℓ≤(log X)/4`, then
`|S|≤4XV`.

**Theorem 1.2 (fixed-set stacking; PROVED).** Let A be a fixed finite set
of positive integers `a≡3 (4)`, `J=|A|`. Then

```
#{p≤N prime, p≡1 (24): −1∉Rat_a((p+a)/4) for every a∈A} ≪_A N/(log N)^{1+J/2}.
```

*Proof.* It suffices to treat `p∈(N/2,N]`. Write `p=24t+1`; t runs over an
interval I with `X≍N` integers. By Lemma 1.1, each counted p has a
selection vector `σ=(σ_a)_{a∈A}` with `C(x_a)⊆S_{σ_a}` for all a; there
are `∏_a 2^{β(a)}=O_A(1)` vectors, so fix one. Put `y=2max A+24`,
`log z=(log X)/(5(J+1))`, `P={primes y<ℓ≤z}`, and

* `Ω_ℓ∋` the class `24t+1≡0 (ℓ)`;
* `Ω_ℓ∋` the class `24t+1+a≡0 (ℓ)` for each `a∈A` with
  `(ℓ mod a)∉S_{σ_a}`.

Every counted t avoids `Ω_ℓ`: `p>N/2>z≥ℓ`, so `ℓ∤p`; and if
`ℓ | p+a` with `ℓ` odd then `ℓ|x_a`, so `ℓ mod a∈C(x_a)⊆S_{σ_a}`. The listed
classes are distinct because `ℓ>2max A` exceeds every `|a−a'|` and every
a; and `ℓ∤24`. So `ν(ℓ)=1+#{a: ℓ mod a∉S_{σ_a}}≤J+1<ℓ`.
Then `Λ≤(J+1)Σ_{ℓ≤z}log ℓ/ℓ≤(J+1)(log z+O(1))≤(log X)/4` for large N.
By Mertens in the fixed progressions mod a (each `G∖S_{σ_a}` is a union
of `φ(a)/2` reduced classes),

```
Σ_{ℓ∈P} ν(ℓ)/ℓ = (1+J/2)·log log z + O_A(1) = (1+J/2)·log log N + O_A(1).
```

Hence `|S|≤4X·exp(−Σν/ℓ)≪_A N(log N)^{−1−J/2}`. Sum over the `O_A(1)`
vectors σ and over dyadic ranges. ∎

**Corollary 1.3 (PROVED).** For every fixed `Z≥3`, with
`J(Z)=#{a≤Z: a≡3 (4)}=⌊(Z+1)/4⌋`,

```
T(N,Z)=#{p≤N, p≡1 (24): a_min(p)>Z} ≪_Z N/(log N)^{1+J(Z)/2} = π(N)·(log N)^{−J(Z)/2}.
```

*Proof.* For `p>3Z` every `a≤Z` is admissible (`x_a<p`, so `p∤x_a`), and
`a_min(p)>Z` means each such window fails, in particular `−1∉Rat_a(x_a)`.
Apply Theorem 1.2 with `A={a≤Z: a≡3 (4)}`. ∎

*What this says.* The random model of POINTWISE_SIZE §8.4 /
notes Heuristic 70.1 predicts
`P(a_min(p)>Z)≈∏_{a≤Z}c_a(log p)^{−1/2}=(log p)^{−J(Z)/2+o(1)}`.
Corollary 1.3 proves this as an **upper bound with the model's exact
exponent**, for every fixed Z. Previously proved: exponent `1/2` (one
window, notes Thm 70.9) and `δ_J=Σ_{a prime}1/(a−1)≈½log log Z` (notes
Cor 71.4, via the single excluded class −1). For instance
`T(N,7)≪N/(log N)^2`, `T(N,11)≪N/(log N)^{5/2}`, `T(N,23)≪N/(log N)^4`
versus notes (71.26)'s `2/3, 23/30, 859/990` (beyond the `1/log N`).

**Corollary 1.4 (two-sided orders; lower bounds cited).**
* `#{p≤x: a_min(p)≥7}≍x/(log x)^{3/2}`: upper bound Cor 1.3 (Z=3; also
  notes Thm 70.9), lower bound POINTWISE_WINDOW Thm W1 (PROVED modulo cited
  sieve theorems, restricted to a subclass, which only helps).
* `#{p≤x: a_min(p)≥11}≍x/(log x)^2` **CONDITIONAL on Elliott–Halberstam**
  for the lower bound (POINTWISE_WINDOW Thm W2); the upper bound
  `≪x/(log x)^2` is unconditional (Cor 1.3, Z=7). So W2 is sharp.

## 2. Growing window sets: a proved weak form of H_STACK up to `a≤(log N)^{2/5}`

(In progress; written lemma by lemma.) Plan: replace the half-set
majorant (whose union cost `2^{φ(a)/4}` limits it to `a≲log log N`) by a
**second-moment bound on random signed products in G**, uniform in a,
and feed it into a pattern-summed large sieve over the prime factors of
`x_a` in a range `(y,y']`. The pattern sum factorises over windows and
reproduces, as an upper bound, the Poisson model of the prime factors.

### 2.1 Random signed products (finite group lemma)

Let G be a finite abelian group of order n, `τ∈G` with `τ≠1`, `τ²=1`, and
`t(G)=#{g: g²=1}`. For a tuple `c=(c_1,…,c_k)∈G^k` put
`Σ±(c)={∏c_i^{ε_i}: ε∈{−1,0,1}^k}` (each entry used at most once), and
call c *bad* if `τ∉Σ±(c)`. Let `ρ_k=#{bad c}/n^k`.

**Lemma 2.1 (PROVED).** For all `k≥0`,
`ρ_k ≤ 3n·3^{−k} + (9/4)·t(G)·(5/9)^k`.
Consequently, if K is Poisson with mean μ,
`E ρ_K ≤ 3n·e^{−2μ/3} + (9/4)·t(G)·e^{−4μ/9}`.

*Proof.* k=0: `ρ_0=1≤3n`. Let `k≥1`, c uniform on `G^k`, and
`N=Σ_{ε≠0}1[E_ε]`, `E_ε={∏c_i^{ε_i}=τ}` (ε=0 gives 1≠τ). For `ε≠0` some
`ε_i=±1`, and `c_i↦c_i^{±1}` is a bijection independent of the other
coordinates, so `P(E_ε)=1/n` and `μ_N:=EN=(3^k−1)/n`. For a pair
`ε,ε'≠0`:
* (i) `ε=ε'`: probability `1/n`; `3^k−1` pairs.
* (ii) some i has exactly one of `ε_i,ε'_i` equal to 0, say `ε_i=0≠ε'_i`:
  `E_ε` is determined by `c_{−i}` and has probability `1/n`; given
  `c_{−i}`, exactly one value of `c_i` gives `E_{ε'}`. Probability `1/n²`;
  at most `(3^k−1)²` pairs.
* (iii) otherwise the supports agree and `D={i: ε_i=−ε'_i≠0}≠∅`. Put
  `B=∏_D c_i^{ε_i}`, `A=∏_{i:ε_i=ε'_i≠0}c_i^{ε_i}`. Both events give
  `AB=τ=AB^{−1}`, so `B²=1` and `A=τB`. B is uniform (D≠∅) and
  independent of A. If A involves some coordinate it is uniform:
  probability `t(G)/n²`; there are at most `5^k` such pairs (5 choices
  `(0,0),(±,±),(±,∓)` per coordinate). If A is empty (`A=1`) the
  condition is `B=τ`: probability `1/n`; at most `3^k−1` such pairs
  (choices `(0,0),(+,−),(−,+)`, D≠∅).

Hence `EN² ≤ 2μ_N + μ_N² + t·5^k/n²`, `Var N ≤ 2μ_N + t5^k/n²`, and by
Chebyshev `ρ_k=P(N=0) ≤ Var N/μ_N² ≤ 2n/(3^k−1) + t5^k/(3^k−1)²`. Use
`3^k−1≥(2/3)3^k`. The Poisson statement follows from `E x^K=e^{−μ(1−x)}`
with `x=1/3, 5/9`. ∎

*Remark.* `ρ_k≥2^{−k}·(#index-2 subgroups avoiding τ)` (all entries in
such a subgroup), so the base `5/9` cannot be improved below `1/2` by any
argument; the second moment loses only `log(10/9)` per prime factor.
For `G=(Z/a)^×` (a odd) `t(G)=2^{ω(a)}`, `τ=−1`, `n=φ(a)`.

