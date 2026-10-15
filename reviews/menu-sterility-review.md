# R251 — hostile review #1 of O240 (MENU_STERILITY.md, memos z15_*)

Reviewer: R251 (side-agent/review-menu-sterility). Reviewed: merge of side-agent/menu-sterility at ccddde8b.
From-scratch scripts: `scripts/review_r251_proth3.py` (Theorems B/C: rules, ET classes, coverage, exact solutions),
`scripts/review_r251_brute.py` (rule-free ES search, small s). No z15_/z8/ec_cover code was imported or reused.

## Summary verdicts
| claim | verdict |
|---|---|
| Theorem B (window-11 identity, s ≡ 0, 12 mod 40) | SOUND |
| Theorem C (ES for every 3·2^s + 1) | SOUND (minor presentation defects) |
| Theorem C vs (J)22 Cor 1.5 consistency | SOUND |
| (pending) | |

## Theorem B / Theorem C — independent verification

**(i) Theorem B.** Re-derived by hand from CAP_DOWN Lemma 1.1 at m = 11: K = (n + 11)/4 = 12X⁴ + 3 = 3f₊f₋
(f± = 2X² ± 2X + 1, Sophie Germain), 4/n − 1/K = 11/(nK), and 11/(nK) = 1/y + 1/z with y = n(K + d)/11,
z = nK(K + d)/(11d) for any d. With d = 9f₋: K + d = 3f₋(f₊ + 3) = 6f₋(X² + X + 2), y = 6n f₋(X² + X + 2)/11,
z = 2n f₊f₋(X² + X + 2)/11 — exactly the stated terms (sympy, script). Divisibility needed: only 11 | X² + X + 2
(n is prime to 11 on the class, d | K² so K(K + d)/d = K²/d + K ∈ ℤ[X]); X² + X + 2 ≡ 0 (11) ⟺ X ≡ 4, 6 (table of all
residues printed by the script). X = 2^{(s−4)/4}: 2 is a primitive root mod 11, 2⁹ ≡ 6, 2² ≡ 4, so s ≡ 0, 12 (mod 40). ✔
Note (not a defect): in the (a,b,c) = 3^a f₊^b f₋^c notation of Theorem C, Theorem B's d = 9f₋ is (2,0,1), while
the Theorem C table lists (0,2,1) at s ≡ 0, 12 — both fire there (script output); the table is consistent, just a
different choice.

**(ii) SG rules.** For all 27 vectors 0 ≤ a, b, c ≤ 2 I checked the identity and exact integer-valuedness of y, z on
every X mod 11 (polynomial P ∈ ℤ[X] over a constant L: L | P(r + 11j) for all j mod L). Firing residues X mod 11:
{2, 3, 4, 5, 6, 7, 8, 9}; dead: X ≡ 0 (impossible for X = 2^e), 1, 10. Via X = 2^{(s−4)/4}: dead s ≡ 4, 24 (mod 40)
exactly; every author-listed (a,b,c) fires at its residue. ✔ Positivity: f± have negative discriminant, K + d > 0. ✔

**(iii) ET/divisor classes**, each rebuilt by hand:
* n ≡ 0 (7): ES(7) = (2, 15, 210) scaled: (2n/7, 15n/7, 30n). n ≡ 0 (5): ES(5) = (2, 4, 20): (2n/5, 4n/5, 4n).
  n ≡ 0 (61): ES(61) = (16, 326, 2608·61)/… : (16n/61, 326n/61, 2608n) (identity checked).
* n ≡ 6 (7): 4/n = 7/(2(n+1)) + 1/(2n) + 7/(2n(n+1)) [numerator 7n + (n + 1) + 7 = 8(n + 1)].
* n ≡ 7 (15): x = (4n+2)/15, 4/n − 1/x = (n + 8)/(n(4n + 2)), minus 1/(4n) = 30/(4n(4n+2)) → z = 4n(2n+1)/15.
* n ≡ 13 (15): x = (4n+8)/15, remainder (n + 32)/(4n(n + 2)), minus 1/(4n) → z = 2n(n + 2)/15.
All six agree with the JSON certificate's coefficient lists; integrality on the class and non-negative coefficients
checked exactly. ✔

**(iv) Coverage.** ord₅2 = ord₁₅2 = 4, ord₇2 = 3, ord₆₁2 = 60, SG depends on s mod 40: true period lcm = **120**
(author: 360, a harmless multiple). Hand derivation: s ≡ 1 (3) → 7 | n; s ≡ 2 (3) → n ≡ 6 (7); s ≡ 3 (4) → 5 | n;
s ≡ 1, 2 (4) → n ≡ 7, 13 (15); s ≡ 0 (4) → SG unless s ≡ 4, 24 (40); the leftover s ≡ 4, 24 (40) ∧ s ≡ 0 (3) is
s ≡ 24, 84 (120), both ≡ 24 (60), and 3·2²⁴ + 1 ≡ 0 (mod 61). Script: no uncovered residue mod 120. ✔
(The memo's "s ≥ 10" restriction is a builder artefact; my checker verifies every s ≥ 1 directly.)

**(v) Exact solutions.** Script `review_r251_proth3.py 2000`: an exact Fraction-verified solution for every
1 ≤ s ≤ 2000 from the rebuilt rules; s = 0 (n = 4) is 1/2 + 1/3 + 1/6. Rule-free search `review_r251_brute.py 60`
finds an ES solution for every s ≤ 60 independently. ✔

**(vi) T1.** By hand: 3·2^s + 1 = m² ⟹ (m − 1)(m + 1) = 3·2^s with m − 1, m + 1 ∈ {2^a, 3·2^b} differing by 2 ⟹
m ∈ {5, 7} (plus n = 4 at s = 0): s ∈ {0, 3, 4}. Only s = 4 is ≡ 0 (mod 4) and it lies in the dead class s ≡ 4 (40),
handled by the divisor class 7 | 49. So no rule is asked to work at a square, and the dead residues are exactly the
neighbourhoods of X = ±1 (φ(±1) = 49), as claimed in §4.3 (whose attribution to Thm 3.3 is correct; φ has no real
root, X₀ = ±1 > ρ = −∞).

**(vii) Consistency with (J)22.** EXPONENT_COVERING Thm 1.4 + Cor 1.5 (re-read on main): ν(0) of 3·2^s + 1 is in
Sq^×, so no finite ET/divisor set covers {n_s : s ≡ 0 (mod L)} for any L. Since {s ≡ 0 (40)} contains s ≡ 0 (mod L)
for every 40 | L, the SG rule there cannot coincide (on its class) with any finite union of ET/divisor classes — and it
indeed is not polynomial in n: y has degree 8 in X with non-zero X³ coefficient (6n·f₋(X² + X + 2) contains odd powers
of X), while polynomials in n = 48X⁴ + 1 are polynomials in X⁴. The theorem is not a contradiction with Cor 1.5. ✔

**Verdict Theorem B: SOUND. Theorem C: SOUND.** Defects listed below (D1–D3) are MINOR.
