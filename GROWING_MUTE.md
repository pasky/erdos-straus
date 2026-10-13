# GROWING_MUTE — bounded exponent cap with a growing mute set (task O201, spark relay V)

Status: in progress (O201). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on EXPONENT_CAP.md (O200; Def 1.1, Prop 1.2, Prop 1.3, Thm 2.1; review R200 M1), FROBENIUS_FIRING §4,
UNIT_ORBIT_ES §2, FIXED_MODULUS_SHOTS Lemma 1.1 / Prop 6.1. Scripts `scripts/gm_*`, outputs `data/gm/`.

Notation. n > 1 odd. Shot datum (Q, g): Q ≥ 1 odd, gcd(Q, n) = 1, g ≡ 3 (mod 4), g | n + 4Q²; K := (g+1)/4,
Q₀ := gcd(Q, K), Q₁ := Q/Q₀ (overflow), k := K/Q₀. Shot solution (UNIT_ORBIT Prop 2.1): x = (n + m)/4,
y = n(g+1)/4 = nQ₀k, z = n·x·(g+1)/(4Q²), m = (n + 4Q²)/g; den(z) = Q₁² (EXPONENT_CAP Prop 1.2).

## 0. Iteration log

(V1) Rewrite the e = 1 condition as a divisibility "Q | K·rad K" and notice the natural intermediate
ES^{[2]}: Q | K² (equivalently Q₁ | Q₀, equivalently den(z) | y²). Hierarchy ES = ES^{[1]} ⇒ ES^{(y,1)} ⇒ ES^{[2]} ⇒ ES^{(y)}.
(V2) In Prop 1.3 coordinates, Q₁ | Q₀ turns "g ≡ −1 (mod 4k)" into "g ≡ −1 (mod 4kQ₁)": the ES^{[2]} shot is the
symmetric statement **nA² + B² has a divisor ≡ −1 (mod 2AB)** (A = 2k, B = Q₁); ES is B = 1 (Prop 1.1).
(V3) Writing g = 2ABλ − 1 gives the Markov-type equation nA² − 2μAB + B² = −D, D | μ (Prop 1.2): for fixed (μ, D)
a binary-form representation problem with an infinite automorph (unit) orbit. ES = the slice B = 1 of it.

## 1. The exact dictionary for capped overflow

**Definition 1.0.** For 4/n = 1/x + 1/y + 1/z with x, y ∈ ℤ_{>0}, z ∈ ℚ_{>0}, write den(z) = q² (required to be a
square) with q odd and gcd(q, n) = 1. Then
* ES^{(y)}(n): rad(q) | y (FROBENIUS_FIRING Def 4.1);
* **ES^{[2]}(n): q | y** ("den(z) | y²");
* **ES^{(y,1)}(n): q | y and q squarefree** (= EXPONENT_CAP Def 1.1 with e = 1: v_ℓ(z) ≥ −2, ℓ | y);
* ES(n): q = 1.
So ES ⇒ ES^{(y,1)} ⇒ ES^{[2]} ⇒ ES^{(y)} for all solutions, not only shots.

**Proposition 1.1 (cap hierarchy and the (A, B) form; PROVED, elementary).** Let (Q, g) be a shot datum.
(a) The shot solution is in ES^{(y,e)} (EXPONENT_CAP Def 1.1) iff v_ℓ(Q) ≤ v_ℓ(K) + e and ℓ | K for every ℓ | Q.
In particular e = 1 iff **Q | K·rad(K)**; ES iff Q | K; ES^{(y)} iff rad Q | K.
(b) Q | K² ⇔ Q₁ | Q₀ ⇔ den(z) | y² (given gcd(Q₁, nk) = 1, which always holds: if ℓ | Q₁ then v_ℓ(Q) > v_ℓ(K), so
ℓ ∤ k; ℓ ∤ n by hypothesis). And Q | K·rad(K) ⇒ Q | K² (v_ℓ(K) + 1 ≤ 2v_ℓ(K) for v_ℓ(K) ≥ 1). So
**ES ⇒ ES^{(y,1)} ⇒ ES^{[2]} ⇒ ES^{(y)}** in the shot family, where ES^{[2]} := "den(z) | y²".
(c) (**(A, B) form.**) Shot data with Q | K² are in bijection with triples (A, B, g): A ≥ 2 even, B ≥ 1 odd,
gcd(A, B) = 1, gcd(B, n) = 1, and **g | nA² + B², g ≡ −1 (mod 2AB)** (plus gcd(Q₀, n) = 1 for the shot-datum
convention; not needed for the solution), via A = 2k, B = Q₁, Q₀ = (g+1)/(2A), Q = Q₀B. The overflow is B,
den(z) = B². ES^{(y,1)} ⇔ additionally **B squarefree**; ES ⇔ B = 1 (the Type II line "4k²n + 1 has a divisor
≡ −1 (mod 4k)", FIXED_MODULUS_SHOTS Lemma 1.1).
*Proof.* (a) is EXPONENT_CAP Prop 1.2 (σ ≥ max(1, c − e)). (b) v_ℓ(Q) ≤ 2v_ℓ(K) ⇔ [v_ℓ(Q) ≤ v_ℓ(K)] or
[v_ℓ(Q₀) = v_ℓ(K) and v_ℓ(Q₁) = v_ℓ(Q) − v_ℓ(K) ≤ v_ℓ(Q₀)] ⇔ v_ℓ(Q₁) ≤ v_ℓ(Q₀). y² = n²Q₀²k² and gcd(Q₁, nk) = 1.
(c) By EXPONENT_CAP Prop 1.3(b), g·D = 4k²n + Q₁² = nA² + B², and g + 1 = 4Q₀k = 2AQ₀; with B | Q₀ this is
g ≡ −1 (mod 2AB). Conversely, g ≡ −1 (mod 2A) and g | 4k²n + Q₁² with Q₁ ≡ … is the converse half of Prop 1.3
(D := (nA² + B²)/g ≡ −B² (mod 2A) since g ≡ −1 (mod 2A)), giving a shot with overflow exactly B, and
Q₀ = (g+1)/(2A) ≡ 0 (mod B) by the extra congruence. ∎
*Check (`scripts/gm_dict.py 201 60 301`):* odd n ≤ 201, even A ≤ 60, odd B ≤ 60: all 816 (A, B, g) give a valid
solution (exact rationals) with den(z) = B², B | Q₀, den(z) | y²; conversely all 497 shots with odd n ≤ 201,
odd Q ≤ 301, gcd(Q, n) = 1, Q | K² map to a valid (A, B, g).
*T1.* For n = m², nA² + B² = (mA)² + B² with gcd(mA, B) = 1 has only divisors ≡ 1 (mod 4); but g ≡ −1 (mod 4) (4 | 2AB).
So no ES^{[2]} shot (a fortiori no ES^{(y,1)} shot) exists at odd squares.

**Proposition 1.2 (the Markov-type equation and its unit orbits; PROVED).** Write g = 2ABλ − 1 and D := (nA² + B²)/g.
(a) ES^{[2]} shot data ⇔ positive integer solutions of
`  nA² + B² + D = 2λD·AB,   A even, B odd, gcd(A, B) = 1, gcd(B, n) = 1,`
equivalently, with μ := λD, (B − μA)² − (μ² − n)A² = −D, D | μ. (ES: B = 1, the Type II line. ES^{(y,1)}: B squarefree.)
(b) For fixed (λ, D), if μ² − n is not a square and there is one solution, there are infinitely many: the automorphs
(A, B) ↦ ((t + μu)A − uB, nuA + (t − μu)B), t² − (μ² − n)u² = 1, u even, preserve all side conditions and the branch
A, B > 0. (B-involution B ↦ 2μA − B is also always available; it is the one used in ES's own Type II pairs.)
(c) (**No Markov tree for n ≡ 1 mod 4.**) The A-involution A ↦ 2μB/n − A is integral iff n | λ; for n ≡ 1 (mod 4) no
solution has n | λ. So the solution set is a union of Pell orbits (one per (λ, D, class)), never a Markov-type tree.
*Proof.* (a) g·D = nA² + B² with g = 2ABλ − 1 rearranges to the display; the converse defines g := 2ABμ/D − 1 ≡ −1
(2AB) dividing nA² + B². Completing the square gives the norm form. (b) the matrix has determinant t² − (μ² − n)u² = 1
and preserves f = nA² − 2μAB + B² (standard automorph of [n, −2μ, 1]); u even ⇒ A' ≡ uB ≡ 0, t odd ⇒ B' ≡ tB ≡ 1
(mod 2); B' ≡ (t − μu)B (mod n) with (t − μu)(t + μu) ≡ 1 (mod n), so gcd(B', n) = 1; unimodularity keeps gcd(A, B) = 1.
f < 0 confines B/A to the interval between the two positive roots μ ± √(μ² − n), a cone preserved by automorphs of
positive trace; squaring a fundamental automorph makes u even. (c) The A-quadratic nA² − 2μBA + (B² + D) has root
sum 2μB/n; gcd(B, n) = 1 and gcd(D, n) = 1 (a common prime q would divide B) make this integral iff n | 2λ, i.e.
n | λ. Then g ≡ −1 (mod n), so every prime q | g has q ∤ nB and (−n/q) = 1; the Jacobi symbol gives (−n/g) = 1,
(−1/g) = −1, so (n/g) = −1, while reciprocity (n ≡ 1 mod 4) gives (n/g) = (g/n) = (−1/n) = 1. ∎
*Reading.* The overflow coordinate B is exactly what turns ES's finite Type II problem (B = 1: D(2λA − 1) = nA² + 1,
bounded A) into an orbit problem: for B free, each (λ, D) carries a Pell orbit with A, B → ∞ — this is the precise
sense in which bounded cap + growing mute set has NO archimedean wall (R200 M1). The difficulty does not disappear,
it moves: existence of ONE representation of −D by the principal form of discriminant 4(λ²D² − n), for some (λ, D)
— a class-group lottery over a 2-parameter family of real quadratic orders (§2).
