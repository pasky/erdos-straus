# Z69_MINE — what do the hard primes' U₇ witnesses know? (data-mining lane, wave z69)

**ES is OPEN. Nothing here proves or disproves it.** Status: CHECKPOINT 1 (skeleton; sections marked TODO are filled
in later commits).

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

## 4. Mining (TODO)
## 5. Verdict (TODO)
