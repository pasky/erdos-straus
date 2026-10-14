# CAP_TWO — the e = 2 cell at k = 1 and its relation to ES^{[2]} (task O214, spark relay Y6)

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
differ only in the residue of c mod 4 (Thm 1.2). Consequence: the per-slice contrast of O204 between
e ≤ 1 and e = 2 on the slice k = 1 (finite vs no wall seen) is a slicing effect (§2): ES^{[2]} with k free and cap-2 at k = 1 are the two halves of one
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
* c ≡ 2 (mod 4): forces 2 | a (g ≡ 3 mod 4); not used here.
*Proof.* c ≡ 0: GROWING_MUTE Prop 1.1(c) is "g | nA_GM² + B², g ≡ −1 (mod 2A_GM B)" with A_GM even; put A_GM = 2a,
then 2A_GM B = 4aB and g + 1 = 4λ·aB. c odd: Thm 1.1. c = 2c': g ≡ 3 (mod 4) needs 4 | 2c'aB. ∎
*The fibre picture (both cells).* Put x := c·E. Then W_n is **f_x(a, B) := 4na² − x·aB + B² = −E**, a value of the
principal form of discriminant Δ_x = x² − 16n. So every cell of {ES, ES^{(y,1)}, ES^{[2]}, k = 1 cap-2} is:
"for some x, the principal form of discriminant x² − 16n represents −E for a divisor E | x", the cell being read off
from x/E mod 4 and from B. For fixed (c, E) the solutions are finitely many orbits of SO(f_x)(ℤ) (GROWING_MUTE
Prop 1.2(b) for c ≡ 0; same proof for c odd), infinite as soon as one exists and Δ_x is not a square.
*Check (`scripts/y6_dict.py 61 401 40`, exact rationals, Def 1.1 checked prime by prime):* all 120 k = 1 cap-≤2 shots
(odd n ≤ 61, odd Q₁ ≤ 401, all divisors) map to W_n points with 4 | a, E ≡ 3 (mod 4); conversely all W_n points with
a, B ≤ 40 give exact solutions: 121 with c odd (den z = c²B⁴, cap ≤ 2) and 179 with c ≡ 0 (mod 4) (ES^{[2]}, den z = B²);
no violation of "E ≡ 3 ⟺ 4 | a" among c-odd points.

## 2. Slices are finite, orbits are infinite: the O204 "transition" is k fixed vs k free

**Proposition 2.1 (PROVED).** Let n > 1 be odd and consider W_n with c odd (all side conditions of Thm 1.1 except
squarefreeness are irrelevant here).
(a) (fixed a) If 4 | a then every point has B ≤ 8na², E ≤ 4na² + B², c ≤ (4na² + B² + E)/(aBE): finitely many.
(b) (fixed B) Every point has c ≤ (4n + 1)(B² + 1)/B, and for fixed B there are finitely many points.
(c) (fixed (c, E), i.e. fixed x = cE) If Δ_x = x² − 16n is not a square, the points form finitely many orbits of the
automorph group of f_x; if one point satisfies the conditions of Thm 1.1 then infinitely many points of its orbit
satisfy all of them **except possibly "B squarefree"** (a, B → ∞ along the orbit).
*Proof.* (a) B-Vieta: B' := caE − B = (4na² + E)/B is a positive integer, B + B' = caE ≥ 4E, BB' = 4na² + E.
If B ≥ B' then B ≥ caE/2, so E ≤ 2B/(ca) and B ≤ BB' ≤ 4na² + 2B/(ca), i.e. B ≤ 4na²/(1 − 2/(ca)) ≤ 8na² (ca ≥ 4);
if B < B' then 2E·B ≤ (B + B')B... precisely B² < BB' = 4na² + E and B' ≥ caE/2 ≥ 2E give B ≤ (4na² + E)/(2E) ≤ 2na² + 1.
The rest is read off W_n (E·g = 4na² + B² with g ≥ 1). (b) a-Vieta: t := cBE − 4na = (B² + E)/a is a positive
integer (product of roots (B² + E)/(4n) > 0 and sum cBE/(4n) > 0, so cBE − 4na = 4n·(other root) > 0), with
a·t = B² + E. Put m := E = at − B² ≥ 1; then c = (4na + t)/(Bm) ≤ (4n + 1)(B² + m)/(Bm) ≤ (4n + 1)(B² + 1)/B, using
a, t ≤ B² + m. For fixed (B, c): substituting E = at − B² gives a(cBt − 4n) = t + cB³, so cBt > 4n and
t(cB − 1) ≤ cB³ + 4n (from a ≥ 1) bound t (if cB = 1: t − 4n | 4n + 1), hence a and E. (c) As GROWING_MUTE Prop 1.2(b):
f_x has automorphs of infinite order; those ≡ identity modulo 4cn (a finite-index subgroup) preserve a mod 4,
B mod c, gcd(caB, n) = 1 and (squaring if needed) the positive branch; E ≡ 3 (mod 4) and B odd are forced by
f_x(a, B) = −E with x odd. Squarefreeness of B is not a congruence condition. ∎
*Reading (Assessment, built on Thm 1.2 + Prop 2.1).* O204 Cor 3.2 / §3 table: "k = 1: ES^{(y,1)}, ES^{[2]} finite;
e = 2 no wall". In W_n-coordinates ES^{[2]}'s k is the coordinate a, while the k = 1 cap-2 cell has a free. So the
k = 1 slice of ES^{[2]} is the line a = 1 of the c ≡ 0 half, but the k = 1 slice of the cap-2 cell is the WHOLE c-odd
half. The per-slice contrast "k = 1 slice finite at e ≤ 1, no wall at e = 2" is "one line vs a whole half-surface".
(Calibration, R210: no cap is shown to be a global finite search; ES^{(y,1)} and ES^{[2]} have finite slices but an
unbounded band of (k, Q₁), and bounded cap with growing S remains OPEN, R200 M1.) Taken with
k free, ES^{[2]} has the same structure: every slice is finite (O204 Thm 2.1) and the Pell orbits are infinite. So the
two problems are of one kind: **does some fibre x of the conic bundle f_x(a, B) = −E (E | x) have a point,
with x/E odd (cap-2, k = 1) or x/E ≡ 0 mod 4 (ES^{[2]})?** Neither is easier on structural grounds; for e = 2 the
squarefreeness of B along an orbit is an extra problem that ES^{[2]} does not have.

## 3. Numerics (EVIDENCE)

`scripts/y6_cover.py 1000000 1000000 primes` (AP marking: for each admissible (a, B, c) with g = caB − 1 ≤ 10⁶, W_n
holds iff n ≡ −B²(4a²)^{−1} (mod g); 4 614 210 triples; 47 s, 0.7 GB) and the independent exact re-check
`scripts/y6_verify.py 1000000` (exact rationals, Def 1.1 prime by prime):
* **every prime 3 ≤ p < 10⁶ has a k = 1 cap-≤2 shot with g ≤ 10⁶** (78 497 verified). Least g by decade
  (1–9, 10–99, …): 45 812 / 25 462 / 6 179 / 962 / 79 / 3; the largest least g is 955 979 at p = 379 (4·379 + 1 =
  37·41 has no factor ≡ 3 mod 4, so no ES k = 1 shot). The least shot needs B > 1 (exponent exactly 2) for 13 402
  primes; for p ≡ 1 (mod 4): 26 858 ES k = 1 shots (c = B = 1), 5 618 with B = 1 < c, 6 699 with B > 1.
* T1 control: none of the 499 odd squares ≤ 10⁶ is covered (as forced: E ≡ 3 mod 4 divides 4m²a² + B²).
* Composites: 8 703 odd non-squares ≤ 10⁶ are not covered within g ≤ 10⁶, 8 535 of them divisible by 3 (gcd(caB, n) = 1
  excludes 3 from the parameters and forces g ≡ E ≡ 1 mod 3); not pursued (composites are not the target; reduction to
  a prime factor needs the mute primes prime to the cofactor).
*Caution.* The least-g of p = 379 being within 5% of the search limit shows the k = 1 cap-2 lottery has a long tail even
for small p; nothing here bounds g in terms of p.

## 4. The D-face: an ES-shaped normal form and a box criterion

**Theorem 4.1 (PROVED).** Let n > 1 be odd. k = 1 cap-2 shots correspond bijectively (via Thm 1.1) to positive
integers (a, w, B, c) with
`  a·(cBw − 4n) = w + cB³,     D := cBw − 4n ≡ 3 (mod 4),`
plus the side conditions of Thm 1.1 (c, B odd squarefree coprime, gcd(caB, n) = 1). Here D = (4n + Q₁²)/g is the
duality cofactor of EXPONENT_CAP Prop 1.3 (k = 1), w = (4na + cB³)/g, E = aw − B², g = caB − 1, Q₁ = cB²; and
D ≡ 3 (mod 4) ⟺ 4 | a. Equivalent forms:
(i) **D := cBw − 4n > 0, D ≡ 3 (mod 4), D | w + cB³** (then 4D | w + cB³ automatically and a := (w + cB³)/D);
(ii) (**box criterion**) D ≡ 3 (mod 4), gcd(D, n) = 1, and a factorisation D + 4n = c·w·B with **(w/B)² ≡ −4n (mod D)**;
(iii) (**fixed-modulus tests**) for some (c, w): **64n³ + c²w⁴ has a divisor D ≡ −4n (mod cw) with D ≡ 3 (mod 4)**, gcd(D, ncw) = 1
(then B := (4n + D)/(cw)).
*Proof.* From Thm 1.1: w := (4na + cB³)/g is an integer since caB ≡ 1 (mod g) gives a(4na + cB³) ≡ 4na² + B² ≡ 0 and
gcd(a, g) = 1; then a·w·g = 4na² + caB³ = 4na² + B² + B²g = (E + B²)g, so aw = E + B². W_n multiplied out with
E = aw − B²: caB(aw − B²) = 4na² + aw, i.e. a(cBw − 4n) = w + cB³ (divide by a). D := cBw − 4n: D·g = (cBw − 4n)(caB − 1)
and, using a(cBw − 4n) = w + cB³, D·caB = cB(w + cB³) = cBw + c²B⁴, so D·g = cBw + c²B⁴ − D = 4n + c²B⁴ = 4n + Q₁².
Conversely a(cBw − 4n) = w + cB³ with a, w, B, c > 0 gives E := aw − B² and W_n by reversing the computation, and
E·g = 4na² + B² > 0 gives E > 0. Mod 4 (c, B, w odd since cBw = D + 4n is odd): w + cB³ ≡ w + cB and cBw ≡ D, so
a·D ≡ w + cB (mod 4); if D ≡ 3 then w ≡ 3cB, w + cB ≡ 0, so 4 | a·D, 4 | a; if 4 | a then w ≡ −cB, D ≡ cBw ≡ −1.
(i) is a restatement; "4D | w + cB³" by the mod-4 computation. (ii) cwB ≡ 4n (mod D) and gcd(w, D) = 1 (a common prime
divides 4n and D, impossible as gcd(D, 2n) = 1) give: w + cB³ ≡ 0 ⟺ w² ≡ −cwB³ ≡ −4nB² (mod D) ⟺ (w/B)² ≡ −4n.
(iii) with B = (4n + D)/(cw): B ≡ 4n/(cw) (mod D) and w + cB³ ≡ 0 ⟺ (×c²w³) c²w⁴ + 64n³ ≡ 0 (mod D). ∎
*Check:* `scripts/y6_dict.py 61 401 40` re-derives w, D from every c-odd W_n point and asserts a·D = w + cB³,
aw = E + B², D·g = 4n + Q₁², D ≡ 3 (mod 4), D | w² + 4nB² (121 points).
*Comparison with ES (FIXED_MODULUS_SHOTS (J)25).* ES Type II: 4cdj − 1 | pj + c, box criterion −p ∈ {c/j : cj | (h+1)/4}
(mod h) with h = O(p²) (a finite search). Here: target ±2√(−n) (mod D), box {w/B : wB | D + 4n}, and **D is unbounded**
(test (iii) with w → ∞). The pure-square cell c = 1 is "a(Bw − 4n) = w + B³": ES's Type II normal form
k(4ab − n) = a + b (O204 Prop 1.1, Q₁ = 1) with n ↦ 4n and one summand cubed. ES k = 1 is c = B = 1: D | 4n + 1.
*Example (test (iii), (c, w) = (1, 1)): every divisor D ≡ 3 (mod 4) of 64n³ + 1 = (4n + 1)(16n² − 4n + 1) gives the
shot Q₁ = (4n + D)², g = (4n + Q₁²)/D (a polynomial identity; a k = 1 cap-2 shot iff B = 4n + D is squarefree and
prime to n, which holds e.g. for n = 13, D = 7: B = 59, g = 1 731 059 = (52 + 59⁴)/7).* Such fixed (c, w) tests are
covering-type (B1: finitely many of them never cover a non-residue class); the content is in letting (c, w) grow.
T1: at n = m², D ≡ 3 (mod 4) would divide w² + (2mB)², a sum of two coprime squares (after removing gcd(w, B), which is
prime to D) — impossible. This is the only place T1 enters, in every face.

## 5. The exact place where the k = 1 slice stops being finite

**Proposition 5.1 (PROVED).** Let n > 1 be odd and T a set of odd primes. Consider k = 1 shots whose overflow Q₁ has
v_ℓ(Q₁) ≤ 2 for all ℓ, v_ℓ(Q₁) ≤ 1 for ℓ ∉ T (exponent 2 allowed only on T) and rad Q₁ | Q₀.
(a) If T is finite, there are finitely many such shots; explicitly Q₁ = cB² with B | ∏T and c ≤ (4n + 1)(B² + 1)/B.
(b) If T is all primes (the cap-2 cell) and one shot exists whose W_n-orbit (Prop 2.1(c)) contains infinitely many
squarefree B, there are infinitely many, with Q₁ → ∞.
(c) For comparison (O204): exponent ≤ 1 everywhere (T = ∅) gives the sharper Q₁ ≤ (16n + 1)/3; unbounded exponents on a
fixed finite S (ES^{(y)}, no squarefreeness) give an infinite k = 1 slice for non-square n with gcd(n, 15) = 1 (O204
Prop 3.1(a), |S| ≥ 4).
*Proof.* (a) B is a squarefree product of primes of T: finitely many; Prop 2.1(b) for each. (b) Prop 2.1(c). ∎
*Reading.* On the slice k = 1 the infinite direction is exactly "B unbounded", i.e. **exponent 2 at infinitely many
primes**; any finite exponent-2 budget keeps the slice finite. "e = 1 + ε" variants (exponent 2 on a fixed finite set,
or on primes ≤ a fixed bound) are therefore still finite on this slice. Bounded cap with unbounded exponent-2 support is
the first point where the slice is infinite — conditionally on (b)'s squarefree hypothesis, which is a Wieferich-type
statement about a binary recurrence and is open.

## 6. The real layer: class groups of x² − 16n (same as MARKOFF_ES §6 for ES^{[2]})

**EVIDENCE (`scripts/y6_fibres.py 3000 13 379 1009 9 25`; every reported fibre comes with an explicit point
f_x(ha, hB) = −E found as a CF convergent value, exact integers).** Odd fibres x ≤ 3000 (gcd(x, n) = 1, c = x/E ≥ 3)
carrying a c-odd W_n point (side conditions on (a, B) not imposed):
`  n = 13: 197 fibres   (per octave of x, bits 5..12: 1, 4, 2, 10, 16, 26, 73, 65)`
`  n = 379: 90 fibres   (bits 8..12: 3, 6, 14, 33, 34)`
`  n = 1009: 165 fibres (bits 8..12: 10, 14, 27, 58, 56)`
`  n = 9, 25 (T1): 0`
So a positive proportion (≈ 5–15%) of fibres carry points, while the shot search of §3 sees only a handful of shots per
n (n = 13: 4 shots with g ≤ 10⁶, n = 379: 1, `scripts/y6_count.py`). The reason: the points are deep in long CF
periods, e.g. n = 379, x = 161, E = 23: (a, B) = (8 207 552, 1 238 990 989), g ≈ 7·10¹⁶ (B squarefree, a valid
shot); n = 13, x = 33, E = 11: (267 468, 443 777), g ≈ 3.6·10¹¹. Fixing E and varying c (`scripts/y6_fixE.py 13 E 301`;
explicit points: `scripts/y6_pt.py n x E`): n = 13, E = 7: 18 of 118 admissible c ≤ 301 carry a point, all with 3 | c — the
genus layer: p = 3 has (13/3) = 1, (−7/3) = −1, so the prime 3 must not divide Δ = 49c² − 208 to first order, forcing
c ≡ 0 (mod 3); E = 11: 61 of 125; E = 19: 23 of 131 (again 3 | c); n = 379, E = 23: 16 of 72 (c ≤ 151). ("no" counts are
upper bounds when Δ ≤ 0 or E ≥ √Δ/2, where the scan is not complete; the "yes" points are explicit.)
*Assessment.* The c-odd half has exactly the two-layer structure MARKOFF_ES §6 found for ES^{[2]} (c ≡ 0 mod 4):
a local (genus) layer, a half-dimensional sieve condition on x, and a global layer "the ideal of norm E is in the
narrow class of negative-norm principal ideals of ℤ[(x + √(x² − 16n))/2]", which holds with probability bounded
below (Cohen–Lenstra; large regulators). So the e = 2, k = 1 cell is NOT a polylog lottery: like ES^{[2]} (O202
Prop 6.1(a)) it has a polynomially large heuristic main term in the fibre count, and solutions of size exp(x^{1−o(1)}).
The residual statement, **"for some odd x and some E ≡ 3 (mod 4), E | x, the split ideal of norm E is narrowly
principal with a negative-norm generator in the order of discriminant x² − 16n"**, is a class-group statement in a
quadratic family of real quadratic orders: no unconditional technique proves it (MARKOFF_ES Prop 6.1(c)). On top of
it the cap-2 cell needs B squarefree at some orbit point (Prop 2.1(c)), which ES^{[2]} does not need.
Families x ≡ 0 (mod 4n) would be Richaud–Degert (explicit short CF) but are excluded: x odd here (and the RD
subfamily of ES^{[2]} is killed by reciprocity, GROWING_MUTE Prop 1.2(c)). (Schinzel's criterion for bounded CF periods of √f(x) along
progressions suggests no bounded-depth family exists for odd x; not re-derived here, Assessment.) The
proof of MARKOFF_ES Thm 5.1 (units of y² = μ² − n over ℚ[s]) applies verbatim with μ = x/2 to rule out polynomial
families (a(s), B(s), c(s)) with c non-constant at fixed E, n non-square (PROVED by that argument: η = (x + √f)/2,
f = x² − 16n, has constant norm 4n, α = B − aη has norm −E; R* = ℚ*×⟨ε⟩; b odd forces N(α) > 0, b even forces 4n square).

## 7. Verdict (O214 checkpoint 1)

1. **Dictionary (Thm 1.1, 1.2, PROVED, checked).** k = 1 cap-2 shots ⟺ 4na² + B² + E = c·a·B·E with c odd
   (Q₁ = cB², g = caB − 1, 4 | a ⟺ E ≡ 3 mod 4). The same equation with c ≡ 0 (mod 4) is GROWING_MUTE's ES^{[2]} (A, B)
   form (k = a, Q₁ = B). Both are "the principal form of discriminant x² − 16n represents −E for some E | x"
   (x = cE), the cell read off from x/E mod 4. ES = {B = 1, 4 | c}; k = 1 ES^{(y,1)} = {B = 1, c odd}.
2. **Slices vs orbits (Prop 2.1, 5.1, PROVED).** Fixed a or fixed B: finite (c ≤ (4n + 1)(B² + 1)/B). Fixed (c, E):
   Pell orbits. The k = 1 slice is infinite exactly when exponent 2 is allowed at infinitely many primes (B unbounded);
   any finite exponent-2 budget keeps it finite. O204's per-slice contrast (k = 1: e ≤ 1 finite, e = 2 no wall) is
   "the line a = 1 of one half vs the whole other half" of the same equation — no cap is shown to be a global finite
   search (R210).
3. **D-face (Thm 4.1, PROVED).** a(cBw − 4n) = w + cB³, D = cBw − 4n ≡ 3 (mod 4): ES's Type II normal form with n ↦ 4n
   and one summand cubed; box criterion ±2√(−n) ∈ {w/B : wB | D + 4n} (mod D), D unbounded; fixed-modulus tests
   "64n³ + c²w⁴ has a divisor ≡ −4n (mod cw), ≡ 3 (mod 4)". T1 enters only as "D ≡ 3 (mod 4) cannot divide a sum of two
   coprime squares".
4. **EVIDENCE.** Every prime 3 ≤ p < 10⁶ has a k = 1 cap-2 shot with g ≤ 10⁶ (exact re-verification; no odd square has
   one); positive proportion of fibres x ≤ 3000 carry points, at heights up to 10¹⁷ (§6).
5. **Negative calibration (Assessment).** ES^{(y,2)} at k = 1 is NOT a new easier target: its existence problem is the
   class-group layer of MARKOFF_ES §6 (now in the odd discriminants x² − 16n) plus a squarefree-B layer on a Pell orbit
   (Wieferich-type, open). Brief ideas: (a) explicit infinite candidate family — yes (tests (iii), Pell orbits), but
   firing is a class-group/lottery event; (b) DFI root equidistribution acts at scale ≫ 1/D, the box is D^{o(1)} (B3);
   (c) the R ↔ s symmetry is a ↔ B with n ↦ 1/(4n) weights, not an involution of W_n; (d) GRH does not touch the box
   or the class layer; (e) answered on the k = 1 slice by Prop 5.1. No proof of ES^{(y,2)}; no infinite case of ES.
