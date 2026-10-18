# R281 — hostile review of O270 (EXP_15.md, exp-fifteen: F2 Pierpont boundary + F1 15·2^s + 1)

Reviewer: R281 side agent. Branch reviewed: side-agent/exp-fifteen (merged into review worktree).
From-scratch scripts: `scripts/review_r281_*.py` (pierpont, pierpont_open, boxed, iiad, iid); logs `data/review_r281/`.
Status: round 1 complete.

**Repairs applied** (author quiet since 16:11; marked "(R281 repair)"): EXP_15.md — D1/D2 (§2.4 Ridout sentence), D3/D4/D5
(Computation 3.2), D6/D7 (§1.3 scope and "iff", Lemma 1.1 neighbourhood remark), D8 (wording, QNR list), D10 (§3
"31 boxed solutions with A, d odd"), D11 (missing script); memos z40_iiad_branches (D1/D2), z40_menu_IId (D3);
AGENT_REPORT_O270 (S2) and Step 3 (D1–D3). Not applied: D9 (optional); re-running z40_seeded with deg g ≥ 2 (author's
tooling) is left to the author.

## Summary verdicts
| claim | verdict |
|---|---|
| §0 (I1) {2,3}-unit-square points (0,1), (3,0) | SOUND (C1) |
| Lemma 1.1 ((0,1) window base-free) | SOUND (C2); wording D8, neighbourhood remark D7(ii) |
| Lemma 1.2 ((3,0) cyclotomic descent) | SOUND (C3) |
| §1.3 2D covering-tree EVIDENCE | SOUND as EVIDENCE, spot-checked (C14); scope D6, "iff" D7 |
| Lemma 2.1 (C1)–(C3), Capelli | SOUND (C4, C5); D9 optional |
| Theorem 2.2 (u ≡ 3 (8) sterile ∀D) | SOUND (C6) — the board's disputed all-D claim is now genuinely PROVED |
| Lemma 2.2′ (39 solutions) | SOUND (C7), own bound proof + exhaustive check; D10 |
| Remark 2.3 (argon refuted) | SOUND (C8) |
| §2.4 u ≡ 7 (8) reduction | algebra SOUND; Ridout assessment wrong → GAP (C9; D1, D2) |
| §2.4 EVIDENCE + 63 control | SOUND, reproduced and extended (C10) |
| Lemma 3.1 (even D) | SOUND (C11) |
| Computation 3.2 (II-d searches) | GAP: seeded "hits" are degenerate constant-gap artefacts (D3); grid D4, D5; negative result independently confirmed for D = 3 (C13) |

No FATAL. 3 MAJOR (D1–D3; none touches a PROVED statement), 8 MINOR.

## Claim-by-claim

### C1. §0 (I1) boundary points of P = {2^a3^b + 1} — SOUND
Re-derived: an integer point 2^a3^b + 1 = v² needs v − 1, v + 1 both {2,3}-smooth at distance 2 (Størmer-type list):
(1,3), (2,4), (4,6), (6,8), (16,18) → n = 4, 9, 25, 49, 289 = (a,b) = (0,1), (3,0), (3,1), (4,1), (5,2)
(`review_r281_pierpont.py`, a ≤ 60, b ≤ 40, same list). Only 4 = 2² and 9 = 3² are squares of primes in S = {2,3}; the
others are squares of 5, 7, 17 and their neighbourhoods lie in the divisor classes 5 | n, 7 | n, 17 | n. So the
{2,3}-unit-square points (with a, b → ∞ in the real sense) are exactly (0,1) and (3,0). ✓ (See D6 for the
finite-a / finite-b edges.)

### C2. Lemma 1.1 ((0,1) window is base-free) — SOUND
Re-derived from MENU_STERILITY Theorem C(a): for each of the eight rules d = f₊^b f₋^c (a = 0) the numerators of
y = n(K+d)/11 and z = nK(K+d)/(11d) are integer polynomials in X (z: d cancels symbolically against K(K+d) in all four
shapes (b,c) ∈ {(2,1),(0,2),(2,0),(1,2)}), so integrality is a condition on X mod 11 only, valid for every integer X ≥ 0
in the class; positivity holds for real X. The s-mod-40 table maps to X ≡ 6, 2, 4, 8, 5, 9, 7, 3 (mod 11) — all eight
classes 2…9. From-scratch exact check: all 540 values X = 2^t3^{t′} (t, t′ ≤ 25) with X ≢ ±1 (mod 11) give exact
solutions 4/n = 1/x + 1/y + 1/z with n = 2^{4t+4}3^{4t′+1} + 1. Also checked: at (a,b) → (0,1) in Ẑ², X → 1/2 ≡ 6
(mod 11), so the whole neighbourhood of (0,1) lies in a window class (the lemma really does dissolve the point, which the
text does not say explicitly — see D7). Wording defect D8.

### C3. Lemma 1.2 ((3,0) cyclotomic descent) — SOUND
Trivial and correct: Z^p + 1 = (Z + 1)Φ, 3 ≤ Z + 1 < n, scaling a solution of 4/(Z+1) by r = n/(Z+1). From-scratch:
28 cases a ≤ 12, b ≤ 9, odd p | gcd(a,b), brute-force solution for Z + 1 scaled to an exact solution for n. It is a
*reduction* (ES for n ⇐ ES for the smaller Pierpont number Z + 1), fine in a covering tree by well-founded induction;
the text correctly says "reducing to" ✓.
Capelli remark: 15Y^D + 1 irreducible for all D ✓ (−1/15 ∉ ℚ^p for odd p; −1/15 ∉ −4ℚ⁴; ∉ ℚ² as < 0).

### C4. §2.1 Type II identity f·f′ = n + 4a²d — SOUND
(4abd − n)(4acd − 1) = 16a²bcd² − 4abd − 4acdn + n = 4ad(4abcd − b − cn) + n = 4a²d + n using cn = 4abcd − a − b. ✓

### C5. Lemma 2.1 (II-ad limit conditions (C1)–(C3)) — SOUND (minor presentational points D9)
Re-derived line by line.
* Capelli: 15Y^D + K, K = 1 + 4a²d ≥ 5 odd. Y^D − c, c = −K/15 < 0: p = 2 impossible (c < 0); −4w⁴ form needs
  K s⁴ = 60 r⁴ with gcd(r,s) = 1 ⇒ s = 1, K = 60r⁴ even — impossible. So c = (−u)^p, p | D odd prime, u ∈ ℚ_{>0};
  K s^p = 15 r^p ⇒ s^p | 15 ⇒ s = 1. u = 1 gives 4a²d = 14 (impossible), u even gives K even; so u ≥ 3 odd, and
  K ≡ 1, 15 ≡ −1 (mod 4) give u^p ≡ 3 ⇒ u ≡ 3 (mod 4). ✓ From-scratch sympy sample (`review_r281_boxed.py`):
  for D = 2…12 and all K ≡ 1 (mod 4), K < 2000, "15Y^D + K reducible" ⇔ "15 | K and K/15 a p-th power, p | D odd":
  0 mismatches.
* (C2): f, f′ > 0 at arbitrarily large real Y ⇒ positive leading coefficients; B = 15Y^D + K > 0 on [0, ∞), so neither
  factor vanishes there ⇒ X, X′ > 0. ✓ X ∈ ℤ[1/2]: X + 16 = 4ad·b(1) and b(1) ∈ ℤ[1/2] (MENU_LADDER Lemma 2.1). ✓
  X ∈ ℤ_(2): f = κP, P monic, roots α of B satisfy 15α^D = −K so |α|₂ = 1; v₂(X) = v₂(κ) + Σv₂(1 − α) ≥ v₂(κ) =
  v₂(f(0)) ≥ 0. ✓ Congruences: simpler than the ℓ-adic continuity argument given — (X + 16)/(ad) = 4b(1) ∈ ℤ[1/2] has
  odd denominator dividing odd(ad), so q | X + 16 directly; likewise X′ + 1 = 4ad·c(1). ✓
* (C3): f(0) = 4ad·b(0) − 1 with b(0) ∈ ℤ_(2) ✓; f′(0) likewise ✓.
* Degenerate cases: f′ constant ⇒ c constant ⇒ b = (cn + a)/(4acd − 1) is one ET congruence class in n — excluded near
  μ = 0 by EXPONENT_COVERING Cor 1.5 (which lists 15·2^s + 1, cf. MENU_STERILITY §4.1) ✓; f constant = constant gap
  4x − n ⇒ EXP_OPEN Theorem W, whose Computation 1.6 covers (15, 1) for all D ✓.
* Sufficiency remark ("(C1)–(C3) sufficient given the factor shape"): ✓ via MENU_LADDER Lemma 2.1 (b(1), c(1) ∈ ℤ[1/2]
  from (C2), b(0), c(0) ∈ ℤ_(2) from (C3)), positivity from κ > 0.

### C6. Theorem 2.2 (u ≡ 3 (mod 8) branch sterile for every D) — SOUND
u odd, p odd ⇒ u^p ≡ u (mod 8); 4a²d = 15u^p − 1 ≡ −u − 1 (mod 8): ≡ 4 iff u ≡ 3, ≡ 0 iff u ≡ 7. So u ≡ 3 (8) ⇔ a, d
odd ⇔ q = ad. X = m₁ad − 16 > 0, X′ = m₂ad − 1 > 0 with m₁, m₂ ∈ ℤ forces m₁, m₂ ≥ 1; expanding XX′ = 16 + 4a²d and
dividing by ad gives a(m₁m₂d − 4) = m₁ + 16m₂ ✓ (equivalently (am₁d − 16)(am₂d − 1) = 16 + 4a²d, checked on all 39
solutions). D enters only through "p | D", and the factor shape not at all — the proof uses only X = f(1), X′ = f′(1)
and (C1). This is a genuine, all-D closure of the branch the board disputed (memo item "e | D, e < D"): the board's
objection (astra/fable round 4: "does not exhaust the valuation parameter E") is answered because u ≡ 3 (8) forces
E = 2 exactly. ✓
Remark: 8 of the 39 solutions have a or d even ((a,d) = (1,2)×2, (1,6), (2,1), (2,2), (3,2), (5,2), (6,1)); they are
irrelevant to the u ≡ 3 branch (there q ≠ ad), harmless but worth one sentence (D10). The 31 relevant ones have 20
distinct odd pairs (a,d).

### C7. Lemma 2.2′ (boxed equation: exactly 39 solutions) — SOUND
Own bound proof: d ≤ 1/m₂ + 16/m₁ + 4/(m₁m₂) ≤ 21; (m₁ − 16)(m₂ − 1) ≤ 20; m₂ = 1 ⇒ m₁ ≤ 24 (d = 1, m₁ − 4 | 20) or
m₁ ≤ 20 (d ≥ 2); m₂ ≥ 2, m₁ ≥ 17 ⇒ m₁ ≤ 36, m₂ ≤ 21; m₁ ≤ 16, t = m₁d ≥ 5 ⇒ a ≤ (m₁ + 32)/6, m₂ = (m₁ + 4a)/(am₁d − 16)
≤ 48; t ≤ 4 ⇒ (at − 16)(tm₂ − 4) = tm₁ + 64 ≤ 80 ⇒ m₂ ≤ 84. Exhaustive box d ≤ 21, m₁ ≤ 36, m₂ ≤ 84: **39 solutions**;
a far larger box (d ≤ 60, m₁, m₂ ≤ 3000, numpy) gives the same 39. Max a = 81, d = 21, m₁ = 36, m₂ = 69. Only
(a,d) = (1,11) has 15 | 4a²d + 1, quotient 3 (not a perfect power). ✓ Author's hand bounds re-checked case by case
(m₂ = 1; m₁d ≥ 5 monotonicity in m₂; m₁d = 1…4 factorisations): all correct (m₁d = 2 even gives a ≤ 25 < 42).

### C8. Remark 2.3 (argon's P₀(Y^{2^r}) claim refuted) — SOUND
sympy: Y⁶ + 27 = (Y² + 3)(Y² + 3Y + 3)(Y² − 3Y + 3); by hand Y⁴ − 3Y² + 9 = (Y² + 3)² − (3Y)². Argon's round-4 text
(board rounds/04-argon.md l.29) explicitly asserts "Y⁴ − 3Y² + 9" is a factor P₀(Y²) and that "Capelli never splits
further" — false (Capelli is about binomials; Y⁴ − 3Y² + 9 is not one). New (P(0), P(1)) pairs (3, 7), (3, 1) ✓.
astra's example: 1 + 4·101 = 405 = 15·3³ ✓, u = 3 ≡ 3 (8) ⇒ killed by Thm 2.2 ✓.

### C9. §2.4 (u ≡ 7 (mod 8) branch: reduction to 2-adic approximation) — GAP (label/assessment errors; algebra SOUND)
* 2-adic bookkeeping ✓: v₂(1 + u^p) = v₂(1 + u) (cofactor 1 − u + … + u^{p−1} is a sum of p odd terms); with
  N = 16 + 2^E a₁²d₁: E = 3 ⇒ V = 3, E = 4 ⇒ V ≥ 5, E ≥ 5 ⇒ V = 4 (u ≡ 15 (32)); converses ✓.
* Magnitude ✓ (even slightly sharper: X ≥ q − 16, X′ ≥ q − 1 ⇒ q ≤ √N + 16): a₁ = a₁²d₁/q gives
  2^E a₁ ≥ (15u^p − 1)/(√N + 16).
* a = 1 sub-branch ✓ as algebra: |15u^p − 1|₂ = 2^{−E} ≲ (15u^p)^{−1/2}; and since |u − ζβ|₂ = 1 for ζ ≠ 1
  (|1 − ζ_p|₂ = 1, p odd), |u − β|₂ = |15u^p − 1|₂ with β = 15^{−1/p} ∈ ℤ₂. **But the conclusion drawn is wrong (D1):**
  approximation of a 2-adic algebraic β by *integers* u (denominator 1, an S-unit) has Ridout exponent 1 + ε, not 2 + ε
  (Ridout 1958 in Lang's form with S = {∞, 2}, α_∞ = ∞: |u − β|₂·u^{−1} < u^{−2−ε} ⇔ |u − β|₂ < u^{−1−ε}; equivalently the
  p-adic Subspace Theorem with forms (X, Y) at ∞ and (X − βY, Y) at 2, which yields u·|u − β|₂ < u^{−ε} finitely often).
  Dirichlet exponent here is 1 (one integer per residue class mod 2^k), so p/2 ≥ 3/2 > 1 is already "abnormally good":
  **Ridout gives finiteness (ineffective) for every odd p, including p = 3**, in the a = 1 (indeed bounded-a₁) sub-branch.
  I could not open Ridout's paper in sources/; the statement used is the standard one (Lang, *Fundamentals of Dioph.
  Geometry*, Ch. 7; Schmidt LNM 785), and the Subspace derivation above is self-contained.
* The *general* branch is not a 2-adic approximation problem (D2): with a₁ unbounded, the requirement is
  15u^p − 1 = 2^E a₁²d₁ with a₁d₁ ≤ √N + 16 — a large *square* odd part is equally good (e.g. E = 3, d₁ = 1:
  15u^p − 8a₁² = 1, a hyperelliptic/superelliptic equation). EXP_15 §2.4 states this correctly ("2^E·a₁²" part), but
  AGENT_REPORT (S2) and memo z40_iiad_branches compress it to "divisible by a power of 2 of about half its size" /
  "at least as hard as an effective 2-adic Thue/Ridout problem", which is wrong for a₁ > 1 and unproved as a hardness
  claim (necessary conditions (C1)–(C2) only; (C3) and factor shape are ignored, so a closure might never need it).
* q ≤ 16 sub-branch ✓: q = 1 makes (C2) vacuous; (C1) is 15u^p − c2^E = 1, c ≤ 256 — for fixed p a Thue equation
  15X^p − c2^r Y^p = 1 (E = pk + r), finite and effective (Baker). ✓
* D = p factor shape ✓ (κκ′ = 15 so v₂(κ) = 0; Φ(1) = (1 + u^p)/(1 + u) odd; v₂(X) ∈ {0, V}).
* Attribution of argon's "similarly bounded via Lemma 1.5": argon items/argon.md l.67 indeed says this; author's
  rejection is fair (Lemma 1.5 bounds a constant window m; no such object here). ✓
* Label: "OPEN; reduction + EVIDENCE" is the right label for the branch; the sentence about Ridout must be corrected.

### C10. §2.4 EVIDENCE (no (C1)+(C2) solution) and positive control — SOUND (reproduced, extended)
From-scratch `review_r281_iiad.py` (factor 15u^p − 1, all a with a² | (15u^p − 1)/4, all divisors X of N):
p = 3, u ≤ 6·10⁴ (21737 tuples); p = 5, u ≤ 2000 (692); p = 7, u ≤ 70; p = 11, u ≤ 30; p = 13, u ≤ 20; p = 17, 19, 23,
u ≤ 15, 12, 10: **0 hits**, both branches (u ≡ 3, 7 (8)). (Author's count 7414 vs mine 7430 at the author's nominal ranges
differs only by range rounding for p ≥ 11; my ranges are supersets.) Positive control c₀ = 63: exactly one hit
(u, p, a, d, X, X′) = (3, 3, 5, 17, 21, 84) = EXP_OPEN Thm 2.3 ✓; c₀ = 63, p = 5, u ≤ 30: none.

### C11. Lemma 3.1 (even D ⇒ a has no real root) — SOUND
c ∈ ℚ[Y] ⇒ 4ad·c = f′ + 1 ⇒ f′(y₀) = −1 at a real root y₀ of a; f′ has positive leading coefficient (f′ = 4acd − 1 > 0
at large Y; f′ constant would be −1 < 0); IVT gives y₁ > y₀ with f′(y₁) = 0, so B(y₁) = 0, contradicting
B = 15Y^D + 1 + 4da² ≥ 15Y^D + 1 > 0 on ℝ for D even. ✓ (Uses d > 0 and only that a, c are real polynomials.)

### C12. Computation 3.2 (II-d search EVIDENCE) — GAP (misreported seeded hits; restricted trinom grid)
* **Seeded "2 rational solutions" are degenerate (D3).** For both reported (15, 1) solutions, B = 15Y³ + 1 + 4da² is
  *irreducible* and f = B/f′ is the constant 14 (sympy, `review_r281` session): a = (Y+1)/2, d = 3 gives
  f′ = (15Y³ + 3Y² + 6Y + 4)/14; a = 3(Y+1)/2, d = 5 gives f′ = (15Y³ + 45Y² + 90Y + 46)/14. Same for D = 5. These are
  constant-gap families (gap 14), already excluded by Theorem W; the seeded interpolant g degenerated to a constant
  (φ = X = −n(−1) = 14). The (63, 1) D = 3 "solutions" have c = 1/4 constant, i.e. f′ constant (ET-class degenerate).
  So the log contains no genuine II-d configuration at all, and the memo's "Reading: the Y = 0 specialisation is where
  II-d dies (a(0) ∈ ½ℤ)" is drawn from degenerate artefacts.
* **z40_trinom grid (D4).** It enumerates the *monic* quadratic factor Y² + pY + q with denominators of p, q dividing 8.
  For 15Y^D + … the natural denominators of monic factors are 3, 5, 15 (e.g. (3Y + α)(5Y² + …)), and a may have odd
  denominators (a(0) ∈ ℤ_(2), a(1) ∈ ℤ[1/2] allow a = (2Y + 1)/3). The EVIDENCE is honestly stated ("denominators | 8")
  but this is a poor grid. My independent D = 3 search (`review_r281_iid.py`, parametrised by the rational root r of B
  and the root y₀ of a, any denominators ≤ DEN): see C13.
* z40_seeded's c₀ = 63 seeds use the c₀ = 15 box (a ≤ 81, d ≤ 21, m₁ ≤ 36), which is not exhaustive for 4^J = 64
  (control only; MINOR).

### C13. Independent II-d search, D = 3, linear a (R281 EVIDENCE, supplements C12)
`review_r281_iid.py c₀ H DEN TMAX`: B = c₀Y³ + 1 + 4da² must have a rational root r; parametrise by (r, y₀) (y₀ the root
of a; |r|, |y₀| ≤ H with any denominator ≤ DEN), d·α² = −(c₀r³ + 1)/(4(r − y₀)²), d = sqfree·t² (t ≤ TMAX), both
roles (f′ linear / f linear) with f′(y₀) = −1; exact Type II identity asserted for every configuration reaching
polynomial b, c; validity = MENU_LADDER Lemma 2.1 + positive leading coefficients.
(15, 1): H = 4, DEN ≤ 10, t ≤ 20: 13110 algebraic configurations, **0 valid** (H = 2, DEN ≤ 6: 3420 identity-checked
configurations, none even ℤ[1/2]-integral at Y = 1). (3, 1), H = 2, DEN ≤ 6: 0 valid (29 pass Y = 1, 114 pass Y = 0,
none both). Agrees with the author's negative EVIDENCE on a grid that includes odd denominators (D4). No positive
control exists for II-d (none known for any c₀), so this is a non-discovery only.

### C14. §1.3 Pierpont 2D covering-tree EVIDENCE — SOUND as EVIDENCE (spot-checked); framing defects D6, D7
From-scratch `review_r281_pierpont_open.py` on the author's open-cell lists: L = 5040 (`lv2_5040.json`, 47 cells) and
L = 20160 (`tree_w.json`, 496 cells): no open cell is reachable by Lemma 1.2 descent (odd p | gcd(a₀, b₀, L)), by a
Lemma 1.1 window, or by a divisor class q | n with q admissible (q | 2^L − 1 and q | 3^L − 1, all such q < 2·10⁷ found);
every open cell is a QNR modulo some admissible q ✓. Caveat: at L = 5040 the cell (5, 2522) is a QR modulo every
admissible prime < 3000 and first fails at q = 13441 (still ≤ the stated Mmax 3·10⁴, so the claim stands, but the
quoted list "97, 113, 127, 193, 211, …" is incomplete). All 44 cells of the divisor class 17 in `lv2_5040.json` verified.
Tree densities in the text match `tree_w.json`'s log (7, 20, 32, 128, 496 open at L = 360 … 20160) ✓. I did not
re-derive the ET-class cells (would need an independent ET-class enumerator); as the result is a non-discovery this is low
risk.

## Defects

**No FATAL defect.** All PROVED items (Lemmas 1.1, 1.2, 2.1, 2.2′, 3.1, Theorem 2.2, Remark 2.3) re-derived and SOUND.

**D1 (MAJOR — misapplied citation, §2.4 bullet "Magnitude"; memo z40_iiad_branches bullet 3; AGENT_REPORT (S2)).**
"Ridout's theorem makes this finite (ineffectively) for p ≥ 5, and nothing elementary bounds it for p = 3" / memo
"p = 3 is beyond Roth's exponent". For approximation of β = 15^{−1/p} ∈ ℤ₂ by *integers* the Ridout exponent is 1 + ε,
not 2 + ε (Ridout with the denominator an S-unit; Lang's form with S = {∞, 2}; or the p-adic Subspace Theorem with forms
(X, Y) at ∞, (X − βY, Y) at 2). Since |u − β|₂ = |15u^p − 1|₂ (|u − ζβ|₂ = 1 for ζ ≠ 1), the a = 1 condition
|u − β|₂ ≲ u^{−p/2} has exponent p/2 ≥ 3/2 > 1, so it has finitely many solutions **for every odd p including p = 3**;
more generally every solution with a₁ ≤ u^{p/2 − 1 − ε} is among finitely many (per p). *Repair:* replace the sentence by
"Ridout (integer approximants, exponent 1 + ε) gives finiteness, ineffectively, for each odd p (p = 3 included) in the
sub-branch a₁ ≤ u^{p/2−1−ε}; open are effectivity, uniformity in p, and the large-a₁ sub-branch (see D2)"; fix the
memo and AGENT_REPORT (S2) accordingly.

**D2 (MAJOR — overclaim in AGENT_REPORT (S2) and memo z40_iiad_branches).** (S2) says a solution "needs 15u^p − 1 …
to be divisible by a power of 2 of about half its size" and the memo says closing the branch "is at least as hard as an
effective 2-adic Thue/Ridout problem (Assessment)". (i) The first is false for a₁ > 1: what is needed is a large
2^E·a₁ (equivalently a large 2^E·a₁² part of 15u^p − 1 with a₁d₁ ≤ √N + 16); e.g. E = 3, d₁ = 1 is the superelliptic
equation 15u^p − 8a₁² = 1, not a 2-adic approximation condition. EXP_15 §2.4 itself states this correctly. (ii) "at least
as hard" is an unproved hardness claim: (C1)–(C2) are only necessary conditions; (C3), the factor shape, and positivity are
not used, so a closure might bypass the Diophantine problem entirely. *Repair:* "(C1)–(C2) alone reduce the branch to …;
we found no way to use (C3)/factor shape to avoid this (Assessment)".

**D3 (MAJOR — EVIDENCE misreported, §3 Computation 3.2 bullet 2; memo z40_menu_IId bullet 4; AGENT_REPORT Step 3).**
The two (15, 1), D = 3 "rational solutions" of z40_seeded (a = (Y+1)/2, d = 3; a = 3(Y+1)/2, d = 5), and the D = 5 ones,
are degenerate: B is irreducible and f ≡ 14 is constant (the seeded quadratic interpolant collapsed to a constant), i.e.
they are constant-gap families already killed by Theorem W; the (63, 1) ones have c = 1/4 constant (f′ constant).
No genuine II-d configuration occurs in `data/z40/seeded.log`. The interpretation "Y = 0 is where II-d dies (a(0) ∈ ½ℤ)"
rests on these artefacts. *Repair:* make z40_seeded reject deg g < 2 (or deg f, deg f′ < 1), re-run, and report
"0 genuine algebraic configurations"; drop or re-base the "Reading".

**D4 (MINOR — weak search grid, §3 Computation 3.2 bullet 1).** z40_trinom restricts the monic quadratic factor's
coefficients to denominators | 8; monic factors of 15Y^D + … naturally have denominators 3, 5, 15, and a itself may have
odd denominators (a(0) ∈ ℤ_(2), a(1) ∈ ℤ[1/2], e.g. a = (2Y+1)/3). *Repair:* parametrise by roots (as in
`review_r281_iid.py`: rational root r of B and root y₀ of a, any denominators) or use DEN = 120; state the grid.

**D5 (MINOR — control only).** z40_seeded's "boxed" seeds for c₀ = 63 reuse the c₀ = 15 bounds (a ≤ 81, d ≤ 21,
m₁ ≤ 36); for 4^J = 64 the analogous bounds are larger (d ≤ 69, …), so the (63, 1) seeding is not exhaustive.
*Repair:* derive the 4^J-bounds (d ≤ 4^J + 5, (m₁ − 4^J)(m₂ − 1) ≤ 4^J + 4) or label it a sample.

**D6 (MINOR — scope, §1.3 last bullet, §0 (I1), AGENT_REPORT Step 1).** "A finite certificate for all Pierpont numbers"
and the "iff" via EXPONENT_COVERING §5.1 concern cells with a, b ≥ A0 only (§5.1 transfers Thm 1.4 to "members whose every
exponent is ≥ m₀"). "All 2^a3^b + 1" additionally needs the finitely many edge lines 3^{b₀}·2^a + 1 (b₀ < A0) and
2^{a₀}·3^b + 1 (a₀ < A0), each a 1D family with its own certificate (board rounds 3–4: b₀ ≤ 6 settled; a₀-lines not
discussed). *Repair:* one sentence stating the theorem shape "a, b ≥ A0, plus the 2A0 edge lines", and list which edge
lines are certified.

**D7 (MINOR — §1.3 "iff" and the role of Lemma 1.1).** (i) "it exists iff the closure … minus the neighbourhoods of (0,1)
and (3,0) avoids S′" — the "only if" direction holds only for certificates built from ET/divisor classes plus Lemmas
1.1–1.2; with other windows a sterile point could still be covered. (ii) That Lemma 1.1 covers a full neighbourhood of
(0, 1) needs the (unstated) fact that X → 1/2 ≡ 6 (mod 11) as (a, b) → (0, 1) in Ẑ², so the excluded classes X ≡ ±1
(mod 11) stay away from (0, 1). *Repair:* add both sentences.

**D8 (MINOR — wording).** Lemma 1.1: "j ≡ 1,…,9 except j ≡ 0, 5 (mod 10)" → "j ≢ 0, 5 (mod 10)". §1.3: the QNR witness
list omits q = 13441, needed for the L = 5040 cell (5, 2522).

**D9 (MINOR — proof presentation, Lemma 2.1 (C2)).** The congruences need no ℓ-adic continuity: (X + 16)/(ad) = 4b(1) and
(X′ + 1)/(ad) = 4c(1) lie in ℤ[1/2] and have odd-part denominators dividing odd(ad), whence q | X + 16, q | X′ + 1.
Optional simplification.

**D10 (MINOR — Lemma 2.2′ / §3).** Of the 39 solutions only 31 (20 distinct pairs) have a, d both odd, which is the only
case Theorem 2.2 uses; §3's "for A, d odd the Y = 1 data are exactly the 39 boxed solutions" should read "the 31 boxed
solutions with A, d odd". *Repair:* one sentence each.

**D11 (MINOR — missing verification script, Lemma 1.1 *Proof*).** "re-verified in `scripts/z40_pierpont_check.py`" —
no such file exists on the branch (z40_pierpont_cover.py only applies the X mod 11 rule, it does not re-verify the
identities). *Repair:* cite `scripts/review_r281_pierpont.py` (identities, integrality on whole classes mod 11, 540
exact Pierpont checks) or add the script.
