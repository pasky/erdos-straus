# Windmills on a general surface Z: from "narrowed" to "barred under H" (O162)

**Status: ES is not solved here.** Follow-up of INVOLUTION_ES.md (O158 + R158), Thm 5.1: every finite-menu
involution on X(p) with ES-only fixed points certifies ES(p) through `E(p) ∩ Z ≠ ∅`, for a fixed proper
algebraic set Z ⊂ A³ (depending on the menu). Labels as in DISCOVERIES.md. Scripts: `scripts/inv2_*`.

## 0. Summary (outcome: the route is **barred under Bateman–Horn**, barred under H for cylinder surfaces, and
barred **unconditionally** unless Z contains a "Siegel cylinder")

* **Axis lines (PROVED, Lemma 2.1).** On a line parallel to a coordinate axis, the E-values form finitely many
  arithmetic progressions, none containing an odd square (INVOLUTION_ES Lemma 2.2 at `n = m²`). So every prime
  that is a unit square modulo the moduli (e.g. `p ≡ 1 mod 8α`) misses them. No hypothesis needed.
* **Non-cylindrical components are thin (PROVED, Prop 3.2, Cor 3.3).** An irreducible surface or curve that is
  not a 2-dimensional axis cylinder `C × A¹` carries, off its finitely many axis lines, only `O(N^{2/3})` points
  with `P ≤ N`. Axis cylinders over curves C with finitely many integer points (Siegel) reduce to lines
  (Cor 3.4). So **unconditionally, for Z without "Siegel cylinder" components, `E(p) ∩ Z = ∅` for 100% of
  the primes `p ≡ 1 (mod α₀)`** (Thm 6.1(b)), and the corresponding windmills are barred (Cor 6.2.1).
* **Siegel cylinders: the slice divisor divides a fixed polynomial (PROVED, Lemma 4.1).** On `{f(t,u) = 0}`,
  `A | R_f(p) := p^{deg_T f} f(−1/p, −p)`; on `{f(t,v) = 0}`, `B | R_f(p)`; on `{g(u,v) = 0}`, `u | g(0,−p)` and
  `v | g(−p,0)`. So E(p) ∩ W is found by a *bounded* divisor search (Lemma 4.2). New **character lemma**
  (PROVED, Lemma 5.1): for `p ≡ 1 (8)` and `x ∈ E(p)`, the odd parts of A, B **and uv** all have Jacobi symbol
  −1 mod p.
* **Siegel cylinders are barred under H (Thm 5.3, CONDITIONAL on H for the factors of `R_W(24X+1)`; the step
  "admissible ⇒ E(p) ∩ W = ∅" is PROVED).** At the square-mimicking point of POINTWISE_SIZE Theorem C, every
  prime factor of `R_W(p)` other than p itself is a residue mod p (Lemma 5.2), contradicting Lemma 5.1. This includes the
  coordinate planes: INVOLUTION_ES Cor 5.3 is now a complete conditional proof (Dickson) with a simpler family
  (`24X+1`, `(24cX+c+1)/·`, `(24X+1+c)/·`). Example: if `q, 12q+1, 24q+1` are prime then `E(24q+1) ∩ {t=u} = ∅`.
* **General Z (Thm 6.1).** Under Bateman–Horn (lower bound), for every proper closed Z, `≫ N/(log N)^{|S|}` primes
  `p ≡ 1 (24)` have `E(p) ∩ Z = ∅`. Under H alone: when all 2-dimensional components of Z are axis cylinders.
  **Consequence (Cor 6.2): no finite-menu affine windmill on X (INVOLUTION_ES Thm 5.1 class) proves ES for all
  large `p ≡ 1 (24)`, CONDITIONAL on Bateman–Horn.**
* **Unconditional cylinder example (Prop 7.1, PROVED).** For `Z = {t = u}` (INVOLUTION_ES Remark 5.4), at least
  72% of the primes `p ≡ 1 (24)` (lower density) have `E(p) ∩ Z = ∅` (Brun–Titchmarsh; mass `μ ≈ 0.1385`).
* **Residue (§7).** Unconditionally: Siegel cylinders (in particular coordinate planes) — a half-dimensional
  sieve problem with a prime variable per linear factor of `R_W`. Under H alone: non-cylindrical surfaces
  (one needs an admissible prime outside an `O(N^{2/3})` set). Outside Thm 5.1's class (infinite menus,
  non-affine maps, n-dependent SL₂, other auxiliary sets): open, as in INVOLUTION_ES §6.

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
plane curve in the other two coordinates; we call it a **Siegel cylinder** if the curve C contains
infinitely many integer points with positive coordinates (the condition is on C: one such point of C
already gives infinitely many on W). Coordinate planes `{t=c}`, `{u=c}`, `{v=c}` are
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
(lcm of 24 and of the `8α` over the finitely many axis lines of Lemma 2.1 inside the components) such that

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

## 5. Siegel cylinders are barred under Hypothesis H

**Lemma 5.1 (character lemma; PROVED).** Let `p ≡ 1 (mod 8)` be prime, `p > 3`, and `x = (t,u,v) ∈ E(p)`. Write
`y₀` for the odd part of an integer y. Then the Jacobi symbols satisfy

  `(A₀/p) = (B₀/p) = ((uv)₀/p) = −1`.

In particular each of `A`, `B`, `uv` has an odd prime factor ℓ with `(ℓ/p) = −1`; all of them are prime to p.

*Proof.* `(A₀/p) = −1` is INVOLUTION_ES Lemma 5.2. In general `4 | A | tp+1` and `p ≡ 1 (4)` give
`t ≡ 3 (mod 4)`.
*B.* Write `B = 2^e β`. For a prime `ℓ | β`, `tp ≡ −1 (mod ℓ)`, so `(p/ℓ) = (−t/ℓ)`; hence
`(β/p) = (p/β) = (−t/β)`. From `B ≡ −1 (mod t)`: `(2/t)^e(β/t) = (−1/t) = −1`. Reciprocity with
`(t−1)/2` odd: `(t/β) = (β/t)(−1/β)`. So `(p/β) = (−1/β)(t/β) = (β/t) = −(2/t)^e`. If `e ≥ 1` then
`8 | AB = tp + 1`, so `t ≡ 7 (mod 8)` and `(2/t) = 1`. Either way `(β/p) = −1`.
*uv.* `u ≡ t (mod 4)` (as `tu ≡ 1`), so u is odd, `u ≡ 3 (mod 4)`. Write `v = 2^b v₀`. By Lemma 4.1(b),
`p ≡ −v (mod ℓ)` for primes `ℓ | u` and `p ≡ −u (mod ℓ)` for primes `ℓ | v`. (A common prime of u and v, or
`p | uv`, would force `p | u` and `p | v`, hence `tuv ≥ p·max(u,v) > p + u + v` for `p > 3`: impossible.)
So `(p/u) = (−v/u) = (−1/u)(2/u)^b(v₀/u)` and `(p/v₀) = (−u/v₀) = (−1/v₀)(u/v₀)`. Multiplying and using
reciprocity, `(p/uv₀) = (2/u)^b·(−1/u)(−1/v₀)(−1)^{(u−1)(v₀−1)/4}`, and with `u ≡ 3 (4)` the last three
factors multiply to −1 for either class of `v₀` mod 4. If `b ≥ 1`: `Av = p + u` (Lemma 4.1(b)) and `4 | A`
give `8 | p + u`, i.e. `u ≡ 7 (mod 8)`, so `(2/u) = 1`. Hence `(uv₀/p) = (p/uv₀) = −1`. ∎

EVIDENCE: all three symbols are −1 on all 647 points of `E(p)`, `p ≡ 1 (8)`, `p < 3000` (the `t`, `u`, `v`
symbols separately take both values) — `scripts/inv2_formal_check.py` re-runs this.

**Lemma 5.2 (QR lemma; PROVED part of POINTWISE_SIZE Theorem C, made explicit).** Let `R ∈ ℤ[n]` be nonzero,
`P := 24X + 1`, and let `h_1, …, h_k ∈ 𝒫` be the irreducible factors of `R(P(X))` other than P, so that
`R(P(X)) = κ·P^{e₀}·∏ h_j^{e_j}`. Work at `q* = q*_univ` (every `q*_ℓ` a unit, every `h` nondegenerate,
`24q*_ℓ + 1` a nonzero square unit). Let `Λ` contain 2, 3, the primes of every `C_{h_j}`, of
`K := κ∏C_{h_j}^{e_j}` and of `H_j := 24^{deg h_j} h_j(−1/24)` (nonzero, as `P ∤ h_j`), with `E₂ ≥ 3`,
`E_ℓ ≥ 1` and `E_ℓ > max_j v_ℓ(C_{h_j})` (as in Theorem M; needed for its normalised family). If q is admissible for `S = {P, h_1, …, h_k}` (i.e. `q ≡ q*_ℓ (mod ℓ^{E_ℓ})` for `ℓ ∈ Λ`,
`p = P(q)` and all `r_j := h_j(q)/C_{h_j}` prime, q beyond the finitely many q with `r_j = p` or `p | H_j`),
then **every prime `ℓ ≠ p` dividing `R(p)` has `(ℓ/p) = 1`**, and `p ≡ 1 (mod 24)`.

*Proof.* This is the "characters" paragraph of the proof of Theorem C. The primes of `R(p)` other than p are
the primes of K (in Λ) and the `r_j`. For odd `ℓ ∈ Λ`, `p ≡ P(q*_ℓ) (mod ℓ)` is a nonzero square, so
`(ℓ/p) = (p/ℓ) = 1`; `(2/p) = (−1/p) = 1` as `p ≡ 1 (8)`. For `r_j`: `24q ≡ −1 (mod p)` gives
`24^{deg h_j} h_j(q) ≡ H_j (mod p)`, so `(r_j/p) = (H_j/p)(24/p)^{−deg h_j}(C_{h_j}/p) = 1`, all primes
involved lying in Λ. ∎

**Theorem 5.3 (cylinders barred under H; CONDITIONAL on Hypothesis H for one explicit finite family).** Let
`Z₁` be a finite union of axis cylinders (of any dimension, i.e. including axis lines), and of curves. Then
there are infinitely many primes `p ≡ 1 (mod 24)` with `E(p) ∩ Z₁ = ∅`. Precisely: let `W_1, …, W_k` be the
Siegel cylinders among the 2-dimensional cylinders used in the reduction below, and
`R := ∏_i R_{W_i}`, where `R_W := R_f` (v- or u-cylinder over `{f = 0}`) or `R¹_g R²_g` (t-cylinder over
`{g = 0}`). Enlarge Λ of Lemma 5.2 by the primes of the moduli α of Lemma 2.1 for the finitely many axis lines
involved, with `E_ℓ ≥ v_ℓ(α)`. Then **(PROVED)** every admissible q (beyond a threshold) gives
`E(P(q)) ∩ Z₁ = ∅`; **(CONDITIONAL)** under H for `{P, h_1, …, h_k}` (Theorem M(b)) there are infinitely
many admissible q, and under Bateman–Horn `≫ N/(log N)^{|S|}` of them with `P(q) ≤ N`, `S = {P, h_1, …, h_k}`.
The hypothesis is applied, exactly as in Theorem M(b), to the normalised family `f_h(y) = h(My + q̃)/C_h`
(`M = ∏_{ℓ∈Λ} ℓ^{E_ℓ}`, `q̃ ≡ q*`, with `E_ℓ > max_h v_ℓ(C_h)`), **not** to the raw factors `h(X)`: the raw
factors may have a fixed prime divisor (see Remark 2). If R splits into linear factors (e.g. coordinate planes)
Dickson's conjecture suffices.

*Reduction.* Every curve component D that is not an axis line lies in a 2-dimensional axis cylinder
(`π_v⁻¹(π_v(D))` closure, which is 2-dimensional as D is not a v-line). Every 2-dimensional cylinder is Siegel
or not; non-Siegel ones reduce to finitely many axis lines (Cor 3.4); axis lines are handled by Lemma 2.1.

*Proof.* Let q be admissible, `p = P(q)`, with p beyond the roots of R and the thresholds of Lemmas 4.2,
5.2. Axis lines: p is a unit square modulo `ℓ^{v_ℓ(α)}` for every `ℓ | α` and `p ≡ 1 (8)`, so Lemma 2.1 gives
`E(p) ∩ ℓ = ∅`. Siegel cylinder `W_i`: if `x ∈ E(p) ∩ W_i`, Lemma 4.1(c)/(d) gives `A | R(p)` (v-cylinder),
`B | R(p)` (u-cylinder) or `uv | R(p)` (t-cylinder), where `R(p) ≠ 0`. By Lemma 5.1 that divisor has an odd
prime factor `ℓ ≠ p` with `(ℓ/p) = −1`, and `ℓ | R(p)`: this contradicts Lemma 5.2. ∎

**Remarks.**
1. *Relation to Theorem C.* Theorem 5.3 is Theorem C applied to the bounded program `Π_W` of Lemma 4.2; the
   direct proof above needs only Lemma 5.2, and its H-family is just the factors of `R(24X+1)` (Theorem C would
   also factor every `A+1`, `p+u`, … met by `Π_W`, a larger family).
2. *Coordinate planes (Cor 5.3 of INVOLUTION_ES, simplified).* `{t = c}`: `R = −(cp+1)`; `{u = c}`:
   `R = −(p+c)`; `{v = c}` as a t-cylinder over `g = V − c`: `R¹R² = c(p+c)`. So for the 33 planes
   `t,u,v = c ≤ 11` the linear forms are `24X+1`, `24cX + c + 1`, `24X + 1 + c` (c ≤ 11), with
   no A-dependent forms (`cd·A = (d+1)p + c`, … of the old sketch are not needed, because the `uv`-character
   of Lemma 5.1 replaces the `A`-character on `{v = c}`). The Dickson family is their normalisation
   `h(My+q̃)/C_h` at `q*_univ` (self-review repair: the raw forms after removing contents are inadmissible, e.g. the
   `{u = c}` forms `12X+1, 8X+1, 6X+1, 24X+5, 4X+1` (c = 1..5) cover all residues mod 5; at `q*_univ` the
   offending power of 5 goes into `C_h`). This upgrades Cor 5.3 from "sketch" to a complete conditional proof.
3. *Example `{t = u}` (Remark 5.4 of INVOLUTION_ES).* `R = p² − 1`, `R(24X+1) = 48·X·(12X+1)`; Λ = {2,3}
   (`H_X = −1`, `H_{12X+1} = 12`). So: **if q, 12q+1, 24q+1 are all prime then `E(24q+1) ∩ {t=u} = ∅`**
   (PROVED, for every such q: directly, `(q/p) = (p/q) = 1` and `(12q+1/p) = (2/p) = 1` as `2(12q+1) = p+1`;
   infinitely many such q under Dickson).

EVIDENCE (`scripts/inv2_formal_check.py 30000 3000`, log `logs/inv2_formal_check_30000.txt`, 3 min): Lemma 5.1
on all 647 E-points with `p ≡ 1 (8)`, `p < 3000`. For 11 sample Siegel cylinders (v-, u- and t-cylinders,
including 4 planes and `t = u`, `u = 2t+1`, `u = t²+2`, `v = 2t−1`, `v = u+4`, `v = 2u+3`) and all 385 primes
`p = 24q+1 ≤ 30000`: whenever every prime `ℓ ≠ p` of `R_W(p)` is a residue mod p, the bounded search finds
`E(p) ∩ W = ∅` (no exception); and every "admissible" p (each factor of `R_W(24q+1)` = Λ-unit × one prime,
p a residue mod the odd primes of Λ) has that QR property (Lemma 5.2). The cylinders are not vacuous: e.g.
`E(p) ∩ {t=u} ≠ ∅` for 52, `{u = 2t+1}` for 158, `{t = 3}` for 193 of the 385 primes. (For the single plane
`{t=3}` the QR property holds exactly at the other 192 primes.)

## 6. General Z, and the consequence for windmills

**Theorem 6.1 (fixed surfaces; parts as labelled).** Let `Z ⊂ A³` be any proper closed set. Split its
irreducible components into
* (i) 2-dimensional Siegel cylinders,
* (ii) 2-dimensional non-Siegel axis cylinders and axis lines,
* (iii) the rest: non-cylindrical surfaces, curves that are not axis lines, points.

Let S, Λ be the data of Theorem 5.3 for the components (i) and the axis lines from (ii) and from (iii)
(Prop 3.2: finitely many), and let `𝔈_Z` be the set of primes `P(x)`, x a point of a component (iii) on no
axis line, so `#(𝔈_Z ∩ [1,N]) ≪ N^{2/3}` (Prop 3.2).
(a) **PROVED.** Every admissible q with `P(q) ∉ 𝔈_Z` (beyond a threshold) has `E(P(q)) ∩ Z = ∅`.
(b) **PROVED (unconditional), if Z has no component of type (i).** There is `α₀` with `E(p) ∩ Z = ∅` for all
primes `p ≡ 1 (mod α₀)` outside a set of size `O(N^{2/3})`; i.e. for 100% of them (Cor 3.3, 3.4).
(c) **CONDITIONAL on H** (for the family of Theorem 5.3), **if every 2-dimensional component of Z is an axis
cylinder:** infinitely many primes `p ≡ 1 (24)` have `E(p) ∩ Z = ∅`. (Curves are absorbed into cylinders as in
the reduction of Thm 5.3, so 𝔈 is not needed.)
(d) **CONDITIONAL on the Bateman–Horn lower bound** for the family `{f_h : h ∈ S}` of Theorem M(b)–(c):
for every proper closed Z, `#{p ≤ N : p ≡ 1 (24), E(p) ∩ Z = ∅} ≫ N/(log N)^{|S|}`; in particular infinitely
many.
*Proof.* (a) Components (i) and the axis lines: Theorem 5.3's proof. Components (iii) off axis lines: by
definition of `𝔈_Z`. Components (ii): Cor 3.4 and Lemma 2.1 at admissible q. (b) Cor 3.3 + Cor 3.4. (c)
Theorem 5.3. (d) By (a), since BH gives `≫ N/(log N)^{|S|}` admissible q, which exceeds `#𝔈_Z ≪ N^{2/3}`. ∎

**Corollary 6.2 (finite-menu windmills on X; labels as in 6.1).** Let `(τ_p)_{p ∈ F}` be a finite-menu
family of involutions of X(p), F a set of primes `p ≡ 1 (mod 4)` (as INVOLUTION_ES Thm 5.1 requires), as in INVOLUTION_ES Theorem 4.4(1) ((t,u,v) coordinates with coefficients in
ℚ(n), or (A,B,t) with n-independent menu), with `Fix τ_p ⊆ E(p)`, and let Z be the proper closed set of
Theorem 4.4 for its menu. By INVOLUTION_ES Thm 5.1, `E(p) ∩ Z ≠ ∅` for all but finitely many `p ∈ F`. Hence:
1. (**PROVED, unconditional**) If Z has no Siegel-cylinder component, F omits 100% of the primes
   `p ≡ 1 (mod α₀)`: no such windmill proves ES on any set of primes of positive relative density in that
   class.
2. (**CONDITIONAL on H**) If every 2-dimensional component of Z is an axis cylinder, F omits infinitely many
   primes `p ≡ 1 (24)`.
3. (**CONDITIONAL on Bateman–Horn**) For every finite menu, F omits `≫ N/(log N)^{|S|}` primes `p ≡ 1 (24)`,
   `p ≤ N` (S as in Thm 6.1, depending on the menu). **So no finite-menu affine windmill on X proves ES for all large primes
   `p ≡ 1 (24)`: the route is barred under Bateman–Horn**, and under H for all menus whose exceptional
   surfaces are cylinders (in particular coordinate planes, the case of INVOLUTION_ES Cor 5.3). ∎

*Scope.* This concerns the O158 set X and finite affine menus in the coordinates of Theorem 4.4(1). Not
touched: infinite or p-growing menus, non-affine maps, the n-dependent SL₂ group, auxiliary sets other than X
(INVOLUTION_ES §6, unchanged). Also, Cor 6.2 does not use the windmill beyond INVOLUTION_ES Thm 5.1: it is
really a statement about the bounded-surface statement `E(p) ∩ Z ≠ ∅ ∀p`, which it refutes.

## 7. What resists, and one unconditional cylinder

**Proposition 7.1 (PROVED, unconditional; the constant is a rounded-up partial sum plus an elementary tail bound, `scripts/inv2_bt_mass.py`, log `logs/inv2_bt_mass.txt`).**
The primes `p ≡ 1 (mod 24)` with `E(p) ∩ {t = u} = ∅` have lower relative density `≥ 1 − 2μ ≥ 0.72`, where
`μ := Σ φ(gcd(24, a²−1))/φ(a²−1)` over odd `a ≥ 3` whose class `−a mod (a²−1)` is compatible with `1 mod 24`
(i.e. `a ≡ 15, 23 mod 24`); `μ ≤ 0.1384505 + 1.5·10⁻⁴ < 0.13860`, so `1 − 2μ > 0.7228`. (Partial sum to `a = 2·10⁵`
in 40-digit decimal arithmetic rounded up; tail from `φ(n) ≥ 0.375·n^{0.9}` and `φ(gcd) ≤ 8`. For a given N only
`a ≤ (1 + √(4N+5))/2` occur, since `a² − 1 ≤ p + a`.)
*Proof.* `x ∈ E(p) ∩ {t=u}` iff `t = u = a` odd and `a² − 1 | p + a` (then `8 | A`, `v = (p+a)/(a²−1)`). For
`a ≤ N^{θ/2}` apply Brun–Titchmarsh (Montgomery–Vaughan: `π(x;q,b) ≤ 2x/(φ(q) log(x/q))`) to the modulus
`lcm(24, a²−1) ≤ 24N^θ`; relative to `π(N;24,1) ∼ N/(8 log N)` this gives `≤ (2/(1−θ) + o(1))·μ`, using
`φ(lcm)φ(gcd) = φ(24)φ(a²−1)`. For `a > N^{θ/2}` the number of p is `≤ Σ_a ((N+a)/(a²−1) + 1) ≪ N^{1−θ/2} + N^{1/2}`.
Let `θ → 0`. ∎ (The empirical covered fraction is 0.132 for `p < 2·10⁶`: 2439 of 18507 primes; so the bound
0.72 is well below the empirical uncovered fraction 0.868 for `p < 2·10⁶`; the factor 2 of Brun–Titchmarsh accounts for
most of the gap.)
The same argument works for any non-plane Siegel cylinder (the moduli then have `Σ 1/φ(m) < ∞`), but gives a
positive proportion only when the mass satisfies `2μ < 1`; this is a numerical condition per cylinder, not a
theorem for all cylinders (raising the modulus 24 to kill large early terms enlarges the gcd weights of the
later ones).

**The honest residue of the windmill route on X (after O162).**
1. **Unconditionally**, the only obstruction to barring a finite-menu windmill is a Siegel-cylinder component of
   its exceptional set Z: `C × A¹` with C an integral-point-rich (genus 0, ≤ 2 places at infinity) curve in two
   of the coordinates. On such W, `E(p) ∩ W ≠ ∅` is a divisor statement about the fixed polynomial `R_W(p)`
   (Lemma 4.1), and failure is forced as soon as every prime factor of `R_W(p)` other than p is a residue mod p (Lemmas 5.1,
   5.2). Producing infinitely many such p unconditionally is a sieve problem with a prime variable and
   half-dimensional conditions on each linear factor of `R_W`. Example: for the single plane `{t = 3}` the
   condition is exactly that `(3p+1)/4` has only prime factors `≡ 1 (mod 3)` (data: QR(p) ⇔ `E(p)∩{t=3} = ∅`
   on all 385 primes tested), i.e. `3p + 1 = 4(x² + xy + y²)` primitively. Iwaniec's theorem on primes
   represented by binary quadratic polynomials (Acta Arith. 24, 1974) is the natural tool for one such
   condition. I have not checked that it covers the primitivity and congruence side conditions (**not
   claimed**). For several planes at once (k linear factors) this becomes a dimension-k/2 problem with a prime
   variable, which I do not know how to do.
2. **Under H alone**, non-cylindrical surface components are not handled: they need an admissible prime outside
   the thin set `𝔈_Z` (`O(N^{2/3})`), which qualitative H does not supply. Bateman–Horn (lower bound) does.
   One would like the formal mechanism to apply to non-cylindrical points directly. On such W the slice divisor
   A is not tied to a fixed polynomial in p (the free coordinate enters `F(t,u,v) = 0`), so this is open.
3. Everything outside the class of INVOLUTION_ES Thm 5.1 stays open as in INVOLUTION_ES §6: infinite/growing
   menus, non-affine maps, the n-dependent SL₂ group, auxiliary sets other than X.
