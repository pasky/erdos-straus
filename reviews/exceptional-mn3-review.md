# R108 — hostile review of EXCEPTIONAL_MN3.md (task O108, branch side-agent/et-typei-loglog)

Reviewer branch: `side-agent/review-emn3`. Source checked: ET = arXiv:1107.1010v6
(`sources/elsholtz-tao-1107.1010.pdf`, pp. 25–32 read via pdftotext). From-scratch scripts:
`scripts/review_emn3_*.py` (+ `.out.txt`).

## Verdict summary (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Lemma 2.1 (coprime harmonic sums) | SOUND |
| Lemma 2.2 (PV / Kronecker PV) | SOUND |
| Prop 2.3 (ET Prop 1.4 with φ(k)/k) | SOUND (minor presentational defects) |

## 1. Lemma 2.1, Lemma 2.2, Prop 2.3 — re-derivation

**Lemma 2.1.** Re-derived: n ≤ y coprime to K has all prime factors ≤ y outside K, so
`W_K(y) ≤ Π_{p≤y,p∤K}(1−1/p)^{−1}`; the swap to `φ(K)/K` costs `Π_{p|K,p>y}(1−1/p)^{−1} ≤ e^{2ω(K)/y}`
(`−log(1−x) ≤ 2x` for x ≤ 1/2). Correct.

**Lemma 2.2.** (a) `(·/q)` for non-square odd q is non-principal; the imprimitive-PV reduction is
standard. (b) For `D = −4ka < 0`, `D ≡ 0 (4)`, the Kronecker symbol χ_D is a character mod |D|,
non-principal since D is not a square, `χ_D(q) = (4/q)(−ka/q) = (−ka/q)` for odd q, 0 for even q.
Correct. (Only a fixed real character is needed, so the classical PV constant is uniform.)

**Prop 2.3 hypotheses vs ET Thm 7.1 (p. 25).** Thm 7.1 needs: non-negative integer coefficients
`≤ N^l`, and `ρ(p^j) ≤ C` for all prime powers; conclusion `Σ_{n≤N} τ(P(n)) ≪_{D,l,C} N Σ_{m≤N} ρ(m)/m`.
No irreducibility. (a): `P(a) = kb²a+1`, coefficients `≤ kB² ≤ A^l`, ρ(p^j) ∈ {0,1}, and
`Σ_{m≤A} ρ(m)/m = W_{kb}(A) ≤ W_k(A)` — correct. (b): `P(b) = kab²+1`, coefficients `≤ kA ≤ B^l`,
ρ(p^j) ≤ 4 (I recomputed: ρ(2)=1, ρ(4)∈{0,2}, ρ(2^j)∈{0,4} for j≥3 when ka odd; odd p ∤ ka: Hensel,
≤ 2) — correct; ET p. 30 states the same.

**The (m₀,k)=1 indicator.** Re-derived case by case (odd m₀):
* `(m₀,k) > 1`: `P ≡ 1 (mod p)` for `p | k`, so ρ = 0; RHS 0 by definition.
* `(m₀,k)=1`, `(m₀,a) > 1`: ρ = 0; RHS `= Π_{p^j∥m₀} Σ_{i≤j} (−ka/p^i)`, factors with `p | a` are 1,
  others ≥ 0 — so RHS ≥ 0 = LHS.
* `(m₀,ka)=1`: ET p. 31. Correct.
Brute force (`review_emn3_prop23.py`, part 1): all k ≤ 40, a ≤ 12, odd m₀ ≤ 400 — **0 failures**;
ρ(2^j) ≤ 4 for K < 200, j ≤ 8 — 0 failures.
ET indeed drop the indicator: their final sum (p. 31, display before (7.11)) is
`Σ_{q:(q,2k)=1} Σ_a (−ka/q) Σ_{m≤B: q|m} 1/m`, i.e. `n = m/q` unrestricted, which is where the
`log B` instead of `(φ(k)/k) log B` enters. The author restricts `n` to `(n,2k)=1`: legitimate,
because the indicator `(m₀,k)=1` is a property of `m₀ = qn` and (q,k)=1 is forced anyway.

**q-ranges.** The four ranges {squares ≤ Q₂}, {non-squares ≤ Q₁}, {non-squares in (Q₁,Q₂]},
{all q > Q₂} *are* a partition once the square range is read as "squares ≤ Q₂" (the text bounds all
squares, which dominates since square terms are ≥ 0). So the "non-partition" remark in the text is
correct but unnecessary — see defect m1.
* Small q: `Σ_{a≤A} (−ka/q) = (−k/q) Σ_{a≤A} (a/q)`; PV for the non-principal `(·/q)`;
  `Σ_{q≤Q₁} W(B/q) q^{−1/2} log q ≤ W(B) · O(√Q₁ log Q₁)` — correct. (ET used the period bound O(q)
  and silently mishandled squares — "sums to zero" is false for square q; the author's separate
  square range repairs ET as well.)
* Middle: trivial, correct.
* Large q: weight `g(q) = W(B/q)/q` is positive non-increasing, partial sums of χ_D bounded by
  `C√(4ka) log(4ka)`; Abel gives `≤ 2·sup|S|·g(Q₂⁺) ≤ … W(B/Q₂)/Q₂`. Correct; the `(q,k)=1`
  restriction is automatic since χ_D(q) = 0 when (q,2ka) > 1.
* Choice 1: checked both sub-cases `Q₂ = kA ≥ Q₁` (middle log ≤ log k + O(1), tail
  `A^{1/2}k^{−1/2} log(2kA) ≪ A`) and `Q₂ = Q₁ > kA` (tail `≤ W(B) log(2kA) log(2A) ≪ A W(B)`).
  Choice 2: both PV and tail give `A^{1/2}k^{1/6} log(2kA)`. Correct.
* `Σ_j ρ(2^j)/2^j ≤ 1 + 4·1 = 5 ≤ 9` — the constant 9 is safe.

**Numerics (from scratch, part 2 of the script).** See §1.1 below.
