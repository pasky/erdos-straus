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

| 2.1 | Random signed products: `P(τ∉Σ±(c_1..c_k)) ≤ 3n·3^{−k}+(9/4)t(G)(5/9)^k` in any finite abelian G of order n (second moment) | PROVED |
| 2.2 | Pattern-summed sieve: for any set A of windows `a≤(log N)^θ`, the joint failure count is `≤2N(log N)^{δ−1}∏_{a∈A}F_a`, `F_a≈3φ(a)e^{−2λ/3}+(9/4)2^{ω(a)}e^{−4λ/9}`, `λ≈(1−θ−δ)log log N` | PROVED modulo Siegel–Walfisz |
| 2.3 | `#{p≤N: a_min(p)>(log N)^θ} ≤ N exp(−(κ(θ)−ε)(log N)^θ log log N)` for `0<θ<2/5`, `κ=(1−θ)/9` (θ≤2/11) | PROVED modulo Siegel–Walfisz |
| 1.3 (EVIDENCE) | `T(x,Z)·(log x)^{1+J/2}/x` flat for `x=10^6..10^8`, `Z≤23` | EVIDENCE |

Cor 2.3 is an unconditional (modulo SW) version of the *conclusion* of
the open stacking hypothesis H_STACK (notes Thm 71.6), with per-window
saving `(4/9)(1−θ)` instead of `1/2`, and it improves notes Thm 12.2's
`exp(−c(log log N)²)` tail for the small-window statistic to
`exp(−c(log N)^θ log log N)`. It does not approach ES (needs θ=1).
Sections 3–4: Goals 2–4 and what blocks further progress.

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

### 1.3 Numerical check (EVIDENCE)

`T(x,Z)` for all primes `p≡1 (24)`, `p<x` (census of
`pointwise_size_amin.py`), normalised by `x/(log x)^{1+J(Z)/2}` in
parentheses (`scripts/xwin_tail_table.py`):

| x | Z=3 | 7 | 11 | 15 | 19 | 23 |
|---|---|---|---|---|---|---|
| 1e6 | 4540 (0.233) | 989 (0.189) | 395 (0.280) | 266 (0.701) | 134 (1.313) | 53 (1.931) |
| 1e7 | 35750 (0.231) | 7144 (0.186) | 2681 (0.280) | 1732 (0.725) | 849 (1.427) | 308 (2.079) |
| 1e8 | 289372 (0.229) | 54226 (0.184) | 18868 (0.275) | 11250 (0.703) | 5125 (1.375) | 1742 (2.006) |

Every column is flat to within a few per cent over two decades, as the
exponent `1+J/2` of Corollary 1.3 (and the model) predicts; this is
consistent with Corollary 1.3 being sharp in the exponent for each fixed
Z (proved only for Z=3, and Z=7 on EH, by Cor 1.4).

## 2. Growing window sets: a prime-side proof of the window tail (independent of notes §14)

**Priority.** notes §14 (Thm 14.4, θ<2/5; Thm 14.9, every
`θ<θ_*=log3/(1+log3)=0.5235`; DISCOVERIES (A)5, review status not
stated) already bounds this window statistic: its sufficiency step uses
exactly a signed witness `−1∈Rat_w((m+w)/4)` at a window `w≤W=(log N)^θ`,
so its proof gives `T(N,(log N)^θ)≤N exp(−c(log N)^θ log log N)` for
`θ<θ_*` (integer-side Λ² weights, Paley–Zygmund local factors, exclusion
corrections). Lemma 2.1 below is essentially notes Lemma 12.5 (same pair
calculation). What this section adds is an **independent second proof**
of that window tail by a different architecture (a prime-side large sieve
with a pattern sum over the small prime factors; primality used through
the sieve), with explicit per-window exponents. It is a cross-check of
the window form of notes Thm 14.4/14.9, not a new frontier.

Plan: replace the half-set
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

**Lemma 2.1 (PROVED; = notes Lemma 12.5 up to presentation).** For all `k≥0`,
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

*Remark.* If some index-2 subgroup avoids τ (e.g. the squares, a prime),
then `ρ_k≥2^{−k}` (all entries in it), so the base `5/9` cannot be
improved below `1/2` by any argument; the second moment loses only `log(10/9)` per prime factor.
For `G=(Z/a)^×` (a odd) `t(G)=2^{ω(a)}`, `τ=−1`, `n=φ(a)`.

### 2.2 The pattern-summed sieve

Notation: `ℒ=log N`, `L=log log N`. Fix `0<θ<1` and `0<δ<(1−θ)/2`. Put

```
Z=ℒ^θ,  y=exp(ℒ^δ),  M=⌈6L⌉,  log y'=ℒ^{1−θ}/(100M),  z_0=N^{1/20},
λ(u,v)=Σ_{u<ℓ≤v}1/ℓ,  λ=λ(y,y')=(1−θ−δ)L−log L−O(1).
```

**Input (SW).** Siegel–Walfisz plus partial summation: uniformly for
`a≤ℒ^θ=(log y)^{θ/δ}`, `(c,a)=1` and `y≤u<v`,
`Σ_{u<ℓ≤v, ℓ≡c (a)}1/ℓ ≤ (λ(u,v)+η)/φ(a)` with `η=ℒ·exp(−c_0ℒ^{δ/2})`.
(Ineffective through Siegel–Walfisz; nothing else is ineffective.)

**Theorem 2.2 (uniform pattern sieve; PROVED modulo SW and notes Lemma
12.1).** For N large in terms of θ, δ, and every set A of integers
`a≡3 (4)`, `a≤Z`,

```
#{N/2<p≤N prime, p≡1 (24): −1∉Rat_a((p+a)/4) ∀a∈A}
   ≤ 2N·ℒ^{δ−1} · ∏_{a∈A} F̄_a,
F̄_a = e^{η}·E ρ^{(a)}_{K} + O((φ(a)+2^{ω(a)})ℒ^{−3}),   K ~ Poisson(λ+η),
```

where `ρ^{(a)}_k` is the bad proportion of Lemma 2.1 for `G=(Z/a)^×`,
`τ=−1`; the O is uniform in a and A. By Lemma 2.1,
`E ρ_K ≤ 3φ(a)e^{−2λ/3}+(9/4)2^{ω(a)}e^{−4λ/9}` (uncapped), and for any
`k_0≤λ` (capped; `ρ_k≤1` below `k_0`, Chernoff for the Poisson tail)

```
E ρ_K ≤ e^{−λ}(eλ/k_0)^{k_0} + 3φ(a)3^{−k_0} + (9/4)2^{ω(a)}(5/9)^{k_0}.   (2.1)
```

*Proof.* **Step 0 (patterns).** For a counted p and `a∈A`, let `R_a` be
the set of the M smallest primes of `(y,y']` dividing `x_a` (all of them
if there are fewer). Order `R_a` and take the tuple of classes mod a; it
is *bad* in the sense of Lemma 2.1 (`G=(Z/a)^×`, `τ=−1`), because for
`ε∈{−1,0,1}^{R_a}` the coprime `u=∏_{ε_r=1}r`, `v=∏_{ε_r=−1}r` have
`uv|x_a`, so `Σ±⊆Rat_a(x_a)`. Put `m_a=y'` if `|R_a|<M` and
`m_a=max R_a` if `|R_a|=M`. Then the event `R_a=R` is: `r|x_a` for
`r∈R`, and `ℓ∤x_a` for primes `ℓ∈(y,m_a]∖R`.

**Step 1 (one pattern vector).** Fix `(R_a)_{a∈A}`. If two `R_a` share a
prime ℓ the count is 0 (`ℓ|a−a'`, but `ℓ>y>Z`). Otherwise put
`Q=∏_a∏_{r∈R_a}r`; `log Q≤MJ log y'≤ℒ/100`. Write `p=24t+1`; t runs over
X≍N/48 integers, and the conditions `r|x_a` put t in one class mod Q:
`t=t_0+Qu`, u in an interval of `X/Q+O(1)≥N^{0.9}` integers. Sieve u
by the primes `ℓ∈P=(y,z_0]∖∪_aR_a`, removing the class `p≡0` and, for each
a with `ℓ≤m_a`, the class `p≡−a`. These classes are distinct (`ℓ>y>Z`),
so `ν(ℓ)=1+#{a: ℓ≤m_a}≤J+1<ℓ`, and
`Λ≤log z_0+(J+1)(log y'+O(1))≤ℒ/20+ℒ/50≤log(X/Q)/4`. Notes Lemma 12.1
gives the bound `4(X/Q)(1+o(1))∏_{ℓ∈P}(1−ν(ℓ)/ℓ)`, and

```
Σ_{ℓ∈P}ν(ℓ)/ℓ ≥ λ(y,z_0)+Σ_a λ(y,m_a) − (J+1)Σ_{ℓ∈∪R_a}1/ℓ,
```

where the last sum is `≤(J+1)MJ/y=o(1)`. With
`e^{−λ(y,z_0)}=(1+o(1))log y/log z_0=20(1+o(1))ℒ^{δ−1}`:

```
count ≤ 80(1+o(1))·(X/Q)·ℒ^{δ−1}·∏_a e^{−λ(y,m_a)}.
```

**Step 2 (sum over patterns).** Dropping disjointness, the sum over
pattern vectors factorises: total `≤80(1+o(1))Xℒ^{δ−1}∏_aP_a` with the
pattern sum `P_a=Σ_{R bad}e^{−λ(y,m_R)}/∏_{r∈R}r`, and `80X≤2N`. Step 3
shows `P_a≤F̄_a`.

**Step 3 (one window).** Let `n=φ(a)`, `t=2^{ω(a)}`.
* `|R|=k<M`. Bound the sum over k-sets by `1/k!` times the sum over
  ordered k-tuples of primes whose class tuple is bad, and group the
  tuples by class tuple. By (SW) each class contributes `≤(λ+η)/n`, so
  this part is `≤e^{−λ}Σ_k(λ+η)^kρ_k/k! = e^{η}E ρ_K`, K Poisson of mean
  `λ+η` (ρ_k for k≥M only enlarges the sum). (2.1) is Lemma 2.1 for
  `k≥k_0` plus `P(K<k_0)≤e^{−μ}(eμ/k_0)^{k_0}` (`k_0≤μ`).
* `|R|=M`. Write `R=R'∪{m}`, `m=max R`. Badness is inherited by
  `R'` (`Σ±(R')⊆Σ±(R)`), and `R'⊆(y,m)`. The same grouping gives
  `≤Σ_{y<m≤y'}m^{−1}·e^{−λ(y,m)}(λ(y,m)+η)^{M−1}ρ_{M−1}/(M−1)!`
  `≤e^{η}ρ_{M−1}(λ+o(1))`, since a Poisson probability is ≤1. With
  `M=⌈6L⌉`, Lemma 2.1 gives `ρ_{M−1}≪nℒ^{−6.5}+tℒ^{−3.5}`, so this part
  is `O((n+t)ℒ^{−3})`. ∎

### 2.3 Consequences for `a_min`

Write `c=1−θ−δ`, so `e^{−λ}=ℒ^{−c}·L·O(1)`; `2^{ω(a)}=ℒ^{o(1)}` and
`φ(a)≤ℒ^θ` for `a≤ℒ^θ`. Take `k_0=bL` with `θ/log 3<b<c` in (2.1):

```
F̄_a ≤ ℒ^{−d+o(1)},   d(θ,b) = min{ c−b+b·log(b/c),  b·log 3−θ,  b·log(9/5) }.
```

All three exponents are positive iff `θ/log 3<b<c`, which is possible iff
`θ<c·log 3`, i.e. (δ→0) **`θ<θ_*=log3/(1+log3)=0.52349…`** — the same
entropy threshold as notes §14.4. Put `d(θ)=sup_b d(θ,b)` at δ=0
(`d(θ)>0` for `θ<θ_*`, `d(θ)→0` as `θ→θ_*`). For `θ≤2/11` the uncapped
form gives the simpler `d(θ)≥4(1−θ)/9`; e.g. `d(0.1)≥0.40`.

**Corollary 2.3 (PROVED modulo SW).** Fix `0<θ<θ_*` and `ε>0`. For
`N≥N_0(θ,ε)`

```
T(N,(log N)^θ) = #{p≤N, p≡1 (24): a_min(p)>(log N)^θ}
               ≤ N·exp(−(d(θ)/4−ε)·(log N)^θ·log log N).
```

*Proof.* Put `f=(log N)^θ log log N`. Primes `p≤N_1:=N e^{−f}` contribute
`≤N e^{−f}`. Cover `(N_1,N]` by `O(f)` dyadic blocks `(N'/2,N']`; on each,
`log N'=(1+o(1))log N` uniformly (since `f=o(log N)`). A prime with
`a_min(p)>(log N)^θ` fails at every `a≤(log N')^θ`, all admissible.
Apply Theorem 2.2 in the block with `A={a≤(log N')^θ, a≡3 (4)}`,
`J=(1/4+o(1))(log N)^θ`, and δ small in terms of ε: the block count is
`≤2N'·exp(−(d(θ)−ε/2)J log log N)`. Sum the `O(f)` blocks. ∎

*Per-window saving.* The worst window saves `ℒ^{−d(θ)}`, not the model's
`ℒ^{−1/2}`. Losses: the second-moment base `5/9` vs `1/2` (term
`b log(9/5)`), the φ(a)-entropy term (`b log 3−θ`), and the sifting range
`(y,y']` (`c=1−θ` instead of 1: the sieve dimension `J≍ℒ^θ` forces
`log y'≲ℒ^{1−θ}`).

**Position.**
* **Not new in shape or range**: notes Thm 14.4/14.9 (see the Priority
  note at the head of §2) already give the window tail
  `N exp(−c(log N)^θ log log N)` for every `θ<θ_*`, with unspecified c.
  Corollary 2.3 is an independent proof via a prime-side sieve, with an
  explicit per-window exponent `d(θ)`; it confirms the window extraction of
  Thm 14.9 (whose review status is not stated in DISCOVERIES (A)5).
* notes Thm 12.2 is an ES exceptional-set bound; its B-window part alone
  (an adaptation, not stated there) gives `T(N,δℒ)≪N exp(−c(log log N)²)`.
* notes Thm 71.6 (CONDITIONAL on `H_FAIL`, `H_STACK`) bounds the prime-modulus
  tail by `N exp(−(1+o(1))ℒ^θ/(4θ))`. Its *tail conclusion* (in the
  weaker form `exp(−cℒ^θ log ℒ)`, composite windows included) holds
  unconditionally for `θ<θ_*` — by notes Thm 14.9 already, and by Cor 2.3.
  H_STACK itself (per-window constant `C_0ℒ^{−1/2}`, an integer event)
  is not proved.
* The literature exceptional-set bounds (Vaughan, the 3/4 note) use
  witnesses at the opposite end (window `q≈p/M`, POINTWISE_SIZE §8.1).
  The window tail says: all but `N exp(−cℒ^θ log ℒ)` primes `p≤N` have a
  Type II solution with p-free denominator `x≤(p+(log p)^θ)/4`.
  Literature novelty of that statement: **not checked**.
* Count-below-one (ES) would need `θ=1`. Both proofs stop at `θ_*`
  (entropy: `3^K` signed products need `K≥log_3 φ(a)` small prime factors
  in the sifted range), and at `θ<1` regardless (dimension vs. sifting
  range).

## 3. Goals 2–4

### 3.1 Goal 2: positive-density sets

* **Trivial version.** `S_3={p≡1 (24): (p+3)/4 has a prime factor ≡2 (3)}`
  has relative density 1 (notes Thm 70.9), satisfies `a_min=3` on it, and
  is not a finite union of classes (its complement meets the class
  `1 mod 840` in `≫x/(log x)^{3/2}` primes, POINTWISE_WINDOW W1; a finite
  union of classes of relative density 1 would be cofinite). But it is
  certified by a *bounded* procedure (window 3), so it is not what
  POINTWISE_SIZE §10 asks for.
* **Meaningful version: sets where every bounded window search fails
  on a positive proportion.** Let `F_K={p: a_min(p)>K}`.

  **Corollary 3.1 (PROVED modulo SW and the W1/W2 inputs).** Let
  `𝒲_1={p≤x: p≡1 (840), window 3 fails by F1}` (W1: `|𝒲_1|≫x/(log x)^{3/2}`).
  Then all but `O(x·exp(−(log x)^{2/5−ε}))` primes of `𝒲_1` have
  `7≤a_min(p)≤(log p)^{2/5−ε}`. CONDITIONAL on EH, the same holds for
  the W2 family (`a_min≥11`, size `≫x/(log x)^2`).

  *Proof.* Cor 2.3 with θ close to 2/5, compared with the W1/W2 lower
  bounds (any `N exp(−cℒ^θ log ℒ)` is `o(N/(log N)^A)` for all A). ∎

  So on a set of primes of size `≍x/(log x)^{3/2}`, on which the bounded
  search "window 3" fails identically, the unbounded window search is
  proved to succeed within `(log p)^{2/5}` for relative density 1. Beyond
  `K=7` (EH: 11) no lower bound for `|F_K|` is known (POINTWISE_WINDOW
  §7.3), and that — not the upper side — is what blocks the analogous
  statement for larger K.

### 3.2 Goal 3: seeded windows on average (Assessment; no new theorem)

Theorem 2.2 applies verbatim to the seeded windows `q≡−p (4n)` after
conditioning on `n_p=n` (drop all but the conditions `(ℓ/p)=1`, `ℓ≤w`,
and `(n/p)=−1`, a congruence mod `4n∏_{ℓ≤w}ℓ`; Brun–Titchmarsh bounds
`#{p≤N: n_p>m}≤(2+o(1))π(N)2^{−π(m)}` for `log m=o(L)`... ). Because the
seeded moduli are `≈4n_pj`, the usable number of windows is
`J≲ℒ^{2/5}/n_p`, and the result is weaker than Cor 2.3 (balance at
`n_p≈ℒ^{1/5}` gives a saving `exp(−ℒ^{1/5−o(1)})`). The second-moment
lemma cannot see the advantage of seeding (no F1 at prime seeded
windows): Lemma 2.1 bounds all bad tuples, including F3-type half-sets
containing the planted non-residue. So nothing unconditional specific to
X_QNR is obtained.

### 3.3 Goal 4: conditional statements

* **GRH** makes Theorem 2.2 effective (Siegel–Walfisz → GRH-PNT in APs)
  and allows `log y≍(log L)^2`, i.e. δ→0 at no cost; it does **not**
  change the range `θ<2/5` or the per-window constant.
* **EH / higher level**: no help. The binding constraint is
  `Λ=Σν(ℓ)log ℓ/ℓ≲log X` (dimension × log sifting range ≤ level), and a
  level beyond `X` carries no information about integers `≤X`.
* **Proposition 3.2 (dimension–range obstruction for V-type majorants;
  PROVED as an optimisation; its relevance to "all sieve methods" is
  Assessment).** Consider any majorant of the form
  `count ≤ X·∏_a(log z_a)^{−δ_a}`, where window a excludes primes of
  relative density `δ_a` up to `z_a` (any `δ_a>0`; even with `y=1`),
  subject to the level constraint `Λ≈Σ_aδ_a log z_a≤ℒ` (Lemma 12.1 needs
  `ℒ/4`; we allow level X). Then the bound is `≥X·e^{−ℒ/e}=N^{1−1/e+o(1)}`.

  *Proof.* Put `u_a=log z_a`, `D=Σδ_a`. Maximise `Σδ_a log u_a` subject to
  `Σδ_au_a≤ℒ`: by concavity (Jensen with weights `δ_a/D`) the maximum is
  `D log(ℒ/D)`, and `max_D D log(ℒ/D)=ℒ/e` (at `D=ℒ/e`). ∎

  So no window-sieve majorant of this type reaches count-below-one, at
  any level of distribution and with any per-window densities: **ES via
  X_win cannot be proved by stacking window sieves**. Even H_FAIL+H_STACK
  (notes §71.5) would, once the level constraint is imposed, give at best
  `N^{1−1/e}` from such majorants; notes (71.44)–(71.46) (where `L=log N`)
  ignore the constraint. The constraint is binding exactly because the
  dimension grows with the number of windows.
* **No clean "ES ⇐ standard hypothesis".** X_win is a pointwise
  statement about the factorisations of `≍log p` specific integers
  `(p+a)/4`; GRH, EH, Bateman–Horn/Dickson (which go the *other* way,
  Prop 8.4) and Hooley-type hypotheses control averages over p or over
  moduli. We found no standard hypothesis implying X_win; Prop 3.2 shows
  that sieve-averaging cannot even give the "count below one" route.

