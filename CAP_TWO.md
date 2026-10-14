# CAP_TWO — the e = 2 cell: where the ES ladder turns from finite to infinite (task O214, spark relay Y6)

Status: in progress (O214). **ES is not solved here, nor any infinite case of ES, nor ES^{(y,2)}.** Labels as in
DISCOVERIES.md. Builds on EXPONENT_CAP.md (Def 1.1, Props 1.2/1.3), GROWING_MUTE.md (Prop 1.1(c) (A, B) form,
Prop 1.2 Pell orbits), MARKOFF_ES.md, PHASE_DIAGRAM.md (O204: Thm 2.1, Prop 3.1, Prop 4.1). Scripts `scripts/y6_*`.

Notation. n > 1 odd. Shot datum (Q, g): gcd(Q, n) = 1, g ≡ 3 (mod 4), g | n + 4Q² (widened family: Q may be even);
K = (g+1)/4, Q₀ = gcd(Q, K), Q₁ = Q/Q₀ (overflow, odd), k = K/Q₀; den z = Q₁² (EXPONENT_CAP Prop 1.2,
GROWING_MUTE R201-M1). ES^{(y,e)}: den z = q², rad q | y, v_ℓ(q) ≤ e. "k = 1 cap-2 shot": k = 1, rad Q₁ | Q₀,
v_ℓ(Q₁) ≤ 2 for all ℓ.

## 0. Iteration log

(Y6-1) Construction attempt as briefed: parametrise ALL k = 1 cap-2 shots (not only the pure-power family Q₁ = R²
of PHASE_DIAGRAM Prop 4.1). Writing Q₁ = cB² (c, B squarefree, coprime) and g + 1 = c·A·B gives a Markoff-type
equation (§1, Thm 1.1). Surprise: it is the SAME equation as GROWING_MUTE's ES^{[2]} (A, B) form; the two cells
differ only in the residue of c mod 4 (Thm 1.2). Consequence: the "finite → infinite" transition of O204 between
e = 1 and e = 2 at k = 1 is a slicing effect (§2): ES^{[2]} with k free and cap-2 at k = 1 are the two halves of one
family of Pell-orbit fibrations.

## 1. The k = 1 cap-2 cell is the c-odd half of the ES^{[2]} equation

**Theorem 1.1 (exact dictionary; PROVED, elementary).** Let n > 1 be odd. k = 1 cap-2 shot data (Q, g) are in bijection
with quadruples (a, B, c, E) of positive integers satisfying
`  W_n :   4n·a² + B² + E = c·a·B·E,     c, B odd squarefree, gcd(c, B) = 1,  E ≡ 3 (mod 4),  gcd(caB, n) = 1,`
via Q₁ = cB², Q₀ = caB/4, g = caB − 1, Q = Q₀Q₁ = c²aB³/4, E = (4na² + B²)/g. In W_n, **E ≡ 3 (mod 4) ⟺ 4 | a**
(given c, B odd). The shot solution has den z = Q₁² = c²B⁴, rad Q₁ = cB | Q₀ | y.
*Proof.* (⇐) 4 | a (below), so g = caB − 1 ≡ 3 (mod 4) and W_n is E·g = 4na² + B². Since caB ≡ 1 (mod g),
a²(4n + Q₁²) = 4na² + (caB)²B² ≡ 4na² + B² ≡ 0 (mod g), and gcd(a, g) = 1, so g | 4n + Q₁². With K = (g+1)/4 = Q₀:
4Q² = 4Q₀²Q₁² = (g+1)²Q₁²/4, so 4·(n + 4Q²) ≡ 4n + Q₁² ≡ 0 (mod g): g | n + 4Q². Primes of Q are primes of caB,
so gcd(Q, n) = 1. Q₀ | Q and K = Q₀ give gcd(Q, K) = Q₀ and k = 1; the overflow is Q₁ = cB², with v_ℓ ≤ 2 and
rad Q₁ = cB | caB/4 = Q₀ (4 | a). den z = Q₁² by EXPONENT_CAP Prop 1.2 (GROWING_MUTE R201-M1 for even Q).
(⇒) Given the shot, write Q₁ = cB² with c := ∏_{v_ℓ(Q₁)=1} ℓ, B := ∏_{v_ℓ(Q₁)=2} ℓ (unique). rad Q₁ = cB | Q₀ = K, so
a := 4Q₀/(cB) is a multiple of 4 and g = 4Q₀ − 1 = caB − 1. g | n + 4Q² gives (reversing the computation above)
g | 4n + Q₁², hence g | a²(4n + Q₁²) ≡ 4na² + B²; E := (4na² + B²)/g ∈ ℤ_{>0} and W_n holds. gcd(caB, n) = 1
since primes of cB divide Q and primes of a divide 4Q₀ | 4Q.
(E ≡ 3 ⟺ 4 | a.) Mod 4, W_n reads B² + E ≡ caBE. If 4 | a: E ≡ −B² ≡ 3. If E ≡ 3 and a odd or a ≡ 2 (mod 4),
caBE ≡ 1 + 3 ≡ 0 (mod 4) is impossible for a odd and gives 2·(odd) ≡ 0 for a ≡ 2 — contradiction. ∎

**Theorem 1.2 (one equation, two cells; PROVED).** Consider all positive solutions (a, B, c, E) of
`  4n·a² + B² + E = c·a·B·E,   B odd, gcd(B, n) = 1`   (equivalently: **4na² + B² has a divisor g ≡ −1 (mod aB)**,
g = caB − 1, E = (4na² + B²)/g). Then, by the residue of c mod 4:
* **c ≡ 0 (mod 4): ES^{[2]} shots** — this is GROWING_MUTE Prop 1.1(c) with A_GM = 2a, k = a, Q₁ = B, λ = c/4,
  E = D (the duality cofactor of EXPONENT_CAP Prop 1.3); side conditions gcd(a, B) = 1, gcd(λB, n) = 1. ES = {B = 1};
  ES^{(y,1)} = {B squarefree}.
* **c odd: k = 1 shots with overflow Q₁ = cB²** (Thm 1.1); cap 2 iff c, B squarefree and coprime. On {B = 1}:
  k = 1 ES^{(y,1)} shots with Q₁ = c (the walled cell, PHASE_DIAGRAM Thm 2.1(a)); on {c = 1}: the pure-power family
  Q₁ = B² (PHASE_DIAGRAM Prop 4.1, e = 2, k = 1).
* c ≡ 2 (mod 4): forces 2 | a, and the same computation gives overflow 2c'B² (c = 2c'), i.e. a 2-adic denominator,
  excluded from every ES^{(·)} variant.
*Proof.* c ≡ 0: GROWING_MUTE Prop 1.1(c) is "g | nA_GM² + B², g ≡ −1 (mod 2A_GM B)" with A_GM even; put A_GM = 2a,
then 2A_GM B = 4aB and g + 1 = 4λ·aB. c odd: Thm 1.1. c = 2c': g = 2c'aB − 1 ≡ 3 (mod 4) needs 2 | a; then
1/(2a) ≡ c'B (mod g), so the shot index Q with 4Q² ≡ −n, i.e. 2Q ≡ ±B/(2a)... (2Q)² ≡ B²/(4a²) ≡ (c'B²)²: Q ≡ ±c'B²/2,
whose gcd with K = c'aB/2 leaves the even part 2c'B² as overflow (the same computation as Thm 1.1 with 1/4 ↦ 1/2). ∎
*The fibre picture (both cells).* Put x := c·E. Then W_n is **f_x(a, B) := 4na² − x·aB + B² = −E**, a value of the
principal form of discriminant Δ_x = x² − 16n. So every cell of {ES, ES^{(y,1)}, ES^{[2]}, k = 1 cap-2} is:
"for some x, the principal form of discriminant x² − 16n represents −E for a divisor E | x", the cell being read off
from x/E mod 4 and from B. For fixed (c, E) the solutions are finitely many orbits of SO(f_x)(ℤ) (GROWING_MUTE
Prop 1.2(b) for c ≡ 0; same proof for c odd), infinite as soon as one exists and Δ_x is not a square.
