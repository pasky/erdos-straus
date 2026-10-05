# EXCEPTIONAL_INTERFREQ2 — hybrid methods: small classes exact, large classes trivial (task O25)

Status: **checkpoint 2 (O25; §§9–10 added after the parent's follow-up).** Labels follow `DISCOVERIES.md`. PROVED means
proved in this file, internal checks only. No θ > 3/4 is claimed. Notation
as in `EXCEPTIONAL_INTERFREQ.md` (IF below), `EXCEPTIONAL_KARY2.md` (K2).

## 0. Summary

| item | statement | label |
|---|---|---|
| Def 1.2 | hybrid = exact (or any valid) count of the small part (moduli ≤ N/2) + least position-blind charge `β*(a,d) = a⌈N/d⌉` (a>0), `a⌊N/d⌋` (a<0) on large terms; IF's `aN/d + |a|` dominates it | definition |
| Prop 2.1 | LP dual: `min B_hyb = max μ(𝒜)` over μ ≥ 0 on ℤ/Q′ agreeing with λ_N on small classes and with `⌊N/d⌋ ≤ μ(s) ≤ ⌈N/d⌉` on large ones | PROVED |
| Lemma 3.1 | **sign rule**: `B_hyb = Σ_{n≤N}ν + (wrong-sign mass)`; positive terms on classes meeting [1,N] maximally ("full") and negative terms on "sparse" classes are counted exactly | PROVED |
| Ex 3.2 | N = 20: `1[0 mod 21]` has a representation with hybrid charge 0 (12 full patches mod 21 + classes mod 3, 7). Hence no bound `B_hyb(ν) ≥ c·N·Eν` (c > 0) holds for ν ≥ 0, and IF Thm 2.5's Selberg accounting cannot extend to hybrids as is | PROVED |
| Lemma 4.1, 6.1 | `B_hyb(ν) ≥ Σ_{n∈W}ν` for every *twisted window* W = φ([1,N]), φ componentwise affine preserving the small-class profile (translates by lcm(1..N/2)-multiples, reflections on primes in (N/4, N/2], any affine map on primes > N/2) | PROVED (that averaging over them cannot give the cap: Assessment only) |
| Lemma 4.2 + numerics | a class on which every dual μ vanishes (equivalently, some representation of it has hybrid charge 0) has `gcd(d, L₀) > N` with `b mod gcd` missing [1,N]; sampled scan (N ≤ 40, e ≤ 3N, e | L₀): such e occur only just above N, summed density ≤ 0.14 | PROVED / EVIDENCE |
| Cor 5.1 | cap `S_A + O(log(1+c))` for hybrids whose free mass (patches through [1,N] with d > N, right-signed terms with N/2 < d ≤ N) is ≤ c·B, c ≤ e^{O(S_A)}; wrong-signed and free negative terms unrestricted | PROVED (from IF Thm 2.5) |
| Thm 5.2 | **conditional cap**: if a *flat minorant* exists (Flat: F ≤ 1_{[1,N]}, uniform on classes mod d ≤ N/2, F(s) ≥ M/d + s₀ on classes mod d > CN through [1,N], ≥ M/d − 1 on the others, bounded deviation on (N/2, CN]), then every hybrid with right-signed mass on (N/2, CN] at most c·B saves `≤ C(log N)^{3/4}(log log N)^{3/4} + log((1+Δ(1+c))/t)`; patches above CN are unrestricted. Flat is needed at the given (every large) N with `s₀ ≥ N^{−A₁}`, `t ≥ e^{−S_A}`, `Δ ≤ e^{S_A}` | PROVED implication |
| Prop 9.1 | **SPW ⇒ Flat**: a spread pseudo-window R (≥ 0, exact window profile mod every d ≤ N/2, mass ≤ 1 − σ on every class of modulus > CN) yields Flat with t, s₀ ≍ σ, via `θF_S + (1−θ)(1_{[1,N]} − R)`; so SPW (constants σ, Δ₀) ⇒ the 3/4 cap of Thm 5.2 | PROVED implication |
| Lemma 9.2 | SPW ⇒ patch-cancellation inequality (9.1) for all ν ≥ 0 (converse for LP truncations) | PROVED |
| §9 | SPW found by LP at N ≤ 60 (σ ≈ 0.34–0.40, C = 2); big-prime re-randomisation proves the profile part but not (P2) on lcm(1..N/4)-smooth moduli; SPW itself open | EVIDENCE / Assessment |
| §5 numerics | finitely supported F satisfying Flat found by LP at the sampled parameters N ∈ {20,30,40,60,80,100}, t = 0.1, C ∈ {1.5, 2} (s₀ ≥ 0.04, Δ ≤ 1.5); C = 1 infeasible at N = 20 (rigidity); medium sign conditions on (N/2, N] compatible with s₀ = 1/3 at C = 2 (N ≤ 40, long support); periodic certificates: (N/2, N] not freeable at C = 1.5, (N/2, CN] not freeable at N = 20 | EVIDENCE (floating-point LP) |

**Verdict.** The hybrid gap of IF Rem 2.6 is *not* closed unconditionally.
It is narrowed to two precisely stated pieces:
1. (Flat) — an extremal-function statement about a single explicit LP
   (no arithmetic, no 𝒜), checked by LP at sampled N ≤ 100. Under Flat, hybrids that
   charge large classes blindly are capped at 3/4 (with the K2 log log
   loss) *whatever they do above modulus CN*.
2. Right-signed mass at moduli in (N/2, CN]. This is a genuine phenomenon:
   Example 3.2 shows that hybrids count some classes of modulus N + 1
   exactly, and imposing cost-free accounting there contradicts Flat
   numerically (finite-support LPs only). No hybrid beating 3/4 is known; in the toy LPs the
   optimal hybrid uses free mass ≈ B/2 (Cor 5.1 regime).
After §9 the analytic hypothesis is reduced further to **SPW**: a random
integer that looks exactly like a uniform element of [1,N] modulo every
d ≤ N/2 but has probability ≤ (1 − σ)/N on every class of modulus > CN.
(H_eq) of IF §4 plays no role here: hybrids never evaluate per-frequency
sums. No θ > 3/4 is claimed or suggested.

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

*Scope (review R25, m1).* The charge is per term. A method that charges a
*group* of large classes of one modulus by the worst case of their joint
count over shifts of the window (shift-blind but not term-blind) can pay
less than Σβ*; such grouped charges are outside Definition 1.2. Lemma 4.1-
type duals cover them only when the group is invariant under the shifts
used.

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

**Rigidity (PROVED).** If a small class r mod e is the disjoint union of
large classes s_1, …, s_k that are all full, then every μ ∈ 𝔐(Q′) has
`μ(s_j) = u(d) = λ_N(s_j)` for all j (the `μ(s_j) ≤ u` sum to `μ(r mod e) =
λ_N(r mod e) = Σ_j u`). In Example 3.2 this gives `μ(r mod 21) = 1` for every
r ∈ [1,20] (via the classes mod 7 with r ≢ 0 and mod 3), hence
`μ(0 mod 21) = λ_N(0 mod 7) − μ(7) − μ(14) = 0`: every μ ∈ 𝔐(Q′) vanishes on
`0 mod 21` (N = 20, 21 | Q′).

**Consequence (PROVED).** Let `μ = λ_N − φ + tρ` with `φ ≤ λ_N` pointwise,
`t > 0`, ρ ≥ 0, `tρ − φ` of zero mass on every small class, and ρ exactly
uniform (mass `N/d` per class) on all classes of modulus ≤ N^K (K ≥ 2), the
form produced by dualising a capped comparison problem. Then μ ∉ 𝔐(Q′)
whenever N + 1 = d₁d₂ with coprime d₁, d₂ ≤ N/2 (and N+1 | Q′): off [1,N]
we have `μ ≥ tρ`, so `μ(0 mod (N+1)) ≥ tN/(N+1) > 0`, contradicting the
rigidity above (the argument for N = 20 uses only that the rows mod d₁ and
d₂ other than the one through 0 are full; this holds for d = N+1 because
every class mod N+1 except 0 meets [1,N] exactly once). Any comparison
measure must deviate from uniform on large classes in a way correlated
with [1,N]. (LP check: `scripts/interfreq2_phi_lp.py`, N = 20, exact mode,
d = 21 alone infeasible for every t > 0; d = 22 = 2·11, 11 > N/2,
feasible.)

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

**Lemma 4.2 (where rigid-null classes can live; PROVED).** If a class
`s = b mod d` has `μ(s) = 0` for every μ ∈ 𝔐(Q′), then
`e := gcd(d, L₀) > N` and the class `b mod e` misses [1,N].

*Proof.* `μ_k(s) = #{n ∈ [1,N] : n ≡ b − kL₀ (d)}`. As k varies, `kL₀ mod d`
runs over the multiples of e, so some `μ_k(s) > 0` unless no n ∈ [1,N]
satisfies `n ≡ b (e)`. If e ≤ N every class mod e meets [1,N]. ∎

Example 3.2 is such a class (e = 21 | L₀ = lcm(1..10)). Note that d itself
need not be L₀-smooth or close to N: every subclass `0 mod 21p` (p any
prime) inherits rigid-nullity. "Rigid-null" means every μ ∈ 𝔐 vanishes on
the class, i.e. *some* representation has hybrid charge 0; writing the class
as itself still costs 1.

**Numerics (EVIDENCE; `scripts/interfreq2_rigid.py`, `interfreq2_rigid_points.py`,
`interfreq2_rigid_scan.py`).**
* N = 20, Q′ = 2520 = lcm(1..10): some μ ∈ 𝔐 puts *all* its mass N off
  [1,N] (so 𝔐 is far from {λ_N}). Per-point maxima: the only rigid-null
  points are the 120 multiples of 21, i.e. Example 3.2's class.
* Rigid-null sparse classes `b mod e`, e | lcm(1..N/2), N < e ≤ 3N: N = 20:
  e = 21 {0}, e = 42 {0, 21}; N = 30: none; N = 40: e = 42 {0, 41},
  e = 45 {43}, e = 84, 90 (lifts). They sit just above N; the summed
  density is ≤ 0.14 in these ranges.

## 5. Caps: what Theorem 2.5 already gives, and a flat-minorant reduction

Throughout, 𝔊 is a K2 mixture with all family primes ≤ N^A, and
`S_A = C_A(log N)^{3/4}(log log N)^{3/4}` is IF Thm 2.5's mean-side bound.
Split the large terms of a representation by sign rule (Lemma 3.1):
* `W⁺` = mass of positive terms on full classes with d > N ("patches");
* `T⁻_sp` = mass of negative terms on sparse classes with d > N;
* `T_mid` = mass of right-signed terms with `N/2 < d ≤ CN` (C ≥ 1 fixed),
  and `W⁺_{>CN}` the part of W⁺ with d > CN;
* `T_wr` = wrong-signed mass (charged `|a|` by (3.1)).

**Lemma 5.0 (free negatives can be dropped; PROVED).** Deleting all
negative terms on sparse classes with d > N gives a majorant ν′ ≥ ν with
`Σ_{n≤N}ν′ = Σ_{n≤N}ν` and `B_hyb(ν′) = B_hyb(ν)`. (Such classes miss
[1,N], and β* charges them `a·l(d) = 0`.) So WLOG `T⁻_sp = 0`. ∎

**Corollary 5.1 (PROVED; from IF Thm 2.5/Rem 2.6 and (3.1)).** After
Lemma 5.0, `T_> = T_wr + W⁺ + T_mid^{(C=1)}` and `B_hyb ≥ T_wr`. Hence a
hybrid bound B saves at most `S_A + log(2 + 12(1 + c))` whenever
`W⁺ + T_mid ≤ c·B` (C = 1), and at most `S_A + log 48` whenever
`W⁺ + T_mid ≤ (N/48)e^{−S_A}`. ∎

So Corollary 5.1 does not cover representations whose *free* large mass —
positive terms on classes through [1,N], or right-signed terms at moduli
in (N/2, N] — exceeds the bound by more than `e^{O(S_A)}`. (Large free mass
alone is harmless: `ν = (1+K) − K·Σ_{b mod N} 1[b mod N] ≡ 1` has B = N and
right-signed medium mass KN. It is only a gap in the proof.) Example 3.2
is a representation with W⁺ = 12 and B = 0; the Selberg-minorant accounting of IF Thm 2.5 cannot
handle it because Selberg's F is ≈ 0 near the ends of [1,N] (a patch at
an edge point costs 1 but has F-weight ≈ 0), and by Example 3.2 *no*
inequality `B_hyb(ν) ≥ c·N·Eν` holds for all ν ≥ 0.

**Hypothesis Flat(C, t, s₀, Δ) at N.** There is F: ℤ → ℝ, absolutely
summable, with
* (F1) `F ≤ 1_{[1,N]}` on ℤ;
* (F2) `Σ_{n≡b (d)} F(n) = M/d` for all d ≤ N/2 and all b, with `M = tN`;
* (F3) `F(s) ≥ M/d + s₀` for every class s mod d > CN meeting [1,N]
  (`F(s) := Σ_{n∈s}F(n)`);
* (F4) `F(s) ≥ M/d − 1` for every class s mod d > CN missing [1,N];
* (F5) `|F(s) − M/d| ≤ Δ` for every class s mod d, `N/2 < d ≤ CN`.

(For d → ∞, (F3)–(F4) say `F ≥ s₀` on [1,N] and `F ≥ −1` off it: F is a
*flat* minorant, unlike Selberg's.)

**Theorem 5.2 (conditional cap; PROVED implication).** Assume
Flat(C, t, s₀, Δ) at N with `t, 1/Δ ≥ e^{−S_A}` and `s₀ ≥ N^{−A₁}`. Let a
hybrid bound B (Def 1.2) for 𝒜(𝔊) satisfy `T_mid ≤ c·B`, where now T_mid
is the right-signed mass at moduli in `(N/2, CN]`. Then for N ≥ N₀(A, A₁, C),

    log(N/B) ≤ S′ + log((1 + Δ(1 + c))/t),   S′ = C_{A,A₁,C}(log N)^{3/4}(log log N)^{3/4}.

Patches of modulus > CN, wrong-signed terms and free negatives are
unrestricted.

*Proof.* Lemma 5.0: WLOG `T⁻_sp = 0`. Since ν ≥ 0 and (F1),
`B ≥ B_hyb = Σ_{n≤N}ν + T_wr ≥ Σ_n F(n)ν(n) + T_wr`. Expand ν termwise; (F2) gives
`Σ_n F·ν_𝒮 = M·Eν_𝒮`. So

    B ≥ M·Eν + Σ_{i∈𝓛} [ a_i(F(s_i) − M/d_i) + |a_i|·1[i wrong] ].

Term by term, for `d_i > CN`: positive full (patch): `≥ a_i s₀` by (F3);
positive sparse (wrong): `≥ a_i(F(s) − M/d + 1) ≥ 0` by (F4); negative full
(wrong): `|a_i|(1 + M/d − F(s)) ≥ 0` because `F(s) ≤ F(n₀) ≤ 1` by (F1)
(the only point of s in [1,N] is n₀, F ≤ 0 elsewhere). For
`N/2 < d_i ≤ CN`: by (F5) the term is `≥ −Δ|a_i|` if right-signed and
`≥ (1 − Δ)|a_i|` if wrong. Hence, with `B ≥ T_wr`,

    (1 + Δ)B ≥ M·Eν − Δ·T_mid + s₀·W⁺_{>CN}.                       (5.1)

*Mass of high terms.* Put `K = 1 + Δ(1+c)`. If `KB ≥ tN` the claimed bound
holds trivially. Otherwise (5.1) and `T_mid ≤ cB` give `M·Eν < KB < tN`,
so `Eν < 1`, and the terms with d > CN (patches, wrong-signed, or dropped)
have mass `T_{>CN} ≤ W⁺_{>CN} + T_wr ≤ KB/s₀ + B < tN/s₀ + N ≤ N^{A₁+1} + N`.
Now run IF Thm 2.5's mean side (projection to the family
modulus, ET Lemma 2.9 coarsening at
`λ = max{λ₀, log(CN), Λ₀ + log max(T_{>CN},1) + S}`, `Λ₀ = A log N`; terms of
the projection with level > log(CN) come from terms with d > CN), now with
`λ ≤ (A + A₁ + 2)log N + S + λ₀`. K2 Thm 5.1 and the case analysis of K2
Cor 6.1 give `S = log(1/Eν) ≤ S′`. Then (5.1) with `T_mid ≤ cB` gives
`(1 + Δ + Δc)B ≥ tN e^{−S′}`. ∎

*Remarks.* (i) The margin s₀ enters only through `log T_{>CN}` in the level,
so polynomially small margins cost nothing in the exponent. (ii) t and Δ
enter as `log(1/t) + log(1+Δ(1+c))`, so they may degrade like `e^{−O(S′)}`.
(iii) Theorem 5.2 does not use C > 1 except through (F3)–(F5); by
Example 3.2 and Lemma 3.1's rigidity, (F3) *must fail* at some
`d ∈ (N, CN]` when N+1 = d₁d₂ with coprime `d₁, d₂ ≤ N/2`, so the moduli just
above N have to be treated as T_mid.

**Numerics for Flat (EVIDENCE; `scripts/interfreq2_flatF.py`, t = 0.1,
support [−5N, 6N], data in `data/interfreq2/flatF_scan*.txt`).** The LP
maximises the margin s₀ in (F3)–(F4) for all d > CN up to the support
length (pointwise beyond), with (F1)–(F2) exact; Δ is then measured.

| N | C = 1.5: s₀ / Δ | C = 2: s₀ / Δ | min F on [1,N] (C = 2) |
|---|---|---|---|
| 20 | 0.250 / 1.31 | 0.400 / 1.26 | 0.86 |
| 30 | 0.250 / 1.08 | 0.400 / 1.08 | 0.77 |
| 40 | 0.200 / 1.23 | 0.380 / 1.15 (L = 5N) | 0.62 |
| 60 | 0.187 / 1.10 | 0.326 / 1.17 | 0.55 |
| 80 | — | 0.255 / 1.40 | 0.45 |
| 100 | 0.044 / 1.15 | 0.167 / 1.48 | 0.35 |

Support matters: at N = 60, C = 2 the margin rises from 0.326 (support
[−5N, 6N]) to 0.372 ([−8N, 9N]), so much of the decrease is truncation.
With C = 1 the LP is infeasible at N = 20 (rigidity, Example 3.2).
*Medium moduli (corrected after review R25, M1).* Option `med` adds the
sign conditions that make right-signed terms with `N/2 < d ≤ N` cost
nothing (margin 0 there). On the short support [−5N, 6N] this forced the
margin above CN to ≤ 0; that was a **truncation artefact** at C = 2: on
[−10N, 11N] and longer the margin is 1/3 at N = 20, 30, 40 (finite-support
witnesses, `data/interfreq2/med_periodic.txt`). Rigorous statements come from
the *periodic* relaxation on ℤ/Q′ (`scripts/interfreq2_med_periodic.py`):
every F on ℤ projects to a feasible point there, and Farkas certificates are
Q′-periodic ν ≥ 0 on all of ℤ. Results at Q′ = lcm(1..N/2)·(small): C = 1.5,
N = 20: `med` forces max s = 0 (a genuine periodic certificate); C = 2,
N = 12, 16, 20: max s = 0.5, 0.4, 0.4 with `med`, i.e. no obstruction;
sign conditions on all of (N/2, CN] (`medall`): infeasible at N = 20 (the
rigid modulus 21 = N + 1 of Example 3.2), feasible (0.4) at N = 16. See §10.
The
margins decrease slowly with N; Theorem 5.2 only needs `s₀ ≥ N^{−A₁}` and
`Δ ≤ e^{S_A}`, so the trend is harmless unless it is faster than
polynomial. Independent check (`scripts/interfreq2_checks.py`): the N = 20
F satisfies (F1)–(F5) on ℤ/360360 with Δ = 1.263, s₀ = 0.400, and (5.1)
holds on 200 random ν ≥ 0. **Flat itself is not proved**: the LP
solutions are spread-spectrum functions (F ≈ 1 on [1,N], ≈ −0.3 outside)
with no visible closed form; Selberg's band-limited minorant fails (F3)
near the ends of [1,N] for every C.

## 6. Twisted windows: the symmetry group of the hybrid dual

**Lemma 6.1 (PROVED).** Let φ: ℤ/Q′ → ℤ/Q′ act componentwise affinely,
`φ(x) ≡ u_q x + v_q (mod q)` for each prime power `q ∥ Q′` (u_q units). For
d | Q′ let φ_d be the induced bijection of ℤ/d. Suppose that for every
d | Q′ with d ≤ N/2 and d ∤ N, φ_d maps `I_d = {1, …, N mod d}` (mod d) onto
itself. Then `λ_{φ([1,N])} ∈ 𝔐(Q′)`, so `B_hyb(ν) ≥ Σ_{n≤N} ν(φ(n))`.

*Proof.* `#{n ≤ N : φ(n) ≡ b (d)} = c(φ_d^{−1}(b), d) ∈ [l(d), u(d)]` for
every d, and for small d it equals `c(b,d)` because `c(·,d) = l(d) + 1_{I_d}`
is φ_d-invariant (for d | N it is constant). ∎

The admissible φ form a group G_N. It contains: translations by multiples
of L₀ (Lemma 4.1); the global reflection `x ↦ N+1−x` (which maps [1,N]
onto itself while permuting residue classes, e.g. 1 ↔ 2 mod 3 at N = 20);
the reflection on a single prime p with `N/4 < p ≤ N/2` (p divides no other
small modulus), chosen independently per such p; and arbitrary affine maps
on primes `p > N/2`. So the hybrid bound is blind to these twists of
[1,N]. *Assessment (not proved):* the subgroup generated by the listed
elements maps [1,N] to sets with the same multiset of residues as [1,N]
modulo every d dividing the part of L₀ built from primes ≤ N/4, so
averaging over it conditions on n modulo that part and is, for ES
families, heuristically CRT-small. We have not determined the full G_N or
its orbits, so we do not claim that twisted windows cannot give the cap;
we only found no way to make them do so.

## 7. Toy LPs (EVIDENCE only)

`scripts/interfreq2_hybrid_lp.py`: family on ℤ/30030, F_p = quadratic
non-residues mod p ∈ {3,5,7,11,13} (squares avoid), all classes mod divisors
of Q. Values are optimal bounds.

| N | exact #𝒜∩[1,N] | H_{Q′} (hybrid, moduli \| Q′ = Q) | IF Thm 2.5 functional `Σν + T_>` | small moduli only | N·Eν, d ≤ N |
|---|---|---|---|---|---|
| 20 | 4 | 7 | 10 | 11 | 8 |
| 30 | 5 | 11 | 12 | 12 | 11.4 |
| 40 | 6 | 13 | 17 | 17 | 11.4 |
| 60 | 7 | 17.7 | 23 | 23 | 16.7 |

H_{Q′} is the optimum for the fixed Q′ = 30030, an upper bound for H*.
At the H_{Q′} optimum (N = 20, 30) the patch mass W⁺ is 3 and 4, i.e. below B:
the optimum sits in Cor 5.1's regime. The toys are far too small to say
anything about exponents.

## 8. What would close the gap

* **Prove Flat** (for some fixed C, t, Δ and s₀ ≥ N^{−O(1)}). It is a
  statement about functions on ℤ with prescribed sums over all residue
  classes of modulus ≤ N/2 and one-sided bounds above CN. Selberg's
  band-limited minorant is useless (it vanishes at the ends of [1,N]);
  the LP optima are spread-spectrum. Equivalent form: with
  `R = 1_{[1,N]} − F`, Flat asks for R ≥ 0 on ℤ with `R(b mod d) = c(b,d) − M/d`
  for d ≤ N/2, `R(s) ≤ 1 − M/d − s₀` on full classes and `R(s) ≤ 1 − M/d` on
  sparse classes of modulus > CN, and `|c(s) − R(s) − M/d| ≤ Δ` for
  N/2 < d ≤ CN. The LP optima have R ≈ 0 on [1,N] and R spread outside:
  a "copy" of the window's small-class profile that no large class
  concentrates. We found no way to build it from (twisted) windows.
* **Medium moduli** (N/2, CN]: either a separate argument or a hybrid that
  exploits rigidity (Example 3.2) at scale. A natural first test is the
  exact-evaluation class with moduli ≤ CN (𝓘_spec(CN), C > 1), to which
  IF Thm 2.2 does not apply.

## Replay

```
PYTHONPATH=scripts uv run --with scipy --with sympy python scripts/interfreq2_checks.py data/interfreq2/flatF_N20.npy   # Ex 3.2, Lemma 4.1, (5.1) on Z/360360; ~1 min
uv run --with scipy python scripts/interfreq2_flatF.py 20 100 0.1 2 data/interfreq2/flatF_N20.npy                     # regenerates the saved F (1 s)
for a in "20 100 0.1 1.5" "20 100 0.1 2" "30 150 0.1 1.5" "30 150 0.1 2" "40 200 0.1 1.5" "60 300 0.1 1.5" "60 300 0.1 2" "80 400 0.1 2"; do uv run --with scipy python scripts/interfreq2_flatF.py $a; done   # flatF_scan.txt, <2 min
for a in "60 480 0.1 2" "100 500 0.1 2" "100 500 0.1 1.5"; do uv run --with scipy python scripts/interfreq2_flatF.py $a; done   # flatF_scan2.txt, ~8 min, <1 GB
for a in "20 100 0 2" "30 150 0 2" "40 200 0 2" "60 300 0 2" "40 200 0 1.5"; do uv run --with scipy python scripts/interfreq2_flatF.py $a; done   # SPW (t = 0): flat0_scan.txt, ~1 min
for a in "100 1000 0.1 2" "100 1000 0.1 1.5"; do uv run --with scipy python scripts/interfreq2_flatF.py $a; done   # flatF_scan3.txt, ~45 min each, ~3.2 GB
uv run --with scipy python scripts/interfreq2_flatF.py 20 100 0.1 1.5 - med                                           # medium sign conditions: margin 0
uv run --with scipy python scripts/interfreq2_phi_lp.py 20 60 0.1                                                     # exact-uniform comparison: infeasible (§3)
uv run --with scipy --with sympy python scripts/interfreq2_rigid.py 20 2520                                           # mass off [1,N] = N
uv run --with scipy --with sympy python scripts/interfreq2_rigid_points.py 20 2520                                    # rigid nulls = 21Z (~5 min)
uv run --with scipy --with sympy python scripts/interfreq2_rigid_scan.py 40 3                                         # rigid-null scan
for N in 20 30 40 60; do uv run --with scipy python scripts/interfreq2_hybrid_lp.py $N 2,3,5,7,11,13 qnr; done          # §7 toys (N=60: ~8 min, ~1.2 GB)
```
(all under `ulimit -v 8000000`).

## 9. Towards Flat: reduction to spread pseudo-windows (O25 follow-up)

**Hypothesis SPW(C, σ, Δ₀) at N (spread pseudo-window).** There is a
summable R ≥ 0 on ℤ with
* (P1) `R(b mod d) = c(b,d)` for every d ≤ N/2 and every b (R has the exact
  small-class profile of the window; its mass is N);
* (P2) `R(s) ≤ 1 − σ` for every class s of modulus d > CN;
* (P3) `|R(s) − c(s)| ≤ Δ₀` for every class s with N/2 < d ≤ CN.

R = λ_N satisfies (P1), (P3) but has `R(s) = 1` on full classes; Lemma 4.1
and 6.1 windows do the same. SPW asks for a pseudo-window that no class
of modulus > CN sees as a point of [1,N].

**Proposition 9.1 (SPW ⇒ Flat; PROVED).** Let F_S be Selberg's minorant
of `1_{[1/2, N+1/2]}` with δ = 2/N (IF Thm 2.2), and
`τ := sup Σ_{x∈s} max(−F_S(x), 0)` over classes s of modulus > CN. Then τ is
bounded by an absolute constant, and SPW(C, σ, Δ₀) implies
Flat(C, t, s₀, Δ) with

    θ = σ / (2(σ + τ + 1/(2C))),   t = θ/2,   s₀ = σ/2,   Δ = 6θ + Δ₀,

via `F := θ F_S + (1 − θ)(1_{[1,N]} − R)`.

*Proof.* τ: for x outside I the Beurling–Selberg construction gives
`|F_S(x)| ≤ c₁/(1 + δ² dist(x,I)²)` and `‖F_S‖_∞ < ∞`. Source: Beurling's function satisfies `0 ≤ B(z) − sgn(z) ≤ 2K(z)`,
`K(z) = (sin πz/πz)²` (Vaaler, Bull. AMS 12 (1985), Lemma 5 / Thm 6 as
quoted in review R25; the paper is not in `sources/` and the numbering was
not re-checked). With `F_S(x) = −½[B(δ(α−x)) + B(δ(x−β))]` (α = 1/2,
β = N + 1/2), for x > β both errors lie in [0, 2K(δ·dist)], so
`−2K(δ·dist(x,I)) ≤ F_S(x) ≤ 0`, i.e. c₁ = 2 up to the form of K; similarly
for x < α. A class of modulus
d > CN > N has at most one point in [1,N] and its outside points are spaced
d apart, so `τ ≤ ‖F_S‖_∞ + 2c₁(1 + Σ_{k≥1}(N/(2kd))²) = O(1)`.
(F1): both summands are ≤ `1_{[1,N]}` and the weights are convex. (F2):
F_S has mass `N/2·1/d` on every class mod d ≤ N/2 (IF Lemma 2.4, error 0),
and `1_{[1,N]} − R` has mass 0 there by (P1); so `M = θN/2`. (F3): for a
full class s mod d > CN, `F_S(s) ≥ −τ` and `1 − R(s) ≥ σ` by (P2), so
`F(s) ≥ (1−θ)σ − θτ = σ/2 + θ/(2C) ≥ s₀ + M/d` by the choice of θ. (F4): for
a sparse class, `F(s) ≥ −θτ − (1−θ)(1−σ) ≥ −1 + θ/(2C) ≥ M/d − 1`, again
because `(1−θ)σ ≥ θ(τ + 1/(2C))`. (F5): `|F_S(s) − N/(2d)| ≤ 6` (IF Lemma 2.4
with D = N/2) and `|c(s) − R(s)| ≤ Δ₀`. ∎

So the edge problem of Selberg's minorant is cured by mixing in a little of
`1_{[1,N]} − R`, at constant cost in t and s₀. **Hence, by Theorem 5.2:
SPW(C, σ, Δ₀) with fixed C, σ > 0, Δ₀ (at every large N) implies the 3/4
cap `C′(log N)^{3/4}(log log N)^{3/4}` for every hybrid whose right-signed
mass on (N/2, CN] is ≤ e^{O(S)}·B.** (PROVED implication.)

**Lemma 9.2 (dual form of SPW; PROVED direction).** If R satisfies
(P1)–(P3), then every ν ≥ 0 on ℤ of the form
`ν = g + Σ_{d_i > CN} z_i 1_{s_i} + m` (g a combination of classes mod
d ≤ N/2, `z_i ≥ 0`, m a combination of classes mod `N/2 < d ≤ CN` with
coefficient mass |m|) satisfies the **patch-cancellation inequality**

    Σ_{n≤N} ν(n) + (1 − σ)·Z_sparse + Δ₀|m| ≥ σ·Z_full,          (9.1)

Z_full / Z_sparse the z-mass on classes meeting / missing [1,N].
(A converse holds for the *periodic* LP on ℤ/Q′ by finite LP duality: its
Farkas certificates are Q′-periodic ν ≥ 0 on ℤ violating (9.1) restricted
to moduli dividing Q′. For finite-support truncations a certificate is only
≥ 0 on the support window and proves nothing about ℤ.)

*Proof.* `Σ_n R ν ≥ 0`. By (P1) `Σ_{n≤N} g = Σ_n R g`, so
`Σ_{n≤N}ν = Σ_n Rν + Σ_i z_i(c(s_i) − R(s_i)) + Σ_med a(c(s) − R(s))`, and
(P2)–(P3) bound the last two sums below by
`σZ_full − (1−σ)Z_sparse − Δ₀|m|`. ∎

(9.1) says: positive patches of modulus > CN through [1,N] cannot be
cancelled cheaply by a small-modulus part that is negative on [1,N].
Example 3.2 is such a cancellation at modulus N + 1 (counted in |m|).

**Numerics for SPW (EVIDENCE; `interfreq2_flatF.py` with t = 0, so
R = 1_{[1,N]} − F; `data/interfreq2/flat0_scan.txt`).** Support
[−5N, 6N], C = 2: σ = 0.400, 0.400, 0.384, 0.335 at N = 20, 30, 40, 60
(Δ₀ ≤ 1.24); C = 1.5, N = 40: σ = 0.200. The t > 0 runs behave alike and
the decrease is largely truncation (Flat at N = 100, C = 2: s₀ = 0.167 on
[−5N, 6N] versus 0.320 on [−10N, 11N]; `flatF_scan3.txt`). The optimal R
is ≈ 0 on [1,N] and spread at density ≈ 0.1–0.3 over [−5N, 6N].

**Lemma 9.3 (local upper bound for σ; PROVED, due to review R25 C11).**
If R satisfies (P1)–(P2) of SPW(C, σ, ·) at N, then

    σ ≤ σ_C(N) := min_{q ≤ N/2} ( 1 − ⌈N/q⌉ / k_q ),   k_q = ⌊CN/q⌋ + 1.

*Proof.* Take b with `c(b,q) = ⌈N/q⌉`. The class b mod q is the disjoint
union of the k_q classes `b + jq mod k_q q`, whose modulus `k_q q > CN`; by
(P2) each has R-mass ≤ 1 − σ, and by (P1) they sum to `c(b,q)`. ∎

For q ∈ (2N/5, N/2) one gets `⌈N/q⌉ = 3`, `k_q = 5` at C = 2, so σ ≤ 2/5 for
all N ≥ 12 or so; at C ≤ 1, q ∈ (N/3, N/2) gives k_q = 3 and σ ≤ 0, so
**SPW with C ≤ 1 is impossible at every N** (a cleaner reason than
Example 3.2 for the C = 1 failures). As C ↓ 1, σ_C → 0, so the medium range
cannot be shrunk to (N/2, (1+ε)N] at fixed σ. Review R25's independent LPs
(C10) attain σ_C(N) exactly (2/5 at C = 2, 4/7 at C = 3, 1/5 or 1/4 at
C = 1.5) at every tested N once the support is long enough (e.g. N = 60
needs [−12N, 13N]); our decreasing margins in the table above are
truncation. The same lifting argument bounds the Flat margin s₀ (some
lifts are sparse there, so the bound is weaker); the `med` value 1/3 has
not been explained.

*Assessment.* The pinning of the LP optimum at the purely local bound
σ_C(N) suggests SPW(2, 2/5 − ε, O(1)) holds for all N, with the optimum
dictated by single small classes mod q ≈ 0.45N and their lifts. We did not
find a construction attaining it; the obstruction to the obvious
constructions is the one described next.

**Why SPW is not yet proved (Assessment, with the proved pieces).**
* *Translates and twists cannot do it.* Any R built from L₀-translates or
  from the twists of Lemma 6.1 with the identity on primes ≤ N/4 has
  `R(s) = c(s)` on every class s whose modulus divides the N/4-smooth part of
  L₀ (those maps fix such classes), so (P2) fails on full classes of
  modulus e > CN, e | lcm(1..N/4) (e.g. e = q₁q₂, q_i ≤ N/4). This is the
  same obstruction as the edge problem.
* *Big primes can be re-randomised (PROVED, easy).* Let L_s be the part of
  L₀ = lcm(1..N/2) on primes ≤ √(N/2). Draw n′ uniform in [1,N] and, for
  each prime p ∈ (√(N/2), N/2], an independent n′_p uniform in
  `{m ≤ N : m ≡ n′ (mod L_s(p))}`, `L_s(p) = lcm{d ≤ N/(2p)}`; put
  `Z ≡ n′ (mod L_s)`, `Z ≡ n′_p (mod p)`. Every small d is `d_s` or `d_s p`
  with `d_s ≤ N/(2p)`, and `(n′_p mod d_s, n′_p mod p)` has the window law,
  so `N·Law(Z)` satisfies (P1) on ℤ/L₀. But Z ≡ n′ (mod L_s) exactly, so
  classes of modulus e | L_s with e > CN keep mass 1/N: (P2) fails there.
* *What is needed* is a random integer Z whose residues modulo every
  d ≤ N/2 are jointly distributed exactly like those of a uniform
  n ∈ [1,N], while `Pr(Z ∈ s) ≤ (1 − σ)/N` for every class of modulus
  > CN. The constraints couple all prime powers q, q′ with qq′ ≤ N/2, so
  componentwise or sequential-conditional constructions break the joint
  laws of non-small products. Single patches are harmless (Fréchet: with
  only the classes mod q₁, q₂ of a patch mod q₁q₂ > N, the minimal coupling
  mass on the patch cell is `max(0, c₁ + c₂ − N) = 0`), so any failure of
  (9.1) must cancel many patches jointly, as in Example 3.2.
* *Not structurally false as far as we can see:* the LP optima exist with
  margins bounded away from 0 at every tested N once the support is long
  enough, and no certificate of the form (9.1)-violation was found above
  modulus CN.

## 10. Medium moduli (N/2, CN] (status)

* What is proved: Cor 5.1 (C = 1) and Thm 5.2/Prop 9.1 (any C) charge the
  right-signed medium mass `T_mid` at rate Δ. Moduli in (N/2, CN] have
  level ≤ log(CN), so they never affect the mean side; the issue is
  purely the interval side.
* **(N/2, N] can probably be freed at C = 2.** Theorem 5.2′ (PROVED
  implication, same proof as Thm 5.2): if F satisfies Flat and in addition
  the sign conditions `F(s) ≥ M/d` on full and `F(s) ≤ M/d` on sparse classes
  with N/2 < d ≤ N, then T_mid in Thm 5.2 may be restricted to right-signed
  mass on (N, CN] (the right-signed (N/2, N] terms then contribute ≥ 0 to
  the expansion in the proof of (5.1)). Finite-support witnesses with
  margin s₀ = 1/3 exist at N = 20, 30, 40 (C = 2, t = 0.1, support
  ≥ [−10N, 11N]); the periodic relaxation shows no obstruction at
  N ≤ 20 (C = 2). EVIDENCE.
* **(N, CN] cannot be fully freed.** Periodic certificate (rigorous up to
  floating point): at N = 20, C = 2 sign conditions on all of (N/2, CN] are
  infeasible on ℤ/2520, via the rigid modulus N + 1 = 21. With C = 1.5,
  even (N/2, N] cannot be freed at N = 20 (periodic relaxation: max s = 0).
* So a cap for hybrids with large right-signed mass at moduli in (N, CN]
  probably needs more than ν ≥ 0 (e.g. ν ≥ 1 on 𝒜, i.e. the arithmetic of
  the family at moduli comparable to N); this is supported by the periodic
  certificate at N = 20 but not proved in general. We have no such argument and no
  beating hybrid. Precisely open: *bound `B_hyb` below for majorants of
  𝒜(𝔊) whose free mass sits at moduli in (N/2, CN].*
