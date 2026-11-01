# z52d avenue — batch Q13 (113 items) summary
ES is OPEN. Rows: `out_Q13.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. Non-proof-attempt batch, dominated
by the SL₂-word / continued-fraction / thin-orbit / numerical-semigroup analogy line. About 54 rows are calibration, local-layer or tooling, handled briefly.
**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 1 | 0 | 0 | 62 | 63 |
| known-false | 25 | 0 | 0 | 0 | 25 |
| circular | 12 | 0 | 0 | 0 | 12 |
| unclear | 9 | 2 | 0 | 0 | 11 |
| open-plausible | 0 | 1 | 1 | 0 | 2 |
Novelty: 0 → 58, 1 → 55, 2 → 0. Plaus-3 rows are calibration, local (mod q) statements or main terms (yield none).
**Plausibility ≥ 2 AND novelty ≥ 1 with any yield beyond calibration**: none. The one plaus-2 open row, **Z1762** (*the limit shape of certificate
locations for almost all p*), is B6 and distributional. The only open row with an ES yield is **Z1298** (*the Pell/reduction cycle of ℚ(√p)
contains a root yielding a bichromatic forest edge*; plaus 1, novelty 0). It is FRONTIER §7.2's listed lead, and its `next` has a cheap falsifier
on the 14 (★)-sterile primes and 2521.
**Recurring missing theorems**
1. *Local ⇒ integral for fixed-length SL₂ words* (known-false by T1: short words are already locally full mod q, so the gap is integral):
   Z0641, Z1700, Z1654, Z2503; local-layer calibrations Z2150, Z2265, Z2279, Z2455, Z2592, Z2593, Z1005, Z1092, Z1156.
2. *Thin-orbit / expansion / equidistribution transfer* (B3/M1a; fixed length 3 means a polylog count): Z0476, Z0523, Z1704, Z2456, Z2521, Z2253,
   Z2276, Z2458, Z1730, Z2046, Z2275, Z0204; Z2283 (*bounded alphabet + length 3 ⇒ bounded p*, trivially false).
3. *Restatements of (★)/ES₅* (circular): Z0166, Z0178, Z0180, Z0640, Z1462, Z1499 (SL₂ form), Z1970/Z1974/Z2006 (k-Frobenius numbers of
   ⟨4Cu, 4CB, u + B⟩: the semigroup universality theorem's freedom is exactly the M4 input ES lacks), Z1738 (×a×b → C_min window), Z1899 (genus split).
4. *Mutation / Vieta / closure / involution* (multilinear: no second root; reachability ≠ existence; M5/T1 for parity): Z0987, Z2055, Z2259,
   Z1017, Z3187, Z0556, Z1977, Z1004.
5. *Chain world = Engel length 3* (P00 Z0216 criterion; fails on a half-dimensional sieve set): Z0152, Z1461, Z1742.
6. *Bounded procedures / identity families / finite partitions* (B1): Z1159, Z1160, Z2542, Z1612, Z2359, Z2144 (H4_NOT_POLYLOG).
**New in this pass**
* **Z1007/Z0838 correction.** Pass 1's 'five-slice' helper (`scripts/z52b_p1_U06_e.py`, `cf_len` counts the leading 0) counts
  {A : regular CF of A/p has ≤ 2 non-zero quotients} = {1} ∪ divisors of p − 1, not ES₅ certificates. The "47 % all-even" parity bias is
  divisor parity of p − 1 = 2^k m′: the share (k − 1)/(k + 1) averages ≈ 0.47. Z0838's Spearman 0.049 is τ(p − 1)-type vs U and says nothing about ES₅.
* **Z0977 (elementary).** 'x succeeds' means (px)² has a divisor ≡ −px (mod 4x − p), which depends on p (shared) and the factorisation of x.
  Consecutive x are coprime, so neighbouring trials share no prime factors beyond p, and the 'coupling' idea dies by privacy.
* **Z1977.** The denumerant involution n ↦ g_t − n is centred at the unknown certificate g_t(u, v) = p, so it cannot seed a windmill.
* **Z3192.** Compactness via limiting divisor-class measures fails twice. For fixed K, avoiding limits exist under H. For growing K, a certificate is
  an atom of vanishing mass, invisible to weak limits.
**Assessment.** The SL₂/CF/thin-orbit analogies all land on one dichotomy: their pointwise theorems use power-size orbits or a free choice of
objects (M1a/M4), while ES₅ is a fixed-length, polylog-count, locally unobstructed event (T1/B3). The only listed lead is Pell/cycle data (§7.2).
