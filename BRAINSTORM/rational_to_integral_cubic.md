# From rational to integral points on the nodal ES cubic: tori, nodes, rounding, secants (O143, memo 4)

Labels as in DISCOVERIES.md. Uses memo 1 (`cayley_markoff_cm.md`) and memo 3 (`elliptic_fibration_es.md`).
Strong approximation with Brauer–Manin is closed by GEOMETRY_ES §1/§6 (BL Thm 1.9), so we screen the other
"rational ⇒ integral" mechanisms known for surfaces.

## 1. Idea
U_n(ℚ) is dense (the surface is rational), and every positive rational point of U_n is an ES point of *some*
multiple of n after scaling. ES(p) asks for a positive rational point whose denominators are absorbed by p alone.
Is there a mechanism that moves a rational point to an integral one, or that reduces denominators?
Candidates:
* (M1) integral points of the tori inside the surface;
* (M2) the local structure at the four nodes and the reduction mod p;
* (M3) Aubry / Davenport–Cassels rounding;
* (M4) Manin's secant–tangent composition on cubic surfaces.

## 2. Screens (PROVED unless labelled)

**M1a, the split torus V_n ≅ 𝔾_m² (BL Lemma 2.1).** Its characters are u_i/u_j. Torus-integral points have u_i/u_j
∈ ℤ^× = {±1}, so the only positive ones have u₁ = u₂ = u₃, i.e. the trivial point 3/u = 4/n (4 | n). ES-integral
points are not torus-integral, and the torus action does not extend to 𝒰_n (BL Remark 3.12). **Dead.**

**M1b, the anisotropic tori T_K¹ × T_K¹ (memo 1, P4).** Their integral points are finite (norm-one units of an
imaginary quadratic order are roots of unity), so they yield only finitely many points with fixed K. Their
rational points are α/ᾱ (Hilbert 90). Strong approximation fails for T_K¹, which is anisotropic at ∞ (from
memory, standard), and weak approximation only controls finitely many places. The ES condition, written in
memo 1's coordinates, is a **gcd-absorption** condition: D·y·y'·Re(αβ) / gcd(y₀,…,y₃) = p up to 2-powers (Type I).
It is a condition at all primes simultaneously, with moduli made of the coordinates. **Collapses to B2.**

**M2, nodes and reduction mod p.** Near each node the surface is a quadric cone AB = C² (≅ 𝔸²/±1). For the node Q₁
at infinity, the cone in the coordinates of the fibre u₁ = const is
`((4u₁−n)u₂ − nu₁)((4u₁−n)u₃ − nu₁) = (nu₁)²`:
the conic bundle (F1) of GEOMETRY_ES §3.1, whose integral points are divisors in a residue class (B2). New
observation:
* **(PROVED) The reduction of 𝒰_p mod p is the toric boundary.** Mod p the equation reads 4u₁u₂u₃ ≡ 0, the
  union of the three coordinate planes. So 𝒰_p/ℤ_p is a degeneration of the log CY U_p to the union of the
  three planes (a "vertex" degeneration as in Gross–Hacking–Keel mirror constructions; analogy only, from
  memory).
* ES points reduce into the strata. **Type I** (exactly one p | u_i) lands in an open 2-dimensional stratum,
  **Type II** (exactly two) in a 1-dimensional stratum.
* The 0-dimensional stratum is empty: if p | u₁, u₂, u₃ then 4 = Σ p/u_i ≤ 3.

So the ET type is the p-adic "tropical" position (v_p(u₁), v_p(u₂), v_p(u₃)) of the point. This gives a clean
geometric meaning to the dichotomy, with the odd-square failure of Type I/II being BL's Brauer class on the
open strata. But it supplies no existence input: the degeneration is fixed, and integral points of the general
fibre are not controlled by the special fibre (Hensel lifts give ℤ_p-points, never global ones). **Collapses**
(B2/T8: the coarse invariant is the stratum; lifting it is the slice divisor problem).

**M3, Aubry / Davenport–Cassels rounding.** The mechanism: on an anisotropic quadric q(x) = m with a Euclidean
condition (for every x ∈ ℚ^k some y ∈ ℤ^k has |q(x−y)| < 1), the line through a rational solution x and a
lattice point y meets the quadric again at a solution with strictly smaller denominator. So rational ⇒ integral.
Requirements and what ES offers:
* (a) A quadric, i.e. a degree-2 structure in which a line meets the variety in exactly one further point. On
  the ES cubic, lines through a smooth rational point and an integral point meet S in two further points,
  conjugate in general (not rational). Lines through the node P meet S in one further point. But that is the
  rational parametrisation (projection from P), and its "rounding" is exactly choosing a direction with
  divisibility: the s-coordinates of GEOMETRY_ES §2.2.
* (b) Anisotropy plus a Euclidean property. The quadratic structures inside ES are the split conics (F1)–(F3)
  (GEOMETRY_ES Prop 3.2) and the isotropic hyperboloids X_d : ef − 4da² = 1. Split or isotropic forms are never
  Euclidean in the DC sense. For XY = N rounding is vacuous: every rational x gives a rational point, and
  integrality is "x | N".
* (c) The ES side conditions (4da | f + p, or a ≡ −b (mod e)) have point-dependent moduli. DC rounding changes the
  point and destroys them.

**Collapses** at (b); this is the precise reason in Prop 3.2 form. (The CM norm forms of memo 1 are anisotropic,
and Euclidean for d ∈ {1, 2, 3, 7, 11}, but ES is not a norm-representation problem on them; see M1b.)

**M4, Manin's secant–tangent composition.** For rational points P, Q of the cubic, the third point on line PQ is
`R = D_P F(Q)·P − D_Q F(P)·Q`, using F(λP + μQ) = λ²μ D_Q F(P) + λμ² D_P F(Q).
* With the total family viewed as the cone over the Cayley cubic (x₀ = n), we get
  x₀(R) = D_PF(Q)·n − D_QF(P)·n', and the new n'' is x₀(R)/gcd(R).
* At an ES point, ∇F = (−e₂, x₀x₂x₃/x₁, x₀x₁x₃/x₂, x₀x₁x₂/x₃), so the signs of D_PF(Q) and D_QF(P) are indefinite,
  and R is positive only for suitable pairs.
* Tangent sections give rational curves of points: polynomial families, hence B1.

Bounded-depth compositions are algebraic recipes of bounded complexity, so LONGSHOT_FIBRED Cor 2.4 applies.
Unbounded depth gives heights that grow multiplicatively, so ≪ (log N)^{O(1)} outputs per seed set below N (as for
memo 1, P5). Hitting n'' = p requires D_PF(Q)n − D_QF(P)n' = p·gcd: one linear equation whose coefficients
are values at the seeds, which is B2 again. **Collapses** (B1 at bounded depth, sparsity/B2 at unbounded depth).

## 3. Literature anchor
* BL (arXiv:1908.02526) Lemma 2.1, Remark 3.12, Thm 1.9 (as recorded in GEOMETRY_ES).
* Davenport–Cassels lemma and Aubry's argument (Serre, *A Course in Arithmetic*, Ch. IV, Appendix; from memory).
* Manin, *Cubic Forms*, for secant/tangent composition and the Mordell–Weil problem for cubic surfaces (from
  memory). Siksek (J. Number Theory 2012) on the number of generators for smooth cubic surfaces (from memory;
  the ES cubic is singular, so it does not apply directly).
* Gross–Hacking–Keel for degenerations of log CY surfaces (analogy only).

## 4. Barrier screen summary
* **B1:** M4 at bounded depth, and tangent curves.
* **B2:** M1b, M2 and M4 all end in "a specific integer has a divisor in a class modulo a coordinate".
* **B3:** no main term anywhere.
* **B5 / T1:** M2 explains the odd-square obstruction structurally (Type I/II = open strata of the reduction
  mod p; BL's α is non-trivial there). Nothing produces points, so nothing is false at m². ES(m²) points reduce
  into the strata of 𝒰_{m²} mod primes q | m by the same rule.
* **B6:** not applicable; no averaging is used.

## 5. Viability Assessment
**COLLAPSES** (M1a dead; M1b/M2 → B2; M3 fails at anisotropy (b); M4 → B1/B2).

By-product (PROVED, elementary): the reduction-mod-p picture of M2. 𝒰_p ⊗ 𝔽_p is the union of the three
coordinate planes, ET Type I/II are the open 2-dimensional and 1-dimensional strata, and the vertex stratum is
empty. Novelty unverified; it is presumably implicit in ET/BL. It is a convenient language, not a lever.

No experiment was needed: all statements are elementary identities.

## Errata (triage O156/O157)

Appended by O160; the memo body above is unchanged. Source: reviews/triage-brainstorm-B.md (§0.3 and the per-memo
paragraph). Counterexamples re-verified by `scripts/errata_check.py` (tag in brackets).

* **M3(b): "split or isotropic forms are never Euclidean in the DC sense" is false.** q(x,y) = xy with coordinatewise
  nearest-integer rounding gives |q(x−a, y−b)| ≤ 1/4 < 1 [M3b]. Anisotropy can still matter because q(error) = 0
  obstructs the descent formula; the displayed inequality itself is not the obstruction.
* M4 invokes LONGSHOT_FIBRED Cor 2.4 without its hypotheses (geometrically irreducible fibres, Zariski-dense
  integral solver subsets). Unbounded composition need not grow height: secant composition with a fixed point is
  generically involutive. The polylog output bound is unsupported.
* M2: the vertex is not empty as a scheme (it contains (0,0,0)); only reductions of positive ES(p) points avoid it.
  The square extension needs care: ES(9) has (3,12,36), which reduces to the vertex mod 3.
* **Corrected verdict:** PARTIAL → H-F (displayed instantiations collapse; a positivity-preserving descent with
  strictly decreasing denominator is not excluded, though no candidate move exists).
