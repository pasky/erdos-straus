# R276 — hostile review of O266 (ZAREMBA_TRANSFER.md, z36 memos/scripts)

Reviewer: R276 side agent (branch side-agent/review-zaremba, merged side-agent/zaremba-transfer @ O266 cp1).
Sources checked: Shkredov arXiv:2603.14116v2 (full PDF downloaded from arxiv.org, pdftotext + bbox font check);
Rickards–Stange arXiv:2401.01860v3 (excerpt in repo + arXiv PDF, see §1); Chang preprint excerpt in repo;
Zhang arXiv:2605.02518v2 (excerpt in repo). From-scratch scripts: `scripts/review_r276_*.py`.

## Summary verdicts (filled in claim by claim)

| # | Claim | Verdict |
|---|---|---|
| 2 | Method extraction, threshold 1 − w ≤ κ/8, constants | SOUND-AFTER-REPAIRS (MAJOR: M = 22000 is a misreading of M = 2^2000) |

## Defects

**D1 (MAJOR) — Shkredov's constant is M = 2^{2000}, not 22000.** Locations: ZAREMBA_TRANSFER.md §1.4 ("M = 22000
suffices"), §4 Reading ("constant M ≥ 22000 (Shk (158))"), BRAINSTORM/z36_density_threshold.md line 10,
AGENT_REPORT_O266 SHARP 2. In the arXiv PDF (p. 38, eq. (158)) the "2000" is a superscript: pdftotext -bbox gives the
glyph "2" at baseline (yMin 221.96, height 9.7) and "2000" raised and smaller (yMin 219.49, height 7.1). pdftotext
-layout flattens this to "22000". Internal consistency confirms 2^{2000}: (157) bounds the digits by
max{10(κε)^{−1}, 100δ^{−60}}, and with κ ≥ 2^{−1656}, ε < 1/18 this is ≈ 180·2^{1656} ≈ 2^{1663.5}; Theorem 38
(1 − w_M ≥ 1/(4M) … ) plus M∗ ≥ 40M then lands below 2^{2000}. Moreover the author's own threshold 1 − w ≤ κ/8 with
1 − w_M ≥ 1/(4M) (Shk Thm 38) forces M ≥ 2/κ ≥ 2^{1657}, which is flatly incompatible with M = 22000 — the document
contradicts itself in §1.3 vs §1.4. Repair: replace "M = 22000" by "M = 2^{2000}" everywhere, and add the one-line
consistency check (threshold ⇒ M ≳ 2/κ). The qualitative conclusions of §4 ("negligible contribution") only get
stronger.
