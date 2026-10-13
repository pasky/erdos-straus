# R169 — hostile review of O169 `DEDEKIND_ES.md` (Parts I–II)

Reviewer: R169 (side-agent/review-dedekind). Author branch merged: side-agent/dedekind-sums.
From-scratch scripts: `scripts/review_dk_*.py` (none of the author's `dk_*` code reused).

## Summary verdicts (filled in progressively)

| Claim | Verdict |
|---|---|
| Lemma 1.1 (+ Cor 1.2, D2, D3) | pending |
| Prop 3.1 | pending |
| Thm 4.5 | pending |
| Cor 4.6 | pending |
| §8 (sign mod 4, Klein, rotation, scaling) | pending |
| §9.2 lemma | pending |
| CONJECTURE SQ₅ / §9.1 evidence | pending |
| §10.1 complexity | pending |

## Defects

(numbered below as found)

## 1. Lemma 1.1, Cor 1.2, (D2), (D3) — SOUND (minor citation/wording repairs)

Re-derived by hand:
* `[[v,t,u]] = v − u/(tu−1) = (tuv−u−v)/(tu−1)`; `(tu−1)(tv−1) = t(tuv−u−v)+1`; `A < n` since
  `n − A = (v−1)(tu−1) − u ≥ u(t−1) − 1 > 0` (the proof only states `tv−1 < n`; the other bound is the same
  by u↔v symmetry). HJ uniqueness ⇒ bijection. Boundary `u = 1`: `n = v(t−1) − 1`, `n/(t−1) = [[v, t−1]]` ✓.
* Cor 1.2 Type I: `4bcd = c + p(b+1)` reduces, with `p+u+v = tuv`, to `(tu−1)(p+v) = u(tp+1)` ✓; `u | p+v` since
  `p+v = u(tv−1)` ✓. Type II: `4abc − a − b = p` with `(a,b,c) = (u,v,t/4)` ✓. Matches CONDITIONAL_ES Lemma 1.1
  (c,f,g) = (v,u,t) exactly.
* (D3): from (D2) for A and n−A plus Riemenschneider `Σ(b_i−2) = r'−1` one gets `12s = r' − r − 1 + (A+A*)/n` ✓.
  On a certificate `r' = t+u+v−5` ✓.

From scratch (`scripts/review_dk_core.py 5000 250`): Lemma 1.1 as a set identity, word `[[v,t,u]]`, `A* = tv−1`,
`AA* = tn+1`, and the exact ES identities of Cor 1.2 and of the e-slice (see Thm 4.5 below) for **all** n ≤ 5000
(not only primes/squares): 0 failures. (D2), (D3), Riemenschneider duality and (R) by the *defining* sawtooth
sum (no reciprocity algorithm) for all coprime pairs with n ≤ 250 (19 022 pairs): 0 failures.

**Citation check.** (R) is in Rademacher–Grosswald, *Dedekind Sums* (Carus Monogr. 16, 1972), Ch. 3 §C, eq. (44),
p. 34: `12k s(h,k) ≡ k + 1 − 2(h/k) (mod 8)` for odd k, (h,k) = 1, attributed to Dedekind — verified in a scanned
copy (webhomes.maths.ed.ac.uk/~v1ranick/papers/rademacher2.pdf, OCR). Statement as used is correct. (D2) I could
not check against Hirzebruch–Zagier 1974 (no access); it is numerically exact on all 19 022 pairs above and is a
standard formula (Zagier/Barkan–Hickerson–Knuth/Myerson form).

## 2. Prop 3.1 — SOUND (one false numerical side-remark)

The proof is (R) + (D2) + a finite mod-8 polynomial check; both inputs are classical and verified above, and the
polynomial `2(A/n) ≡ n+1 − n(t+u+v−9) − (tu−1) − (tv−1) (mod 8)` is a function of (t,u,v) mod 8 (n is a polynomial
in t,u,v). `scripts/review_dk_cells.py` recomputes the 512-cell table independently: 160 admissible cells, the value
is always ±2 mod 8, and it is −2 on every cell with `4 | tu−1` or `4 | t`. No circularity: Prop 3.1 uses nothing
about ES. Credit to redteam-automorphic Lemma 5.2 is correct: there `(d/p) = −1` with d = A/4, and
`(A/p) = (4/p)(d/p) = (d/p)`.

## 3. Theorem 4.5 — SOUND (repair: write out the e-slice ES identity)

* Proof re-done: polynomial cell check (`review_dk_cells.py`, `poly_cells`): 160 admissible mod-8 cells,
  120 with value −1, all of them satisfying one of the five conditions, 40 with value +1, none of them
  satisfying one. 0 failures.
* Brute force with a direct Jacobi symbol, `review_dk_cells.py 1000000`: **21 430 357** words with n ≡ 1 (4),
  n ≤ 10⁶ (the same count as the author's), 0 failures, every mod-8 cell constant (no mixed cell), and 0 slice
  words at odd squares.
* **Slice identification checked.** Conditions 1–3 are Cor 1.2 (Type I, one denominator divisible by n; Type II,
  two). For `4 | u = 4w`, `f = tv−1`: `n + v = u(tv−1) = 4wf`, so `f | N = (n+v)/4` and `f ≡ −1 (mod v)`. This is
  the CONDITIONAL_ES §1 "Type II slice a = 1" (`b | (p+e)/4`, `b ≡ −1 (mod e)`, with b = f, e = v), i.e.
  `−1 ∈ Σ_e(N)` of LONGSHOT_PIGEONHOLE with (a,b) = (f,1). The explicit Type II solution, which the document does
  not write down, is
  `4/n = 1/(wf) + 1/(tnw) + 1/(tnwf)`
  (from `4/n − 1/N = v/(nN)` and `v = (f+1)/t`). It is verified in exact rationals for all n ≤ 5000
  (`review_dk_core.py`). `4 | v` is the u↔v reversal (n is symmetric in u, v).
* The proof is complete relative to (R) and (D2), which are proven classical theorems, so the label PROVED is
  fair. One could make it self-contained by Jacobi reciprocity alone (n = vA − u with n ≡ 1 (4) gives
  `(A/n) = (−u/A)` for odd A, and so on), but this is optional.
