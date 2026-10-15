# AGENT_REPORT_O228 — STERILE_LOWER (checkpoint 1)

SHARP:
* **Level-1 counts can be certified for *every* prime in a range at amortised polylog cost per prime** (STERILE_LOWER
  Lemma 3.1, PROVED, checked 0 mismatches vs per-n enumeration): P-data of N ↔ triples (a, c, d) with N ≡ −4a²d
  (mod 4acd − 1); Q-data of n ↔ (a, d, f | 4a²d + 1, c) with n = 4acd − f. Since the binding term of SE's (S) is the
  level-1 Type I count (uniform bound ≈ 10 r^{0.6} ln r, true value ~10²), a joint sweep would move r₀ from 2^{30.16}
  to ≈ 2^{22.5} (then P at K = 3 binds). Not run (multi-day C job). This is the concrete next step.

Results:
* **Thm 2.1 (PROVED, computer-assisted, same inputs as SE Thm 3.4): (S) holds for every prime r ≥ 2^{30.15625} ≈ 1.19·10⁹**
  (2^{30.34375} using only SE's reviewed se_box). Ingredients: value-selected tails (Lemma 1.2; SE's tail constant 873 → 0.0136
  at N₀ = 2^800 — SE's ≈ 0.11 tail term disappears), ℓ²-Minkowski in Coppersmith (Lemma 1.1, −5–7 %), 1/32-octave r-cells.
  Certificate: `ZL_L2=1 python3 scripts/zl_r0.py 30.15625 800 34`, tables `data/zl/` (MANIFEST.txt). Max S = 0.49783.
* Quantified limit (Assessment, I1/I3/§3.0): below 2^30 the only obstruction is the level-1 Type I count; finer boxes, exact
  max-τ tables (envelope already within 10 %), small-e exact enumeration, Lenstra's 11-divisor bound, extra f-τ₃ routes: each
  ≤ 10–40 %. Target 10⁶ needs Q₁ ×25 and P₃ ×5 — not reachable by uniform box bounds.
* Comp. 4.1 (CERTIFIED, exhaustive): r ≤ 13 all non-residue cells covered at level 1; every prime 17 ≤ r < 20000 has
  level-1 survivors.
* r = 17 (goal 2): **undecided**. Assessment 4.2: box-sum certificates are off by ≈ 10⁴ at N ≈ 17^{15}. New Lemma 4.3 (U–V
  factorisation UV = c²p²q² + G r z² for data covering a rational u; forces e ≤ 4q²a) restricts but does not exclude coverings.
* Goal 3 (all r ≥ 17): not reached; the gap is r ∈ [17, 2^{30.16}) (or [17, ~2^{22.5}) after SHARP 1).

Files: STERILE_LOWER.md; scripts/zl_{tail.py, r0.py, box.c, joint_check.py, level1_survivors.py, level1_overlap.py};
data/zl/. Labels: Thm 2.1 PROVED (computer-assisted); Lemmas 1.1, 1.2, 3.1, 4.3 PROVED; Comp 4.1 CERTIFIED; rest Assessment.

Sparks: see STERILE_LOWER §5 (joint sweep; level-2 cubic-residue sweep; descent in U for a rational point).

---
# Checkpoint 2 (round 2: the SHARP run)

SHARP (new, prominent):
* **(S) holds for every prime r ≥ 2^{21.4375} ≈ 2.84·10⁶** (STERILE_LOWER Thm 6.3, PROVED, computer-assisted; was 2³² in SE,
  2^{30.16} at checkpoint 1). Mechanism: Lemma 3.1 joint sweep gives the *exact* level-1 counts of every prime in an octave
  (P: factoring-free AP sweep; Q: sieve / ρ factoring of 4a²d + 1 for a < A), plus the AD bound for ad ≤ Y and the engine only
  for a ≥ A (none at all for r < 2^24). Worst exact level-1 counts: 1.6·10⁴–7.5·10⁴ (≤ 0.6 % of r).
* Below 2^{21.44} the binding term is K = 3 (N = r³, uniform engine); a level-2 sweep (Lemma 3.1(i) restricted to cubes N = r³)
  is the next step and would be a per-r computation of cost ~ r^{1.2} per prime in the P-route — not obviously feasible.

Budget: total sweep wall ≈ 5.8 h on ≤ 2 cores (all runs under ulimit -v 8000000 and timeout); per-octave times in §6 table.
Every octave was certified fail-closed and committed as it finished (data/zl/sweep_NN.txt, r1_NN.txt, MANIFEST.txt).
Validation: per-n comparison with R223's enumerators (0 mismatches), byte-identical dumps across sieve/ρ/split variants.
Bug log: (1) zl_r1 initially skipped the first cell of an odd-started sweep (fixed); (2) a false "prime table too small" exit
(fail-closed) fixed; (3) first 2^23/2^22 runs used A = X₁/4 instead of > X₁/2 — caught by zl_r1's check, rerun.

r = 17 descent (Lemma 4.3), §7: **negative** (Assessment): covering data of a rational u are the integral points of the conic
c(qa − pb)² − 4rcdz²·ab + rz²(a + b) = 0 with (qa − pb)/(rz) = ±r^{L−1}; the levels are where a binary-recurrence-like quantity hits
powers of r — a uniform S-unit problem over the two-parameter family (c, d, z) of conics. Naive Vieta moves don't even keep
integrality (checked on the known covering of 11/9). No descent; r = 17 undecided.

Files new in round 2: scripts/zl_{sweep.c, sweep_check.py, merge.py, boxa.c, r1.py}; data/zl/{sweep_*, r1_*, Qa_*, P_q32_k3*,
P_q32_k5_l2}.txt. §§1–4 untouched except the status line.
Sparks: (a) level-2 (cube) sweep or a sharper K = 3 engine to pass j ≤ 685; (b) the same joint idea for the r = 17 *cell-wide*
counts is hopeless (17^K levels needed to K ≈ 40), but a joint sweep over *many* r for level 2 might show where P₃ truly sits.
