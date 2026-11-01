# z52d avenue layer — independent ranking and negative audit (reviewer O)

ES is OPEN. Labels as in FRONTIER. Inputs: `out_*.jsonl` (2,995 rows; PILOTH excluded), `master.jsonl`, FRONTIER §§1–4, 6, 7.
Files: `negsample.json` (seed, allocation), `negaudit.jsonl`, `F.jsonl`, `clusters.json`; scripts `scripts/z52d_rank_O_*`.

## A. Negative audit (Assessment, with two small EVIDENCE checks)

**Pool.** status ∈ {circular, known-false, harder-than-open} with plausibility 0: **1,308 rows** (688 kf, 599 circ, 21 hto).
**Sample.** 40 rows, seed 520411, largest-remainder allocation proportional to each batch's pool count (28 batches, 1–2 per
batch), uniform within each batch → 22 kf, 14 circ, 4 hto. Each row re-derived from its master item, not from the row's prose.

| verdict | n | mids |
|---|---|---|
| holds | 35 | (see negaudit.jsonl) |
| partly: verdict right, reason or label wrong | 4 | Z1304 (Brandt *entry* is class-level, so the reason is not "genus layer"; the right kill is B2 Thm 2.2(i)); Z0703 (not equivalent to ES; it is a *strengthening* of Type II existence, so "harder-than-open"); Z1344 (the privacy lemma is Assessment-level, so "known-false" is overstated); Z1714 (it is a B2 slice, not known-false) |
| **wrong** | 1 | **Z3022** (Graham-type affine closure maps): B1/Mordell–Schinzel was cited, but closure used with strong induction runs to depth ≍ log p, so B1 Thm M does not apply. T1 does not bind either, since ES(m²) holds by scaling. Should be: unclear, plausibility 1 |

* **False-negative rate (strict: verdict wrong *and* corrected status non-negative): 1/40 = 2.5 %** (95 % Clopper–Pearson
  0.06 %–13 %; ≈ 33 rows of the 1,308 if extrapolated, plausibly 1–170). The corrected Z3022 is still not a real avenue
  (plausibility 1, no candidate map). **Rate of real avenues buried as negatives: 0/40** (upper 95 % bound 8.8 %).
* Label hygiene: 5/22 known-false verdicts rest on CONDITIONAL results (H, Dickson, GRH: Z1925, Z0379, Z1080, Z2748, Z1118),
  but the label does not say so. "Circular" is used loosely for "ES-strength sufficient condition", e.g. Z0726 12/p and
  Z2123 (★) in a sub-range. Neither problem changes a ranking.
* Targeted FN hunt (not part of the random sample): I searched the pool for closure/induction architectures cited to B1.
  Z3016, Z3187, Z3115 and Z0223 repeat Z3022's flaw: the "thin polynomial image" argument is wrong for strong induction from
  *all* smaller n. The valid bar is privacy (affine shifts do not transport divisors). That bar is only an Assessment, so
  these rows should read "open, plausibility 0–1", not known-false. They form cluster C10 below.
* Spot checks (EVIDENCE): the Z0703 Type I size lemma (a ≥ (3p+1)/4) and the Z1454 conic-bundle identity were re-derived by hand;
  the Z0866 lemma "Type I is never primitive at p ≡ 1 (4)" was re-checked: 0 of 439 Type I solutions with p < 400 are primitive.

**Verdict:** the avenue pass's negatives are reliable for ranking purposes. The kill list is not hiding avenues. Its main
defect is that it overstates its labels (Assessment/CONDITIONAL reported as "known-false").

## B. Candidate set F and clusters

F (script `z52d_rank_O_F.py`): c1 (plausibility ≥ 2, novelty ≥ 1, yield ≠ none) 33; c2 (ES-yield, status open/unclear/known-true,
plausibility ≥ 1) 76; c3 (new_ingredient ≠ none) 18; c4 (overturned) 1 → **|F| = 115** (63 open-plausible, 25 unclear, 24 known-true,
3 known-false). No F row has an ES-yielding missing theorem with plausibility ≥ 2 except 9 known-true *restatements*.
The 115 rows collapse onto **23 clusters** (`clusters.json`; every F mid in exactly one).

**Scoring (explicit).** EV = Y·P. Y: full ES 1.0 · pointwise sub-step that a proof would need 0.3 · side (thin family,
average, main term) 0.03 · none or superseded 0. P from my plausibility: 0 → 0, 1 → 0.01, 2 → 0.1, 3 → 0.4. ES-strength statements
(statements implying ES for large p) get P = 0.002 when their plausibility is ≥ 1. Ties are broken by h (handle: 0 none,
1 formal escape of the named obstruction, 2 a specific ingredient that plausibly beats it), then by f (a cheap falsifier exists).
Tier (ii) is ordered by hand: P(provable in about a week) × calibration value / cost.

### (i) Could be part of a proof of ES — all at plausibility ≤ 1
| # | cluster (members) | FRONTIER | EV, h, f | obstruction → does a member beat it? |
|---|---|---|---|---|
| 1 | **C1** cancellation on the height-tied hyperbola (Z1034 Z1855 Z2997 Z0211 Z1480 Z2958 Z3149) | §7.1 verbatim | .003, 1, 1 | tied modulus; B3 for the full form → no; only the coupling C = (xy−1)/4p is unexploited |
| 2 | **C4** Pell/reduction-cycle/E2 primitives as forest roots (Z0596 Z0465 Z1298 Z0385 Z1687 Z1048 Z0378) | §7.2 Astra question | .002, 1, 1 | B2 per root; escapes B1 Thm M and the (J)106 Dickson root constructions formally (power-size p-dependent root set, M1b-like) |
| 3 | **C3** parity/involution/topological index (14 rows: Z2921 Z1386 Z3101 Z3094 Z2764 Z2765 …) | §6 (J)2 (finite affine menus) | .002, 1, 1 | M5/T1 → formally: the 4-/8-rank of Cl(−4p) is a non-congruential parity source, but no member uses it; Z3101's ℤ/m (m > 2) actions are not covered by (J)2 |
| 4 | **C14** class forcing beyond parity (Z2818 Z1649 Z2534 Z1954 Z0250) | §7.6, §7.7 | .002, 1, 1 | CLASS_FORCING 2.1 → partly: Lucas primitive divisors cut the class to ±1 (Z1954); the only class-level forcing in 2,995 rows, but it does not reach integers linear in p |
| 5 | **C2** one-coordinate polylog window: HC, least level, Vmin, u_min (11 rows) | §7.2 | .002, 0, 1 | Landau-type lower tail → no; useful as a falsification target |
| 6 | C20 high-multiplicity lift (Z2060) | B3 Rem. 2.4 hatch | .002, 0, 1 | no candidate lift exists |
| 7 | C15 amplified second moment on a polylog family (Z2982) | §6 fixed-p variance | .002, 0, 1 | B6 at polylog scale |
| 8 | C10 propagation/closure/induction (Z2095 Z2809 Z1153 Z3028 Z3005 Z2351 Z3022) | §6 (rule Λ, Y–Δ open) | .002, 0, 1 | privacy + numerator 8 (8/131) → no |
| 9 | C16 positivity of exact expressions (Shintani ζ(0), interlacing; Z2845 Z3104) | §6 exact identities | .002, 0, 1 | T1 + positivity is the spin event |
| 10 | C9 regime split / exceptional character (Z2940 Z3003 Z2941 Z2512 Z3002 Z2964 Z1787) | → §7.3 | .002, 0, 0 | **falsified (EVIDENCE, this review)**: see below |

C9 falsifier (`z52d_rank_O_charobs.py`; EVIDENCE): I took 9 (★)-zeros (409 … 712321), 3 size-matched controls each, and
Type II e-slices e ≤ 400. About half of the obstructed windows are poverty-type (−1 lies in ⟨factors⟩ but not in the ratio set).
The subgroup-type windows are mostly killed by the quadratic genus/BM character χ_{−e}. Non-quadratic subgroup obstructions
show **no excess at hard primes** (3–12 per prime vs 4–10 in controls). Where hard primes do show excess (83449, 102001, 712321),
it lies in the quadratic layer. So no exceptional character exists beyond the BM layer,
which is already pointwise free; out_Q11 Z1596 agrees (179/183 rich (★) failures are poverty-type). C9 therefore collapses
into §7.3.

### (ii) Side theorems worth a depth lane (cheap / provable / calibrating)
1. **C6** thin exponential families (Z2969 Z3189 Z0417 Z2031 Z2995 Z2776 Z1557; §7.8, §7.17). Plausibility 2. A recursion in s escapes the
   finite-covering no-go. Calibration only: (J)84 Thm A blocks transfer to primes.
2. **C13** primitive ES (Z0866; not in FRONTIER). Structure lemma PROVED (elementary) and re-checked here: primitive ⟺
   p = 4ab − (a+b)/m. This is the k ↔ m dual of (★). Cheap census; it gives a cleaner ES-strength target.
3. **C8** explicit constants (Z2418 Z2858 Z2901 Z2551). Plausibility 3. Bookkeeping, needed for any eventual "large p + finite check".
4. **C17** numerator 9 (Z0735): a finite covering with exceptions {2, 5, 11, 19}, or a sterile point. Decides whether B1 is "exactly T1".
5. **C5** local-factor floor inf F(p) > 0 at pseudosquare-type p (Z0671 Z2000 Z2981; §2.2). Main term only.
6. **C7a** non-CRT bilinear exceptional set (Z2356; §7.12). This is the one row aimed at the 3/4 cap. Plausibility 1.
7. **C7b** almost-all ES on primes a² + b⁴ and (★)-primes in x^{0.525}-intervals (Z0240 Z2947). Provable; B6.
8. **C18** Cobham closing lemma for growing-length digit recursions (Z0482). Also cheap closing lemmas: (J)2 → ℤ/3, S₃ (Z3101),
   and "equivariant transport factors through the trace" (Z0338).
Also (aside to C1): a pointwise upper bound R(p) ≪ p^{2/5−δ} by the determinant method (Browning–Elsholtz line) is a
plausibility-2 side theorem. It counts and does not cancel, so it is worth nothing for ES.

### (iii) The rest
C12 relaxation→transport (Z0084 Z0091 Z0338 Z0424) · C19 Question R (Z0416; §7.11, needs power-size orbits) · C11 restatements
(torsor/Cox/BM/U_n ≅ U_1/singular series/thin orbits; 10 rows) · C7c moments/positive proportion (superseded) · C7d other averaged
inputs (14 rows; superseded or capped at 3/4).

## C. Depth-lane plans (top tier-(i) clusters + the top side lane; C20 skipped, since there is no candidate to work on)

**C1 (hyperbola cancellation).** *First lemma:* take the balanced block u, B ~ p^{1/4}. There
N(U,V) = #{4uB | p+u+B} has trivial bound p^{1/4+o(1)} (for each u, B | p+u) against an O(1) mean. Expand with additive
characters mod 4uB and attempt a bilinear dispersion in (u, B). This is the one range where both factors of the modulus vary
and neither is p. *Falsifier:* for ~10⁴ primes near 10¹², measure N(U,V) − M_F(U,V) per block and its variance against Poisson,
and its correlation with the local factor F(p). If the error is a local-factor effect, the target must be re-stated relative to M_F.
*Paper:* PARITY_AUDIT §2–3 and Shparlinski's modular-hyperbola survey, Thm 13. *Changes the picture:* any proved saving on one
block at one p would be the first class-aware single-integer input. Alternatively, a scoped no-go (the dual is at least as long
as the original sum, Z1034) would demote §7.1 from "the only lead not ruled out".

**C4 (cycle roots).** *Falsifier first:* for the (★)-zeros, the ES₅ zeros {5, 13, 17, 2521}, 3361, and ≥ 50 Dickson-constructed primes
p = 2521 + 9240a with (p+11)/12 prime (where least-QNR roots fail), versus 200 controls: walk the CF period of √p and use each
P_k, Q_k (and |P_k² − pQ_k²| only in the non-coprime case) as a forest root. Record whether a bichromatic edge lies within depth 2.
Report the hit rate per cycle element against random roots of equal size. Do not reuse the cycle-centre two-squares
p = a² + b² (dead: (J)3). *Lemma:* does Legendre's descent (as for N(ε_p) = −1) force any factorisation of p + u + v for u, v in
the cycle? *Changes the picture:* an undiminished hit rate on the Dickson family would make the cycle the first p-dependent root
source that survives the (J)106 constructions. A zero or decaying rate closes §7.2's Astra question in evidence.

**C3 (parity).** *Lemma:* extend (J)2 Thm 6.1 from involutions to ℤ/3 and S₃ actions by finite affine menus (Z3101). If the
proof goes through verbatim, every finite-group affine menu is closed. *Falsifier:* for p ≡ 1 (24) < 10⁵, correlate the 4- and
8-rank of Cl(−4p) with natural certificate parities (R(p)/2, f_II/6, the number of bichromatic forest edges, each mod 2), after
conditioning on p mod 16. *Changes the picture:* any correlation would be the first M5 input that sees more than p mod M.

**C14 (class beyond parity).** *Search:* look for an algebraic identity making 4Cp+1 (C = 2, 3, 4) a value or a factor of
U_{4C}(P, Q) with P, Q polynomial in p. Without one, the Lucas ±1 reduction never reaches the ES integers. Then test the
candidate joint-Frobenius properties 𝒜 (Z2818) against AMPLIFY_EXCEPTION Thm 3.2's adversary at the T1 point.
*Changes the picture:* an identity would be a class-level forcing mechanism, which FRONTIER says does not exist.

**C2 (one-coordinate window).** *Lemma:* extend H4_NOT_POLYLOG's construction (energy lemma + Gallagher) from both endpoints to
one coordinate (HC(p) or the least level). *Computation:* compute record growth of HC, the least level over all lines and Vmin by
decade to 10⁹, and fit log log p against (log p)^A. *Changes the picture:* if the extension works, §7.2 loses its last polylog
target. If it fails, the failing step is the only structural reason a one-coordinate window might be polylog.

**C6 (side: 15·2^s + 1).** Run Berlekamp–Massey on the *proof* certificates of 3·2^s+1 and 63·2^s+1, per residue class of s. If they
are recurrent, search the same template on the open u ≡ 7 (8) branch of 15·2^s+1 for s ≤ 80. In parallel run the I3_DEEP
exponent-covering harness on 3^k ± 2. *Outcome:* a closed §7.8 or §7.17 family, which is calibration and does not transfer.

## D. Bottom line (Assessment)

* **There is no ES avenue in this layer at plausibility ≥ 2.** F has 79 ES-yielding rows. 70 of them have plausibility ≤ 1. The other 9
  are restatements, "known-true" only as dictionaries. Every
  cluster that yields ES reduces to the B2 single-integer lower tail, or to its §7.1/§7.2/§7.3 faces.
* The negatives are sound: 0/40 real avenues were buried, and 1/40 rows were mislabelled (Z3022, still implausible). The cost of
  the kill list is label inflation, not lost avenues.
* Best expected value for ES is C1. It ranks first only because its first step is not ES-strength, and it has no handle.
  The productive use of depth lanes is **falsification**: C4 (cycle roots on Dickson-sterile primes), C2 (one-coordinate
  extension of H4_NOT_POLYLOG) and C3 (rank parity). Each of these can remove an open item from §7 within a day. The side
  lanes C6, C13 and C8 are cheap and will produce theorems, but none of them moves ES.
