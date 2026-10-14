# PHASE_DIAGRAM — the (k, Q₁) phase diagram between ES^□ / ES^{(y)} and ES (task O204, wave Y-a)

Status: in progress (O204). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on EXPONENT_CAP.md (O200: Prop 1.2, Prop 1.3 duality D·g = 4k²n + Q₁², Thm 2.1, Prop 3.1, Thm 3.2; R200 M1),
GROWING_MUTE.md (O201: (A, B) form, V_n), MARKOFF_ES.md (O202), COMPOSITION_ES.md (O203), FROBENIUS_FIRING §4,
UNIT_ORBIT_ES §2, SYNTHESIS_SPARKS2 §2 (ES^□). Scripts `scripts/pd_*`.

Notation (as in GROWING_MUTE, widened shot family): n > 1 odd; shot datum (Q, g): Q ≥ 1, gcd(Q, n) = 1, g ≡ 3 (mod 4),
g | n + 4Q²; K := (g+1)/4, Q₀ := gcd(Q, K), overflow Q₁ := Q/Q₀ (odd), k := K/Q₀; den(z) = Q₁², y = n(g+1)/4 = nQ₀k.
Variants: ES ⇒ ES^{(y,1)} ⇒ ES^{[2]} (Q₁ | Q₀, "den z | y²") ⇒ ES^{(y)} (rad Q₁ | Q₀k); ES^□: no mute condition.

## 0. Iteration log

(Y1) Construction attempt as briefed (sieve r ≡ −1 mod 4P, P ≈ r^{1/4}, Q₁ | P). Screen: for each r the admissible
set {Q : Q | K·rad K} has size ≤ τ(K)2^{ω(K)} = r^{o(1)}, so a single-n statement needs a *hit*; switching the
order of summation turns the hit count into Σ_Q #{r | n + 4Q² : r ≡ −1 (mod 4Q₀)}, i.e. divisors of n + 4Q² in a
class of modulus 4Q₀ ≥ 4√Q ≈ (n + 4Q²)^{1/4} — the Lenstra/Coppersmith threshold (EXPONENT_CAP Prop 4.1).
Hypothesis to violate: "the per-r box is r^{o(1)}". Bounded cap cannot violate it (Prop 3.1), so look for
(a) a deterministic mechanism (Pell / genus / units: T1-exact facts that hold exactly at non-squares), or
(b) a different slicing in which the modulus is fixed.
(Y2) Exact re-slicing (§1): ES^{[2]} ⟺ ∃ (t, j): n t² + 4 j² has a divisor ≡ −n (mod 4tj) (t = overflow), the
"D-face" of the duality; ES is t = 1. The λ = 1 sub-family is the quartic family "n + 4t⁴ has a divisor ≡ −1
(mod 4t)", and its j = 1 member is the FIXED-modulus test "64 + n³ has a divisor ≡ 3 (mod 4)" (e.g. n = 13:
64 + 13³ = 7·17·19, D = 7, t = 5, g = 359 | 13 + 4·25² → an ES^{(y,1)} solution of 4/13 with overflow 5). Fixed modulus only for one number per j: no infinite fixed-modulus family.
(Y3) Screen of (Y2): every slicing is one number per fixed parameter; the infinite directions all have moving
modulus. But the slicing exposes a structural fact that is new: with the self-mute cap Q₁ | Q₀ BOTH coordinate
directions of the duality plane are walled (§2), while every weaker variant has an unwalled direction. The phase
diagram is therefore organised by walls, and ES^{[2]} is the unique doubly-walled cell above ES (§3–§4).

## 1. Normal form: the overflow is a Q₁²-weight in the Type II equation

**Proposition 1.1 (PROVED; a re-expression of EXPONENT_CAP Prop 1.3 / Cor 1.4).** Let n > 1 be odd. Shot data
(Q, g) correspond bijectively to quadruples (a, b, k, Q₁) of positive integers with Q₁ odd, gcd(Q₁, k) = 1 and
`  k·(4ab − n) = b + a·Q₁²,    (1.1)`
via a = Q₀, b = (m + n)/(4Q₀) (m := (n + 4Q²)/g), k = (g+1)/(4Q₀), Q = aQ₁, g = 4ak − 1, m = 4ab − n
(plus gcd(aQ₁, n) = 1 for the shot convention). The overflow is Q₁, den z = Q₁², y = nak. In these coordinates
* ES (shot family = the d = 1 slice of ET's Type II 4abcd = a + b + nc): Q₁ = 1, i.e. k(4ab − n) = a + b;
* ES^{(y,1)}: Q₁ squarefree and Q₁ | a;  ES^{[2]}: Q₁ | a;  ES^{(y)}: rad Q₁ | a;  ES^□: no condition.
*Proof.* Prop 1.3: j' := (m + n)/Q₀ ∈ 4ℤ, so b = j'/4 ∈ ℤ_{>0}; D := kj' − Q₁² = 4kb − Q₁² and (a) reads
4Q₀D = 4kn + j', i.e. aD = kn + b, i.e. a(4kb − Q₁²) = kn + b, which is (1.1). Conversely (1.1) gives
m := 4ab − n > 0 with k m = b + aQ₁²; put g := 4ak − 1; then g·m = 16a²bk − 4akn − 4ab + n = 4a(b + aQ₁²) − 4ab + n
= n + 4a²Q₁², so g | n + 4Q² with Q = aQ₁, and gcd(Q, (g+1)/4) = a·gcd(Q₁, k) = a. ∎
*D-face (ES^{[2]}).* Writing a = λt, Q₁ = t: k(4λtb − n) = b + λt³; equivalently (eliminating k)
**ES^{[2]} shot ⟺ m := 4λtb − n > 0 divides b + λt³** ⟺ m | nt² + 4b² (as 4b(b + λt³) ≡ nt² + 4b² mod m and
gcd(m, 2bn) = 1). ES is t = 1: 4λb − n | λ + b. The quartic family of (Y2) is λ = 1.

## 2. The double wall of ES^{[2]}

**Theorem 2.1 (PROVED).** Let (Q, g) be an ES^{[2]} shot of odd n > 1 (overflow Q₁ odd, Q₁ | Q₀), k = (g+1)/(4Q₀).
(a) (**k-wall, new**) Q₁ ≤ (16k³n + 1)/(4k − 1) (< 4k²n + k n + 1).
(b) (Q₁-wall) g ≤ 2nQ₁²(n + Q₁²) (EXPONENT_CAP Thm 2.1); moreover if Q₁ > (n+1)/2 then k < Q₁²/2.
Hence every ES^{[2]} shot with Q₁ > (n+1)/2 lies in the band **√(Q₁/(4n+n/k))·(1 − o(1)) < k < Q₁²/2**: both
coordinates must grow together, every horizontal (fixed Q₁) and every vertical (fixed k) slice is a finite search.
*Proof.* (a) Prop 1.3(b): Dg = 4k²n + Q₁² with D ≥ 1. As Q₁ | Q₀, g = 4kQ₀ − 1 ≡ −1 (mod 4kQ₁), so g ≥ 4kQ₁ − 1
and, reducing Dg mod Q₁, D + 4k²n ≡ 0 (mod Q₁); hence D ≥ Q₁ − 4k²n. If Q₁ ≤ 4k²n, (a) holds because
(16k³n + 1) − 4k²n(4k − 1) = 4k²n + 1 > 0. Otherwise 4k²n + Q₁² = Dg ≥ (Q₁ − 4k²n)(4kQ₁ − 1), which expands to
(4k − 1)Q₁² ≤ (16k³n + 1)Q₁. (b) In the proof of EXPONENT_CAP Thm 2.1, the case kj' ≥ 2Q₁² gives Q₀ ≤ (n+1)/2, and
Q₁ | Q₀ then gives Q₁ ≤ (n+1)/2; so Q₁ > (n+1)/2 forces the case kj' < 2Q₁² with j' ≥ 4, i.e. k < Q₁²/2. ∎
*Sharpness.* (a) is attained: (n, k, Q₁) = (3, 2, 55), g = 439 (W = 385/7 = 55). Family: for every n ≡ 2 (mod 3),
k = 1, Q₁ = 4n + 3, D = 3, g = (16n² + 28n + 9)/3, Q₀ = (4n+3)(n+1)/3 is an ES^{[2]} shot (Q₁ | Q₀, gcd(Q, n) = 1)
with Q₁/W(1) → 3/4. (b): k/Q₁² up to 0.436 is observed ((n, k, Q₁) = (29, 126, 17), g = 8567).
*Check (`scripts/pd_band.py 101 6 1.3`, `scripts/pd_band2.py 41 41`; exact rationals):* all 360 shots with odd
n ≤ 101, k ≤ 6, Q₁ ≤ 1.3·W(k), and all 36 shots with n ≤ 41, (n+1)/2 < Q₁ ≤ 41, k ≤ 2Q₁²: identity (1.1), solution,
den z = Q₁² (when gcd(Q₀, n) = 1), walls (a), (b) hold; max Q₁/W(k) = 1.000, max k/Q₁² = 0.436.
*Reading.* Without the self-mute cap the k = 1 slice is infinite and elementary (ES^□: "4n + Q₁² has a divisor
≡ 3 (mod 4)", Dirichlet). The cap Q₁ | Q₀ converts the modulus 4 into 4Q₁ and the slice into a finite search: the
k-wall is created exactly by the self-mute cap, as the Q₁-wall of EXPONENT_CAP is created by fixing Q₁.
