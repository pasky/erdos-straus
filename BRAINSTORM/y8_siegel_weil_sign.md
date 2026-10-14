# y8_siegel_weil_sign — the correct Siegel–Weil weighting of words, and why comparing it with |X_p| is circular (O217)

## Idea
Goal (a) of O217: use that the genus of I₃ = ℤ³ has one class (so r(T, I₃) = Siegel's local-density product exactly)
to get an exact formula for N₊(p), then compare with |X_p| to force a non-represented word.

**Prop 1 (PROVED; Siegel + one-class genus + Hilbert reciprocity; R-O217 repair).** For a word w ∈ X_p put
T_w = [[A*, 1], [1, A]], det tp. Then r(T_w, I₃) = c_∞ ∏_ℓ α_ℓ(T_w, I₃), and for χ(w) = −1 the local obstruction
sits at an even number of places: **both α_p and α₂ vanish** (e.g. p = 5, w = (1, 3, 4), T = [[3,1],[1,2]]: a vector of
norm 3 has three odd coordinates, one of norm 2 has two, so their dot product is even — no solution mod 4).
Consequently there is no canonical positive "χ = +1 extension" ρ₊ of the Siegel product to negative words (the
checkpoint-1 version divided by ρ₊ and was 0/0 on χ = −1 words — withdrawn). The only exact statements are
N₊(p) = #{w : r(T_w, I₃) > 0} and Σ_w r(T_w, I₃) = Σ_{χ(w)=+1} r(T_w, I₃), with r(T_w, I₃)/48 ∈ {1, 2, 3, 4, 6}
for p ≤ 157 (reviewer's enumeration; this is the source of O209's 5-vs-6 mismatch). Representations need not be
primitive: p = 61, w = (63, 1, 1) has r = 288, r* = 192 (x = (−7,−3,−2), y = (1,−6,5), x × y = (−27, 33, 45)
divisible by 3).

**Prop 2 (dictionary; PROVED for compatible embeddings and primitive forms).** For χ = +1 words and a compatible
pair (x, y) of Thm A(iii) (x × y ≡ x + y mod t), z := x × y has |z|² = tp; if z is primitive, z^⊥ = ℤx + ℤy ≅ T_w.
When the form (A*, 2, A) is primitive (gcd(A, A*, 2) = 1) its class corresponds to the ideal (A, 1 + √−tp) of norm A,
a divisor of (1 + √−tp), and χ(w) = (A/p) is the genus character at p. Caveat (R-O217): for imprimitive forms the
ideal is not invertible in ℤ[√−tp] (p = 5, w = (7,1,1): form [6, 2, 6], ideal (6, 1 + √−35)); the proper-class
language then needs the order of the primitive form. So the words of level t are the factorisations (1 + √−tp) = 𝔞𝔞′ with N𝔞 ≡ N𝔞′ ≡ −1 (mod t), and
Gauss's map z ↦ [z^⊥] (onto the three-squares genus, equidistributed among its classes, Disq. Arith. art. 291–292;
Venkov) carries the χ = +1 ones.

**Prop 3 (circularity, PROVED).** An independent evaluation of Σ_w r(T_w, I₃) (or of any r-weighted word count) would be a lattice-point count of {(x, y) ∈ ℤ³ × ℤ³ : x·y = 1, |x × y|² = tp, t | |x|² + 1, t | |y|² + 1, t ≥ 1},
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
* Σ_w r/48 vs N₊ (illustrates that r/48 is not an indicator): (5: 6 vs 5), (13: 10 vs 7), (17: 16 vs 11), (29: 16 vs 11), (53: 22 vs 13), (61: 16 vs 9).
* Per-word r/48 for p = 101: (tp mod 8, ω(tp), r) = (2,2,48)×2, (2,3,144)×2, (3,2,96)×3, (5,1,48)×4.

## Assessment
PROVED (Props 1–3, classical inputs) / CERTIFIED (small checks). Negative for goal (a): no exact Siegel–Weil
weighting of words beyond the tautological indicator exists in this form (α₂ and α_p vanish together on χ = −1);
nothing can be compared with |X_p| without B2 information.
