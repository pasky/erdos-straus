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

## 2. Complete witness at a fixed level (CERTIFIED engine, validated)

`scripts/m13c_witness.py` lists **all** ET classes with modulus `M | L` (no size cap) containing a node
`x + Lℤ`. Reductions (each elementary; see the docstring): for every pair `(a,d)` with `4ad | L`, the
parameters of I1, II1, I4 are determined by `x mod 4ad` (a divisor below `4ad` is the least positive residue;
for I1 a cofactor argument); II3/I2/I3 parameters are divisors of `gcd(K_c, x+4a²d)`, `gcd(K_c, ax+d)`,
`gcd(K_c, x²+4a²d)`; II2 runs over `f | L`, `f≡3 (4)`, `a | (f+1)/4`, with `d` determined mod f.
*Validation:* `scripts/m13c_witness_validate.py L` compares the full witness sets with brute-force
`mordell_lib` tables for every unit mod L: L = 9240, 10920, 65520 — 0 mismatches.

**Computation 2.1 (EVIDENCE for the role of moduli).** `scripts/m13c_level.py 1000000 13,17,19,23 complete`:
refining the six classes at 13, 17, 19, 23 (L = 69604975440) leaves 1499 residues uncovered by classes
`M | L, M≤10⁶`, and **1399** uncovered by *all* classes `M | L` (any size; cf. 1412 at `M≤10⁸`,
POINTWISE_MORDELL §3). Per root: 352801: 649, 112561: 250, 483841: 174, 473761: 132, 380881: 116,
418321: 78. At fixed prime support the modulus cap is not the bottleneck; new primes are.

## 3. T-generic picture for T = {3,11,13} and {7,11,13} (EVIDENCE, brute force M ≤ 10⁶, k = 2)

`mordell_tgen.py 1000000 13 2 3,11,13` (logs/o100_tgen_3,11,13.log): of the 25740 target cells mod
`9·121·169`, only 49 are uncovered, all with `x_3≡1 (9)` and `(x_11,x_13)≡(2,2)`.
`mordell_tgen.py 1000000 13 2 7,11,13`: 147 of 180180 uncovered, all `x_7≡1 (7)`, `(x_11,x_13)≡(2,2)`.
Hence the {3,11,13}-generic points of class 112561 (`x_3≡7 (9)`) and the {7,11,13}-generic points of
class 380881 (`x_7≡4 (7)`) are all covered, as are the {11,13}-generic points of 352801, 418321, 483841
(POINTWISE_MORDELL §2). **Only class 473761 contains known uncovered T-generic points (e.g. x**).**

**Computation 3.1 (CERTIFIED, complete at k = 2; engine of 13B §4).** 13B's k = 2 row was incomplete only because
ES levels up to `F²` are needed; for T-levels `F | 11²13²` the ES level N divides `F² | 11⁴13⁴` (13B Cor. 2.5), and the
only such N above 4·10⁷ is `11⁴13⁴ = 418161601`. `m13b_es 418161601` (72 min, 131104 solutions) + `m13b_invert.py`
(20668 boxes, none containing x*) + `m13b_cell.py 2` over all ES levels: **the uncovered part of the (2,2) cell at
resolution `11²·13²` is exactly the product `x_11 mod 121 ∈ {2,57,79}` × `x_13 mod 169 ∈ {15,28,54,132,145}`**
(15 of 143 subcells, 10.5%), now for *all* ET classes whose T-level divides `11²·13²` (any T-free part).

## 4. Tree certificates (method)

A tree certificate (`m13c_dfs.py` output) refines each of the six roots `x mod 720720` at primes p
(children = the unit residues `x+Lt mod Lp`; for `p∤L` the one non-unit child can contain only the prime
p itself); every leaf carries an ET class whose coordinates are integer-valued on the leaf's progression,
or is marked *open*. Two checkers:
* `scripts/m13c_check.py` (sympy engine of `mordell_check.py`: identity, positivity for n>1, integrality at
  s = 0..deg; recomputes the children of every split; ES checked directly for the split primes p with
  `(p/13)=−1`);
* `scripts/m13c_review_tree.py` (R80 engine `review_mordell_check.py`: coordinates re-derived from ET,
  exact Fractions, s = 0..4; re-checks the partition and that the leaf masses sum to 1).
Negative controls (a perturbed leaf parameter; a deleted child): both checkers FAIL.
If both pass, ES holds for every prime p with `(p/13)=−1` outside the open leaves (Theorem 3.1(b) handles all
residues outside the six roots).

## 5. x** = x(2,15): extended targeted searches (CERTIFIED within ranges, one engine)

**Computation 5.1.** `scripts/m13c_target2.c` (= `m13b_target2.c` + start offset; validated engine of
POINTWISE_MORDELL13B §5): x** lies in **no I2, II1, I4 class with `h = f, e ∈ (2·10⁷, 2·10⁸]`** and
`|i|,|j| ≤ 12` (logs/o100_xss_U_A.log `(2·10⁷,1.1·10⁸]`, logs/o100_xss_U_B.log `(1.1·10⁸,2·10⁸]`, 0 hits,
≈80 min each). Together with 13B Comp. 5.1: no I2/II1/I4 class up to `2·10⁸`; II3/I3/I1/II2 up to `10⁹` (13B Comp. 5.3).
Sanity: the same binary re-finds x*'s I2 datum (125, 88, 11999) on `(10⁴, 2·10⁴]`.
*The cap `|i|,|j|≤12` is vacuous here* (as for P/Q in 13B): at a T-prime q dividing `ab` (resp. `ac`) the box
condition is `e≡−u_q`, `u_q e≡−1` or `f≡−u_q (mod q^{v_q(ab)})` with `u_q∈{2,15}`, so
`q^{v_q(ab)} ≤ 15·2·10⁸+1 < 11¹⁰`, i.e. `v_q ≤ 9`; for `q | f` (I2) the T-exponents of `a, c` are 0 by coprimality.
After dropping a common T-factor, `|i|,|j| ≤ 9`. So Computation 5.1 holds with no T-level restriction.

**Computation 5.2.** `m13b_target 2 15 2000000000 20 1000000000` (logs/o100_xss_PQ_1e9_2e9.log, ≈4.3 h, one core):
x** lies in **no II3, I3, I1, II2 class with `e` (resp. `f`) in `(10⁹, 2·10⁹]`**, 0 hits. The cap 20 is vacuous
(13B §5 argument: `v_q(ad) ≤ log_11(2·10⁹+15) < 9`, so `v_q(λ) ≤ 16`). With 13B Comp. 5.3: no P/Q-type class with
`e ≤ 2·10⁹`. Extending to `10¹⁰` would take ≈ 36 core-hours with this engine (and a segmented sieve); not done.

## 6. Theorem 3.1(b) sharpened (PROVED by finite computation; two independent checkers)

**Theorem 6.1.** Let p be a prime with `(p/13) = −1`. Then `4/p = 1/x+1/y+1/z` has a solution in positive
integers unless p lies in one of the 35459 residue classes listed as *open* leaves of
`data/mordell13c/tree6_6000.json.gz` (moduli of the open leaves divide `2⁴·3²·5²·7²·11·13·∏_{17≤ℓ≤83}ℓ`, all of them
refinements of the six classes of POINTWISE_MORDELL Thm 3.1(b)). Their union has Haar density
**8.42·10⁻⁵ of the six classes** of Thm 3.1(b) (i.e. `≈2.3·10⁻⁷` of the Mordell-hard residues with `(p/13)=−1`,
using the 6/2160 of POINTWISE_MORDELL §3).

*Proof.* Thm 3.1(b) outside the six roots. Inside: the tree (`m13c_dfs.py` with brute-force classes `M≤10⁶`,
primes ≤ 100, 6000 expansions) has 136494 covered leaves using 2140 distinct ET classes; `m13c_check.py` and
`m13c_review_tree.py` (§4) both accept it (`CERTIFICATE OK`, `REVIEW OK`; 15 s resp. 7 s). The split primes are ≤ 83
and satisfy ES directly. ∎

Open leaves / open density per root: 112561: 13986 / 1.26·10⁻⁴; 352801: 18070 / 3.10·10⁻⁴;
380881: 873 / 1.93·10⁻⁵; 418321: 455 / 5.8·10⁻⁶; 473761: 871 / 1.62·10⁻⁵; 483841: 1204 / 2.78·10⁻⁵
(`/tmp`-free replay: see Replay). The two roots with `x_11≡9` (a square) are the hardest in measure: there the
non-square witness of a covering class (§1) must be 13 alone.

*Scope.* This is the Salez/ET level sieve pushed adaptively, with explicit certificate; it shrinks the exceptional
set by a factor ≈1.2·10⁴ but **does not remove any of the six classes**: in every root, open leaves remain
(the open mass decays like a power of the node count, cf. §1). It is not progress towards zero exceptions
in any structural sense.

## 7. What remains (Assessment)

* **Zero exceptions is not reached for any of the six classes.** Theorem 6.1 only thins them. No sterile point is
  proved anywhere.
* Class 473761 contains x** (T-generic, survives all targeted searches: I2/II1/I4 to `2·10⁸`, II3/I3/I1/II2 to `10⁹`,
  §5 and 13B). The other five classes contain **no** uncovered S-generic point for the S tested
  (S = {11,13}, {3,11,13}, {7,11,13}; §3), so no "simple" sterile candidate exists there; still the DFS open set
  does not close. Its open leaves in 418321 (the smallest) are all `≡1 (17)` and take exactly three values at each of
  19, 23, 31 (`{1,13,17}`, `{1,16,13}`, `{1,21,26}`), not all squares — the non-square heuristic of §1 is only
  approximate. Locating their limit points (candidate sterile points off the T-generic locus) is the natural next step.
* Fixed-level moduli are not the bottleneck (§2); the bottleneck is the number of primes in the support.

## Replay

```
R=112561:720720,352801:720720,380881:720720,418321:720720,473761:720720,483841:720720
PYTHONPATH=scripts uv run python scripts/m13c_dfs.py $R 1000000 100 3 6000 tree.json      # ~11 min; gzip -> data/mordell13c/
PYTHONPATH=scripts uv run python scripts/m13c_check.py data/mordell13c/tree6_6000.json.gz        # Thm 6.1, 15 s
PYTHONPATH=scripts uv run python scripts/m13c_review_tree.py data/mordell13c/tree6_6000.json.gz  # Thm 6.1, 7 s
PYTHONPATH=scripts uv run python scripts/m13c_tree_stats.py data/mordell13c/tree6_6000.json.gz   # per-root stats
for L in 9240 10920 65520; do PYTHONPATH=scripts uv run python scripts/m13c_witness_validate.py $L; done   # §2
PYTHONPATH=scripts uv run python scripts/m13c_level.py 1000000 13,17,19,23 complete          # Comp 2.1, ~16 min
PYTHONPATH=scripts uv run python scripts/mordell_tgen.py 1000000 13 2 3,11,13                 # §3, ~7 min (also 7,11,13)
uv run python scripts/m13c_sqchk.py                                                          # §1 (PYTHONPATH=scripts)
gcc -O2 -o /tmp/o100/es scripts/m13b_es.c; /tmp/o100/es 418161601 > R/es_418161601.txt   # Comp 3.1, 72 min; R = copy of 13B run dir
PYTHONPATH=scripts uv run python scripts/m13b_invert.py 418161601 R/es_418161601.txt R/inv_418161601.pkl; PYTHONPATH=scripts uv run python scripts/m13b_cell.py 2 R
gcc -O2 -o /tmp/o100/target2 scripts/m13c_target2.c; /tmp/o100/target2 2 15 110000000 12 20000000   # §5 (also 2e8 from 1.1e8)
```

## 8. Limit points of the open leaves (O100 continuation)

**Computation 8.1 (EVIDENCE/CERTIFIED by brute force).** For an open leaf `x mod L` let S = primes of L and
`P` its S-generic point (`P_q = x` for q∈S, `P_q = 1` otherwise). `scripts/m13c_sgen.py`: for all 455 open leaves of
root 418321 in Thm 6.1's tree, P lies in an ET class of modulus `≤ 2·10⁵` (453 leaves) resp. `≤ 10⁶` (the other
two: moduli 283140 and 235352). So **no S-generic sterile candidate sits at the frontier of 418321**; the leaves
are spread (no dominant joint residue pattern at 19, 23, 31, 41, 43, 71), not converging to a few points.
The open set persists because each covering class of P needs `x≡1` modulo its S-free part N, and the complement
`x≢1 (mod N)` opens new nodes.
