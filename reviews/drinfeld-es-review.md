# R181 — hostile review of O181 (DRINFELD_ES.md + BRAINSTORM/bsH_*)

Reviewer branch side-agent/review-drinfeld (merged side-agent/drinfeld-degree-k). From-scratch scripts:
`scripts/review_dr_*.py` (own F_p[T] arithmetic, own Cantor–Zassenhaus factorisation, own power-residue /
tame-symbol code; nothing imported from `scripts/bsH_*`). ES is not solved anywhere; nothing below changes that.

Status: IN PROGRESS.

## Per-claim verdicts (filled in incrementally)

### §1 Lemma 1.1, Prop 1.2, Thm 1.3 — SOUND (minor wording)
* Lemma 1.1 re-derived: (λ/ℓ)_k = λ^{(q^d−1)/k} = (λ^{(q−1)/k})^{1+q+…+q^{d−1}}, exponent ≡ d mod (q−1) hence
  mod k. SOUND. Checked on 200 random (λ, g) per q, all k | q − 1 (`scripts/review_dr_kpow.py`).
* Prop 1.2 re-derived: P ≡ −Aa²d (mod f); (−1/f)_k = ε^{deg f}; (Ad/f)_k = ε^{deg Ad·deg f}(f/Ad)_k =
  ε^{deg Ad(1+deg f)} since f ≡ −1 mod Ad; (a/f)_k = ε^{deg a deg f}(−1/a)_k = ±1, so (a²/f)_k = 1. Product
  ε^{(1+deg f)(1+deg Ad)−1}. All quantities monic (deg A ≥ 1 forces deg E < deg Aabd, so P is monic). SOUND.
  From scratch: random Type II data (a, b, c, d, A) with c a random monic divisor of a + b, q ∈ {7, 13, 19, 31},
  every k | q − 1 (incl. even k with ε_k = −1): 58 362 symbol tests, 0 mismatches; a control with P replaced by a
  random monic polynomial of the same degree gives uniformly distributed symbols (test is discriminating).
* Thm 1.3: (f/P)_k = ε^{n deg f}(P/f)_k = 1 for odd k; x^k − f then splits into distinct linear factors over F_P
  (p ∤ k, Hensel), so no place above P has local degree k and K = F(f^{1/k}) cannot embed in a degree-k division
  algebra with inv_P of exact order k (standard local–global embedding criterion; Reiner, *Maximal Orders*,
  Thm 32.15 / Pierce §18.4 — I could not open either; the criterion itself is classical and correctly stated).
  From scratch: 5 724 (P irreducible, odd k) tests, 0 mismatches. SOUND.
  Remarks (no defect): when k | deg f, f is monic of degree divisible by k, so f^{1/k} ∈ F_∞ and K also splits at
  ∞ — a second, independent reason for non-embedding; worth one sentence. The phrase "the order-k analogue of
  Diff = {P} is Diff = ∅" (§0) is interpretation (Assessment), since the choice of f^{1/k} as "the" degree-k CM
  datum is the author's.
* Rosen theorem numbering (Thm 3.5) not checkable here (book not in sources/); the reciprocity law used,
  (x/y)_k = ε_k^{deg x deg y}(y/x)_k for monic coprime x, y, is correct (Rosen Ch. 3, the d-th power reciprocity
  law) and is confirmed by the numerics above. Suggest "Rosen Ch. 3 (d-th power reciprocity law)" without number.
