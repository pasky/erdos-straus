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
Classes: (i) `p ≡ −ma²d − e`… i.e. `p + e ≡ −ma²d (mod made)`; (ii) `p ≡ −ma²d (mod macd−1)`; (iii) `p ≡ −e (mod mab)`.
`φ(xy) ≥ φ(x)φ(y)` used correctly. ✓

**A5. Prop 3.4.** Per block `Σ_{ad~X} τ/φ(ad) ≪ Σ_{s,t}(st)^{-2}[log² X + #lossy·L log(1+k)] ≪ log² X + L log² m`
re-derived (uses `log L ≪ log m`). Block sum with BT weights `≍ 1/j`, j ≤ 2L → `(L² + L log² m) log L`. ✓
Small boxes: see m3 — the statement is right, the justification as written is not.

**A6. Lemma 3.5 / assembly.** ✓ (`e^{CL/log L} = m^{o(1)}` when `L < 10 log m`; `ρ_rep > 0 ⇒ p ≥ m/3`.)
Theorem L uses only BT, PV, Shiu, ET Thm 7.1 — all effective, so Theorem L is effective; worth saying.
