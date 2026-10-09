# POINTWISE_MORDELL13C — reducing the exceptional classes of Theorem 3.1(b) (task O100)

Status: work in progress (side agent O100, branch `side-agent/r13-cover-all`). Labels as in DISCOVERIES.md.
Builds on POINTWISE_MORDELL.md (Thm 3.1), POINTWISE_MORDELL13B.md (§1–5).

## 0. The six exceptional classes mod 720720 (local data)

| p mod 720720 | mod 16 | mod 9 | mod 5 | mod 7 | mod 11 | mod 13 |
|---|---|---|---|---|---|---|
| 112561 | 1 | 7 | 1 | 1 | 9 | 7 |
| 352801 | 1 | 1 | 1 | 1 | 9 | 7 |
| 380881 | 1 | 1 | 1 | 4 | 6 | 7 |
| 418321 | 1 | 1 | 1 | 1 | 2 | 7 |
| 473761 | 1 | 1 | 1 | 1 | 2 | 2 |
| 483841 | 1 | 1 | 1 | 1 | 6 | 7 |

Observation (trivial). Only the last four classes contain {11,13}-generic points (`x_q=1` for q∉{11,13}).
112561 (`x≡7 mod 9`) and 380881 (`x≡4 mod 7`) contain none; their "simplest" points are
{3,11,13}- resp. {7,11,13}-generic. x** = x(2,15) lies in 473761.

## 1. First runs (EVIDENCE)

* `scripts/m13c_dfs.py` = the `mordell_dfs` engine started from explicit roots `x:L`.
  Root 112561 mod 720720, brute-force classes `M≤10⁶`, primes ≤60: after 400 expanded nodes,
  2263 open leaves, open mass `2.19·10⁻⁴` of the root, the queue growing ≈5.7 per node.
  The heaviest open leaves are squares at every prime `≥17` they fix (e.g. `x≡8 (17)`, `17 (19)`, `13 (23)`,
  `10 (31)`) and match no rational of height `<3000` at 2,3,5,7,11,17,19,23,31.
* *Non-square lemma (EVIDENCE; classical in spirit, cf. Mordell/Yamamoto, ET Prop. 1.6).* `scripts/m13c_sqchk.py`:
  for every ET class with `M≤6000` (102124 residues) the residue is a local non-square at some prime of M
  (2-adic: `r≢1 (8)` if `8∣M`, `r≢1 (4)` if `4∥M`). Consequently the points of an exceptional class that are
  local squares at every prime `q∉{11,13}` (resp. `≠13` in the cells `x_11≡9`) can only be covered by classes
  whose "non-square witness" is 11 or 13. This is the hard core the DFS leaves converge to.
