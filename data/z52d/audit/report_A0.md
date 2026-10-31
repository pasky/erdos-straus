# z52d audit — shard A0 (14 items): Opus blind redo vs Haiku Pass-1

ES remains OPEN. Phase 1 (blind) was committed before haiku_A0.jsonl was opened. Files: `opus_A0.jsonl`, `compare_A0.jsonl`,
scripts `scripts/z52d_audit_A0_*`, data `data/z52d/audit/A0/`.

**Verdict counts:** AGREE 5 · MISS-MINOR 8 · MISS-MAJOR 0 · HAIKU-WRONG-COVERED 1 · HAIKU-BETTER 0.
**Opus outcomes:** nothing 8 · covered 5 · interesting 1 (Z2001, calibration only). Content: one item at 2, thirteen at 1, none at 3.

**MISS-MAJOR items:** none. Closest calls:
- Z2001 (set-cover menu growth): Haiku had the same law (33, 112 items at 10⁴, 10⁵), labelled it `nothing`. Extended to 10⁸
  (2484 items; local slope 0.52 → 0.42), I found the structure: 90 % coverage plateaus at 46 items (fixed-menu density, the
  quantitative face of B1), and growth is driven by the tail and by singletons. A real calibration, but the core number survived.
- Z1234 (model disagreement): Haiku `skipped` it as meta, yet the step was actionable with repo models. Result: M_BM·F wins on
  the mean in both disagreement tails; 5 of the 7 (★) zeros ≤ 10⁶ lie in the 5 % low-F tail; the zero law there is off by ≈2.7×.
  This only sharpens RESIDUE_HARDNESS §0.6.

**HAIKU-WRONG-COVERED:** Z1739. It cited FRONTIER §2.1 (the trial form only) for a discrepancy question. Low stakes: the
measurement is null (the law is the same for primes and composites, and the ES atom sits 100× below resolution).

**Patterns in Haiku's failures (Assessment, n = 14):**
1. *Unjustified skips.* Two items were skipped as "meta" or "no map given" (Z1234, Z0257) even though the item or the repo
   supplied the machinery. Both steps took < 15 min. Neither result was important here, but this is the main way a real lead
   could be lost in a larger sample.
2. *Over-narrow operationalisation.* One window e = 7 for a many-windows question (Z3146); a gcd table not tied to certificates
   (Z1139); a smaller range with no structural read-out (Z2001).
3. *No premise check.* Haiku missed that H(p² + 4c²d) ≡ 0 (not a discriminant; Z1484) and that C > p/4 is empty (Z1494). It
   repeated the item's flawed heuristic instead.
4. *Shallow repo checks.* It rarely found the memo that actually covers the item (Croot/Bloom memo for Z2163, O147(b) for Z2531,
   O170/SIGN_IDENTITY for Z1484, the repo's own flagged Chinese-literature gap for Z1884). It cited the setting (FRONTIER §2.1)
   instead of the question (Z1739). Its `covered` for Z2766 was right without re-reading.
5. Haiku's numbers, where it computed, agreed with mine (Z2001 menus, Z2591 deficit). No fabricated results were seen.

**Bottom line (Assessment).** In this shard Haiku under-recorded often (9 of 14 not AGREE) but never lost anything that bears on a
proof of ES. The fair reading of its `nothing`/`skipped` labels is "not examined at depth", not "examined and empty". Its `skipped`
items are the place to re-run.
