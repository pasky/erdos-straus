# Z70_CLASS — the I17 residual and the class-group structure of good forms (wave z70, lane CLASS): on the tested windows the residual is divisor-lattice structure seen through a class map injective on small primitive ideals; no forcing mechanism; not a HOT LEAD

**ES is OPEN. Nothing here proves or disproves it.** Status: internal hostile review round 1 applied (§8): the first PSC/PSF null implementations were wrong — their calibrated readings (§§1.3, 1.5) are withdrawn and replaced by corrected runs (§§1.9–1.10). Verdict (§4): **narrowed descriptively, not closed — the I17 residual beyond DL + CS is real (d = 1; d = 3 at larger n) and, on the tested windows, no positive residual remains once all divisor-lattice relations (Lemmas Φ, DL′) and ideal identities are kept; no forcing mechanism established; item 2 null apart from a genus effect.** Not a HOT LEAD.
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
| **F4 known zeros** | The hard list (14 (★)-zero primes, 38 𝔊*-zero primes below 10⁶ [correction: 26 — the file has 38 up to 10¹⁰], 2521, 3361, 21841, 76441) is in the d = 1 and d = 3 samples. | run registered |

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

### 1.3 Registered outcome of §1.2 (PSC) — RESIDUAL fires for d = 1 and d = 2; K-RES fires for d = 3, 5, 7 [WITHDRAWN: PSC was mis-implemented, see §1.9; corrected results §1.10]
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

### 1.5 Results of the original PSC / PSF runs [WITHDRAWN as calibrated evidence (§1.9); kept as a record]
**PSC (DL + CS exact)** — fresh windows (registered statistics Mx, Ex, L1, L3; controls C0 for d = 1, A2 for d > 1):

| d | window (primes p ≡ 1 (8)) | n analysed | Z_Mx | Z_Ex | Z_L1 | Z_L3 | control |
|---|---|---|---|---|---|---|---|
| 1 | F1 [24000, 30000) | 141 | +3.80 | +3.02 | **+4.05** | +2.73 | C0 −2.72 |
| 1 | F2 [202000, 206000) | 77 | +4.05 | +1.75 | **+5.18** | +2.96 | C0 +0.12 |
| 1 | F3 [1001000, 1004000) | 61 | +6.37 | +3.34 | **+7.47** | +6.94 | C0 +1.12 |
| 1 | F4 [4000000, 4003000) | 47 | +5.60 | +3.68 | **+8.44** | +7.29 | C0 +0.50 |
| 2 | F1 / F2 / F3′ | 129 / 156 / 78 | +2.09 / +1.98 / +3.42 | +2.29 / +2.13 / +4.20 | −0.17 / +0.10 / −0.91 | +0.25 / −1.15 / +0.21 | A2 ≤ 1.1 |
| 3 | F1 / F2 / F3′ | 120 / 147 / 74 | +1.22 / +1.03 / +1.67 | +0.89 / +1.94 / +1.82 | +0.59 / +0.38 / −0.70 | +0.75 / −0.51 / −1.02 | A2 ≤ 0.8 |
| 5 | F1 / F2 / F3′ | 96 / 129 / 70 | +1.16 / +1.07 / +0.83 | +0.90 / +0.55 / +0.84 | −0.44 / +1.30 / −0.93 | +0.31 / +0.64 / +2.16 | A2 ≤ 0.9 |
| 7 | F1 / F2 / F3′ | 70 / 110 / 58 | −1.31 / +1.93 / +1.55 | −0.81 / +2.46 / +0.93 | −0.20 / +1.12 / −0.27 | −0.96 / +0.30 / +0.28 | A2 ≤ 1.4 |

Pooled over the fresh windows (`scripts/z70_class_pool.py`): d = 1 Mx +9.7, Ex +5.8, L1 +11.5, L3 +8.9; d = 2 Mx +4.3,
Ex +5.0; d = 3 Mx +2.1, Ex +2.7; d = 5, 7 all ≤ 2.3. Replication of z69's windows against PSC: d = 1 L1 +4.83, +3.64, +3.99
(Mx +2.7, +3.9, +3.0); d = 3 Ex +1.82 (z69 against N2: +3.55); d = 5 Ex +0.19. Hard list (d = 1, 32 primes with |G| ≥ 2;
d = 3, 4 primes): all |Z| ≤ 1.7. Composite (★)-zeros below 10⁵ (d = 1; 24 analysed, 61 skipped because an ideal norm
shares a prime with n, 8 with |G| < 2): all |Z| ≤ 1.9. Power checks against PS (no CS): C0 +23.7 (d = 1, F1), A2 +17.9
(d = 3, F2). Not registered but notable: against PSC the d = 1 order-2 overlap A2 = O(J) is *below* the null (pooled −6.65)
— explained exactly in §1.6 (Corollary J).
**Registered verdicts (§1.2):** d = 1 **RESIDUAL** (L1 ≥ 3 on all four fresh windows); d = 2 **RESIDUAL** by the pooled
clause (Ex +5.0); d = 3, 5, 7 **K-RES** (every registered |Z| < 3 on every fresh window): the z69 d = 3 "residual energy"
is accounted for by DL + CS.

**PSF (all active-fibre principal relations exact)** — registered §1.4 (non-degenerate fraction = good ideals whose null
class varies; "no power" if < 20 %):

| d | window | non-degenerate | Z_Mx | Z_Ex | Z_L1 | Z_L3 | control |
|---|---|---|---|---|---|---|---|
| 1 | F1 / F2 | 8 % / 15 % (no power) | −1.03 / −0.03 | +0.54 / −0.91 | −2.47 / −2.18 | −1.11 / −1.93 | C0 −2.28 / 0.00 |
| 1 | F3 / F4 | 22 % / 26 % | +1.40 / −1.17 | +1.57 / +0.08 | −0.66 / −2.02 | −1.67 / −2.58 | C0 −1.71 / −1.10 |
| 1 | G1 / G2 / G3 | 20 % / 26 % / 34 % | −0.43 / −0.25 / +1.31 | +0.72 / −0.30 / −1.15 | −1.11 / −0.85 / −0.67 | −1.47 / **−3.04** / −2.96 | C0 −2.40 / −2.09 / −1.33 |
| 2 | F1 / F2 / F3′ | 5 % / 15 % / 26 % | +0.70 / −1.52 / −0.16 | −0.11 / −0.55 / −1.25 | +1.84 / +1.39 / −1.02 | +2.87 / −0.66 / −1.74 | A2 ≤ 1.3 |
| 2 | G1 / G2 | 20 % / 25 % | −0.44 / −0.85 | −0.41 / +0.95 | −0.24 / +0.81 | −0.51 / −0.36 | A2 ≤ 1.1 |
| 3 | F1 / F2 / F3′ | 13 % / 26 % / 32 % | +0.92 / +0.62 / −0.33 | +1.26 / +0.78 / −0.73 | +1.15 / −1.34 / +0.17 | +1.03 / **−3.18** / −1.53 | A2 ≤ 0.7 |

Pooled (all windows): d = 1 Mx −0.2, Ex −0.2, L1 −3.9, L3 −5.3 (C0 −4.5, A2 −3.2); d = 2 all |Z| ≤ 1.3 except none; d = 3
L3 −2.5, others ≤ 1.3. **Registered verdict:** the *positive* residual is gone everywhere (largest positive Z among the
registered statistics on a window with power: +1.57); RESIDUAL-2 does not fire. K-FIB fails formally, and only in the
*negative* direction (L3 −3.04 on d = 1 G2, −3.18 on d = 3 F2): PSF over-produces coincidences (pooled d = 1 L1 −3.9, L3 −5.3,
C0 −4.5). Diagnostic (post hoc, not registered): restricting the swap to primes with the same 2-Sylow projection of
their class (`Z70_MATCH2=1`) moves L3 on G2 from −3.04 to −2.32 and leaves the rest similar. *Assessment:* the overshoot
is a property of the null — pivot-solved classes of small primes lose the "free region" protection of §1.6 (distinct small
ideals lie in distinct classes), so the null has more chance coincidences than the data; it is an anti-coincidence, not a
symmetry candidate. Recorded as **unresolved (negative direction)**.

### 1.6 What the structure is — three principal relations per solution and the free region (PROVED + CERTIFIED)
Notation of §1.1; O = ℤ[√−dn] (discriminant −4dn), invertible ideals ↔ primitive forms (standard; e.g. Cox, *Primes of the form
x² + ny²*, §7). Hypotheses throughout §1.6: n ≡ 1 (4), **gcd(n, d) = 1** and, for the fibre a, **gcd(a, n) = 1** (automatic for prime n and
a < n). Put B_a := 4ad and, for M | N_a, φ_a(M) := class of [M, 4ad, dN_a/M].

**Lemma Φ (fibre homomorphism; generalises DL, CS and FIB). PROVED.** (i) [M, 4ad, dN_a/M] is primitive of discriminant
−4dn; (ii) φ_a(MM′) = φ_a(M) + φ_a(M′) whenever MM′ | N_a (coprime or not); (iii) φ_a(N_a) = T_d, φ_a(1) = 0;
(iv) if a′ ≡ a (mod M) and M | N_{a′} then φ_{a′}(M) = φ_a(M).
*Proof.* (i) (4ad)² − 4M·dN_a/M = 16a²d² − 4d(n + 4a²d) = −4dn. A common prime of M and 4ad divides gcd(N_a, 4ad), which
divides gcd(n, 4ad) = gcd(n, a) = 1 (n odd, gcd(n, d) = 1). (ii) [M, 4ad, dN_a/M] ↔ the ideal 𝔐 = (M, 2ad + √−dn) ⊇ 𝔅_a := (N_a, 2ad + √−dn). β_a = 2ad + √−dn is primitive (no rational
prime divides it, its √-coefficient being 1) and N_a is prime to 2dn, hence to the conductor of O; so 𝔅_a has a unique
factorisation into invertible prime ideals, all "on one side" (for each q | N_a only the prime 𝔔 = (q, 2ad + √−dn) occurs,
never its conjugate, as 𝔔·conj 𝔔 = (q) would put q | β_a). The divisors of 𝔅_a are therefore in bijection with the
divisors M of N_a, M ↦ 𝔐 = (M, 2ad + √−dn), and 𝔐𝔐′ = (MM′, 2ad + √−dn) whenever MM′ | N_a. (For coprime M, M′ this is
also Dirichlet composition of the concordant forms [M, B, M′·dN_a/(MM′)], [M′, B, M·dN_a/(MM′)]; Cox §3.) (iii) (β_a) = 𝔡·𝔅_a, and directly: [N_a, 4ad, d] ~ [d, −4ad, N_a] and (x, y) ↦ (x + 2ay, y) turns it
into [d, 0, N_a − 4a²d] = [d, 0, n]; [1, B, ·] is principal. (iv) the middle coefficients 4ad, 4a′d agree mod 2M. ∎
Reading: the good classes are G_d(n) = {φ_a(A) : a ≥ 1, A | N_a, A ≡ −1 (mod 4ad)} (§1.1), and the e-side classes are
φ_a(e) = T_d − φ_a(A). Lemma DL = (ii) with M′ = ℓ; Lemma CS = (ii)+(iii) with M′ = N_a/M; FIB (§1.4) = (ii)+(iii) with
three coprime factors. (For composite n with gcd(a, n) > 1 the statements need the usual coprimality; such n were skipped in the scripts.)

**Lemma DL′ (the c-fibre lattice). PROVED.** For a solution (a, b, c, e): (4acd − 1)(4bcd − 1) = 4c²dn + 1, i.e. A·B =
4c²dn + 1 = N(1 + 2c√−dn); conversely every factorisation 4c²dn + 1 = A·B with A ≡ B ≡ −1 (mod 4cd) is a solution with this
(c, d) (a = (A+1)/(4cd), b = (B+1)/(4cd), e = (a+b)/c). Hence moving a factor ℓ ≡ 1 (mod 4cd) of B into A gives a second
solution (a + kA, ·, c, ·), k = (ℓ − 1)/(4cd), whose A-ideal is 𝔄·𝔏 — an ideal identity between the A-representatives of two
good classes in *different* a-fibres. *Proof.* (4acd − 1)(4bcd − 1) = 16abc²d² − 4cd(a + b) + 1 = 4cd(c(4abd) − ce) + 1 = 4cd·cn + 1, using 4abd = n + e and
a + b = ce. Conversely, with a := (A + 1)/(4cd), b := (B + 1)/(4cd) ∈ ℕ the same expansion gives 4c²dn = 16abc²d² − 4cd(a + b),
i.e. a + b = c(4abd − n); so e := 4abd − n = (a + b)/c is a positive integer and (a, b, c, e) is a solution. Moving
ℓ ≡ 1 (mod 4cd) with gcd(ℓ, A) = 1 from B to A keeps both factors ≡ −1 (mod 4cd); the new first letter is
a′ = (ℓA + 1)/(4cd) = a + kA (as ℓ − 1 = 4cdk, A + 1 = 4acd), so a′ ≡ a (mod A) and the new A-ideal (ℓA, 2a′d + √−dn) is
the product of 𝔄 = (A, 2ad + √−dn) and 𝔏 = (ℓ, 2a′d + √−dn) (coprime norms, compatible roots). ∎ (Lemma DL′ is the c-fibre analogue of z69's DL; the complement in the c-fibre is the a ↔ b inversion.)

**Lemma SR (small natural representatives). PROVED.** Every good class g of a solution (a, b, c, e) contains ideals of
norms A = 4acd − 1, B = 4bcd − 1 and de (namely 𝔄, conj 𝔅, 𝔡·conj 𝔈), and
  min(A, B, de) ≤ √(d(2n + e)) ≤ √(d(2n + (n + 4d)/(4d − 1)))   (d = 1: ≤ √((7n + 4)/3)).
*Proof.* g = φ_a(A) = T_d − φ_a(e) (Lemma Φ), and T_d − φ_a(e) is the class of [d, 0, n]∘[e, −4ad, dA], which represents
de; g = −φ_b(B) (a ↔ b) is the class of [B, −4bd, ·]. A·de = dN_a and B·de = dN_b; take the letter min(a, b), for which
N = n + 4 min(a,b)²d ≤ n + 4abd = 2n + e, and e ≤ (n + 4d)/(4d − 1) (z69). ∎ *Caveat (added in the final pass):* as a
statement about classes SR is weak — every class of discriminant −4dn contains an ideal of norm ≤ √(4dn/3) (its reduced
form). Its content is that the *natural* representatives, which carry the solution's arithmetic, are of that size; and
when a natural representative has norm N < √(dn) it *is* the reduced form of the class (reduce B into (−N, N]; then
C = (B² + 4dn)/(4N) > dn/N > N). CERTIFIED: the least natural norm is ≤ √(dn) — so the reduced form of the class is a natural
good form — for 95 % (d = 1, n ≈ 2.7·10⁴), 97.7 % (10⁶), 98.4 % (4·10⁶) of good classes, and ≥ 96 % for d = 2, 3, 5, 7 at
2·10⁵ (`i1_repid_*.txt`, K_small/K).

**Remark RF (good classes read off the reduced forms). PROVED; CERTIFIED check.** A class g contains a good form (Type II
with this d) iff g has a primitive form [A, B, C] with B ≡ B* (mod 2A) for some positive B* ≡ 0 (mod 4d) dividing A + 1.
(⇐: put a = B*/(4d), c = (A + 1)/B*; [A, B*, C*] ~ [A, B, C] with C* = (B*² + 4dn)/(4A) = dN_a/A, so A | N_a (gcd(A, d) = 1),
e := N_a/A ≡ −n (mod 4ad) because A ≡ −1, and (a, (n + e)/(4ad), c, e) is a solution. ⇒: take [A, 4ad, de].) If A < √(dn)
the form [A, B, C] with |B| ≤ A is the reduced form of g (C > dn/A > A). Check (`scripts/z70_class_rfcheck.py`,
`i1_rfcheck.txt`): for every prime p ≡ 1 (8) in [20000, 24000), [1001000, 1003000) (d = 1) and [202000, 206000) (d = 3), the
reduced forms with A < √(dn) satisfying the criterion are exactly the good classes with a natural A-norm < √(dn) (216 primes,
0 discrepancies). So, for ≈ 97 % of good classes, membership in G is visible on the reduced form itself: first coefficient
A, middle coefficient B ≡ a positive multiple of 4d dividing A + 1 — the tied divisor condition again, now on the list of
reduced forms.

**Lemma FR (free region). PROVED.** Let 𝔞, 𝔟, 𝔱 be invertible ideals of O with [𝔟] = [𝔞] + [𝔱] and
N(𝔞)N(𝔟)N(𝔱) < dn. Then 𝔟·conj(𝔞)·conj(𝔱) = xO with x ∈ ℤ_{>0} and x² = N(𝔞)N(𝔟)N(𝔱).
*Proof.* conj(𝔞) has class −[𝔞] (𝔞·conj 𝔞 = N(𝔞)O for invertible 𝔞; Cox §7), so the product is invertible and principal, = αO with
α ∈ O (it is integral), α = x + y√−dn, N(α) = x² + dny² = N(𝔞)N(𝔟)N(𝔱) < dn (norms are multiplicative on invertible
ideals), so y = 0. ∎
**Corollary FR′ (PROVED).** Two distinct *primitive* invertible ideals 𝔞 ≠ 𝔟 (not contained in mO for any integer m > 1)
with N(𝔞)N(𝔟) < dn lie in distinct classes. *Proof.* By FR with 𝔱 = O, 𝔟·conj 𝔞 = xO, so N(𝔞)𝔟 = x𝔞; comparing the largest
integers dividing both sides (contents N(𝔞) and x) gives x = N(𝔞) and 𝔟 = 𝔞. ∎ (Primitivity is needed: O and 2O.) The natural
representatives (A, 2ad + √−dn), (de, ·) are primitive. FR concerns *triples*: a class relation g′ = g + t is forced to be a
rational identity only when the product N(𝔞)N(𝔟)N(𝔱) < dn; two representatives each below √(dn) do not suffice.
**Corollary J (d = 1). PROVED.** J = [2, 2, (n + 1)/2] (n ≡ 1 (4)). If g and g + J both lie in G_1(n), then
2·m(g)·m(g + J) ≥ n, where m(·) is the least norm of an odd-norm ideal in the class (in particular of a natural
representative). *Proof.* FR with 𝔱 = (2, 1 + √−n) (norm 2) would give x² = 2·(odd)·(odd), impossible. ∎
CERTIFIED (`i1_jcheck.txt`, with m = the least *natural* norm, an upper bound for the least odd norm): 148 + 28 + 6 J-overlap
pairs in three d = 1 windows, 0 violations of 2m(g)m(g+J) ≥ n; 84–90 % of good classes have 2m² < n, so their J-partner, if
any, must have least odd norm ≥ n/(2m) > m (the review found 24 such small classes *with* a J-partner in the first window,
e.g. n = 22129, natural minima 95 and 143). This explains the J-avoidance seen by z69 (K-I17 fired for J) qualitatively — an
arithmetic exclusion for pairs of small classes; against the corrected nulls the d = 1 order-2 overlap A2 = O(J) is below
FIX-CS (pooled −8.9) and slightly below FIX-ALL (−3.5).

**Explicit decomposition (CERTIFIED; `scripts/z70_class_repid.py`).** Every overlap pair (g, g + [𝔏]) at a translation
prime ℓ is classified as EID (e-side ideal identity — preserved by PSC), REP-ID (identity between other natural
representatives: A–A pairs, all of them inside one c-fibre = Lemma DL′; A–E and B–E pairs = Lemma Φ in a common fibre or a
shared divisor of two N's), or OTHER (no identity of natural representatives):

| d | window | good classes (least natural norm ≤ √(dn)) | L1 pairs: EID / REP-ID / OTHER | other translation primes: EID / REP-ID / OTHER |
|---|---|---|---|---|
| 1 | [24000, 30000) | 1736 (95.2 %) | 264 / 159 / 81 | 153 / 172 / 345 |
| 1 | [1001000, 1004000) | 1534 (97.7 %) | 192 / 94 / 18 | 172 / 97 / 79 |
| 1 | [4000000, 4003000) | 1510 (98.4 %) | 132 / 84 / **2** | 124 / 86 / 28 |
| 2 | [202000, 210000) / [1001000, 1005000) | 1716 / 1166 | 6 / 4 / 29 ; 4 / 2 / 5 | 48 / 20 / 63 ; 36 / 18 / 24 |
| 3, 5, 7 | [202000, 210000) | 984 / 582 / 400 | 8/4/4 ; 8/4/4 ; 0/2/1 | 18/18/7 ; 14/8/9 ; 10/0/3 |

At d = 1 the number of REP-ID pairs (94 on F3, 84 on F4) is of the size of the (withdrawn) PSC excess on L1 (67; 62),
and the OTHER share falls from 16 % to 1 % as n grows. **Identification (PROVED lemmas + CERTIFIED counts; descriptive):**
almost every small-prime translation overlap of G_d(n) is an explicit ideal identity between natural representatives —
an e-side identity (DL), an A-side identity inside a c-fibre (Lemma DL′) or an A/B–e identity from a common divisor
lattice (Lemma Φ). These are statements about the divisors of the integers N_a = n + 4a²d and 4c²dn + 1. Whether the
remaining coincidences (OTHER) exceed chance is a calibrated question for the corrected nulls (§1.9–1.10); the
counts alone do not show that the identities *account for* the excess, only that they are present in that number.

### 1.6b In-sample comparison of the unexplained overlaps (pre-registered before the run; descriptive — see the verdict)
PSF over-corrects (§1.5); a null-free check: for each n, call an ordered pair (g, g′) of good classes *explained* if some
natural representatives R of g, R′ of g′ divide one another as ideals (R | R′ or R′ | R, signed prime-ideal exponents;
the 𝔡-part equal) — then g′ − g is the class of the integral ideal R′/R (or its inverse). O_u(t) := number of unexplained
pairs with g′ − g = t. Control translations T_c(n) := all t of order > 2 in the principal genus other than the
translation-prime classes ±t₁, ±t₂, ±t₃ of L1/L3; λ(n) := mean of O_u over T_c(n) (chance rate of unexplained
coincidences). Statistics: U1 = O_u(t₁) against λ, U3 = Σ_{i≤3} O_u(t_i) against 3λ; z = Σ_n (obs − exp)/√Σ_n exp
(Poisson). Windows: d = 1 F3, F4, G2, G3; d = 2 F3′, G1, G2; d = 3 F2, F3′ (the PSF windows with power).
**K-OTHER:** |z| < 3 for U1 and U3 on every window and pooled |z| < 4 per d ⟹ no class-level structure at the small
split-prime translations beyond explicit ideal identities between natural representatives. **RESIDUAL-3:** z ≥ 3 on ≥ 2
windows of one d, or pooled z ≥ 4 ⟹ a genuine class-level effect remains → report and hunt.

**Result of §1.6b (CERTIFIED counts; `i1_other_v2.txt`, `i1_other_small_v2.txt` — rerun after the review with the
registered "equal 𝔡-part" rule; the first run had let a representative without 𝔡 divide one with 𝔡, which changed only the
"explained" counts for d ≥ 2, e.g. 1 896 → 1 254 on d = 2 F3′, and the expectations by < 1.5 %).** Unexplained overlaps at
the translation primes are far *below* the in-sample rate:

| d | window | ordered pairs (explained) | U1 obs vs λ (z) | U3 obs vs 3λ (z) | post hoc, small-prime controls: U1 (z), U3 (z) |
|---|---|---|---|---|---|
| 1 | F3 | 48 726 (7 874) | 18 vs 88.3 (−7.5) | 93 vs 265.0 (−10.6) | 18 vs 68.6 (−6.1), 93 vs 205.7 (−7.9) |
| 1 | F4 | 65 390 (8 442) | 2 vs 54.7 (−7.1) | 30 vs 164.1 (−10.5) | 2 vs 36.0 (−5.7), 30 vs 108.0 (−7.5) |
| 1 | G2 | 50 874 (7 884) | 17 vs 67.2 (−6.1) | 63 vs 201.7 (−9.8) | 17 vs 46.7 (−4.4), 63 vs 140.2 (−6.5) |
| 1 | G3 | 38 014 (4 668) | 4 vs 23.9 (−4.1) | 10 vs 71.6 (−7.3) | 4 vs 16.2 (−3.0), 10 vs 48.4 (−5.5) |
| 2 | F3′ / G1 / G2 | 23 142 / 41 860 / 45 696 (1 254 / 2 642 / 2 650) | z −4.7 / −6.4 / −4.3 | z −6.6 / −9.4 / −7.1 | z −3.9 / −5.7 / −3.2; −5.2 / −8.0 / −5.2 |
| 3 | F2 / F3′ | 7 552 / 7 002 (412 / 396) | z −4.1 / −2.0 | z −7.2 / −4.6 | z −3.4 / −1.1; −6.0 / −3.3 |

**Registered verdict:** RESIDUAL-3 does not fire (no positive z anywhere); K-OTHER fails formally, in the *negative*
direction — **unresolved**, not a kill. The Poisson z ignores the dependence of overlap counts (inversion symmetry, shared
classes), so these z are descriptive. The deficit is what Lemma FR predicts: a coincidence g′ = g + [𝔏] with N(R)N(R′)ℓ < dn must be a rational ideal
identity, so unexplained coincidences at small translations need both classes outside the free region, while the
registered controls (all translations of order > 2) are mostly classes of large minimal norm, where FR excludes much less.
The post hoc control by the next 20 split primes (norm closer to ℓ₀, still larger) reduces but does not remove the deficit,
as expected from the ℓ-dependence of the free region (the control design was not norm-matched — a flaw of the
registration exposed by its outcome). **Reading:** in this descriptive comparison the small-prime translations carry *fewer* unexplained coincidences than
the in-sample rates, never more; no positive excess was detected (this is not a calibrated proof of absence).

**Remark V (no coordinate-wise Vieta moves for Type II at fixed n; PROVED, scoped).** Eliminating e, Type II at fixed n is
cn = 4abcd − a − b, which has degree 1 in each of a, b, c, d. A Vieta root swap in one of these coordinates needs degree 2
in it, so none exists (this does not exclude non-linear reparametrisations or simultaneous moves); every
two-variable slice is a hyperbola xy = N — fix (c, d): (4acd − 1)(4bcd − 1) = 4c²dn + 1 (Lemma DL′); fix (a, d):
A·e = N_a (Lemma Φ); fix (a, c): b·(4acd − 1) = a + cn; fix (a, b): c·e = a + b — whose only symmetry is the swap of the
two factors (CS, resp. a ↔ b) and whose "moves" are re-factorisations (DL, DL′). The Vieta/descent machinery of
`Z69_TWIST.md` §4 lives on Type I (quadratic in a, b) and moves n. Type I classes, for the record, are classes of the
ideals (f, 2ad + √−d), f = 4acd − p | 4a²d + 1, in the *fixed* group Cl(−4d) — no p-dependent class group is involved.
The (★) line is the c = 1 slice of Lemma DL′ with d = C: (4uC − 1)(4BC − 1) = 4Cp + 1.

### 1.7 Is any of it generative? No forcing mechanism established — a reformulation, not a no-go theorem
**Proposition NG (a reformulation; PROVED, but it is not an obstruction).** Let Σ be the set of partial maps on pairs (a, M) with M | N_a generated by: multiplication or
division of M by a divisor of N_a (Lemma Φ; DL), complement M ↦ N_a/M (CS), moving a factor between A and B in a c-fibre
(DL′), a ↔ b, and transport along free-region identities (FR). (i) Every element of Σ maps (a, M) to some (a′, M′) with
M′ | N_{a′}, and the class changes by the class of an ideal dividing 𝔅_a, 𝔅_{a′} or 1 + 2c√−dn. (ii) The image is a good
pair iff M′ ≡ −1 (mod 4a′d). (iii) Under the hypotheses of §1.6 (gcd(n, d) = 1, gcd(a, n) = 1, so gcd(N_a, 4ad) = 1) the residues R_a := {M mod 4ad :
M | N_a} are closed under M ↦ nM⁻¹ (complement) and under products of divisors whose product divides N_a (without these
hypotheses the complement can leave the unit residues: n = 9, a = 3, d = 1); G_d(n) ≠ ∅ ⟺ −1 ∈ R_a for some a. So exhibiting a good
class by these operations *is* exhibiting −1 ∈ R_a — the original divisor event (the operations may start anywhere, e.g. at
n = 73, a = 1, N_1 = 77: 1 ↦ 7 ≡ −1 (mod 4) is a good divisor; nothing forces such a step). At every n with G_d(n) = ∅ they
produce nothing — tautologically; in particular at odd squares, where every M | m² + 4a²d with gcd(M, 2dm) = 1 has
χ_{−4d}(M) = +1 while χ_{−4d}(−1) = −1 (good A are automatically prime to 2dm), and, for d = 1, at the primes 37, 1621, 3361.
*Proof.* (i)–(ii) are the statements of Lemmas Φ, DL′, FR and §1.1; (iii) N_a ≡ n (mod 4ad). The square case: every prime
q | m² + 4a²d with q ∤ 2dm has (−d/q) = 1. ∎ NG is a reformulation, not a theorem that these operations *cannot* be part
of a forcing argument; "transport along FR identities" is a relation between classes, not an effective map. What the
lane establishes is only that no forcing mechanism was found among them.
**Where primality must enter (Assessment).** At a prime p, divisors of N_a can contain primes q with (−d/q) = −1 =
(p/q) — the genus character attached to p makes the coset {χ_{−4d} = −1} available. A generative mechanism would have to
produce, from data present for every p, an M | N_a in the class −1 mod 4ad. For pairs of small natural representatives
(norm product below dn) the class group adds no relation beyond ideal identities (Lemma FR, Cor. FR′); SR bounds the least
natural norm only by √(d(2n + e)), so this "free region" covers most, not all, of the relevant pairs (Assessment, based on
the counts of §1.6). The always-present data (the principal relations φ_a(N_a) = T_d for
every a, the ambiguous classes, the classes of small split primes) generate only the divisor monoids of the N_a and
4c²dn + 1, not a residue class inside them. The J-exclusion (Corollary J) is the only "negative" class-level law found;
it constrains where good classes sit but forces nothing.

### 1.8 Verdict for item 1 (revised after the internal review; see §1.10 for the corrected calibrated runs)
**Narrowed, descriptively; not closed.** PROVED: Lemma Φ (a-fibre divisor lattice; contains DL, CS, FIB), Lemma DL′ (c-fibre
lattice), Lemma SR (bound for the least natural norm), Lemma FR and Cor. FR′ (free region; injectivity on primitive
ideals), Corollary J, Remark V (scoped). CERTIFIED: the corrected FIX-CS / FIX-ALL runs, the explicit decomposition, the
J-check. EVIDENCE: the d = 1 (and n ≈ 3·10⁶, d = 3) residual beyond DL + CS is real; against the null that keeps every
fibre relation and every ideal identity no positive residual is detected for d = 1, 2, 3; at n ≈ 4·10⁶ (d = 1) 216 of 218
L1 overlaps are explicit ideal identities. Unresolved: negative deviations against FIX-ALL (d = 1 pooled L3 −6.2), mostly
attributable to the null (ALLF diagnostic). Proposition NG is a reformulation: **no forcing mechanism was established**
— none of the operations supplies the divisor event. Not a HOT LEAD.

### 1.9 Internal review round 1 — the nulls were wrong; corrected nulls (pre-registered here, before any corrected run beyond a 3-prime smoke test)
The hostile review (§8) found two FATAL implementation errors: **PSC** imposed CS by overwriting classes along a BFS tree,
which breaks the prime-factorisation (DL) identities of the overwritten ideals (1 468 directed DL violations in four
replicates per prime on F1, d = 1, 2, 3) and drops CS self-loops (A = e, 2x = T_d); **PSF** skipped fibre rows without a ±1
coefficient (e.g. n = 25169, a = 3: N_a = 5·71², relation [𝔔₅] + 2[𝔔₇₁] = 0 left unenforced; 23 violated equations). All
PSC and PSF *calibrated* conclusions of §§1.3–1.5 are therefore **withdrawn** (their tables are kept as a record of what was
run). Corrected nulls (`scripts/z70_class_nullfix.py`): the variables are the classes x_q of the prime ideals over all
primes of the good norms and of the imposed fibres; every ideal class is computed multiplicatively (so every ideal
identity — DL, DL′, REP-ID — holds in every replicate by construction); imposed relations Σ k_q x_q = T_d (one per
imposed fibre) are solved by repeated Gauss–Jordan passes with ±1 pivots; rows left with only non-unit coefficients have
all their variables frozen at the real classes (so they hold); free variables are swapped (genus- and size-matched, as
before) or, above the largest good prime, uniform in their genus coset; **every imposed original equation is asserted
in every replicate**. Mode **FIX-CS** imposes the fibres that contain a CS solution (4ad | n − 1) — this is the
registered PSC hypothesis "DL and CS exactly"; mode **FIX-ALL** imposes every active fibre — the registered PSF
hypothesis. Power is reported per statistic as the number of n with null variance > 0 (and the exact summed excess and
variance are printed, replacing the rounded pooling of `z70_class_pool.py`). Smoke test (excluded from the outcome):
n = 24001, 25169 (d = 1) and 24481 (d = 2), the review's counterexamples — all assertions pass.
**Registered (before the runs):** R = 200; windows: d = 1 F1–F4, G1–G3 and new H1 = [3000000, 3003000), H2 = [6000000,
6002000); d = 2 F1, F2, F3′, G1, G2 and H1 = [3000000, 3006000); d = 3 F1, F2, F3′ and H1 = [3000000, 3010000); d = 5, 7 F1, F2,
F3′ (FIX-CS only). Statistics Mx, Ex, L1, L3 (controls C0 for d = 1, A2 for d > 1).
* FIX-CS: outcomes K-RES / RESIDUAL exactly as in §1.2 (per window |Z| < 3; RESIDUAL = Z ≥ 3 on ≥ 2 windows of one d or
  pooled Z ≥ 4), evaluated on all listed windows.
* FIX-ALL: **K-FIB** = every |Z| < 3 on every window and pooled |Z| < 4 per d; **RESIDUAL-2** = Z ≥ 3 on ≥ 2 windows or
  pooled Z ≥ 4 (positive); a pooled Z ≤ −4 is reported as **unresolved (negative)**. A window counts for a statistic
  only if at least 10 of its n have null variance > 0 for it (else "no power" for that statistic).
* validity: controls |Z| < 3 against both modes (they are imposed).

### 1.10 Results with the corrected nulls (CERTIFIED computations; `data/z70/class/i1_FIX*.txt`; registered in §1.9)
Per-window Z (one rounding, from the per-n lines); pooled = Σ excess / √Σ var over the listed windows. The §1.9 smoke-test
primes (24001, 25169 for d = 1; 24481 for d = 2) lie in window F1 and were — contrary to §1.9 — included in the first
aggregates; the numbers below **exclude** them (`scripts/z70_class_reagg.py`; effect: FIX-CS d = 1 F1 L1 +3.6 → +3.3, the
other entries unchanged or changed by ≤ 0.3). Power (number of n with null variance > 0 per statistic) is printed in the
data files; for d = 1–3 it is 10–140 per window and statistic, for d = 5, 7 only 2–46.

**FIX-CS (DL + CS exact, all ideal identities among e-ideals exact):**

| d | windows (n analysed) | Z_Mx | Z_Ex | Z_L1 | Z_L3 | control | pooled (Mx, Ex, L1, L3; control) |
|---|---|---|---|---|---|---|---|
| 1 | F1 F2 F3 F4 G1 G2 G3 H1 H2 (139 77 61 47 59 54 21 54 30) | +3.4 +4.2 +6.0 +4.9 +4.0 +6.2 +10.2 +3.9 +5.7 | +2.5 +1.9 +3.1 +3.3 +1.7 +3.2 +6.0 +0.6 +2.4 | **+3.3 +5.0 +7.0 +7.6 +6.8 +9.3 +9.8 +6.7 +6.9** | +2.1 +2.7 +5.9 +6.6 +2.5 +6.1 +8.9 +4.7 +5.9 | C0 −2.7 −0.2 +0.9 +0.7 −0.6 −0.2 +0.8 +2.5 +2.4 | +14.9, +7.9, **+18.7**, +13.2; C0 +0.4 |
| 2 | F1 F2 F3′ G1 G2 H1 (128 156 78 181 108 104) | +2.0 +1.9 +3.3 +4.5 +3.6 +1.9 | +2.3 +2.0 +4.2 +4.0 +8.1 +2.3 | −0.6 −0.3 −1.0 −1.1 +0.2 −0.9 | +0.6 −1.1 −0.0 +0.2 +2.1 −0.3 | A2 +0.2 −0.8 +1.1 **+3.3 +4.2 +3.4** | +7.2, +10.0, −1.5, +0.5; A2 +4.8 |
| 3 | F1 F2 F3′ H1 (120 147 74 169) | +1.2 +1.1 +1.8 **+4.9** | +1.0 +2.0 +1.6 **+4.4** | −0.0 −0.5 −0.7 +1.3 | −0.2 −1.1 −1.2 +2.6 | A2 −0.4 −0.8 −0.1 +0.8 | **+4.9, +5.2**, +0.3, +0.3; A2 −0.2 |
| 5 | F1 F2 F3′ (96 129 70) | +1.7 +1.0 +0.8 | +1.1 +0.4 +1.1 | −0.4 +1.4 −0.9 | −0.0 +0.6 +2.0 | A2 −0.4 −0.6 −0.8 | +1.9, +1.3, +0.2, +1.3 |
| 7 | F1 F2 F3′ (70 110 58) | −0.6 +1.9 +1.5 | −0.7 +2.4 +0.7 | −0.2 +1.2 −0.3 | −1.0 +0.4 +0.3 | A2 −0.2 −0.2 −0.3 | +2.0, +2.0, +1.0, +0.1 |

Hard list, d = 3, full 35-prime list (z69 used the sub-list below 10⁵ for d = 3; the full list was added after review
round 1): 18 analysed, all |Z| ≤ 1.5. z69's own windows (the §1.2 replication) were rerun with both corrected nulls after
review round 2 (§1.11).
**Registered verdicts:** d = 1 **RESIDUAL** (L1 ≥ 3 on all nine windows); d = 3 **RESIDUAL** by the pooled clause (Ex +5.2,
Mx +4.9), driven by the new window H1 = [3·10⁶, 3.01·10⁶) — on F1–F3′ alone every |Z| < 3, which is what the withdrawn PSC
run saw; the z69 d = 3 energy residual is therefore **not** explained by DL + CS at larger n (correcting §1.3); d = 2: the
positive control A2 fails (|Z| ≥ 3 on G1, G2, H1), so by the validity rule the d = 2 FIX-CS runs are **not interpreted**
— the reason is CERTIFIED (`scripts/z70_class_a2check.py`, `i1_a2check.txt`, post hoc; independently reproduced by the
round-2 reviewer on G1): every ordered pair (g, g + T_d) of good classes is an ideal identity between natural
representatives, 𝔡·conj 𝔈₁ = 𝔡·𝔄₂ (A₂ = e₁, a₂ ≡ b₁ (mod e₁)) or its B-side mirror; with a₂ = b₁ this is Lemma CS, with
a₂ ≠ b₁ a cross-fibre identity that FIX-CS does not impose: d = 2 G1: 946 pairs = 898 CS + 48 cross-fibre + 0 other (FIX-CS
null 917.5); G2: 748 = 708 + 40 + 0; H1: 630 = 598 + 32 + 0; d = 3 H1: 356 = 352 + 4 + 0. d = 5, 7 **K-RES** (low power).

**FIX-ALL (every active-fibre relation exact):**

| d | windows | Z_Mx | Z_Ex | Z_L1 | Z_L3 | control | pooled (Mx, Ex, L1, L3; control) |
|---|---|---|---|---|---|---|---|
| 1 | F1 F2 F3 F4 G1 G2 G3 H1 H2 | −0.6 +0.5 +1.3 −1.0 −0.4 −0.5 +1.4 −1.6 −0.4 | +0.5 +1.5 +2.2 +1.0 +0.7 +0.2 −1.0 −0.6 −0.5 | −2.7 −1.6 −0.4 −2.1 −1.2 −0.8 −0.6 −3.0 −1.1 | −1.2 −1.2 −1.3 −2.7 −1.3 **−3.0** −2.9 **−4.0** −1.6 | C0 −2.3 −2.2 −2.3 −1.8 −2.4 −2.2 −1.4 −2.1 −1.8 | −0.6, +0.6, **−4.6**, **−6.2**; C0 **−6.2** |
| 2 | F1 F2 F3′ G1 G2 H1 | +0.4 −1.5 −0.1 −0.5 −0.8 −1.8 | +0.3 −0.5 −1.3 −0.4 +1.0 −1.6 | +1.2 +1.1 −0.8 −0.4 +0.9 −1.6 | +2.9 −0.8 −1.5 −0.7 −0.4 −1.6 | A2 −0.6 −1.0 −0.5 −1.0 −1.0 −0.7 | −2.0, −1.2, +0.2, −1.1; A2 −2.0 |
| 3 | F1 F2 F3′ H1 | +0.9 +0.8 −0.3 +0.5 | +1.2 +0.9 −0.7 −0.2 | +0.8 −1.4 +0.3 −0.3 | +0.7 **−3.1** −1.4 −0.7 | A2 −0.4 −0.4 −0.1 −0.4 | +1.0, −0.0, −0.6, −2.6; A2 −0.7 |

**Registered verdicts:** no positive Z ≥ 3 anywhere — **RESIDUAL-2 does not fire** for d = 1, 2, 3; d = 2 meets **K-FIB**;
d = 1 and d = 3 fail K-FIB only in the negative direction (d = 1 pooled L1 −4.6, L3 −6.2: **unresolved (negative)**; d = 3
one window L3 −3.1). The validity rule ("controls |Z| < 3") was applied per window, where it passes; the *pooled* d = 1
control C0 = −6.2 fails it — a warning that FIX-ALL over-produces collisions, so the pooled d = 1 FIX-ALL readings are to be
taken with caution. Post hoc diagnostic (mode ALLF: never pivot on a prime of a good norm, freeze instead;
`i1_FIXALLF_d1_*.txt`, two windows only): d = 1 F3 all |Z| ≤ 1.2 (FIX-ALL: L3 −1.35, C0 −2.29); H1 L1 −2.6, L3 −2.4, C0 −1.2
(FIX-ALL: −3.0, −4.0, −2.1). ALLF also freezes 371 variables on H1 (varied good ideals 272/2234 against 646/2234), so it is
a *confounded* diagnostic: the shrinking deficit is consistent with — not a demonstration of — the explanation that
pivot-solved classes of small good ideals lose the free-region protection (Lemma FR, Cor. FR′) of the real small ideals.
A second post hoc diagnostic (final pass; `Z70_DIAG=1`, `i1_FIXALL_d1_{G2,H1}_diag.txt`, same seed, registered outputs
reproduced identically) splits ideal-pair coincidences by whether an ideal involves a pivot-solved or uniformly drawn
prime class (S) or not (P): H1 — collisions S 522 vs null 532.9, P 34 vs 37.4; L3-pairs S 953 vs 1020.5, P 545 vs 581.1;
G2 — collisions S 438 vs 445.0, P 20 vs 24.5; L3-pairs S 803 vs 830.3, P 296 vs 320.8. The deficit is **not confined to
solved classes**: pairs built only from swapped/fixed/frozen primes also show ≈ 6–8 % fewer coincidences than the null. So
the artefact explanation is at best partial, and the negative deviations remain **unresolved** — possibly a genuine
anti-coincidence of good classes at small-prime translations beyond ideal identities (not a forcing mechanism either
way).
**Summary of the calibrated evidence:** beyond DL + CS there is a positive residual for d = 1 and, at n ≈ 3·10⁶, for d = 3
(d = 2: not interpreted, control fails); against the null that keeps every relation of Lemma Φ in every active fibre and
every ideal identity (incl. Lemma DL′) **no positive excess is detected** in any window for d = 1, 2, 3; the remaining
deviations are negative (fewer coincidences than that null) and unresolved.

### 1.11 z69's windows with the corrected nulls (the §1.2 replication; run after review round 2)
`i1_FIXCS_*_z69w*.txt`, `i1_FIXALL_*_z69w*.txt` (R = 200). FIX-CS: d = 1 [20000, 24000) / [200000, 202000) / [10⁶, 10⁶ + 1000):
L1 +4.6 / +3.2 / +3.9, Mx +2.8 / +3.3 / +2.8, Ex +2.4 / +2.1 / +3.2, L3 +2.3 / +3.4 / +2.7 (C0 −2.2 / −0.8 / −1.9); d = 3
[20000, 24000): Ex +1.8, others ≤ 0.3 in absolute value (A2 −1.2); d = 5: all |Z| ≤ 2.0. FIX-ALL: every |Z| ≤ 1.9 on all five.
So z69's d = 1 excess is reproduced against DL + CS and disappears against the full fibre structure; z69's d = 3 window is
too small to show the residual that appears at n ≈ 3·10⁶.

### 1.12 Extension windows (post hoc, after review round 2; not registered)
`i1_FIX{CS,ALL}_d{3,5,7}_X1.txt`, R = 200: d = 3 [6·10⁶, 6.01·10⁶) (160 n): FIX-CS Mx +4.2, Ex +4.1, L1 +1.1, L3 +0.1 — the d = 3
residual beyond DL + CS replicates on a second large window; FIX-ALL Mx +0.4, Ex −0.7, L1 +0.3, L3 −0.5. d = 5
[3·10⁶, 3.01·10⁶) (155 n, power 50–76 n per statistic): FIX-CS Mx +1.4, Ex +2.0, L1 +1.2, L3 −0.4; FIX-ALL all |Z| ≤ 1.0.
d = 7 [3·10⁶, 3.01·10⁶) (136 n): FIX-CS all |Z| ≤ 1.0; FIX-ALL all |Z| ≤ 1.4.

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
**2c (added before running; same design for (★) witnesses).** For a (★) solution p = 4uBC − u − B with modulus
d = 4uC − 1 ≤ 10⁵ (exhaustive in that range, `scripts/z70_class_star.c`): representation ideal (d, 2uC + √−Cp) ↔ form
[4uC − 1, 4uC, C(u + B)] of discriminant −4Cp (the good form of Type II with c = 1); Cp ≤ 10¹³, ≤ 8 per prime; exact decoys
as in 2b (odd primes of Cp); statistics S1–S3; samples H_train, H_test, CTRL and the band sample (2 000 primes of the z69
band B, drawn with seed 7071 — the band was added to 2a/2b after the registration, as a replication with the same fixed
statistics). Signal criterion as in 2b.

### 2.4 Results (CERTIFIED computations; EVIDENCE for the readings; `data/z70/class/i2*`)
**2a (registered).** H_train / H_test vs CTRL (Welch z; `scripts/z70_class_mine2.py 2a`, `i2a_summary.txt`):

| invariant | CTRL (2 547) | H_train (438): mean, z | H_test (411): mean, z |
|---|---|---|---|
| v₂ h(−4p) (cap 6) | 2.923 | 2.998, +1.21 | 2.837, −1.34 |
| v₂ h(−8p) (cap 6) | 2.975 | 2.986, +0.18 | 2.908, −1.09 |
| 3 \| h(−4p) | 0.427 | 0.427, +0.01 | 0.406, −0.78 |
| 3 \| h(−8p) | 0.431 | 0.434, +0.11 | 0.399, −1.23 |
| h(p) = 1 | 0.770 | 0.751, −0.82 | 0.747, −0.98 |
| ρ_ℓ = log ord[𝔏] / log h(−4p) | 0.906 | 0.809, **−14.50** | 0.813, **−13.04** |

Deviation (found by the review): the implementation capped v₂ at 6, which the registration did not specify; the
registered, uncapped statistics (`scripts/z70_class_mine2a_uncapped.py`, `i2a_uncapped.txt`) are v₂h(−4p): CTRL 2.994,
H_train 3.016 (z +0.33), H_test 2.869 (z −1.79); v₂h(−8p): 3.042, 3.046 (+0.05), 2.961 (−1.12) — also null. For prime p ≡ 1 (8)
the 2-Sylow subgroups of Cl(−4p) and Cl(−8p) are cyclic (genus theory: two prime discriminant factors, 2-rank 1), so v₂h
encodes the 2-, 4- and 8-ranks the brief asks about; no separate Rédei-symbol analysis was done.
The registered signal criterion **fires for ρ_ℓ** (and for nothing else). Follow-up (post hoc, explored on H_train + CTRL,
then H_test scored once; `scripts/z70_class_mine2a_post.py`): ℓ is the least prime with (−p/ℓ) = 1, and for p ≡ 1 (8)
[𝔏] lies in the principal genus iff ℓ ≡ 1 (mod 4), which caps its 2-part below that of h. The share of ℓ ≡ 1 (4) is
0.275 (CTRL), 0.895 (H_train), 0.900 (H_test) — the pseudo-square profile of the hard primes ((p/3) = +1 makes 3 inert,
etc.). **Within the strata the groups agree**: ℓ ≡ 1 (4): ρ = 0.798 / 0.794 / 0.796, v₂h − v₂ord = 1.66 / 1.67 / 1.64,
odd-part ratio 0.934 / 0.933 / 0.932; ℓ ≡ 3 (4): ρ = 0.948 / 0.936 / 0.966 (CTRL / H_train / H_test). Disjoint band
(added after registration; 2 000 primes of band B, seed 7071, W(p) by `z69_mine_allwit.c`; `i2a_band.txt`): corr(log W, ρ_ℓ)
= +0.141 (z = +6.35) overall, −0.009 and +0.006 within the two strata; all other invariants |z| ≤ 1.7 overall and
within strata. (Review recomputation of within-stratum z, H_train / H_test vs CTRL: ℓ ≡ 1 (4) −0.50 / −0.18; ℓ ≡ 3 (4) −0.61 / +1.61.)
*Reading:* the ρ_ℓ "signal" is carried by the genus position of the least split prime, i.e. local (quadratic-character)
data of p already known to separate the hard primes (Z69_MINE §3.1(b)); **no residual was detected within these strata**.
(The H_test stratified table was produced once, after the train table and with the same script, in the same session;
the commit history alone cannot certify "scored once".)
**2b (registered; U₇ representation ideals vs exact decoys)** — real − decoy, cluster-by-prime z:

| sample | primes / witnesses (decoy failures) | S1 = log ord / log h | S2 = v₂ ord | S3 = 1[3 \| ord] |
|---|---|---|---|---|
| H_train | 436 / 2 984 (407) | +0.0007 ± 0.0021 (+0.34) | +0.0040 ± 0.0032 (+1.26) | +0.0075 ± 0.0067 (+1.12) |
| H_test | 406 / 2 759 (409) | +0.0001 ± 0.0023 (+0.05) | −0.0036 ± 0.0042 (−0.87) | −0.0074 ± 0.0077 (−0.97) |
| CTRL | 2 541 / 17 451 (2 875) | +0.0012 ± 0.0008 (+1.48) | −0.0016 ± 0.0017 (−0.93) | −0.0021 ± 0.0028 (−0.74) |
| band (added) | 2 000 / 14 153 (1 847) | −0.0002 ± 0.0007 (−0.33) | +0.0012 ± 0.0015 (+0.83) | −0.0012 ± 0.0031 (−0.38) |

**2c ((★) representation ideals, d = 4uC − 1 ≤ 10⁵; registered before running):**

| sample | primes / witnesses (decoy failures) | S1 | S2 | S3 |
|---|---|---|---|---|
| H_train | 428 / 1 927 (554) | −0.0035 ± 0.0032 (−1.11) | +0.0026 ± 0.0033 (+0.77) | −0.0118 ± 0.0090 (−1.31) |
| H_test | 400 / 1 876 (489) | −0.0005 ± 0.0034 (−0.16) | −0.0071 ± 0.0075 (−0.95) | −0.0081 ± 0.0108 (−0.75) |
| CTRL | 2 540 / 14 229 (6 010) | +0.0018 ± 0.0010 (+1.79) | +0.0011 ± 0.0015 (+0.71) | +0.0052 ± 0.0032 (+1.63) |
| band | 2 000 / 11 095 (4 840) | +0.0003 ± 0.0009 (+0.38) | −0.0010 ± 0.0016 (−0.60) | −0.0012 ± 0.0037 (−0.33) |

No signal (all |z| < 1.8). Scope and caveats: witnesses for which 4 000 random draws found no decoy are dropped (12 % of
attempted witnesses in 2b, 21–30 % in 2c — mostly the smallest moduli, where the ±5 % window contains few integers of the
right residue and symbols); at most 8 witnesses per prime; yp ≤ 10¹³ resp. Cp ≤ 10¹³. Class numbers and orders come from
PARI `quadclassunit`, which is **CONDITIONAL on GRH** (the class number enters both the order computation and the
normalisation); all item-2 numbers are therefore CONDITIONAL (GRH) computations. The review re-verified all 66 474 saved
witness rows and 132 948 decoys (representation identities, roots, window, residue, coprimality, characters) and 120
sampled orders. Non-rejection, not equivalence: 2-s.e. half-widths ≈ 0.002–0.007 on
S1 (relative to a spread of ρ-values of order 0.1).
*Reading (Assessment):* by Lemma SR/FR the representation ideal of a witness is a small-norm ideal whose class is
"generic" among small-norm ideals of the same norm range and genus; the data show no trace of the class-group position of
witness ideals beyond that.
**Verdict item 2: null; one registered signal (ρ_ℓ) fired and is fully explained by the genus position of the least
split prime (local data).** Not a HOT LEAD.

## 3. Mandatory falsifier table — final

| screen | outcome | label |
|---|---|---|
| **F1 odd squares** | G_d(m²) = ∅ for all d (T1); in this memo's language: every divisor M of m² + 4a²d prime to 2dm (good A always are) has χ_{−4d}(M) = +1 while the target residue −1 has χ_{−4d} = −1 (Prop. NG); the identified structure (Φ, DL′, SR, FR, Cor. J) consists of statements about existing divisors/solutions and is vacuous at squares. The non-squareness step a generative mechanism must use is exactly the availability of divisors q \| N_a with (−d/q) = −1 (equivalently (p/q) = −1 at a prime). Item 2 statistics are about witnesses of primes (none exist at squares). | PROVED |
| **F2 numerator 8 / C-even** | Lemmas Φ, DL′, SR, FR hold for every d, in particular even d (d = 2 runs: no positive residual against FIX-ALL; the FIX-CS d = 2 runs are uninterpretable because the A2 control fails); Type II with d even is the C-even side; nothing here distinguishes C odd from C even, and nothing claims positivity. 2c includes (★) witnesses of both parities of C. | PROVED / CERTIFIED |
| **F3 composites** | The lemmas need gcd(n, d) = 1 and, for Φ, gcd(a, n) = 1; the scripts skip n where an ideal norm shares a prime with n (not the same as non-invertibility — those ideals are simply not handled). Composite (★)-zeros below 10⁵ (d = 1): 61 of 93 skipped, 8 with \|G\| < 2, 24 analysed: all \|Z\| ≤ 1.7 against FIX-CS and FIX-ALL (`i1_FIX*_d1_compzeros.txt`); decomposition L1: 9 EID / 0 REP-ID / 13 OTHER (22 pairs). A symmetry of existing solutions cannot separate primes from composite zeros. | PROVED / CERTIFIED |
| **F4 known zeros** | Hard list (d = 1: the 14 (★)-zero primes, the 26 𝔊*-zero primes below 10⁶ and 2521, 3361, 21841, 76441 — 35 distinct, 32 with \|G\| ≥ 2): all \|Z\| ≤ 1.8 against FIX-CS and FIX-ALL; d = 3, full list: 18 analysed, all \|Z\| ≤ 1.5 (FIX-CS). H_train/H_test (incl. 2521, 3361, 21841, 76441) in item 2: no class-group difference beyond the local ρ_ℓ effect. | CERTIFIED |

## 4. Verdict
**Narrowed descriptively, not closed; no forcing mechanism established; not a HOT LEAD. ES is OPEN.**
* Item 1. With corrected nulls (§1.9–1.10; the first PSC/PSF implementations were wrong and their calibrated readings are
  withdrawn): the I17 residual beyond DL + CS is real for d = 1 (pooled L1 Z = +18.8 over nine windows), present at
  n ≈ 3·10⁶ and 6·10⁶ for d = 3 (pooled Ex +5.2 over the registered windows; replicated at 6·10⁶, §1.12; absent on the
  three smaller windows), not interpretable for d = 2 (control fails),
  and not seen for d = 5, 7 (low power). Against a null that keeps every relation of Lemma Φ in every active fibre and
  every ideal identity (incl. the new Lemma DL′), no positive excess is detected for d = 1, 2, 3; what remains is a
  negative deviation (fewer coincidences than the null; pooled d = 1 control also negative), unresolved — partly a null
  artefact (ALLF), but present also among pairs without solved classes (DIAG): possibly a genuine anti-coincidence. Descriptively, almost all
  small-prime translation overlaps are explicit ideal identities between small natural representatives (Lemmas Φ, DL′; at
  n ≈ 4·10⁶, 216/218), and Lemma FR / Cor. FR′ explain why small classes cannot carry other coincidences; Corollary J is
  the one class-level exclusion found. No operation found produces a good class without exhibiting the divisor event
  (Prop. NG, a reformulation — not a no-go theorem).
* Item 2 (CONDITIONAL on GRH for the PARI class groups). 2- and 3-parts of h(−4p), h(−8p) and h(p) = 1 do not separate the
  hard primes (uncapped registered statistics too); the order of the least split prime's class does (z −14.5 / −13.0),
  but the effect sits in the genus of that prime (ℓ mod 4) and no within-stratum residual was detected (H_train,
  H_test, band); orders of U₇ and (★) representation-ideal classes match exact decoys on H_train, H_test, CTRL and a
  disjoint band.
* What this buys: a calibrated, corrected account of I17 (structure = divisor lattices of n + 4a²d and 4c²dn + 1 seen
  through a class map that is injective on small primitive ideals), two short new lemmas (DL′, Cor. J) and the
  free-region principle — and the negative information that, in these tests, class-group *positions* of good forms and
  witness ideals showed no detected signal beyond divisor identities and local data.

**Hard screens (FRONTIER §4).** T1 squares: passes (vacuous; NG names the genus step). 8/131: no positivity claim.
Tied modulus: the identified structure lives inside the tied divisor event (it presupposes M ≡ −1 (mod 4ad)); it does not
loosen the tie. Fixed p: all statements are per n, none produces a solution.

## 5. Proposed FRONTIER §7 text (do not edit FRONTIER here)
"z70 CLASS (`Z70_CLASS.md`; narrowed descriptively). I17 rerun with corrected symmetry-preserving nulls (prime-class
variables, fibre relations solved exactly, all ideal identities kept): residual beyond z69's DL + CS is real for d = 1
(pooled Z_L1 +18.8) and appears for d = 3 at n ≈ 3·10⁶; against the null keeping all relations of the fibres n + 4a²d
no positive excess detected (d = 1, 2, 3); negative deviations (fewer coincidences than the null) unresolved — partly a
null artefact, partly possibly a genuine anti-coincidence. PROVED: Lemma Φ
(divisors M of N_a = n + 4a²d ↦ classes is additive on products MM′ | N_a, with φ_a(N_a) = T_d; contains DL, CS), Lemma DL′ ((4acd − 1)(4bcd − 1) = 4c²dn + 1,
c-fibre lattice), Lemma SR (least natural norm ≤ √(d(2n + e))), Lemma FR (class relations with norm product < dn are
rational ideal identities; primitive small ideals lie in distinct classes), Cor. J (g, g + J ∈ G₁ ⟹ 2m(g)m(g+J) ≥ n).
CERTIFIED: at n ≈ 4·10⁶ (d = 1) 216 of 218 L1 overlaps are explicit ideal identities. No forcing mechanism (Prop. NG is a
reformulation). MINE class-group item (GRH-conditional): h-parts, h(p) null; least-split-prime class order separates hard
primes only through its genus; U₇ and (★) representation-ideal class orders match exact decoys (H_train/H_test/CTRL/band)."

## 6. Bottom line
The good-form class sets G_d(p) have translation structure beyond DL and CS (d = 1; d = 3 at n ≈ 3·10⁶). Descriptively,
the overlaps at small-prime translations are almost always explicit identities among small natural ideal representatives
(norms 4acd − 1, 4bcd − 1, de) coming from the factorisations of n + 4a²d and 4c²dn + 1 (Lemmas Φ, DL′); for pairs of small
primitive ideals the class group adds no further relation (Lemma FR, Cor. FR′). Against a null that keeps all these
relations no positive excess is detected (corrected runs; the first implementation of the nulls was wrong and is
withdrawn); the negative deviations left (fewer coincidences than that null, also among pairs not touched by the null's
solved classes) are unresolved. The one class-level law found is an exclusion (Corollary J). No
forcing mechanism was established: exhibiting a good class by these operations is exhibiting a divisor M ≡ −1 (mod 4ad)
of some N_a, the B2 event. Item 2 is null apart from a genus effect
of the least split prime (no within-stratum residual detected). Not a HOT LEAD. ES is OPEN.

## 7. Reproduction
Corrected nulls (the valid calibrated runs): `bash scripts/z70_class_run2.sh P|Q` (FIX-CS / FIX-ALL, §1.9), single runs
`uv run --with sympy --with numpy python scripts/z70_class_nullfix.py CS|ALL|ALLF d R seed range P0 P1` (or `list n …`),
pooled Z from the exact sums: `python3 scripts/z70_class_pool2.py FILES`.
Withdrawn first implementations (record only): `scripts/z70_class_run1.sh A|B|C|D` (PSC, §1.2), `… E|F` (PSF, §1.4); single runs:
`uv run --with sympy --with numpy python scripts/z70_class_null.py PSC d R seed range P0 P1`,
`… scripts/z70_class_psf.py d R seed range P0 P1` (`Z70_MATCH2=1` for the 2-adic diagnostic),
`… scripts/z70_class_repid.py d range P0 P1`, `… scripts/z70_class_jcheck.py P0 P1`, `… scripts/z70_class_a2check.py d range P0 P1`,
`… scripts/z70_class_rfcheck.py d P0 P1`, `… scripts/z70_class_reagg.py FILE [excluded n …]`,
`… scripts/z70_class_other.py d range P0 P1` (`Z70_SMALLCTL=1` for the post hoc control),
`python3 scripts/z70_class_pool.py FILES` (pooled Z from rounded output — superseded by pool2), `… scripts/z70_class_core.py`
(selftest of the dictionary).
Item 2: `uv run --with cypari2 --with sympy python scripts/z70_class_mine2.py 2a data/z70/class/i2a`,
`… 2b SET data/z70/class/i2b_SET.txt`, `… 2c SET data/z70/class/i2c_SET.txt data/z70/class/star_d1e5.txt.gz`,
`… scripts/z70_class_mine2a_post.py CTRL H_train` / `H_test`, `… scripts/z70_class_mine2a_band.py`,
`… scripts/z70_class_mine2a_uncapped.py` (registered uncapped v₂ statistics); band witnesses
`gcc -O2 scripts/z69_mine_allwit.c -o allwit` on the 2 000 band primes (seed 7071 sample of `raw_r2_gen2_band.jsonl.gz`);
(★) solutions `gcc -O2 scripts/z70_class_star.c -o star; ./star 100000 < primes`. All runs: `ulimit -v 6000000`,
`timeout` ≤ 1800, ≤ 2 compute processes (two exceptions: a < 3 s PARI job, and the < 1 min `z70_class_rfcheck.py` run, each
ran briefly as a third process). Run time of
everything: about 1.5 h.

## 8. Review log
**Internal hostile review, round 1** (deep-mode reviewer subagent via the `review` tool on `ac1d9f8a9..ea81a6405`; reviewer
model reported as `openai/gpt-6-astra`; no provider / auth / quota error). It verified the commit order of every
pre-registration, re-ran a PSC window with another seed, independently rebuilt the F1 REP-ID decomposition (exact match)
and the first J-check window, and re-verified all 66 474 item-2 witness rows, 132 948 decoys and 120 orders. Findings and
fixes:
* **FATAL 1 — PSC broke DL identities and CS self-loops** (BFS overwrite; e.g. n = 24001; n = 24481, d = 2, A = e = 159).
  Fixed: PSC/PSF calibrated conclusions withdrawn; corrected nulls with prime-class variables, exact elimination, frozen
  non-unit rows and per-replicate assertion of every imposed equation (§1.9), pre-registered and run on every window listed
  in §1.9 (z69's replication windows were added after round 2, §1.11). Outcome changed: the d = 3 "K-RES" became RESIDUAL at n ≈ 3·10⁶; d = 2 FIX-CS is uninterpretable
  (control fails).
* **FATAL 2 — PSF skipped rows without a ±1 coefficient** (n = 25169, a = 3). Fixed as above (FIX-ALL).
* MAJOR — FR's consequences overstated ("faithful copy", "fully identified", injectivity without primitivity): FR now
  stated with its product bound, Cor. FR′ added (primitive ideals), identification wording made descriptive (§1.6).
* MAJOR — Corollary J's "no J-partner at all" was false (24 counterexample classes, e.g. n = 22129): corrected.
* MAJOR — Prop. NG is a reformulation, not a no-go; the "needs a good divisor to start" wording was false (n = 73: 1 ↦ 7):
  reworded ("no forcing mechanism established"); Remark V scoped to coordinate-wise Vieta swaps.
* MAJOR — Lemma Φ lacked gcd(n, d) = 1 (n = d = 5) and covered only coprime factors: hypotheses stated; (ii) now proved for
  all MM′ | N_a via the one-sided prime factorisation of 𝔅_a; NG's square argument restricted to divisors prime to 2dm
  (n = 9, a = 3 counterexample otherwise).
* MAJOR — deviations from the registrations: the v₂ cap at 6 in 2a (uncapped registered statistics now reported: null);
  PSF windows at 19.9 % / 19.5 % non-degenerate were "no power" (moot after withdrawal); OTHER ignored the registered
  equal-𝔡 rule (rerun; counts for d ≥ 2 changed, conclusions not); the d = 3 hard screen used z69's sub-list (full list
  now run); "38 𝔊*-zero primes below 10⁶" corrected to 26.
* MAJOR — "non-degenerate fraction" is not a power measure; OTHER's Poisson z is not justified: per-statistic counts of n
  with nonzero null variance now reported; OTHER labelled descriptive; failed kills recorded as unresolved, not kills.
* MINOR — exact pooled sums replace rounded pooling (`pool2`); REP-ID subtype labelling simplified (first identity found);
  decoy wording ("no decoy in 4 000 draws"), 2c failure fraction 21–30 %; PARI class groups labelled CONDITIONAL (GRH);
  the new run script propagates failures and writes via temporary files; the cyclic 2-Sylow (2-, 4-, 8-ranks ⊂ v₂h) stated.
Not done: a separate Rédei-symbol analysis; a fully calibrated (dependence-aware) version of the OTHER comparison; a null
that keeps free-region protection for pivot-solved classes (ALLF is a partial diagnostic).

**Internal hostile review, round 2 (delta)** (deep reviewer on `ea81a6405..b36b6f061`; reviewer model reported as
`openai/gpt-6-astra`; no provider / auth / quota error). No FATAL. It audited `z70_class_nullfix.py` (valid: ±1-pivot
Gauss–Jordan over an abelian group, repeated passes, frozen rows satisfied, frozen ∩ pivots = ∅, every imposed equation
asserted; 18 instrumented runs with extra genus / representative / CS-self-loop checks passed; FIX-CS d = 1 F1 reproduced
byte-for-byte), confirmed the §1.9 commit precedes the FIX data, re-pooled all outcomes, re-checked Lemma Φ(ii) (also in the
non-maximal order ℤ[√−39]), Cor. FR′ and NG's square argument, and reproduced the A2 decomposition (946 = 898 + 48 + 0)
independently. Findings, all applied: (1) MAJOR — the §1.9 smoke-test primes had been included in the F1 aggregates: now
excluded (`z70_class_reagg.py`; d = 1 F1 L1 +3.6 → +3.3, verdicts unchanged); (2) MAJOR — NG(iii)'s complement closure was
false without coprimality (n = 9, a = 3): hypotheses added; (3) MAJOR — surviving overclaims ("real structure for d = 2",
"no hidden class-level law", "accounted for", "every operation needs a divisor", "fully explained") reworded; (4) MAJOR —
ALLF is a confounded diagnostic (it freezes 371 variables on H1) and the pooled d = 1 FIX-ALL control fails (C0 −6.2):
"mostly a null artefact" replaced by "unresolved; consistent with a null artefact", per-window application of the validity
rule stated, pooled failure recorded as a warning; MINOR — §0 count (26, not 38) annotated, "monoid map" made precise,
single rounding of the table entries, power legend corrected, z69 windows rerun with the corrected nulls (§1.11).

