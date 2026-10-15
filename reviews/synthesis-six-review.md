# R245 — hostile review #1 of O238 Synthesis VI (SYNTHESIS_SPARKS6.md + BRAINSTORM/s6_*.md)

Reviewer: R245 (side-agent/review-synthesis-six). Base: merge of side-agent/synthesis-six at a472a48b.
From-scratch scripts: `scripts/review_r245_cert.py`, `scripts/review_r245_small.py` (no s6_*/z8/ec_cover code imported;
only the JSON parameters are read).

## Summary verdicts (filled in incrementally)

| claim | verdict |
|---|---|
| Thm 1.1 (ES for all 4^s + 105), Lemma 1.0, 1.0′ — the mathematics | SOUND (independently re-verified) |
| Thm 1.1 — exposition / labels | SOUND-AFTER-REPAIRS (minor) |

## 1. Headline Thm 1.1 — independent verification

**(a) ET classes, rebuilt from parameters.** `review_r245_cert.py` rebuilds each of the 13 classes from `params` only:
* `II2` = ET Prop 1.9 Type II family 2 ("−4a²d mod f, 4ad | f + 1"; checked against sources/elsholtz-tao-1107.1010.pdf §10:
  sextuple (a, ce − a, (f+1)/(4ad), d, (n+4a²d)/f, f), π^II = (abd, acdn, bcdn)). For all 9 II2 classes: f = M, 4ad | f + 1,
  r ≡ −4a²d (mod f); the sextuple satisfies ET (2.13)–(2.20) identically in n; the rebuilt (x, y, z) equals the JSON
  polynomials; 4/n = 1/x + 1/y + 1/z holds in ℚ(n).
* `D` (divisor) classes M = p ∈ {11, 41, 13, 19}, r = 0: (x, y, z) = (n/p)(X, Y, Z) with 4/p = 1/X + 1/Y + 1/Z checked
  exactly ((3, 34, 1122), (11, 154, 6314), (4, 18, 468), (5, 96, 9120)).
* Integer-valuedness: for every polynomial, g(t) = f(r + Mt) is checked integer at t = 0..deg g (which is equivalent to
  integer-valuedness on the whole class). Positivity: all coefficients ≥ 0 and not all zero, so positive for every n ≥ 1
  (stronger than the doc's "n ≥ 4⁴").
* Periodicity: all M odd, ord_M(4) ∈ {5, 6, 9, 10, 15, 20, 30} all divide 360, so n_s mod M depends only on s mod 360
  **for every s ≥ 0** (pure periodicity, M odd).
* Coverage: uncovered s mod 360 = exactly {34, 124, 214, 304} = {s ≡ 34 (mod 90)}. ✔

**(b) Exponential class.** sympy: 4x − n = 151; 2(32u+33)(u²−u+1) = 151A identically; 4/n = 1/x + 1/y + 1/z in ℚ(u).
A(32 + 151t) = 1459264t³ + 928046t² + 196734t + 13902 (integer coefficients ⇒ A ∈ ℤ_{>0} on the whole class; t ≥ 0 since
u ≥ 1). ord₁₅₁(4) = 15, 4¹⁰ ≡ 32 (mod 151). s ≡ 34 (mod 45) ⇒ s − 4 ≡ 30 (mod 45) ⇒ 3 | s − 4 and (s−4)/3 ≡ 10 (mod 15) ⇒
u ≡ 32 (mod 151). Checked also by brute force for all such s < 1354. Every uncovered residue {34, 124, 214, 304} is ≡ 34 (mod 45). ✔

**(c) Exact solutions.** For every 0 ≤ s ≤ 2000 an exact positive solution 4xyz = n(xy + yz + zx) was built from my
rebuilt classes (1979 by ET classes, 22 by the exponential class) — the doc's own check went to s ≤ 1500.
Independent brute-force (no certificate) found solutions for s ≤ 8 (`review_r245_small.py`).

**(d) T1 / non-square control.** All 9 II2 residues r are non-squares mod M (exhaustive), so those classes contain no square.
The 4 divisor classes (r = 0) contain squares, which is fine (they are not polynomial-in-n-on-a-primitive-class identities that
would contradict Mordell: they are multiples of a fixed solution). Exponential class: see §2 below.

**Verdict on the mathematics of Thm 1.1: SOUND.** I could not find any gap: the proof is a finite, fully explicit certificate
plus one cubic identity, and both halves re-verify from scratch.
