# EXPONENT_CAP — the exponent cap between the provable ES^{(y)} and ES (task O200, spark relay U)

Status: in progress (O200). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on FROBENIUS_FIRING.md (O196, CLAIMED, under review R196; Thm 4.2, Cor 4.3), UNIT_ORBIT_ES.md ((J)23; Prop 2.1,
Lemmas 2.2/2.3, Thm 2.4, Prop 6.1), FIXED_MODULUS_SHOTS.md ((J)25; Lemma 1.1, Prop 6.1, Cor 3.2). Scripts
`scripts/xc_*`, outputs `data/xc/`.

## 0. Iteration log

(U1) Construction attempt as briefed: make the cap v_s((r+1)/4) large by r ≡ −1 (mod s^K) and hope the exponent box
∏[0, K_i + e] equidistributes in ⟨S⟩ mod r. First screen: the box has ≤ ∏(K_i + e + 1) elements, and with e = 0 this
is ≤ τ((r+1)/4) = r^{o(1)} — the divisor bound, B3. So the KEY OBSERVATION cannot work at e = 0 by counting. The
hypothesis to violate is "box size r^{o(1)}" ⇒ allow overflow e and ask how large e must be (§3).
(U2) Before the analytic question, an archimedean one: is the overflow problem at bounded e still a finite search?
Yes (Thm 2.1, rigidity): a shot with overflow Q₁ (den z = Q₁²) has modulus g ≤ 2nQ₁²(n + Q₁²). So every bounded cap
is a finite search like ES; the sieve regime r → ∞ *forces* log den(z) ≥ ½ log(r/4n) − O(1).
(U3) The exact equation behind (U2) is a duality (Prop 1.3): overflow Q₁ and "growing modulus" 4k swap roles;
ES = (Q₁ = 1, k free), ES^□ = (k = 1, Q₁ free).

## 1. Definitions and the exact dictionary

Throughout n > 1 is odd. A **shot datum** is (Q, g) with Q ≥ 1, gcd(Q, n) = 1, g ≡ 3 (mod 4), g | n + 4Q². UNIT_ORBIT
Prop 2.1 (whose proof uses only these hypotheses) gives
`x = (n + m)/4,  y = n(g+1)/4,  z = n·x·(g+1)/(4Q²),   m := (n + 4Q²)/g,`
with 4/n = 1/x + 1/y + 1/z, x, y ∈ ℤ_{>0}, Type II shape at every prime of n.

**Definition 1.1.** Put Q₀ := gcd(Q, (g+1)/4) and **Q₁ := Q/Q₀ (the overflow)**. For a cap e ∈ ℤ_{≥0} ∪ {∞},
**ES^{(y,e)}(n)**: 4/n = 1/x + 1/y + 1/z with x, y ∈ ℤ_{>0}, z ∈ ℚ_{>0}, and every prime ℓ with v_ℓ(z) < 0 satisfies
ℓ ∤ 2n, ℓ | y, v_ℓ(z) even and **v_ℓ(z) ≥ −2e**. So ES^{(y,0)} = ES and ES^{(y,∞)} = ES^{(y)} (FROBENIUS_FIRING Def 4.1).
Equivalently: den(z) = q² with q odd, gcd(q, n) = 1, rad(q) | y and v_ℓ(q) ≤ e for all ℓ.

**Proposition 1.2 (the shot solution's denominator; PROVED).** For a shot datum with Q odd, den(z) = Q₁². Hence the shot
solution lies in ES^{(y,e)} iff (i) Q₁ odd, rad(Q₁) | (g+1)/4 and (ii) v_ℓ(Q) ≤ v_ℓ(g+1) + e for every ℓ | Q, i.e.
**g ≡ −1 (mod 4·Q^{(e)}),  Q^{(e)} := ∏_{ℓ | Q} ℓ^{max(1, v_ℓ(Q) − e)}**   (for Q odd).
e = 0: g ≡ −1 (mod 4Q) (UNIT_ORBIT Prop 6.1, ES). e = ∞: g ≡ −1 (mod 4 rad Q) (FROBENIUS_FIRING Cor 4.3).
*Proof.* For ℓ | Q odd, c = v_ℓ(Q), σ = v_ℓ(g+1): from 4gx = n(g+1) + 4Q² one gets v_ℓ(z) = 2σ − 2c if σ < c and
v_ℓ(z) ≥ 0 if σ ≥ c (UNIT_ORBIT Prop 2.1/6.1, whose computation covers σ < 2c; for c ≤ σ < 2c it gives 2σ − 2c ≥ 0).
So the ℓ-part of den(z) is ℓ^{2 max(0, c − σ)} = ℓ^{2 v_ℓ(Q/gcd(Q, g+1))}. Condition ℓ | y = n(g+1)/4 with ℓ ∤ n is
ℓ | (g+1)/4 (ℓ odd); v_ℓ(z) ≥ −2e is c − σ ≤ e. Combine: σ ≥ max(1, c − e). ∎

**Proposition 1.3 (exact dictionary: overflow ↔ growing modulus; PROVED).** Let (Q, g) be a shot datum, Q₀, Q₁ as
above, k := (g+1)/(4Q₀) ∈ ℤ, m = (n + 4Q²)/g. Then j := (m + n)/Q₀ is a positive integer, 4 | j, and
`(a)  4Q₀(kj − Q₁²) = 4kn + j,      (b)  D·g = 4k²n + Q₁²  with  D := kj − Q₁² ≥ 1,   D ≡ −Q₁² (mod 4k).`
Conversely, given n, Q₁ odd, k ≥ 1 with gcd(Q₁, k) = 1 and a divisor D of 4k²n + Q₁² with D ≡ −Q₁² (mod 4k),
put g := (4k²n + Q₁²)/D, j := (D + Q₁²)/k, Q₀ := (4kn + j)/(4D). Then Q₀ ∈ ℤ_{>0}, g = 4Q₀k − 1 and g | n + 4(Q₀Q₁)²:
a shot datum (when gcd(Q₀Q₁, n) = 1) whose overflow is exactly Q₁ (as gcd(Q₀Q₁, Q₀k) = Q₀).
*Proof.* g ≡ −1 (mod Q₀) and Q₀ | Q give m ≡ −n (mod Q₀), so j ∈ ℤ, and j > 0 as m, n > 0. Expanding
g·m = (4Q₀k − 1)(jQ₀ − n) = n + 4Q₀²Q₁² gives Q₀(4kjQ₀ − 4kn − j − 4Q₀Q₁²) = 0, i.e. (a); so 4 | j, and D > 0.
Multiplying (a) by k and using kj = D + Q₁²: 4Q₀kD = 4k²n + D + Q₁², i.e. (g + 1)D = 4k²n + D + Q₁², which is (b);
D ≡ −Q₁² (mod 4k) is kj = D + Q₁² with 4 | j. Conversely: 4 | j by the congruence; D·g = 4k²n + Q₁² is odd so D is odd;
k(4kn + j) = 4k²n + D + Q₁² ≡ 0 (mod D) and gcd(D, k) | gcd(Q₁², k) = 1, so D | 4kn + j, and 4 | 4kn + j: Q₀ ∈ ℤ.
Then 4Q₀k = (4k²n + kj)/D = g + 1, and g(jQ₀ − n) = Q₀(4kjQ₀ − 4kn − j) + n = 4Q₀²(kj − D) + n = n + 4Q₀²Q₁². ∎
*Check (`scripts/xc_rigidity.py 301 301`):* all 46 084 shot data with odd n ≤ 301, odd Q ≤ 301, gcd(Q, n) = 1, every
divisor g ≡ 3 (mod 4) of n + 4Q²: (a), (b), D > 0 and den(z) = Q₁² (exact rationals) hold in every case.
*Reading.* Q₁ = 1 is the ES Type II line "4k²n + 1 has a divisor ≡ −1 (mod 4k)" (FIXED_MODULUS_SHOTS Lemma 1.1,
d = 1, j ↔ k): the modulus 4k grows, the shot index is frozen. k = 1 is "4n + Q₁² has a divisor ≡ 3 (mod 4)", the
fixed-modulus orbit of SYNTHESIS_SPARKS2 Prop 2.2 (ES^□), now with the shot index Q₁ free. **The overflow Q₁ and the
growing modulus 4k are dual coordinates on the same equation; ES^{(y,e)} interpolates by capping the overflow,
while k stays free.** The self-mute condition (i) reads rad(Q₁) | Q₀k.
*T1 in these coordinates.* At n = m² with gcd(Q₁, 2km) = 1, 4k²m² + Q₁² is a sum of two coprime squares, so all its
divisors are ≡ 1 (mod 4), contradicting D ≡ −Q₁² ≡ 3 (mod 4): no shot datum at any e (the mod-4 part of (b) is the T1).

## 2. Rigidity: every bounded cap is a finite search

**Theorem 2.1 (overflow rigidity; PROVED).** For every shot datum (Q, g) of n with overflow Q₁,
`g ≤ max(Q₁⁴n + Q₁²,  n(n + 1)(Q₁² + ½) + 1) ≤ 2nQ₁²(n + Q₁²).`
In particular Q₁ ≥ min(√g/(2n), (g/(4n))^{1/4}), i.e. **den(z) = Q₁² ≥ min(g/(4n²), √(g/(4n)))**.
*Proof.* Notation of Prop 1.3; j ≥ 4 (4 | j, j > 0). *Case kj < 2Q₁²* (so Q₁ ≥ 2, k < Q₁²/2): by (b),
g ≤ 4k²n + Q₁² < Q₁⁴n + Q₁². *Case kj ≥ 2Q₁²:* D = kj − Q₁² ≥ kj/2, so by (a) Q₀ = (4kn + j)/(4D) ≤ 2n/j + 1/(2k)
≤ (n + 1)/2, and by (b) g ≤ (4k²n + Q₁²)/(kj/2) ≤ 2kn + 1 (j ≥ 4, Q₁² ≤ kj/2). Since g = 4Q₀k − 1 divides n + 4Q₀²Q₁²,
4Q₀k − 1 ≤ n + 4Q₀²Q₁², so k ≤ (n + 1)/(4Q₀) + Q₀Q₁² ≤ (n + 1)/4 + (n + 1)Q₁²/2, and g ≤ 2kn + 1 ≤ n(n+1)(Q₁² + ½) + 1.
The final bound: Q₁⁴n + Q₁² ≤ 2nQ₁²(n + Q₁²), and n(n+1)(Q₁² + ½) + 1 ≤ 2n²Q₁² for n ≥ 3. ∎
*Check (`xc_rigidity.py 301 301`):* max g/(nQ₁²(n + Q₁²)) = 0.583 over the 46 084 shots (attained at n = 3, g = 7).
*Sharpness of the Q₁⁴ term (PROVED, explicit family).* D = 3, j = 4, k = (Q₁² + 3)/4 (Q₁ odd, so 4 | Q₁² + 3), and
n ≡ −1/k (mod 3): Q₀ = (kn + 1)/3, g = 4Q₀k − 1 = (4k²n + Q₁²)/3 ≈ Q₁⁴n/12. (E.g. Q₁ = 5, k = 7, n = 5: Q₀ = 12,
Q = 60, g = 335, 5 + 4·60² = 14405 = 335·43, den(z) = 25.) So the exponent 4 in g ≲ nQ₁⁴ cannot be lowered.

**Corollary 2.2 (bounded caps are finite searches; PROVED).** Let S be a finite set of odd primes and e < ∞. Every
shot solution of ES^{(y,e)}(n) with Q ∈ ⟨S⟩ has g ≤ 2nQ₁²(n + Q₁²) ≤ 2n·P^{2e}(n + P^{2e}), P := ∏_{s∈S} s; the
same bound holds for every S if "Q ∈ ⟨S⟩" is replaced by "rad(Q₁) | (g+1)/4 and v_ℓ(Q₁) ≤ e", with P := rad(Q₁) ≤ g.
Hence, for fixed S and e, the firing set {g} of ES^{(y,e)}(n) in the shot family is finite and polynomially bounded
in n — the same situation as ES itself (e = 0: g ≤ 2n(n+1); cf. FIXED_MODULUS_SHOTS Prop 6.1, h ≤ (p+1)(p+5)/4).
**Consequently any argument that produces the certifying prime r by a sieve with r → ∞ (as Thm 4.2 of
FROBENIUS_FIRING does, ineffectively) can only certify ES^{(y,e)} with e·log P ≥ log Q₁ ≥ ¼ log(r/(4n)) − O(1)**
(for r ≥ 4n³, the Q₁⁴ branch); for fixed S this is e ≥ (log r)/(4 log P) − O_n(1). ∎ (Immediate from Thm 2.1.)
*Reading (Assessment).* The exponent cap is not a parameter that a sieve can push down to 0. Between the sieve
regime and ES there is a sharp archimedean wall: the moment the overflow is bounded, the certifying moduli are
bounded, and existence becomes a statement about one finite set (B2/B3). The rigidity is archimedean, not
congruential: Q₀ | (g+1)/4 makes Q₀ ≤ g/4, so 4Q² ≤ 4Q₁²·g²/16 and the integer quotient m = (n + 4Q²)/g is forced into
the class −n mod Q₀ with m ≈ Q₀Q₁²/k — for Q₁ = 1 this pins everything down (g ≤ 2n(n+1)).
