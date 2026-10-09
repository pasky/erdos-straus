# AGENT REPORT O115 — two-engine completion (compute only)

Branch `side-agent/two-engine-cells`. No disagreement between engines anywhere.

## TYPEI7 Cor 3.2 (17 cells, second engine `review_typei4_jsearch.c`)
Cells `b=2: L=22,23`; `b=3: L=20–22`; `b=4: L=16–19`; `b=5: L=14–17`; `b=6: L=13–15`; `b=7: L=12`: **0 hits each**
(author's `typei4_lb`: 0 each). `scripts/typei7_xcheck.py` against the author's `/tmp/t7/lb_*` files + completion
records: 17/17 agree. Times 65 s – 2238 s per cell (≈ 2.9 h CPU). Control `(14,3)` reproduced (1 hit = table row).
→ whole Cor 3.2 grid is two-engine. POINTWISE_TYPEI7.md §3a added; Cor 3.2 / Comp 3.4 / §5 scope sentences updated.

## TYPEI6 Cor 4.2 (3 cells, R99 engine `review_typei6_vsearch.c`)
| (L,b) | solutions | R99 pass-bound | author candidates | time |
|---|---|---|---|---|
| (10,14) | 0 | 1 499 924 669 | 1 499 924 669 | 2289 s |
| (9,15) | 0 | 2 178 532 979 | 2 178 532 980 | 3855 s |
| (10,15) | 0 | 5 491 182 408 | 5 491 182 409 | 13187 s |

The off-by-one counts are the known safe-direction slack effect (author's `1+1e-9` admits a superset). New diagnostic
`scripts/o115_slack_boundary.py` (exact rationals, `P_1 ≤ 999`) finds exactly the extra candidate in each
off-by-one cell (`(9,15)`: `a=1,c'=1359402097,δ=1,P_1=3`; `(10,15)`: `a=1,c'=4940395087,δ=1,P_1=1`), none at `(10,14)`.
It also re-finds R99's known `(9,12)` extra and one at `(9,14)`, and none at `(10,13)`, which serve as controls.
→ all of Cor 4.2 is two-engine. POINTWISE_TYPEI6.md updated.

## Also
STATUS.md (TYPEI6 scope line) and DISCOVERIES.md (Follow-ups 5, 6) scope sentences updated: "two engines, all cells".
Logs: `reviews/agent-reports/O115_two_engine_log.txt`. Labels unchanged (CERTIFIED once replayed).

## Replay
```
ulimit -v 8000000
gcc -O2 -o js scripts/review_typei4_jsearch.c -lm; ./js L b        # 17 TYPEI7 cells; then typei7_xcheck.py DIR
gcc -O2 -o vs scripts/review_typei6_vsearch.c -lgmp -lm; ./vs L b  # (10,14),(9,15),(10,15)
uv run python scripts/o115_slack_boundary.py 10 15 999             # slack diagnostic (seconds)
```
