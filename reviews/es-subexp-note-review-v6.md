# Referee report R77 — `paper/es-subexp-note.tex` v6 (branch `side-agent/subexp-paper-v6`)

Referee: R77 (hostile). Scope: everything new/changed in v6 per `AGENT_REPORT_O77.md` (C1–C7).
Base: merged `side-agent/subexp-paper-v6` (tip `ca58456`) into the referee branch.

## Compilation
`pdflatex` ×2 (+bibtex) in a scratch dir: 61 pp., 0 undefined references/citations, 0 overfull boxes,
no errors. **OK.**

## Per-claim verdicts (filled in incrementally)

### Lemma 12.3 (quantitative transfer) — SOUND
Re-derived case by case against the proof of Thm 6.1 (lines ≈1340–1440):
* Case 0: `S ≥ (1 − 1/400 − 1/200)μx/φ(Q)` (R₁ ≤ 1/400, middle sum ≤ 1/200). ≥ 1/3. ✓
* Exceptional, χ₁ not in support: middle sum ≤ min(u,1)/200 ≤ 1/200; same bound. ✓
* Case B: `1 − 1/2 − 1/200 − 1/400 = 0.4925 ≥ 1/3`. ✓
* Case A: `S ≥ 0.98λ'μx/φ(Q)`, `λ' ≥ min(u,1)/2`, `u ≥ 16(1−β₁) ≥ 2a` with
  `a = 8c₂⁻¹q₁^{-1/2}(log q₁)^{-2}` (q₁ ≥ 3 as χ₁ is a real primitive non-principal character, so Thm 5.x
  applies). Then `0.98·min(2a,1)/2 ≥ min(a,1)/3` in both sub-cases (2a ≤ 1: 0.98a ≥ a/3; 2a > 1: 0.49 ≥ 1/3). ✓
* "q₁ | Q ⇔ Case A": real primitive conductor is `2^e f'` (e ∈ {0,2,3}, f' odd squarefree) and 8 | Q, so
  `f₂ = 1 ⇔ q₁ | Q`. ✓ (the paper only states ⇐-direction in the parenthetical; both hold.)
* Counting step: terms with `B(p) > 0` satisfy `B(p) ≤ 1[W(p)>T] ≤ 1`, so each positive term ≤ log x;
  negative terms only help. ✓
The constant 8 in λ is conservative (16 would also work); harmless.

### Lemma 12.4 (leaves) — SOUND
Re-derived: per-step ratio (process prob)/(conditional Haar mass) is 2 at level 0 (incl. the forced step at 3:
1 vs 1/2) and 1 at level ≥ 1; root Haar mass 1/4. Hence `P(L) = 4·2^{k_L}/φ(Q_L)`. From-scratch check
`scripts/review_r77_leaves.py`: enumerates the full decision tree for 4 arbitrary deterministic
(hash-driven) step/stop rules over ℓ ∈ {3,5,7,11,13} with forced 3,5,7: probabilities sum to 1, the formula
holds exactly (Fractions) at all 546–1037 leaves, leaf classes pairwise incompatible, `r_L` square mod every
odd ℓ | Q_L. The identity only uses that the rule is a function of (Q,r) — true for "least heavy ℓ ≤ Y".

### Lemma 12.5 (level-0 steps) — SOUND
* Optional-stopping step: unforced (ℓ,0) step taken ⇒ `w̃_ℓ > η` ⇒ `1 ≤ G^{(ℓ,0)}_τ/η`; G supermartingale by
  Lemma 4.x(a) with `φ = β^ω 1[ℓ|M]`; summing ℓ ≤ Y gives `ω_Y(M)`. Forced steps: 3 and log 105; prime 2: log 2. ✓
* `y ≤ (1+loglogY)t^y` and `y ≤ (logY)e^{y/logY}`, `ℓ^s−1 ≤ (e−1)s logℓ` (s logℓ ≤ 1): checked numerically
  (same script) and by the max of `y t^{−y}` at `y = 1/log t`. ✓
* NT class for twisted f₂: values ≤ 7 resp. ≤ 6e < 17 at prime powers, so `F ∈ 𝓜₂(17, B, 1/200)` with B
  absolute (`17^{ω(a)} ≪ a^{1/200}`); Euler-ratio products `exp(O((t−1)loglogY)) = O(1)` and
  `exp(O(s·Σ_{ℓ≤Y} logℓ/ℓ)) = O(1)`. ✓ Exponents: `η⁻¹·Λ³·logY·loglogY ≍ Λ³(logΛ)²logloglogΛ`... i.e.
  `Λ³(logΛ)²loglogΛ` as stated (loglogY ≍ loglogΛ); `η⁻¹Λ³(logY)² ≍ Λ³(logΛ)³`. ✓

### Theorem 12.1 (lower tail) — SOUND (one MINOR label point, D1)
* P(good) ≥ 1 − 1/4 − 4·(1/8) = 1/4. ✓ Good leaf ⇒ (6.x)=eq:goodQ with C→2C (8× instead of 4× means). ✓
* Uniformity (author's check point 2): with `S₁ = 2CΛ³logΛ` fixed (independent of L), Lemma 11.x gives
  `E[F−B] ≤ δ_L/100` for every good leaf (needs only `S_β(L) ≤ S₁`, `δ_L ≥ e^{−3S₁}`), so `μ_L ≥ 0.99δ_L`,
  `A_L ≤ 1.03`, `d_i ≤ T³e^{2τ}` with the same τ; `log Z_L ≤ log Q_L + 3Λ + 2τ ≤ C₃Λ⁴logΛ` uniformly
  (the paper's `2(3Λ+2τ)` is a harmless overestimate). One x works for all good leaves. ✓
* Leaf-dependent exceptional character (check point 2 / C1 deviation): Lemma 12.3 is applied leaf by leaf;
  only `q₁ | Q_L` is used, and `q₁ = 2^e f'` with `f' | rad_odd(Q_L)` gives `q₁ ≤ 8·rad(Q_L)` (even ≤ 4·rad).
  Removing the "depends only on x" sentence is correct and sufficient. ✓
* Summation: `Σ_good λμx/(3φ(Q_L)log x) = (x/(12 log x))Σ P(L)2^{−k_L}λμ ≥ (x/(48 log x)) min`. ✓
  `x/log x ≥ π(x)/1.26` (Rosser–Schoenfeld 1.25506). ✓ Disjoint fibres + 840 | Q_L ⇒ distinct hard primes. ✓
* Hypotheses of Thm 6.1 for (Q_L, r_L): leaves are square-class quarantines; `B ≤ F` on ℤ and Lemma 4.x(i). ✓

### Corollary 12.2 — SOUND
Range arithmetic re-done: `c' ≤ 1` ⇒ `logΛ ≤ ¼ loglog x` (x ≥ e^e), so `CΛ⁴logΛ ≤ (C/4)c'^4 log x ≤ log x`
iff `c'^4 ≤ 4/C`. Lower side from Thm 11.2 (range `Λ ≤ c₁(log x)^{1/4}` contains ours). Labels consistent. ✓

### One-fibre paragraph, Remark 12.6 — SOUND
`log(1/λ) ≤ ½log Q + O(loglog Q)` since `q₁ | Q`. Conditional improvement: `u ≥ c₀ log x/log Q_L ≥ 1` needs
`log x ≥ log Q_L/c₀`, true as `log x ≫ Λ⁴logΛ ≫ log Q_L`; correctly labelled conditional.

### §15 setting + identity (15.1) — SOUND
From scratch (`scripts/review_r77_mjacobi.py`): identity (15.1) verified in exact arithmetic for every
`uvw = A`, `gcd(v,M)=1`, and `{−uv⁻¹} = R_m(M) = {−mD : D | A²}` for 20 values of m, M ≤ 600. ✓

### Lemma 15.1 (Jacobi dichotomy) — SOUND
Proof re-derived ((d): t=1 ⇒ 8 | mA in both sub-cases m ≡ 0 (8), m ≡ 4 (8)). Brute force from scratch:
(a)–(d) and "M ≡ 7 (8) ⇒ symbol −1" on **911 163** m-atoms (M odd, M ≤ 2·10⁴,
m ∈ {4,…,16,18,20,21,22,24,28,30}): no failures.

### Proposition 15.2 — SOUND
Both constructions re-derived (m odd: q = 2, ℓ ≡ 5 (8); m ≡ 2 (4): q ≡ 3 (4), ℓ ≡ −1 (mq), ℓ ≡ 1 (4)).
Brute force: firing primes exist for every m ≢ 0 (4) tested (first ones e.g. m=5: 19, 29, 59, …; m=6: 11, 17,
…), and **none** for m ≡ 0 (4) (ℓ < 3000), as Lemma 15.1(d) predicts. The example m=5, ℓ=29 (A=6) ✓.
Note: the smallest firing prime for m=5 is ℓ = 19 (≡ 3 (8), via D = 2, t = 1) — not covered by the
construction, but the proposition only claims infinitely many; no defect. The "M ≡ 7 (8): sufficient,
not necessary; e.g. m=5, M=19, D=1" sentence is correct at the level of atoms (atom (19,2) does fire).
