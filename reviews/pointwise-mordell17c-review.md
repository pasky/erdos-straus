# Review R98b of POINTWISE_MORDELL17C.md (O98) — hostile reviewer

Reviewed: POINTWISE_MORDELL17C.md and reviews/agent-reports/AGENT_REPORT_O98.md (merged from `side-agent/r17-explicit-et`).
From-scratch scripts: `scripts/review_m17c_*.py` (the author's scripts were not reused).

## Verdicts

| claim | verdict |
|---|---|
| Lemma 1.1 (cumulative (H_P),(H_Q)) + table | SOUND (minor wording) |

## Claim-by-claim

### Lemma 1.1 (Abel summation)
Re-derived: with `D(K) = S(K) − S(K−2)` (S(11) := 0), `Σ_{13}^{K₁} w_K D(K) = w_{K₁}S(K₁) + Σ_{13}^{K₁−2}(w_K − w_{K+2})S(K)`;
`w_K − w_{K+2} = (16/17)w_K` for `w_K = 17^{(1−K)/2}`; boundary `≤ C·17^{1/2}·17^{(θ−1/2)K₁} → 0` for θ < 1/2; all summands ≥ 0.
Same for Q with `w_k = 17^{1−k}`, ratio `1 − 17^{−2}`. Correct. Only cumulative bounds are needed; M17B Thm 4.1's proof
(Lemma 1.1 of M17B + `NB ≤ 2D` + summation) uses (H_P) only inside `Σ w_K D_P(K)`, so the replacement is legitimate.

Table recomputed from closed-form geometric series (`scripts/review_m17c_tail.py`, mpmath 40 digits, no truncation):
`Σ_{K≥K₀ odd} 17^{θK+(1−K)/2} = 17^{1/2} r^{K₀}/(1−r²)`, `r = 17^{θ−1/2}`; `T_Q = 34·q⁹/(1−q²)`, `q = 17^{−2/5}` = 1.410566·10⁻³.
Exact thresholds (θ = 0.4): pointwise K≥13 = 1.409796…, cumulative K≥13 = 1.497908…, cumulative K≥15/ρ₂ = 2.639795…;
all 18 floor-rounded entries of the table agree digit for digit, and the pointwise row equals M17B §4 (also the M17B
K≥15 row 2553/272.9/27.53/2.484/0.8947/0.1692 is reproduced). Data check `1463 ≤ 1.497·17^{5.2} ≈ 3.7·10⁶`: true (trivially).

### Lemma 2.1 (Type-I/Q identities; ≤ 2 points per (a,d))
Re-derived (i)–(iii) by hand from `4abcd = F(a+b)+c`, `e = (a+b)/c`, `f = 4acd − F`: all correct. (iv): `c` is fixed by `f`
given `(a,d)`; `f | t = 4a²d+1`, `f ≡ −F (mod s = 4ad)`, `gcd(f,s)=1`, `s² > t` for all `a,d ≥ 1`. Small divisors (`≤ √t < s`)
are the least positive residue of their class; large ones have cofactor `e < √t < s` in the class `(−F)^{−1}` (note
`t ≡ 1 mod s`). Correct; the bound 2 is attained (below).

From-scratch brute force (`scripts/review_m17c_qbrute.py`, `scripts/review_m17c_qsweep.py`): enumerator solves the defining
equation for `b = (Fa+c)/(4acd−F)` with an independently derived range (`b ≥ a ⇔ 4acd ≤ 2F + c/a`), so it does not
presuppose Lemma 2.1 or the ET range.
* F = 17, 4913, 1001, 9999: 2, 73, 10, 179 points; max per `(a,d)` = 1, 1, 1, 2 — **identical to the author's numbers**;
  73 = D_Q(3) (all 73 have 17∤e). F = 17⁴ = 83521: 0 points (consistent with Q-levels being odd).
* Sweep over **every** F ∈ [1, 1500]: 27 919 points, 0 failures of (i)–(iii) and of `F < 4acd ≤ 3F`, max per pair = 2
  (4 601 pairs attain 2).
Verdict: SOUND.

### Corollary 2.2 (c ≥ F^{1/2} part unconditional; cost 4.3·10⁻³)
`F/4 < acd ≤ 3F/4` (checked above for all F ≤ 1500). With `c ≥ c₀`, `ad ≤ 3F/(4c₀) = Y`; `#{(a,d): ad ≤ Y} ≤ Y·H_⌊Y⌋ ≤ Y(1+ln Y)`
(Y ≥ 1; for Y < 1 the count is 0). With Lemma 2.1(iv), `#{c ≥ c₀} ≤ 2Y(1+ln Y)`. Brute check at the five c₀ values in
`review_m17c_qbrute.py` for each F above: all counts below the bound (very loosely). Sum recomputed with mpmath `nsum` to ∞:
`Σ_{k≥9 odd} 3·17^{1−k/2}(1+k ln 17) = 4.22545·10⁻³ < 4.3·10⁻³` ✓. Accounting: `T_Q ≤ 2Σ17^{1−k}(D_Q^{c<√F} + D_Q^{c≥√F})`,
so (H_Q) restricted to `c < F^{1/2}` plus 4.3·10⁻³ is a correct replacement. Verdict: SOUND.
(Remark, not a defect: keeping `ln Y` instead of the bound `ln Y ≤ ln F` halves the cost to 2.146·10⁻³.)

### Assessment 2.3 (route to unconditional (H_Q))
Label correct (Assessment, not carried out). Re-derived the thresholds: (a,c): `M = aF+c ≈ F^{1+α}`, modulus `4ac ≈ F^{α+γ}`;
`α+γ > (1+α)/3 ⇔ 2α+3γ > 1`, `> (1+α)/4 ⇔ 3α+4γ > 1` ✓. (c,d): `M ≈ F²` (as `2γ+δ ≤ 2`), thresholds 2/3, 1/2 ✓.
`(0.4,0,0.6)` is indeed uncovered by Lenstra-1/3 in all three regimes ✓. Lenstra (1984) gives ≤ 11 divisors for s > n^{1/3}
and O_α(1) for α > 1/4 (statement from memory; source PDF not in sources/, not checked). See defect m3 (corner not
listed). The P-side "no free regime" remark: re-derived, correct.

### §3 Assessment (P side, ET-type covers)
Re-derived: P-point constraints `(N+e)/4 ≤ acde ≤ (N+e)/2` ✓; at the symmetric point each two-variable regime has `≍ N^{1/2}`
parameter pairs ✓; ET balance with `X_ad,X_ac,X_cd ≤ N^{0.4}` forces `X_e ≥ N^{0.4}` ✓; `#{ad ≤ X} ≥ X ln X − X` and
`X ln X − X > 1.497X ⇔ ln X > 2.497` ✓ (true for every K ≥ 13, as `ln 17^{5.2} = 14.7`). Nicolas–Robin
`τ(n) ≤ n^{1.5379 ln 2/ln ln n}` (n ≥ 3): exponent `1.066/ln ln n = 0.189` at `n = 17^{100}` ✓. The conclusions are
methodological and correctly not claimed as theorems, but two sentences overclaim (defects m4, m5).

### §4 Assessment + EVIDENCE (averaging over K)
* Class structure (PROVED): re-derived. For fixed `(a,b,e)`, `17∤cd` is K-independent (`c = (a+b)/e` fixed; `17 | d ⇔ 17 | 17^K+e ⇔ 17 | e`),
  so the admissible set is exactly {odd K ≡ K₀ mod lcm(2, ord_m 17)} ∩ {17^K + e ≥ m} or empty ✓.
* "17 never a primitive root mod 4ab, ab > 1" ✓ (ab even ⇒ 8 | m; ab odd > 1 ⇒ (ℤ/4)^× × (ℤ/p^j)^× with two even factors;
  even ab = 1 holds since 17 ≡ 1 mod 4). `−e ≡ 1 mod gcd(m,16)` ✓.
* EVIDENCE table: independent C code `scripts/review_m17c_dlog.c` reproduces **every entry** for B = 3000 and 30000
  (pairs, Σ τ, E_∞, ratios, #K_min ≤ 13 = 123/231, median 167/1411, max 2811/28795). The underlying model (M17B Lemma 5.1)
  was validated from scratch: `scripts/review_m17c_pcount.c` counts N-points of `Σ^II_{17^K}` (a ≤ b, 17∤cd) via
  `e = −17^K mod 4ab` and returns D_P = 2, 32, 121 for K = 1, 3, 5, matching M17/M17B.
* Extended range (this review): B = 10⁴, 10⁵, 3·10⁵ give E_∞ = 4698, 52861, 165511; E_∞/Στ = 1.40 %, 1.04 %, 0.92 %;
  E_∞/(B ln B) = 0.051, 0.046, 0.044; #K_min ≤ 13 = 175, 303, 372; median K_min = 491, 4515, 12525. So the
  growth statement in the text is wrong in detail (defect m6), though the Assessment's conclusion (θ ≈ 1 for K-blind
  arguments) is unaffected: any `E_∞ ≥ B^{1−o(1)}` gives it.
* Assessment: the reduction "(H_P^cum) ⇔ discrete logs of −e rarely fall in `[log_17 4ab, K]`" is a correct reformulation
  (modulo the multiplicity remark m7). Label CONDITIONAL for (H_P) correct.

