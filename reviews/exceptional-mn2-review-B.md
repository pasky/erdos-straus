# Hostile review B of EXCEPTIONAL_MN2.md (task R102B)

Reviewer: side-agent/review-emn2-b. Reviewed: `EXCEPTIONAL_MN2.md` as merged from
`side-agent/mn-transition` (HEAD at review start), `reviews/agent-reports/AGENT_REPORT_O102.md`.
Sources checked against: `sources/elsholtz-tao-1107.1010.pdf` (pdftotext, §7 pp. 25–32, (A.12) p. 49),
`sources/pw.txt` (PW §2–3, Lemma 7.4), `EXCEPTIONAL_MN.md` (Def 1.2, Lemma 1.3, Prop 3.1, Cor 3.2).
Shiu 1980 used as quoted (Thm 1 standard form); not re-read from PDF.


## Verdicts

| Claim | Verdict |
|---|---|
| Lemma 3.3 (ET Prop 1.4 + Pólya–Vinogradov) | **SOUND** (checked line by line against ET pp. 30–32; minor write-up defects m1–m3) |
| Lemma 3.1(a) | SOUND |
| Lemma 3.1(b) (repaired FATAL) | SOUND (re-derived; Rankin truncation, Shiu range, small-u swap all check) |
| Prop 3.2 (Type II ≪ L³/m) | SOUND |
| Prop 3.4 (Type I) | SOUND-AFTER-REPAIRS (minor: small-box bookkeeping misstated, log² vs log⁴; bound itself holds, even with m^{0.03} in place of m^{0.1}) |
| Lemma 3.5 | SOUND |
| **Theorem L** | **SOUND** as stated (effective, absolute constants); comparison-with-PW wording should be tightened (m5) |
| Lemma 1.1 (reduced CRT model) | SOUND |
| Lemma 1.2 (Shiu multiplicities, repaired k ≤ K) | SOUND (minor: inconsistent X-hypotheses in statement) |
| Thm 1.3 / **Theorem U** | **SOUND** (ineffective via BV; constants uniform in m — checked) |
| §2 numerics | EVIDENCE confirmed: scanner exact on 75 753 (m,p) pairs; L_{1/2} reproduced from scratch. Precision of "exponent 0.333" overstated (m7) |
| Conjecture C2 | correctly labelled CONJECTURE |

No FATAL or MAJOR defect found. I specifically attacked the four repaired spots (3.1(b), 3.3, 1.2 k ≤ K,
3.1(a) Y ≥ log m): all four repairs are correct.

## A. Theorem L (primary focus) — re-derivation notes

**A1. Lemma 3.3 vs ET (pdf pp. 30–32).** Dictionary: ET's linear `a`/`A` = our `d`/`D`, ET's quadratic
`b`/`B` = our `a`/`A`, ET case "A ≤ B" = our `D < A`. Checked:
* `D ≥ A`: ET Cor 7.4 per a, coefficient `ka² ≤ (AD)^l A² ≤ D^{2l+2}` — legit, no loss.
* `D < A`: ET Thm 7.1 per d with `P(a) = kd a² + 1`, coefficients `kd ≤ (AD)^l D ≤ A^{2l+1}`, `ρ(p^j) ≤ 4`
  uniformly → `Σ_a τ ≪_l A Σ_{q≤A} ρ_{kd}(q)/q`. ET's reductions (q odd, d odd via `d = 2^j d'`, `k → 2^j k`,
  `D → D/2^j`), `ρ_{kd}(q) ≤ Σ_{q'|q,(q',2kd)=1} (−kd/q')`, and the `O(1/q)` error give exactly the signed (7.11).
  Since the LHS is a nonnegative quantity bounded by a sum of three ranges, bounding each range by its
  absolute value separately is legitimate (the author's claim is right).
* Middle range `D' ≤ q ≤ min(kD', A)` (k = 2^j k_0 here): summand is `(−k/q)·χ(d)` with `χ = (·/q)·1_{odd}`
  a single character mod 2q, non-principal iff q is not a square. PV gives `≪ √q log q`; squares
  `q = r² ≥ D'` give `≪ D' log A Σ_{r ≥ √D'} r^{-2}`. Hence `≪ D' log A(1 + √(k/D') log(kD'))`. ✓
* j-summation: the middle range is `[D/2^j, kD]`; lossy iff `4^j > D/(k log²)`; geometric tail
  `Σ_{j ≥ j_0} 2^{-j} log(1+2^j k) ≪ 2^{-j_0} log(kAD) ≤ 1` when `D ≥ k log⁴(kAD)`. ✓
* Outer ranges reused from ET: q > kD' — `q ↦ c(q)(q/k'd)` is non-principal (the `(−1)^{(q−1)/2}` factor
  of `c(q)` is a non-principal character mod 4, coprime to the odd part), period `≤ 8kD'`, partial
  summation `≪ log A` per d. ✓ q < D': see m1.
Conclusion: Lemma 3.3 is correct; it is effective with constant depending only on l.

**A2. Lemma 3.1(b).** Re-derived: `n/φ(n) ≤ e⁴ Σ_{s|(n,P(y))} μ²(s)/φ(s)` (ω(n) ≤ 1.45y); Rankin with
σ = 1/log y gives `S^{-σ} ≤ exp(−y/(4 log y)) ≪ y^{-10}` for `S = U^{1/2}` since `log U ≥ y/2` ⇔ `U ≥ m`. Large-u
Shiu: modulus `s ≤ x^{1/1.1}` is inside Shiu's range (β = 0.09); Shiu actually gives `(φ(s)/s)³` (an
improvement), the author's `(s/φ(s))³` is a valid weaker bound; `Σ_s μ²(s)(s/φ(s))³/φ(s)²` converges. Small u:
swap is exact, `max_{s ≥ u^{0.909}} 1/φ(s) ≪ log log(3u) u^{-0.909}`, the u-series converges with `m^{0.01}`. ✓
In Prop 3.2(ii) U = 3N^{0.82}/m ≥ m holds as m ≤ N^{0.1}. ✓

**A3. Lemma 3.1(a).** The class-sum `Σ_{b≡β(e)} 1/φ(b) ≪ 1/φ(β_0) + log Y/e` via `b/φ(b) = Σ_{g|b} μ²(g)/φ(g)`
is correct (`(g,e) > 1` impossible as `(β,e) = 1`); convolution and `S'_m(Y)` with `Y ≥ log m` correct. ✓

**A4. Prop 3.2.** Re-derived the flip: `(made)(macd)(mab)^{1/2} = m^{5/2} a^{5/2} b^{1/2} c d² e ≤ m^{5/2} a²b(ce)d²
≤ 2m^{1/2}(mabd)² ≤ 8m^{1/2}N²` using `a ≤ b`, `ce ≤ 2b`, `mabd = p+e ≤ 2N` (e ≤ 2ab ≤ 2p/(m−2) ≤ p). So
`min ≤ (8m^{1/2}N²)^{2/5} ≤ 3N^{0.82}` for m ≤ N^{0.1}. ✓ Coprimalities `(e,m) = (e,ad) = 1` hold since p ∤ m, p ∤ ad.
Classes: (i) `p ≡ −ma²d − e (mod made)` (from `b ≡ −a (mod e)`); (ii) `p ≡ −ma²d (mod macd−1)`; (iii) `p ≡ −e (mod mab)`.
`φ(xy) ≥ φ(x)φ(y)` used correctly. ✓

**A5. Prop 3.4.** Per block `Σ_{ad~X} τ/φ(ad) ≪ Σ_{s,t}(st)^{-2}[log² X + #lossy·L log(1+k)] ≪ log² X + L log² m`
re-derived (uses `log L ≪ log m`). Block sum with BT weights `≍ 1/j`, j ≤ 2L → `(L² + L log² m) log L`. ✓
Small boxes: see m3 — the statement is right, the justification as written is not.

**A6. Lemma 3.5 / assembly.** ✓ (`e^{CL/log L} = m^{o(1)}` when `L < 10 log m`; `ρ_rep > 0 ⇒ p ≥ m/3`.)
Theorem L uses only BT, PV, Shiu, ET Thm 7.1 — all effective, so Theorem L is effective; worth saying.

## B. Theorem U (lighter check)

* Lemma 1.1: for primes p > K, `p mod L_K` is reduced, so MN Cor 3.2's lower bound `μ_c ≥ a_u t³/m` (stated
  there for `(c,L_K) = 1`, `X ≥ X_h`, `4 ≤ m ≤ t³`) applies to every fibre. Conditional independence and
  distinct non-zero classes mod ℓ (MN Lemma 1.3, which needs ℓ ∤ m: `ℓ > X^{1/2} > t³ ≥ m` ✓). `P(ξ_ℓ=1)=f_c(ℓ)/(ℓ−1)`
  because ñ mod ℓ is uniform on units. `E[C(H,r+1)|c] = e_{r+1}(p_ℓ) ≤ (Σp_ℓ)^{r+1}/(r+1)!` ✓.
* Thm 1.3 main term: `q_B | 𝓜`, `a_B` a unit, so `P(ñ ≡ a_B) = 1/φ(q_B)` exactly; empty-intersection B
  contribute 0 on both sides. ✓ Moduli `≤ e^{(1+κ)rt} ≤ N^{0.45}` with `rt ≍ s^{4/3}m^{1/3}` ✓.
* Lemma 1.2: given q, the ℓ's are the prime factors > X^{1/2} (as k ≤ K < X^{1/2}); per ℓ at most
  `Σ_{k|q',k≤K} τ(kℓ+1)²` atoms; CS; Shiu on `n ≡ 1 (mod k)`, `n ∈ (kx,2kx]` (length kx, modulus k ≤ (kx)^{1/2})
  gives `≪ (kx/φ(k))(log X)^{15}` ✓; the bound does not see m (u, v range over all divisors), so `C(r)` is
  m-free ✓. `Σ τ(q')^{2r}/φ(q') ≪_r (log)^{4^r}` ✓.
* Error: CS with BT pointwise and BV in mean, `A' = 17r + 4^r + 5`, `t ≤ L` ✓. `N_0(s)` depends on s only
  (through r and the Siegel-ineffective BV constant), not on m ✓. Uniformity in m: ✓.
* Ineffectivity statement is accurate (BV at `L^{−A'(r)}` with r → ∞ as ε → 0).

## C. Defects

No FATAL. No MAJOR.

**m1 (MINOR, Lemma 3.3 proof, "ET split q into q < D (period 2q, inner sum O(q): no loss)").** This inherits a
slip in ET p. 31: for **square** q the map `d ↦ (−kd/q)1_{(d,2q)=1}` is principal (not mean-zero), so the inner sum
is ≍ D', not O(q). Harmless (`Σ_{r² < D'} D' log A/r² ≪ D' log A`), but since the lemma is advertised as a
line-by-line re-derivation, say so explicitly (the author already treats squares this way in the middle range).

**m2 (MINOR, Lemma 3.3 statement).** Hypothesis `A, D ≥ 2` is used by Prop 3.4 also for boxes with `D' = 1`
or `A' = 1` (e.g. `d' = 1`). Add one line: by positivity one may enlarge the box to `D' = 2`, which keeps
`k ≤ (AD)^l` and lands in the lossy case (cost already counted).

**m3 (MINOR, Prop 3.4, small boxes).** "they exist only in blocks with `X ≤ st·k^{0.1}`" is false as a statement
about blocks: for every X there are (s,t) with st ≍ X (all of a, d absorbed into s, t), so small boxes occur in
every block. Correct bookkeeping: for each block, the (s,t) with small boxes satisfy
`(st)^{1.2} m^{0.1} ≫ X`; their weighted mass is `≪ Σ_{st ≫ (X/m^{0.1})^{1/1.2}} (st)^{-1.94} m^{0.03} log(mst)
≪ m^{0.03} log m · min(1, (X/m^{0.1})^{-0.7})`; summing over blocks with weights `≤ 1` gives
`≪ m^{0.03} log² m`, i.e. a count `≪ (N/φ(m)) m^{0.03} log² m`, better than the stated `m^{0.1} log² m`.
Replace the sentence with this computation.

**m4 (MINOR, Prop 3.4 vs Lemma 3.3).** Lossy boxes are defined as `D' < k log²(kN)` in Prop 3.4 but
`D < k log⁴(kAD)` in Lemma 3.3. Use log⁴ (count `≪ log k + log L` unchanged).

**m5 (MINOR, §0 / §3 intro, comparison with PW).** "Improves PW's `L³ log² m/φ(m)` by a factor log m":
PW's proof actually gives Type I `≪ (N/φ(m)) L² log L log m` and Type II `≪ (N/φ(m)) L² log L` (pw.txt
§3, before they replace `log log N` by `log m`). The new Type I bound is `(L² + L log² m) log L`, i.e. the
gain over PW's *unsimplified* bound is a factor `min(log m, L/log m)`; it is a full log m only for
`L ≥ log² m` (true at the transition `L ≍ m^{1/3}`, where `log L ≍ log m`). State it that way.

**m6 (MINOR, Lemma 1.2 statement).** "for fixed r and `X ≥ X_2(r)`, … (for `X ≥ X_1`; …)" — two
different size hypotheses in one sentence; the proof needs neither beyond `K < X^{1/2}`. Pick one.

**m7 (MINOR, §1 Thm 1.3, BV step).** `Δ(q,a)` is centred at `π*(N)/φ(q)`, not at `(li N − li N/2)/φ(q)`;
the difference `|π*(N) − (li N − li N/2)| Σ_{q≤N^{0.45}} M(q)/φ(q)` must be bounded too (it is: PNT error
`N e^{−c√L}` times `Σ M(q)/φ(q) ≤ (Σ M²/φ)^{1/2}(Σ 1/φ)^{1/2} ≤ t^{O_r(1)} L`). One line.

**m8 (MINOR, §2 precision).** The proportion curves are flat and noisy near 1/2 (from-scratch full counts,
see D below: m = 64 gives 0.487, 0.482, 0.516 at L = 7.45, 7.62, 7.80 — non-monotone). With ~800 sampled primes
per window (σ ≈ 0.018 in the proportion) the first-crossing L_{1/2} has an uncertainty of order ±0.1–0.2 in L
(±0.02–0.03 in the ratio). "Local log-log slope 60 → 300: 0.333" from two endpoints therefore has an
uncertainty of roughly ±0.02 and should be quoted with it; likewise the odd-m slopes 0.36–0.40. The table
rows m ≤ 24 in `emn2_half.out.txt` are pinned at the grid start N = 16 (L = 2.773) — artefacts; they are not
used in the text, but mark them as such in the output file.

**m9 (MINOR, status line of Theorem L).** Lemma 3.3 is now checked against ET line by line (A1); the report's
suggested fallback "PROVED modulo Lemma 3.3" is unnecessary. Add "effective" to Theorem L's label (all inputs
are effective), contrasting with Theorem U.

## D. From-scratch numerics (EVIDENCE)

`scripts/review_emn2B_brute.py`: exact test of `m/p = 1/x+1/y+1/z` via smallest denominator
`x ∈ (p/m, 3p/m]` and `A/B = 1/y+1/z ⟺ (Ay−B)(Az−B) = B²` (enumerate δ | B², `δ ≡ B²/δ ≡ −B mod A`).
Independent of PW Cor 2.2/2.4 and of the author's u,v-criterion. Sanity: m = 4, 5 no exceptions p ≤ 400;
m = 8 exceptions include 3; m = 9 include 2, 5 (as PW §3).

* `scripts/review_emn2B_compare.py` vs the author's `emn2_scan.c` (count=2 mode), per prime:
  m = 4..120 ∪ {150,199,200,256,300}, p ≤ 2000: 36 747 pairs (17 447 exceptional), 0 mismatches;
  m = 121..300, p ∈ (20000, 22000]: 36 360 pairs (20 803 exceptional), 0 mismatches;
  m = 40..60 ∪ {100,128,199,200,256,300}, p ∈ (70000, 71000]: 2 646 pairs (325 exceptional), 0 mismatches.
  Total 75 753 pairs, 0 mismatches. The scanner is exact on this range.
* `scripts/review_emn2B_half.py` (all primes in each window, no sampling):

| m | L_.5 (mine) | L_.5 (author) | ratio (mine) |
|---|---|---|---|
| 60 | 7.636 | 7.636 | 1.950 |
| 64 | 7.718 | 7.718 | 1.930 |
| 61 | 6.397 | – (odd file) | 1.625 |
| 63 | 7.127 | – | 1.791 |
| 100 | 9.207 | 9.207 | 1.983 |
| 101 | 7.586 | 7.586 | 1.629 |
| 127 | 8.842 | 8.842 | 1.759 |
| 128 | 9.645 | 9.645 | 1.914 |
| 199 | 10.384 | 10.384 | 1.779 |
| 200 | 11.143 | 11.209 (sampled) | 1.905 |
| 256 | 12.277 | 12.217 (sampled) | 1.934 |

  Identical where the author's stride is 1; for m = 200, 256 (sampled) the full count moves L_.5 by
  ∓0.06 — consistent with m8. m = 300 full count did not finish in 50 min (my Python brute force) — not
  replicated. The even/odd split (odd m lower) is reproduced.

## E. Bottom line

Theorem U and Theorem L both survive a hostile line-by-line check; no FATAL/MAJOR defects. All four
self-review repairs are correct. Requested changes are presentational (m1–m9). The labels (PROVED rel. …,
EVIDENCE, CONJECTURE) are appropriate; I recommend adding "effective" to Theorem L and keeping
"ineffective" on Theorem U.
