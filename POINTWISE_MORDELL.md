# POINTWISE_MORDELL — Mordell-type coverings of non-residue classes mod a new prime r (task O80)

Status: work in progress (side agent O80, branch `side-agent/mordell-13`). Labels as in DISCOVERIES.md.

## 0. Setup

*Families.* ET Prop 1.9 (arXiv:1107.1010, §10) lists seven families of residue classes
(four Type I: I1–I4, three Type II: II1–II3). Each class is solvable by polynomials:
every sufficiently large n in the class has the explicit ES solution obtained from ET's
parametrisation (proof of Prop 1.9) and the maps `π^I=(abdn,acd,bcd)`, `π^II=(abd,acdn,bcdn)`.
(R80 repair, applied by reviewer.) In fact every n ≥ 1 in the class works. With the three family
parameters fixed, the coordinates x,y,z are polynomials in n of degree ≤ 4 with non-negative
coefficients (II3: `b=(n+e)/(4ad)`), and they are positive at n = 1, so they are positive for all n ≥ 1.
(O85 correction: this previously said "degree ≤ 2". The true (x,y,z)-degrees are I1 (2,1,2), I2 (3,1,2),
I3 (4,1,2), I4 (2,1,1), II1 (1,2,2), II2 (1,1,2), II3 (1,2,3). The integrality test must therefore use
s = 0,…,4, as `scripts/mordell_check.py` does via the true degree. B = 1 stands. Checked for all 153
certificate coordinates in verify.py block (dx).) Integrality on the class
is the class condition. For the certificates of §3 one can therefore take B = 1 below.
`scripts/mordell_lib.py` implements: `cls_modulus_residues(fam,P)` (modulus M and residues),
`solve(fam,P,n)` (returns (x,y,z), checked with exact fractions), `classes_for_modulus(M)`
(all classes of exact modulus M), `residue_table(M)`.
Sanity: 7955 random (class, n) samples all solve (0 failures); `residue_table` reproduces
Salez's `S_7={3,5,6}`, `S_11={7,8,10}`, and contains no square residue mod 840.

*Target set.* `Σ_r` (main variant): units x of `Ẑ` with `x≡1 (24)`, x a square mod 5 and 7
(Mordell-hard), x a non-square mod r. Variant 'np': also a non-zero square mod every prime `5≤ℓ<r`.
A prime `p>r` lies in `Σ_r^{np}` iff it is Mordell-hard... with `n_p=r` (reciprocity).

*Compactness.* Each class is clopen in `Ẑ`, `Σ_r` is compact. Hence a finite covering of `Σ_r`
by family classes exists iff every point of `Σ_r` lies in some class (PROVED, trivial).
Given such a covering with moduli M_i and with all ET coordinates positive for `n>B`,
ES holds for every prime `p∈Σ_r` with `p>B` (and the rest is a finite check).

## 1. First computations (EVIDENCE)

`mordell_cover.py r variant Mmax stages`: level-wise filter of unit residues of `Σ_r` mod
`L` by all class moduli `M|L`, `M≤Mmax`.
* r=7: covered already mod 5880 (Mordell's theorem, sanity check).
* r=13, Mmax=10⁵, stages 2,3,11,17,19: uncovered 4/36 at L=10920, then 50 of 622080 lifts
  at `L=2^4·3^2·5·7·11·13·17·19`. The residues 5,6,8,11 mod 13 are covered at low level;
  **the survivors are all `≡2` or `7 (mod 13)`** (note `2·7≡1`), `≡1 (16)`, mostly `≡1 (9)`.
* Larger moduli do not help at fixed prime support: with `Mmax=10⁷, 10⁸` the counts at
  `L=2^4·3^2·5·7·11·13^2·17·19·23` are 1438, 1412 (R80 repair, applied by reviewer: 1499 at 10^6 and 2620 at 10^5, both confirmed by
  `scripts/review_mordell_deep.py` and by `mordell_cover.py`; this previously read 1499 at 10⁵). Survivors need new primes.
* Survivor structure at `L=720720`: six nodes, `x≡1 (16)`, `x≡1,7 (9)`, and
  `(x mod 11, x mod 13) ∈ {(2,2),(2,7),(6,7),(9,7)}`.
* **13-generic points are covered.** Points with `x_q=1` for all `q≠13` are covered at
  13-level 1 for every non-residue u: `u≡2`: II2 `(a,d,f)=(9,2,143)` (residue 67 mod 143,
  `≡1 (11)`); `u≡7`: II2 `(2,2,143)`; `u≡5,6,8,11`: II2 with f=39. So the hard points are not
  13-generic; they need special residues at 11 as well.
* `mordell_probe.py L x Mmax lmax`: for a node, survivors among the children at one new prime ℓ.
  For the nodes 352801, 473761 (mod 720720) about half of the children survive at each
  ℓ∈[29,59]; at ℓ=17 only 5 resp. 1 survive. Not a square-class pattern.

## 2. Adaptive search and T-generic points (EVIDENCE)

`mordell_dfs.py r variant Mmax Pmax emax maxnodes`: best-first (largest open Haar mass) tree
search; each node refined at the prime (power) with the fewest uncovered children.
* r=13, np variant, Mmax=10⁷, primes ≤60: after 4000 nodes the open Haar mass is 1.8·10⁻⁶ of
  `Σ_13^{np}` and decreasing slowly (7.8e-6 at 800 nodes); the queue grows ≈6 per node.
  Deep open leaves are squares at every prime ≥17 they visit, with `x_13≡7 (13³)`, `x_11≡9`.
* *T-generic points* (`mordell_tgen.py`): points with `x_q=1` for all `q∉T`. A class of modulus
  `M=M_T·N` meets them iff its residue is `≡1 (mod N)`, giving a box in `∏_{q∈T}ℤ_q`.
  T={11,13}, resolution `11²·13²`, target `x_13` non-square:
  * M≤3·10⁴: 225 boxes, uncovered 3.05% (cells ≡ (9,7), (2,2), (2,7) mod (11,13));
  * M≤10⁶: 534 boxes, uncovered 0.57%: **only cells ≡ (2,2) mod (11,13) remain** (49 of the 143
    cells mod `11²·13²` above (2,2)).
  The 49 uncovered cells are nearly a product: `x_11 mod 121 ∈ {2,57,68,79,101}` (5 of the 11
  lifts of 2) times `x_13 mod 169 ∈ {2,15,28,41,54,67,80,93,132,145}` (10 of 13 lifts), minus (57,41).
* Other T (coarse resolution k=1, i.e. cells mod ∏_{q∈T} q, boxes with `v_q(M)≤1`, M≤3·10⁴):
  T={13,ℓ} for ℓ=2,3,5,7,17,19,23 — every target cell covered (main variant).
  np variant (x_11 square), M≤10⁵: T={11,13,ℓ} for ℓ=2,3,5,7,17,19,23 and T={13,17,19} — all
  covered except `(x_2≡1 (16), 9, 7)` for T={2,11,13}, which is the cell (9,7) covered at M≤10⁶.
  So **for the np variant no T-generic obstruction is visible** for |T|≤3; for the main variant
  the cell `x_11≡2 (11), x_13≡2 (13)` is the only T-generic survivor found.
* Same with resolution `11³·13³` (M≤10⁶, boxes with `v_q(M)≤3`): 1306 boxes, uncovered 0.44% of
  the target (5390 cells, all in the (2,2) cell, i.e. 26% of that cell; at resolution 2 it was
  34%, at M≤3·10⁴ 56%). Slow decay — consistent with either a sterile set or late coverage.

### 2.1 T-generic classes = ℤ[1/T]-points of the ES variety at n=1 (PROVED, elementary)

For each family the class is exactly the set of n for which ET's non-constant coordinates
(linear/quadratic in n with integer coefficients over the modulus) are integers. At a T-generic
point (`x_q=1` for q∉T) integrality at q∉T is integrality of the coordinates at **n=1**.
Writing `m'` for the T-free part, the T-generic conditions are:

| family | constants | T-generic condition (besides the family's coprimality) | box residue mod F=T-part of M |
|---|---|---|---|
| I1 | a,d,f; `f∣4a²d+1` | `4(ad)'∣f+1` | `−f` |
| I2 | a,c,f | `4(ac)'∣f+1`, `f'∣a+c` | `−f` mod `(ac)_T`, `−c/a` mod `f_T` |
| I3 | c,d,f | `4(cd)'∣f+1`, `f'∣4c²d+1` | `−f` mod `(cd)_T`, roots of `n²≡−4c²d` mod `f_T` |
| I4 | a,b,e; `e∣a+b` | `4(ab)'∣e+1` | `−1/e` |
| II1 | a,b,e; `e∣a+b` | `4(ab)'∣e+1` | `−e` |
| II2 | a,d,f; `4ad∣f+1` | `f'∣4a²d+1` | `−4a²d` |
| II3 | a,d,e | `4(ad)'∣e+1`, `e'∣4a²d+1` | `−4a²d−e` |

(Derivations: the coordinate formulas of ET §10; e.g. II2: `e=(n+4a²d)/f`, so T-generic ⟺
`f'∣1+4a²d`.) Rigid forms: II1/I4 ⟺ `4iabk=F(a+b+k)` with `k=(a+b)/e`, `e+1=4i·ab/F`
(symmetric in a,b,k); II2 ⟺ `4adm=f+1`, `g∣a+m` (f=Fg), equivalently with `a+m=gj`:
`(4dja−F)(4djm−F)=F²+4dj²`; I1 ⟺ `(4ni−1)(4nj−1)=4naF+1`, `ad=Fn`.
(R80 repair, applied by reviewer.) In the I1 rigid form, n is an auxiliary integer, not the ES
variable; read it as a fresh symbol, e.g. nu. Scope of the PROVED label: R80 independently
re-derived the II1/I4 and II2 rows, their rigid forms and the finiteness per T-level. The I1, I2,
I3 and II3 rows and the I1 rigid form were not independently re-checked.
* c²-generic points (x_q = c² for q∉T, c a T-unit rational), np variant, M≤10⁵, k=1:
  (c,T) = (2,{2,13}), (3,{3,13}), (5,{5,13}), (6,{2,3,13}), (7,{7,13}), (11,{11,13}), (1/2,·),
  (1/3,·), (2/3,·), (3/2,·): all covered. Also c-generic with c=−1 (T={2,3,7,11,13}),
  c=2, 1/2 (T={2,3,5,11,13}), c=−2 (T={2,5,7,13}): all covered. **No structured obstruction
  found for the np variant.**
* np DFS (Mmax=10⁷, primes ≤100): open mass ≈2.2·10⁻⁶ after 3600 nodes, decreasing slowly, queue
  growing ≈6/node. The heaviest open nodes are squares at every prime ≠13 they fix (x_13≡7).
  Probing one (L=10760950200, x=10675056841) at new primes ℓ≤100: surviving children are
  mostly, not only, squares; for ℓ≥61 more than half survive (the Mmax cap bites: M=ℓ·D needs
  D≤Mmax/ℓ).
* In the (2,2) cell of the main variant, the boxes found (M≤10⁶) mostly have F a pure power of 11
  or of 13 (53 boxes: F=1331: 20, 2197: 14, 121: 5, 169: 3, mixed F: 11), often with large T-free
  part (e.g. II2 f=1331·709). Since brute force in M truncates the T-free part, a complete
  enumeration per T-level F (rigid forms of §2.1) is needed.

## 3. Finite-exception Mordell-type theorems for r=13 (PROVED by finite computation; independently re-checked by R80, `scripts/review_mordell_check.py` (R80 repair, applied by reviewer))

**Theorem 3.1.** Let p be a prime with `(p/13) = −1`.
(a) If `(p/11) = +1`, then `4/p = 1/x+1/y+1/z` has a solution in positive integers unless
`p ≡ 112561 (mod 240240)`, i.e. `p≡1 (16)`, `p≡1 (3)`, `p≡1 (5)`, `p≡1 (7)`, `p≡9 (11)`, `p≡7 (13)`.
(b) Without condition at 11, the same holds unless
`p mod 720720 ∈ {112561, 352801, 380881, 418321, 473761, 483841}`.
(c) (R80 repair, applied by reviewer.) Combining both certificates, (a) sharpens to: if
`(p/11)=+1`, ES holds for p unless `p mod 720720 ∈ {112561, 352801}`. The third lift 592801 of
112561 mod 240240 is covered by the main certificate. These two are exactly the (b) exceptions
with `(p/11)=+1`.

*Proof.* If p is not a square mod 840, Mordell's identities apply. Otherwise
`p mod L ∈ Σ_13` (L = 240240 for (a), 720720 for (b); np resp. main variant). The certificates
`data/mordell/cert_r13_np_240240.json` (20 classes) and `data/mordell/cert_r13_main_720720.json`
(31 classes) list ET Prop 1.9 classes. `scripts/mordell_check.py` (stand-alone; imports only
sympy) verifies for each class that ET's parametrisation gives `x,y,z ∈ ℚ[n]` with
`4xyz = n(xy+yz+zx)` identically and `x,y,z>0` for `n>1`; and that every residue of `Σ_13` mod L
other than the listed exceptions has a class whose `x,y,z` are integer-valued on the whole
progression `t+Lℤ` (a degree-k polynomial in s is integer-valued iff it is integral at
s=0,…,k). ∎

* Negative controls: deleting one class, or perturbing one parameter, makes the checker FAIL.
* Context and novelty (R80 repair, applied by reviewer). Theorem 3.1 is an **explicit packaging
  of the Salez/ET level sieve**, not a new kind of filter. Salez (arXiv:1406.6307 §3–4) sieves
  with seven modular equations, including filters with *composite* moduli (`S_m`, shortened
  `S*_55, S*_65, S*_77, …`), and tabulates the uncertified residue sets `R_i` mod
  `G_i = 840, 9240, 120120, …`. Mihnea–Dumitru (arXiv:2509.00128) extend this to
  `G_8 = 25878772920`. Using all ET Prop 1.9 classes with modulus `| L`, R80
  (`scripts/review_mordell_level.py`) reproduces Salez's counts `#R_3=34`, `#R_4=192` exactly.
  Salez's `R_4` (mod 120120) already contains only 7 residues with `(p/13)=−1`
  ({3361, 20521, 57961, 79081, 90721, 112561, 113401}; 2 of them with `(p/11)=+1`). So a
  Theorem-3.1-type statement mod 120120 follows from Salez's 2014 data. Theorem 3.1 is the same
  sieve one level deeper (2⁴, 3²), sliced by `(p/13)`, with explicit, independently checkable
  certificates. The single-prime filter `S_13={0,5,6,8,11}` gives `p≡5,6,8,11 (13)`. The level
  sieve also handles the residues 2 and 7 mod 13, except for the listed classes, which carry 1/360 (a) resp. 6/2160 (b) of the Mordell-hard primes with `(p/13)=−1`.
  Deeper levels shrink the exceptional set (e.g. 1412 residues mod `L=2^4·3^2·5·7·11·13^2·17·19·23`
  in case (b); R80 repair, applied by reviewer: relative density 7.9e-6 of the (p/13)=-1 Mordell-hard
  residues, or 4.0e-6 of all Mordell-hard residues; this previously read 1.6·10⁻⁶) but, by §1–2, apparently never to zero in case (b).

## 4. The candidate sterile point x* for the main variant (EVIDENCE / CERTIFIED computation)

(R80 repair, applied by reviewer.) Label scope: the next paragraph, with its survivor rates and
uncovered percentages, is EVIDENCE only. Computation 4.1 is CERTIFIED. Its Consequence is PROVED.
Conjecture 4.2 is a CONJECTURE.

Complete rigid enumeration of the II1, II2, I4 boxes with T-level `F | 11³·13³`
(`mordell_rigid.py 11,13 3`; any T-free part; validated: it contains all 164 brute-force boxes
of these families) together with the all-family brute-force boxes (M≤10⁶) leaves 24.9% of the
(2,2) cell uncovered at resolution `11³·13³` (26.4% without the rigid boxes): the Type II
families contribute little here; the boxes in this cell are mostly I1. Survivors per added
digit: ≈5/11 then 9/11 (at 11), ≈10/13 then 11.6/13 (at 13) — not a product set.

**Computation 4.1 (CERTIFIED; see the R80 note below).** Let `x*∈Ẑ^×` have `x*_11=2`,
`x*_13=2`, `x*_q=1` for every other prime q. Then `x*∈Σ_13` (main variant), and
* (`mordell_point.py 1000000 11:2:8 13:2:8`) `x*` lies in no class, of any of the seven
  families, with modulus `M≤10⁶`;
* (`mordell_rigid.py 11,13 3` + `mordell_cellcov.py`) `x*` lies in no II1/II2/I4 class whose
  modulus has {11,13}-part dividing `11³·13³` (T-free part unrestricted).

*R80 note (R80 repair, applied by reviewer).* An independent from-scratch engine
(`scripts/review_mordell_point.py`) confirms the first clause in full: 0 classes with M up to 10^6.
The second clause was re-checked by `scripts/review_mordell_rigid.py` for every T-level F dividing
11^3*13^3 except F = 11^3*13^3 itself. That level, and the level-4 extension in 4.1 below, rest on
one engine only. In the Consequence below, the exponent 8 is arbitrary. The precise statement is
`p = x* modulo the lcm of the moduli`; for moduli up to 10^6, exponent 5 already suffices.

*Consequence (PROVED from 4.1).* Every finite covering of `Σ_13` (main) by ET classes contains a
class with modulus `>10⁶`. Indeed a finite union of clopen classes missing `x*` misses a
neighbourhood of `x*`, i.e. a reduced residue class `p≡1 (mod Q)`, `p≡2 (mod 11^8·13^8)` with Q
coprime to 143, which contains infinitely many primes (Dirichlet), all Mordell-hard with
`(p/13)=−1`.

**Conjecture 4.2.** `x*` is sterile: it lies in no ET Prop 1.9 class. In particular (R80 repair,
applied by reviewer; this is an implication, not an equivalence, since another point of `Σ_13` (main) could be
sterile even if `x*` is not; the argument is Dirichlet near `x*`, then ET Prop 1.9's converse on
the identity's primitive class containing `x*`, then compactness + Dirichlet again) no finite set of polynomial ES identities covers all sufficiently
large Mordell-hard primes with `(p/13)=(p/11)=−1`; Theorem 3.1(b) cannot be improved to zero
exceptions.

*Why Theorem C does not explain it (Assessment; R80 repair, applied by reviewer).* The first
statement is correct: x* is not square-mimicking, so Theorem C does not apply. The parity remark
and the "TYPEI2 mechanism" below are heuristic; no lemma or computation backs them here. `x*` is not square-mimicking: `x*_11, x*_13` are
non-residues, and Jacobi-parity arguments (ET Prop 1.6 style) only force odd total
{11,13}-valuation in the relevant parameters — satisfiable. The mechanism is the TYPEI2 one:
at T-generic points the classes become rigid (finitely many boxes per T-level, §2.1), so a
specific T-adic point can escape all of them. Like `x̂_9` of TYPEI2 (Conj 3.4) this is open.

### 4.1 Background runs completed (2026-10-06)

* `mordell_rigid.py 11,13 4` finished (log `/tmp/o80_rigid4.txt`, 6865 boxes; largest level
  `F=11⁴·13⁴` took 81 min). Levels with even total valuation (`F=11^α13^β`, α+β even) contribute
  no II1/II2/I4 boxes, as at lower levels. **No box contains `x*`** (u=2 at both primes), so
  Computation 4.1's second clause extends to {11,13}-part dividing `11⁴·13⁴` (CERTIFIED, one
  engine). Uncovered part of the (2,2) cell at resolution `11⁴·13⁴` (all-family brute-force boxes
  with M≤10⁶ and v_q≤3, plus rigid II boxes): 24.88% with rigid level ≤3, **24.76%** with level ≤4
  (EVIDENCE: level 4 barely moves it).
* np DFS (`mordell_dfs.py 13 np 10000000 100 3 30000`) finished at its node cap: 30000 nodes
  expanded, 197786 open leaves, open Haar mass **4.10·10⁻⁷** of `Σ_13^{np}` (5.5·10⁻⁷ at 16800
  nodes). Still undecided; no covering found (EVIDENCE).

## 5. r=11 and r=17 (EVIDENCE)

* Level-wise covering (Mmax=10⁷): r=11 main/np: 8 survivors mod `2^4·3^2·5·7·11` (np = main,
  as no prime 5≤ℓ<11 besides 5,7). Survivors have `x_11∈{2,6}` (Salez: `S_11={0,7,8,10}`).
  r=17 main: 50 survivors mod `2^4·3^2·5·7·11·13·17`; np: 19/1440 at the base `L=2042040`.
* T-generic (M≤10⁵): r=11: T={11} covered (k=2); T={11,13}: cells (2,2),(2,7) uncovered at k=1;
  T={11,17}: covered.
* **r=17, T={17}: the cells `x_17≡5` and `x_17≡7 (mod 17)` (note 5·7≡1) are entirely
  uncovered by all classes with M≤10⁵ (k=2).** Complete rigid II1/II2/I4 enumeration with
  `F=17^β`, β≤4: boxes exist only at odd β; at β=3 they cover 13 of the 289 subcells of each of
  the two cells (4.5%); residues mod 17³ in cell 5: 192, 1501, 1739, 2436, 3031, 3252, 3813, 4034,
  4493, 4578, 4731, 4748, 4850. No II box contains u=5, 7, −12, 22, 90.
  So for r=17 the candidate sterile point is one-dimensional: `x̃_17=u` (u≡5 or 7 mod 17),
  `x̃_q=1` for all q≠17 — the simplest possible shape (a twist at r only).

**Computation 5.1 (CERTIFIED, two independent engines; R80 repair, applied by reviewer: R80's
`review_mordell_point.py` gives 0 classes with M up to 10^6 for u=5, and up to 10^5 for u=7;
`review_mordell_rigid.py 4 17:5` and `4 17:7` find no II1/I4/II2 class with 17-part dividing 17^4).** Let `x̃∈Ẑ^×` have `x̃_17=5`,
`x̃_q=1` for all q≠17. Then `x̃∈Σ_17^{np}` (a square at every prime <17, a non-square at 17), and
(`mordell_point.py 1000000 17:5:8`) `x̃` lies in no ET class with modulus `≤10⁶`; nor in any
II1/II2/I4 class with 17-part dividing `17⁴` (rigid enumeration). Consequence (PROVED from 5.1, as
in §4): every finite ET covering of the Mordell-hard primes with `n_p=17` (even of the np
variant) contains a class of modulus `>10⁶`.
**Conjecture 5.2.** `x̃` is sterile; then no finite set of polynomial identities proves ES for all
primes with `n_p=17`.

## Replay

```
PYTHONPATH=scripts uv run python scripts/mordell_check.py data/mordell/cert_r13_np_240240.json
PYTHONPATH=scripts uv run python scripts/mordell_check.py data/mordell/cert_r13_main_720720.json
PYTHONPATH=scripts uv run python scripts/mordell_cert.py 13 main 100000000 720720 /tmp/c.json   # regenerate
PYTHONPATH=scripts uv run python scripts/mordell_cover.py 13 main 100000000 2,3,11,17,13,19,23  # §1
PYTHONPATH=scripts uv run python scripts/mordell_tgen.py 1000000 13 3 11,13       # §2 (~16 min)
PYTHONPATH=scripts uv run python scripts/mordell_rigid.py 11,13 3                 # §4 (~30 s)
uv run python scripts/mordell_cellcov.py 3 /tmp/o80_rigid_11,13_3.pkl /tmp/o80_boxes_1000000_11,13_3.pkl
PYTHONPATH=scripts uv run python scripts/mordell_point.py 1000000 11:2:8 13:2:8   # Comp 4.1 (~15 min)
PYTHONPATH=scripts uv run python scripts/mordell_point.py 1000000 17:5:8   # Comp 5.1 (~15 min)
PYTHONPATH=scripts uv run python scripts/mordell_rigid.py 17 4; PYTHONPATH=scripts uv run python scripts/mordell_tgen.py 100000 17 2 17
MORDELL_I1CAP=1e11 PYTHONPATH=scripts uv run python scripts/mordell_dfs.py 13 np 10000000 100 3 30000 /tmp/t.json
```
