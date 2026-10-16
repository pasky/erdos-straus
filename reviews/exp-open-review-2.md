# EXP_OPEN (O246) — hostile review #2 (R258), round 1

Reviewer R258. Round 1: no edits to the author's files. Scripts written from scratch: `scripts/review_r258_*.py`
(no z19_/z15_/z14_ imports). Document reviewed: EXP_OPEN.md at side-agent/exp-open (merged into this branch).

## Summary verdicts
| claim | verdict |
|---|---|
| Theorem 3.1 (ES for every 63·2^s + 1) + Theorem 2.3 | **SOUND** (minor wording defects D1–D3) |
| Theorem W / Lemmas 1.1–1.5 / Cor 1.7 / Comp 1.6 | (pending) |
| Prop 2.1, Reduction 2.5, Prop 4.1, Comp 4.2, labels, novelty | (pending) |

## 1. Theorem 3.1 / Theorem 2.3 — SOUND

Independent checker `scripts/review_r258_cert63.py` (pure `fractions`, no sympy; reads only (M, r, xyz) from the JSON,
ignores the author's `fam/exps/L_M` metadata). Run: `uv run python scripts/review_r258_cert63.py 1500` — all PASS:
* (A) all 18 classes: identity 4xyz = n(xy + yz + zx) as polynomials in n over ℚ; integer-valuedness on n = r + Mt via
  Newton forward differences (complete for polynomials); positivity for n ≥ 63·2^10 + 1 by Taylor-shifting to
  n = 64513 + u and checking every coefficient ≥ 0 (stronger and cleaner than the author's Cauchy bound); for every M,
  v₂(M) ≤ 10 and ord_{odd(M)}(2) | 2520, so n_s mod M is periodic of period | 2520 on s ≥ 10; r ≡ 1 (mod 2^{v₂(M)}).
* (B) coverage: the 18 classes cover every s mod 2520 except **{0, 840, 1680}** — all ≡ 0 (mod 24), hence covered by the
  moving class. (See D1: the text says the ET part leaves "exactly s ≡ 0 mod 2520"; that is the z15_tree statement, not
  this certificate.)
* (C) moving class: c·n = 4abcd − a − b checked as a polynomial identity in Y (n = 63Y³ + 1), which is equivalent to
  4/n = 1/(abd) + 1/(acdn) + 1/(bcdn) after multiplying by abcdn. Integrality re-derived by hand: Y = 2^{8j}, j ≥ 1;
  2^8 = 256 ≡ 1 (mod 85) (ord₅2 = 4, ord₁₇2 = 8), and 4 | Y; so Y ≡ 1 (mod 85), Y ≡ 0 (mod 4), whence
  21Y + 64 ≡ 85 ≡ 0 and 63Y³ + 3Y² − 9Y + 28 ≡ 85 ≡ 0 (mod 85), both ≡ 0 (mod 4): 340 | both, for ALL j ≥ 1 (also
  checked over the unique residue Y mod 340). Positivity: 63Y³ + 3Y² − 9Y + 28 > 0 for Y ≥ 1. The author's algebra
  f = 340b − n = 3(Y² − 3Y + 9), f′ = 340c − 1 = 21(Y + 3), ff′ = 63(Y³ + 27) = n + 1700 = n + 4a²d, and
  (4abd − n)(4acd − 1) = 4ad(4abcd − b − cn) + n re-derived: correct.
* (D) explicit exact solutions for every s = 0..1500 (10 by bounded search for s ≤ 9, 62 moving, 1429 ET-only); at
  every s ≥ 10 EVERY applicable ET class (not just the first) was evaluated and verified exactly.
* (E) squares: (m − 1)(m + 1) = 63·2^s with gcd 2 forces 2^{s−2}v = u ± 1, uv = 63; the only solutions are s = 0 (n = 64,
  even) and s = 8 (n = 127²) — confirmed numerically for s < 400. 127² lies in D₁₂₇ (s ≡ 1 mod 7) whose formula is a
  genuine solution, and s = 8 < 10 is brute-forced anyway. T1 control: every non-divisor class has r a NON-square mod M
  (all 14 checked), divisor classes have r = 0.
* Unit-square point: at μ = 0, n → 64 = 8² at every odd place and n → 1 at 2, so n_μ is a square in Ẑ; every
  ET/divisor class has r a non-square or q | n (q odd, q ∤ 64), so none contains μ = 0 (consistent with (B): residue 0
  uncovered). The moving class does contain μ = 0, so it is genuinely outside the ET/divisor menu (and is visibly not
  polynomial in n: x = (n − 1 + 3Y² − 9Y + 28)/4).
* Context the author omits (not a defect of the proof): mod 840, n_s ≡ 1 (mod 168) and n_s ≡ 3·2^s + 1 (mod 5), so
  Mordell's classical identities already settle every s ≢ 0 (mod 4); only s ≡ 0 (mod 4) (n ≡ 169 mod 840) is
  "hard". Worth one sentence in Scope.

Defects:
* **D1 (MINOR)** Thm 3.1 proof (b): "ET/divisor classes alone leave exactly s ≡ 0 mod 2520 (`z15_tree.py …`)" is placed
  as if describing the certificate; the certificate's 18 classes leave {0, 840, 1680} mod 2520. Repair: "the 18 classes
  leave s ≡ 0, 840, 1680 (mod 2520), all ⊂ {s ≡ 0 mod 24}; (a larger z15_tree run leaves only s ≡ 0 mod 2520)".
* **D2 (MINOR)** Theorem 2.3 says "s ≡ 0 (mod 24), s ≥ 6"; effectively s ≥ 24 (s = 0 fails: c = 85/340). Repair: "s ≥ 24".
* **D3 (MINOR)** Thm 3.1 checker description "positivity (Cauchy bound below 63·2^10)": fine, but also state that
  n_s mod M is periodic only for s ≥ v₂(M) (max v₂(M) = 3 here), which is why the cut is s ≥ 10.
