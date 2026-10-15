# R252 — hostile review #2 of O240 (MENU_STERILITY.md, memos z15_*)

Reviewer: R252 (round 1, no edits to the author's files). Branch reviewed: side-agent/menu-sterility (merged at bf14ed4c).
From-scratch scripts: `scripts/review_r252_*.py` (no z15_/z8/ec_cover imports).

## Summary verdicts
| claim | verdict |
|---|---|
| Theorem B (window-11 SG identity, s ≡ 0, 12 mod 40) | SOUND |
| **Theorem C (ES for every 3·2^s + 1)** | **SOUND** (minor presentation defects only) |
| (vii) consistency with (J)22 Cor 1.5 | SOUND |
| (pending below) Theorem A, Prop 4.1, Prop 4.3, Prop 3.1, Prop 5.1, labels, novelty | see sections |

## 1. Theorem B / Theorem C (HEADLINE) — independent re-derivation

Script: `scripts/review_r252_proth3.py 2000` (sympy; ~1 min). Output (abridged):
```
Thm B identity: OK
window-11 SG rules (a,b,c) -> X residues mod 33: (0,0,2):[2,3,13,14,24,25] (0,1,2):[5,7,16,18,27,29]
  (0,2,0):[8,9,19,20,30,31] (0,2,1):[4,6,15,17,26,28] + 8 rules with a ≥ 1 (denominator 33)
s mod 40:  4 -> X≡1: NONE ; 24 -> X≡32≡−1: NONE ; all other s ≡ 0 (4) have ≥ 2 rules
author's (a,b,c) table: each valid on its class
ET identities: OK ; period: 120 ; uncovered residues mod 120: [] ; exact ES solutions s ≤ 2000: failures []
```

(i) **Identity and integrality (Thm B).** Re-derived by hand: with K = (n + 11)/4 = 3f₊f₋ (f± = 2X² ± 2X + 1; 4X⁴ + 1 = f₊f₋),
4/n − 1/K = 11/(nK), and for any d: 11/(nK) = 1/y + 1/z with y = n(K + d)/11, z = nK(K + d)/(11d). For d = 9f₋:
K + d = 3f₋(f₊ + 3) = 6f₋(X² + X + 2), so y = 6nf₋(X² + X + 2)/11, z = nf₊·6f₋(X²+X+2)/33 = 2n(4X⁴+1)(X²+X+2)/11 —
exactly the stated denominators. Needed divisibility: only 11 | X² + X + 2 (all other factors are integer polynomials);
X² + X + 2 ≡ 0 (11) ⟺ (2X + 1)² ≡ −7 ≡ 4 ⟺ X ≡ 4, 6 (mod 11). ✓. Note d = 9f₋ is the (a,b,c) = (2,0,1) rule; the table in
Thm C(a) uses (0,2,1) for the same classes — both are valid (my enumeration finds both), so no inconsistency, but the text
should say which d Theorem B uses (MINOR D1).
X = 2^{(s−4)/4}: ord₁₁(2) = 10, 2⁹ ≡ 6, 2² ≡ 4 ⟹ s ≡ 0, 12 (mod 40) ✓.

(ii) **Other window-11 rules.** All 64 vectors (a,b,c) ∈ {0..3}³ with z a polynomial were enumerated; integrality is a condition
on X mod 33 (denominators divide 33; ord₃₃(2) = 10, so it depends on s mod 40 only). Exactly the author's eight residues
{0, 8, 12, 16, 20, 28, 32, 36} mod 40 are covered, and the author's table (a,b,c) per residue is valid on each.
Residues 4, 24 (X ≡ ±1 mod 11) have NO rule with exponents ≤ 3 — consistent with §4.3 (T1 at X = ±1).
Positivity: K, d, f± > 0 for real X, so x, y, z > 0 for every integer X ≥ 1 ✓. s ≡ 0 (40) needs s ≥ 40 (X = 1/2 at s = 0); the
text's "s ≥ 4" plus s ≡ 0 (40) already implies this.

(iii) **ET/divisor classes**, rebuilt by hand (not read from the certificate) and checked symbolically:
n ≡ 0 (7): (2n/7, 15n/7, 30n); n ≡ 6 (7): (2(n+1)/7, 2n, 2n(n+1)/7); n ≡ 0 (5): (2n/5, 4n/5, 4n);
n ≡ 7 (15): ((4n+2)/15, 4n, 4n(2n+1)/15); n ≡ 13 (15): ((4n+8)/15, 4n, 2n(n+2)/15); n ≡ 0 (61): (16n/61, 326n/61, 2608n).
These match the certificate's six classes exactly. (They are ET Prop 1.9-type / divisor identities; correctness here needs only
the identity + integrality, which I checked; no appeal to ET is necessary.)

(iv) **Coverage and period.** By hand: mod 7, s ≡ 1, 2 (3) give n ≡ 0, 6; mod 15 (resp. 5), s ≡ 1, 2, 3 (4) give n ≡ 7, 13 (mod 15),
0 (mod 5). Left: s ≡ 0 (12); intersected with the SG-dead residues s ≡ 4, 24 (40) this is s ≡ 24, 84 (mod 120), both ≡ 24 (mod 60),
and 3·2^24 + 1 ≡ 0 (mod 61) with ord₆₁(2) = 60. So the true period is lcm(40, 3, 4, 60) = **120** (the author's L₀ = 360 is a
harmless multiple); the computer confirms 0 uncovered residues mod 120. Every s ≥ 1 is covered by a rule valid at that s (no
"s ≥ 10" threshold is needed; MINOR D2), and s = 0 (n = 4) is 1/2 + 1/3 + 1/6.

(v) **Exact solutions.** For every s ≤ 2000 my checker produces (x, y, z) from the rules above and verifies 4/n = 1/x + 1/y + 1/z in
exact rationals with x, y, z positive integers: 0 failures. Independent brute force for s ≤ 8 also finds solutions (sanity only).
I did not use the author's certificate file except to compare the six classes.

(vi) **T1.** 3·2^s + 1 = y²: for s ≥ 2, ((y−1)/2)((y+1)/2) = 3·2^{s−2} with coprime consecutive factors ⟹ {3, 2^{s−2}} consecutive
⟹ s = 3, 4; plus s = 0. So squares are exactly s = 0, 3, 4 (4, 25, 49) as claimed. s = 4 (X = 1) is in the SG-dead class 4 (40) and is
covered by the divisor class n ≡ 0 (7); s = 3 is not ≡ 0 (4); s = 0 has X ∉ ℤ. So no rule fires at a square. ✓ (The general
statement "48X⁴ + 1 is a square only for X = 1" is only numerically checked by the author — fine as stated, it is not used.)

(vii) **Not an ET/divisor class.** y = n(K + f₊²f₋)/11 (the s ≡ 0 (40) rule): since f₊(−X) = f₋(X), y(−X) ≠ y(X), so y is not a
polynomial in X⁴, hence not a polynomial in n = 48X⁴ + 1 (the same holds for every rule with b ≠ c, i.e. all eight used). The
d = 9f₋ form of Theorem B likewise. So the dissolving class is genuinely outside the ET/divisor menu, and Cor 1.5 (no finite
ET/divisor covering of {s ≡ 0 (L)}) is not contradicted: x = K is polynomial in n, but y, z are polynomial only in
X = ((n − 1)/48)^{1/4}. I re-read EXPONENT_COVERING Thm 1.4/Cor 1.5 on main: the hypothesis is exactly "ET and divisor classes"
(identities polynomial in n on congruence classes of n), so the logic "proved uncoverable by M₀, yet ES holds" is correct.
Small wording point: "the class {s ≡ 0 (40)} is the n-congruence class n ≡ 4 (mod 2⁴⁰ − 1), n ≡ 1 (mod 16)" should read "is the
intersection of the family with" that class (true: ord of 2 modulo (2⁴⁰ − 1)/3 is 40) (MINOR D3).

**Verdict Theorem C: SOUND.** The proof is complete and elementary once the rule table is fixed; computer assistance is only
needed for the finite residue bookkeeping, which is small enough to be done by hand (done above). Label "PROVED (computer-
assisted)" is correct; it could even be "PROVED" with the by-hand coverage argument of (iv) inserted.

## Defects
(collected at the end)
