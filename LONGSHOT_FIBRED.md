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
`#orbits ≤ c(n)/w_min ≤ C(Γ')·#orbits ≤ C(Γ')·μ(n)·f(n)` (#orbits = number of Γ'-orbits in E(n)).
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

## 4. Catalogue of concrete fibred encodings (Step 1)

Each entry: definition, fibre, growth, recipe class (§2 algebraic / §3 orbit), what survives. All PROVED unless
labelled; references are to the reviewed sources.

**F1 (free parameters).** `E = Sol(n) × ℤ^r_{≥0}`, `ht(s,k) = |k|`, φ = projection. Fibre `≍ H^r`.
Algebraic, constant on each component (`{s} × 𝔸^r`); `c(n) = f(n)·vol`. Baseline: power fibres by fiat.

**F2 (Pell orbits, Type II; O128 Prop 7.2).** A Type II quadruple gives the unit `ε_s = T + 2c√D'`,
`D' = d²m² + dp`, `m = a − b`, `T = 2cd(a+b) − 1`. Fibre: `{ε_s^k : k ≥ 1}` on the conic `T² − D'U² = 1`.
(i) *Growth is logarithmic*, `#{k : ε_s^k ≤ H} = log H/log ε_s + O(1)`: δ = 0, not power-fibred (rank-1 split
torus). (ii) *The orbit is ES-dead after k = 1*: with `ε² = T₂ + U₂√D'`, `T₂ = 2T² − 1`, `U₂ = 4cT`, the Type II
congruence would need `T₂ ≡ −1 (mod d·U₂)`, i.e. `4cdT | 2T²`, i.e. `2cd | T`, impossible since `T ≡ −1 (mod 2cd)`
and `2cd ≥ 2`. (So an algebraic recipe on the conic is constant: RT1 Prop 6.1.) (iii) *Even regulator weights
are polylog:* `Reg(ℤ[√D']) ≤ log ε_s ≤ log(2T) = O(log p)` because `a, b, c, d` divide coordinates of a positive solution, all of which are `≤ p^{O(1)}`, while
`Reg ≥ log((1+√5)/2)`. So a regulator-weighted count (Thm 3.1(c)) has `w_max/w_min = O(log p)`: the
solution *is* the small unit, which caps the weight. Lemma 1.3 applies with an extra `O(log p)`.

**F3 (Type I on the hyperboloid X_d; GEOMETRY_ES §4.3).** `X_d : ef − 4da² = 1`, two-sheeted, stabiliser the
anisotropic CM torus of `ℚ(√−d)`, compact at ∞; `Γ' ⊂ SO(q_d)(ℤ)` congruence. Encoding: `E = ⋃_s Γ'_s·x_s`
over the Type I points `x_s` at level d (e.g. `Γ'_s = Γ(4da_s)`, which keeps `f ≡ −p (mod 4da_s)` but moves a).
Fibre `≍ H` (DRS: `#{x ∈ Γ'x_s : |x| ≤ H} ≍ H`). The level-d Type I set is finite (GEOMETRY Prop 4.1, `c ≠ 0`), so
no infinite subgroup preserves it: an orbit contains finitely many solutions and the recipe is "orbit ↦ a
solution in it" (orbit class). Thm 3.1(b) applies: `c(n) = κ·Σ_O 1/|Γ'_{x_O}|`, a weighted solution count.
The intrinsic (non-circular) version replaces "orbit of a solution" by an adelic condition; see F5 and §5.

**F4 (Type II as pair embeddings; O128 Props 7.1, 8.2).** `L` = binary forms with `q = B² − 4AC`; `E_{c,d}(n)` =
pairs `(Q,S) ∈ L²` with Gram matrix `4T₀`, `T₀ = [−dn, 1, c²]`, Q positive definite, and `(Q,S)` in the
`SL₂(ℤ)`-orbit of some `(Q', S_c)` with `B' ≡ 0 (4d)`, `d | C'`, `gcd(B'/4d, c) = 1`. `SL₂(ℤ)` acts on pairs;
the stabiliser of `S_c` is `{±I}` (O128 Prop 8.2(i)), so each orbit is a copy of `PSL₂(ℤ)` and
`#{γ : ‖(Q,S)γ‖ ≤ H} ≍ H²` (hyperbolic lattice-point count). Orbits ↔ Type II solutions with this (c,d), up to
the gcd normalisation of Prop 8.1 (μ = 1). All stabilisers equal: Thm 3.1(b) gives `c(n) = κ_{c,d}·F_{c,d}(n)`,
`F_{c,d}(n) = #{f | 4c²dn+1 : f ≡ −1 (mod 4cd)}` exactly (O128 Prop 8.1). The power fibre is the `SL₂(ℤ)`
change of basis and carries no information.

**F5 (drop one condition: the genus-full closures of F3/F4).** Replace the ES orbit set by the full adelic set it
lies in: for F4, *all* embeddings of the binary lattice `4T₀` into L with Q of either sign and S of either class
`k = ±1` (no positivity/class condition); for F3, all of `X_d(ℤ) ∩ W` for an adelic open W containing the Type I
points. These are the encodings to which a mass formula (Siegel–Weil, Borovoi–Rudnick) applies, with a computable
main term. But the recipe is no longer valid: F4's closure contains `Q₀ = [−1, 0, −dn]` for **every** n, incl. odd
squares (O128 Prop 8.3), so its mass main term is positive at `n = m²` where `f = 0`: **T1 fails.**

**F6 (definite quaternion orders; QUATERNION_ES).** Type I orders lie in `B_{p,∞}`, Type II factorisations in the
definite algebra `(−d,−p)`: unit groups are finite, so there are no positive-dimensional fibres to count. Not
power-fibred.

*Summary of Step 1.* Every power-fibred encoding found is F1 (algebraic, idle by Thm 2.3), F3/F4 (orbit, compact
or trivial stabilisers, `c(n)` = weighted solution count by Thm 3.1(b)), or a genus-full closure F5 (computable
main term, invalid recipe, fails T1). F2 and F6 are not power-fibred; F2 even with regulator weights stays
polylog-weighted.

*Literature check for (C) and §5 (research subagent, 2026-10-11; primary texts opened except DRS).*
Eskin–McMullen 1993 **Thm 1.4** is exactly (C) for affine symmetric `G/H`, Γ a lattice (weakly irreducible),
`Γ∩H` a lattice in H; norm balls are well-rounded (Thm 6.1). DRS 1993 Thm 1.2 (number quoted second-hand by EM
and EMS). Eskin–Mozes–Shah 1996 **Thm 1.16** for reductive H, needing `H⁰` in no proper ℚ-parabolic (equivalently
`(Z(H)∩Γ)\Z(H)` compact) and a non-focusing condition. Borovoi–Rudnick 1995 **Def 2.3, Thm 0.6**: under (C),
`N(T; B∞×B_f) ~ ∫ δ dm` (Tamagawa measure), with `δ(x) = |C(H)|` if the Kottwitz invariant `κ(x) = 0` and 0
otherwise (C(H) dual to Pic H); `δ ≡ 1` if H is simply connected. Colliot-Thélène–Xu 2009 **Thm 3.7**: G semisimple
simply connected, H ⊂ G any connected subgroup (tori allowed), every almost simple factor non-compact at a place
of S₀: Brauer–Manin is the only obstruction to strong approximation for S∪S₀-integral points of `G/H`;
Borovoi–Demarche 2013 Thm 0.1 extends this. *Consequence for F4:* the stabiliser of `S_c` is a ℚ-split torus,
which lies in a ℚ-parabolic, so EMS 1.16 does not apply to orbits of `S_c` alone; F4 uses the pair (Q,S), whose
stabiliser is finite, and the count is the plain lattice-point count in `PSL₂(ℤ)`.

## 5. The T1 test, and where a non-local factor can come from (Step 2)

**5.1 Where T1 must act (PROVED, elementary, under the stated hypotheses).** Let a main term have the
Borovoi–Rudnick/Siegel shape `M(n) = m_∞(n) · ∏_ℓ m_ℓ(n) · β(n)` for a family `(V_n, W(n))`, where `m_ℓ(n)` is
the local density of `W_ℓ(n)` and `β(n) = |B|^{−1} Σ_{α∈B} ∏_ℓ E_ℓ(α,n)` with
`E_ℓ(α,n) = m_ℓ(n)^{−1}∫_{W_ℓ(n)} e(inv_ℓ α(x)) dx` (the BR density averaged over the adelic set; B ⊂ Br V_n
finite). Assume **(U)**: there are a finite set S₀ of primes and k ≥ 1 such that for `ℓ ∉ S₀`, `ℓ ∤ n`:
`m_ℓ(n) > 0` and `E_ℓ(α,n) = 1`; for `ℓ ∈ S₀`, `ℓ ∤ n`: `m_ℓ(n)` and `E_ℓ(α,n)` depend only on `n mod ℓ^k`; and
`m_∞(n) > 0` for large n. Let `Q₀ = ∏_{ℓ∈S₀} ℓ^k`. If `M(p) > 0` for a prime `p ∤ Q₀` and `M(m²) = 0` for an odd
`m ≡ m₀ (mod Q₀)` with `m₀² ≡ p (mod Q₀)`, `gcd(m, Q₀) = 1`, then the two values differ only through the factors
at the places `ℓ | m` (for `m²`) and `ℓ = p` (for p): either `m_ℓ(m²) = 0` for some `ℓ | m`, or some
`E_ℓ(α, m²)`, `ℓ | m`, differs from its value at a unit.
*Proof.* All other factors coincide by (U). ∎
*Reading.* T1 cannot be passed by the S₀-part (it is the same at p and at a square in p's class mod Q₀; this is
CONDITIONAL_ES Prop 7.3 in mass-formula form). A "global factor" passing T1 is a local density or a Brauer
evaluation **at the primes dividing m**, coupled to the rest by reciprocity. For `n = p` the only such place is p.

**5.2 Such factors exist in nature (classical; EVIDENCE check).** The ternary `3x² + 4y² + 9z²` (genus with two
spinor genera) represents every integer it represents locally except `n = w²` with every prime factor of w
`≡ 1 (mod 3)` (Earnest, arXiv:2203.02620, Prop 5.1(i); Jones–Pall 1939; Schulze-Pillot 1980 identifies these as the
spinor exceptions; by CTX §8 these are Brauer–Manin obstructions). `scripts/lsb_spinor_example.py` (N = 5·10⁴,
`data/lsb/spinor_example.out`): in the 12 generically represented classes mod 72 the only exceptions are the 29
squares `w²` with all primes of `w ≡ 1 (3)`, and every such square is an exception. This is exactly the shape 5.1
predicts: the factor `β(w²) = 0` is produced at the primes `ℓ | w` (through `(ℓ/3) = 1`). So "a main term that
vanishes on a square class and is positive elsewhere" is not absurd for homogeneous counting problems.

**5.3 The ES genus factor passes T1 and is invalid (PROVED; EVIDENCE table).** For Type II at level d (O128 Lemma
6.1), the natural genus refinement of the F5 closure is `𝔊⁻_d(n)` = primitive positive definite forms of
discriminant `−4dn` with `χ_{−4d}(Q) = −1` (χ evaluated at any represented integer prime to 4dn).
(a) For odd `n = m²` with `gcd(m, 2d) = 1`, `𝔊⁻_d(m²) = ∅`. *Proof.* A represented k prime to `D = −4dm²` has
`(D/k) = 1`, and `(D/k) = (−4d/k)(m/k)² = χ_{−4d}(k)`. ∎
(b) For a prime `p ≡ 1 (4)`, `p ∤ 2d`, `χ_{−4d}(Q) = (k/p)` (since `(−4dp/k) = 1` and `(p/k) = (k/p)`), a genus
character that is non-trivial on the form class group, so `#𝔊⁻_d(p) = h(−4dp)/2`. ∎ (Gauss: each genus
character not identically 1 takes both values on exactly half of the classes; here `(k/p)` is non-trivial on the class group: the assigned
characters of disc `−4dp` include `(·/p)` and at least one more (a character at 2 if `dp ≢ 3 (4)`; otherwise d is
odd with a prime factor `q ≡ 3 (4)`, giving `(·/q)`; Cox Thm 3.15), and only the product of all of them is trivial.)
So the genus-twisted mass `Σ_d (mass of 𝔊⁻_d(n))` vanishes at odd squares (coprime to the levels) and is
`≍ Σ_d h(−4dn)` at primes: **it passes T1, through the place p**, as 5.1 says it must. But the encoding is not
valid. A Type II point of level d is a form in `𝔊⁻_d(p)` lying on the shell `T_c` (O128 Prop 2.5) with level data;
this is a class-level, Planck-scale condition, and the number of such forms is `F_d(p)`. EVIDENCE
(`scripts/lsb_genus_minus.py` → `data/lsb/genus_minus.out`, 5 primes `p ≡ 1 (4)` in `[10³, 10⁴]` and 5 odd squares,
`d ≤ 8`): `#𝔊⁻_d = h/2 ∈ [10, 144]` at every prime and level, `= 0` at every square; `F_d(p) ∈ [0, 22]`, and
`F_d(p) = 0` at 19 of the 40 (prime, level) pairs where `𝔊⁻_d(p)` has 10–144 classes. The genus is nonempty
at every prime and level, and the ES points occupy a vanishing fraction of it.

**Theorem 5.4 (obstruction for fibred encodings, exact scope; PROVED relative to (C), ET, and — for (iii) — CTX
Thm 3.7).** *Class X:* power-fibred encodings `E(n) = ⨆_{θ∈Θ(n)} E_θ` (Θ(n) arbitrary, may grow with n, may be
defined through factorisations), where each piece `E_θ` is either
* (X1) Zariski-dense in an irreducible `V_θ/ℚ` with `φ|_{E_θ}` the restriction of a rational map; or
* (X2) a finite union of `Γ_θ`-orbits in setting (O) with (C), `φ` `Γ_θ`-invariant, and orbit weights in
  `[w_θ, R·w_θ]`. (R = C(Γ_θ) for compact or finite stabilisers (Thm 3.1(b)); `R = O(log n)` for the
  Pell/regulator encoding F2(iii).)

Let `μ(n)` be the maximal number of pieces (X1 pieces, X2 orbits) over one solution. Then:
1. *(Idle or normalised.)* X1 pieces are constant (`φ ≡ s_θ`, Thm 2.3). The normalised count
   `c̃(n) := Σ_θ c_θ/w_θ` (with `w_θ := c_θ` for X1 pieces) satisfies `#pieces ≤ c̃(n) ≤ R·μ(n)·f(n)`.
2. *(Scale constraint returns.)* A counting route proving `c̃(n) ≥ M(n)/2` needs `M(n) ≤ 2Rμ(n)f(n)`; with ET
   (RT1 §5.5) this is `≤ 2Rμ(n)ξ log³n log log n` outside a density-o(1) set of primes, for any ξ → ∞.
   The factor `H^δ` from the fibres cancels out of every such statement.
3. *(Mass formulas.)* A main term computed by a mass formula (Siegel–Weil, Borovoi–Rudnick) is the mass of a
   genus-full set `V_θ(ℤ) ∩ W_θ(n) ∩ Ω` with `W_θ(n)` adelic-open. Either `E_θ` is that whole set, and then (G simply
   connected, connected stabiliser, CTX hypotheses) `E_θ ≠ ∅` is decided by local and Brauer–Manin data, without
   counting; or `E_θ` is a proper subset, and the mass is not `c_θ`. In the first case the encoding is a criterion
   "local + BM data at n ⇒ ES(n)", and by 5.1 its vanishing at odd squares must be produced at the places dividing
   m. For the ES-natural genus-full sets (F5: all Gram embeddings; 5.3: `𝔊⁻_d`) the criterion is false: F5 contains
   `Q₀` at every n, and `𝔊⁻_d(p) ≠ ∅` at primes with `F_d(p) = 0`.
4. *(Bounded complexity.)* If Θ is finite and the X1 data are uniform in n (Cor 2.4), all large `p ≡ 1 (mod D')`
   are missed.
*Proof.* 1: Thm 2.3 and Thm 3.1(a),(b) piece by piece; each piece lies over one solution, and each solution
has ≤ μ pieces. 2: Lemma 1.3. 3: definitions, CTX Thm 3.7, Prop 5.1, F5 and 5.3. 4: Cor 2.4. ∎

**5.5 What escapes Theorem 5.4 (exact list; Assessment).**
* (E-a) Orbit encodings whose weights vary by a power of n *and* are not capped by the height of the solution:
  split-torus stabilisers whose regulators are not produced by the solution itself. Among ES encodings the only
  split torus that appears is the Type II Pell unit (F2), where the solution *is* the unit, which caps the weight at
  `O(log n)`. No other was found.
* (E-b) A *valid* uniform genus-full criterion with a Brauer/spinor factor at the place p (the 5.2 mechanism moved
  to ES). If it existed, ES(p) would follow from local + BM data of a homogeneous space (CTX), and counting would be
  unnecessary. The natural candidates (F5, `𝔊⁻_d`) fail validity by a factor `≍ h(−4dp)/F_d(p)`. Nothing in the
  campaign excludes an unnatural one; it would be a structural theorem "a nonempty genus at p forces a Type I/II
  solution", which is of the same strength as ES.
* (E-c) Recipes that are neither algebraic on dense pieces nor invariant under a lattice (for example procedures
  with floors, gcds and factorisations on the points of a non-homogeneous variety). They are outside class X, and
  in the scope of POINTWISE_SIZE Thm M (procedures) instead; counting theorems do not apply to them as such.
* Bilinear/parity-breaking sieves (Friedlander–Iwaniec, Heath-Brown) act at fixed p on the base problem (divisors of
  `N_θ(p)` in a moving class; RT2 H-B). Fibring them over free parameters is F1. They stay single-target counts with
  polylog mass, so fibring gives them no extra room.

## 6. Numerics (Step 4; EVIDENCE)

**6.1 F4 fibre counts** (`scripts/lsb_pair_orbits.py 3000` → `data/lsb/pair_orbits_H3000.out`). At
`(c,d) = (1,1)`, the `SL₂(ℤ)`-orbits of pairs `(Q,S)` with Gram matrix `4[−n,1,1]` have base points
`(Q_A, S_1)`, `Q_A = [A, A+1, ((A+1)²+4n)/4A]`, one for each odd divisor `A` (of either sign) of `4n+1`
(`b(Q,S_1) = 4B − 4A = 4`). The Type II orbits are those with `A > 0`, `A ≡ 3 (4)` (positivity plus the level
datum `4 | B`); `A = −1` is Q₀. For each orbit the script counts `#{γ ∈ PSL₂(ℤ) : max|coeff((Q,S)γ)| ≤ 3000}`.
| n | `4n+1` | orbits (genus-full) | ES orbits | per-orbit counts (min–max) |
|---|---|---|---|---|
| 29 | 117 | 12 | 2 | 1792–1818 |
| 41 | 165 | 16 | 4 | 1514–1526 |
| 53 | 213 | 8 | 2 | 1322–1330 |
| 9 = 3² | 37 | 4 | 0 | 3230 (all) |
| 25 = 5² | 101 | 4 | 0 | 1918 (all) |
| 49 = 7² | 197 | 4 | 0 | 1382 (all) |
For each n, every orbit (ES or not) has the same count to within 1.5% (at H = 400 they were within 3%). This is
Thm 3.1(b) in action: the fibre is a copy of `PSL₂(ℤ)` and carries no information. `#E_ES(≤H)` is `F_{1,1}(n)` times a
common orbit count, i.e. `c(n) = κ(n)·F_{1,1}(n)` with `F_{1,1}(n) = #{f | 4n+1 : f ≡ 3 (4)}` (O128 Prop 8.1).
At the odd squares the genus-full set still has 4 orbits, including Q₀, and the ES set is empty: every prime factor
of `4m²+1` is `≡ 1 (4)`. That is O128 Cor 6.2 at `c = d = 1`, the T1 mechanism. A mass formula for the genus-full
set gives a positive main term at the squares too (F5).

**6.2 Genus `𝔊⁻_d`** (§5.3): `#𝔊⁻_d = h/2` at all 40 (prime, level) pairs, `0` at all 40 (square, level) pairs; ES
counts `F_d(p) ∈ [0, 22]`.

**6.3 Spinor-exception control** (§5.2): `3x²+4y²+9z²`, N = 5·10⁴: 29 exceptions in the generically represented
classes, all of the predicted square shape, and all predicted squares are exceptions.
