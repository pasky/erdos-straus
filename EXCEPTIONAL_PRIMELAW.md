# EXCEPTIONAL_PRIMELAW — prime-only majorants over all forced-class mixtures (task O22)

Status: **checkpoint 1 (O22), in progress.** Labels follow `DISCOVERIES.md`.
PROVED means proved in this file, internal checks only, not refereed.

Notation follows `EXCEPTIONAL_KARY2.md` (K2), `EXCEPTIONAL_KARY.md` (EK),
`EXCEPTIONAL_TWIN.md` (ETw), `EXCEPTIONAL_THETA.md` (ET) and
`EXCEPTIONAL_NONCRT.md` (NC). ElT = Elsholtz–Tao, J. Aust. Math. Soc. 2013.

## 1. Setting: prime majorants and the unit measure

Let 𝔊 be a finite family of ℛ(M)-, (a,D)-, Case-A and selector classes
(K2 Definition 2.0; arbitrary moduli), and `𝒜 = 𝒜(𝔊) ⊂ ℤ` its avoider set.
Every exceptional prime (a prime p with no ES solution) lies in 𝒜, since
the first three types are forced (K2 §2) — selector classes aside, which a
method adds deliberately.

**Definition 1.1 (prime majorant).** A *prime majorant* of 𝒜 is a finite
combination `ν = Σ_i a_i 1[n ≡ b_i (mod d_i)]` such that, for all primes p
outside a finite set,

    ν(p) ≥ 0,      and      ν(p) ≥ 1 if p ∈ 𝒜.

Its *level* is `max_i Σ_{ℓ | d_i, ℓ > W} log ℓ` (K2 Thm 5.1; W the absolute
constant there). The method's count is `Σ_{p ≤ N} ν(p)`, evaluated by prime
equidistribution.

Let L be the lcm of all `d_i` and all moduli of 𝔊. `E*` is the uniform
probability on `(ℤ/L)^×`; `E*ν` does not depend on the choice of common
period L.

**Lemma 1.2 (Dirichlet reduction; PROVED).** ν is a prime majorant of 𝒜 iff

    ν ≥ 0 on every reduced class mod L,   ν ≥ 1 on every reduced class mod L contained in 𝒜.

*Proof.* ν and 𝒜 are L-periodic, so every class mod L is either contained
in 𝒜 or disjoint from it, and ν is constant on it. A reduced class contains
infinitely many primes (Dirichlet), so finitely many exceptions cannot hide
it. Conversely every prime `p ∤ L` lies in a reduced class. ∎

No hypothesis on the family is needed (NC Lemma 3.1 needed
`|F_ℓ(c)∖{0}| < ℓ−1` only for the ET Step-0 slice reduction, which is not
used here). So the prime-majorant LP is

    min E*ν   over ν with  ν ≥ 0 on (ℤ/L)^×,  ν ≥ 1 on 𝒜 ∩ (ℤ/L)^×,  level ≤ λ.      (1.1)

**Selector classes are invisible under E*.** A selector class `0 mod p`,
`p | L`, contains no unit, so adding or removing it does not change
`𝒜 ∩ (ℤ/L)^×`. Primality is built in for every prime of L at once; this is
the "selector classes for all small primes" of K2 review 2, D4 comment, and
more (all p | L, not only p ≤ W).

**Lemma 1.3 (CRT product; PROVED).** Write `L = Q₀ · Π_{ℓ > W} ℓ^{E_ℓ}` with
Q₀ W-smooth. Under E*, the coordinates `n mod Q₀` (uniform on `(ℤ/Q₀)^×`)
and `y_ℓ = n mod ℓ^{E_ℓ}` (uniform on `Ω*_ℓ := (ℤ/ℓ^{E_ℓ})^×`) are
independent. A residue class `b mod ℓ^v` (`v ≤ E_ℓ`) has `E*`-probability
`1/φ(ℓ^v) = (ℓ/(ℓ−1))ℓ^{−v}` if `ℓ ∤ b`, and 0 if `ℓ | b`.

*Proof.* `(ℤ/L)^× ≅ (ℤ/Q₀)^× × Π_ℓ (ℤ/ℓ^{E_ℓ})^×` by CRT, and the uniform law
on a product of finite groups is the product of the uniform laws. A unit
mod `ℓ^{E_ℓ}` reduces to a unit mod `ℓ^v`, and each unit mod `ℓ^v` has
`φ(ℓ^{E_ℓ})/φ(ℓ^v)` lifts. ∎

So (1.1) is K2's LP with every alphabet `ℤ/ℓ^{E_ℓ}` replaced by its unit
group, and the base `ℤ/Q₀` replaced by `(ℤ/Q₀)^×`. §2 checks that every
ingredient of K2 Thm 5.1 survives this replacement.

## 2. The ingredients of K2 Theorem 5.1 under the unit measure

Fix W (absolute, `W ≥ 16`, enlarged below if needed). Enlarge L so that
`8P_W | L`, and let `Q₀` be the W-smooth part of L (so `Q₀` is a multiple
of K2's `Q₀`; K2 Lemma 2.3 holds verbatim for it, since (R1)–(R2) and the
R-term do not depend on the exponents in `Q₀`). For the primes `ℓ > W`
dividing L, `y_ℓ = n mod ℓ^{E_ℓ} ∈ Ω*_ℓ`, `U*_ℓ` uniform on `Ω*_ℓ`, and
`U* = E*` (Lemma 1.3).

### 2.1 The base

**Lemma 2.1 (unit-square base under E*; PROVED).** Let `R = R_W^□ ⊂ ℤ/Q₀`
(K2 Lemma 2.3: unit square mod every `p^e ∥ Q₀`). Then:
1. `R ⊆ (ℤ/Q₀)^×`, and (R1) holds: no `c ∈ R` lies in a W-smooth class of
   𝔊 of any of the four types.
2. `log(φ(Q₀)/|R|) = (π(W) + 1)·log 2 ≤ 2W`.
3. (R2) holds unchanged: under the uniform law on R residues at distinct
   primes are independent and `P(c ≡ a (mod p^e)) ≤ γ(p)/p^e`.
4. If `g ≥ 0` on `(ℤ/Q₀)^×`, then `E_{(ℤ/Q₀)^×} g ≥ (|R|/φ(Q₀))·E_R g`.

*Proof.* 1. Unit squares are units; (R1) is K2 Lemma 2.3(1), which uses
only Lemmas 2.1–2.2 of K2 (no square in an ℛ(M)-, (a,D)- or Case-A class)
and the fact that `0 mod p` contains no unit. 2. Mod `p^e`, p odd, the
unit squares are half of the units; mod `2^e`, `e ≥ 3`, a quarter. By CRT
`φ(Q₀)/|R| = 4·2^{π(W)−1}`. 3. Unchanged (R is unchanged). 4. R is a
subset of `(ℤ/Q₀)^×` and `g ≥ 0`. ∎

The R-term is *smaller* than in K2 (`(π(W)+1)log 2` instead of
`3log 2 + Σ_{3≤p≤W}log(2p/(p−1))`), and smaller than NC Thm 3.2's
`log(P/φ(P))`-type selector term, which is 0 here but would be replaced by
the unit-square restriction anyway.

### 2.2 The abstract sequential theorem under E*

**Proposition 2.2 (EK Thm 4.1 / ETw Thm 2.3′ for prime majorants; PROVED).**
Take blocks `V_1, …, V_J` of the primes `ℓ > W` of L, laws `Π_j(h)`, maps
`Y_j` and costs `Φ_j ≥ 0` as in EK Thm 4.1, but with every alphabet
`Ω_ℓ = ℤ/ℓ^{E_ℓ}` replaced by `Ω*_ℓ` and U by `U*`, so that (S_w) reads:
for every λ-level `f ≥ 0` on `Ω*_{V_j}`,
`E_{U*} f ≥ E_{ω~Π_j(h)}[e^{−Φ_j} f(Y_j)]`. Let `Q'` be the history law
(base uniform on R, then the blocks). If `𝔏 = Q'(final history ∉ 𝒜) ≤ 1/2`,
every prime majorant ν of level λ satisfies

    log(1/E*ν) ≤ log(φ(Q₀)/|R|) + log 2 + 2 Σ_j E_{Q'}Φ_j(H_{<j}, ω_j).

*Proof.* Put `g_j(h) = E*[ν | H_{<j} = h]` for unit histories h. Three
points of the EK/ETw proof need checking.
* `g_j ≥ 0`: it is an average of ν over units, and ν ≥ 0 on units
  (Lemma 1.2).
* `f(y) = g_{j+1}(h, y)` is λ-level on `Ω*_{V_j}`: under `U*` the
  coordinates are independent (Lemma 1.3), so a term
  `a_i 1[n ≡ b_i (d_i)]` conditions to `a_i·(factor fixed by h)·
  1[y_T ≡ b_i]·(U*-probability of the later coordinates)`, with
  `T = {ℓ ∈ V_j : ℓ | d_i}`, a function of `y_T`.
* `g_{J+1} ≥ 1_𝒜` on unit histories: the final history fixes `n mod Q₀`
  and every `y_ℓ`, hence fixes membership in 𝒜 (all moduli of 𝔊 divide
  L). Since `Q₀ · Π_ℓ ℓ^{E_ℓ} = L`, the final history is `n mod L`, so
  `g_{J+1} = ν` there, which is `≥ 1` on the units of 𝒜 by Lemma 1.2.

The downward induction is then verbatim, ending at
`E*ν = E_{(ℤ/Q₀)^×} g_1 ≥ (|R|/φ(Q₀))E_R g_1` (Lemma 2.1(4)), and the
Jensen step `E_{Q'}[1_𝒜 e^{−S}] ≥ ½e^{−2E S}` is unchanged. ∎

**The three step types are arithmetic-free.**
* *Singleton* (ETw Prop 4.1): `E_{U*} f ≥ (1−p*_ℓ)E_σ f` for `f ≥ 0`, σ
  uniform on `Ω*_ℓ ∖ F_ℓ`; cost `−log(1−p*_ℓ) ≤ (4/3)p*_ℓ` when light,
  0 when heavy (`p*_ℓ = U*_ℓ(F_ℓ)`).
* *Sequential* (EK Thm 2.5, Cor 2.6): stated for any finite alphabets
  `Ω_ℓ` and any product law; take `Ω*_ℓ`, `U*_ℓ`. Cor 2.6's cost
  `d log(C₀(E M + 4d)/d) + (4/3)d + ½log(22d+22) + 3` is unchanged, with
  `M = Σ_{ℓ light} p*_ℓ`.
* *Linear* (ETw Lemma 4.2, Cor 4.3): Lemma 4.2 is stated for finite state
  spaces with independent laws; the in-block capped law has one-coordinate
  marginals that are mixtures of `U*_ℓ` conditioned on sets of
  `U*_ℓ`-measure `≥ 1 − δ_ℓ`, so `ε_ℓ ≤ 2δ_ℓ`, TV defect `≤ δ_ℓ`; cost
  `2log(1 + 3e^{−λ/4})`.
* *Above `e^λ`:* a level-λ term contains no prime `> e^λ`, so f does not
  depend on those coordinates; cost 0.
* *Leak* (EK Lemma 2.1(1), ETw Lemma 2.1′): every class is decided at its
  top prime; a light top is avoided, so
  `𝔏 ≤ Σ_{ℓ>W} E_{Q'}[p*_ℓ 1{p*_ℓ > δ_ℓ}] ≤ Σ_ℓ ℓ^{1/2}E_{Q'}p*_ℓ²`.

So the whole difference from K2 is in the *numbers* `p*_ℓ`, i.e. in the
first and second moments (§2.3–2.4).

### 2.3 Inflation and first moments

Put `γ*(p) = γ(p)` for `p ≤ W` (K2 Lemma 2.3(3)) and

    γ*(ℓ) = (ℓ/(ℓ−1)) · (1 − ℓ^{−1/2})^{−1}        (ℓ > W),

`Γ*(m) = Π_{p | m} γ*(p)`.

**Lemma 2.3 (inflation; PROVED).** For every m and b,
`Q'(n ≡ b (mod m)) ≤ Γ*(m)/m`. Moreover, for `ℓ > W ≥ 16`, with
`x = ℓ^{−1/2} ≤ 1/4`:

    1 ≤ ℓ/(ℓ−1) ≤ γ*(ℓ),   γ*(ℓ) − 1 ≤ 2ℓ^{−1/2},   γ*(ℓ)² ≤ 1 + 5ℓ^{−1/2},   γ*(ℓ) ≤ 3.

Γ* is submultiplicative and `Γ*(m) ≤ 8·3^{ω(m)}`.

*Proof.* Chain rule as in EK Lemma 4.2(1): given the past, `y_ℓ` has
density `≤ (1−δ_ℓ)^{−1}` w.r.t. `U*_ℓ` (EK Lemma 2.1(2)), and
`U*_ℓ` gives a class mod `ℓ^v` mass `≤ (ℓ/(ℓ−1))ℓ^{−v}` (Lemma 1.3); at the
base use Lemma 2.1(3). The inequalities:
`γ*(ℓ) = 1/((1−x)(1−x²))`, so
`γ* − 1 = (x + x² − x³)/((1−x)(1−x²)) ≤ x/(1−x)² ≤ (16/9)x ≤ 2x`;
then `γ*² ≤ (1+2x)² = 1 + 4x + 4x² ≤ 1 + 5x` as `x ≤ 1/4`. ∎

K2 uses the large-prime weight `γ'(ℓ) = (1−ℓ^{−1/2})^{−1}` only through
these four facts: `γ' ≥ 1` (EK Lemma 4.2′ Step 1),
`h(ℓ) = γ'(ℓ) − 1 ≤ 2ℓ^{−1/2}` (EK 4.2′ Step 2, K2 Lemma 3.6, ET
Lemma 3.7's γ-weight clause), `γ'² ≤ 1 + 5ℓ^{−1/2}` (K2 Lemma 3.2 tail)
and the hypothesis `F(p) ≤ κ + Hp^{−1/2}` of K2 Lemma 3.1 for
`F ∈ {Γ, Γ², τΓ², τ²Γ², τ⁵Γ², τ⁵Γ}` (all follow from the first three with
the same κ and a possibly larger absolute H). Lemma 2.3 gives all of them
for γ*.

**Lemma 2.4 (first moment under E*; PROVED; Case-A part uses ElT Prop 1.4).**
Let 𝔘 be the universe of classes of the four types and

    𝔐*(y) = Σ_{C ∈ 𝔘, W < P(C) ≤ y} Γ*(G)/G.

Then for every block V of primes `> W` and every family 𝔊 ⊆ 𝔘,
`E_{Q'} Σ_{ℓ∈V} p*_ℓ ≤ 𝔐*(max V)`, and
`𝔐*(y) ≤ K₃*(W)(log y)³(log log y)³` for `y ≥ y₀(W)`.

*Proof.* *Step 1.* A class with top `ℓ ∈ V`, modulus `G = qℓ^v`,
`P(q) < ℓ`, adds to `p*_ℓ` at most `U*_ℓ(b mod ℓ^v) ≤ (ℓ/(ℓ−1))ℓ^{−v}`
(0 if `ℓ | b`; in particular selector classes add 0), and only if
`n ≡ b (mod q)` holds for the history before ℓ, which has
`Q'`-probability `≤ Γ*(q)/q` (Lemma 2.3). Since
`(ℓ/(ℓ−1)) ≤ γ*(ℓ)`, the product is `≤ Γ*(G)/G`. Sum over classes.
*Step 2.* K2 Lemmas 3.1–3.6 and Cor 3.7 with Γ replaced by Γ*: by the
remark after Lemma 2.3 every hypothesis they place on Γ holds for Γ*,
with constants depending on W only through the Euler factors at `p ≤ W`,
which are unchanged. ∎

### 2.4 Second moments and the leak

**Lemma 2.5 (second moment and leak under E*; PROVED, no external input).**
For every prime `ℓ > W`, `E_{Q'} p*_ℓ² ≤ C(W)ℓ^{−7/4}(log ℓ)^c` with
`C(W) ≤ C(log W)^c`. Hence there is an absolute `W₀*` such that for
`W ≥ W₀*`, every family 𝔊 ⊆ 𝔘 and the block structure of §3, `𝔏 ≤ 1/2`.

*Proof.* By Lemma 1.3, `p*_ℓ ≤ Σ_{v≥1}(ℓ/(ℓ−1))ℓ^{−v}N_{ℓ,v} ≤ 2Σ_v ℓ^{−v}N_{ℓ,v}`,
with `N_{ℓ,v}` as in K2 §4 (classes whose residue mod `ℓ^v` is not a unit
contribute 0 and may be kept or dropped; selector classes contribute 0).
K2 Lemma 4.1 holds with Γ* (it uses only `Q'(class mod m) ≤ Γ*(m)/m`,
submultiplicativity, and Lemma 3.1 with `F = Γ*`, κ = 1). K2 Lemma 4.2
holds with Γ* (Lemma 3.1 with `F = τ²Γ*², τ⁵Γ*², τ⁵Γ*`; the pointwise
bounds use `Γ*(q) ≤ 8·3^{ω(q)}`). K2 Lemma 4.3's Minkowski step then gives
the bound with an extra factor 4, and the leak sum
`Σ_{ℓ>W}ℓ^{1/2}E p*_ℓ² ≪ W^{−1/4}(log W)^{3c+2}`. ∎

## 3. The cap for prime majorants

**Theorem 3.1 (prime-majorant cap for all forced-class mixtures; PROVED;
the Case-A part uses ElT Prop 1.4, published, not re-proved).** There are
absolute constants `W, λ₀, C` such that the following holds. Let 𝔊 be any
finite family of ℛ(M)-, (a,D)-, Case-A and selector classes, mixed
arbitrarily, with arbitrary moduli, and let ν be a prime majorant of
`𝒜(𝔊)` (Definition 1.1) of level `λ ≥ λ₀`. Then

    log(1/E*ν) ≤ C λ^{3/4}(log λ)^{3/4}.

If every modulus of 𝔊 satisfies `G ≤ P(G)^{1+B}` (B fixed), then
`log(1/E*ν) ≤ C(B)λ^{3/4}` for `λ ≥ λ₀(B)`. Families without Case-A
classes use no external input. Constants are astronomically large (as in
K2 §0); the statement is asymptotic only.

*Proof.* By Lemma 1.2, ν is feasible for (1.1). Apply Proposition 2.2
with K2 Thm 5.1's blocks, in increasing order of primes:
`s₁ = λ^{1/4}(log λ)^{−3/4}`; singletons on `(W, e^{s₁}]`; sequential
blocks `V_i = {2^is₁ < log ℓ ≤ 2^{i+1}s₁} ∩ (·, e^{λ/2}]`; one linear
block `(e^{λ/2}, e^λ]`; singletons above `e^λ`. Every class of 𝔊 with
`P(G) > W` is decided at its top prime; W-smooth classes are avoided by
the base (Lemma 2.1(1)). `𝔏 ≤ 1/2` by Lemma 2.5 (W ≥ W₀*).

Costs, with `𝔐*(y) ≤ K₃*(log y)³(log log y)³` (Lemma 2.4):
* base: `(π(W)+1)log 2 + log 2` (Lemma 2.1(2));
* singletons: `2·(4/3)Σ_{W<ℓ≤e^{s₁}}E_{Q'}p*_ℓ ≤ (8/3)𝔐*(e^{s₁})
  ≤ (8/3)K₃*λ^{3/4}(log λ)^{3/4}`;
* block `V_i`, `s = 2^is₁`, `d_i = ⌊λ/s⌋`: by EK Cor 2.6 on the unit
  alphabets and Jensen, `E Φ_i ≤ d_i log(C₀(E M_{V_i}+4d_i)/d_i) +
  (4/3)d_i + ½log(22d_i+22) + 3` with `E M_{V_i} ≤ 𝔐*(e^{2s})`; the
  arithmetic of K2 §5 is unchanged, giving
  `2Σ_iEΦ_i ≤ Cλ^{3/4}(log λ)^{3/4} + O(log²λ)`;
* linear block `2log(1+3e^{−λ/4})`; above `e^λ`: 0.

Sum, and absorb the W-terms into C. For bounded B: K2 Thm 5.2's proof
(`s₁ = λ^{1/4}`, first moment `≤ C(B)(log y)³` by dropping smoothness
over `G ≤ y^{1+B}`) with Γ* in place of Γ; its body sums use only the
facts listed after Lemma 2.3. ∎

**Remark 3.2 (what Theorem 3.1 adds to NC Thm 3.2).** NC Thm 3.2 had the
same conclusion (with `λ^{3/4}`) for ET Cor 3.4 prime-slice families
(dominant prime, `C < 1`, one slice prime per modulus), through ET's
product/fibre argument. Theorem 3.1 covers every mixture of the four
types: composite moduli with any number of large primes, prime-power
tops, η-twins, no B (at the price `(log λ)^{3/4}`), (a,D)- and Case-A
classes. The R-term `log(P/φ(P))` of NC Thm 3.2 is replaced by the
absolute `(π(W)+1)log 2`.

**Remark 3.3 (why nothing is lost).** The unit restriction acts on the
LP in two ways, and both help or are neutral.
* Forbidden classes that are non-units mod ℓ (selector classes; (a,D)
  classes `−(4D+a) mod 4ag` with ℓ | 4ag and `ℓ | 4D+a`, i.e. odd
  `ℓ | gcd(a,D)`) have `U*`-mass 0: they are free.
* Unit classes mod `ℓ^v` gain mass by `ℓ/(ℓ−1)`; this is absorbed into
  γ*, whose excess over 1 is still `O(ℓ^{−1/2})`.
The base needs no change because the K2 base already consists of units:
the Mordell/Jacobi argument (K2 Lemmas 2.1–2.2) says forced classes
contain no *unit* square, which is exactly what a unit-supported base
needs.

## 4. Reading for prime-law methods

### 4.1 Coefficient budget ⇒ level, under E*

**Lemma 4.1 (PROVED).** Let ν be a prime majorant of `𝒜(𝔊)` with
`T = Σ_i|a_i|`, and suppose every prime `ℓ > W` dividing a modulus of 𝔊
satisfies `log ℓ ≤ Λ₀`. Put `S = log(1/E*ν)`. Then for every λ there is
a prime majorant ν' of level `≤ λ`, all of whose moduli divide
`L_𝔊 = lcm(8P_W, moduli of 𝔊)`, with

    E*ν' ≤ E*ν + C·T·e^{Λ₀−λ}·log(λ + 3).

In particular some `λ ≤ Λ₀ + log T + S + 2log log(Λ₀ + log T + S + 16) + C'`
gives `E*ν' ≤ 2E*ν`.

*Proof.* *Projection.* Terms `1[n ≡ b_i (d_i)]` with `gcd(b_i,d_i) > 1`
vanish on units; drop them (ν is unchanged on units, Lemma 1.2). For a
unit `b_i`, average over the units `n'` with `n' ≡ n (mod L_𝔊)`:
the term becomes `κ_i 1[n ≡ b_i (mod gcd(d_i, L_𝔊))]` (or vanishes if
incompatible), with `κ_i = φ(L_𝔊)/φ(lcm(d_i, L_𝔊)) ≤ 1`, because a unit
mod `L_𝔊` has `φ(lcm)/φ(L_𝔊)` unit lifts mod `lcm(d_i,L_𝔊)`, of which at
most one is `≡ b_i (mod d_i)`. The projection `ν̄` has the same `E*`-mean,
is `≥ 0` on units and `≥ 1` on the units of 𝒜 (𝒜 is `L_𝔊`-periodic), and
`Σ|ā_i| ≤ T`.
*Coarsening* (ET Lemma 2.9 under E*). Terms of `ν̄` of level `≤ λ` stay.
A term of level `> λ`: list its primes `> W` increasingly and keep the
longest prefix of level `≤ λ`; it has level `> λ − Λ₀`. Let `r` be the
product of the kept primes and `d'` the W-smooth part of the modulus times
the kept prime powers. Negative terms are dropped, positive ones get
modulus `d'`; both raise ν̄ pointwise. The `E*`-mean rises by at most
`|a|/φ(d') ≤ |a|/φ(r) = |a|·(r/φ(r))/r`, and `r > e^{λ−Λ₀}`,
`log r ≤ λ`, so `r/φ(r) ≤ C log(λ+3)` (Mertens: `r/φ(r) ≪ log log r`). ∎

### 4.2 The cap for prime-law methods

**Corollary 4.2 (PROVED; Case-A part uses ElT Prop 1.4).** Let a method
bound the number of primes `p ≤ N` in `𝒜(𝔊)` (e.g. the exceptional primes)
by

    π(N)·E*ν + Err,     Err ≥ 0,                                   (4.1)

where ν is a prime majorant of `𝒜(𝔊)`, 𝔊 any finite mixture of the four
types with arbitrary moduli. (This is the form of every method that
evaluates `Σ_{p≤N}ν(p) = Σ_i a_i π(N; d_i, b_i)` by the Dirichlet main
term `π(N)/φ(d_i)` and bounds the errors `E(N; d_i, b_i)` in absolute
value: Siegel–Walfisz, BV, BDH, EH, GRH, any level.) Assume either

* (H1) every modulus `d_i` of ν has `Π_{ℓ | d_i, ℓ > W} ℓ ≤ N^A` (the range
  of every equidistribution input, NC Remark 3.4); or
* (H2) every prime of 𝔊 is `≤ N^A` and `T = Σ|a_i| ≤ N^A`.

Then the saving `s = log(π(N)/bound)` satisfies
`s ≤ C_A(log N)^{3/4}(log log N)^{3/4}` for N large, and
`s ≤ C_{A,B}(log N)^{3/4}` if all moduli of 𝔊 satisfy `G ≤ P(G)^{1+B}`.

*Proof.* `s ≤ S := log(1/E*ν)` since `Err ≥ 0`. Under (H1), ν has level
`≤ A log N`; apply Theorem 3.1. Under (H2), Lemma 4.1 with `Λ₀ = A log N`
gives ν' of level `λ ≤ 2A log N + S + 2log log(2A log N + S + 16) + C'`
and `log(1/E*ν') ≥ S − log 2`; Theorem 3.1 gives
`S ≤ log 2 + Cλ^{3/4}(log λ)^{3/4}`. If `S ≤ A log N` then
`λ ≪_A log N`; otherwise `λ ≤ 4S` for N large and S is bounded by an
absolute constant, a contradiction. ∎

So **prime-law methods over any mixture of forced classes cannot give
θ > 3/4**, at any equidistribution level `N^{O(1)}`, with the same
`(log log N)^{3/4}` proviso as K2 Cor 6.1 (none under bounded B).

### 4.3 Signed error accounting: under GRH even the exact prime sum is capped

(4.1) assumes `Err ≥ 0`, i.e. the errors are bounded in absolute value.
A method could instead use one-sided information (some progressions are
known to be over-populated). Under GRH this cannot help, for polynomial
coefficient budgets:

**Proposition 4.3 (CONDITIONAL on GRH for Dirichlet L-functions).** Fix
`A ≥ 1`, `ε > 0`. Let ν be a prime majorant of `𝒜(𝔊)` with every prime of
𝔊 `≤ N^A` and `T ≤ N^{1/2−ε}`, and let F be a set of primes with
`|F| ≤ N^{1/2}` such that `ν(p) ≥ 0` for every prime `p ∉ F`. Then

    Σ_{p ≤ N, p ∉ F} ν(p) ≥ (1 − o(1))·li(N)·E*ν,

and `log(li(N)/Σ_{p≤N,p∉F}ν(p)) ≤ C_A(log N)^{3/4}(log log N)^{3/4}`.
So every valid bound `#{p ≤ N : p ∈ 𝒜} ≤ Σ_{p≤N,p∉F}ν(p) + |F|`, however
its error terms are evaluated (signed, exact), saves at most that much.

*Proof.* Under GRH, `π(x; q, a) = li(x)/φ(q) + O(x^{1/2}log x)` uniformly
for `q ≤ x`, `(a,q) = 1` (partial summation from the GRH bound
`ψ(x;q,a) = x/φ(q) + O(x^{1/2}log²x)`); for `q > x` the same holds
trivially, as both terms are `≤ 1 + li(x)/q ≤ 2`. Terms with
`gcd(b_i,d_i) > 1` have `π(N;d_i,b_i) ≤ 1` and `E*`-mass 0. Hence

    Σ_{p≤N} ν(p) = li(N)E*ν + O(T N^{1/2} log N),

using `Σ_{unit terms} a_i/φ(d_i) = E*ν` (Lemma 1.3). Removing F changes the
sum by at most `|F|·max|ν| ≤ N^{1/2}T`. Both errors are `O(N^{1−ε}log N)`.
By Lemma 4.1 (Λ₀ = A log N, log T ≤ log N) and Theorem 3.1, as in
Cor 4.2 (H2), `E*ν ≥ exp(−C_A(log N)^{3/4}(log log N)^{3/4})`, so
`li(N)E*ν ≥ N^{1−ε/2}` for N large, and the errors are `o(li(N)E*ν)`. ∎

Unconditionally the analogue fails for a trivial reason: the best
unconditional error terms (Siegel–Walfisz, Vinogradov–Korobov, BV on
average) are far larger than `π(N)e^{−(log N)^{3/4}}` (NC Remark 3.4). An
unconditional prime-law method therefore cannot even reach the main
term, and Corollary 4.2 is the relevant statement.

### 4.4 Sieve-detected primality: NC Theorem 3.3 without loss

NC Thm 3.3 handled *integer* majorants that are `≥ 1` only on
`𝒜 ∩ {(n, P(z)) = 1}` and paid `O((log log N)²)`. In the K2 framework this
is free: `𝒜(𝔊) ∩ {(n,P(z)) = 1} = 𝒜(𝔊 ∪ {0 mod p : p ≤ z})`, and selector
classes are one of the four types. So K2 Thm 5.1 / Cor 6.1 apply directly,
for every mixture, with no extra term and no level hypothesis on the
augmented system beyond K2's own (K2 Remark 5.4 is the case of the 3/4
note). Under E* (this file) the selector classes are not even needed.
