# AGENT_REPORT_O143 — brainstorm: cubic surface / Markoff / cluster / elliptic angles

Branch `side-agent/bs-cubic-markoff`. Four memos in `BRAINSTORM/`, scripts `scripts/bs_cubic_*` (all run in
seconds to about a minute; outputs quoted in the memos). **No LIVE angle.** ES is not claimed.

**Memo 1, `cayley_markoff_cm.md` — PARTIAL (exact dictionary), collapses to B2 at the fixed-(K, β) step.**
* ES is the level-4 integral model of Cayley's symmetric cubic Σ_{i=0}^{3} 1/y_i = 0, with y = (4u₁, 4u₂, 4u₃, −n).
* The Markoff surface V_4 is the chart of the same cubic with the Sylvester plane e₁ = 0 removed; U_n is the chart
  with a face removed. The two are not isomorphic (1 vs 4 singular points), and there is no integral
  correspondence.
* U_n has no Vieta involutions: the second root escapes into a node at infinity. ES is the "no square terms"
  degeneration of the Markoff-type family.
* Positive ES points of all n are exactly the rational points on the open faces of the compact (SU(2)) tetrahedron
  of the Cayley cubic.
* Their CM field is ℚ(√−D) with **D ≡ n·u₁u₂u₃ (mod squares)**, which is **d for Type I and dp for Type II**. This
  gives a geometric origin of the campaign's Heegner discriminants −4d / −4dp (checked on all 2256 solutions,
  p < 400).
* Markoff moves do map ES points of 4/n to ES points of 4/n' with K fixed (4/5 → 4/32 → 4/64 → 4/4471 → …).
* Strongest reason it is not a route: orbits are polylog-sparse, and at fixed K and β the condition is the CM-torus
  divisor problem (EXACT_FORMULA Thm 5.2), i.e. B2.

**Memo 2, `markoff_hasse_failures_vs_es.md` — COLLAPSES as a route (B2/B6); two sharp by-products.**
* Validation: Ghosh–Sarnak Table 3 reproduced exactly (12.98% failures, k ≤ 100800).
* EVIDENCE: Markoff h(k) ≈ Poisson(λ) with λ ∝ the local singular series (failure rate 0.86 → 0.0004 across S
  sextiles). GS's ≈ K^{0.89} failures are local-density-driven.
* PROVED: ES local densities at every ℓ ≠ p are p-independent (𝒰_p ≅ 𝒰_1 over ℤ_ℓ), and so is BL's α. Any adelic
  or BM-weighted main term for f(p) is therefore flat in p mod ℓ.
* EVIDENCE (all 2567 primes in (10⁵, 1.3·10⁵)): the true f(p) class means mod 840 vary by ×14 (square classes
  lowest, 0.050 vs 0.697 at p ≡ 839). **The ES main term is non-adelic**, which is a quantitative form of BL
  Thm 1.9.
* PROVED: GS's failure mechanism needs a non-square right-hand side 4(k−4) in its fibre identity. ES's identity
  has right-hand side (nu₁)², a square, so it has no reciprocity content. The GS-(iii) reciprocity+size mechanism
  dies on Type II, which is genus-free.
* Strongest reason it is not a route: GS's existence theorem is a variance average over k (T7), and for ES any
  adelic comparison function is off by O(1)× the main term (T2).

**Memo 3, `elliptic_fibration_es.md` — COLLAPSES (integrality vs rationality; B2 per fibre).**
* The genus-1 pencil u₁+u₂+u₃ = s is the n-independent family C_N : (x+y+z)(xy+yz+zx) = Nxyz, N = 4s/n, with
  Weierstrass discriminant 4096N²(N−9)(N−1)³ and fibres I₂ (node P), I₃ (the lines M_k), I₁ (AM–HM point),
  I₆ (boundary).
* It is a rational elliptic surface of **MW rank 0**, so no section carries ES points and every ES point is a
  sporadic rank-jump point.
* Repeated-entry points are torsion (PROVED); for p ≡ 1 (4) there are none (PROVED); all other tested points are
  non-torsion (EVIDENCE, 441 points).
* Strongest reason it is not a route: ES points have ĥ ≪ log p ≍ log(conductor). They are Lang-scale *small*
  points, which no rank, Heegner or Gross–Zagier statement produces. Each fibre is a lottery with expectation
  p^{−2+o(1)}.

**Memo 4, `rational_to_integral_cubic.md` — COLLAPSES.**
* The split torus gives only the trivial point.
* The anisotropic CM tori lead to a gcd-absorption condition (B2).
* Node-local structure is the (F1) conic bundle.
* Davenport–Cassels/Aubry rounding needs an anisotropic Euclidean quadric, but every quadratic structure in ES is
  split or isotropic (GEOMETRY_ES Prop 3.2).
* Manin's secant–tangent composition gives B1 at bounded depth and sparse B2 at unbounded depth.
* By-product (PROVED, elementary): 𝒰_p mod p is the union of the three coordinate planes (the toric boundary).
  ET Type I/II are exactly its open 2-dimensional and 1-dimensional strata, and the vertex stratum is empty.

**Suggested ledger items (for the parent to judge):**
* the CM dictionary D ≡ n u₁u₂u₃ (memo 1, P4);
* local flatness plus the ×14 non-adelic mod-840 bias (memo 2, F3/F4);
* the s-pencil fibre table and MW rank 0 (memo 3, P2).

Items marked "from memory" (Weierstrass model / BGN, Oguiso–Shioda ℤ/6, Davenport–Cassels, Manin) were not
re-verified against sources. The Weierstrass model is supported by point counts only, i.e. up to isogeny.
