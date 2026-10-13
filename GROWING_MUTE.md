# GROWING_MUTE — bounded exponent cap with a growing mute set (task O201, spark relay V)

Status: in progress (O201). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on EXPONENT_CAP.md (O200; Def 1.1, Prop 1.2, Prop 1.3, Thm 2.1; review R200 M1), FROBENIUS_FIRING §4,
UNIT_ORBIT_ES §2, FIXED_MODULUS_SHOTS Lemma 1.1 / Prop 6.1. Scripts `scripts/gm_*`, outputs `data/gm/`.

Notation. n > 1 odd. Shot datum (Q, g): Q ≥ 1 odd, gcd(Q, n) = 1, g ≡ 3 (mod 4), g | n + 4Q²; K := (g+1)/4,
Q₀ := gcd(Q, K), Q₁ := Q/Q₀ (overflow), k := K/Q₀. (R201 repair M1: in §1–§4 the parity of Q is NOT assumed — Q may be even,
only the overflow Q₁ must be odd; den z = Q₁² still holds, being a prime-by-prime computation (R201 check: all 30 166 shots
with even Q ≤ 300, odd n ≤ 201, gcd(Q, n) = 1 have den z = Q₁²); "shot" below means this widened family.) Shot solution (UNIT_ORBIT Prop 2.1): x = (n + m)/4,
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
convention; not needed for the solution. (R201 repair M1: Q₀ = λB with λ := (g+1)/(2AB), so λ even gives Q EVEN — 370 of the
816 test triples; this is a bijection with the WIDENED shot family of the Notation, and with the original Q-odd family only after
adding "λ odd")), via A = 2k, B = Q₁, Q₀ = (g+1)/(2A), Q = Q₀B. The overflow is B,
den(z) = B². ES^{(y,1)} ⇔ additionally **B squarefree**; ES ⇔ B = 1 (the Type II line "4k²n + 1 has a divisor
≡ −1 (mod 4k)", FIXED_MODULUS_SHOTS Lemma 1.1).
*Proof.* (a) is EXPONENT_CAP Prop 1.2 (σ ≥ max(1, c − e)). (b) v_ℓ(Q) ≤ 2v_ℓ(K) ⇔ [v_ℓ(Q) ≤ v_ℓ(K)] or
[v_ℓ(Q₀) = v_ℓ(K) and v_ℓ(Q₁) = v_ℓ(Q) − v_ℓ(K) ≤ v_ℓ(Q₀)] ⇔ v_ℓ(Q₁) ≤ v_ℓ(Q₀). y² = n²Q₀²k² and gcd(Q₁, nk) = 1.
(c) By EXPONENT_CAP Prop 1.3(b), g·D = 4k²n + Q₁² = nA² + B², and g + 1 = 4Q₀k = 2AQ₀; with B | Q₀ this is
g ≡ −1 (mod 2AB). Conversely (R201 repair m1): D := (nA² + B²)/g ≡ −B² (mod 2A) because 2A | A² and g ≡ −1 (mod 2A);
gcd(B, A/2) = 1; so the converse of Prop 1.3 with k = A/2, Q₁ = B gives Q₀ = (g+1)/(2A) and a shot with overflow
exactly B, and Q₀ ≡ 0 (mod B) by g ≡ −1 (mod 2AB). ∎
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
(c) (**No second integral involution.**) The A-involution A ↦ 2μB/n − A is integral iff n | λ; for n ≡ 1 (mod 4) no
solution has n | λ (R201 repair m2: in fact for NO odd n > 1 — see the end of the proof). So for fixed (λ, D) the solution set
is a finite union of Pell orbits. (R201 repair m5: both Vieta moves fix C = 2μ, so there is never a Markoff-type tree across
C anyway; what (c) removes is classical Vieta jumping, which with both involutions integral would bound μ in terms of D.)
*Proof.* (a) g·D = nA² + B² with g = 2ABλ − 1 rearranges to the display; the converse defines g := 2ABμ/D − 1 ≡ −1
(2AB) dividing nA² + B². Completing the square gives the norm form. (b) the matrix has determinant t² − (μ² − n)u² = 1
and preserves f = nA² − 2μAB + B² (standard automorph of [n, −2μ, 1]); u even ⇒ A' ≡ uB ≡ 0, t odd ⇒ B' ≡ tB ≡ 1
(mod 2); B' ≡ (t − μu)B (mod n) with (t − μu)(t + μu) ≡ 1 (mod n), so gcd(B', n) = 1; unimodularity keeps gcd(A, B) = 1.
f < 0 confines B/A to the interval between the two positive roots μ ± √(μ² − n), a cone preserved by automorphs of
positive trace; squaring a fundamental automorph makes u even. (c) The A-quadratic nA² − 2μBA + (B² + D) has root
sum 2μB/n; gcd(B, n) = 1 and gcd(D, n) = 1 (a common prime q would divide B) make this integral iff n | 2λ, i.e.
n | λ. Then g ≡ −1 (mod n), so every prime q | g has q ∤ nB and (−n/q) = 1; the Jacobi symbol gives (−n/g) = 1,
(−1/g) = −1, so (n/g) = −1, while reciprocity (n ≡ 1 mod 4) gives (n/g) = (g/n) = (−1/n) = 1. (R201 repair m2: for every odd n, g ≡ −1 (mod 4n) and the
Kronecker character χ_{−4n} is odd, so χ_{−4n}(g) = −1, contradicting (−n/q) = 1 for all q | g; R201 check: n | λ in 0 of 1912
points over all odd n ≤ 401.) ∎
*Reading.* The overflow coordinate B is exactly what turns ES's finite Type II problem (B = 1: D(2λA − 1) = nA² + 1,
bounded A) into an orbit problem: for B free, each (λ, D) with μ² − n non-square carries a Pell orbit with A, B → ∞.
(R201 repair M3: this shows there is no archimedean wall for ES^{[2]}, whose exponents are UNBOUNDED; automorphs do not
preserve B squarefree (many images have r² | B), so for the bounded cap e = 1 an infinite orbit inside ES^{(y,1)} needs
infinitely many squarefree B along a binary recurrence — expected, unproved. R200 M1 ("a wall is not proved") is
consistent with this but not "confirmed".) The difficulty does not disappear,
it moves: existence of ONE representation of −D by the principal form of discriminant 4(λ²D² − n), for some (λ, D)
— a class-group lottery over a 2-parameter family of real quadratic orders (§2).

## 2. The growing-mute sieve: what it can and cannot see (task (2))

(V4) Construction as briefed: sieve primes g ≡ −1 (mod 4P), g ≡ a (mod 4 rad n), P = product of a growing set of
primes, P ≈ g^{1/4} (inside the Bombieri–Vinogradov range), and hope −n/4 ∈ {Q² : Q | K·rad K} (mod g).

**Proposition 2.1 (for each fixed P the firing set is an explicit finite divisor set; PROVED).** Fix squarefree odd P
prime to n. The primes g ≡ −1 (mod 4P) whose shot solution is ES^{(y,1)} with overflow Q₁ | P are exactly the prime
divisors g ≡ −1 (mod 4P) of the integers nA² + Q₁², A even, Q₁ | P, with g ≡ −1 (mod 2AQ₁); all of them satisfy
g ≤ 2nP²(n + P²) (EXPONENT_CAP Thm 2.1). Their number is ≤ Σ_{Q₁ | P} Σ_{A ≤ (n+1)(1+2Q₁²)} ω(nA² + Q₁²) (A = 2k and the k-bound in the proof of Thm 2.1),
in any case finite, while the sieve supplies ≫ x/(φ(4P rad n) log x) primes g ≤ x in the progression.
*Proof.* Prop 1.1(c) (B = Q₁ squarefree, A = 2k) and Thm 2.1. ∎
*Consequence (Assessment).* (R201 repair M2: the following holds for FIXED P only — the fixed-S case of EXPONENT_CAP
Cor 2.2. In the construction (V4) P ≈ g^{1/4} grows with g, and then the bound g ≤ 2nP²(n + P²) ≈ 2n·g is vacuous: this is
exactly R200 M1's open regime, and nothing here excludes a level-of-distribution argument with modulus 4P(g). What remains
true: with P = P(g) the firing condition is hitting a g^{o(1)}-size box, and no Chebotarev field is fixed in advance, so
standard BV/Chebotarev input does not DIRECTLY apply.) For fixed P, level of distribution (BV/BDH) and Chebotarev/Kummer inputs are irrelevant here: whether
a prime g in the progression fires is not a Frobenius condition in any field fixed in advance — it is divisibility of
one of finitely many explicit integers nA² + Q₁² by g, where A itself is tied to g by 2AQ₁ | g + 1. The ES^{(y)}
proof (FROBENIUS_FIRING Thm 4.2) works because with FIXED S and unbounded exponents the firing condition
"−n/4 ∈ ⟨S⟩²" is Kummer-type (a covering of (F_g^*)²); at bounded e every per-g box has size g^{o(1)}
(EXPONENT_CAP Prop 3.1) and only hitting is possible, and hitting is the explicit divisor problem of Prop 1.1(c).

**Proposition 2.2 (the e = 1 / growing-S problem is an integral-point problem on a 3-fold with no archimedean
bound; PROVED as an equivalence).** For odd n, the following are equivalent:
(i) ES^{(y,1)}(n) has a shot solution;
(ii) **V_n : nA² + B² + D = 2λD·AB** has an integral point with A, λ, D ≥ 1, A even, B odd squarefree,
gcd(A, B) = gcd(B, n) = 1;
(iii) for some D ≥ 1 the affine Markoff-type cubic surface **S_{n,D} : nA² + B² + D = ABC** has an integral point with
**2D | C** and the side conditions of (ii).
ES's own shot family (the d = 1 slice of the certificate cube) is the curve B = 1 of V_n, on which A ≤ 3(n+1)/2
(Thm 2.1); on V_n with B free, every point with μ² − n non-square (μ = λD) lies on an infinite Pell orbit
(Prop 1.2(b)) — of the version of V_n WITHOUT the squarefree condition (R201 repair M3: automorphs do not preserve B
squarefree). (ii)/(iii) include λ even, i.e. Q = λB² even, so (i) refers to the widened shot family of the Notation
(R201 repair M1). Necessarily D ≡ 3 (mod 4) (mod 4: B² + D ≡ 0).
*Proof.* Prop 1.1(c), Prop 1.2(a), C := 2λD. D ≡ 3 (4): A even, B odd gives nA² + B² + D ≡ 1 + D ≡ 0 (mod 4). ∎
*Reading (Assessment).* Write E_n(X) := #{points of V_n with A, B ≤ X}. The naive expectation
Σ_{A,B ≤ X} τ(nA² + B²)/(2AB) ≍ (log X)³ diverges, so the e = 1 problem at a FIXED n is an infinite lottery — B3
(main term ≤ p^{o(1)} within an archimedean range) and B6 (averages over p) do not apply, because the family is
infinite at fixed n. But the condition 2DAB | nA² + B² + D is a *thin* divisibility (for each (μ, D) the solution set is
finitely many Pell orbits, each with O(log X) points in the box; R201 repair m6: for fixed D, μ = λD still ranges over
≍ nX/D values), not a positive-density congruence condition, so no equidistribution/sieve input
counts E_n(X): the count is a sum over D of integral points on Markoff-type surfaces, the setting of Ghosh–Sarnak
(Invent. Math. 229 (2022), integral points on x² + y² + z² − xyz = k; their surfaces are different and fully
Vieta-symmetric — citation from memory, not re-checked) where the integral Hasse principle holds for almost all k but fails for
infinitely many k (at least √K (log K)^{−1/2} up to K) (R201 repair M4: the earlier "fails for a positive proportion of k"
was wrong; checked against arXiv:1706.06712; I have not checked whether S_{n,D} behaves alike). Prop 1.2(c) shows our
surfaces have only ONE integral Vieta involution when n ≡ 1 (mod 4), so the orbit-descent tools used for Markoff
surfaces (descent to a finite set of fundamental solutions) are unavailable.

## 3. Pushing e → 0: what exactly fails at ES (task (3))

**Proposition 3.1 (the e-ladder in one equation; PROVED).** In the shot family, with (A, B) as in Prop 1.1(c) and
K = (g+1)/4:
* ES (e = 0): B = 1, D(2λA − 1) = nA² + 1 — the classical Type II line; A ≤ 3(n+1)/2, g ≤ 2n(n+1): a finite box;
  the residue −n/4 must be Q² with Q | K, a divisor box of size τ(K) = g^{o(1)}.
* ES^{(y,1)}: B squarefree, Q | K·rad K, box size ≤ τ(K)·2^{ω(K)} = g^{o(1)} per g, but g unbounded (g ≤ 2nB²(n + B²)
  only).
* ES^{[2]}: B free (Q | K²), box size τ(K²) = g^{o(1)}, g unbounded.
* ES^{(y)} (e = ∞), S fixed: Q ∈ ⟨S⟩ with any exponents; box = ⟨S⟩² mod g, which is all of (F_g^*)² for sieved g.
So between e = 0 and e = 1 NOTHING changes at a single modulus g (box g^{o(1)} in both); the entire difference is
archimedean: B = 1 caps A (hence g), B free does not. Between e = 1 and e = ∞ the per-modulus box jumps from g^{o(1)}
to ≍ g (covering becomes possible, EXPONENT_CAP Prop 3.1(c): e ≥ (log g)^{1−o(1)}).
*Proof.* Prop 1.1, Prop 1.2, EXPONENT_CAP Thm 2.1 and Prop 3.1. A ≤ 3(n+1)/2: the proof of Thm 2.1 with Q₁ = 1 gives
k ≤ (n+1)/4 + (n+1)/2. ∎

**Smooth representatives (the brief's GHS question; Assessment with a PROVED count).** The e = 0 condition asks
that −n/4 have a square root mod g of the special form Q | (g+1)/4 (Q < g), not merely a smooth one. Results on
smooth numbers in residue classes (Harman; Granville–Harper–Soundararajan: q^ε-smooth representatives of every class
mod q of size q^{O(1)}; citations from the brief, not re-checked) are statements about Ψ(x, y)-sized sets. The sets
relevant here are tiny: **#{Q ≤ g^C : rad Q | K} ≤ (C log g/log 2 + 1)^{ω(K)}** (each exponent ≤ C log g/log 2),
which is g^{o(1)} unless ω(K) ≫ log g/log log g, i.e. unless (g+1)/4 is essentially a primorial; and with the
exponent cap e the count is ≤ τ(K)(e+2)^{ω(K)} (EXPONENT_CAP Prop 3.1(b)). So at every bounded e the relevant set
of representatives is subpolynomial and smooth-number equidistribution says nothing; GHS-type inputs become
relevant only at e ≍ log g with K primorial-like — the covering regime, which (EXPONENT_CAP Thm 2.1) forces
overflow ≥ (g/4n)^{1/4} and is far from ES. For e = 0 the additional archimedean constraint g ≤ 2n(n+1) makes it the
finite B3 lottery (expected count ≍ log³ n). Comparison with short-range smooth results: none of them restrict the
support to the divisors of a prescribed integer, which is the actual constraint (it is B2).

## 4. Numerics (EVIDENCE; every reported solution re-verified with exact rationals or exact divisibility)

**4.1 Least overflow at primes (`scripts/gm_least.py 1000000 20 300 31`, `data/gm/least_1e6.txt`).** For the 39 175
primes p ≡ 1 (mod 4), 5 ≤ p < 10⁶ (p ≡ 3 mod 4 is free), search the (A, B) family of Prop 1.1(c), A = 2k:
* B = 1 (shot-family ES) with k ≤ 20: 38 705 primes (least-k histogram 1: 29 666, 2: 4 223, 3: 2 153, 4: 733, …).
* Remaining 470: B = 1 with k ≤ 300 solves 354; **116 primes have no B = 1 solution with k ≤ 300**, and all of them
  have an ES^{(y,1)} shot solution with B squarefree: B = 3 (105 primes), 5 (6), 7 (3), 11 (p = 2293), 23
  (p = 12433: A = 26, g = 33487 = 2·26·23·28 − 1 | 12433·26² + 23²). Max k used ≤ 300 throughout.
* Completeness: B = 1 needs k ≤ 3(p+1)/4 (Prop 3.1), so "no B = 1" is exact only for p < 400: **p = 13, 37, 97 have no
  shot-family ES solution at all** (they have other ES solutions, outside the d = 1 slice), but have ES^{(y,1)}
  shots: e.g. p = 13, (A, B, λ, D) = (10, 3, 2, 11), g = 119, Q = 18: **4/13 = 1/6 + 1/390 + 9/65**, 3 | 390.
  For larger p the B > 1 entries are upper bounds for the least B (B = 1 might occur at k > 300).
* Reading: the overflow is almost never needed and, when it is, the least squarefree B is tiny — consistent with a
  divergent lottery in (A, B), not with any structure. Exact least-e statistics in the growing-S sense are not
  meaningful here because e ∈ {0, 1} and P = B.

**4.2 Orbit structure (`scripts/gm_orbits.py 300 13 17 29 73 9 25 49`, A, B ≤ 300).** Solutions of V_n (Prop 2.2):
n = 13: 4 (all B > 1: (λ, D) = (2,11), (3,7), (9,7), (1,47)); 17: 19 (4 with B = 1); 29: 20; 73: 6. Every (λ, D)
pair carries ≤ 3 points in the box (Pell orbits grow fast), so the count is dominated by NEW (λ, D) pairs — the
lottery is over the surfaces S_{n,D}, not along orbits. **n | λ never occurs** (Prop 1.2(c)). D ≡ 3 (mod 4) always.
T1 control: **n = 9, 25, 49: no solution** (as proved, Prop 1.1 T1).

## 5. Verdict (O201 checkpoint 1)

1. **Exact dictionary (Prop 1.1, 1.2; PROVED).** Bounded overflow in the shot family is the symmetric divisor
   problem "nA² + B² has a divisor ≡ −1 (mod 2AB)" (B = overflow, A = 2k), equivalently integral points on
   V_n : nA² + B² + D = 2λDAB, i.e. on Markoff-type cubic surfaces S_{n,D} : nA² + B² + D = ABC with 2D | C. ES's shot
   family is B = 1; ES^{(y,1)} is B squarefree; ES^{[2]} ("den z | y²") is B free. T1 = "sum of two coprime squares".
2. **The growing mute set removes the archimedean wall and nothing else (Prop 1.2(b), 2.1, 3.1).** Every
   solution with B > 1 lies on an infinite Pell orbit (so no bound on g, confirming R200 M1), but the per-modulus box
   is g^{o(1)} at every bounded e, so the problem is pure hitting; and for each fixed P the sieve's progression meets
   the firing set only in an explicit finite divisor set — BV/BDH and Chebotarev contribute nothing.
3. **No Markov tree (Prop 1.2(c); PROVED).** For n ≡ 1 (mod 4) only one Vieta involution is integral (reciprocity
   forbids n | λ), so Markoff-style descent to finitely many fundamental solutions is unavailable.
4. **e → 0 (Prop 3.1).** e = 0 and e = 1 have the same per-modulus box size (g^{o(1)}); they differ only in that
   B = 1 bounds A ≤ 3(n+1)/2. Smooth-number results (GHS etc.) are irrelevant at every bounded e: the admissible
   representatives are divisors of (g+1)/4 (times a cap), a g^{o(1)}-set (B2).
5. **Status of ES^{(y,1)} for all non-squares: OPEN.** Heuristically an infinite (log³) lottery at fixed n, hence
   immune to B3/B6; the missing input is a lower bound for integral points on V_n (a thin set), for which I know no
   method. EVIDENCE: all primes < 10⁶ have ES^{(y,1)} shot solutions with B ≤ 23.
Not an opening for ES (Assessment): the variant is closer to ES than ES^{(y)} only archimedeanly; its proof would need
an integral-point theorem on a family of Markoff-type surfaces, which would be a new kind of input (see sparks).
