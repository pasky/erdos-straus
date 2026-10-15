# SYNTHESIS_SPARKS6 — cross-combinations of wave Z ((J)57–(J)66) (task O238, synthesis VI)

Status: O238 checkpoint 1 (unreviewed). **ES is not solved here, and no infinite case of ES for primes is claimed.** Labels as in
DISCOVERIES.md. Memos `BRAINSTORM/s6_*.md`; scripts `scripts/s6_*`.

## 0. Iteration log
(I1) Mandatory (ii) "force the budget v_s(x) large": the cleanest forcing of a large budget is algebraic, not congruential —
on the exponential family n_s = 4^s + k the window m_j = 4^j − k gives x = K = 4^{j−1}(4^r + 1), r = s − j, whose 2-part
(budget 2j − 2) and cyclotomic/Aurifeuillean factors G_e = 4^{r/e} + 1, A± are forced for every s. Their residues mod m_j
are periodic in r, so each choice (j, e, i, pair) is an *exponential class*: a congruence condition on s, but NOT a
fixed-modulus ET class (the divisor d of K grows with s). → §1.
(I2) Barrier screen: EXPONENT_COVERING Thm 1.4 ("covering by ET + divisor classes exists iff the limit set avoids the
sterile set") has the hypothesis *classes with fixed moduli*. Exponential classes violate it. Test case: (J)62's open
offset k = 105, Mordell-hard for every s, whose adaptive ET covering stalled at uncovered Haar measure 8.5·10⁻⁸ around
the "mixed points". → one exponential class closes it (§1, Thm 1.1).
(I3) The same driver on k = 33, 273, 297 (j ≤ 8, e ≤ 45) does NOT close (residual densities 9·10⁻⁵, 7·10⁻⁷, 6·10⁻⁷ when
no candidate is left): the window menu 4^j − k is too thin there (§1.4).
(I4) Mandatory (i)/(iii)/(iv)/(v) and further cross-combinations: memos §2.

## 1. ES for every n = 4^s + 105 (deep item 1)

**Lemma 1.0 (the exponential class; PROVED, symbolic).** For every integer u ≡ 32 (mod 151) put n := 256u³ + 105 and
`  x = 64(u³ + 1),   A = (64u³ + 2u² − 2u + 66)/151,   y = nA,   z = 32n(u + 1)A.`
Then A ∈ ℤ_{>0} and 4/n = 1/x + 1/y + 1/z.
*Proof.* 4x − n = 151, so 4/n − 1/x = 151/(nx). And 1/(nA) + 1/(32n(u+1)A) = (32u + 33)/(32n(u+1)A); equality with
151/(64n(u³+1)) is 2(32u + 33)(u² − u + 1) = 151A, i.e. 64u³ + 2u² − 2u + 66 = 151A (expand). For u ≡ 32 (mod 151):
64·32³ + 2·32² − 2·32 + 66 = 2 099 202 = 151 · 13 902, and A is a cubic, integer-valued on 32 + 151ℤ (checked by forward
differences). Positivity is clear for u ≥ 1. ∎
*Origin.* This is CAP_DOWN Lemma 1.1 at the window m = 151 = 4⁴ − 105 with x = K, d = K·d₁/d₂, d₁/d₂ = 2⁻⁵/(u + 1),
u + 1 = 4^{r/3} + 1 the cyclotomic factor G₃ of 4^r + 1 (u = 4^{r/3}); cap 0 because 2⁵ | K = 64(u³+1) and (u+1) | u³ + 1.
The class condition 32(u + 1) ≡ −1 (mod 151) is u ≡ 32.

**Lemma 1.0′ (which exponents; PROVED).** If s ≡ 34 (mod 45) then 3 | s − 4 and u := 4^{(s−4)/3} ≡ 32 (mod 151), so
n_s = 4^s + 105 = 256u³ + 105 lies in Lemma 1.0's family. *Proof.* ord₁₅₁(4) = 15 and (s − 4)/3 ≡ 10 (mod 15); 4¹⁰ ≡ 32
(mod 151). ∎

**Theorem 1.1 (PROVED, computer-assisted; certificate + independent checker).** ES holds for every n = 4^s + 105, s ≥ 0.
*Proof.* (a) The 13 ET/divisor classes of `data/s6_cert105_et.json` (moduli 11, 13, 19, 39, 41, 143, 151, 527, 1271; produced by
`scripts/s6_cert105_make.py`, i.e. exactly (J)62's z8 seeding at L₀ = 360, Mmax₀ = 2000, certificates by `ec_cover.certificate`)
are polynomial ES identities in n, integer-valued and positive on their residue classes n ≡ r (mod M), with
4^{360} ≡ 1 modulo the odd part of every M. They cover every residue s mod 360 except s ≡ 34 (mod 90) (for s ≥ 64).
(b) s ≡ 34 (mod 90) implies s ≡ 34 (mod 45): Lemmas 1.0/1.0′.
(c) `scripts/s6_cert105_check.py` re-verifies (sympy, not the z8 checker) every class identity, integer-valuedness, positivity
(n ≥ 4⁴), the periodicity hypothesis, coverage of all s mod 360 by (a) ∪ (b), the exponential identity, and builds and checks
an exact solution 4xyz = n(xy + yz + zx) for every s ≤ 1500 (s ≤ 3 included; no brute force was needed). ∎
*T1 control.* The ET non-divisor classes are z8 classes (non-square classes by (J)62's checker). The exponential class is
not a congruence class in n (n ≡ 59 (mod 151) is a residue), but it contains no square: a square n with a cap-0 window
solution at m = 151 contradicts CAP_DOWN §3 (T1 for Lemma 1.1); numerically 256u³ + 105 is not a square for
u = 32 + 151t, t < 2·10⁵. (The curve a² = 256u³ + 105 has finitely many integral points; 4⁴ + 105 = 19² is u = 1.)
*Scope (honest).* A thin (O(log X) members up to X) Sierpiński-type family; nothing about ES for primes follows. It
answers (J)62's open k = 105 (OPEN → PROVED) and shows that the "mixed points" stall was a class-menu artefact.

**1.2 Reading: mixed points are cube roots (Assessment + PROVED dictionary).** (J)62 located the obstruction at the mixed
point μ* ("4 in every ℓ-adic component except ℓ = 3, where μ* = −2"). The exponential class is exactly the
neighbourhood μ ≡ μ* (mod 45) (μ* ≡ 4 (mod 5), ≡ −2 ≡ 7 (mod 9)), and its parameter u = 4^{(s−4)/3} is the 3-adic
datum: on 3 | s − 4 the family is the CUBIC polynomial family n = 256u³ + 105 in u, on which the square-plus-constant
obstruction of NEAR_SQUARE Thm 2.2 (Z_k^□, polynomial families in m on n = m² + k) does not apply as stated: n = m² + 105
with m = 16u^{3/2}, not a polynomial in u (Assessment: whether Thm 2.2's witness argument extends to such sub-families was not
examined; the identity itself is unconditional). So: **fixed-modulus
classes see n_s only through n_s mod M; exponential classes see the algebraic factorisation of K = (n_s + m)/4, which is
periodic in s but not a function of n_s mod any fixed M.** This violates the hypothesis of EXPONENT_COVERING Thm 1.4 and
of the (J)22/(J)62 sterility criterion; sterility of a profinite point is a property of the class menu.

**1.3 What did NOT work (EVIDENCE).** Exponential classes alone (j ≤ 7, e ≤ 45, divisor classes l < 2·10⁵) cover only 79 % of
s mod 4 754 520 (`s6_cover105.py`); the theorem needs the ET classes for the rest. The closing class is the single
(j = 4, e = 3) class; it covers all of (J)62's residual exponents s ≡ 124 (mod 360), 844 (mod 2520) (`s6_expclass_pts.py`).

**1.4 Other open offsets (EVIDENCE, negative at this menu).** `s6_hybrid105.py k 360 2000 20000 LCAP 8 45`: k = 33 stalls at
density 9·10⁻⁵ (L ≈ 1.2·10⁹), k = 273 at 7·10⁻⁷, k = 297 at 6·10⁻⁷ (no candidate with growth ≤ 60). The window family
4^j − k and the factors of 4^r + 1 are the only algebraic input used; Sophie-Germain/Aurifeuille shapes 4^r + 4w⁴ and Type I
exponential classes are untried (spark).

## 2. The mandatory cross-combinations (memos `BRAINSTORM/s6_*.md`)

| item | memo | result | label |
|---|---|---|---|
| (i) mute set × Fano | s6_unique_forced_cap0 | the forced bit gives cap 0 for every K only when (ℤ/m)^* is 2-elementary, i.e. m = 3 (Mordell's n ≡ 2 (3)); the window analogue of "4 costs zero" is U = 1 | PROVED |
| (i) mute set × pigeonhole | s6_divisor_pigeonhole | \|P\| > (q−1)/2 ⟹ cap 0 (P = divisors of K mod q); structure-free versions need Ω(K) ≳ q/4 (Cauchy–Davenport, sharp); ±-weighted zero-sum theory only yields the trivial relation | PROVED + EVIDENCE |
| (i) × numerators | s6_numerator_windows | self-generated mute set works for every ν/n; window-shape T1 at odd squares for 4 \| ν, ν ≡ 3 (4), ν = □ (strictly more than (J)46's 4 \| ν) | PROVED (only-if) |
| (ii) forced budget | s6_exp_classes_105 (+ §1) | algebraic forcing on 4^s + k; **ES for all 4^s + 105** | PROVED (computer-assisted) |
| (iii) windows × words | s6_witness_onesided | cap-0 window = c-fibre word with m = (u+v)/c; the forced character is sufficient for some cap, not necessary for cap 0 (cap-0 rates 34 % vs 18 %) | PROVED obs. + EVIDENCE |
| (iv) 𝒟_e(M) × windows | s6_ydual_windows | 𝒟_e(M) is the y-window (fixed mute set, almost-all side); x-window is self-generated (pointwise side); boundary = who owns the mute set | PROVED dictionary |
| (v) sterility theory | s6_mixed_points_cuberoots | sterility is menu-relative; the 105 mixed point is a cube-root (3-adic) phenomenon resolved by the cyclotomic factorisation of 4^r + 1, the ℤ shadow of the FF root-product (Weil reciprocity) law | Assessment (105 instance PROVED) |
| steering | s6_window_independence | gcd(K_m, K_m′) \| (m − m′)/4: windows are independent lotteries | PROVED (trivial) + Assessment |
| steering | s6_exp_classes_primes | algebraic budget-forcing needs a thin family; for a single prime it is B2 | Assessment (negative) |

## 3. Verdict (O238 checkpoint 1)
1. **New theorem: ES holds for every n = 4^s + 105** (PROVED, computer-assisted; Thm 1.1). One exponential window class
   (n = 256u³ + 105, u ≡ 32 (mod 151), window 151 = 4⁴ − 105) closes the gap left by (J)62's 13-class ET covering at L = 360.
   (J)62's "mixed points" were an artefact of the fixed-modulus class menu: the hypothesis of EXPONENT_COVERING Thm 1.4
   that is violated is "classes with fixed moduli".
2. For ES at primes nothing changes: every route to cap 0 found here either is a finite congruence menu (m = 3), needs a
   linear-in-q budget (pigeonhole), or needs a thin family with a moving algebraic factorisation. Cap 0 at a window
   remains B2 (CAP_DOWN §4), and windows are independent lotteries.
3. T1 checks: exp class contains no squares (global Lemma-1.1 T1, numerically to u < 3·10⁷); window-shape T1 classified
   for all ν. TES/8/131: untouched (cap-0 statements; s6_numerator_windows records that 8/131 has forced windows at
   some positive cap only).
4. Open: k = 33, 273, 297 (exp menu 4^j − k too thin; Sophie-Germain shapes and Type I exponential classes untried).
