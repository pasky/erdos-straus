# Brainstorm O149(b): tropical geometry, Newton polygons, valuations and amoebas

ES is not solved; nothing here proves any case of it. Script: `scripts/bs_padic_valpatterns.py`.

## 1. Idea

Tropicalise the ES variety at each place, and ask whether the tropical picture constrains the existence of
integral points of bounded height. Candidate tools:
* ℓ-adic Newton polygons of an auxiliary polynomial whose roots encode solutions;
* tropical curve counts;
* the archimedean amoeba of the fixed-p variety near the "Planck-scale" targets (Type I tubes of width 1/p).

To prove ES this way, one would need a tropical (piecewise-linear, valuation-level) certificate that lifts to
an actual positive integral point for every prime p.

## 2. Literature anchor

* Tropical geometry: Maclagan–Sturmfels; the fundamental theorem (Kapranov) says that trop(V) over a valued
  field is the closure of the valuation image. From memory, standard.
* Tropical linear spaces: the plane t_1+t_2+t_3 = 1 tropicalises to the Bergman fan of the uniform matroid
  U_{3,4}. From memory.
* Mikhalkin's correspondence theorem counts complex/real curves through generic points. It is enumerative over
  fields and gives nothing about integrality. From memory.
* GEOMETRY_ES §2.2 gives the toric model: U_n° ≅ {s ∈ G_m³ : Σs_i = 4/n}. Positive points correspond to
  primitive (s_1:s_2:s_3) ∈ ℕ³ with 4s_i | nS.

## 3. Results

Write 4/p = Σ1/u_i, i.e. the plane Σ t_i = 1 with t_i = p/(4u_i).

**Prop T1 (local tropical balancing; PROVED, elementary; EVIDENCE check on all 3756 unordered solutions,
p < 600).**
* *Odd ℓ ∤ p.* The maximum of v_ℓ(u_i) is attained at least twice.
* *ℓ = 2.* The maximum W of v_2(u_i) is attained at least twice, and W ≥ 1.
* *ℓ = p.* There are exactly two patterns: (0,0,1) (Type I: p ∥ the one p-divisible denominator) and
  (0,1,1) (Type II).

*Proof.* Odd ℓ ∤ p: v_ℓ(4/p) = 0, so the minimum of the v_ℓ(1/u_i) must be attained twice, unless it is ≥ 0.

ℓ = 2: v_2(4/p) = 2 exceeds every v_2(1/u_i). If all u_i are odd, then Σ1/u_i has odd numerator
xy+yz+zx (a sum of three odd numbers), so it has valuation 0 ≠ 2.

ℓ = p, Type I: v_p(4/p − 1/x − 1/y) = −1 forces p ∥ z.

ℓ = p, Type II: tropical balancing gives v_p(y) = v_p(z) = a ≥ 1. Suppose a ≥ 2. Write y = p²y'', z = p²z''.
Then 1/y'' + 1/z'' = p(4x−p)/x. The smallest coordinate satisfies p < 4x ≤ 3p, so 2x/p < 2. Since
1/y'' + 1/z'' ≤ 2, we get 4x − p ≤ 2x/p < 2, so 4x − p = 1. But then the right side equals 4p/(p+1) > 2,
a contradiction. ∎

The case a ≥ 2 is excluded by the *archimedean* place (positivity), not by any valuation. This is the only place
in the tropical picture where positivity enters. The statement is presumably folklore: in ET's Type II
parametrisation it amounts to p ∤ c.

**Prop T2 (the adelic tropicalisation is injective, and lifting is the whole problem; PROVED, trivial).** A
positive rational point (t_1, t_2, t_3) is determined by its valuation vectors (v_ℓ(t_i))_ℓ. Prop T1 is
necessary at every place, and each local condition is realisable locally. So a "tropical certificate" for ES(p)
is a choice of factorisation patterns of u_1, u_2, u_3 compatible with T1. Whether it lifts is the global
archimedean identity Σt_i = 1, i.e. the original problem. Compare abc / S-unit equations: local valuation data
are always consistent, and the content is global.

**Newton polygons.** Fix the smallest denominator x. Then the pairs (y, z) correspond to
factorisations (Ay − B)(Az − B) = B², with A = 4x − p and B = px. For each pair, y and z are the roots of
A·T² − (2B + δ + δ')T + (B + δ)(B + δ')/A, where δδ' = B². The
ℓ-adic Newton polygon of any polynomial whose roots are the y-values records the v_ℓ of those roots, which is
factorisation data of B² = p²x². Existence of a root in the residue class y ≡ −B·A⁻¹ (mod … ) is the
"divisor of N_θ(p) in a class" event (B2), with N_θ = p²x². A Newton polygon sees valuations, never residue
classes of the cofactors, so it cannot decide the event.

**Amoebas.** The positive part of {Σt_i = 1} maps under Log to the log-image of an open simplex. The solutions
have log t_i = log(p/4) − log u_i. Near the Type I corner (u_3 ≍ p²), the integral points have spacing ≍ 1/p²
in log u_3. The amoeba/tropical limit (Log base → ∞) sends this spacing to 0, so integrality is invisible there.
At finite base, the "target region" is the Planck-scale tube of POINTWISE_SPECTRAL (I)3, restated in log
coordinates. Tropical curve counting counts curves, not integral points.

## 4. Barrier screen

* **B1.** Every tropical/Newton-polygon datum at a finite place is valuation data. That is congruence data
  modulo prime powers (Haar/CRT), so Theorem M / Prop A apply.
* **B2.** A tropical certificate is a factorisation pattern, i.e. a slice (redteam-2 Thm 2.2). It lifts iff a
  specific integer has a divisor in a specific class. Over a fixed finite set of patterns, it fails infinitely
  often (CONDITIONAL on H).
* **B3.** No main term at all, so the scale constraint is not reached.
* **B5 / T1.** At n = m², Prop T1's conditions at every ℓ ∤ m are again satisfiable. The step that fails is
  "tropical certificate ⇒ lift" (Prop T2), which is the problem itself.
* **B6.** Not applicable: no averaging is involved.

## 5. Viability Assessment

**COLLAPSES to B1/B2 at step "valuation data ⇒ residue-class data of cofactors".** Strongest reason: the
adelic tropicalisation is injective on positive rationals (T2). So a tropical certificate *is* a factorisation
pattern, and its liftability is the slice divisor event.

By-product (PROVED, elementary, probably folklore): the exact p-adic patterns (0,0,1) / (0,1,1) for prime n.
Pole order ≥ 2 at p is ruled out by the archimedean place alone.
