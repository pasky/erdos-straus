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
