# Z70_CLASS — the I17 residual and the class-group structure of good forms (wave z70, lane CLASS): the residual is integer divisor structure seen through a class map injective on small ideals; nothing generative; not a HOT LEAD

**ES is OPEN. Nothing here proves or disproves it.** Status: final draft (all registered runs done; internal review pending). Verdict (§4): **narrowed — the I17 residual is identified as integer divisor structure (Lemmas Φ, DL′, SR, FR, Cor. J); no generative symmetry (Prop. NG); item 2 null.** Not a HOT LEAD.
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

### 1.5 Results (CERTIFIED computations; Z as registered; `data/z70/class/i1_*.txt`)
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
x² + ny²*, §7). For a ≥ 1 with gcd(a, n) = 1 put B_a := 4ad and, for M | N_a, φ_a(M) := class of [M, 4ad, dN_a/M].

**Lemma Φ (fibre homomorphism; generalises DL, CS and FIB). PROVED.** (i) [M, 4ad, dN_a/M] is primitive of discriminant
−4dn; (ii) φ_a(MM′) = φ_a(M) + φ_a(M′) whenever MM′ | N_a and gcd(M, M′) = 1; (iii) φ_a(N_a) = T_d, φ_a(1) = 0;
(iv) if a′ ≡ a (mod M) and M | N_{a′} then φ_{a′}(M) = φ_a(M).
*Proof.* (i) (4ad)² − 4M·dN_a/M = 16a²d² − 4d(n + 4a²d) = −4dn. A common prime of M and 4ad divides gcd(N_a, 4ad), which
divides gcd(n, 4ad) = gcd(n, a) = 1 (n odd, gcd(n, d) = 1). (ii) Dirichlet composition of the concordant forms
[M, B, M′·(dN_a/(MM′))] and [M′, B, M·(dN_a/(MM′))] (same middle coefficient B = 4ad, gcd(M, M′, B) = 1) is
[MM′, B, dN_a/(MM′)] (Dirichlet composition; Cox §3). (iii) [N_a, 4ad, d] ~ [d, −4ad, N_a] and (x, y) ↦ (x + 2ay, y) turns it
into [d, 0, N_a − 4a²d] = [d, 0, n]; [1, B, ·] is principal. (iv) the middle coefficients 4ad, 4a′d agree mod 2M. ∎
Reading: the good classes are G_d(n) = {φ_a(A) : a ≥ 1, A | N_a, A ≡ −1 (mod 4ad)} (§1.1), and the e-side classes are
φ_a(e) = T_d − φ_a(A). Lemma DL = (ii) with M′ = ℓ; Lemma CS = (ii)+(iii) with M′ = N_a/M; FIB (§1.4) = (ii)+(iii) with
three coprime factors. (For composite n with gcd(a, n) > 1 the statements need the usual coprimality and were not used.)

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
N = n + 4 min(a,b)²d ≤ n + 4abd = 2n + e, and e ≤ (n + 4d)/(4d − 1) (z69). ∎ CERTIFIED: the least natural norm is ≤ √(dn)
for 95 % (d = 1, n ≈ 2.7·10⁴), 97.7 % (10⁶), 98.4 % (4·10⁶) of good classes, and ≥ 96 % for d = 2, 3, 5, 7 at 2·10⁵
(`i1_repid_*.txt`, K_small/K).

**Lemma FR (free region). PROVED.** Let 𝔞, 𝔟, 𝔱 be invertible ideals of O with [𝔟] = [𝔞] + [𝔱] and
N(𝔞)N(𝔟)N(𝔱) < dn. Then 𝔟·conj(𝔞)·conj(𝔱) = xO with x ∈ ℤ_{>0} and x² = N(𝔞)N(𝔟)N(𝔱).
*Proof.* conj(𝔞) has class −[𝔞] (𝔞·conj 𝔞 = N(𝔞)O for invertible 𝔞; Cox §7), so the product is invertible and principal, = αO with
α ∈ O (it is integral), α = x + y√−dn, N(α) = x² + dny² = N(𝔞)N(𝔟)N(𝔱) < dn (norms are multiplicative on invertible
ideals), so y = 0. ∎
**Corollary J (d = 1). PROVED.** J = [2, 2, (n + 1)/2] (n ≡ 1 (4)). If g and g + J both lie in G_1(n), then
2·m(g)·m(g + J) ≥ n, where m(·) is the least norm of an odd-norm ideal in the class (in particular of a natural
representative). *Proof.* FR with 𝔱 = (2, 1 + √−n) (norm 2) would give x² = 2·(odd)·(odd), impossible. ∎
CERTIFIED (`i1_jcheck.txt`): 148 + 28 + 6 J-overlap pairs in three d = 1 windows, 0 violations; 84–90 % of good classes have
2m² < n and therefore no J-partner at all. This is the J-avoidance seen by z69 (K-I17 fired for J) and by PSC (A2 −6.65):
an arithmetic exclusion, not a norm-profile artefact.

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

At d = 1 the PSC excess on L1 (F3: 304 − 237 = 67; F4: 218 − 156 = 62) is matched by the REP-ID pairs (94; 84), and the
OTHER share falls from 16 % to 1 % as n grows. **Identification (PROVED lemmas + CERTIFIED counts):** the "translation
structure beyond the norm profile" of G_d(n) is the multiplicative structure of the norms of its small natural
representatives (divisor lattices of N_a = n + 4a²d *and* of 4c²dn + 1, Lemmas Φ, DL′), transported into Cl(−4dn) by a
class map that is injective on small ideals (Lemma FR). The residual of z69/§1.3 is not a third symmetry of the class
group: it is DL′ (the c-fibre twin of DL) plus a-fibre identities between A-side and e-side representatives — all of them
ideal identities, i.e. statements about integers, not about the group.

### 1.6b Calibrated in-sample test of the unexplained overlaps (pre-registered here, before the run)
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

**Result of §1.6b (CERTIFIED; `i1_other_*.txt`).** Unexplained overlaps at the translation primes are far *below* the
in-sample chance rate:

| d | window | ordered pairs (explained) | U1 obs vs λ (z) | U3 obs vs 3λ (z) | post hoc, small-prime controls: U1 (z), U3 (z) |
|---|---|---|---|---|---|
| 1 | F3 | 48 726 (7 874) | 18 vs 88.3 (−7.5) | 93 vs 265.0 (−10.6) | 18 vs 68.6 (−6.1), 93 vs 205.7 (−7.9) |
| 1 | F4 | 65 390 (8 442) | 2 vs 54.7 (−7.1) | 30 vs 164.1 (−10.5) | 2 vs 36.0 (−5.7), 30 vs 108.0 (−7.5) |
| 1 | G2 | 50 874 (7 884) | 17 vs 67.2 (−6.1) | 63 vs 201.7 (−9.8) | 17 vs 46.7 (−4.4), 63 vs 140.2 (−6.5) |
| 1 | G3 | 38 014 (4 668) | 4 vs 23.9 (−4.1) | 10 vs 71.6 (−7.3) | 4 vs 16.2 (−3.0), 10 vs 48.4 (−5.5) |
| 2 | F3′ / G1 / G2 | 23 142 / 41 860 / 45 696 | z −4.6 / −6.3 / −4.2 | z −6.5 / −9.2 / −7.0 | z −3.9 / −5.7 / −3.2; −5.2 / −8.0 / −5.2 |
| 3 | F2 / F3′ | 7 552 / 7 002 | z −4.1 / −2.0 | z −7.2 / −4.6 | z −3.4 / −1.1; −6.0 / −3.3 |

**Registered verdict:** RESIDUAL-3 does not fire (no positive z anywhere); K-OTHER fails formally, in the *negative*
direction. The deficit is what Lemma FR predicts: a coincidence g′ = g + [𝔏] with N(R)N(R′)ℓ < dn must be a rational ideal
identity, so unexplained coincidences at small translations need both classes outside the free region, while the
registered controls (all translations of order > 2) are mostly classes of large minimal norm, where FR excludes much less.
The post hoc control by the next 20 split primes (norm closer to ℓ₀, still larger) reduces but does not remove the deficit,
as expected from the ℓ-dependence of the free region (the control design was not norm-matched — a flaw of the
registration exposed by its outcome). **Reading:** beyond explicit ideal identities, the small-prime translations carry
*fewer* coincidences than chance, never more. There is no hidden class-level law here.

**Remark V (no Vieta moves for Type II at fixed n; PROVED).** Eliminating e, Type II at fixed n is cn = 4abcd − a − b,
which has degree 1 in each of a, b, c, d. A Vieta involution in a variable needs degree 2 in it, so none exists; every
two-variable slice is a hyperbola xy = N — fix (c, d): (4acd − 1)(4bcd − 1) = 4c²dn + 1 (Lemma DL′); fix (a, d):
A·e = N_a (Lemma Φ); fix (a, c): b·(4acd − 1) = a + cn; fix (a, b): c·e = a + b — whose only symmetry is the swap of the
two factors (CS, resp. a ↔ b) and whose "moves" are re-factorisations (DL, DL′). The Vieta/descent machinery of
`Z69_TWIST.md` §4 lives on Type I (quadratic in a, b) and moves n. Type I classes, for the record, are classes of the
ideals (f, 2ad + √−d), f = 4acd − p | 4a²d + 1, in the *fixed* group Cl(−4d) — no p-dependent class group is involved.
The (★) line is the c = 1 slice of Lemma DL′ with d = C: (4uC − 1)(4BC − 1) = 4Cp + 1.

### 1.7 Is any of it generative? No (PROVED, scoped) — and where squares and primality enter
**Proposition NG.** Let Σ be the set of partial maps on pairs (a, M) with M | N_a generated by: multiplication or
division of M by a divisor of N_a (Lemma Φ; DL), complement M ↦ N_a/M (CS), moving a factor between A and B in a c-fibre
(DL′), a ↔ b, and transport along free-region identities (FR). (i) Every element of Σ maps (a, M) to some (a′, M′) with
M′ | N_{a′}, and the class changes by the class of an ideal dividing 𝔅_a, 𝔅_{a′} or 1 + 2c√−dn. (ii) The image is a good
pair iff M′ ≡ −1 (mod 4a′d). (iii) For every n and a the divisor residues R_a := {M mod 4ad : M | N_a} form a set closed
under M ↦ nM⁻¹ and under products of coprime divisors; G_d(n) ≠ ∅ ⟺ −1 ∈ R_a for some a. Hence a composition of Σ
produces a good class only if it starts from a good class or if it exhibits −1 ∈ R_a — which is the original divisor
event; in particular Σ produces nothing at every n with G_d(n) = ∅: all odd squares (where χ_{−4d}(M) = +1 for every
M | N_a while χ_{−4d}(−1) = −1 — this is T1, a genus statement) and, for d = 1, the primes 37, 1621, 3361.
*Proof.* (i)–(ii) are the statements of Lemmas Φ, DL′, FR and §1.1; (iii) N_a ≡ n (mod 4ad) and the residues of coprime
divisors multiply. The square case: every prime q | m² + 4a²d with q ∤ 2dm has (−d/q) = 1, so χ_{−4d}(M) = 1. ∎
**Where primality must enter (Assessment).** At a prime p, divisors of N_a can contain primes q with (−d/q) = −1 =
(p/q) — the genus character attached to p makes the coset {χ_{−4d} = −1} available. A generative mechanism would have to
produce, from data present for every p, an M | N_a in the class −1 mod 4ad; the class group adds nothing to that task in the
region where G lives, because there (Lemmas SR, FR) the class map is injective on the relevant ideals and every class
relation is an ideal identity between integers. The always-present data (the principal relations φ_a(N_a) = T_d for
every a, the ambiguous classes, the classes of small split primes) generate only the divisor monoids of the N_a and
4c²dn + 1, not a residue class inside them. The J-exclusion (Corollary J) is the only "negative" class-level law found;
it constrains where good classes sit but forces nothing.

### 1.8 Verdict for item 1
**Narrowed (structure identified, non-generative).** PROVED: Lemmas Φ (a-fibre homomorphism, containing DL, CS and FIB),
DL′ (c-fibre lattice), SR (small natural representatives), FR (free region), Corollary J, Proposition NG. CERTIFIED: the
registered PSC/PSF runs (§1.5), the explicit decomposition, the J-check. EVIDENCE: on the windows tested, no positive
residual remains against PSF; the d = 1 residual against PSC is carried by Lemma DL′ / Φ identities (REP-ID) and the
OTHER share decays to 1 % at 4·10⁶. Unresolved: a negative (anti-coincidence) deviation of the data against PSF
(pooled d = 1 L3 −5.3), attributed (Assessment) to the null. **No forcing mechanism; not a HOT LEAD.**

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

The registered signal criterion **fires for ρ_ℓ** (and for nothing else). Follow-up (post hoc, explored on H_train + CTRL,
then H_test scored once; `scripts/z70_class_mine2a_post.py`): ℓ is the least prime with (−p/ℓ) = 1, and for p ≡ 1 (8)
[𝔏] lies in the principal genus iff ℓ ≡ 1 (mod 4), which caps its 2-part below that of h. The share of ℓ ≡ 1 (4) is
0.275 (CTRL), 0.895 (H_train), 0.900 (H_test) — the pseudo-square profile of the hard primes ((p/3) = +1 makes 3 inert,
etc.). **Within the strata the groups agree**: ℓ ≡ 1 (4): ρ = 0.798 / 0.794 / 0.796, v₂h − v₂ord = 1.66 / 1.67 / 1.64,
odd-part ratio 0.934 / 0.933 / 0.932; ℓ ≡ 3 (4): ρ = 0.948 / 0.936 / 0.966 (CTRL / H_train / H_test). Disjoint band
(added after registration; 2 000 primes of band B, seed 7071, W(p) by `z69_mine_allwit.c`; `i2a_band.txt`): corr(log W, ρ_ℓ)
= +0.141 (z = +6.35) overall, −0.009 and +0.006 within the two strata; all other invariants |z| ≤ 1.7 overall and
within strata. *Reading:* the ρ_ℓ "signal" is the genus position of the least split prime, i.e. local (quadratic-character)
data of p already known to separate the hard primes (Z69_MINE §3.1(b)); no class-group information beyond it.
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

No signal (all |z| < 1.8). Scope and caveats: witnesses whose ±5 % window has no admissible decoy are dropped (12 % in 2b,
30–42 % in 2c — the smallest moduli d, where the window contains no other integer of the right residue and symbols); at
most 8 witnesses per prime; yp ≤ 10¹³ resp. Cp ≤ 10¹³; class groups by PARI `quadclassunit` (GRH-conditional for the
group structure — immaterial for these statistics). Non-rejection, not equivalence: 2-s.e. half-widths ≈ 0.002–0.007 on
S1 (relative to a spread of ρ-values of order 0.1).
*Reading (Assessment):* by Lemma SR/FR the representation ideal of a witness is a small-norm ideal whose class is
"generic" among small-norm ideals of the same norm range and genus; the data show no trace of the class-group position of
witness ideals beyond that.
**Verdict item 2: null; one registered signal (ρ_ℓ) fired and is fully explained by the genus position of the least
split prime (local data).** Not a HOT LEAD.

## 3. Mandatory falsifier table — final

| screen | outcome | label |
|---|---|---|
| **F1 odd squares** | G_d(m²) = ∅ for all d (T1); in this memo's language: every divisor M of m² + 4a²d has χ_{−4d}(M) = +1 while the target residue −1 has χ_{−4d} = −1 (Prop. NG); the identified structure (Φ, DL′, SR, FR, Cor. J) consists of statements about existing divisors/solutions and is vacuous at squares. The non-squareness step a generative mechanism must use is exactly the availability of divisors q \| N_a with (−d/q) = −1 (equivalently (p/q) = −1 at a prime). Item 2 statistics are about witnesses of primes (none exist at squares). | PROVED |
| **F2 numerator 8 / C-even** | Lemmas Φ, DL′, SR, FR hold for every d, in particular even d (d = 2 runs: same picture — PSC residual explained by PSF and REP-ID); Type II with d even is the C-even side; nothing here distinguishes C odd from C even, and nothing claims positivity. 2c includes (★) witnesses of both parities of C. | PROVED / CERTIFIED |
| **F3 composites** | All lemmas hold for n ≡ 1 (4) with the stated coprimality (gcd(a, n) = 1 for Φ). Composite (★)-zeros below 10⁵ (d = 1): 61 of 93 skipped (an ideal norm shares a prime with n), 8 with \|G\| < 2, 24 analysed: all \|Z\| ≤ 1.9 against PSC and PSF; decomposition L1: 9 EID / 0 REP-ID / 13 OTHER (22 pairs). A symmetry of existing solutions cannot separate primes from composite zeros. | PROVED / CERTIFIED |
| **F4 known zeros** | Hard list (d = 1: 32 primes analysed incl. the 14 (★)-zero and 38 𝔊*-zero primes below 10⁶ where \|G\| ≥ 2; d = 3: 4): all \|Z\| ≤ 1.7 against PSC. H_train/H_test (incl. 2521, 3361, 21841, 76441) in item 2: no class-group difference beyond the local ρ_ℓ effect. | CERTIFIED |

## 4. Verdict
**Narrowed; no forcing mechanism; not a HOT LEAD. ES is OPEN.**
* Item 1: the I17 residual is real for d = 1 (and d = 2) against a null that keeps DL and CS exactly (PSC; registered,
  fresh windows, pooled d = 1 L1 Z = +11.5); the z69 d = 3 residual is *not* (K-RES). The residual is identified: it is the
  multiplicative structure of the small natural representatives of the good classes — the c-fibre lattice (Lemma DL′, the
  twin of DL in the factorisation 4c²dn + 1 = A·B), a-fibre identities between A- and e-side representatives (Lemma Φ) —
  carried into the class group by a map that is injective on small ideals (Lemmas SR, FR). Against a null that keeps all
  fibre relations (PSF) no positive residual remains; the leftover is a negative deviation attributed to the null.
  Corollary J proves the J-avoidance. The in-sample test (§1.6b) finds *fewer* unexplained coincidences at small-prime
  translations than chance (FR). Remark V: Type II at fixed n is multilinear, so no Vieta moves exist. Proposition NG: none of these maps is generative; each needs a divisor M ≡ −1
  (mod 4ad) of some N_a to start, which is the B2 event.
* Item 2: class-group invariants beyond h (2-, 3-parts of h(−4p), h(−8p), h(p) = 1) do not separate the hard primes; the
  order of the least split prime's class does, but only through its genus (local data); orders of U₇ and (★)
  representation-ideal classes match exact decoys on H_train, H_test, CTRL and a disjoint band.
* What this buys: a closed account of I17 (no hidden group law in G_d), two new short lemmas (DL′, Cor. J) and the
  free-region principle (class relations among good classes are integer identities), which tells future lanes that
  class-group *positions* of good forms carry no information beyond the divisor structure of n + 4a²d and 4c²dn + 1.

**Hard screens (FRONTIER §4).** T1 squares: passes (vacuous; NG names the genus step). 8/131: no positivity claim.
Tied modulus: the identified structure lives entirely inside the tied divisor event (it presupposes M ≡ −1 (mod 4ad));
it does not loosen the tie. Fixed p: all statements are per n (per p), but none produces a solution.

## 5. Proposed FRONTIER §7 text (do not edit FRONTIER here)
"z70 CLASS (`Z70_CLASS.md`; narrowed). I17 closed: against a registered null that keeps Lemmas DL and CS exactly (prime-swap
of the ideal factorisation, CS imposed), G_d(n) still shows translation structure for d = 1, 2 (pooled d = 1 L1 Z = +11.5)
but not for d = 3, 5, 7 (z69's d = 3 residual = DL + CS). PROVED: Lemma Φ (n + 4a²d fibres: φ_a is a homomorphism on coprime
divisors with φ_a(N_a) = T_d; contains DL, CS); Lemma DL′ ((4acd − 1)(4bcd − 1) = 4c²dn + 1, c-fibre divisor lattice); Lemma
SR (every good class has a natural ideal of norm ≤ √(d(2n + e))); Lemma FR (free region: class relations with norm product
< dn are rational ideal identities); Corollary J (g, g + J ∈ G₁ ⟹ 2m(g)m(g+J) ≥ n). CERTIFIED: at n ≈ 4·10⁶ (d = 1) 216 of
218 L1-overlaps are explicit ideal identities between natural representatives. So the class-group 'structure' of good
forms is integer divisor structure; Prop. NG: none of it is generative. MINE class-group item: h-parts, h(p) null; the
least split prime's class order separates hard primes only via its genus (local); U₇ and (★) representation-ideal class
orders match exact decoys (H_train/H_test/CTRL/band)."

## 6. Bottom line
The good-form class sets G_d(p) do have structure beyond their norm profile, and it is now fully identified: every good
class contains a small ideal (norm A = 4acd − 1, B = 4bcd − 1 or de), and in the region where these ideals live the class
group is a faithful copy of the ideal monoid (Lemma FR), so the "translations" are divisor-lattice identities of the
integers n + 4a²d and 4c²dn + 1 (Lemmas Φ, DL′) — not a group law. The one class-level law (Corollary J) is an exclusion.
Nothing here can create a first solution: all maps start from a divisor M ≡ −1 (mod 4ad), which is the B2 event; the
class group is a spectator. Item 2 (class-group invariants vs U₇/(★) witnesses) is null, its single registered signal
being the genus of the least split prime. Not a HOT LEAD. ES is OPEN.

## 7. Reproduction
`scripts/z70_class_run1.sh A|B|C|D` (PSC runs, §1.2), `… E|F` (PSF runs, §1.4); single runs:
`uv run --with sympy --with numpy python scripts/z70_class_null.py PSC d R seed range P0 P1`,
`… scripts/z70_class_psf.py d R seed range P0 P1` (`Z70_MATCH2=1` for the 2-adic diagnostic),
`… scripts/z70_class_repid.py d range P0 P1`, `… scripts/z70_class_jcheck.py P0 P1`,
`… scripts/z70_class_other.py d range P0 P1` (`Z70_SMALLCTL=1` for the post hoc control),
`python3 scripts/z70_class_pool.py FILES` (pooled Z), `… scripts/z70_class_core.py` (selftest of the dictionary).
Item 2: `uv run --with cypari2 --with sympy python scripts/z70_class_mine2.py 2a data/z70/class/i2a`,
`… 2b SET data/z70/class/i2b_SET.txt`, `… 2c SET data/z70/class/i2c_SET.txt data/z70/class/star_d1e5.txt.gz`,
`… scripts/z70_class_mine2a_post.py CTRL H_train` / `H_test`, `… scripts/z70_class_mine2a_band.py`; band witnesses
`gcc -O2 scripts/z69_mine_allwit.c -o allwit` on the 2 000 band primes (seed 7071 sample of `raw_r2_gen2_band.jsonl.gz`);
(★) solutions `gcc -O2 scripts/z70_class_star.c -o star; ./star 100000 < primes`. All runs: `ulimit -v 6000000`,
`timeout` ≤ 1800, ≤ 2 compute processes. Run time of everything: < 30 min.

## 8. Review log
(pending: internal hostile deep review)
