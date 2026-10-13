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

**Definition 1.0.** ES^{[a]}(n) (a ≥ 1): 4/n = 1/x + 1/y + 1/z, x, y ∈ ℤ_{>0}, z ∈ ℚ_{>0}, den(z) = q² with q odd,
gcd(q, n) = 1 and **q^{?}** … (see Prop 1.1(c) for the exact form used: in the shot family the condition is Q | K^a.)

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
