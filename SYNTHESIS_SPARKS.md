# SYNTHESIS_SPARKS — cross-pollinating (J)1–(J)10 (task O171, SPARK synthesis)

**ES is not solved here.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts `scripts/syn_*`. Sources: DISCOVERIES (J)1–10 and the documents behind them (cited by short names:
INV = INVOLUTION_ES(2), BF = POINTWISE_BINARYFORM, FF = FUNCTIONFIELD_ES, WR = WINDMILL_REDUCTION,
PF = PARITY_FIXED_P, SA = STRONG_APPROX_ES, DE = DETERMINISTIC_EXISTENCE, DK = DEDEKIND_ES, GI = GROWING_IDENTITIES).

## 0. The common skeleton (Assessment, used to pre-screen every combination)

Every slice in (J)1–10 has the shape: an integer `N_θ(p)` linear in p with small coefficients (θ small), and a
certificate = a divisor of `N_θ(p)` in a class of `(ℤ/q_θ)^*` (q_θ = 4t, e, 4cd, …). Every document then finds the
same two layers:
* **sign layer**: by reciprocity, for a prime `ℓ | N_θ(p)` one has `(ℓ/p) = ψ_θ(ℓ)` for a quadratic character
  ψ_θ of conductor | 4q_θ (PF spin lemma; GI Prop 4.1: `(m''/n) = (−t/m'')`; DE Prop 3.4; DK Thm 4.5 where the
  sign becomes a mod-4 function of the HJ letters). The product of ψ_θ over the factorisation is
  `(N_θ(p)/p) = (j_θ/p)`, a single Legendre symbol of a small number. Group-level success is forced exactly when
  that symbol (and its higher-order analogue, DE Prop 6.2) is right.
* **class layer**: an individual divisor in the exact class; residue data never supply it (DE Prop 6.3, 7.2,
  Thm 7.3; WR Prop 10.3 / Remark 10.4).
At `n = m²` every sign is +1 (T1). So a deterministic mechanism must either (a) produce a class-layer witness
from structure, or (b) work purely in the sign layer *with a set large or structured enough that a non-residue is
forced*. The combinations below are sorted by which of (a)/(b) they aim at.

## 1. Cross-combinations (≥ 8), each with a sketch and a barrier pre-screen

**X1. HJ length-3 locus (DK Thm 4.5) × Conway rivers / Zagier cycles (WR §1).** The word `(v,t,u)` is the
reduced cycle of `γ = T^vST^tST^uS = [[p, −A*],[A, −t]]`, trace `s = p − t`, disc `s² − 4`; all classes of disc
`s² − 4` share the regulator `log s`, cycles are words with continuant-trace s, and the three rotations of one
length-3 cycle are words of the three numbers `s + b_i`. Class inversion = reversal `A ↔ A*`.
*Pre-screen.* Already closed in DK: reversal is fixed-point-free on L₃(p) (C3), and the sign is preserved by
rotations whenever both numbers are ≡ 1 (4) (DK 8.2), i.e. it is a conjugacy-class (genus-type) function of γ. So
no class-inverting involution has −1-words as fixed points at a prime, and rotations cannot transfer the sign.
*Modification tried here:* none promising; recorded as closed (DK C3 + 8.2), not attacked.

**X2. Ray class groups mod t (WR Remark 10.4) × function-field coverings (FF Thms 6.1–6.4).** In ray-class
language a Type I certificate is an ideal 𝔪 | (1+√−tp) whose Frobenius in `K(ζ_t)/K` is the element `σ_{−1}`
(N𝔪 ≡ −1 mod t), plus a 2-adic condition. FF succeeds in char 2, 3 because the bad class coincides with a trivially
solvable class and `T^q − T` confines irreducibles. *Pre-screen.* Chebotarev for the divisor hypercube of a single
δ = 1+√−tp is B2 (2^ω objects); the FF mechanism needs a characteristic accident absent over ℤ (FF §6 reading).
The large-q regime where FF has pointwise equidistribution (Bank–Bary-Soroker–Rosenzweig type) is exactly where
the expected count ≍ n³/q^k → 0 (FF Thm 2.1). Dead as a route; kept as a dictionary line.

**X3. Jacobi forcing (DE Prop 3.4) × SL₂ matrix dictionary (SA Lemma 10.1).** Group level: for prime e ≡ 3 (4)
with (p/e) = −1, a prime ℓ | N_e is a non-residue mod e, so `ℓ^{(e−1)/2·…} ≡ −1`. An "SL₂ orbit upgrade" would need
to realise a product `∏ ℓ_i^{γ_i}` with unbounded γ_i as a single divisor. *Pre-screen.* The e/(pN)=1/y+1/z
criterion allows only coprime `ab | N` (box, DE Prop 6.1); powers ℓ^γ with γ > v_ℓ(N) are not realisable
by any matrix in the double-coset set (SA Prop 10.2 has the same box). The upgrade is exactly DE's "exact
gap". **Attacked in §4 (A3)** via a different upgrade: changing the slice instead of the exponent.

**X4. GI Prop 4.1 (W = Σ_{D*}(1 − (m''/n))/2) × INV Prop 3.1 / WR §6 parity.** *Pre-screen.* Parity of W and of
every ≤2-literal sub-count is random (WR §6, DK C5: 283 + 820 sub-counts). W mod 2 ⟺ (S − O) mod 4; no closed form
for O. Closed by prior EVIDENCE; not attacked.

**X5. DE Thm 7.3 (block witnesses miss p ≡ 1 mod M_E) × DK Thm 4.5 × PF Lemma 1.2 (Type I is p-free up to one
congruence) × (J)1 hardness law.** Insight: `p ≡ 1 (mod M_E)` makes p *locally the square 1²* at every prime
≤ E; then every small prime is a QR mod p (n_p > E), and *both* Type I and Type II congruence witnesses die
together. Pre-screen: B5 predicts exactly this (congruence data cannot separate p from 1²). **Attacked in §2
(A1)**: (i) a joint Type I/II/HJ version of Thm 7.3, (ii) computation of what actually certifies these primes.

**X6. DK Cor 4.6 (λ(p) ≤ 3: a QNR in the Farey ball L_{≤3}(p), |L_{≤3}| ≍ log²p) × GRH least-non-residue scale
(Ankeny/Bach: a QNR ≤ 2 log²p) × index-2 subgroup argument.** Two sets of the same size log²p; Bach's set is an
interval of integers, DK's is a set of HJ words. A T1-safe sign-layer mechanism: "if L₃(p) ⊂ QR_p then its
multiplicative closure with squares is ⊂ QR_p (index 2); show the closure is too big". At m² the Jacobi-(+1) set is
everything, so the argument is vacuous there (T1-safe by construction). Pre-screen: needs multiplicative
*relations* mod p between ball elements and known QNR-rich sets; such relations come from factorisations of
shifted integers (B2/H-A). Bach's scale was noted in BRAINSTORM/noncounting_shapes. **Attacked in §3 (A2)**,
to locate precisely which input is missing.

**X7. PF spin lemma × GI Prop 4.1 × DE Prop 3.4 = one reciprocity, three slices (§0).** The "sign of a prime factor
of N_θ(p)" is ψ_θ(ℓ); `∏ψ_θ = (j_θ/p)`. Combination: choose the slice θ with `(j_θ/p) = −1` so that the sign layer
is forced *and* the slice is one where the sign layer is the *whole* certificate condition. Pre-screen: sign = whole
condition ⟺ (ℤ/q_θ)^* has exponent 2 ⟺ q_θ | 24 (DE Prop 6.3, WR Prop 10.3) — the B1 regime. Recorded as the
precise statement of why X3/X5/X6 cannot be done "for free"; it is the content of (J)10's unifying observation.

**X8. BF Thm 3.2′ (two-variable families, p = u²+v²) × DK C3 (Smith's palindrome converts √−1 into sizes).**
Smith's CF of p/A (A² ≡ −1) passes through (u,v). Candidates for short-HJ QNRs: Möbius images of √−1 with
coefficients from the CF of u/v (non-polynomial, so outside BF Thm 3.2′). Pre-screen: for p ≡ 1 (8), √−1 is a QR
(it is a 4th power iff p ≡ 1 (16)), so Möbius images `(a√−1+b)/(c√−1+d)` have sign `((a²+b²)(c²+d²)/p)`-type
values, i.e. congruence data in (a,b,c,d); the HJ length of the image is a lottery in the CF of u/v. Not attacked
(B3); recorded as a spark.

**X9. (J)1 units as universal divisors (real quadratic O_K, N(ε) = −1; ℤ[1/3]) × DE Jacobi forcing.** Over
ℤ[ε] every −1-class problem is solved by a unit. Over ℤ the only analogue of "a unit in the class −1" is a
divisor in the class −1, i.e. the class layer. Pre-screen: descent from O_K to ℤ by norms does not preserve the
unit-fraction shape (trace/norm of 1/x+1/y+1/z is not of that shape). Dead.

**X10. INV Thm 6.1(b) (Siegel cylinders) × DE Thm 7.3 × BF Cor 3.4′ — "all finite menus miss a positive-density
or infinite set".** Meta-combination: the three barriers are of one form (finite menu ⇒ misses an infinite,
often congruence-defined, set of primes). Their *union* is still a finite menu. The only uncovered menus are
p-dependent ones built from non-congruence data of p: CF of p/q, Cornacchia (u,v), the Euclidean path of √−1.
Recorded; X8 and A2 are the instances examined.

**X11. SA Thm 9.1 (fixed-level identities are quasi-polynomial at primes) × DK 8.4 (the signed sum
S(n) = Σ_{L₃(n)} (A/n) is a mod-4-weighted cubic count) × FF EVIDENCE (extinction of failures).** A T1-respecting
exact formula must vanish at squares; S(n) = N₊ − N₋ with N₋(m²) = 0 has growing level (sum over t ≤ n+2).
Pre-screen: H-A (DK C4). Not attacked.

**X12. Internal consistency audit (brief).** Cross-check of numerical/structural claims that two documents
state about the same object: GI's W(n) (Type I a = 1, t ≡ 3 (4) divisor form) vs DK's a₀(n) + boundary words;
DK Thm 4.5 cells vs INV2 Lemma 5.1 (odd parts of A, B, uv have Jacobi −1). **Done in §5.**

## 2. Attack A1 (X5): block witnesses are witnesses of the locally-equal square

Setting as DE §6–7. For a Type II slice e (e ≡ 3 (4), N_e(n) = (n+e)/4) and a bound Y ≥ every prime factor of e,
write `N_e(n) = s_Y(n)·P_Y(n)` with s_Y the Y-smooth part. A **Y-block witness** at (n, e) is a representation
`−1 ∈ Σ_e(s_Y(n))·{1, P_Y(n)^{±1}}` (the rough part used as one indivisible block). DE Prop 7.2 shows these are
exactly the witnesses that congruence/sharing data can certify; DE uses Y = (E+1)/4.

**Lemma 2.1 (transfer; PROVED, elementary).** Let n₁, n₂ be positive integers coprime to e, with `n₁ ≡ n₂ (mod 4e·∏_{ℓ ≤ Y} ℓ^{K_ℓ})`,
where `K_ℓ > v_ℓ(N_e(n₁)) + 2·[ℓ = 2]`. Then `s_Y(n₁) = s_Y(n₂)`, `P_Y(n₁) ≡ P_Y(n₂) (mod e)`, and n₁ has a Y-block
witness at e iff n₂ has one.
*Proof.* `4(N_e(n₁) − N_e(n₂)) = n₁ − n₂`, so `N_e(n₁) ≡ N_e(n₂) (mod ℓ^{K_ℓ − 2[ℓ=2]})`, hence equal ℓ-valuations
for ℓ ≤ Y (the valuation of N_e(n₁) is below the modulus exponent). So s_Y agree. N_e(n_i) is coprime to e (a prime
ℓ | e dividing N_e(n_i) divides n_i), so s is invertible mod e and `P_Y(n₁) ≡ P_Y(n₂) (mod e)` from
`N_e(n₁) ≡ N_e(n₂) (mod e)`. The block-witness condition depends only on (s_Y, P_Y mod e). ∎

**Lemma 2.2 (T1 for e-slices; PROVED relative to ET Prop 1.6, re-checked numerically in §2.4).** For odd m and every
e ≡ 3 (4) coprime to m, `−1 ∉ Σ_e((m² + e)/4)`. (A pair a ≡ −b (e), ab | N gives the Type II solution
`4/m² = 1/N + 1/(K/a) + 1/(K/b)`, `K = m²N(a+b)/e`, contradicting ET Prop 1.6 / BF Lemma 1.1.)

**Theorem 2.3 (square-mimic; PROVED from 2.1, 2.2).** Let Y ≥ 3 and p > Y a prime with p ≡ 1 (mod 8) and
`(ℓ/p) = 1` for every odd prime ℓ ≤ Y (equivalently, since p ≡ 1 (8): every n ≤ Y is a QR mod p, i.e. the least
non-residue n_p > Y). Then **for every Y-smooth e ≡ 3 (4) with e < p (of any size), slice e has no Y-block witness.**
*Proof.* p is a square mod every ℓ^K (ℓ odd ≤ Y, Hensel) and mod 2^K (p ≡ 1 (8)), so by CRT `p ≡ m² (mod 4e·∏ℓ^{K_ℓ})`
for some odd m, which we may take coprime to e (e | modulus and p ⊥ e). A Y-block witness at (p, e) would, by
Lemma 2.1, give one at (m², e), and a block witness is a witness (P_Y(m²) | N_e(m²) and is coprime to s_Y), contradicting 2.2. ∎

*Comparison with DE Thm 7.3.* DE's case is n₂ = 1 (p ≡ 1 mod M_E), with the size argument a + b < e in place of T1.
Thm 2.3 replaces the single class 1 mod M_E (density 1/φ(M_E) ≈ e^{−1.5E}) by **all square classes** mod the
Y-smooth modulus, i.e. by the Legendre condition n_p > Y (density 2^{−π(Y)} among primes ≡ 1 (8)), and it
covers every Y-smooth slice, not only e ≤ E. With Graham–Ringrose (n_p ≫ log p·log₃p i.o.; cited from memory,
and a version inside p ≡ 1 (8) is assumed), infinitely many primes have no block witness at any Y-smooth slice,
Y ≍ log p·log₃p, versus Y = c₀ log p (c₀ = 1/(1.5L)) from Linnik in DE Cor 7.4. **The same proof applies verbatim to
Type I slices** (divisor form `tn + 1 = m·m''`, m ≡ m'' ≡ −1 (t), 4 | m, t Y-smooth; level (c,d) with
`N = n² + 4c²d`, 4cd Y-smooth: transfer by n ↦ m² and T1 for Type I), and hence to all five HJ slices of DK Thm 4.5.

*Reading (Assessment).* "Congruence/sharing data" of p at a Y-smooth modulus are *literally* the data of a square
m² ≡ p, as soon as p is a QR mod every ℓ ≤ Y. This is B5 made exact at the level of witnesses, and it explains the
(J)1 hardness law (hardness grows with log L(1,χ_p), i.e. with how many small ℓ are QRs mod p): the more small
primes are QRs, the more of the witness space is square-equivalent. Every witness of such a p must either use a
slice modulus with a prime factor > Y, or split the Y-rough part of N_θ(p). This is the precise answer to the brief's
question (v) on the theory side.

**2.4 Checks (CERTIFIED as stated, `scripts/syn_square_mimic.py`).** Lemma 2.2: all 18 348 pairs (m odd ≤ 301,
e ≡ 3 (4) ≤ 600, gcd = 1): `−1 ∉ Σ_e((m²+e)/4)`, 0 violations. Thm 2.3: for primes p ≡ 1 (8), p < 10⁶, with
n_p > Y (Y = 5, 7, 11, 13: 4817, 2370, 1147, 541 primes), every Y-smooth slice e ≡ 3 (4), e ≤ 4000 (12–66 slices per
Y; 212 515 slice checks in total): 0 Y-block witnesses. **Control (EVIDENCE):** for primes p ≡ 1 (8) < 10⁶ with
n_p ≤ Y (first 3000 per Y), a Y-block witness at some Y-smooth slice e ≤ 4000 exists for 94.3 % (Y = 5), 100 %
(Y = 7), 99.5 % (Y = 11), 99.8 % (Y = 13). So in this range the presence of block witnesses at Y-smooth slices is
almost exactly the Legendre condition n_p ≤ Y: a sharp dichotomy.

**2.5 Novelty audit (Assessment; important).** Thm 2.3 is an instance of POINTWISE_SIZE Theorem C, unconditional
part ("FAIL at every admissible q of a square-mimicking point", (H)3), and of the Type I frame (H)9 (Lemma 8.1:
`ck_min(p) ≥ n_p`; Thm 8.5: `ck_min ≫ log p·log₃p` i.o., the Graham–Ringrose bound transported). What is new is
only the *cross-document* observation: **DE Thm 7.3 / Cor 7.4 (O168) did not use (H)9**. Its block-witness notion is a
congruence certificate in the sense of (H)3, so its Linnik scale `c₀ log p` (c₀ = 1/(1.5L), tiny) and density
1/φ(M_E) improve at once to the n_p scale (≫ log p·log₃p i.o.) and to density 2^{−π(Y)}, for Type I, Type II and
the five HJ slices together. This is a repair of DE's scope statement, not a new barrier. Its converse ("n_p ≤ Y ⇒ a
Y-smooth block witness") is the Mordell-covering question for non-residue classes. POINTWISE_MORDELL13–17D
studied it in depth: there is no finite covering of Σ_13 (open leaves at all computed depths), and sterile points are
conjectured in Σ_17. So the 2.4 control rates are a finite-range effect, and I do not pursue the converse.

## 3. Attack A2 (X6): a sign-layer (index-2) mechanism on the Farey ball — precise reduction (negative)

*Idea (T1-safe by construction).* Five-slice ES(p) ⟺ `L_{≤3}(p) ⊄ QR_p` (DK Cor 4.6). If the ball lay in QR_p, then
so would its multiplicative closure with the squares. So it would suffice to show that the closure has more than
(p−1)/2 elements, or that it contains a known non-residue. At n = m² the Jacobi-(+1) set is all of (ℤ/n)^*, so the
argument is vacuous there and B5 does not apply to it.

**Prop 3.1 (PROVED, elementary; the reduction).** For p ≡ 1 (4) and 2 ≤ A < p with A odd:
`A ∈ L₃(p) ⟺ c := (−p mod A) ≥ 2 and c | A + 1` (and then `p/A = [[⌈p/A⌉, (A+1)/c, c]]`), and for such A,
`(A/p) = (−c/A)`, which depends only on (A mod 8, c mod 8), because A ≡ −1 (mod c).
*Proof.* The HJ step gives `r(p/A) = 1 + r(A/c)`, and `r(A/c) = 2` ⟺ `A/c = [[x,y]] = (xy−1)/y` ⟺ `c = y | A+1`
(with y ≥ 2, x ≥ 2). Jacobi reciprocity (A odd, p ≡ 1 (4)) gives `(A/p) = (p/A) = (−c/A)`. Write c = 2^j c′, c′ odd:
`(−c/A) = (−1/A)(2/A)^j (c′/A)`, and `(c′/A) = ±(A/c′) = ±(−1/c′)` with the sign fixed by A, c′ mod 4 (A ≡ −1 mod c′).
So the symbol is a function of (A mod 8, c mod 8). ∎
(For even A use the same with the (2/p) = 1 convention when p ≡ 1 (8).)

*Consequence (Assessment, precise).* Each candidate A carries a sign that is congruence data of the letters, and its
membership in the ball is the event `p ≡ −c (mod A)` for one of the τ(A+1) divisors c. So "the closure contains a
non-residue" needs a multiplicative relation mod p between ball elements and a known non-residue q. Such a relation
is either a membership event of this kind (DK C6: A = q·k² ∈ L₃(p) forces t to be the unique residue −p⁻¹ mod qk²
dividing qk²+1, a 1-in-qk²/τ lottery) or a factorisation of a shifted integer (B2). Product-set growth cannot
replace it. The ball has only ≍ log²p elements, and a set of that size can lie in any index-2 subgroup; growth
theorems (Bourgain–Glibichuk–Konyagin type) need |S| ≥ p^δ. *Bach's scale coincidence* (GRH: a QNR ≤ 2 log²p, the
same size as the ball) is real but structural only in appearance. Bach's argument needs the full interval, through
the explicit formula for L(s, χ_p). The ball is a union over A of congruence events and is not the support of an
Euler product. **A2 reduces to B2/H-A; no sign-layer mechanism on the ball exists beyond DK's.**

## 5. Internal consistency audit (X12; CERTIFIED as stated, `scripts/syn_consistency.py 3000`)

* GI Prop 4.1's W(n) (Type I a = 1, divisor form over t ≡ 3 (4)) equals DK's interior count a₀(n) plus DK's v = 1
  boundary words (4.2), for all 749 n ≡ 1 (4) ≤ 3000 (0 mismatches). So the two documents' Type I slice counts agree,
  including GI's finiteness bound t ≤ n+2.
* GI §4 census reproduced: (class +1, class −1) = (19, 13) at p = 10009 and (26, 14) at 10177.
* INV2 Lemma 5.1 (for p ≡ 1 (8), the odd parts of A, B and uv all have Jacobi −1) holds on all 647 E(p)-points for
  p ≡ 1 (8), p ≤ 3000. It is consistent with DK Thm 4.5, of which its A, B part is the 4 | A slice.
* Scope inconsistency found (not a mathematical error): **DE Cor 7.4 understates its own barrier.** By §2 (an
  instance of (H)3/(H)9), block witnesses fail at every Y-smooth slice whenever n_p > Y, giving scale n_p
  (≫ log p·log₃p i.o.) instead of c₀ log p. Recommend a one-line cross-reference in DE §7.

## 4. What certifies the locally-square primes? (brief item (v); EVIDENCE, `scripts/syn_hard_witness.py`)

By Thm 2.3, a prime with n_p > Y has no block witness at any Y-smooth slice. Its witnesses must either use a slice
modulus with a prime factor > Y ("bigmod") or split the Y-rough part of N_e ("split"). Random primes p ≡ 1 (8)
near 10^L were sampled (seeded), with the Legendre filter applied before primality. For each, Type II slices e ≡ 3 (4)
were scanned upward to the first e with −1 ∈ Σ_e((p+e)/4).

| sample | first-witness e: median / 90 % / max | kind of first witness |
|---|---|---|
| p ≈ 10⁹, n_p > 19 (150 p) | 7 / 23 / 55 | split 131, bigmod 19 |
| control p ≈ 10⁹ (150 p) | 3 / 7 / 11 | split 150 (block witnesses included) |
| p ≈ 10¹¹, n_p > 23 (120 p) | 7 / 19 / 35 | split 120, bigmod 0 |
| control p ≈ 10¹¹ (120 p) | 3 / 7 / 11 | split 120 |

*Reading (Assessment).* What replaces block witnesses is not a new structure. It is the same lottery one level
down: N_e has typically 2–4 prime factors above Y, and a divisor pair *among the rough primes* lands in the class −1
mod a tiny e. Local squareness moves the first witness from e ≈ 3 to e ≈ 7 (median), and it moves it into rough
splits. It does not make the problem "large". So at these sizes the hardest primes are certified by the joint
factorisation of p+3, p+7, p+11, …, i.e. exactly by hatch H-A. No structured family (single private prime in the
class, Jacobi-forced slices) dominates: 87–100 % of first witnesses sit at Y-smooth slices, where Jacobi forcing
carries no information beyond the Legendre symbols that local squareness has already set to +1.

## 6. Verdict and ranking (Assessment)

* **No combination escapes the size layer.** Every one of X1–X12 lands on the same point: a divisor of a specific
  integer N_θ(p) in a class modulo a small parameter, with the sign layer already decided by one Legendre symbol (§0).
  The combinations differ only in which slice family they use and in whether their failure is forced on square classes.
* **Most informative outcome.** The two layers of §0 match the two halves of the campaign's barrier map exactly:
  (1) *sign layer.* Everything here is congruence data, and on Y-smooth slices it is literally the data of the
  locally-equal square m² ≡ p (Lemma 2.1 / Thm 2.3, an instance of (H)3/(H)9). It fails precisely when n_p > Y.
  (2) *class layer.* Here the data are joint factorisations of p+3, p+7, … (H-A). §4 shows that, at the sizes
  computed, this layer certifies even the locally-square primes at tiny slices.
* **Repair recommended.** DE Cor 7.4 should cite (H)9: the scale is n_p (≫ log p·log₃p i.o.), not c₀ log p (§2.5, §5).
* Ranking of the combinations by residual promise (0–5): X5/A1 1 (done; converse = Mordell sterile-point question);
  X6/A2 0 (reduced); X3 0 (exact gap = DE's); X1 0 (closed by DK 8.2); X2 0; X8 1 (p-dependent non-congruence menu,
  untested beyond WR §3's negative SQUFOF test); X10 1 (meta); X11 0; X4 0; X7 0 (meta); X9 0.

## 7. Sparks (not pursued)

1. **Square-mimic depth as a hardness coordinate.** Define d(p) = the largest Y such that p ≡ □ mod every prime power
   ≤ Y (≈ n_p). §4 suggests e_min(p) grows only slowly in d(p). A precise law (e_min against d(p) and log p) would
   calibrate the (J)1 hardness law mechanistically.
2. **Rotation packets (DK 8.2).** The sign is constant on a length-3 cycle class across its rotations that are ≡ 1 (4).
   So a square m² = s + b_i kills the certificate property of its cycle-mates s + b_j. Spark: count "square-poisoned"
   cycles of a prime p. This is a fully explicit, T1-aware deficit term, possibly the exact correction between
   sign-blind counts and certificate counts.
3. **Char-2 reading of T1.** In F₂[T], squaring is bijective on every residue ring, so there is no quadratic
   character and the sign layer is empty; this is why FF's coverings close. One could ask whether some other
   characteristic-free ring (e.g. ℤ[1/3], where (J)1 has positive ES for all n) owes its success to the same
   emptying of the sign layer.
4. **Smith-path menu (X8).** Test whether HJ data along the Euclidean path of (p, √−1 mod p) are enriched for
   five-slice certificates. Prior evidence (WR §3, SQUFOF) suggests not.
5. **Composite inheritance in the "good" direction (DK 8.3).** ES(p) ⟸ some a ≡ 3 (4) and a word [[av′, t, au′]]
   of ap with Jacobi symbol +1 mod ap. Check whether such non-certificate words of ap are forced (e.g. by a sign-blind
   count at ap exceeding the certificate count).
