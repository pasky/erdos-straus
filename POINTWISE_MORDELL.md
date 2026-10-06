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
