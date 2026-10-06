# POINTWISE_MORDELL17 — sterility at r = 17 (task O83)

Status: work in progress (side agent O83, branch `side-agent/sterility-r17`). Builds on
POINTWISE_MORDELL.md (§2.1, §5; unreviewed author branch `side-agent/mordell-13`).
Labels as in DISCOVERIES.md.

Notation. T = {17}. A point `x∈Ẑ^×` is *17-generic* if `x_q = 1` for all q ≠ 17; write
`x = x(u)`, `u = x_17 ∈ ℤ_17^×`. Cell `C_v = {u ≡ v (mod 17)}`, v ∈ {5, 7} (non-residues,
5·7 ≡ 1). A class of modulus `M = 17^k·N` (17 ∤ N) contains `x(u)` iff its residue `r` satisfies
`r ≡ 1 (mod N)` and `u ≡ r (mod 17^k)`; then it contributes the *box* `r + 17^k ℤ_17` of
*level* `k`, `F = 17^k`. Haar measure on ℤ_17, `μ(C_v) = 1/17`.

## 1. The seven families collapse to four box types (PROVED, elementary)

From the T-generic conditions of POINTWISE_MORDELL §2.1 (which are just the ET coordinate
integrality conditions at `n=1` away from 17 and at `n=u` at 17). Throughout, all parameters are
positive integers, `F=17^k`, `'` = 17-free part, `g = f'`.

**Lemma 1.1.** At level `F = 17^k`, the boxes of the seven ET families are exactly the boxes of:

* **(P)** `(a,d,f)`, `17∤f`, `f | 4a²d+1`, `4(ad)' | f+1`, `(ad)_17 = F`; box `−f (mod F)`.
  [= I1; = I3 with `17 | cd`; = II3 with `17 | ad`.]
* **(Q)** `(a,d,f)`, `f = Fg`, `17∤g`, `4ad | f+1`, `g | 4a²d+1`; box `−4a²d (mod F)`.
  [= II2; = II3 with `17 | e`.]
* **(Q⁻¹)** box `−1/(4a²d)` for each (Q)-datum. [= I2 with `17 | f`.]
* **(√Q)** boxes `±√(−4a²d) (mod F)` for each (Q)-datum. [= I3 with `17 | f`.]
* **(U)** `(a,b,e)`, `e | a+b`, `gcd(e,4ab)=1`, `4(ab)' | e+1`, `(ab)_17 = F`; box `−e (mod F)`.
  [= II1; = I2 with `17 | ac`.]
* **(U⁻¹)** box `−1/e` for each (U)-datum. [= I4.]

Moreover (P) is closed under `r ↦ 1/r` (so (P)∪(Q)∪(Q⁻¹)∪(U)∪(U⁻¹) is inversion-symmetric,
and `u ↦ 1/u` maps `C_5 ↔ C_7`; only (√Q) may break the symmetry).

*Proof.* Read off the table of POINTWISE_MORDELL §2.1 with T={17}, splitting each family by which
of its moduli carries the 17 (the gcd conditions of I2, I3, II3 forbid both):
I3 with `17∤f`: conditions `f | 4c²d+1`, `4(cd)'|f+1`, box `−f` mod `(cd)_17` — literally (P).
II3 with `17∤e`: `e | 4a²d+1`, `4(ad)'|e+1`, box `−4a²d−e ≡ −e` mod `(ad)_17` (as
`v_17(a²d) ≥ v_17(ad)`) — (P). II3 with `17 | e`: then `17∤ad`, `4ad | e+1`, `e' | 4a²d+1`, box
`−4a²d−e ≡ −4a²d` mod `e_17` — (Q). I2 with `17∤f`: `f | a+c`, `4(ac)'|f+1`, box `−f` mod
`(ac)_17`, `gcd(f,4ac)=1` — (U). I2 with `17 | f = Fg`: `4ac | Fg+1`, `g | a+c`, box `−c/a` mod F.
Put `t = (Fg+1)/(4ac)`; then `4at | Fg+1` and, as `g | a+c` and `g | 4ac·t−1 = 4at(a+c) − 4a²t − 1`,
`g | 4a²t+1`; so `(a,t,Fg)` is a (Q)-datum, and `c ≡ 1/(4at)` gives box `−c/a ≡ −1/(4a²t)`. Conversely
a (Q)-datum `(a,d,Fg)` gives the I2 class `(a, c=(Fg+1)/(4ad), Fg)` (`g | a+c` since
`m(4a²d+1) ≡ a+m (mod g)` for `m=c`, `4adc ≡ 1`). I3 with `17 | f`: `4cd | f+1`, `f' | 4c²d+1`
(the (Q) conditions with `a=c`), boxes the roots of `n² ≡ −4c²d` mod `f_17`.
(P) closed under inversion: `f* = (4a²d+1)/f` satisfies `f f* ≡ 1 (mod F)` and `f* ≡ −1 (mod 4(ad)')`,
so `(a,d,f*)` is a (P)-datum with box `−f* ≡ −f^{−1} = (−f)^{−1} (mod F)`. ∎

**Lemma 1.2 (no level-0 boxes).** No class of any family contains all 17-generic points
(i.e. there is no box with `F=1`). *Proof:* see §2 (rigid forms with F=1 have no solutions).

## 2. Box types = Erdős–Straus solutions of 4/17^K (PROVED, elementary)

ET notation (arXiv:1107.1010 §2): `Σ^I_n`: `4abcd = n(a+b)+c`, `e=(a+b)/c`, `f=4acd−n`,
`ef=4a²d+1`; `Σ^II_n`: `4abcd = a+b+nc`, `e=(a+b)/c`, `f=4acd−1`, `ef=n+4a²d`,
`4c²dn+1=f(4bcd−1)`. `π^I=(abdn,acd,bcd)`, `π^II=(abd,acdn,bcdn)` map N-points to ordered
solutions of `4/n=1/x+1/y+1/z`, injectively modulo the dilation `(λa,λb,λc,λ^{−2}d)`.

**Lemma 2.1 (Q ↔ Type I points of 4/17^k).** `(a,d,f=Fg)` is a (Q)-datum of level `F=17^k` iff
`(a,b,c,d) = (a, (f+1)/(4ad), (a+b)/g, d)` is an N-point of `Σ^I_F` with `e=g` prime to 17. The box
`−4a²d (mod F)` is dilation invariant, so **#(Q)-boxes of level k ≤ #ordered solutions of
4/17^k** (and the same for Q⁻¹; ≤ twice that for √Q).
*Proof.* Put `m=(f+1)/(4ad)`. `gcd(m,g)=1` and `m(4a²d+1) ≡ a+m (mod g)` give `g | a+m`; with
`j=(a+m)/g`: `jf = F(a+m)`, i.e. `4amjd = Fa+Fm+j`, which is (2.3) for `(a,m,j,d)`, `n=F`; then
`e=(a+m)/j=g` and `f_ET = 4ajd−F = (Fa+j)/m > 0`. Conversely (2.3) gives `j(4amd−1)=F(a+m)=Fje`,
so `4amd−1 = Fe`, and `e | 4a²d+1` is (2.7). ∎

**Lemma 2.2 (U ↔ solutions of 4/17^k).** For a (U)-datum `(a,b,e)` of level `F` put `c=(a+b)/e`,
`i=(e+1)/(4ab/F)`. Then `4/F = 1/(iab) + 1/(iac) + 1/(ibc)`, and the box is
`−e = −(x/y + x/z)` for `(x,y,z) = (iab,iac,ibc)`. Hence **#(U)-boxes of level k ≤ #ordered
solutions of 4/17^k** (same for U⁻¹).
*Proof.* `e+1 = 4i·ab/F` and `a+b = ce` give `4iabc = F(a+b+c)`; divide by `F·iabc`. And
`x/y + x/z = b/c + a/c = e`. ∎

**Lemma 2.3 (P ↔ Type II points of 4/17^K, at half level).** Let `(a,d,f)` be a (P)-datum of level
`k`, `a=17^α a'`, `d=17^δ d'` (`α+δ=k`), `n=a'd'`, `f=4ni−1`, `f*=(4a²d+1)/f=4nj−1`. Then
`(i, j, a', d')` is an N-point of `Σ^II_N`, `N=17^K`, `K=k+α ∈ [k,2k]`, with `17∤a'd'`, and the box is
`−f = −f_ET (mod 17^k)`. Conversely every N-point of `Σ^II_{17^K}` with `17∤cd` and every
`0≤α≤K/2` gives a (P)-datum of level `K−α` with box `−f_ET mod 17^{K−α}`. These boxes are nested;
**the union of all (P)-boxes is the union over K≥1 and over N-points of Σ^II_{17^K} (17∤cd) of the
boxes `−f_ET (mod 17^{⌈K/2⌉})`.**
*Proof.* `(4ni−1)(4nj−1)=4aFn+1` expands to `4nij−i−j=aF=17^K a'`, i.e. `4·i·j·a'·d' = i+j+17^K a'`
— (2.15). Conversely (2.21) `4c²dN+1 = f(4bcd−1)` with `a=17^α c`, `d_P=17^{K−2α}d` gives
`f | 4a²d_P+1`, and `f+1 = 4acd ≡ 0 (mod 4cd)`. ∎

**Corollary 2.4 (no level-0 boxes; Lemma 1.2).** `F=1` would give ES solutions of `4/1` in
positive integers, impossible (`1/x+1/y+1/z ≤ 3`). For (P), `K≥1` as `k≥1`... and `k=0` forces `K=0`. ∎

**Consequence (measure).** With `f(N)` = #ordered positive solutions of `4/N=1/x+1/y+1/z` and
`f_II(N)` = #N-points of `Σ^II_N` modulo dilation,
`μ(⋃ boxes) ≤ Σ_{k≥1} 6 f(17^k) 17^{−k} + Σ_{K≥1} f_II(17^K) 17^{−⌈K/2⌉}`.
By ET Prop 1.7 (`f_I ≪ n^{3/5+o(1)}`, `f_II ≪ n^{2/5+o(1)}`) both series CONVERGE (PROVED, but
ineffective: ET's `n^{O(1/log log n)}` constants are not explicit). The (P) series is the critical
one: exponent `2/5` against measure `N^{−1/2}`.

## 3. Exact low levels (CERTIFIED by one engine; independent re-check pending)

`scripts/m17_enum.c` enumerates, using the bounds of ET Lemma 2.8 (valid for every N-point, not
only Type I/II solutions, as its proof uses only the defining equations):
* `Q k`: N-points of `Σ^I_{17^k}` with `a≤b` (`n/4<acd≤3n/4`, `f=4acd−n | 4a²d+1`), `17∤e`;
  boxes `−4a²d`, `−4b²d` (the reflection `a↔b`);
* `U k`: `4i·uvw = F(u+v+w)`, `u≤v≤w` (`4iuv ≤ 3F`), every choice of `c∈{u,v,w}`, conditions of (U);
* `P K`: N-points of `Σ^II_{17^K}` with `a≤b` (`a²d ≤ abd ≤ N/2`), `f·e = N+4a²d`, `f≡−1`,
  `e≡−N (mod 4ad)`, `17∤cd`; boxes `−f`, `−f* = −(4bcd−1)` mod `17^{⌈K/2⌉}` (reflection).
`scripts/m17_union.py` adds Q⁻¹, √Q, U⁻¹ (Lemma 1.1) and computes the union in `C_5`, `C_7`
exactly (ultrametric: two boxes are nested or disjoint, so the union measure is the sum over
maximal boxes).

Validation: every box of the brute-force run `mordell_tgen.py 100000 17 3 17` (all seven
families, all moduli `M≤10⁵`, 106 boxes) meeting `C_5∪C_7` is in the complete list; the 13 rigid
II-boxes of POINTWISE_MORDELL §5 (cell 5, level 3) are in it. (Brute force leaves 76.1% of each cell
uncovered at level ≤3; the complete enumeration 68.5%: the extra boxes have T-free part >10⁵/17³.)

Number of data (`m17_enum` stderr): Q: 2, 0, 73, 0, 245, 0, 707 (k=1..7); U: 4, 0, 68, 0, 310, 0,
826; P: 2, 0, 32, 0, 121, 0, 258 (K=1..7). Even K are empty (for Q, P: ET Prop 1.6, `f_I=f_II=0` at
odd squares — PROVED; for U: computed for k=2,4,6).

**Computation 3.1.** Covered fraction of `C_5` (identical numbers for `C_7`):

| level k | boxes meeting C_5 (by type) | maximal | covered fraction after level k |
|---|---|---|---|
| 1 | 0 | 0 | 0 |
| 2 | 4 (P, K=3) | 4 | 0.235294 |
| 3 | 32 (Q 12, Q⁻¹ 12, U 4, U⁻¹ 4, P 20) | 23 | 0.314879 |
| 4 | 50 (P, K=7) | 34 | **0.321799** (complete through level 4) |
| 5 (Q,U only) | 67 (Q 39, Q⁻¹ 39, U 25, U⁻¹ 25) | 29 | 0.322147 |
| 7 (Q,U only) | 240 | 94 | 0.322150 |

So the boxes of level ≤4 leave **67.82%** of each cell uncovered (CERTIFIED), and the measure
added per level falls by roughly a factor 17–20 per level (EVIDENCE). The points `u=5`, `u=7`
(the `x̃` of POINTWISE_MORDELL Comp. 5.1) lie in no box of level ≤4, nor in any Q/U box of
level 5 or 7.

## 4. The tail: reduction to explicit counts, and where it breaks

Write `D_Q(k)`, `D_U(k)`, `D_P(K)` for the numbers of data enumerated by `m17_enum` (Q: N-points of
`Σ^I_{17^k}` with `a≤b`, `17∤e`; U: (U)-data; P: N-points of `Σ^II_{17^K}`, `a≤b`, `17∤cd`). By
Lemma 1.1 and §2 the boxes of level k number at most `B_k = 8D_Q(k) + 2D_U(k) + 2D_P(2k−1) + 2D_P(2k)`
(Q: two orientations × {Q, Q⁻¹, √Q, √Q}; P: two orientations), and `D_P(2k) = 0` (ET Prop 1.6).

**Theorem 4.1 (measure criterion; PROVED).** If
`Σ_{k≥5} 17^{1−k}·B_k < 0.678201` (the uncovered fraction of `C_5` after level 4, Comp. 3.1),
then `C_5` contains a sterile point `u`: `x(u)` lies in no class of any of the seven ET families.
The same holds for `C_7`.
*Proof.* Boxes of level ≥5 have total measure `≤ Σ_{k≥5} B_k 17^{−k}`, which is less than the measure
`0.678201/17` of the part of `C_5` missed by levels ≤4. ∎

**Corollary 4.2 (what sterility gives; PROVED from a sterile point).** If `u∈C_5` is sterile, then
no finite set of ET Prop 1.9 classes (equivalently, by ET Prop 1.9, no finite set of the polynomial
ES identities of these seven families) covers all sufficiently large primes `p` with `(p/17)=−1`
and `(p/q)=+1` for every prime `5≤q<17` (Mordell-hard primes with `n_p=17`): the finite union misses
a ball `x ≡ x(u) (mod 17^L·Q)`, `Q` the product of the other moduli' primes to high powers, which
contains infinitely many primes (Dirichlet), all with `x_17 ≡ 5`, i.e. `(p/17)=−1`, and squares at
every other prime ≤ 13 (as `x_q=1`).

**Status of the hypothesis of Theorem 4.1.**
* *Ineffective convergence (PROVED).* By §2 and ET Prop 1.7, `D_Q, D_U ≪ 17^{(3/5+o(1))k}` and
  `D_P(K) ≪ 17^{(2/5+o(1))K}`, so `Σ_k 17^{−k}B_k < ∞`; the tail beyond level `k₀` tends to 0.
  The ET constants (`n^{O(1/log log n)}` from the divisor bound) are not explicit, so this does
  not give a `k₀` that the computation reaches.
* *The critical family is (P)* (= I1, I3 with `17|cd`, II3 with `17|ad`, i.e. the 17 sits in the
  quadratic-form modulus `4ad`). Its boxes have half level `⌈K/2⌉` relative to the ES level `K`,
  so the measure weight is `N^{−1/2}` against ET's `f_II(N) ≪ N^{2/5+o(1)}`: margin only `1/10`.
  Even granting `D_P(K) ≤ 17^{2K/5}` with constant 1, `Σ_{K≥11 odd} 2·17^{2K/5}·17^{1−(K+1)/2} ≈ 0.84`
  exceeds 0.678; one would need exact enumeration through K=11 *and* an explicit ET-quality bound.
  Q and U have margin `2/5` (exponent 3/5 against `N^{−1}`) and are harmless given any explicit
  bound `D ≤ C·N^{0.9}` with moderate C.
* *Why elementary effective bounds fail.* Counting `D_P(K)` amounts to counting `(a,b)` with
  `r=(−17^K mod 4ab) | a+b` (ET Prop 2.7, second form; `d` is then unique since
  `0 < 4abd−N ≤ a+b`), or divisors of `4c²dN+1` in the class `−1 mod 4cd`. Lenstra's bound
  (≤11 divisors in a class mod `s ≥ m^{1/3}`) applies only when `16cd² ≳ N`, and the number of
  pairs is `≍ N log N`; pointwise divisor bounds are `m^{0.2+}` at the relevant sizes. Any route
  needs a genuinely new explicit count of ES solutions at prime powers.
* *Empirics (EVIDENCE).* `D_P = 2, 32, 121, 258` (K=1,3,5,7), `D_Q = 2,73,245,707`, `D_U = 4,68,310,826`
  (k=1,3,5,7): polylogarithmic-looking growth, far below what Theorem 4.1 needs (it suffices, e.g.,
  that `D_Q+D_U ≤ 17^{k/2}` for `k≥9` and `D_P(K) ≤ 17^{K/4}` for `K≥9`: then the tail is `< 0.03`).

**Assessment.** A sterile point in `C_5` is extremely likely (≥ 67.8% of the cell survives all
boxes of level ≤ 4 and the measure added per level decays geometrically in the data), but a
proof needs an explicit bound on the number of ES solutions of `4/17^K` of exactly the strength
that is open in general. Theorem 4.1 is the precise reduction.
