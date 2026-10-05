# EXCEPTIONAL_INTERFREQ2 — hybrid methods: small classes exact, large classes trivial (task O25)

Status: **in progress (O25).** Labels follow `DISCOVERIES.md`. PROVED means
proved in this file, internal checks only. No θ > 3/4 is claimed. Notation
as in `EXCEPTIONAL_INTERFREQ.md` (IF below), `EXCEPTIONAL_KARY2.md` (K2).

## 1. The hybrid class, precisely

Fix N ≥ 2. For a finite representation
`ν = Σ_i a_i 1[n ≡ b_i (mod d_i)]` split the index set into
`𝒮 = {i : d_i ≤ N/2}` (small) and `𝓛 = {i : d_i > N/2}` (large), and write
`ν_𝒮, ν_𝓛` for the two partial sums. For a class `b mod d` put
`c(b,d) = #{1 ≤ n ≤ N : n ≡ b (d)}`, so `l(d) := ⌊N/d⌋ ≤ c(b,d) ≤ ⌈N/d⌉ =: u(d)`
and both values occur.

**Definition 1.1 (position-blind charge).** A function β(a,d) is a
*position-blind charge* if `β(a,d) ≥ a·c(b,d)` for every residue b. The
least one is `β*(a,d) = a·u(d)` for a > 0 and `a·l(d)` for a < 0.
For d > N this is "a class meets [1,N] at most once" (charge a⁺);
for N/2 < d ≤ N "once or twice".

**Definition 1.2 (hybrid method).** A *hybrid method* for an avoider set
𝒜 ⊂ ℤ takes a majorant ν (ν ≥ 0 on ℤ, ν ≥ 1 on 𝒜) with a representation,
evaluates the small part by *any* valid upper bound for `Σ_{n≤N}ν_𝒮(n)`
(the exact value being the least possible), and charges each large term a
position-blind charge. Its bound satisfies

    B ≥ B_hyb(ν) := Σ_{n≤N} ν_𝒮(n) + Σ_{i∈𝓛} β*(a_i, d_i) ≥ Σ_{n≤N} ν(n).   (1.1)

The usual form `N/d + O(1)` (IF Rem 2.6: charge `a_iN/d_i + |a_i|`) is a
position-blind charge, hence dominates β*. A cutoff `D_s < N/2` is also
covered: classes in `(D_s, N/2]` charged blindly cost at least their exact
count. So it suffices to bound

    H*(N; 𝒜) := inf_{ν, representation} B_hyb(ν).

## 2. LP duality for H*

No projection to the family modulus is used: averaging over fibres mod Q
preserves Eν but not interval counts. Instead fix any common multiple Q′ of
the period Q of 𝒜 and all moduli of the representation, and work on ℤ/Q′.

**Proposition 2.1 (dual of the hybrid; PROVED).** Let 𝒜 be Q-periodic,
`Q | Q′`, and `λ_N(n) = #{1 ≤ m ≤ N : m ≡ n (Q′)}` on ℤ/Q′. Let 𝔐(Q′) be the
set of measures μ on ℤ/Q′ with

    μ ≥ 0;   μ(s) = λ_N(s)  for every class s mod d | Q′, d ≤ N/2;
             l(d) ≤ μ(s) ≤ u(d)  for every class s mod d | Q′, d > N/2.     (2.1)

(a) (weak duality) If all moduli of a representation of ν divide Q′, then
`B_hyb(ν) ≥ μ(𝒜)` for every μ ∈ 𝔐(Q′).
(b) (strong duality) `min{B_hyb(ν) : moduli | Q′} = max{μ(𝒜) : μ ∈ 𝔐(Q′)}`.
Hence `H*(N;𝒜) ≥ inf_{Q′} max_{μ∈𝔐(Q′)} μ(𝒜)`, Q′ over multiples of Q.

*Proof.* (b) With all moduli dividing Q′ this is a finite LP. ν ≥ 0 and
ν ≥ 1 on 𝒜 is `ν ≥ 1_𝒜` pointwise on ℤ/Q′. Write large coefficients as
`a⁺ − a⁻` with cost `u a⁺ − l a⁻`; small coefficients are free with cost
`λ_N(s)` (the exact count, since `c(b,d) = λ_N(b mod d)` for d | Q′). The
primal is feasible (ν ≡ 1) and the dual is feasible (μ = λ_N). The dual
variable of `ν(n) ≥ 1_𝒜(n)` is μ(n) ≥ 0; a free coefficient gives an
equality, `a⁺` gives `μ(s) ≤ u(d)`, `a⁻` gives `μ(s) ≥ l(d)`. Finite LP
duality. (a) is the easy half:
`B_hyb(ν) ≥ Σ_i a_i μ(s_i) = Σ_n ν(n)μ(n) ≥ μ(𝒜)` term by term. ∎

So a cap for hybrid methods is the same as a measure μ ≥ 0 that agrees
with the interval on small classes, is *position-blindly* consistent with
it on large classes, and puts mass `≥ N e^{−O(S)}` on 𝒜.

## 3. What the blind charge really is: exact count plus a wrong-sign penalty

**Lemma 3.1 (sign rule; PROVED).** Call a large class `s = b mod d`
*full* if `c(b,d) = u(d)` and *sparse* if `c(b,d) = l(d)`. For `d ∤ N`
every large class is exactly one of the two, and `u − l = 1`; for `d | N`
(i.e. d = N among large d) it is both. Then for every representation

    B_hyb(ν) = Σ_{n≤N} ν(n) + Σ_{i∈𝓛} |a_i|·1[a_i > 0, s_i sparse, not full]
                            + Σ_{i∈𝓛} |a_i|·1[a_i < 0, s_i full, not sparse].     (3.1)

*Proof.* `β*(a,d) − a·c(b,d)` is `a(u − c)` for a > 0 and `|a|(c − l)` for
a < 0; `c ∈ {l, u}` and `u − l ≤ 1`. ∎

So a hybrid method is *exact counting* plus a penalty `|a_i|` for each
large term used with the wrong sign: positive on a class that meets [1,N]
less often than possible, or negative on a class that meets it as often as
possible. For d > N: positive terms on classes through [1,N] and negative
terms on classes missing [1,N] are free. Compare IF Thm 2.5, which needs
the bound to dominate the *whole* large mass `T_>`.

**Example 3.2 (a large class counted exactly; PROVED by inspection).**
N = 20, s = 0 mod 21 (sparse, `c = 0`). Since 21 = 3·7 and 3, 7 ≤ 10,

    1[n ≡ 0 (21)] = 1[n ≡ 0 (7)] − 1[n ≡ 1 (3)] − 1[n ≡ 2 (3)]
                    + Σ_{b mod 21, 3∤b, b ∉ {7,14}} 1[n ≡ b (21)],

and the 12 classes in the last sum each meet [1,20] once (full). So the
hybrid charge of this representation is `2 − 7 − 7 + 12 = 0`, the exact count,
although the class is sparse (charged 1 if written as itself).

**Consequence (PROVED).** The natural route — a measure μ = λ_N − φ + tρ
with ρ the dual of a capped comparison problem that is *exactly* uniform on
classes of modulus ≤ N^K — is impossible already at d = N + 1 when
N + 1 = d₁d₂ with coprime d₁, d₂ ≤ N/2. In the dual of (2.1), Example 3.2's
identity forces `μ(0 mod 21) = λ_N(0 mod 21) = 0` for μ uniform-tested on all
classes mod 21 meeting [1,N] (each `≤ u = 1 = λ_N`, summing with the small
constraints to equality). In general: if a small class r mod e is a disjoint
union of full large classes, every μ ∈ 𝔐 has `μ(s) = u(d) = λ_N(s)` on each
of them. Any comparison measure must therefore deviate from uniform on
large classes in a way correlated with [1,N]. (LP check:
`scripts/interfreq2_phi_lp.py`, N = 20, exact mode, d = 21 alone infeasible
for every t > 0; d = 22 = 2·11, 11 > N/2, feasible.)

## 4. Translates are dual-feasible; what that does and does not give

Let `L₀ = lcm{d : d ≤ N/2}` (or the lcm of the small moduli dividing Q′).

**Lemma 4.1 (PROVED).** For every integer k the window measure
`μ_k = λ_{[1,N]+kL₀}` lies in 𝔐(Q′). Hence, for every representation,

    B_hyb(ν) ≥ max_k Σ_{n ∈ [1,N]+kL₀} ν(n) ≥ Σ_{n≤N} E[ν(n′) | n′ ≡ n (L₀)].

*Proof.* A small class `b mod d` (d | L₀) meets `[1,N]+kL₀` in
`c(b − kL₀, d) = c(b,d)` points. A large class meets any N consecutive
integers in `l(d)` or `u(d)` points. Weak duality (Prop 2.1(a)). ∎

So a hybrid bound is at least the count of ν on every L₀-translate of the
window: it cannot exploit the position of [1,N] modulo L₀. This does
**not** give a cap by itself: the average over translates is
`Σ_{n≤N} f(n)` with `f = E[1_𝒜 | n mod L₀]` for ν ≥ 1_𝒜, i.e. N times
the CRT density of avoiders in a random translate, which for ES families
is heuristically `e^{−c(log N)³}`; the squares, which make
`#(𝒜∩[1,N]) ≥ √N`, are not seen by translates.

**Lemma 4.2 (rigid null classes are L₀-smooth; PROVED).** If a class
`s = b mod d` has `μ(s) = 0` for every μ ∈ 𝔐(Q′), then
`e := gcd(d, L₀) > N` and the class `b mod e` misses [1,N].

*Proof.* `μ_k(s) = #{n ∈ [1,N] : n ≡ b − kL₀ (d)}`. As k varies, `kL₀ mod d`
runs over the multiples of e, so some `μ_k(s) > 0` unless no n ∈ [1,N]
satisfies `n ≡ b (e)`. If e ≤ N every class mod e meets [1,N]. ∎

Example 3.2 is such a class (e = 21 | L₀ = lcm(1..10)).

**Numerics (EVIDENCE; `scripts/interfreq2_rigid.py`, `interfreq2_rigid_points.py`,
`interfreq2_rigid_scan.py`).**
* N = 20, Q′ = 2520 = lcm(1..10): some μ ∈ 𝔐 puts *all* its mass N off
  [1,N] (so 𝔐 is far from {λ_N}). Per-point maxima: the only rigid-null
  points are the 120 multiples of 21, i.e. Example 3.2's class.
* Rigid-null sparse classes `b mod e`, e | lcm(1..N/2), N < e ≤ 3N: N = 20:
  e = 21 {0}, e = 42 {0, 21}; N = 30: none; N = 40: e = 42 {0, 41},
  e = 45 {43}, e = 84, 90 (lifts). They sit just above N; the summed
  density is ≤ 0.14 in these ranges.
