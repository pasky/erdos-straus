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
