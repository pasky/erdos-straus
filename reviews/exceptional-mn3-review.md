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

### 1.1 Numerics (EVIDENCE; `scripts/review_emn3_prop23.out.txt`)
`S(k,A,B) = Σ_{a≤A,b≤B} τ(kab²+1)` for 34 values of k (1…6, all primorials up to 29#, primes
101…100003, 2·3·1009, 4·1009·1013, 2^10, 3^8) and boxes (A,B) ∈ {(2,3000),(6,1000),(40,150),(150,40)}.
* `S/((φ(k)/k)·AB log max(A,B)·Λ)` ∈ [0.18, 1.6] over all 136 cases, non-increasing in k: no sign of
  a hidden k-dependence in the constant (the small-A boxes are where `Λ = 1+log(1+k)` is active).
* The gain is real and visible: `S/(AB log B)` is 2.3–3.0 for prime `k ≈ 10⁵` but 0.85–1.28 for
  `k = 29# ≈ 6.5·10⁹` (larger n, yet fewer divisors), ratio ≈ `φ(k)/k`-driven.
* ET's `log(1+k)` normalisation decays to 0.04 — consistent with ET's bound being lossy in k.

## 2. Prop 2.5 and Theorem L'

Re-derived line by line.
* Substitution `ma²d+1 = k a'²d'+1`, `k = ms²t`, `φ(k)/k ≤ φ(m)/m`: correct; this is the only way the
  gain enters, and the BT factor `1/φ(m)` (from `φ(mad) ≥ φ(m)φ(ad)`) is then cancelled to `1/m`.
* Exponent bookkeeping with l = 30: `D' ≥ max(A',k^{1/28}) ⇒ kA'² ≤ D'^{28+2}`; `A' > max(D',k^{1/28})
  ⇒ kD' ≤ A'^{29}`. Correct. Size hypotheses of Prop 2.3 (`≥ ω(2k)+2`) hold once `k^{1/28} ≥ ω(2k)+2`,
  true for k ≥ m₀ (absolute, since `ω(n) ≪ log n/log log n`). Correct.
* Λ: `Λ ≤ 2` unless `D' < k^{1/3} log²(2kD')`; number of such dyadic D' ≪ `log(2k) + log L`. Per
  (s,t): `(st)^{−2}[L·log X + (log 2k + log L) log X log(1+k)] ≪ (st)^{−2}[L² + L log²(2ms²tL)]`, and
  `Σ_{s,t}(st)^{−2} log²(ms²tL) ≪ log² m` using `log L ≤ log m`. Correct.
* Block sum `Σ_{j≤2L} 1/j ≍ log L`: count `≪ (N/φ(m))·(φ(m)/m)(L²+L log² m) log L`. Correct.
* Tiny boxes: `n ≤ k(2A')²(2D') ≤ 8k^{1+3/28} ≤ 8k^{1.11}`; `τ(n) ≪ n^{0.0108} ≪ k^{0.012}` (absolute
  constant, effective). Occurrence: `X < st·a'd' ≤ 4st·k^{1/14} ≤ 4m^{1/14}(st)^{8/7}` (s²t ≤ (st)²).
  Mass: grouping by `u = st` (multiplicity τ(u) — this is where the `τ(st)` comes from; the text should
  say so, m2), `Σ_{u≥U} τ(u)u^{−2}(mu²)^{0.012}·#boxes ≪ m^{0.013} min(1, U^{−0.97})`,
  `U = (X/4m^{1/14})^{7/8}`, giving exponent `0.976·7/8 ≈ 0.85`. Summed over blocks: ≪ `log m` blocks
  with X ≤ m^{0.072}, geometric beyond: `≪ m^{0.014}`. Count `N m^{0.014}/φ(m) ≪ (N/L)m^{−0.35}` needs
  `L·m^{0.014}·log log m ≤ m^{0.65}`: fine for `L ≤ m^{1/2}`. **Exponents correct.**
* Theorem L': MN2 Prop 3.2 already has `/m`; `m^{0.02}/m ≤ m^{−0.35}`. The consequence: I checked
  `L² log² m ≤ L³ + log⁶ m` (case split `log² m ≤ L`), that `L³ log L/m → 0` forces m → ∞ (N ≥ 16),
  and that the `log m > L/10` range (MN2 Lemma 3.5, `e^{CL/log L}/m = m^{O(1/log L)−1}`) also → 0.
  Also `L > m^{1/2}` makes the hypothesis `L³ log L/m → 0` impossible, so the range restriction is harmless.
* Propagation through MN2: MN2 Prop 3.4's skeleton (PW (3.2), ET (A.12), BT weight) is reused
  unchanged; only MN2 Lemma 3.3 is replaced by Prop 2.3, and MN2 Prop 3.2 (Type II) already had `1/m`
  after the R102A/B repairs. MN2's lossy-box criterion `D' < k log⁴` is replaced by the sharper
  `D' < k^{1/3} log²`; both are only used through a box *count* ≪ `log(2k)+log L`, so nothing else changes.

| Claim | Verdict |
|---|---|
| Prop 2.5 | SOUND (exponents verified) |
| Theorem L' | SOUND; label should add PV and "rel. MN2 Prop 3.2" (m3) |
