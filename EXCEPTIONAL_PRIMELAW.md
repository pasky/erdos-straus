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
