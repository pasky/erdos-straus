# R126 — hostile review of O126 (GEOMETRY_ES.md, AGENT_REPORT_O126.md, scripts/geo_*.py)

Reviewer branch `side-agent/review-geometry`, merged `side-agent/geometry-es` at review start.
Sources checked against the actual text: BL = `sources/bright-loughran-1908.02526.pdf` (pdftotext),
ET = `sources/elsholtz-tao-1107.1010.pdf` (§2, Props 2.2/2.3/2.6, Lemma 2.8). Yamamoto 1965 NOT accessed.
From-scratch scripts: `scripts/review_geo_*.py` (no author code reused).

## Summary verdicts (filled in progressively)

| claim | verdict |
|---|---|
| §1 BL restatement (Lemmas 2.1–3.11, Thms 1.2, 1.5–1.9, Cors 1.3, 1.4, Rem 1.10, 3.12) | SOUND-AFTER-REPAIRS (D1, D2) |
| §1 "BM only obstruction for fixed n ⟺ ES(n)" | SOUND for n ≥ 2; FALSE at n = 1 (D1) |
| §2.1 nine rational lines, nodes, boundary | SOUND (verified symbolically, `review_geo_sym.py` (B)) |
| §2.2 Prop 2.1 toric model | SOUND — reviewer supplies the missing symbolic proof (see §R2) |
| §2.2 integral/positive points ↔ primitive s with 4s_i ∣ nS | SOUND |
| §2.3 Prop 2.2 matrix forms | SOUND (checked against ET (2.1)–(2.21), Props 2.2, 2.6) |
| §3.1 (F1)/(F2)/(F3) equations, splitness | SOUND (symbolic) |
| §3.1 α\|F1 = (n(n−4t), −w), α\|F2 = (−λ, −nZ) | SOUND (F2 had no proof — D4); verified at every place on 16622 solutions |
| §3.1 Br_vert = Br ℚ for (F1) | SOUND (sketch is adequate; D5 cosmetic) |
| §3.1 "only conic-bundle class on Bl_V Π̄ is H − V_k" | SOUND |
| Thm 3.1 | SOUND (= BL Lemma 3.10 + two trivial cases; no novelty, correctly attributed) |
| Prop 3.2 (statement) | SOUND; its use as "the structural reason" / "all conic bundles split" is a GAP (D3) |
| Cor 3.3 / "Aim (B) negative for every fibration" | SOUND for every fibration — but only via Thm 3.1 (real place), not via splitness; "n²-type bounds" wrong (D6) |

## Defects
(pending)
