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
with fixed S (bounded overflow; R200 repair M1) is a finite search like ES; the sieve regime r → ∞ *forces* log den(z) ≥ ½ log(r/4n) − O(1).
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

**Corollary 1.4 (overflow = inflated box at the same modulus; PROVED).** Let h ≡ 3 (mod 4), K := (h+1)/4. A shot datum
(Q, h) with overflow Q₁ exists iff −n ≡ c/j (mod h) for some c = Q₀Q₁², j with **c·j = K·Q₁²** and Q₀ | K (Q = Q₀Q₁,
j = K/Q₀), gcd(Q₁, K/Q₀) = 1 and gcd(Q, n) = 1 (R200 repair m2; this j is Prop 1.3's k, not its j). So ES (Q₁ = 1) is the FIXED_MODULUS_SHOTS box criterion on Box(K) (d = 1 slice), and overflow Q₁ replaces
Box(K) by (a slice of) **Box(K·Q₁²) at the same modulus h** — in the certificate cube (c, d, j) of FIXED_MODULUS_SHOTS
Lemma 1.1 it is the point (Q₀Q₁², Q₁^{−2}, K/Q₀): **ES^{(y)} is the certificate cube with d allowed to be the inverse
of a square of primes dividing y**, ES^{(y,e)} caps the exponents of that inverse square at e.
*Proof.* 4Q₀k = h + 1 gives 4 ≡ (Q₀k)^{−1}, so h | n + 4Q² iff −n ≡ Q₀²Q₁²/(Q₀k) = Q₀Q₁²/k (mod h); and
h | p + 4c²d with (c, d) = (Q₀Q₁², Q₁^{−2}) is h | p + 4Q². ∎ (Asserted on all 46 084 shots of `xc_rigidity.py`.)
*Reading.* Covering by an exponent box at h needs |Box(K·Q₁²)| ≥ (h−1)/2, i.e. τ₃-size of K·Q₁² ≳ h, while
Thm 2.1 below caps h ≤ 2nQ₁²(n + Q₁²): a covering argument needs the cap e ≥ (log h)^{1−o(1)} (Prop 3.1), whereas the archimedean wall (Cor 2.2) only asks e·log rad(Q₁) ≥ ¼ log(h/4n) − O(1).

## 2. Rigidity: every bounded overflow (fixed S, bounded cap) is a finite search (R200 repair M1)

**Theorem 2.1 (overflow rigidity; PROVED).** For every shot datum (Q, g) of n with overflow Q₁,
`g ≤ max(Q₁⁴n + Q₁²,  n(n + 1)(Q₁² + ½) + 1) ≤ 2nQ₁²(n + Q₁²).`
In particular Q₁ ≥ min(√g/(2n), (g/(4n))^{1/4}), i.e. **den(z) = Q₁² ≥ min(g/(4n²), √(g/(4n)))**.
*Proof.* Notation of Prop 1.3; j ≥ 4 (4 | j, j > 0). *Case kj < 2Q₁²* (so Q₁ ≥ 2, k < Q₁²/2): by (b),
g ≤ 4k²n + Q₁² < Q₁⁴n + Q₁². *Case kj ≥ 2Q₁²:* D = kj − Q₁² ≥ kj/2, so by (a) Q₀ = (4kn + j)/(4D) ≤ 2n/j + 1/(2k)
≤ (n + 1)/2, and by (b) g ≤ (4k²n + Q₁²)/(kj/2) ≤ 2kn + 1 (j ≥ 4, Q₁² ≤ kj/2). Since g = 4Q₀k − 1 divides n + 4Q₀²Q₁²,
4Q₀k − 1 ≤ n + 4Q₀²Q₁², so k ≤ (n + 1)/(4Q₀) + Q₀Q₁² ≤ (n + 1)/4 + (n + 1)Q₁²/2, and g ≤ 2kn + 1 ≤ n(n+1)(Q₁² + ½) + 1.
The final bound: Q₁⁴n + Q₁² ≤ 2nQ₁⁴, and 2n²Q₁² + 2nQ₁⁴ − n(n+1)(Q₁² + ½) − 1 ≥ n²/2 + n/2 − 1 > 0
(expand, Q₁ ≥ 1). ∎
*Check (`xc_rigidity.py 301 301`):* max g/(nQ₁²(n + Q₁²)) = 0.583 over the 46 084 shots (attained at n = 3, g = 7).
*Sharpness of the Q₁⁴ term (PROVED, explicit family).* D = 3, j = 4, k = (Q₁² + 3)/4 (Q₁ odd, 3 ∤ Q₁, so 4 | Q₁² + 3 and 3 ∤ k), and
n ≡ −1/k (mod 3), i.e. n ≡ 2 (mod 3) since k ≡ 1, and gcd(n, Q₁) = 1 (R200 repair m4): Q₀ = (kn + 1)/3, g = 4Q₀k − 1 = (4k²n + Q₁²)/3 ≈ Q₁⁴n/12. (E.g. Q₁ = 5, k = 7, n = 17: Q₀ = 40,
Q = 200, g = 1119, 17 + 4·200² = 1119·143, and 4/17 = 1/40 + 1/4760 + 25/119 — an ES^{(y,1)} solution, 5 | y.) So the exponent 4 in g ≲ nQ₁⁴ cannot be lowered.

**Corollary 2.2 (bounded caps are finite searches; PROVED).** Let S be a finite set of odd primes and e < ∞. Every
shot solution of ES^{(y,e)}(n) with Q ∈ ⟨S⟩ has g ≤ 2nQ₁²(n + Q₁²) ≤ 2n·P^{2e}(n + P^{2e}), P := ∏_{s∈S} s; the
same bound holds for every S if "Q ∈ ⟨S⟩" is replaced by "rad(Q₁) | (g+1)/4 and v_ℓ(Q₁) ≤ e", with P := rad(Q₁) ≤ g.
Hence, for fixed S and e, the firing set {g} of ES^{(y,e)}(n) in the shot family is finite and polynomially bounded
in n — the same situation as ES itself (e = 0: g ≤ 2n(n+1); cf. FIXED_MODULUS_SHOTS Prop 6.1, h ≤ (p+1)(p+5)/4).
**Consequently any argument that produces the certifying prime r by a sieve with r → ∞ (as Thm 4.2 of
FROBENIUS_FIRING does, ineffectively) can only certify ES^{(y,e)} with e·log P ≥ log Q₁ ≥ ¼ log(r/(4n)) − O(1)**
(for r ≥ 4n³, the Q₁⁴ branch); for fixed S this is e ≥ (log r)/(4 log P) − O_n(1). ∎ (Immediate from Thm 2.1.)
*Reading (Assessment).* With S fixed, the exponent cap is not a parameter that a sieve can push down to 0 (R200 repair M1: for S growing
with r, see §6 item 2). Between the sieve
regime and ES there is a sharp archimedean wall: the moment the overflow is bounded, the certifying moduli are
bounded, and existence becomes a statement about one finite set (B2/B3). The rigidity is archimedean, not
congruential: Q₀ | (g+1)/4 makes Q₀ ≤ g/4, so 4Q² ≤ 4Q₁²·g²/16 and the integer quotient m = (n + 4Q²)/g is forced into
the class −n mod Q₀ with m ≈ Q₀Q₁²/k — for Q₁ = 1 this pins everything down (g ≤ 2n(n+1)).

## 3. The exponent box at a fixed prime r: coverage scale, a provable upgrade, and the dictionary

Setup. S = {s₁, …, s_k} odd primes, r a prime ≡ 3 (mod 4) with P := ∏ s_i | (r+1)/4, κ_i := v_{s_i}((r+1)/4) ≥ 1.
Λ_r := {a ∈ ℤ^k : ∏ s_i^{2a_i} ≡ 1 (mod r)}, so ℤ^k/Λ_r ≅ Γ_r² := ⟨s_i² mod r⟩. By Prop 1.2, r fires for
ES^{(y,e)}(n) with Q ∈ ⟨S⟩ iff −n/4 ∈ **B_r(e) := {∏ s_i^{2a_i} : 0 ≤ a_i ≤ κ_i + e} (mod r)** (the exponent box).
(e = ∞: B_r = Γ_r²; FROBENIUS_FIRING Thm 4.2 makes Γ_r² = (F_r^*)² for a sieved r.)

**Proposition 3.1 (size of the exponent box; PROVED).** (a) |B_r(e)| ≤ ∏(κ_i + e + 1).
(b) For every r and every S as above, |B_r(e)| ≤ τ((r+1)/4)·(e + 2)^{ω((r+1)/4)} ≤ r^{(1+o(1))·log(e+2)/log log r + o(1)}.
In particular B_r(0) ⊆ the ES box, of size ≤ τ((r+1)/4) = r^{o(1)} (the KEY OBSERVATION's box at e = 0).
(c) Hence B_r(e) ⊇ (F_r^*)² (coverage) forces e ≥ (log r)^{1−o(1)}; and for |S| = k fixed it forces
(log₃ r + e + 1)^k ≥ (r−1)/2, i.e. e ≥ r^{1/k}/2 for large r.
*Proof.* (a) count exponent vectors. (b) κ + e + 1 ≤ κ(e + 2) for κ ≥ 1, so ∏(κ_i + e + 1) ≤ (e+2)^k ∏ κ_i
≤ (e+2)^k τ(∏ s_i^{κ_i}) ≤ (e+2)^{ω((r+1)/4)} τ((r+1)/4); then ω(N) ≤ (1+o(1)) log N/log log N and τ(N) = N^{o(1)}.
(c) (r−1)/2 ≤ r^{(1+o(1))log(e+2)/log log r + o(1)} needs log(e+2) ≥ (1 − o(1)) log log r. Fixed k: κ_i ≤ log₃ r. ∎
*Reading.* The KEY OBSERVATION (enlarge κ_i by r ≡ −1 mod s_i^{K_i}) buys nothing for coverage: the box is
multiplicative in (κ_i + 1) and ∏ s_i^{κ_i} ≤ r, so its size is a divisor function, r^{o(1)}. Coverage is a matter of the
overflow e alone, at the scale e ≈ log r with ≈ log r/log log r primes (all the small primes, r ≡ −1 mod their
product), or e ≈ r^{1/k} with k fixed primes. Combined with Cor 2.2 (necessary: log den z ≥ ¼ log(r/4n)), the
*sieve window* for the overflow is
`¼ log(r/4n) − O(1)  ≤  log den(z)  [necessary]      vs      log den(z) ≈ 2e·log P ≳ (log r)^{2−o(1)}  [coverage].`
(Assessment, R200 repair m5: the right side is heuristic — den z ≤ P^{2e} bounds the hit from above; coverage says
nothing about the den of the particular hit. Prop 3.1 obstructs covering arguments only.)

**Theorem 3.2 (ES^{(y)} with sub-polynomial overflow exponent; PROVED relative to UNIT_ORBIT Lemma 2.2, as Thm 4.2 of
FROBENIUS_FIRING; ineffective).** For every δ > 0 and every odd non-square n > 1 there is a shot solution of
ES^{(y)}(n) with Q ∈ ⟨S⟩ for a fixed set S of k ≥ 2/δ + 1 odd primes prime to n, with
**v_s(Q₁) ≤ v_s(Q) ≤ r^{δ}** for every s, r = the certifying prime (so den(z) ≤ P^{2r^δ}; y = n(r+1)/4). I.e.
ES^{(y, e)} holds with e = y^{δ} (exponent cap polynomially small against ord ≍ r used by Thm 4.2).
*Proof.* Take k ≥ 4 primes and the sieve of FROBENIUS_FIRING Thm 4.2 (modulus M = 4 rad(n) P, r ≡ −1 mod each s_i,
(n/r) = −1, (r−1)/2 with all prime factors ≥ x^{1/4−ε}): ≫ x/log²x primes r ≤ x, all but o(x/log²x) of which have
Γ_r² = (F_r^*)²; and ≤ x^{1−ε} of them are < x^{1−ε}. *Exceptional set:* λ₁(Λ_r) ≤ B (ℓ^∞ successive minimum) means
r | N_c := ∏_{c_i>0} s_i^{2c_i} − ∏_{c_i<0} s_i^{−2c_i} for some c ≠ 0 with |c_i| ≤ B; N_c ≠ 0 has ≪_S B prime factors,
so #{r : λ₁(Λ_r) ≤ B} ≪_S B^{k+1} (as in UNIT_ORBIT Lemma 2.3). With B = x^{1/(k+1) − η}, this is o(x/log²x). So some
sieved r ∈ [x^{1−ε}, x] has Γ_r² = (F_r^*)² and λ₁ > B. *Covering:* Minkowski's second theorem for the ℓ^∞ ball
(volume 2^k) gives λ₁⋯λ_k ≤ det Λ_r = (r−1)/2, so λ_k ≤ x/B^{k−1} = x^{2/(k+1) + (k−1)η}. If v₁, …, v_k ∈ Λ_r are
independent with |v_i|_∞ = λ_i, every class of ℤ^k/⟨v_i⟩ — hence of ℤ^k/Λ_r — has a representative Σ t_i v_i,
t ∈ [0,1)^k, with sup-norm ≤ Σλ_i ≤ kλ_k =: L. Represent the class of (−n/4)·∏ s_i^{−2L} by a with |a_i| ≤ L; then
Q := ∏ s_i^{a_i + L} has exponents in [0, 2L] and Q² ≡ −n/4 (mod r). With ε, η small, 2L ≤ r^{2/(k+1) + δ'} ≤ r^δ.
The shot solution is ES^{(y)} (s_i | (r+1)/4) with v_s(Q) ≤ 2L. ∎
*Remarks.* (1) The gain over Thm 4.2 is only in the exponent's size (r^δ instead of r); by Prop 3.1(c) any
covering argument with fixed k needs e ≥ r^{1/k}/2, so with fixed S this is optimal up to the factor 2 in the exponent
(2/(k+1) vs 1/k). (2) Letting k → ∞ with x requires the sieve modulus M = 4 rad(n)·P to stay ≤ x^{o(1)}, which caps
k at o(log x/log log x) and leaves e ≥ x^{1/k} superpolylogarithmic; e = polylog(r) would need P ≈ r^{1/2}, i.e. a
sieve at level beyond Bombieri–Vinogradov (the modulus P eats the whole BV level). (Assessment, not proved.)

**Dictionary 3.3 (coverage = geometry of numbers = non-pretentiousness of characters on S; PROVED as stated).**
(a) B_r(e) ⊇ (F_r^*)² iff every coset of Λ_r meets the box ∏[0, κ_i + e]; sufficient: kλ_k(Λ_r) ≤ (min κ_i + e)/2;
necessary: ∏(κ_i + e + 1) ≥ (r−1)/2 (Prop 3.1).
(b) The dual lattice Λ_r^* = {θ ∈ ℝ^k : θ·a ∈ ℤ ∀a ∈ Λ_r} is {(φ(s₁²), …, φ(s_k²)) + ℤ^k : χ a character of (F_r^*)²},
where χ(u) = e^{2πiφ(u)}. A short dual vector is a nontrivial character χ with ‖φ(s_i²)‖ ≤ t for all i, i.e. χ
"pretends to be 1 on S" in the sup-angle. Transference (Banaszczyk, Math. Ann. 296 (1993): μ₂(Λ)·λ₁^{(2)}(Λ^*) ≤ k/2, ℓ² covering radius and minimum;
form verified by R200; later work sharpens the constant) gives: the box ∏[0, κ_i + e] contains an ℓ² ball of radius E/2, E := min κ_i + e, and every
coset of Λ_r meets every ball of radius μ₂(Λ_r); so **coverage at overflow e holds once no nontrivial character χ of
(F_r^*)² has ‖φ(s²)‖ < k/E for all s ∈ S** (if λ₁^{(2)}(Λ^*) < k/E, some dual vector θ ≠ 0 has all coordinates < k/E; for k/E ≤ 1 θ ∉ ℤ^k, so χ is
nontrivial, and for k/E > 1/2 the criterion is vacuous — R200 repair m6).
(c) Hence the ES-relevant regime (e ≈ polylog r, S ≈ all primes ≤ log r dividing (r+1)/4) asks for a
**uniform small-prime discrete-log non-concentration statement**: for some (sieved) r, the discrete logs
of the primes ≤ c log r are not simultaneously close to 0 after multiplication by any nonzero j ∈ ℤ/((r−1)/2).
*Assessment.* This is beyond known pointwise GRH inputs (averaged-over-r inputs not examined; R200 repair m6): under GRH, character sums Σ_{s≤y} χ(s) log s ≪ √y log²(ry) are nontrivial only for
y ≫ log⁴ r, and the best GRH generation bound (Bach: primes ≤ 2 log² r generate F_r^*) already needs a product of
primes ≈ e^{2 log² r} ≫ r — which cannot divide (r+1)/4. The radical constraint rad(Q) | (r+1)/4 confines S to
primes of total size ≤ r, i.e. to the range where no known (or GRH-conditional) character-sum input exists.

## 4. The cap as a divisors-in-residue-classes problem (flip to fixed shot)

**Proposition 4.1 (bounded multiplicity below overflow N^{1/4}; PROVED relative to the cited theorem).** For a shot
Q (odd, prime to n), N := n + 4Q², the ES^{(y,e)} certificates with this Q are the divisors g ≡ −1 (mod q_e),
q_e := 4Q^{(e)} ≥ 4Q/rad(Q)^e = 2√(N − n)/rad(Q)^e (Prop 1.2; R200 repair m7: equality, C_n := √(n+4)/4 works). If rad(Q)^e ≤ N^{1/4 − α}/C_n (α > 0), then q_e ≥ N^{1/4+α}
and the number of such divisors is O(α^{−3/2}) (Coppersmith–Howgrave-Graham–Nagaraj, *Math. Comp.* 77 (2008),
divisors in residue classes; Lenstra, *Math. Comp.* 42 (1984): ≤ 11 when q ≥ N^{1/3}; statements verified by R200).
*Reading (Assessment).* With overflow below N^{1/4}, each shot contributes O(1) certificates — the bounded-multiplicity
hypothesis of B3 (CONDITIONAL_ES Prop 2.3) holds; the self-mute theorem lives at overflow ≫ N^{1/4} (Q = s^j with
j ≫ log r, q_e = 4s), where a single N has unboundedly many admissible divisors and the problem is statistical.
So in the shot coordinates the cap interpolates the modulus q_e from N^{1/2} (ES) to O(1) (ES^{(y)}), with the
Lenstra–Coppersmith threshold N^{1/4} in between; nothing in this flip produces existence at a fixed n either
(it is a statement about one integer N per shot, B6/B4-type).

## 5. Numerics (EVIDENCE; every reported best solution verified with exact rationals)

**5.1 Least overflow e, S = {3} (`scripts/xc_leaste.py 3 24 …`, `data/xc/leaste_s3_primes.txt.gz`; columns
n, least e, its least j, g, κ = v₃((g+1)/4), least e over prime g, complete-up-to).** For every prime 5 ≤ p < 10⁶
and j ≤ 24, all divisors g ≡ 3 (mod 4) of p + 4·9^j (GNU `factor`) are scanned; a shot is admissible if j = 0 or
3 | (g+1)/4, with overflow e = max(0, j − κ). Completeness: by the proof of Thm 2.1, Q₀ ≤ Q₁²n/2 + Q₁²/2 + 1, so all
shots with overflow ≤ t are seen when 3^{24−t} exceeds this bound — t = 4 for every p < 10⁶ (column 7); least e ≤ 4
is exact, larger values are exact when ≤ column 7 and upper bounds otherwise (835 primes).
* All 78 496 primes solved within j ≤ 24. Least-e histogram: 0: 73 910 (68 655 by p + 4 itself, 5 255 by Q = 3^j,
  j ≥ 1, i.e. ES), 1: 1 539, 2: 1 118, 3: 708, 4: 365, 5: 263, 6: 210, 7: 118, 8: 91, 9: 76, 10: 33, 11: 29, 12: 15,
  13: 11, 14: 4, 15: 3, 16: 2, 19: 1 (p = 598 537: j = 20, g = 473 027 prime, κ = 1). Prime g only: max 19.
* The tail is geometric, P(e ≥ t+1 | e ≥ t) ≈ 0.65, and nearly p-independent (p ≡ 1 mod 4: P(e ≥ 1) = 0.149, 0.122,
  0.113, 0.107 and P(e ≥ 6) = 0.019, 0.014, 0.016, 0.014 on [0, 10⁵), [10⁵, 3·10⁵), [3·10⁵, 6·10⁵), [6·10⁵, 10⁶)):
  (Assessment, R200 repair m8:) a lottery whose expected number of hits grows by a constant (≈ 0.4) per unit of cap — the "log log lottery" of a
  fixed-S family (Σ_r |B_r(e)|/r over the rigidity range), much thinner than ES's own polylog lottery.
* Least K: at the best solution with e ≥ 1, κ = 1, 2, 3, 4, 5, 6, 7, 8 for 2 542, 1 306, 495, 166, 50, 19, 6, 2 primes.
  **Large K is never what helps**: the data use small κ and spend the overflow, as Prop 3.1 predicts (the box is
  multiplicative in κ_i + 1, so κ buys only a divisor-function factor).
* T1 control: all 332 odd squares m² < 10⁶ with 3 ∤ m, j ≤ 30: **no admissible shot at any e** (as proved, §1).

**5.2 Coverage scale, k = 2 (`scripts/xc_cover.py 3 5 200000`, `data/xc/cover_3_5.txt`).** For the 1 126 primes
r ≡ −1 (mod 60) below 2·10⁵, 1 121 have ⟨9, 25⟩ = (F_r^*)²; for 1 101 of them the least L with
{9^a 25^b : 0 ≤ a, b ≤ L} = (F_r^*)² is ≤ 4√r + 10, with L/√r between 0.65 (the bound of Prop 3.1(c) is
√((r−1)/2) − 1) and 3.99, median 0.955 (statistics over these 1 101 only; R200 repair m8 — also xc_cover.py skips r = 59, so all
three counts are one short); the remaining 20 have L > 4√r + 10 (short multiplicative relations — the
exceptional set of Thm 3.2's proof). So covering needs and typically achieves e ≍ r^{1/k}; Thm 3.2's proof guarantees
r^{2/(k+1)+ε}.

## 6. Verdict (O200 checkpoint 1)

1. **Exact dictionary (Prop 1.3, Cor 1.4).** In the shot family r | n + 4Q², the overflow Q₁ = Q/gcd(Q, (r+1)/4) is
   exactly √den(z), and (Q₁, k = (r+1)/(4Q₀)) satisfy Dr = 4k²n + Q₁², D ≡ −Q₁² (mod 4k). ES is the slice Q₁ = 1
   (growing modulus 4k, fixed shot), ES^□ the slice k = 1 (fixed modulus 4, free shot); ES^{(y)} is the certificate cube
   with d allowed to be Q₁^{−2}, rad(Q₁) | y; T1 is the mod-4 part of the congruence.
2. **Archimedean wall (Thm 2.1, Cor 2.2; PROVED).** r ≤ 2nQ₁²(n + Q₁²), sharp in the Q₁⁴ term. Every bounded cap
   e < ∞ (fixed S) is a finite search with polynomially bounded moduli, exactly like ES; any sieve producing r → ∞
   certifies at best e·log rad(Q₁) ≥ ¼ log(r/4n) − O(1). The interpolation parameter does not reach ES continuously:
   the sieve regime ends at e ≍ log r/log P, and below it there is nothing to sieve. *(R200 repair M1: all of this is
   for FIXED S (bounded rad Q₁). With S growing with r the wall only asks rad(Q₁)^e ≥ (r/4n)^{1/4} − O(1), which is
   no archimedean obstruction even at e = 1 (Q₁ a squarefree divisor of (r+1)/4 of size ≈ r^{1/4}); there the
   obstruction is Prop 3.1, which excludes covering arguments only. Bounded e with growing S and a non-covering
   argument is not ruled out here (open).)*
3. **Coverage scale (Prop 3.1; PROVED).** The exponent box at r has ≤ τ((r+1)/4)(e+2)^{ω((r+1)/4)} elements; the KEY
   OBSERVATION (large κ via r ≡ −1 mod s^K) only buys a divisor-function factor. Covering (F_r^*)² needs
   e ≥ (log r)^{1−o(1)} (all small primes in (r+1)/4), or e ≥ r^{1/k}/2 with k fixed primes. (a)+(b) of the brief
   are incompatible at e = 0 *for a covering argument* (R200 repair m5) by the divisor bound, independently of the
   level of distribution.
4. **Provable side (Thm 3.2; PROVED relative to the Thm 4.2 sieve).** ES^{(y)} with exponent cap y^δ, any δ > 0
   (geometry of numbers on the relation lattice Λ_r + the Lemma 2.3 count of short relations).
5. **Named open problem (Dictionary 3.3).** Coverage at e = polylog(r) ⇔ (up to constants) no nontrivial character
   of (F_r^*)² is sup-angle-close to 1 on the primes dividing (r+1)/4 — a small-prime discrete-log
   non-concentration statement on primes of total size ≤ r, a range where no known pointwise character-sum input,
   even under GRH, suffices (averaged-over-r inputs not examined; Assessment — R200 repair m6). Even solving
   it would prove ES^{(y, polylog)}, not ES (item 2).
6. **Numerics (§5).** S = {3}: least overflow ≤ 4 for 98.9 % of primes < 10⁶, max ≤ 19, geometric tail, p-stable;
   squares: never (T1). Large κ is never used.
Not an opening for ES (Assessment): the exponent cap is B2/B3 seen from the self-mute side — at bounded cap and
fixed S (R200 repair M1) the archimedean wall makes it a finite search; at sieve-able caps the box must be inflated from r^{o(1)} to r.
