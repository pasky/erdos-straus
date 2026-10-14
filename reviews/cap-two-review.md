# R213 — hostile review of CAP_TWO.md (O214, spark relay Y6)

Reviewer: R213 (side agent, branch side-agent/review-cap-two). Reviewed commit: side-agent/cap-two as merged at start.
From-scratch scripts: `scripts/review_r213_*.py` (none reuses `y6_*`).
Repairs applied: (none yet — filled in at the end if the author is quiet).

## Summary verdict per claim

| Claim | Verdict |
|---|---|
| Thm 1.1 (k = 1 cap-2 shots ⟺ W_n, c odd) | SOUND-AFTER-REPAIRS (m1: Q₁ odd must be a hypothesis) |
| Thm 1.2 (one equation, two cells; fibre picture) | SOUND-AFTER-REPAIRS (m1(b) false "other solutions" bullet; m6 halves overlap as shot sets; m7 fibre picture is a necessary condition) |
| Prop 2.1 (a)(b)(c) (slices finite, orbits infinite) | SOUND |
| §2 Reading "O204 contrast is a slicing effect" (Assessment) | SOUND-AFTER-REPAIRS (m6: wording) |
| Thm 4.1 (D-face, (i)(ii)(iii)) | SOUND |
| Thm 4.1 Example (c, w) = (1, 1) | SOUND-AFTER-REPAIRS (m2: missing gcd(a, n) = 1) |
| Prop 5.1 (finite exponent-2 budget ⇒ finite slice) | SOUND (m4: stale citation in (c)) |
| §6 no polynomial families (MARKOFF Thm 5.1 transfer) | SOUND (transfer is verbatim after μ ↦ x/2, N(η) = 4n) |
| §6 fibre EVIDENCE + Assessment | SOUND-AFTER-REPAIRS (m5: "positive proportion" overclaim) |
| §3 EVIDENCE (coverage of primes < 10⁶) | SOUND-AFTER-REPAIRS (m3: 13 402 → 13 401; "need exponent 2" overstated) |
| T1 location | SOUND |
| §7 verdict "ES^{(y,2)} at k = 1 not easier than ES^{[2]}" | SOUND as Assessment (correctly labelled; not PROVED) |

No FATAL, no MAJOR defect found. All PROVED algebra re-derived by hand and brute-forced; all numerical claims I
re-ran agree exactly except one count (m3) explained by tie-breaking.

## Checks performed

**C1 (Thm 1.1, both directions, brute force; `scripts/review_r213_dict.py 200 100000`, 2.7 s).**
Side A enumerates EVERY k = 1 shot datum (odd 3 ≤ n ≤ 200, g ≤ 10⁵, g ≡ 3 mod 4, Q = K·Q₁ with rad Q₁ | K and
v_ℓ(Q₁) ≤ 3 incl. ℓ = 2, gcd(Q, n) = 1), builds the shot solution x, y, z, asserts 4/n = 1/x + 1/y + 1/z exactly and
tests ES^{(y,2)} membership DIRECTLY from EXPONENT_CAP Def 1.1 (den z = q², q odd, gcd(q, n) = 1, rad q | y,
v_ℓ(q) ≤ 2). Side B enumerates all (a, B, c) with c, B odd, g = caB − 1 ≤ 10⁵ and solves W_n for n by the congruence.
Results: 876 k = 1 shots lie in ES^{(y,2)}; 876 canonical W_n points (c, B squarefree coprime, 4 | a,
gcd(caB, n) = 1); the two sets of (n, g, Q₁) are IDENTICAL, the map is injective, and den z = Q₁² for every member.
Among ALL 4 484 c-odd W_n points (no squarefree / coprime / 4 | a restriction) "E ≡ 3 (4) ⟺ 4 | a" holds without
exception. The n = 41 and n = 5 examples of Thm 1.2 re-derived by hand (g = 35, E = 75 / 675; g = 81, E = 1).
Hand re-derivation of the proof of Thm 1.1: correct, including the mod-4 argument.
BUT: 617 further k = 1 shots satisfy the literal CAP_TWO definition "k = 1, rad Q₁ | Q₀, v_ℓ(Q₁) ≤ 2" with Q₁ EVEN
(e.g. n = 3, g = 7, Q = 8, Q₁ = 4; n = 11, g = 23, Q₁ = 18). They are NOT in ES^{(y,2)} (q even), and they are not
in the image of W_n with c, B odd. → defect m1.

**C2 (Thm 1.2 first bullet; `scripts/review_r213_half0.py`).** All 1 155 W_n points with c = 4λ, B odd,
gcd(a, B) = 1, gcd(λB, n) = 1 (odd n ≤ 200, g ≤ 2·10⁴) give, with Q = λB², exact solutions with den z = B², B | y and
k = a — i.e. GROWING_MUTE Prop 1.1(c) with A_GM = 2a. Hand check of the dictionary A_GM = 2a, 2A_GM·B = 4aB,
g + 1 = 4λaB, E = D_GM: correct. BUT 351 c-odd points (4 | a, gcd(caB, n) = 1) have a shot (n, g, Q) that is ALSO an
ES^{[2]} shot (e.g. n = 5: (a, B, c) = (4, 1, 1) and the c ≡ 0 point (1, 1, 4)) → m6.
Hand check of the "other solutions" bullet: c ≡ 2 (mod 4) with a EVEN gives g ≡ 3 (mod 4) AND integral Q₀ = caB/4,
i.e. a k = 1 shot with EVEN overflow Q₁ = cB² (e.g. n = 11, (a, B, c, E) = (4, 3, 2, 31), g = 23, Q₁ = 18, one of
the 617 even-Q₁ shots of C1) → m1(b).

**C3 (Prop 2.1; `scripts/review_r213_bounds.py`).** Proofs re-derived by hand (B-Vieta, a-Vieta with t = (B² + E)/a,
the fixed-(B, c) equation a(cBt − 4n) = t + cB³, the congruence-subgroup argument in (c)): correct. Numerically, over
ALL c-odd W_n points (odd n ≤ 99, caB ≤ 2·10⁵, no side conditions) the bound c ≤ (4n + 1)(B² + 1)/B and, for 4 | a,
B ≤ 8na², E ≤ 4na² + B² never fail; the B = 1 points never exceed O204's wall (16n + 1)/3.

**C4 (Thm 4.1).** Algebra re-derived by hand: w integral, aw = E + B², a(cBw − 4n) = w + cB³, D·g = 4n + Q₁², the
mod-4 equivalence, (i) 4D | w + cB³, (ii) gcd(w, D) = gcd(B, D) = 1 and the square-root criterion, (iii) the
multiplication by c²w³. Numerically (C1 script) all identities incl. D | w² + 4nB², D | 64n³ + c²w⁴ and
cw | D + 4n hold at all 876 points.
Example (c, w) = (1, 1) (`scripts/review_r213_t11.py 400`): 64n³ + 1 = (4n + 1)(16n² − 4n + 1); every D ≡ 3 (mod 4)
dividing it gives 4 | a = (1 + B³)/D and D·g = 4n + B⁴ with B = 4n + D; gcd(B, n) = gcd(D, n) = 1 is AUTOMATIC.
n = 13, D = 7: B = 59, a = 29 340, g = 1 731 059, exact solution with den z = 59⁴, rad | y — confirmed. 1 536 valid
instances for odd n ≤ 400, but 304 instances with B squarefree and gcd(a, n) > 1 (all at composite n; first
n = 21, D = 19, B = 103, a = 57 512 = 7·8 216) → m2.

**C5 (§3 EVIDENCE; `scripts/review_r213_cover.py 1000000 1000000`, 33 s, output `logs/review_r213_cover_1e6.txt`;
`scripts/review_r213_p379.py`).** Independent method (Q₁-side enumeration per modulus g, not the author's (a, B, c)
triples), plus exact Fraction re-verification of every prime's least shot. Reproduced exactly: all 78 497 primes
3 ≤ p < 10⁶ covered with g ≤ 10⁶; least-g decade histogram 45 812 / 25 462 / 6 179 / 962 / 79 / 3; max least
g = 955 979 at p = 379 (Q₁ = 38 307 = 3·113², i.e. (a, B, c, E) = (2 820, 113, 3, 12 611); the W_n-side search for
p = 379 finds this as the UNIQUE shot with g ≤ 10⁶, consistent with "n = 379: 1"); p ≡ 1 (4) split
26 858 / 5 618 / 6 699; odd squares 0 of 499; 8 703 uncovered odd non-squares, 8 535 divisible by 3. 4·379 + 1 = 37·41
(both ≡ 1 mod 4) checked. Discrepancy: 13 401 (not 13 402) primes have no cap-≤1 shot at the least g; the extra one is
p = 837 379, whose least g = 6 995 carries both a B = 1 and a B > 1 shot (the author's script keeps the first triple in
(g, a, B, c) order). Only 783 primes have NO cap-≤1 k = 1 shot at any g ≤ 10⁶ → m3.

**C6 (§6; `scripts/review_r213_pts.py`, `scripts/review_r213_fixE.py`).** Explicit points re-verified as genuine
shots with exact rationals (W_n, 4 | a, gcd(caB, n) = 1, c, B squarefree, den z = Q₁², rad | y): n = 379,
(8 207 552, 1 238 990 989, 7, 23), g ≈ 7.1·10¹⁶; n = 13, (267 468, 443 777, 3, 11), g ≈ 3.6·10¹¹; n = 13,
(32, 7, 1, 239), g = 223 (Δ = 56 913, 3 | Δ ⇒ no norm −1 unit: x² ≡ −4 (mod 3) impossible). Fix-E counts re-derived by an
independent method (X² − ΔY² = −4E via sympy's diop_DN, admissible c = odd, 3 ≤ c ≤ 301, gcd(c, nE) = 1):
n = 13, E = 7: 18/118, all 3 | c; E = 11: 61/125; E = 19: 23/131, all 3 | c; n = 379, E = 23: 27/143 — all EXACTLY as
claimed (so the "upper bound" caveat did not bite). Genus remark for E = 7: if 3 | Δ then f_x ≡ (B − xa/2)² (mod 3)
and −7 ≡ 2 is a non-square mod 3, so 3 | Δ is excluded outright (no "first order" caveat needed); 3 | Δ ⇔ 3 ∤ c. Correct.
The per-octave fibre counts for x ≤ 3000 (197 / 90 / 165) were NOT re-run (not in brief's mandatory list).

**C7 (§6 polynomial families; MARKOFF_ES Thm 5.1).** MARKOFF's proof read in full. Transfer: x := cE ∈ ℚ[s]
non-constant, f := x² − 16n = (x − 4√n)(x + 4√n) (coprime, n non-square), deg f even with square leading coefficient
lc(x)² ⇒ two places at ∞, R* = ℚ*×⟨ε⟩; η = (x + √f)/2 has N(η) = 4n, α = B − aη has N(α) = B² − xaB + 4na² = −E.
The parity argument (b odd ⇒ N(ε) > 0 ⇒ N(α) > 0; b even ⇒ 4n square) goes through word for word. The claim is
correctly scoped (fixed E, c non-constant); it says nothing about families with E varying. SOUND.

**C8 (labels / verdict).** Thm 1.1, 1.2, 4.1, Prop 2.1, 5.1 are elementary and correctly PROVED; the cross-half
comparison, "not a polylog lottery", "neither is easier" and the class-group residual are labelled Assessment, and
5.1(b) is explicitly conditional. ES^{(y,2)} is not claimed. Calibration (R210) respected.

## Defects

**m1 (MINOR; Notation line and Thm 1.1 (⇒)).** The Notation says "Q₁ = Q/Q₀ (overflow, odd)" as if oddness were
automatic, and the definition of "k = 1 cap-2 shot" omits it; in the widened (Q-even) family Q₁ can be even
(617 such k = 1 shots with rad Q₁ | Q₀, v_ℓ(Q₁) ≤ 2 for n ≤ 200, g ≤ 10⁵). The (⇒) proof silently uses c, B odd.
*Repair:* define "k = 1 cap-2 shot" with "Q₁ odd" explicitly (it is exactly what ES^{(y,2)} membership requires:
q odd), and in (⇒) say "c, B odd since Q₁ is odd".
