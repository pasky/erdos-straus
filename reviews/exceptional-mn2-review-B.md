# Hostile review B of EXCEPTIONAL_MN2.md (task R102B)

Reviewer: side-agent/review-emn2-b. Reviewed: `EXCEPTIONAL_MN2.md` as merged from
`side-agent/mn-transition` (HEAD at review start), `reviews/agent-reports/AGENT_REPORT_O102.md`.
Sources checked against: `sources/elsholtz-tao-1107.1010.pdf` (pdftotext, §7 pp. 25–32, (A.12) p. 49),
`sources/pw.txt` (PW §2–3, Lemma 7.4), `EXCEPTIONAL_MN.md` (Def 1.2, Lemma 1.3, Prop 3.1, Cor 3.2).
Shiu 1980 used as quoted (Thm 1 standard form); not re-read from PDF.


## Verdicts

| Claim | Verdict |
|---|---|
| Lemma 3.3 (ET Prop 1.4 + Pólya–Vinogradov) | **SOUND** (checked line by line against ET pp. 30–32; minor write-up defects m1–m3) |
| Lemma 3.1(a) | SOUND |
| Lemma 3.1(b) (repaired FATAL) | SOUND (re-derived; Rankin truncation, Shiu range, small-u swap all check) |
| Prop 3.2 (Type II ≪ L³/m) | SOUND |
| Prop 3.4 (Type I) | SOUND-AFTER-REPAIRS (minor: small-box bookkeeping misstated, log² vs log⁴; bound itself holds, even with m^{0.03} in place of m^{0.1}) |
| Lemma 3.5 | SOUND |
| **Theorem L** | **SOUND** as stated (effective, absolute constants); comparison-with-PW wording should be tightened (m5) |
| Lemma 1.1 (reduced CRT model) | SOUND |
| Lemma 1.2 (Shiu multiplicities, repaired k ≤ K) | SOUND (minor: inconsistent X-hypotheses in statement) |
| Thm 1.3 / **Theorem U** | **SOUND** (ineffective via BV; constants uniform in m — checked) |
| §2 numerics | EVIDENCE confirmed: scanner exact on 75 753 (m,p) pairs; L_{1/2} reproduced from scratch. Precision of "exponent 0.333" overstated (m7) |
| Conjecture C2 | correctly labelled CONJECTURE |

No FATAL or MAJOR defect found. I specifically attacked the four repaired spots (3.1(b), 3.3, 1.2 k ≤ K,
3.1(a) Y ≥ log m): all four repairs are correct.
