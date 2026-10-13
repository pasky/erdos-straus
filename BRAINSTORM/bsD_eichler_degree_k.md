# bsD_eichler_degree_k — a "Diff-parity for degree-k cyclic algebras" exists only as a tautology; the supersingular geometry is a degree-2 accident (Br ℝ = ℤ/2) (O177)

**ES is not solved here.** Labels as in DISCOVERIES.md. No script (classical structure; numerics in bsD_cubic_test).

## Idea
Orchestrator's main escape candidate: replace the quaternion algebra B_T (local invariants ±1, Σ = 0 ⇒ |Diff| odd ⇒
supersingular points exist) by a **degree-k cyclic algebra** with invariants in (1/k)ℤ/ℤ, k = order of the ray
character, hoping for a reciprocity that *forces* an order-k condition on the ES divisor f.

## Literature
Albert–Brauer–Hasse–Noether (Pierce, *Associative Algebras*, §18.4: 0 → Br ℚ → ⊕_v Br ℚ_v → ℚ/ℤ → 0);
cyclic algebras and their local invariants: Pierce §15, Serre *Local Fields* XIV; Eichler's theorem / strong approximation:
Reiner, *Maximal Orders* (1975), §34 (Thm 34.9) and §35; Swan, *Strong approximation and locally free modules* (1980);
Voight, *Quaternion Algebras* (2021), §28.5 (Eichler condition) and Ch. 42 (supersingular class set);
Landherr (1936) / Scharlau, *Quadratic and Hermitian Forms*, X.6 (hermitian forms over number fields: local
invariants ±1 with product 1); Rapoport–Zink, *Period spaces for p-divisible groups* (1996), Ch. 6 (basic-locus
uniformization by the inner form).

## Statement
**Prop 1 (the degree-k "Diff-sum" is Artin reciprocity; PROVED, classical).** Let χ be a Dirichlet character of
order k and conductor q, f ∈ ℚ^×, A(χ, f) the cyclic algebra (L_χ/ℚ, σ, f). For ℓ ∤ q, exp(2πi·inv_ℓ A) =
χ(ℓ)^{v_ℓ(f)} (normalised suitably); the places ℓ | q·∞ carry the local symbols of f. The ABHN law Σ_v inv_v = 0 is
χ(f_{(q)}) = ∏_{ℓ∤q} χ(ℓ)^{v_ℓ(f)} — multiplicativity of χ. Consequently, for M fixed and gcd(f, M) = 1:
`f ≡ −1 (mod M)` ⟺ for every χ mod M, the "finite Diff-sum" Σ_{ℓ ∤ M} inv_ℓ A(χ, f) equals that of A(χ, −1)
(i.e. 0 for χ even, 1/2 for χ odd). **So the ES ray condition *is* a family of degree-k Diff-sum identities** — but
the dictionary is tautological: it restates the class of f, it forces nothing.
**Prop 2 (why only degree 2 has a forcing geometry; PROVED, classical inputs).** Over ℚ, Br ℝ = ℤ/2. Hence:
(i) a central simple ℚ-algebra A of degree k ≥ 3, or of degree 2 split at ∞, satisfies Eichler's condition; by
Eichler's theorem the locally free class set of a maximal order is in bijection with the narrow class group of ℚ,
which is trivial, and the type set (conjugacy classes of maximal orders) is a single class. "Some order in the genus
has property P" = "every order has P" and is decided by local data, i.e. congruences (B1).
(ii) The only ℚ-algebras violating Eichler's condition are the **definite quaternion algebras**; for them inv_∞ = 1/2
forces |Ram_f| odd — this is exactly Kudla's Diff-parity, and the non-trivial class set (≈ p/12 supersingular curves)
is exactly the failure of strong approximation. **Diff-parity and the supersingular geometry are the same
phenomenon, and both are 2-torsion because Br ℝ = ℤ/2.**
(iii) Outer forms: definite unitary groups (any rank, over imaginary quadratic E) do have non-trivial class sets,
but their incoherence law is Landherr's: local invariants ε_v ∈ {±1} with ∏ ε_v = 1 — quadratic again
(bsC_parity_quadratic_only Prop 1 applies). For GU(D), D of degree k over E with an involution of the second kind,
cores_{E/ℚ} D = 0 forces inv_{w̄} = −inv_w at split ℓ = w w̄: the order-k invariants come in opposite pairs, and
their sum at ℓ is 0 identically (the corestriction collapse of bsD_brauer_cores in algebra form); the only global
parity is again Landherr's ±1.
*Proof sketch.* (i) Reiner Thm 34.9 + Swan: Eichler condition ⇒ strong approximation for SL₁(A) ⇒ locally free class
set ≅ Cl⁺ via nrd; types of maximal orders are a quotient of that set. (ii) A ⊗ ℝ a division algebra ⟺ A ⊗ ℝ ≅ ℍ
(Frobenius), degree 2. ABHN: inv_∞ = 1/2 ⇒ Σ_{ℓ} inv_ℓ = 1/2 ⇒ odd number of finite ramified places (all invariants
1/2 in degree 2). (iii) Involution of the 2nd kind on D/E exists iff cores_{E/ℚ}[D] = 0 (Knus–Merkurjev–Rost–Tignol,
*Book of Involutions*, Thm 3.1); at split ℓ, cores is the sum of the two invariants. ∎

## Barrier screen
* **Hypothesis map of the orchestrator's escape.** "Higher-order Diff-parity" needs (α) local invariants of order k
  *and* (β) a non-trivial global class set / incoherence (so that "∃ object" is a non-local statement). (α) and (β)
  are incompatible over ℚ: (β) requires compactness at ∞, available for inner forms only in degree 2 (ℍ), and for
  outer (unitary) forms only with ±1 incoherence (Landherr) or paired invariants (iii).
* Escape attempt: base fields with more real places (totally real F, D of degree k over F)? Br(ℝ) = ℤ/2 at every real
  place, same conclusion; CM fields: unitary case (iii). Function fields F_q(T)? The place ∞ has Br = ℚ/ℤ —
  **degree-k definite algebras exist over F_q(T)** (Drinfeld modules of rank k, supersingular loci of rank-k Drinfeld
  modular varieties with D_∞ of invariant 1/k). So the escape is *genuinely available over function fields only*:
  see sparks (the F_q[T] ES analogue lacks T1 for odd q — FUNCTIONFIELD_ES Prop 4.1 — consistent).
* T1: passes (the degree-2 case is T1). B1: Prop 2(i) — all degree ≥ 3 local–global content is congruence data.

## Assessment
PROVED structural negative with exact scope: **over ℚ (and any number field) a forcing "degree-k Diff-parity" does
not exist; the ES ray condition is a degree-k Diff-sum only tautologically (Prop 1), and the existence engine (odd
|Diff| ⇒ supersingular objects) is tied to Br ℝ = ℤ/2 (Prop 2).** The one structural loophole is the function-field
place ∞ (Br F_q((1/T)) = ℚ/ℤ, rank-k Drinfeld supersingular loci). Promise 1 over ℚ; 2 as a function-field spark.
