# Hostile cross-lab review (Claude Opus), round 3 — `notes/z80/EXTREME.md` §0 and §§10–13 at `5d8e8b2f1`

Reviewer: Claude Opus (Anthropic), cross-lab to the GPT/Astra author. Scope: the final-round diff `63fb1747a..5d8e8b2f1`
(§0 rewrite, new §§10–13, `scripts/z80_gap_{constants,genus}.py`, `data/z80/model/*`). Rounds 1–2 were reviewed
exhaustively before (`REVIEW_EXTREME_OPUS.md`, `REVIEW_EXTREME_R2_OPUS.md`) and are not re-reviewed here; their
censuses were not rerun. Nothing was committed, no author file was edited, and nothing was posted externally. Every
computation ran under `ulimit -v 6000000` and `timeout ≤ 1800`, with at most 2 concurrent processes and offline `uv`.
No binaries are left behind (compiled into `/tmp`, now deleted).

## 1. Verdict

* **§13 (MS⁺₁₀₅) on (2·10¹¹, 3·10¹¹]: CONFIRMED** in three ways. (i) A full replay of both z75 engines reproduces
  `data/z80/model/ms1.txt` and `ms2.txt` exactly (diff-identical). (ii) An **independently written Opus engine**
  (`scripts/z80_xr3_opus_ms.c`, with a different design; see §3.1) finds no unknown. (iii) It reproduces every
  reported statistic: the eligible counts, the 2,198,720 late nonsquares, the 22,974 squares, the maximum modulus
  11,074,055 at 218,136,733,117, and even the primary engine's post-pair-crossing residuals 143/1012 with their maxima
  579,239 @ 218,294,896,081 and 1,462,103 @ 289,626,521,041.
* **Theorem H: CORRECT as stated.** I checked the genus error term O(X/(log X)^{1+J/2+1/12}) step by step (§2.1).
* **Theorem I: CORRECT relative to FHRSS Thm 1.1(2).** All hypotheses of the archived statement hold, including at 2,
  3, 5 and 7 and for imprimitive or non-squarefree k. A falsification run on 23 windows (112,509 constructed primes)
  found no failure. One citation-strength caveat applies (F3).
* **Dickson / growing-BH paragraph: CORRECT.** The rate distinction is stated properly, and the arithmetic of the BH
  rate checks out. The construction was instantiated for J = 1, 2, 3 (20 primes each, g = T+4, all in 1 (840)).
* **§11 Landau constants: CORRECT.** I re-derived the model coefficients (5) with a different method (direct CRT
  enumeration, L(1,χ) from Dirichlet partial sums, products to 10⁶). On 12 tuples × 6 residues, including the
  residue-dependent ones, they agree with `coeff.csv` to ≤ 6·10⁻⁶ relative.
* **Numerical illustrations: REPRODUCED.** `genus.txt` is reproduced exactly (all 16 rows) by independent pure-Python
  code with no PARI. `forecast.txt` and `coeff.csv` are reproduced byte-identically by a replay. My own
  reimplementation of the §12 rules gives 0.3901 against the author's 0.38987 for the expected number of g ≥ 111
  through 5·10¹².
* **No-fit forecasting check: the §12 model already fails on the bulk at 10⁷, not only at the records** (F1). The note
  never claims a successful prediction, so this is a scope and diagnosis correction, not a retraction. The note's stated
  mechanism for the miss is the wrong one.
* **No ES claim anywhere; scope discipline is good.** The findings below are F1–F8. Only F1 and F3 are substantive. None
  blocks the RECORD/DATA promotions.

## 2. Mathematics: what I checked

### 2.1 Theorem H (full-window genus reduction)
* **E ⇒ failure.** p = 4x − k gives χ(p) = χ(4)χ(x) = χ(x) = 1 for quadratic χ when every prime of x lies in ker χ. All
  divisors of px are then in ker χ, while χ(−1) = −1, so u ≡ −v is impossible. For p > k the factors are units:
  ℓ | k and ℓ | x would force ℓ | p. ✓
* **Converse.** The plentiful subgroup H is realised by squarefree divisors because the generators are distinct
  classes, each with ≥ |G| > ord(g) − 1 distinct primes. Failure forces −1 ∉ H. At index 2, any prime b ∉ H gives
  −b⁻¹ ∈ H; it is realised by a divisor d coprime to b, since b lies in a non-plentiful class, and bd ≡ −1 follows. So
  index 2 is *exactly* E(k,χ_H) with χ_H odd. ✓ Exceptions are < |G|², because there are < |G| primes in each of at
  most |G| non-plentiful classes. ✓
* **Exponent.** The non-genus case needs index ≥ 3 in some coordinate. The cost is
  (1−t)Σ(1−1/i_j) ≥ (1−t)(J/2+1/6) ≥ J/2+1/6−1/24 > J/2+1/12 for t = 1/(12(J+1)). ✓
* **Weight trick.** 1[#exc ≤ E] ≤ t^{−E}·t^{#exc}. Primes above z are dropped, which is legitimate for an upper bound.
  The forbidden classes −k_j are distinct for large ℓ, and Mertens in APs gives the density (1−1/i_j). ✓
* **Overlaps.** Two distinct odd quadratic characters in one coordinate give a joint kernel of index 4, so the cost is
  ≥ J/2+1/4. ✓ Finitely many subgroup choices. ✓
* **Remark (not an error).** For prime windows a ≥ 13, H's secondary exponent is strictly better than
  `notes.md` (70.28)'s 3/2 + 1/(a−1). For example, at a = 19 the odd-order subgroups have index 2, 6 or 18, so the
  non-genus saving is ≥ 1/3 − O(t). The "compare `notes.md` Thms 70.5, 70.7, 70.9" pointer should say that H sharpens
  (70.28), or explain why not (F5).
* **Size of the constant.** The implied constant is ≍ t^{−Σφ(k_j)²}; at k = 19, J = 1 that is 24^{324} ≈ 10^{447}. Also,
  the "plentiful" threshold (≥ φ(k) distinct primes in one class) is never met at any computable height. So (4) carries
  no numerical information at observable heights. This matters for F1.

### 2.2 Theorem I (each window fails at ≍_k X/(log X)^{3/2} 𝔐-primes)
* **FHRSS Thm 1.1(2)** (`sources/sieve/2504.20289.txt` l.34–56). The hypotheses, with f = U²+UV+sV², a = 1, B = k+1,
  A = −k, l = 1:
  * f is primitive (a = 1) and positive definite, with D = 1−4s = −k not a square. (a, 2D) = 1 ✓
  * gcd(A, B) = gcd(k, k+1) = 1 ✓
  * 2 | AB because B is even, so the D ≡ 5 (8) exclusion is moot ✓
  * gcd(m, 2DB) = gcd(m, 2k(k+1)) = 1 by the choice of m ✓
  * gcd(l−A, m) = gcd(1+k, m) = 1 ✓
* **Lemma 4.1 exceptions.** The squarefree-d exception "3 | D, 3 ∤ A, …" cannot occur, since 3 | D = −k forces 3 | A.
  The other exceptions need 2 ∤ AB. ✓
* **Membership in 𝔐 and failure.**
  * At ℓ | k+1: p ≡ −k ≡ 1 (ℓ). At odd ℓ | k: 4p ≡ (2U+V)² (ℓ), a nonzero square. At ℓ = 3 that gives residue 1. ✓
  * At 2: if k ≡ 7 (8), then 8 | k+1. If k ≡ 3 (8), then s is odd, F is odd on primitive pairs, and p ≡ 4−3 ≡ 1 (8). ✓
  * x = sF. Odd ℓ | s gives (−k/ℓ) = 1. For odd ℓ | F, primitivity forces ℓ ∤ V, and ℓ ∤ k since ℓ | k would give
    ℓ | p. Reciprocity for odd k ≡ 3 (4) gives (ℓ/k) = (−k/ℓ), valid for any odd k including non-squarefree k. If
    2 | x then k ≡ 7 (8) and (2/k) = 1. ✓
* **Falsification run** (`scripts/z80_xr3_opus_thmI.py` → `r3_opus/thmI_check.txt`). k ∈ {3, 7, …, 63, 75, 99, 119,
  147, 175, 231, 243, 343}, |U| ≤ 300, 1 ≤ V ≤ 300: 112,509 primes (with multiplicity), **0 outside 𝔐, 0 window
  successes**, and the Jacobi-kernel assertion held throughout.
* **Remaining items.** The upper bound from G is fine. The g ≥ 7 infinitude via Vaughan's exceptional-set bound is
  fine. "No g ≥ 11" is correctly disclaimed.

### 2.3 Dickson construction and the growing-tuple BH rate
* 4j | Q, since j | lcm(1..T) and 4 | 3360. At ℓ ≤ T the extra ∏ℓ ensures ℓ | Q/(4j), so the values there are 1. At b
  the forms are constant in v, equal to (4j−2)/(4j) ≢ 0, because 0 < k−1 < b. At other ℓ > T there are ≤ J+1 roots,
  fewer than ℓ. Window b fires through (u, v) = (1, p). ✓
* **Instances** (`scripts/z80_xr3_opus_dickson.py` → `dickson_check.txt`). J = 1, 2, 3, 20 instances each, all with
  p ≡ 1 (840) and g = T+4 ≤ b.
  * At J = 1 the note's b ∈ (2T, 4T) can be 7 | Q. The note's "for large T" covers this; the script uses b = 11.
* **Rate.** log p = (1+ε)J log J + O(J), so g > 4J ≈ 4 log p/((1+ε) log₂ p). ✓ The expectation is
  V/(log V+O(T))^{J+1} = exp((ε+o(1))J log J). ✓
* **Singular series.** The loss is Σ_{ℓ>T} O(J²/ℓ²) = O(J/log J). ✓
* **Labels.** "Stronger than ordinary BH" and "fixed-tuple BH gives only X/log^{J+1}X" are both correct and correctly
  labelled CONDITIONAL.

### 2.4 §11 constants
* **Landau constant.** F(s)² = ζ(s)L(s,χ)·∏_{ℓ|k}(1−ℓ^{−s})·∏_{χ(ℓ)=−1}(1−ℓ^{−2s}) with imprimitive L. Selberg–Delange
  at exponent 1/2 then gives C = π^{−1/2}[…]^{1/2}. ✓
* **L(1,χ_f) formula.** L(1,χ_f) = −πf^{−3/2}Σaχ_f(a). Sign check at f = 3: π/(3√3). ✓
* **Odd quadratic characters.** For odd k these correspond to squarefree f | k with f ≡ 3 (4). ✓
* **Model (5).**
  * The per-residue local factors at 2, 3, 5, 7 are handled correctly, including the mod-8 test at 2.
  * The distinct-class count at colliding shifts is right.
  * Expanding the sign product over subsets is equivalent to my direct CRT enumeration.
  * The residue dependence (k = 75, 99, 115, 231) arises exactly as the local analysis predicts. For example, for
    χ₁₅ with k = 75, 7 is forbidden, and r = 121 ≡ 2 ≡ −75 (7) kills that tuple.
* **Normalization.** The all-primes figure is Σ_r A_r/192 = A/32 for residue-independent A. ✓
* **Agreement.** Independent values are in `r3_opus/coef_indep.txt`. The largest deviation from `coeff.csv` is
  2.5·10⁻⁵ absolute, attributable to truncation at 3·10⁴ versus 10⁶. This is consistent with the note's
  "not certified final digits".

## 3. Independent computations (coverage statement)

### 3.1 (MS⁺₁₀₅) on [200000000001, 300000000000]
| engine | output | time |
|---|---|---|
| z75 `push2_comp.c R 1` (replay) | `nonM.n=10714285715 late=143 max_late_d=579239 n=218294896081 … M.n=714262740 late=1012 max_late_d=1462103 n=289626521041 … unk=0` — identical to `model/ms1.txt` | 6m16s |
| z75 `push2_comp_verify.c` (replay) | `squares 22974 late_unsquared 2198720 max_f 11074055 n 218136733117 unknown 0` — identical to `model/ms2.txt` | 48s |
| **Opus `z80_xr3_opus_ms.c` (new, independent)** | eligible nonM 10,714,285,715, M 714,262,740; survivors of d ≤ 8191: 2,198,720 nonsquares (676,925 in 𝔐) + 22,974 squares; max minimal d 11,074,055 @ 218,136,733,117; **unknown 0**; comp-style residual 143 / 1012 with the same maxima and arguments | 51s |

Design of the Opus engine (no author code):
* It uses R(n) ≥ 1 ⇔ ∃ d = 4cu−1 with n ≡ −u (mod d), so that b = (n+u)/d ≥ 1. This is equivalent to the `Z59_MSPLUS.md`
  definition 4uBC − u − B = n.
* n ≡ 5 (12) is discharged by (c, u) = (1, 1), with the identity asserted for every such n.
* n ≡ 1 (12) is split into its 48 classes mod 840 coprime to 105. Each AP 840i + r is sieved by (d, u) pairs, d ≤ 8191,
  through a CRT offset that is checked explicitly at the first hit.
* Survivors get a minimal-d search up to 2·10⁹. Each witness is verified in 128-bit arithmetic as 4cub − u − b = n.
* A separate pass applies the primary engine's t ≤ 20000 pair family, only to compare the residual counts.
* The eligible counts also agree with a closed-form class/square count in Python.
* On [10⁶+1, 3·10⁶] it reproduces the known sub-threshold zeros (1134241, 1724209, 1726201, 2956321) exactly like the
  verifier, as a sanity check.

**Coverage:**
* (2·10¹¹, 3·10¹¹] now has two same-lab engines plus one cross-lab, independently coded engine. All three agree.
* For (10¹¹, 2·10¹¹], round 2 supplied only a replay of the same-lab engines.

### 3.2 Other replays and checks
* `z80_gap_constants.py` replay: `coeff.csv` byte-identical; `forecast.txt` identical apart from a trailing newline.
* Genus census (`z80_xr3_opus_model.py census` → `census_indep.txt`). Own sieve, SPF factoring and Jacobi symbol;
  18,878 hard primes. All 15 windows plus the 3:7 row equal `genus.txt`, e.g. 6263/5554 at 11 and 9014/5751 at 19.
  - **Why the zero non-genus rows are deterministic, not luck.** At k = 7, 𝔐 forces 2 | x and ⟨2⟩ = QR₇, so any
    nonresidue prime factor completes −1. At k = 3 there is only one odd character.
* Empirical least-gap distribution, same 18,878 primes:
  3:8311, 7:4557, 11:3896, 15:844, 19:694, 23:378, 27:56, 31:100, 35:16, 39:14, 43:2, 47:5, 55:2, 59:3.

### 3.3 Short no-fit forecasting check (`z80_xr3_opus_forecast.py` → `forecast_check.txt`)
This is my own implementation of the §12 rules on the verified coefficients. It compares model survival
P(g ≥ 4j+3), averaged over (10⁷, 2·10⁷] with weight 1/log p, against the empirical distribution above.

| g ≥ | 7 | 11 | 15 | 19 | 23 | 27 | 31 | 35 | 39 | 43 | 47 | 51 | 55 | 59 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| model | .545 | .299 | .0825 | .0491 | .0143 | .0041 | .0022 | 5.5e-4 | 3.2e-4 | 9.1e-5 | 3.0e-5 | 7.8e-6 | 4.8e-6 | 1.3e-6 |
| actual | .560 | .318 | .112 | .0673 | .0305 | .0105 | .0075 | .0022 | .0014 | 6.4e-4 | 5.3e-4 | 2.6e-4 | 2.6e-4 | 1.6e-4 |

Reading the table:
* The ratio grows monotonically with depth: 1.03, 1.07, 1.36, 1.37, 2.1, 2.5, 3.3, 4.0, 4.2, 7.0, 17, 34, 55, 119.
* For g ≥ 47 the model expects 0.58 primes and 10 are observed, a Poisson tail of ~10⁻⁹.
* The model expects 0.0024 zeros in total, all below 10⁶. That is consistent with ES, but carries no information.
* It expects 0.390 primes with g ≥ 111 through 5·10¹²; 9 are observed (Opus R2 census).

## 4. Findings

* **F1 (substantive; model scope and diagnosis, §12).**
  * **What the model is.** The §12 single-window marginals s_j = A_r(k_j)/√t are **genus-only** (index-two) constants.
  * **What the data show.** At observable heights the non-genus share of actual failures is large: 11% at k = 11,
    36% at k = 19, 17% at 27, 25% at 51, 26% at 231 (`genus.txt`). By §2.1, Theorem H's asymptotic suppression of this
    share has an astronomically large constant, with no numerical content at observable heights.
  * **Effect on the tail.** The §12 tail is therefore biased thin, window by window. §3.3 shows the bias compounding
    into a 10–100× underprediction already at 10⁷, for gaps 43–59, far from the records.
  * **The note's diagnosis is the wrong one.** It says "Even the prefix marginals can miss hard inputs with many
    factors in very small residue sets". The dominant mechanism in the data is the opposite: inputs with **few** prime
    factors, in the bounded-exception regime of H's proof.
  * **Requested fix.** State that (5) and §12 model only genus failures. State that the no-fit model is rejected at
    bulk level at 10⁷, not just "far from identified" at the records. Correct the mechanism sentence.
  * **Knock-on scope.** The `forecast.txt` thresholds (75/99/147/175) and the "5·10⁻⁷⁰ beyond 10¹⁸" figure should
    carry the explicit qualifier "genus-only marginals; underpredicts observed tails at 10⁷". The note already labels
    them "not an empirical bound".
* **F2 (wording error, §11 last sentence).** "even when the fixed-k remainder in (4) has a power saving" is wrong.
  (4) has a **log-power** saving (log X)^{−1/12} (§0 correctly says "log-power"). Fix the wording.
* **F3 (citation strength, Theorem I and §0/STATUS).**
  * FHRSS is an unrefereed arXiv v1.
  * Its Theorem 3.9 extends BF12 Thm 1.2 to bounded powers of bad primes; the authors explicitly "do not include the
    proof" (source l.838–841). Thm 1.1 depends on it.
  * The note's "PROVED rel. FHRSS Thm 1.1(2)" is formally fine. But the §0 Scope ("each fixed k … ≍_k") and the
    proposed STATUS §1D clause ("each single window has the matching order on 𝔐") should say "rel. the FHRSS preprint".
    Implicit constants depend on k (and m).
  * Priority of Theorem I and of (4) for composite or joint windows is unverified; say so as for G.
* **F4 (§0 form).**
  * The label line omits **CONDITIONAL** (the Dickson construction; the growing-tuple BH rate) and **CONJECTURE**
    (g = O(log p) on 𝔐).
  * Triage gives no class for the proposed §1D line (G/H/I). Theorem-level STATUS lines need an explicit RECORD or
    HEADLINE class and its review gate. This review supplies the cross-lab review for §§10–11.
  * At export, replace "final-round review pending" with a pointer to this file.
* **F5 (cross-reference).** H sharpens the secondary exponent of `notes.md` (70.28) for prime a ≥ 13 (§2.1). The
  "compare" pointer should note this or explain why not. This is also worth an erratum-style pointer in notes.md §70 at
  export, not by the lane.
* **F6 (export consistency, (MS⁺₁₀₅) 3·10¹¹).**
  * The delta's "z75 and z80 two engines" is accurate, but both engines are z75 code from one lab. Add "cross-lab
    independent engine on (2·10¹¹, 3·10¹¹] (`REVIEW_EXTREME_R3_OPUS.md`); replay only on (10¹¹, 2·10¹¹]".
  * Range references to update at export: STATUS §1F l.165 and §2 item 1 l.178–179 ("certified to 10¹¹"), FRONTIER
    l.966, OPERATIONS l.60. Use `git grep -n 'certified to \*\*10¹¹\|certified to 10¹¹'`.
  * The round-2 paragraph in §0 still names its own sync list, which is fine. Make sure the round-3 endpoint is the one
    exported.
* **F7 (minor wording, §12).**
  * "The reported figure integrates down to 10¹⁸" should read "from 10¹⁸ up to e^{86}"; the value 4.65·10⁻⁷⁰ checks.
  * The late-zero proxy uses only the (★)/c=1 count R. Since P(no ES solution) ≤ P(R = 0), z is an *upper* proxy for
    zeros; say so.
  * "one-expected-exceedance g" is the last threshold whose cumulative mean is ≥ 1; spell that out once.
* **F8 (minor, §13 wording).** "Independent modulus-word verifier" means independent of the primary engine's
  algorithm, by the same lab. Keep "independent" but qualify it as same-lab unless citing §3.1 here.

## 5. Promotion recommendations
* **R₈ floor and (MS⁺₁₀₅) → 3·10¹¹: promotable** with the F6 consistency edits. (MS⁺₁₀₅) on (2·10¹¹, 3·10¹¹] now has
  cross-lab independent coverage.
* **G/H/I one-line §1D: acceptable** if labelled "PROVED rel. upper sieve, fixed-modulus Mertens; single-window order
  rel. FHRSS preprint", with F4's triage class. The test for STATUS is met only marginally. A FRONTIER §3/§6 entry would
  be an acceptable alternative.
* **§§11–12 model: EVIDENCE only.** Not for STATUS. If quoted in FRONTIER, add the F1 qualifier.

## 6. Replay (all under `ulimit -v 6000000; timeout ≤ 1800`, serial or ≤ 2 parallel)
```
cc -O3 scripts/z75_push2_comp.c -lm -o /tmp/comp && /tmp/comp R 1 200000000001 300000000000
cc -O3 scripts/z75_push2_comp_verify.c -lm -o /tmp/verify && /tmp/verify 200000000001 300000000000
cc -O3 scripts/z80_xr3_opus_ms.c -lm -o /tmp/mine && /tmp/mine 200000000001 300000000000 8191
uv run --offline --no-project python -B scripts/z80_xr3_opus_model.py census   # genus census + g distribution
uv run --offline --no-project python -B scripts/z80_xr3_opus_model.py coef     # independent A_r(K)
uv run --offline --no-project python -B scripts/z80_xr3_opus_forecast.py       # no-fit check
uv run --offline --no-project python -B scripts/z80_xr3_opus_thmI.py           # Theorem I falsification
uv run --offline --no-project python -B scripts/z80_xr3_opus_dickson.py        # Dickson instances
```
Outputs: `data/z80/xreview/r3_opus/{ms1_replay,ms2_replay,opus_ms_indep,census_indep,coef_indep,forecast_check,thmI_check,dickson_check}.txt`.
Delete the `/tmp` binaries afterwards.
