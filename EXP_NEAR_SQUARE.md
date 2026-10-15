# EXP_NEAR_SQUARE — exponential near-squares 4^s + k: mixed profinite points, k = 105, S-unit near-squares (task O235)

Status: in progress (O235). **ES is not solved here, nor any infinite case of it unless stated with a complete proof and a
replayed certificate.** Labels as in DISCOVERIES.md. Builds on SIGN_FIELDS.md §1 (O232: Thm 1.3, Lemmas 1.1–1.2,
§1.4), EXPONENT_COVERING.md ((J)22: Thm 1.4 compactness criterion), NEAR_SQUARE.md ((J)55). Memos BRAINSTORM/z11_*.md,
scripts `scripts/z11_*`, certificates `data/z11/`.

Notation. n_s = c₀·4^s + k (c₀ = 1 unless stated). Exponent space Ẑ = Π_ℓ ℤ_ℓ; ν(μ) ∈ Ẑ (n-space) with ν(μ)_2 = k and
ν(μ)_q = c₀·4^μ + k for odd q. A *class* = an ET Prop 1.9 residue class (M, r) (mordell_lib's seven families) or a
divisor class D_q (q | n, q odd prime, q ∤ k). For a class of modulus M = 2^a·M′, L_M := lcm_{q^e ∥ M′} ord_{q^e}(4);
for s ≥ a/2, n_s mod M depends only on s mod L_M, so the class pulls back to a clopen set E_M ⊂ Ẑ of period L_M.

## 0. Plan
1. Tree (per-branch) coverings of Ẑ instead of the global-period lifting of z8_adaptive: a node is a residue u mod L;
   it is a leaf if one class with L_M | L contains it, else it is split to lcm(L, L_M′) for a well-chosen class.
   Certificate size = number of leaves, not the global period. Independent replay checker.
2. Mixed points: classify the Ẑ-points that evade all divisor classes of the integer square points; test sterility.
3. k = 33, 273, 297; then c₀ ∈ {2, 3, 5} and 4^a·9^b + k.
4. Conceptual: which k admit a covering.
