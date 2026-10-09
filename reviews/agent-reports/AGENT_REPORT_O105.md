# AGENT_REPORT O105 — consolidation after the 2026-10-09 round

Branch `side-agent/consolidate-oct9`. No new mathematics; no label changed.

## (1) verify.py blocks (eh)–(ek)

All four use the reviewers' from-scratch scripts first; the author's code appears only as the object under test or
as a second engine. Full run: `OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 timeout 3000 uv run --with scipy --with mpmath
python verify.py` under `ulimit -v 8000000`: **all checks passed**, ≈ 7.4 min wall (log `logs/o105_verify.log`).
New blocks add ≈ 43 s.

| block | document | content | s |
|---|---|---|---|
| (eh) | POINTWISE_MORDELL13C | R100 `review_m13c_tree.py` on the **full** tree6_6000 (it runs in 1.6 s, so no sampling was needed): 6000 splits, 136494 covered / 35459 open leaves, 2140 classes, 0 errors, per-root open masses and mean 8.424e-5; inline per-root open-leaf counts (13986, 18070, 873, 455, 871, 1204); R100 `review_m13c_extra.py`: 7 sympy identities, split primes ≤ 83, open moduli, roots (x/13) = −1, four negative controls rejected; R100 witness brute force = author `witness_all` at L = 840, 9240; R100 `review_m13c_cell22.c`: 0 data at λ = 11⁴13⁴ and 20449, 34 at λ = 143 (control) | 25 |
| (ei) | POINTWISE_MORDELL17C | Lemma 1.1 Abel identity exact (Fractions, random D, both weight systems); 24 table entries (pointwise and cumulative, K ≥ 13 / ≥ 15) from author `m17c_tail_cum.py` and R98b `review_m17c_tail.py`, each floor-rounded against an inline closed form; S_P(13) = #p13.txt = 1463; Lemma 2.1 R98b brute force at F = 17, 4913, 1001, 9999 (2/73/10/179 points, max 1/1/1/2 per (a,d)), author qcheck agrees, sweep F ≤ 1500 (27919 points, 0 failures); Cor 2.2 cost 4.22545e-3 | 2 |
| (ej) | POINTWISE_TYPEI6 | R99 sympy identities (Lemma 1.1(a)–(d), 1.3, 3.1, Prop 2.1, Remark 1.2 numbers); inline integer replay of Lemma 1.1(a)–(c) and the regime-(v) criterion on (13,1) and relaxed (7,293); Remark 1.2 control found by both Comp 4.1 engines (1143 candidates each); L = 7, b = 0..4: 0 solutions, candidate counts 1, 5, 12, 56, 201 equal in both engines (gcc + libgmp) | 15 |
| (ek) | EXCEPTIONAL_MN2 | `emn2_scan` (count = 2) = R102B brute force on 6617 (m,p) pairs (m = 4..60, p ≤ 600; six m on (1000,1600]); R102A = R102B on m = 12, 40, 60; R102A §1 identities; R102B `L_{1/2}(60) = 7.636`, ratio 1.950 (all primes, no sampling); the scanner reproduces the proportions at the three grid points | 1 |

## (2) STATUS.md / CAMPAIGN_SUMMARY.md

Refreshed to the ledger: (D)31 follow-up (MN2: Thm U, Thm L, gap, EVIDENCE, Conj C2), (H)17 follow-ups 4–5
(TYPEI5, TYPEI6), (H)34 follow-ups (13B, 13C, 17B, 17C), (F)11 (x* refuted, x** candidate, now with the 13C ranges).
Papers: es-mn-short-note 25 pp (O97 + O104 §8; R97 and R104, ACCEPT); es-coverings-note 25 pp with R98 round 2
on the O91/O96 additions (TYPEI5 added). I stated that TYPEI6, MORDELL13C and MORDELL17B/17C are **not** in the
coverings note (checked by grep of the .tex). The summary got table rows E30 and P54–P56, the novelty "not
audited" list and the reading guide were extended, and the §1 paragraph and open problem 6 were updated.
ES is stated as not solved throughout.

## Notes for the parent
* R100's tree checker is fast enough to run the full certificate. The brief's fallback (sampling ≥ 2000 leaves)
  was therefore not used.
* Block (ej) needs libgmp headers; without gcc it skips with a message, but if gcc exists and `-lgmp` fails, the  engine part is skipped without an error (only the printed line says SKIPPED).
* My Edit calls with non-ASCII text sometimes inserted broken escape sequences. Every one was reverted or fixed,
  and a final grep found no `\uXXXX` remnants or CRs in STATUS.md, CAMPAIGN_SUMMARY.md or verify.py. A few new
  summary lines use ASCII notation (`<=`, `e-5`) for that reason.
