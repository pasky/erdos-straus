# z52d avenue — batch P03 (100 items) summary
ES is OPEN. Rows: `out_P03.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| circular | 32 | 0 | 0 | 0 | 32 |
| known-false | 26 | 0 | 0 | 0 | 26 |
| known-true (gap named) | 23 | 0 | 0 | 3 | 26 |
| unclear | 4 | 3 | 0 | 0 | 7 |
| open-plausible | 0 | 2 | 3 | 2 | 7 |
| harder-than-open | 2 | 0 | 0 | 0 | 2 |
Novelty: 0 → 47, 1 → 51, 2 → 2 (Z2519 Strömbergsson–Venkatesh, Z0292 triangle orbifolds; both no ES role).

**Plausibility ≥ 2 AND novelty ≥ 1** — all averaged (B6) or explicit-constant bookkeeping; none has ES yield:
* Z2362: Σ_{p≤X}R(p)² ≪ π(X)log⁴X + BV first moment ⇒ R(p) ≫ log²p on a positive density of primes (Paley–Zygmund over p).
* Z2947: every [x, x+x^{0.525}] contains a prime with ES — already a corollary of (D)30 + BHP; the (★)-only version needs a check.
* Z2418: explicit (c, N₀) in E(N) ≤ N exp(−c(log N)^{3/4}).  Z2858: explicit level bound in SYNTHESIS_SPARKS9 Prop 2.2.
* Z2901: explicit M_BM(p) ≥ c·log²p — explicit Pólya–Vinogradov already suffices (Burgess only improves c).
* Z2379 / Z2400: level of distribution > 1/2 for the forced classes / for R(n) in APs — only constants move under the 3/4 CRT cap.

**Recurring missing theorems**
1. *One tied-divisor event / H⁻_BM at a fixed p* (circular): Z2376, Z2954 (Maynard m = 1), Z2387, Z2389, Z2397, Z2413, Z2975,
   Z3049 (analytic error terms; the two-sided forms are false i.o. by Linnik — Z2398 known-false), Z2422, Z2714, Z2903, Z3076
   (GRH insufficient), Z3093, Z3012, Z3067, Z2950. Restatements of ES itself: Z3105, Z1812, Z2519, Z2785, Z2802, Z2895, Z1678.
2. *Split-fibre fibrations / descent / BM shortcuts*: Z0281, Z0493, Z0526, Z2295, Z2466, Z2703 (each fibre is a divisor event;
   Harpaz/Châtelet hypotheses fail structurally — split fibres).
3. *No infinite automorphism group* (Vieta/Markoff/Fricke): Z1355, Z2140, Z0988, Z2463 (boundary through the nodes, M3).
4. *Finite menus / identity coverings (B1)*: Z1277, Z1286, Z1320, Z0106, Z1301, Z2417 (sterile r-generic points).
5. *Eisenstein-only automorphic forms* (no cusp part to bound; B3/T1): Z1680, Z1490, Z1699, Z1900, Z1307, Z2743 (Galois orbits), Z0274.
6. *Averaged layer (B6)*: Z2362, Z2379, Z2400, Z2444, Z2754, Z3062, Z3042, Z3086, Z2947, Z3031 (prime gaps below x^{0.525}).
7. *Calibration only*: Z2411, Z2561, Z3047, Z3178, Z0042, Z0221, Z0292, Z0826, Z1589, Z2049, Z0703, Z2517, Z2646.

**Cheap checks / small results in this pass** (timeout 60, ulimit 4 GB)
* Z2841 (`scripts/z52d_avenue_P03_forest_priv.py`): at p ≈ 10⁶ the forest has 55–131 edges, 18–44 with odd part on primes ≤ 50
  (congruence data, B1) and 16–32 carrying a private prime (no constraint on χ_p) — monochromaticity cannot force pretentiousness.
* Z3003 (`scripts/z52d_avenue_P03_fourier_check.py`, 300/300 cases): r(−1) = φ(e)⁻¹Σ_χ χ(−1)Π_{s|N}(1 + 2Re χ(s)) (squarefree N), so
  every obstructed window has a χ ≠ 1 with |Π(1+2Re χ(s))| ≥ 3^ω/(φ(e)−1). Exact but weak; the only open-plausible item with a
  proof-shaped missing theorem (plausibility 1). Next: do obstructions at hard primes share ONE character across windows?
* Z0703: a Type I solution has its p-multiple denominator ≥ p(3p+1)/4, so "minz(p) ≡ 0 (mod p)" follows from a Type II solution with
  max denominator ≤ p(3p+1)/4 (any (★) solution with min(u,B) ≥ 2) — ES-strength; Pass 1's "covered" via 0190 was overstated.
* Z3121 decided without computation: positive proportion over polylog attempt sets is false i.o. (POINTWISE_OMEGA13 Thm 5.1, H4_NOT_POLYLOG).

**Corrections to inputs**: Z3105 premise false (the two-term step fails for ~89 % of x, not a thin set); Z2417 first step ill-posed
(n₂(p) ≤ 13 fails i.o. by Dirichlet); Z2950 orientation backwards (Siegel-exceptional p are the easy ones); Z2901 Burgess not needed.

**Assessment.** No P03 item points outside the repo's B2 / H⁻_BM / averaged-layer picture. The only items with plausibility ≥ 2 are
averaged or explicit-constant statements (zero ES yield). Most useful follow-up: the Z3003 single-character test (cheap, falsifiable).
