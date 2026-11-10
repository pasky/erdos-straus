# Z69_MINE — what do the hard primes' U₇ witnesses know? (data-mining lane, wave z69)

**ES is OPEN. Nothing here proves or disproves it.** Status: final + round 2 (§12; verdict §7/§12.6: **null (non-rejection) result; narrowed; no HOT LEAD**;
not a HOT LEAD).

Definitions (Z60_LOPEZ Lemma 7; Z68_U7F, Z68_U7O). For odd n: a **witness** is f ≡ 7 (mod 8) with
r := (−n mod f) ∈ {1, …, f−1} dividing f + 1; its canonical **word** is (x, y, z) = (r, (f+1)/r, (n+r)/f), with
xyz − x − z = n and 8 | xy. U₇(n) :⟺ W(n) ≥ 1, where **W(n) := #{witnesses f}** (all witnesses satisfy f ≤ 2n + 1).
Only p ≡ 1 (mod 8) matters (p ≡ 5 (8): f = p + 2). Scripts `scripts/z69_mine_*`, data `data/z69/mine/`.

## 0. Mandatory falsifier table (z58 → z69; checkpoint-1 version, restated at the end)

| screen | how a mined rule must behave / how this lane checks it | label |
|---|---|---|
| **F1 odd squares** | W(m²) = 0 for every odd m (Z60 Lemma 7(ii)); re-checked by the census engine for all odd squares ≤ 10⁸ (0 exceptions). A mined *search* rule outputs only verified words and is vacuous here; a mined *constructive* rule (formula p ↦ candidate word) must be run on all odd m² ≤ 10⁶ (= K1) and must produce nothing. Any proof built on a mined rule must say where non-squareness of p enters. | PROVED (Z60) + CERTIFIED |
| **F2 numerator 8 / C-even** | The 12 R₈-zero primes in [10¹⁰, 1.1·10¹⁰] are U₇-positive (Z68). Additional screen U⁽⁸⁾: 45 U⁽⁸⁾-zero primes ≤ 10⁸ (38 of them ≡ 1 (8), `data/z68/u7f/u8zero_primes_1e8.txt`): a mined rule must produce non-U⁽⁸⁾ words there (= K3). | CERTIFIED (Z68) |
| **F3 composites** | The non-square composite U₇-zeros n ≡ 1 (8) ≤ 10⁸ are exactly Z₇ = {105, 1465, 3865, 4545, 10305, 12145, 39361, 67425} (census engine, CERTIFIED here to 10⁸, Z60 to 10¹⁰). A constructive rule must not "produce" a word there (= K2); a rule that is defined only for primes must name the step using primality. | CERTIFIED |
| **F4 known zeros** | The 14 (★)-zero and 38 𝔊*-zero primes are U₇-positive (Z60). The hard set H below contains the prime-witness-free primes (2521, 21841, 66529, …), the Conjecture-C exceptions and the cascade/Dickson primes; K4 requires success on all of H. | CERTIFIED (Z60, Z68) |

## 1. Precise questions attacked

**Q1 (structure of W).** For primes p ≡ 1 (8): how is W(p) distributed, how much of its variation is explained by
*local* data (p mod small moduli), and what characterises the low-W tail?

**Q2 (p-intrinsic witness rule — the brief's target).** Is there a rule R: p ↦ finite candidate set of words, built
from p's own arithmetic — Gaussian representation p = a² + b², p = c² + 2d², p = e² − 2g², the fundamental unit /
negative Pell solution of ℚ(√p), the continued fraction of √p, factorisations of p ± 1, p + 2, p + 4, 2p + 1, 4p + 1,
class-group / Rédei data, the least non-residue n_p — that yields a witness at (essentially) every prime?

**Hard set H** (fixed at checkpoint 1):
* H-low: primes p ≡ 1 (8) ≤ 10⁸ with normalised count w(p) := W(p)/(0.179 log² p) < 0.30 (574 primes);
* H-np: the 231 prime-witness-free primes ≤ 10⁹ (`data/z68/u7f/noprime_primes_1e9.txt`);
* H-C: the Conjecture-C exceptions 3361, 21841, 76441;
* H-deep: the 20 cascade-depth primes m(p) ≥ 16 ≤ 4·10⁹ (`data/z68/u7o/deep_m16_4e9.txt`) and the 22 Dickson primes
  (`data/z68/u7o/dickson_C{3,4}.txt`);
* H-u8: the 38 U⁽⁸⁾-zero primes ≡ 1 (8) ≤ 10⁸.
**Controls:** for each H prime three nearby primes p ≡ 1 (8) (≈ ±26 % linear window, then next prime; approximate size
matching, *not* log-uniform, gap-weighted; medians 19.0·10⁶ vs 19.2·10⁶); same-p shuffled controls
(dictionary of a *different* prime of the same size tested against the witnesses of p); odd squares; Z₇.

## 2. Pre-registered kill tests for any candidate rule R (from the brief; fixed before any mining run)
* **K1** R gives no word at any odd square ≤ 10⁶ (constructive rules; vacuous for verified-search rules).
* **K2** R does not "prove" U₇ at Z₇ = {105, 1465, 3865, 4545, 10305, 12145, 39361, 67425}.
* **K3** R produces witnesses beyond U⁽⁸⁾ (type 2/4/6 with 8 ∤ y) on the U⁽⁸⁾-zero primes ≤ 10⁸.
* **K4** R succeeds on ≥ 99.9 % of primes p ≡ 1 (8) ≤ 10⁸ AND on all of H.
* **K5 (lane-added)** R is not, for a fixed bound, contained in the bounded-letter / bounded-shift-divisor menus
  that Z68_U7O Prop K / Cor K′ kill under Dickson, and is not a finite congruence menu (Cor B′).
* **Enrichment criterion (lane-added, for feature statistics):** a feature counts as *p-specific* only if its hit
  rate on H (or on all primes) exceeds the same-p shuffled control by ≥ 4σ *and* the excess replicates on a disjoint
  held-out sample. Hits that are forced or forbidden by p mod f alone (local arithmetic) are reported separately as
  *local*, not as p-intrinsic.
A rule passing K1–K5 is a HOT LEAD.

## 3. First result (checkpoint 1): the full witness count W(p) to 10⁸ — CERTIFIED (computation) / EVIDENCE

Engine `scripts/z69_mine_W.c` (sieve over f ≡ 7 (8), r | f + 1, n = ft − r; exhaustive since every witness has
f ≤ 2n + 1); cross-checked against the independent per-prime engine `scripts/z69_mine_allwit.c` (direct f ≤ 2√n + 8,
plus t ≤ n/F + 1 with r | n + t) on 300 random primes ≤ 10⁸: 0 mismatches; and against Z68 lists (2521: 1 witness
f = 87; 3361: 2; 14177: 9; 21841: 4 — identical to `movingr_noprime_1e9.txt`).
* All 1 439 970 primes p ≡ 1 (8) ≤ 10⁸ have W ≥ 1; odd squares ≤ 10⁸: W = 0 (all); non-square n ≡ 1 (8) ≤ 10⁸ with
  W = 0: exactly Z₇ (CERTIFIED).
* Mean W(p) ≈ 0.179 log² p, stable over 10⁴–10⁸ (EVIDENCE); standard deviation ≈ 1.85 × Poisson (W/log²p
  over-dispersed by local factors).
* **Local share of the variance (EVIDENCE):** the class of p mod M (leave-one-out class means, primes in (10⁶, 10⁸])
  explains R² = 0.049 (M = 3), 0.117 (15), 0.217 (105), 0.263 (1155), 0.299 (15015) of Var w; Poisson noise
  accounts for ≈ 1/E W ≈ 0.018 of Var w = 0.060.
* Lowest-W primes: W = 1 only at 2521 (f = 87); W = 2 at 17, 3361, 9601; lowest normalised w: 2521 (0.091),
  2 031 121 (W = 4, 0.106), 1 381 969 (4), 1 095 481 (4), 4 149 601 (5), 712 321 (4), 45 553 561 (W = 7, 0.126),
  …, 96 049 801 (W = 10, 0.165).

* Correction to the brief: 2521 = 35² + 36² (45² + 16² = 2281).

### 3.1 What the size of W(p) is made of (Q1) — EVIDENCE (descriptive fits)
Files `data/z69/mine/{local_fit,hvsE,chi_fit,tau_fit,scales_corr,types_corr,morph,redei}.txt`. Samples: (a), (b), (d)
use the 1 420 418 primes p ≡ 1 (8) in (10⁶, 10⁸]; (c) the 163 592 primes in (10⁵, 10⁷]; (e) the 1 273 994 primes in
(10⁷, 10⁸]. Fits are 2-fold cross-fitted or held-out as stated. "Noise share" = fraction of the variance a Poisson count
with the fitted mean would already produce.

(a) *Local residues.* A multiplicative model E W(p) = 0.179 log²p · ∏_q g_q(p mod q), q ∈ {16, 32, 64, 128, 9, 25, 27,
49, 121} ∪ {primes < 200}, fitted by Poisson backfitting (`z69_mine_local.py`, 2-fold cross-fit) explains
**R²(w) = 0.434** out of fold (both folds 0.433–0.434); Poisson noise share 0.308; Pearson residual variance 1.85
(Poisson = 1). Part of the over-dispersion is exact clustering: a witness with 8 | y and its reversal (z, y, x) are
both witnesses — 41.5 % of the control witnesses lie in such pairs.

(b) *Legendre symbols carry about half of the local part, through four truncated Euler sums.* On log w (held-out),
"one-hot p mod ℓ, ℓ ≤ 60" gives R² = 0.314; a free linear model in χ_p(ℓ), ℓ ≤ 200, gives 0.151; and **four numbers**
give 0.150: the truncated sums S_a(p) = Σ_{ℓ ≡ a (8), 3 ≤ ℓ ≤ 2000} χ_p(ℓ)/ℓ, a ∈ {1, 3, 5, 7} (equivalently four
truncated Euler products, *proxies* for L(1, χ_p ψ), ψ ∈ {1, χ₋₄, χ₈, χ₋₈}; no tail control, so no claim about the
actual L-values or class numbers is made). Coefficients: S₇ −0.45, S₃ −0.17, S₅ −0.11, S₁ +0.09 — inert primes
≡ 7 (8), the possible prime witnesses, matter most. Consistently, the *normalised CF period length* L/√p of √p (a rough
regulator proxy; h(p) = 1 for 77 % of both groups) has median **2.03 on H-low vs 0.76 on the controls**. Rédei 2-part
data show no difference (v₂ h(−4p) = 2/3/4/≥5: H-low 0.52/0.24/0.10/0.14, controls 0.49/0.26/0.13/0.12).

(c) *Rough small shifts.* log τ(p + c), log τ(cp + 1) (c ≤ 8; `z69_mine_tau.c`) alone give R²(log w) = **0.371**
(all coefficients positive except 5p + 1 (−0.001); largest for p + 1, p + 2, p + 3, p + 4, p + 7, 2p + 1, 4p + 1);
residues (ℓ < 100, p mod 64) 0.391; both 0.438; the plug-in Poisson/delta-method benchmark mean(1/W)/Var(log w) is 0.352
(an observed-count benchmark, not an identified component: 0.44 and 0.35 are not additive parts of a decomposition). The lowest 0.1 % in w have mean Σ log τ = 35.7 vs
39.1 overall. Hard primes look like *approximate Prop K primes* (Z68_U7O §6A.3: p ≡ 1 mod M with p + c = (c+1)·prime) —
the Dickson family along which no bounded cascade closes. (This is a regression description, not a causal claim.)

(d) *The extreme tail is not explained by these models.* For the 556 H primes in (10⁶, 10⁸] the cross-fitted local
model gives median E/μ = 0.742 (2.8th percentile) while median W/μ = 0.27: the fitted local factor accounts for ≈ 23 %
of the log-deficit (medians −0.30 of −1.30; ratio of means 0.233). Calibration of the lower tail (`hvsE.txt`): the
number of primes with P(X ≤ W) ≤ t is far above what the fitted count models predict — Poisson(E): 1 158 observed vs
11.0 expected at t = 1.1·10⁻⁵; a negative binomial with the same mean and the observed variance inflation 1.85: 63 vs
11.2 (t = 1.1·10⁻⁵), 318 vs 106 (10⁻⁴), 5 vs 0.9 (10⁻⁶). Adding the shift variables of (c) (on (10⁵, 10⁷], NB with
inflation 1.58) narrows but does not close the gap: 180 vs 122 at t = 10⁻³, 31 vs 11.3 at 10⁻⁴ (size-only model: 73 vs
11.3). So the hard tail is **heavier than "local + shifts + over-dispersed noise"**; the extra structure is not
identified here (interactions of local and shift conditions — exactly what Prop K primes have — are a natural
candidate, untested).

(e) *No compensation across scales or 2-adic types (descriptive).* Counting witness clusters (8 | y pairs once) by scale
(log f / log p ∈ [0, ¼], (¼, ½], (½, ¾], > ¾) and removing size (20 log-size bands, or log p and log²p) together with
local structure (class means mod 15015 or 240240 within size bands, or a one-hot model ℓ < 100 + p mod 64), the
four scale counts remain **positively** correlated (0.08–0.39; Var(Σ)/ΣVar = 1.42–1.45). By 2-adic pair type (0, 2, 4, 6)
the raw counts are negatively correlated (types 2 vs 4/6: −0.11, −0.14; ratio 0.92; after size-only detrending −0.13,
−0.15, ratio 0.87), but after local conditioning the correlations are |ρ| ≤ 0.06 (some weakly negative) and the ratio
is 0.96–1.05. So no strong, robust compensation across these conditioning choices is visible; an identity involving data not conditioned on
here (e.g. the tail of an L-value, a weighted count) is not excluded.

(f) *Morphology of hard witnesses* (`morph.txt`; per witness, H-low p ≥ 10⁴ vs controls): min letter ≤ 2: 9.6 % vs
26.8 %; min letter ≥ 20: 40.4 % vs 24.7 %; f prime: 24.9 % vs 19.4 % (0 % on H-np by definition); 8 | y (reversal
pair): 27.3 % vs 41.5 %; f > √p: 79 % vs 78 %. Hard primes are rescued by "big-letter" words.

## 4. The main mining question (Q2): do p's own data point to its witnesses? — EVIDENCE (non-rejection) + PROVED lemma

### 4.1 Design
Data per prime (`z69_mine_feat.py`, `lite_feats` in `z69_mine_phantom.py`; PARI): p = a² + b² (a odd); p = c² + 2d²;
p = e² − 2g² (least g); p = u² + 3v² (p ≡ 1 (3)); p = s² + 7t² ((p/7) = 1); h(−4p); n_p; nq₇ (least prime ≡ 7 (8) with
(p/q) = −1); the CF of √p; the negative-Pell unit T² − pU² = −1 (reduced mod the moduli tested; recurrence checked
against exact convergents). **Exact dictionary of the phantom tests** (`dictionary()` in `z69_mine_phantom.py`):
G1 {a, b}; G2 |αa + βb| (0 ≤ α ≤ 3, |β| ≤ 3, gcd(α, β) = 1, excluding (α, β) = (1, 0), (0, 1) and zero values;
C2, E2 likewise); G3 nine quadratic forms in (a, b); G4 six cubic/quartic Gaussian
expressions; C1, C2, E1, E2 the analogues for (c, d), (e, g); N37 (u, v), (s, t) and combinations with |coeff| ≤ 2;
CL {h(−4p), h(−4p)/4, n_p, nq₇} (h(p), h(−8p) are **not** in the phantom tests — they appear only in the descriptive
§3.1(b) and in the unconditional shuffle); CFq the **first 12 and middle 3** partial quotients, a₀ + k (|k| ≤ 3), the
period L; QS the Q_i of the **first 4 000 period positions** (truncated for 505/840 H and 973/2 520 control primes);
CFk / CFh: all convergent denominators k_i / numerators h_i of √p over the full period (counts of f | k_i, f | h_i);
CFpA: convergent denominators of p/A, A ∈ {a, b, c, d, e, g}; PELL T, U, T ± 1, U ± 1, T ± U, T ± 2U.
Relations with a witness f of p, word (x, y, z) = (r, (f+1)/r, (p+r)/f): divf f | v; divq q | v for a prime q | f,
q ≥ 5; divxy x or y (≥ 5) | v; vdivxy v | f + 1; eqxyf v ∈ {x, y, f, f + 1}; divz, vdivz, eqz the same with z.

**Estimand and controls.** For a fixed f, witness status is a function of p mod f; we ask whether *specified relation
frequencies* between p's dictionary and its sampled witnesses differ from those of **phantom primes** sharing the local
event. Sampling: every prime of the list with 10⁴ ≤ p ≤ 2·10¹⁰ (this skips 27 of the 849 H primes — 18 below 10⁴, among them
2521, 3361, 9601, and 9 above 2·10¹⁰ — and 79 of the 2 547 controls: 822 H / 2 468 controls analysed), then ≤ cap of its witnesses uniformly at random (each witness is included with probability min(W, cap)/W);
the estimators are **record-weighted** over the covered sampled witnesses (a prime contributes as many records as it has
covered sampled witnesses — up to 8 for H, 3 for controls), and the hard-set selection is part of the H estimand. Phantom samplers:
(i) **same-size f-phantoms** p′ = p + 8jf, 1 ≤ |j| ≤ p/(16f) (so |p′ − p| ≤ p/2; f stays a witness with the same
x, y). Impossible when f > p/16: those witnesses are **not covered** (coverage table below);
(ii) **(x, z)-phantoms** p′ = p + 8jxz, |p′ − p| ≤ p/2, word (x, y + 8j, z) required canonical — for z-relations
(in (i) z changes with p′, which confounds every z-relation); covers most large-f witnesses;
(iii) **profile-matched f-phantoms** p′ ≡ p mod 840f with χ_{p′}(ℓ) = χ_p(ℓ) for ℓ = 11, …, 23 — for H, whose
selection biases these symbols; these phantoms are ~10³ times larger than p (median q/p ≈ 740 (H), 1 240
(controls)), so only divf/divq (moduli fixed and ≪ dictionary values) are interpreted, the size-sensitive families
are dropped, and H is compared with the controls run through the *same* sampler (difference-in-differences).
Statistics: per test, a cluster score z = Σ_p d_p / (Σ_p d_p²)^{1/2} with d_p = Σ_{sampled witnesses of p}
(1[real hit] − mean over phantoms of 1[phantom hit]) (independent prime clusters; unreliable for very sparse keys —
the number of discordant primes is printed); a size-sensitive family is counted only in records where the real prime
and all its phantoms are below the CF/Pell cutoff (exposures printed; in the matched runs PELL is measured on 1 487 of
3 098 H and 2 101 of 4 628 control records); pooled ratios over the 11 size-robust families (G1–G4, C1, C2, E1, E2,
N37, CL, PELL) with a cluster delta-method 2-s.e. interval. Runs process primes in random order; all five runs below
completed. These are non-rejection results for the listed relations and samplers, not equivalence tests.

### 4.2 Results (`data/z69/mine/phantom_*.txt`; raw records `raw_*.jsonl.gz`)
* **Controls, same-size f-phantoms** (`phantom_same_C.txt`; 7 404 sampled witnesses of 2 468 primes p ≥ 10⁴, 4 129
  covered, from 2 229 primes; coverage by f/p: < 10⁻³ 2 271/2 271, < 10⁻² 1 295/1 327, < 1/16 563/1 244,
  ≥ 1/16 **0/2 562**). 65 f/x/y relation tests, max |z| = 2.80 (QS divxy); the 30 divf/divq/divxy tests of the
  size-robust families: max 2.56. Pooled ratios: **divf 1.005 ± 0.035, divq 1.008 ± 0.008, divxy 1.011 ± 0.016.**
  Also null: CFk divf 1 703/1 714 (f divides some convergent denominator of √p), CFpA divf 289/281.5, PELL divf
  123/139.
* **Controls, (x, z)-phantoms** (`phantom_xz_C.txt`; 4 695 of 7 404 witnesses covered, including 1 882/2 528 with
  f ≥ p/16): 35 z-relation tests, max |z| = 3.15 (CL vdivz: v | z for v ∈ {h(−4p), h/4, n_p, nq₇}); pooled divz
  1.011 ± 0.016. The apparent z-signals of the f-phantom design are therefore the confound described.
* **Hard set, same-size f-phantoms** (`phantom_same_H.txt`; 4 197 covered witnesses, 822 primes): strong deviations,
  e.g. letter-divides-coordinate G1 divxy +9.5, G3 divxy +12.6, N37 divq +14.9, CL divq +9.6, CFk divf +10.0, CFh divf
  +8.9, QS divxy +19.5, QS eqxyf +11.4, CFpA divxy +5.7; pooled divf 1.115 ± 0.063, divq 1.049 ± 0.009, divxy
  1.154 ± 0.019. Suggested reading: the H primes have a pseudo-square profile at small primes (§3.1(b)), which
  same-size phantoms do not share; a prime ℓ can divide b, d, g, v or a Q_i only if χ_p(ℓ) ∈ {0, 1} (a necessary
  condition, not an equivalence: 41 = 5² + 4², χ₄₁(5) = 1, 5 ∤ 4), so a pseudo-square p offers more such divisibilities.
  * *Resolved by profile matching* (next bullet): the size-robust families G1–G4, C, E, N37, CL, PELL.
  * *Mostly tracks period length* (`cfk_period.txt`, `scripts/z69_mine_cfk_period.py`; diagnostic uniform-residue
    model L/f, not a null model): CFk divf multiplicity 62 546 vs 38 056 (ratio 1.64) against a model ratio 1.59;
    normalised rate ratio **CFk 1.032 ± 0.025, CFh 1.027 ± 0.026** (controls 0.983 ± 0.017, 0.987 ± 0.017). The
    residual is small but not excluded; the H primes have median L/√p = 1.97 vs 0.88 for their phantoms.
  * *Unresolved:* QS divxy — normalising by the size of the Q-set leaves a normalised rate ratio **1.377 ± 0.051**
    (controls 1.025 ± 0.031); see §12 for the round-2 analysis; QS eqxyf and CFpA divxy/vdivz were not analysed further. The pseudo-square profile
    (ℓ | Q_i requires χ_p(ℓ) = 1) is a plausible explanation, not a demonstrated one; these families were dropped from
    the matched runs (size-sensitive) and remain open. Likewise the hard set's **z-relations** were not tested with
    (x, z)-phantoms (that design was run on the controls only).
* **Hard set, profile-matched** (`phantom_match_H_did.txt`; 3 098 covered witnesses of 822 primes): the size-robust
  divf/divq/divxy deviations disappear (CL divq 635/631.5, N37 divq 1 566/1 581.5, G1 divxy 626/651.5); pooled **divf
  1.041 ± 0.076, divq 1.003 ± 0.010, divxy 0.983 ± 0.016**; 30 tests, max |z| = 3.72 (N37 divxy, a *depletion*, and
  divxy is size-sensitive in this design: large letters can divide the larger phantom coordinates but not p's).
  Size robustness is *not* blanket even for divf: in 2 053 of the 3 098 H records f > 3√(2p), so every G2 value of the
  real p is smaller than f and real G2 divf is structurally impossible while the ~10³× larger phantom can hit (the
  analogous C2 bound excludes 2 104 records). The matched / DiD conclusions are conditional on exchangeability of H and
  control witnesses under the sampler (unverified: their f, letter, size and profile distributions differ).
  Matched controls (`phantom_match_C.txt`): pooled 1.006 ± 0.045, 1.002 ± 0.007, 0.998 ± 0.014; max |z| 1.92.
  **Difference-in-differences H − controls:** 30 divf/divq/divxy tests, max |z| = 2.96 (N37 divxy). The z-relations
  and v | xy differ hugely in *both* matched runs (phantoms ~10³× larger) — a design artefact, not interpreted. Caveat:
  matching covers residues mod 840 and χ at 11 … 23 only; letters with larger prime factors are not matched.
* **Unconditional size-neighbour shuffle** (`shuffle_scan.txt`; descriptive only; older test set incl. z, families
  without G4/CFpA/CFk/CFh): huge deviations, e.g. G1 divf 0 vs 954, C1 divf 0 vs 992, QS divf 0 vs 471 522,
  PELL divf 2 108 vs 4 085, G2 divf 6 007 vs 4 042, CL divf 3 884 vs 2 940 — local consequences of (p/f) = −1
  (Lemma 4.3) and of p mod f, removed by conditioning.

### 4.3 Lemma (anti-alignment of quadratic data; PROVED, elementary — the Pell T, T ± 1 cases are Z68_U7O Lemma P(ii))
Let p ≡ 1 (mod 8) be prime and f a U₇ witness of p. Then (p/f) = −1 (Jacobi; Z60 Lemma 7(ii)), and consequently f
divides **none** of: a, b (p = a² + b²); c, d (p = c² + 2d²); g (p = e² − 2g²); v, and u unless (3/f) = −1
(p = u² + 3v²); any Q_i of the CF of √p; T, U, T + 1, T − 1 of the negative Pell solution T² − pU² = −1.
*Proof.* gcd(f, p) = 1: f ≤ 2p + 1 and f ≡ 7 (8) exclude f ∈ {p, 2p}, and a common factor would be p. In each case we
derive (p/f) ∈ {0, 1} or a contradiction. If f | b, then gcd(a, f) = 1 (a common prime would divide a² + b² = p) and
p ≡ a² (mod f), so (p/f) = 1. If f | a: p ≡ b², same. If f | d: p ≡ c² (gcd(c, f) = 1 as before). If f | c:
p ≡ 2d² and (2/f) = 1 for f ≡ 7 (8). If f | g: p ≡ e². If f | v: p ≡ u². If f | u: if 3 | f then 3 | u and 3 | p,
impossible; otherwise p ≡ 3v², so (p/f) = (3/f), excluded unless (3/f) = −1. Q_i: h² − pk² = ±Q_i with gcd(h, k) = 1;
if f | Q_i then gcd(k, f) = 1 (a common prime would divide h) and p ≡ (h k⁻¹)² (mod f). Pell: if f | U then
T² ≡ −1 (mod f), impossible because (−1/f) = −1 for f ≡ 3 (mod 4) (−1 would be a square modulo every prime factor of f;
gcd(T, f) = 1 since a common prime would also divide U and hence T² − pU² = −1). If f | T then pU² ≡ 1, so gcd(U, f) = 1 and
(p/f) = 1. If f | T ∓ 1 then pU² = T² + 1 ≡ 2 (mod f), gcd(U, f) = 1 (f odd), and (p/f) = (2/f) = 1 (cf. Z68_U7O
Lemma P(ii)). ∎
*Check* (`scripts/z69_mine_lemma43_check.py`): all 136 998 witnesses of the H and control primes ≤ 2·10¹⁰ — 0 violations.
(e is *not* excluded: f | e gives p ≡ −2g², and (−2/f) = −1 is allowed.)
Reading: a modulus that divides one of the listed coordinates has Jacobi symbol (p/f) = +1 (or is impossible), whereas
a witness modulus needs (p/f) = −1 (Jacobi +1 does not mean p is a square mod f: 257 = 15² + 2·4², f = 15 | c, and
257 ≡ 2 is not a square mod 15). Hence rules of the form "take a divisor of a, b, c, d, g, v, a
Q_i, T, U or T ± 1 as the witness modulus f" can never succeed (CERTIFIED zero hit counts G1/C1/QS in the shuffle
scan). This does **not** apply to e (e.g. p = 41 = 7² − 2·2², f = 7 | e is a witness, word (1, 8, 6)), to linear or other
combinations, nor to rules that take *letters* (rather than f) from coordinate divisors.

### 4.4 Candidate rules and the kill tests
No replicated, adequately controlled enrichment was established (the H QS divxy excess is unresolved — §12), so no rule
reached the stage of a candidate built on a signal. The
natural "least non-residue" rules and the dictionary-union rule were scored (`nprule.txt`: 2 468 controls and 822 H
primes with p ≥ 10⁴; `shuffle_scan.txt`: all 2 520 controls and 840 H primes, union over its families G1–G3, C1–C2,
E1–E2, N37, CL (incl. h(p), h(−8p)), CFq, QS, PELL — not G4, CFpA, CFk, CFh):

| rule (≥ 1 witness of the stated kind) | controls | H | K4 |
|---|---|---|---|
| some witness divisible by n_p | 0.991 | 0.725 | fail |
| some witness divisible by nq₇ | 0.900 | 0.443 | fail |
| nq₇ itself is a witness | 0.750 | 0.146 | fail |
| some witness has an inert prime factor ≤ 59 | 1.000 | 0.950 | fail (a sieve menu, cf. Z68_U7O Thm A) |
| ∃ witness f dividing a dictionary value | 2 436/2 520 = 0.967 (size-neighbour shuffle: 0.996) | 485/840 = 0.577 (shuffle 0.828) | fail |

K1/K2 are vacuous for these search rules (they output only verified witnesses; W = 0 at odd squares and on Z₇); K3 was
not reached. **No HOT LEAD; no rule passes K4.**

## 5. Falsifier table (restated, final)

| screen | outcome for the material of this memo | label |
|---|---|---|
| F1 odd squares | W(m²) = 0 for all odd m² ≤ 10⁸ (census). Lemma 4.3 is a statement about witnesses of primes (it uses gcd(f, p) = 1 and (p/f) = −1). The statistics are about primes and claim nothing at squares. No mechanism was produced, so there is no "step where non-squareness enters" to exhibit. | CERTIFIED / PROVED |
| F2 numerator 8 / C-even | The 12 R₈-zero primes of `r8_zeros_1e10.txt` are all U₇-positive (re-witnessed here with `z69_mine_allwit.c` and by the cross-model review), least witnesses in file order 7, 7, 2239, 87, 1559, 143, 7, 143, 15, 7, 39, 31. No mechanism was tested against the C-even sub-line. The 38 U⁽⁸⁾-zero primes ≡ 1 (8) ≤ 10⁸ are included in H (no subgroup analysis; by definition they have no witness with 8 \| y). | CERTIFIED |
| F3 composites | Of the 285 composite (★)-zeros of `composite_zeros_le8e6.txt`, **277 are U₇-positive and exactly the 8 of Z₇ are not** (exhaustive witness lists, here and in the cross-model review); the census gives Z₇ as the only non-square zeros n ≡ 1 (8) ≤ 10⁸. Not engaged by a mechanism. | CERTIFIED |
| F4 known zeros | The 14 (★)-zero and 38 𝔊*-zero primes are all U₇-positive (re-witnessed here and by the cross-model review); separately, every prime p ≡ 1 (8) ≤ 10⁸ has W ≥ 1, minimum W = 1 only at 2521. | CERTIFIED |

## 6. Assessment: what the mining says about proof strategies
* **No detected pointing on the controls; partial on H.** Controls: 65 f/x/y tests with same-size f-phantoms and
  35 z-tests with (x, z)-phantoms show no relation beyond the local event (pooled ratios 1.005 ± 0.035 divf,
  1.008 ± 0.008 divq, 1.011 ± 0.016 divxy, 1.011 ± 0.016 divz). Hard set: the size-robust families are null under profile
  matching (1.041 ± 0.076 divf — compatible with up to ≈ 12 % enrichment —, 1.003 ± 0.010 divq, 0.983 ± 0.016 divxy) and
  in the difference-in-differences against controls (conditional on unverified exchangeability); most of the CFk/CFh
  excess tracks period length (small residuals 1.03 ± 0.03 remain); QS/CFpA deviations and H z-relations are unresolved
  (§4.2, §12). These are observed, non-replicated, sampler-specific non-rejections, and the pooled intervals are not
  limits on per-prime coverage of any rule. This is a non-rejection result: it does not prove independence, does not test untested
  families or rules, does not cover witnesses with f > p/16 in the f-phantom design, and says nothing about per-prime
  coverage of a cleverly designed rule. For each *fixed* modulus, Hecke-type equidistribution (e.g. of Gaussian primes
  in residue classes mod f) predicts that representation data add nothing to p mod f; the data are consistent with the
  same holding for the covered witnesses of the tested families. No general "blind search" conclusion follows: untested
  letter rules (Pell residues modulo candidate letters, CF positions), class-group / non-residue rules beyond the tested
  n_p menus, joint and adaptive constructions, and rare (possibly large-f) witnesses per prime are not addressed by
  pooled non-rejections. (Assessment.)
* **Hardness.** The low tail of W combines (i) a pseudo-square profile at small primes (four truncated Euler sums; long
  CF period of √p), (ii) rough small shifts (approximate Prop K primes) and (iii) a remainder that the fitted local +
  shift + over-dispersed-noise models do **not** explain (the observed tail is 2–6× heavier than calibrated). (i) and
  (ii) are what Prop K / Cor K′ (Dickson) exploit; (iii) is unidentified.
* **Not excluded by anything here:** weighted counts with built-in compensation (theta-type proxies — Z58_AUTOMORPH,
  Z58_TERNARY), relations involving several primes' data jointly, moduli drawn from non-quadratic (cubic/quartic
  residue-symbol) data of p, rules choosing letters rather than f, and any argument that does not try to *locate* a
  witness.

## 7. Verdict
**Null (non-rejection) result on the brief's target; narrowed.** Not a HOT LEAD.
* CERTIFIED: W(p) ≥ 1 for all 1 439 970 primes p ≡ 1 (8) ≤ 10⁸ (two independent engines agree on 300 random primes; the
  census was independently regenerated by the reviewer), W = 1 only at 2521; non-square zeros n ≡ 1 (8) ≤ 10⁸ = Z₇.
* PROVED: Lemma 4.3 (anti-alignment; Pell T, T ± 1 parts are Z68_U7O Lemma P(ii)); checked on 136 998 witnesses.
* EVIDENCE: mean W ≈ 0.179 log²p; local residues + small-shift divisor structure give held-out R²(log w) ≈ 0.44 on
  (10⁵, 10⁷] (plug-in Poisson benchmark 0.35; not an additive decomposition); the Legendre part is captured by four truncated Euler sums; hard primes have long CF periods and
  rough small shifts; the extreme tail is heavier than these models predict; no compensation across scales or 2-adic
  types under the stated conditioning; no detected relation between p's quadratic / Pell / CF / class-number / n_p data
  and its witnesses beyond the local event, for the tested relations and samplers (controls; on the hard set for the
  size-robust families under profile matching, CF convergents up to period length; Q-set / CFpA / z-relations open).
* Killed as candidate rules (K4): n_p / nq₇ / inert-prime-menu rules, the dictionary-divisor union rule.
* New relative to Z68: the full witness-count census and the descriptive anatomy (§3.1), the phantom-prime design and
  its outcome (§4), Lemma 4.3's non-Pell cases. Reversal pairs and 2-adic types are Z68_U7F's.

## 8. Proposed FRONTIER text (do not edit FRONTIER here)
"z69 MINE (`Z69_MINE.md`; null, narrowed). CERTIFIED: full U₇ witness counts W(p) for primes p ≡ 1 (8) ≤ 10⁸ (W ≥ 1;
minimum W(2521) = 1; mean ≈ 0.179 log²p). PROVED (elementary): a witness never divides a, b, c, d, g, v, any CF norm Q_i
of √p, or the Pell T, U, T ± 1 (it needs (p/f) = −1). EVIDENCE (non-rejection, phantom-prime design conditioning on
p mod f resp. p mod xz): no detected relation between Gaussian / norm-form / Pell / CF / class-number /
least-non-residue data of p and its witnesses beyond the local event on typical primes; on the hard set the same for the
size-robust families under profile matching, conditional on unverified exchangeability (most CF-convergent excess
tracks period length; the Q-set excess and z-relations are open — see the round-2 result in §12). Hardness =
pseudo-square profile at small primes + rough p + c, cp + 1 (approximate Prop K primes) + an unexplained heavy tail; no
compensation across scales or 2-adic types under local conditioning. These are sampler-specific non-rejections, not a
general barrier; the B2 atom is untouched."

## 9. Bottom line
On typical primes, within the tested families and samplers, witnesses show no detected trace of p's own arithmetic
beyond the local event: Fermat / norm-form coordinates and their linear, quadratic and cubic combinations, the CF of
√p, the negative-Pell unit, CF denominators of p/A, h(−4p), least non-residues — all non-rejections, pooled effect sizes
within a few per cent. On the hard set the size-robust families are likewise null under profile matching (wider
intervals), most of the CF-convergent excess tracks period length, and the Q-set / CFpA deviations and z-relations
remain unresolved (§12). The strong "relations" are local and mostly negative (Lemma 4.3: a modulus dividing one of p's
listed quadratic coordinates has Jacobi symbol (p/f) = +1, a witness modulus needs (p/f) = −1). Hardness is a pseudo-square
profile plus rough small shifts plus an unexplained heavy tail; no conservation law is visible in the raw count. Not a
HOT LEAD. Reusable output: the census, and the phantom-prime test (any future witness-rule proposal should first beat
its phantoms).

## 10. Reproduction
`scripts/z69_mine_run_all.sh` lists every command (intermediates in /tmp/z69mine; ≤ 2 concurrent compute processes;
`ulimit -v 6000000`; `timeout` ≤ 1750). Engines: `z69_mine_W.c` (census, 9 s / 1 GB at 10⁸), `z69_mine_allwit.c`
(per-prime witness lists; reads the first number of each input line), `z69_mine_scales.c` (clusters by scale / type),
`z69_mine_tau.c`. Python: `z69_mine_{sets,feat,local,hvsE,chi,tau_an,scales_an,morph,nprule,redei,lemma43_check,
phantom,phantom_an,scan,cfk_period}.py`. Committed outputs: `data/z69/mine/*.txt`, raw phantom records `raw_*.jsonl.gz`, witness
lists `{H,CTRL}_witnesses.txt.gz`, census `W_1e7.tsv.gz`, hard list `Hlow_w030_1e8.txt`.

## 11. Review log
Hostile deep-mode review (reviewer subagent; 15 findings, 0 FATAL, 10 MAJOR). Fixed: (1) universal "no information /
independence" language replaced by scoped non-rejection statements with the estimand stated (§4.1, §6–9); (2) the
same-size phantom window was not enforced (17.9 % of phantoms outside [p/2, 1.5p], large-f witnesses silently dropped)
— window enforced, coverage by f/p reported, all runs redone; (3) matched phantoms are ~10³× larger and earlier runs were
time-truncated sorted prefixes — runs redone in random order to completion, size-sensitive families dropped in matched
mode, and H compared with controls under the same sampler (difference-in-differences); (4) the tested dictionary is
listed exactly (CFq truncation, QS first 4 000 positions, CL in phantom tests lacks h(p), h(−8p), union rule's family
set); (5) the Poisson-tail calibration claim was wrong — cross-fitted model, Poisson and negative-binomial tail counts
reported; the tail is heavier than all fitted models (§3.1(d)); (6) "L-values"/"regulator" renamed to truncated Euler
sums / normalised CF period; (7) scale correlations recomputed with size detrending, conclusion restricted; (8) the
"success probability" formula replaced by the expected hit count; (9) Lemma 4.3 reading restricted (e and letter rules
not covered; example p = 41); (10) the unsupported F2 subgroup sentence removed; (11) cluster delta-method intervals
replace the naive ones, discordant counts printed; (12) numbers corrected (163 592 primes in (10⁵, 10⁷]; union
denominators 840/2 520; type correlations); (13) xz phantoms restricted to canonical words with full identity asserts;
(14) reproduction driver added, allwit reads tagged input; (15) engines abort on saturation / buffer / range violations.
Operational note: one census-type job (`z69_mine_scales.c`, < 1 min) briefly ran as a third concurrent process.
Delta review (deep; 0 FATAL, 4 MAJOR, 3 MINOR; it regenerated all phantom analyses, fits and census outputs from the
committed raw files with exact agreement). Fixed: (1) H CF/QS deviations were presented as resolved by matching —
now split into resolved by matching (size-robust families), resolved by period length (CFk/CFh, new
`z69_mine_cfk_period.py`), and unresolved (QS, CFpA, H z-relations); the p ≤ 2·10¹⁰ cutoff (9 H, 27 controls) stated;
(2) precision stated separately for controls and H (H divf compatible with ≈ 12 % enrichment); (3) the analyzer now
tracks per-key exposure (CF/Pell keys only where measurable, cutoff applied symmetrically to real and phantom primes)
and the DiD uses these exposures; (4) the estimator is described as record-weighted (the earlier 1/min(W, cap) claim was
wrong); (5) dictionary details corrected (G2/C2/E2 exclusions; k_i denominators, h_i numerators); (6) the
"coordinate divisibility ⇔ splitting" and "p is a square mod f" readings replaced by necessary-condition / Jacobi
statements with counterexamples 41 and 257; (7) type correlations labelled (raw −0.11/−0.14, ratio 0.92; size-detrended
−0.13/−0.15, 0.87).

### Cross-model review (`data/z69/xreview/REVIEW_MINE.md`, verdict ACCEPT-WITH-FIXES)
The reviewer reproduced the full census, the Z₇ list, Lemma 4.3 (independent re-derivation), the local fits, the NB tail
counts, all pooled phantom ratios and the CFk normalisation exactly; it re-witnessed the F2/F3/F4 screens. Required fixes
applied: (1) §4.4/§6–§9/FRONTIER language restricted to observed, non-replicated, sampler-specific non-rejections; no
general blind-search conclusion; CF residuals, QS, CFpA, H-z and untested letter/class-group rules explicitly left open;
(2) the analysed populations corrected (27 of 849 H excluded — 18 below 10⁴ incl. 2521, 3361, 9601, and 9 above
2·10¹⁰; 2 468 of 2 547 controls), controls described as approximately (not log-uniformly) size-matched, structural
size exclusions disclosed (2 053/3 098 matched H records with real G2 divf impossible), matched/DiD conclusions made
conditional on exchangeability; (3) "CFk/CFh explained" → "most of the multiplicity excess tracks period length", CFh
diagnostic added, normalised residual ratios 1.032 ± 0.025 / 1.027 ± 0.026 reported; (4) 0.352 labelled as a plug-in
benchmark, no additive decomposition; (5) full F2 (12 R₈ zeros with least witnesses), F3 (277/285) and F4 (14 + 38)
outcomes restored, re-checked here with `z69_mine_allwit.c`; Jacobi-vs-square shorthand fixed in §9. Its list of
open / under-powered families is taken up in §12.

## 12. Round 2 — chasing the Q-set signal; witness-free generators; H z-relations (cross-model review items 1, 2, 5)

**12.0 Pre-registration** (`data/z69/mine/round2_prereg.md`, committed in c7f02544b before any round-2 run, unchanged
since): hash split of all 849 H primes into H_train (438, incl. 2521, 9601) and H_test (411, incl. 3361, 21841, 76441,
3613009); band B = 10 000 uniformly drawn primes p ≡ 1 (8) in [5·10⁹, 5·10⁹ + 4·10⁷]; Part A (within-prime decoys),
Part B (bounded generators), Part C ((x, z)-phantoms on H); kill tests K1–K6 and two HOT-LEAD tiers (user criterion:
some generator covers ≥ 99.9 % of B and all of H_test; mechanism: K1–K6). Signal criterion for A/C: |z| ≥ 4 on H_train
and same sign with |z| ≥ 3 on H_test.

**12.1 Deviations from the pre-registration (complete list).**
| item | registered | done | consequence |
|---|---|---|---|
| Part A decoys | per-factor χ-matched primes in [q/1.5, 1.5q] | run as registered **and** an exact decoy (same 2-adic part, odd part within ±5 %, same χ_p-signature), designed on H_train + controls after the registered decoy showed a size drift, then applied to H_test | both reported |
| Part A controls | all witnesses | ≤ 20 per control prime (H: all) | control precision lower than possible |
| exact-decoy sampler | — | first version floored its window (504/523/2 306 rows outside ±5 %); rerun with exact integer bounds and uniform odd sampling (`qs4_*`); dropped letters = 600-try rejection budget exhausted (34/14 232, 47/13 527, 452/84 987) | only the corrected run is reported |
| Part B GEN-Q | "the 10 largest Q_i" | the 10 largest *distinct* Q-values (amendment; a superset) | K4 failure carries over |
| Part B decoy sampler | |log c′ − log c| ≤ 0.05, v₂ equal | registered run used floored bounds and `randint | 1` (window violations, e.g. 184 → 168); rerun with exact bounds (`gen2_*`) | both reported for K6 |
| K5 statistic | share of successes with Λ-type letter | first table gave non-Λ *coverage*; both now reported | — |
| Part C | all witnesses, ordinary + χ-matched xz | first run capped at 40 witnesses and p ≤ 2·10¹⁰ (9 H primes lost), no ordinary run; **rerun** with all witnesses, all H primes p ≥ 17 (CF/Pell families skipped above 2·10¹⁰), both variants (`ph2xz*`) | only the rerun is reported |
| power | (not registered) | an injection check was reported and is **withdrawn** (it flipped arithmetically impossible outcomes) | no power claim |

**12.2 Part A — Q-set / CFpA letters against within-prime decoys (item 1).** `z69_mine_qs2.py`, `z69_mine_qs2_an.py`;
`r2A_qs2_*` (registered decoy), `r2A_qs4_*` (exact decoy). For every prime (H: all witnesses), letters ℓ ∈ {x, y}, ℓ ≥ 5,
against the **full** CF period of √p: D = 1[ℓ | some Q_i], R = fraction of positions with ℓ | Q_i, E = 1[ℓ = some Q_i],
A = 1[ℓ | a convergent denominator of p/A]; 2 decoys per letter for the *same* p (decoys never consult D/R/E/A or the
witness set beyond the letter itself); prime-weighted means, cluster-by-prime z.
* *Registered decoy:* the signal criterion fires for D (+4.84 / +5.90), R (+8.23 / +5.88) and A (+4.28 / +4.99) (train /
  test), not E. The same design gives D +9.92 on the *controls*, and stratifying by letter size removes the H excess
  (H_train ℓ ≤ √p: ratio 1.000) — while the controls show a significant *reversal* there (ℓ ≤ √p: z = −4.58). Reading:
  the registered decoys are not size-matched (per-factor windows), and D falls steeply with ℓ; the firing is not
  interpretable as a p-specific signal, but this design cannot isolate the cause further.
* *Exact decoy (corrected sampler):* **59 % of the letters have both decoys identical to the letter** (8 367/14 198
  H_train, 7 967/13 480 H_test, 50 667/84 535 controls: small odd parts have no other admissible value with the same
  signature) and contribute no contrast; ≈ 82 % of real D-hits are of this kind. On the **informative subset** (both
  decoys differ from the letter):
  | sample | primes / letters | D real vs decoy (diff ± 2 s.e.) | z | R, E, A (z) |
  |---|---|---|---|---|
  | H_train | 419 / 4 485 | 0.1050 vs 0.1051 (−0.0001 ± 0.0028) | −0.08 | −0.89, +0.71, −0.31 |
  | H_test | 380 / 4 235 | 0.1201 vs 0.1232 (−0.0031 ± 0.0045) | −1.39 | −1.02, +0.35, +1.14 |
  | controls | 2 498 / 26 521 | 0.0547 vs 0.0542 (+0.0005 ± 0.0011) | +0.90 | +1.42, +0.66, −0.55 |
  Over all letters (identical decoys included) all four statistics are null as well (|z| ≤ 1.4).
* Reading (EVIDENCE, scoped): on the letters where the comparison is informative, the full Q-set of √p shows **no detected
  residual** beyond the χ_p-signature and size of the letter (2-s.e. half-width ≈ 3–4 % of the D base rate on H). This is
  a non-rejection on a self-matched design, not an equivalence result and not a decomposition of the round-1 phantom
  estimand (normalised QS divxy 1.377 ± 0.051); small letters (most real D-hits) are untested by construction; gcd/ratio
  relations between Q_i and letters were not tested. First-hit position (median 0.001–0.003 of the period) and
  odd-index share (0.52–0.54) coincide for real and decoy letters (descriptive, pooled over hit rows).

**12.3 Part B — pre-registered witness-free generators (items 1, 2, 5).** Engine `z69_mine_gen.c` (each candidate
c ≥ 65 tried exactly in the x-, y- and z-role; every word verified in 128-bit arithmetic; validated against brute-force
enumeration of all words for every prime p ≡ 1 (8) < 1500 and c ≤ 40: 753/753, 0 mismatches,
`scripts/z69_mine_gencheck.py`, `r2B_engine_check.txt`; input range guarded); driver `z69_mine_genrun.py`. Coverage =
fraction of primes with ≥ 1 word from the generator; corrected decoy sampler (`r2B_coverage.txt`):

| generator (cand./prime on B) | band B (10 000) real / decoy (McNemar z) | non-Λ coverage | H_train (438) | H_test (411): real / decoy (z), failures |
|---|---|---|---|---|
| G Gaussian (16) | 0.007 / 0.007 (−0.4) | 0.004 | 0.021 | 0.027 / 0.029 (−0.3), 400 |
| N other norm forms (48) | 0.022 / 0.020 (+1.3) | 0.014 | 0.100 | 0.088 / 0.073 (+0.9), 375 |
| J joint sums/differences/gcds (58) | 0.099 / 0.102 (−0.9) | 0.050 | 0.281 | 0.282 / 0.241 (+1.9), 295 |
| Q CF positions (24) | 0.039 / 0.040 (−0.6) | 0.016 | 0.027 | 0.020 / 0.034 (−1.3), 403 |
| A convergents of p/A (34) | 0.626 / 0.622 (+0.7) | 0.256 | 0.237 | 0.234 / 0.209 (+1.1), 315 |
| C class numbers (7.5) | 0.010 / 0.011 (−0.2) | 0.007 | 0.043 | 0.056 / 0.027 (+2.4), 388 |
| ALL (173) | **0.685** / 0.677 (+1.4) | 0.313 | 0.534 | **0.518** / 0.465 (+2.0), **198** |

* **K4 fails for every generator** (best 68.5 % of B; ALL leaves 198 of the 411 H_test primes uncovered). **No HOT LEAD**
  in either tier.
* K1/K2: no word on the 499 odd squares 9 … 999² nor on Z₇ (engine sanity). K3: ALL covers 16 of the 38 U⁽⁸⁾-zero primes.
  K5 (registered statistic): of the 11 456 successful (prime, candidate) pairs of ALL on B, 7 641 (66.7 %) use a Λ-type
  letter (dividing p + c′ or c′p + 1, c′ ≤ 64); non-Λ coverage 31.3 %.
* K6: **the registered run passed K6 for ALL** (McNemar b = 1 675, c = 1 504, +1.71 points, z = +3.03; GEN-A +2.92), but
  its decoy sampler violated the registered window; with the corrected sampler the same band gives z = +1.36 (b = 1 565,
  c = 1 490, +0.75 points; GEN-A +0.74). An exploratory fresh band sample (seed 7070, 6 000 primes, 143 overlapping B)
  gave ALL +1.78 (+1.87 without the overlap), GEN-A +1.79, penultimate convergent denominators k of p/A (kp ≡ ±1 mod A)
  +2.39 at 4.3 % coverage. Reading: a small positive real-minus-decoy difference (≈ 1 point of coverage) is compatible
  with all runs and is not established at 3σ under a correct sampler; it is irrelevant for K4.

**12.4 Part C — z-relations on H with (x, z)-phantoms (item 2).** Mode `xz` and `xzm` (χ_{p′}(ℓ) = χ_p(ℓ) for
ℓ ∈ {3, 5, 7, 11, 13} ∤ xz) of `z69_mine_phantom.py`, all witnesses of all H primes p ≥ 17 (`r2C_ph2*`). Coverage
(records with a phantom): xz 5 023/7 767 (train) and 4 810/7 309 (test); xzm 3 222/7 767 and 3 031/7 309 (the matching
fails when few admissible j exist — e.g. 2521, 3361 get no matched phantom; 1 253/1 710 and 945/1 710 large-f records
covered on train).
* *Ordinary xz:* the signal criterion fires for six z-relations: CL vdivz +12.9/+12.2, CL eqz +10.8/+9.4, CL divz
  +6.8/+5.3, N37 divz +8.3/+6.8, QS eqz −5.5/−5.6, QS vdivz −5.1/−5.8 (train/test).
* *χ-matched xzm:* N37 and QS vanish (|z| ≤ 1.6); CL shrinks to vdivz +3.84/+4.46 and eqz +2.81/+4.59 (criterion no
  longer met on train). Component diagnostic (`z69_mine_cl_diag.py`, `r2C_cl_diag.txt`): the remaining CL excess is
  entirely n_p and nq₇ dividing / equal to z (vdivz n_p 456 vs 439 and 378 vs 362; nq₇ 144 vs 110 and 126 vs 93;
  h(−4p) contributes ≤ 1.5 hits), and the phantoms' least non-residue is smaller than p's in 14 % of records and larger
  in 9 %. Mechanism (correct as algebra, assessment as attribution): q | z forces p′ ≡ p (mod q), hence equal χ at q;
  whether q is the *least* non-residue depends on the symbols at the unmatched primes 17 ≤ ℓ < q — the pseudo-square
  profile of the hard primes. The dose-response (6 relations at +5…+13 without matching → one component family at
  ≈ +4 with 5-prime matching) fits a local-profile explanation; it is not an independently validated causal attribution,
  and records without a matched phantom (≈ 58 %) are not covered. In the xz designs divf/divq compare different moduli
  (f′ ≠ f) and are not interpreted.

**12.5 Kill-test summary (round 2).** K1 ✓, K2 ✓, K3 16/38, **K4 ✗ (all generators)**, K5 66.7 % of successes Λ-type,
K6 ✓ in the registered run for ALL (+3.03) / ✗ with the corrected sampler (+1.36). Signal criterion fired in two
experiment families: Part A (registered decoy: D, R, A) and Part C (ordinary xz: six relations; matched: CL vdivz on
test only).

**12.6 Verdict of round 2.** **No HOT LEAD**: no tested generator meets K4 (best 68.5 % on a disjoint band; 198 H_test
failures). Exact within-prime comparisons show no detected residual in the reported Q-set / CFpA statistics on the
informative letters, but they are heavily self-matched (59 % of letters) and establish neither equivalence nor power.
The covered CL z-relation excess on H is concentrated in the least-non-residue components and is consistent with the
unmatched local profile. Broader resolution is not established — still open: small letters against the Q-set, gcd/ratio
relations, Pell residues modulo candidate letters, class-group structure beyond h, generators of unbounded complexity
or adaptive coefficient search, and the uncovered (unmatchable) records. ES is OPEN.

**Round-2 hostile review** (deep reviewer subagent on §12 as first drafted; 0 FATAL, 5 MAJOR, 5 MINOR; it verified the
hash split, regenerated the committed analyses, re-checked every stored phantom and generator word and the engine
enumeration (753/753 plus 4 533 further candidate-role cases)). Fixed: (1) the injection "power" check flipped
arithmetically impossible outcomes — withdrawn; (2) the exact decoys are self-matched for 59 % of letters — identity
rates and an informative-subset analysis added, "fully accounted for / knows no more" replaced by scoped non-rejection;
(3) undisclosed departures from the pre-registration — complete deviation table (§12.1), Part C rerun with all
witnesses, all H primes, ordinary and matched variants; (4) K6 goalposts — the registered run's pass for ALL (+3.03) is
reported as such, with the corrected-sampler (+1.36) and follow-up (+1.78, 143 overlapping primes) results; (5) the
reproduction driver covers every round-2 output; the engine validation script and the registered-run raw records are
committed; (6) both decoy samplers now use exact integer windows and uniform odd sampling (all affected runs redone);
(7) GEN-Q amendment stated; (8) K5 reported as the registered successful-letter share; (9) denominators, the list of
statistics that fired, and descriptive labels corrected; the "one anomaly left" phrasing removed; (10) engine input and
subprocess-status guards added.
