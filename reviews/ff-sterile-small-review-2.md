# R221 — hostile review of FF_STERILE_SMALL.md §5 (O220 checkpoint 2: Theorem 5.2, q = 9)

Reviewer: R221 (side agent, branch side-agent/review-ff-small-2). Scope: §5.1 (exact enumeration, `fz_enum.c`), §5.2
(exact masses), Lemma 5.1 (linearised Lemma 4.1, `fz_tail.c` RANK = 1), Theorem 5.2 (`fz_hybrid.c`, `fz_certify9.sh`,
log `data/fz/certify9.txt`), Case A at q = 9, §5.3 (q = 3 s₀ Assessment), labels. §§1–3 were reviewed by R220; §6 not reviewed.
From-scratch scripts: `scripts/review_fz9_enum.c` (own F₉ model and three factoring-free reconstruction routes, full (B)
check), `review_fz9_compare.py`, `review_fz9_rankin.py` + harness `review_fz9_rkdump.c` (Lemma 5.1 constants),
`review_fz9_sum.c` (finite bound sum with OWN Lemma 4.1 on R220's independent route code, optional exact counts),
`review_fz9_tail.c` (tail with OWN linearised Lemma 4.1 on R220's independent tail code). Logs `data/fz/review_r221_*`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| §5.1 completeness of fz_enum's eight routes (incl. the factoring routes M11–M16) | **SOUND** (proved below; pattern-by-pattern agreement with my independent enumerator for all patterns s ≤ 17 [s = 18: see §1]) |
| §5.2 exact masses (per level, Σ_{s≤18} = 0.592177, Σ_{s≤22} = 0.592201) | **SOUND** (s ≤ 17 independently reproduced exactly; s = 18–22 from the author's files, cross-checked only for consistency, see m-2) |
| Lemma 5.1 (linearised Lemma 4.1) and its implementation in fz_tail (RANK = 1) | **SOUND** |
| Hybrid splice (exact s ≤ 22, bounds 23 ≤ s ≤ 80, tail s > 80) | **SOUND** (no double counting, no omitted pattern) |
| Case A at q = 9 (0.17501 + 1.1·10⁻⁵) | **SOUND** |
| Theorem 5.2 (certified total ≤ 3.58 < 8) and its corollaries | **SOUND-AFTER-REPAIRS** (minor: documentation of the regeneration command and of what is independently verified) |
| §5.3 s₀ ≈ 80–85 at q = 3 (Assessment) | (see §6) |
| Labels (Conjecture 0.2 not claimed; ES not claimed) | **SOUND** |

No FATAL, no MAJOR so far.
