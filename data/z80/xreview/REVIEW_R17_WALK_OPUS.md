# Hostile cross-lab review of `notes/z80/R17_WALK.md` (commit 21787d85f, diff 36dcbec35..21787d85f)

**Reviewer.** Claude (Anthropic), running as a Claude Code subagent ("Opus" cross-lab slot). I cannot read an exact model
version from inside the session. **Author lane:** GPT-6.2 Astra. Nothing was committed by the reviewer.

## 0. Verdict and exact scope

I found **no soundness defect** in any decisive new stage. Every new Round-2 certificate replays byte-identically from
the author's engines. I independently re-implemented, or re-ran through a second independent engine, every decisive
new count. In every case I obtained the same counts or the same empty result, including under alternative cutoffs and
partitions. Subject to the form fixes in §2, the following claims stand:

1. **Positive sterile measure on the r-generic line at r = 83 and r = 73.** Combined with Round 1 this means every prime
   r ≥ 83, plus 73. The ledger margins are 19111 ppm at 83 and 18189 ppm at 73. Label: PROVED, relative to SE §3.1,
   the z78/z79 ledger lemmas (including BBR), the inherited large-shift tables and the r ≥ 919 libm qualification; it
   is computer-assisted. The primes 79 and 17..71 remain open. Nothing here concerns ES in ℕ.
2. **At r = 17 the endpoints 5 and 1/5 have no P hit at L = 15, 16 and no Q hit at any odd k ≤ 39.** Together with the
   inherited P certificate through L = 14, this gives survival of the two *points* through depth 16, and avoidance of
   Q through odd level 39. Label: CERTIFIED. It is not all-depth survival and not survival of a cylinder.
3. **The rational Vieta bound on d.** Every Q hit of x = 5 or 1/5, at every depth and for any modulus F, satisfies
   d ≤ min_m dcut(F, m). Label: PROVED; I re-derived it (§3.1).

The weakest points are in §5. Both passes rest decisively on inherited large-shift tables, which were replayed in
earlier rounds but not re-implemented here. They also rest on load-bearing files that are still labelled as reviewer
experiments (F1).

## 1. Coverage

| stage | author replay (byte-diff) | independent work by reviewer | result |
|---|---|---|---|
| `layers`: P₁₁ prefix (`z80_fullprefix.c`), 7 primes × 4 windows | ✔ all 28 rows identical | ✔ new engine `scripts/z80_xr_p11.c`, all 8 **decisive** windows (73, 83) | identical (5942/104/46/44; 21710/98/52/40) |
| P₁₁ truth mode | — | exhaustive H_e and genuine tuples, e < 2²², r = 13, 17, 59, 73, 83 | centres ≤ #H_e ≤ bound for every e |
| `layers`: shift33 (inherited `z79_shiftwide.c`), 14 rows | ✔ all 14 identical | — (inherited engine; replayed **all** rows, not rewritten) | — |
| `layers`: shift35, 10 rows | ✔ all 10 identical | — (replay only) | not load-bearing for any pass |
| `local`: pshift P₉ rows at 59..83 (`xr_prefix_lo`) | ✔ identical | (author engine, independently reimplemented in the Round-1 review) | — |
| `local`: CF P₉ rows at 59..83 (`xr_cf_lo`, reviewer engine) | ✔ identical | ✔ re-ran the **author's** `z78_r2cf.c` at all 7 primes | identical (294, 222, 340, 196, 180, 128, 186) |
| `local`: `z80_budget2.py` → `local.txt`, `z80_crush_checks.py` | ✔ identical, checks pass | ablation/sensitivity harness `scripts/z80_xr_walk_ablate.py`; route probe `scripts/z80_xr_walk_probe.py`; re-derived `z80_mid.py` | §3.4–3.5 |
| `qwalk` (`z80_qwalk.py 39`) | ✔ identical | ✔ `scripts/z80_xr_qwalk.py`: independent cutoff, p-adic exponent square roots, separately coded branches; brute force; lemma stress tests | identical D, pairs and 0 hits for all 20 odd k ≤ 39 |
| `p15` (`z80_ep15.c` e, HZ; `z80_epfast.c` J, Hd) | ✔ identical (629 s) | ✔ alternative partition (E, J₀, V, Y) = (20000, 5·10⁷, 200, 10¹⁰), split σ = 20: own J/Hd engine `scripts/z80_xr_ep.c`, own e/HZ `scripts/z80_xr_ehz.py` (sympy factorint, not GNU factor) | all domains empty, both orientations |
| `p16` | ✔ identical (2435 s) | ✔ alternative partition (12000, 4.5·10⁸, 1300, 3.5·10¹⁰), σ = 20, same engines | all domains empty, both orientations |
| four-index constants (`z80_ep_bounds.py`) | ✔ | ✔ re-derived; own rational check `scripts/z80_xr_epcut.py` (constant 0.7951 < 1) | OK for both partitions |
| positive controls for the J/Hd logic | **none by the author** | `scripts/z80_xr_epcontrol.py`: 1157 containment checks of my engine (general weights) on complete M17B lists | all pass |
| falsifier r = 13 | ✔ `crush_checks` (single-13, II3); `solve(13,1)` nonempty | Round-2 combiner run at 13: margin −2427694 ppm (fails, as it must); Q brute = search at 13, k = 1, 3, 5 | OK |
| SHA256SUMS | ✔ OK | — | — |

Replay commands: `bash scripts/z80_round2_replay.sh local|qwalk|p15|p16`. The `layers` stage was run engine by engine,
with identical command lines and diffs. Logs are in `data/z80/xreview/walk/`.

Process notes:
* Every run used `ulimit -v 6000000` and a timeout of at most 1750 s.
* Twice, for about 4 and 10 minutes, a third short process (`pbrute2`, `epcontrol`) overlapped the two
  background jobs.
* All reviewer scratch (binaries, patched copies and temporary files in `data/z80/xrtmp/`) has been deleted. Nothing
  was committed.

## 2. Form defects

**F1 (must fix): load-bearing reviewer-experiment artifacts.**
* `z80_budget2.py` starts with `from z80_xr_extend import *`. The header of that file says "Opus cross-review
  experiment (NOT a certificate)".
* The CF rows `data/z80/xreview/xr_cf_lo.txt` were produced by the Round-1 reviewer's engine `z80_xr_cf.c`.
* Dropping the two xreview row files loses **both** passes: 73 falls to −53762 and 83 to −37363, and the union-ledger
  P₉ charge jumps to about 214k–250k ppm (`ablate1.txt`, `noxr`).
* The note words this as "we also replay the reviewer's P₉ improvements", which understates it.
* I re-ran the author's own `z78_r2cf.c` and it agrees on all seven primes, so the numbers are right.

Fix: move the rows into `data/z80/crush2/` as author-owned certificates. Regenerate the CF rows with `z78_r2cf.c` and
cross-check them with `z80_xr_cf.c`. Fold the loading code of `z80_xr_extend.py` into an author script. Update the
note's sentence accordingly.

**F2 (must fix): there is no statement of which stages are load-bearing for 73 and 83.** Round 1 had one. Add the
table in §3.5, or at least its content:
* P₁₁ to 2³² is needed at both primes, and all four windows are needed.
* The z80_mid band is needed at both.
* The xreview P₉ rows are needed at both.
* shift33 K = 15 is needed at 73. At 83 shift33 is not needed: the margin falls to 17 ppm.
* shift35 is not needed anywhere.

**F3 (should fix): there are no positive controls for the new engines.** `z80_epfast.c` (grouped J and Hd) and the
L = 15/16 entry points in `z80_ep15.c` were only ever run on the empty x = 5 problem. z79 had `point/check.txt` with
seeded containment checks; nothing comparable exists for the new code. Positive x = 5 hits are genuinely unavailable:
* my brute force at (19,6), (23,5), (29,5), (31,5), (37,5), (41,5), (43,5), (47,5), with every e ≤ e₀ factored, finds
  **zero** x = 5 P hits;
* the Q search likewise finds only the k = 1 hit at 13.

A control therefore needs general weights. I did this for my own engine (§3.3) but could not do it for `epfast`
without rewriting it, because q = 6 − p is hard-coded there.

**F4 (should fix): the replay guarantees.**
* The Round-2 `local` stage proves the passes only by a byte diff of `local.txt`. Nothing explicitly asserts that the
  73 and 83 margins are positive. z79's ledger stage had such an assertion.
* `z80_crush_checks.py` still checks only the Round-1 ledger file.

Fix: add `assert` lines for 73 and 83, and a Round-2 r = 13 run. Mine gives −2427694 ppm, i.e. not certified.

**F5 (wording).**
* §0 Label reads "CERTIFIED", but the threshold claim is PROVED relative to the z78/z79 lemmas.
* The STATUS delta "threshold 89 → 83 plus 73" should read "every prime r ≥ 83, and r = 73; 79 and 17..71 open". It
  must also keep the r ≥ 919 libm qualification and the point-not-cylinder qualification at 17.
* "x₁ ≤ √5 a" needs x₁ to be the *smaller weighted* coordinate. Say so; it holds because a is the smaller unweighted
  side.
* "2d ≤ 5^m+6": the derivation actually gives 5^m+5, so this bound is safe but slack.

**F6 (cosmetic).**
* `z80_budget2.py` is hard to audit: it monkeypatches through `old.sh=mid`, has import-time side effects, and reuses
  `row()` twice.
* The P₁₁ files have no header line.
* `z80_qwalk.py`'s binary search starts from u = F+100, which is not excluded for small F. It is harmless because of
  the `min(…, (F+1)//2)` cap, but deserves a comment.

## 3. Substance

### 3.1 Q rational Vieta descent (re-derived; PROVED)
* **The equation.** From (a+b)(pa+qb) = ceFH = h(4abd−1) one gets pa² + qb² + h = (4dh−6)ab ✓.
* **Reflections.** In weighted coordinates X = √p a, Y = √q b, the reflections are X ↦ SY − X and Y ↦ SX − Y. The new
  coordinate is positive because its product with the old one is Y²+h (resp. X²+h) > 0.
* **The walk alternates.** If X > SY/2, the image satisfies X' < SY/2, so it cannot be reduced again at once.
* **Denominators.** For (1,5) the moves are a ↦ Vb − a and b ↦ Va/5 − b; for (5,1) they are swapped. Hence after i
  moves:
  * the new coordinate has denominator dividing 5^⌈i/2⌉;
  * the product of the two denominators divides 5^i.
* **Stopped case.** At a stopped pair, X ≤ (S/2)Y and Y ≤ X give h ≥ (S/2−1)XY = (V/2−√5)ab. With ab ≥ 5^−m this
  gives h(2d−5^m) ≤ 3+√5, hence 2d ≤ 5^m+5.
* **Non-stopped case.** If there are m+1 reductions, the chain x₁ > (S/2)^m x_{m+1} holds. Combining it with
  x_{m+1} ≥ 5^−⌈m/2⌉, x₁ ≤ √5 a, a ≤ (F+1)/(2d) and V ≥ 4d−6 (h ≥ 1) gives exactly the coded inequality, with 9
  in place of 5 (which only weakens it).
* The bound is uniform in h, uses no assumption on V mod 5, and does not need F to be prime.

Stress tests in `xr_qwalk.txt`. None of them failed.
* **Brute force over all F ≤ 5000 coprime to 10.** This enumerates every (a,d,c) and uses no roots. It found 31 hits,
  all with d ≤ D(F)/2. On each hit, the exact rational walk asserted alternation, the 5-adic denominator claims and the
  stopped-pair inequality.
* **Complete Q search at 1500 primes F ∈ [3000, 60000)** with the trivial cutoff: 1 hit, d/D = 0.046.
* **The equation pa²+qb²+h = (4dh−6)ab without Q structure** (d, h ≤ 40, a ≤ 2·10⁴, plus integral points from
  14-step upward reflection chains). 72 points were tested, with walks of up to 21 moves. For every m ≤ 19, the
  dichotomy held, in its sharper form with V rather than 4d−6.

Caveat: real x = 5 Q hits are rare, so the lemma is tested much more on the bare equation than on hits.

Search completeness:
* a is the least positive residue because 2ad ≤ F+1.
* The roots of 4pda² ≡ −q mod F cover a ↦ F−a.
* Since ef = 4a²d+1 < s² with s = 4ad, either f < s or e < s. In the first case f ≡ −F (mod s); in the second
  e ≡ −F⁻¹ (mod s).
* The case f₁ = 0 is impossible because s is even and F is odd.
* My implementation computes square roots as t·(u/t²)^((r^(k−1)+1)/2), with no Hensel step and with branches coded
  separately. It matches the author's D, m and pair count at every odd k ≤ 39, with 0 hits. Brute force equals search
  at (13; 1, 3, 5) and (17, 19, 23, 29; 1, 3).

### 3.2 P four-index cover and windows at L = 15, 16 (re-derived)
* **Product bound.** e·HZ·J·(Hd)² ≤ 4(pq)³h³jz U²/68³. The terms are:
  * H ≤ hqU/(68ad), using the ρ bound outside Hd ≤ Y;
  * J ≤ j·4pa²d/U, using J ≥ 1;
  * eZ = 17HJ − (q−p)pa ≤ z p² a.

  My exact check gives 500·(constant) = 0.7951 < 1 for both orientations and both partitions, at both levels.
* **J window.** pMa ≤ pM²/4 and MH ≤ qB+J₀ give UJ ≤ K/H² + qe₀. Since J ≥ 1, this bounds H. J ≡ −qB (mod 4H)
  because 4 | M. ✓
* **Grouped Hd window.** a − a₀ = qe/(4Uv) + pa²/(UH), and a ≤ 6B(1+e/N)/(4v), with constants 36/272 < 1/6 and
  qe₀/(4U) < 1. The H ≥ h / H < h split is exactly complementary. The d interval and the d | v test are complete. ✓
* **The two-root window** in part A of `epfast` is inherited z79. I additionally proved that only the **small** root
  can give a ≤ b:
  * for (1,5) the large root exceeds V/2;
  * for (5,1) it would need dH² ≤ 15/17.

  So my engine scans only small roots in production. Both roots are scanned in the general-weight control.
* **uint128.** N = 17³¹ ≈ 2^126.1 fits, but 5N does not. `epfast` uses GMP for d < 5 and a split quotient for d ≥ 5;
  both are exact (ceil/floor checked). Further checks:
  * p(qB+J₀)² < 2¹²⁸ is asserted;
  * in `scanv`, a ≲ 6·10¹² so 4pa² fits;
  * in `test()`, every product is guarded by division;
  * in e-mode, q·b ≤ 5(N+e)/4 < 2¹²⁸.

  There is no headroom for L = 17, since N itself would overflow. The note's "No P17 census" is consistent with this.
* **Index completeness.**
  * e runs over every e ≡ −N mod 4 with 17 ∤ e up to E;
  * HZ runs over every H, Z ≥ 1 with HZ ≤ V;
  * the e-mode factor records are reused for both orientations, which is valid because the keys do not depend on
    (p,q);
  * the split pieces are consumed in order (16 pieces or fewer).

### 3.3 Independent P endpoint search with an alternative partition
I wrote `scripts/z80_xr_ep.c` from the identities alone.
* **J mode** enumerates (H, M) rather than (H, J).
* **Hd part A** uses padded long-double small-root windows (pad ≥ 2¹⁴ ulp). Every candidate is then verified in mpz.
  This replaces the author's mpz square-root windows.
* **Hd part B** uses its own a-window, a ≤ ⌊a₀⌋ + 3 + ⌊36pB/(16·17·h v²)⌋.
* The split is σ = 20 instead of 12.
* The e and HZ domains are re-done in Python with **sympy factorint** instead of GNU factor.

The partition (E, J₀, V, Y) is chosen with V 100× smaller and Y 10× larger than the author's, so the HZ, Hd-B and
Hd-A/B boundaries all differ.

Results (`xep_L15.txt`, `xep_L16.txt`):

| L | J (p=1,5) | Hd A pairs (p=1 / p=5) | Hd B (v ≤ Y) | e (keys) | HZ (keys) |
|---|---|---|---|---|---|
| 15 | 0, 0 | 2.39·10⁸ / 5.35·10⁸ pairs, 0 hits | 0, 0 | 4706, 0 | 1316, 0 |
| 16 | 0, 0 | 9.87·10⁸ / 2.2·10⁹ pairs, 0 hits | 0, 0 | 2824, 0 | 11442, 0 |

**Positive controls** (`epcontrol.txt`) use my engine compiled `-DGEN`, which allows general (p,q), both roots and
e ≤ E₀.
* The ground truth is the complete M17B lists at r = 17, L = 2..4, with synthetic endpoints q ≡ −pa/b, as in
  `z79_r2check.py`.
* There were 1157 checks: 284 in J mode and 873 in Hd mode, with σ = 3, 12, 20. Each check satisfied
  expected ⊆ found ⊆ genuine.
* The production (x = 5) path differs from GEN only in the small-root restriction and the constant window, both proved
  above.
* After the edits for GEN, the final source reproduced the production runs exactly on a spot check
  (`xep_final_source_spot.txt`).

### 3.4 Middle-shift band (`z80_mid.py`) (re-derived; PROVED)
Order a ≤ b with abd = M, and take e ≥ t.
* **Case a < t.** Here a is the least residue of −b mod e, and b ≥ (a+b)/2 ≥ t/2. So the count is at most
  τ(M) − D_M(⌊(t−1)/2⌋).
* **Case a ≥ t.** Here d ≡ −M/b² (mod e) is a unit and d ≤ M/t² ≤ t ≤ e, and t ≤ b ≤ M/t. So the count is at most
  τ(M) − 2D_M(t−1), and the two tails are disjoint because t² ≤ M.
* Two orientations give 4τ − 2D − 4D.

Summation:
* Στ ≤ tsum, which is the same contract as the existing `4*tsum` route.
* ΣD_M(b) ≥ H·Σ_{n≤b}1/n − b, with `harmonic` a floored lower sum.
* The anchors are valid: t³ ≥ m ≥ M, and t² ≤ ⌊n/8⌋ ≤ N/4 ≤ M.

The band is load-bearing at both primes: without it, 73 → −6189 and 83 → −9019.

### 3.5 Ledger combiner, ablation and sensitivity
The combiner:
* `analyze` uses an unconditional union bound: depth-3 live mass minus Σ_k P_k(live = 1) minus Σ Q_k minus tails.
  The split route at live = 1 charges ≤ 2⌈T/r^(D−1)⌉/r of the whole space. This is valid without conditioning.
* The global margin is the maximum of two valid lower bounds.
* The cylinder table divides an inverse-stable budget by 2 for b ≠ b⁻¹. This is valid because inversion preserves
  measure and maps the hit union to itself. It is not load-bearing; all its entries fail.
* At 73 and 83 the route is `det` at cuts 2³²/2³³, with c taken from the inherited `fine`/`local`/`layers` grids.

Ablation, margins in ppm (from `scripts/z80_xr_walk_ablate.py`; logs `ablate1.txt`, `ablate2.txt`):

| change | 73 | 83 |
|---|---|---|
| full | 18189 | 19111 |
| −P₁₁ prefix | −53762 | −37363 |
| P₁₁ only to 2³⁰ (window 0) | −4454 | −22724 |
| P₁₁ counts ×10³ / ×10⁵ | 18044 / 3717 | 19092 / 17234 |
| −shift33 | −12933 | 17 |
| −shift33 K = 15 / −K = 13 | −5569 / 10825 | 1437 / 17691 |
| shift33/35 ×10 | 9766 | 16852 |
| −shift35 | = | = |
| −mid band | −6189 | −9019 |
| −xreview P₉ rows | −53762 | −37363 |

**Debate point.** The *values* of the new prefix counts hardly matter: they can be inflated 10⁵-fold, and shift rows
10-fold, without losing a pass. What carries the passes is moving the cut point to 2³² and 2³³, where the inherited
large-shift charge c is much smaller. So the residual risk sits in the inherited z78/z79 large-shift tables at those
cuts, not in the new code. This is reassuring about the new stages, but it means the threshold is only as good as
those tables, which were replayed in Round 1 and reviewed in z79 but not re-implemented here.

## 4. Tail-transfer section
* The obstruction is correct but nearly tautological. A live depth-j cylinder has zero exact charge at depth j, yet
  deep centres inside it exist (z78 PUSH §2), so no finite multiplier of that zero bounds the future.
* The Bonferroni remark is right: Σ − Σpairs is a *lower* bound on a union.
* Scope: none of this refutes envelope recursions. The note says so.

## 5. Residual risks and recommendations
1. Both passes depend decisively on the inherited large-shift tables (`det` route) at the new cuts. They also depend
   on reviewer-labelled P₉ files (F1). A second reviewer should target the K = 11, 13, 15 `fine`/`local` rows at
   73/83, j = 32..33.
2. The margins are about 18–19k ppm. They are robust to large errors in the new counts (§3.5), but not to removal of
   any of the four load-bearing stages.
3. Positive controls exist only for my engine. Add a general-weight harness for `epfast` (F3).
4. The Q-lemma stress tests have few genuine Q hits. Most evidence is on the bare quadratic equation; the proof itself
   is short and checked.
5. The decisive inherited engine `z79_shiftwide.c` was replayed at J = 33 and 35 (all 24 rows), not rewritten.
   `z79_runs` and the layer and local tables were not rerun in this review.

## 6. Reproduce
From the repository root. Writes go only to `scripts/z80_xr_*` and `data/z80/xreview/`.
```
bash scripts/z80_round2_replay.sh local; bash scripts/z80_round2_replay.sh qwalk; …p15; …p16
gcc -O3 scripts/z80_xr_p11.c -o X && X 83 0 32            # likewise idx 1..3, r=73; 'X r 0 22 truth' for truth mode
gcc -O3 scripts/z80_xr_ep.c -lgmp -lm -o E && E 17 16 5 Hd 35000000000 20 B 1 8750000000
python3 scripts/z80_xr_epcut.py 17 16 12000 450000000 1300 35000000000
uv run --offline --no-project --with sympy --with gmpy2 python -B scripts/z80_xr_ehz.py 17 16 e 12000
uv run --offline --no-project --with sympy python -B scripts/z80_xr_qwalk.py search 17 39   # also vs/lemma/lemma2/markov
gcc -O3 -DGEN scripts/z80_xr_ep.c -lgmp -lm -o G && python3 scripts/z80_xr_epcontrol.py G
uv run --offline --no-project python -B scripts/z80_xr_walk_ablate.py nop11 73 83
```
