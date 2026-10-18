# R281 — hostile review of O270 (EXP_15.md, exp-fifteen: F2 Pierpont boundary + F1 15·2^s + 1)

Reviewer: R281 side agent. Branch reviewed: side-agent/exp-fifteen (merged into review worktree).
From-scratch scripts: `scripts/review_r281_*.py`. Status: IN PROGRESS.

## Summary verdicts
(filled in claim by claim below)

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
*reduction* (ES for n ⇐ ES for the smaller Pierpont number Z + 1), which in a covering tree is fine by well-founded
induction; 4/(Z+1) is always solvable for Z + 1 ≥ 3 only if ES is known for Z + 1 — the text says "reducing to" ✓.
Capelli remark: 15Y^D + 1 irreducible for all D ✓ (−1/15 ∉ ℚ^p for odd p; −1/15 ∉ −4ℚ⁴; ∉ ℚ² as < 0).

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
2^{a₀}·3^b + 1 (a₀ < A0), each a 1D family with its own certificate (board: b₀ = 0, 1, 2, 3, 4, 5 settled; a₀-lines not
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
