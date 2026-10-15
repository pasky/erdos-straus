# Hostile review #2 of O238 Synthesis VI (SYNTHESIS_SPARKS6.md + BRAINSTORM/s6_*.md) — R246, round 1

Reviewer: R246 (independent; no author files edited). From-scratch scripts: `scripts/review_r246_*.py`.

## Summary verdicts
(filled in progressively)

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
