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
