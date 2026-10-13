# COMPOSITION_ES — composition as a generator of ES certificates on V_n (task O203, spark relay X)

Status: in progress (O203). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on MARKOFF_ES.md (O202; Thms 4.1–4.3, Prop 7.1 after R202 repair M2), GROWING_MUTE.md (Prop 1.1–1.2),
reviews/markoff-es-review.md (M2, `scripts/review_mk_compose.py`). Scripts `scripts/cp_*`.

Notation. n > 1 odd; μ > √n an integer with f := μ² − n not a square; K = ℚ(√f), O := ℤ[√f], **O' := ℤ[2√f]**
(discriminant 16f); η := μ + √f, η̄ := μ − √f, so η + η̄ = 2μ, ηη̄ = n, η̄² = 2μη̄ − n, ℤ[η̄] = O, ℤ[2η̄] = O'.
V_n : nA² + B² + D = 2μAB, D | μ, A even, B odd, gcd(A, B) = gcd(B, n) = 1, A, B, D > 0 ("a V_n point at μ").
"ES point" := V_n point with B = 1 = a solution of ES's d = 1 Type II shot family ("4k²n + 1 has a divisor
≡ −1 (mod 4k)", GROWING_MUTE Prop 1.1(c)). ES(n) itself can hold without any ES point (e.g. n = 13, 37, 97; exactly
99 primes < 10⁶, GROWING_MUTE R201); all of Type II is covered by the slices V_{nd} (Prop 4.1(b)).

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

**Corollary 1.4 (composition is not a generator of ES at a fixed μ; PROVED).** For every μ, the existence of an ES point at
μ is the scalar condition N(ε_μ) | μ on the element ε_μ, which exists in O'_μ for every μ > n regardless of any
other point. Hence:
(a) if 4tj − 1 ∤ μ, no element of O'_μ obtained by any operation (products, units, conjugation, quotients) from
V_n points at μ has B = 1 — however many V_n points exist at μ (they typically do: MARKOFF_ES §6);
(b) if 4tj − 1 | μ, the ES point already exists, and it is "obtained by composition" from V_n points at μ in the
trivial sense ε_μ = ε^k·(ε^{−k}ε_μ) (ε the fundamental unit of O'; the factor ε^{−k}ε_μ is a B > 1 point of the
same Pell orbit). Nontrivially (r ≥ 3 V_n points, each of norm ≤ −3) iff there is a chain of principal divisors
𝔡₁ | 𝔡₂ | (ε_μ), 1 < N𝔡₁ < N𝔡₂ < D = 4tj − 1, with negative-norm generator of 𝔡₁ and positive-norm generator of
𝔡₂ (then 𝔡₁, 𝔡₂𝔡₁⁻¹, (ε_μ)𝔡₂⁻¹ all have negative-norm generators; longer chains likewise). A single principal
proper divisor only gives ε_μ = u·α·β with one factor of POSITIVE norm, which is not a V_n point (R-O203 #3:
n = 29, μ = 60, D = 15 has principal divisors of norms 3 and 5 but no composition of V_n points).
So, at a FIXED μ, the census question of the brief has the exact answer: **a recipe "V_p points at μ ↦ (compose)
↦ B = 1" is impossible at every μ with 4tj − 1 ∤ μ, and superfluous at every other μ.** (R-O203 #1: this is a
fixed-μ statement. It does not exclude a mechanism that SELECTS a good μ or d, or proves that one exists — that is
exactly the divisor problem N(ε_μ) | μ, see Prop 4.1(c).)
*Proof.* Thm 1.3 and Prop 1.2. ∎

## 2. Class-group dictionary at fixed μ

Let S(μ) be the set of primes ℓ | μ with ℓ ∤ 2n and (−n/ℓ) = 1 (these split in O' as 𝔩𝔩̄, since f ≡ −n mod ℓ).
The **box** 𝔅(μ) is the set of primitive ideals 𝔡 ⊂ O' with N𝔡 | μ and N𝔡 supported on S(μ) (equivalently
𝔡 = ∏ 𝔩_i^{e_i} with one prime chosen above each ℓ_i and e_i ≤ v_{ℓ_i}(μ)); |𝔅(μ)| = ∏_{ℓ∈S(μ)} (2v_ℓ(μ) + 1).
Let Cl⁺(O') be the narrow class group and **δ ∈ Cl⁺(O')** the class of principal ideals having a generator of
negative norm. By Prop 1.2(c) O' has no unit of norm −1, so δ ≠ 1, δ² = 1, and δ ↦ 1 in the wide group Cl(O').
χ₋₄ : 𝔞 ↦ (−4/N𝔞) is a character of Cl⁺(O') (on ideals prime to 2) with χ₋₄(δ) = −1 (Prop 1.2(c)).

**Proposition 2.1 (V_n values are the δ-fibre of the box; PROVED).** (a) D is the D-value of a V_n point at μ iff
some 𝔡 ∈ 𝔅(μ) with N𝔡 = D has [𝔡]⁺ = δ. The V_n points with α ∈ 𝔡 form, up to ι_B, one orbit of ε (fundamental
unit of O'), whose members have unbounded A.
(b) Composition (Prop 1.2) is ideal multiplication: [𝔡₁𝔡₂𝔡₃]⁺ = δ³ = δ, and the product is again in the box iff
the norms multiply inside μ AND the product is primitive (same prime above every shared ℓ; R-O203 #2: n = 53,
μ = 54, α = −107 + 2√2863, N α = −3: α·(−ᾱ)·α = 3α is not primitive although 27 | 54).
(c) (**ES is not a class condition.**) For μ > n, ε_μ = 1 − 2jη̄ generates the ideal 𝔢_μ := (4tj − 1, 2jη̄ − 1),
whose class is δ for EVERY μ. ES at μ ⟺ 𝔢_μ ∈ 𝔅(μ) ⟺ N𝔢_μ | μ: membership of one prescribed principal ideal in the
box. Among the ideals of the δ-fibre, 𝔢_μ is singled out by its generator (B = 1), not by any class datum.
(d) (**T1.**) If n = m² then every ℓ ∈ S(μ) has ℓ ≡ 1 (mod 4), so χ₋₄ ≡ 1 on 𝔅(μ) and the δ-fibre of the box is
empty for every μ: no V_n point at all (the class-group form of MARKOFF_ES Cor 3.2).
*Proof.* (a) Lemma 1.1: an element of O' of norm −D is a negative-norm generator of a primitive ideal of norm D
(primitive ⟺ gcd(x, y) = 1 since D is odd); the generator is unique up to units of O', all of norm +1.
A → ∞ along the orbit by MARKOFF_ES Prop 7.1(b)/GROWING_MUTE Prop 1.2(b). (b) Prop 1.2. (c) N(ε_μ) = −(4tj − 1) < 0
(Thm 1.3), ε_μ is primitive; Thm 1.3 for the equivalence. (d) (−m²/ℓ) = (−1/ℓ). ∎

**Remark 2.2 (where B = 1 sits in the principal cycle; μ > 2n).** (For n < μ ≤ 2n, j = 1, the ES element is
2η̄ − 1 itself, at depth 1: MARKOFF_ES R202 repair M1.) In the regular CF of √N, N = 4f, the principal
cycle of reduced ideals of O' begins 1, (2η̄ − 1), (2η̄), (2jη̄ − 1) = 𝔢_μ, … with norms 4μ − 1 − 4n, 4n, 4tj − 1
(MARKOFF_ES Thm 4.3: p₀ − q₀√N = 2η̄ − 1, p₁ − q₁√N = 2η̄, p₂ − q₂√N = 2jη̄ − 1 — the recursion
p₂ = a₂p₁ + p₀ reads 2jη̄ − 1 = (j − 1)·2η̄ + (2η̄ − 1)). So for μ > 2n ES at μ is "the third reduced principal
ideal has norm dividing μ". The second one is 2η̄, i.e. 2× the element of norm n that defines the family; ε_μ ≡ 1 (mod 2η̄O).

## 3. Pigeonhole in Cl⁺(O'_μ) (modification 1: unbounded box, MARKOFF_ES spark 4)

Idea: make |S(μ)| large (μ highly composite in split primes) so that pigeonhole in Cl⁺(O'_μ) forces a δ-product.
Barrier screen first: this can only ever give V_n points (ES^{[2]}), since by Prop 2.1(c) B = 1 is not a class
condition. Even for ES^{[2]} it fails as a forced mechanism:

**Proposition 3.1 (pigeonhole delivers the wrong sign; PROVED).** Let c₁, …, c_r ∈ G := Cl⁺(O') be the classes of
the chosen primes over S(μ) (each may be replaced by its inverse = conjugate). (a) Davenport: if r ≥ D(G) (the
Davenport constant) then some nonempty product ∏_{i∈I} 𝔩_i^{±1} is narrowly principal — but with a POSITIVE-norm
generator, i.e. not a V_n point. (b) A V_n point at μ using each prime of S(μ) at most once exists iff δ ∈ Σ^±(c₁, …, c_r)
(signed subset sums), which no lower bound on r forces: e.g. if G ⊇ ⟨δ⟩ × ⟨g⟩ ≅ (ℤ/2)² and every 3-mod-4 prime has
class δg and every 1-mod-4 prime has class 1, then Σ^± ⊂ {1, δg} for all r (R-self: with a
1-mod-4 class g the product δg·g = δ would be reachable). (c) The necessary condition
χ₋₄ = −1 forces an odd number of primes ≡ 3 (mod 4) in I (the genus layer of MARKOFF_ES §6); the remaining
condition is the class layer, the same Cohen–Lenstra-type input as MARKOFF_ES Prop 6.1(c).
*Proof.* (a) Davenport's definition; a narrowly principal ideal has a totally positive generator, norm > 0.
(b) Prop 2.1(a); the example is a group computation ((δg)^{±1} = δg, (δg)² = 1, so signed products are 1 or δg).
Whether the example occurs in some O'_μ is not claimed; the point is that no counting of S(μ) alone excludes it. ∎
*Reading.* Pigeonhole in class groups naturally manufactures elements of norm +D (D ≡ 1 mod 4) — these are the
"even products" that Prop 1.2(c) excludes. Reaching δ is a target-sum problem whose answer depends on the actual
classes, i.e. on h(O'_μ) and its structure. Even a full solution would give ES^{[2]}(n), not ES(n).

## 4. Scope: the B = 1 locus is a finite explicit set — any generator on V_n must solve the divisor problem

**Proposition 4.1 (PROVED, elementary).** (Here V_{n'} is allowed for EVEN n' = pd too: Lemma 1.1, Prop 1.2,
Thm 1.3 and GROWING_MUTE Prop 1.2(a) at B = 1 never use the parity of n; R-O203 #5, e.g. p = 13, (c, d, j) =
(1, 2, 1) gives the V₂₆ point (A, B, D, μ) = (2, 1, 15, 30).) (a) The ES points of V_n (all μ) are exactly
{(A, B, D, μ) = (2j, 1, D, nj + t) : 1 ≤ t ≤ n, D | n + 4t², D ≡ −1 (mod 4t), j = (D + 1)/(4t)}, a finite set; all
have μ ≤ n² + n + (n + 1)/4.
(b) (All of Type II.) For a prime p, the Type II cube points (c, d, j) of FIXED_MODULUS_SHOTS Lemma 1.1 are in
bijection with the pairs (d, P), d ≤ (p + 1)/3, P an ES point of V_{pd} whose λ = μ/D is divisible by d, via
A = 2j, λ = cd (and then g = 2λA − 1 = 4cdj − 1 = h).
(c) Consequently (an exact equivalence, PROVED; its strategic reading is an Assessment, R-O203 #1), any mechanism
acting on V_{pd} points (composition, units, Vieta moves, class-group
pigeonhole, …) that outputs ES points outputs elements of this finite explicit set, and it succeeds at p iff
some 4dj²p + 1 has a divisor ≡ −1 (mod 4dj) (cube (d, j)-line) — the moving-modulus divisor problem of B2. Confined
to d = 1 (V_p itself) it is FALSE at exactly 99 primes p < 10⁶ (13, 37, 97, …; GROWING_MUTE R201).
*Proof.* (a) Thm 1.3; the bound from j ≤ (n + 4t² + 1)/(4t) = t + (n + 1)/(4t), μ = nj + t convex in t, maximal at
t = n. (b) For n' = pd, A = 2j: n'A² + 1 = 4dj²p + 1 = D·g with g = 2λA − 1 = 4λj − 1. A cube point is a divisor
h ≡ −1 (mod 4dj) of 4dj²p + 1; take h = g, c = λ/d: g ≡ −1 (mod 4dj) ⟺ d | λ. Conversely from h put g := h,
λ := (g + 1)/(2A) = cd ∈ ℤ, D := (n'A² + 1)/g; by GROWING_MUTE Prop 1.2(a) (g | n'A² + B², g ≡ −1 mod 2AB, B = 1)
this is a V_{n'} point with μ = λD, and d | λ. (c) (a), (b) and FIXED_MODULUS_SHOTS Lemma 1.1. ∎
*Check (`scripts/cp_law.py 401 12`):* for odd n ≤ 401 and μ ≤ 12n, brute-force B = 1 points (all even A) equal the
Thm 1.3 prediction (804 points, 0 mismatches); Prop 1.2(a) product formula on 172 random pairs.
*Check (`scripts/cp_typeii.py 200`):* for all primes 5 ≤ p ≤ 200, cube points = d-sliced ES points of V_{pd}
(602 points, 0 mismatching primes).

## 5. Across μ (modification 2: violate "one order O_μ")

Different μ give different real orders, so the only ring seeing all μ at once is the imaginary order ℤ[√−n]
(V_n point ⟷ β = B + A√−n with N(β) = nA² + B² = D·g, g ≡ −1 mod 2AB; GROWING_MUTE Prop 1.1(c)).

**Proposition 5.1 (Type II = two-term "Machin" composition in ℤ[√−nd]; PROVED, elementary).** Let p be prime,
c, d, j, s ≥ 1. The following are equivalent:
(i) 4csdj = pj + c + s (Type II cube point (c, d, j) with partner s = (pj + c)/(4cdj − 1));
(ii) **(2cd + √−pd)(2sd + √−pd) = (d(c + s)/j)·(1 + 2j√−pd)** in ℚ(√−pd);
(iii) arccot(2c√(d/p)) + arccot(2s√(d/p)) = arccot(1/(2j√(pd))) (a two-term Machin-type relation);
and then **4/p = 1/(cds) + 1/(pdsj) + 1/(pdcj)**.
*Proof.* (ii): the product is (4csd² − pd) + 2d(c + s)√−pd, proportional to 1 + 2j√−pd iff 2j(4csd² − pd) = 2d(c + s),
i.e. (i). (iii): cot(θ₁ + θ₂) = (ab − 1)/(a + b) with a = 2c√(d/p), b = 2s√(d/p) gives (4csd − p)/(2(c+s)√(dp)),
equal to 1/(2j√(dp)) iff (i) (all angles in (0, π/2)). The Egyptian identity is (i) divided by pcdsj. ∎
*Reading.* This is the arctangent/Gaussian-integer correspondence of Machin–Størmer, transported to ℤ[√−pd]: the
ES point is the factorisation of the "target" 1 + 2j√−pd into two elements of the prescribed shape 2(·)d + √−pd,
i.e. (by norms) (4cdj − 1)(4sdj − 1) = 4dj²p + 1 — the cube's (d, j)-line. For d = 1 it is the real-quadratic slot
ε_μ of Thm 1.3 seen from the imaginary side (D = 4tj − 1 with t = c). Shape parity: a product of r elements
(even) + (odd)·√−n has shape (odd) + (even)·√−n iff r is even, so longer compositions ∏(2t_i + √−n) ∝ 1 + 2j√−n
need r even ≥ 4 (they no longer have the two-factor shape of (ii); whether they can encode 3-term ES identities is not examined). The classical Størmer theory has no
existence theorem to import: for two terms it is exactly "1 + c² has a divisor in the right place", i.e. B2 again
(Todd's reducibility criterion, P(1 + m²) < 2m, is the closest analogue: it is a largest-prime-factor condition,
not a divisor-in-a-residue-class condition; quoted from memory (Todd 1949), not re-checked).

**EVIDENCE (`scripts/cp_cross.py n X ntrip`, n = 13, 59, 97, 101; X = 40, 120).** Products β₁β₂, β₁β̄₂ of V_n
points with A, B ≤ X (14 resp. 21 points for X = 120) and 20 000 random triple products: **0** of the admissible
products are V_n points (pair: 0/123, 0/199; triple: 0/6001, 0/2904), and 0 in the size-matched random baseline.
Composition in ℤ[√−n] does not preserve V_n: the congruence modulus 2AB of the product is a new, multiplicatively
larger modulus (B2's "modulus part of the solution").

**Census (EVIDENCE; `scripts/cp_census.py lo hi cap [sq]`).** For every ES point (μ, D = N(ε_μ)) of every prime
5 ≤ p ≤ 1000, one full period of the CF of √(4(μ² − p)) was run and every proper divisor of the ES ideal 𝔢_μ
tested for principality in O' (Lagrange: all primitive representations of |norm| < √N are convergents; orientation
by p_{k−1}j ≡ ±(1 − 2μj)q_{k−1} mod d'; the script asserts that the ES element is the negative-norm convergent at k = 3 for μ > 2n and k = 1 for μ ≤ 2n —
never failed (R-O203 #4: assertion sharpened after review); ES points with D prime are skipped, nothing to test):
`  166 primes, 1736 ES points: D prime 690; D composite 1046, of which 284 (27%) have a principal proper divisor`
`  ("decomposable": ε_μ = u·α·β with N α = ∓d', N β = ±D/d'); 41 are V-decomposable (unit × product of three`
`  V_n points at the same μ, the R202 shape); 88 of 166 primes have ≥ 1 decomposable ES point.`
T1 control: odd squares 9 ≤ m² ≤ 1849: 0 ES points (Prop 2.1(d)). The "decomposable" share is the share of
composite D for which some proper divisor ideal of 𝔢_μ (not necessarily prime; e.g. n = 59, μ = 135: norms 9 and
15 principal, 3 and 5 not) happens to be principal in O'_μ (a wide-class-group statement, Cohen–Lenstra
flavoured); it is consistent with R202's two V-decomposable cases among odd n ≤ 301, μ ≤ 6n (here: all μ, primes
only). In every case the factorisation is a re-expression of an ES point that exists by Thm 1.3.

## 6. Barrier screen and remaining modifications

* **(ii) weaker target.** B ≡ 1 (mod n) ⟺ α ≡ 1 (mod η̄O) (O/η̄O ≅ ℤ/n, η̄ ↦ 0, so α = B − Aη̄ ↦ B): a ray-class
  condition mod the norm-n ideal (η̄), which composition and pigeonhole CAN address (ray class groups, Davenport).
  But B = 1 is this condition PLUS the archimedean condition B < n + 1, which singles out the depth-3 member of
  one unit orbit (Thm 1.3); B ≡ 1 (mod n) with B > 1 gives only ES^{[2]}, den z = B² (GROWING_MUTE hierarchy).
  Dead as a route to ES; recorded because it is the one place where a class-group statement touches B.
* **B2 (moving modulus).** Thm 1.3/Prop 4.1: ES at μ is N(ε_μ) | μ; over all μ it is "n + 4t² has a divisor
  ≡ −1 (mod 4t)", and over all d (Type II) "4dj²p + 1 has a divisor ≡ −1 (mod 4dj)". Composition changes none of
  these moduli; in ℤ[√−n] it multiplies them (§5 numerics: 0 hits). Fully inside B2.
* **B3 (main term).** The λ-direction main term (MARKOFF_ES §6, ≍ Λ/√log Λ) belongs to ES^{[2]} (B free). The
  B = 1 locus is finite (Prop 4.1(a): μ ≤ n² + n + (n+1)/4), so for fixed n there is no growing parameter and no main term at all (the Type II count per
prime is the classical one; no lower bound for it is known pointwise);
  composition cannot transfer the large ES^{[2]} main term to B = 1 because B = 1 is not a class/ideal condition
  (Prop 2.1(c)).
* **B5 (T1).** Prop 2.1(d): at n = m² the δ-fibre of every box is empty (χ₋₄ ≡ 1); census control: 0 ES points at
  21 odd squares ≤ 1849. Every statement above is consistent with T1; none uses a step false at squares that is
  claimed true for primes.
* **B6.** Not applicable (fixed n throughout).
* **Hatches.** H-A (joint factorisation): the R202 phenomenon IS a joint factorisation (𝔢_μ = 𝔡₁𝔡₂𝔡₃ with all 𝔡_i
  principal of negative norm) but of an ideal whose relevant property (norm | μ) is fixed beforehand. H-E (exact
  positive identities): Prop 5.1 is an exact identity, but it is equivalent to the Type II equation itself.

## 7. Verdict (O203 checkpoint 1, after self-review R-O203)

1. **Composition law (PROVED, §1–2).** V_n points at μ = negative-norm primitive elements of O'_μ = ℤ[2√(μ² − n)]
   whose norm divides μ; composition = ideal multiplication; a product of r points is a point iff r is odd, the
   product is primitive (same prime above each shared ℓ) and ∏D_i | μ. V_n values at μ = the fibre over the
   order-2 narrow class δ of the box 𝔅(μ) of primitive ideals of norm dividing μ. At squares the fibre is empty.
2. **ES slot rigidity (PROVED: Thm 1.3, Cor 1.4, Prop 4.1).** At each μ > n the only possible B = 1 point is the
   explicit element ε_μ = 1 − 2jη̄ (μ = nj + t), which exists for every μ and has class δ; ES at μ ⟺
   |N(ε_μ)| = 4tj − 1 divides μ. B = 1 is not a class condition. So at a FIXED μ, composition (or any operation
   inside O'_μ) cannot create an ES point: impossible where 4tj − 1 ∤ μ, superfluous elsewhere. The whole B = 1
   locus is a finite explicit set, and all of Type II is the d-sliced B = 1 locus of V_{pd} (pd may be even).
   The R202 M2 phenomenon is real: 41 of 1736 ES points (p ≤ 1000) are unit × three V_n points at the same μ, and
   284 of the 1046 with composite D have some principal proper divisor (a weaker, two-element factorisation);
   both only re-express ES points that exist anyway.
3. **Pigeonhole (PROVED negative, Prop 3.1).** Davenport-type pigeonhole in Cl⁺(O'_μ) produces positive-norm
   elements; reaching δ is a target-sum question that no count of split primes forces (abstract group example,
   not an arithmetic no-go theorem); and it would give ES^{[2]} only.
4. **Across μ (§5).** Type II ⟺ two-term Machin/arccot relations (2cd + √−pd)(2sd + √−pd) ∝ 1 + 2j√−pd (PROVED, an
   exact but equivalent dictionary); composition in ℤ[√−n] does not preserve V_n (EVIDENCE, 0 hits).
5. **Status: ES untouched.** The composition route is closed at fixed μ (PROVED). Across μ or d, any mechanism
   that outputs B = 1 points succeeds at p iff it exhibits a divisor ≡ −1 (mod 4dj) of some 4dj²p + 1 (PROVED
   equivalence, Prop 4.1(c)); that composition contributes nothing to that selection problem is an Assessment
   (R-O203 #1), not a theorem. What survives is the ES^{[2]} class-group lottery of MARKOFF_ES §6, unchanged.
