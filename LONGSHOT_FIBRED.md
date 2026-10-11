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

**Corollary 2.4 (uniform algebraic encodings miss the square classes; PROVED relative to ET Prop 1.6 and
Dirichlet; known in substance: Mordell 1969 / Schinzel 2000 as quoted in ET p. 8, and the unconditional
instances of POINTWISE_SIZE Thm C).** Let `𝒱 ⊂ 𝔸^N × 𝔸¹_n` be an irreducible ℚ-variety whose generic fibre over
`𝔸¹_n` is geometrically irreducible, and `φ : 𝒱 ⇢ 𝔸³` a rational map over ℚ. Let `P_cov` be the set of primes p
for which some `E(p) ⊂ 𝒱_p(ℤ)`, Zariski-dense in `𝒱_p` (irreducible), satisfies `φ(E(p)) ⊂ Sol(p)`. Then there
is an integer `D' ≥ 1` (depending only on `(𝒱, φ)`) such that all but finitely many `p ∈ P_cov` are
quadratic non-residues mod `D'`. In particular infinitely many primes (all large `p ≡ 1 mod D'`) are not covered.
*Proof.* (i) *A section.* By Lemma 2.1, `φ|_{𝒱_p}` is constant for every `p ∈ P_cov`. If `P_cov` is finite there
is nothing to prove. Otherwise the closure of the image of `(φ, n) : 𝒱 ⇢ 𝔸³ × 𝔸¹` has finite fibres over the
infinite (hence Zariski-dense) set `P_cov`, so it is a curve dominating `𝔸¹`; its generic fibre is the image of
the geometrically irreducible generic fibre of 𝒱, hence one Galois-stable point: `s₀ = (x,y,z) ∈ ℚ(n)³`, with
`s₀(p) ∈ Sol(p)` for `p ∈ P_cov` (large). The identity `4xyz = n(xy+yz+zx)` holds at infinitely many n, hence in
`ℚ(n)`. (ii) *Polynomiality.* Write `x = A + r/Q` with `A ∈ ℚ[n]`, `deg r < deg Q`, and D a denominator of A.
Then `D·r(p)/Q(p) = D·x(p) − D·A(p) ∈ ℤ` and tends to 0, so `r(p) = 0` for infinitely many p, `r = 0`.
So `x, y, z ∈ ℚ[n]`, with positive leading coefficients. (iii) *The pattern is polynomial.* Each `s₀(p)`,
`p ∈ P_cov`, is Type I or II at p; fix one of the six patterns (which coordinate(s) p divides) occurring for an
infinite subset `P'`. Say Type I with `p | x(p)`, `p ∤ y(p)z(p)` (the other cases are identical). Let D be a common
denominator of x, y, z. `D x(p) ≡ D x(0) (mod p)` gives `p | D x(0)` for all `p ∈ P'`, so `x(0) = 0`, `x = n x₁`.
If `y(0) = 0` then `p | D y(p)`, so `p | y(p)` for `p ∤ D`, a contradiction; so `y(0)z(0) ≠ 0`.
(iv) *Transport to a square.* Put `D' = D²·|num(y(0)z(0))|·2` (num = numerator) and suppose `p ∈ P'`, `p > D'`,
is a square mod D', `p ≡ m₀² (mod D')`. Choose a prime `m ≡ m₀ (mod D')`, m large (Dirichlet; gcd(m₀, D') = 1
because `gcd(p, D') = 1`), and `n = m²`. The integrality of `x₁(n), y(n), z(n)` depends only on `n mod D`, and
holds at `n = p`; so it holds at `n = m²`, and the values are positive for m large. `y(n) ≡ y(0) (mod m)` in
`ℤ_(m)` with `m ∤ D·num(y(0))`, so `m ∤ y(n)`; likewise for z. Thus `(n x₁(n), y(n), z(n))` is a positive
solution of `4/m²` with `m² | x`, `gcd(m², yz) = 1`, a Type I solution of the odd square `m²`, contradicting
ET Prop 1.6. (Type II pattern: `y = n y₁`, `z = n z₁`, `x(0) ≠ 0`, same argument.) Hence every `p ∈ P'` with
`p > D'` is a non-square mod D'. There are finitely many patterns. ∎

**Corollary 2.5 (growing families reduce to the parameter search; PROVED from 2.3).** Let
`E(p) = ⨆_{θ∈Θ(p)} E_θ`, each `E_θ` Zariski-dense in an irreducible `V_θ`, `φ|_{E_θ}` algebraic, with
`Θ(p)` any set (growing with p, defined through factorisations, etc.). Then `φ|_{E_θ} ≡ s_θ` (explicit), and
`#E(p)(≤H) = Σ_{θ : E_θ ≠ ∅} #E_θ(≤H)`. If each `E_θ` has its own asymptotic `c_θ H^{δ_θ}`, the main term of
`#E(p)(≤H)` is `Σ_{θ ∈ Θ_*(p)} c_θ · H^{δ*}` over the occupied θ of maximal exponent; occupied θ have
`s_θ ∈ Sol(p)`, and the map `θ ↦ s_θ` has fibres of size `μ(p)`. So Lemma 1.3 applies to the θ-sum with weights
`c_θ`: the fibring adds the factor `H^{δ*}` and nothing else. *Proof.* Lemma 1.2 with fibres grouped by θ. ∎

*Reading.* Cor 2.4 is the classical "polynomial identities miss the square classes" obstruction, now valid for
every algebraic fibred encoding of bounded complexity, however large its fibres. Cor 2.5 says that once a
parameter growing with p is allowed (hatch H-A of RT2), fibring changes the normalisation, not the problem.

## 3. Orbit recipes: c(n) is a weighted orbit count

By §2, a recipe that is algebraic on a Zariski-dense piece is constant there. The only non-trivial power-fibred
encodings therefore use *orbit recipes*: E is a union of orbits of an arithmetic group, and φ is invariant under
the group, i.e. a function on the finite orbit set (computed, e.g., by reduction theory).

**Setting (O).** G a connected semisimple ℚ-group, `G(ℝ)` without compact factors, acting ℚ-rationally on
affine space; `V = \overline{G x₀}` a closed orbit; `Γ' ⊂ G(ℤ)` arithmetic; `E(n) ⊂ V(ℤ) ∩ Ω` a union of
Γ'-orbits (by Borel–Harish-Chandra, `V(ℤ)` is a finite union of Γ'-orbits, so E is a finite union);
`φ : Γ'\E(n) → Sol(n)` any map; `μ(n)` = max number of orbits over one solution.
**Counting input (C)** (DRS 1993 for symmetric V; Eskin–McMullen 1993 Thm 1.4; Eskin–Mozes–Shah 1996 for
reductive stabilisers; statements to be checked against the papers before any use beyond this file): for an
orbit `O = Γ'y` with `Γ'_y` a lattice in `H_y(ℝ) = Stab_{G(ℝ)}(y)`, and a well-rounded family `B_H ⊂ V(ℝ)`,
`#(O ∩ B_H) ~ w_O · vol(B_H)`, `w_O = vol(Γ'_y \ H_y(ℝ)) / vol(Γ' \ G(ℝ))` (Haar measures compatible with the
fixed invariant measure on V(ℝ)).

**Theorem 3.1 (orbit-weight principle; PROVED relative to (C)).** In setting (O) with (C):
(a) `#E(n)(≤H) ~ c(n)·vol(B_H)` with `c(n) = Σ_{O ⊂ E(n)} w_O = Σ_{s ∈ Sol(n)} Σ_{O ↦ s} w_O`, hence
`c(n) ≤ μ(n)·f(n)·max_O w_O`.
(b) If every stabiliser `H_y(ℝ)` is compact (e.g. V a two-sheeted hyperboloid / positive definite binary data,
stabiliser a CM torus), then `w_O = κ/|Γ'_y|` with κ independent of O and `|Γ'_y| ≤ C(Γ')` (arithmetic groups
have finitely many conjugacy classes of finite subgroups), so `w_max/w_min ≤ C(Γ')` and
`c(n)/w_min ∈ [#orbits, C(Γ')·#orbits] ⊂ [f(n)·1_{f(n)>0}… , C(Γ')·μ(n)·f(n)]`.
The scale constraint (Lemma 1.3) then holds verbatim with multiplicity `C(Γ')μ(n)`: a main term `M(n)` for
`c(n)/w_min` with `M ≫ μ(n)·ξ log³n log log n` is impossible at density-one of primes.
(c) If `H_y(ℝ)` is non-compact (a split torus factor), `w_O` is a regulator-type covolume and may vary by a
power of n across orbits. This is the only way the weights escape (a)–(b).
*Proof.* (a) Lemma 1.2 over the finitely many orbits, with (C) for each. (b) For compact `H(ℝ)` the stabilisers
`H_y(ℝ)` are conjugate in `G(ℝ)` to `H(ℝ)` (one closed orbit), with equal Haar volume, and `Γ'_y` is finite. The
bound on finite subgroups: Borel–Harish-Chandra / Minkowski. (c) is a definition. ∎

*Reading.* Fibring under a lattice with compact stabilisers multiplies each solution by `≍ vol(B_H)` and does
nothing else: `c(n)` is the solution count weighted by `1/|Γ'_y|`. Lemma 2.2 + Thm 2.3 forbid algebraic recipes,
so the recipe sees only the orbit, and the orbit count is what the counting theorem returns.
