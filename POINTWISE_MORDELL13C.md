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

## 6. Theorem 3.1(b) sharpened (PROVED by finite computation; two independent checkers)

**Theorem 6.1.** Let p be a prime with `(p/13) = −1`. Then `4/p = 1/x+1/y+1/z` has a solution in positive
integers unless p lies in one of the 35459 residue classes listed as *open* leaves of
`data/mordell13c/tree6_6000.json.gz` (moduli `L | 2^7·3^5·5^4·7^4·11^4·13^4·∏_{17≤ℓ≤83}ℓ`, all of them
refinements of the six classes of POINTWISE_MORDELL Thm 3.1(b)). Their union has Haar density
**8.42·10⁻⁵ of the six classes** of Thm 3.1(b) (i.e. `≈2.3·10⁻⁷` of the Mordell-hard residues with `(p/13)=−1`,
using the 6/2160 of POINTWISE_MORDELL §3).

*Proof.* Thm 3.1(b) outside the six roots. Inside: the tree (`m13c_dfs.py` with brute-force classes `M≤10⁶`,
primes ≤ 100, 6000 expansions) has 136494 covered leaves using 2140 distinct ET classes; `m13c_check.py` and
`m13c_review_tree.py` (§4) both accept it (`CERTIFICATE OK`, `REVIEW OK`; 15 s resp. 7 s). The split primes are ≤ 83
and satisfy ES directly. ∎

*Scope.* This is the Salez/ET level sieve pushed adaptively, with explicit certificate; it shrinks the exceptional
set by a factor ≈1.2·10⁴ but **does not remove any of the six classes**: in every root, open leaves remain
(the open mass decays like a power of the node count, cf. §1). It is not progress towards zero exceptions
in any structural sense.
