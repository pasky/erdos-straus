# y8_siegel_weil_sign — the correct Siegel–Weil weighting of words, and why comparing it with |X_p| is circular (O217)

## Idea
Goal (a) of O217: use that the genus of I₃ = ℤ³ has one class (so r(T, I₃) = Siegel's local-density product exactly)
to get an exact formula for N₊(p), then compare with |X_p| to force a non-represented word.

**Prop 1 (PROVED; Siegel + one-class genus + TWO_FIBRES Thm A).** For a word w ∈ X_p (p prime) put
T_w = [[A*, 1], [1, A]], det tp. Then r(T_w, I₃) = c_∞ ∏_ℓ α_ℓ(T_w, I₃) and α_p(T_w, I₃) = 0 ⟺ χ(w) = −1;
α_p depends only on the ℤ_p-class of T_w ≅ ⟨A, A·tp⟩ (a function of χ(w) and (t/p)). Hence with
ρ₊(w) := c_∞ ∏_{ℓ≠p} α_ℓ(T_w, I₃) · α_p^{(+)}(t) (the value the product would have on the χ = +1 class),
  N₊(p) = Σ_w r(T_w, I₃)/ρ₊(w),   N₊(p) − N₋(p) = Σ_w (2 r(T_w, I₃)/ρ₊(w) − 1).
ρ₊(w) is NOT constant: r(T_w, I₃)/48 ∈ {1, 2, 3, 4} already for p ≤ 157 (depends on tp mod 8 and ω(tp)); this is
the source of O209's p = 5 mismatch (Σ r/48 = 6 vs N₊ = 5). All representations found for p ≤ 61 are primitive
(x × y primitive), so here r = r* and each χ = +1 word is counted by 2·#{primitive z ∈ ℤ³ : |z|² = tp, z^⊥ ≅⁺ T_w}.

**Prop 2 (PROVED; dictionary).** For χ = +1 words, z := x × y satisfies |z|² = tp, z^⊥ ⊇ ℤx + ℤy ≅ T_w, and
x × y ≡ x + y (mod t) (Thm A(iii)). The class of z^⊥ is the class of the ideal 𝔞_A = (A, 1 + √−tp) of norm A in
ℤ[√−tp] (a divisor of the principal ideal (1 + √−tp), norm tp + 1), and χ(w) = χ_p(𝔞_A) = (A/p) is the genus
character at p. So the words of level t are the factorisations (1 + √−tp) = 𝔞𝔞′ with N𝔞 ≡ N𝔞′ ≡ −1 (mod t), and
Gauss's map z ↦ [z^⊥] (onto the three-squares genus, equidistributed among its classes, Disq. Arith. art. 291–292;
Venkov) carries the χ = +1 ones.

**Prop 3 (circularity, PROVED).** Σ_w r(T_w, I₃)/ρ₊(w) is identically N₊(p) by Prop 1; an independent evaluation
would be a lattice-point count of {(x, y) ∈ ℤ³ × ℤ³ : x·y = 1, |x × y|² = tp, t | |x|² + 1, t | |y|² + 1, t ≥ 1},
whose defining conditions involve the unknown level t = |x × y|²/p as a modulus — not an orbit of an arithmetic group
on a quadric, so Siegel–Weil does not apply to the family (only term by term). Comparing with |X_p| therefore needs
exactly the divisor-in-class information it was meant to produce.

## Literature
Siegel, *Über die analytische Theorie der quadratischen Formen* (1935); Gauss, Disq. Arith. art. 278–292; Venkov,
*Elementary Number Theory* ch. 4 (three squares and classes); Kitaoka, *Arithmetic of quadratic forms* §6.8 (local
densities); Shemanske, "Representations of ternary quadratic forms and the class number of imaginary quadratic fields"
(Pacific J. Math. 122, 1986). Schulze-Pillot, "Representation by integral quadratic forms — a survey" (2004).

## Barrier screen
B2: Prop 2 is literally "a divisor of N_θ(p) = tp + 1 in the class −1 mod t with a genus-character condition".
B3/B6: Siegel–Weil weights are main terms per T; the family sum is an extraction (O205 Thm 2.2, O209 §3.3).
T1: at p = m², 𝔞_A ⊂ ℤ[m√−t] and χ_p is trivial (the "p-genus character" disappears) — consistent.

## Cheap numerics (`scripts/y8_gauss_weight.py`)
* Thm A re-checked by brute-force vectors: all 166 words of primes 5 ≤ p ≤ 61 (r(T_w, I₃) > 0 ⟺ χ = +1, 0 mismatches).
* Σ_w r/48 vs N₊: (5: 6 vs 5), (13: 10 vs 7), (17: 16 vs 11), (29: 16 vs 11), (53: 22 vs 13), (61: 16 vs 9).
* Per-word r/48 for p = 101: (tp mod 8, ω(tp), r) = (2,2,48)×2, (2,3,144)×2, (3,2,96)×3, (5,1,48)×4.

## Assessment
PROVED (Props 1–3, classical inputs) / CERTIFIED (small checks). Negative for goal (a): the correct weighting exists
and is explicit, but it is a term-by-term identity; it cannot be compared with |X_p| without B2 information.
