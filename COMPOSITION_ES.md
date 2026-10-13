# COMPOSITION_ES — composition as a generator of ES certificates on V_n (task O203, spark relay X)

Status: in progress (O203). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on MARKOFF_ES.md (O202; Thms 4.1–4.3, Prop 7.1 after R202 repair M2), GROWING_MUTE.md (Prop 1.1–1.2),
reviews/markoff-es-review.md (M2, `scripts/review_mk_compose.py`). Scripts `scripts/cp_*`.

Notation. n > 1 odd; μ > √n an integer with f := μ² − n not a square; K = ℚ(√f), O := ℤ[√f], **O' := ℤ[2√f]**
(discriminant 16f); η := μ + √f, η̄ := μ − √f, so η + η̄ = 2μ, ηη̄ = n, η̄² = 2μη̄ − n, ℤ[η̄] = O, ℤ[2η̄] = O'.
V_n : nA² + B² + D = 2μAB, D | μ, A even, B odd, gcd(A, B) = gcd(B, n) = 1, A, B, D > 0 ("a V_n point at μ").
ES ⟺ some V_n point has B = 1 (GROWING_MUTE Prop 1.1(c)).

## 0. Iteration log

(X1) Composition law written out (§1): it is ideal multiplication in O'; V_n values at μ are the fibre over a
fixed order-2 narrow class δ of the "box" of primitive ideals of norm dividing μ (§2). Composition is closed
only for an odd number of factors (sign) and only inside one μ.
(X2) First kill: the B = 1 slot at μ is a SINGLE explicit element ε_μ = 1 − 2jη̄ that exists in O' for every μ;
ES at μ is the scalar divisibility N(ε_μ) | μ (Thm 1.3). No operation inside O_μ can change that. Hypotheses of
this kill: (i) one order O_μ; (ii) target exactly B = 1. Modifications tried: §3 (pigeonhole in Cl⁺, violating
"bounded data"), §5 (across μ, violating (i)), §6 (weaker target B ≡ 1, violating (ii)).

## 1. The exact composition law

**Lemma 1.1 (V_n points = negative-norm elements of O'; PROVED).** Fix μ. The map (A, B, D) ↦ α := B − Aη̄
= (B − μA) + A√f is a bijection from V_n points at μ onto the set of α = x + y√f ∈ O' with gcd(x, y) = 1,
N(α) = −D, D | μ, gcd(D, n) = 1, y > 0, x + μy > 0. Every primitive α ∈ O' of norm −D (D | μ, gcd(D, n) = 1)
gives exactly two V_n points, from the four elements ±α, ±ᾱ: y > 0 forces B > 0, and α ↔ −ᾱ is the involution
ι_B : B ↦ 2μA − B.
*Proof.* N(B − Aη̄) = B² − 2μAB + nA², so the V_n equation is N(α) = −D. A even ⟺ y even ⟺ α ∈ O' (x then odd as
N(α) is odd). gcd(A, B) = gcd(y, x + μy) = gcd(x, y). gcd(B, n) = 1 is automatic (MARKOFF_ES Thm 4.1). For y > 0:
(x + μy)(μy − x) = μ²y² − x² = ny² + D > 0 and the two factors sum to 2μy > 0, so both are positive; −ᾱ = −x + y√f
has B' = μy − x = 2μA − B. ∎

**Proposition 1.2 (composition law; PROVED).** For V_n points (A_i, B_i, D_i) at the same μ, with α_i = B_i − A_iη̄:
(a) α₁α₂ = B₃ − A₃η̄ with **A₃ = A₁B₂ + A₂B₁ − 2μA₁A₂, B₃ = B₁B₂ − nA₁A₂**, N = +D₁D₂; replacing α₂ by its ι_B
partner −ᾱ₂ replaces (A₂, B₂) by (A₂, B₂') = (A₂, 2μA₂ − B₂) (and ᾱ₂ itself is (−A₂, B₂ − 2μA₂)).
(b) A product of r V_n points (each possibly conjugated) is ± a V_n point (after the normalisation of Lemma 1.1)
**iff r is odd, the product is primitive, and D₁⋯D_r | μ**. Primitivity holds iff for every prime ℓ dividing two
or more of the D_i, all those factors lie in the SAME prime of O above ℓ (choose conjugations accordingly).
(c) Products of an even number of points have norm +D₁⋯D_r ≡ 1 (mod 4) and are never V_n points; more generally
every primitive x + y√f ∈ O' has norm ≡ 1 (mod 4), so **sign(N α) = χ₋₄(|N α|)** (χ₋₄ the character mod 4). In
particular O' has no unit of norm −1, and multiplying by elements of O ∖ O' never returns to O' ∖ 2O.
*Proof.* (a) Expand with η̄² = 2μη̄ − n. ᾱ₂ = B₂ − A₂η = (B₂ − 2μA₂) + A₂η̄. (b) Norm multiplicativity gives
(−1)^r ∏D_i; Lemma 1.1 needs the sign −, primitivity and the divisibility. Every ℓ | D_i is odd, prime to n and
has (−n/ℓ) = 1 (f ≡ −n mod ℓ as ℓ | μ), so ℓ ∤ 2f splits in O as 𝔩𝔩̄; a primitive element lies in at most one of
𝔩, 𝔩̄; the product is divisible by ℓ iff it lies in 𝔩𝔩̄, i.e. iff two factors use different primes. (c) x odd
(as α ∉ 2O and y even), so x² − f y² ≡ 1 (mod 4); a product of an element of O ∖ O' (y odd) with one of O' ∖ 2O
(x odd) has odd √f-coefficient. ∎

**Theorem 1.3 (the ES slot is one explicit element; PROVED, elementary).** Let μ > n and write μ = nj + t with
j ≥ 1, 1 ≤ t ≤ n. Put **ε_μ := 1 − 2jη̄ ∈ O'**, N(ε_μ) = −(4tj − 1). Then the only possible V_n point with B = 1
at μ is (A, B) = (2j, 1), D = 4tj − 1, i.e. α = ε_μ, and it is a V_n point iff (4tj − 1) | μ
(⟺ (4tj − 1) | n + 4t²). For μ ≤ n there is no B = 1 point.
*Proof.* B = 1 gives D = 2μA − nA² − 1. D > 0 forces μ > (nA² + 1)/(2A) > nA/2, and D | μ forces D ≤ μ, i.e.
μ ≤ (nA² + 1)/(2A − 1). For A = 2j: nj < μ ≤ nj + (nj + 1)/(4j − 1) ≤ nj + n (as n + 1 ≤ 3nj). So j = (μ − t)/n
is determined by μ, and D = 4j(μ − nj) − 1 = 4tj − 1. Finally 4t(t + nj) ≡ 4t² + n (mod 4tj − 1) and
gcd(4t, 4tj − 1) = 1. ∎
(This re-proves, without continued fractions, MARKOFF_ES Thm 4.3 + R202 repair M1: B = 1 forces A = 2⌊(μ−1)/n⌋.)

**Corollary 1.4 (composition is not a generator of ES; PROVED).** For every μ, the existence of an ES point at
μ is the scalar condition N(ε_μ) | μ on the element ε_μ, which exists in O'_μ for every μ > n regardless of any
other point. Hence:
(a) if 4tj − 1 ∤ μ, no element of O'_μ obtained by any operation (products, units, conjugation, quotients) from
V_n points at μ has B = 1 — however many V_n points exist at μ (they typically do: MARKOFF_ES §6);
(b) if 4tj − 1 | μ, the ES point already exists, and it is "obtained by composition" from V_n points at μ in the
trivial sense ε_μ = ε^k·(ε^{−k}ε_μ) (ε the fundamental unit of O'; the factor ε^{−k}ε_μ is a B > 1 point of the
same Pell orbit), and nontrivially iff the ideal (ε_μ) ⊂ O' has a proper divisor that is principal in O'.
So the census question of the brief has the exact answer: **a deterministic recipe "any V_p point ↦ (compose)
↦ B = 1" is impossible at every μ with 4tj − 1 ∤ μ, and superfluous at every other μ.** Composition can only
re-express an existing ES certificate (as in R202's n = 59, μ = 126 instance), never create one.
*Proof.* Thm 1.3 and Prop 1.2. ∎
