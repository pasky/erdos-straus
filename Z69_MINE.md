# Z69_MINE — what do the hard primes' U₇ witnesses know? (data-mining lane, wave z69)

**ES is OPEN. Nothing here proves or disproves it.** Status: final draft (verdict §7: **null result, precise; narrowed**;
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
**Controls:** random primes p ≡ 1 (8) matched in size (log-uniform in the same ranges); same-p shuffled controls
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

### 3.1 What the size of W(p) is made of (Q1) — EVIDENCE
All statements are held-out fits (half of the primes fit, the other half scored) on the 1 420 418 primes
p ≡ 1 (8) in (10⁶, 10⁸] (resp. the 165 811 in (10⁵, 10⁷] for 3.1(c)); "noise share" = the fraction of the variance that
a Poisson count with the fitted mean would already produce. Files `data/z69/mine/{local_fit,chi_fit,tau_fit,hvsE}.txt`.

(a) *Local residues.* A multiplicative model E W(p) = 0.179 log²p · ∏_q g_q(p mod q) over q ∈ {16, 32, 64, 128, 9, 25,
27, 49, 121} ∪ {primes < 200} (`z69_mine_local.py`) explains **R²(w) = 0.434**; the Poisson floor is 0.308; Pearson
residuals have variance 1.85 (Poisson = 1). Part of the over-dispersion is exact clustering: a witness with 8 | y and its
reversal (z, y, x) are both witnesses — 41.5 % of all witnesses of the controls are in such pairs (`z69_mine_scales.c`
counts clusters).

(b) *Legendre symbols alone capture half of the local part, and they are four L-values.* On log w, the model
"one-hot p mod ℓ, ℓ ≤ 60" gives R² = 0.314, a free linear model in the symbols χ_p(ℓ) (ℓ ≤ 200) only 0.151, and the
same 0.150 is reached by **four numbers**, the Euler sums S_a(p) = Σ_{ℓ ≡ a (8), ℓ ≤ 2000} χ_p(ℓ)/ℓ, a ∈ {1, 3, 5, 7}
— equivalently the four twisted values log L(1, χ_p ψ), ψ ∈ {1, χ₋₄, χ₈, χ₋₈}, i.e. the class number × regulator data of
ℚ(√p), ℚ(√−p), ℚ(√2p), ℚ(√−2p). Fitted coefficients: S₇ −0.45, S₃ −0.17, S₅ −0.11, S₁ +0.09 (inert primes ≡ 7 (8)
matter most — they are the possible prime witnesses). Consistently, the CF period of √p (∝ regulator, h(p) = 1 for
77 % in both groups) has median L/√p = **2.03 on H-low vs 0.76 on the controls** (`redei.txt`): hard primes have large
regulators. The Rédei 2-part data (v₂ h(−4p), v₂ h(−8p)) show no difference (H-low 0.52/0.24/0.10/0.14 for v₂ = 2/3/4/≥5,
controls 0.49/0.26/0.13/0.12).

(c) *Rough small shifts.* log τ(p + c), log τ(cp + 1) (c ≤ 8; `z69_mine_tau.c`) alone give R²(log w) = **0.371**
(all coefficients positive except 5p + 1 (−0.001); largest for p + 1, p + 2, p + 3, p + 4, p + 7, 2p + 1, 4p + 1), the residue model (ℓ < 100, p mod 64) 0.391,
both together 0.438; noise share 0.352. The lowest 0.1 % in w have Σ log τ = 35.7 vs 39.1 on average. So hard primes are
*approximate Prop K primes* (Z68_U7O §6A.3: p ≡ 1 mod M and p + c = (c+1)·prime) — exactly the Dickson family along which
no bounded cascade closes.

(d) *The extreme tail is mostly fluctuation.* For the 556 hard primes in (10⁶, 10⁸] the local model of (a) predicts
E/μ with median 0.74 (2.8th percentile among all primes) while the observed W/μ has median 0.27: the local factor
accounts for only ≈ 23 % of the log-deficit (medians −0.30 of −1.30; ratio of means 0.23); the Poisson probability P(X ≤ W | E) has median 1.1·10⁻⁵
over H — consistent with H being the extreme tail of 1.4·10⁶ draws (`hvsE.txt`).

(e) *No compensation (no conservation law).* Counting witness clusters (8 | y pairs once) by scale
(log f / log p ∈ [0, ¼], (¼, ½], (½, ¾], > ¾) and removing the local structure (class means mod 15015 or 240240, or a
one-hot model ℓ < 100 + p mod 64), the four scale counts are **positively** correlated (0.13–0.41; Var(Σ)/ΣVar = 1.53;
`scales_corr.txt`). By 2-adic pair type (0, 2, 4, 6) the raw counts are negatively correlated (−0.11, −0.14 between
types 2 and 4/6; Var ratio 0.92), but this is entirely local: after conditioning on p mod 15015 the correlations are
|ρ| ≤ 0.05 and the ratio is 1.04 (`types_corr.txt`). A Siegel-mass-type identity (a weighted total of witnesses
fixed by local data and an L-value, with classes compensating each other) would show negative residual correlation
and residual variance below the noise floor; neither is seen. (EVIDENCE about the raw count W and these partitions
only; it does not exclude a cleverly weighted count.)

(f) *Morphology of hard witnesses* (`morph.txt`; per witness, H-low p ≥ 10⁴ vs size-matched controls): min letter ≤ 2:
9.6 % vs 26.8 %; min letter ≥ 20: 40.4 % vs 24.7 %; f prime: 24.9 % vs 19.4 % (0 % on H-np by definition); 8 | y (reversal
pair): 27.3 % vs 41.5 %; f > √p: 79 % vs 78 %. Hard primes are rescued by "big-letter" words, not by special shapes.

## 4. The main mining question (Q2): do p's own data point to its witnesses? — EVIDENCE (null) + PROVED (lemma)

### 4.1 Design
Data per prime (`z69_mine_feat.py`, PARI): Gaussian p = a² + b² (a odd); p = c² + 2d²; p = e² − 2g² (least g); p = u² + 3v²
(p ≡ 1 (3)); p = s² + 7t² ((p/7) = 1); h(−4p), h(−8p), h(p); least non-residue n_p; least inert prime nq₇ ≡ 7 (8);
the CF of √p (a₀, period L, partial quotients, the set of all Q_i of the period — norms of the reduced principal
ideals —, all convergents (h_i, k_i)); the negative-Pell unit T² − pU² = −1 (reduced mod the moduli tested; exact
recurrence, checked against big-integer computation); the convergent denominators of p/A for A ∈ {a, b, c, d, e, g}
(the "CF/HJ words of p/A"). Families (`z69_mine_phantom.py`): G1 {a, b}; G2 |αa + βb| (|α|, |β| ≤ 3); G3 nine quadratic
forms in (a, b) (ab, a² − b², a² ± 2b², 2a² ± b², …); G4 six cubic/quartic Gaussian expressions (Re/Im of (a+bi)³,
(a+bi)⁴, a³ ± b³); C1, C2, E1, E2 analogous for (c, d), (e, g); N37 (u, v), (s, t) and their combinations; CL class
numbers, h/4, n_p, nq₇; CFq partial quotients, a₀ + k, L; QS the Q_i; CFk/CFh all convergents k_i / h_i of √p over a
period; CFpA convergent denominators of p/A; PELL T, U, T ± 1, U ± 1, T ± U, T ± 2U.
Relations with a witness f of p, word (x, y, z) = (r, (f+1)/r, (p+r)/f): **divf** f | v; **divq** q | v for a prime
q | f, q ≥ 5; **divxy** x or y (≥ 5) | v; **vdivxy** v | xy = f + 1; **eqxyf** v ∈ {x, y, f, f + 1}; and the z-relations
**divz**, **vdivz**, **eqz**.

**Null hypothesis and controls.** Whether f is a witness depends only on p mod f. The right null is therefore
*conditional*: given p mod f, p's global data carry no further information about f. Test: for each witness f of p
draw **phantom primes** p′ = p + kf (8 | k) — f is then a witness of p′ with the same (x, y) — and compare the
relation hits of p's dictionary with those of p′'s. Variants: (i) same size (|kf| ≤ p/2), for the controls; (ii)
*profile-matched* (p′ ≡ p mod 840 f and χ_{p′}(ℓ) = χ_p(ℓ) for ℓ = 11, …, 23), for H, whose selection biases these
symbols; (iii) **(x, z)-phantoms** p′ = p + kxz (word (x, y + k, z)), for the z-relations (in (i)/(ii) z changes with
p′, which confounds every z-relation). z-scores are clustered by prime (per-prime differences of witness indicators).
An unconditional size-neighbour shuffle (`z69_mine_scan.py`) is reported only to show what the conditioning removes.
Samples: controls 2 407–2 466 primes (≤ 3 witnesses each, 2 phantoms per witness); H 491–822 primes (≤ 8 witnesses
each); p ≥ 10⁴; primes > 2·10¹⁰ (9 Dickson primes) skipped. The profile-matched runs hit the 1 750 s time limit and are
partial (H: 491 primes / 3 559 witnesses; controls: 1 837 / 5 211) — stated in the file headers.

### 4.2 Results (`data/z69/mine/phantom_*.txt`, `shuffle_scan.txt`)
* **Controls, same-size f-phantoms (`phantom_ph2_C.txt`): every f/x/y relation of every family is null** — 66 tests,
  all |z| < 2.5 (largest: CL vdivxy −2.49, CL divf +1.78, G2 vdivxy +1.76). Examples (real / phantom hits): G2 divf
  404 / 394, G4 divf 409 / 414, C2 divf 351 / 361, E2 divf 198 / 179, N37 divf 115 / 115.5, PELL divf 156 / 142.5,
  CFk divf 99 566 / 101 454 (f divides some convergent denominator k_i of √p), CFpA divf 537 / 517.5. The tests
  have power: a 15 % excess in G2 divf would be ≈ 3σ; any *rule* would need an excess of an order of magnitude.
* **Controls, (x, z)-phantoms (`phantom_phxz_C.txt`): every z-relation is null** (35 tests, |z| ≤ 2.45). The
  apparent z-signals of the same-size f-phantom run (e.g. CFq eqz +8.8, CFpA divz −6.1) are therefore the confound
  described above.
* **Hard set, profile-matched f-phantoms (`phantom_phm2_H.txt`): every divf / divq / divxy test of the size-robust
  families (G1–G4, C1–C2, E1–E2, N37, CL, CFq, PELL) is null** (33 tests, |z| ≤ 2.66, E1 divxy; the matched control
  run gives max 2.60). The size-dependent
  families (QS, CFk, CFh, CFpA, and v | xy for small v) differ because matched phantoms are much larger than p (their CF
  periods are longer, their dictionary values larger); this is a size artefact, visible equally in the matched control
  run (`phantom_phm2_C.txt`), not a p-signal. Without profile matching (`phantom_ph_H.txt`) H shows large *letter*
  signals (e.g. G1 "letter | a or b" +9.9, QS +18): the hard primes have smooth representation coordinates (b, d, g,
  v divisible by many small primes ⇔ χ_p(ℓ) = +1 for those ℓ), i.e. the local profile of 3.1(b) seen through the
  coordinates. They disappear under matching.
* **What the unconditional shuffle shows** (`shuffle_scan.txt`, all witnesses, 840 H + 2 520 controls): huge
  deviations, e.g. G1 divf 0 vs 954, C1 divf 0 vs 992, QS divf 0 vs 471 522, PELL divf 2 108 vs 4 085, G2 divf
  6 007 vs 4 042 (z ≈ +31), CL divf 3 884 vs 2 940. All of them are local consequences of (p/f) = −1 (Lemma 4.3) and
  of the conditional distribution of the representation mod f; they vanish when conditioning on p mod f.

### 4.3 Lemma (anti-alignment of quadratic data; PROVED, elementary)
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
Reading: the moduli that p's quadratic data produce "naturally" are moduli at which p is a square; witnesses need a
modulus at which p is not. This is why every representation-coordinate rule of the form "take a divisor of a
coordinate" is dead on arrival (CERTIFIED zero hit counts G1/C1/QS above), and why the surviving relations
(f | αa + βb, f | T + U, …) can only "know" p mod f.

### 4.4 Candidate rules and the kill tests
No relation family showed p-specific enrichment, so no rule reached the stage of a candidate built on a signal.
For completeness the natural "least non-residue" rules and the dictionary-union rule were scored (`nprule.txt`,
`shuffle_scan.txt`; fraction of primes with at least one witness of the stated kind):

| rule | controls (2 468) | H (822) | K4 | comment |
|---|---|---|---|---|
| some witness divisible by n_p | 0.991 | 0.725 | fail | n_p = 3 for half of all primes |
| some witness divisible by nq₇ | 0.900 | 0.443 | fail | |
| nq₇ itself is a witness | 0.750 | 0.146 | fail | |
| some witness has an inert prime factor ≤ 59 | 1.000 | 0.950 | fail | a sieve menu (Z68_U7O Thm A) |
| ∃ witness f dividing some dictionary value (all families) | 0.967 (shuffled: 0.996) | 0.577 (shuffled: 0.828) | fail | real < shuffled: Lemma 4.3 depletion |

K1/K2 are vacuous for these (they only output verified witnesses, and W = 0 at odd squares and Z₇); K3 was not reached.
**Verdict on Q2: no HOT LEAD; no rule passes K4.**

## 5. Falsifier table (restated, final)

| screen | outcome for the material of this memo | label |
|---|---|---|
| F1 odd squares | W(m²) = 0 for all odd m² ≤ 10⁸ (census). Lemma 4.3 uses primality of p only through gcd(f, p) = 1 and the Jacobi law (p/f) = −1, which also holds for odd squares *vacuously* (they have no witness). The statistical results are about primes and claim nothing at squares. No mechanism was produced, so there is no "step where non-squareness enters" to exhibit. | CERTIFIED / PROVED |
| F2 numerator 8 / C-even | Not engaged by a mechanism. The H set contains the 38 U⁽⁸⁾-zero primes ≡ 1 (8) ≤ 10⁸ and they behave like the rest of H in every statistic; the 2-adic-type partition shows no compensation after local conditioning (3.1(e)). | EVIDENCE |
| F3 composites | Census: the only non-square composite zeros n ≡ 1 (8) ≤ 10⁸ are Z₇. Not engaged by a mechanism. | CERTIFIED |
| F4 known zeros | All primes p ≡ 1 (8) ≤ 10⁸ have W ≥ 1; minimum W = 1 at 2521 only. | CERTIFIED |

## 6. Assessment: what the mining says about proof strategies
* **"Read the witness off p's arithmetic" is empirically a blind search.** Conditional on p mod f (resp. p mod xz) no
  representation, Pell, CF, class-number or least-non-residue datum of p carries detectable information about its
  witnesses (101 relation tests on the controls — 66 f/x/y tests with f-phantoms, 35 z-tests with (x, z)-phantoms, max |z| = 2.49 —
  and 33 size-robust tests on H with profile-matched phantoms, max |z| = 2.66; all consistent with the null). For each *fixed* modulus this is what
  Hecke equidistribution predicts (e.g. Gaussian primes with a given norm class mod f are equidistributed over the
  conic a² + b² ≡ p mod f); the data say the same holds for the actual witnesses, of all sizes up to 2p, where no
  theorem applies. So a p-intrinsic rule succeeds only as often as a blind search through as many candidate moduli —
  its success probability at p is Σ_{candidates f} P(p mod f ∈ T_f) — and producing ≍ log²p candidates with
  P ≍ τ(f+1)/f each is exactly the counting problem B2 already is. (Assessment.)
* **Hardness is local + sieve + luck.** The low tail of W is (i) a pseudo-square profile at small primes (four L(1)
  values / a large regulator of ℚ(√p)), (ii) rough small shifts (approximate Prop K primes), and (iii) mainly a
  fluctuation at large f with no compensation between scales or 2-adic types. (i) and (ii) are exactly what Prop K /
  Cor K′ (Dickson) exploit; (iii) is the B2 atom.
* **Not excluded by anything here:** weighted counts with built-in compensation (theta-type proxies — the subject of
  Z58_AUTOMORPH/TERNARY), relations involving several primes' data jointly, rules drawing moduli from non-quadratic
  (e.g. cubic or quartic residue-symbol) data of p, and any argument that does not try to *locate* a witness.

## 7. Verdict
**Null result (precise) on the brief's target; narrowed.** Not a HOT LEAD.
* CERTIFIED: W(p) ≥ 1 for all 1 439 970 primes p ≡ 1 (8) ≤ 10⁸ (two independent engines agree on 300 random primes),
  W = 1 only at 2521; non-square zeros n ≡ 1 (8) ≤ 10⁸ = Z₇.
* PROVED: Lemma 4.3 (anti-alignment).
* EVIDENCE: mean W ≈ 0.179 log²p; local + small-shift structure explains ≈ 0.44 of Var(log w) against a noise floor
  ≈ 0.35; the Legendre part is four L(1)-values; hard primes have large regulators and rough small shifts; the extreme
  tail is dominated by fluctuation; no compensation across scales/types; **conditional on p mod f (or mod xz), no
  p-intrinsic datum predicts witnesses** (controls: all f/x/y/z relation tests null; H: all size-robust tests null under
  profile matching).
* Killed (as candidate rules, by K4): n_p / nq₇ / inert-prime-menu rules, dictionary-divisor rules.

## 8. Proposed FRONTIER text (do not edit FRONTIER here)
"z69 MINE (`Z69_MINE.md`; null, narrowed). CERTIFIED: full U₇ witness counts W(p) to 10⁸ (W ≥ 1, minimum W(2521) = 1;
mean ≈ 0.179 log²p). PROVED: a witness never divides a, b, c, d, g, v, any CF norm Q_i of √p, or the Pell T, U, T ± 1
(it needs (p/f) = −1). EVIDENCE: conditional on p mod f, Gaussian / norm-form / Pell / CF / class-number / n_p data
carry no information about U₇ witnesses (phantom-prime tests, all null; profile-matched on the hard set). Hardness =
pseudo-square profile at small primes (captured by four twisted L(1, χ_p ψ), large regulator) + rough p + c, cp + 1
(approximate Prop K primes) + large-f fluctuation; no compensation across scales or 2-adic types (no mass-formula
structure in the raw count). Consequence (Assessment): p-intrinsic witness rules are blind searches; the B2 atom is
untouched."

## 9. Bottom line
The hard primes' witnesses know nothing about the hard primes beyond p mod f. Every p-intrinsic datum we could build
(≈ 15 families: Fermat/norm-form coordinates and their linear, quadratic, cubic combinations, the whole CF of √p, the
negative-Pell unit, CF words of p/A, class numbers, least non-residues) is, conditionally on the local event, independent
of the witness set; the only strong "relations" are local and mostly *negative* (Lemma 4.3: p's quadratic data produce
moduli where p is a square, while witnesses need moduli where it is not). Hardness itself is explained by local
pseudo-squareness, rough small shifts and plain fluctuation, with no hidden conservation law. Not a HOT LEAD; the
useful output is a calibrated null (phantom-prime design, reusable for future rule proposals: any proposed rule should
first beat its phantom) and the precise anatomy of the hard tail.

## 10. Reproduction
* `gcc -O2 -o W scripts/z69_mine_W.c -lm && ./W 100000000 100000000` (9 s, 1 GB): census; `scripts/z69_mine_allwit.c`
  per-prime witness lists (stdin primes).
* `uv run --with sympy python scripts/z69_mine_sets.py` (H, CTRL); `allwit < H.txt|CTRL.txt` →
  `data/z69/mine/{H,CTRL}_witnesses.txt.gz`; `uv run --with cypari2 python scripts/z69_mine_feat.py <list> <out>`.
* Phantoms: `uv run --with numpy --with sympy --with cypari2 python scripts/z69_mine_phantom.py <wit> <cap> 2 <seed> <out>
  [match|xz]`, analysis `scripts/z69_mine_phantom_an.py`. Shuffle: `scripts/z69_mine_scan.py`.
* Q1: `scripts/z69_mine_local.py`, `z69_mine_chi.py`, `z69_mine_hvsE.py`, `z69_mine_tau.c` + `z69_mine_tau_an.py`,
  `z69_mine_scales.c` (mode 0 scales / 1 types) + `z69_mine_scales_an.py`, `z69_mine_morph.py`, `z69_mine_nprule.py`,
  `z69_mine_redei.py`. Intermediate files live in /tmp/z69mine (census tables regenerate in seconds).

## 11. Review log
(pending hostile review)
