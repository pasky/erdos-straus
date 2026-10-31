# z52d audit — shard A0 (14 items): Opus blind redo vs Haiku Pass-1
ES remains OPEN. Phase 1 (blind) was committed before haiku_A0.jsonl was opened. Files: `opus_A0.jsonl`, `compare_A0.jsonl`.

**Verdict counts:** AGREE 5 · MISS-MINOR 8 · MISS-MAJOR 0 · HAIKU-WRONG-COVERED 1 · HAIKU-BETTER 0.
**Opus outcomes:** nothing 8 · covered 5 · interesting 1 (Z2001, calibration only). Content: one item at 2, thirteen at 1, none at 3.

**MISS-MAJOR items:** none. Closest calls:
- Z2001 (set-cover menu growth): Haiku had the same law (33, 112 items at 10⁴, 10⁵), labelled it `nothing`. Extended to 10⁸
  (2484 items; local slope 0.52 → 0.42), I found the structure: 90 % coverage plateaus at 46 items (fixed-menu density, the
  quantitative face of B1), and growth is driven by the tail and by singletons. A real calibration, but the core number survived.
- Z1234 (model disagreement): Haiku `skipped` it as meta, yet the step was actionable with repo models. Result: M_BM·F wins on
  the mean in both disagreement tails; 5 of the 7 (★) zeros ≤ 10⁶ lie in the 5 % low-F tail; the zero law there is off by ≈2.7×.
  This only sharpens RESIDUE_HARDNESS §0.6.

**HAIKU-WRONG-COVERED:** Z1739 — FRONTIER §2.1 (trial form only) cited for a discrepancy question; low stakes (null result).

**Patterns in Haiku's failures (Assessment, n = 14):**
1. *Unjustified skips:* Z1234 and Z0257 were skipped as "meta" or "no map given", although the item or the repo supplied the
   machinery. Each step took < 15 min. This is the main way a real lead could be lost in a larger sample.
2. *Over-narrow operationalisation:* one window e = 7 for a many-windows question (Z3146); a gcd table not tied to certificates
   (Z1139); a smaller range with no structural read-out (Z2001).
3. *No premise check:* Haiku missed that H(p² + 4c²d) ≡ 0 (not a discriminant; Z1484) and that C > p/4 is empty (Z1494).
4. *Shallow repo checks:* it rarely found the memo that actually covers the item (Z2163, Z2531, Z1484, Z1884's flagged gap), and
   it cited the setting instead of the question (Z1739).
5. Where Haiku computed, its numbers agreed with mine (Z2001, Z2591); no fabrication seen.

**Bottom line (Assessment).** Haiku under-recorded often (9 of 14 not AGREE) but lost nothing that bears on a proof of ES.
Read its `nothing`/`skipped` as "not examined at depth", not "examined and empty"; its `skipped` items are the place to re-run.
