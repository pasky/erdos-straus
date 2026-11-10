# Z70_CLASS — the I17 residual and the class-group structure of good forms (wave z70, lane CLASS)

**ES is OPEN. Nothing here proves or disproves it.** Status: checkpoint 1 (pre-registration; no registered run yet).
Scripts `scripts/z70_class_*`, data `data/z70/class/`. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Sources: `Z69_TWIST.md` §9 (I17 round 2: Lemmas DL, CS; residual d = 3 energy Z_Ex = +3.6 and a small d = 1
residual on the 10⁶ window, both against nulls that do not contain DL/CS), `Z69_MINE.md` §§3, 12 (open: class-group
structure beyond the class number vs U₇ / (★) witnesses), `data/z69/xreview/REVIEW_{TWIST,MINE}.md`.

## 0. Mandatory falsifier table (checkpoint-1 version; restated at the end)

| screen | behaviour of the objects of this lane | label |
|---|---|---|
| **F1 odd squares** | G_d(m²) = ∅ for every d and odd m (T1). In the language of §1.1 this is a genus statement: a good form [A, 4ad, de] has A ≡ −1 (mod 4d), so χ_{−4d}(A) = χ_{−4d}(−1) = −1, while a positive form of discriminant −4dm² can represent A (coprime to 2dm) only with χ_{−4d}(A) = +1; for n prime the same computation gives the Jacobi condition (n/A) = −1. Every symmetry studied here (DL, CS, anything found by the residual hunt) is a map *on existing solutions* and is vacuous at squares; a generative map would have to produce a good class in the target genus coset, which does not exist at squares — that is where non-squareness must enter. | PROVED (elementary; §1.1) |
| **F2 numerator 8 / C-even** | Type II with even d (d = 2) is in the sample; DL and CS hold verbatim for every d, so no statement here distinguishes C even from C odd. No positivity claim. | PROVED (lemmas) |
| **F3 composites** | DL, CS and the e-ideal dictionary (§1.1) hold for every n ≡ 1 (4) (composite n: primes dividing gcd(e, n) need care, handled in the scripts). The residual profile is also run on the composite (★)-zeros below 10⁵ (d = 1). | PROVED / run registered |
| **F4 known zeros** | The hard list (14 (★)-zero primes, 38 𝔊*-zero primes below 10⁶, 2521, 3361, 21841, 76441) is in the d = 1 and d = 3 samples. | run registered |

## 1. Item 1 — the I17 residual

### 1.1 Precise objects (PROVED, elementary; checked by `scripts/z70_class_core.py`)
d ≥ 1, n ≡ 1 (4), D = −4dn, Cl(D) the form class group. Type II solution: (a, b, c, e) ∈ ℕ⁴, 4abd = n + e, ce = a + b;
A := 4acd − 1, N_a := n + 4a²d = A·e (z69 §9.1). Good class g = [A, 4ad, de] ↔ ideal 𝔄 = (A, 2ad + √−dn);
**e-ideal** 𝔈 = (e, 2ad + √−dn) ↔ [e, 4ad, dA]. Since 𝔄·𝔡·𝔈 = (2ad + √−dn) (𝔡 = (d, √−dn), [𝔡] = T_d = [d, 0, n]),
  **G_d(n) = T_d + X_d(n),  X_d(n) := {±[𝔈] : 𝔈 an e-ideal of a solution}**
(the b-side solution (b, a, c, e) has e-ideal conj(𝔈) because e | a + b). Check: `selftest` reproduces the z69 sets for
ten (n, d) incl. 409, 4545, 21841. Translation statistics of G and X coincide. Every e-ideal factors into split prime
ideals: [𝔈] = Σ_q ε_q k_q [𝔔_q] (𝔔_q the prime ideal over q with the least root; ε_q = ±1) — checked exactly.
Equivalent description (PROVED): for gcd(e, 2dn) = 1 the ideal (e, ρ + √−dn) is an e-ideal of a solution iff
4d | n + e and M_e := (n + e)/(4d) has a divisor a ≡ ρ/(2d) (mod e) (then b = M_e/a ≡ −a (mod e) automatically).
* **Lemma DL in this language**: two e-ideals of the same fibre a with norms e and e/ℓ are related by the *ideal identity*
  𝔈 = 𝔈′·𝔏 (𝔏 the prime ideal over ℓ dividing 2ad + √−dn).
* **Lemma CS in this language**: if 4ad | n − 1, the complement A of a fibre-a solution is itself the norm of an e-ideal of
  fibre a (namely 𝔄), and [𝔄] = T_d − [𝔈] — a *class* identity coming from the principal ideal (2ad + √−dn), not an ideal
  identity. For d = 1 (T_1 = 0) it makes 𝔄 and conj(𝔈) distinct ideals in one class ("collisions").

### 1.2 Pre-registration (committed before any registered run; smoke tests listed)
**Null PSC (prime swap + CS imposed)** (`scripts/z70_class_null.py`, null `PSC`): a random injection π on the primes q
occurring in good norms — π(q) = q for q ≤ 50 and for the translation primes of L1/L3; otherwise π(q) uniform among unused
split primes q′ with the same genus signature (q′ mod 8, Legendre symbols at the odd primes of dn) and |log q′ − log q| ≤ 0.1
(widened until ≥ 8 candidates). Null class of 𝔈 = Σ ε_q k_q [𝔔_{π(q)}]; then the CS relations are imposed exactly
([𝔄]_null := T_d − [𝔈]_null along a BFS tree of the CS graph; inversion closure kept). **PSC preserves every ideal-level
identity among good ideals (all DL pairs), every CS class identity, inversion closure, the genus coset and the norms (to the
window); it randomises every other class-level coincidence.** R = 200 replicates; Z_S := Σ_n (obs − mean)/√Σ_n var.
(Design note: a pure conjugation-flip null, s_q = ±1, was tried first and is *degenerate* — X_s = X whenever all good norms
are prime powers — so it was dropped before any registered run; the plain prime-swap PS without CS is kept as the
power check.)
**Statistics** (per n, on X; O(t) = #{x ∈ X : x + t ∈ X}): Mx, Ex = max and Σ O(t)² over translations t of order > 2;
L1 = O at the class of the least split prime whose class is a square; L3 = Σ O over the first three such distinct classes
(mod inversion); reported also: K = |X|, C0 = (#distinct good ideals) − K (collisions), M, E, A2 (overlap at order-2
translations). **Positive controls**: C0 (d = 1) and A2 (d > 1) carry Lemma CS: |Z| < 3 against PSC (imposed) and strongly
positive against PS (power check).
**Samples (fresh, disjoint from z69's windows and from the smoke tests below; primes p ≡ 1 (8)):**
* d = 1: F1 = [24000, 30000), F2 = [202000, 206000), F3 = [1001000, 1004000), F4 = [4000000, 4003000);
* d = 2, 3, 5, 7: F1, F2 = [202000, 210000), F3′ = [1001000, 1005000);
* replication of z69's windows: d = 1 on [20000, 24000), [200000, 202000), [10⁶, 10⁶ + 1000); d = 3, 5 on [20000, 24000);
* screens: d = 1 and d = 3 on the hard list (as z69); d = 1 on the composite (★)-zeros below 10⁵.
**Registered outcomes (per d, on the fresh windows):**
* **K-RES (kill: no third structure):** |Z| < 3 for each of Mx, Ex, L1, L3 against PSC on every fresh window ⟹ the
  translation structure of G_d beyond its norm profile is accounted for by DL + CS (bounded: these windows).
* **RESIDUAL:** Z ≥ 3 for the same statistic on ≥ 2 fresh windows of one d, or Z ≥ 4 for the sum over the fresh windows
  of one d ⟹ a residual survives → hunt: decompose the excess overlap pairs (which pairs, which ideals, which relation),
  try the candidate mechanisms of the brief (Vieta/descent, genus/ambiguous, Rédei, composition with small split primes,
  (★) ↔ Type I/II maps), prove what is found, and test whether it is *generative*.
* anything else: **unresolved**, reported with the numbers.
* validity: if a positive control has |Z| ≥ 3 against PSC the CS imposition is incomplete and the run is not interpreted
  until fixed.
**Smoke tests done before this registration (exploratory, not part of any registered outcome):** PS and PSC, d = 1,
[20000, 21000), R = 100: C0 = 148 vs PS 76.9 (Z +10.4) and vs PSC 150.4 (Z −0.75) — the positive control behaves;
PSC Z_Mx +2.66, Z_Ex +1.57, Z_L1 +1.70, Z_L3 +1.09. PSC d = 3, [200000, 201000), R = 100: Z_A2 −0.34, Z_Mx +3.19,
Z_Ex +4.05, Z_L1 −0.74, Z_L3 −0.70 — the d = 3 energy residual reappears against PSC in the smoke test. These two
windows are excluded from the registered samples.

### 1.3 Registered outcome of §1.2 (PSC) — RESIDUAL fires for d = 1 and d = 2; K-RES fires for d = 3, 5, 7
Data `data/z70/class/i1_PSC_*.txt` (pooled over the fresh windows by `scripts/z70_class_pool.py`). Positive controls behave
(C0 d = 1 and A2 d > 1: |Z| < 3 against PSC on every window; against PS: C0 Z = +23.7 (d = 1, F1), A2 Z = +17.9 (d = 3, F2)).
Full table in §1.5. In short: d = 1 L1 Z = +4.05, +5.18, +7.47, +8.44 on F1–F4 (pooled +11.5), Mx pooled +9.7;
d = 2 pooled Ex +5.0, Mx +4.3 (per window only F3 ≥ 3); d = 3, 5, 7: every registered |Z| < 3 on every fresh window
(pooled d = 3 Ex +2.7). So the z69 d = 3 "residual energy" is accounted for by DL + CS; the d = 1 residual is real and
grows with n.

### 1.4 Residual hunt, step 1 — Lemma FIB and the fibre-principal null PSF (pre-registered before any PSF run beyond a smoke test)
**Lemma FIB (PROVED).** (2ad + √−dn) = 𝔡·𝔅_a with N(𝔅_a) = N_a, and every e-ideal *and* every A-ideal of a fibre-a solution
divides 𝔅_a. Hence [𝔅_a] = T_d, and every good class has three natural ideal representatives
  g = [𝔄] = [conj 𝔅′] = T_d − [𝔈]   (𝔄 of norm A = 4acd − 1, 𝔅′ the A-ideal of the b-side solution, of norm 4bcd − 1),
and for two e-ideals of one fibre with coprime norms [𝔈] + [𝔈′] = T_d − [𝔚], 𝔚 = 𝔅_a/(𝔈𝔈′) (CS: 𝔚 = 1). In particular a
good class contains an ideal of norm min(A, B, ·) — small when c and a (or b) are small — and *ideal* identities among
these A-side representatives (e.g. 𝔄′ = 𝔄·𝔏₀ across fibres) are *class* coincidences from the e-side point of view, which
PSC randomises.
**Null PSF**: PSC's prime swap, plus the principal relation [𝔅_a] = T_d for every active fibre a imposed exactly (integer
elimination with ±1 pivots, pivots preferably primes outside the good norms; primes above the largest good-norm prime get a
uniform class of their genus coset; `scripts/z70_class_psf.py`). PSF preserves DL, CS, Lemma FIB and every ideal identity
among all representatives; it randomises the remaining coincidences. Power caveat (seen in the smoke test, d = 1,
[20000, 21000)): at small n most good classes are *determined* by the fixed small primes through these relations (26 of
472 good ideals had a non-degenerate null class), so the script reports the non-degenerate fraction.
**Registered (before the runs):** windows = the fresh windows of §1.2 for d = 1 (F1–F4), d = 2 (F1–F3), d = 3 (F1–F3),
plus unseen windows d = 1: G1 = [500000, 503000), G2 = [2000000, 2003000), G3 = [8000000, 8002000); d = 2: G1 = [500000, 510000),
G2 = [2000000, 2006000); R = 200.
* **K-FIB:** against PSF |Z| < 3 for Mx, Ex, L1, L3 on every window with ≥ 20 % non-degenerate good ideals, and pooled |Z| < 4
  per d ⟹ the residual of §1.3 is accounted for by Lemma FIB (no third mechanism visible at this resolution).
* **RESIDUAL-2:** otherwise (same thresholds as §1.2) ⟹ decompose the OTHER-type L1 pairs and continue.
* validity: C0 (d = 1) / A2 (d > 1) |Z| < 3 against PSF; windows with < 20 % non-degenerate ideals are reported as "no power".
Smoke test only (excluded): d = 1, [20000, 21000), R = 100: all |Z| ≤ 1.7, C0 −0.97, L1 −0.11.

## 2. Item 2 — class-group structure beyond h vs U₇ witnesses (pre-registration)
Samples (from `Z69_MINE.md` round 2, `data/z69/mine/`): H_train (438), H_test (411), CTRL (2 547 size-matched controls);
exploration on H_train + CTRL only; H_test scored once.
**2a (prime-level invariants).** For each p: v₂h(−4p), v₂h(−8p), 1[3 | h(−4p)], 1[3 | h(−8p)], h(p) = 1, and the order
of the class of a prime ideal over the least split prime in Cl(−4p) relative to h (log ord / log h). Test: H vs CTRL
difference (two-sample z on means/proportions). Signal ⟺ |z| ≥ 4 on H_train and the same sign with |z| ≥ 3 on H_test.
(z69 reported the v₂ parts descriptively for H-low; this is the split, registered version.)
**2b (orders of representation-ideal classes, exact decoys).** For a U₇ witness (f, x, y, z) of p (f = xy − 1,
xyz − x − z = p) the representation ideal is 𝔣 = (f, 1 + √−yp) in discriminant −4yp (form [f, 2, zy − 1]; PROVED: f·(zy − 1)
= yp + 1). Exact decoy: an ideal (f′, r + √−yp) of the *same discriminant*, f′ ≡ f (mod 8), |f′/f − 1| ≤ 0.05, gcd(f′, 2yp) = 1,
the same Legendre symbols (f′/q) as f at every odd prime q | yp (⟹ same genus coset), r a random root; 2 decoys per witness.
Statistics: S1 = log ord[𝔣] / log h(−4yp); S2 = v₂ ord[𝔣]; S3 = 1[3 | ord[𝔣]]. Witnesses used: those with 4yp ≤ 4·10¹³
(class groups by PARI), at most 8 per prime (uniform), primes from H_train, H_test, CTRL. Estimator: real − mean(decoys)
per witness, averaged per prime, cluster-by-prime z. Signal ⟺ |z| ≥ 4 on H_train and same-sign |z| ≥ 3 on H_test;
CTRL reported. Not a HOT LEAD unless a signal also yields a rule passing Z69_MINE K1–K4.
