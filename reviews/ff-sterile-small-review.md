# R220 — hostile review of FF_STERILE_SMALL.md (O220 checkpoint 1: §§1–3, q = 27 certificate)

Reviewer: R220 (side agent, branch side-agent/review-ff-small). Reviewed commit: side-agent/ff-sterile-small @ 030af7a5.
Scope: Lemmas 1.1–1.4, Lemma 2.1, Theorem 3.1 (q = 27), Lemma 4.1 / Cor 4.2, the q = 9 statement, labels.
Own scripts (all from scratch, none derived from `fz_*`; the sum/tail extend R218's author-independent `review_fs2_*`):
`scripts/review_fz_bounds.py, review_fz_brute.py, review_fz_rankin.py, review_fz_lemma14.py, review_fz_sum.c,
review_fz_tail.c, review_fz_caseA.py, review_fz_certify.sh, review_fz_q9.py`; logs in `data/fz_review/`.

## Summary verdicts

| claim | verdict |
|---|---|
| Lemma 1.1 (Euclidean division determines v₁) | **SOUND** |
| Lemma 1.2 (division routes D1, D1c, D2, D3) | **SOUND** |
| Lemma 1.3 (v₁ ≡ −T^{s−2} mod every factor; V(D)) | **SOUND** (stated bound weaker than the one the scripts use, m-1) |
| Lemma 1.4 (T-adic refinement of class bounds) | **SOUND** (hypothesis wording, m-3) |
| Lemma 2.1 (Case A ≤ (α+1)³ q^{(α−1)/2} 3^{α/2}) | **SOUND** |
| Theorem 3.1 (q = 27, k ≥ 2: no finite linear covering; covered measure over the 26 slices ≤ 3.06) | **SOUND-AFTER-REPAIRS** (documentation repairs only: m-1, m-2; the inequality is independently re-certified with a strict subset of the stated routes: total ≤ 3.0556 < 26) |
| Lemma 4.1 (fixed-q Rankin/knapsack divisor bound) | **SOUND** |
| Cor 4.2 (Case B count q^{(2/5)s+o(s)} at every odd q) | **SOUND** as labelled (bound PROVED via DEPTH_ASPECT Lemma 2.2 + q^{o(n)} divisor bounds; the o(n) step is only sketched, m-7) |
| q = 9 CERTIFIED negative statement about the method | **SOUND** (Σ_{s≤8} = 9.2236 > 8 reproduced by independent code; the "tail negligible" remark depends on Lemma 4.1 and is EVIDENCE, m-6) |
| Labels (ES not solved; Conjecture 0.2 not claimed) | **SOUND** (document); report spark slightly overstated (m-8) |

No FATAL, no MAJOR defects.

(sections below)
