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
