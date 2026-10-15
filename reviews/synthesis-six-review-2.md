# Hostile review #2 of O238 Synthesis VI (SYNTHESIS_SPARKS6.md + BRAINSTORM/s6_*.md) — R246, round 1

Reviewer: R246 (independent; no author files edited). From-scratch scripts: `scripts/review_r246_*.py`.

## Summary verdicts
| claim | verdict |
|---|---|
| **Thm 1.1** ES for every n = 4^s + 105 (Lemma 1.0, 1.0′, 13 ET classes, coverage) | **SOUND** (independently re-certified from scratch; MINOR D1) |
| Thm 1.1 T1 control | SOUND, but stronger than stated: the exp class is a LOCAL non-square class (D4) |
| §1.2 / s6_mixed_points_cuberoots "mixed points were a menu artefact; sterility is menu-relative"; Thm 1.4 "violated hypothesis" | **GAP** (D2 MAJOR, D4) |
| s6_unique_forced_cap0 | SOUND (D6 MINOR) |
| s6_divisor_pigeonhole (incl. Cauchy–Davenport with zero images excluded) | SOUND (D7 MINOR) |
| s6_numerator_windows: sign-level only-if Theorem | SOUND |
| s6_numerator_windows: "works for every ν/n", "window shape strictly more T1-rigid" | **GAP** (D3 MAJOR) |
| s6_witness_onesided (EVIDENCE) | SOUND-AFTER-REPAIRS (D5, D8 MINOR) |
| s6_ydual_windows | SOUND (D9 MINOR) |
| s6_window_independence (heuristic) | SOUND as labelled after D10 (MINOR) |
| s6_exp_classes_primes (Assessment, negative) | SOUND |
| Novelty / labels | Thm 1.1 genuinely new in the campaign (non-ET identity class); NOT the first all-Mordell-hard ES family (D11) |

No FATAL defect. The headline theorem stands.

## Thm 1.1 (ES for every 4^s + 105) — checks

### C1. Certificate, from-scratch checker (`scripts/review_r246_cert105.py`, no s6_/z8/ec_cover imports)
Reads only `data/s6_cert105_et.json`. Results (all assertions pass, 1.5 s):
* all 13 classes: 4xyz = n(xy+yz+zx) as a polynomial identity in n (sympy expand);
* integer-valued on n = r + Mt: each of x, y, z expanded in t is integral at deg+2 consecutive t (⟹ integer-valued on ℤ);
* positivity: every coefficient (in n) of every x, y, z is ≥ 0 and not all zero ⟹ positive for all n > 0 (so no
  "n ≥ 4⁴" restriction is needed);
* all M odd; ord_M(4) ∈ {5, 6, 9, 10, 15, 20, 30} all divide 360 (lcm = 180), so n_s mod M depends only on s mod 180
  for EVERY s ≥ 0 — the "(for s ≥ 64)" in Thm 1.1(a) is unnecessary (harmless);
* uncovered s mod 360 = exactly {34, 124, 214, 304} = {s ≡ 34 (mod 90)};
* exponential class: identity (sympy simplify), 4x − n = 151, 2(32u+33)(u²−u+1) = 151A, A integer-valued on 32 + 151ℤ,
  A > 0 for u ≥ 1; ord₁₅₁(4) = 15, 4¹⁰ ≡ 32 (mod 151), and for s ≡ 34 (mod 45): 3 | s − 4, (s−4)/3 ≡ 10 (mod 15);
* exact solutions built and checked for every 0 ≤ s ≤ 2000 (22 of them via the exponential class).

### C2. ET Prop 1.9 provenance (`scripts/review_r246_et19.py`)
Checked against the actual statement and §10 proof of Elsholtz–Tao arXiv:1107.1010 (sources/ PDF): every `II2` class with
params (a, d, f) satisfies 4ad | f + 1 and r ≡ −4a²d (mod f), and its (x, y, z) equals ET's sextuple
(a, c(n+4a²d)/f − a, c = (f+1)/(4ad), d, e = (n+4a²d)/f, f) pushed to (abd, nacd, nbcd) — exactly the second Type II family.
`D` classes: M | n and the JSON gives m·(x₀, y₀, z₀) with 4/M = 1/x₀ + 1/y₀ + 1/z₀ (11: 3, 34, 1122; 41: 11, 154, 6314;
13: 4, 18, 468; 19: 5, 96, 9120). Citation correctly applied (only the "converse" direction is used; no primality needed).

### C3. Independent search, no certificate (`scripts/review_r246_bruteforce.py`)
Divisor search ((my − N)(mz − N) = N², N = nx) found and verified a solution for every 0 ≤ s ≤ 20 (n up to 1.1·10¹²).

### C4. T1 controls (`scripts/review_r246_t1.py`)
* All 9 non-divisor classes: r is a non-square mod M (no square in the class). Divisor classes do contain squares (fine).
* Exponential class: n ≡ 59 (mod 151), (59/151) = +1, so 151 ∤ n and gcd(K, n) = 1. The solution is CAP_DOWN Lemma 1.1 at
  m = 151 with K = x = 64(u³+1) and d = K/(32(u+1)) = 2(u² − u + 1) — an honest divisor of K, cap 0. I re-derived CAP_DOWN
  §3 "T1 for Lemma 1.1" (Jacobi (d/m) = −1 from d ≡ −K, vs (d/m) = +1 primewise via reciprocity, m ≡ 3 (4), and
  m ≡ 7 (8) at s = 2); it applies (m = 151 ≡ 3 (4), gcd(m, n) = 1). So "no square in the exp class" is PROVED, not just
  numerical. Numerics agree: 256u³ + 105 is a square for no u = 32 + 151t, t < 10⁶, and for u < 10⁶ only u = 1 (19²).
  (Remark: T1 is a consistency control only — any valid identity proves ES regardless.)

### C5. Labels / novelty
* "Mordell-hard for every s" (§0 (I2), AGENT_REPORT l.6) is false for s = 0, 1 (106 even; 109 ≡ 5 (8)); for s ≥ 2 the
  residues n_s mod 840 are exactly Mordell's six hard classes {1, 121, 169, 289, 361, 529} (recomputed). SIGN_FIELDS
  already carries the R236 repair "s ≥ 2".
* "First infinite ES family all of whose members are Mordell-hard"? NO, and the author does not claim it: (J)22 Thm 4.1
  already gives all 315·2^m + 1 (≡ 1 mod 2520 for m ≥ 3) and 15015·2^m + 1, and trivial families (e.g. 121(840t+1),
  11 | n) exist. What appears new within the campaign: the first family closed with a non-ET identity class whose
  witness divisor d = 2(u² − u + 1) ≍ n^{2/3} moves algebraically with n. Literature: no treatment of ES on 4^s + k found
  (3 Jina web searches; R236 likewise); not exhaustive.

## s6_unique_forced_cap0 — check
Re-derived. In Thm 1.1′'s setting (every prime factor of m is ≡ 3 (4)) G = (ℤ/m)^* = E × U with E ≅ (ℤ/2)^r, so U = 1 ⟺
every q_i^{k_i} has φ = 2 ⟺ m = 3, and then G = {±1} and any forced K has a prime ≡ −1: cap 0. If U ≠ 1 pick
g = (−1,…,−1)·u, ord u = o > 1 odd; a prime s ≡ g (Dirichlet), s odd, gives n = 4s − m ≡ 1 (4), (q_i/n) = (s/q_i) = −1,
m ≡ 4 − n (8): admissible, and Σ_m(s) = {1, g, g⁻¹} ∌ −1. Brute force (`scripts/review_r246_pigeon.py` (b)): among all
admissible m ≤ 300 (including m ≡ 1 (4) with two prime factors), m = 3 is the only window at which every forced prime K
has cap 0. Verdict: **SOUND** (two MINOR wording points, D6).

## s6_divisor_pigeonhole — check
* Pigeonhole: P, −P ⊂ (ℤ/q)^* (gcd(K, q) = 1), |P| + |−P| > q − 1 ⟹ d₁ ≡ −d₂, and d = K·d₁/d₂ has c_s = b_s + δ_s ≤ 2b_s:
  cap 0. Correct.
* Cauchy–Davenport: for q ≡ 3 (4), G = {±1} × U, u odd; only s₀ carries the sign, so the U-condition is ±log w₀ ∈
  Σ δ_s·a_s with |δ_s| ≤ v_s; N copies of the 3-set {−a, 0, a} (a ≠ 0) give |sumset| ≥ min(u, 2N + 1) for u prime,
  equality when all a equal. The R-O238 repair (N counts only primes with nonzero image; s ≡ 1 contributes {0}) is
  correct and necessary (q = 7, K = 3·29^N: Σ = {1, 3, 5} ∌ 6 for every N). Brute-force confirmation of
  min |sumset| = min(u, 2N+1) for u ∈ {5, 7, 11, 13}, N ≤ 5 (script (c)).
* Numerics reproduced exactly from scratch (own sieve/Jacobi/factoring): 8977 primes, criterion 4870, cap 0 6149, no
  criterion-true/cap-0-false case.
* "the other primes map to even exponents in log coordinates" (memo l.8) is unexplained and seems unnecessary (D7).
* ±-weighted Davenport constant D_{±}(ℤ/n) = ⌊log₂ n⌋ + 1 matches Adhikari–Chen–Friedlander–Konyagin–Pappalardi (2006)
  (from memory; paper not in sources/).
Verdict: **SOUND** (Prop + sharpness PROVED, numerics EVIDENCE as labelled).

## s6_numerator_windows — check
* Lemma-1.1 algebra for ν/n (m = νK − n, ν/n − 1/K = m/(nK)): correct.
* The Theorem's Jacobi computation (n = a²: (K/q_i) = (ν/q_i); ν square; ν odd via (m/ν) = (−a²/ν) and reciprocity;
  4 | ν via m ≡ −a² ≡ 3 (4), (2/m) = 1 when 8 | ν since m ≡ 7 (8)) re-derived line by line: **correct as a statement about
  the sign condition** ("(K/q_i) = −1 for all i" is impossible at n = a² in those cases). The only-if direction is all
  that is claimed; fine.
* **But the mechanism and the reading are broken for odd ν (D3, MAJOR).** A forced window has m = ∏ q_i odd. For odd ν
  and odd n, νK = m + n is even, so **K is always even** — exactly the case the memo's own R-O238 repair excludes ("K ODD").
  Hence (1) "the self-generated mute set works for every ν/n" is false/vacuous for odd ν at odd n; (2) the even-K
  forced windows really can fail: `scripts/review_r246_numwin_even.py` (non-squares n < 4000, prime q ≡ 3 (4) < 200,
  sign condition (K/q) = −1, gcd(K, qn) = 1) finds forced-sign windows with NO Lemma-1.1 d at any cap: ν = 3: 173/7479
  (e.g. n = 5, q = 19, K = 8: −8 ≡ 11 ∉ ⟨2⟩ = {1,2,4,8,16,13,7} mod 19), ν = 5: 120/4616 (n = 21, q = 19, K = 8),
  ν = 7: 100/3168; (3) the memo's numerics for ν ∈ {5, 13, 17, 21} (`s6_numerator_windows.py` does not check K's
  parity) count sign-forced windows with K even, which are not guaranteed to produce solutions; (4) "the window shape is
  strictly more T1-rigid than the problem" is FALSE as a statement about window-shape solutions: `scripts/review_r246_numwin.py`
  finds integral window solutions (x = K, y = nA, z = nKA/d, m odd with all prime factors ≡ 3 (4), gcd(m, n) = 1) at odd
  squares for ν = 3, 7, 9, 11, 19 — e.g. 3/49 = 1/20 + 1/98 + 1/980 (m = 11), 7/25 = 1/4 + 1/50 + 1/100 (m = 3),
  9/169 = 1/20 + 1/338 + 1/3380 (m = 11) — while the control ν = 4 gives none (CAP_DOWN §3 T1). What is rigid is the
  *sign-forcing hypothesis*, not the window shape.
Verdict: Theorem (sign-level only-if) **SOUND**; "works for every ν/n" and "window-shape T1 … strictly more than (J)46"
readings **GAP** (D3).

## s6_witness_onesided — check (`scripts/review_r246_witness.py`, from scratch)
* Observation: for q ≡ 3 (4), p ≡ 1 (4): (−K/q) = −(p/q) = −(q/p); a square d forces (q/p) = −1, a non-square d does not.
  Correct but, as a "PROVED observation", it only removes a Legendre obstruction; the actual content (cap-0 windows with
  (q/p) = +1 exist) is shown by examples — e.g. p = 13, q = 3 ((3/13) = +1), K = 4, d = 2: 4/13 = 1/4 + 1/26 + 1/52.
  Suggest stating it as "Example/EVIDENCE: non-necessity, witnessed by …".
* Numerics reproduced: (q/p) = −1: cap 0 at 561, dead at cap ≤ 6 at 218; (q/p) = +1: cap 0 at 279 (53 with K odd), dead 784.
  The pair TOTALS do not match: I get 1635 / 1530 (sum 3165 = 15 windows × 211 primes), the memo says 1655 / 1531 (sum
  3186, not a multiple of 15) — transcription slip (D8, MINOR); rates become 34.3 % vs 18.2 % (unchanged to 2 digits).
* "(q/p) = −1 forces firing at some cap" is **false without the 2-adic hypothesis**: 14 pairs with (q/p) = −1 are dead
  at EVERY cap (E = q), all with K even and CAP_DOWN Thm 1.2's (E) failing (q ≡ 3 (8), v₂(K) odd). Needs "(and K odd or
  (E))" (D5, MINOR; the correct statement is already CAP_DOWN Thm 1.2).
Verdict: **SOUND-AFTER-REPAIRS** (EVIDENCE label appropriate).

## s6_ydual_windows — check
* (a) Re-derived including the branches where p divides the D₁ of (Mx − pA)(Mz − pA) = p²A²: D₁ = p^j·D, D built from
  primes of A (any cap: primes of den z divide y = pA). j = 0, 2 give −p/4 ≡ D or A²/D ∈ ⟨primes of A⟩ (using 16A² ≡ 1
  mod M); j = 1 would put p in x, y, z (4 = sum of three unit fractions, impossible). So necessity holds for the whole
  y = pA slice, not only the 𝒟_e family. Brute force (`scripts/review_r246_ydual.py`, cap-0 slice, all p < 2·10⁴,
  A ∈ {2, 3, 5, 6, 8, 12}): no integer solution with −p/4 ∉ ⟨primes of A⟩. M = 7, A = 2 example (p ≡ 1, 2, 4) correct.
* (b) is CAP_POINTWISE Thm 1.1 (needs K odd / (E) for the firing half, cf. D5).
* "Phase boundary = who owns the mute set": a dictionary/Assessment, fairly labelled.
Verdict: **SOUND** (PROVED dictionary; the Assessment part should be labelled as such, D9 MINOR).

## s6_window_independence — check
gcd(K_m, K_{m′}) | (m − m′)/4 is correct (K_m − K_{m′} = (m − m′)/4). The R-O238 self-review heuristic label is right.
But "essentially disjoint sets of primes" / "no pigeonhole over windows exists because the K_m are pairwise almost
coprime" overstate even the heuristic: the shared primes are exactly the SMALL ones (3 | K_m for a third of windows, …),
which dominate |P| and hence the cap-0 events; correlation through them is not excluded (D10, MINOR). Average f(p) ≍ log³p
matches ET Thm 1.1 (N log²N ≪ Σ f(p) ≪ N log²N log log N) up to the log log. Verdict: **SOUND** as PROVED (trivial) +
Assessment, after toning down the "no pigeonhole exists" sentence to Assessment.

## s6_mixed_points_cuberoots / "sterility is menu-relative" — check
* μ* (4 at ℓ ≠ 3, −2 at ℓ = 3) reduces mod 45 to 34 (34 ≡ 7 ≡ −2 (9), ≡ 4 (5)): correct.
* **"T1 respect global, not local" is FALSE for the exponential class (D4, MAJOR for the Assessment, MINOR for Thm 1.1).**
  q = 18837001 is a prime factor of 2⁹⁰ − 1 = 4⁴⁵ − 1 with ord_q(4) = 45, and (n_s/q) = −1 for every s ≡ 34 (mod 45)
  (`scripts/review_r246_localT1.py`). So the exponential class, read as a congruence class of n mod 4⁴⁵ − 1 (as the
  author's own R-O238 self-review does), IS a non-square class — T1 is respected locally, exactly as for ET classes.
  Only the larger cubic family 256u³ + 105, u ≡ 32 (151) (u not a power of 4) hits squares mod q and needs the global
  Lemma-1.1 T1. Repair SYNTHESIS §1 "T1 control" ("no non-square congruence is certified here") and the memo's
  "congruence-wise square-compatible … new kind of T1 respect": cite (n_s/18837001) = −1.
* **Sterility framing (D2, MAJOR).** (i) The sterile set S′ of EXPONENT_COVERING Thm 1.4 is *defined* as the complement of
  the union of ET + divisor classes, so "sterility is menu-relative" is a tautology, not a finding. (ii) No point of
  Λ₁₀₅ was ever shown sterile: SIGN_FIELDS (J)62 says μ* itself lies in the II2 class (2, 23, 919), "no mixed point found
  so far is sterile", and calls the stall "EVIDENCE (weak) that k = 105 is coverable at very large cost". Hence the 105
  theorem does not show that a sterile point was overcome, nor that the stall was "an artefact" in any sense beyond
  "the greedy ran out of budget". (iii) The question (J)62/(J)22 actually left open for k = 105 — does a finite covering by
  ET + divisor classes exist, i.e. Λ₁₀₅ ∩ S′ = ∅? — is UNCHANGED by Thm 1.1 and must be stated as still OPEN. (iv)
  Internal inconsistency on which hypothesis of Thm 1.4 fails: §0 (I2) and §3 item 1 say "classes with fixed moduli",
  §1.2 / s6_exp_classes_105 / AGENT_REPORT say (correctly) the class IS a fixed-modulus congruence (mod 45 in s,
  mod 4⁴⁵ − 1 in n) and what fails is "identity polynomial in n (an ET class)". Thm 1.4 is not "violated" — it is simply
  not about non-ET identities. Repair: delete "fixed moduli" in §0 (I2), §3.1; replace "mixed points were an artefact /
  sterility is menu-relative" by "ES on the family does not need Λ₁₀₅ ∩ S′ = ∅; whether a fixed-class covering exists
  remains open".
* Weil-reciprocity / FF root-product "dictionary": an analogy; labelled Assessment — acceptable, but the "ℤ shadow of
  Weil reciprocity" phrasing in SYNTHESIS §2 (v) should not appear outside an Assessment.
Verdict: instance (Thm 1.1) PROVED; reading **GAP** (D2, D4).

## s6_exp_classes_primes — check
"Every exponential class is a polynomial family in a root parameter" is correct for this one (n = 256u³ + 105), and the
density-0 argument for finitely many polynomial families of degree ≥ 2 is standard. "B1 (POINTWISE_SIZE Thm M analogue)"
is an analogy (Assessment). Verdict: **SOUND** as Assessment (negative).

## Numbered defects

**D1 (MINOR) Thm 1.1 presentation.** (a) "(for s ≥ 64)" in Thm 1.1(a) is unnecessary: all M are odd and every
coefficient is ≥ 0, so coverage, integrality and positivity hold for every s ≥ 0. (b) "Mordell-hard for every s"
(SYNTHESIS §0 (I2), AGENT_REPORT l.6) is false for s = 0, 1 (106, 109); write "s ≥ 2" as SIGN_FIELDS does. (c) Lemma 1.0
integrality: replace "checked by forward differences" by the one-liner 32·32 + 33 = 1057 = 7·151, so 151 | 32u + 33 for
u ≡ 32 and 151A = 2(32u+33)(u²−u+1). (d) Add the explicit d = K·d₁/d₂ = 2(u² − u + 1) (an honest divisor of K, cap 0).

**D2 (MAJOR) Sterility framing and the Thm 1.4 hypothesis.** Locations: SYNTHESIS §0 (I2), §1.1 "Scope", §1.2 last
sentences, §2 row (v), §3 item 1; s6_mixed_points_cuberoots; AGENT_REPORT ("(J)62's mixed points are sterile only for
menus of polynomial-in-n ET identities"). Problems: no point of Λ₁₀₅ is known to be sterile ((J)62: μ* lies in II2
(2, 23, 919); "no mixed point found so far is sterile"; the stall is weak EVIDENCE of coverability); S′ is defined
relative to the ET menu, so "menu-relative" is a tautology; Thm 1.4's hypothesis is not "fixed moduli" (the exp class
has a fixed modulus) but "ET/divisor classes"; and the fixed-class coverability of k = 105 remains OPEN. Repair: as in
the mixed-points section above; in particular add to §1.1 "Thm 1.1 does not decide whether Λ₁₀₅ ∩ S′ = ∅ ((J)62/(J)22
question remains OPEN)", delete "fixed moduli" in §0 (I2) and §3.1, and downgrade "the stall was an artefact" to
"the greedy stall is bypassed".

**D3 (MAJOR) s6_numerator_windows for odd ν.** For odd ν and odd n every forced (odd) window has K even, which the
memo's own R-O238 repair excludes; even-K sign-forced windows fail at every cap in ≈ 2–3 % of cases (ν = 3: n = 5,
q = 19, K = 8). And window-shape solutions DO exist at odd squares for ν = 3, 7, 9, 11, 19 (3/49 = 1/20 + 1/98 + 1/980).
Repair: restrict "works for every ν/n" to ν ≡ 2 (4) (K may be odd) and to 4 | ν, and for odd ν state the even-K 2-adic
condition (analogue of CAP_DOWN Thm 1.2 (E)); rename "window-shape T1" to "sign-forcing T1" and delete "the window shape
is strictly more T1-rigid than the problem"; flag that the ν ≡ 1 (4) numerics count even-K windows (not solutions).
Also SYNTHESIS §2 table row and §3 item 3 ("window-shape T1 proved impossible-at-squares").

**D4 (MAJOR for the Assessment; MINOR for Thm 1.1) local T1 for the exp class.** (n_s / 18837001) = −1 for all
s ≡ 34 (mod 45) (18837001 | 4⁴⁵ − 1, ord = 45). Locations: SYNTHESIS §1 "T1 control" ("no non-square congruence is
certified here"), s6_mixed_points_cuberoots barrier screen ("congruence-wise square-compatible … a new kind of T1
respect, 'global, not local'"), AGENT_REPORT caveat 2. Repair: cite the local certificate; the "global T1" remark
applies only to the full cubic family u ≡ 32 (151).

**D5 (MINOR) s6_witness_onesided.** "(q/p) = −1 forces firing at some cap" needs "K odd, or CAP_DOWN Thm 1.2 (E)":
14 pairs (p < 3000, q < 120) with (q/p) = −1 are dead at every cap, all with K even and (E) failing.

**D6 (MINOR) s6_unique_forced_cap0.** State admissibility as in Thm 1.1′ (m ≡ 4 − n (8), all prime factors ≡ 3 (4))
rather than "m ≡ 3 (4)"; say explicitly that U = 1 ⟹ (ℤ/m)^* = {±1} uses G = E × U with E ≅ (ℤ/2)^r; the ν-version
("For numerator ν the same statement … m | 24") is unproved — label Assessment or prove it.

**D7 (MINOR) s6_divisor_pigeonhole.** The hypothesis "other primes map to even exponents in log coordinates" is
unexplained and unused in the Cauchy–Davenport bound; delete or explain. State u prime for CD (Kneser otherwise).

**D8 (MINOR) s6_witness_onesided totals.** Pair totals are 1635 / 1530 (sum 3165 = 15·211), not 1655 / 1531.

**D9 (MINOR) s6_ydual_windows.** Label the "phase boundary = who owns the mute set" paragraph as Assessment; note that
necessity in (a) holds for the whole y = pA slice (including p | D₁ branches), which strengthens the Prop.

**D10 (MINOR) s6_window_independence.** "No pigeonhole over windows exists because … pairwise almost coprime" is an
Assessment; the shared primes are precisely the small ones that drive cap-0 events.

**D11 (MINOR) Novelty statement.** Add: not the first infinite all-Mordell-hard ES family ((J)22 Thm 4.1: 315·2^m + 1,
15015·2^m + 1, m ≥ 3); the new feature is closing a family with a non-ET identity class whose divisor 2(u² − u + 1) moves
with n. Literature search (3 web queries) found nothing on ES for 4^s + k; not exhaustive. §1.3–1.5 numerics
(79 %, k = 33/273/297 stall densities) were NOT re-run by this reviewer (EVIDENCE, untouched by the theorem).

## Scripts (all from scratch)
`review_r246_cert105.py` (full certificate + exact s ≤ 2000), `review_r246_et19.py` (ET Prop 1.9 provenance),
`review_r246_bruteforce.py` (certificate-free ES for s ≤ 20), `review_r246_t1.py`, `review_r246_localT1.py`,
`review_r246_pigeon.py`, `review_r246_numwin.py`, `review_r246_numwin_even.py`, `review_r246_witness.py`,
`review_r246_ydual.py`. All runs < 1 min, single core, under ulimit -v 8 GB.
