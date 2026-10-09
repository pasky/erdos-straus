# Hostile review B of EXCEPTIONAL_TYPEI_LOGLOG3.md (task R121B)

Reviewer: side agent `side-agent/review-ttl3-b` (independent of reviewer A). Reviewed: `EXCEPTIONAL_TYPEI_LOGLOG3.md`
and `scripts/ttl3_*.md` as of merge of `side-agent/eff-di7` @ f0c5fe9. From-scratch scripts: `scripts/review_ttl3b_*.py`.

**Status: IN PROGRESS** (written claim by claim).

## Verdict per section

| Section / claim | Verdict |
|---|---|
| §1 Lemmas 1.1–1.3 (toolkit) | SOUND |
| §2 (M), (PS), Prop 2.1, Thm 2.2, Cor 2.3 | SOUND (relative to (P1)–(P3)) |
| §3 (P3) from Thm 2 | SOUND |
| §4 / `ttl3_lemma81_effective.md` (P1),(P2) | SOUND (structure + key inequalities re-derived; absolute constants not all re-derived) |
| §5 / `ttl3_thm2_effective.md` | SOUND in its ε-structure; absolute numerical majorants only spot-checked |
| §6 / `ttl3_thm14_effective.md` | SOUND in its ε-structure (U-form confirmed on DI p. 276) |
| §7 constants | SOUND (numerically re-checked in log-log) |
| §8 / `ttl3_nebentypus.md`, `ttl3_lemma81_twisted.md`, `ttl3_thm2_twisted.md` | SOUND relative to (B1),(B3) |
| Thm 9.1 → TTL2 (DI7_ε) conversion; Thm 9.2 | SOUND relative to (B1)–(B5), TTL/TTL2 inputs |
| Claimed literature repairs | all checked ones REAL and correctly fixed (see table below) |

### §1 — SOUND
Re-derived line by line. Lemma 1.1: `f(n)/n^δ ≤ Π((a+1)p^{−aδ/B})^B`, factor ≤ 1 if `p ≥ 2^{B/δ}`, else
≤ `max_a (a+1)e^{−ca} = e^{c−1}/c ≤ 1/c ≤ 2B/δ` (`1/log 2 < 2`); count of small primes ≤ `2^{B/δ}`. ✓.
Exact `sup_n τ(n)^B/n^δ` computed for 5 (B,δ) pairs, always far below the bound (`review_ttl3b_toolkit.py`).
Lemma 1.3: Cauchy circle `|z−x| = x/2` gives `Re(1/z) ≥ 2/(9x)` ✓; max of `u^pe^{−2u/9}` ✓; Leibniz with
`Σ_k C(p,k)k!²(p−k)!² = p!Σk!(p−k)! ≤ (p+1)(p!)²` ✓; convolution identity for η^{(p)} ✓; final constant
`2^{p+1}·4·18^{p−1} ≤ 8·36^p` ✓. Numerically: `max|h^{(p)}|/(9^p(p!)²) ≤ 1` for p ≤ 24 (exact polynomial recursion
`Q_{p+1} = u²(Q_p − Q_p')`), `I = 4.85·10^{−5} ≥ e^{−16}/4` ✓.

### §2 — SOUND relative to (P1)–(P3)
(M) needs only `0 < 2σ_j ≤ 1/2` ✓. (PS) Abel summation + Cauchy–Schwarz in `dξ/ξ` ✓ (constant `2(1+t²(log 2)²)`).
Prop 2.1 (A),(B),(C) re-derived: `Q₁ = πQ^{1−2δ} ∈ [N, Q/2]`, `Y/Y₁ = (Q^{2δ}/π)^{2−2δ} ≥ 1`, exponent
`2δ(1−δ)+(1−2δ)(1+4δ) = 1+4δ−10δ²` (sympy) ✓, `2√2π·π^{1.4} = 44.13 < 45` ✓, `∫(1+t²)/(1+t⁴) = √2π` ✓, error term
`c·Q^{2δ−2δ²}·3Q·N` ✓. Thm 2.2 both branches ✓. Cor 2.3 ✓ (`δ^{−2} ≤ e^{2/δ}/4` for δ ≤ 1/10).
Note: the whole induction is only as good as the *shape* of (P2) (same N, same interval I, `t`-integral with weight
`(1+t⁴)^{−1}` and the switched parameter `πNY/Q`); this is checked against DI Lemma 8.1 below (§4).

## Defects
(numbered as found)

### §8 (nebentypus induction, Prop 8.1, Thm 8.2) — SOUND relative to (P1χ)–(P3χ)
Re-derived independently. Switching geometry: for the first trace at levels rq the arithmetic side is
`Σ_{q,c} g(q)Sχ(m,n;rqc)φ(4π√mn/(rqc))/(rqc)`; for fixed c this *is* the Kuznetsov sum of `(Γ₀(rc),χ)` at moduli
`(rc)q` (same χ mod r induced), so the destination levels are `rc`, `c ∈ (C,16C)`, `C = πNY/(rQ)`, with the **same**
Y (x-support of φ is `≍ 1/Y` on both sides). The `1/r` in C is real and C can be `< N` or `< 1/16`. ✓
* (C1) `C ≥ N`: `C = πQ^{1−2δ}/r ≤ Q/2`, `Y_C = C^{2−2δ}/N ∈ [1, Y]`, `(Y/Y_C)^{1/2} = (Q/C)^{1−δ}`, giving
  `2√2π c H Q^{1−δ}C^{5δ}N`, and `C^{5δ} ≤ π^{5δ}Q^{5δ−10δ²}` uses r ≥ 1 only. ✓ (constant `2√2π·π^{1/2} ≈ 15.7 < 45`).
* (C2) `C < N`: (P1χ) at C with `Y₁ = C+N`: `(C+N+Y₁) ≤ 4N`, `(NY₁)^δ ≤ (2N²)^δ`, `√(YN) = Q^{1−δ}`, `N ≤ Q^{1−2δ}`. ✓
  (Actually gives `10K₁Q^{1+δ}N`.) If `C < 1/16` the destination sum is empty (main term 0). ✓
* Error term `c(QYN)^δ·3Q·N = 3cQ^{1+3δ}N` ✓; closing `H/2 + 90cK₁ + 3c ≤ H` with `H ≥ 200cK₁` ✓.
* Thm 8.2, `Q ∈ [1/16,1)`: (P1χ) at Q with `Y₁ = 1+N`, `Q+N+Y₁ ≤ 4N` ✓.
So the "extra branch" is genuinely needed (Drappeau's "r appears only with negative powers" is not enough on its own:
nothing is inducted when the switched level drops below N) and the author's repair works. The new branch costs only
the absolute factor `200cK₁` in H; class 𝓔 preserved.

### Thm 9.1 conversion and Thm 9.2 deduction — SOUND (relative to Thm 8.2 and TTL2 Thm 4.1)
Checked against TTL2 §1 (DI7_ε): levels `M = rq ≤ M₀` covered by `≤ 2 + log M₀` blocks with `Q_i ≥ 1/16`; prefix
`[1,t]` = closed blocks `[2^k, min(2^{k+1}−1,t)]`, `K ≤ log₂t + 1 ≤ 1.5 log 2t` blocks (Cauchy–Schwarz cost K, which
TTL2 even allows as `(log 2t)²`); `(Q N_k + 1)^{5δ} ≤ (2M₀t)^{5δ}`; with `δ = ε/6`,
`2^{5ε/6}(2 + log M₀) ≤ (2 + 6/(eε))·1.16·M₀^{ε/6} ≤ (12/ε)M₀^{ε/6}` (Lemma 1.2) ✓. Bracket `Q_i ≤ M₀/r ≤ M₀` ✓.
Constant chain `K₇χ(δ) ≤ exp(exp((4B_χ+4)/δ))` ⇒ `C_ε ≤ exp(exp((24B_χ+30)/ε))` ✓ (absorbing `100/ε`).
TTL2 Thm 4.1(ii) uses (DI7_ε) only at `ε = w_N/128`, `w_N = 256A₀/log L`, where `log C_ε ≤ exp(A₀/ε) = L^{1/2}` ✓;
TTL2 needs χ even mod q, levels `4dq²` (q | level), exceptional `t_j ∈ iℝ∖{0}` — all match Thm 8.2's setting. ✓
TTL2's other inputs (Drappeau Prop 4.7 at the fixed tolerance `ε₁ = 1/100`, etc.) carry absolute constants. ✓

### §3 — SOUND
`ch(πκ) = cos(πσ) ∈ [2^{−1/2},1]`, `‖1_I‖² ≤ N+1 ≤ 2N`, `Σ_{Q<q≤16Q}(1 + N^{1+δ}/q) ≤ 16(Q + N^{1+δ})` ✓ ⇒ `K₂ = 32K_{T2}`.

### §4 / `ttl3_lemma81_effective.md` — SOUND (ε-structure fully re-derived)
* Shape of (P2) vs DI (8.5) p. 271 (scan): same N, same interval, `dt/(t⁴+1)`, switched parameter `πNYQ^{−1}`, same Y ✓.
* Sign: with `r = −iσ`, printed (1.22) gives `π/(2 sin πσ)∫(J_{2σ}−J_{−2σ})φ dx/x < 0`; the author's `φ̂ := −φ̂_print`
  convention and "two sign flips cancel" are correct (only absolute values of the arithmetic side are ever used).
* (c) positivity re-derived: ratio of bracket terms `≤ exp(−4σ(log(2/x) − 2))` (uses `Γ(1−u)/Γ(1+u) ≤ e^{4u}`,
  true on `u ≤ 1/2`), main term `≥ 0.18·Y^{2σ}` on the plateau `[1/Y, 4/(3Y)]` ✓.
  **Numerics** (`review_ttl3b_transforms.py`, exact η of Lemma 1.3, mpmath Bessel): `φ̂(−iσ)/(cos πσ·Y^{2σ})` at
  `Y = 2^{32}` and `σ = 10^{−6}, 10^{−3}, .05, .15, .25` is `16.0, 15.3, 3.59, 1.28, 0.85` (all ≥ 1/64 ✓; growth `∝ log Y`
  as σ→0 confirms the `L_Y` factor). At `Y = 1` the same quantity is **negative** (`−0.22 … −0.42`): the repair (ii)
  "DI (8.3) not uniform near Y = 1" is real, and the author's `Y ≥ 2^{32}` + (M) workaround is necessary and sufficient.
* (a) via the Bessel ODE `(D_x² + x²)K = −4r²K` (two self-adjoint moves) ✓; (d),(e) by mean value in the order ν with
  `1/sin πσ ≤ 1/(2σ)` cancelling the `4σ` ✓ (uniform as σ → 0 — the brief's worry about Kuznetsov transform bounds
  "as σ → 0" is answered correctly here).
* Support: `c/C ∈ [64/51, 128/11] = [1.2549, 11.636] ⊂ (1,16)` ✓ (script). (P1): k-support `[8.87NY, 27.4NY]` ✓,
  `K(K+4N²)/(8NY) ≤ 128(N+Y)N` ✓, `K^e(4KN²)^e ≲ N^{4e}Y^{2e} ≤ (NY)^δ` ✓.
* §3.5 small-C range (untwisted): `Q > πNY` ⇒ `Y^{1/2}N ≤ (QN)^{1/2} ≤ Q + N` ✓.

### §5 / `ttl3_thm2_effective.md` — SOUND in ε-structure
* Step 4 (growing order, DI p. 257): ratio `|B/2√t|/|A−u| ≤ 4(√2−1)/√3 = 0.9566 < 31/32` for `t ≥ 3N/4` ✓; with DI's
  support `(1/2,3)`: `2√2(√2−1) = 1.1716 > 1` ✓ (DI's printed `|B/2√t| ≤ 2(√2−1)c^{−1}` silently assumes `t ≥ N`).
  On the disc of radius `2^{−12}`: `|1 + βz^{−1/2}| ≥ 0.0433 ≥ 1/64` ✓. `R_p` count: `(p+1)!·2^{40p}·8e^{16}36^p(p!)² ≤
  2^{100(p+1)}(p!)⁴` ✓; `Σ_{u≠a}|f̂| ≤ 4R_pN(c/N)^p ≤ 4R_p/c` iff `s(p+1) ≥ 2` ✓ for `p = ⌊2/s⌋`.
* Step 2 Gaussian row sum: `e√π cT(1 + 4√πN/(Tc)) ≈ 4.82cT + 34.2N ≤ 100(cT+N)` ✓.
* DI p. 259: for `c < N`, `(cN)^εN ≤ c^{−ε}N^{1+3ε}` and not `1+2ε` ✓ (repair real, harmless). (5.2)'s
  `½K² + O(μN^{1+ε})` cannot hold when `q ≫ N^{1+ε}` since `D_K = ½K² + O(1)` ✓ (repair real, harmless).
* The only growing-order constants are `R_p` (single exponential in 1/δ) and `D(s)` (double exponential); envelope
  `log K_{T2} ≤ exp(96/δ)` re-checked numerically: `loglog K_{T2} = 448, 1336, 4441, 44367` at
  `δ = .1, 1/30, .01, .001` vs `96/δ = 960, …` ✓ (`review_ttl3b_envelopes.py`).
* Not re-derived: the absolute constants in Steps 6–8 (`2^{−20}` Gaussian lower bound, `E_K` angular split). These
  cannot affect the class 𝓔 unless an inequality is *false*, and their shape matches DI pp. 258–261.

### §6 / `ttl3_thm14_effective.md` — SOUND in ε-structure
* U-form: DI p. 276 (scan) indeed first bounds `|Σ_{m,n}S(m,n;c)| ≤ Σ*_d|Σ_m e(md/c)||Σ_n e(nd̄/c)| ≤ Σ*_d f_M f_N`;
  so Prop 6.1's U-form is what the proof bounds ✓ (needed for χ-removal in (P1χ)).
* `TV(f_M') = 2M²` (corners `M²/2` each, interior `M² − 16`, periodic endpoint 16) ⇒ `|a_m| ≤ 2M²/(2πm)² ≤ (M/m)²` ✓;
  `a₀ = 4 + 4log(M/4)` ✓. Zero frequencies via `Σ_{c≤Z}τ(c) ≤ Z(1+log Z)` — no pointwise divisor bound ✓.
* x-support ratio `(17/7)² = 5.90 < 8` ✓; `(1+X+√U)(1+X+√V)/(1+X) ≤ 10√(UV)` for `D ≥ 1, κ < 6` ✓.
* K-transform: `cosh(πr)K_{2ir}(x) = ∫₀^∞cos(x sinh ξ)cos(2rξ)dξ` is the correct normalised representation; DI p. 264
  (scan) uses `K_{2ir}(x) = ∫e^{−x ch ξ}cos(2rξ)dξ` for `f̌`, which carries a `cosh(πr)` — the missing-cosh repair is real.
* Level one has no exceptional spectrum (B5) ✓; only fixed-order derivatives ⇒ `K₁₄` is `2^{1200}(1+K_{T2})(1+6/δ)³` ✓.

### §8 inputs: `ttl3_lemma81_twisted.md`, `ttl3_thm2_twisted.md`, `ttl3_nebentypus.md` — SOUND rel. (B1),(B3)
* (P1χ): `k = rqc ∈ (8NY, 32NY)` independently of r; multiplicity `≤ τ(k/r) ≤ τ(k)`; `|χ| = 1` ⇒
  `|Σ_{m≤M,n≤H}Sχ(m,n;k)| ≤ U(k;M,H)` and positivity lets one drop `r | k` ✓. Valid for every `Q > 0` (`#(Q,16Q] ≤ 16Q`,
  `Σ1/q < 4`) ✓. So no positive power of r and no conductor constant enters K₁χ ✓.
* (P2χ): first trace at levels rq, second at levels rc (same χ induced), switched `C = πNY/(rQ)` ✓; the small-C
  warning ("do not import the untwisted error-only argument, `Q > πNY/r` does not give `Q > πNY`") is correct and the
  replacement (keep the ≤ 15 cofactors; `C < 1/16` empty) works ✓.
* Twisted large sieve: √r enters only through the `c > N²` Weil range (Steps 1, 6, 7), giving `√r L^{−1}N^{1+δ}`;
  Steps 3–5 are χ-free (Cauchy–Schwarz kills `χ̄(d)`; at resonance `δ₁ ≡ δ₂ (mod c)`, `r | c` ⇒ `χ̄(δ₁)χ(δ₂) = 1`) ✓.
  Envelope `K_{LSχ} ≤ exp(exp(B_χ/δ))` and the chain to `A₀ = 24B_χ + 30` re-checked in log-log for
  `(B_W,C_W) ∈ {(1,1),(3,10),(10,10⁶)}`: e.g. at `δ = 1/40`, `loglog K₇χ ≈ 7.1·10³` vs claimed `(4B_χ+4)/δ ≈ 1.1·10⁵` ✓.
* "Even χ is a square" counterexample: `χ₃χ₇` mod 21 is even, `χ₃` is not a square in the dual of `(ℤ/3)^× ≅ C₂` ✓.
* (B3) EVIDENCE (`review_ttl3b_twisted_weil.py`, all even χ mod r, all `r | c ≤ 90`, all m,n mod c, via 2-D FFT):
  `max |Sχ(m,n;c)| / (τ(c)(m,n,c)^{1/2}(cr)^{1/2}) = 1` (attained only at c = 1). So `C_W = 1, B_W = 1` is consistent
  with all small cases; the author's example `A₀ < 2·10⁴` is plausible but (B3)'s constants remain uncertified.

## Literature repairs claimed by the author — checked against the scans

| Claimed repair | Checked against | Real? | Fix works? |
|---|---|---|---|
| DI p. 257: derivative separation fails for η-support (1/2,3) | scan pp. 256–257 | YES: DI's `|B/2√t| ≤ 2(√2−1)c^{−1}` needs `t ≥ N`; true ratio up to `1.1716` | YES (`[3/4,9/4]` ⇒ 0.9566) |
| DI pp. 271–273: supports `[1/2,5/2]` give `16C/25 ≤ c ≤ 32C`, not `(C,16C]` | scan pp. 271–273 | YES (computed: `[0.64C, 32C]`) | YES (`[1.255C, 11.64C]`); harmless for DI (two extra enlargements) |
| DI (8.3) lower bound not uniform near Y = 1 | numerics | YES (transform negative at Y = 1 for all σ) | YES (`Y ≥ 2^{32}` + (M)) |
| DI (8.2) needs `log Y` at κ = 0 | numerics (σ→0 value ≈ 16 ≈ `L_Y`-size at `Y = 2^{32}`) | YES | YES |
| DI p. 259 `2ε → 3ε` | scan p. 259 | YES | YES (final 5ε unchanged) |
| DI (5.2) asymptotic with `O(μN^{1+ε})` | scan p. 258 (`D_K = ½K² + O(1)`) | YES for `q ≫ N^{1+ε}` | YES (`D_K ≤ 2K²`) |
| DI p. 264 missing cosh in `f̌` | scan p. 264 | YES | YES (oscillatory representation) |
| DI below (8.18): `Y₁ = √(Q+N)` → `Q+N` | scan p. 277 | YES (known from O116) | YES |
| Dr p. 17: `S∞∞(m,n;qc)` → `Sχ(m,n;q₀qc)` | Dr pp. 17–18 text | YES | YES |
| Dr p. 17: single `g = Φ(q/Q)` cannot majorise `(Q,16Q]` | Dr p. 17 | YES | YES (DI's four enlargements) |
| Dr p. 17: `dx` → `dx/x`; `ρ_f(m)` → `ρ_f(n)`; p. 18 `S(Q,N,Y,0)` → `S(Q,Y,N,0)` | Dr pp. 17–18 | YES (typos) | YES |
| Dr p. 19: "q₀ only with negative powers" insufficient; C < N branch | Dr p. 19 + §8 | YES (no induction hypothesis when C < N) | YES (Prop 8.1 (C2)) |
| Thm 13 six derivatives beyond (7.7) | not checked (pp. 268–270 not rendered) | — | moot: T-B uses its own cutoff with 7 derivatives |
