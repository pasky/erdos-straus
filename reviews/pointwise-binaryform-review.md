# R159 — hostile review of POINTWISE_BINARYFORM.md (O159, branch side-agent/binaryform-identities)

Reviewer: R159. Reviewed commit: merge of `side-agent/binaryform-identities` into
`side-agent/review-binaryform`. From-scratch scripts: `scripts/review_bf_*.py`.
ES is not solved; nothing below changes that.

## Verdict table (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Lemma 1.1 | SOUND (MINOR framing defect D1) |
| Lemma 2.1 | SOUND |
| Lemma 2.2 | SOUND |
| Lemma 3.1 | SOUND |
| Theorem 3.2 | SOUND-AFTER-REPAIRS (D2 minor) |
| Lemma 3.3 | SOUND |

## Claim-by-claim

### Lemma 1.1 (square vanishing for N-points)

Re-derived. ψ(k) = (−d/k) is a real character mod 4d, odd (ψ(4d−k) = −ψ(k)). Type I: (2.7)
`ef = 4a²d+1` ⇒ f odd, coprime to 2ad, −d ≡ (2a)^{−2} mod f ⇒ ψ(f) = 1; (2.1) ⇒ gcd(n,d)=1; (2.6)
f ≡ −n mod 4d ⇒ (−d/n) = −1 for n odd. Type II: (2.18) f ≡ −1 mod 4d ⇒ ψ(f) = −1; (2.21) ⇒
(−dn/f) = 1 ⇒ (n/f) = −1, which is impossible for any square n coprime to f (and n is, by
(2.21)). Sign reduction (§1): abd, acd, bcd > 0 ⇒ d > 0 and a, b, c of one sign; e = (a+b)/c > 0;
f > 0 from f = (4a²d+1)/e (I) resp. f = 4acd − 1 (II). Correct.

From scratch: `scripts/review_bf_lemma11.py` enumerates all N-points with a,b,c,d < 40
(38 827 Type I, 250 770 Type II; no gcd restriction) and verifies the ET equations, `(−d/n) = −1`
(Type I, odd n > 1), `(n/f) = −1` (Type II), no square n (Type II, either parity) and no odd square
(Type I, including n = 1); plus the periodicity/oddness of ψ for d < 200. 0 violations.

Framing (D1, MINOR): ET define Σ^I_n, Σ^II_n as *all* nonzero sextuples satisfying (2.1)–(2.9)
resp. (2.13)–(2.21) (ET p. 11), with no gcd(c, n) condition, and ET §4's proof of Prop 1.6 uses only
(2.1), (2.2) and n ≡ 1 (8) for an arbitrary N-point of Σ^I_n. So "ET Prop 1.6 without coprimality"
is not a strengthening; ET §4 already is the N-point statement. The genuinely extra bits are the
Jacobi-symbol refinements `(−d/n) = −1`, `(n/f) = −1` and the Type II case for even squares.

### Lemma 2.1 (odd squares dense in square-class cosets and sectors) — SOUND

Re-derived. X: Q(u,v) = w² is a smooth conic (disc of ternary form ≠ 0). X(Q) ≠ ∅: if 2D | M, every
ℓ ∤ M is a good prime and gets a point (Chevalley–Warning + Hensel), ℓ | M gets
(u₀ : v₀ : √Q(u₀,v₀)) since Q(u₀,v₀) is an ℓ-adic unit square (ℓ = 2 uses 8 | M: unit square mod 8
⇒ ≡ 1 (8) ⇒ square in Z₂), ∞ is fine (Q definite); Hasse–Minkowski. If instead Q is in the
principal genus, Q is Q-equivalent to the principal form, which represents 1, so X(Q) ≠ ∅ directly.
Then X ≅ P¹ and weak approximation on P¹ holds at any finite set of places. The scaling step is
right: a primitive (u₁,v₁,w₁) that is ℓ-adically close to a primitive representative of P_ℓ is ≡
μ_ℓ·(u₀,v₀,w_ℓ) mod ℓ^{k_ℓ}, the sign flip at ∞ multiplies every μ_ℓ by −1 consistently, and
λ ≡ μ^{−1} (M), λ > 0 large, puts λ(u₁,v₁) in C ∩ S with Q = (λw₁)², λw₁ odd because Q(C) is odd.
No hidden parameter dependence.

Checked from scratch (`scripts/review_bf_lemma21.py`, `review_bf_lemma21b.py`): for
Q ∈ {u²+v², u²+uv+v², u²+2v², u²+5v²} and M ∈ {8, 24, 40, 16, 40} every pair (square class mod M,
octant) contains a point with Q = odd square (the first pass with a box of side 3000 missed 56 resp.
96 pairs for M = 40; a targeted box of side 80 000 per class finds all of them — box effect, not a
counterexample). The non-principal form 2u²+2uv+3v² (D = −20) has no square class mod 40 at all,
consistent with Remark (1). M = 4 for u²+v²: 32 of 64 (class, octant) pairs have no square point,
e.g. class (1,2) mod 4 (even leg of a Pythagorean triple is ≡ 0 mod 4) — Remark (2) is right.

### Lemma 2.2 (Gaussian "class of one") — SOUND

Re-derived: CRT splits G_M into local pieces modulo the diagonal i; for odd ℓ the local quotient is
detected by Q mod ℓ (split: xy; inert: F_ℓ* ⊂ squares of F_{ℓ²}*, norm of a generator is a
non-square) and i dies because N(i) = 1 is trivial there; at 2 (k ≥ 3), Z₂[i]*/□ ≅ (Z/2)³, ⟨5, i⟩
has order 4 (5 ∉ ±Q₂*²; ζ₈ ∉ Q₂(i)), quotient Z/2 detected by Q mod 8. My independent brute force
(`review_bf_lemma21.py`, group H = (Z/M)*·⟨i⟩·squares computed directly) gives 0 mismatches for
M ∈ {8, 16, 32, 48, 72, 80, 104} and mismatches exactly when 8 ∤ M (M = 4: 4/8, M = 12: 16/64,
M = 20: 32/128). So "8 | M is needed" is correct and necessary, and the reason is the 2-adic
component: mod 4 the norm condition Q ≡ 1 (4) is automatic but does not see the class of 5·(unit)
versus i in Z₂[i]*/□. Minor wording point only (proof says "i dies" for odd ℓ, and at ℓ = 2 it is
i that is quotiented out — the text is correct but terse).

### Lemma 3.1 (signs at infinity) — SOUND

Each H_j is a nonzero form, so H_j(cos θ, sin θ) has finitely many zeros; off a δ-neighbourhood
|H_j| ≥ c_δ|P|^{deg} dominates the O(|P|^{deg−1}) tail. Constant coordinates are covered (H_j
constant ≠ 0). R_δ depends on δ and F only — this is used correctly in Thm 3.2(c) (the bounded
exceptional set depends on δ, which is harmless).

### Theorem 3.2 — SOUND-AFTER-REPAIRS (D2, MINOR)

(a) Valid ⇒ (after the λ = −1 dilation) an N-point of Σ_{Q(P)}; Lemma 1.1. Correct.
(b) Integrality is a function of P mod K_F (δ·g ∈ Z[u,v] ⇒ g(P) ∈ Z ⇔ δg(P) ≡ 0 mod δ), so
integral at one point of C ⇒ integral on C. Lemma 3.1 on a closed subarc of A_F + Lemma 2.1 (with
2D | M) gives a valid point with Q(P) an odd square, contradicting (a). Correct.
(c) **D2 (MINOR, logical gap in the deduction):** §1 defines validity up to the dilation
(a,b,c) ↦ −(a,b,c), i.e. F(P) ∈ ±N³ × N³, but A_F only records the pattern (+,+,+,+,+,+). A point far
out with arg P ∈ A_F⁻ := {H_a, H_b, H_c < 0 < H_d, H_e, H_f} is also valid, and (b) as stated says
nothing about A_F⁻. Repair: apply (b) also to the dilate F⁻ = (−a,−b,−c,d,e,f), which is a
polynomial family with the same K_F (ET (2.10) with λ = −1); then A_F ∪ A_F⁻ = ∅ and (c) follows.
One line; the theorem is true.

Quantifiers, made explicit (what "valid only near finitely many directions" means): for each fixed F,
each square class C mod M (8, 2D, K_F | M) and each δ > 0 there is R(F, δ) such that every valid
P ∈ C with |P| > R lies within angle δ of Z_F (|Z_F| ≤ 2·Σ_j deg H_j). Nothing is claimed about
how many valid points lie in those thin regions (they can be infinite, e.g. parabolic regions around
a zero direction of some H_j); only that their angular density is 0. That is exactly what Cor 3.4
needs.

### Lemma 3.3 (rational coordinates) — SOUND; exponent right and sufficient

Re-derived: B = B₁B₂ in Z[u,v] (Gauss), so B₁(P) | B(P) | A(P); R(u) = Res_v(A, B₁) ∈ (A, B₁)∩Z[u]
is ≢ 0 because A, B₁ are coprime and deg_v B₁ > 0 (if deg_v A = 0, R = A^{deg_v B₁}); B₁(P) | R(u);
for the O(X) non-exceptional u there are ≤ 2τ(κR(u)) ≪ X^ε admissible values of B₁(u,·), each hit by
≤ deg_v B₁ values of v; the finitely many u with R(u) = 0 or B₁(u,·) constant give O(X) each. So
≪ X^{1+ε}. This is essentially sharp (linear B gives ≫ X log X): `scripts/review_bf_lemma33.py`
counts 28 284 integral points of (u²+v²+1)/(u+2v) in [−2000, 2000]², growth ≈ X log X, and bounded
counts for a definite denominator. Since prime points of a class number ≍ X²/log X in the disc of
radius X, X^{1+ε} = o(X²/log X) — enough. (Note the comparison is points-in-disc vs points-in-disc,
not primes ≤ X vs points; the author's "≍ X²/log X" is the right normalisation.)

