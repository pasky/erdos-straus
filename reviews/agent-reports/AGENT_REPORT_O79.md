# AGENT REPORT O79 — verify.py blocks (dt)–(dv) (branch `side-agent/verify-blocks-6`)

Added three replay blocks after (ds), same style as (dn)–(ds) (scripts run as subprocesses with
`OMP_NUM_THREADS=2`, exact-string assertions on their outputs, plus small independent inline checks):

| block | document | what is replayed | time |
|---|---|---|---|
| (dt) | EXCEPTIONAL_LARGESIEVE7 | Lemmas 1.1–1.2 for all M ≡ 3 (4), M < 2000: `largesieve7_triples.py 2000` (9472 triples) and R73 `review_ls7_triples.py 2000 2000` (16513 pinning checks, brute-force `H* ≤ min(max(u,v),4u²t,4v²t)` on all 9472, 0 failures; Remark (a) (167, 9): H* = 13 via −13/5); R73 `review_ls7_counterex.py` (135 Prop 4.1 + 1218 Prop 5.1 instances, 0 failures); inline pure-Python H* on 134 Prop 4.1 instances (H* = k, residue −1/k at all p ∈ P) and 64 Prop 5.1 instances (H* ≥ pq/(4ℓ+1)) | ~6 s |
| (du) | POINTWISE_MN2 | §4 table: `mn2_delta.py 5 8 9 11 13 16 17` (\|H\| = 12, 18, 132, 898, 1796, 17510; 1/δ as tabled) and `mn2_delta.py 7 8 11`; R74 `review_mn2_delta.py` exact fractions (m = 5: 1/4, 1/8, 11/120, 449/8640; m = 6: 7/20, 421/1440); inline from the definition δ_5(Q(8)) = 12/48, δ_5(Q(9)) = 18/144, \|H_5(840)\| = 48/192 | ~0.5 s |
| (dv) | POINTWISE_TAIL | Lemma 3.1: R76 `review_tail_leaves.py 1` (seed 0, 543 leaves; the full 6-seed run is ~60 s, too slow); inline independent toy mod 8·3·5³·7 with a forced step at 3 and 16 sha256-hash rules over {5 (cap 3), 7 (cap 1)} — 1085 leaves, lifts at 5 exercised (level ≥ 2 leaves in all non-trivial trees): exact leaf probabilities sum to 1, `P_proc(L) = 4·2^{k_L}/φ(Q_L)`, disjoint fibres, union equals the n ≡ 1 (8) units surviving their own path; also R76 `review_tail_twist.py 1e5 30 300` ratio within its stated bound (EVIDENCE) | ~9 s |

Full `verify.py` under `ulimit -v 8000000`, `taskset -c 0,1`, `uv run --with scipy --with mpmath`:
**all checks passed**, 5 m 7 s wall, no skips. STATUS.md verify.py bullet added.

Notes / limits: these are replays of finite checks and toys; they do not upgrade any label
(LS7 Props 4.1/5.1 asymptotic parts, MN2's circularity Assessment, and TAIL Lemma 3.2's Euler-product
claim are still only as proved in their documents). No document text changed except STATUS.md.
