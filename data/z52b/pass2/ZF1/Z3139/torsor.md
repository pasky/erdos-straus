# Z3139 — universal torsor of the ES surface vs the Elsholtz–Tao parametrisation

**Premise check.** BL §2.1 (sources/bright-loughran-1908.02526.pdf): S_n: 4x₁x₂x₃ = n(x₀x₁x₂ + x₀x₁x₃ + x₀x₂x₃) ⊂ P³ is
isomorphic over Q to Cayley's 4A1 cubic Σ 1/t_i = 0 ((t₁,t₂,t₃,t₄) = (x,y,z,−n w/4)); 4 A1 nodes, 9 lines, all over Q.
BL Lemma 2.3: Pic Ũ_n = ℤ (affine resolved surface), V_n = Ũ_n ∖ (3 lines) ≅ G_m².
Derenthal (arXiv:math/0604194, Table 7, read): type 4A1 has 9 lines and "≥ 2 relations" (reference [HB03] = Heath-Brown,
Cayley cubic, arXiv:math/0210333: N(B) ≍ B(log B)⁶). So the torsor is NOT a hypersurface — this settles Pass 1's open question.

**Torsor equations (PROVED here, sympy-checked: scripts/z52d_p2_ZF1_Z3139_torsor.py → torsor_check.txt).**
X̃ = blow-up of P² in the 6 vertices P_ij = L_i ∩ L_j of a complete quadrilateral L₁+L₂+L₃+L₄ = 0. Negative curves:
4 strict transforms ℓ_i (class H − Σ_{j≠i}E_ij, the (−2)-curves), 6 exceptional e_ij, 3 diagonals d_{ij|kl}
(H − E_ij − E_kl). Cox ring generators: 13 (= 4 + 9); torsor dimension 2 + rk Pic = 9; relations
  R:  ℓ₁e₁₂e₁₃e₁₄ + ℓ₂e₁₂e₂₃e₂₄ + ℓ₃e₁₃e₂₃e₃₄ + ℓ₄e₁₄e₂₄e₃₄ = 0,
  d_{ij|kl}·e_kl = ℓ_i e_ik e_il + ℓ_j e_jk e_jl  (= −(ℓ_k e_ki e_kj + ℓ_l e_li e_lj)·e_kl/e_ij; the two forms agree ⟺ R),
three diagonals → 6 trinomials, ≥ 2 independent (consistent with Derenthal). Anticanonical map:
t_i = ∏_{j≠i} ℓ_j · ∏_{{a,b}∌i} e_ab; checked: σ₃(t) = R · ℓ₁²ℓ₂²ℓ₃²ℓ₄² ∏ e_ab (so Σ 1/t_i = 0 on the torsor).
Variables per equation: R has 13−3 = 10 variables (4 monomials of degree 4); each diagonal trinomial 6 variables, degree 3.

**Comparison with ET (sources/elsholtz-tao-1107.1010.pdf §2, eqs (2.1)–(2.9), Prop 2.2/2.6/2.7).** The w-slot
t₄ = −n/4 = λ·ℓ₁ℓ₂ℓ₃e₁₂e₁₃e₂₃ forces the six "w-face" variables to be divisors of n (bounded; for n = p prime, p sits in
exactly one slot). Specialising (ℓ₁,ℓ₂,ℓ₃,e₁₂,e₁₃,e₂₃) = (1,1,1,1,1,n), λ = −1/4, ℓ₄ = −4d and
(a,b,c,e,f) = (e₃₄, e₂₄, e₁₄, d_{23|14}, d_{13|24}) gives EXACTLY ET's Σ^I_n: (x,y,z) = (abdn, acd, bcd), R → 4abcd = na+nb+c
(2.3), diagonals → ce = a+b (2.2), bf = na+c (2.8), and a·f′ = nb+c (the third diagonal, f′ = 4bcd − n, cf. (2.9)).
Putting n into ℓ₁ instead gives Type II: (x,y,z) = (abd, acdn, bcdn), 4abcd = a + b + nc (ET Prop 2.7). The 6 w-face slots
↔ 3 Type I + 3 Type II placements of p. ET's dilation (2.10) is the residual G_m = the universal torsor of the affine
Ũ_n (Pic ℤ, BL Lemma 2.3). Hence: **ET's Σ^{I/II}_n already IS the descent** (projective 9-dim torsor restricted to the
n-face: 7 variables, 3-dim), not a cruder parametrisation.

**Circle-method question (Assessment, with one PROVED step).** Descent is a bijection on integral points (ET Prop 2.2,
2.6), so the count stays f(p) ≍ polylog (ET Thm 1.1); the 13-variable torsor has many variables only for rational
points of bounded height (Heath-Brown's B(log B)⁶), where the 6 w-face variables are free. For fixed n those 6 variables
are frozen and the remaining system is 3 equations in 7 variables (degrees 4, 3, 3, 3) on a 3-fold — a "more variables"
gain does not exist, and the main term is polylog, not a power (B2/B3). Next variable-increasing step would have to be a
non-universal (e.g. Type-II-only, or level-t) torsor over a cover; none suggested itself.

Not done: no Gröbner basis of the full ideal (number of minimal relations not determined — Derenthal says ≥ 2; the 6
trinomials + R generate at least a codim-4 locus by construction, but minimality/saturation was not checked); no Heath-
Brown 2003 details read beyond the abstract and Derenthal's citation; integral model of the torsor over ℤ (signs, the
factor 4 and 2-adic units) only handled by the λ = −1/4 scaling.
