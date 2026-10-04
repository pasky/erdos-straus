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
