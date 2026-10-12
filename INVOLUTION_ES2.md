# Windmills on a general surface Z: from "narrowed" to "barred under H" (O162)

**Status: ES is not solved here.** Follow-up of INVOLUTION_ES.md (O158 + R158), Thm 5.1: every finite-menu
involution on X(p) with ES-only fixed points certifies ES(p) through `E(p) ∩ Z ≠ ∅`, for a fixed proper
algebraic set Z ⊂ A³ (depending on the menu). Labels as in DISCOVERIES.md. Scripts: `scripts/inv2_*`.

## 0. Summary

(filled in at the end, §7)

## 1. Setup

`X(n) = {(t,u,v) ∈ ℤ³_{≥1} : P(t,u,v) = n}`, `P := tuv − u − v`, `A := tu − 1`, `B := tv − 1`, so that
`AB = tn + 1`. `E(n) := {x ∈ X(n) : 4 | A}` (ES elements; CONDITIONAL_ES Lemma 1.1 with `(g,f,c) = (t,u,v)`
gives the solution `4/n = 1/(Bdn) + 1/(vd) + 1/(Bvd)`, `d = A/4`). Lemma 2.2 of INVOLUTION_ES: **`E(m²) = ∅`
for every odd m** (this includes m = 1).

Z always denotes a proper Zariski-closed subset of `A³` over ℚ̄ in the coordinates (t,u,v). (Sets given in
the `(A,B,t)` coordinates of Thm 4.4 are covered: the morphism `(t,u,v) ↦ (t, tu−1, tv−1)` is dominant, so the
preimage of a proper closed set is proper closed, and it is a bijection on integer points of X.)

**Axis cylinders.** For an axis `e ∈ {t,u,v}`, an irreducible closed `W ⊆ A³` is an *e-cylinder* if
`W + ℚ̄·e = W`, i.e. `W = π_e⁻¹(π_e(W))` with `π_e` the projection along e. A 1-dimensional e-cylinder is an
*axis line* (`{(a,b)} × A¹` in suitable order). A 2-dimensional e-cylinder is `C × A¹` with C an irreducible
plane curve in the other two coordinates; we call it a **Siegel cylinder** if C (equivalently W) contains
infinitely many integer points with positive coordinates. Coordinate planes `{t=c}`, `{u=c}`, `{v=c}` are
Siegel cylinders (in two directions).

## 2. Axis lines: congruence classes without odd squares (unconditional)

**Lemma 2.1 (PROVED).** Let ℓ ⊂ A³ be an axis line. There are integers `α ≥ 1` and a finite set
`R_ℓ ⊂ ℤ/α` such that, for every n ≥ 1, `E(n) ∩ ℓ ≠ ∅` implies `n mod α ∈ R_ℓ`, and **no class in `R_ℓ`
contains an odd square** (i.e. `m² mod α ∉ R_ℓ` for every odd m). Consequently, if p is prime and p is a
square of an ℓ'-adic unit modulo `ℓ'^{v_{ℓ'}(α)}` for every prime `ℓ' | α`, and `p ≡ 1 (mod 8)` when
`2 | α`, then `E(p) ∩ ℓ = ∅`. In particular this holds for all `p ≡ 1 (mod 8α)`.

*Proof.* The three types of axis lines, with `a,b,c ≥ 1` fixed:
* `ℓ = {(a,b,v)}`: `P = (ab−1)v − b`, and `x ∈ E` iff `4 | ab − 1` (independent of v).
* `ℓ = {(a,u,c)}`: `P = (ac−1)u − c`, and `x ∈ E` iff `4 | au − 1`, a congruence condition on u mod 4.
* `ℓ = {(t,b,c)}`: `P = bc·t − b − c`, and `x ∈ E` iff `4 | bt − 1`, a congruence condition on t mod 4.

If the slope (`ab−1`, `ac−1`, resp. `bc`) is 0 then P ≡ −1 on ℓ and `E(n) ∩ ℓ = ∅` for n ≥ 1. Otherwise the
values `{P(x) : x ∈ ℓ ∩ E, P(x) ≥ 1}` form the set `{n ≥ n₀ : n mod α ∈ R_ℓ}` up to finitely many elements,
with `α := 4·slope` and `R_ℓ` the image of the admissible free coordinate mod 4. More precisely: every
`n ≡ r ∈ R_ℓ (mod α)` with `n ≥ n₀(ℓ)` is `P(x)` for some `x ∈ ℓ ∩ E` with positive coordinates. If some odd
`m₀` had `m₀² mod α ∈ R_ℓ`, then every odd `m ≡ m₀ (mod α)` would have the same residue, and the large ones
would give `E(m²) ≠ ∅`, contradicting INVOLUTION_ES Lemma 2.2. For the last statement: under the hypothesis,
CRT and Hensel (`p ≡ 1 (8)` is a 2-adic square) give an odd `m₀` with `m₀² ≡ p (mod α)`, so `p mod α ∉ R_ℓ`. ∎

This is the classical fact (Mordell, Schinzel; ET Prop 1.6) that polynomial identities only cover non-square
classes, here for the linear identities carried by single axis lines. It needs no hypothesis because the
"rational square point" `n = m²` is available.

## 3. Non-cylindrical components carry few points (unconditional)

**Lemma 3.1 (PROVED).** For `x ∈ ℤ³_{≥1}` with `t ≥ 2`: `P(x) + 1 ≥ tuv/2`.
*Proof.* `tuv/2 − u − v + 1 ≥ uv − u − v + 1 = (u−1)(v−1) ≥ 0`. ∎ (For `t = 1`, `P + 1 = (u−1)(v−1)`.)

**Proposition 3.2 (PROVED).** Let `W ⊂ A³` be irreducible closed of dimension ≤ 2 (over ℚ̄) that is not
a 2-dimensional axis cylinder. Then W contains only finitely many axis lines, and

  `#{x ∈ W ∩ ℤ³_{≥1} : 1 ≤ P(x) ≤ N, x on no axis line ⊂ W} ≪_W N^{2/3}`.

*Proof.* Lines. Fix the axis v (the others are symmetric). If `W` is a surface `{F = 0}` (F irreducible) and
F involves v, the set `L_v := {(a,b) : {(a,b)}×A¹ ⊆ W}` is the common zero set of the coefficients of F as a
polynomial in v. If L_v contained a curve D, then `D × A¹ ⊆ W`, both irreducible surfaces, so `W = D × A¹`
is a v-cylinder: excluded. So L_v is finite. If F does not involve v, W is a v-cylinder: excluded. If W is a
curve, it contains at most one line (itself). So finitely many axis lines, and for `(a,b) ∉ L_v` the fibre
`W ∩ ({(a,b)} × A¹)` has at most `D_W` points (`D_W` := degree bound, e.g. `deg F`, or the degree of W).

Count. Split the points x (not on an axis line of W) with `1 ≤ P(x) ≤ N`.
* `t = 1`: then `u, v ≥ 2` and `(u−1)(v−1) = P + 1 ≤ N + 1`, so `min(u,v) ≤ √(N+1) + 1`. For each value
  `u = b` of the smaller coordinate the point lies in the fibre of W over `(t,u) = (1,b)` (≤ D_W points, as
  x is on no v-line of W), similarly for v. Total `≤ 2 D_W (√(N+1) + 1)`.
* `t ≥ 2`: by Lemma 3.1, `tuv ≤ 2N + 2`. Let `w` be a largest coordinate, and `(y₁,y₂)` the other two; then
  `y₁y₂·max(y₁,y₂) ≤ tuv ≤ 2N+2`. The number of pairs `(y₁,y₂) ∈ ℤ²_{≥1}` with `y₁y₂ max(y₁,y₂) ≤ X` is
  `≤ 2Σ_{y₁ ≤ X^{1/3}} √(X/y₁) ≤ 4X^{2/3}`. Each pair gives at most D_W points of W (fibre along the axis of
  w, not a line of W). Over the 3 choices of w: `≤ 12 D_W (2N+2)^{2/3}`. ∎

**Corollary 3.3 (PROVED, unconditional; ineffective only through Siegel in Cor 3.4).** Let `Z₀` be a finite
union of irreducible closed sets as in Prop 3.2 (no 2-dimensional axis cylinders). There is `α₀ ≥ 1`
(lcm of `8α` over the finitely many axis lines of Lemma 2.1 inside the components) such that

  `#{p ≤ N prime : p ≡ 1 (mod α₀), E(p) ∩ Z₀ ≠ ∅} ≪_{Z₀} N^{2/3}`.

So `E(p) ∩ Z₀ = ∅` for all primes `p ≡ 1 (mod α₀)` outside a set of relative density 0 (and of size
`O(N^{2/3})`). More generally the same holds for all primes p that are unit squares modulo `ℓ^{v_ℓ(α₀)}` for
every `ℓ | α₀`, with `p ≡ 1 (8)`.
*Proof.* Points on axis lines: Lemma 2.1. The other points: Prop 3.2, each prime p with `E(p) ∩ Z₀ ≠ ∅` is
`P(x)` for at least one counted x. ∎

**Corollary 3.4 (PROVED; ineffective).** Let `W = C × A¹` be a 2-dimensional axis cylinder that is **not** a
Siegel cylinder (C has only finitely many integer points with positive coordinates, e.g. by Siegel's theorem
whenever C has genus ≥ 1, or genus 0 with ≥ 3 places at infinity, or C is not defined over ℚ). Then the
positive integer points of W lie on finitely many axis lines, and Lemma 2.1 applies: there is α with
`E(p) ∩ W = ∅` for every prime `p ≡ 1 (mod α)` (and every prime that is a unit square mod the prime powers of α
with `p ≡ 1 (8)`). ∎

So, unconditionally, **only Siegel cylinders can carry E(p) for a positive proportion of primes in every
square class**. These are `C × A¹` with C an integral-point-rich curve (genus 0, ≤ 2 places at infinity,
by Siegel) in two of the three coordinates; they include the coordinate planes and e.g. `{t = u}`.

## 4. Siegel cylinders: the slice divisor divides a fixed polynomial in p

By Cor 3.4 we may assume `C` is defined over ℚ, with irreducible equation in `ℤ[·,·]`. The key point: on an
axis cylinder, the integer that carries the ES congruence (`A`, `B`, or the pair `(u,v)`) **divides a fixed
nonzero polynomial in n**, independent of the point. So E(n) ∩ W is found by a *bounded* search over divisors.

**Lemma 4.1 (PROVED).** Let `x = (t,u,v) ∈ X(n)`, n ≥ 1. Then:
(a) `gcd(t,A) = gcd(n,A) = 1`, `u ≡ −n` and `t·n ≡ −1 (mod A)`; likewise `v ≡ −n`, `t·n ≡ −1 (mod B)`.
(b) `u | n + v` and `v | n + u`; precisely `uB = n + v` and `vA = n + u`.
(c) For `f ∈ ℤ[T,U]` put `R_f(n) := n^{deg_T f}·f(−1/n, −n) ∈ ℤ[n]`. If `f(t,u) = 0` then `A | R_f(n)`;
  if `f(t,v) = 0` then `B | R_f(n)`.
(d) For `g ∈ ℤ[U,V]` put `R¹_g(n) := g(0,−n)`, `R²_g(n) := g(−n,0)`. If `g(u,v) = 0` then `u | R¹_g(n)` and
  `v | R²_g(n)`.
(e) `R_f ≡ 0` (as a polynomial) iff `f` vanishes on the hyperbola `TU = 1`; `R¹_g ≡ 0` iff `U | g`; `R²_g ≡ 0`
  iff `V | g`. For irreducible f, g these are the curves `{TU = 1}`, `{U = 0}`, `{V = 0}`, which carry no
  point of X (A = 0, resp. u = 0, v = 0).

*Proof.* (a) `tu − A = 1`; `AB = tn + 1`. From `tu ≡ 1`, `tn ≡ −1 (mod A)`: `t(u+n) ≡ 0`, and t is a unit
mod A. Same for B. (b) `u(tv−1) = tuv − u = n + v`; symmetric. (c) Modulo A, `t ≡ −n⁻¹` and `u ≡ −n`, so
`n^{deg_T f} f(t,u) ≡ n^{deg_T f} f(−n⁻¹, −n) = R_f(n)`; the left side is 0. Same for B. (d) Modulo u,
`v ≡ −n` by (b), so `0 = g(u,v) ≡ g(0,−n) (mod u)`; symmetric. (e) `f(−1/x, −x) ≡ 0` means f vanishes on the
curve `(−1/x, −x)`, i.e. on `{TU = 1}` (irreducible). `g(0,y) ≡ 0` iff `U | g`. ∎

(Examples: `f = T − U` (`W = {t = u}`): `R_f = n² − 1`, i.e. `t² − 1 | n² − 1`. `f = T − c` (the plane
`t = c`): `R_f = −(cn+1)`, the slice integer. `f = U − c`: `R_f = −(n+c)`. `g = V − c`: `R¹_g = −(n+c)`,
`R²_g = −c`. These recover the candidate lists of Cor 5.3 of INVOLUTION_ES.)

**Lemma 4.2 (the bounded search; PROVED).** Let `W = C × A¹` be a Siegel cylinder over ℚ. There is a bounded
program `Π_W` in the sense of POINTWISE_SIZE §1.1 (ring operations, divmod, DIVIDES, FACTOR/DIVISORS, finite
loops over the resulting lists; no `while`) such that for every `n ≥ n₀(W)`, `Π_W(n)` outputs
`(SUCCESS, x, y, z)` with a positive solution of `4/n = 1/x + 1/y + 1/z` if `E(n) ∩ W ≠ ∅`, and `FAIL`
otherwise.

*Proof.* Take `n₀` beyond the largest root of the relevant nonzero polynomial(s) of Lemma 4.1(e). Then:
* *v-cylinder, `C = {f(t,u) = 0}`.* For each `A ∈ DIVISORS(R_f(n))` and each `t ∈ DIVISORS(A+1)`: put
  `u := (A+1)/t`; test `f(t,u) = 0`, `4 | A`, `A | tn+1`; put `B := (tn+1)/A`; test `t | B+1`; put
  `v := (B+1)/t`. On success output the Lemma 1.1 solution `(Bdn, vd, Bvd)`, `d = A/4`.
* *u-cylinder, `C = {f(t,v) = 0}`.* For each `B ∈ DIVISORS(R_f(n))`, `t ∈ DIVISORS(B+1)`: `v := (B+1)/t`,
  test `f(t,v) = 0` and `B | tn+1`, `A := (tn+1)/B`, test `4 | A` and `t | A + 1`, `u := (A+1)/t`; output.
* *t-cylinder, `C = {g(u,v) = 0}`.* For each `u ∈ DIVISORS(R¹_g(n))`, `v ∈ DIVISORS(R²_g(n))`: test
  `g(u,v) = 0` and `uv | n + u + v`, `t := (n+u+v)/(uv)`, test `4 | tu − 1`; output.

Every candidate that passes the tests is a point of `E(n) ∩ W`, and the output is a solution (CONDITIONAL_ES
Lemma 1.1). Conversely every `x ∈ E(n) ∩ W` is enumerated: by Lemma 4.1(c)/(d) its `A` (resp. B, resp. (u,v))
divides the listed nonzero integer, and t divides `A + 1` (resp. `B + 1`; in the t-cylinder case
`tuv = n + u + v`). ∎

(For a 2-dimensional set that is a cylinder in two directions, i.e. a coordinate plane, any one of the
descriptions works.)
