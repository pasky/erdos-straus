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
| 1.1 | Half-set lemma: failure of window a ⇒ all prime factors of `x_a` lie in one of `2^{β(a)}` explicit sets `S_σ` of exactly half the classes mod a (any a≡3 (4), prime or composite); no budget exceptions | PROVED |
| 1.2–1.3 | For every fixed finite set A of moduli ≡3 (4): `#{p≤N: −1∉Rat_a(x_a) ∀a∈A}≪_A N/(log N)^{1+|A|/2}`; hence `T(N,Z)≪_Z N/(log N)^{1+J(Z)/2}`, `J(Z)=⌊(Z+1)/4⌋` — the random-model exponent, for each fixed Z | PROVED (fixed-dimension upper sieve). New: improves notes Cor 71.4 (`δ_J≈½log log Z`) and makes POINTWISE_WINDOW §6's joint "dimension ≥J/2" Assessment a theorem |
| 1.4 | over `p≡1 (24)`: `#{a_min≥7}≍x/(log x)^{3/2}`; `#{a_min≥11}≍x/(log x)^2` | upper halves PROVED; lower halves = POINTWISE_WINDOW W1 (PROVED modulo cited sieve theorems S1–S3) / W2 (CONDITIONAL on EH) |
| 1.5 | uniform version (`Z≤C_0 log log N`): `T(N,Z)≤π(N)(log N)^{−(1/2−o(1))J(Z)}` for `Z=o(log log N)`; `N exp(−(0.2225−o(1))(log log N)²)` at `Z≈3.56 log log N` | PROVED (SW only for moduli `≤(log y)^{1/2}`) |
| §1.3 | `T(x,Z)·(log x)^{1+J/2}/x` flat (±9%) for `x=10^6..10^8`, `Z≤23` | EVIDENCE |
| 2.1 | Random signed products: `P(τ∉Σ±(c_1..c_k)) ≤ 3n·3^{−k}+(9/4)t(G)(5/9)^k` | PROVED (= notes Lemma 12.5) |
| 2.2 | Pattern-summed prime-side sieve for windows `a≤(log N)^θ` | PROVED modulo Siegel–Walfisz |
| 2.3 | `T(N,(log N)^θ) ≤ N exp(−(d(θ)/4−ε)(log N)^θ log log N)` for `θ<θ_*=log3/(1+log3)`, explicit `d(θ)` (`≥4(1−θ)/9` for θ≤2/11) | PROVED modulo SW; **independent re-proof** of the window form of notes Thm 14.4/14.9 (same range θ_*), not a new frontier |
| 3.2 | Optimisation: V-type window-sieve majorants under the level constraint are `≥N^{1−1/e}` | PROVED as stated (scope: that majorant class only) |

Goal-1 summary: `f=3` already gives `o(π)`; the best known window tail is
`f=(log x)^{θ_*−σ}` with exceptional set `x·exp(−c(log x)^{θ_*−σ}log log x)`,
implicit in notes Thm 14.9 and re-proved here (Cor 2.3). Genuinely new
here: the fixed-Z exact exponent (Thm 1.2/Cor 1.3) and its sharpness
consequences (Cor 1.4). Nothing approaches ES (needs θ=1).

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

**Corollary 1.4 (two-sided orders; upper halves PROVED, lower halves
PROVED modulo the sieve theorems cited for W1, resp. CONDITIONAL on EH).**
All counts are over primes `p≡1 (24)` (the class of Theorem 1.2;
running the same sieve with `p=4t+1` covers all `p≡1 (4)`).
* `#{p≤x, p≡1 (24): a_min(p)≥7}≍x/(log x)^{3/2}`: upper bound Cor 1.3
  (Z=3; also notes Thm 70.9), lower bound POINTWISE_WINDOW Thm W1 (PROVED
  modulo cited sieve theorems S1–S3; it counts the subclass `p≡1 (840)`,
  which only helps).
* `#{p≤x, p≡1 (24): a_min(p)≥11}≍x/(log x)^2` **CONDITIONAL on Elliott–Halberstam**
  for the lower bound (POINTWISE_WINDOW Thm W2); the upper bound
  `≪x/(log x)^2` is unconditional (Cor 1.3, Z=7). So W2 is sharp.

### 1.2' Uniformity: exponent exactly 1/2 per window for `Z=o(log log N)`

**Theorem 1.5 (PROVED; Siegel–Walfisz used only for moduli
`≤C_0(log y)^{1/2}`, constants possibly ineffective).** Let
`L=log log N`, `ℒ=log N`, and fix `C_0≥1`. Uniformly for `3≤Z≤C_0L` and
`N≥N_0(C_0)`, with `J=J(Z)` and `β_tot(Z)=Σ_{a≤Z, a≡3 (4)}β(a)`,

```
#{N/2<p≤N, p≡1 (24): a_min(p)>Z}
   ≤ (N/ℒ)·exp( −(J/2)(L − 3 log L − C) + β_tot(Z)·log 2 + O(log L) ),
```

with C and the O depending on `C_0` only. Since
`β_tot(Z)≤Σ_{a≤Z}(φ(a)/4+2^{ω(a)−2})=O(Z²)`, this is
`π(N)·(log N)^{−(1/2−o(1))J(Z)}` uniformly for `Z=o(L)` — the model rate
with the exact per-window exponent 1/2. With `C_0=4` and
`Z=⌊π²L/(4 log 2)⌋≈3.56L` (inside the range), using
`Σ_{a≤Z, a≡3 (4)}φ(a)=(1+o(1))Z²/π²` (so `β_tot=(1+o(1))Z²/(4π²)`), it
gives `T(N,Z)≤N exp(−(π²/(64 log 2)−o(1))(log log N)²)`, where
`π²/(64 log 2)=0.2225…`.

*Proof.* As Theorem 1.2, with `y=exp(L²)` and `log z=ℒ/(5(J+1))`.
Moduli `a≤Z≤C_0L=C_0(log y)^{1/2}`, so SW gives
`Σ_{y<ℓ≤z, ℓ≡c (a)}1/ℓ=(1/φ(a))log(log z/log y)+O(e^{−c_1L})` uniformly;
summed over `≤C_0L` windows and `≤C_0L` classes the error is `o(1)`.
Roots are distinct as `y>2Z`, `ν(ℓ)≤J+1<ℓ`, and
`Λ≤(J+1)(log z+O(1))≤ℒ/4`. For a fixed selection vector σ, Lemma 12.1
gives `≤4X exp(−(1+J/2)log(log z/log y)+o(1))` with
`log(log z/log y)=L−2log L−log(5(J+1))≥L−3log L−C(C_0)` (as `J≤C_0L`),
and `e^{−(L−3log L−C)}=O(L³/ℒ)` supplies the `1/ℒ` (the extra `L³` is
the `O(log L)`). Sum over the `2^{β_tot}` selection vectors (Lemma 1.1).
For the last claim, `−(J/2)L+β_tot log 2=−(Z/8)L+(log 2/(4π²))Z²+o(L²)`
is minimised at `Z=π²L/(4log 2)` with value `−(π²/(64log2))L²`. ∎

*Comparison.* notes Cor 71.4 has, for fixed J, exponent
`δ_J≈½log log Z` in total; Theorem 1.5 has `J/2≈Z/8`, uniformly up to
`Z=o(log log N)`. The union cost `2^{β_tot}≈2^{Z²/(4π²)}` is what stops
the half-set method at `Z≍log log N`; §2 handles larger Z with a weaker
per-window exponent. This is the only range in which the stacking
hypothesis H_STACK's per-window constant (`ℒ^{−1/2}`) is attained here.

### 1.3 Numerical check (EVIDENCE)

`T(x,Z)` for all primes `p≡1 (24)`, `p<x` (census of
`pointwise_size_amin.py`), normalised by `x/(log x)^{1+J(Z)/2}` in
parentheses (`scripts/xwin_tail_table.py`):

| x | Z=3 | 7 | 11 | 15 | 19 | 23 |
|---|---|---|---|---|---|---|
| 1e6 | 4540 (0.233) | 989 (0.189) | 395 (0.280) | 266 (0.701) | 134 (1.313) | 53 (1.931) |
| 1e7 | 35750 (0.231) | 7144 (0.186) | 2681 (0.280) | 1732 (0.725) | 849 (1.427) | 308 (2.079) |
| 1e8 | 289372 (0.229) | 54226 (0.184) | 18868 (0.275) | 11250 (0.703) | 5125 (1.375) | 1742 (2.006) |

Every column is flat to within 9% (mostly 1–4%) over two decades, as the
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

*Remark.* If some index-2 subgroup avoids τ, then `ρ_k≥2^{−k}` (all
entries in it). For `G=(Z/a)^×`, `τ=−1`, this holds for **every**
`a≡3 (4)`, prime or composite: the kernel of the Jacobi character
`(·/a)` has index 2 and avoids −1 since `(−1/a)=−1`. So so the base `5/9` cannot be
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
`k_0≤λ+η` (capped; `ρ_k≤1` below `k_0`, Chernoff for the Poisson tail
of K, whose mean is `λ+η`)

```
E ρ_K ≤ e^{−(λ+η)}(e(λ+η)/k_0)^{k_0} + 3φ(a)3^{−k_0} + (9/4)2^{ω(a)}(5/9)^{k_0}.   (2.1)
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
* **Within thin hard families the bounded search still wins.** Theorem
  1.2 gives `#{p∈𝒲_1: a_min(p)>7}≤T(x,7)≪x/(log x)^2=o(|𝒲_1|)` for the
  W1 family `𝒲_1` (`|𝒲_1|≫x/(log x)^{3/2}`, window 3 failing): almost
  every W1 prime has `a_min=7`; on EH almost every W2 prime has
  `a_min=11`. More generally, for each fixed K, whenever
  `|F_K|≫N/(log N)^{1+J(K)/2}` (known for K=3, and K=7 on EH), almost
  all of `F_K` lies in `F_K∖F_{K+4}`. So a family on which *every*
  bounded window search fails on a positive proportion would have to be
  of size `≤N/(log N)^{A}` for every A, and then Cor 2.3 still puts
  almost all of it below `(log p)^{θ_*−ε}` provided it is larger than
  `N exp(−c(log N)^{θ_*−ε}log log N)`. No such family with a proved
  lower bound is known (POINTWISE_WINDOW §7.3: lower bounds stop at K=7,
  11 on EH). **Verdict on Goal 2:** in the window frame the question
  reduces to Ω-type lower bounds for `|F_K|` (the O29 side), not to
  upper-bound technology.

### 3.2 Goal 3: seeded windows on average (proposed adaptation; no theorem)

The seeded windows `q≡−p (mod 4n_p)` depend on p through `n_p` and
`p mod 4n_p`. A proof would split p by `n_p=n` (keeping `(n/p)=−1` and
`(ℓ/p)=1` for primes `ℓ≤w`, a congruence modulo `4n∏_{ℓ≤w}ℓ`) and by
`p mod 4n`, apply a progression-uniform version of Theorem 2.2 on each
class (not stated or checked here), and bound `#{p≤N: n_p>m}` by
Brun–Titchmarsh (`≤(2+o(1))π(N)2^{−π(m)}` for `m=o(log N)`, primorial
modulus `≤N^{o(1)}`). Because the seeded moduli are `≈4n_pj`, only
`J≲ℒ^{θ}/n_p` seeded windows fit below `ℒ^θ`, so the expected outcome
is *weaker* than Cor 2.3. The second-moment lemma does not see the
advantage of seeding (no F1 at prime seeded windows; Lemma 2.1 bounds all
bad tuples). Nothing unconditional specific to X_QNR is obtained.

### 3.3 Goal 4: conditional statements

* **GRH (Assessment; proof sketch, not written out).** GRH would make
  Theorem 2.2 effective (Siegel–Walfisz → GRH-PNT in APs), with the floor
  `y=ℒ^C` for a fixed `C>2θ`: this keeps `y>Z` (roots distinct), gives
  `(J+1)MJ/y=o(1)`, and makes the GRH error `φ(a)y^{−1/2}log y→0`. This
  would remove the δ-loss
  (`c=1−θ−O(log L/L)`). It does **not** change the range `θ<θ_*` or the
  form of `d(θ)`.
* **EH / higher level (Assessment, about this argument only)**: no help. Its binding
  constraint is Lemma 12.1's `Λ=Σν(ℓ)log ℓ/ℓ≤(log X)/4`, i.e. dimension ×
  log(sifting range) ≲ level, and levels beyond X carry no information
  about integers `≤X`.
* **Proposition 3.2 (optimisation for one majorant class; PROVED as
  stated, scope limited).** Consider bounds of the constant-free form
  `X·∏_a(log z_a)^{−δ_a}` with `X=N^{1+o(1)}`, where window a contributes
  excluded primes of relative density `δ_a` up to `z_a`, under the
  *explicitly imposed* constraint `Σ_aδ_a log z_a≤ℒ`. Then every such
  bound is `≥X·e^{−ℒ/e}=N^{1−1/e+o(1)}`.

  *Proof.* Put `u_a=log z_a`, `D=Σδ_a`. By Jensen (weights `δ_a/D`),
  `Σδ_a log u_a≤D log(ℒ/D)≤ℒ/e`. ∎

  *Scope.* This says only that the Lemma-12.1-type window-sieve majorants
  used in §§1–2 cannot be pushed to count-below-one by choosing ranges.
  It is not a theorem about sieve methods in general: the Λ-condition is
  sufficient for Lemma 12.1, not necessary for every sieve; real sieve
  bounds carry per-dimension constants (`e^{O(D)}` at `D≍ℒ`), and the
  optimiser has `log z_a=e`, outside any Mertens regime. It says nothing
  against the *conditional* implications of notes Thm 71.6 / (71.44)–(71.46),
  which assume the stacking estimate H_STACK rather than derive it from
  Lemma 12.1. (Assessment: any proof of count-below-one by window
  stacking must use correlation information beyond a level-constrained
  upper sieve — which is what H_STACK postulates.)
* **No clean "ES ⇐ standard hypothesis".** X_win is a pointwise
  statement about the factorisations of `≍log p` specific integers
  `(p+a)/4`; GRH, EH, Bateman–Horn/Dickson (which go the *other* way,
  POINTWISE_SIZE Prop 8.4) and Hooley-type hypotheses control averages
  over p or over moduli. We found no standard hypothesis implying X_win
  (Assessment).

## Replay

```
PYTHONPATH=scripts uv run python scripts/xwin_checks.py halfset 399        # Lemma 1.1 orbit/selection counts
PYTHONPATH=scripts uv run python scripts/xwin_checks.py lemma11 63 20000   # Lemma 1.1 on all x<=2e4, a<=63 (~10 min)
PYTHONPATH=scripts uv run python scripts/xwin_checks.py rho 47 16 20000 1  # Lemma 2.1 Monte Carlo -> data/xwin/rho_a47_k16.txt
PYTHONPATH=scripts uv run python scripts/pointwise_size_amin.py census 1000000   > data/xwin/amin_census_1e6.json
PYTHONPATH=scripts uv run python scripts/pointwise_size_amin.py census 10000000  > data/xwin/amin_census_1e7.json
uv run python scripts/xwin_tail_table.py data/xwin/amin_census_1e6.json data/xwin/amin_census_1e7.json data/pointwise_size/window/amin_census_1e8.json
```
All checks exit non-zero on a violation. Run heavy modes under
`ulimit -v 8000000` and `timeout`.
