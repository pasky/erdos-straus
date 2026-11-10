# Z70_LOOSE — the untested ideation leftovers (I6, I5, IDEAA #10, MINE Pell-letter residues, I9)

**ES is OPEN.** This memo proves or computes nothing that settles ES. Labels: PROVED / CONDITIONAL / CERTIFIED /
EVIDENCE / CONJECTURE / Assessment. Internal review only. Scripts `scripts/z70_loose_*`, data `data/z70/loose/`.
Status: **checkpoint 1** (statements + pre-registered kill tests; no result yet).

Notation. (★) / R(n) as in `z52bbriefs/z58_lanes.md`. Fibre form: R(n) = Σ_{d ≥ 1} r_d(4dn + 1),
r_d(N) := #{A | N : A ≡ −1 (mod 4d)} (A = 4ad − 1, B = 4bd − 1, AB = 4dn + 1 ⟺ 4abd − a − b = n).
Words: T_n = {(x, y, z) ∈ ℕ³ : xyz − x − z = n}; certificate words C_n ⊂ T_n as in `Z69_TWIST.md` Remark C.
Type I (IDEAB R2/R4): 4abd = pe + 1, ce = a + b; K3 form p ≡ −f (mod 4ad), f | 4a²d + 1.

## 0. Mandatory falsifier table (checkpoint-1 version; restated at the end)
| item | F1 odd squares | F2 C-even / R₈ | F3 composites | F4 known zeros |
|---|---|---|---|---|
| I6 (fibre laws, level sum) | the fibre coefficient r_d(4dm² + 1) = 0 for 4 ∣ 4d (T1); a transformation law is a statement about the whole generating function and is coefficient-blind — it cannot by itself use primality; must be checked that the law holds identically at squares (it will) | n/a (the law is per fibre; C-even = d even fibres) | same as F1 | same as F1 |
| I5 (involution on T_p) | |T₉| = 11 odd, C₉ = ∅ ⟹ any involution family with certificate fixed points must fail at 9 (and at 105) | the swap-even sub-counts are even at primes; a map whose fixed points are C-even certificates would prove R₈-positivity — false at the 12 R₈ zeros; record which certificate type the fixed points have | 105: |T₁₀₅| = 11, C₁₀₅ = ∅ | none needed at primes (C_p ≠ ∅ at every tested prime) |
| #10 (Type I, d-rule) | Lemma T10: Type I at n = m² needs (d/m²) = −1, impossible: every rule fails at squares, by the Jacobi step (uses non-squareness exactly there) | n/a (Type I is outside (★)); reported: rule coverage on the 12 R₈ zeros | Type I at composites not tested (rule defined via p's quadratic data) | coverage on the 14 (★)-zeros, 38 𝔊*-zeros, 231 noprime primes reported |
| Pell letters | statistics on witnesses only; no witness at squares | n/a | n/a | H sets = hard primes |
| I9 | in a primitive m² = X² + 840Y², every q ∣ X has (840/q) = +1 ⟹ Q = 0 (classifier silent) | Q computed on the 𝔐-members of the R₈ zeros | n/a | hard sets are the test population |

## 1. Precise statements and pre-registered kill tests (fixed before any computation of this lane)

### 1.1 I6 — completion / transformation law of the fibre generating functions
Φ_d(z) := Σ_{A, B ≥ 1, A ≡ B ≡ −1 (4d)} e(ABz) = Σ_{N ≡ 1 (4d)} r_d(N) e(Nz) (Im z > 0), and
G(z) := Σ_n R(n) e(nz) = Σ_d e(−z/4d) Φ_d(z/4d).
**Target statements.** (S1) an explicit identity relating Φ_d(z) and dual series at −1/(16d²z) with explicit
boundary (residue) terms and an explicit period function, for d = 1 and d = 3, proved and numerically verified;
(S2) the nature of the period function: is it a mock period (Eichler integral of a weight-1 modular shadow), i.e. is
Φ_d the holomorphic part of a harmonic Maass form with modular shadow?; (S3) does Σ_d produce a law for G?
**Kill tests (pre-registered).**
* K6a (correctness): the derived law must reproduce Φ_1, Φ_3 at ≥ 5 points z (incl. |z| small, Re z ≠ 0) to relative
  error < 10⁻¹⁵ (mpmath, 30 digits); failure = derivation wrong (fix, not a result).
* K6b (mock?): compute the discontinuity of the period function across its cut. If it is (up to elementary
  log-terms) a weight-1 modular form → fibre mock-modular (positive outcome, pursue). If it is a non-modular
  q-series (dual partial Lambert series) → "no harmonic completion with modular shadow" for that piece (scoped).
* K6c (level sum): compute the leading singular coefficients κ(r) of G at rationals r (G(r + iy) ~ κ(r) y⁻¹log²(1/y)
  · const). If there are r₁, r₂ in the same Γ(N)-orbit for every N with κ(r₁) ≠ 0 = κ(r₂), then G satisfies no
  quantum-modular law of any real weight and unitary multiplier on any finite-index subgroup (with period functions
  o(y⁻¹log²) at rationals) — the kill. Numerical cross-check of κ at a few r.
* Squares: verify r_1(4m² + 1) = r_3(12m² + 1) = 0 and that the law holds at those coefficients (no special
  behaviour).

### 1.2 I5 — a fixed-p non-affine cross-slice involution on T_p
**Statement.** Find σ_p : T_p → T_p, an involution, σ ≠ swap (x, y, z) ↦ (z, y, x), changing y on some word
("cross-slice"), not affine in (x, y, z), with Fix(σ_p) ⊆ C_p. (Then |T_p| odd ⟹ C_p ≠ ∅ ⟹ ES(p).)
**Kill test (pre-registered).** Stage 1: on complete T₇₃ and T₄₀₉ (and T₉, T₁₀₅ as controls) every candidate must be
a well-defined involution with all fixed points in C_p at both primes; failing candidates are dead as stated. Stage 2
(only for survivors): all primes p ≡ 1 (4) ≤ 10⁴, and it must fail (be undefined, or have a non-certificate fixed
point) at 9 and 105. Candidate list (fixed now): (σ1) the SL₂ "coset swap with unipotent correction":
γ_w = [[xy − 1, n], [y, zy − 1]] ↦ the unique word in the coset-transposed double coset nearest in a fixed norm;
(σ2) x ↔ y partial exchange (x, y, z) ↦ (y, x, (n + y)/(xy − 1)) completed by the swap where undefined;
(σ3) continuant-flip maps from the HJ continuant n = K(x, y, z) = xyz − x − z (length-3 ↔ length-3 via the identity
K(x, y, z) = K(x − 1, 1, y − 1, z)-type relations, followed by re-contraction); (σ4) any further map found during
the lane, listed in §3 before it is run on T₇₃/T₄₀₉. A candidate passing stage 1 and 2 = HOT LEAD (announce).

### 1.3 IDEAA #10 — Type I with an explicit nonlinear d-selection rule
**Statement.** A rule p ↦ d(p) (computed from p's own data, never from solutions; d non-square; (d/p) = −1
necessary by Lemma T10) such that the Type I slice at d(p) is non-empty for every prime p ≡ 1 (24).
Slice test: ∃ a ≤ A, f | 4a²d + 1, f ≡ −p (mod 4ad) (then c = (p + f)/4ad, e = (4a²d + 1)/f, b = (pe + 1)/4ad give a
Type I solution; A = 2000 fixed; coverage is a lower bound for the full slice — this truncation is part of the
rule). Rules (fixed now): R-np d = n_p (least prime non-residue); R-q3 d = least prime q ≡ 3 (4) with (q/p) = −1;
R-G Gaussian: p = a₀² + b₀² (a₀ odd), first of a₀, b₀/2^{v₂(b₀)}, a₀ + b₀, |a₀ − b₀|, a₀ + 2b₀, 2a₀ + b₀ that is
non-square with (·/p) = −1; R-CF first partial quotient a_i (i ≥ 1) of the CF of √p that is non-square with
(a_i/p) = −1 (if any in the first period); R-sm d = least non-square d with (d/p) = −1 (= least d ∈ {n_p, ...},
also composite d). Matched decoy for each rule: a uniformly random non-square d′ with (d′/p) = −1 and
|d′ − d| ≤ max(2, 0.1 d) (d′ ≠ d when possible).
**Kill tests.** K10a: coverage < 99.9 % on primes p ≡ 1 (24) ≤ 10⁸ ⟹ not a forcing rule. K10b: any failure on the
14 (★)-zeros / 38 𝔊*-zeros / 231 noprime primes / 12 R₈ zeros ⟹ dead. K10c (information): rule coverage not
above the matched decoy by ≥ 3σ (McNemar) ⟹ the rule's choice of d carries no information beyond its size and
(d/p) = −1. Fixture: the engine must find (p, a, d) = (1033, 1, 132).

### 1.4 MINE open item — Pell residues modulo candidate letters
**Statement.** For witnesses (U₇ words (x, y, z) of p, from `data/z69/mine/{H,CTRL}_witnesses.txt.gz`), letters
ℓ ∈ {x, y, z}, ℓ ≥ 5, and the negative-Pell solution T² − pU² = −1: is the event
D(ℓ) = [ℓ | v for some v ∈ V], V = {T, U} ∪ {T + cU + s : 1 ≤ |c| ≤ 3, |s| ≤ 2} ∪ {T + s : 1 ≤ |s| ≤ 2},
enriched relative to (i) the **exact local null** — (T, U) mod ℓ uniform on the conic T² − pU² ≡ −1 (mod ℓ) (exact
probability per letter, no sampling) — and (ii) exact decoy letters of the same p (MINE round-2 sampler: same 2-adic
part, odd part within ±5 %, same χ_p-signature), both on H_train / H_test / controls?
**Kill test / signal criterion (MINE round 2, unchanged):** |z| ≥ 4 on H_train and same sign |z| ≥ 3 on H_test;
otherwise non-rejection. Letters ℓ ≤ 2·10⁵ (exact null computable); p ≤ 2·10¹⁰ (Pell mod ℓ via the CF of √p).

### 1.5 I9 — X-coordinate classifier, rerun with disjoint factor-two controls and a q-to-word construction
**Statement.** p ∈ 𝔐 classes, p = X² + 840Y² (primitive); Q(p) = [∃ prime q | X, (840/q) = −1]. Is Q(p) more or
less frequent on hard primes than on controls? Does such a q build words?
**Design (pre-registered).** Hard sets as in `Z69_TWIST.md` I9 (𝔐-members of: 14 (★)-zeros, 38 𝔊*-zeros, 231 noprime
primes, U⁽⁸⁾-zeros ≤ 10⁸). Controls: for each hard prime, 20 primes p′ ≡ p (mod 840) drawn uniformly at random from
[p/2, 2p], excluding all hard-list members, **without replacement across the whole design** (disjoint). Statistic:
stratified difference Δ = mean_h(Q(h) − c̄_h) with s.e. from the binomial variances; **effect bound** registered:
on the 145-member noprime set, "no effect of size ≥ 0.10" is accepted if the 95 % CI of Δ lies in (−0.10, 0.10);
"effect" if |Δ/s.e.| ≥ 3. q-to-word construction (fixed now): for the least q | X with (840/q) = −1, the candidates
f = qm, m ≤ 64, f ≡ 3 (mod 4), f ≤ (4p + 1)/3; Y(p) := [some candidate is a (★) witness: (−p mod f) | (f + 1)/4].
Decoy: for the same p, q′ = a prime with (p/q′) = −1, q′ ∤ X, q′ ≡ q (mod 8), |q′ − q| ≤ 0.1 q (nearest such),
same construction. Kill K9: Y(q) − Y(q′) not ≥ 3σ above 0 ⟹ q | X carries no word-building information beyond being
a non-residue of its size; HOT LEAD only if Y = 1 on every hard prime and the excess is significant.

## 2–5. (results for I6, I5, #10, Pell letters: below as they come)

## 6. I9 — result (EVIDENCE; registered design; one deviation + one post-hoc size check, disclosed)
Run: `uv run --with sympy python scripts/z70_loose_i9.py` (seed 7070) → `data/z70/loose/i9_run.txt`, rows
`i9_rows.json`; post-hoc `scripts/z70_loose_i9b.py` → `i9b_twosided.txt`. Disjoint controls: 20 per hard prime,
same class mod 840, uniform in [p/2, 2p], no hard-list member, no reuse (hard primes with no admissible control:
5569, 9601 (𝔊*), 9601, 23041 (noprime), 1129, 2521, 3361 (U⁽⁸⁾) — dropped from Δ).

| hard set (𝔐-members with controls) | Q hard | Q controls | Δ (stratified) ± s.e. | z | 95 % CI |
|---|---|---|---|---|---|
| (★)-zeros (9) | 0.444 | 0.524 | −0.009 ± 0.158 | −0.06 | (−0.32, +0.30) |
| 𝔊*-zeros (18) | 0.450 | 0.569 | −0.121 ± 0.115 | −1.05 | (−0.35, +0.10) |
| noprime (143) | 0.559 | 0.590 | −0.022 ± 0.041 | −0.53 | (−0.101, +0.058) |
| U⁽⁸⁾-zeros (8) | 0.636 | 0.598 | +0.157 ± 0.179 | +0.88 | (−0.19, +0.51) |
| R₈-zeros (4, F2) | 0.500 | 0.637 | −0.138 ± 0.245 | −0.56 | (−0.62, +0.34) |

* **Registered effect bound:** on the noprime set the 95 % CI is (−0.101, +0.058): it reaches −0.101, just outside the
  registered (−0.10, 0.10) band, so the equivalence criterion is **narrowly not met** (it is met for +0.10, not for
  −0.10); no effect criterion (|z| ≥ 3) fires anywhere. Reading (EVIDENCE): no detected difference; an effect of
  size ≥ 0.10 in the direction "hard primes have Q *more* often" is excluded at 95 %; a deficit of ≈ 0.10 is not.
* **q-to-word construction (registered decoy, |q′ − q| ≤ 0.1 q):** Y(q) is tiny (≈ 0.02–0.03 on controls) and equal
  to the decoy rate (noprime controls 889 pairs: McNemar b = 23, c = 20, z = +0.46). The 10 % window is empty for
  most small q (772 of the noprime-control Q-primes had no decoy) — a design flaw of the registration.
  *Deviation (disclosed):* a window-free "nearest admissible prime" decoy gave a large apparent excess on controls
  (noprime controls: Y(q) = 0.158 vs Y(q′) = 0.094, z = +5.91). *Post-hoc size check:* that decoy is
  biased upward in size for small q (Y falls like ≈ (log q)/q); with a **two-sided** decoy (mean of the nearest
  admissible prime below and above q; mean log(decoy/q) ≈ −0.02) the excess disappears: noprime controls
  1 233 pairs, Y(q) = 0.068 vs 0.061, z = +0.84; all sets |z| ≤ 1.0. So the +5.9 was a size artifact.
* On hard primes the construction essentially never fires (noprime hard: Y(q) = 0.016 on 64 two-sided pairs).

**Verdict I9 (EVIDENCE):** with disjoint factor-two-matched controls the X-coordinate classifier shows no
difference (|z| ≤ 1.05 everywhere); a q | X with (840/q) = −1 builds (★) words exactly as often as a size-matched
non-residue prime not dividing X. K9 fires (no word-building information). Nothing here is a mechanism; the
remaining untested direction is any construction using q *together with* Y (e.g. f built from q and Y) — not
pursued.
