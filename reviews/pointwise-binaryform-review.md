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
| Corollary 3.4 | SOUND-AFTER-REPAIRS (D3, D4 minor) |
| Prop 5.1 | SOUND (D5 minor wording) |
| Prop 5.2 (+ O145 Prop 3.2 dependency) | SOUND |
| §6 search | SOUND as EVIDENCE (independent e-slice: 0 genuine families) |
| Headline scope (§0, §3 end, §7) | GAP (D6 MAJOR: (x,y,z)-families not covered) |

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

### Corollary 3.4 — SOUND-AFTER-REPAIRS (D3, D4, MINOR)

Re-derived. #certified p ≤ X is at most the number of valid prime points P with Q(P) ≤ X. By
Lemma 3.3 the non-polynomial families contribute ≪ X^{1/2+ε} such points (radius ≍ X^{1/2}); by
Thm 3.2(c) (with D2) the polynomial ones lie, beyond R(F, δ), in ≤ |Z_F| cones of width 2δ. The
number of represented primes p ≡ r (M), p ≤ X, is ≫ X/log X, and each has ≤ 2w(D) ≤ 12
representations (r_D(p) = w(1 + (D/p)) summed over classes), so the comparison is legitimate. What
is needed from Hecke is: *for an imaginary quadratic order O of discriminant D, a fixed proper ideal
class (= the form Q), a fixed class mod M and a cone S in the (u,v)-plane, the prime points P ∈ C ∩ S
with Q(P) ≤ X number (μ(S)/2π + o(1))·(#prime points of C with Q(P) ≤ X)*, where μ is the
angle measure transported by the linear map (u,v) ↦ uω₁ + vω₂ (so a δ-cone in the (u,v)-plane has
μ ≤ C_Q δ). This is a true classical theorem (Hecke 1918/1920, Grössencharacters of K with
modulus f·M and infinity type (α/|α|)^k; e.g. Hecke, Math. Z. 1 (1918) 357–376 and 6 (1920) 11–51;
Narkiewicz, *Elementary and Analytic Theory of Algebraic Numbers*, Ch. 7). I could not access these
texts in sources/; the statement used is standard and the application is correct. "Unconditional"
is justified (Hecke is a theorem, no GRH needed for a density-zero statement).

The Mordell-hard part: 1, 121, 169, 289, 361, 529 are 1², 11², 13², 17², 19², 23² mod 840 and all ≡ 1
(8); a prime ≡ r₀ (840) is a unit square mod M iff it is a QR mod each odd ℓ | M, ℓ ∤ 840 (the 2-, 3-,
5-, 7-parts are automatic: ≡ 1 (8) is a square mod 2^k, a unit QR mod ℓ is a QR mod ℓ^k). Dirichlet
gives relative density ∏ 1/2. Correct, including "infinitely many, indeed a positive proportion of
Mordell-hard primes are missed" — for each fixed 𝔉, with the proportion depending on 𝔉 through M.

* **D3 (MINOR, citation):** "Hecke's theorem" is cited with no reference and only in the
  Gaussian form; give a precise reference and state the version used (order of discriminant D,
  ray class mod M, cones transported by (u,v) ↦ uω₁ + vω₂). For non-maximal orders say that primes
  dividing the conductor are excluded (they divide 2D | M anyway).
* **D4 (MINOR, overstatement in prose):** the paragraph after Cor 3.4 says no certificate covers "a
  positive proportion of the primes in any square class" and §0 says "on every coset C mod M (8D | M)".
  Both are correct only for square classes *modulo the joint modulus M ⊇ K_F*; a finite 𝔉 *can*
  cover a positive proportion of a Mordell-hard class mod 840 (one-variable identities on non-square
  subclasses, as §4.4 itself says). Add "mod M, where M is divisible by the families' moduli" in §0,
  §3 closing paragraph and the §7 bullet. Also §0's "8D | M" differs from the theorem's "8, 2D | M"
  (harmless: 8D | M implies both; make them agree).
* Not a defect but worth stating: the theorem is per fixed form Q; finitely many forms Q₁,…,Q_k
  (each with its own finite 𝔉ᵢ) are handled by taking M = lcm of all moduli — union of density-zero
  sets. §4.2 says this only for one-parameter families.

### Prop 5.1 (constant level ⇒ one-variable) — SOUND (wording D5, MINOR)

Re-derived. For any nonzero r, Q − r is irreducible over C (Q nondegenerate ⇒ the ternary form
Q − r t² is nondegenerate). Hence for g ∈ Q[n] with g(0) ≠ 0, every divisor of g(Q) in Q[u,v] is,
up to a constant, a product of Galois-stable sets of factors Q − rᵢ, i.e. lies in Q[n]. Apply to
g = n² + 4c²d (Type I) and g = 4c²dn + 1 (Type II): f ∈ Q[n], then a, b, e (and in Type II a is
constant) are in Q[n]. Correct.
**D5 (MINOR):** the proof says "neither factor Q ± 2ic√d is defined over Q, so Q² + 4c²d is
irreducible". That is true for d > 0 but false for d = −m² (Q² − 4c²m² = (Q − 2cm)(Q + 2cm)), and
the proposition is stated for "every family" (d < 0 families are never valid but are families). The
conclusion still holds with the argument above (every divisor of g(Q) lies in Q[n]); replace the
irreducibility claim by that, or add "d > 0 (forced by validity)".

### Prop 5.2 (Type II on a cone ⇒ one-variable) and its dependency O145 Prop 3.2 — SOUND

*O145 Prop 3.2 (BRAINSTORM/ident_form_families.md §3), checked by me line by line.* With
S = deg d + deg g + deg g′, G = max(deg g, deg g′): g + g′ = ch has no cancellation (positive leading
coefficients), so G = deg c + m. In P = 4dgg′ − h cancellation *can* occur (both terms have positive
leading coefficient) — the brainstorm's phrase "there is no cancellation" is inaccurate there — but
the stated consequence S = max(2, m) is still right: S < m would give P a negative leading
coefficient, S > m forces S = 2, and S = m forces m ≥ 2. Case m ≥ 2: S = m ≤ G ≤ S forces c, d and
one of g, g′ constant, and h(4dcg′ − 1) = P + 4dg′² puts everything in Q[P] (4dcg′ − 1 ≠ 0 since
P > 0). Cases m ≤ 1, S = 2: (2,0,0) trivial; (0,2,0) m = 0 trivial, m = 1 impossible (h's real root
is a root of P + 4dg′² > 0); (1,1,0) and (0,1,1) impossible by the sign arguments as written (I
re-did both). The g ↔ g′ symmetric cases are identical. So O145 Prop 3.2 is correct (PROVED).

*Prop 5.2 itself.* For rational θ ∈ A_F and rational P₀ off the line Rθ, F∘ℓ ∈ Q[t]⁶ with leading
coefficients H_j(θ) > 0, and Q∘ℓ is a positive definite quadratic, so Prop 3.2 applies (it only uses
(2.13), (2.14)). G∘ℓ ∈ Q[Q∘ℓ] is symmetric about the vertex t* = −B(P₀,θ)/Q(θ), and the reflection
t* + s ↦ t* − s on ℓ is x ↦ x − 2B(x,θ)θ/Q(θ) = σ_θ(x) (check: B(x,θ) = Q(θ)(t − t*)). The union of
such lines is Zariski dense, so G∘σ_θ = G. Rational θ are dense in the arc, so the group generated
contains Q-rotations by a dense set of angles; by continuity G is SO_Q(R)-invariant (−I included,
so G restricted to a ray is even), hence G ∈ R[Q] ∩ Q[u,v] = Q[Q]. Correct. The same A_F⁻ remark
as D2 applies (a family valid on a cone with sign pattern (−,−,−,+,+,+): apply the result to the
dilate). Prop 5.2 does not use integrality or the principal genus; it is purely algebraic.

### Scope of the headline (§0, §3 closing paragraph, §7) — GAP in the stated scope (D6, MAJOR)

§0 frames the question as certificates "ES solution = polynomial in (u,v)" and then states in bold
"the square specialisation kills **every such certificate** on every square class". The theorems,
however, are proved only for families whose **ET coordinates (a,…,f)** are polynomial/rational in
(u,v). A family given as (x,y,z) ∈ Q[u,v]³ (the literal "ES solution polynomial in (u,v)") is
exactly case §4.4(iv), which the author correctly lists as *not done*. The gap is real, not
cosmetic: at a square point n = m² the specialised (x,y,z) is a genuine positive solution of 4/m²
(such solutions exist whenever ES holds for m), so Lemma 1.1 says nothing unless that solution is
of ET Type I/II shape *with the polynomial ET coordinates specialising to it*; ET's one-variable
reduction from (x,y,z)-polynomials to (a,…,f)-polynomials (ET §10, proof of Prop 1.9: "d(p) =
q(p)·d̃(p) with q(p) taking finitely many values", then passing to subclasses) uses that gcds of
values of coprime one-variable polynomials are bounded, which fails in two variables (gcd(u, v)
is unbounded), and also uses p prime to fix the Type. So for the natural certificate shape the
result is not proved.
Repair (required): in §0 replace "every such certificate" by "every certificate whose ET
coordinates (a,…,f) are polynomial or rational in (u,v)"; same qualifier in the paragraph after
Cor 3.4 ("no Fermat + identity certificate …") and in the §7 Cor 3.4 bullet; and move §4.4(iv) up
into §0 as the main open case. (The statement "a polynomial or rational ET identity" in the §3
closing paragraph is fine if "ET identity" is defined there as an (a,…,f)-family.)

### §6 search — SOUND as EVIDENCE (independent re-run agrees)

I did not reuse `bf_search_typeI.py`. `scripts/review_bf_search_e.py` slices by **e** instead of
(c, d): for e = κ·e₀ it factors n e + 1 = 4abd over Q, distributes the irreducible factors among
a, b, d in all ways (dilation (2.10) fixes a's scalar; b's scalar β is solved from e | a + βb by
division modulo the principal ideal (e₀)), sets c = (a+b)/e, f = 4acd − n, checks (2.1), (2.2),
(2.6)–(2.9) symbolically, discards families with a zero coordinate, keeps those that are
*sign-feasible* (abd, acd, bcd > 0 somewhere on a grid in [−25, 25]²), and tests membership in
Q[n]⁶ by a method different from O159's (g ∈ Q[u²+v²] ⇔ g(t,0) even and g = h(u²+v²) with
h(s) = g(√s, 0)).
* Positive control: on u² + 21 with e = (u²+22)/22 it rediscovers the O145 k = 21 family
  (a, b) = (u² ∓ u + 22, u² ± u + 22), c = 44, d = 1/88, f = u² ∓ 2u + 23 (a dilate of O145's).
* Q = u² + v², e₀ = (quadratic form, coefficients in {−1,0,1}) + (linear form, coefficients in
  {−1,0,1}) + ζ, ζ ∈ [−8, 8], κ ∈ {1, 1/2, …, 1/12, 2, 3}: 57 596 (e₀, κ) pairs, 57 914 formal
  Σ-families (almost all with b, d negative constants — never valid), **50 sign-feasible families,
  all in Q[n]⁶, 0 genuinely two-variable** (`data/review_bf/search_e_{neg,pos}.txt`, plus the ζ = 0
  run quoted in the commit log: 3 388 pairs, 0 sign-feasible). The 50 one-variable hits are an
  internal positive control for the Q[n] test.
This is complementary to O159's (c, d)-slice and agrees with it. Caveat (MINOR, D7): O159's text
should say explicitly that its box only contains *formal* identities and that a family integral
only on a coset with non-polynomial a, b, e is outside the search (it does say so); my e-slice has
the same limitation.

### Novelty / literature

* ET (sources/elsholtz-tao-1107.1010.pdf, read): p. 7 and §10 — one-variable polynomial
  solvability, perfect-square classes unsolvable "(this also follows from Proposition 1.6)"; p. 6
  remark that any method "must necessarily fail when p is replaced by an odd square". O159's
  Thm 3.2 is exactly this principle transported to a binary-form parameter, with the conic
  Q = w² supplying the squares. Assessment: folklore-level, as the author says; the proof is short
  and correct.
* Schinzel, "On sums of three unit fractions with polynomial denominators", Funct. Approx. 28
  (2000) 187–194: **not accessible** (Project Euclid paywall); I could only confirm the bibliographic
  data. From ET's and the campaign's secondary descriptions (Schuh arXiv:2404.01307 p. 2 via
  BRAINSTORM/ident_form_families §2) it concerns one-variable linear parameters only. Mordell's
  *Diophantine Equations*: not accessible here.
* Elsholtz–Planitzer (sources/lit2026/arxiv-1805.02945, grepped): parametric families for counting,
  no two-variable identity obstruction.
* Ghermoul, arXiv:2508.07383 (abstract read): 3-variable polynomial families n = 4pᵢ(x,y,z)+1 with
  explicit solutions; consistent with §4.1 (such n are never odd squares at valid points) and not
  overlapping the binary-form result.
* Web searches for two-variable / sum-of-two-squares ES identity obstructions found nothing
  specific. Novelty status: **unverified, probably folklore**; the label in §7 is appropriate.

## Numbered defects

1. **D6 (MAJOR, overclaimed scope).** §0 bold answer, paragraph after Cor 3.4, §7 Cor 3.4 bullet:
   "every such certificate" / "no Fermat + identity certificate" read as covering families given by
   (x,y,z) ∈ Q[u,v]³, which §4.4(iv) itself says are not covered; ET's one-variable reduction
   (x,y,z) → (a,…,f) (ET §10) needs bounded value-gcds and a prime n, both unavailable here.
   Repair: qualify every headline by "whose ET coordinates (a,…,f) are polynomial or rational in
   (u,v)" and flag (iv) as the main open case. Possible route to close it (unverified): if Q | x and
   Q ∤ yz in Q[u,v], it suffices to find, in each C ∩ S, square points with gcd(Q(P), y(P)z(P)) = 1
   (then the specialised solution is Type I for m² and ET Prop 2.2 + Lemma 1.1 apply); on the
   parametrised conic this is a coprimality sieve between w(s,t) and y∘φ(s,t), which works when
   their resultant is nonzero and fails only if y vanishes at the isotropic points of Q.
2. **D2 (MINOR).** Thm 3.2(c) deduction ignores the sign pattern (−,−,−,+,+,+) allowed by §1
   (A_F⁻). Repair: apply (b) to the dilate (−a,−b,−c,d,e,f) as well (same in Prop 5.2).
3. **D3 (MINOR).** Cor 3.4: give a precise Hecke reference and the exact version used (order of
   discriminant D, ray class mod M, cones transported by (u,v) ↦ uω₁ + vω₂).
4. **D4 (MINOR).** §0/§3/§7: "every square class" must read "every square class mod M, M divisible
   by 8, 2D and the families' moduli"; §0's "8D | M" vs the theorem's "8, 2D | M".
5. **D5 (MINOR).** Prop 5.1 proof: "neither factor is defined over Q" is false for d = −m²;
   replace by "every divisor in Q[u,v] of g(Q), g ∈ Q[n], g(0) ≠ 0, lies in Q[n] (each Q − r is
   C-irreducible)" or restrict to d > 0.
6. **D1 (MINOR, framing).** Lemma 1.1 is not a strengthening of ET Prop 1.6 "without coprimality":
   ET's Σ_n has no coprimality condition and ET §4 already argues for arbitrary N-points. The real
   additions are the Jacobi refinements and even squares in Type II.
7. **D8 (MINOR, dependency).** O145 Prop 3.2's proof says "there is no cancellation"; in
   P = 4dgg′ − h cancellation can occur; the stated degree consequence is nevertheless right (see
   above). Fix the sentence in BRAINSTORM/ident_form_families.md and upgrade the Prop 5.2 label
   to "PROVED (dependency checked by R159)".

## Overall verdict

The mathematical core is **correct**: Lemma 1.1, Lemmas 2.1/2.2, Lemma 3.1, Lemma 3.3, Theorem 3.2
(with the one-line D2 fix), Cor 3.4 (relative to the classical Hecke theorem, so unconditional),
Props 5.1/5.2 and the O145 dependency all survive line-by-line re-derivation and from-scratch
brute force. No FATAL defects. One MAJOR defect (D6): the headline claims more than is proved —
the theorems cover ET-coordinate families, not arbitrary (x,y,z)-polynomial families. Novelty:
folklore-level two-variable Mordell–Schinzel analogue; Schinzel 2000 and Mordell's book not
accessible to me.

## Repairs applied (author quiet)

The author's branch had no commits after its final report (`91febab9`), so per the brief I applied
D1–D6 directly to POINTWISE_BINARYFORM.md, each marked "(R159 repair)": §0 headline qualifier and
modulus; Lemma 1.1 framing; Thm 3.2(c) dilate F⁻; Cor 3.4 Hecke reference; paragraph after
Cor 3.4 qualifiers; Prop 5.1 d > 0 / divisor argument; Prop 5.2 and §7 labels (dependency checked);
§7 Cor 3.4 qualifier. D8 (the "no cancellation" sentence in BRAINSTORM/ident_form_families.md, an
O145 file) was not edited. No mathematical content was changed; D6 remains an open problem
(§4.4(iv)), not something I closed.
