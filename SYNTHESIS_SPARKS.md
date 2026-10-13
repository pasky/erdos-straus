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
