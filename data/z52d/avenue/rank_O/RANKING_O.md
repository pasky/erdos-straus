# z52d avenue layer — independent ranking and negative audit (reviewer O)

ES is OPEN. Labels as in FRONTIER. Inputs: `out_*.jsonl` (2,995 rows; PILOTH excluded), `master.jsonl`, FRONTIER §§1–4, 6, 7.
Files: `negsample.json` (seed, allocation), `negaudit.jsonl`, `F.jsonl`, `clusters.json`; scripts `scripts/z52d_rank_O_*`.
This revision follows a cross-model review of the first version; the changes are in the git log.

## A. Negative audit (Assessment; small EVIDENCE checks)

**Pool.** Rows with status ∈ {circular, known-false, harder-than-open} and plausibility 0: **1,308 rows** (688 kf, 599 circ, 21 hto).
**Sample.** 40 rows, seed 520411, stratified by batch: largest-remainder allocation proportional to each batch's pool count
(28 batches, 1–2 rows each), uniform within each batch. This gives 22 kf, 14 circ, 4 hto. Each row was re-derived from its master item.

| verdict | n | mids |
|---|---|---|
| holds | 32 | see negaudit.jsonl (4 of these — Z1925, Z0379, Z1080, Z2748 — rest on CONDITIONAL results (H, Dickson, GRH); the label should say so) |
| partly: conclusion right (plausibility 0), but the status label/reason is not established | 7 | Z1304 (Brandt matrices are *untested* in redteam-automorphic-2, and an entry is class-level) · Z1714 (no candidate map; B3 only for the equidistribution variant) · Z1344 (privacy is an Assessment) · Z1674 (U_n ≅ U_1 over ℚ kills rank arguments, not integral ones) · Z1690 (ratio set p^{o(1)}: BGK inapplicable ≠ refuted) · Z2742 (B3 refutes only the power-size encoding) · Z0703 (a calibration statement, not circular) |
| **wrong: corrected plausibility ≥ 1** | 1 | **Z3022** (Graham-type affine closure maps). B1/Mordell–Schinzel was cited, but closure used with strong induction runs to depth ≍ log p, outside B1 Thm M. T1 does not bind solvability, since ES(m²) holds by scaling (it still binds Type I/II-preserving transports). Corrected status: unclear, plausibility 1, no handle |

* **The kill list's verdicts are reliable; its labels are not.** No real avenue (corrected plausibility ≥ 2) was found in the
  sample: 0/40. The binomial 95 % upper bound is 8.8 %; the design is stratified, so read it as approximate. One verdict was
  wrong in a way that changes plausibility: 1/40, 2.1 % population-weighted, about 27 of the 1,308 rows. It is still not an
  avenue. Labels are overstated (Assessment or "architecture inapplicable" reported as known-false/circular) in 8/40 rows,
  ≈ 20 % weighted. A small sample cannot show that nothing is hidden; it shows that buried avenues are rare.
* **Targeted hunt** (outside the random sample). Closure/induction rows citing B1 or the "thin polynomial image": Z3016, Z3187,
  Z3115 and Z0223 repeat Z3022's flaw. The image argument is wrong for strong induction from *all* smaller n, and the valid bar
  (privacy) is an Assessment. Corrected status: open, plausibility 0–1. They are added to F and to cluster C10.
* **Spot checks** (EVIDENCE/by hand). Re-derived: the Z0703 Type I size lemma (a ≥ (3p+1)/4) and the Z1454 conic-bundle identity.
  Re-checked numerically: the Z0866 lemma "Type I is never primitive at p ≡ 1 (4)" (0 of 439 Type I solutions, p < 400).

## B. Candidate set F and clusters

F (`z52d_rank_O_F.py`) is the union of four criteria:

| criterion | rows |
|---|---|
| c1: plausibility ≥ 2, novelty ≥ 1, yield ≠ none | 33 |
| c2: ES-yield, status open/unclear/known-true, plausibility ≥ 1 | 76 |
| c3: new_ingredient ≠ none | 18 |
| c4: overturned (Z3022 + 4 from the targeted hunt) | 5 |

**|F| = 119.** F has 79 ES-yielding rows: 70 at plausibility ≤ 1 and 9 known-true *restatements*. The 119 rows collapse onto
**23 clusters** (`clusters.json`), with every F mid in exactly one cluster.

**Scoring (explicit).**
* EV = Y·P.
* Y: full ES 1.0 · a pointwise sub-step a proof would need 0.3 · side result (thin family, average, main term) 0.03 · none or superseded 0.
* P, from my plausibility: 0 → 0, 1 → 0.01, 2 → 0.1, 3 → 0.4. ES-strength statements (statements implying ES for large p) get
  P = 0.002 if their plausibility is ≥ 1.
* Ties are broken by h (handle: 0 none, 1 formal escape of the named obstruction, 2 a specific ingredient), then by f (a cheap
  falsifier exists).
* Tier (ii) is ordered by hand: P(provable in about a week) × calibration value / cost.

### (i) Could be part of a proof of ES — every cluster is at plausibility ≤ 1
| # | cluster (members) | FRONTIER | EV, h, f | obstruction → does a member beat it? |
|---|---|---|---|---|
| 1 | **C1** cancellation on the height-tied hyperbola (Z1034 Z1855 Z2997 Z0211 Z1480 Z2958 Z3149) | §7.1 verbatim | .003, 1, 1 | tied modulus; B3 for the full form → no; only the coupling C = (xy−1)/4p is unexploited |
| 2 | **C3** parity/involution/topological index (14 rows, e.g. Z2921 Z1386 Z3101 Z3094 Z2764 Z2765) | §6 (J)2 (finite affine menus) | .002, 1, 1 | M5/T1 → formal handle only (below) |
| 3 | **C14** class forcing beyond parity (Z2818 Z1649 Z2534 Z1954 Z0250) | §7.6, §7.7 | .002, 1, 1 | CLASS_FORCING 2.1 → partly (below) |
| 4 | **C4** Pell/reduction-cycle/E2 primitives as forest roots (Z0596 Z0465 Z1298 Z0385 Z1687 Z1048 Z0378) | §7.2 Astra question | .002, 0, 1 | B2 per root → formal escape only (below) |
| 5 | **C2** one-coordinate polylog window: HC, least level, Vmin, u_min (11 rows) | §7.2 | .002, 0, 1 | Landau-type lower tail → no; useful as a falsification target |
| 6 | C9 regime split / exceptional character (Z2940 Z3003 Z2941 Z2512 Z3002 Z2964 Z1787) | → §7.3/§7.4 | .002, 0, 1 | B2 per regime; B1 for congruence splits → no |
| 7 | C20 high-multiplicity lift (Z2060) | B3 Rem. 2.4 hatch | .002, 0, 1 | no candidate lift |
| 8 | C15 amplified second moment on a polylog family (Z2982) | §6 fixed-p variance | .002, 0, 1 | B6 at polylog scale |
| 9 | C10 propagation/closure/induction (Z2095 Z2809 Z1153 Z3028 Z3005 Z2351 Z3022 Z3016 Z3187 Z3115 Z0223) | §6 (rule Λ, Y–Δ open) | .002, 0, 1 | privacy + numerator 8 (8/131) → no |
| 10 | C16 positivity of exact expressions (Shintani ζ(0), interlacing; Z2845 Z3104) | §6 exact identities | .002, 0, 1 | T1 + spin event |

Notes on the handles:
* **C3.** The handle is formal only. The 4-rank of Cl(−4p) is congruential, but 8 | h(−4p) ⟺ p = x² + 32y² (Barrucand–Cohn) is
  a non-abelian Chebotarev condition, and the 16-rank has no governing field. These are non-congruential parity sources, though
  (J)96 calls non-abelian Frobenius inert on finite witness sets. Separately, Z3101's ℤ/m actions (m > 2) are not covered by (J)2.
* **C14.** Lucas primitive divisors cut the class to ±1 (Z1954). This is the only class-level forcing among the 2,995 rows, but it
  does not reach integers linear in p.
* **C4.** The cycle escapes B1 Thm M and the (J)106 root constructions, but only for long-period p. **The period of √p is not
  uniformly power-size**: it is O(1) at p = m² + 1 or m² + 4, and near-square primes are the hardest ones. There, cycle data form a
  fixed polynomial recipe in m, which is B1-exposed under Hypothesis H.

C9 diagnostic (`z52d_rank_O_charobs.py`; EVIDENCE, limited). Inputs: 9 (★)-zeros (409 … 712321), 3 distinct controls each, Type II
e-slices with e ≤ 400.
* About half of the obstructed windows are poverty-type: −1 lies in ⟨factors⟩ but not in the ratio set.
* Subgroup-type windows are almost all killed by an **odd real (genus) character** mod e, mostly χ_{−e} itself (= Jacobi (·/e)).
* Windows killed only by characters of order ≥ 3 number 0–3 per prime, at hard primes and controls alike.
* At 5569, 83449, 102001 and 712321 the extra subgroup-type windows lie in the real-character layer.
* The diagnostic does not measure the Z3003 Fourier products or look for characters shared across windows, so it does **not**
  falsify C9. It does point the cluster at the genus layer (§7.3/§7.4) rather than at an exceptional higher-order character.

### (ii) Side theorems worth a depth lane (cheap / provable / calibrating)
1. **C6** thin exponential families (Z2969 Z3189 Z0417 Z2031 Z2995 Z2776 Z1557; §7.8, §7.17). Plausibility 2. A recursion in s
   escapes the finite-covering no-go. Calibration only: (J)84 Thm A blocks transfer to primes.
2. **C13** primitive ES (Z0866; not in FRONTIER). Structure lemma PROVED (elementary) and re-checked here: primitive ⟺
   p = 4ab − (a+b)/m. It is the k ↔ m dual of (★). Cheap census; a cleaner ES-strength target.
3. **C8** explicit constants (Z2418 Z2858 Z2901 Z2551). Plausibility 3. Bookkeeping, needed for any "large p + finite check".
4. **C17** numerator 9 (Z0735): either a finite covering with exceptions {2, 5, 11, 19} or a sterile point. Decides whether B1 is
   "exactly T1" for one numerator.
5. **C5** local-factor floor inf F(p) > 0 at pseudosquare-type p (Z0671 Z2000 Z2981; §2.2). Main term only.
6. **C7a** non-CRT bilinear exceptional set (Z2356; §7.12). The one row aimed at the 3/4 cap. Plausibility 1.
7. **C7b** almost-all ES on primes a² + b⁴ and (★)-primes in x^{0.525}-intervals (Z0240 Z2947). Provable; B6.

Cheap closing lemmas worth a few hours: extend (J)2 to ℤ/3 and S₃ (Z3101); "equivariant transport factors through the trace"
(Z0338). Aside to C1: a pointwise upper bound R(p) ≪ p^{2/5−δ} via the determinant method (Browning–Elsholtz line) is a
plausibility-2 side theorem. It counts rather than cancels, so it is worth nothing for ES.

### (iii) The rest
* C18 growing-length digit recursion (Z0482). Its proposed Cobham closing lemma is unsupported: growing registers are not
  finite-state.
* C12 relaxation→transport (Z0084 Z0091 Z0338 Z0424).
* C19 Question R (Z0416; §7.11): needs power-size orbits.
* C11 restatements (10 rows: torsor/Cox, BM, U_n ≅ U_1, singular series, thin orbits).
* C7c moments/positive proportion: superseded.
* C7d other averaged inputs (14 rows): superseded or capped at 3/4.

## C. Depth-lane plans

Plans cover the top five tier-(i) clusters plus the top side lane. C9, C20 and the rest have no concrete first lemma.

**C1 (hyperbola cancellation).**
* *First lemma.* In the balanced block u, B ~ p^{1/4}, N(U,V) = #{4uB | p+u+B} has trivial bound p^{1/4+o(1)} (for each u, B | p+u)
  against an O(1) heuristic mean. Expand with additive characters mod 4uB and attempt a bilinear dispersion in (u, B). This is the
  one range where both factors of the modulus vary and neither equals p.
* *Falsifier.* For ~10⁴ primes near 10¹², compute the block errors N − M_F, their variance against Poisson, and their correlation
  with F(p).
* *Paper.* PARITY_AUDIT §2–3; Shparlinski's modular-hyperbola survey, Thm 13.
* *Changes the picture.* A proved saving on one block at one p would be the first class-aware single-integer input. A scoped
  no-go (the dual is at least as long as the original, Z1034) would demote §7.1's "only lead not ruled out".

**C3 (parity).**
* *Lemma.* Does (J)2 Thm 6.1 extend verbatim to ℤ/3 and S₃ actions by finite affine menus? If so, every finite-group affine menu
  is closed.
* *Falsifier.* For p ≡ 1 (24) < 10⁵, correlate [8 | h(−4p)] and h(−4p) mod 16 with certificate parities (R(p)/2, f_II/6, the
  number of bichromatic forest edges, each mod 2), after conditioning on p mod 16.
* *Changes the picture.* A correlation would be the first M5 input that sees more than congruence data.

**C14 (class beyond parity).**
* *Search.* Look for an identity making 4Cp+1 (C = 2, 3, 4) a value or a factor of U_{4C}(P, Q) with P, Q polynomial in p.
  Without one, the Lucas ±1 reduction never reaches the ES integers.
* *Then.* Test the joint-Frobenius properties 𝒜 (Z2818) against AMPLIFY_EXCEPTION Thm 3.2's adversary at the T1 point.
* *Changes the picture.* Such an identity would be a class-level forcing mechanism. FRONTIER says none exists.

**C4 (cycle roots).**
* *Lemma first.* For p = m² + 1 or m² + 4, the cycle is O(1)-long and polynomial in m. Show, under Hypothesis H, that infinitely
  many such primes defeat every cycle root (a (J)106-type construction). If this works, C4 is dead on its hardest primes.
* *Falsifier.* On the (★)-zeros, {5, 13, 17, 2521}, 3361, and ≥ 50 primes p = 2521 + 9240a with (p+11)/12 prime, against 200
  controls: use each P_k, Q_k of √p as a forest root and test for a bichromatic edge within depth 2. Report the per-element hit rate
  against random roots. Do not use the cycle-centre two-squares p = a² + b² ((J)3, dead).
* *Changes the picture.* A hit rate that does not drop on the Dickson family, *and* survival of the near-square lemma, would make
  the cycle the first p-dependent root source to survive (J)106.

**C2 (one-coordinate window).**
* *Lemma.* Extend H4_NOT_POLYLOG's construction (energy lemma + Gallagher) from both endpoints to one coordinate (HC(p) or the
  least level).
* *Computation.* Record growth by decade to 10⁹, and fit log log p against (log p)^A.
* *Changes the picture.* If the extension works, §7.2 loses its last polylog target. If it fails, the step that fails is the only
  structural reason a one-coordinate window might be polylog.

**C6 (side: 15·2^s + 1).**
* Run Berlekamp–Massey on the *proof* certificates of 3·2^s+1 and 63·2^s+1, per residue class of s. If they are recurrent, search
  the same template on the open u ≡ 7 (8) branch, s ≤ 80.
* In parallel, run the I3_DEEP exponent-covering harness on 3^k ± 2.
* *Outcome.* A closed §7.8 or §7.17 family: calibration only, no transfer.

## D. Bottom line (Assessment)

* **This layer contains no ES avenue at plausibility ≥ 2.** Each ES-yielding cluster reduces to the B2 single-integer lower tail
  or to one of its faces (§7.1, §7.2, §7.3), or it lacks any mechanism.
* The negatives are sound as verdicts: 0/40 real avenues buried, 1/40 plausibility-changing error (Z3022, still implausible).
  The cost of the kill list is label inflation (~20 %): Assessments and "method inapplicable" are written as refutations.
  A downstream user should read "known-false" as "dead by the cited argument or by Assessment", not as a theorem.
* C1 ranks first only because its first step is not ES-strength; it has no handle. The most productive use of depth lanes is
  **falsification**: the C4 near-square lemma, the C2 one-coordinate extension of H4_NOT_POLYLOG, and the C3 (J)2 extension
  plus the 2-power parity test. Each could support or remove a §7 entry. The side lanes C6, C13 and C8 are the most likely to
  yield theorems; none of them moves ES.
