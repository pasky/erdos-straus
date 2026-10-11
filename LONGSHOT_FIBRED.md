# LONGSHOT_FIBRED — fibred encodings of Erdős–Straus solutions (task O136, long shot B)

**ES is not solved, here or anywhere. Nothing below proves ES(p) for any new p.**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment, as in DISCOVERIES.md.

Notation. `n ≥ 2`; `Sol(n)` = the finite set of positive solutions `(x,y,z)` of `4/n = 1/x+1/y+1/z`;
`Sol_I(n)`, `Sol_II(n)` the Type I / Type II solutions (ET: Type I = `n | x`, `gcd(n,yz) = 1`; Type II =
`n | y, n | z`, `gcd(n,x) = 1`); `f(n) = #Sol_I(n) + #Sol_II(n)`. ET Prop 1.6: `f(m²) = 0` for odd m.
For a prime p every solution is Type I or II, so `Sol(p) ≠ ∅ ⟺ f(p) > 0`.

## 0. Summary

(written at the end)

## 1. Fibred encodings: definition and the trivial decomposition

**Definition 1.1.** A *fibred encoding at n* is a triple `(E, ht, φ)`: a countable set `E = E(n)`, a height
`ht : E → [0,∞)` with `E(≤H) := {e : ht(e) ≤ H}` finite, and a map `φ : E → Sol(n)` (or into `Sol_I ∪ Sol_II`).
It is *power-fibred* if `#E(≤H) = c(n)H^δ(1+o(1))` as `H → ∞` (n fixed) for some `δ > 0`, `c(n) ≥ 0`.
A *counting route* proves this asymptotic with `c(n)` given by an independent formula and then reads off
`c(n) > 0 ⇒ E ≠ ∅ ⇒ Sol(n) ≠ ∅`.

**Lemma 1.2 (fibre decomposition; PROVED, trivial).** Suppose each fibre `E_s = φ^{−1}(s)` has a limit
`c_s := lim_H #E_s(≤H)/H^δ` (finite, possibly 0). Then `c(n) = Σ_{s∈Sol(n)} c_s`, a finite sum.
*Proof.* `E = ⊔_s E_s` with `#Sol(n) < ∞`; add the limits. ∎

*Reading.* The H-asymptotic is free (n is fixed; no uniformity in n is needed), and the scale constraint
(CONDITIONAL_ES Prop 2.3; RT1 Prop 2.4 / §5.5), which bounds main terms by `μ·f(n)`, is blind to it because
`#E(≤H)` grows like `H^δ`. But the *constant* `c(n)` is still a sum over the finitely many solutions. So the
question is never the H-asymptotic. It is whether some method evaluates `c(n)` without knowing `Sol(n)`.
§§2–3 classify the encodings by how `φ` is computed and show what `c(n)` can be.

**Lemma 1.3 (weighted scale constraint; PROVED, trivial).** In Lemma 1.2 put `w_max(n) = max_s c_s` and let
`μ(n)` be the largest number of "pieces" (orbits, components) of E lying over one solution, each piece of
density `≤ w_max^{piece}`. Then `c(n) ≤ f(n)·max_s c_s ≤ f(n)·μ(n)·w^{piece}_max(n)`. In particular a route
that proves `c(n) ≥ M(n)/2` from a main term `M(n)` needs `M(n)/w_max(n) ≤ 2 f(n)`; by ET (via CONDITIONAL_ES
Prop 2.3 / RT1 §5.5) this is `≤ 2ξ log³n log log n` outside a density-o(1) set of primes (any ξ → ∞),
`≤ 2p^δ'` outside `O(N^{1−δ'} log³N)` primes `p ≤ N`, and `≤ 2p^{3/5+o(1)}` for every p.
*Proof.* Lemma 1.2 and the three bounds on `f(p)` merged in RT1 §5.5. ∎

So a power-fibred encoding escapes the scale constraint *only* if the fibre densities `c_s` vary by a power of
n across solutions, or if the main-term formula for `c(n)` is not of the "count with error term" kind at all.
The rest of this file determines, for each mechanism that produces power fibres, what the densities `c_s` are.

## 2. Algebraic recipes: rigidity, and counting is idle

**Lemma 2.1 (rigidity; PROVED, elementary; generalises RT1 Prop 6.1 from curves to any dimension).** Let `V/ℚ`
be an irreducible variety, `E ⊂ V(ℚ)` Zariski-dense in V, and `φ : V ⇢ 𝔸³` a rational map defined over ℚ,
regular at every point of E, with `φ(E)` finite. Then φ is constant: `φ ≡ s₀ ∈ ℚ³` on its domain.
*Proof.* Let `U = dom φ` (open dense, irreducible) and `φ(E) = {s_1,…,s_k}`. The sets `Z_i = φ^{−1}(s_i) ⊂ U`
are closed in U and `E ⊂ Z_1 ∪ … ∪ Z_k`. E is dense in V, hence in U, so `U = Z_1 ∪ … ∪ Z_k`; U is
irreducible, so `U = Z_i` for one i. `s₀ = s_i` is ℚ-rational because E has ℚ-points. ∎

**Lemma 2.2 (orbits are Zariski-dense; PROVED relative to Borel's density theorem).** Let G be a connected
semisimple ℚ-group with `G(ℝ)` having no compact factor, `Γ ⊂ G(ℚ)` an arithmetic subgroup, and G acting
ℚ-rationally on an affine variety. For every `x ∈ V(ℚ)` the orbit `Γx` is Zariski-dense in the (irreducible)
orbit closure `\overline{Gx}`.
*Proof.* Borel density: Γ is Zariski-dense in G. The orbit map `G → \overline{Gx}`, `g ↦ gx`, is a dominant
morphism, so the image of a dense subset is dense. G connected ⇒ `\overline{Gx}` irreducible. ∎
This covers every setting of the brief: DRS, Eskin–McMullen, Eskin–Mozes–Shah and Oh–Shah all count points
of orbits `Γx` of such Γ (the counting theorems are not needed for Lemma 2.2; Borel density suffices).

**Theorem 2.3 (algebraic recipes make the count idle; PROVED from 2.1–2.2).** Let `E = ⋃_{i≤k} E_i` with each
`E_i ⊂ V_i(ℤ)` Zariski-dense in an irreducible `V_i/ℚ` (e.g. `E_i = Γ_i x_i` as in Lemma 2.2), and let
`φ|_{E_i}` be the restriction of a rational map `φ_i : V_i ⇢ 𝔸³` with `φ(E) ⊂ Sol(n)`. Then:
(a) `φ_i ≡ s_i` is constant, and `s_i` is the value of `φ_i` at *any* point of `dom φ_i` over `\bar ℚ`
(for instance the generic point): it is computable from the defining equations of `(V_i, φ_i)` alone.
(b) Hence any proof that `E ≠ ∅` (via a power asymptotic or otherwise) yields only "some `V_i(ℤ) ∩ Ω ≠ ∅`",
and the solution produced is the explicit `s_i` written into the data. If `s_i ∈ ℕ³` solves `4/n`, ES(n) is
already proved without any counting; if not, `E_i = ∅`.
(c) If moreover `φ_i` is given by polynomials with coefficients in `ℤ_ℓ` (resp. a real-analytic map sending
the counting region `Ω` into the positive octant), then a single ℓ-adic point of `V_i` forces `s_i ∈ ℤ_ℓ³`
(resp. a single real point in Ω forces `s_i > 0`). So with ℤ-polynomial `φ_i` the purely *local* statement
"`V_i(ℤ_ℓ) ≠ ∅` for all ℓ, and `V_i(ℝ) ∩ Ω ≠ ∅`" already implies `s_i ∈ Sol(n)`: the Siegel/Hardy–Littlewood
main term carries no information beyond the explicit point `s_i`.
*Proof.* (a) Lemma 2.1 applied to `(V_i, E_i, φ_i)`. (b) is (a). (c) `s_i = φ_i(v)` for any `v ∈ dom φ_i`,
in particular for an ℓ-adic or real point; ℤ_ℓ-coefficients map `ℤ_ℓ`-points to `ℤ_ℓ³`. `s_i ∈ ℤ_ℓ³` for all
ℓ means `s_i ∈ ℤ³`. ∎

*Reading.* For algebraic recipes, power fibres are an illusion of the parametrisation: each fibre is a whole
component on which the recipe is constant, the component "knows" its solution, and counting its points
certifies nothing about `Sol(n)` that is not visible from the equations. This is RT1 Prop 6.1 ("a whole curve
maps to one solution") in every dimension, plus the observation that the count is then logically idle.
