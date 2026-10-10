# R130 — hostile review of O130 (QUATERNION_ES.md, AGENT_REPORT_O130{,b}.md, scripts/quat_*)

Reviewer: side-agent/review-quaternion. Reviewed: QUATERNION_ES.md as merged from `side-agent/quaternion-es`.
From-scratch scripts (none reuse the author's code or `geo_common`):
* `scripts/review_quat_hilbert.py` — my own Type I enumeration over (a,c,d) (f = 4acd − p | 4a²d+1) and my own
  Hilbert symbol (Serre's formulas, incl. ℓ = 2). Log `logs/review_quat_hilbert_3000.txt`.
* `scripts/review_quat_brute.py` — raw brute force of `4/p = 1/x+1/y+1/z`, split into Type I / II, compared with
  the parameterisations of Lemma 1.1 and Prop 3.2. Log `logs/review_quat_brute_200.txt`.
* `scripts/review_quat_symbolic.py` — my own quaternion multiplication in (α,β), symbolic in d,m,a,b,c,p.
  Log `logs/review_quat_symbolic.txt`.
* `scripts/review_quat_fixed_de.py` — §3.4 pairs and the 40/93, 120/450 counts. Log `logs/review_quat_fixed_de.txt`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (K-factorisation) | SOUND |
| Lemma 1.2 (Λ_{d,m}, disc 4dm−1) | SOUND |
| Prop 1.3 (Λ ⊂ B_{p,∞}, reduced disc pe) — algebra/ramification part | SOUND-AFTER-REPAIRS (minor: p ∤ e used silently) |
| Prop 1.3 — "Gross–Zagier parameter x = 2" | GAP in the citation (GZ hypotheses fail); the arithmetic identity is trivial and correct |
| Remark after 1.3 (minimal hypotheses for B_{p,∞}) | SOUND-AFTER-REPAIRS (add v_p(pe) odd) |
| Prop 2.1 + isogeny reading | SOUND |
| Prop 2.2 | SOUND (mathematically trivial); one heuristic sentence over-labelled |
| Lemma 3.1 | SOUND (symbolically verified) |
| Prop 3.2 + ideal reading | SOUND |
| §3.3 | SOUND as Assessment; cited facts correctly stated |
| §3.4 (EVIDENCE) | SOUND — every number reproduced |
| §4 (ET Prop 1.6, square-mimicking) | SOUND (minor: same p ∤ e point) |
| Prop 5.1 | GAP — "PROVED modulo cited shape" cites a shape (GZ coprime-fundamental F(n)) that does not apply; conclusion repairable by a direct local argument (given below) |
| Novelty of x = 2 dictionary | UNVERIFIABLE (no hits; see §N) |
| Labels / scope of negative statement | Mostly honest; scope paragraph in §6 adequately limited |

## Claim-by-claim checks
