# Review R73 of EXCEPTIONAL_LARGESIEVE7.md (hostile reviewer, branch side-agent/review-ls7)

Status: in progress. Reviewed text: `EXCEPTIONAL_LARGESIEVE7.md` as merged from
`side-agent/residue-dispersion` (commit 6bae2a4). From-scratch scripts: `scripts/review_ls7_*.py`.

## Verdict summary (per claim)

| claim | verdict |
|---|---|
| Lemma 1.1 | SOUND (proof re-derived; brute force M<20000) |
| Lemma 1.2 | SOUND (re-derived; brute force all p \| M, M<20000) |
| Lemmas 2.1–2.2 | (pending) |
| Thm 3.1 | (pending) |
| Prop 4.1 | (pending) |
| Remark 4.2 | (pending) |
| Thm 4.3 | (pending) |
| Prop 5.1 | (pending) |
| (RD′) / §5 sketch | (pending) |
| Cor 6.1, §7 | (pending) |

## Defects

(numbered below as found)

## Per-claim notes

### Lemmas 1.1, 1.2 — SOUND
Re-derived: `g = gcd(D,A)`, `u = D/g`, `v = A/g` is coprime, `u | Av` ⇒ `u | A`, `uv | A`;
injectivity via `gcd((A/v)u, A) = A/v`; `4A ≡ 1 (M)` gives the three congruent labels, all of
the admissible form `−r/s`, `r ≥ 0`, `s ≥ 1`, `gcd(s,M) = 1` (LS6 §6.2 definition of H*), so
the H* bound is immediate. Lemma 1.2: `uvt = A ≡ 1/4 (p)` for odd `p | M`. Correct.
`scripts/review_ls7_triples.py` (from scratch; `uv run --with sympy --with numpy`): for all
`M ≡ 3 (4)`, `M < 20000`: set equality `{−4D : D | A²} = {−u/v}`, the bijection, `D = u²t`,
`A²/D = v²t`, all three label congruences, and Lemma 1.2's pinning at every prime `p | M`
(310815 (triple, prime) pairs) — 0 failures. Additionally (not checked by the author) the
H* upper bound `H* ≤ min(max(u,v), 4u²t, 4v²t)` against a brute-force least-label-height
for all `M < 4000` (22502 triples; equality in 20608) — 0 failures; Remark (a)'s example
`M = 167`, class 131, `H* = 13` via `−13/5` confirmed. (The author's "159390 triples" counts
triples, not (triple, prime) pairs — consistent.)
