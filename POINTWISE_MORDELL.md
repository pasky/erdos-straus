# POINTWISE_MORDELL — Mordell-type coverings of non-residue classes mod a new prime r (task O80)

Status: work in progress (side agent O80, branch `side-agent/mordell-13`). Labels as in DISCOVERIES.md.

## 0. Setup

*Families.* ET Prop 1.9 (arXiv:1107.1010, §10) lists seven families of residue classes
(four Type I: I1–I4, three Type II: II1–II3). Each class is solvable by polynomials:
every sufficiently large n in the class has the explicit ES solution obtained from ET's
parametrisation (proof of Prop 1.9) and the maps `π^I=(abdn,acd,bcd)`, `π^II=(abd,acdn,bcdn)`.
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
  `L=2^4·3^2·5·7·11·13^2·17·19·23` are 1438, 1412 (vs 1499 at 10⁵). Survivors need new primes.
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

## 3. Finite-exception Mordell-type theorems for r=13 (PROVED by finite computation; independent re-check pending)

**Theorem 3.1.** Let p be a prime with `(p/13) = −1`.
(a) If `(p/11) = +1`, then `4/p = 1/x+1/y+1/z` has a solution in positive integers unless
`p ≡ 112561 (mod 240240)`, i.e. `p≡1 (16)`, `p≡1 (3)`, `p≡1 (5)`, `p≡1 (7)`, `p≡9 (11)`, `p≡7 (13)`.
(b) Without condition at 11, the same holds unless
`p mod 720720 ∈ {112561, 352801, 380881, 418321, 473761, 483841}`.

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
* Context: Salez's single-prime filter `S_13={0,5,6,8,11}` (arXiv:1406.6307 §3.1) gives
  `p≡5,6,8,11 (13)`; Theorem 3.1 adds the residues 2 and 7 mod 13 except for the listed
  classes, which carry 1/360 (a) resp. 6/2160 (b) of the Mordell-hard primes with `(p/13)=−1`.
  Deeper levels shrink the exceptional set (e.g. 1412 residues mod `L=2^4·3^2·5·7·11·13^2·17·19·23`
  in case (b), relative density 1.6·10⁻⁶) but, by §1–2, apparently never to zero in case (b).
