# z52d avenue — batch P06 (98 items) summary
ES is OPEN. Rows: `out_P06.jsonl`. Batch content: mostly probability/heuristics and sibling/calibration items (45 rows have role "calibration"). Per-row labels are Assessments unless a PROVED/CERTIFIED source is cited.

**Status × plausibility** (columns 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (mostly calibration facts; gap named) | 39 | 0 | 0 | 2 | 41 |
| circular | 23 | 0 | 0 | 0 | 23 |
| known-false | 14 | 0 | 0 | 0 | 14 |
| unclear | 12 | 2 | 0 | 0 | 14 |
| open-plausible | 0 | 2 | 1 | 2 | 5 |
| harder-than-open | 1 | 0 | 0 | 0 | 1 |
Novelty: 0 → 56, 1 → 41, 2 → 1 (Z0863: a sub-lottery, no proof role).

**Plausibility ≥ 2 AND novelty ≥ 1** (none yields ES; all are side theorems)
* **Z0240** (plaus 3): #{n = a² + b⁴ ≤ X with no (★) certificate} = o(X^{3/4}/log X), so ES for almost all primes a² + b⁴ — via a 2-D large sieve on (a, b) with the classes a² + b⁴ ≡ −u (mod 4uC − 1) plus Friedlander–Iwaniec's lower bound. B6; an almost-all theorem on a thin set.
* **Z1760** (plaus 3): M₀(p) = (3/(2π²)) log²p + b log p + c + O(p^{−δ}) (Mellin on Σ 1/φ(4uB) over the hyperbolic region). Main term only.
* **Z0417** (plaus 2): a CF folding (Niederreiter-type) construction giving ES₅ words for every member of a thin family (target: the open 15·2^s + 1). Thin families only ((J)76, (J)84).
* Plaus ≥ 2 with novelty 0: Z1525 (Chebyshev gives only X/log²X; Vaughan is far stronger), Z0599 (no covering-type failure, follows from (D)30).

**The one item with an ingredient not in the repo, plausibility 1:** Z0596 (Legendre's negative-Pell proof as the template for a primality-forced descent on the CF cycle of √p, used as roots in the forest F_p). Cheap check run here: with the cycle norms and partial quotients as roots, one-step forest neighbourhoods miss a bichromatic edge at 6 of 1610 primes < 3·10⁴ (577, 1129, 7057, 8761, 11257, 19441) — `scripts/z52d_avenue_P06_pell_roots.py`. Next step: whole components, p ≤ 10⁷.

**Recurring missing theorems** (items that reduce to the same statement)
1. *One tied-divisor event / H⁻_BM at each p* (circular): Z0805 (two-line union), Z1349 (cavity = character expansion), Z2319, Z2384 (fixed-p average over C: modulus = variable), Z0389 (Ono–Sound: no cusp part), Z1685 (GGZ: L-values only in the main term), Z1648, Z2281 (Helfgott/EFL: nothing to make effective), Z0223, Z0248, Z2740 (Thue/pigeonhole: height vs class), Z1523, Z2220, Z2291 (divisor-form re-indexings), Z2123, Z2124 (Lenstra regime), Z2178 (subset products = PH/B4), Z2314 (infinite family = hatch H-A), Z3129.
2. *Fixed finite menu / covering / escalation* (known-false, B1/B2(iii)/T1): Z1208, Z2317, Z0380 (Heath-Brown quantifier mismatch), Z2250 (absorption), Z0391, Z0220.
3. *Polylog explicit witness set* (known-false i.o.: H4_NOT_POLYLOG, POINTWISE_OMEGA13): Z3100, Z0581. Its Ankeny/GRH form (Z2076, Z2146) is known true for the BM coset (level ≤ 4ℓ(p), (J)103) — the class −1 inside the coset is the open step (§7.3, HC(p)).
4. *Relaxation then transport*: Z2057, Z2105, Z2289 (4 → 3 terms is a bijection: ES itself), Z2112 (semi-integral = ES^{(S)}: provable, no transport).
5. *Averages / exceptional set (B6)*: Z1525, Z1754 (Chen–Stein vacuous, Δ/μ ≥ 3.6), Z1576 (K-fold uniform sieve = RLD-U/FL∞ of §7.12), Z0240, Z2450.
6. *Function-field transfer*: Z0458 (large-q limit PROVES positive-proportion failures, EXSET_FUNCTION_FIELD §0.6), Z0509, Z2292, Z2293.
7. *Pooling across windows/shifts* (privacy of large primes): Z3184, Z2178.

**Corrections / notes on inputs**
* Z1525: Turán–Kubilius/Chebyshev gives an exceptional set of size X/log²K, not X·exp(−c log K) as the item suggests; exponential decay needs the large sieve/CRT architecture.
* Z1526: Pass 1 showed the item's integer "C-form conjecture" is false (860 odd non-squares ≤ 2·10⁷ with R(n) = 0); recorded known-false.
* Z1543: a polylog upper bound f(p) ≪ (log p)^A is false infinitely often (R(p) ≥ exp(c log p/log log p) i.o., Linnik).
* Z2749: any "restricted Legendre-PRF" hypothesis implies n₂(p) ≤ log²p, which is known only under GRH.

**Assessment.** No P06 item points to a proof architecture outside the repo's B2 / H⁻_BM / transport / B6 picture. The only new handle, Z0596 (Pell-cycle roots), lost its simplest form to the cheap check. The plaus ≥ 2 items are side theorems: an almost-all result on a thin set, a main-term expansion, and a thin-family tool.
