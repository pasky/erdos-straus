# Hostile review A of EXCEPTIONAL_TYPEI_LOGLOG3.md (task R121A)

Reviewer: side agent R121A (independent of reviewer B). Branch reviewed: `side-agent/eff-di7` (merged into
`side-agent/review-ttl3-a`). Round 1 COMPLETE.

## Verdicts (summary)
| Section / claim | Verdict |
|---|---|
| §1 toolkit (Lemmas 1.1–1.3) | SOUND |
| §2 induction (Prop 2.1, Thm 2.2, Cor 2.3) | SOUND (rel. (P1)–(P3)); double-exponential class propagates, no circularity |
| §3 (P3) | SOUND |
| §4 / lemma81 file: (P1), (P2) | SOUND (absolute numerals not all re-derived, m2) |
| §5 / thm2 file: effective DI Thm 2 incl. exceptional | SOUND (m3, m4 minor) |
| §6 / thm14 file: effective Thm 14, U-form | SOUND |
| §7 Thm 7.1 | SOUND |
| §8 nebentypus (twisted resonance, small-C branch) | SOUND |
| Thm 9.1 | SOUND-AFTER-REPAIRS (m1: constant 100 → 200); label PROVED rel. (B1)–(B5) acceptable |
| Thm 9.2 | SOUND rel. (B1)–(B5), TTL's inputs, TTL2 Thm 4.1(ii); outward claim should await external expert check |

No FATAL, no MAJOR; 5 MINOR (m1–m5). Scripts: `scripts/review_r121a_{induction,toolkit,thm2,transform}.py`.

## §2 (induction (8.19), Prop 2.1, Thm 2.2, Cor 2.3) — verdict: SOUND (relative to (P1)–(P3))

Re-derived line by line; from-scratch sweep `scripts/review_r121a_induction.py` (log-space, 2·10⁵ random
`(δ, c, K₁, K₂, Q, N)` per case, δ down to 10⁻³, constants up to e³⁰) finds no violation of cases (A), (B), (C) of
Prop 2.1 or of Cor 2.3 (max of `log log H − (B+3)/δ` over the grid is −27.6).
* (P2) is a faithful transcription of DI (8.5) (scan p. 271: `S(Q,Y,N,0) ≤ c(ε)∫S(πNYQ⁻¹,Y,N,it)dt/(t⁴+1) +
  c(ε)(YN)^ε(Q+N+NYQ⁻¹)‖a‖²`, S as in (8.4) with `Q<q≤16Q`), with ‖a‖² ≤ 2N for closed intervals absorbed.
* (M) needs only `0 < 2σ_j ≤ 1/2` (Selberg 3/16) ✓. (PS): Abel summation and Cauchy–Schwarz in `dξ/ξ` over
  `[N,N₁] ⊂ [N,2N]` give `|·|² ≤ 2|A(N₁)|² + 2t²(log 2)∫|A|²dξ/ξ`; after weighting/summing,
  `≤ 2S* + 2t²(log 2)²S*` ✓. The intervals `[N,ξ]` are admissible (closed, `ξ ≤ 2N`) ✓.
* Case (C): `Q₁ = πQ^{1−2δ}` satisfies `N ≤ Q₁ ≤ Q/2` exactly when `Q^{2δ} ≥ 2π` and `N ≤ Q^{1−2δ}` ✓; the main term
  is in fact `2√2π·π^{5δ}·cH·Q^{1+4δ−10δ²}N` (the text's `π^{1+4δ}` overestimates harmlessly), the error term
  `≤ 3cQ^{1+2δ}N` ✓, and `H/2 + 3c ≤ H` because `H ≥ 6c` ✓. **No accumulation**: the same H is reproduced at every
  dyadic step, so the number of induction steps (≍ log Q) does not enter the constant. This is the crux of the
  double-exponential claim and it is correct: `log Q₀ ≍ δ^{−2}log c(δ)`, `log H ≤ log(2K₂) + log Q₀`, so
  `log log K₇ ≤ max(log log K_i) + 2 log(1/δ) + O(1)` ✓ (Cor 2.3).
* Thm 2.2: both branches re-derived ✓ (`Y₂ = Q^{2−2δ}/N ≥ Q^{1−2δ} ≥ 1`).
* Non-circularity: (P1), (P3) are non-inductive; (P2) is applied only with `Q₁ ≤ Q/2` and `N ≤ Q₁` ✓.
Cross-check with DI's own proof (scan pp. 276–278): DI inducts with `Q₁ ≤ Q − 1`; the dyadic variant is
equivalent. DI's step "extend q from [Q,2Q] to [Q,16Q] by applying the estimate at (2^lQ, 2^lY)" (p. 273) is
the place where C is held fixed; that is inside (P2) (§4), not here.

Minor (§2): m1 below.

## §1 (toolkit) — verdict: SOUND
From scratch (`scripts/review_r121a_toolkit.py`): Lemma 1.3(a) `max_p≤15 sup|h^{(p)}|/(9^p p!²) = 0.905`; `I = 4.85·10⁻⁵ ≥
e^{−16}/4`; `|ρ^{(p)}|` (p ≤ 8) at most `2·10⁻⁷` of the stated bound. Lemma 1.1 brute force (`τ^B`, B ∈ {1,2},
δ ∈ [1/4,1], n ≤ 2·10⁵): ratio ≤ 0.25. Proofs re-read: Cauchy-circle argument, Leibniz sum
`Σ C(p,k)k!²(p−k)!² ≤ (p+1)p!²`, convolution formula for η^{(p)} — all correct. Lemma 1.2 ✓.

## §4 / `ttl3_lemma81_effective.md` (P1), (P2) — verdict: SOUND (modulo un-re-derived absolute numerals; see m2)
Checked against DI pp. 271–273, 276–277 (scan).
* Support repair (§3.2) re-computed exactly: with `q ∈ [3Q/4,9Q/4]`, `xY ∈ [11/12,17/12]`, `√mn ∈ [N,2N]` one gets
  `c/C ∈ [64/51, 128/11]` ⊂ (1,16]; DI's pictured supports give `[16/25, 32]` — the author's observation of a
  (harmless) gap in DI's printed bookkeeping is correct. k-range in (P1): `k/(NY) ∈ [8.87, 27.42]` ⊂ (8,32) ✓.
* Positivity (c): independent mpmath evaluation of the exact kernel `π/(2 sin πσ)(J_{−2σ}−J_{2σ})` (with the
  sign that makes it positive, i.e. DI (8.1), not printed (1.22)) for `Y ∈ {2³²,2⁴⁰}`, `σ ∈ [10⁻⁶,1/4]`:
  kernel positive on the whole support, and `φ̂(−iσ)/cos πσ ≥ 0.67·Y^{2σ}` using only the plateau — far above
  1/64 ✓. The σ → 0 uniformity argument (MVT on the order *difference* before dividing by `sin πσ`) is right; the
  limit is a `log(2/x)` kernel, which is why (d) carries `L_Y` ✓.
* Mellin separation, the `m^{−it/2}n^{−it/2}` twists, the Cauchy–Schwarz `|A(t/2)||A(−t/2)| ≤ (|A(t/2)|²+|A(−t/2)|²)/2`,
  substitution `t = ±2u` ✓; the second trace formula's spectral side carries **no** `1/c` weight, so the regular
  error is `Σ_{c∈(C,16C]}K_{T2}(1+N^{1+e}/c)‖a‖² ≤ K_{T2}(16C+4N^{1+e})2N` ✓ (matches DI (8.10)).
* Exceptional split at σ = e: the `1/sin πσ ≤ 1/(2e)` loss for σ > e and `Y^{2e}L_Y` for σ ≤ e are polynomial
  in 1/δ — consistent with `c(δ) = Aδ^{−2}[1+K_{T2}(δ/4)]` ✓. Four blocks `(2^lQ,2^lY)` keep C fixed ✓ (DI p. 273).
* Small-Y branch (`Y < 2³²`) and `C < 1` branch: re-derived; with `Q > πNY` one has `Y^{1/2}N^{1+e} ≤ QN^e` ✓.
* (P1) partial summation with a k-independent majorant measure and prefix rectangles, then Thm 14 in the
  U-form for each prefix — correct and indeed necessary (sup over prefixes inside the k-sum would not follow).
  Two-variable Abel summation on `[N,N₁]²` needs `|∂_m w|, |∂_n w| ≤ H/N`, `|∂_m∂_n w| ≤ H/N²` ✓ (u ∈ [11/12,17/12]).
* Transform bound (a): heuristically re-derived (normalised kernel `≍ r^{−1/2}` via `|Γ(1+2ir)|² = 2πr/sinh 2πr`;
  Bessel ODE `(D_x²+x²)J_{2ir} = −4r²J_{2ir}` ✓), constants plausible, B = 2^{2048} generous. The claim
  "H = 2^{512} bounds D_x^j-norms, j ≤ 12" re-estimated: ≈ 2^{212} ✓.
No growing-order step occurs in §4; the only δ-dependence is `δ^{−2}`, `K_{T2}(δ/4)`, `D(δ/4)`, `K₁₄(δ/4)` ✓.

## §5 / `ttl3_thm2_effective.md` (effective DI Thm 2 at ∞) — verdict: SOUND (minor defects m3, m4)
Checked against DI pp. 253, 256–261 (scan); from-scratch numerics `scripts/review_r121a_thm2.py`.
* **Step 4 (the only growing-order step).** Re-derived: after Cauchy–Schwarz and Poisson in m with the majorant
  `η(m/N)` (supp `[3/4,9/4]`), the phase derivative ratio is `≤ 2θ(√2−1)/(√3·c|a−u|) ≤ 0.9566 < 31/32` (θ < 2,
  `|a−u| ≥ 1/c`); with DI's support (1/2,3) it is `1.17 > 1` — the author's repair of DI p. 257 is correct.
  Cauchy disc radius `2^{−12}`: `min|1 − βz^{−1/2}| = 0.031 ≥ 1/64` numerically ✓ ⇒ `‖g^{(j)}‖ ≤ 64·2^{12j}j!` ✓.
  Term count of `p` nested Leibniz expansions `(p+1)!`, derivative-factorial products `≤ (p!)²` against the Gevrey-2
  η ⇒ `R_p = 2^{100(p+1)}(p!)⁴` dominates (re-derived: `2^{40p}36^p·8e^{16}(p+1)(p!)³`) ✓. `sp ≥ 2−s` with
  `p = ⌊2/s⌋` gives `N(c/N)^p ≤ 1/c` for `c ≤ N^{1−s}` ✓. Cost `log R_p ≍ δ^{−1}log(1/δ)`: single-exponential ✓.
* Step 5 resonant/Ramanujan term and the final `|B| ≤ Pθ^{−1/2}c^{1/2}N^{1/2+s}‖b‖²` re-derived (`(Σ|b|)² ≤ 2N‖b‖²`,
  `Σ_{h≤N}(h,c)/h ≤ τ(c)(1+log N)`) ✓; the range `N^{1−s} < c < N` from Step 3 ✓.
* Step 2 (DI's exercise (5.1)): row-sum constant numerically ≤ 34 < 100 over a grid ✓.
* Step 6: `D_K ≤ 2K²` (numerically ≤ 0.28·2K²), `∫wξ = 2e^{−1/K}` (exact, verified), `∫wξ^{±1/2} ≤ 32`, angular
  integrals ≤ 4Δ, 4/Δ ✓; the exponent bookkeeping for `F(c) ≤ AP c^{−s}N^{1+5s}` in all three c-ranges re-derived ✓;
  the `c^{−s}` is what makes `Σ_{q|c}|F(c)|/c ≤ AP(1+1/s)q^{−1}N^{1+5s}` summable ✓.
* Step 7: the restricted Gaussian lower bound: numerically `∫_{[|r|,|r|+1]}t sh(πt)H(r,t)e^{−(t/K)²}dt ≥ 0.0067(1+|r|)`
  (`|r| ≤ K`), far above `2^{−20}` ✓. Step 8 enlargement `L = K + X^s` and `sup_X Xe^{−X^{2s}/2} ≤ (1+1/s)^{1/s}` ✓;
  partial summation with `1/(1+r)` ✓.
* Step 9 (exceptional spectrum): `H(iσ,t) = cos πσ/(sh²πt + cos²πσ)` (verified against DI's definition p. 253), so the
  M-weight `H/ch(πκ)` integrated over `t ∈ [1,2]` is `≥ 0.0038` uniformly for `0 ≤ σ ≤ 1/4` ✓ (it degenerates only
  as σ → 1/2; at σ = .4999 the bare H-integral is 8·10⁻⁵). So exceptional terms are handled once `σ ≤ 1/4` is known,
  and that is (B4). See m4.
* Step 10: `log log K_{T2} ≤ 96/δ` re-computed from the explicit formula (margin ≥ 500 on δ ∈ [0.01,0.1]) ✓; the
  double-exponential comes solely from the divisor constant `D(s)` (`τ^4`, `s = δ/16`), as claimed.

## §6 / `ttl3_thm14_effective.md` (effective DI Thm 14, U-form) — verdict: SOUND
* U-form: `|Σ_{m≤M}e(mξ)| ≤ min(M,1/(2‖ξ‖)) ≤ f_M(ξ)`, and `Σ*_d f_M(d/c)f_N(d̄/c) = Σ_{m,n∈ℤ}f̂_M(m)f̂_N(n)S(m,n;c)`
  (absolutely convergent, `|f̂_M(m)| ≤ (M/m)²`) is real and ≥ 0, so `g_D ≥ 1_{[D,2D)}` may be inserted ✓. This is
  exactly DI (8.14) and is what (P1) needs (sum of |·| over k after partial summation) ✓. The majorant also covers
  any interval of length ≤ M, so the prefix decomposition in §4 is not even needed.
* Fourier separation: x-support `[κ√UV/D, (17/7)²κ√UV/D]`, `κ = 28π/17`, `(17/7)² = 5.90 < 8` ✓;
  `(1+X+√U)(1+X+√V)/(1+X) ≤ 10√UV` re-derived ✓; `A = U^{(1+δ)/2}` replacement ✓.
* (B8): dyadic tail sums `Σ2^{−j/2}`, `Σ2^{−2j}` and `R^{−5/2}+X³R^{−4} ≤ 2/(1+X)` (R = 4+X) ✓. Only fixed
  derivative orders (≤ 7) and fixed contour shifts (to Re s = −3) — no hidden δ ✓. No exceptional term at level 1
  (B5) ✓; so the σ → 0 non-uniformity of DI (7.1) noted by the author is indeed irrelevant here.
* Zero frequencies via the *mean* divisor bound `Σ_{c≤Z}τ(c) ≤ Z(1+log Z)` ✓; block sums `Σ_U b_U ≤ 5M^{1+α}` ✓;
  absorption `(1+log P)³ ≤ (1+6/δ)³P^{δ/2}` ✓; c-decomposition without log loss ✓.
* The numerical allowances `2^{50}`, `2^{1000}` for the transform/derivative bounds were spot-checked only at the
  level of orders of magnitude (each step is fixed-order, so any finite absolute constant suffices; see m2).

### Transform-ledger uniformity (supports §4 and §8)
`scripts/review_r121a_transform.py` evaluates the exact Bessel transforms (generic smooth bump on `[11/12,17/12]`,
mpmath) for `Y ∈ {2³², 2⁶⁴, 2¹²⁸}`: (a) `|φ̂_t(r)|(1+r)⁴/((1+|t|)⁴L_Y) ≤ 0.45` for r ∈ {10⁻⁸, .5, 2, 8}, t ∈ {0,3};
(d) `|φ̂_t(−iσ)|/(Y^{2σ}L_Y) ≤ 0.19` for σ ∈ {10⁻⁹, 10⁻⁴, 10⁻²} — no blow-up as σ → 0 and no growth in Y;
(e) `σ·|φ̂_t(−iσ) − main| ≤ 0.031` for σ ∈ [0.01, 1/4]. All consistent with the claimed absolute constants and with
the `1/sin πσ` cancellation. So the flagged point "transform bounds uniform as σ → 0" is **not** a gap.

## §3, §7 (assembly, trivial character) — verdict: SOUND
(P3) from Thm 2: `Σ_{Q<q≤16Q}(1+N^{1+δ}/q) ≤ 16(Q+N^{1+δ})`, `cos πσ ≥ 2^{−1/2}` ⇒ `K₂ = 32K_{T2}` ✓. §7 constant chain
re-derived: `K₁₄(δ/4) ≤ exp(exp(404/δ))` (from `(B₂+1)/δ'`, B₂ = 100, δ' = δ/4), `log log D(δ/4) ≤ 3/δ` (checked at
δ = 0.1: 29.2 ≤ 30), hence `K₁, c ≤ exp(exp(405/δ))` and `K₇ ≤ exp(exp(408/δ))` ✓.

## §8 / `ttl3_nebentypus.md`, `ttl3_thm2_twisted.md`, `ttl3_lemma81_twisted.md` — verdict: SOUND
* **Twisted resonance step** (flagged by the author): re-derived. After Cauchy–Schwarz and Poisson in the outer
  variable, the residue pair `(d₁,d₂)` carries `χ̄(d₁)χ(d₂)`; resonance means `d̄₁ ≡ d̄₂ (mod c)`, hence `d₁ ≡ d₂`, and
  since `r | c` the character factor is exactly 1, leaving the ordinary Ramanujan sum `≤ (n₁−n₂, c)` ✓. Off resonance
  the character is t-independent and only `|·| ≤ 1` is used ✓. Twisted Weil (B3) is used only in the `c > N²`
  ranges, giving the `√r/L` term, never on the diagonal ✓; `√r ≤ L` makes the large-K case of Step 8 work ✓.
  Dr Lemma 4.2 checked in the PDF: `S_aa(m,n;c) ≪ (m,n,c)^{1/2}τ(c)^{O(1)}(cq₀)^{1/2}` — exactly (B3) ✓.
* Switching for nebentypus: `k = rqc`; for fixed c the q-sum is Kuznetsov for `(Γ₀(rc), χ)` with the **same**
  Kloosterman function `Sχ(m,n;rcq)` as in the first trace (both are trace formulas for χ, so no conjugation mismatch)
  ✓; destination levels `rc`, `c ∈ [64C/51, 128C/11]`, `C = πNY/(rQ)` ✓. Small cofactors (`C < 1/16`: Kloosterman side
  empty; `1/16 ≤ C < 1`: ≤ 11 cofactors) ✓.
* **Small-C branch** (flagged): Prop 8.1 (C2) re-derived: `Y₁ = C+N ≤ 2N`, `C+N+Y₁ ≤ 4N`, `√(YN) = Q^{1−δ}`,
  `5K₁N^{2δ}(N+Q^{1−δ})N ≤ 10K₁Q^{1+2δ}N`, main term `2√2π·c·10K₁ ≤ 90cK₁`, closed by `H ≥ 200cK₁` ✓. (P1χ) for
  `0 < Q < 1` (`Σ_{Q<q≤16Q}1 ≤ 16Q`) ✓. (C1) needs `1 ≤ N ≤ C ≤ Q/2` ✓. Thm 8.2 for `Q < 1` ✓.
  The sweep in `review_r121a_induction.py` covers (C1); (C2) is a two-line inequality, checked by hand.
* Selberg for `Γ₁(L)` (B4) covers `(Γ₀(L),χ)` weight-0 forms ✓; positivity kernel is level/character-free ✓.
* The author's side remark that "even χ is a square" fails (χ₃χ₇ mod 21) is correct (χ₃ is odd, has no square root
  mod 3); not used.

## §9 (Thm 9.1, 9.2) — verdicts: Thm 9.1 SOUND-AFTER-REPAIRS (m1 only); Thm 9.2 SOUND relative to its inputs
* Constants: `K₁χ, cχ ≤ exp(exp((4B_χ+1)/δ))`, Cor 2.3 analogue with `200cK₁` ✓, `A₀ = 24B_χ+30 ≥ 6(4B_χ+4)` ✓.
* Conversion to TTL2's (DI7_ε): Q-blocks `(Q_i,16Q_i]`, `Q_i ≥ 1/16`, at most `2 + log M₀` of them ✓; prefix split into
  closed dyadic blocks `[2^k, min(2^{k+1}−1,t)]` ✓; `Σ_k(Q+2^k+√(2^kY))2^k ≤ 2(Q+t+√(tY))t` ✓ (re-derived:
  `Σ2^{1.5k} ≤ 1.55 t^{1.5}`). Levels in `(Q_i,16Q_i]` beyond M₀ only add positive terms ✓.
* TTL2 Thm 4.1(ii) needs exactly `log C_ε ≤ exp(A₀/ε)` at `ε = 2A₀/log L` ✓ (LOGLOG2 §4, which had two independent
  reviews with no FATAL/MAJOR).
* **Honest label.** I found no FATAL or MAJOR defect. Thm 9.1: **PROVED relative to (B1)–(B5)**, with the caveats that
  (i) the large absolute numerals (`2^{50}`, `2^{512}`, `2^{1000}`, `2^{2048}`, `2^{10000}`, …) were checked by me only
  for being fixed-order/parameter-free and, where cheap, numerically (all observed values are tiny fractions of the
  allowances) — finiteness, not their values, is what Thm 9.2 needs; (ii) the explicit A₀ additionally needs numerical
  `C_W, B_W` (B3). Thm 9.2: **PROVED relative to (B1)–(B5), TTL's cited inputs and TTL2 Thm 4.1(ii)**. Given that the
  §§4–6 derivations are machine-written and only internally refereed, I would phrase any outward claim ("resolves
  Elsholtz–Tao's open Type I bound") as *conditional on external expert verification*, not as an established result.

## Defects

No FATAL. No MAJOR.

* **m1 (MINOR, Thm 9.1 proof, last sentence).** The number of prefix blocks is `⌊log₂t⌋+1 ≤ 1.443·log(2t)`, and turning
  this single log into the `(log 2t)²` of TTL2's form costs a further factor up to `1/log 2 = 1.443` at small t (and
  `1.5 log(2t) ≤ (log 2t)²` fails for `2 ≤ t < 2.24`). Then `2·1.5·2·(12/ε)` should be `≈ 2·2.1·2·12 ≈ 101`.
  *Repair:* write `C_ε ≤ 200ε^{−1}K₇χ(ε/6)` (A₀ unchanged).
* **m2 (MINOR, §9 "Honest status", all `ttl3_*.md`).** The absolute numerals are asserted, not derived in detail
  (e.g. `H = 2^{512}`, `B = 2^{2048}`, `2^{50}` in Thm 14 §2, `2^{1000}` in §4 of the Thm 14 file). I re-estimated the
  D_x^j-norm bound (≈ 2^{212} ≤ 2^{512}) and checked the transform shapes numerically, but not every constant.
  *Repair:* state explicitly that A₀'s numerical value is "explicit modulo these unverified absolute allowances", while
  the *form* `exp(exp(A₀/ε))` and Thm 9.2 need only their finiteness/parameter-independence.
* **m3 (MINOR, `ttl3_thm2_effective.md` Step 7).** The displayed `Φ(x)=√π iK³∫ξe^{−(Kξ)²} sinh ξ sin(x cosh ξ)dξ` should
  have `tanh ξ` (DI (5.6) `th ξ`; re-derived from `K_{2it}(y)=(y/2t)∫e^{−y chξ}shξ sin(2tξ)dξ` and
  `∫_{−i}^{i}…dv/v`). Since `|tanh| ≤ |sinh|` the upper bounds derived remain valid, but the identity is false as written.
  *Repair:* replace `sinh ξ` by `tanh ξ`.
* **m4 (MINOR, `ttl3_thm2_effective.md` Step 9; LOGLOG3 §5).** The "non-circular limiting proof" of `σ ≤ 1/4` is
  unnecessary — Selberg 3/16 is black box (B4) — and as written it is only a sketch (`|φ̂(κ)| ≥ c(σ)Y^{2σ}` "for all
  sufficiently large Y", unquantified `C(n,v)`). *Repair:* cite (B4) directly, as `ttl3_thm2_twisted.md` Step 9 already
  does, and drop or label the sketch as a remark.
* **m5 (MINOR, presentation, Prop 2.1 (C)).** The main term is `2√2π·π^{5δ}cHQ^{1+4δ−10δ²}N`; the text's `π^{1+4δ}`
  (dropping `π^{−(1−δ)}`) is a valid but confusing overestimate. *Repair:* display the exact power.
